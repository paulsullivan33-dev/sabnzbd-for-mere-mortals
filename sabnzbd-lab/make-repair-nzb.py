#!/usr/bin/env python3
"""Second lab fixture: a download that NEEDS repair.

Reuses payload.bin from make-test-nzb.py. Builds a PAR2 set for it
(block size = one segment, 30,000 bytes; two recovery blocks —
postings carry spare blocks because a missing segment's cost is
not always exactly one block), then
writes an NZB whose fourth segment points at a message ID the fake
server does not have (it answers 430). The PAR2 files are included
in the NZB as files of their own. A correct downloader must fetch
the PAR2 data, verify, repair the missing 30,000 bytes and finish
with a byte-identical file.

Usage: make-repair-nzb.py <workdir> <par2-binary>
Outputs in <workdir>: repair-segments.json, labtest-repair.nzb
"""
import binascii
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

WORK = sys.argv[1]
PAR2 = sys.argv[2]
SEG_SIZE = 30_000
ESCAPES = {0x00, 0x0A, 0x0D, 0x3D}


def yenc_encode(data: bytes) -> str:
    out, col = [], 0
    for byte in data:
        c = (byte + 42) % 256
        if c in ESCAPES:
            out.append("=" + chr((c + 64) % 256))
            col += 2
        else:
            out.append(chr(c))
            col += 1
        if col >= 128:
            out.append("\r\n")
            col = 0
    return "".join(out)


def encode_file(path, name, idprefix, segments):
    """yEnc-encode a whole file into segments; return NZB <file> data."""
    data = open(path, "rb").read()
    parts = [data[i:i + SEG_SIZE] for i in range(0, len(data), SEG_SIZE)] or [b""]
    elems = []
    for idx, part in enumerate(parts, start=1):
        msgid = f"{idprefix}-part{idx}@example.invalid"
        begin = (idx - 1) * SEG_SIZE + 1
        end = begin + len(part) - 1
        crc = format(binascii.crc32(part) & 0xFFFFFFFF, "08x")
        body = (f"=ybegin part={idx} total={len(parts)} line=128 "
                f"size={len(data)} name={name}\r\n"
                f"=ypart begin={begin} end={end}\r\n"
                + yenc_encode(part)
                + f"\r\n=yend size={len(part)} part={idx} pcrc32={crc}\r\n")
        segments[msgid] = body
        elems.append((idx, len(body.encode("latin-1")), msgid))
    return name, elems


payload_path = os.path.join(WORK, "payload.bin")
subprocess.run([PAR2, "c", "-s30000", "-r50", "-n1", "payload.bin"],
               cwd=WORK, check=True, capture_output=True)

segments = {}
files = []

# The payload, with segment 4 deliberately pointing nowhere.
payload = open(payload_path, "rb").read()
elems = []
for idx in range(1, 5):
    if idx == 4:
        elems.append((4, 30720, "labtest-missing-segment@example.invalid"))
    else:
        elems.append((idx, 30720, f"labtest-5.1.3-part{idx}@example.invalid"))
files.append(("payload.bin", elems))

for extra in sorted(f for f in os.listdir(WORK)
                    if f.startswith("payload.bin") and f.endswith(".par2")):
    files.append(encode_file(os.path.join(WORK, extra), extra,
                             "labtest-" + extra.replace(".", "-"), segments))

with open(os.path.join(WORK, "repair-segments.json"), "w") as fh:
    json.dump(segments, fh)

nzb = ET.Element("nzb", xmlns="http://www.newzbin.com/DTD/2003/nzb")
head = ET.SubElement(nzb, "head")
ET.SubElement(head, "meta", type="title").text = "labtest-repair"
for name, elems in files:
    f = ET.SubElement(nzb, "file", poster="lab@example.invalid",
                      date="1767225600", subject=f"labtest-repair {name}")
    groups = ET.SubElement(f, "groups")
    ET.SubElement(groups, "group").text = "alt.binaries.test"
    segs = ET.SubElement(f, "segments")
    for number, nbytes, msgid in elems:
        s = ET.SubElement(segs, "segment", bytes=str(nbytes), number=str(number))
        s.text = msgid
ET.ElementTree(nzb).write(os.path.join(WORK, "labtest-repair.nzb"),
                          xml_declaration=True, encoding="utf-8")
print("repair fixture ready:", [n for n, _ in files])

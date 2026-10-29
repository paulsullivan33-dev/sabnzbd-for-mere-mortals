#!/usr/bin/env python3
"""Generate the lab's test download: a plain-text file, yEnc-encoded
into segments, plus the NZB that maps them.

Writes, into the directory given as argv[1]:
  payload.bin        the original file (120,000 bytes of pangrams)
  segments.json      {message_id: yEnc body text} for the fake server
  labtest.nzb        the NZB pointing at those message IDs

The content is stock sentences only - no personal data anywhere.
"""
import binascii
import hashlib
import json
import os
import sys
import xml.etree.ElementTree as ET

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

LINE = (b"The quick brown fox jumps over the lazy dog. "
        b"Pack my box with five dozen liquor jugs. "
        b"How vexingly quick daft zebras jump!\n")
payload = (LINE * (120_000 // len(LINE) + 1))[:120_000]
with open(os.path.join(OUT, "payload.bin"), "wb") as fh:
    fh.write(payload)

SEG_SIZE = 30_000
ESCAPES = {0x00, 0x0A, 0x0D, 0x3D}  # NUL, LF, CR, '='


def yenc_encode(data: bytes) -> str:
    out = []
    col = 0
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


segments = {}
seg_elems = []
parts = [payload[i:i + SEG_SIZE] for i in range(0, len(payload), SEG_SIZE)]
for idx, part in enumerate(parts, start=1):
    msgid = f"labtest-5.1.3-part{idx}@example.invalid"
    begin = (idx - 1) * SEG_SIZE + 1
    end = begin + len(part) - 1
    crc = format(binascii.crc32(part) & 0xFFFFFFFF, "08x")
    body = (f"=ybegin part={idx} total={len(parts)} line=128 "
            f"size={len(payload)} name=payload.bin\r\n"
            f"=ypart begin={begin} end={end}\r\n"
            + yenc_encode(part)
            + f"\r\n=yend size={len(part)} part={idx} pcrc32={crc}\r\n")
    segments[msgid] = body
    seg_elems.append((idx, len(body.encode("latin-1")), msgid))

with open(os.path.join(OUT, "segments.json"), "w") as fh:
    json.dump(segments, fh)

nzb = ET.Element("nzb", xmlns="http://www.newzbin.com/DTD/2003/nzb")
head = ET.SubElement(nzb, "head")
ET.SubElement(head, "meta", type="title").text = "labtest-payload"
f = ET.SubElement(nzb, "file", poster="lab@example.invalid",
                  date="1767225600", subject="labtest payload.bin")
groups = ET.SubElement(f, "groups")
ET.SubElement(groups, "group").text = "alt.binaries.test"
segs = ET.SubElement(f, "segments")
for number, nbytes, msgid in seg_elems:
    s = ET.SubElement(segs, "segment", bytes=str(nbytes), number=str(number))
    s.text = msgid
ET.ElementTree(nzb).write(os.path.join(OUT, "labtest.nzb"),
                          xml_declaration=True, encoding="utf-8")

print("payload sha256:", hashlib.sha256(payload).hexdigest())
print("segments:", len(parts), "nzb bytes:",
      os.path.getsize(os.path.join(OUT, "labtest.nzb")))

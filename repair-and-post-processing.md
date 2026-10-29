# Repair and Post-Processing

By the end of this chapter you have seen
a download survive a missing piece —
fetched, found short, repaired exactly,
and finished byte-identical — and you
know what each post-processing level
promises, including the honest way a
repair fails when the arithmetic is
against it.

## The stages after the fetch

**Post-processing** is everything that
happens after the last article lands.
History's stage report names them in
order, and the lab's jobs show all of
them: **Download** (with the count of
missing or malformed articles, if any),
**Servers** (how many bytes each server
supplied), **Repair** (verify, and
repair if needed), **Unpack**, the
deobfuscation rename, and cleanup —
deleting the articles' remains and the
archive volumes, so the complete folder
holds files, not scaffolding.

How much of that runs is the job's
**post-processing level**, set per
category or per job:

- **Download only** — fetch and stop.
  The pieces stay as they fell.
- **+ Repair** — verify against PAR2,
  and repair what can be repaired.
- **+ Unpack** — also extract the
  archives into real files.
- **+ Delete** — also remove the pieces
  afterwards. The lab's `documents`
  category ran at this full level.

## The repair, run for real

Chapter 2 described PAR2 arithmetic.
The lab made it concrete. It built a
second test NZB for the same 120,000-byte
file, this time with the PAR2 files
included as files of their own — and
with the fourth segment's message ID
pointing at an article **the server does
not have**. The server answered the
request with Usenet's honest refusal,
`430 no such article found`, and the
download finished its fetch 30,000 bytes
short. The stage report tells the rest:

```text
Download -> 1 articles were missing
Repair   -> Verified in 0 seconds, repair is required;
            Repaired in 0 seconds
```

and the completed file's checksum
matched the original exactly. The
missing 30,000 bytes were *rebuilt* —
not refetched, not approximated —
recomputed from the PAR2 recovery blocks
the posting carried. That is the safety
net working as designed, and it is why
the PAR2 files in a posting are not
clutter.

## The same repair, failing honestly

The lab's first attempt at that fixture
carried exactly **one** recovery block
for the missing segment — and failed:

```text
Repair failed, not enough repair blocks (1 short)
```

One missing 30,000-byte segment cost
more than one 30,000-byte block of
repair — a segment's true cost is not
always its neat share — so the fixture
was regenerated with two recovery blocks,
and the rerun above is the result. This
is the general rule, worth memorising
in place of the arithmetic: **repair
succeeds when surviving recovery blocks
cover the blocks that are missing or
damaged, and fails — plainly, in the
history, with the shortfall named —
when they do not.** No downloader can
do better; the data either exists or it
doesn't. Real postings carry generous
PAR2 sets for exactly this reason, and a
job that fails this way is answered by
a backup server (chapter 2) or a fresher
posting, not by retrying the same one.

## Unpack, passwords and scripts

Unpacking is done by the external tools
of chapter 3 — chiefly **unrar** — and
handles the split RAR sets big postings
use, joining the volumes as it goes. An
archive can be **password-protected**;
the password travels with the job (the
interface asks; the API takes
`password=`), or can be kept in
SABnzbd's password file for archives
that reuse one. A job whose unpack
fails keeps its pieces in the incomplete
folder rather than deleting evidence —
the stage report says which stage
stopped, and chapter 13 works from
there. Finally, a category can name a
**user script** to run on the finished
files — the hook everything from a
notification to a media-library refresh
hangs off. The lab ran no scripts; the
hook is described from the documentation
and flagged as such in `criteria.md`.

## Check yourself

Your own history is the check: open any
completed job and read its stage report
top to bottom. Every stage that ran is
named, with its result. If a job's story
ever puzzles you, that report — not the
queue, not the folder — is the first
place the answer is written down.

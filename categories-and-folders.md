# Categories and Folders

By the end of this chapter a label you
stick on a job decides where its files
land, how they are post-processed and
what priority they carry — and you have
watched a job file itself into its
category's folder with no hand on it.

## The two folders everything uses

Chapter 4 mentioned the defaults:
beside the config file, SABnzbd keeps

- `Downloads/incomplete` — the workshop.
  Articles are assembled here, verified
  here, repaired here. Nothing in it is
  finished, and it belongs on your
  fastest disk if you have a choice.
- `Downloads/complete` — the shelf.
  Only finished, unpacked, cleaned-up
  downloads land here.

Both are settings (Config → Folders),
absolute paths welcome, and moving them
is the first thing most people do —
onto the big drive, off the system disk.
The queue's status line quietly reports
free space for both, which is how you
will learn one has filled up.

## A category is a bundle of answers

Left alone, every job makes the same
choices: complete folder root, default
post-processing, arrival priority. A
**category** is a named bundle of
different answers:

- **Folder** — a subfolder of the
  complete folder (or an absolute path)
  where this category's jobs land.
- **Post-processing** — how far to take
  a finished fetch: just download, or
  also repair, unpack, and delete the
  pieces afterwards (chapter 8).
- **Priority** — a standing claim on the
  queue, for jobs that should always
  jump or always wait.
- **Script** — a program to run on the
  result (chapter 8 again).

SABnzbd ships with four ready-made —
`movies`, `tv`, `audio`, `software` —
plus the `*` default that catches
everything else. Out of the box they
are empty vessels: no folders, inherit
everything, waiting for you to give
them meaning in Config → Categories.

## The lab's category, made and used

The lab made one through the API (the
Config → Categories page writes the
same settings):

```bash
curl -s "http://127.0.0.1:8080/api?mode=set_config&section=categories&keyword=documents&name=documents&dir=documents&pp=3&apikey=YOUR-API-KEY"
```

— a category `documents`, folder
`documents`, post-processing `3` (the
full course: repair, unpack, delete the
pieces). Reading the categories back
showed it sitting alongside the built-ins,
each at priority `-100`, inherit. Then
the proof: the lab added its test NZB
again with `cat=documents`, and the job
filed itself —

```text
history: labtest-second | cat: documents | Completed
path: Downloads/complete/documents/labtest-second/
```

— under `complete/documents/`, not the
complete root where its uncategorised
twin landed. No dragging, no sorting
after the fact. Multiply that by every
download you ever make and the point of
categories makes itself: they are how a
download folder stays organised when
you are not watching it.

## Where categories come from

You will rarely pick a category by hand
for long. The inputs of chapter 7 —
RSS feeds, the watched folder's
subfolders, other programs calling the
API — can each stamp a category on what
they deliver, so the sorting decision is
made once, at the source, and the bundle
does the rest. A category with no folder
set is still useful: it can carry just a
priority, or just a script. And a job
whose category you disagree with can be
re-categorised while it waits in the
queue; the bundle applies when
post-processing runs, not when the NZB
arrived.

## Check yourself

Make a category with a folder of its
own, send your test NZB in under it,
and find the finished file in
`complete/<your-folder>/` while the
history line names the category. If the
file lands in the complete root instead,
the job never carried the category —
check the `cat=` on the way in, not the
folder settings on the way out.

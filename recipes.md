# Recipes

Short, complete jobs that combine the
chapters. Each assumes SABnzbd is
installed (chapter 3), configured
(chapter 4) and reachable at
`127.0.0.1:8080` with your API key in
hand. The examples use the lab's kind of
material — freely available files and
test NZBs — because recipes are about
the moves, not the cargo.

## 1. Fetch a large free file by NZB

You have an NZB for something large and
freely distributed — an operating-system
image posted to Usenet by its own
project, say. Add it at high priority
with a name you will recognise:

```bash
curl -F "name=@big-free-image.nzb" \
  "http://127.0.0.1:8080/api?mode=addfile&priority=1&nzbname=big-free-image&apikey=YOUR-API-KEY"
```

Watch it in the interface or poll
`mode=queue` for its percentage and time
left. When it leaves the queue, read its
stage report in history before you trust
the file: **Completed**, a Repair line
that says verified (or repaired), and a
checksum you can compare against the
publisher's, if they publish one —
`sha256sum` on the finished file is the
last word, as it was in the lab.

## 2. A category that files itself

From chapter 6, generalised: decide the
three answers once — folder,
post-processing, priority — and make a
category per kind of thing you fetch
(`documents`, `images`, `audio-files`,
whatever your shelf looks like). Stamp
it at every door: `cat=` on API adds,
the category subfolder in the watched
folder, the category field on each RSS
feed. The recipe is the habit: nothing
arrives uncategorised, so the complete
folder never needs a sort-out day.

## 3. A watched folder a laptop can feed

Make the watched folder a synced or
shared folder — the folder your file
sync tool already mirrors between
machines. Now saving an NZB on the
laptop queues it on the server at home,
in the category of the subfolder you
saved it into, and the finished file is
waiting in the complete folder when you
get back. The lab verified the scan and
the queueing live (chapter 7); the sync
tool in the middle is whichever you
already trust.

## 4. Pause for the video call

The queue is eating the connection and
the house wants it back for an hour:

```bash
curl -s "http://127.0.0.1:8080/api?mode=pause&apikey=YOUR-API-KEY"
```

and later `mode=resume`. For the
standing version of the same idea, use
a **speed limit** instead (Config →
General → maximum bandwidth) during the
hours the connection is shared, and let
the scheduler (Config → Scheduling)
raise it again overnight. The lab's
pause held a queued job perfectly
still; a limit would have let it crawl
instead — choose per occasion.

## 5. Read the whole state in one call

For a script, a dashboard, or a
morning check:

```bash
curl -s "http://127.0.0.1:8080/api?mode=fullstatus&output=json&apikey=YOUR-API-KEY"
```

returns the service's whole account of
itself — version, folders, disk space,
servers, queue summary — in one JSON
document. If you ever automate around
SABnzbd, this and `mode=history` are
the two calls that tell you whether the
night went well.

## 6. When a job fails for missing articles

History says **Failed** and the stage
report counts missing articles and a
repair that came up short. In order:
check the posting's age against your
server's retention (chapter 2); add a
backup server if you have one and use
the history entry's **Retry**; or fetch
a fresher posting of the same file.
What not to do is retry the identical
NZB against the identical server and
expect arithmetic to change its mind —
the lab's one-block-short repair failed
identically until the fixture itself
gained a block.

# Feeding SABnzbd — RSS, Watched Folders and the API

By the end of this chapter NZBs reach
SABnzbd without you handing them over:
dropped in a folder it watches, matched
from an RSS feed it polls, or posted by
another program through the API. These
three doors are the difference between a
downloader you operate and one that
operates itself.

## Door one: the watched folder

Point SABnzbd at a folder (Config →
Folders → **Watched Folder**) and every
`.nzb` file that appears in it becomes a
job, on a scan that runs every few
seconds. The lab set it through the API
(the setting's name in the config is
`dirscan_dir`), copied its test NZB in
as `labtest-watched.nzb`, and waited:
within twelve seconds the queue showed
`labtest-watched | Downloading`, and the
job completed like any other. The NZB
file itself is consumed in the process —
the folder is an in-tray, not an archive.

Two refinements worth knowing: a
**subfolder** of the watched folder
named after a category stamps that
category on what it delivers (chapter 6's
bundles, applied at the door), and a
file named `name [cat].nzb` can carry
its category in the filename. A folder
other programs can write to — a synced
folder, a shared drive — turns this door
into the simplest integration there is:
anything that can save a file can feed
SABnzbd.

## Door two: RSS feeds

An **RSS feed** is a list a site
publishes and updates — new postings, as
they appear. Config → RSS lets SABnzbd
poll feeds on a schedule (hourly by
default; the lab's log showed the task
being scheduled every 60 minutes) and
download what matches your **filters**:
for each feed, lines that accept or
reject titles by words and patterns, a
category to stamp on matches, and a
priority.

The lab built a feed of its own — one
item, linking its test NZB, served from
a local web server — and registered it
through the API:

```bash
curl -s "http://127.0.0.1:8080/api?mode=set_config&section=rss&keyword=labfeed&uri=http://127.0.0.1:8099/feed.xml&cat=documents&enable=1&apikey=YOUR-API-KEY"
```

Reading the section back showed the feed
in place, with SABnzbd's default filter
row already attached: accept `*` —
everything — which is the right shape
for a one-item lab feed and exactly the
wrong shape for a busy real one. Filters
are the whole craft of this door: start
from reject-everything, accept the
patterns you mean, and let the feed run
a day before trusting it. Two honest
limits from the lab: the API has **no
force-fetch** (asking returned
`"not implemented"` — fetching belongs
to the schedule, and to the Fetch button
on the RSS config page), so the lab
verified a feed's creation, storage and
readback live, and its polling cycle
from the documentation and the scheduler
log rather than by waiting the hour out.

## Door three: the API, for programs

Everything the earlier chapters did with
`curl` is this door. `mode=addfile`
uploads an NZB; `mode=addurl` hands over
the URL of one; both accept `cat=`,
`priority=`, `nzbname=` and a password
for protected archives. A second, weaker
credential exists for exactly this job:
the **NZB key** (Config → General) may
*only* add NZBs — safe to give to a
feeder program you would not trust with
the full API key, which can also read
your config and shut the service down.

This is the door the neighbours of
chapter 11 stand at: catalogue sites and
automation tools that watch for postings
and post matching NZBs to SABnzbd as
they appear. The receiving end — this
chapter — is mechanics, and mechanics
are neutral: the lab's feeder was a
text file and a `curl` command. What a
feeder goes looking for is, per
chapter 1, the responsibility of whoever
points it.

## Check yourself

Set a watched folder, drop in a test
NZB, and watch it queue itself. Then
read the folder setting back through
`mode=get_config&section=misc` and find
`dirscan_dir` naming your folder — the
door, the setting and the result all
agreeing is what "configured" means.

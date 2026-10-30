# SABnzbd for Mere Mortals

A big file on Usenet is not a file. It
is thousands of small text articles,
scattered across a news server, waiting
for something to gather them in order,
decode them, check them for damage,
repair what can be repaired, and unpack
the result. **SABnzbd is that something**:
a downloader that runs quietly as a
background service, takes its orders
from a small map file called an NZB, and
does the whole pipeline — fetch, decode,
verify, repair, unpack — while you watch
from a web page on your own machine.

This guide explains how the pipeline
fits together, how to install SABnzbd
and point it at a news server through
its first-run wizard, and how to run
its queue: priorities, categories that
file downloads for you, the three doors
NZBs arrive by (a watched folder, RSS
feeds, and an API other programs can
call), and the repair machinery that
lets a download survive missing pieces.
It teaches the mechanics with neutral
material throughout, and it draws its
line early and plainly: SABnzbd fetches
what it is pointed at, so download only
what you have the right to download.

The lab behind this guide ran the real
thing: **SABnzbd 5.1.3**, the official
source release, on this machine's
loopback — with a news server the lab
built itself for the occasion, a few
dozen lines of Python answering NNTP on
a local port. Against it the lab
completed the first-run wizard over
HTTP, read the resulting configuration
back through the API, and downloaded a
test file of stock sentences — 120,000
bytes in four yEnc segments — verifying
the finished file byte for byte against
the original. It paused the queue and
watched a job wait; it filed a download
into a category's folder; it fed SABnzbd
from a watched folder and registered an
RSS feed; it killed the server
mid-download and read the genuine
connection errors; and it broke a
download on purpose — a whole segment
missing — and watched PAR2 repair rebuild
the file exactly, after first watching
the same repair fail for want of one
more recovery block.

What the lab could not do, it did not
fake. It had no account with a real
Usenet provider, so the one thing it
never did is fetch a real article from
a real server: everything up to that
boundary — the protocol conversation,
the authentication, the article requests,
the errors a dead server earns — is real
and transcribed, and `criteria.md` says
exactly where the line sits. Everything
in the lab was throwaway: a fake server,
an invented username and password, a
test file of pangrams. The transcripts
are in `sabnzbd-lab/`, fake credentials
and all, labelled for what they are.

## What this guide covers

- [**What SABnzbd is**](what-sabnzbd-is.md) —
  the mental model: an NZB map, a queue,
  a pipeline, a web page — and the
  ethics line, drawn early
- [**The moving parts**](the-moving-parts.md) —
  servers, articles, decoding, PAR2
  repair and unpacking, stage by stage
- [**Installing SABnzbd**](installing-sabnzbd.md) —
  the source route the lab ran, and the
  par2 and unrar lesson it learned first
- [**First run — the wizard and your server**](first-run.md) —
  two screens of setup, the config file
  they write, and reading it back by API
- [**The queue and priorities**](the-queue-and-priorities.md) —
  adding a job, queue versus history,
  the pause that holds everything, and
  who goes first
- [**Categories and folders**](categories-and-folders.md) —
  the incomplete and complete folders,
  and a label that files downloads for you
- [**Feeding SABnzbd**](feeding-sabnzbd.md) —
  the watched folder, RSS feeds and
  filters, and the API door for programs
- [**Repair and post-processing**](repair-and-post-processing.md) —
  the stages after the fetch, a repair
  run for real, and one that failed
  honestly one block short
- [**Recipes**](recipes.md) — a big free
  file by NZB, a self-filing category, a
  watched folder across machines, the
  pause for the video call
- [**The neighbours**](the-neighbours.md) —
  the Usenet guide as concepts companion,
  NZBGet, newsreaders, feeders, and plain
  fetchers: who does which job
- [**Limits**](limits.md) — the
  arithmetic it cannot beat, the finding
  it does not do, and the trust it places
  in its inputs
- [**Troubleshooting**](troubleshooting.md) —
  the missing-module stall, connection
  refused, the repair that came up
  short, and the file that was renamed
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Finding content. SABnzbd does not search
Usenet and this guide does not teach
anyone to hunt for downloads: it teaches
the downloader's mechanics, with a test
file and freely available material as
the standing examples. Reading and
posting in discussion groups is a
newsreader's job, covered by the
[Usenet guide](https://paulsullivan33-dev.github.io/usenet-for-mere-mortals/)
in this series. Running SABnzbd as
a public internet service is out of
scope and out of character — it is a
tool for your own network, and the
guide's defaults keep it there.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before installing anything —
once the pipeline stages are named,
every later surprise is one stage
misbehaving, and the stage report in
history tells you which. Chapters 3 and
4 get you a running, configured service
in one sitting; chapter 5 makes the
first download with training wheels on.
The lab's transcripts live in
`sabnzbd-lab/transcripts/`, its two
fixture scripts in `sabnzbd-lab/` —
everything the verification notes in
`criteria.md` claim can be re-run from
those files and a loopback port.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Usenet for Mere Mortals](https://paulsullivan33-dev.github.io/usenet-for-mere-mortals/)
- [aria2 for Mere Mortals](https://paulsullivan33-dev.github.io/aria2-for-mere-mortals/)
- [APIs for Mere Mortals](https://paulsullivan33-dev.github.io/api-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/sabnzbd-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/sabnzbd-for-mere-mortals/blob/main/LICENSE-CODE).

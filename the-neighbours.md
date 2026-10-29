# The Neighbours

SABnzbd sits in a small neighbourhood of
tools that all speak some of the same
words — Usenet, NZB, queue — while doing
different jobs. This chapter draws the
map, so you can tell which tool a piece
of advice you find online is actually
about.

## Usenet itself: the layer underneath

Everything in this guide assumes the
ideas underneath it: what a newsgroup
is, how articles flood from server to
server, why binary postings are chopped
into segments, what retention means.
That layer — the system itself,
including the discussion groups
SABnzbd ignores — is bigger than this
guide; the glossary covers the pieces
SABnzbd touches, and your news
provider's own documentation covers
the rest. This guide stays with the
*how*; the *why* lives there.

## NZBGet: the other downloader

The neighbour you will meet most often
in forum advice is **NZBGet**, the other
long-lived Usenet downloader. The jobs
are the same — NZB in, verified files
out — and the pipeline stages match
chapter 2's almost part for part. The
differences are of build and taste:
NZBGet is written in C++ and is famously
light on small hardware; SABnzbd is
written in Python, runs anywhere Python
does, and leans into its web interface
and API. Advice for one rarely copies
verbatim to the other — config names,
API calls and folder defaults all differ
— which is why "my downloader won't…"
is always the start of a conversation,
not the end of one.

## Newsreaders: the reading side

A **newsreader** (Pan, Thunderbird,
slrn and their kin) is for the
discussion half of Usenet: subscribing
to groups, reading threads, replying.
Some can also fetch binaries, slowly and
by hand. If your interest in Usenet is
conversation, that is your tool, and
SABnzbd will seem to be missing its
point on purpose — because it is. The
two share a server account happily: the
reader takes a connection or two, the
downloader takes the rest.

## The feeders: where NZBs come from

Chapter 7 met the inputs SABnzbd accepts
— watched folder, RSS feeds, other
programs calling its API. The programs
built to stand in that spot are
**indexers** (sites that catalogue what
has been posted and hand out NZBs) and
**automation tools** that watch feeds
and forward matches. This guide teaches
the receiving end: the API calls, the
RSS filters, the category hand-off. What
you point those feeders at is, per
chapter 1's line, your responsibility —
the mechanics are content-neutral, and
a public test feed works exactly like
any other.

## Plain fetchers: aria2 and friends

For ordinary web downloads — a file at
an `https://` address — the right tool
is a plain fetcher, and this series'
aria2 guide covers a good one.
SABnzbd cannot do that job at all: give
it a URL and it expects the URL of an
*NZB*, not of the file itself. The two
tools divide the world by protocol, not
by size or importance, and many a
download folder hosts both without
either minding.

## Check yourself

Ask which of these you actually need by
answering one question: *where does the
thing I want live?* On a web server —
a fetcher. In a discussion group, to
read — a newsreader. Posted to Usenet
as binaries, with an NZB in hand —
you are in the right guide.

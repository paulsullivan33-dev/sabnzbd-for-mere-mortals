# Glossary

**API** — The surface other programs use
to give SABnzbd orders and read its
state: add this, pause, how is the queue.
Guarded by an API key.

**API key** — The secret token the API
checks. SABnzbd generates one (and a
second, weaker **NZB key** that may only
add NZBs). Found under Config →
General.

**Article** — One Usenet message. A file
posted to a binary group travels as many
articles, each holding one segment.

**Backup server** — A second configured
news server, asked only when the primary
lacks an article. Cheap block accounts
are commonly used this way.

**Category** — A label on a job that
selects its complete folder, priority
and post-processing in one move.

**Complete folder** — Where finished,
unpacked downloads land. Per-category
subfolders grow under it.

**Connections** — The simultaneous
sessions a server account allows.
SABnzbd opens up to that many at once;
more than the account allows is refused
by the server, not by SABnzbd.

**Daemon** — A program that runs in the
background, waiting for work, with no
window of its own. SABnzbd is one; its
face is a web page.

**Decode** — Turning an article's encoded
text back into the original bytes.
yEnc is the encoding almost everything
uses.

**History** — SABnzbd's record of
finished jobs: what completed, what
failed, and the post-processing report
for each.

**Incomplete folder** — The scratch
folder where articles are assembled and
verified before anything is unpacked.
Fast disk here matters; nothing in it is
a finished file.

**Indexer** — A site that catalogues
Usenet postings and hands out NZBs. A
neighbour, not a part of SABnzbd.

**Message ID** — The unique name of an
article, the address an NZB lists and a
server answers to.

**Newsgroup** — One of Usenet's topic
channels. Postings a job fetches come
from a group, though the NZB spares you
naming it.

**NNTP** — The protocol clients and news
servers speak: asking for articles by
message ID. SABnzbd's fetching is NNTP.

**NZB** — The small XML map of a
download: which message IDs, in which
order, make which files. Not the content
itself.

**PAR2** — Repair data posted alongside
big files. It can detect damage and,
given enough surviving blocks, rebuild
missing pieces exactly.

**Post-processing** — Everything after
the fetch: verify, repair, unpack,
clean up, and any user script. Set per
category.

**Priority** — A job's claim on the
queue: Force, High, Normal, Low, or
paused. Higher claims download first.

**Queue** — The ordered list of jobs
waiting or downloading, with their
speeds and times to finish.

**RAR** — The archive format most big
postings are packed in, split into
numbered volumes that unpack together.

**Repair blocks** — The units PAR2
arithmetic counts: damage is measured in
blocks missing, repair in blocks
available, and the second must cover the
first.

**Retention** — How long a server keeps
articles before discarding them. Older
than retention means gone, however good
the NZB is.

**RSS feed** — A machine-readable list a
site publishes and SABnzbd can poll,
downloading entries that match your
filters.

**Segment** — The slice of a file inside
one article; the NZB lists them so the
file can be reassembled in order.

**Server** — In this guide, always a
*news server*: the Usenet provider whose
articles SABnzbd fetches, reached over
NNTP, usually on an encrypted connection.

**Watched folder** — A folder SABnzbd
scans for `.nzb` files; any file dropped
there becomes a job automatically.

**Wizard** — The first-run setup pages —
language, server, folders — that write
the initial `sabnzbd.ini`.

**yEnc** — The encoding that packs binary
bytes into article text with little
overhead. Decoding it is built in.

# The Moving Parts

By the end of this chapter you can take
any problem SABnzbd shows you and say
which stage of the pipeline it belongs
to. That is the chapter's whole job,
because nearly every confusing thing
SABnzbd does becomes obvious once you
know which part did it.

A download passes through the same
stages every time:

```text
NZB ──► queue ──► fetch ──► decode ──► verify ──► repair ──► unpack ──► done
 (map)   (order)  (articles) (bytes)   (check)    (fix)     (files)   (history)
```

## The NZB: a map, not the territory

An **NZB** is a small XML file. It does
not contain the download. It contains a
list of **message IDs** — the unique
names Usenet gives every article — plus,
for each file in the posting, which
segments (articles) hold which byte
ranges. Think of it as a parts list for
flat-pack furniture: no wood, just the
inventory. SABnzbd reads the map, works
out how many articles it needs and how
big the finished thing should be, and
puts the job in the queue. A job in the
queue whose download later fails has
usually failed *downstream* of the map;
a job that cannot even be queued has a
broken map. Chapter 13 starts there.

## Servers: where the articles live

SABnzbd knows nothing until you tell it
a **news server**: a host name, a port,
your username and password, and how many
simultaneous **connections** your
account allows. Usenet providers sell
access measured exactly that way —
connections and speed — because fetching
is the expensive part. You can configure
several servers. SABnzbd treats one as
primary and others as **backup**: if an
article is missing on the primary (old
postings fade as servers discard them —
that fading is called **retention**), it
asks the backup before giving up. The
wizard in chapter 4 sets up the first
one.

## Fetch and decode: articles become bytes

Articles are text. Binary data travels
inside them **encoded** — historically
with **yEnc**, an encoding that packs
bytes into printable characters with
little waste. SABnzbd opens its
connections, asks for articles by
message ID, and decodes each one as it
arrives, writing the real bytes to its
**incomplete folder** on disk. This
stage is pure plumbing: network speed,
connection count and disk speed set how
fast it goes, and chapter 5's speed
readings are this stage talking.

## Verify and repair: the PAR2 safety net

Big postings travel with **PAR2** files:
extra data computed from the files
themselves, the way a checksum is
computed — except PAR2 data can do more
than detect damage. Given enough of it,
SABnzbd can *rebuild* missing or corrupt
chunks exactly, the way a RAID array
rebuilds a failed disk. After the fetch,
SABnzbd first runs a quick check (cheap:
sizes and light checks), and if anything
is short it runs a full verify: every
file checked against the PAR2 data,
damaged blocks listed, and a repair
attempted *if* enough repair blocks
survived. "Enough" is arithmetic, not
luck — chapter 8 works an example. If
repair succeeds, the download continues
as if nothing happened. If it cannot,
the job fails honestly, and history
says why.

## Unpack: archives become files

Postings are usually packed: a set of
**RAR** archives (or occasionally ZIP or
7z), split into numbered volumes, with
the real files inside. After a verified
repair, SABnzbd extracts them with the
unarchiver the operating system
provides, into the **complete folder**,
then deletes the pieces — the articles'
bytes, the archive volumes, the PAR2
files — leaving only the finished files.
A password-protected archive needs the
password supplied with the job, and
chapter 8 covers where it goes.

## The conductor: config, API, web page

Around the pipeline sits the machinery
that steers it. Everything SABnzbd knows
about itself lives in one INI-style
config file, `sabnzbd.ini`: servers,
folders, categories, switches. The web
interface is a view onto that file and
the queue; the **API** is the same
surface for programs, guarded by an
**API key** the program generates. Change
a setting in the web page and you are
editing that file by hand-held remote
control — chapter 4 reads the file back
through the API to prove the point.

## Check yourself

With SABnzbd running (chapter 4), ask it
for its own state:

```bash
curl "http://127.0.0.1:8080/api?mode=version&output=json"
```

You get the version back as JSON. That
one call touches the conductor only —
no server, no articles — and it is the
check this guide returns to whenever it
needs to prove the service is alive
before blaming the pipeline.

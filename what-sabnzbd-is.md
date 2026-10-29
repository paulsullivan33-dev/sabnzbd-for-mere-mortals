# What SABnzbd Is

**Usenet** is one of the oldest systems
on the internet: a worldwide network of
**news servers** that pass **articles**
— messages — from server to server, so
a message posted once can be read
anywhere. Most articles are text. Some
carry binary files, chopped into many
small pieces, one piece per article,
because that is how the system moves
data. Putting a file back together from
thousands of pieces, by hand, is nobody's
idea of an afternoon.

**SABnzbd is the program that does that
putting-back-together for you.** You hand
it a small file called an **NZB** — a map
that lists, by message ID, every article
a download consists of. SABnzbd talks to
your news server, fetches those articles
in parallel, decodes them, checks the
result for damage, repairs it if repair
data was posted alongside, unpacks any
archives inside, and leaves the finished
files in a folder you chose. You watch
and steer all of it from a web page it
serves on your own machine.

The name is a fossil: SAB stood for the
project it grew from, and *nzbd* is
"the NZB daemon" — a **daemon** being a
program that runs quietly in the
background, waiting to be told what to
do. That is exactly the shape of it.
There is no window and no button on your
desktop. There is a service, a web
interface, and an **API** — a way for
other programs to give it orders — which
is why so much else can plug into it.

## The ethics line, early

SABnzbd is a downloader. Like a web
browser or a postal service, it fetches
what it is pointed at and does not know
or judge what that is. That makes the
pointing your responsibility. Download
only what you have the right to
download: files their owners have made
freely available, material in the public
domain, your own postings coming back to
you, test files posted for exactly that
purpose. This guide stays on that side
of the line throughout. Its examples use
a test file this guide generates itself,
and a freely available operating-system
image used as the standing example of "a
large legitimate download". What other
people fetch with the tool is their
business and their problem; the
mechanics taught here are the same
either way, and the mechanics are what
a guide can honestly teach.

## A first taste

Once SABnzbd is installed and running
(chapters 3 and 4), its whole life is
visible at one address in your browser:

```text
http://127.0.0.1:8080/sabnzbd/
```

That page shows the **queue** — what is
downloading, in what order, how fast,
and how long is left — and the
**history** of what finished and what
happened to it. Everything chapter 5
onwards does can be done from that page,
and most of it can also be done by a
program through the API, which is the
door the automation chapters use.

## What it is not

It is not a news *reader*: it does not
show you discussion threads to read and
reply to, and it is not how you would
follow a text newsgroup — the Usenet
guide in this series covers the concepts
and the reading side. It is not a search
engine: SABnzbd does not find content;
an NZB has to arrive from somewhere —
saved from a web page, dropped in a
watched folder, delivered by an RSS
feed or another program (chapter 7). It
is not a server: it holds no articles of
its own and shares nothing back. And it
is not magic about damage: if pieces of
a posting are missing from your server
and the repair data runs out, no
downloader can invent them (chapter 8
is plain about how that ends).

## Who it is for

Anyone whose downloads genuinely come
from Usenet: the person fetching large
freely-distributed files posted there,
the archivist pulling their own old
postings back down, the hobbyist whose
other tools speak NZB. And, honestly,
the curious: SABnzbd is a tidy example
of a headless service with a web face
and a real API, and running it teaches
that pattern as well as it teaches
Usenet. This guide's lab ran it exactly
that way — on loopback, with a made-up
server and a test file — and chapter by
chapter, that is the machine you will
build here too.

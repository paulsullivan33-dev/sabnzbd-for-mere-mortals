# First Run — the Wizard and Your Server

By the end of this chapter SABnzbd knows
who your news server is, the wizard is
behind you, and the main interface
answers — proven by reading the server
back out of the config through the API,
so you know the setting *took*, not just
that a form was filled in.

## Step one: language

A fresh SABnzbd sends every visit to
`http://127.0.0.1:8080/` onward to
`/wizard/`, a page titled **SABnzbd
Quick-Start Wizard**. The first screen
asks one thing: the language of the
interface. Pick yours and continue. (The
lab picked English; nothing else in this
guide depends on the choice.)

## Step two: the server

The second screen is the one that
matters. It asks for a single news
server — the account of chapter 2:

- **Host** — the server's name, for
  example `news.example-provider.invalid`
  in this guide's examples, or
  `127.0.0.1` in the lab.
- **Port** — 563 for an encrypted
  connection, 119 for a plain one.
- **Username** and **password** — the
  account your provider gave you.
- **Connections** — how many simultaneous
  connections your account allows. Do
  not guess high: the server refuses the
  extras, and chapter 13 shows the shape
  of that refusal.
- **SSL** — the encrypted-connection
  switch. On, for any real provider:
  NNTP carries your credentials, and the
  articles travel as data. The lab's
  home-made server speaks plain text on
  loopback, so the lab switched it off —
  a loopback-only exception, not a habit.

The lab filled in its throwaway local
server — host `127.0.0.1`, port `1199`,
username `labuser`, password `labpass`
(invented for the lab and worthless
anywhere else), 4 connections, SSL off —
and the wizard answered with the whole
of step three: **"Setup is now
complete!"** Two screens is all the
wizard has. Everything else SABnzbd can
do is configured later, in the main
interface, as the need arises.

## What the wizard actually did

The wizard is a form that writes a file.
Open `sabnzbd.ini` (beside the path you
gave `--config-file`) and the server is
there under `[servers]`, in the plain
INI style chapter 2 promised — host,
port, username, connections, `ssl = 0`.
That is worth knowing the first time a
setting seems not to stick: the file is
the truth, the pages are a view of it.
Two folders were also created beside it:
`Downloads/incomplete` and
`Downloads/complete`, the pipeline's
in-tray and out-tray, which chapter 6
returns to.

## Check it took, through the API

The wizard also generated the **API
key**: a long random token in the ini
(`api_key = ...`), and shown in the main
interface under Config → General. With
it, ask SABnzbd to read its own config
back:

```bash
curl -s "http://127.0.0.1:8080/api?mode=get_config&section=servers&output=json&apikey=YOUR-API-KEY"
```

The lab's answer listed its server in
full — host `127.0.0.1`, port `1199`,
`connections: 4`, `ssl: 0`, `enable: 1` —
and, just as usefully, the queue call
(`mode=queue`) showed an empty queue, no
pause, and the free disk space of both
folders. The service is configured and
idle. It has downloaded nothing yet,
because nothing has given it an NZB —
which is the next chapter's job, and it
starts with a download small enough to
watch closely.

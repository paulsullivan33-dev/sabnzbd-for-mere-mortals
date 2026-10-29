# Installing SABnzbd

By the end of this chapter SABnzbd is
running on your machine and answering
its web page — not yet configured, just
alive, which the check at the end proves.
Everything after this chapter assumes
that much.

## What you need first

SABnzbd is a **Python** program. It needs
three things around it:

- **Python 3** (3.8 or newer) and, on
  Linux, the packages in its
  `requirements.txt` — the web framework,
  the template engine, and **sabctools**,
  the compiled helper that does the fast
  decoding and checking.
- **par2** — the repair tool of
  chapter 2, an external program
  SABnzbd calls.
- **unrar** — the unpacker for the RAR
  archives most big postings use.

The last two are not optional extras.
This guide's lab learned that the direct
way: a first launch without them started
the web interface happily, then posted
warnings — `par2 binary... NOT found!`,
`unrar binary... NOT found!` — and the
verdict `Essential modules are missing,
downloading cannot start.` SABnzbd will
serve its pages all day in that state
and download nothing. Install par2 and
unrar first (on Debian or Ubuntu:
`sudo apt install par2 unrar`), and the
same launch comes up with no warnings
at all.

## The routes in

- **Windows and macOS** have official
  installers and app bundles from the
  SABnzbd site — the ordinary route
  there, and the one to take.
- **Linux distributions** package it to
  varying freshness. The project's own
  route, and the one this guide's lab
  used, is the source release: it runs
  anywhere Python does and is always the
  current version.
- **Python's package index does not
  carry it.** `pip install sabnzbd`
  fails with "No matching distribution
  found" — the lab checked. The source
  tarball is the Python route.

## The source route, as the lab ran it

Download `SABnzbd-5.1.3-src.tar.gz` (use
the current release in place of 5.1.3)
from the project's GitHub releases page,
unpack it, and install its requirements
into a virtual environment so the rest
of your system stays untouched:

```bash
tar xzf SABnzbd-5.1.3-src.tar.gz
cd SABnzbd-5.1.3
python3 -m venv ~/sabnzbd-venv
~/sabnzbd-venv/bin/pip install -r requirements.txt
```

Then start it, telling it where its
config file should live and to stay on
this machine only:

```bash
~/sabnzbd-venv/bin/python SABnzbd.py \
  --config-file ~/sabnzbd-config/sabnzbd.ini \
  --server 127.0.0.1:8080 --browser 0
```

The options, briefly: `--config-file`
is the folder-and-file where all state
will live (chapter 2's `sabnzbd.ini`,
plus the queue, logs and default
download folders, which are created
beside it); `--server 127.0.0.1:8080`
binds the web interface to **loopback**
— this machine only — on port 8080;
`--browser 0` stops it opening a browser
window at you. Leave the terminal
running; SABnzbd is now a service in a
window, and closing the window stops it.
(For a permanent install you would hand
it to your system's service manager
instead — the shape of the command is
the same.)

## Check it is alive

From a second terminal:

```bash
curl -s "http://127.0.0.1:8080/api?mode=version&output=json"
```

The lab's answer:

```json
{"version":"5.1.3"}
```

And in a browser, `http://127.0.0.1:8080/`
answers with a redirect to `/wizard/` —
the first-run wizard, which is exactly
where chapter 4 goes next. If the
version call answers and the wizard
appears, the install is real: program,
dependencies and web server all working.
If instead you meet warnings about
missing modules, scroll up — that is
the par2 and unrar lesson, and it is
cheaper learned here than in chapter 13.

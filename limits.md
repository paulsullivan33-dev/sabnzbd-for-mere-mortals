# Limits

What SABnzbd cannot do, stated as
plainly as the rest of the guide. Most
of these are the shape of the tool, not
faults in it — but a reader who knows
the edges in advance meets fewer
surprises.

- **It cannot invent missing data.**
  Repair is arithmetic: surviving PAR2
  blocks must cover what is missing.
  The lab watched a repair fail one
  block short and succeed with two. Past
  the arithmetic there is no appeal —
  only a backup server or a better
  posting.
- **It cannot beat retention.** An
  article older than your server keeps
  is gone, however perfect the NZB. The
  map outlives the territory, often.
- **It downloads; it does not find.**
  SABnzbd has no search and no notion of
  what is posted where. NZBs arrive from
  outside — you, a folder, a feed, a
  feeder program — and choosing those
  sources is yours (chapter 1's line).
- **It is not a newsreader.** No groups
  to browse, no threads to read, no
  posting back. The discussion half of
  Usenet belongs to other tools
  (chapter 11).
- **It depends on external programs.**
  No par2 and unrar on the machine means
  no downloading at all — SABnzbd says
  so in its warnings and means it. They
  are separate projects with their own
  limits; unrar in particular handles
  RAR and leaves other formats to 7zip
  and friends.
- **It trusts its inputs.** An NZB is a
  list of orders, and SABnzbd follows
  it. A crafted NZB can ask for a great
  deal of disk and bandwidth. Feed it
  from sources you trust, and keep the
  full API key — which can reconfigure
  the service and shut it down — as
  guarded as any admin credential. The
  NZB key exists precisely so feeder
  programs need less trust.
- **Its web interface is a small
  server's interface.** It is built for
  you on your network, with a login you
  can set (Config → General). Reaching
  it from the open internet is a job for
  a VPN or a reverse proxy with its own
  authentication — chapter 3's loopback
  binding is the safe default, not a
  suggestion to publish port 8080 to
  the world.
- **One queue, in order of claim.**
  Priorities order the work; they do not
  parallelise a single job past your
  connection count, your bandwidth, or
  your disk. A fast incomplete-folder
  disk matters more to real speed than
  any setting in the program.
- **Post-processing is not inspection.**
  SABnzbd verifies that the bytes match
  the posting. It does not and cannot
  tell you the *content* is what its
  name claims, safe, or lawful. That
  judgement stays with the person who
  pointed it — which is chapter 1 again,
  and why it is chapter 1.

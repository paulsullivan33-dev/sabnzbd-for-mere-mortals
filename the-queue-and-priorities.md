# The Queue and Priorities

By the end of this chapter you have
given SABnzbd its first real job,
watched it cross the queue into history,
and held the whole queue still with the
pause button and released it again —
the three moves every later chapter
assumes you can make.

## Adding a job

A job is born when an NZB arrives. The
web interface takes one through its
**Add NZB** button (or by dropping the
file on the page); the API takes the
same file as an upload:

```bash
curl -F "name=@labtest.nzb" \
  "http://127.0.0.1:8080/api?mode=addfile&apikey=YOUR-API-KEY&output=json"
```

```json
{"status":true,"nzo_ids":["c8658419-1615-4eab-a4a9-0f92f0d0bde7"]}
```

`status: true` and a job ID: accepted.
The lab's test NZB — a 120,000-byte file
of stock sentences, in four segments on
its practice server — crossed so fast on
loopback that a queue snapshot one second
later already showed an empty queue. It
had not vanished; it had *finished*.
Which is the queue's first lesson:

## The queue is only the present tense

```bash
curl -s "http://127.0.0.1:8080/api?mode=queue&output=json&apikey=YOUR-API-KEY"
```

shows what is waiting and downloading
*now*: each slot's name, status,
percentage, speed, time left. What is
done moves to **history**
(`mode=history`), and history is where
the truth about a job lives:

```text
labtest | Completed | 122,409 bytes downloaded
        | stored in Downloads/complete/labtest/
```

Note the two numbers a moment: 122,409
bytes came down the wire to make a
120,000-byte file — the difference is
the yEnc encoding and the articles'
wrapping, the cost of moving binary
bytes as text. And note the stage report
history keeps per job — Source,
Download, Servers, Repair, Unpack — the
pipeline of chapter 2, initialled at
every stage. When a job disappoints,
that report is where chapter 13 starts.

One surprise the lab met here, worth
knowing before it meets you: the
finished file had been **renamed** —
`payload.bin` came out as `labtest.bin`,
after the job. SABnzbd's deobfuscation
step renames finished files whose names
it judges unclear, and records the fact
in the stage report ("Deobfuscate
renamed 1 file(s)"). The bytes were
verified identical; only the name
changed. If a file is not called what
you expected, the stage report says why.

## Pause and resume: the big lever

The queue-level pause stops *all*
fetching while keeping every job in
place. The lab proved the hold honestly:
it paused the queue, *then* added a
second job, and watched the queue hold
it — `paused: true`, the job sitting at
**Queued**, not an article fetched:

```bash
curl -s "http://127.0.0.1:8080/api?mode=pause&apikey=YOUR-API-KEY"
curl -s "http://127.0.0.1:8080/api?mode=resume&apikey=YOUR-API-KEY"
```

Resume released it, and it completed
seconds later. The same lever exists per
job (pause one row in the interface)
when only one download should wait. Two
neighbours of the pause are worth
naming: a **speed limit** (Config →
General, or the queue's own control),
which throttles rather than stops —
for shared connections — and the
scheduler, which can pause and resume
on a clock, at Config → Scheduling.

## Priorities: who goes first

Every job carries a **priority**:
Force, High, Normal, Low, or Paused.
SABnzbd works the queue from the highest
claim down; within a claim, first come
first served. You set a job's priority
when adding it (the interface offers it;
the API takes `priority=`) or change it
on the queued row. Categories can carry
a standing priority of their own —
chapter 6's readback showed the built-in
categories at `-100`, which means
*inherit*: use the priority the job
arrived with. Priority matters exactly
when the pipe is the bottleneck — one
big job ahead of a small urgent one —
and is ceremony the rest of the time.
The lab's honest note: it exercised the
pause, the queue states and the
category-priority readback live; priority
*reordering* between two live jobs is
described from the documentation, since
on loopback both jobs finish before
order can matter.

## Check yourself

Add any small NZB twice. Pause the
queue, add the second copy, and confirm
in the queue that it waits; resume, and
confirm in history that both completed.
You have then seen every state a job
can be in — Queued, Downloading,
Completed — and the lever that moves
between the first two.

# Troubleshooting

The failures this guide's lab actually
met, plus the ones the documentation
warns every new user about. Work from
the evidence SABnzbd itself keeps: the
warnings list (the bell in the
interface, or `mode=warnings`), a job's
stage report in history, and the log
file at `logs/sabnzbd.log` beside the
config.

## Pages load, but nothing ever downloads

**Symptom:** the interface is fine, the
queue accepts jobs, and they sit there.
**Cause, as the lab met it:** par2 or
unrar missing. The warnings read
`par2 binary... NOT found!`, `unrar
binary... NOT found!`, and the verdict
`Essential modules are missing,
downloading cannot start.` **Fix:**
install both (chapter 3), restart
SABnzbd, and confirm the warnings list
is empty — the lab's second launch came
up clean and downloaded immediately.
This is the first thing to check on any
source install, before servers, before
anything.

## "Failed to connect: Connection refused"

**Symptom:** jobs show Downloading but
make no progress; warnings repeat
`Failed to connect: [Errno 111]
Connection refused ... @host:port`.
**Meaning:** the server is not there —
wrong host or port, the provider down,
or (the lab's version) the server
process killed mid-download. SABnzbd
does not give up: it retries with a
delay, and the lab's interrupted jobs
**completed on their own** once the
server returned, no re-adding needed.
**Fix:** check the server line in
Config → Servers (there is a Test
button), check your network, then wait
a minute before concluding anything —
the retry delay after an outage is
deliberate, and the queue's stillness
for a minute or so is that delay, not a
hang.

## A job fails: "not enough repair blocks"

The stage report counts missing or
malformed articles, and the repair line
names the shortfall (`1 short` in the
lab's first attempt). The data on your
server cannot rebuild the file. In
order: try the job's **Retry** if a
backup server has since been added;
check the posting's age against
retention; find a fresher or
better-supplied posting. Retrying the
same NZB at the same server returns the
same arithmetic. Chapter 8 has the full
story.

## The finished file has the wrong name

The deobfuscation step renames files
whose names it judges unclear, after the
job name — the lab's `payload.bin`
became `labtest.bin`, bytes verified
identical. The rename is recorded in the
job's stage report ("Deobfuscate renamed
1 file(s)"). If names matter to
downstream tools, the setting lives at
Config → Switches (deobfuscate
filenames), and the stage report is how
you confirm it was the culprit.

## The API answers "API Key Required" or "Invalid API key"

Everything except `mode=version` needs
the key, as `apikey=` on the call. Find
it in `sabnzbd.ini` or Config → General,
and check you are using the **API key**,
not the NZB key, for anything beyond
adding NZBs. A key can be regenerated
on that page if it has leaked — the old
one stops working at once, so update
your feeder programs in the same sitting.

## The wizard keeps coming back

A fresh visit redirects to `/wizard/`
until the wizard has been completed
once — it is how SABnzbd knows setup is
unfinished. If it returns after you
completed it, the config file was not
saved or not the one being read: check
the `--config-file` path you launched
with, and that the folder is writable.
The ini beside it is the truth; if
`[servers]` is empty there, the wizard
never landed.

## Everything is slow

In the order the lab would check:
connections set higher than the account
allows (the server refuses extras and
retries cost time); the incomplete
folder on a slow or nearly full disk;
a speed limit set and forgotten
(the queue status shows it); and the
connection itself — SABnzbd cannot beat
the pipe it is given. The stage report's
Servers line, showing bytes per server,
tells you if a backup server is doing
all the work while the primary idles,
which points at the primary's settings.

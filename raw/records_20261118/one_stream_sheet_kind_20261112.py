# one_stream_sheet_kind_20261112.py -- work file (Claude Opus 5.5, effort max; 12 Nov 2026).
# The two repairs that war game round 2 (section 1, item 1; section 4.1) asks before the crystal packages are sent:
# (1) one stream: Pro transcribes the pages itself, in order, without parallel workers (package 07, split among four
#     workers, read his signs inconsistently; package 11, one stream of 82 scans, came back clean);
# (2) a "sheet kind" column in the inventory (text; reused typed; cancelled draft; cover).
# Applied to ARCHIVE_PROMPT_TEMPLATE.md and to the unsent packages 30-33. Backups: *_before_one_stream_20261112.md.
# Every replacement must match exactly once; the script starts from the backup, so it can be rerun.
import io, os, shutil, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TARGETS = [os.path.join(HERE, "ARCHIVE_PROMPT_TEMPLATE.md")]
for d in sorted(os.listdir(os.path.join(HERE, "packages"))):
    if d[:3] in ("30_", "31_", "32_", "33_"):
        TARGETS.append(os.path.join(HERE, "packages", d, "PROMPT.md"))

ITEM5_NEW = (
    "5. **One stream, one notation.** Transcribe the pages yourself, in one stream, in the order given: do not split\n"
    "   them among parallel workers or sub-agents. When the pages of an earlier package of this archive were split among\n"
    "   workers, the same signs were read in different ways and the errors went unmarked. Keep one notation table for the\n"
    "   package from the first page on: his recurring signs and exponents, the letters of each alphabet, his quotation\n"
    "   marks and abbreviations, each with how it is written in LaTeX. Before the transcription is final (and before any\n"
    "   context is opened), compare how each recurring sign was read across all the pages, check every difference\n"
    "   against the ink, and make the readings agree. Put the table at the top of the doubts file.")
ITEM8_NEW = (
    "8. **A second reading of every page, then a frozen transcription.** When every page is done, read each page once\n"
    "   more against its image, as a second reader would: correct, or mark doubt, and append\n"
    "   `scan NNN audited <current UTC time>` to `progress.log`. Then write the SHA-256 of each page file and of the\n"
    "   combined transcription to `progress.log` with the line `transcription frozen <current UTC time>`; only then open\n"
    "   the context zip, if there is one.")
SHEET_SENTENCE = (
    " The column `sheet_kind` says what the sheet is: `text` (his notes on the subject of the folder), `reused_typed`\n"
    "   (a typed page of another text that he wrote on or whose back he used), `cancelled_draft` (a draft of his own that\n"
    "   he struck through), or `cover` (a folder cover or title sheet). A reused or cancelled sheet is still transcribed in\n"
    "   full.")

def load(p):
    return io.open(p, encoding="utf-8", newline="").read()

def save(p, t):
    io.open(p, "w", encoding="utf-8", newline="").write(t)

def between(t, start, end, new, tag):
    if t.count(start) != 1:
        raise SystemExit(tag + ": start found " + str(t.count(start)) + " times")
    i = t.find(start)
    j = t.find(end, i)
    if j < 0:
        raise SystemExit(tag + ": end not found")
    j += len(end)
    if j - i > 1500:
        raise SystemExit(tag + ": span too long")
    return t[:i] + new + t[j:]

def once(t, old, new, tag):
    if t.count(old) != 1:
        raise SystemExit(tag + ": found " + str(t.count(old)) + " times")
    return t.replace(old, new)

for p in TARGETS:
    b = p[:-3] + "_before_one_stream_20261112.md"
    if not os.path.exists(b):
        shutil.copyfile(p, b)
    t = load(b)
    crlf = (chr(13) + chr(10)) in t
    if crlf:
        t = t.replace(chr(13) + chr(10), chr(10))
    tag = os.path.basename(os.path.dirname(p)) or "template"
    t = between(t, "5. **One notation for the whole package.**", "Put the table at the top of the doubts file.",
                ITEM5_NEW, tag + " item 5")
    t = between(t, "8. **A second reader for every page, then a frozen transcription.**",
                "only then open the context zip, if there is one.", ITEM8_NEW, tag + " item 8")
    if "(columns `cote,scan,element," in t:
        t = once(t, "(columns `cote,scan,element,", "(columns `cote,scan,sheet_kind,element,", tag + " columns")
    else:
        t = once(t, "(columns `scan,element,", "(columns `scan,sheet_kind,element,", tag + " columns")
    t = once(t, "A row that is not yes means the transcription is not finished.",
             "A row that is not yes means the transcription is not finished." + SHEET_SENTENCE, tag + " sheet kind")
    if crlf:
        t = t.replace(chr(10), chr(13) + chr(10))
    save(p, t)
    print("edited:", p[len(HERE) + 1:])

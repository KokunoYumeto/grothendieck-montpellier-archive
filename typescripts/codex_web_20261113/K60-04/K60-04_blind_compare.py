"""Compare the independent readings, with the first-pass excerpts kept at disputed places.
Run beside K60-04_blind.tsv. A directory of first-pass pages can optionally be supplied.
The current final text is also located for every entry.
"""
from pathlib import Path
import argparse
import csv
import re
root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--first-pass", type=Path)
args = parser.parse_args()
changes = {
    '037 coefficient field': (
        '\\mathbb{Q}_{\\ell}',
        '\\mathbb{Q}_{\\ell}',
        'Kept the double-stroked Q first and Φ as its alternative. The long stroke runs through a loop and does not decide the alphabet.',
    ),
    '037 first local factor': (
        'L_{E_y}(t)',
        'L_{E_\\eta}(t)',
        'Changed y to η on the shared returning tail. The t/T doubt remains at the argument.',
    ),
    '037 second local factor': (
        'L_{E_y(x)}(t)',
        'L_{E_\\eta(x)}(t)',
        'Changed y to η consistently with the first factor and with scan 47.',
    ),
    '037 summands at x': (
        'E_y(x)=\\sum E_y^{i*}(x)',
        'E_\\eta(x)=\\sum E_\\eta^{i*}(x)',
        'Changed the two y subscripts to η. The dotted i and following star are separate strokes.',
    ),
    '037 qualifier of simple': (
        'abst.',
        'abst.',
        'Kept abst. first. The extra vertical is visible, but abs. joins the alternative readings.',
    ),
    '039 underlined heading': (
        '\\uline{Suite de la moyenne}',
        '\\uline{Sorite de la moyenne}',
        'Changed Suite to Sorite as first candidate. A distinct round o follows S and precedes the dotted run. Suite and Boîte remain alternatives.',
    ),
    '039 NB first line': (
        "S'il s'agit de groupes de type galoisien",
        "S'il s'agit de grpes de type galoisien",
        'The compact run before p favours grpes. Kept groupes as an alternative.',
    ),
    '039 after donc': (
        '\\deleted{si \\illegible{2}}',
        '\\deleted{si on est}',
        'The low second group and hooked end permit on est, possibly on a. Replaced the two-word illegible mark with those candidates, still cancelled.',
    ),
    '041 cancelled operation': (
        '\\deleted{opération \\uline{additive}, qui nous induis}',
        '\\deleted{opération \\uline{additive}, qui nous induit}',
        'The small raised end favours t on the second inspection. Kept s second under the cancellation.',
    ),
    '041 obliteration before virtuel': (
        '\\deleted{groupe}',
        '\\deleted{groupe}',
        'Kept groupe first. A second low run follows the descending loop, but gr remains possible.',
    ),
    '042 last number-system letter': (
        'N',
        '\\underline{N}',
        'Restored the faint typed underbar. Its distance from the baseline and width match the bars below Q on this page.',
    ),
    '043 after ss-gpe': (
        "\\deleted{d'ind}",
        "\\deleted{d'ind}",
        "Kept the short d'ind first. The cancellation covers the rest, and d'indice stays as an alternative.",
    ),
    '043 word over replacement': (
        '\\inserted{obtient}',
        '\\inserted{obtient}',
        'Kept obtient and the alternative obtiendra. The faint ending fails to establish the extended future form.',
    ),
    '043 after the cancelled Z': (
        'et disons',
        'et notons',
        'Changed the first candidate to et notons. There is an upright in the middle of the word. The slashes still impede the reading.',
    ),
    '043 characteristic series clause': (
        'déterminé par sa série car.',
        'donné par sa série car.',
        'The short letter run favours donné. Kept donnée and the longer déterminé/déterminée as alternatives inside the cancelled paragraph.',
    ),
    '045 blot before E to angular power': (
        '\\deleted{\\text{on}}',
        '\\deleted{\\text{en}}',
        'The first low loop is more e-like. Gave en first and retained on in the cancellation.',
    ),
    '045 struck first factor of trace': (
        '\\deleted{I}\\pi g',
        '\\deleted{I}\\pi g',
        'Kept I first because of the two horizontal strokes. The reading 1 remains under the deletion.',
    ),
    '045 mark between boxed limits': (
        '\\deleted{i}\\\\\\psi_\\alpha\\to\\varphi',
        '\\substack{\\deleted{i}\\\\\\psi_\\alpha}\\to\\varphi',
        'Kept the cancelled upright as first reading. A bar on the lower psi and a separate dash are now explicit alternatives.',
    ),
    '045 cancelled words after défini': (
        '\\deleted{si}',
        '\\deleted{même si}',
        'There are two separated groups under a single line. Gave même si first, keeping si as an alternative.',
    ),
    '045 verb on last line': (
        'réduisant',
        'restreignant',
        'Changed to restreignant. A tall medial t and a descending g are both visible.',
    ),
    '047 last member of quotient chain': (
        '\\widehat{Z}',
        '\\widehat{\\mathbb{Z}}$.',
        'Restored the double-struck Z under the hat and the adjacent point. The enlarged crop separates both diagonals and the point from its foot.',
    ),
}
glyph = '\\mathord{\\text{\\tikz[x=.66em,y=.68em,baseline=0pt]{\\draw[line join=round] (.80,.95)--(.12,.24)--(.83,.34)--(.14,-.37);}}}'
def clean(value):
    value = value.replace(glyph, "ϟ")
    token = r"\unsure{"
    while token in value:
        i = value.rfind(token)
        start = i + len(token)
        depth = 1
        for j in range(start, len(value)):
            if value[j] == "{": depth += 1
            if value[j] == "}": depth -= 1
            if not depth: break
        else: raise ValueError("Unclosed doubt")
        value = value[:i] + value[start:j].split("|", 1)[0] + value[j+1:]
    value = re.sub(r"([_^])\{(\\[A-Za-z]+|[A-Za-z0-9])\}", r"\1\2", value)
    return re.sub(r"\s+", "", value.replace("$", ""))
def esc(s): return s.replace("|",r"\|").replace("\n"," ")
def table(rows):
    return "\n".join("| " + " | ".join(map(esc, row)) + " |" for row in rows)
disputes, tracks, missing = [], [], []
with (root/"K60-04_blind.tsv").open(newline="") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        n, place, blind = row.values()
        key = n+" "+place
        filename = "K60-04_60_scan"+n+".tex"
        current = clean((root/"pages"/filename).read_text())
        first, settled, comment = changes.get(key, [blind, blind, "Same reading."])
        if args.first_pass and clean(first) not in clean((args.first_pass/filename).read_text()):
            missing.append(key+" in supplied first pass")
        final = settled
        found = clean(final) in current
        if not found: missing.append(key+" in delivered page")
        if clean(first) != clean(blind):
            disputes.append([n, place, "`"+blind+"`", "`"+first+"`", comment])
        tracks.append([n, place, "`"+final+"`", "located" if found else "unlocated"])
body = "# Blind reading compared with the page files\n\n"
body += (f"{len(tracks)} places compared. {len(disputes)} differences in the primary reading or its page state. "
         "Comparison ignores whitespace, math delimiters and alternative readings after the first. "
         "ϟ stands for the angular sign drawn in the TeX. At a disputed place the first-pass excerpt is retained so that later corrections do not erase the comparison. "
         "The last table locates the accepted text in the delivered page, including any subsequent witness annotation.\n\n")
body += "## Differences\n\n| Scan | Place | Blind | First pass | Settlement on the image |\n|---|---|---|---|---|\n" + table(disputes)
body += "\n\n## All compared places\n\n| Scan | Place | Delivered text | Search |\n|---|---|---|---|\n" + table(tracks)+"\n"
(root/"K60-04_blind_compare.md").write_text(body)
if missing: raise SystemExit("\n".join(missing))
print(f"{len(tracks)} compared; {len(disputes)} differences; all accepted readings located.")

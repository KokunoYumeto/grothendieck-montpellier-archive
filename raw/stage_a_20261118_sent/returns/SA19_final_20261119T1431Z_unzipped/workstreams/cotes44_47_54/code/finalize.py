"""Final presentation and provenance notes; does not generate audit verdicts."""
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
months = ('January|February|March|April|May|June|July|August|September|October|November|December')

for name in ['synthesis.md', 'directions.md', 'our_project_leads.md']:
    p = ROOT / name
    s = p.read_text()
    s = re.sub(r'\b(Theorems?|Propositions?|Corollar(?:y|ies)|Lemma|Definition|Exercise|Chapter|Exposé)(?=[0-9IVX])', r'\1 ', s)
    s = re.sub(r'\b([Cc]otes?)(?=\d)', r'\1 ', s)
    s = re.sub(r'\b(pp?\.)(?=\d)', r'\1 ', s)
    s = re.sub(r'\b(is|gives|by|and|in|on|first|unrecorded)(?=\d)', r'\1 ', s)
    s = re.sub(r'(\d)(' + months + r')', r'\1 \2', s)
    s = re.sub(r'(' + months + r')(?=\d)', r'\1 ', s)
    s = re.sub(r',(?!\s)', ', ', s)
    s = s.replace('Exposé XXI', 'Exposé XXI').replace('EGA IV₃11.', 'EGA IV₃ 11.')
    s = s.replace('and44 references', 'and 44 references').replace('and63 claim-specific', 'and 63 claim-specific')
    s = s.replace('A3, B29, C21, D0, E7, F3', 'A 3, B 29, C 21, D 0, E 7, F 3')
    s = s.replace('A3, B26, C21, D0, E6, F3', 'A 3, B 26, C 21, D 0, E 6, F 3')
    p.write_text(s)

# This change replaces a paraphrase with a short literal source quotation.
p = ROOT / 'claims.json'
claims = json.loads(p.read_text())
for claim in claims:
    if claim['id'] == 'CL-SA19-461':
        claim['his_statement'] = 'symétrique, donc provenant — du moins modulo le facteur 2'
p.write_text(json.dumps(claims, ensure_ascii=False, indent=2) + '\n')

(ROOT / 'source_coverage.md').write_text('''# Source-reading coverage: cotes 47, 54 and 44

All 37 assigned entries were read against their actual passages: `MPL_16+47+54+44#44–79` and `#85`. All 28 pages of the three cotes were read, including covers, reused typescripts, canceled arguments and retained marginal additions. `reading_coverage.tsv` gives every page and its original LaTeX line range. `entries.tsv` gives each entry’s individual verdict; those verdicts were written from reading, not inferred from headings by script.

The mixed package label is not the physical cote. Cote 47 contains 11 pages (original LaTeX lines 2051–2572), cote 54 contains 8 pages (2574–2751), and cote 44 contains 9 pages (2753–3001). Entry #79 concerns cote 54’s last reused page, not cote 44. Entry #85 is bibliographical and is merged with #64 in item SA19-217.

The supplied doubts table for these cotes occupies Markdown lines 480–685 of `MPL_16+47+54+44_doubts.md`; its later page-level comments were also read. Those comments report the earlier transcription run’s visual inspection. This audit has no scans and makes no visual claim of its own. The 48 mathematical reading alarms in `readings.tsv` identify what a subsequent scan audit must decide. No transcription was edited.

The supplied second-pass files concern cote 16, not these three cotes. Their absence here is not an uncompleted second-pass task. Historical dates were not transferred from reused material or later publications to undated manuscript leaves. Only the cote 44 letter supplies its explicit Bures, 12 August 1964 date.

Every one of the 63 claim records has a dated searched fate, a source-status check and reference closure. Four records are separately labelled refinements or historical specializations introduced in this run: CL-SA19-459, 460, 465 and 467. The remaining 59 records target claims actually recorded in the supplied source. CL-SA19-458 retains a deleted source formulation and explicitly distinguishes the reconstruction of its invoked universal-ideal consequence.

Primary mathematical passages, bibliographic metadata and withdrawal records have different verification strengths, recorded in `references.bib`, `research/reference_audit.json` and `CHECK_EVENTS.tsv`. `note = {verified}` means that the cited URL was opened; it does not silently mean that every result in the work was verified. The original Lieberman chapter is marked unverified. Search provenance is retained in `research_log.tsv` and the numbered raw search records.

The eight directions in `directions.md` are prospective tasks, each with originating item, claim and problem IDs. They have not been developed here. Independent reconstructions and counterexamples needed to audit the existing claims are in `computations.md`; executable exact certificates and their outputs are supplied separately. No direction was substituted for an unfinished entry verdict or an unsearched claim.
''')

print('Final prose spacing, literal source quotation and source-coverage note written.')

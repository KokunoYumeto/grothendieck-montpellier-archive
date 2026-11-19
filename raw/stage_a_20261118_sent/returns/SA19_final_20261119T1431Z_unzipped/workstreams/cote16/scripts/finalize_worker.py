"""Explicit final editorial amendments and provenance ledger.

This script serializes decisions already made by direct reading; it does not
infer entry verdicts, claim meanings or source matches from text cues.
"""
from pathlib import Path
import csv,json

root=Path(__file__).resolve().parents[1]

def replace(path,old,new):
    p=root/path
    s=p.read_text()
    assert old in s,(str(path),old[:80])
    p.write_text(s.replace(old,new))

# Primary EGA text could not be obtained. Keep the lead outside checked links.
p=root/'scripts/build_links.py'
s=p.read_text()
s=s.replace('rows=[]\n','rows=[]\nleads=[]\n')
old="a('published work','c16/43 lines1706–1716','EGAIV4 §18.11.6–18.11.7; https://numdam.org/item/PMIHES_1967__32__5_0/','Galley discussion of purely inseparable local extensions and proposed deletion of(ii).','Supplied galley number and mathematical paragraph read; published chapter metadata/section location checked. Exact deleted subclause is not reconstructed from the later version.',P+'#20')"
new="leads.append(['published work','c16/43 lines1706–1716','EGAIV4 §18.11.6–18.11.7; https://numdam.org/item/PMIHES_1967__32__5_0/','Publication-comparison lead: local inseparability obstruction and proposed deletion of(ii).','Source passage read. Primary metadata opened, but the49,852,990-byte publication PDF exceeds web extraction limit and two direct download attempts stalled and were interrupted. Exact published primary passage remains unread; English translation proxy is only a locator. NOT a verified two-endpoint link.',P+'#20'])"
assert old in s
s=s.replace(old,new)
s=s.replace("print(f'Wrote {len(rows)} individually checked links.","with (root/'publication_comparison_leads.tsv').open('w',newline='') as f:\n    w=csv.writer(f,delimiter='\\t');w.writerow(fields);w.writerows(leads)\nprint(f'Wrote {len(rows)} individually checked links and {len(leads)} separate unverified publication-comparison lead.")
p.write_text(s)

replace('scripts/build_claims.py',
 'The stated date on the letter is 6.1.1966 and is not changed to 1967 on bibliographic grounds.',
 'This low-dimensional list is in the first Coates letter, dated4.1.67 on scan44. The separate second letter begins on scan48 and reads6.1.1966; its date is not transferred to this list.')
replace('scripts/build_claims.py',
 'Publication 1968; draft date literally 6 January 1966, earlier-run inferred 1967 not accepted as ink.',
 'Publication1968; this list belongs to the first letter dated4January1967. The separate second letter dated6January1966 is preserved literally, without chronological amendment.')
replace('scripts/build_claims.py',
 'Published EGA IV4 Remark 18.11.6 is the locator. The original galley is supplied; a modern English transcription of 18.11.6 was opened as a comparison aid, not used to decide manuscript ink or editorial causality.',
 'EGA IV4 Remark18.11.6 is the identified publication locator from the galley and a modern English transcription. Primary publication metadata was opened, but the49.85MB primary PDF exceeded web limits and two downloads stalled. Exact primary passage remains unread, so the publication comparison is a separate lead, not a verified two-endpoint link. The local mathematical obstruction is independently checked.')
replace('scripts/build_claims.py',
 'Compared the exact EGA IV4 18.11.6–18.11.7 neighborhood. The supplied fragment ends before its conclusion, and the marginal Vider|Virer reading remains undecided.',
 'Located the EGA IV4 18.11.6–18.11.7 neighborhood through the supplied galley and an English translation proxy; exact published primary text was unavailable. The supplied fragment ends before its conclusion, and the marginal Vider|Virer reading remains undecided. No verified published counterpart to the deleted(ii) is claimed.')

replace('scripts/build_support.py',"'refuted, with refined statement’s id'","\"refuted, with the refined statement's id\"")
replace('scripts/build_support.py',
 "    elif n in proof:\n",
 "    elif n in {227,268}:\n        ev(c['id'],'targeted proof check','Literal detached assertion fails under the stated interpretation; the exact counterexample and missing qualification are documented. '+c['computation'])\n    elif n in proof:\n")
replace('scripts/build_support.py',
 'read original-exposé statements X3.8–3.9 and XI1.1 with their contexts;',
 'read original-exposé statements X3.4 with its purity-based proof context, X3.8–3.9 and XI1.1;')
replace('references.bib',
 'II§7 pp125--136 directly OCR-read,',
 'II§7 pp120--136 directly OCR-read,')
replace('references.bib',
 'Primary bibliographic record checked; very large primary PDF exceeded web extraction limit. Supplied galley c16/43 read. English transcription of 18.11.6--18.11.7 used only as a comparison lead, not an authoritative ink check.',
 'Primary bibliographic record checked;49,852,990-byte primary PDF exceeded web extraction limit, and two direct downloads stalled and were interrupted. Exact original18.11.6--18.11.7 text remains unread. Supplied galley c16/43 read; English transcription used only as a comparison lead, not a verified publication match or authoritative ink check. The lead is excluded from the checked links table.')

# Save actual interruption outcomes, not fabricated timeout exceptions.
for label,url,session in [
 ('EGAIV4','https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf',67772),
 ('EGAIV4_article','https://www.numdam.org/article/PMIHES_1967__32__5_0.pdf',39343)]:
    report={'label':label,'url':url,'status':'interrupted after repeated empty polls; no file produced','session_id':session,'exit_code':130,'tool_input':'Ctrl-C','qualification':'Actual process output was empty. This is an interruption record, not a reported urllib exception. The alternative web extraction explicitly reported content length49,852,990 bytes as too large.'}
    (root/'outputs'/f'fetch_{label}.json').write_text(json.dumps(report,indent=2)+'\n')

# Each exception is a manually specified provenance decision.
exceptions={
 227:('source assertion; this-run refutation','The norm-one assertion is in the source; the exact nondegenerate four-form norm-zero counterexample is this audit’s addition.'),
 228:('source question; earlier-run example rechecked','Infinite-orbit question on source; the normalized six-dimensional positive example came from the earlier run and was independently checked here.'),
 229:('source question; earlier-run family rechecked','Unbounded-span question on source; the normalized family came from the earlier run; all-parameter argument and finite certificates checked here.'),
 231:('reused foreign typescript; author unidentified','Cohomological vanishing fragment; no Grothendieck authorship inferred from location.'),
 232:('reused foreign typescript; author unidentified','Amitsur argument fragment; no Grothendieck authorship inferred from location.'),
 245:('source historical report of named prior work','Letter reports Tate’s communication about Hodge1938; original Hodge full text and broad reception not checked.'),
 246:('source self-correction reporting Serre objection','The source abandons a proposed smooth reduction and reports Serre’s fundamental-group objection.'),
 256:('named foreign author: Karoubi','The reused announcement explicitly names Max Karoubi; expanded primary1968paper read.'),
 257:('reused English typescript; exact mathematical lineage','HartshorneII7.6 is an exact mathematical counterpart; detached draft authorship not proved.'),
 258:('reused English typescript; exact mathematical lineage','HartshorneII7.17 and7.18 match theorem content; preliminary draft provenance remains separate.'),
 259:('named prior work recalled: Matlis','The source explicitly attributes module decomposition to Matlis; primary Matlis1958read.'),
 260:('reused English typescript; author unidentified','Coherent sheaf Ext/local injectivity material; mathematical lineage checked, draft identity separate.'),
 261:('reused English typescript; author unidentified','Way-out/RHom fragment; no unique original author assigned.'),
 279:('earlier-run reconstruction only','Normalized integral-string model; not the literal ordinary-contraction exterior construction.'),
 280:('this-run reconstruction only','Two-sided cutoff repair; not changed ink or a separately asserted manuscript formula.'),
 281:('this-run reconstruction only','Flat finite-fibre criterion retaining the flatness on source scan56; not literal scan54 claim.')
}
with (root/'claim_origins.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['claim_id','origin','qualification'])
    for n in range(201,285):
        origin,qualification=exceptions.get(n,('source-record claim or program','Precise status and attribution are in claims.json; this category does not imply originality or a proved theorem.'))
        w.writerow([f'CL-SA19-{n}',origin,qualification])

newrows=[
 ['2026-11-19','CL-SA19-246','SGA1 primary annotated reprint','ExposéX3.3–3.4 and proof context, printed213–214/reprintPDF228–229','Proper regular birational fundamental groups canonically identified; proof via purity read. Specialization separately usesX3.8–3.9.','Primary exact statement and preceding argument opened/read; source date and author-objection report remain distinct.'],
 ['2026-11-19','CL-SA19-262–263','Numdam primary metadata;primary PDF;translation proxy','EGAIV4 §18.11.6–18.11.7;item/article PDF URLs','Primary web extraction rejected49,852,990bytes; two direct downloads produced no file and were interrupted with exit130. Lead removed from verified links.','Source galley and modern related algebra checked; exact primary published neighborhood unread.']
]
p=root/'research_log.tsv'
with p.open(newline='') as f:
    reader=csv.reader(f,delimiter='\t');allrows=list(reader)
allrows.extend(newrows)
with p.open('w',newline='') as f:csv.writer(f,delimiter='\t').writerows(allrows)

replace('synthesis.md','28 checked links, 28 bibliography entries, 178 check events and 26 research-log rows before the final supplementary source checks.','27 checked links, one separate publication-comparison lead, 28 bibliography entries, 178 check events and 28 research-log rows.')

print('Moved EGA primary-text-unread comparison outside checked links; saved two interrupted fetch outcomes.')
print('Corrected CL-SA19-244 date association: first letter4January1967, second letter6January1966.')
print('Saved84-row claim-origin ledger, exact SGA1X3.4 reading event, and two final research rows.')

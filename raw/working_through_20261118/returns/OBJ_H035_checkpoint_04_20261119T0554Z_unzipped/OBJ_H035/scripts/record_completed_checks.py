"""Record the actual second pass and source checks, and update the dated ledger."""
from pathlib import Path
from datetime import datetime,timezone
import csv,re

root=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; OBJ_H035 single-stream run'
with (root/'STATEMENTS.tsv').open() as stream: statements=list(csv.DictReader(stream,delimiter='\t'))
with (root/'NOTES_VERDICTS.tsv').open() as stream: notes=list(csv.DictReader(stream,delimiter='\t'))
with (root/'CHECK_EVENTS.tsv').open('a') as stream:
    writer=csv.writer(stream,delimiter='\t')
    for row in statements[21:]:
        n=int(row['id'].split('.')[1])
        result=row['status']
        if n==39:result+='; dense generic comparison, countable local-completion lemma, Dedekind and artinian cases checked'
        writer.writerow([row['id'],stamp,who,'targeted proof check — independent second pass from hypotheses',result,f'research/SECOND_CHECKS.md H035.{n}; PROOFS.tex H035.{n}'])
    for row in notes:
        writer.writerow([row['entry_id'],stamp,who,'used and rechecked in this run — specified note subclaim and scan anchor',row['mathematics']+'; '+row['reason'],'NOTES_VERDICTS.tsv: '+row['anchor']])
    refs={
      'Grothendieck94':('carried as documentary background; no blanket mathematical endorsement','Official PDF and attached readings compared; targeted continuation found on scans 15–24'),
      'EGAIII2':('used and rechecked in this run','7.7.6–9 pp.69–71; extra source-presentation hypothesis in 7.7.8 retained'),
      'EGAIV2':('used and rechecked in this run','Proposition 6.11.8 p.162 and Remarques 6.11.9 pp.162–163: CMU, not generic canonical existence'),
      'Murre294':('used and rechecked in this run','Theorem 3 p.255; flat finite type over locally noetherian base plus adic condition; proper case matched'),
      'Hall2014':('used and rechecked in this run','Final author version Theorems C,D,E p.4 and Example 3.10 p.18; underived/derived distinction retained'),
      'Lyu2025':('used and rechecked in this run','Final journal PDF: Corollary 4.7 p.225; Lemma 6.1(ii), Theorem 6.2 p.230; Remarks 7.7,7.9 and Theorem 8.1 p.233'),
      'Stacks08K6':('used and rechecked in this run','Proposition 99.3.10 checked as a geometric Hom comparison; not used as the exact six-axiom theorem'),
      'Stacks08JY':('used and rechecked in this run','Lemma 99.3.9, noetherian Hom case; hypotheses retained'),
      'Stacks0DW3':('used and rechecked in this run','Section 47.19 canonical-module convention matched to completion in H035.16'),
      'Stacks0DW4':('used and rechecked in this run','Section 47.20 canonical modules and CM duality used in H035.17–18'),
      'Jaffe1997':('used and rechecked in this run','1994 arXiv section 7 pp.26–29: proper flat and Dedekind positive cases, then underived-cohomology obstruction to coherence; not a counterexample to H035.39'),
      'Illusie2004':('used and rechecked in this run','Corollary 2.9 printed p.14/PDF p.16, formal Ext comparison; compared with EGA III 4.5.1'),
      'SGA3VIII':('used and rechecked in this run','2009 revision Theorem 6.4 and Corollary 6.5 pp.18–19; essentially-free hypothesis distinct from proper flatness'),
      'Stacks058G':('used and rechecked in this run','Theorem 10.81.4: flat modules as filtered colimits of finite free modules, used for flat scalar extension'),
      'Stacks00IP':('used and rechecked in this run','Lemma 10.51.4: Krull intersection for finite local modules, used in support/isomorphism tests'),
      'Stacks023N':('used and rechecked in this run','Proposition 35.3.9: effective faithfully flat module descent, matching H035.3'),
      'Stacks00MB':('used and rechecked in this run','Lemma 10.97.2: noetherian completion flat and exact on finite modules'),
      'Stacks01PJ':('used and rechecked in this run','Lemma 28.23.6: finitely presented quasi-coherent approximation on quasi-compact quasi-separated schemes'),
      'Stacks051S':('used and rechecked in this run','Lemma 10.118.2: relative generic freeness over a noetherian domain; finite-type coefficient algebra hypotheses matched'),
      'Stacks02OC':('used and rechecked in this run','Theorem 30.20.5: proper coherent formal functions over noetherian base and arbitrary ideal'),
      'Stacks0A0H':('carried as background without fault found','Section 52.7 derived formal functions opened; not used to replace the underived tensor in H035.34'),
    }
    for key,(how,result) in refs.items():
        writer.writerow([key,stamp,who,how,result,'references.bib '+key+'; research/SEARCH_AUDIT.md; indicated PROOFS.tex dependencies'])
    writer.writerow(['H035.39',stamp,who,'targeted proof check — proved reduction only','Over countable local R, every finite principal-completed module has finite image by descent from Rhat; principal-completion continuity still open','PROOFS.tex H035.39, further finiteness reduction; research/COMPOSITION_ATTEMPTS.md'])

ledger=root/'PROGRESS_LEDGER.md'
old=ledger.read_text()
history=old.split('## Dated milestones (not the mandatory hourly reviews)',1)[1].split('## Mandatory progress reviews',1)[0]
head=f'''# H035 progress ledger

**Main question: H035.30, Théorème 12 (94/016–017): PROVED.**

The six-axiom finite-representability criterion has a complete reconstruction
in PROOFS.tex and a second derivation from its hypotheses in
research/SECOND_CHECKS.md. The false intermediate statements are repaired
using hypotheses actually present in Theorem 12; its own hypotheses are
not strengthened.

**Current research gate: H035.39, the broad composition programme.**

Only completion compatibility remains for the explicit affine reconstruction.
The generic condition has been upgraded to a dense open and proved stable
under composition. Full closure holds for Dedekind domains and artinian
rings. For countable A, maximal-ideal completion is stable. For countable
local A, outputs on finite principal-completed modules are finite by
faithfully flat descent from the maximal completion, leaving continuity on
the nonartinian tower. The smallest outstanding test is principal completion
over a two-dimensional countable regular local ring; arbitrary uncountable
bases also retain a formal-output finiteness issue. H035.40 tracks the
undefined general two-scheme extension separately from its proved examples.

Start: 2026-11-19T02:54:34Z. One stream; no delegated workers.
Current ledger update: {stamp}.
Mandatory three-hour review due 05:54:34 UTC, then hourly.
The results attachment remains unopened.

## Current statement rows

| Item | State | Current gate or checked result |
|---|---|---|
'''
for row in statements:
    detail=row['reconstruction'] if row['id'] not in {'H035.39','H035.40'} else row['statement']
    head+='| '+row['id']+' | '+row['status']+' | '+detail.replace('|','/')+' See PROOFS.tex and research/SECOND_CHECKS.md. |\n'
head+='\n## Supplied-note subclaim rows\n\nAll six entries were read in full. The 44 rows below distinguish their claims; a documentary uncertainty is not a pending mathematical proof.\n\n| Entry and anchor | Verdict | Placement |\n|---|---|---|\n'
for row in notes:
    head+='| '+row['entry_id']+' — '+row['anchor'].replace('|','/')+' | '+row['mathematics'].replace('|','/')+' | '+row['placed'].replace('|','/')+' |\n'
head+='\n## Dated milestones (not the mandatory hourly reviews)'+history
head+=f'- {stamp}: second checks completed for H035.22–38 and H035.41–46; main H035.30 proved. All 44 supplied-note subclaims have individual verdicts. H035.39–40 remain open with the narrower gates stated above.\n'
head+='\n## Mandatory progress reviews\n\nNone yet due. Movement means an open row changes status or a main gate becomes strictly smaller; packaging and restatement do not count.\n'
ledger.write_text(head)

proof=root/'PROOFS.tex'
data=proof.read_bytes()
bad=b'{\rm prime}'
assert data.count(bad)==1
proof.write_bytes(data.replace(bad,b'{\\mathrm{prime}}'))
index=root/'readings/LINE_INDEX.md'
index.write_text(index.read_text().replace('16 gr O_X','16 first graded coefficient uncertain'))
for path in [root/'NOTES_VERDICTS.tsv',root/'scripts/write_note_verdicts.py']:
    path.write_text(path.read_text().replace('Corollary 6.11.9','Remarques 6.11.9'))
with (root/'progress.log').open('a') as stream:
    stream.write(f'main theorem H035.30 second-check complete; 44 note subclaims adjudicated; H035.39–40 open {stamp}\n')
print('Recorded 25 statement second checks, 44 note-subclaim checks,',len(refs),'source checks, and one new composition reduction.')
print('Updated dated ledger; fixed one carriage-return escape in the LaTeX and one EGA locator label.')

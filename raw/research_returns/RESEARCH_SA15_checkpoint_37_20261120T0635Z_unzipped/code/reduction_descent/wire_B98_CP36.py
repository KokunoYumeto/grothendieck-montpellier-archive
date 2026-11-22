from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib,re
own=Path(__file__).resolve().parents[1];root=own.parents[1]
hist=own/'notes/CP36_before_B98_wiring';hist.mkdir(exist_ok=False)
con=root/'code/consolidate.py';cfg=root/'notes/checkpoint36_promoted_inputs.json'
changes=root/'notes/checkpoint36_changes.md';log=root/'notes/ROOT_SEARCH_LOG_36.md';bib=own/'reduction_descent.bib'
old={p:p.read_text() for p in (con,cfg,changes,log,bib)}
for p,v in old.items():(hist/p.name).write_text(v)
anchor="'B_irreducible_point_field_layers.tex']"
assert old[con].count(anchor)==1 and 'B_first_wild_cyclotomic_different.tex' not in old[con]
newcon=old[con].replace(anchor,"'B_irreducible_point_field_layers.tex',\n                    'B_first_wild_cyclotomic_different.tex']")
items=json.loads(old[cfg]);entry='agents/reduction_descent/B_first_wild_cyclotomic_different.tex'
assert entry not in items;items.append(entry)
newcfg=json.dumps(items,indent=2)+'\n'
newchanges=old[changes]+'''\n## Exact first wild height-two index at five (B98)\n\nPromoted at05:37:57.534831 UTC after full root and obstruction/crystal companion proof/source/code audits at05:35:54.361771 and05:37:26.262536 UTC. The exact full B.4 result is nu_min(5,20,2)=2: actual125-torsion determines every requested prime-to-five special character, while the retained B63 construction gives failure at actual25. The all-prime theorem excludes irreducible-residual whole height-two comparisons with different special characters at e=p(p−1). Its actual two-point-column conductor bound contradicts the final cyclotomic character, using a direct different calculation over the Cohen field; the common first cyclotomic layer is explicitly retained. The full p5 conclusion additionally uses B76, B96 and B90 with their exhaustive prior reductions. General B.4, other first-wild primes, arbitrary ramification and higher height remain open. Unchanged isolated reruns took1.8024525419896236 and1.875493136991281seconds, preserving author bytes. Exact candidate, field-scope clarification, code/output and audits are retained. The canonical follows B97 and is required by CP36; no build or future review was executed by this wiring.\n'''
newlog=old[log]+'''\n## B98 cyclotomic different and exact first-wild index\n\nThe author, root and companion freshly read the retained original Colmez Proposition3.17 trace-dual transitivity proof, complete Proposition3.18 monogenic derivative proof including its continuation, and Corollary3.19 ramification-different proof, printedpp17–18. The retained text is agents/reduction_descent/sources/colmez_corps_locaux.txt, SHA795ebafb9326f68ed625c2f44b7f4a220e0209c489530ace62cda3de357ca419. Full actual B86 Cohen-field and B97 point-field arguments were checked; the complete B76 reduction and B63 all-index lower construction were freshly reread for the exact(5,20,2) assembly. No new web opening, PDF-image inspection, finite-residue class-field theorem, Hasse–Arf theorem or priority claim is made. Full root audit05:35:54.361771 and companion audit05:37:26.262536 are retained in outputs/root_B98_audit.json and agents/obstructions_crystals/B98_independent_audit.json. The bibliography preserves all older reading scopes and appends these precise new passages.\n'''
match=re.search(r'@misc\{ColmezCorpsLocaux,[\s\S]*?\n\}',old[bib]);assert match
oldentry=match.group()
assert oldentry.count('UTC.}\n}')==1
newentry=oldentry.replace('UTC.}\n}', 'UTC. Fresh B98 reading on 20 November 2026: complete Proposition3.17 trace-dual transitivity proof, Proposition3.18 monogenic derivative proof including its continuation, and Corollary3.19 ramification-different proof, printedpp17--18. The author and both full auditors independently read the retained original text, with root PASS05:35:54.361771 and companion PASS05:37:26.262536 UTC. The complete B86 Cohen-field proof and actual B97 field arguments supply the arbitrary-perfect-residue scope. No new external web opening, PDF image, finite-residue class-field theorem or Hasse--Arf integrality theorem is claimed.}\n}')
newbib=old[bib][:match.start()]+newentry+old[bib][match.end():]
new={con:newcon,cfg:newcfg,changes:newchanges,log:newlog,bib:newbib}
compile(newcon,str(con),'exec')
for p,v in new.items():
 p.write_text(v)
 (hist/(p.name+'.diff')).write_text(''.join(difflib.unified_diff(old[p].splitlines(True),v.splitlines(True),fromfile='before/'+p.name,tofile='after/'+p.name)))
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'status':'WIRED_CP36','actual_utc':datetime.now(timezone.utc).isoformat(),'canonical':entry,
 'canonical_sha256':h(root/entry),'prior_directory':str(hist),
 'files':{str(p.relative_to(root)):{'before_sha256':hashlib.sha256(old[p].encode()).hexdigest(),'after_sha256':h(p)} for p in new},
 'scope':'Single B98 include after B97, required-input addition, append-only CP36 changes/source-log and exact owned bibliography reading-scope addition. Prime-Heisenberg and all other A4 entries preserved. No updater, report, ledger or build edit.'}
(own/'outputs/B98_CP36_wiring.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))

from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib
own=Path(__file__).resolve().parents[1];root=own.parents[1]
hist=own/'notes/CP36_before_B97_wiring';hist.mkdir(exist_ok=False)
con=root/'code/consolidate.py';cfg=root/'notes/checkpoint36_promoted_inputs.json'
changes=root/'notes/checkpoint36_changes.md';log=root/'notes/ROOT_SEARCH_LOG_36.md'
old={p:p.read_text() for p in (con,cfg,changes,log)}
for p,v in old.items():(hist/p.name).write_text(v)
anchor="'B_full_Iwahori_selected_point.tex']"
assert old[con].count(anchor)==1 and 'B_irreducible_point_field_layers.tex' not in old[con]
newcon=old[con].replace(anchor,"'B_full_Iwahori_selected_point.tex',\n                    'B_irreducible_point_field_layers.tex']")
items=json.loads(old[cfg]);entry='agents/reduction_descent/B_irreducible_point_field_layers.tex'
assert entry not in items;items.append(entry)
newcfg=json.dumps(items,indent=2)+'\n'
newchanges=old[changes]+'''\n## Audited irreducible-residual point-field layers (B97)\n\nPromoted at 05:34:20.925830 UTC after full root and monodromy companion audits at 05:32:32.208856 and 05:32:53.522155 UTC. For every p>=5 at e=p(p−1), every residual-irreducible different-special-character actual p³ comparison has all nonzero second-point degrees p² and third-point relative degrees p². The actual first layer has dimension at least three and nonzero trace; only traceful layer shapes (3,4) or (4,4) remain. The complete actual point-field and terminal-character conductor bounds are proved. At p5/e20, with the separately promoted B96 residual-wild exclusion and earlier reducible exclusions, this result leaves only irreducible orders5^7 and5^8; it does not itself close the least index. The exact author checker and literal isolated reruns (1.2067616679996718 and 1.1990244229964446 seconds) are retained. The canonical is included after B96 and required by CP36; no build or future review was executed. B98 remains a separate candidate pending its full audits.\n'''
newlog=old[log]+'''\n## B97 actual irreducible point fields and conductors\n\nThe complete six-label candidate and standalone checker passed the root audit at05:32:32.208856 UTC and monodromy companion audit at05:32:53.522155 UTC. Both rederived the actual field intersections, stabilizer normality, coefficient boundary cases, exact upper-conductor conversions and Lie-algebra reduction. Complete invoked internal B79/B80/B81/B86/B90/B96 proofs were reread in the recorded scopes. The companion freshly reread the retained original Colmez text from Remark3.6 through the full Proposition3.7, Lemma3.8, Corollary3.9, Theorem3.10 and Propositions3.12–3.13 proofs, printed14–16. No new external-source opening or image inspection is claimed. Exact scopes, unchanged author hashes and all isolated outputs are in outputs/root_B97_audit.json and agents/monodromy/outputs/independent_B97_point_field_layers_audit.json. No priority claim or additional literature theorem follows from the finite supplement.\n'''
new={con:newcon,cfg:newcfg,changes:newchanges,log:newlog}
compile(newcon,str(con),'exec')
for p,v in new.items():
 p.write_text(v)
 (hist/(p.name+'.diff')).write_text(''.join(difflib.unified_diff(old[p].splitlines(True),v.splitlines(True),fromfile='before/'+p.name,tofile='after/'+p.name)))
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'status':'WIRED_CP36','actual_utc':datetime.now(timezone.utc).isoformat(),'canonical':entry,
 'canonical_sha256':h(root/entry),'prior_directory':str(hist),
 'files':{str(p.relative_to(root)):{'before_sha256':hashlib.sha256(old[p].encode()).hexdigest(),'after_sha256':h(p)} for p in new},
 'scope':'Single B97 include after B96, required-input addition, and append-only CP36 changes/source-log entries. Existing A4 entries preserved. No updater, report, ledger, bibliography or build edit.'}
(own/'outputs/B97_CP36_wiring.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))

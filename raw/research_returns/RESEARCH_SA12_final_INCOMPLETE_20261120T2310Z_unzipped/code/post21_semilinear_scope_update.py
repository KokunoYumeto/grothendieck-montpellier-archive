"""Record the completed unbounded-field reduction without a new formal review."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
names=['parts/B/post21_research/integration_manifest_B_coherent_root_sectors.json',
       'parts/D/post21_research/integration_manifest_root_projective_semilinear_crowns.json']
verified=[]
for name in names:
 m=json.loads((root/name).read_text());assert hashlib.sha256((root/m['path']).read_bytes()).hexdigest()==m['sha256']
 verified.append(dict(path=m['path'],sha256=m['sha256'],audit_manifest=name))
p=root/'code/output/review15_main_assessment.json';assessment=json.loads(p.read_text())
assessment['assessment_staged_utc']=now
assessment['strict_main_gate_reductions'].append('One strict crown-gate enlargement after review14: the coherent full coefficient-gerbe extension and single-sector compression give q^(A_R t r²) projective semilinear counts with unrestricted tame field-image order, and therefore the stated faithful projective automorphism crowns have uniform multiplicity and generator bounds with only the graph quotient bounded.')
assessment['verified_files']+=verified
for item in assessment['verified_files']:
 m=json.loads((root/item['audit_manifest']).read_text())
 item['sha256']=m['sha256']
 if m.get('typesetting_delta'):item['typesetting_delta']=m['typesetting_delta']
assessment['remaining_strongest_gates'][3]='General monolithic nonabelian crowns outside the proved radially tame one-smooth-exceptional-curve faithful-linear field-permutation and faithful-projective automorphism families. The latter now allow unrestricted diagonal and field-image actions, with a bounded graph quotient and the stated projective embedding/order hypotheses. Wild radial permutation quotients, other outer realizations and other geometries remain unresolved.'
assessment['auxiliary_not_movement'].append('The three coherent-gerbe, single-sector and skew-unit statements are dependencies of the one unbounded-field crown enlargement, not separate movements. The normal-subgroup graph refinement is under separate examination and cannot be counted separately from that same enlargement.')
assessment['report_summary']='Two strongest main gates are strictly smaller after review14: the local unrestricted-period projective count covers SNC exceptional trees, and the one-curve projective crown family permits unbounded tame field-image order. General D.1, D.2(ii) and residual L8 remain open.'
p.write_text(json.dumps(assessment,indent=2)+'\n')
closure=dict(utc=now,earlier_gate_record='parts/D/post21_research/projective_semilinear_equivariant_gerbe_gate_root.json',
 status='Closed in the stated one-curve radial-tame scope',verified_files=verified,
 mechanism='Extend the actual twisted-band gerbe with its Isom torsors and full deck coherence to root_en; choose one spectral sector via a descended Azumaya module; use compressed normal order and only nu=f/a one-step phases; nu*E*v=t*f.',
 remaining='Wild outer quotient covers, other geometries and embeddings outside the stated faithful projective/order and bounded graph hypotheses.')
(root/'parts/D/post21_research/projective_semilinear_gate_closure_root.json').write_text(json.dumps(closure,indent=2)+'\n')

p=root/'code/assemble.py';s=p.read_text()
s=s.replace('The conditional unbounded-field theorem is explicitly conditional.',
            'The bounded-graph theorem is retained in its proved implication form; its counting hypothesis is discharged by the later projective semilinear theorem.')
old="'Unbounded-field projective semilinear descent remains an exact open gate: the actual coefficient gerbe on the field cover must have a coherent extension compatible with the deck and band actions and retain the index-linear weighted budget. An arbitrary extension at the geometric period does not establish that coherence. Root-extension and character-sector compression are under investigation. No new semilinear projective count is claimed from the H2 bound alone.',"
new="'The previously isolated unbounded-field gerbe gate is now closed in the precise one-curve radial-tame scope. Three full proofs extend the actual twisted-band lifting gerbe coherently to the full root, realize every punctured object in one spectral sector through a descended Azumaya algebra, and retain exact skew-Frobenius unit frames with the deck cocycle. The compressed ideal removes all n/m layers. The synthesis uses nu=f/a stages on a degree-ta field cover and the exact identity nu*E*v=t*f, yielding q^(A_R t r²) with no bounded field-image assumption. Its crown consequence discharges the stated bounded-graph reduction. All five units passed four actual-file/source audits. This is one further strict crown-gate enlargement after review14, grouped with its supporting constructions. Wild outer covers, other geometries, residual simple families and full finite generation remain open.',"
assert old in s;s=s.replace(old,new)
s=s.replace('hereditary tree constants, unbounded-field projective descent and full finite generation remain unresolved.',
            'hereditary tree constants and full finite generation remain unresolved. The separate one-curve unbounded-field descent is closed in the next synthesis.')
scope="""semilinear_scope='; the one-curve radial-tame projective hereditary count also holds with arbitrary fixed tame field action, and the stated faithful projective automorphism crowns permit unrestricted field-image order with a bounded graph quotient'
outcomes=[(item,state+semilinear_scope,locator+'; D:tame-projective-semilinear-count; D:tame-projective-automorphism-crowns') if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]
"""
assert "report=['INCOMPLETE'" in s;s=s.replace("report=['INCOMPLETE'",scope+"report=['INCOMPLETE'",1);p.write_text(s)
p=root/'parts/D/unresolved_D.tex'
with p.open('a') as f:f.write(r'''

\paragraph{Coherent unbounded-field descent is now proved in the one-curve scope.}
Lemmas and propositions
\ref{D:coherent-full-root-coefficient-gerbe}--\ref{D:compressed-skew-Frobenius-unit-jets}
extend the actual twisted-band coefficient gerbe with its full deck
coherence, choose one residual sector without losing punctured objects,
and compress the extra root-character layers. Theorem
\ref{D:tame-projective-semilinear-count} consequently proves the
index-linear projective semilinear bound with unrestricted field-image
order. Corollary~\ref{D:tame-projective-automorphism-crowns} removes
that boundedness condition from the stated projective crown family.
This is one further strict reduction after review14. The cover and
field character must still be radially tame over the one-curve
resolution, and the faithful projective embedding, order comparison
and bounded graph hypotheses remain. Wild outer quotient covers,
other exceptional configurations and general finite generation are
not settled by these proofs.
''')
with (root/'PROGRESS_LEDGER.md').open('a') as f:f.write('\n\n## Post-review14 unbounded-field projective crown reduction\n\nINCOMPLETE. '+now+'. Five statements, consisting of three coherent-gerbe/sector/skew inputs and the projective semilinear count with its crown corollary, have all four actual-file audits and are assembled. This is one strict crown-gate enlargement beyond the bounded-field scope already counted at review14. Together with the SNC-tree local projective result, two reductions are staged for the17:10UTC review. No requested row changes. The last completed formal review remains14 with counter0. No archive or formal review is created by this scope record.\n')
print(json.dumps({'utc':now,'staged_review':15,'strict_reductions':len(assessment['strict_main_gate_reductions']),'formal_review_completed':False,'archive_created':False},indent=2))

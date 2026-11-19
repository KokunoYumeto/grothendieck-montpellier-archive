"""Serialize the completed human-readable review and actual check scopes.
No verdict or mathematical conclusion is inferred by this program.
The claim/item rows were manually authored after passage-by-passage reading.
"""
from pathlib import Path
import json,csv,collections,re
R=Path('/workspace/scratch/a77a578fa7d4/SA12_work/reviews/31')
def js(f):return json.loads((R/f).read_text())
items=js('items.json'); claims=js('claims.json'); problems=js('problems.json'); refs=js('reference_verification.json')
events=[]
who='GPT-6 Astra Pro; inherited parent effort (not separately exposed); SA12/review31'
def event(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
for i in items:
 event(i['id'],'used and rechecked in this run','Manually compared source note entry/entries with the actual transcription at '+i['lines']+'. Textual check: '+i['check']+'. '+i['check_reason']+' This is a source comparison, not an ink decision or formal proof certificate.')
for c in claims:
 event(c['id'],'used and rechecked in this run','Actual source passage read at '+c['lines']+'. Compared the written scope with the contemporary statement and opened references '+', '.join(c['refs'])+'. '+c['fate']+' Search requests: '+', '.join(c['query_ids'])+'. This event records source/hypothesis/literature comparison; it does not certify every proof in the cited works.')
for r in refs:
 kind='carried as background without fault found' if r['note']=='unverified' or r['key'] in ['Shatz1966','HigmanBibliography'] else 'used and rechecked in this run'
 event(r['key'],kind,r['verification']+' Exact scope: '+r['locator']+'. Access: '+r['url']+'. Bibliographic verification and verification of a theorem are distinguished here; no general proof certificate is intended.')
proofs=[
 (421,'targeted proof check','module_chain','Computed the nilpotent shift and its colimit; checked Hom-finiteness and the failure of Ext1-finiteness for the historical versus modern cofiniteness definitions.'),
 (423,'independent re-proof',None,'The real closure of Q(t), ordered with t larger than every integer, is orderable of transcendence degree1. Any embedding in R preserves squares and hence its unique order, contradicting the Archimedean property. This refutes the finite-transcendence-degree extension.'),
 (424,'computation or formal certificate','strict_cd_bound','Enumerated squares in F3 and checked the quadratic torsor; the event is a finite computation, not a general formal certificate.'),
 (426,'targeted proof check',None,'For Fp and Fp(t), Artin–Schreier gives cd_p≤1; a nontrivial degree-p constant extension gives cd_p≥1. Thus the unqualified transcendence-additivity statement fails.'),
 (445,'independent re-proof',None,'Integer translation on the simplicial line fixes no vertex, while [0,1] and [1,2] meet. Checked the closed-simplex obstruction and distinguished the valid covering-lift argument.'),
 (446,'independent re-proof','orbit_transfer','Reproved the chain identity p*T=|G| with stabilizer multiplicities; the finite C3 example is only an illustration.'),
 (448,'targeted proof check','relative_corestriction','Checked relative trace one and the endomorphism trace identity phi+sigma phi sigma^-1=id in the faithful C4 setup.'),
 (453,'computation or formal certificate','relative_corestriction','Enumerated Tate H0(H,M), its stable diagonal and corestriction; separately computed Tate H0(G,M). The bijection from stable classes fails although full corestriction is onto.'),
 (456,'computation or formal certificate','semilocal_H1','Exhaustively computed the Artin ring F2[e]/e^3, its units, faithful order2 action, cocycles and coboundaries; checked the unique maximal ideal and trivial residual unit group.'),
 (457,'targeted proof check','semilocal_H1','Checked that the GLn proposal includes n=1, so the explicit unit-group counterexample applies.'),
 (460,'independent re-proof','unit_norm','Reproved surjectivity of the unit norm in C((u))/C((t)), u^2=t, by the recursive formal square-root construction; checked ramification index2.'),
 (464,'independent re-proof','degree1_torsion_cocycle','Checked the quadratic character over C(t), trivial action on all roots of unity, and its becoming a coboundary in Ksep*. Then used the exact sequence to recover precisely degrees≥2 and the degree1 kernel.'),
 (466,'targeted proof check','additive_automorphism','Checked the additive-polynomial automorphism and its inverse. It disproves a GLn description of all automorphisms, not the vector-group classification itself.'),
 (468,'computation or formal certificate','regular_norm','Recomputed the permutation determinant, including the unique C2 exception, and the extra inverse-determinant character repair. Finite enumerations supplement the general cycle-count formula.'),
 (475,'independent re-proof','closed_restriction','Constructed the injective all-functions sheaf on A2; proved the two-curve closed-cover obstruction from incompatible ambient germs, without assuming that restriction to each component is flasque.'),
 (476,'independent re-proof','closed_restriction','Transferred the two-curve H1 obstruction to an irreducible affine plane embedded in A3 using a second graph plane and exact closed pushforward.'),
 (483,'targeted proof check','spectral_degrees','Checked the differential bidegrees and total-degree inequality; p+q is the needed total degree, whereas the written p−q does not support the argument.'),
 (496,'independent re-proof','pointwise_affine_bound','Combined the exact ILO existence theorem and fraction-field bound with SGA4X2.4 to produce an all-noetherian counterexample satisfying invertibility; checked the nonreal clause for ell=2. This uses, but does not independently reprove, the published existence theorem.'),
 (523,'independent re-proof',None,'For an Artin local ring with |G| invertible in the residue field, filter principal units by powers of the nilpotent maximal ideal. Each additive quotient has vanishing positive group cohomology by averaging; the exact sequences give H1 comparison. This is a sufficient tame reconstruction, absent from the page.'),
 (524,'targeted proof check','regular_norm','Checked det(rho direct_sum det(rho)^-1)=1 and that adjoining a character preserves faithfulness. The altered representation dimension is explicit.'),
 (525,'independent re-proof','closed_restriction','On the punctured union of two axes, ambient constant germs0 and1 on the branches cannot extend across their intersection, since nonempty ambient opens in A2 meet.')]
for n,t,k,o in proofs:
 if k:o+=' Saved calculation/proof record: programs/check_calculations.py; outputs/calculations.json#'+k+'.'
 event('CL-SA12-'+str(n),t,o)
for a,b,reason in [(423,422,'finite transcendence degree is insufficient for the whole equivalence list'),(424,497,'strict sign replaced by the established weak upper bound'),(426,426,'prime invertible in the base field is necessary'),(445,444,'use uniqueness of lifts/open-star argument rather than disjoint closed simplices'),(453,452,'relative projectivity does not imply stable-corestriction bijectivity'),(456,523,'unqualified wild residual comparison replaced by a sufficient tame Artin statement'),(457,523,'n=1 already refutes the unrestricted GLn claim'),(460,460,'local-field finite-residue hypotheses restored'),(464,464,'degree1 replaced by a surjection with explicit kernel; isomorphism begins in degree2'),(468,524,'regular representation repaired by one inverse-determinant character'),(496,493,'all-noetherian bound replaced by the applicable excellent strict-local theorem')]:
 event('CL-SA12-'+str(a),'refuted, refined CL-SA12-'+str(b),reason+'. Counterexample/proof and all checked hypotheses are in the cited claim record and its saved calculation where applicable. A refinement with the same id means the corrected statement is in that record; it is not a claim that the manuscript already states the correction.')
with (R/'CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
entries=list(csv.DictReader((R/'entries.tsv').open(),delimiter='\t'))
verdicts=collections.Counter('merged' if x['verdict'].startswith('merged') else x['verdict'] for x in entries)
classes=collections.Counter(x['class'] for x in claims)
audit={'entries':len(entries),'items':len(items),'verdicts':dict(verdicts),'claims':len(claims),'classes':dict(classes),'problems':len(problems),'reading_rows':len(list(csv.DictReader((R/'readings.tsv').open(),delimiter='\t'))),'link_rows':len(list(csv.DictReader((R/'links.tsv').open(),delimiter='\t'))),'references':len(refs),'check_events':len(events),'search_queries':len(js('search_manifest.json')),'all_claims_have_query':all(x.get('query_ids') for x in claims),'all_claim_references_resolve':all(set(c['refs'])<={r['key'] for r in refs} for c in claims),'unique_entry_ids':len({e['entry_id'] for e in entries})==len(entries),'unique_item_ids':len({i['id'] for i in items})==len(items),'unique_claim_ids':len({i['id'] for i in claims})==len(claims)}
assert audit['entries']==118 and audit['all_claims_have_query'] and audit['all_claim_references_resolve']
(R/'outputs/closing_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(audit,ensure_ascii=False))

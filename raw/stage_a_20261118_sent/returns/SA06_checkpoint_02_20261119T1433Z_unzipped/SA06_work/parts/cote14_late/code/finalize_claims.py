"""Recorded human refinements after primary-source matching; run after builders."""
from pathlib import Path
import json,datetime
P=Path(__file__).resolve().parents[1]
items=json.loads((P/'items.json').read_text())
for x in items:
 if x['id']=='SA06-209': x['check']='agrees'
 if x['id']=='SA06-270':
  x['reconstruction']='LM6 A.50 and A.22 are external project links. The retrieved RESULTS_STATE verifies their endpoint labels and returned statuses; its statements are truncated, so no external proof is certified by this part. See contextual_endpoint_audit.md.'
 if x['id']=='SA06-264':
  x['reconstruction']='The external cote16 singular-hypersurface programme is now read at scan47, lines1785–1796 of the combined external transcription. It explicitly asks for reformulation on singular varieties. The present cote14 pages retain regular X,Y and contain no such completed formalism.'
(P/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
claims=json.loads((P/'claims.json').read_text())
for x in claims:
 n=int(x['id'].split('-')[-1])
 if n==209:
  x['class']='B';x['confidence']='medium'
  x['fate']='The statement follows by the independent comparison of Čech complexes under cofinality of covering families and preservation of the relevant fibre products, using the site criterion in SGA4 V Proposition4.3 and Corollary4.5. An exact separately numbered publication of this functor statement was not identified. Continuity alone is insufficient.'
 if n==215:
  x['class']='B'
  x['fate']='Brawley–Gao–Mills (2001), Lemma5, author manuscript pp.3–4, gives the exact degree reduction for associative polynomials over any field. The two-sided unit0 forces b=c=1,d=0 in axy+bx+cy+d. The independent inverse calculation shows that a polynomial antipode exists only for a=0. The sheet stops at Consequently: this last antipode step is the run’s completion. No extension to nonreduced base rings or first-priority claim is made.'
  x['fate_date']='Exact later published counterpart2001; the source refers backwards to1978/1998 treatments, not independently opened. Earlier historical priority remains unassigned.'
  x['refs']=['BrawleyGaoMills2001','MilneAlgebraicGroups2017']
 if n==216:
  x['fate_date']='The letter gives the contemporary1964 context. The exact modern statement was read in Mumford–Oda’s undated penultimate author draft, VIII.1 Theorem1.11; no2015 date is inferred from the stable reference key.'
 if n==250:
  x['statement']='Later restricted answer to the manuscript’s much stronger rational/Albanese equivalence question: for a smooth projective variety over an algebraically closed field, the Albanese map is an isomorphism on torsion in degree-zero CH0. The pages do not separately assert this torsion theorem.'
 if n==254 and 'codimension2' not in x['fate']:
  x['fate']+=' The independent diagram check is for a pencil (j=1) with a regular codimension2 base locus; the general j-labelled diagram requires its omitted dimension and incidence hypotheses.'
  x['confidence']='medium'
 if n==266:
  x['fate']='For ℓ different from char(k), the injective map Tℓ(A)→Tℓ(B) induced by an isogeny u:A→B has cokernel canonically isomorphic to ker(u)(k)[ℓ∞]. Thus integral invertibility is equivalent to ℓ not dividing deg(u). Milne I §7 and Lemma10.16 supply the divisibility statement. This prime-support criterion survives the correction of the minimal denominator in C-SA06-265.'
 if n==270:
  x['fate']='The H¹-inverse requirement is exactly the (1,2n−1) Künneth condition for an integral universal zero-cycle: the induced endomorphism of Alb(X) is the identity by faithful H¹ realization. Voisin (2025), §2 before Lemma2.1 and Theorem1.4, gives a smooth projective complex threefold with representable CH0 and no such cycle. Alexandrou (2026), Theorem1.3, improves this to a surface with Alb(S)=E under the stated End(E) hypotheses. Thus the universal integral assertion is false, even under representability of CH0. A rational universal cycle exists; a rational point of the stated generic symmetric-power fibre remains a sufficient special hypothesis. See the complete integral correspondence proof in computation_notes.md.'
  x['fate_date']='Voisin: first arXiv2025-08-04, revised2025-10-15; journal Algebraic Geometry12(6),888–901(2025), accepted2025-10-10. Alexandrou: v1,2026-02-13; v2,2026-03-08; preprint theorem, no journal publication verified.'
  if 'Alexandrou2026' not in x['refs']:x['refs'].append('Alexandrou2026')
 x['present_status']='As of2026-11-19: '+x['fate']
(P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
with(P/'progress.log').open('a')as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\tPRIMARY_REFINEMENTS_SAVED\tExact source matches, integral counterexamples and bounded claims updated.\n')
print({'items':len(items),'claims':len(claims)})

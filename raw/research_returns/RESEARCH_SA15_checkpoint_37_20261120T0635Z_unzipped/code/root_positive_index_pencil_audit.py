"""Record the completed root proof audit of the determinant-pencil model.

No finite numerical computation is performed or substituted for the proofs.
"""
from pathlib import Path
import csv,datetime,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_positive_index_pencil_audit.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
events=[
 ('lem:DE-A3-positive-pencil-candidate',
  'PASS: whole local proof rederived over possibly nonreduced Cartier D. A unit entry in the rank-one section matrix gives an actual line subbundleR0. Near either disjoint zero scheme the surface ideal(f,w) is a regular sequence, so its remaining equation is a nonzerodivisor onD. ThusR0=O_D(Z0),R0P=O_D(Z1); their squares give a basepoint-free pencilA=R0² of degreeb. The Tor kernel of0->O²->Q->iRs->0 isRs(-D). The actual local row(1,u f²), retaining the unit inP², identifies it withA^-1. Adjunction givesRs=omega_D A^-1. No reducedness or smoothness is assumed.'),
 ('lem:DE-A3-positive-norm-pencil-candidate',
  'PASS: complete norm, quotient and differential proof rederived. The alpha2 local norma²+h b² targetsdet(nu_*J)=L because det(nu_*O)=O. OnR0 it is a section sigma ofL_D A^-1=RsP, and norm(si)=Si givesSi|D=sigma a_i with the Frobenius-twisted sections explicitly retained. Generic norm divisors have no common component, since the two source linear systems are generated andnu is a universal homeomorphism. Therefore sigma avoids every minimal prime of the Cohen-Macaulay Cartier curve and is a nonzerodivisor. Acyclicity ofP givesH0L=H0(omega_DP) and the stated quotient. The formsdlogu glue because transition units square; Cartier fixes them by the local p-basis formula. If their global form vanished, each unit would be a square locally on the smooth normal perfect-base surface, and unique roots trivializeP, impossible. Invariant-form and pencil-ratio claims follow; no nonzero restriction toD is inferred.'),
 ('lem:DE-A3-positive-pencil-contraction-candidate',
  'PASS: entire derived-cohomology and cup-product proof rederived. The alpha2 self-fibre product has trivial square-zero diagonal ideal, so nu*nu_*J filters byJ twice; finite adjunction computesExt(E0,E1) by a bundle filtered byQ twice, hence acyclic. The surface cokernel ofO plusP->E0 isL_D R0^-1; its Ext1-dual isR0P. Tensoring byE1 identifies all cohomology ofG_s=E0_D R0 withE0 plusE1. The inclusionR0->E0_D gives0->A->G_s->L_D->0, whose quotient row is precisely the two Cartier contractions. Thus sharpness givesh0A=h1A=h0Rs=2 and the pencil is the fullH0A. Multiplication by local alpha2 coordinatez sendsr tozr withr wedgezr=normr; the differences of lifts ofsigma a arec_ij a. Therefore the boundary iscup with the actual alpha2 classbeta. The twisted kernel-span to cokernel criterion for first rank=stable rank makesbeta cup an isomorphism. All source and target Frobenius twists are retained.'),
 ('cor:DE-A3-positive-first-rank-candidate',
  'PASS: full etale-base-change argument rederived. Acyclicity survives the double cover because its pushforward is an extension of two copies; the same applies toP and higher cohomology ofEi. The pulled contraction kernel isH0(Dtilde,pi*A). Its trace exact sequence yields dimension2+nullity(alpha cup:H0A->H1A). Since source and target full spaces both have dimension2b, the full first rank is2b-2-nullity. This is kept distinct from the previously proved restricted-image first and stable rank2b-4.'),
 ('rem:DE-A3-positive-norm-pencil-scope-candidate',
  'PASS: complete final scope read. No smoothness ofD, generic pencil separability, Petri identification or variation nonvanishing is asserted. The finite-probe correction is explicit: the weight images of dimensions1 and2 overlap, total dimension2, with an invertible sum of the displayed generators. A uniform lower bound3 is neither proved nor used. The exact open question remains exclusion of a common kernel or common image for the variation on an arbitrary mixed surface.')]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,result in events:wr.writerow([sid,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort','independent re-proof' if not sid.startswith('rem:') else 'targeted proof check',result])
record={'status':'FULL MATHEMATICAL PASS','actual_utc':now,'events':len(events),
        'finite_computation':'None; all four mathematical assertions were checked by full local and cohomological proofs.',
        'source_scope':'Entire preceding toral-bundle and variation-kernel/cokernel proofs reread. Original Edixhoven-van der Geer-Moonen7.19 acyclicity proof previously read in full is reused forP andQ; no new network retrieval or visual source inspection claimed.',
        'remaining_gate':'Actual first-variation/Petri identification and determinant nonvanishing are still open.'}
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))

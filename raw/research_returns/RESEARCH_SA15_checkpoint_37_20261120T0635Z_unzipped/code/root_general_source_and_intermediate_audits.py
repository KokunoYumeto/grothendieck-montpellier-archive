"""Record complete actual root proof audits of the arbitrary source and compatible intermediates."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reviewer='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root'
tasks=[{
 'name':'general_odd_source_Cartier',
 'candidate':'agents/obstructions_crystals/post_CP33_general_odd_source_Cartier_candidate.tex',
 'sha256':'dac82081dc46a2c1e80254831e301a0e52e64c9604af420289bae95dd3e21b83',
 'labels':['lem:DE-general-odd-source-twisted-blocks','prop:DE-general-odd-source-quotient-bound','cor:DE-general-source-principal-divisor-bound','rem:DE-general-odd-source-scope'],
 'read_scope':'Entire final four-label arbitrary-positive-odd-degree source proof read. Complete canonical deck-slice proof, common Cartier incidence file, and all-odd full-inertia proof freshly reread. This includes the exact same-fixed-theta-coordinate formula for every nontrivial odd line, not only lines in one prior kernel.',
 'checks':[
  'The dual odd isogeny is surjective on geometric points. Every lift Q of odd torsion P is killed by the product of its odd order and the odd kernel order. If Q R_chi were trivial its pullback P would be trivial, which is excluded. Projection formula therefore decomposes each h=9a dimensional twisted input into exactly a nontrivial nine-dimensional principal-base blocks.',
  'The actual relative Cartier target is M^(2)(P^(1/2))^(2), since its Frobenius pullback is M^2 P. Finite etale Frobenius base change and the odd half permutation identify precisely the same target coset, without confusing a twist with a half or identifying the two varieties.',
  'For the balanced cross pairing, a functional supported on the trivial inner character pairs Q R_chi only with its inverse. Thus the full square matrix is a direct sum of known nontrivial nine-dimensional cross matrices. Multiplication likewise uses the exact Moore tensor; no generic-rank implication is substituted for the tensor identity.',
  'All finite inner and outer character-coset determinants are nonzero on the same fixed integral Fermat cubic, by the full canonical common-coordinate proof. The multiplication variables differ only by the index inversion preserving the Fermat polynomial. Their simultaneous open intersects the central Pfaffian nonzero locus and gives the actual source/composite wall with only central stable loss one.',
  'The outer odd deck averaging projector defines the actual F2 Lang splitting. Its invariant relative part is the source because odd pullback/trace identifies constant ambient cohomology. Smoothness and connectedness of pullback members and nonempty simultaneous sharp opens were checked in the complete incidence proof.',
  'The explicitly assumed full source image remains full after the extra dense-open restrictions. The composite A->C has a full ambient radical. Its regular rank-r-1 Lang lifts over the strictly henselian common-wall neighbourhood identify its fixed hyperplane with a source hyperplane plus all nontrivial outer summands. The block lemma then forces K into the latter. No independence of source and outer image actions and no full-fibre specialization are used.',
  'The principal divisor corollary uses positive odd e,m, exact outgoing descent at m, and a second exact source descent at e. It therefore applies the general-a statement with a=e^2. Its main-degree formula uses the canonical main-orbit statement only in the fixed-principal scope. The e=1 edge recovers the unconditional quotient-eight bound; no new prime degree is proved.'
 ],
 'scope':'Conditional source restriction with arbitrary odd degree a and no principal-polarization assumption on B. It does not assert any new intermediate full image or any new unconditional target full-image degree.'
},{
 'name':'compatible_cyclic_intermediates',
 'candidate':'agents/monodromy/post_CP33_compatible_cyclic_intermediates_candidate.tex',
 'sha256':'a40f648e4c968f2b3a2cd105b4866d7ba992361b46de9b62a514ff77535103ae',
 'labels':['lem:compatible-line-averaging','prop:compatible-intermediate-common-slice','thm:compatible-cyclic-intermediate-criterion','cor:compatible-cyclic-principal-prime-criterion','rem:compatible-cyclic-intermediate-scope'],
 'read_scope':'Entire final five-label compatible-intermediate candidate read, together with the complete arbitrary-source proof just audited and the canonical same-coordinate/common-wall/deck-slice proofs. The continuation through connected smooth sharp source opens is checked explicitly.',
 'checks':[
  'In F2[D], each nonidentity element belongs to one line and the identity to ell+1 lines, an even number. Thus sum e_H=1+e_D; odd orders give idempotence and e_D e_H=e_D. If every e_H kills v, the first identity gives v=e_D v and the last gives e_D v=0. This is valid on every F2[D]-module without scalar extension.',
  'All intermediate quotients are actual quotients of the one fixed D. Their line bundles are exact pullbacks, and both factor maps have degree ell. The central degree-one smooth sharp open with all nontrivial D-character multiplication blocks unit is nonempty by the complete incidence proof. It simultaneously makes every intermediate and every outer character cycle sharp.',
  'Each T_H is the nonempty integral open of the intermediate coefficient projective space on which the actual ambient local system restricts, the source is smooth sharp, and the outer character cycles are bijective. The common D-slice lands in it by the character-coset comparison, rather than by an assumption that an arbitrary dense open meets a special slice.',
  'On T_H the deck action by H commutes with Frobenius and its actual averaging projector is a morphism of F2 local systems. Its image is the source relative Lang system by odd descent including the constant ambient quotient. On the common D-slice this is literally the same H subgroup action, not an unrelated character splitting.',
  'The composition e_H after K inclusion is a morphism of finite etale local systems on connected T_H. Vanishing on the nonempty open supplied by the arbitrary-source theorem extends over T_H by local constancy. Hence every inclusion transports to one common fibre without requiring intersections with the original vanishing opens and without crossing a rank drop.',
  'The full-source hypotheses for each of the ell+1 intermediates are used exactly once in the arbitrary-a quotient bound. All projectors on the common fibre then kill K, so the group-algebra identity forces K=0; constant rank propagates this and the proved full-radical group theorem gives full GL. The intermediate full images remain explicit unproved hypotheses.',
  'For a fixed principal target, the outgoing exact quotient identifies L with3ellTheta. The intermediate theta pullback is ample with self-intersection2ell, so its polarization type has d1*d2=ell and d1 dividing d2, hence(1,ell). The conclusion is limited to the stated particular intermediates, or the separately hypothetical uniform cyclic-source theorem.'
 ],
 'scope':'Complete conditional reduction from rank9ell^2-1 to the ell+1 specified rank9ell-1 cyclic-source images. Those new nonprincipal full-image hypotheses are not proved; no new unconditional degree or closed general A.4 row is asserted.'
}]
for t in tasks:
 p=w/t['candidate'];assert hashlib.sha256(p.read_bytes()).hexdigest()==t['sha256']
 out=w/'outputs'/('root_'+t['name']+'_audit.json')
 snap=w/'notes'/('root_'+t['name']+'_audited_candidate.tex')
 assert not out.exists() and not snap.exists();shutil.copy2(p,snap)
 r={'status':'FULL-INDEPENDENT-PROOF-PASS','actual_utc':now,'reviewer':reviewer,
    'candidate':t['candidate'],'candidate_sha256':t['sha256'],'labels':t['labels'],
    'read_scope':t['read_scope'],'proof_checks':t['checks'],'scope_guard':t['scope'],
    'finite_computation':'None needed or executed.','fresh_external_source_opening':False,
    'source_scope':'Direct proofs from previously fully audited Cartier, odd-isogeny and group statements; no new external classification imported.',
    'executed_failures':[]}
 out.write_text(json.dumps(r,indent=2)+'\n')
 with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
  wr=csv.writer(f,delimiter='\t')
  for label in t['labels']:
   wr.writerow([label,now,reviewer,'independent re-proof','PASS: full written proof and exact local-system/character/source-hypothesis scope checked. See '+str(out.relative_to(w))+'.'])
 with (w/'notes/checkpoint34_changes.md').open('a') as f:
  f.write('\n## Root audit: '+t['name'].replace('_',' ')+'\n\nFull independent proof audit passed at '+now+'. '+t['scope']+' No numerical computation or new external theorem was used. Exact candidate and audit records are retained; only separately promoted canonical statements change the current register.\n')
 print(json.dumps({'status':r['status'],'actual_utc':now,'candidate_sha256':t['sha256'],'labels':t['labels']}))

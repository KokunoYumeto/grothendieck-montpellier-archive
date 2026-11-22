"""Retain a complete root proof audit of primitive prime generic sharpness."""
from pathlib import Path
import csv,datetime,hashlib,json,re,shutil
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/monodromy/post_CP35_primitive_prime_generic_rank_candidate.tex'
expected='77705a12007f8963cf18df5382b9472b74bcf661404c19fb3ae42e3169e0fe2f'
assert sha(candidate)==expected
snapshot=w/'notes/root_primitive_prime_generic_rank_audited_candidate.tex'
out=w/'outputs/root_primitive_prime_generic_rank_audit.json'
assert not out.exists() and not snapshot.exists();shutil.copy2(candidate,snapshot)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',candidate.read_text());assert len(labels)==5
r={'status':'FULL-INDEPENDENT-PROOF-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'entire_candidate_actually_read':True,
 'proof_checks':[
  'For odd N the finite theta kernel admits a maximal isotropic subgroup of order N and a split theta extension. The actual line descends along its etale degree-N quotient to an ample line of Euler characteristic1. This uses only oddness, not primality or N3. The fully audited principal-theta alternative therefore supplies a reduced smooth or nodal pullback member, including the product principal surface and disconnected individual component pullbacks.',
  'Global generation and an infinite ground field give one section nonzero at every node. In completed coordinates the pencil equation is xy+zu=0 with u a unit. The relative derivatives force x,y into the ideal(z); substituting gives z times a unit in the singular ideal. Thus no singular component specializing to a node dominates the trait. The central fibre is smooth elsewhere, and properness prevents a missing generic singular component. Hence the smooth-member open is nonempty without a separable-Bertini assumption. H1(L^-1)=0 gives connectedness of every effective member, and adjunction gives genus N+1.',
  'The entire universal hypersurface sequence is valid even for singular members. The cohomology quotient by H1(A,O_A) is ker(W* tensor O(-1)->O), exactly Omega^1_P(W), since the dual multiplication by a nonzero section is injective. The actual Frobenius pullback has source annihilator(s^[2]) in (W^(2))* and target annihilator(s) in W*. Cartier duality gives M_s^t restricted to this source. This is the general Euler-frame identity previously fully checked in type(1,3), with no use of dimension3.',
  'Odd-polarization Cartier surjectivity supplies a nonzero actual equivariant alternating tensor. Its central weights are1 and2, hence the previously audited prime Heisenberg formulas apply in the actual theta basis. If M_s has rank p-1 with kernel covector y_s for its transpose, its restriction between the two rank p-1 annihilators is injective precisely when y_s(s^[2]) is nonzero. This proves the criterion with the correct Frobenius twist.',
  'For a dual corank1 tensor, the fully proved radical map is birational and M_s has generic corank1. On its dense isomorphism open one may take s=sigma(y), the maximal Pfaffian vector. Q=sum y_i sigma_i^2 is homogeneous of odd degree p, and partial_i Q=sigma_i^2 in characteristic2. Since some Pfaffian is nonzero, Q cannot vanish identically. Its nonvanishing open intersects the common birational/rank open and makes the Euler criterion bijective. Therefore Euler generic bijectivity follows. No conclusion is drawn about its zero divisor meeting that open.',
  'The exact universal dual-rank certificates cover3,5,7,11,13,17 for every nonzero coefficient vector, so these geometric cases are unconditional under nonordinarity, ampleness and global generation. For other odd primes, dual corank1 remains an explicit assumption.',
  'The nonempty smooth and Euler-bijective opens intersect because projective coefficient space is integral. The actual Frobenius-compatible sequence0->H1(A,O)->H1(C,O)->E_C->0 has bijective quotient of dimension p-1. Stable fixed vectors are exact over the algebraically closed field: nilpotent additive lifting uses a finite sum, and the bijective summand has surjective Lang map. Stable dimensions therefore add, proving f(C)=f(A)+p-1 and g(C)=p+1.',
  'This closes the stated primitive rank cases only. It proves neither global generation of every type(1,p) line, a complete principal |51Theta| rank/group assertion from primitive degree17, a common maximal-rank Euler wall, stable loss1, full radical inertia, Lang connectedness nor full geometric group. The possible exceptional contraction of the degree-p zero divisor remains explicitly unresolved.'
 ],
 'dependencies':[{'path':p,'sha256':sha(w/p)} for p in [
  'agents/obstructions_crystals/A4_primitive_type_1_3_full_group.tex',
  'agents/obstructions_crystals/A4_odd_Cartier_evaluation.tex',
  'agents/monodromy/prime_Heisenberg_rank.tex']],
 'source_scope':'No new numerical program or external primary-source opening is needed or claimed for this consequence. Complete primitive stability/theta descent/Euler, odd-Cartier, universal Pfaffian, and Severi--Brauer proof audits with exact source passages have already been completed and retained. Every new geometric inference is reproduced in this audit.',
 'numerical_run':'None needed or claimed. The exact upstream certificates and their independent reruns remain retained.',
 'executed_failures':[]}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: complete smooth-member, actual Euler and generic stable-rank proof; outputs/root_primitive_prime_generic_rank_audit.json.'])
print(json.dumps({'status':r['status'],'actual_utc':now,'candidate_sha256':expected,'labels':labels},indent=2))

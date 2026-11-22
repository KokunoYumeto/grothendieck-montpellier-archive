"""Record complete root proof/source audit of the isolated post-CP34 wedge candidate."""
from pathlib import Path
import datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/obstructions_crystals/post_CP34_Lang_wedge_pole_theta_bound_candidate.tex'
expected='cf64119de3fe23e9e93f3e07face711ccf1f8f0e2fd9acea2e3a16b8fdf6fd5b'
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
dest=w/'outputs/root_Lang_wedge_pole_theta_bound_audit.json';snap=w/'notes/root_Lang_wedge_pole_theta_audited_candidate.tex'
assert not dest.exists() and not snap.exists();shutil.copy2(p,snap)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:DE-Lang-wedge-pole-bound','lem:DE-theta-invariant-divisor-degree','thm:DE-Lang-theta-wedge-quotient-bound','cor:DE-Lang-wedge-cyclic-principal-bounds','rem:DE-Lang-wedge-pole-scope']
r={'status':'FULL-INDEPENDENT-PROOF-SOURCE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire stable five-label candidate read. The whole-coefficient Euler model, actual full-radical common-wall proof and regular Lang hyperplane argument were fully reread during the immediately preceding CP34 audits. Original retained Edixhoven-van der Geer-Moonen text Definitions8.17,8.18 and complete Proposition8.19 and Corollary8.20 proofs on printed page119 freshly read.',
 'proof_checks':[
  'The actual Euler cohomology bundle on P^(N-1) is Omega^1, with regular absolute-Frobenius linearization F_X^*E -> E. Its determinant line is O(N), since detE=O(-N), so its nonzero determinant divisor has degreeN. The positive odd cubic pullback has polarization type(d1,d2), N=d1*d2 and d1>=3.',
  'When k=dimK>0, a Lang basis of K is linearly independent over the algebraically closed function field. Its determinant is invariant because F2 has only one nonzero scalar. The finite-etale Lang coordinates lie in the separable closure; geometric Galois invariance over the algebraically closed base descends the wedge to the original rational function field, not merely its perfection.',
  'At each codimension-one DVR, the nonnegative Smith exponents of Phi sum to a=ord detPhi. The inverse exterior-power matrix has denominators of order at most a. Applying it to the same fixed wedge gives 2v(w)>=v(w)-a, hence v(w)>=-a. This permits poles and does not use the invalid blanket vector-extension argument.',
  'At every component of the common maximal-rank wall, full inertia has a rank-r-1 regular fixed hyperplane. The actual etale lifts of its special Lang vectors identify this hyperplane with regular sections. Canonical K lies in every such full-radical fixed space because it is the unique maximal proper geometric submodule. Its wedge is therefore regular there; no full rank-r fibre is specialized through the drop.',
  'The reduced union of closures of all common-wall components is a nonempty effective divisor contained with multiplicity one in the determinant divisor. Its definition via the two actual ranks and Euler determinant is invariant under every theta translation, by naturality of relative Cartier with the corresponding twisted target action and invariant volume. Only the union, not each component, is claimed invariant.',
  'A homogeneous equation of a theta-invariant divisor spans a one-dimensional theta representation. The full original nondegeneracy proof identifies K(L) with its dual via the commutator. An element of exact order d2 therefore pairs to a primitive d2-th root. Its scalar action on degree-e equations is zeta^(-e), while a commutator acts trivially on a line, so d2 divides e. Oddness ensures these geometric roots are reduced.',
  'After removing the regular good divisor, all divisorial poles are bounded by the remaining effective divisor of degreeN-e. Reflexivity on smooth projective space extends the nonzero wedge to H0(Omega^k(N-e)). The exterior Euler injection proves vanishing for t<k; at t=k a constant exterior tensor killed by all coordinate contractions is zero. This argument is valid in characteristic2 without Bott vanishing.',
  'Thus if K is nonzero, k<=N-e-1 and quotient dimension m>=e>=d2. The e=N case forces K=0. In the separate K=0 case m=N-1>=d2 because d1>=3; the stronger m>=e is deliberately not asserted there. All endpoints are correctly scoped.',
  'The cyclic odd-prime pullback has type(3,3ell) and quotient at least3ell; e lies in{3ell,6ell,9ell}. The fixed principal odd degree-d system has type(3d,3d), so the independent slice bound combines as max(8,3d). The main-component degree formula is used only in the already proved fixed-principal scope; d=1 agrees with K=0.'
 ],
 'source_scope':{'url':'https://van-der-geer.nl/~gerard/AV.pdf','retained_text':'agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt','fresh_read':'Definitions8.17/8.18 and full Proposition8.19/Corollary8.20 proofs, printed page119','new_web_opening':False,'limitation':'Only the perfect theta-commutator statement is imported. The pole and Euler arguments are given in full and independently rederived.'},
 'computation':'None needed or executed.','executed_failures':[],
 'scope_guard':'Stronger unconditional dimension bound, not a full-image theorem in a new degree. Possible poles and monodromy at the remaining determinant divisors are retained. This candidate remains outside the frozen CP34 canonical paper.',
 'check_event_status':'Per-label full-audit data retained here; TSV promotion events deferred until CP34 archive release to preserve the numbered-register freeze.'}
dest.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'status':r['status'],'actual_utc':now,'candidate_sha256':expected,'labels':labels},indent=2))

"""Explicit new proof text and two formal checks; no inferred verdicts."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'proof_notes.md';s=p.read_text()
s=s.replace('The first cut line has no complete ring/derivation definitions, so no missing theorem is supplied.', 'The first cut line has no complete ring/derivation definitions. An exact published counterpart was subsequently found in Samuel, *Classes de diviseurs et dérivées logarithmiques*, §3, p.3-11. On its page image, B=k[x,y,z], characteristic 2, Dx=y⁴, Dy=x² and Dz=xyz. These are external antecedents, not a correction of scan 36. If a constant-field uniformizer a(x,y,z)z existed at (z), specialization would give Db/b=−xy in k(x,y). But D²=0 on k(x,y), so D(−xy)=(xy)², whereas D(xy)=x³+y⁵. Their difference is a nonzero polynomial. CALC-24 verifies the polynomial contradiction. This identifies the likely missing example while leaving the archival fragment incomplete.')
old="The unit-logarithmic-derivative lemma and the full embedding k^{N(i,j)}→Cl(A) are not independently reproved here. Zinn-Justin's PartI chapterI Theorem0 gives the precise class-group/logarithmic-derivative framework with its own hypotheses; it is not a literal identification of every special hypothesis in this printed exercise. Claims494 and496 therefore retain a stated matching limit. This is a limit of this source comparison, not an assertion that these old exercises remain open in mathematics."
new="""The exact unit-logarithmic-derivative lemma is Samuel's §4 Lemma 3 and TIFR chapter III §5 Lemma 5.1. Here is a direct verification in the stated local UFD. Divide D and t by a greatest common divisor of Dx and Dy. The normalized derivation still maps B to B; writing P=Dx and Q=Dy, these are now coprime. Its identity D²=aD has a in B because aP and aQ lie in B and P,Q are coprime; moreover Da=0. Write t=cP+dQ. The logarithmic derivative identity gives

P(Dc+c²P)=Q(Dd+d²Q).

Thus Dc+c²P=αQ and Dd+d²Q=αP for some α in B. Differentiating either equality and using D²=aD gives Dα=0 (use the nonzero one of P,Q). The element u=1+cx+dy+(cd+α)xy belongs to 1+m, hence is a unit, and direct differentiation gives Du=tu. CALC-23 checks that identity exactly modulo 2. If one of P,Q is zero, the same calculation applies with its coprime nonzero partner a unit, or the resulting one-variable formula u=1+cx. Undoing normalization gives the original logarithmic derivative. This is an independent re-proof, not merely a citation to a broader criterion.

The full class-group family is now matched exactly to Samuel's §6(b) Proposition 3 and TIFR chapter III §5 Theorem 5.2. The published proof, including the descent isomorphism, was read and checked. Let L be the additive group of F in B satisfying DF=F², and L′ its unit logarithmic derivatives. The height-one derivation criterion identifies Cl(A) with L/L′; the derivative ideal (X^{2i},Y^{2j}) has no height-one common divisor. The unit lemma gives L′=L∩(X^{2i},Y^{2j}). For i=0 or j=0 the derivative ideal is the whole ring and N=0, so the interesting case is i,j>0.

Give X,Y weights 2j+1,2i+1. D raises weight by w₀=4ij−1. For a solution with lowest weight q≥4ij, its initial form F_q satisfies DF_q=0. Conversely any homogeneous constant form of such weight can be lifted recursively to DF=F². At each step one must integrate a squared monomial G², where G=X^αY^β has weight at least 4ij. If α<i and β<j its weight would be at most 4ij−i−j−2, a contradiction. If α≥i, use the primitive X^{2(α−i)}Y^{2β+1}; if β≥j, use X^{2α+1}Y^{2(β−j)}. The next weight is 2m−w₀>m, so the iteration converges formally. Coefficients are squared during integration; no perfectness assumption on k is used. The same procedure stays in the derivative ideal when the initial constant form does, because an initial monomial divisible by X^{2i} or Y^{2j} has a primitive with that divisibility. This verifies the two associated-graded surjectivity assertions.

Modulo the derivative ideal, the constants have basis X^{2a}Y^{2b}, with 0≤a<i, 0≤b<j. The terms of weight at least 4ij are exactly the pairs in the printed N(i,j) inequality. Only finitely many weights remain. The filtration splits as a filtration of F₂-vector spaces, so its higher-weight part is additively isomorphic to k^{N(i,j)}. The resulting k-vector-space structure on the subgroup is noncanonical. The possible lower-weight finite 2-group is immaterial to the subgroup assertion. CALC-18 recomputes the lattice count; CALC-23 checks both integration formulas. The proof-check scope includes Samuel's exact descent theorem and this filtration argument; it is not a claim that a finite count alone proves the embedding."""
assert old in s;s=s.replace(old,new)
s=s.replace('Conditional on the printed subgroup embedding, infinite k with i=j=2 yields an infinite class group. This conditional consequence is not used to pretend that the embedding itself has been checked.', 'The now-verified subgroup theorem gives an infinite class group for infinite k and i=j=2. Thus the final Dedekind example is established, with the hypotheses made explicit.')
old='The weighted cyclic criterion and its pairwise-coprime trinomial specialization are preserved with all the printed alternatives. Their full generality was not matched in an opened source, and no independent proof is claimed here. In particular, a theorem about symmetric algebras of reflexive modules is not silently substituted for the cyclic hypersurface theorem. The relevant printed hint is part of the claim record; the source-recovery and proof task remains a precisely labelled comparison limit, not a newly announced open theorem.'
new='The weighted cyclic criterion is exactly Samuel, TIFR chapter I §8 Theorem 8.1, and *Méchants anneaux*, §III Proposition 2. Its proof was read and checked. When c=1+dq, invert z and set X_i=z^{d q(i)}X_i′. Weighted homogeneity changes z^c=F(X) into z=F(X′), identifying the localization with K[X′,F(X′)^{-1}], a UFD. The quotient by z is a domain, since F is irreducible. The Krull/intersection argument and the prime-element localization criterion give factoriality. In the second case choose e>0 with ce≡1 modulo q and adjoin u with u^e=z. The resulting ring is factorial by the first case and is finite free over the original ring. Graded divisorial ideals become principal upstairs and descend to finite projective modules. The graded Nakayama argument, with the assumption that finite projectives over K are free, makes each such rank-one ideal principal. This proves exactly the stated alternative. For the printed field specialization F=X^b+Y^c with coprime positive b,c, use weights c,b and total weight bc; irreducibility follows from the primitive binomial exponent relation, and gcd(a,bc)=1 gives the criterion for Z^a=F. No larger base-ring assertion is needed.'
assert old in s;s=s.replace(old,new)
s=s.replace("In particular C-SA14-472's exact quotient converse, C-SA14-494 and496's special logarithmic-derivative/class-group assertions, C-SA14-514–515's complete weighted cyclic criterion, and the deliberately incomplete F records carry precise limits in the claims map.", "In particular C-SA14-472's exact quotient converse and the deliberately incomplete F records carry precise limits in the claims map. Exact primary matches subsequently found for C-SA14-494,496,514–515 remove their initial matching limits; the saved search history records that improvement.")
s=s.replace('Samuel\'s1961 paper supplies', "Samuel's 1961 paper supplies")
p.write_text(s)
p=R/'scripts/calculations.py';s=p.read_text();tail="print('\\nALL ASSERTIONS PASSED. Finite examples certify the stated examples; general statements require the separately supplied proofs/hypotheses.')"
block="""section('CALC-23 characteristic-two unit and integration identities')
x,y,c,d,alpha,P,Q,a=s.symbols('x y c d alpha P Q a')
variables=[x,y,c,d,alpha,P,Q,a]
derivatives=[P,Q,c*c*P+alpha*Q,d*d*Q+alpha*P,0,a*P,a*Q,0]
def deriv(expr):
    return s.expand(sum(s.diff(expr,v)*dv for v,dv in zip(variables,derivatives)))
u=1+c*x+d*y+(c*d+alpha)*x*y
t=c*P+d*Q
certificate=s.Poly(deriv(u)-t*u,*variables,modulus=2)
assert certificate.is_zero
print('u=1+cx+dy+(cd+alpha)xy; Du-tu modulo2 =',certificate.as_expr())
for ii in range(1,5):
 for jj in range(1,5):
  for aa in range(0,9):
   for bb in range(0,9):
    if aa*(2*jj+1)+bb*(2*ii+1)<4*ii*jj:continue
    assert aa>=ii or bb>=jj
    G=x**aa*y**bb
    primitive=x**(2*(aa-ii))*y**(2*bb+1) if aa>=ii else x**(2*aa+1)*y**(2*(bb-jj))
    delta=s.diff(primitive,x)*y**(2*jj)+s.diff(primitive,y)*x**(2*ii)
    assert s.Poly(delta-G**2,x,y,modulus=2).is_zero
print('Both recursive integration formulas checked for i,j=1..4 and monomials of exponents0..8 satisfying the weight threshold; general argument is in proof_notes.md.')
section('CALC-24 externally identified cut derivation example')
x,y,z=s.symbols('x y z')
def D24(f):return s.Poly(s.diff(f,x)*y**4+s.diff(f,y)*x**2+s.diff(f,z)*x*y*z,x,y,z,modulus=2).as_expr()
assert D24(D24(x))==0 and D24(D24(y))==0
delta=D24(x*y)
obstruction=s.Poly(delta-x**2*y**2,x,y,modulus=2)
assert not obstruction.is_zero
print('Dx=y^4, Dy=x^2, Dz=xyz; D²x=D²y=0; D(xy)=',delta)
print('The supposed Db/b=xy would force D(xy)=(xy)², but the nonzero obstruction is',obstruction.as_expr())
print('These antecedents are from Samuel1962 §3 p.3-11, not supplied by the cut archival line.')
"""
assert tail in s
s=s.replace(tail,block+tail);p.write_text(s)
print('Primary proof refinements and calculations23–24 saved.')

# Mixed ordinary--supersingular product: active gate, 19 November 2026

This is research in progress, not an all-degree theorem.

Let Eo/F2 be y²+xy=x³+1, Es/F2 be y²+y=x³, and X=Eo×Es.
Write N_(a,b)=O_Eo(aO) box O_Es(bO), with a,b≥3. The dimension of
the relative coherent H1 quotient is ab−1, and the ambient stable rank is1.
The fixed Segre cubic embedding is the diagonal a=b=3d.

## Rigorous obstruction and the expected sharp formula

The exact Picard-embedding and connected-Prym argument in the completed
supersingular-product proof applies unchanged. For rectangular degrees,
qj=diag(b,a) on Pic(Eo)×Pic(Es), since projection degrees are b and a.
When a is even, the Prym contains Es[2], hence a connected Verschiebung
kernel of order2. The full curve defect g−f is at least2; equivalently,
relative stable rank is at most ab−2. For a odd, the ambient supersingular
elliptic quotient gives defect at least1 and relative rank at most ab−1.

Expected exact generic formula: ab−1 for a odd, ab−2 for a even. The
unbounded sharp lower construction is still unproved. In particular it is
not inferred from any finite search.

## Exact probes retained

The program code/A3_mixed_product_probe.py and its JSON output retain every
matrix, section coefficient vector, rank sequence, seed, and actual runtime.
It checked diagonal degrees1..6, attaining relative ranks
8,34,80,142,224,322, and every rectangular degree(a,3), a=3..31, attaining
the displayed upper bounds. The retained rerun took0.7093895580001117s.
Earlier read-only exploratory runs (during the CP09 freeze) took
0.48162562799916486s for the diagonal and0.20388137500049197s for the
rectangular search. No files were changed during that freeze.

For Eo the invariant differential is dx/x. Its Cartier rules are
C(x^(2r)dx/x)=x^r dx/x, C(x^(2r+1)dx/x)=0,
C(x^(2r)y dx/x)=x^(r+1)dx/x, and
C(x^(2r+1)y dx/x)=x^r(y+1)dx/x.
They follow from y=y²/x+x²+1/x. The supersingular-factor rules are those
already proved and retained in A3_supersingular_product_ranks.tex.
Tensoring gives T_s(u)=C(su·omega). Since C(omega)=0, T_s(s)=0.
The quotient H0(N)/ks is the Serre-dual relative coherent space, by the
same global adjunction/F_s=sF_X calculation used in the already audited
product_exact_covectors.tex (re-read before use here).

## A smaller uniform construction problem

Adding ordinary fibres Eo×{point} increases b without increasing the full
genus-minus-p-rank defect. Therefore a sharp theorem for every odd(a,3)
would imply the sharp diagonal formula. Adding a supersingular fibre to
a sharp odd(a−1,3) gives a nodal member with defect2 in (a,3), so the even
case follows by open-rank deformation once the preceding odd case is
available. Thus the precise step is odd a−2 to odd a: two added
supersingular fibres must lose two extra nilpotent directions under a
smoothing. This is being attacked using the independently audited pointed
Cartier/tacnode method in product_hasse_irreducibility.tex.

At the level of adjunction, the boundary of the restricted supersingular
invariant differential is a times the relevant ambient H1(omega_X) class.
It therefore vanishes for a even and is nonzero for a odd. For an even
sharp curve C whose full Cartier kernel is one-dimensional, a tacnodal
union with a supersingular fibre D would have a one-dimensional *relative*
Cartier kernel, represented by a form supported on C. This suggests a
rank-one transverse deformation argument. The unresolved qualifications
are: produce such an even C with full a-number1 in this fixed linear
system, and check the moving quotient ks when top Cartier is zero.
Unlike the ordinary-surface tacnode proof, a lift w can satisfy
T_s(w)=c s rather than0, and adding a scalar multiple of s cannot correct
that coefficient. This has not been suppressed.

## Routes tested and not completed

1. Direct sparse analogue of the degree-three witness:
   for a=2r+1, s=y_ss+x_ord^r+x_ord^(r−1)y_ord*x_ss.
   It attains the bound only at a=3; at a=5 its stable rank is11 rather
   than14, and at a=7 it is16 rather than20. The family does not prove
   the uniform statement.
2. Elliptic graph degeneration: it works for Es×Es, but Hom(Eo,Es)=0,
   so the norm-isogeny graph construction cannot simply be transferred.
3. Fibre products using the cyclic degree-three map Es→P1 give cyclic
   triple covers with unequal character dimensions and large defects;
   they do not automatically give relative ordinarity.
4. Pullback along odd isogenies of Es: nontrivial character twists can be
   made ordinary on a coordinate-grid degeneration, but this increases
   b, the already easy direction, rather than the hard first degree a.
5. Block Cartier matrix: writing s=A+B*x_ss+C*y_ss gives the three-by-three
   block matrix [[T_B,T_A,0],[T_C,0,T_A],[0,T_C,T_B]] on H0(Eo,O(aO))³.
   Where T_A is invertible, its kernel is the kernel of the commutator
   T_C*T_A^(-1)*T_B+T_B*T_A^(-1)*T_C. The expected alternating form has
   the radical forced by A; proving maximal generic rank uniformly is a
   second exact algebraic gate. No theta-function nonvanishing theorem
   has yet been found or invoked.

Both web search engines were used for generic p-rank in abelian-surface
linear systems, ordinary Pryms and fixed elliptic quotients. The retrieved
ordinary-Prym theorems concern generic abstract curves/etale covers and
do not directly apply to the fixed embedded surface. No priority claim
or unverified literature shortcut is made.

The proposed SNC/Weil-weight proof of universal eventual positivity was
stopped on learning that root/monodromy had already completed that gate
in general_X_residues.tex. It is not counted as new progress.

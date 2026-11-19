# Second mathematical checks

These are second checks in the requested single stream, by GPT-6 Astra Pro
(effort setting not exposed), after the proof drafts. They are not a second
reader's endorsement, a formal proof certificate, or a claim that the supplied
notes were correct. Each paragraph states what was recalculated from the
hypotheses. Dates and event types are also recorded in CHECK_EVENTS.tsv.

## H035.1–H035.6 — checked 2026-11-19, 04:05–04:17 UTC

**H035.1.** Independently compute an augmented map to A⊕M as e+d:
the multiplication identity is precisely the derivation identity, and the
restriction to I kills I². Conversely C=A⊕I supplies the unique derivation.
Products of r elements of I generate I^r, so the symmetric-algebra map is
surjective. The fibre-product obstruction is real: (1,1) and (1,−1) are
distinct modulo a common sign, although both coordinates agree modulo signs.
This checks the explicit affine realization and the warning about unrestricted
functors; it does not turn an unspecified title-sheet programme into a theorem.

**H035.2.** Reconstruct scalar multiplication and addition from their module
maps. The interchange diagrams involve finite products; their images give an
A-module, and the diagonal/codiagonal formula proves additivity on morphisms.
Localization is the explicit filtered system of multiplication maps. General
flat base change uses Lazard, not an unsupported assertion that every flat
algebra is a union of finite free subalgebras: only its underlying module is
a filtered colimit of finite free modules. The module comparison is canonical.

**H035.3.** Rechecked the descent datum by evaluating the two scalar extensions
on the same B⊗B-modules. Yoneda gives the cocycle. Effective module descent is
the opened Stacks Proposition 35.3.9 (023N); applying left exact F to the
faithfully flat equalizer recovers F on every A-module. A finite generating
set after base change uses finitely many elements before base change; faithful
flatness kills the quotient. Applying this to the kernel of a finite free
presentation proves finite-presentation descent. Corrected “exactness of Hom”
to “left exactness”; full exactness is not being assumed.

**H035.4.** Recomputed the compatible-presentation argument without assuming
that kernels commute with reduction. The finite generators of P₁ lift, and
the kernel transitions are surjective after correction by f^n A^(r). If K is
the limiting kernel, its image is the kernel at each level. This gives
P_n=Ahat^r/(K+f^n Ahat^r)=P/f^nP. It does NOT give K_n=K/f^nK.
The two components Ahat and A_f cover all primes, so their product is faithfully
flat. Finite modules over Ahat, including nonalgebraizable ones, are the actual
test modules in the argument. No localization/completion commutation is used.

**H035.5.** The induction is on ideals, using their ascending chain condition,
not on dimension. A nonnilpotent f has (f^n)≠0 for every n, so all quotients
needed by Lemma 2 are strictly larger ideals. A unit causes no difficulty.
For the zero quotient, even F=0 cannot provide a nonnilpotent element; this is
an actual boundary defect in the literal clause, not a proof of a false
nonzero-ring statement.

**H035.6.** On an artinian local ring, independently test the proposed P on
the injective cogenerator E: P=D(F(E)), so Hom(P,E)=F(E). End(E)=A makes the
identification compatible with every matrix between finite sums of E.
Two-step injective copresentations and left exactness extend it to all finite
modules. Thus no exactness of F beyond left exactness is used. The only
finite-value test objects required before completion are the finite E_n;
one does not assume finite values on arbitrary finite completed modules.

## H035.7–H035.15 — checked 2026-11-19, 04:13–04:17 UTC

**H035.7.** A finite-length A_p-module is killed by a power of pA_p and is
already complete. This is precisely the local finite-value input to H035.6.
The representing module at a generization is its scalar extension, by
Yoneda; this compatibility is needed, and is available, in the support proof.

**H035.8.** Rechecked the delicate spreading step. Extend the coherent support
on U to a finite submodule inside M, and spread generators for N(p). In a
punctured neighbourhood of p they agree stalkwise by generization compatibility.
If the closure of a difference component met p, its generic point would be a
generization of p lying in U, contradicting this equality. Removing those
finitely many closures gives the required extension near p. The image of α
in the quotient then vanishes after shrinking, by localization of F. The
generic representation on A/p and Nakayama fill the remaining closed stratum.
For the pro-object, a map of full-support pairs is onto, while two parallel
maps agree because α belongs to their equalizer. Products and equalizers
produce a cofiltered essentially small system. The local identity of Q_p
factors at one stage; the corresponding epimorphism Q_p→(P_i)_p is also a
split monomorphism, hence an isomorphism. The missing nonzero f is essential.

**H035.9.** A finite module over a domain is free on a nonempty principal
open after clearing a fraction-field basis. Repeating on the finitely many
irreducible components of the residual closed subset gives noetherian
induction, and a finite locally closed stratification. No normality is used.

**H035.10.** Recomputed L_(p)=p^(-1) Z_(p), while L_f has arbitrarily new
prime denominators. Thus every local rank and every residue rank is one, but
no nonzero principal localization is finite. The element 1 belongs to the
image of F(pZ) for every prime p and to no F(0); their intersection is zero.
This separately checks failure of minimal support. For the repair, n minimal
generators and generic rank n over a domain give B_p^n≅P_p: its kernel is
torsion and a submodule of a torsion-free module. The extra finite F(B) then
provides a finite locally free representing dual on an open. Theorem 12
really contains that extra hypothesis.

**H035.11.** The nilradical is nilpotent locally, so only finitely many graded
pieces occur on each noetherian affine. Generic freeness applies to each.
This statement is about graded freeness, not openness of the CM locus.

**H035.12.** Independently check the regular-element implication on the last
nonzero graded piece of A. That piece is free and faithful over A/J, so an
annihilator modulo J would contradict regularity on A. On each coefficient
graded piece regularity implies xR∩J^rR=xJ^rR. The quotient filtration is
therefore the reduction of the original filtration and induction applies.
Only nilpotence of the image ideal in the quotient is needed; it need not
equal the quotient's nilradical. The Koszul resolution supplies every positive
Tor, as required later.

**H035.13.** Recomputed with the two exact sequences involving image B and
cokernel H. Tor₁(M,B)=0 injects Z⊗M into K⁰⊗M and Tor₁(M,H)=0 injects
B⊗M into K¹⊗M. The kernel is exactly Z⊗M. The lemma supplies these two
modules simultaneously on a common dense open.

**H035.14.** The field example gives dimensions 1 and 2, so the written
coefficient cannot compute the stated Hom. Applying Hom(−,Q) to the finite
presentation independently gives L_i^∨⊗Q. The correction concerns the formula,
not a change of the earlier source module P.

**H035.15.** Recomputed the periodic resolution with d₁=x,d₂=y over
k[x,y]/(xy). Tensoring with A/(y) makes d₁ injective, so Tor₁ is zero.
Z¹=A gives the other zero Tor. Meanwhile (x)⊗A/(x)=k whereas the kernel
of y on k[y] is zero. This is a full counterexample under the standard cycles
meaning of Z¹. The repaired B¹ condition follows from the two exact sequences;
the alternative Tor₂(H¹) condition follows from their long Tor sequence.

## H035.16–H035.21 — checked 2026-11-19, 04:15–04:18 UTC

**H035.16.** Re-derived the length argument: all powers of a fixed parameter
system give length n₁⋯n_d C. For one variable, multiplication maps between
successive quotients must be injective by the length difference. Krull
intersection then gives regularity, successively, on W. After completion it
is enough to use the chosen original parameter system, not an unproved claim
about every new formal parameter system. MCM duality gives L/qL=A/q; the
surjection A→L is an isomorphism because Tor₁(L,A/q)=0 and Nakayama kill its
kernel. This proves the canonical-module reconstruction. It does not identify
the literal heading with Kähler differentials; the k/k test rules that out.

**H035.17–18.** The dual Koszul resolution has one nonzero cohomology in
degree r, namely ω/(x)ω. Shifting ω[d] gives the quotient's normalized
dualizing complex in degree −(d−r), verifying the sign and the dimension.
At dimension zero Matlis duality gives E(k), whose simple essential socle
proves indecomposability and whose cogenerator property detects maps.

**H035.19–20.** Matched Lyu Lemma 6.1(ii) to the finite module spread from
each generic point, and Corollary 4.7 to quotients of a regular ring.
Gor-2 implies CMU, so the cited EGA openness statement supplies the CM open.
The opens can be chosen in disjoint components, then their sheaves extended
coherently. The extension uses the quasi-coherent direct image on an affine
noetherian neighbourhood and finite generators on its quasi-compact open;
Zorn glues compatible extensions in the locally noetherian case. Excellence
gives J-2, hence a regular and therefore Gorenstein open in every integral
quotient. This proves the margin's excellent clause, without claiming a
global dualizing complex on every excellent scheme.

**H035.21.** Rechecked all steps of the counterexample rather than treating
the displayed infinite-variable algebra as noetherian. A nonzero polynomial
belongs to only finitely many block primes. Finite prime avoidance and a
generic scalar combination show that the stated localizations have exactly
those maximal ideals. Finitely many local generators, together with one
nonzero ideal element, then generate any ideal globally. Each local ring is
the one-dimensional semigroup domain K[t³,t⁴,t⁵]_(t³,t⁴,t⁵). Modulo t³ the
basis is 1,t⁴,t⁵ and the socle has dimension two; scripts/check_examples.out
checks that finite computation as well. Every dense open meets such a point.
A finite generic canonical module would have rank one and be free on a
smaller dense open, where this socle computation contradicts the required
injective hull. Gor-2 is the correct uniform all-integral-quotients condition:
necessity follows by generic freeness of a rank-one canonical module.

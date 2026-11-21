# Compatible collision classes across pointed covers: exact implications and remaining gate

Date: 2026-11-21. Author: GPT-6 Astra Pro, AN_GRH `/root/row_audit`. Effort is not exposed. This is a focused main-route probe, not a new numbered finding or a claim that the witness gate has closed.

## Setup and source scope

Let C/k be a smooth projective geometrically connected curve of genus at least two over a finite field k=F_q of characteristic p. Hypothetically suppose distinct P,Q in C(k) have equal geometrically pro-prime-to-p point sections. On every permitted pointed cover D→C, the covering implication gives a rational lift Q_D corresponding to P_D and

\[
\delta_D=[Q_D-P_D]\in J_D(k)[p^\infty].
\]

The full statement and proof of recovered A1 A.31 were read in
`recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`, lines1653–1700. Its independent uniqueness argument uses Hilbert90 and the degree of an invariant divisor under a free prime-to-p cyclic action. In particular compatible refinements give compatible point lifts and norm-compatible classes. This note uses that covering implication and uniqueness. It does not use A.31's final invocation of the already-proved A1 theorem, the cuspidal A05 argument, or the desired nonexistence of the hypothetical collision.

All subsequent norm identities are identities on the actual Jacobians. They do not replace a primitive subvariety by an arbitrary isogenous representative.

## 1. Exact refinement decomposition

Let h:D'→D be a finite etale refinement of degree d prime to p, defined over k, with compatible rational lifts P',Q' above P_D,Q_D. Write δ'=[Q'−P'] and δ=δ_D. Pushforward of these degree-zero divisors gives

\[
h_*\delta'=\delta,
\qquad h_*h^*=[d].
\]

Multiplication by d is an automorphism on every p-primary torsion group. Thus there is a direct-sum decomposition of actual rational p-primary groups

\[
J_{D'}(k)[p^\infty]
=d^{-1}h^*J_D(k)[p^\infty]
\oplus\ker(h_*:J_{D'}(k)[p^\infty]\to J_D(k)[p^\infty]),
\]

and in particular

\[
\delta'=d^{-1}h^*\delta+b,\qquad h_*b=0.
\]

The decomposition follows directly by subtracting d^{-1}h*h_* from the identity; the two summands have zero intersection because applying h_* to an element of the first recovers its unique downstairs antecedent. If m,m' are the exact orders of δ,δ', then

\[
m\mid m',\qquad m'=\operatorname{lcm}(m,\operatorname{ord}(b)).
\]

Thus compatibility preserves the old order. It does not, through these identities, bound the new norm-kernel component. This is an exact statement about the actual groups, rather than an assumption that every formal element b can occur as a difference of points. The latter representation constraint remains essential and is not resolved here.

## 2. Principal functions and the norm equation

Since mδ=0 and the divisor m(Q_D−P_D) is k-rational, a principal function with that divisor can be chosen in k(D)^×. Indeed Frobenius changes any geometric choice by a scalar; Hilbert90 removes that scalar. The same holds for f' with divisor m'(Q'−P'). Exactness of the p-power order implies that f and f' are separable: over the perfect field k, a pth-power function would divide the displayed divisor multiplicities and contradict exactness. If the exact order is one, simple zeros and poles give the same conclusion.

The divisor formula for the function-field norm gives

\[
N_h(f')=c\,f^{m'/m},\qquad c\in k^\times.
\]

For m'>m, the right side is a pth power, because k is perfect. A pth-power norm does not imply a pth-power function upstairs. For example, in the separable extension k(z)/k(t), t=z^d, with p not dividing d and a nontrivial dth root ζ in k, the function (z−1)/(z−ζ) has norm1 and simple zero and pole, so is not a pth power. This example is only a counterexample to that unrestricted norm inference: its map is ramified, and its zero and pole have the same image. It is not a counterexample to the pointed-etale-cover problem.

More intrinsically, Hilbert90 supplies norm-one functions σ(u)/u in a cyclic refinement. Their divisors generally have many points of support. To exploit the norm equation here one must use the special two-point support and all the compatible refinements together. No argument in this probe turns those extra conditions into an upper bound on m'.

## 3. A point-supported constraint goes in the opposite direction

Assume now that D→C is geometrically Galois of degree n with constant deck group over k, and has the specified rational P_D. Then its P-fibre is entirely rational. The hypothetical collision supplies a rational Q_D, so its Q-fibre is also entirely rational. The two fibres are disjoint and contain 2n rational points.

Let m be the exact order of [Q_D−P_D], and choose the descended function f above. The map f:D→P^1 has degree m. Its zero and pole fibres have exactly one geometric point each, namely Q_D and P_D. Each of the q−1 other rational values has at most m rational points in its fibre. Consequently

\[
2n\le\#D(k)\le(q-1)m+2,
\qquad
m\ge\left\lceil\frac{2n-2}{q-1}\right\rceil.
\]

This lower bound concerns the particular point-difference class. It is not an upper bound on the entire Prym and does not require an abstract torsion-module example. It illustrates why a bound on these particular orders needs genuinely new input. The constant-deck hypothesis is necessary for the 2n rational points; the argument is not applied to a nonconstant-deck tower. Nor is existence of arbitrarily large constant pointed covers over a fixed k assumed. Enlarging k changes q and hence changes the bound.

## 4. What happens on a common refinement of two cyclic witnesses

Let D_i→C be constant connected cyclic covers of coprime odd degrees n_i>1, prime to p, with rational lifts of P. Their connected fibre product D has constant group

\[
G=C_{n_1}\times C_{n_2}\simeq C_{n_1n_2}.
\]

Connectedness follows from the coprime Galois degrees. The rational lifts give a rational point on the fibre product. Let h_i:D→D_i and K_i=ker(G→C_{n_i}). On Jacobians,

\[
h_i^*h_{i*}=\sum_{\gamma\in K_i}\gamma.
\]

On a character nontrivial on K_i, this trace operator is zero. In particular every faithful conductor-n_1n_2 character is killed by both traces. Equivalently, with the actual integral primitive projector p_n=ne_n, the integral group-ring identity

\[
\Bigl(\sum_{\gamma\in K_i}\gamma\Bigr)p_n=0
\]

holds. Since h_i^* is injective on p-primary groups, h_{i*} kills the actual primitive p-primary group P_n(k)[p^infinity]. Thus the top primitive component of δ_D is invisible to both norm conditions h_{i*}δ_D=δ_{D_i}.

A good character packet downstairs imposes the corresponding inflated-character constraint upstairs. It does not impose the same constraint on the faithful product-conductor component. The same observation applies to norms to any proper cyclic quotient of a fixed cyclic cover: a faithful character is nontrivial on every nontrivial quotient kernel.

This does not prove that an arbitrary element of the invisible component can be added while preserving representation by the compatible pair of point lifts. It proves the narrower point that norm compatibility and the separate packet tests alone do not determine that component. No tensor-product formula identifying the new Jacobian factor with the old factors is available in these identities. A49's variable-quotient lemma supplies a unit signed orbit for some character; it supplies no theorem that the union of these constraints covers every faithful character of one useful common cover.

## 5. Exact remaining input

The attempted compatibility route still needs at least one of the following genuinely geometric or arithmetic statements:

1. An upper bound, strong enough for a small-support divisor argument, on the exact order of a suitable projected **point-difference** class on one allowed cover.
2. A theorem forcing the actual faithful component of a compatible two-point class to vanish from the signed-orbit constraints across a family of covers.
3. Another argument using the two-point support to contradict the norm equations, without replacing those classes by unconstrained torsion elements.

Neither the exact splitting of norm maps nor the norm equation gives one of these statements. The nonzero rational norm-kernel component is the remaining place where the orders may grow, while the full faithful component is the remaining place where separate packet constraints can be missed. These are precise limits of this attempted deduction, not a geometric counterexample, an impossibility theorem for a different compatibility argument, or a claim that the universal main witness condition has been reduced.

## Check record

The author read the complete recovered A.31 statement/proof, then checked every displayed identity and all five sections above. The two short assertions in Sections1–3 were also sent to `/root/effective_galois`, whose independent algebra reading confirmed them under the stated hypotheses before this complete note was finalized. That preliminary message is not counted as a whole-note review. No computation, new numerical example, external literature theorem, or formal proof verification is asserted.

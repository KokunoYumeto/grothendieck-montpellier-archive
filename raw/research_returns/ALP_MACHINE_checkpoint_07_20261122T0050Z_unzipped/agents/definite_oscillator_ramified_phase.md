# AM-DO-021: an exact ramified compact character and a rank-two to rank-four counterexample

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`; inherited
reasoning effort not separately exposed; 21 November 2026 UTC.

This result uses the standard unitary Weil splitting attached to characters
χ_S,χ_T in Kudla's normalization, with Pan's explicit comparison to the
lattice model. It computes the missing scalar at the ramified prime 7.
It does not infer that every representation satisfying only some of the
source's listed axioms has already been identified with this standard
splitting. The split-place proof AM-DO-020 did not require this additional
identification.

## Statement

Character labels use the source convention
`LocalNewformFunction.splitFacO`, whose source factor is
\(\chi_T(x)^{-1}\) and target factor is \(\chi_S(y)\) on
determinant roots. Thus conventional Harris–Kudla–Sweet tensor
parameters are \((\chi_S,\chi_T^{-1})\); corrected AM-DO-023
records the same conversion at infinity. In particular every
trivial-character assertion below is independent of that labeling
choice.

Let E=Q(ζ₇), F=E⁺, and let v be the unique place of F above 7. Put
K=F_v, L=E_v, O=O_K, O_L=O_{E_v}, and s=ζ₇−ζ₇⁻¹. Conjugation on L is
written with a bar. The residue fields of K and L are both F₇, and s is an
anti-invariant uniformizer of L. Let ξ=s/7.

For positive even integers a,b, take the standard Hermitian lattices
O_L^a,O_L^b and their Hom lattice Λ=M_{b×a}(O_L). Use the actual rational
symplectic form of AM-DO-018 and the corresponding additive character.
Let φ₀ span the trace-one Heisenberg vacuum line of Λ. Let

    K_a=U(I_a)(O),       K_b=U(I_b)(O).

For t∈L¹={t:t bar(t)=1}, define

\[
 \epsilon(t)=\begin{cases}1,&t\equiv1\pmod{s},\\-1,&t\equiv-1\pmod{s}.
 \end{cases}
\tag{DO21.1}
\]

Every norm-one t is a unit and has residue ±1, so this is a continuous
quadratic character. Let χ_S,χ_T be the unitary splitting characters; at
these even ranks their restrictions to K× are trivial. For determinant
roots x/bar(x)=det g, y/bar(y)=det h, the exact scalar is

\[
 \boxed{\omega_{\psi,\chi}(g,h)\phi_0
   =\chi_T(x)^{-1}\chi_S(y)
      \epsilon(\det g)^{b/2}\epsilon(\det h)^{a/2}\phi_0,
       \quad g\in K_a,\ h\in K_b.}
\tag{DO21.2}
\]

In particular, take a=2,b=4, g=1 and
h=diag(−1,1,1,1). Both lattices are unchanged. Both prescribed finite
averages in AM-DO-018 are therefore the identity. Nevertheless, with
s supported at the place v and y=−2s as a determinant root at v,

\[
               \omega(1,h)\phi_0=-\chi_S(y)\phi_0.
\tag{DO21.3}
\]

Thus the unchanged two-average formula (DO19.1), whose right side is
+χ_S(y)φ₀, is false for this actual standard splitting at these ranks.
This is a specified nonzero-vector counterexample, not an argument from
absence of a canonical map. Twisting a splitting character changes both
sides by the same determinant-root factor, so it does not remove the
residual minus sign.

For this fixed standard-lattice construction, agreement with the prescribed
root factor on the *entire compact pair* is equivalent to

\[
                            4\mid a\quad\text{and}\quad4\mid b.
\tag{DO21.4}
\]

Alternatively it holds on K_a⁺×K_b⁺, where K_n⁺ consists of elements whose
determinant has residue +1. Each K_n⁺ has index 2. This changes the level
or adds an orientation to the lattice data; it is not equality on the
unchanged compact group. The new index is a 7-adic unit and an 11-adic
unit. No conclusion about an iterated terminal mass or the net step-8
lift count follows without the other recorded arithmetic identities.

## Proof

### 1. Identification of the actual trace lattice with Pan's lattice

Use the additive character ψ_K=ψ_Q∘Tr_{K/Q₇}, where ψ_Q has conductor Z₇.
The different of F/Q has v-adic exponent 2 (the discriminant is 7²), so
ψ_K has conductor exponent λ_K=−2 in the convention that ψ_K is trivial
on p_K^{λ_K}. The relative extension L/K is tamely ramified quadratic.
The element s has L-valuation 1, and 7 has L-valuation 6; hence
v_L(−2ξ)=−5.

Pan (2001), §3.1, equation (3.1.a), uses

\[
 \langle\!\langle\ ,\ \rangle\!\rangle
       =\tfrac12\operatorname{Tr}_{L/K}(h\otimes\overline{h'}).
\tag{DO21.5}
\]

Take V=L^b with h=I_b and V′=L^a with skew-Hermitian form
h′=−2ξI_a. Conjugating the source tensor factor identifies V⊗_L V′ with
the Hom realization used in AM-DO-009 and AM-DO-018. Then (DO21.5) is
exactly Tr_{L/K}(ξ h_Hom). The finite operators (DO18.5) instead have
Heisenberg cocycle ψ_f(E_H/2), where E_H is the negative of that trace
form. Accordingly use ψ_K^{-1} with Pan's displayed trace form, or
equivalently negate that form and keep ψ_K. These two descriptions
realize the same central character and operators. Lemmas 7.2–7.3 below
give the same displayed αβ formulas for every nontrivial ψ_K, so the
computed determinant-root factor and residual real sign are unchanged.

Set the duality exponents of Pan §1.3, equation (1.3.a), to κ=0 and
κ′=−5. Both standard O_L lattices are selfdual for these conventions:
for I_b the duality ideal is O_L, and for −2ξI_a it is s^{-5}O_L.
Moreover

\[
                   \kappa+\kappa'=-5=2\lambda_K-1,
\tag{DO21.6}
\]

which is exactly Pan's compatibility condition (3.1.b) in the ramified
case. His good lattice (3.2.c) is therefore

\[
 B(L_0,L_0')=L_0^*\otimes L_0'\cap L_0\otimes L_0'^*
                  =O_L^{ab}=\Lambda.
\tag{DO21.7}
\]

It is selfdual for the trace symplectic form and ψ_K. Since 2 is a unit
at 7, the trace-one local character ψ_K(B(x,w₀x)/2) is trivial on Λ:
w₀ preserves Λ, B is integral in the additive-character convention,
and its conductor ideal is stable under multiplication by 1/2. Thus
φ₀ is exactly the ordinary selfdual-lattice vacuum in Pan's model.

For an element preserving Λ, the lattice operator M_B is pullback by
its inverse (Pan §2.3, equation (2.3.e), or the selfdual formula in §2.4).
It fixes the vacuum supported on Λ. The actual split Weil operator is
β^Y times the Schrödinger operator, and Pan (3.3.a) compares the latter
with α M_B. Therefore its scalar on this vacuum is exactly αβ^Y.
This identifies the normalization being computed; one cannot replace
that scalar by the value of the spherical symplectic splitting without
this comparison.

### 2. The integral Witt decomposition of the identity forms

The two-dimensional Hermitian form I₂ over L/K is anisotropic. Indeed a
nonzero isotropic vector would give N_{L/K}(z)=−1 after dividing by one
nonzero coordinate. Such a norm must have valuation zero, so z is a unit.
Conjugation is the identity on the residue field, hence the residue of
its norm is a square in F₇. The residue −1=6 is not a square. This is a
contradiction.

The four-dimensional symmetric form I₄ over F₇ is the sum of two
hyperbolic planes. For a direct elementary check, (1,1,1,2) is a nonzero
isotropic vector. A vector pairing nontrivially with it can be adjusted
by a multiple of it, using that 2 is invertible, to give a hyperbolic pair.
The orthogonal binary complement has determinant −1 modulo squares,
because det I₄=1 and a hyperbolic plane has determinant −1. A binary
nondegenerate symmetric form is isotropic precisely when the negative
of its determinant is a square: this follows immediately after
orthogonal diagonalization by solving A x²+B y²=0. The complement is
therefore another hyperbolic plane.

This mod-7 isometry lifts to O. To see this without assuming a lifting
classification, suppose an invertible matrix C_r realizes the isometry
mod p_K^r. Correct C_r by C_r(1+p_K^r X). The first-order correction of
the Gram matrix is XᵗJ+JX. For every symmetric error matrix S, choosing
X=−J^{-1}S/2 solves this linear equation. Inducting and taking the
p_K-adic limit gives an integral invertible isometry. Consequently
I₄ is integrally isometric to H⊥H over O, and hence over O_L. By taking
orthogonal sums,

\[
 I_{4k}\simeq H^{\perp 2k},\qquad
 I_{4k+2}\simeq H^{\perp 2k}\perp I_2,
\tag{DO21.8}
\]

with the standard lattice decomposed as the corresponding integral
orthogonal sum. Multiplying all forms by −2ξ preserves this decomposition
and the lattice admissibility. These are precisely the decompositions
needed for Pan's tensor-product identity (3.6.e).

### 3. The compact scalar on a determinant section

First let the moving group act on a single nondegenerate Hermitian or
skew-Hermitian line, and write its element as t=x₀+s y₀∈L¹, t≠1.
Pan Lemma 7.2 (printed p.207) states that, against a hyperbolic plane,

\[
                        \alpha(t)\beta^Y(t)=\chi((t-1)s).
\tag{DO21.9}
\]

Pan Lemma 7.3 (printed p.208) gives, against an anisotropic plane,

\[
 \alpha(t)\beta^Y(t)=
 \begin{cases}
   -\chi((t-1)s),&x_0\not\equiv1\pmod{\mathfrak p_K},\\
   +\chi((t-1)s),&x_0\equiv1\pmod{\mathfrak p_K}.
 \end{cases}
\tag{DO21.10}
\]

At a ramified quadratic place, a norm-one element has residue +1 or −1.
Its residue agrees with that of x₀, so the extra factor in (DO21.10) is
exactly ε(t). Also

\[
       \frac{(t-1)s}{\overline{(t-1)s}}
        =\frac{(t-1)s}{(t^{-1}-1)(-s)}=t.
\tag{DO21.11}
\]

Thus the argument of χ in these formulas is the actual determinant
root, not the determinant t. Since χ|K×=1, its value is independent of
the chosen root. At t=1 the root may be chosen to be 1 and the formula
follows from the identity operator.

Use (DO21.8) for the opposite even-dimensional space. Choose splitting
characters on the hyperbolic and anisotropic summands with product χ;
all but one may be trivial because every summand has even dimension.
Pan (3.6.e) multiplies their αβ factors. Therefore the scalar for the
one-dimensional moving subgroup is

\[
                   \chi(y)\epsilon(t)^{d/2},
       \qquad y/\bar y=t,
\tag{DO21.12}
\]

where d is the opposite even rank. For d divisible by 4 the anisotropic
summand is absent; for d congruent to 2 modulo 4 it occurs exactly once.
This proves (DO21.12), including its phase, for diagonal elements
 diag(t,1,…,1) of the compact unitary group.

### 4. Extension to the full compact group

Pan's Proposition 3.3 (printed pp.179–180) says that the scalar αβ^Y on
the compact special unitary group equals the character ζ defined there.
When the opposite rank is even, ζ is trivial. Thus αβ^Y factors through
the determinant on the compact unitary group. The determinant map is
surjective onto L¹, since t↦diag(t,1,…,1) is a section and every norm-one
element of L is integral. Formula (DO21.12) consequently determines
its value on the entire compact group.

For the target group U(I_b), d=a and this yields
χ_S(y)ε(det h)^{a/2}. For the source group U(I_a), the Hom action is
contragredient: its determinant on the source factor is (det g)^{-1}.
The corresponding root is x^{-1}, the splitting factor is χ_T(x)^{-1},
and ε((det g)^{-1})=ε(det g). Hence its contribution is
χ_T(x)^{-1}ε(det g)^{b/2}. The two commuting unitary actions multiply.
This proves (DO21.2).

For a=2,b=4 and h=diag(−1,1,1,1), ε(det h)=−1, proving (DO21.3).
The trace-one seed is nonzero (AM-DO-015), so its finite vacuum is
nonzero by the injectivity in AM-DO-018. The equality cannot hold with
the positive sign. Both lattice indices are 1 since h is integral
unitary. Finally the determinant-section elements with determinant −1
exist in each compact group; thus vanishing of both residual characters
is equivalent to evenness of a/2 and b/2. This proves (DO21.4). The
kernels K_n⁺ have index exactly 2 by the same determinant section.

## Scope and next gate

The theorem separates two questions that were previously conflated.
The mixed CM trace lattice and the finite averaging construction exist,
and their relative split-place phases are exactly solved in AM-DO-020.
The standard ramified compact phase is now also computed. For ranks
2→4 the literal lattice-indexed phase formula fails; at ranks divisible
by 4, or after the stated compact restriction, this particular
obstruction disappears. Neither alternative by itself proves the
noncompact ramified move formula, the rational compatibility of the
fixed two-step averages, an all-polynomial arithmetic `MainX` identity,
or a terminal pairing value. Those remain separate equations.

An arbitrary choice of a local character twist is not a way to change
(DO21.3) while retaining the same determinant-root pins: the twist
appears on both sides. A new constructor could add orientation/level
information to its lattice objects or alter its arithmetic column
transformation law. Such a construction must be specified and checked;
this theorem does not exclude it, nor does it exclude actual nonzero
unitary theta lifts (including the first torus lift being constructed
in ALP-LIFT).

## Primary source and check status

Pan, S.-Y. (2001). Splittings of the metaplectic covers of some reductive
dual pairs. *Pacific Journal of Mathematics, 199*(1), 163–226.
https://msp.org/pjm/2001/199-1/pjm-v199-n1-p10-p.pdf .
Exact locators used: §1.1 conductor convention; §1.3 equations(1.3.a–c);
§2.3 equation(2.3.e) and §2.4; §3.1 equations(3.1.a–b); §3.2 equation(3.2.c);
§3.3 equation(3.3.a) and Proposition; §3.6 equations(3.6.a,e);
Lemmas7.2–7.3, printed pp.207–208. These statements and the displayed
proofs of Lemmas7.2–7.3 were directly read. Proposition3.3 is applied as
a published theorem, not advertised as independently re-proved here.

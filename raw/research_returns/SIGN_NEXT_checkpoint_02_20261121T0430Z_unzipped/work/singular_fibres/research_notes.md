# Cote 44: singular-fibre correction and the actual height

Author: `/root/singular_fibres`, GPT-6 Astra Pro; effort not exposed.
Run: SIGN_NEXT, 21 November 2026. These notes accompany `contribution.tex`,
findings SN-44-01–SN-44-06. The parent owns the integrated paper and delivery.

## Completed result and scope

The corrected formula is an actual intersection theorem with admissible Chow
extensions, and its height is identified with an ordinary Poincare
Neron–Tate pairing on incidence higher Picard varieties. It is not a new name
for an unspecified cohomological pairing.

For a smooth projective pencil model of dimension `2m`, let `V_s` be the
numerical image of actual codimension-`m` cycles on fibre `s`, `R_s` its
intersection radical, `D_s,i` actual cycles giving a basis of `V_s/R_s`, and
`G_s=(D_s,i D_s,j)`. For ambient cycles with algebraically trivial generic
restrictions, put `a_s(Z)=(pi*Z D_s,i)`. Then

`<z,z'>_G = (-1)^m [ZZ' - sum_s a_s(Z)^t G_s^(-1) a_s(Z')]`.

The formula holds over any algebraically closed field whenever the stated
smooth model exists. It assumes no general positive-characteristic
resolution theorem. Admissible extensions are obtained by subtracting the
displayed actual vertical projection; radical classes are killed because an
admissible extension already exists, by Kahn's theorem for algebraically
trivial cycles. Numerical finite-dimensionality is justified by a rational
full-rank intersection matrix, not merely by embedding a Q-vector space in
finite-dimensional Q_l cohomology.

At an ordinary node in characteristic different from 2, the local form is
`DD' = (-1)^m nu(D)nu(D')`, where `nu=u-v` is the difference of the two ruling
coefficients on the exceptional quadric. This includes `m=1`: the quadric
has two points, the strict fibre may be disconnected, and the formula is
the negative fibre-component pairing. Only the actual algebraic image is
used; no Hodge or Tate conjecture produces a local generator. If the image
is nonzero it can be normalized rationally to `nu(D_s)=1`.

For a Lefschetz pencil of odd-dimensional members, of any positive odd
dimension, the node formula becomes

`<z,z'>_G = (-1)^m ZZ' - sum_s c_s(Z)c_s(Z')`.

If the vanishing part `E` is nonzero, conjugacy makes every local vanishing
cycle nonzero, the local algebraic defect vanishes, and the correction is
zero. If `E=0`, the normalized Neron–Tate height is zero and the raw signed
intersection is exactly the sum of the node terms. These two assertions are
proved in characteristic different from 2. In characteristic 2 the general
Gram theorem and the algebraic height comparison remain available, but this
ordinary-node specialization is not asserted.

## The three individual terms

In the example on `P²_x × P²_y`, with coefficients
`(lambda,lambda+mu,lambda+2mu)`, put

`D_i = {x=e_i, [lambda:mu]=[-i:1]} × P²_y`.

These are actual surfaces in the smooth total space. They are the reduced
regular zero scheme of the section of
`F = Q_y^vee tensor O(a+t)` given by `(d_0x_0,d_1x_1,d_2x_2)`.
The top Chern identity, integrally in the Chow group, is

`D_0 + D_1 + D_2 = pi*(a²-ab+b²) + t(2a-b)`.

The normal bundle of every `D_i` is `Omega¹_P²(1)`, of second Chern number
1. Therefore `D_i²=1`, distinct `D_i` are orthogonal, and `(pi*Z)D_i=1`.
The corrected extension is `t(b-2a)`, a vertical radical class of square
zero. Each node contributes **one**, giving `0=3-(1+1+1)`.

The class `D_i` meets the exceptional quadric in one ruling line, so the
local normalization is also checked geometrically. This is stronger than
inferring equal terms from the symmetry or from the total square 3.

## Height normalization and characteristic-free argument

Use the geometric Poincare biextension **bilinear** Neron–Tate pairing. For
an incidence Poincare cycle of multiplicity `k_Y^m` and its transpose
duality `lambda_Y^m`,

`h_geom(z,z') = (1/k_Y^m)<theta z, lambda_Y^m theta z'>_Poincare`,

and the archive's signed height is `(-1)^m h_geom`. There is no extra 1/2.
If the polarization convention defines its bilinear form with 1/2, divide
the entire identity, including the intersection side, by 2. In the curve
case the incidence duality is the negative theta polarization. The proof
does not assert that every unmodified higher Picard autoduality is a
positive polarization; the primitive-sign issue in scan 008 is retained.

Chen's Theorem 7.9 supplies the complex comparison without the Griffiths
incidence conjecture. His later Theorem 7.19(c), concerning a Lear/Hodge
biextension comparison, is a different statement with that conjectural
input. We do not use it.

SN-44-06 separately derives the comparison over `k(B)` in any
characteristic. After finite extension, an algebraically trivial cycle is
a sum of `Gamma_*([c_0]-[c_1])` on curves. Refined Gysin associativity gives
the arbitrary-degree height adjunction. Kahn's Proposition 3.8 states only
degree-zero adjunction, so the proof explicitly writes the degree-shifted
calculation from his Lemma 3.3 instead of misquoting the proposition. Curve
intersection height is Neron's pairing by Pepin's Theorem 2.3. Saito's
Proposition 4.4 supplies `k_Y lambda_C b = a^vee lambda_Y`. Functoriality of
the Poincare biextension gives the comparison. Alterations and division by
degrees, as in Kahn's Theorem 4.14(b), avoid unavailable smooth models after
base change. Full finite degrees, including inseparable degrees, are used.

The same calculation treats complementary codimensions `i+j=dimY+1`.
Choose the Poincare **i**-cycle of multiplicity `k_Y^i`; its transpose is
`lambda_Y^j:P^j -> (P^i)^vee`. The comparison denominator is `k_Y^i`.
Thus the nonmiddle vanishing in the margin of scan 004 also concerns the
actual Neron–Tate pairing, not only geometric intersection height.

For `E=0`, one must not simply pass to an arbitrary finite separable base
cover, whose genus could be positive. Instead descend the incidence Picard
variety over the perfect closure, and descend the finite data to some
`K_r=k(t^(1/p^r))`. This retains base `P¹`. The Poincare cycle makes `H¹(P)`
a quotient of the constant odd middle Galois representation; all Tate
twists are constant because `k` is algebraically closed. NOS gives good
reduction everywhere, and the Neron model on `P¹` is a projective abelian
scheme. In Leray, the zero section makes `H²(P¹)->H²(total)` injective, so
`H¹(total)->H¹(fibre)` is an isomorphism. Restriction of
`Pic⁰(total)_red` gives an isogeny from a constant abelian variety to the
dual generic fibre. Hence `P` is constant **up to isogeny**; nonconstant
supersingular families are not excluded. A constant abelian variety has
only constant `k(t^(1/p^r))`-points, since `Alb(P¹)=0`, also for inseparable
maps. The trace quotient is torsion, the pairing vanishes, and dividing by
`[K_r:K]` gives vanishing over the original base.

This is a proof assembled from established inputs; no claim of literature
priority for the general comparison or fixed-part argument is made.

## Framework translations

| Framework | Precise object in this contribution |
|---|---|
| Archive cote 44 | Scan 004 Theorem 5, manuscript page 2; its omitted singular-fibre correction is the vertical Gram projection. Scan 008's primitive-sign caveat is preserved. |
| HODGE_SIGN and intake | AR-01 supplies the counterexample; SG-02 supplies the quadric ruling calculation for `r>=1`; intake Q4 asks for each individual nodal contribution. The new contribution computes those terms and the corrected theorem. |
| Schemes and intersection theory | Smooth blowup pencil model; actual vertical Chow cycles; regular section, normal bundle, refined Gysin and self-intersection; no Cartier assumption on cycles inside integral fibres. |
| Neron–Tate and higher Picard varieties | Incidence quotient, Poincare-cycle multiplicity, normalized transpose duality, trace quotient and full-degree field normalization. |
| Etale and vanishing-cycle formalism | Local defect is the ruling-difference quotient, identified via the Gysin sequence of `O_Q(-1)`; `E=0` gives constant odd middle local system and next-degree skyscraper defects. |
| Motives | `p_s=(-1)^m D_s×D_s` are explicit orthogonal Chow idempotents with image `L^m`; no standard conjecture is used to construct them. |
| K-theory and lambda-rings | In the example, the regular-section Koszul class is `lambda_{-1}(F^vee)`, and `ch_2=c_2(F)` is the integral Chow correction identity. |
| Finite fields and L-functions | Over odd `F_q`, the three example projectors give three `Q_l(-2)` summands, eigenvalue `q²`, weight 4, and factor `(1-q²T)^(-3)`. |
| Arithmetic schemes | Example and Chow/K-theory identities spread over `Z[1/2]`; no Arakelov height theorem over `Spec Z` is asserted. |

## Exact archive and source locators

All nine `sources/ARCHIVE_44_scan001.tex` through `scan009.tex` were read in
full. The running `mspage` markers in scan 004 are 2 at its beginning and 3
at its end; cite Theorem 5 as manuscript page **2**. The unrelated cancelled
graded-module/root-system material on scans 003/005 and the printed
terminology sheet on scan 007 do not supply hypotheses for Theorem 5.

The supplied run source is
`sources/RETURN_HODGE_SIGN_final_20261121T0057Z/HODGE_SIGN.tex`, AR-01
statement and full proof (around lines 798–884), and SG-02 full proof
(around lines 614–655). The intake is
`sources/INTAKE_HODGE_SIGN_20261121.md`, section “Item 4: cote 44 (Q4)”.
These are existing results, explicitly distinguished from this run's
new calculation and corrected formulation.

| Primary source | Exact used locations | Local cache / retrieval |
|---|---|---|
| B. Kahn, *Refined height pairing*, ANT 18(6), 2024, 1039–1079 | Def. 2.2; Prop. 2.8; Def. 2.10/(2-9); Lemma 3.3 and proof; Props. 3.6, 3.8, 3.9; Prop. 4.12(c); Th. 4.14(b); Th. 5.6(a), Lemmas 5.7/5.8; Th. 5.10(b) for sign | `kahn-published.pdf/.txt`; https://msp.org/ant/2024/18-6/ant-v18-n6-p01-p.pdf |
| Z. Chen, arXiv:2512.22788v1 | Lemma 3.16, Def. 3.17, Lemma 3.19, Example 3.20, Remark 3.21; complete Th. 7.9 proof; distinguish Th. 7.19(a),(b) from (c) | `chen2512.22788v1.pdf/.txt`; https://arxiv.org/pdf/2512.22788v1 |
| H. Saito, Nagoya Math. J. 75 (1979), 95–119 | Arbitrary characteristic stated p. 96; Prop. 3.4, Th. 3.6; (4.1), (4.2), Prop. 4.4 and Cor. 4.5. Prop. 4.4 refers its proof to Lieberman's *Intermediate Jacobians*. | `saito1979.pdf/.txt`; DOI 10.1017/S0027763000024855, official Cambridge PDF |
| C. Pepin, arXiv:1103.0570 | Def. 2.1 and complete Th. 2.3 proof pp. 6–8; curve intersection formula p. 2 | `pepin2011.pdf/.txt`; https://arxiv.org/pdf/1103.0570 |
| SGA 7 I, Expose IX | Cor. 2.2.9 statement printed p. 335, proof p. 336; Prop. 3.2 printed p. 347; §3.2.1 and proof p. 348. Internal expose pp. 17–18 and 29–30. Original PDF pp. 340–341 and 352–353. | `sga7-i-original.pdf` and page PNGs; https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf |
| P. Deligne, *Weil I*, PMIHES 43 (1974), 273–307 | (4.1), p. 287; (4.3.3), p. 288; (5.4); (5.8)(a),(b), pp. 292–293 | `deligne-weil1.pdf/.txt`; https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf |
| Fulton, *Intersection Theory* | Prop. 1.8; Cor. 6.3; Prop. 6.7; regular-section top Chern and normal-bundle calculation in Example 6.3.4(a) / Prop. 14.1(c) | Standard source already used in HODGE_SIGN; formulas specialized and signs checked explicitly here. |

The original SGA scan was visually read at the stated pages. Its extracted
text contains no useful OCR. Digital transcriptions at
`https://grothendiecksga.com/read/sga7/fr/9-2.html` and `9-3.html` first
located the statements, then the original scan confirmed them. The correct
NOS locator is **IX 2.2.9**, not IX 7.4.

An older Kahn draft remains in the cache but is not used for theorem
numbering. `anantharaman1973.pdf/.txt` is Anantharaman's paper, formerly
downloaded under a misleading Raynaud filename; its filename has been
corrected. Kunnemann 1996 is listed as the number-field antecedent cited by
Chen, not as an independently read function-field proof. Holmes–de Jong
2015 was inspected for its complex Deligne/Poincare sign comparison; it is
not used as an arbitrary-characteristic input.

## Verification and limitations of the machine checks

The proofs in SN-44-01–06 were read and rederived by the author. The parent
independently checked the local blowup signs, the Chern/Chow identity and
projector computation, and then the characteristic-free fixed-part route.
`/root/critical_lefschetz` independently reviewed the full contribution,
including the curve case and arbitrary-degree adjunction; its separate
review records identify its exact checked hashes.

`verify_intersections.py` is an exact symbolic certificate, not a formal
proof of the geometric hypotheses. It passes the quadric/parity expansion
for `m=1,...,9`, every nodal Hessian, the individual normal Chern and
intersection numbers, the total square, and a full seven-by-seven middle
Gram matrix of determinant 1. The saved output is
`computation_certificate.json`.

Static TeX checks pass for braces, environments, unique labels, references
and citations. Earlier standalone compilation was unavailable:
`pdflatex` lacked its format, and `tectonic` could not obtain its bundle
(HTTP 403). No compiled-PDF verification is claimed. One optional OCR
attempt stalled and was interrupted; original SGA pages were read as
images instead. These tool failures affect neither source availability
nor the mathematical checks.

The author `check_events.tsv` uses the parent run's five-column schema.
Its timestamps record when this batch of completed checks was entered,
not separate estimates of historical wall-clock check times. Model effort
has not been inferred. The proof is unchanged after SHA-256
`cb58112da407c5749a83ccd6dde7fe31bd0258f2691a5efe55a6c691ac72df86`
at the time these notes were completed.

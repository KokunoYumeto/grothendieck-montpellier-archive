# K17-GL2-CONDUCTOR — independent whole-proof and primary-source audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, archive_kummer.
Verdict: **PASS**, for the assumptions and conclusion in the reviewed argument.
The original 1997 journal PDF was not recovered. The precise compatibility theorem was instead read in full in an author-hosted survey by Saito, with an explicit citation to his 1997 paper. No original theorem number is asserted.

## Reviewed document and actual checks

The entire root argument `work/hecke_level_one/gl2_conductor_bridge.md` was read and independently reconstructed. Its reviewed SHA256 is
`b8216b3340c3e7ae797aefa360d15e9faa498ae8706b76ecee61638da8c7962d`.

The following complete local source files were read for the source interpretation:
`AutNewformW.lean`, `Newform.lean`, `AdmissibleRankTwoSelf.lean`, and
`BlochKatoSelmerVanishes.lean`, all in `work/hecke_level_one/`.
This is a source-content audit, not a Lean execution.

In particular, `Adm2A` retains the existence of an irreducible W, the modular attachment for
R = W chi_ell^(-e), the exact Level assertion, determinant weight zero, and the conjugacy of rho to W restricted to E plus the trivial character. `Level` contains continuity. Its away-prime condition is actual diagonal inertia, and its coefficient-prime condition is an actual flag on the entire decomposition group, with the stated inertial characters. The additional local disjunction in `LevelAt` is not needed by this proof. `Newform.Att` is semisimple attachment at cofinally many geometric Frobenius elements, not an all-prime compatibility theorem by definition.

## Primary coefficient-prime theorem: exact resolved locator

**Takeshi Saito, _Galois representations in arithmetic geometry_, author-hosted survey,
§2c, pp. 8–9, Theorem 3 on p. 9.**

Primary URL:
https://www.ms.u-tokyo.ac.jp/~t-saito/pp/suams.pdf

Local source:
`work/hecke_level_one/saito_galois_arithmetic_survey.pdf` and its extracted `.txt`.

PDF SHA256:
`76be87c49eb2fc44d43076173c8f9762b6ef8d20bfa7d3a3a4aac201523c4cf7`.

All of §2, including §§2a–2c on pp. 5–9, was read. Pages 8 and 9 were also visually checked in rendered images. The displayed theorem states, in Saito's notation,
\[
D_{\mathrm{pst}}\!\left(V_{f,p}|_{G_{\mathbf Q_p}}\right)^{F\text{-ss}}
 \simeq \sigma(\pi_{f,p}).
\]
Here the objects are representations of the full Weil–Deligne group. The preceding subsection defines the Weil representation together with monodromy N; F-semisimplification is not replacement by the semisimplification of the original Galois representation. The paragraph immediately following the theorem explicitly lists potential semistability, equality of Weil traces, and equality of monodromy ranks as the three steps of its proof.

The setup in §2a, p. 6, uses normalized eigen newforms and geometric Frobenius in the Euler factor. For weight at least 2, it identifies the associated representation with the geometric construction in modular-curve/Kuga–Sato cohomology. Theorem 3 is for classical forms over Q. The next paragraph separately discusses a Hilbert analogue under additional hypotheses. There is no degree-greater-than-one hypothesis in this classical theorem and no restriction to trivial nebentypus.

The theorem bears the citation [S7]. The bibliography on p. 16 identifies [S7] as Saito, _Modular forms and p-adic Hodge theory_, Inventiones mathematicae 129 (1997), 607–620. This is a precise primary author restatement of the needed result.

The author's publication list,
https://www.ms.u-tokyo.ac.jp/~t-saito/publ.html ,
links this exact survey and labels it as published in Sugaku Expositions, with the author-page date 01/04/26. Page numbers here are those of the inspected author PDF; no unverified journal pagination is substituted.

The weaker corroborating survey _Galois representations in arithmetic geometry II_, §2.3, p. 10, was also saved and read, but is not needed once the displayed Theorem 3 above is available. Its local path is `saito_GR2_2002.pdf`; its source URL is https://www.ms.u-tokyo.ac.jp/~t-saito/pp/GR2.pdf .

The 2000 weight-monodromy supplement is not substituted for the compatibility theorem, and the 2009 Hilbert paper is not applied directly to Q.

## Primary semistable-module properties

**Pierre Colmez and Jean-Marc Fontaine, _Construction des représentations p-adiques semi-stables_, author PDF.**

Primary URL:
https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf

Local source:
`work/hecke_level_one/colmez_fontaine_2000.pdf` and extracted `.txt`.

PDF SHA256:
`f0b5c51191831415b39cd363cc9eb5ba759d1ea7e46d9b4c1d15cea0a7aa6490`.

The relevant passages were read in full:

* §1.5, p. 11: the construction gives N phi = p phi N and B_cris = B_st^(N=0).
* §3.3, p. 21: the category of finite (phi,N)-modules is abelian, and N carries slope alpha to slope alpha minus 1.
* §4.1, Proposition 4.2 and its following paragraph, p. 23: semistable representations are closed under subobjects and quotients; D_st is an exact tensor functor.
* §4.2, Proposition 4.4 and its full rank-one proof, p. 24: the rank-one construction uses an unramified period of unit Frobenius and a power of the cyclotomic period.

These are author-PDF page numbers. The proof only uses exactness after one finite Galois extension over which R is semistable, with its natural descent action. It does not require an unqualified exactness assertion for D_st on arbitrary p-adic representations.

## Independent reconstruction

### 1. Global characters and the classical eigenform

For an algebraic closure of Q, fixing mu_6 is equivalent to fixing mu_3. Thus a global character satisfying `KillsMu 6` factors through the order-two group Gal(Q(mu_3)/Q). In characteristic zero its only possibilities are 1 and chi_-3.

The simultaneous good-prime eigensystem of the source cusp form is supplied by a primitive newform of a level dividing the original level, by the classical newform decomposition. The source's minimal-level clause excludes a proper divisor. More weakly, merely replacing by this primitive eigenform already suffices for the conductor proof. Cofinite attachment, continuity, Chebotarev, and Brauer–Nesbitt identify R with the semisimple Deligne representation. The source irreducibility is consistent with this identification. A finite coefficient field and a finite extension defining the local flag may therefore be chosen.

The finite determinant character is interpreted with the same geometric-Frobenius convention as the attachment. Its parity is odd because the weight is 2e+1. An inverse convention for a Dirichlet character would not change the final quadratic character, but conventions should still be stated consistently.

### 2. Every prime away from ell

The actual diagonal inertia assertion, rather than only a semisimplification, implies that inertia acts through a group of order at most 2. The ell-adic cyclotomic twist is unramified at every q distinct from ell. On an open inertia subgroup, R is the identity. Hence its monodromy logarithm is zero.

At every q other than 3 and ell the two finite characters are trivial. At 3 they are 1 or chi_-3, and are tame because their orders divide 2. This gives the full local Weil–Deligne inertia and N, not merely the characteristic polynomials of unramified elements.

Carayol's primary source was checked at §0.3, p. 409, and §§0.5–0.7, pp. 410–411, including the entire Theorem (A). The extra finite discrete-series assumption occurs only when the totally real field has even degree; it does not apply to Q. The local correspondence is his Hecke normalization, involving a dual and an unramified twist relative to a common Langlands normalization. Both operations preserve conductor. The theorem therefore gives the required equality of local automorphic and Weil–Deligne conductors at q distinct from ell.

### 3. The coefficient-prime slope argument

The actual local flag has successive characters
delta_1 and delta_2 chi_ell^(-2e), with delta_i unramified. Their continuity follows from the continuous matrix representation and a fixed flag basis. Their Frobenius values are units: a continuous character of the compact unramified Galois quotient has compact image, and its valuation is a compact subgroup of a discrete subgroup of Q, hence zero.

Both characters are crystalline. After a common finite extension of Q_ell making R semistable, exactness of D_st shows that its two normalized Newton slopes are 0 and 2e, up to the harmless simultaneous sign convention obtained by dualizing. More explicitly, for an unramified residue degree f the eigenvalue valuations of phi^f differ by 2ef.

If N were nonzero, the relation N phi^f = ell^f phi^f N would force a slope difference f for phi^f, equivalently 1 in normalized slope. Since 2e is at least 2, N is zero. This is also the direct implication N(D_alpha) subset D_(alpha-1).

The descent inertia in the Weil–Deligne representation has finite image. Its two rank-one graded characters are trivial. Maschke semisimplicity for this finite image in characteristic zero forces the entire inertia action to be trivial. Thus the full Weil–Deligne representation has trivial inertia and N=0.

Saito's full theorem now implies that the classical automorphic component at ell is unramified. This step has no smallness restriction such as 2e < ell-1. It does not assert that every potentially semistable extension of two crystalline characters is crystalline; the slope gap is essential.

### 4. Exact level and trace

The nebentypus is unramified away from 3 and is tame of exponent at most 1 at 3. Its primitive conductor divides 3. Odd parity forces chi_-3. Consequently the two inertia characters at 3 have product chi_-3, so precisely one is nontrivial. Their tame conductor is exactly 1. With N=0, the classical primitive conductor is exactly 3.

At a split rational prime p distinct from 3 and ell, arithmetic Frobenius sigma has chi_ell(sigma)=p. Thus
R(sigma^(-1))=p^e W(sigma^(-1)).
All-prime local compatibility for the now identified primitive form gives trace a_p at this geometric Frobenius. The explicit W-plus-1 source decomposition yields
\[
\iota\operatorname{tr}\rho(\sigma^{-1})=1+p^{-e}a_p.
\]
For e=6 this is covered by the complete weight-13 conductor-3 space already computed. No multiplicity convention for a source trace list is needed by this particular conductor statement.

## Scope of verdict

The mathematical argument passes. Its previously missing compatibility source is now supplied by a precise, fully read primary author theorem. The original 1997 article itself was not inspected beyond metadata/preview. This audit does not independently reprove the external local-global compatibility theorem or rerun Lean. It supplies the source reading and the full independent reconstruction of the new deduction.

A final typeset version should cite the author survey's actual Theorem 3 and its PDF pagination, and the exact Colmez–Fontaine passages above. No mathematical correction to the reviewed argument is requested.

## Final TeX readback

The complete final `gl2_conductor_section.tex` and `gl2_conductor_bibitems.tex` were independently read on 2026-11-21 and pass. The requested exact source locators and the honest original-1997 retrieval status are preserved. Their reviewed SHA256 values are respectively `6419cf200c28a8ffff42aaf7778049c86a60e3f265a67767db1947632c1671c3` and `90ff482fb0cf3cc206814ecb2e7912d06fb22a62f63a09df2f1112fe796b5eda`. The combined K12 deduction has a separate complete audit in `k12_hecke_archive_audit.md`.


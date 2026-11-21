# What ZETA_NEXT changes

Date: 21 November 2026. The mathematical conclusions below are proved or refuted in the paper under the source conventions requested in the prompt. “Checked” means the whole new proof was read; the individual events and their limits are in CHECK_EVENTS.tsv. A is the supplied Alpöge theorem. M is the separately identified conditional Masullo draft claim. The previous IA01 and CONDITIONAL_AUDIT.tsv have not been redone.

## 1. The main question: explicit arithmetic bounds

The main advance over ZETA_TWO IA05 is numerical and quantitative. Its exceptional-zero descent was accepted at the level of logic; NX01 checks the original Stark constants and obtains

\[
\kappa_K>\frac{1}{173\log D_K},\qquad
h_KR_K>\frac{w_K\sqrt{D_K}}{173\,2^{r_1}(2\pi)^{r_2}\log D_K}
\]

for every normal \(K\ne\mathbb Q\). The exact denominator constant before rounding is

\[
4C_4=8\exp\!\left(\frac{21}{8}+
\frac{\gamma+2\log2}{4\log3}\right)<173.
\]

Stark, Inventiones 23 (1974), Lemma 8 is on printed p. 145, and Theorem 1′ is on p. 148, equations (24)–(25). The residue estimate is Lemma 4, equation (11), pp. 140–141. The extraction of C4 uses equation (7), p. 139, and C4=2C3, p. 141. A rational-arithmetic certificate verifies the rounding to 173. The unused c8 branch is not imported.

NX02 passes through the normal closure by transferring **zeros**, not residues: Aramata–Brauer makes the quotient of the closure zeta function by the subfield zeta function entire, and Stark Lemma 7 bounds the closure discriminant. This gives \(1/(173n!\log D_K)\) in degree n. In particular the normal-field result really propagates to all fixed-degree CM fields, without claiming their full GRH.

NX03 combines this with Louboutin 2001, Theorem 1(1), to give a two-sided effective Brauer–Siegel error interval. This applies to normal families with \(n/\log D\to0\), and to arbitrary fixed-degree families with the displayed factorial loss.

### CM class numbers, heights, and all orbit constants

| Finding | New usable statement | What closes the old gate |
| --- | --- | --- |
| NC01 | \(h_E\ge h_E/h_{E^+}>c_gD_E^{1/4}/(\log D_E)^g\), with c_g fully specified; explicit epsilon bounds and a discriminant cutoff for bounded class number | The exact CM regulator quotient, Louboutin equation (21), and NX02. A lower bound for hR is not substituted directly for h. |
| NC01, quadratic case | \(h_E>\sqrt{D_E}/(173\pi\log D_E)\), hence \(h_E>e\varepsilon D_E^{1/2-\varepsilon}/(173\pi)\) | A quadratic field is normal and has regulator 1. Earlier sharper large-discriminant IA02–IA03 estimates remain available. |
| NC02 | \(h_F(A)\le a_g\log D_E+b_g\), where \(a_g=2^{g-1}(75/2+16g!)\), \(b_g=4g(2^g-1)\) | Stark Lemma 9 excludes the exceptional zero of the relative quadratic Hecke function; Wei Proposition 5.3 and the proved averaged Colmez formula give all constants. Height normalizations are explicitly matched. |
| NC03 | Primitive full-ring CM orbit bound with exponent \(1/(16384g^3)\) and elementary constant \(\ell_g/s_g\) | All ideal quotients are defined over one field containing the endomorphisms; every comparison isogeny is E-linear. The general-dimensional Gaudron–Rémond Duke theorem supplies explicit isogeny constants. |
| NC04 | Every CM point \(x\in\mathcal A_g\) satisfies \(|\mathrm{Orb}(x)|\ge s_g^{-1}T_g^{-1/P_g}|\mathrm{disc}R_x|^{1/P_g}\), \(P_g=28672g^4\) | Rémond's maximal-order replacement stays over the same field. A controlled isogeny gives \(N\mathcal O\subset R_x\subset\mathcal O\), controlling nonmaximal orders and products. All of T_g, s_g, and P_g are explicit. |

The field factors of the centre are counted by simple isogeny component. Two distinct components can have isomorphic CM fields and must still be counted separately. Repeated isogenous factors are handled by the endomorphism algebra and by the dimension bound. No simplicity, maximal-order, or conductor restriction remains in NC04.

These results require A and the cited established arithmetic theorems. They use neither M nor the general individual Colmez conjecture. The difference from the older IA05 height statement matters: the present upper bound isolates one CM type from the **averaged** formula using a universal lower height bound.

The completed result is the effective arithmetic orbit input to Tsimerman's proof. His 2018 §6.3, Theorem 6.1, and §6.5 use counting and family reductions that, as stated there, do not provide algorithms for their constants or finite families. We do not claim that NC04 by itself effectivizes that entire procedure. For powers of the modular curve, Binyamini's Theorem 1, arXiv:1809.05302v2 §1.2, provides an effective replacement once Dirichlet GRH eliminates the exceptional quadratic field; this specialization is effective under A. The general claim “no effective André–Oort proof exists” is not made.

### The sufficient power in SA06

NX04 supplies the unconditional bound

\[
h_K\le\sqrt{D_K}\left(1+\tfrac12\log D_K\right)^{n_K-1}.
\]

It follows from Minkowski's ideal-class bound and counting ideals. Whenever SA06 B.4e's supplied finite factors have their stated meanings, its sufficient expression \(2h_K|D_p|/|\mu(K)|\) therefore has an unconditional explicit upper estimate. This does not re-prove B.4e from the abbreviated intake, and it does not repair the refuted B.4c.

The directions of regulator arguments are now explicit: a **lower** bound for hR needs an **upper** regulator bound to yield a lower bound for h. An upper hR bound needs a lower regulator bound to yield an upper bound for h. The CM lower-bound route uses exact cancellation instead.

## 2. The Λ-scheme question

The literal conjecture in the prompt is **refuted** by NX-L01. Glue two affine planes over Z along the complement of the vertical affine curve \(y^2=x^3-x\) over F5. The scheme is flat and of finite type and has commuting Frobenius lifts. Its correction at 5 is

\[
R_5(t)=\frac{1+2t+5t^2}{1-5t}.
\]

The inverse roots \(-1\pm2i\) have norm \(\sqrt5\), so they cannot be roots of unity times integral powers of 5. The construction works with any affine finite-field closed subscheme in place of the curve. It is nonseparated, a hypothesis the literal question did not exclude. Borger's definition allows it; his §6 explicitly adds separatedness.

For the proper-flat question the answer is **positive**, including bad primes. NX-L02 proves that a single Frobenius lift over Z_p gives, for finite prime-to-p coefficients, the special-fibre cohomology as the colimit of generic cohomology under the lift. Its rational form is a Galois-stable direct summand. The argument checks the strict-p-ring limit, the perfectoid and plus-ring hypotheses, the constant tilt, equivariance, and the integral Fitting projector; it does not commute colimits with rationalization without justification.

NX-L03 combines that comparison with Borger Theorem 6.1 and Corollary 6.2. Actual special-fibre cohomology is semisimple finite-Artin–Tate, and after a finite residue-field extension it is a sum of integral Tate twists. The derived splitting is noncanonical. This is a statement about realizations; no cycle-level decomposition or Tate conjecture is asserted.

The finite correction must still be retained. NX-L04 has \(X=\mu_p\): generic H0 has dimension p, its inertia invariants have dimension 2, and special H0 has dimension 1. The correction is \(1-t\). NX-L05 closes an attempted proper counterexample route: blowing up a vertical plane cubic produces \(H^3_{\mathrm{special}}=H^1(E)(-1)\) while generic H3 is zero, so that model cannot have a Frobenius lift at p.

NX-L06 proves the corrected proper Λ-RH conclusion under A: all non-real divisors lie on half-integer lines. The global primitive Dirichlet–Tate factors give lines \(j+1/2\); the local factors give integer lines j. The nonseparated counterexample also has half-integer local weight support, so it does not refute the broader half-integer-line target.

A separately imposed **separated but nonproper** version is not decided here. It would require new control of the boundary or a suitable equivariant compactification. That limitation does not leave the literal conjecture undecided.

The prompt's abelian-integer-ring example also needs its hypothesis distinguished from its conclusion. The cyclotomic local-factor shape holds, but \(Z[\zeta_5]\) has no Frobenius lift at 5: every endomorphism is an automorphism, while reduction modulo 5 has noninvertible Frobenius. This scope correction is NX-L07. DP_MULT DP11 treats the identity-Adams binomial case, not all Λ-rings.

## 3. The exact non-CM gate

NG01 closes the splitting gap in ZETA_TWO ZT06 for every pure motive of abelian type in the category of absolute Hodge cycles:

\[
M=C(M)\oplus N(M),\qquad
H_B(C(M))=H_B(M)^{(G_M^\circ)^{\mathrm{der}}}.
\]

The connected derived group is normal in the full, possibly disconnected motivic group, so the projector descends over Q. Its image is the canonical maximal potentially-CM subobject, including every finite Artin motive. Its complement has no CM subobject. Faltings supplies the semisimple ℓ-adic realization; Deligne supplies the absolute-Hodge category and its projectors. No Mumford–Tate conjecture is needed for this motivic construction.

The distinction from the largest potentially abelian subrepresentation of a fixed-ℓ tensor representation is retained. Faltings alone does not identify every higher-tensor Galois projector with a motivic one.

| Geometric input | Exact remaining functions | Finding |
| --- | --- | --- |
| Any finite-type curve over Q | \(L(B_i,s)^{m_i}\), where the \(B_i\) are precisely the non-CM Q-simple factors of the Jacobian of the smooth projective normalization | NG02; open, singular, nonreduced, disconnected, and nonseparated cases add explicit virtual Artin corrections |
| Abelian variety A of dimension g | \(L(N_r,s-k)\), \(1\le r\le g,\ 0\le k\le g-r,\ N_r\ne0\), where \(N_r\) is the CM complement of primitive degree r | NG03; exponent \((-1)^r\), weight \(r+2k\), desired line \((r+1)/2+k\) |
| \(\mathrm{MT}(A)=\mathrm{GSp}_{2g}\) | Primitive exterior-power functions of rank \(\binom{2g}{r}-\binom{2g}{r-2}\), and the specified shifts | NG04; the only CM terms are the powers of the polarization |
| \(E^m\), E non-CM elliptic | The symmetric powers \(\mathrm{Sym}^nE\), \(1\le n\le m\), with the full shifts and binomial multiplicities | NG05; continuation is known by the cited modularity and Newton–Thorne results, RH remains |

For an arbitrary A, NG03 is an exact universal representation-theoretic formula. With its actual Mumford–Tate representation supplied, the CM projector is computed by intersections of Lie-algebra kernels. No general algorithm recovering that representation from arbitrary equations is asserted.

The shortcut “remove only the CM abelian isogeny factors” is refuted. Even \(E^2\) has three Tate terms in H2. NG06 explains the imaginary-quadratic determinant mechanism for non-Tate higher CM terms; NG07 makes it explicit:

\[
A=\operatorname{Jac}(y^3=x^5-x-1),\quad
\operatorname{End}_{\overline{\mathbb Q}}A=Z[\zeta_3].
\]

This is an absolutely simple non-CM abelian fourfold, but its primitive H4 has a rank-two CM summand over Q with Hodge types (3,1) and (1,3). Zarhin's Theorem 1.1 and Examples 1.3(1) supply the endomorphism theorem for this exact family; the differential basis and projector descent are proved here.

The analytic use of the CM terms remains **conditional on M**, via ZETA_TWO CM01 and Anderson Corollary 5.7.2 / Remark 5.7.3. M must include infinite-order unitary Hecke characters. Neither A nor M is asserted to prove RH for the named non-CM functions. For curves the order identity and the holomorphy hypothesis needed to prevent cancellation are stated explicitly; for the general abelian product the list is a sufficient analytic gate, without an unjustified converse.

## 4. Grothendieck and run-by-run integration

| Programme location | Exact change or preserved boundary |
| --- | --- |
| ZETA_TWO IA05; intake §6(1)(a) | Replace statement-level Stark constants by NX01–NX03. Add NC01–NC04 as explicit consequences using averaged Colmez. |
| ZETA_TWO IA02–IA03 | Retain sharper quadratic/abelian estimates; NC01 provides a uniform all-degree CM statement, not a replacement for those sharper bounds. |
| SA06 B.4a–e; intake §4.1 | Add NC01's CM lower bound and NX04's unconditional upper bound for the class-number contribution to B.4e. B.4c stays refuted. No precise cote/scan for these rows is supplied. |
| SA06 A.8a; cote 15, scan 70 | Existing quadratic class-number and supersingular link remains IA02–IA03. The scan locator is carried, not reopened. A.8c is related, but the intake does not define its R or supply a separate scan locator. |
| ZETA_TWO ZT04–ZT05; ALPOGE_BRIDGES CC-F01b | Preserve actual finite factors. Add literal counterexample NX-L01, proper splitting NX-L03, multiplicity warning NX-L04, and corrected proper conclusion NX-L06. |
| DP_MULT DP11; cote 153, PDF scan 3/archive p. 2 | Preserve the binomial/identity-Adams equivalence; use Borger's commuting-lift criterion for general Λ-schemes. No new archival bad-fibre theorem is attributed here. |
| ZETA_TWO ZT06; intake §1 and §5.1 | Close the pure abelian-type CM-summand gap with NG01; replace the unspecified list for curves/abelian varieties by NG02–NG05. |
| ZETA_TWO ZT07 | The first non-CM elliptic gate extends to exact symmetric-power gates for E^m. |
| ZETA_TWO CM01 | Keep its conditional infinite-order Hecke scope; apply it to the actual projectors produced by NG01, NG06, NG07. |
| ZETA_TWO ZT08, SV01–SV02 | Retain the distinction between determinant information and extension/lattice information. NX-L03 gives extra actual splitting by geometry; it is not extracted from a determinant alone. NC04 separately controls an integral order by an isogeny. |
| Cote 60, scans 3 and 5 | Exterior/symmetric powers and determinant framework; SGA6 V §2, §7 (7.1.1). No new scan reading. |
| Cote 60, scan 7/archive p. 6 | Reciprocal characteristic-polynomial identity; no purity follows from reciprocity alone. |
| Cote 60, scan 9/archive p. 8 | The supplied reading explicitly assumes Weil and dual/Tate data. No transcription change or replacement of that hypothesis. |
| Cote 34, scan 64 | Struck Remark 1.17 and its tentative language remain as in the predecessor. |
| Cote 34, scan 74 | Equation (2.5.5), dimension-one Riemann–Weil context; literal multiplicative trivial group 1 is not silently changed to additive 0. |

The scheme-theoretic placement is EGA IV_3 (8.8.2) for spreading finite-presentation identities; SGA4 XII Theorem 5.1/Corollary 5.2 and XVI Theorem 2.1 for base change; XVII §§5.1–5.3 for compact support; SGA5 XV §3 no. 2 equation (1) for the trace determinant. The perfectoid comparison and the later absolute-Hodge theorems are cited at their own primary sources. No theorem in FGA is claimed to contain the new analytic estimates.

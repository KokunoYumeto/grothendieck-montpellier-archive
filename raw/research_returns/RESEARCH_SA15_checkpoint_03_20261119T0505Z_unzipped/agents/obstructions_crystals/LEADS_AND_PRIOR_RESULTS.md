# Literal leads and prerequisite audits

Updated 2026-11-19 04:00 UTC. Statements below quote the supplied, unrefereed readings; statuses distinguish their entire claims from the numbered Part E questions.

## Lead E4

- **H1-4 (the stratifying site of a singular X; 7:70-72).** The intrinsic complex of 7:70 is the Čech nerve of
  X -> X_dR (X x_{X_dR} X is the completion of X x X along the diagonal). The question is whether that nerve computes de
  Rham (infinitesimal) cohomology when X is singular; for X with an embedding in a smooth Y the infinitesimal version is
  Herrera-Lieberman and Hartshorne. Test case: the cusp C[t^2,t^3], where the intrinsic complex can be computed by the
  weight grading. Status unknown to me.

**Status and scope.** Proved in the finite type characteristic-zero setting by Bhatt Corollaries 4.19 and 4.30. The explicit cusp nerve is included in D_E_partial.tex; its positive cohomology vanishes.

## Lead E5

- **H1-5 (a corrected 7:24).** For an affine curve over C with isolated plane singularities, dim H^1 of the Kähler de
  Rham complex should be b_1 + sum over the singular points of (mu - tau) (the local H^1 of the Kähler complex has
  dimension mu - tau; zero exactly for quasi-homogeneous germs, K. Saito). To be checked against Bloom-Herrera and Saito
  (locators unverified).

**Status and scope.** Proved for reduced affine locally planar complex curves, including H2=0, by Bonnet plus the retained finite-jet argument.

## Lead E6

- **H1-3 (integral W-M invariance, 7:42-43).** For two lifts u, u' of u_0 between W-M lifts, u' - u lies in pA, and the
  homotopy coefficients are p^(m+1)/(m+1), which are integral. So the integral statement of his corollary may hold for
  W-M lifts; what remains is overconvergence of the homotopy series. Literature to check: van der Put, "The cohomology
  of Monsky and Washnitzer" (Mém. SMF 23, 1986), Davis-Langer-Zink on overconvergent de Rham-Witt cohomology (locators
  unverified).

**Status and scope.** Proved integrally for all primes and all degrees: Ertl--Sprang Proposition 1, Proposition 2, Lemma 3. Their homotopy supplies exactly the missing overconvergence.

## Lead E7

- **H2-3 (8:48-50, 8:75).** The integer alpha (t_G = pi^(-alpha) Omega^dual, depending only on A) measures the gap between
  the crystalline lattice and the Lubin-Tate tangent lattice; 8:48 gives alpha = 0 when e < p - 1. What may be true:
  alpha is governed by the different of A over W (as in Fontaine's 1982 bound for the Hodge-Tate map of p-divisible
  groups over O_K, locator unverified) and is nonzero for some e >= p - 1; this is the "double reseau" item of the 8:75
  agenda. Links: Breuil 2000, Kisin modules, Bhatt-Morrow-Scholze (the Pro notes L.25, T.29).

**Status and scope.** Proved and independently audited by the parent: alpha=0 for every A, although full lattices differ for A=Z_p[pi] with pi^(p+1)=p. The proof distinguishes the Z_p-dual inverse-different line from an A-linear dual, fixes the shifted Frobenius component convention, and compares the actual covariant special-fibre lattice. Detailed proof and all-prime source bridge are in the main TeX. The manuscript states only that full lattice equality implies alpha=0; the converse error belongs to the supplied reading, not to the manuscript.

## Lead E9

- **H1-3 (9:22, 9:29 d)).** The two isomorphisms dét (_pA)_ét ≅ dét (_pA*)_ét (de Rham, and α_A mod p) agree up to a
  constant sign c_g, multiplicative in products, so c_g = c_1^g. Grounds: rigidity of rank-one F_p-sheaves on the
  connected ordinary locus (the Igusa cover of level p is connected for g = 1).

**Status and scope.** Exact comparison proved after independent sign audits by the parent and this agent. Standard Poincaré biduality gives alpha_(A*)=alpha_A^(-1) exactly. The Hodge-first determinant/trace isomorphism beta_A:omega_A→omega_(A*) equals epsilon_g alpha_A^(-1) mod p, epsilon_g=(-1)^(g(g+1)/2); in the Tate-line direction requested, beta_A^(-1)=epsilon_g alpha_A mod p. The literal multiplicativity claim is false for odd p: epsilon_(g+h)=(-1)^(gh)epsilon_g epsilon_h, so two ordinary elliptic curves give c_2=-1 while c_1^2=1. All signs disappear at p=2. The matrix naturality check, degree-one Čech sign, canonical-lift argument (including p-divisible polarization degree), and exact finite exterior-algebra checks are retained.

## Lead E10

- **H1-2 (7:18 anticipates rigid cohomology).** His triples (U_0, V~, i) with B/pB -> A_0 of nilpotent kernel are, up to
  passing to K and to overconvergent neighbourhoods, the objects of Le Stum's overconvergent site; I expect the
  cohomology of his site, tensored with K, to be rigid cohomology for smooth X_0, so that tests a) and b) hold. Links:
  SA15-15, the letter "sur coh. p-adiques" (cote 5).

**Status and scope.** Test (a) is now refuted both integrally and rationally on the literal flat old site. The integral affine-line example detects missing p-torsion. The stronger multiplicative-group calculation proves H^1(old site,O)=0 whereas H^1_MW tensor K=K[dx/x], directly refuting the rational conclusion of the literal lead. A fibre-product detection argument checks arbitrary permitted weak formal thickenings, and a self-contained dagger finite-Nakayama lemma closes its finiteness gate. The proper test (b) is also refuted: for the supersingular elliptic curve y²z=x³−xz² over F̄₃ with its smooth proper W-lift, old-site H¹(O)=0 but H¹_dR of the lift is free of rank two. All three comparisons requested in Part E10 are now refuted, and the parent independently audited both complete proofs.

## Lead E11

**H3. The "principe d'approche transcendante" (6:14) holds for convergent F-isocrystals.** If S has a proper smooth lift
X over W with X_C simply connected, rigid GAGA for connections on X_K and Riemann-Hilbert make every convergent
isocrystal on S constant; with de Jong's full faithfulness (1995, 1998) every family of p-divisible groups over S would
then be isogenous to a constant one. Pages: 6:14-15.

**Status and scope.** Both claims are now proved with the exact proper algebraic lift and specified embedding into C. For the additional p-divisible-group claim, a fibre over a finite extension supplies an F,V-stable lattice; intersection of its conjugates and finite étale Galois descent produce one over W(k), without assuming a rational point. De Jong Theorem 4.1.1 and Corollary 5.1.2 recover the constant group and the isogeny. The original paper and the 1998 erratum were opened; the latter repairs Lemma 7.1.13.1 and leaves the corollary intact.

## Earlier results actually used

- **R5:** Read the supplied general-linear proof and independently rebuilt the necessary Steinberg relation systems. Exact modular elimination gives ranks 46 (d=3,p=3) and 177 (d=4,p=2) with inconsistency certificates; small positive groups were enumerated. The result is confirmed. Equation counts differ only because our retained system has redundant equations. The supplementary SL/Sp statements are separately proved.
- **R6:** Read the complete 9:24--29 proof. The identity Delta(u)Delta(u*)=deg(u) and Rosati symmetry force the square-root sign; rational polynomial interpolation on symmetric endomorphisms then permits the positivity argument. Self-duality of the polarization kernel makes its ordinary connected and etale p-parts have equal order, which verifies integrality. These arguments do not themselves determine the de Rham comparison sign; the previous biduality caveat remains under audit.
- **R8:** Not used in D/E proofs so far. In particular the Lubin--Tate argument uses Lau's integral crystalline realization, not the truncated-ring trace-duality assertion. No implied verification is claimed.
- **R9:** The no-PD versus PD distinction was read and respected. E3 uses the no-PD infinitesimal site and Ogus, not Grothendieck--Messing. E7 uses a modern all-prime Breuil-window theorem rather than extrapolating a nilpotent-PD deformation theorem to high ramification. Its old low-ramification calculation is valid only with nilpotent divided powers (e<p-1), as recorded in the supplied reading.
- **R10:** The supplied mod-p Frobenius argument was read and rechecked: Frobenius is flat on smooth X; its kernel thickenings are cofinal; proper finite-dimensional coherent cohomology stabilizes, and Artin--Schreier identifies the fixed Fp-space. This is the finite-level starting point of E3, not a replacement for its integral induction and inverse-limit check.
- **R11:** The two rules imply p!pi(x)=x^p by repeated addition with r=p+1, whose coefficient is a p-local unit even at p=2. Stacks Lemma 23.5.3 then gives the unique divided powers. This repairs any proof that inadvertently loses p=2. The constants c_n are exactly those in R11; the claim that all residues are 1 is false for p>=3.

No mathematical remark has been taken independently from Michel Hua's project in this fragment; supplied mentions of that project are not treated as a primary source.

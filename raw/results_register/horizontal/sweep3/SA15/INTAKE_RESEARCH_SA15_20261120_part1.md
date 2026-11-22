# Intake of RESEARCH_SA15 (cp37), part 1: the rows of packets 20-24

Claude Opus 5.5 at effort max (agent SA15-c9_c100-part2, the sweep-3 reader of cote 100 scans 3-45), 20 Nov 2026,
resumed by the main session for this intake. Brief: `field_experts/intake_20261120/INTAKE_BRIEF.md`. Part 2 (packets 25-29)
is agent afcdf31bb407576f5 (Claude Opus 5.5 at effort max). Check events: `INTAKE_RESEARCH_SA15_20261120_part1_CHECK_EVENTS.tsv`.

## 0. What was read, and the scope

- **Return read:** checkpoint 37,
  `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`
  (GPT-6 Astra, ChatGPT Pro mode), with its report (the item table at its head), `sections/*.tex` at the lines the packets
  give, and the prompt as sent (`pro_prompt_builds/RESEARCH_SA15/PROMPT.md`, Parts A-F). No earlier intake of this run
  exists.
- **My rows:** the RESEARCH_SA15 rows of packets 20-24: 510 rows (packet 20: 48, 21: 97, 22: 117, 23: 99, 24: 149). By
  file: `sections/B.tex` 335 (Part B, cote 9 and 100:48-53), `D.tex` 39 (Parts D and E), `C.tex` 26 (Part C, cote 100),
  `F.tex` 17, the `A_*` files 93 (Part A, cote 4).
- **Order of reading:** C.tex in full first (my field: cote 100, read by me in sweep 3); then the rows other rows rest on
  and the bridge-flag rows; then D, F, A; then the B rows.

- **Scope reached.**
  - Read in full: 103 rows (C 26, D 39, F 17, A 12, B 9).
  - Partly read: 3 rows (B).
  - Statement level only: 404 rows. These are A 82 (81 rows, plus A1-SMALL as a pointer), B 323, and 2 remarks of C
    (counted under "statement level" below).
- **Verdicts over the 510 rows.**

  | Verdict | Rows |
  |---|---:|
  | confirmed by a targeted check or re-proof | 61 |
  | argument followed, cited theorems carried as background, no fault found | 33 |
  | partly confirmed (the decisive step, the arithmetic, or a spot computation) | 9 |
  | statement level | 407 |

  No row of the run is refuted. Four of our own earlier statements are refuted (section 8).
- **Sections:** 1 C, 2 D-E, 3 F, 4 A foundations, 5 bridges, 6 B, 7 the other A rows, 8 what is new, 9 implications,
  10 prompt updates.

## 1. Part C (cote 100:3-45): 26 rows, all read in full

The run's own summary (report, item table): C.1 the reducedness criterion refuted and the exact essential image
determined; C.2 refuted in the stated generality, normal case proved; C.3 proved; C.4 effective on geometrically unibranch
bases, refuted on general reduced bases. I re-derived every proof in `sections/C.tex` (lines 1-1313) except the cited
external theorems, which are named below.

| Row | Statement (short) | Verdict |
|---|---|---|
| prop:C-RD3 | p locally nilpotent: the triple extends iff its reduction does | targeted proof check, confirmed (Serre-Tate, Katz 1981 Thm 1.2.1) |
| cor:C-RD4 | k[[t]][eps]/(eps^2): a), b) hold, base nonreduced, F an equivalence | confirmed; the trait case uses de Jong 1998 (cited, not opened by me) |
| prop:C-RD5 | Z_5[eps]/(eps^2), y^2 = x^3+x+(1+eps): not in the image | confirmed; j = 6912/(31+54 eps) recomputed |
| thm:C-RD6 | S normal, U dense, T of char p: F an equivalence, no excellence | argument around the citation checked; the extension itself is Krishnamoorthy-Pal, Selecta 27 (2021), Cor. 6.12 and Thm 6.3 (recorded by the run as opened; not opened by me). To check in that source: whether it covers mixed characteristic or only bases of characteristic p |
| rem auto:C:4b7cbcb1fe87 | the sweep-3 spreading argument for 100:15-17 has a gap | confirmed: a BT isomorphism is an infinite system; 8.8.2 spreads each level with neighbourhoods that may shrink |
| lem:C-RD11-ring | R = {a in V_0 : D(a) in V_0}: noetherian, dim 1, geom. unibranch, completion V[eps]/eps^2, normalization not finite | confirmed, every step |
| thm:C-RD11 | 100:3 2) fails for a reduced geom. unibranch local domain with non-finite normalization | confirmed (discriminant, R/5R = k[eps], Serre-Tate contradiction) |
| rem auto:C:3d23f9b8075d | symbolic certificate | not run by me; the identities it checks I recomputed by hand |
| rem auto:C:2b1cfc4567d4 | the BT isomorphism extends over V_0, not over R | confirmed; consistent with C-RD1 (V_0 is not finite over R) |
| prop:C-RD1 | proper epimorphisms of noetherian schemes descend BT homomorphisms | confirmed, full re-derivation (rigidity on noetherian test rings; finite image B; Omega_(B/R) = 0; Nakayama) |
| prop:C-RD2 | Hom(G,H) is not formally unramified on non-noetherian thickenings | confirmed (z_n = 1 + p^(-n) in Z_p + Q_p/Z_p) |
| thm:C-RD7 | local systems effective over reduced geom. unibranch bases | confirmed, given the closure-finiteness in Grothendieck, Invent. Math. 2 (1966), Lemma 1.2.1 (locator unverified) |
| lem:C-RD8-sections | compatible local sections of a separated unramified H glue | confirmed |
| thm:C-RD8 | reduced S with a finite geom. unibranch cover: local systems effective | confirmed (C-RD7, C-RD1, Grothendieck 1966 Prop. 1.2) |
| rem auto:C:63e1d81ef0f5 | the nodal [-1] twist is effective | confirmed (agrees with the sweep-3 hunch H5) |
| lem:C-RD9-coherent | compatible germs of a coherent module glue | confirmed |
| thm:C-RD9 | nilpotents add no obstruction to local systems | confirmed (torsor under Lie(A_0) (x) Lie(A_0^v) (x) I; H^1 = 0 on affines) |
| rem auto:C:24b235bcb6c7 | a nonreduced failure by base change of C-RD10 | confirmed |
| thm:C-RD10 | infinitely many split nodes: a local system of elliptic schemes not from S | confirmed, every step |
| rem auto:C:3a7ebde95252 | scope; Hochster 1973 not obtained | statement level; the proof does not use Hochster |
| lem:C-RD12-complete | Serre-Tate across a nilpotent thickening of a p-adically complete base | confirmed (Artin-Rees, completeness) |
| thm:C-RD12 | given a reduced realization: extends iff the punctured-completion comparison holds | confirmed, given Moret-Bailly, Bull. SMF 124 (1996), Thm 0.3 (cited) |
| rem auto:C:35345d1cc7ea | what C-RD12 removes | confirmed |
| thm:C-RD13 | exact essential image by formal models and quasi-affine charts | confirmed in structure, given Moret-Bailly 1996 Thm 1.1, 1.2 (cited) |
| cor:C-RD14 | elliptic case: algebraization and atlas automatic | confirmed (EGA III 5.4.5; Moret-Bailly QPROJ case) |
| rem auto:C:cfff6b2c31f1 | relation of C-RD12 and C-RD13 | confirmed |

**What changes for the reading of cote 100.**
- 100:3, part 2): false for non-reduced bases in mixed characteristic (C-RD5, my sweep-3 counterexample made explicit);
  true when p is nilpotent and the reduced case holds (C-RD3, C-RD4), so the failure is not "nonreducedness" but the
  comparison over the punctured completion (C-RD12, exact). Also false for a reduced, geometrically unibranch base whose
  normalization is not finite (C-RD11): **his "O.K." on 100:11 for the non-finite normalization is wrong**, and the
  refined statement of my sweep-3 reading ("2) holds for S reduced", c9_c100_part2 correction row 2) is refuted. The
  right hypothesis is his own boxed one on 100:7 ("si le normalisé de S_red est fini sur S"). True for S normal
  (C-RD6, resting on Krishnamoorthy-Pal).
- 100:25, Corollary 3 (descent of p-divisible groups along proper epimorphisms): true over noetherian bases (C-RD1), by a
  route other than his ("X formellement net" is false for non-noetherian thickenings, C-RD2).
- 100:17, the local-system lemma marked "Douteux, sans doute faux": **his doubt is right**. False for a reduced,
  one-dimensional, noetherian Q-algebra with infinitely many nodes (C-RD10); true on reduced geometrically unibranch
  bases and on reduced bases with a finite geometrically unibranch cover (C-RD7, C-RD8); nilpotents change nothing
  (C-RD9). My sweep-3 hunch H4 ("may target non-reduced bases") is refuted: the failure comes from infinitely many local
  twists, not from nilpotents.
- 100:15-17: my sweep-3 re-proof of the local-to-global step has a gap at the spreading of the BT isomorphism
  (rem auto:C:4b7cbcb1fe87). The claim "case e) follows from case d)" stands unproved in that form.
- Not settled in my rows: 100:3 part 2) for a reduced base with finite normalization that is not normal (his case d)
  needs effective descent of abelian schemes along the finite epimorphism S' -> S, his 100:27-45).

## 2. Parts D and E (cotes 5-9): the 39 rows of `D.tex`, all read in full

| Row(s) | Statement (short) | Verdict |
|---|---|---|
| thm:DE-split | GL_d(Z/p^2) -> GL_d(F_p) splits iff d = 1 or (d,p) = (2,2),(2,3),(3,2); SL_d: d = 1, (2,3), (3,2); Sp_2g: (g,p) = (1,3) | confirmed: the p >= 5 argument ((T-1)^(p-1) = 0, so (U+pX)^p = 1+pE_12) and the SL_2 mod 4 parity argument re-derived; the three positive cases recomputed by me (groups of orders 6, 48 with determinant-one part 24, and 168, each mapping isomorphically onto GL_2(F_2), GL_2(F_3), GL_3(F_2)); the (3,3) and (4,2) inconsistency certificates not rerun (the sweep-3 c7_c8 readers recomputed the same list); Sp_2g for g >= 2 cited to Detinko-Flannery-Hulpke 2018, Thm 2.5. Known in substance (Sah, J. Algebra, 1974/1977, locator unverified) |
| rem auto:D:fa384818cda6 | supplements versus complements | confirmed |
| lem:DE-kappa | kappa = 0 iff V lifts to a free Z/p^2-module | confirmed (change of rings) |
| lem:DE-free-ci, thm:DE-coherent-obstruction | an explicit smooth projective threefold S = Y/GL_d(F_p) with xi != 0 for every nonsplit (d,p) | confirmed: eigenspace bound for the nonfree locus, base-point freeness and tangent separation of the norm system, Bertini on the free locus, H^1(Y,O) = 0, injective edge map of Cartan-Leray; the co-Lie identification cited to Bergh-Rydh 2019, Prop. B.4 |
| rem:DE-universal-negative | on curves xi = 0 although kappa != 0 | confirmed (coherent H^2 of a curve is 0) |
| thm:DE-PD-pi | PD structures = maps pi with the two rules (E.1, cote 5:41); c_n = prod (a_i!)^(-1) mod p | confirmed: c = ((p+1)^p - (p+1))/p! is a p-local unit (c = 3 at p = 2), so p! pi(x) = x^p; Stacks 07GS cited; Wilson's congruence re-derived |
| prop:DE-E2-coherent, lem:DE-crystal-Fdiv, prop:DE-E2-Fpure, prop:DE-E2-flat-charzero, lem:DE-Fdiv-universal-homeomorphism, prop:DE-E2-cusps, prop:DE-E2-relative-Frobenius, cor:DE-E2-relative-node | positive comparisons of crystals and stratifications | argument followed; the derived comparisons are cited (Gaitsgory-Rozenblyum 2014 Prop. 3.4.3; Tonini-Zhang 2019 Thm 6.8; Mesablishvili 2000 Thm 4; Ben-Zvi-Nevins 2004), not opened by me; the elementary steps (nilpotent Nakayama, B^q in A, the Frobenius splitting of R[x,y]/(xy)) re-derived |
| thm:DE-E2-counterexample | a finite free X over a non-noetherian F_p-algebra where restriction is not faithful | confirmed, every step: t^(p^n) b_(n+1) = b_n since s_(n+1) = s_n + p^n; delta_T = b_n z^(p^n) independent of lift and of n; on R[x]/(f^2), delta_T = b_1 x^p = b_1 f != 0 |
| cor:DE-E2-Noetherian-counterexample | the same over F_p[t] with the coefficient crystal O_T (x) I | confirmed |
| rem:DE-E2-Noetherian-scope | role of the manuscript's insertion "du moins si R loc. noeth., et se bornant aux Modules cohérents" | confirmed |
| prop:DE-E2-coherent-faithfulness, lem:DE-E2-completed-Cech | faithfulness; the exact completed Čech complex | confirmed (Krull intersection, flat local maps; split Čech nerve mod I and finite filtration) |
| prop:DE-E2-flat-Noetherian, cor:DE-E2-coherent-any-field, thm:DE-E2-coherent-Noetherian, the scope remarks | the manuscript's noetherian coherent version of 6:7 (1.8) is true | argument followed; rests on Jiang 2023 (derived crystals), cited, not opened by me; the ordinary steps (H^0 of a D^(<=0) object, nilpotent Nakayama, extension to arbitrary tests) re-derived |
| thm:DE-inf | H^i((X/W)_inf, O) = H^i_et(X, Z_p) (x) W, integrally (E.3) | known (Ogus, Ann. ENS 1975, Cor. 4.7, 4.11, cited); the local-embedding extension followed |
| thm:DE-intrinsic-nerve | the completed nerve computes de Rham cohomology; the cusp is contractible (E.4) | known (Bhatt 2012, Cor. 4.30, cited) |
| thm:DE-curves | dim H^1 = b_1 + sum (mu - tau), H^2 = 0 for reduced affine planar curves (E.5) | confirmed given Bonnet 2006 Thm 1.2 (cited); the local length tau and the global surjectivity of d re-derived; agrees with the sweep-3 c7_c8 correction to 7:24 (quasi-homogeneous points give no defect) |
| thm:DE-integral-MW-independence | integral Monsky-Washnitzer independence (E.6) | known (Ertl-Sprang 2018, Prop. 1-2, cited) |
| prop:DE-LT | alpha(A) = 0; the full lattices differ for pi^(p+1) = p (E.7) | the last step re-derived (R/pi_act R = F_p[pi_base]/(pi_base^(p+1)), so the first factor of g(pi) is not integral); the window computation (Lau 2014) followed, not re-derived; refutes the sweep-3 c7_c8 hunch H2-3 |
| thm:DE-hasse | beta_A^((p-1))(sigma_A) = sigma_(A*) exactly (E.8, cote 9:22) | confirmed (F = C diag(pI, I), det C = 1, Jacobi's complementary minor) |
| thm:DE-ordinary-sign | alpha_(A*) = alpha_A^(-1); beta_A = eps_g alpha_A^(-1), eps_g = (-1)^(g(g+1)/2) (E.9, cote 9:29) | the arithmetic re-derived (eps_(g+h) = (-1)^(gh) eps_g eps_h; eps_2 = -1); the Čech sign convention followed, not independently re-derived |
| prop:DE-old-site, lem:DE-weak-finite, thm:DE-old-Gm, prop:DE-old-proper | the literal site of 7:18 fails all three tests (E.10) | followed in full; spot checks: H^0(C, O/p) = k on A^1; [x^(p-1)dx] killed by p and not integrally exact; y^2 = x^3 - x is supersingular in characteristic 3 with Delta = 64 |
| thm:DE-simply-connected-convergent, cor:DE-BT-constant | E.11 under a proper smooth lift with simply connected complex fibre | argument followed; rests on Esnault-Shiho 2018 and de Jong 1995 (cited) |

## 3. Part F: the 17 rows of `F.tex` in my packets

- rem:DE-quote-D1 ... rem:DE-quote-E11 (13 rows): each maps a page (cote and scan) to a result of D.tex; read in full;
  consistent with the D/E verdicts above. Two of them change the reading of the archive: 8:81 "sans doute pas nulle"
  is wrong exactly for (d,p) = (2,2), (2,3), (3,2); 7:24's cusp example does not show the defect (mu = tau there).
- prop:DE-R7 (ordinary stratification exists iff A_0 ordinary, 9:16-18), prop:DE-R8 (Dieudonné duality over D_n with
  W_(n+1) in place of W_n, 9:5-8), prop:DE-R9 (no functorial ordinary stratification of H^1_dR, 6:22-27), prop:DE-R10
  (7:16-17): read in full. Spot checks: the normal form of D_n has length (n+1)^2; the Legendre family at p = 3,
  H_3(lambda) = 1 + lambda = t at lambda = 2 + t, Delta = 64 at t = 0; at p = 2, y^2 + txy + y = x^3 has
  Delta = t^3 - 27 = t^3 + 1 mod 2 and Hasse invariant t. R9 agrees with STUDY.md §2 (check event SA15-S3-5).

## 4. Part A (cote 4): the `A_foundations.tex` rows, read in full (11 rows)

| Row | Statement (short) | Verdict |
|---|---|---|
| A-ALG-FITTING | semilinear Fitting decomposition; stable part exact | confirmed (standard; Ogus 1975 Lemma 4.8) |
| A-R1 | F nilpotent on H^j(X, O_X(-d)), j < n; stable coherent weak Lefschetz | confirmed; this is the sweep-3 proof of 8.5.7 (STUDY.md §1, SA15-S3-3; readings/check_8_5_7.md) |
| A-R2 | the edge map H_dR -> H(O) is an isomorphism on stable parts | confirmed; Lemma 8.4.3 by the same F = beta alpha, alpha beta argument (STUDY.md §1, SA15-S3-1) |
| A-NAKAYAMA | integral Nakayama for perfect complexes over a DVR | confirmed (universal coefficients) |
| A1-HIGH (thm:A-high-degree) | integral crystalline weak Lefschetz for d >= max reg(Omega^j) | confirmed (Serre duality puts RGamma(Omega^a(-t)) in D^(>=n); conormal resolution; derived Nakayama); BMS 2016 Lemma 2.12 cited |
| thm:A-all-degree-ranges | all d >= 1 for complete intersections, or n <= p with a W_2-lift | argument followed; rests on Cotner-Zavyalov 2024, Thm 2.2.3 (cited, not opened by me); the complete-intersection cone argument re-derived |
| A2-EXACT (thm:A-exact85) | 0 -> T^n(X)[p]_ss -> (E/pE)_ss -> E(Y,O_Y)_ss -> 0, every d; 8.5.10 both ways | confirmed (stable universal coefficients, A-R1, snake lemma) |
| A2-UNIT (thm:A-unit-count) | for k = F_q, dim (E/pE)_ss = number of p-adic unit reciprocal roots of P_van, every d | confirmed given two citations: Ogus 1975 Thm 4.9, Cor. 4.11 (slope-0 part = etale Z_p (x) W, with torsion) and Katz-Messing, Invent. Math. 23 (1974), Thm 1 (crystalline and l-adic characteristic polynomials agree degree by degree); the mod-p weak Lefschetz and derived Nakayama over Z_p re-derived |
| A1-TRANSPOSE (prop:A-transpose-u2) | the transpose of i^* on T^n[p] is Gysin; = d c_1 cup on T^(n-1)/p | confirmed (linking pairing, projection formula, self-intersection); answers what (8.2.1) on 4:4 must be |
| A2-STAR-DUAL (prop:A-star-dual) | (*) and (**) of 8.4.4 (4:2) are dual, with V the Poincaré adjoint of F | confirmed; settles his "Sans doute (*) et (**) sont transposés l'un de l'autre" (4:2), with the operator convention made explicit |
| A1-SMALL (rem open:A-small-degree) | A.1(a)-(c) false; exact degree ranges | statement level here; its proofs are in the A_*_counterexample files (rows in packets 23-24, section 5 below) |

## 5. Bridges (criterion of the brief, corrected 20 Nov ~21:1x UTC)

Alpöge: L. Alpöge, *Remark*, https://alpo.ge/remark.pdf, with the Lean archive (files at
`Papors/Chatnotes/Zeta-Function-Foundation/literature/alpoge_rh_20261120/`). Deligne: *La conjecture de Weil* I (Publ.
Math. IHES 43, 1974) and II (52, 1980).

**A genuine purity bridge, used by the run.**
- **A2-UNIT (thm:A-unit-count; 8.5.4 on 4:7).** His count is of the eigenvalues of Frobenius on the vanishing part of
  H^(n-1) that are p-adic units. The run identifies it with dim (E/pE)_ss through Katz-Messing (1974), Thm 1: for
  X smooth projective over F_q, the characteristic polynomial of Frobenius on H^i_cris (x) Q equals the one on l-adic
  H^i, for each i. That theorem is a consequence of Deligne's purity (Weil I, Thm 1.6). The zeta function alone fixes
  only the alternating product of the P_i, and the weights q^(i/2) separate the factors. So purity is what makes the
  l-adic statement of 8.5.4 equal to a crystalline and coherent rank. What the row gives back: nothing to purity; it is
  a consumer of it. Alpöge's RH carries nothing here: the setting is over a finite field, where the Riemann hypothesis
  is Deligne's theorem.
- **thm:DE-inf, prop:DE-R10 (E.3, 7:16-17).** The slope-0 part H^i_et(X, Z_p) (x) W is, over F_q, the unit-root
  factor of the zeta function. The row is stated over an algebraically closed field and uses no zeta function. The
  link to the l-adic P_i again goes through Katz-Messing, and so through purity; the row uses neither.

**A genuine use of the Weil conjectures (Lang-Weil), flagged.**
- **thm:projective-all-residues (A_monodromy.tex:543; the consequence in 8.6, 4:9-12).** For P^n over F_q and
  d >= pn + 1, every nonempty open of degree-d hypersurfaces contains, over a finite extension F_Q, a smooth Y with
  #Y(F_Q) = t mod p for any prescribed t. Mathematics of the link: the point counts are the coefficients of the zeta
  function, and mod p they are read from the slope-0 part, #Y(F_(Q^e)) = 1 + (-1)^(n-1) Tr(Frob_(Q^e) | V_Y) mod p
  (the coherent trace congruence of SGA 4 1/2, "Fonctions L modulo l^n et modulo p"). The proof uses Lang-Weil (a
  consequence of Weil's Riemann hypothesis for curves) to put rational points in an open of a geometrically integral
  variety, and finite Chebotarev on W_d, whose effective form rests on the same bounds. Deligne's purity would give
  the archimedean size |#Y(F_Q) - #P^(n-1)(F_Q)| = O(Q^((n-1)/2)), which a mod-p statement does not need. What the row
  gives back: the slope-0 side of these zeta functions takes every residue mod p in every open set; nothing to RH.
  Alpöge's RH: no role (function-field setting).

**Rows whose link carries nothing, with the reason.**
- **Part B, all rows on T_p, T_l, the cyclotomic character, Tate twists and Hodge-Tate weights** (flagged: thm:B-RD1,
  prop:B-RD3, prop:B-RD4, prop:B-RD4-dictionary, prop:B-RD5, lem:B-RD17-degree, prop:B-RD32, prop:B-RD41, lem:B-RD52-CM,
  thm:B-RD52, thm:B-RD80). They concern representations of G_K for a p-adic field K: Z_p(1) restricted to G_K is the
  p-adic realization of the Tate motive at one place. RH and GRH (Alpöge) are statements about zeros of global
  L-functions and give nothing at one place. Purity gives, for potentially good reduction, Frobenius eigenvalues of
  weight 1 on the reduction (Weil 1948 for abelian varieties); the rows use only finite-order inertia, whose traces are
  sums of roots of unity, independent of l (Serre-Tate, Ann. of Math. 88 (1968), Thm 2), so purity is not used either.
  What the rows give back, stated exactly: by prop:B-RD4-dictionary, under potential semistability the manuscript
  character is the inertia trace chi of the Weil-Deligne representation of V. For a finite inertia image I_0, the
  degree of the local Euler factor at p is dim V^I = (1/|I_0|) sum over g in I_0 of chi(g), and on tame inertia chi
  fixes the tame part of the conductor exponent, codim V^I. So B.4 (thm:B-RD42, thm:B-RD48, thm:B-RD49 and the rows
  under them) asks at which torsion level M(nu) the degree of the local L-factor at p and the tame conductor of V are
  determined. That is local information on L-functions; it says nothing about zeros. The Tate twist in (B-RD4.1) shifts
  L-factors, L_p(V(n), s) = L_p(V, s+n): the same shift that makes GRH for chi the RH of chi (x) Q(n). It leaves the
  inertia trace unchanged, since inertia acts trivially on D_cris(Q_p(1)). prop:B-RD4 gives back a negative fact:
  the manuscript condition admits M whose V is not de Rham (nonzero nilpotent Sen operator). Such a V is not the
  p-adic realization of any motive (realizations of motives are de Rham at p, Faltings 1988), so it has no motivic
  L-function and no weight. lem:B-RD52-CM, thm:B-RD52 (formal CM): global CM curves have Hecke L-functions of
  infinite-order characters, outside Alpöge's GRH for Dirichlet characters, and these rows are local anyway.
- **thm:DE-hasse, thm:DE-ordinary-sign** (flagged for T_p(A)). Over F_q, ordinarity means that the Newton polygon of
  P_1(A, T) has only slopes 0 and 1 (Manin), i.e. g eigenvalues are p-adic units. These are p-adic invariants;
  purity (|alpha| = q^(1/2)) is not used, and the rows hold over arbitrary F_p-schemes. thm:DE-ordinary-sign uses the
  positivity chi(L) = sqrt(deg lambda) > 0 of a polarization only to fix a sign. The Rosati positivity behind it is how
  Weil proved RH for abelian varieties over finite fields (the abelian case of the positivity in the standard
  conjectures), but the row gives nothing back to it.
- **prop:DE-E2-coherent** (flagged "purity/weights"): the word is F-purity of a ring map (N -> B (x) N injective,
  Mesablishvili), unrelated to purity of weights. Nothing.
- **lem:char2-group-inputs** (flagged for "l(2)"): ord_l(2) and primitive prime divisors of 2^a - 1 (Zsigmondy).
  Elementary; no L-function. Nothing.
- **A rows on the Hasse-Witt local system** (prop:projective-generic-hw-rank, thm:plane-all-residues,
  thm:all-X-explicit-positive-rank, cor:eventual-hodge-parenthesis, thm:relative-ordinarity-fails-smooth,
  thm:odd-plane-char2-obstruction): V is the slope-0 (unit-root) part, an F_p-local system; its Frobenius traces are
  the zeta function mod p. The monodromy questions are the characteristic-p analogue of the big monodromy in Weil II
  (Picard-Lefschetz for l-adic vanishing cycles), with no use of purity. thm:plane-all-residues has the same link as
  thm:projective-all-residues.
- **A1-TRANSPOSE**: cup product with d c_1(O(1)) on p-torsion in one degree. Hard Lefschetz and the positivity of the
  standard conjectures concern rational cohomology; nothing.
- **Parts C, D.1-D.2 and E.1, E.2, E.4-E.7, E.10-E.11**: none treats the listed topics (E.11 uses only the topology of
  a simply connected complex fibre).

## 6. Part B (cote 9:10-14, with 100:48-53): 335 rows, from thm:B-RD1 to rem:B-RD100-scope

**Read in full (9 rows).**

| Row | Statement (short) | Verdict |
|---|---|---|
| thm:B-RD1 | for every odd p: K with e(K) = (p^2-1)/2, mu_p in K, E with E[p] in E(K), additive supersingular potentially good reduction, defect 2, inertia trace -2 | confirmed: [p](T)/T is Eisenstein of degree p^2-1 (height 2), so F(E_0[p]) is the cyclic tame extension of that degree acting freely on E_0[p] - 0; its involution acts as -1; mu_p is fixed (det(-1) = 1); the twist by delta = y(P)^2 makes E[p] rational; Néron-Ogg-Shafarevich excludes good reduction |
| thm:B-RD2 | Q_3(zeta_3), y^2 + y = x^3: E[3] in E(K), defect 6 | confirmed: Delta = -27, j = 0, psi_3 = 3x(x^3+1); the eight points (0,0), (0,-1), (x,y) with x in {-1,-zeta,-zeta^2}, y in {zeta, zeta^2} lie over K; v_K(Delta) = 6 excludes good reduction; the degree-six extension followed |
| prop:B-RD3 | mu_p in K, potentially good ordinary, A[p] unramified: good reduction, any dimension | confirmed (connected-étale splitting; Serre's lemma for finite-order automorphisms congruent to 1 mod p, p >= 3). Known in substance |
| cor:B-RD6 | the "cas test" of 9:13 is negative for every odd p | confirmed: E of B-RD1 and the canonical lift E' of an ordinary curve have isomorphic p-torsion over K, inertia traces -2 and 2 at the involution |
| prop:B-RD4 | a height-two BT group over Q_p(zeta_p) satisfying the manuscript condition, not potentially Hodge-Tate | confirmed (rho = (1, p^(-1) log chi; 0, 1); Sen operator nonzero nilpotent; Berger 2004 §II.1.2) |
| prop:B-RD4-dictionary | under potential semistability the manuscript character is the inertia trace of D_pst(V) | confirmed in structure; (B-RD4.1) is Kisin 2006, Lemma 2.2.4 and Cor. 2.2.6; exactness Fontaine 1994 (cited) |
| prop:B-RD5 | height one: nu = 0 | confirmed (values in mu_(p-1): Teichmüller lift of the mod-p character; Brauer character across filtrations) |
| lem:B-RD60-break | v_E(gx - x) >= v_E(x) + b(g), equality iff p does not divide v_E(x) | confirmed (expansion with coefficients from D; the degree-A change is A d varpi^(A+b)); standard (Serre, Corps locaux IV, locator unverified); used by 19 rows |
| lem:B-RD49-inertia | p >= 5: the faithful good-reduction extension is tame cyclic of degree dividing p^2-1 | confirmed given lem:B-RD17-degree (finite subgroups of the quaternion units have order prime to p for p >= 5, as Q_p(zeta_p) has degree p-1 > 2, and embed in F_(p^2)^x); used by 13 rows |

**Partly read (3 rows).**
- thm:B-RD26-wild (the sharp wild criterion at p = 3): the sufficiency construction followed (A, B of (B-RD26.11),
  descent by the subgroup of order m); necessity is prop:B-RD20 and the construction uses lem:B-RD26-trace-arc,
  neither read.
- cor:B-RD27-exact-three: the formula N(e) = 1 + min(s, floor((L+1)/2), floor((L+s+1)/4)) is consistent with B-RD26
  (m = 12 gives e >= (2/3) 3^max(2n-2, 4n-4-s), i.e. n-1 <= s, (L+1)/2 and (L+s+1)/4); at e = 216 (u = 108, s = 3,
  L = 4) it gives N = 3, and e >= (2/3)·243 = 162 holds, so full 27-torsion with defect twelve is allowed, as stated.
- thm:B-RD42 (nu_min(3,2,2) = 2): the proof skeleton followed; it rests on prop:B-RD29, thm:B-RD34, prop:B-RD35,
  B-RD37, B-RD38, B-RD40, B-RD41 and the two B-RD42 lemmas, not read.

**Statement level only (323 rows).** The other B rows (the B.2 tame range B-RD7 to B-RD13, the B.3 rows B-RD14 to
B-RD27, the B.4 rows B-RD28 to B-RD100 with their lemmas and remarks) were read as statements in the packets. No fault
is claimed and none is excluded. The run records independent audits and exact certificates for most of them; I did not
rerun those.

## 7. Part A: the other 82 rows (packets 23-24)

- **thm:projective-all-residues: read in full, confirmed.** The hyperplane union Y_0 (t Frobenius orbits of n
  hyperplanes and one orbit of d - nt > n, in general position) has exactly t rational points and lies in W_d
  (bijective Frobenius of rank binom(d-1, n)). The coherent trace congruence and finite Chebotarev then give a smooth Y
  in any open set with the same residue. The bound d >= pn + 1 leaves room for the long orbit when t = p - 1.
- **The other 81 rows: statement level.** They are:
  - the A.1 counterexamples: `A_injectivity_counterexample`, `A_integral_counterexample`, `A_surface_counterexample`,
    `A_coherent_counterexample`, `A_product_degrees`, `A_injectivity_degrees`;
  - the A.6 rows of `A_lifting`;
  - the abelian-surface and monodromy rows: `A_ppav_two_jets`, `A_nonordinary_*`, `A_theta_torsion_avoidance`,
    `A_char2_uniform`, `A_route_limitations*`, `A_full_radical_image_structure`, `A_mixed_six_three_seed`, and the
    other `A_monodromy` rows.

  One cross-check against our results: the A.1 counterexamples refute only the ingredients 8.3 admits ("Nous
  admettrons", 4:4). They do not touch 8.5.7, which the run reproves as A-R1, in agreement with sweep 3
  (STUDY.md §1).

## 8. What is new

Against the literature (as far as I know, and as the run's source census records) and against our own results:

- **New, and checked by me:**
  - C-RD11: 100:3 2) fails for a reduced, geometrically unibranch base with non-finite normalization. The ring is a
    classical analytically ramified one, put to new use.
  - C-RD10: the local-system lemma of 100:17 fails on a base with infinitely many nodes.
  - C-RD1: descent of BT homomorphisms along proper epimorphisms of noetherian schemes. This answers Corollary 3 of
    100:25.
  - C-RD12 to C-RD14: exact criteria for the essential image, by formal gluing.
  - The E.2 counterexamples: DE-E2-counterexample and its noetherian version.
  - B-RD1, B-RD2 and B-RD6: explicit answers to the cas test of 9:13.
  - The D.2 threefold with ξ ≠ 0.
  - thm:projective-all-residues.
- **Our own results, made explicit or reproved:**
  - C-RD5 is the sweep-3 counterexample (c9_c100_part2, check event 100:7), with an explicit curve.
  - A-R1 is the sweep-3 proof of 8.5.7.
  - A-R2 is Lemma 8.4.3, as checked in sweep 3.
  - DE-split agrees with the c7_c8 recomputation.
- **Known, with locators:**
  - D.1: Sah 1974/1977 (locator unverified).
  - E.1: Stacks 07GS.
  - E.3: Ogus 1975.
  - E.4: Bhatt 2012.
  - E.5: Bonnet 2006; Dimca-Greuel 2018.
  - E.6: Ertl-Sprang 2018.
  - E.8: Bijakowski 2018, in substance.
  - C-RD6: Krishnamoorthy-Pal 2021.
  - B-RD3: Serre's lemma.
- **Corrections to our own records.** I did not edit the files concerned (`readings/c9_c100_part2_CORRECTIONS.tsv`,
  `readings/c7_c8.md`), because the brief limits my writing to the intake files.
  - (1) The refined statement in my sweep-3 reading ("100:3 2) holds for S reduced", c9_c100_part2 correction row 2) is
    false, by C-RD11. The hypothesis needed is his own boxed one on 100:7: the normalization of S_red is finite.
  - (2) My sweep-3 check event (100:15, 100:17) claimed a re-proof of case e). It has a gap where the BT isomorphism is
    spread (rem auto:C:4b7cbcb1fe87).
  - (3) My sweep-3 hunch H4 is refuted by C-RD10.
  - (4) The c7_c8 hunch H2-3 (the different forces α ≠ 0) is refuted by prop:DE-LT.

## 9. Implications for the reading of the archive, and for the programme

- **Cote 100** (detail in section 1):
  - 100:3, part 2) is true in three cases: for normal S; when p is nilpotent and the reduced case holds; and exactly
    when the punctured-completion criterion of C-RD12 and C-RD13 holds.
  - It is false for some non-reduced S (C-RD5), and for some reduced, geometrically unibranch S with non-finite
    normalization (C-RD11). So his "O.K." on 100:11 is wrong.
  - Corollary 3 of 100:25 holds over noetherian bases (C-RD1).
  - His doubt on 100:17 ("Douteux, sans doute faux") is justified (C-RD10).
- **Cote 9:**
  - 9:13: the cas test is negative (B-RD6).
  - Full p-torsion with additive reduction exists for every odd p (B-RD1), and over Q_3(ζ_3) (B-RD2).
  - 9:11: the monodromy condition is weaker than potential semistability (B-RD4).
  - 9:22: the Hasse invariant transports exactly (E.8).
  - 9:29: the sign is ε_g = (−1)^(g(g+1)/2) (E.9).
  - 9:5-8: the duality holds with W_(n+1) in place of W_n (R8).
  - 9:16-18: an ordinary stratification exists iff A_0 is ordinary (R7).
- **Cote 8:**
  - 8:81: the universal obstruction is zero exactly in the three small cases; the coherent class is nonzero on an
    explicit threefold and zero on curves (D.1, D.2).
  - 8:48-50: α = 0, and the full lattices can differ (E.7).
- **Cote 7:**
  - 7:16-19: the old site gives étale Z_p ⊗ W, and all three "tests décisifs" fail (E.3, E.10).
  - 7:24: the correction stands (E.5).
  - 7:42-43: his integral independence is true (E.6).
  - 7:70: settled for finite-type complex schemes (E.4).
- **Cotes 5 and 6:**
  - 5:41: the two rules suffice, and c_n is not always 1 for p ≥ 3 (E.1).
  - 6:7: his inserted proviso (noetherian base, coherent modules) is exactly what makes the equivalence true (E.2).
  - 6:14: true under the lift hypothesis (E.11).
  - 6:22-27: agrees with STUDY.md §2 (R9).
- **Cote 4:**
  - 8.5 holds unconditionally (A2-EXACT, A2-UNIT).
  - The ingredients that 8.3 admits are false in general, and true for d ≥ d_int(X) (A1-HIGH).
  - (8.2.1) on 4:4 is settled (A1-TRANSPOSE).
  - The remark on 4:2 is right, with V the adjoint of F (A2-STAR-DUAL).
  - The consequence of 8.6 holds for P^n with d ≥ pn + 1.
- **Programme:** the companion to the "Cristaux" dossier can state Part C, Parts D-E and A.2 as settled, with the
  checks above. The open edges, as the run's own summary also has them:
  - Part C: the reduced case with finite normalization;
  - Part B: the general least index of B.4;
  - Part A: A.3-A.4 for general X.

## 10. Prompt updates for a successor of RESEARCH_SA15

1. Part C: decide 100:3 2) for reduced S with finite normalization of S_red (his boxed hypothesis, 100:7). Prove or
   refute effective descent of abelian schemes along the finite epimorphism S' -> S (his route, 100:27-45), or decide
   it through the criterion of C-RD13.
2. C-RD6: open Krishnamoorthy-Pal (Selecta 27, 2021) and state whether Corollary 6.12 covers normal bases of mixed
   characteristic. If it does not, give the mixed-characteristic proof: Tate's full faithfulness for normal domains
   with generic characteristic 0, then the extension of the abelian scheme.
3. 100:15-17: decide whether the local-to-global step holds when the BT isomorphism must be spread uniformly. That
   means a proof by an algebraicity-locus argument, or a counterexample of C-RD10 type that carries a p-divisible
   group.
4. Part B: give ν_min(p, e, h) in general, or its strongest proved reduction. State the link with it: ν_min is the
   torsion level that fixes the degree of the local Euler factor at p and the tame conductor (section 5).
5. For every row that touches Tate twists, weights or zeta functions, state the bridge as in section 5: the local or
   global link, and what purity or GRH gives there.
6. Sources:
   - open Moret-Bailly (Bull. SMF 124, 1996);
   - open Grothendieck (Invent. Math. 2, 1966), Lemma 1.2.1 and Prop. 1.2;
   - open Hochster (1973);
   - search the literature on elliptic curves over local fields with full p^n-torsion and additive reduction, and
     check B.3 against it.

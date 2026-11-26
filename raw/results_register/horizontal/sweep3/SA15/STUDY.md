# SA15 (Cristaux), sweep 3: unit-root eigenvalues in vanishing cohomology, the Dieudonné crystal and the turn to divided powers, Néron models and p-divisible groups

Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. Read in sweep 3, in full: cote 4, scans 2-12
(`MPL_8_079-081+9+4+100`); cote 6, scans 22-27 (`MPL_5+6_001-037`); cote 100, scans 48-53 (`MPL_8_079-081+9+4+100`).
Not read in sweep 3 (the budget ran out first): cote 5 (divided powers, the p-adic letter), cote 6 scans 1-21 and 28-67
(including the Tate-Hodge pages, read on the images in part 2), cote 7, cote 8 (F-crystals, Dieudonné-Manin, Tannakian
categories of crystals), cote 9, cote 100 scans 3-45; that is items SA15-1 to -8, -10 to -15, -17, -18, -20. The order
follows sweep2/SA15/WHAT_IS_WHERE.md.

## 1. Unit-root Frobenius eigenvalues in the vanishing cohomology of hypersurface sections (cote 4) — SA15-9

His section "8. Une estimation (heuristique) du nombre des valeurs propres de frobenius dans la cohomologie évanescente
qui sont des unités p-adiques", on IHES paper, with the joined sheet 8.4.4 (4:2). X smooth projective connected of
dimension n over a perfect k of characteristic p, Y a smooth hypersurface section, E(Y) = Coker(H^(n-1)(X) -> H^(n-1)(Y)).

- **8.1 (4:3)** a crystalline cohomology H(X) "au sens des catégories dérivées" with H_DR(X) = H(X) (x)^L_W k and the
  universal coefficient sequences; "Sauf erreur, ceci marche dès maintenant pour p != 2, grâce à Berthelot". The snake
  lemma for X and Y gives (8.1.3).
- **8.3 (4:4-5)** "Nous admettrons" weak Lefschetz with torsion for crystalline cohomology (E(Y) torsion-free,
  Tors^(n-1)(X) = Tors^(n-1)(Y), Ker u_0 = 0); u''_2 is cup product with the polarization class.
- **8.4 (4:5-6)** semisimple parts V_SS for p-linear endomorphisms (an exact functor); 8.4.2 these are F_p-local systems,
  or Galois representations over F_p. **Lemma 8.4.3:** for X proper over k, H^i_DR(X) -> H^i(X, O_X) is an isomorphism on
  semisimple parts, by the Hodge spectral sequence (Frobenius is zero on E_1^(a,b) for a != 0).
- **8.4.4 (4:2)** F is nilpotent on H^i(X) (x) k, Tors^i (x) k and pTors^i for i > n, so
  (H^n (x) k)_ss = H^n(X, O_X)_ss; dually for V and i < n.
- **"Théorème" 8.5 (4:6-8)** granting the crystalline ingredients: the exact sequence (8.5.1) with
  v: H^(n-1)(X, O_X)_SS -> H^(n-1)(Y, O_Y)_SS; for k finite, the rank of (E(Y) (x) k)_SS is the number of unit-root
  Frobenius eigenvalues on the vanishing cohomology; (8.5.5) and the inequality (8.5.6)
  dim (E(Y) (x) k)_SS >= dim E(Y, O_Y)_SS.
- **8.5.7** "Je pense que l'homomorphisme v de (8.5.2) est injectif"; true if n = 2 or if H^(n-1)(X, O_X(-d)) = 0.
  **Proved in sweep 3 for every smooth ample Y, n >= 2** (check event SA15-S3-3): let x be in the semisimple part with
  v(x) = 0. Choose k with H^(n-1)(X, O_X(-p^k Y)) = 0 (Serre duality and Serre vanishing, since n - 1 < n). Write
  x = F^k(x_k) with x_k semisimple; v(x_k) = 0 because F is injective on the semisimple part of H^(n-1)(Y, O_Y); so x_k
  comes from y_k in H^(n-1)(X, O_X(-Y)), and x = F^k(x_k) comes from F^k(y_k) in H^(n-1)(X, O_X(-p^k Y)) = 0. (The
  standard Frobenius-amplification argument; with it, the "seulement si" of 8.5.10 holds without his reservation.)
- **8.5.8-8.5.10 (4:8-10)** constancy of the number of unit roots on an open U_d of hypersurfaces of degree d; he wants it
  nonzero for d large, which (8.5.6) reduces to dim E(Y, O_Y)_SS > 0, "établi au n° 7" (not in this cote); the local
  systems over U_d; phi bijective iff (pTors^n(X))_ss = 0.
- **8.5.11 (4:11)** dim H^(n-1)(X, O)_SS = dim H^(n-1)(X̄, Z/p) >= dim((H^(n-1)/Tors) (x) k)_SS, and Serre's example from
  the Mexico symposium (locator unverified) (a free Z/p quotient of a complete intersection, H^1 = 0 but H^1(X, Z/p) = Z/p) shows phi need not
  be injective.
- **8.6 (4:12)** the question: is the representation of pi_1(U_d) on V = E(Y, O_Y)_ss irreducible, with image all of
  Aut(V)? Then, with the Woods Hole formula and Chebotarev, over a finite field every nonempty open set of hypersurfaces
  would contain Y with card Y(k') congruent mod p to any prescribed residue; "malgré l'assistance de gens compétents comme
  Katz, il ne semble pas qu'un résultat de cette nature soit prouvé (même si X = P^2)".
- **Checked:** Lemma 8.4.3 (SA15-S3-1, a two-line proof: F_DR = beta alpha and F_O = alpha beta, with alpha the augmentation
  and beta induced by x -> x^p, so alpha is an isomorphism on semisimple parts); 8.4.4 a) (SA15-S3-2); 8.5.7 (SA15-S3-3,
  proved); the unit-root count of 8.5.4 (SA15-S3-4).
- **Status.** His heuristic section, conditional on crystalline foundations that came later (Berthelot 1974). 8.5.7 is
  true. His aim in 8.5.8 (unit roots in the vanishing cohomology of a general hypersurface section of large degree) follows
  from Illusie's generic ordinarity of complete intersections in projective space ("Ordinarité des intersections
  complètes générales", Grothendieck Festschrift II, Progr. Math. 87, 1990, 375-405), as far as I know. 8.6 is open on the page; I have not determined its status.

## 2. The Dieudonné crystal of an abelian scheme, and why the infinitesimal version fails (cote 6, scans 22-27) — SA15-16

Pages 20-25 of a numbered manuscript (sections 1.10-2.7, with a "Chapitre 3" on formal groups announced).

- **6:22** the Frobenius DR(f)^(p) -> DR(f) and, by duality, V with FV = VF a power of p: the de Rham isocrystal is a
  bi-isocrystal. "je m'étais canulé": DR^i(f) is a bi-crystal of weight i only given an isomorphism (not an isogeny)
  DR^i = (DR^(2d-i))^dual (x) T^-(d-i), which exists "très exceptionnellement".
- **2.4 (6:22-23)** for an abelian scheme, DR^1 is a bi-crystal of weight 1, a Dieudonné crystal. First assertion:
  H^1_DR of a lifting B over T depends only on A over S and S -> T. Second: over a perfect field it is the classical
  Dieudonné module. **2.5 (6:24)** "Je n'ai pas vérifié ... mais n'ai pas le moindre doute"; third assertion: liftings of A
  correspond to liftings of the Hodge filtration (an equivalence of categories).
- **2.6 (6:25-26)** Serre's universal vector extension G(A) of A by V(t_A*), whose Lie algebra is dual to the Hodge
  sequence; a crystal in smooth groups; the canonical connection of G(A), met while simplifying Manin's Picard-Fuchs map.
- **6:27** what he has verified: a) characteristic 0; b) G(A) has no infinitesimal automorphisms, so canonical absolute
  stratifications (margin "faux"); c) first-order liftings (dual numbers). **2.7:** "je m'aperçois avec consternation
  qu'elles sont fausses telles quelles": no stratification of H^1_DR(A/S) relative to k, functorial and compatible with
  base change, exists for all elliptic schemes, because Frobenius M^(p) -> M would be horizontal, and F^2 = 0 at a point of
  Hasse invariant zero would spread to its infinitesimal neighbourhoods, false for the modular family.
- **Checked:** the self-correction of 6:22 (SA15-S3-6); the counterexample of 2.7 (SA15-S3-5), and that it fails once
  divided powers are used (t^p is horizontal and vanishes at 0 without vanishing nearby).
- **Status.** Known since: the three assertions hold for nilpotent PD thickenings (Grothendieck's ICM 1970 address;
  Messing, LNM 264, 1972; Mazur-Messing, LNM 370, 1974; Berthelot-Breen-Messing, LNM 930, 1982). 2.7 is the reason the
  theory needs divided powers: it refutes the version over arbitrary nilpotent thickenings, which is what 1º-3º state.

## 3. Néron models and p-divisible groups (cote 100, scans 48-53) — SA15-19

- **100:48-51** a typescript, "Modèles de Néron et groupes p-divisibles" (100:53 calls its theorem "le th. de Raynaud"):
  over a trait S, a morphism from the generic fibre of a p-divisible group H to a Néron model G (generic fibre
  semi-abelian) extends uniquely; Lemmas 1-3; the semi-stable case by Tate's theorem twice, then base change and the Weil
  restriction; "le théorème de Tate, qui en toute rigueur n'est démontré que lorsque eta est de caractéristique 0".
  Corollary: good reduction iff the p-divisible group extends. His margin on the theorem: "[ ] inutile" (the
  semi-abelian hypothesis).
- **100:52-53** his handwritten extension: for any algebraic group G over K and a p-divisible M -> G, the map factors through
  a semi-abelian subgroup (centralizers stabilize; for p = char K through p^nu G, semi-abelian for nu large; for K perfect
  with no G_a, G is semi-abelian); then, for G Néron over S, the morphism extends by Raynaud's theorem for the Néron model
  of that subgroup. **Checked** (SA15-S3-7): the argument is right; G_K has no G_a because it has a Néron model; the case of
  K imperfect of characteristic p is covered by his case 1. This justifies "[ ] inutile".
- **Status.** Known: SGA 7 IX (Grothendieck's criterion); Tate's theorem in characteristic p of the generic fibre is de
  Jong (Invent. Math. 134, 1998).

## How it connects

- SA15-9 uses SA15-1 (crystalline cohomology in the derived sense, 4:3), SA15-2 (p-linear Frobenius, 4:5) and the
  Lefschetz theorems of SA06-6 (4:4). SA15-16 uses SA15-1 and SA15-2 (6:22-23). SA15-19 uses SA15-16 (p-divisible groups,
  100:48-50).
- The supersingular curves are the obstruction in 6:27 (2.7) and the subject of SA06-8 (15:34-78): the same points that
  make the motivic gerbe of F_p non-split at p (SA05-18) make the infinitesimal de Rham crystal impossible.
- Wrong on the pages: nothing that he did not correct himself (2.7 and the margin "faux" on 6:27 b)).

<!-- readers:start -->
## Sweep 3 readers (files in readings/; rows folded into CHECK_EVENTS.tsv and CORRECTIONS.tsv)

- **readings/check_8_5_7.md**: independent check of 8.5.7 by a922466087ec53798 (Claude Opus 5.5 at effort max), written without seeing our argument. Verdict: v is injective for every n >= 2, every d >= 1 and every smooth Y. Frobenius twists carry the kernel into H^(n-1)(X, O_X(-p^e d)), which is 0 for e large. His two cases are special cases. The claim in §1 (check event SA15-S3-3) now has an independent re-proof.
- **readings/c5_c6.md**: cote 5 and cote 6 scans 1-21, 28-67: 113 scans. Read by a1cf7c6b5992a5d3b with sub-readers a5d23772f38c43927 and a486000d1ad547de6, all Claude Opus 5.5 at effort max. 102 check events, 46 corrections, 20 hunches. 5:49-53 is his own letter to Deligne of 10 Dec 1965, an unsigned typed copy he kept; the docket in his hand reads 'Lettre à Deligne'. Sweep 2 recorded it as another's letter, so SA15-15 and SA15-20 are relabelled. 6:2-32 is his letter to Tate ('Pise, Mai 1966'), which dates the manuscript of §2 (H3).
- **readings/c7_c8.md**: cotes 7 and 8: 147 pages. Read by afcdf31bb407576f5 with sub-readers a28f4edc0783f3d6a and aa78098b7d78d6642, all Claude Opus 5.5 at effort max. 61 check events, 44 corrections, 18 hunches. On 8:81 he expected the universal obstruction to lifting the representation of GL(d, F_p) to Z/p^2 to be nonzero for d >= 2 ('sans doute pas nulle'). It is zero exactly for (d, p) = (2,2), (2,3), (3,2) and nonzero in every other case (recomputed and re-proved).
- **readings/c9_c100.md**: cote 9 (29 pages) and cote 100 scans 3-45 (43 pages), read by a8d07e7854f1cb9b4 with the sub-reader a8d91f19c2d8f19c1, both Claude Opus 5.5 at effort max. 48 check events, 29 corrections, 15 hunches. Part 2) of his Theorem on 100:3 is false over non-reduced bases: a Serre-Tate counterexample over Z_p[eps]/(eps^2). It holds for reduced S; the gap is his step a) on 100:7, which he marked '?' twice. 9:14 'faux par Tate': his expectation holds for ordinary reduction (proved) and fails for supersingular reduction (a sketched counterexample over Q_p(zeta_(p^2)), resting on Kisin's theory and Illusie's lifting theorem). Cote 100 is probably from 1968, not March 1967.
<!-- readers:end -->

## Integration of POLISH_CRISTAUX, checkpoints 13-18 (23 Nov 2026)

Added by Claude Opus 5.5 at effort max (agent a512cf71295c14ccb). The polish run of this study (prompts 92 and 92b,
GPT-6 Astra, ChatGPT Pro mode) has 21 papers at checkpoint 18; the intake is
`field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_CRISTAUX_20261123_cp18.md`.
- **Cote 8:49 answered** (Paper 19): Lubin-Tate lattices agree iff e <= p; extremal containment exponents max(0, e - p);
  tangent images always agree. Targeted check of the mechanism in the intake.
- **Cote 8:81 extended** (Paper 8): least non-split co-Lie rank 4, 3, 2 for p = 2, 3, >= 5, realized on surfaces.
- **The inertia-character question (SA15-B chain)** (Paper 2, now 120 pages): exact wild bands
  nu_min(p, p^v(p-1), 2) = v + 1 and nu_min(p, k p^v(p-1), 2) = v + 2 for 2 <= k <= p - 1; a bracket at every wild index;
  nu_min(p, (p^2-1)p^v, 2) = v + 2; and v + 2 for all k <= p^2 outside an explicit exceptional set of size
  (3p-5)/2 + floor((p-2)/3). Read at statement level with arithmetic consistency checks; the proofs carry only the run's
  same-model reconstructions.
- **Hyperplane-section monodromy in characteristic two** (Papers 18, 20, 21): full GL_8(F_2) and GL_80(F_2) for degree 1
  and 3 sections of the square of y^2 + y = x^3; GL_8 on an ordinary open; F_2^96 x| GL_32 for quadrics; invariant
  covectors 2^f - eps_A. Statement level, with genus and rank consistency recomputed.
- Correction carried from the cp12 intake: full rational 27-torsion with additive reduction first occurs at e = 162, not 216.

## Integration of POLISH_CRISTAUX, the final (23 Nov 2026)

Added by Claude Opus 5.5 at effort max (agent a512cf71295c14ccb); intake
`field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_CRISTAUX_20261123_final.md`.
- **Two threads.** The run's final (sealed 18:48 UTC, 18 papers, 461 pages) continues the original prompt 92 from
  checkpoint 13. Checkpoints 16-18, described in the block above, belong to the continuation 92b, which also started
  from checkpoint 13. The final therefore lacks the 92b results: the E_p theorem of Paper 2, the proper integral H^1
  comparison of Paper 9, and 92b's Papers 18, 20, 21 (invariant covectors; GL_8 and GL_80 monodromy). Its Paper 18 is
  92b's Paper 19 (the Lubin-Tate lattices, 8:49). Merging the threads is open.
- **What the final adds.**
  - Paper 2: exact bands nu_min(p, k p^r (p-1), 2) = r + 2 for 2 <= k <= (p^2-1)/2, p not dividing k or k = p, and
    r + 3 for p | k, k >= 2p.
  - Paper 2: the first open coefficient k0 = (p^2+1)/2. At e = k0 (p-1) p^r and n = r + 3, an unequal-character pair has
    a forced normal form (equal Hasse parameters, opposite tangent scalars, split residual representations), and its
    image is not in the principal nonsplit Cartan.
  - Paper 8: the complete table of sections of GL_d, SL_d and Sp_2g(Z/p^2) over F_p.
  - Paper 10: eventual generic defect two for every positive-index mixed pair in characteristic two.
- **Checks in that intake.** The two threads' Paper 2 values agree on 1,595 overlapping cases. Seven small cases of the
  section table were recomputed by exhaustive search. The alpha_2 theta-descent lemma of Paper 10 was re-proved. The
  Monsky-Washnitzer half of Paper 9's affine theorem was checked.
- **Index convention.** nu_min(p, e, 2) is the least nu such that M[p^(nu+1)] determines the character, so nu = 2 means
  p^3-torsion (Paper 2, introduction.tex line 14). The values above and in the block before are the paper's nu.

## Thread B of POLISH_CRISTAUX to checkpoint 22 (24 Nov 2026)

Added by Claude Opus 5.5 at effort max (agent a512cf71295c14ccb); intake
`field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_CRISTAUX_20261124_threadB_cp22.md`.
Thread B (the 92b continuation) did not stop at checkpoint 18. Its checkpoint 22 (filed 21:45 UTC on 23 Nov) was still
an active snapshot.
- **The inertia-character question, whole band.** Paper 2, thm:next-wild-band-complete: nu_min(p, (p-1)p^v k, 2) = v + 2
  for every v >= 0 and 2 <= k <= p^2 with p not dividing k, and v + 1 at k = 1. The exceptional set E_p of the block
  above is gone. The reduction to the single multiplier p^2 - (p-1)/2 (thm:single-exception-recovery) had a targeted
  check, given three carried inputs. Its exchanged case forces p^2 | k + (p-1)/2, so it also excludes thread A's open
  boundary k = (p^2+1)/2. The exclusions of the last multiplier at every v were read at statement level only.
- **Weak-formal cohomology.** Paper 9:
  - H^1(C_X, O[1/p]) is rigid H^1 for every smooth separated X of finite type, with no lift (thm:nolift);
  - integral H^1 is p-torsion-free and injects into it (thm:integral-rational-injection);
  - on the affine line, integral H^2 contains a countable direct sum of K/W (thm:affine-second-torsion; the H^2
    deduction was checked).
  - Thread A's remark on "the absence of p-torsion on the affine-line site" holds only in degree one.
- **Hyperplane sections in characteristic two.** Paper 21:
  - the Hasse divisor in |3d Theta| on an ordinary principally polarized surface is reduced, of degree 9d^2 (the degree
    was recomputed);
  - full GL_8 on an ordinary moduli open;
  - an actual GL_8 block for every d >= n + 1.
- **Naming trap.** The two threads use k0 for different numbers: thread A's (p^2+1)/2, thread B's p^2 - (p-1)/2.

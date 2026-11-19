# SA14 (Picard), sweep 3: the Picard scheme, its existence, separation and finiteness, Lefschetz-Grauert, and the functional equation

Merged by Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 19 Nov 2026. Two readers, both Claude Opus 5.5 at
effort max, read every scan of cotes 57-60:
- aa478f9ff10218651 read cote 57, 315 scans: `readings/c57.md`;
- a262249a0710a599b read cotes 58, 59 and 60, 162 scans: `readings/c58_c60.md`.

The item-by-item study, in page order, is in those two files. This page gives what the topic contains, what is new,
what is wrong and what is open. Nothing is left unread. Scans 14-88 and 180-225 of cote 57 and 58:2-19 and 59:2-28 have
only one transcription (Codex web/Work); a Pro pass is needed before they can be edited (DELIVERABLES.tsv).

## What the pages contain

**Cote 57: the Picard dossier, 1961-1962.**
- **Existence and separation of Pic_{X/S}:**
  - the criteria of equivalence on hyperplane sections, 57:97 (SA14-3);
  - properness of Pic^0 for normal X, 57:100;
  - Seshadri's theorem, 57:103-111 (SA14-4): a Weil divisor that is Cartier on the generic fibre and has no vertical part
    is Cartier;
  - separation through units and rational sections, 57:115-124;
  - relative existence by rigidification and descent, 57:125-140;
  - the Picard functor and its variants Prépic and Prépic', 57:173-179.
- **Curves:**
  - the Picard group of a reduced complete curve, with its multiplicative and additive parts, 57:147-155;
  - the Abel map and its tangent sequence, 57:164;
  - the Kummer class ξ_n = δ_n(η), 57:141-145 (SA14-17);
  - pinching, 57:298-304 (SA14-8).
- **Formal and local Picard:**
  - the letter to Hironaka (Neuilly, 6 July 1962) on Picard groups of germs and formal neighbourhoods, 57:227-231;
  - Pic of a formal scheme in characteristic 0, 57:233-264 (SA14-5);
  - "Local Picard schemes", 57:3-13 (SA14-6).
- **Néron-Severi and finiteness:**
  - polarizations and the Néron-Severi scheme, 57:274-281 (SA14-7);
  - Igusa's example and planned counterexamples, 57:283-297;
  - a family where the divisibility of an NS class jumps, 57:289-290;
  - finiteness after Matsusaka, Igusa and Kleiman, 57:67-72;
  - the letters to Murre of 18 July 1962 ("Problem A"), 57:73-79.
- **Group schemes and extensions:**
  - rigidity and rigid group schemes, 57:14-58 (SA14-9);
  - the Albanese scheme, 57:59-64;
  - the universal extension by divisors with connection, 57:80-88 (SA14-2);
  - pseudomorphisms, 57:166-171 (SA14-18);
  - Picard and Albanese for non-complete varieties, 57:305-306;
  - his open questions on the structure of Pic_{X/S}, 57:308-315;
  - the plan of a treatise on Picard, 57:65-66 (SA14-13).

**Cote 58: Lefschetz-Grauert.**
- connectedness in dimension ≥ h;
- Lefschetz-Grauert pairs, with π_0, π_1 and Pic under (LG);
- permanence for projective flat morphisms;
- vanishing, finiteness and an algebraization theorem;
- Picard groups of projective cones;
- the local connectedness theorem and the local Lefschetz theorem for π_1, with a conjecture on 58:19 (SA14-3, SA14-6).

**Cote 59: the determinant of cohomology on Picard torsors.**
- the map NS_{X/S} → NS_{B/S} computed by Riemann-Roch;
- the inversion of polarizations of abelian schemes;
- powers of the torsors Pic^δ and the Albanese torsor;
- principally polarized abelian schemes and their canonical class.

**Cote 60: "Notes sur l'équation fonctionnelle" (SA14-10).**
- characteristic polynomials and the λ-ring of power series;
- the functional equation over F_p, proper and non-proper;
- for curves, the virtual inertia invariants E^♮ and the local constants;
- the normalization, and "niveau".

## What is new, wrong or settled (details and proofs in the readings)

- **57:111, his Question 2, is false as stated** (aa478f9f).
  - Counterexample: X = Spec k[[t]][x,y,z,w]/(xy − z² − t²) with D = V(x, z − it). The fibres are normal, but D is
    not Cartier along a 3-fold node.
  - The refined form is proved: S regular and fibres R_2.
  - The smooth case is Ramanujam-Samuel.
- **57:144:** the relation ξ_n = δ_n(η) that he marked "à vérifier" is re-proved, up to sign. This is the Kummer
  comparison that sweep 2 located.
- **57:100:** the kernel in his corollary has Lie algebra of dimension h¹(X, O_X(−1)). It is nonzero exactly when
  Kodaira vanishing in degree 1 fails for O_X(1).
- **57:70:** Igusa's b₂ as written lacks a factor 2 (his slip).
- **60:53:** his open question "δ^♮² = q^{χ^♮} ?" has the answer yes (a2622492, §2.5(d)). His correction terms μ_x
  vanish for every E, so E ↦ E^♮ commutes with duality.
- All corrections are in CORRECTIONS.tsv (30 from cote 57, 14 from cotes 58-60). The check events are in
  CHECK_EVENTS.tsv (100 + 40).

## What is open

- **His open questions on Pic_{X/S}** (57:308-315): separation, finite type, and the behaviour of Pic^τ.
- **The local Lefschetz conjecture of 58:19:** finite generation of the local étale fundamental group. This is RP-S2.
- **The canonical points of the torsors Pic^δ** (59:10-14, 26-28) and the sign of the Albanese torsor (59:23-25). This
  is RP-S3.
- **The 6 packages of cote 57** (RESEARCH_PACKAGES.md).

## How it connects

- SA19 (Jacobians): generalized Jacobians, Rosenlicht theory and the duality of Néron models (cote 43); Albanese
  equivalence (cote 44).
- SA18 (abelian varieties): Picard of abelian schemes (cote 49); polarizations (59:10-14).
- SA06-3 and SA06-7 (Albanese, zero-cycles, cote 14).
- SA15 (crystals): the universal extension, 57:89-92, against 6:25-26.
- SA05: the Kummer class 57:144 and the period questions of the motives dossiers.

<!-- readers:start -->
## Sweep 3 readers (files in readings/; rows folded into CHECK_EVENTS.tsv and CORRECTIONS.tsv)

- **readings/c57.md**: cote 57, all 315 scans (about 230 of them his own mathematics). Read by aa478f9ff10218651 (Claude Opus 5.5 at effort max): 100 check events, 30 corrections, 13 hunches, 6 packages. His Question 2 on 57:111 is false as stated: X = Spec k[[t]][x,y,z,w]/(xy - z^2 - t^2) and D = V(x, z - it) has normal fibres, but D is not Cartier along a 3-fold node. A refined form is proved (S regular, fibres R_2); the smooth case is Ramanujam-Samuel. 57:144: the relation xi_n = delta_n(eta) is re-proved up to sign. 57:100: the kernel has Lie algebra of dimension h^1(X, O_X(-1)). 57:70: Igusa's b_2 lacks a factor 2.
- **readings/c58_c60.md**: cotes 58, 59 and 60, 162 scans. Read by a262249a0710a599b (Claude Opus 5.5 at effort max): 40 check events, 14 corrections, 9 hunches, 2 packages. His open question on 60:53, delta^nat^2 = q^{chi^nat}, has the answer yes: the corrections mu_x vanish for every E, so E -> E^nat commutes with duality (§2.5(d)). The packages are RP-S2 (finite generation of the local étale pi_1, 58:19) and RP-S3 (canonical points of the torsors Pic^delta, 59:10-14 and 59:26-28).
<!-- readers:end -->

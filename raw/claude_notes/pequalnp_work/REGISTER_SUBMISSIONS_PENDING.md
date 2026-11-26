# What session 672ae3a0 submits to the results register

Session 672ae3a0, the pequalnp session (Claude Opus 5.5 at effort max), 25 Nov 2026 15:3x UTC. This file lists what goes in
once the main session's tools in `results_register/` are ready (submit_check.py, submit_relation.py; HOW_TO_SUBMIT.md
pending).

The user, P9852-P9857: a register that every checker submits into, with what was checked and what was found, and the
relations already settled, so that no check is redone and no settled link is dismissed. Nothing is running here: every
intake of this session finished before the cancellation at 15:32 UTC.

## Checks (scope, verdict, who, where), all by Claude Opus 5.5 at effort max

| File | Rows | What |
|---|---|---|
| `pequalnp_work/square_note/CHECK_EVENTS_GATE1_20261125.tsv` | 18 | Gate 1: runs 98 (cp12) and 99 (cp09), the five hinge statements; af3258db |
| `Documents/field_experts/intake_20261121/intakes/VPVNP_HINGE/INTAKE_VPVNP_HINGE_20261125_CHECK_EVENTS.tsv` | 3 | SH-60b, PG-OP-DETERMINISTIC spot checks; a5ef71dd |
| `.../VPVNP_WIRE_GEOMETRY/INTAKE_VPVNP_WIRE_GEOMETRY_20261125_CHECK_EVENTS.tsv` | 3 | Q4n re-derived; a5ef71dd |
| `.../THETA_CIRCUIT_SIZE/INTAKE_THETA_CIRCUIT_SIZE_20261125_CHECK_EVENTS.tsv` | 5 | Theorem 1.1 read in full; the 18-gate circuit on all 4,096 inputs; a4ee2342 |
| `.../FLEET_HARD_LINKS/INTAKE_FLEET_HARD_LINKS_20261125_cp07_CHECK_EVENTS.tsv` | 4 | The weighted level-space bound, every step; a4ee2342 |
| `.../COUNTING_VARIETIES/INTAKE_COUNTING_VARIETIES_20261125_CHECK_EVENTS.tsv` | 3 | Height-one proposition, exact-height reduction, fixed thresholds; a5ef71dd |
| `.../MOONSHINE_AFTER_ALPOGE/INTAKE_MOONSHINE_AFTER_ALPOGE_20261125_CHECK_EVENTS.tsv` | 5 | `landau_window` hypotheses, Mellin identity, off-line zeros; a74a9a15 |
| `Documents/reports_20261124/INTAKE_PILE_20261124/CONFERENCE/papers/SQUARE/CHECK_EVENTS.tsv` | 12 | The square note's proofs, including Lemma 2.10 (F(beta) < 4, proved there); af3258db |
| `.../SPLIT_ZERO_AFTER_FGJM/FLEET_647_CHECK_20261124.md` | — | L-meta-647 against paper 4, Theorem 1.1, remark (a)-(c); this session |

Also the checks recorded inside our own files:
- the 23 Nov targeted check of the L-meta-647 proof: fleet_map/FLEET_MAP.md, line 583;
- the 67c deposit checks: Documents/reports_20261124/grh_algorithms_67c/RECORDS.md (v1 and v2);
- the lambency-6 pass's computations: moonshine/lambency6_checks/;
- the atlas checks: moonshine/atlas_checks/.

## Settled relations (so they are never dismissed again)

| Source | Rows | What |
|---|---|---|
| `Documents/reports_20261124/INTAKE_PILE_20261124/FLEET_MAP.tsv` | 63 | Pile items to fleet nodes: settles / sharpens / same statement / parallel / input / uses / no node |
| `pequalnp_work/mirror/extension/EXTENSION.tsv` | 48 | Our public entries and the fleet nodes each attaches to and uses |
| `pequalnp_work/fleet_mirror/INTAKE_FLEET_MAPS.md` | 42 ids | Fleet nodes named in the main session's intakes |
| `pequalnp_work/moonshine/LAMBENCY6_PASS.md` | 13 findings | The user's lambency-6 / 3-2 leads (see below) |
| `pequalnp_work/moonshine/MOONSHINE_ATLAS.md` | — | How the moonshine appearances map onto each other (swarm, 23 Nov) |
| `pequalnp_work/square_note/GATE1_CHECK_20261125.md` | — | The VP/VNP hinge equivalences, strongest checked form |

The relations of the lambency-6 pass are settled, by computation and proof, with no second reader. They are user-led and
must never be called "unrelated" again:
- 2 × 3 = 6 made exact: V ⊗ Sym²V = Sym³V ⊕ (V ⊗ det). The user's [the user's words, omitted] is det = χ₋₃, Alpöge's sign.
- PG(2,3) with its polarity is the plane of sl₂(F₃).
- The (2,3,6) triangle group maps onto the Singer group with polarity.
- GL(2) × GL(3) → GL(6) (Kim–Shahidi) is the GRH-side form of the same 2 × 3.

Its corrections are settled too: P205's monodromy is not Sp₄(F₂); Codex's three signs at j = 2304 are not χ₋₄, χ₋₃,
χ₁₂.

## The register's test case: "how did lambency show up in a complex structure on S6"

The chain, with locators, to go in as relations when the formats arrive. The fields are filled per the user's rule:
- HEXAGON: "not yet" for every link below;
- NEW: "new" for C4, settled by our computation; "known" for Bolza and the octahedral group.

1. **The S6 example.** In the S6 series on complex structures on S6, Paper II's example P205 has two elliptic curves over
   three double fibres, through double covers.
   - Relayed by the user from the S6 intake, 23 Nov: `moonshine/INPUT_S6_PAPER_II_III_FINDINGS_relayed.md`, lines 7-26
     and 71.
   - The S6 intake note on 02L5: `Documents/task_notes/INTAKE_S6_SERIES_PUBLISH_cp51_20261123.md`, lines 20-100.
2. **The user's lead** (23 Nov): it is the same 3-2 pattern as GL(2)/GL(3) in the GRH work and lambency 6 = 2 × 3
   (`INPUT_...relayed.md`, lines 26-36).
3. **The link, settled: finding C4 of the lambency-6 pass** (`moonshine/LAMBENCY6_PASS.md` §0, line 79).
   - P205's six ramification points {0, ∞, ±1, ±i}, of the base cover t = (z + 1/z)²/4, are the octahedron's vertices.
   - They are the Weierstrass points of the Bolza curve.
   - The Bolza curve's automorphism group, the binary octahedral group ≅ GL₂(F₃), is the umbral group of lambency 6
     (A5^4 D4).
   - P205's deck involutions lift through it.
4. **What fails** (same file, "What fails"): the Sp₄(F₂) = S₆ explanation of P205's level-2 match. P205's monodromy
   preserves no symplectic form.

## Not submitted until the user says otherwise
- The square note (on hold; the conference is cancelled).
- The rebuild of prompt 102 (held as Q90).

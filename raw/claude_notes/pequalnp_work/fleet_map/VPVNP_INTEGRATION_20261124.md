# The two VP ≠ VNP claims and our GCT material (24 Nov 2026)

Written by Claude Opus 5.5 at effort max (agent a4348514ce0275bbf, the agent that built the joint GCT lemma space), at the
request of main session 329fb1e6 (Claude Opus 5.5 at effort max), 24 Nov 2026 about 20:00-21:30 UTC. Reading and writing
only; nothing was sent anywhere. Work file: `<local>/Documents\agent_notes\a4348514ce0275bbf_NOTES.md`.
Corrected 24 Nov 2026.

**What these claims are.** No human mathematician has checked either.

- **Anthropic, "VP ≠ VNP over every field".**
  - Its author is given as Claude, "found by an internal research Claude model"; the release names no model version or
    effort setting.
  - It was posted 23 Nov about 21:00 UTC with a 324-file Lean development.
- **OpenAI, "VP and VNP are different".**
  - Its author is given as OpenAI; it names no model.
  - It was committed 24 Nov 01:20 UTC.

**What I read.**

- **Anthropic:**
  - `Statement.lean` in full, which is standard;
  - `Challenge.lean`, `Solution.lean` and the README;
  - pages 1-12 of the paper through `p1-12.txt`: Section 1, Section 2 in full, and Section 3. The mathematical glyphs
    are lost in that text, so a few formulas are read from context.
- **OpenAI:**
  - `Paper.tex` lines 1-345: abstract, introduction, the hinge, the no-shortening proof, the stretch theorem and the
    replay and boundary lemmas;
  - its last page;
  - `Challenge_VPVNP.lean`, `ClassSeparation.lean` and the head of `Valiant_Project.lean`.
  - Its bibliography file (`references.tex`) is not in the local copy.

**Not read.** Neither paper's appendix or proofs beyond these sections. Every check below is against the statements and
the overviews; it is marked so where it matters.

The verdict table is `VPVNP_NODE_VERDICTS_20261124.tsv`, with 33 rows. The claims are now external nodes (side
`external`) of `JOINT_GCT_LEMMA_SPACE.tsv`: 8 rows and 17 edges, with backups `*_before_vpvnp_20261124.*`.

## The five most useful findings

1. **One architecture and one open hinge.** Both proofs are win-win arguments over the same question: whether the cost of
   wires in tensor networks can be beaten below Euclidean length.

   - **If it cannot** (Anthropic: "flat"; OpenAI: "no strict shortening"), the argument is direct. A small circuit
     splits the coefficient tensor of a clause-sum polynomial over balanced cuts (Anthropic `lem_balanced`; OpenAI's
     "usual balanced-product decomposition"). A hub moved toward the resultant of the wires that cross a cut then saves
     length, a contradiction.
     - Anthropic uses the complete network and gets 2^Ω((log m)^{4/3}).
     - OpenAI uses an expander and gets exp(Ω((log n)^{5/4})).
   - **If it can** (Anthropic: "contracting"; OpenAI: "strict shortening"), the circuit lets weighted sums over the runs
     of short programs be accelerated, and a diagonal argument refutes it.
     - Anthropic gets 2^Ω((log m)^2/log log m).
     - OpenAI gets 2^{n^σ}.
   - **Neither decides which case holds.** Anthropic: "We do not know which of the two hypotheses holds, even over R, nor
     do we show that the two are mutually exclusive."
   - **How the two dichotomies nest.**
     - **Shortening defeats flatness at every scale.** Over every field, a strict shortening (OpenAI, Definition 2.1)
       makes Anthropic's flat hypothesis (Anthropic, Definition 2.1) fail at every scale. Sources: run 98, SH-02, SH-03 and
       SH-10; run 99, Q3a. The mechanism is the selector inequality of Anthropic's Lemma E.7.
     - **The converse.** Assuming Anthropic's Theorem A.6 and Proposition C.3, a strict shortening exists iff flatness
       fails (run 98, SH-08).
     - **Contraction.** With Anthropic's Theorem D.2, a strict shortening implies the contracting hypothesis. The two
       dichotomies coincide iff the flat and contracting hypotheses exclude each other (run 98, SH-09; run 99, Q3c).
   - **A shared source.** OpenAI adapts a square scheme, with its two-layout
     crossing, from an earlier Anthropic paper (`Paper.tex` line 1099).
2. **GCT's target follows from either claim. GCT's method gains nothing.**
   - **The fleet's L-gct-011 (Mulmuley-Sohoni for every c) is implied.**
     - OpenAI's Corollary 1.2 states it for m ≤ N ≤ exp(c(log m)^{5/4}), with padding by a new or by an existing
       variable.
     - Anthropic's Theorem 1.4 gives it through division-free determinant circuits (its Remark N.6, the one numbered
       statement it did not formalize).
     - Both pass through the converse of L-gct-006, our survey row `PNP-SURVEY:converse-006`, which the fleet lacks as a
       node.
   - **Also implied:** L-gct-026 (the cubic target) for large m, and L-gct-028 for m ≥ m0.
   - **Moot as routes:** L-gct-086, 036/037, 025 and 103/104. They stay open as statements.
   - **No obstructions.** Neither claim gives an occurrence or a multiplicity obstruction. If they hold, our exclusions
     change meaning: the separation then holds in ranges where every low-height witness is impossible.
     - No occurrence obstruction exists for m ≥ (n+1)^25 (GCT_FLIP `thm:new-variable-no-occurrence`).
     - No multiplicity obstruction with ≤ 2c+1 rows exists at n ≥ m^c (GCT_KRON M-008, transferred to the fleet's padding
       by GCT_OBS S-004).
     - No four-row obstruction exists beyond n^2 = 2m^2 - m + 1 (CUE_GCT R-14).
   - **What the claims do imply** for GCT: separating equations exist. For every c and large m some highest-weight vector
     of I(Ω_{m^c+1}) is nonzero on the orbit of the padded permanent, since Z ⊄ Ω gives I(Ω) ⊄ I(Z). Whether a
     multiplicity obstruction q_λ > K_λ exists stays open.
3. **The named explicit spectral points cannot be flat.**
   - **The named explicit families over C:**
     - the flattening ranks;
     - the quantum functionals of Christandl-Vrana-Zuiddam, with their singleton and laminar extensions;
     - Strassen's support functionals, which coincide with the quantum functionals (Sakabe-Doğan-Walter,
       arXiv:2601.21553, Theorem I.1).
   - **What they give.** On wire tensors they give only clustered-star and tree pseudometrics. These lie at sup-norm
     distance exactly (√2 - 1)/2 from the Euclidean square (run 99, Q1d-1, Q1d-2, Q1d-6, Q2a-Q2c).
   - **Every tree pseudometric is a price, over every field** (run 98, PG-TREE-ALL).
   - The computation below covers the quantum functionals and the flattening ranks.
   - **On a product of wires** (a graph tensor, whose marginals are uniform), a quantum functional with weight vector θ
     on the parties gives F^θ = ∏_wires d^{θ_x + θ_y}. So its wire metric is the star metric δ(x,y) = θ_x + θ_y.
   - **A flattening rank across A gives the cut metric δ_A.**
   - **Neither realizes a Euclidean square up to scale** (sides 1, diagonals √2).
     - A star metric forces θ_1 = θ_3 and θ_2 = θ_4 with θ_1 + θ_2 = 1 from the sides, but θ_1 + θ_2 = √2 from the
       diagonals.
     - Cut metrics take only the values 0 and 1.
   - **On Mat_n(F_2) a star metric has bounded rank ratios.** E[δ(x,x+y)^2] over rank-n steps is at most twice its value
     over rank-1 steps, because 2E[θ^2] ≤ E[(θ_x+θ_z)^2] ≤ 4E[θ^2].
   - **So flatness needs a non-tree price.**
     - The Euclidean square is a price iff some non-tree pseudometric is a price (run 98, PG-FOUR-CONDITIONAL).
     - Assuming Anthropic's Theorem A.6 and Proposition C.3, no planar strict shortening exists iff the square is a price,
       iff every finite planar Euclidean configuration is a price (run 98, PG-CROSSPOLY-GATE at D = 2).
     - Such a price needs a spectral point outside the named families. This is consistent with Anthropic's remark that
       its points come from Zorn's lemma (`prop_gauge`).
   - **Matrix multiplication cannot contradict flatness.** ⟨n,n,n⟩ is a restriction of a star of rank n^ω, so a price
     must satisfy perimeter ≤ ω · min_h Σ_x |x h| on every triangle. In Euclidean space perimeter ≤ 2 min_h Σ|xh| by the
     triangle inequality, and ω ≥ 2, so that constraint never fails.
4. **The hinge is the real mathematics for us, and it pays in both directions.**
   - Prove the contracting hypothesis over some field, or construct a strict shortening, and the bounds jump. Anthropic's
     contracting case gives 2^Ω((log m)^2/log log m); OpenAI's Theorem 1.3 (stretch) turns a shortening into 2^{n^σ}.
   - Prove flatness, and one of the two cases of each proof becomes unnecessary. Both proofs could then be shortened to
     their direct halves.
   - The tools are ours:
     - moment polytopes and invariant theory of tensors (GCT_POS K-series, GPK18), which compute quantum functionals;
     - border apolarity, Koszul and substitution certificates (BR_PENCIL; BORDER_RANK thm:43/44/52), which bound
       asymptotic restrictions;
     - image substitution and norm certificates (GCT_GINEQ F-13, F-23);
     - the bridges of prompt 23 (ALPOGE_GCT B5: which analytic functionals can obstruct an orbit at all; B7: transfer of
       separations between characteristics).

   A Pro prompt for this is drafted: `vpvnp_integration/PROMPT.md`.
5. **What is formalized is less than what is claimed.**
   - **OpenAI's Lean challenge states only one thing:** `IsVP ≠ IsVNP` for exact circuits, on families in the variables
     `Fin n × Bool`. Outside it lie:
     - Theorem 1.1 (border circuits, quantitative);
     - Corollary 1.2 (permanent, Hamiltonian cycle, border dc, orbit closure);
     - Theorem 1.3.
   - **Anthropic's Lean covers Theorems 1.1, 1.4 and Corollary 1.2.** It does not cover Remark N.6, the determinantal
     complexity and orbit-closure consequence. I read `Statement.lean` in full; its definitions are the standard ones.
   - **So the GCT-facing statement of each claim is unformalized** in both releases. It is a short derivation:
     orbit-closure membership gives a border determinantal expression (the converse of L-gct-006); that gives an
     approximating circuit of size poly(N) from a division-free determinant circuit; and that contradicts the bound.
   - **I found no error in what I read** (section d).

## (a) What the claims change

The verdict for every node they touch is in the TSV; the headline rows follow. If either claim holds:

| node | exact statement (short) | verdict |
|---|---|---|
| L-gct-011 | ∀ c ≥ 1, large m: paddedPerm C m (m^c) ∉ orbitClosure(det_{m^c+1}) | implied (OpenAI Cor 1.2 directly; Anthropic through Thm 1.4 + Remark N.6) |
| L-gct-026 | ∃ c, m0: m^3 ≤ c n for every border expression of perm_m, m ≥ m0 | implied for large m |
| L-gct-028 | border dc(perm_m) ≥ m^2/2 + 1 for all m ≥ 3 | implied for m ≥ m0 only |
| L-gct-025, 036/037, 086, 103/104 | routes to lower bounds | made moot as routes; open as statements |
| L-gct-009/010/015/064/070/072/074 | checked bounds | unchanged; superseded asymptotically |
| L-gct-024/029/045 | smooth forms, power sums (VP polynomials) | unchanged |
| riffle rank, level-space small cases | | unchanged |
| WB-0002, GCT_FLIP main-collapse | GCT VI's RH, PH1, OH fail | unchanged; the flip's target is reached without the flip |
| GCT_FLIP no-occurrence; KRON M-008/O-018; OBS S-004; CUE R-14 (H14) | where obstructions cannot be | unchanged; they now say where the (claimed) separation has no low-height witness |
| KRON A-030/A-034/O-030; SEPARATIONS I/II; CUE R-12/R-13; OBS Q1a/Q1b | explicit obstructions, fixed sizes | unchanged |
| KRON M-007, CUE G-08, KRON F-009, OBS QC-014 | explicit determinantal containments | unchanged, consistent |
| ALPOGE_GCT B7.1-B7.3 (prompt 23) | transfer of separations between characteristics | applies: B7.1 carries OpenAI's characteristic-0 exclusion to all but finitely many p for each (m, N) |
| BR_PENCIL, BORDER_RANK, GINEQ, GCT_POS, GCT_NSRH, ALPOGE_GCT P-F, PLETH | | unchanged; several are tools for the hinge (finding 4) |

**No tension anywhere.** Nothing of ours contradicts either claim. Our barrier results (GINEQ F-01..F-12; ALPOGE_GCT B4,
B5; CUE_GCT P-09, P-10) concern norm, single-flattening and sampler methods. Both proofs use ranks across varying cuts and
diagonalization instead.

**Neither claim touches P vs NP.** The fleet's other programmes (meta, pcx, clb, lib, alg) are unchanged.

## (b) Where our material adds

- **The flat/contracting dichotomy.**
  - **Nothing we have decides it.** What we can say is finding 3.
    - The named explicit spectral points give only clustered-star and tree pseudometrics (run 99, Q2a-Q2c).
    - The star metrics have rank-ratio ≤ 2, which is the contracting side; the exact constant of Definition 2.1 is lost in
      the text extraction.
    - These metrics realize no Euclidean square.
    - Every tree pseudometric is a price (run 98, PG-TREE-ALL).
  - **How OpenAI's shortening and Anthropic's flatness meet.**
    - **At every scale.** A strict shortening makes the flat hypothesis fail at every scale, over every field (run 98,
      SH-02, SH-03 and SH-10; run 99, Q1a-1, Q1a-2 and Q3a). A terminal selector gives a homogeneous finite-cover
      inequality, which is the mechanism of Anthropic's Lemma E.7.
    - **The converse.** Assuming Anthropic's Theorem A.6 and Proposition C.3, it holds too: a strict shortening exists
      iff flatness fails (run 98, SH-08).
    - **Coincidence.** The two dichotomies coincide iff the flat and contracting hypotheses exclude each other (run 98,
      SH-09). That exclusion is the open part of the hinge.
  - **The two possible answers, in terms of what would have to be built:**
    - The flat case needs a non-tree price, equivalently a price on the Euclidean square (run 98, PG-FOUR-CONDITIONAL
      and PG-CROSSPOLY-GATE). That is a spectral point outside the named families, which give only trees (run 99,
      Q2a-Q2c). It is Strassen's open question on the asymptotic spectrum, here restricted to graph tensors.
    - Proving the contracting case needs an identity among wire networks, an asymptotic restriction. Its wire-length
      inequality has to fail for the Euclidean metric on some finite configuration.
  - **Why one configuration is enough.** By Anthropic's Theorem 2.2 (`thm_alt`), one Euclidean configuration that is not
    a price already gives contracting.
- **OpenAI's strict shortening.**
  - A single network cannot shorten C_{D,m}. Crofton's formula bounds the integral, over hyperplanes, of the rank across
    each hyperplane. Every hyperplane at distance t from the centre is crossed by the m·#{i: |v_i| > t} bits of the
    diameters, and integrating gives exactly the direct cost 2Dm.
  - A shortening must therefore be a sum of A networks whose cheap cuts differ from term to term. This is the
    "varying cuts" phenomenon both papers name.
  - The rank lower bound does not survive sums. log rank(ΣT_a) ≤ log A + max_a width_H(T_a), and the maximising term
    changes with the hyperplane H.
  - So whether a shortening exists is genuinely open, and it is an asymptotic-restriction question about graph tensors
    with hubs. Our border-rank tools (apolarity, Koszul flattenings, substitution, P-01's torus degeneration) give lower
    bounds for exactly such restrictions. The constructions in BORDER_RANK (18-, 19- and 20-term degenerations) are the
    upper-bound side.
- **The exponents 1/3 and 5/4.** Anthropic's m^{c(log m)^{1/3}} = 2^{c(log m)^{4/3}} beats OpenAI's exp(c(log m)^{5/4}). Both
  are set by the direct case.
  - **I re-derived OpenAI's 5/4** from `Paper.tex` lines 231-276:
    - the gain is m·u·√(γd) with u = b/√d, against the bridge h;
    - selection costs 2Dd = O(d^2) and must stay below a constant times m = c log n, so d ≍ √(log n);
    - then h ≥ m√(γd)/2 ≍ (log n)^{5/4}.
  - **Anthropic gains** by using the complete network, where every balanced set is crossed by ≥ 2n^2/9 wires, with a
    sharper count of the bits that name a balanced set (`lem_few`, `prop_cube`: "the balanced sets cost about n^{3/2}
    bits"). I could not re-derive its arithmetic from the glyph-damaged text.
  - **The exponent is limited** by naming the balanced cut against the saving per cut. A decomposition lemma with
    polynomially many cut types would improve it. That is open in both papers.
- **Checks of key lemmas against our results.**
  - The decomposition over balanced cuts is the classical one (Hyafil; Valiant-Skyum-Berkowitz-Rackoff; Raz), as both
    say.
  - The passage from orbit closures to circuits uses the converse of L-gct-006, which our survey (a8d75352, Claude Opus
    5.5 at effort high) proved on paper on 23 Nov.
  - Reducing constants modulo a prime (Anthropic: "survives reduction to a finite field [Eis95, Thm 4.19]"; OpenAI:
    "outside a fixed finite set of primes") is the mechanism of our ALPOGE_GCT B7.1-B7.2. Our B7.3 (bad-prime
    noncontainment need not lift) warns only against the reverse transfer, which neither paper uses.
- **Relation to our moment polytopes and invariant theory.**
  - Spectral points are Strassen's monotone multiplicative functionals in Anthropic's variant. On graph tensors the
    explicit ones are the moment-polytope entropies (quantum functionals). Our GCT_POS K-series (polystable tensors,
    SL_n^3-invariants, grading stabilizers) and GPK18 (vertex denominators of Kronecker polytopes) compute exactly these
    polytopes for 3-tensors.
  - Anthropic's prices are CAT(0) metrics (Bruhat-Tits inequality, `thm_cn`). The moment-map side of GIT also has a
    natural nonpositively curved geometry: the symmetric space GL/U, where Kempf-Ness functions are convex.
  - Relating Anthropic's prices to geodesics in GL/U is a concrete route to new spectral points, and so to the flat
    case. It is route R2 of the prompt.

## (c) The two proofs compared

| step | Anthropic | OpenAI |
|---|---|---|
| hinge | flat versus contracting prices on Mat_n(F_2) (Def 2.1); one holds (Thm 2.2, via Bruhat-Tits CN, CAT(0), flat rectangles) | strict shortening exists or not (Def 2.1); a tautological split |
| permanent enters | clause sums by substitution (`lem_fkl_perm`, `cor_clauses`), via Valiant | f_n's projections (Valiant completeness) |
| circuit enters | `lem_balanced` (flat); `lem_lowdeg` low-degree evaluation by parse trees (contracting) | balanced-product decomposition (direct); parse map Y(X) with universal weights (stretch) |
| direct case | complete network P_{n,b}; Euclidean hubs from a spectral point; 2^Ω((log m)^{4/3}) | expander partition function; hubs moved by b/√d; exp(Ω((log n)^{5/4})) |
| saving case | Poincaré inequality on unitriangular groups → rerouting laws (Strassen duality) → trees → cutting; accelerators; P = 1 + P | ribbon switching hosts, iterated wire saving, the square scheme of an earlier Anthropic paper, Cartier operators, boundary evaluation; 2^{n^σ} |
| border | circuits over k((ε)); identities survive reduction mod p | closure; eigenvector law with matrices W_μ; Cartier extraction |
| Lean | 324 files; Theorems 1.1, 1.4 and Corollary 1.2 checked; Remark N.6 not | only IsVP ≠ IsVNP for exact classes |

**Shared sources.**

- OpenAI cites an earlier Anthropic paper for its square scheme.
- Both cite:
  - the OpenAI cubic border-dc manuscript (Anthropic [OAI26]; OpenAI CubOAI);
  - Sheshadri's extensions ([She26b], [She26]; Sheshadri287, SheshadriBorder2026);
  - Kumar-Volk ([KV26]; KumarVolk2026);
  - BIP19, LST and Forbes, VSBR, Raz13 and GKSS17/FSV18.
- The fleet's chain L-gct-023-027 was taken from that same OpenAI cubic manuscript.
- OpenAI's bibliography (`build/references.tex`, 80 items, fetched 24 Nov) settles the rest:
  - CubOAI is "A cubic lower bound for border determinantal complexity of the permanent", OpenAI Math Release preprint, 24
    September 2026.
  - KumarVolk2026 is arXiv:2609.34462 (a quadratic dc bound). Sheshadri287 is ECCC TR26-287. SheshadriBorder2026 is
    arXiv:2606.13628.
  - It cites nothing on Strassen's asymptotic spectrum: no Strassen 1988, no Christandl-Vrana-Zuiddam, no
    Wigderson-Zuiddam. Nor does it cite Anthropic's [Raz26] or [Cur26].
  - **So OpenAI's direct case argues with Euclidean geometry alone, without spectral points.** Spectral points are
    Anthropic's ingredient only.

**What one has and the other lacks.**

- Anthropic has a theorem that one of its two cases holds (`thm_alt`). OpenAI's dichotomy needs none.
- OpenAI's saving case gives an exponential-type bound (2^{n^σ}). Anthropic's contracting case gives only
  2^Ω((log m)^2/log log m).
- Anthropic formalizes far more.
- OpenAI adds a low-degree application: clique polynomials with polylogarithmic clique size have border complexity
  exp(Ω((log N)^{5/4})).

## (d) Errors and unstated points

No mathematical error found in what I read. Five points to record, all checkable from the quoted passages:

1. **OpenAI's formal statement is far weaker than its paper.** `Challenge_VPVNP.lean` proves only "(IsVP : Family F (fun n
   => Fin n × Bool) → Prop) ≠ IsVNP". The abstract's "The lower bound holds for border circuits and is superpolynomial, of
   the form exp(Ω((log n)^{5/4}))" is not formalized, nor is Corollary 1.2's orbit-closure clause.
2. **Anthropic's orbit-closure consequence is stated but not proved in Lean.** The paper says so: "this consequence is
   the one numbered statement of this paper that is not formalized in Lean".
3. **OpenAI's corollary proof is a sketch at the GCT step.** It reads: "use that the orbit consists of determinants of
   linear matrices and that padding by a power of a new variable can be undone by specialization. Even padding by an
   existing variable works: split into components by degree in that variable, discard too-low degrees and undo the
   shift".
   - I checked the step for both padding conventions of our joint space: the fleet's x00, which is independent, and
     GCT_KRON's internal X11. It goes through: extracting X11-homogeneous components is linear interpolation, at
     polynomial cost.
   - The one input not spelled out is that a border determinantal expression yields an approximating circuit of
     polynomial size. That needs a division-free determinant circuit; they cite Mahajan-Vinay, which is correct.
4. **The constants are ineffective.** Anthropic: "the constants, among them m0, depend on the integer n, for which the
   proof gives no value". OpenAI's σ depends on the unknown shortening data. Neither gives a bound at any explicit m,
   so the fixed-size questions (our (8,9), (17,23)) are untouched.
5. **The flat hypothesis quantifies over all finite Euclidean configurations; nothing in the papers exhibits one.**
   Section 2.2 obtains it only from the failure of contraction, through compactness and the flat-rectangle property of
   CAT(0) spaces. I could not check that compactness step from pages 1-12. A reader should check `thm_alt` in
   Appendix B-C together with its Lean statement (Table 3 of the paper lists the counterparts).

## (e) The form

**Both.**

- **The joint lemma space is updated now:** 8 external rows and 17 edges, with the verdicts in the TSV. The public
  mirror's roadmap should add one line per claim and mark L-gct-011, 026 and 028 as "implied if either claim holds;
  unchecked by humans". That is the main session's call.
- **A Pro prompt** on the shared hinge is warranted. A resolution changes the strength of VNP lower bounds by an
  exponential order, and it is mathematics our runs are equipped for.
  - The draft is `<local>/pequalnp_work\fleet_map\vpvnp_integration\PROMPT.md`. It passes
    `push_rule_pro_prompts.py --lint-math` and `paper_completeness_lint.py`.
  - Attachments: OpenAI's `Paper.tex` (LaTeX); Anthropic's `paper.pdf` (only PDF exists); `Statement.lean`; our
    GCT_GINEQ.tex, BORDER_RANK `border_rank.tex`, BR_PENCIL sections, GCT_POS K-branch TeX and the ALPOGE_GCT B-section.

## Paths

- `<local>/pequalnp_work\fleet_map\VPVNP_INTEGRATION_20261124.md` (this file)
- `<local>/pequalnp_work\fleet_map\VPVNP_NODE_VERDICTS_20261124.tsv` (33 rows; generator
  `vpvnp_integration\gen_verdicts.py`)
- `<local>/pequalnp_work\fleet_map\JOINT_GCT_LEMMA_SPACE.tsv` (now 1,571 rows: 226 swarm, 1,337 ours, 8
  external; 138 edges); backups `JOINT_GCT_LEMMA_SPACE_before_vpvnp_20261124.tsv` / `.md`; builder
  `joint_tools\ext_claims.py`
- `<local>/pequalnp_work\fleet_map\vpvnp_integration\PROMPT.md`

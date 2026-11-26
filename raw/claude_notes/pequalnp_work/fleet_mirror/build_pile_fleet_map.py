"""Build FLEET_MAP.md and FLEET_MAP.tsv for the intake pile of 24-25 Nov 2026: the curated links between pile items and
pequalnp.com fleet lemmas (below), with each fleet lemma's exact formal statement and live status taken from our mirror
(RESULTS.json), open nodes first. The judgments are in LINKS; the statements and statuses are never typed by hand.
usage: python -I -B build_pile_fleet_map.py
Written 24-25 Nov 2026 by Claude Opus 5.5 at effort max (session 672ae3a0) for the main session's intake pile."""
import csv, json, pathlib, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path("<local>/Documents/reports_20261124/INTAKE_PILE_20261124")
data = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))
F = {r["id"]: r for r in data["lemmas"]}
UP = (HERE.parent / "fleet_lean" / "UPSTREAM_COMMIT.txt").read_text().strip()[:7]

# (cluster, run, item ids, fleet ids, relation, mechanism, check status of our side)
LINKS = [
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 thm:onesided (both runs)", ["L-meta-647"], "settles (paper)",
     "647's AND condition is syntactic X-degree <= 1, so every monomial has at most one X-variable; one-input and "
     "constant gates removed without growth; size >= |E| + vc - 1 (remark (a)-(c) in X-meta-005)",
     "first run read step by step by a2fedc2a (Claude Fable 5.2 at effort max); our own 23 Nov proof (two derivations "
     "and a targeted step check, Claude Opus 5.5 at effort max); public: pequalnp-mirror X-meta-005, commit d1464a4"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 prop:readone (first run) = thm:main read-1 case (second run)",
     ["L-meta-2239"], "settles (paper)",
     "lower bound: the fleet's checked L-meta-2237 (or our prop:readone) on the incidence graph, which has no 4-cycle "
     "(two points share one line), |E| = N(q+1), and every vertex cover >= N (each point lies on q+1 lines, so every "
     "vertex has degree q+1); upper bound: the star circuit of the N points (L-meta-154), read-1, size N(q+2) - 1",
     "prop:readone read step by step by a2fedc2a (Claude Fable 5.2 at effort max); the degree count and the read-1 "
     "check of the star circuit by Claude Opus 5.5 at effort max (this map)"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 prop:readone / thm:main read-1 case", ["L-meta-2237"],
     "same statement (fleet checked first)",
     "read-1 AND/OR circuits for the edge function of a 4-cycle-free graph need |E| + tau - 1 gates; the fleet's Lean "
     "proof was merged 24 Nov 18:29 UTC; paper 4 should cite it", "as above"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 thm:twomissing, thm:threemissing (second run, cp08 19:40 / cp10)",
     ["L-meta-612", "L-meta-608"], "sharpens (paper)",
     "by thm:main (Mon(f_G) = min over Sup(G) of the arithmetic complexity), a circuit with fewer than |E| + vc - 1 "
     "gates lifts to a P in Sup(G); thm:threemissing forces at least four edges with no quadratic witness in P",
     "proved by the second run with a same-model audit; not checked by another model"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 thm:onesided applied to both sides", ["L-meta-612", "L-meta-608"],
     "sharpens (paper)", "a bipartite counterexample must have a monomial with two distinct X-variables and one with "
     "two distinct Y-variables", "as for 647"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 thm:threemissing", ["L-meta-2585", "L-meta-2635"],
     "consistent, neither settled", "2585 (any circuit for 4-cycle-free incidence can be made read-1 without growth) "
     "with the checked 2237 would give 612 for incidence graphs; threemissing says a circuit beating the count is far "
     "from read-1 (>= 4 edges without a quadratic witness)", "second run only"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 Lemma 4.1 (OR-only Boolean sums)", ["L-meta-529"],
     "strengthens a checked node", "sum (|S_i| - 1) OR gates even with AND gates and constants; 529 counts all gates",
     "first run, read by a2fedc2a; also step 4 of X-meta-005"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 Thm 1.2 / thm:main", ["L-meta-606", "L-meta-608", "L-meta-612"],
     "reformulates", "Mon(f_G) = min over Sup(G) of Arith(P): the three node questions become arithmetic questions; "
     "support criterion credited to Jukna", "first run, read by a2fedc2a"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 Prop 6.1 (flat count)", ["L-meta-613"],
     "same statement, attribution", "the literature source is the proof of Amano-Maruoka's Theorem 5",
     "first run, read by a2fedc2a"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 Petersen example", ["L-meta-584"], "explains a checked node",
     "four edges are covered only by monomials with a square; #OR >= |E| - 1 fails there while the total does not",
     "recomputed by a2fedc2a"),
    ("AG_POLISH", "SPLIT_ZERO_AFTER_FGJM", "paper 4 sections 9-10", ["L-meta-608", "L-meta-612", "L-meta-650",
     "L-meta-655", "L-meta-582"], "pruning for searches", "a minimum counterexample has no terminal product, no common "
     "mask and no private mask; with H_X 4-cycle-free every output monomial has at most three marked variables",
     "first run, statement level in the intake"),
    ("AG_POLISH", "POLISH_ALGEBRAIC_GEOMETRY", "Paper 2 G1 (AG-05 bridge)", ["L-pcx-071"], "parallel (constructed)",
     "integral transvections act on quadratic refinements of the Weil pairing with two orbits (Arf 0, 1) and no fixed "
     "point for rank >= 4: route M, node M3 (Arf maps on theta characteristics)", "run; intake map, not graded"),
    ("AG_POLISH", "POLISH_ALGEBRAIC_GEOMETRY", "P90a, Theorem 2/3 (AG-06)", ["L-gct-025"], "parallel (constructed)",
     "marks where characteristic-2 vanishing fails: reduction mod 2 and specialization of smoothness",
     "P90a v2 posted (hexagon:2611.00936); map not graded"),
    ("AG_POLISH", "POLISH_TOPOLOGY_PERIODS", "S20 note Lemma 6 (indicator power step), map M1", ["L-clb-033",
     "L-clb-002", "L-clb-009", "L-clb-010"], "parallel (constructed), input",
     "raising to Q^m is the amplifier x -> x^(p^k) (0/1 mod p to 0/1 mod p^(k+1), degree p^k, prime-power moduli); "
     "Beigel-Tarui have degree 2k - 1; completion: replace by the Toda polynomial and keep the degree budget",
     "S20 posted (hexagon:2611.00937); map not graded"),
    ("AG_POLISH", "NEG_NIGHT / COUNTING_VARIETIES", "NN-C005, C023, C024; CV-THM-MAIN; CV-SP-*", [], "no node",
     "the fleet's graph has no counting-class node (#P, ParityP, Mod_pP: 0 hits); #SAT mod p as a Frobenius scalar of "
     "a smooth Calabi-Yau hypersurface would be a new node", "CV-THM-MAIN core lemmas checked by the pile's intake"),
    ("AG_POLISH", "NEG_NIGHT", "NN-G032..G037 (GCT VIII E_3 lifts)", ["L-gct-011"], "no direct node; nearest",
     "GCT VIII positivity is not in the graph", "checked by a8d75352"),
    ("ALPOGE", "CX_GRH / BEYOND_DIRICHLET / ALP_MACHINE", "CX-N01..N04, N13, N15; BD-R22..R24", [], "no node",
     "the fleet's graph has no GRH-, ERH- or L-function-conditional node (0 hits) and no primality, factoring or "
     "Nullstellensatz/AM node: Miller-Bach primality, r-th nonresidues and primitive roots from A (Alpoge's theorem) "
     "are knowledge the fleet does not have", "CX-N13 checked by af2a18f6 and again"),
    ("ALPOGE", "ALP_MACHINE", "AM-S4 (cp55 intake)", ["L-gct-011"], "parallel", "barrier-type statement toward the "
     "separation target", "intake map"),
    ("GCT", "CUE_GCT", "R-14 (H14)", ["L-gct-011"], "parallel (see MAP_COMPLEXITY)",
     "four-row multiplicity obstructions for padded permanent against determinant when c_m + 3 > 2n^2 + 2",
     "proved; intake TPC"),
    ("GCT", "GCT_KRON", "A-030 (H13), F-025, M-008, O-018, M-013, F-021", ["L-gct-011"],
     "parallel (see MAP_COMPLEXITY)", "an occurrence obstruction per_n against det_n without padding (A-030); row "
     "conditions for multiplicity obstructions in the BIP range", "A-030 proved, intake TPC+COMP"),
    ("GCT", "GCT_OBS", "QC-014, QC-019 (+S-025), S-004", ["L-gct-011"], "parallel (see MAP_COMPLEXITY)",
     "no <= 4-row multiplicity obstruction for padded per_4 against det_n, n >= 7; independent padding row cap",
     "intake TPC(+COMP)"),
    ("GCT", "CUE_GCT", "ctx-G13", ["L-gct-010", "L-gct-028", "L-gct-070", "L-gct-074", "L-gct-056"],
     "correction to the run's text", "the run calls border dc(perm_m) >= m^2/2 the established bound; the fleet has "
     "Lean-checked (2m^2 - 10m + 11)/3 (070) and 'exceeds R m^2 for every R' (074, 056)", "intake"),
    ("GCT", "CUE_GCT", "P-02", ["L-gct-129", "L-gct-103", "L-gct-104"], "parallel, undecided",
     "whether character-point hitting sets give DIV-type bounds", "primer level"),
    ("GCT", "GCT_GINEQ / BR_PENCIL", "F-13 (border substitution); P-01", ["L-gct-139"],
     "specialization claimed (see MAP_COMPLEXITY)", "F-13's proof works verbatim for exact decompositions with any "
     "atoms; after the atom translation PNP-MBR:A2 it gives riffle rank of [a=b][c=d] >= 2n - 1; P-01 needs the "
     "torus degeneration to transfer to border riffle rank (PNP-MBR:A4)", "F-13 intake TPC+COMP; translation unchecked"),
    ("GCT", "BR_PENCIL / GCT_GINEQ / GCT_OBS", "R-05, R-08, R-10 (H03); F-23; BR-006", [], "no node",
     "the fleet's GCT has no border-rank node ('border' there is border determinantal complexity)", "H03 posted"),
    ("GCT", "GCT_POS / GCT_NSRH", "K-023 (H02b), F34", ["L-gct-011"], "no direct node; nearest",
     "numerical PH3 (GCT VI Hyp. 3.3.4) fails for Kronecker coefficients; GCT VI Hyp. 1.6.4(2) false: the GCT VI "
     "hypotheses are not in the graph", "K-023 checked by the main session and intake"),
    ("GCT", "CUE_GCT", "I-18, P-11", [], "no node", "the fleet's hitting-set nodes concern MCSP, not identity testing",
     "intake TPC"),
    ("HODGE", "HODGE_FINISH", "Q11", ["L-pcx-092"], "parallel", "minimum rank 24 of the induced pairing on Lambda^2 V "
     "for invariant alternating four-forms on F2^4, against 2 dim U <= dim V + rank", "run; statement level"),
    ("ZETA_GRH", "GRH_ALGORITHMS / GRH_ALGORITHMS_FINISH", "P144, P145, P126 (hexagon:2611.00987)",
     ["L-meta-606", "L-meta-608", "L-meta-612", "L-meta-649", "L-meta-650", "L-meta-660", "L-meta-661", "L-meta-766",
      "L-meta-885", "L-meta-2239"], "input (ANT-07)", "succinct descriptions of the plane families over every prime "
     "power q need a presentation of F_{p^r} in time poly(r log p): Lenstra's construction problem, solved here "
     "unconditionally for small cyclotomic cofactor and under A at fixed valuation", "paper posted; targeted checks"),
    ("ZETA_GRH", "GRH_ALGORITHMS_FINISH", "ANT-07 (characteristic 2)", ["L-meta-664", "L-meta-683"], "input",
     "characteristic-2 quadratics", "intake map"),
    ("ZETA_GRH", "ZETA_HEAT", "prop:fd-certificate-size", ["L-gct-128", "L-gct-138"], "uses",
     "the run's certificate-size bound uses the Descartes bounds; both are classical and await Lean on the fleet",
     "intake map"),
    ("AG_POLISH", "NIGHT_GROTHENDIECK_QUESTIONS (via its intakes)", "cp04 Part A; cp13 Part A",
     ["L-gct-126", "L-gct-154", "L-gct-149"], "uses / nearest", "the ring identities of the algebraic route and the "
     "Kronecker exponent; L-gct-126 already has a merged proof in the fleet's repository (commit 7dc6cc2, PR #2, "
     "23 Nov: ring) while its record still says conjecture", "intake map"),
]
NO_NODE = {
    "DERIVATEURS": "no fleet node: localizers, derivators, reversible closures and free monoids have no node in a graph "
                   "about circuits, proof systems and algebraic complexity",
    "LONGUE_MARCHE_A": "no fleet node: Grothendieck-Teichmüller, loop equations, Fermat towers and sections",
    "LONGUE_MARCHE_B": "no fleet node: anabelian sections, Torelli chains, profinite completions",
    "SWEEP3_A": "no fleet node: local cohomology, Chow groups, Picard categories, CM comparisons",
    "SWEEP3_B": "no fleet node: Ab^2 autoduality, monodromy mod 2, orthosets, Fuglede-Kadison determinants",
    "HODGE": "apart from Q11, no fleet node: Weil classes, CM fourfolds and sixfolds",
}
ORDER = {"conjecture": 0, "in_work": 1, "blocked": 2, "checked": 3, "refuted": 4, "retired": 5, "dead": 6}


def st(i):
    r = F.get(i)
    return (r.get("status") if r else "not in the mirror"), r


# ---------------- TSV ----------------
with open(OUT / "FLEET_MAP.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["cluster", "run", "items", "fleet_id", "fleet_status", "fleet_attempts", "relation", "mechanism",
                "our_check_status", "fleet_title", "fleet_formal_statement"])
    for cl, run, items, ids, rel, mech, chk in LINKS:
        for i in ids or [""]:
            s, r = st(i) if i else ("", None)
            w.writerow([cl, run, items, i, s, (r or {}).get("attempt_count", ""), rel, mech, chk,
                        (r or {}).get("title", ""), " ".join(((r or {}).get("formal_statement") or "").split())])

# ---------------- MD ----------------
named = sorted({i for L in LINKS for i in L[3]}, key=lambda i: (ORDER.get(st(i)[0], 9), i))
opened = [i for i in named if st(i)[0] in ("conjecture", "in_work", "blocked")]
md = ["# The intake pile against the pequalnp.com fleet's graph", "",
      "From session 672ae3a0 (Claude Opus 5.5 at effort max), 24-25 Nov 2026, for the main session's intake pile and "
      "the conference that reads it.",
      "",
      "**Data.**",
      f"- Our mirror of data.pequalnp.com: {len(data['lemmas'])} lemmas, refreshed hourly.",
      f"- The fleet's Lean tree at upstream commit {UP}.",
      "- Statuses and statements below are generated from that mirror, not typed.",
      "- Any lemma can be looked up with `python -I -B <local>/pequalnp_work/fleet_mirror/fleet_lookup.py "
      "--id <id>`.",
      "",
      "**Method.**",
      "1. Every fleet id named in the pile and in the main session's intakes (`fleet_mirror/INTAKE_FLEET_MAPS.md`).",
      "2. Term-weighted matching of all 530 items against all lemmas, read pair by pair "
      "(`fleet_mirror/PILE_CANDIDATES.tsv`). It found no further link: shared words, different mathematics.",
      "3. Targeted searches of the fleet by topic:",
      "   - L-functions, GRH and ERH;",
      "   - finite-field construction;",
      "   - primality and factoring;",
      "   - counting classes;",
      "   - the Nullstellensatz and AM;",
      "   - identity testing;",
      "   - multiplicities;",
      "   - border rank;",
      "   - read-1 circuits;",
      "   - alternating forms;",
      "   - Beigel-Tarui.",
      "",
      "**The GCT overlap.** It is mapped in a4348514's MAP_COMPLEXITY.md. The gct rows here give the fleet's exact "
      "statements and statuses, to be read side by side, not a second mechanism.",
      "",
      "## 1. What the fleet's graph does not contain",
      "",
      "No lemma on any of these (0 hits each):",
      "- L-functions, GRH, ERH or zero-free regions;",
      "- finite-field construction;",
      "- primality or factoring;",
      "- counting classes (#P, ParityP, Mod_pP);",
      "- the Nullstellensatz or AM;",
      "- polynomial identity testing (its 'hitting set' nodes are about MCSP);",
      "- Kronecker or plethysm multiplicities, or the GCT VI positivity hypotheses;",
      "- border rank (its 'border' is border determinantal complexity).",
      "",
      "So most of the pile has no fleet node. The following are knowledge the fleet does not have:",
      "- Alpöge's theorem and its algorithmic consequences (CX_GRH);",
      "- #SAT mod p as a Frobenius scalar (COUNTING_VARIETIES, NEG_NIGHT);",
      "- the GCT VI refutations (GCT_POS, GCT_NSRH);",
      "- the border-rank bounds (BR_PENCIL, GCT_GINEQ, GCT_OBS).",
      "",
      "The links concentrate on four areas:",
      "- edge-function circuits (paper 4 of SPLIT_ZERO_AFTER_FGJM);",
      "- GCT (border determinantal complexity, level spaces, riffle rank, the DIV hypotheses);",
      "- three proof-complexity and ACC0 nodes;",
      "- the projective-plane families.",
      "",
      "## 2. Open fleet nodes that our checked results settle (on paper)",
      "",
      "**L-meta-647** (conjecture since 23 Nov 13:21 UTC, 0 attempts).",
      "- Settled by paper 4's one-sided theorem, both runs. The first run was read step by step by a2fedc2a "
      "(Claude Fable 5.2 at effort max).",
      "- Also settled by our own proof of 23 Nov.",
      "- Remark (a)-(c) in the public entry X-meta-005 (pequalnp-mirror commit d1464a4) checks that the posted Lean "
      "statement falls under both.",
      "",
      "**L-meta-2239** (conjecture since 24 Nov 07:46 UTC, 0 attempts). Planes of order q, read-1 circuits: exactly "
      "N(q + 2) - 1.",
      "- *Lower bound.* The fleet's own L-meta-2237 (checked 24 Nov 18:29 UTC: read-1 circuits on a 4-cycle-free graph "
      "need |E| + tau - 1 gates) applied to the incidence graph, with three facts:",
      "  - it has no 4-cycle, since two points share one line;",
      "  - it has |E| = N(q + 1);",
      "  - every vertex cover has at least N vertices. Each point lies on q + 1 lines, because the other q^2 + q points "
      "fall q to a line through it, so every vertex has degree q + 1.",
      "- *Upper bound.* The star circuit on the N points (L-meta-154): for each point, an AND of it with the OR of its "
      "q + 1 lines, then an OR of the N terms. It is read-1, and N(q + 1) + N - 1 = N(q + 2) - 1.",
      "- *Independently,* paper 4's read-one proposition (first run; thm:main in the second) proves the lower bound for "
      "every 4-cycle-free graph.",
      "- *Checks.* The proposition was read step by step by a2fedc2a (Claude Fable 5.2 at effort max). The degree count "
      "and the read-1 check of the star circuit are mine.",
      "- Public entry: X-meta-006, pequalnp-mirror commit f8123ad.",
      "",
      "**L-meta-2237** (checked) states the same thing as paper 4's read-1 case. The fleet merged its Lean proof first; "
      "paper 4 should cite it.",
      "",
      "**Sharpened, not settled: L-meta-612 and L-meta-608.**",
      "- Paper 4's second run (thm:main, thm:twomissing, thm:threemissing; checked by the run only) shows that a circuit "
      "beating |E| + vc - 1 lifts to a polynomial in Sup(G) with at least four edges lacking a quadratic witness.",
      "- The one-sided theorem, applied to both sides, adds that a bipartite counterexample must have a monomial with "
      "two distinct variables of each side.",
      "- L-meta-2585 and its negation L-meta-2635 are both open. If 2585 held, then with 2237 it would give 612 for "
      "incidence graphs.",
      "",
      "**Elementary nodes, not ours to settle.** The TRACTABLE nodes our runs use are classical or elementary and need "
      "only Lean: L-gct-126, 128, 129, 138, 149, 154; L-pcx-091, 092.",
      "- L-gct-126 already has a merged proof in the fleet's repository (commit 7dc6cc2, PR #2, 23 Nov, `ring`), but "
      "its record still says conjecture.",
      "",
      "**L-gct-139** (riffle rank >= 2n - 1). GCT_GINEQ F-13 is claimed to specialize to it after the atom translation "
      "PNP-MBR:A2. The translation is unchecked here and belongs to MAP_COMPLEXITY.",
      "",
      "## 3. Per cluster",
      ""]
for cl in ["AG_POLISH", "ALPOGE", "DERIVATEURS", "GCT", "HODGE", "LONGUE_MARCHE_A", "LONGUE_MARCHE_B", "SWEEP3_A",
           "SWEEP3_B", "ZETA_GRH"]:
    md += [f"### {cl}", ""]
    rows = [L for L in LINKS if L[0] == cl]
    for _, run, items, ids, rel, mech, chk in rows:
        idl = ", ".join(f"{i} ({st(i)[0]})" for i in ids) if ids else "no fleet node"
        md.append(f"- **{run}, {items}** -> {idl}. *{rel}.* {mech}. Our side: {chk}.")
    if cl in NO_NODE:
        md.append(f"- Everything else: {NO_NODE[cl]}.")
    md.append("")
md += ["## 4. Exact statements and live statuses of every fleet node named above", "",
       f"Open nodes first ({len(opened)} open of {len(named)}).", ""]
for i in named:
    s, r = st(i)
    if not r:
        md += [f"**{i}**: not in the mirror.", ""]
        continue
    md += [f"**{i}** ({s} since {r.get('status_at')}; attempts {r.get('attempt_count')}; seat {r.get('seat')}; "
           f"used by {len(r.get('used_by') or [])}): {r.get('title')}", "",
           "```", " ".join((r.get("formal_statement") or "").split()), "```", ""]
(OUT / "FLEET_MAP.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
print("links", len(LINKS), "| fleet ids", len(named), "| open", len(opened), "| written FLEET_MAP.md/.tsv in", OUT)

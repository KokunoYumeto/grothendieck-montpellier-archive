"""Write SETTLED_BACKGROUND/cote_94.tsv: what the OBJ_H035 run and its verdict settled on cote 94, for the range prompts.

The main session, 19 Nov 2026 ~13:5x UTC (after sweep 3.5, SUMMARY.md item 1): the range pilot 033_WT_94_002-013_B
carries the state before the verdict; it gets the verdict's settled statements as background, stated with their checks,
so that the range run builds on them and does not redo them. The checks are copied from the verdict's own check events
(PILOT_VERDICT_OBJ_H035_20261119_CHECK_EVENTS.tsv); the statements are written here from the verdict (sections 2, 3,
7.3) and the run's STATEMENTS.tsv (returns/OBJ_H035_checkpoint_04_20261119T0554Z_unzipped/OBJ_H035/).

usage: python -I -B make_cote_94_20261119.py
Claude Opus 5.5 at effort max (agent a11a6de3), 19 Nov 2026.
"""
import csv
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
WT = HERE.parent
CE = WT / "PILOT_VERDICT_OBJ_H035_20261119_CHECK_EVENTS.tsv"
RUN = WT / "returns/OBJ_H035_checkpoint_04_20261119T0554Z_unzipped/OBJ_H035/STATEMENTS.tsv"
COLS = ["id", "kind", "cote", "scan_first", "scan_last", "locator", "status", "settled", "run_status", "checks", "source"]
RUN_WHO = "GPT-6 Astra (ChatGPT Pro mode), run OBJ_H035 (sent 19 Nov 2026 02:54 UTC), its checkpoint 04"
SRC = ("working_through_20261118/PILOT_VERDICT_OBJ_H035_20261119.md (sections 2, 3, 7.3) and its CHECK_EVENTS.tsv; "
       "the run's STATEMENTS.tsv")

# the statements: id -> (scans, locator, status, what is settled)
STATEMENTS = {
    "H035.5": ((4, 5), "94/004.14-005.12, Proposition 3", "True as written",
               "His Proposition 3 holds as he wrote it. The ink has \"non nul\" before B at 94/004 l.19 (written small "
               "under \"lim\" on the line above, with a curved leader down to B in \"Pour tout quotient B de A\"); our "
               "transcription has it (cote_94.tex l.79, `\\inserted{non nul}`); witness H omits it. He also writes "
               "\"A ≠ 0\" at the head of the proof on scan 5. With A noetherian: F is finitely representable if and only "
               "if it is left exact, commutes with filtered colimits, satisfies the principal-completion comparison "
               "(H035.4) for every f in A, and for every nonzero quotient B of A there is a non-nilpotent f in B such "
               "that F on B_f-modules is representable. Proof: the run's proof of this statement (it called it its "
               "corrected statement; it is his)."),
    "H035.8": ((6, 7), "94/006.22-007.27, Lemme 5 (v)", "Slip",
               "The condition needs f ≠ 0 (an omitted convention; the crop shows \"il existe f dans A/p\" with no "
               "nonzero condition): for every prime p there is a nonzero f in A/p such that F on (A/p)_f-modules is "
               "representable. With it the statement holds (the run's proof)."),
    "H035.10": ((8, 8), "94/008.8-26, Remarque 5 bis (the converse)", "False",
               "The converse fails: A = Z, L = Σ_p (1/p)Z ⊂ Q, F = L ⊗ −. L is torsion-free, hence flat; L_(p) ≅ Z_(p); "
               "dim L/pL = 1 = dim L⊗Q; no L[1/n] is finitely generated. The repair holds: if F(B) is finite (de type "
               "fini), the converse follows (on the constant-rank open, μ(Q_p) = the generic rank makes Q_p free, and "
               "F ≅ F(B) ⊗ −). He uses \"F(N) est de type fini\" (scan 8), which his hypotheses do not give; he supplies "
               "it later as Théorème 12 (iv). The forward implication stands."),
    "H035.14": ((10, 10), "94/010.5-11, the Hom complex", "Slip",
                "He writes ⊗P twice where ⊗Q is meant (ink, 94/010 l.9): for a finite presentation L_1 → L_0 → P → 0 "
                "with L_i finite free, Hom(P,Q) = H⁰[L_0^∨ ⊗ Q → L_1^∨ ⊗ Q]. The written formula fails already for "
                "P = k, Q = k² over a field."),
    "H035.15": ((10, 10), "94/010.12-18, the Z¹ criterion", "False",
                "The conditions Tor_1(M, H¹(K)) = Tor_1(M, Z¹(K)) = 0 (ink: Z¹, 94/010 l.15) do not make "
                "H⁰(K) ⊗ M → H⁰(K ⊗ M) an isomorphism: A = k[x,y]/(xy), M = A/(x), K = [A --y--> A] (Tor_1(A/x, A/y) = 0, "
                "Z¹ = A free, H⁰ ⊗ M ≅ k, H⁰(K ⊗ M) = 0). With B¹ in place of Z¹ the criterion holds (re-proved from the "
                "two short exact sequences). Corollaire 7, which it serves, is true."),
    "H035.21": ((11, 11), "94/011.17m, margin (EGA IV 6.11.8)", "False",
                "The margin \"il suffit qu'il soit excellent, ou seulement qu'il satisfasse les conditions de EGA IV "
                "6.11.8\" overreaches in its second clause: localize k[t_i³, t_i⁴, t_i⁵ : i ≥ 1] at the complement of the "
                "union of the block ideals. The result is a one-dimensional noetherian Cohen-Macaulay domain (Nagata's "
                "criterion) whose non-Gorenstein points meet every nonempty open (the semigroup ⟨3,4,5⟩ is not "
                "symmetric), so no nonempty open carries a rank-one canonical module. The clause \"excellent\" stands; "
                "the pointer to EGA IV 6.11.8 is on the page."),
    "H035.22": ((12, 12), "94/012.5-8, the typescript leaf on absolute values", "Slip",
                "Multiplicativity, subadditivity and f(x) = 0 ⇒ x = 0 alone allow f ≡ 1, and then f(x − y) is no "
                "distance; with f(0) = 0 added, the normalized absolute value gives a field topology."),
    "H035.24": ((12, 12), "94/012.21-23", "Slip",
                "\"Tout élément n.1 est une racine de l'unité\" (ink) fails at n = p; what the argument uses holds: "
                "every nonzero element of the prime field has finite multiplicative order, so every normalized absolute "
                "value on a field of characteristic p > 0 is valuative."),
    "H035.25": ((12, 12), "94/012.24-25", "Slip",
                "\"Un nombre réel s\": the exponent must be strictly positive; equivalence of normalized absolute values "
                "is f = g^s with s > 0, and is equivalent to inducing the same field topology."),
    "H035.26": ((12, 12), "94/012.26-30", "Slip",
                "The classification on Q leaves out the trivial absolute value: a normalized absolute value on Q is "
                "trivial, |·|_p^s for a unique prime p and s > 0, or |·|_∞^s with 0 < s ≤ 1."),
}
# Work's notes on these pages (K94-01, in the notes zip): the verdict's verdicts on them
NOTES = {
    "work:K94-01#1 [Proposition 3]": ((4, 5), "the note is right: \"non nul\" is on the page (H035.5)"),
    "work:K94-01#1 [Remarque 5 bis]": ((8, 8), "right: the forward implication holds, the converse fails (H035.10)"),
    "work:K94-01#1 [Corollaire 7]": ((10, 10), "right: the result is true; P for Q and the Z¹ criterion corrected "
                                               "(H035.14, H035.15)"),
    "work:K94-01#1 [Corollaire 10 and margin]": ((11, 11), "right: the enlargement to the conditions of EGA IV 6.11.8 "
                                                           "is false, the clause \"excellent\" kept (H035.21)"),
}


def main():
    ce = {}
    for r in csv.DictReader(open(CE, encoding="utf-8"), delimiter="\t"):
        ce.setdefault(r["id"], []).append(r)
    run = {r["id"]: r for r in csv.DictReader(open(RUN, encoding="utf-8"), delimiter="\t")}

    def checks(i):
        ev = [f"{RUN_WHO}: {run[i]['status']}"] if i in run else []
        ev += [f"{r['date_utc']}, {r['who']}: {r['how']}: {r['result']}" for r in ce.get(i, [])]
        return " || ".join(ev)

    rows = []
    for i, ((a, b), loc, st, txt) in STATEMENTS.items():
        rows.append(dict(id=i, kind="statement", cote="94", scan_first=a, scan_last=b, locator=loc, status=st,
                         settled=txt, run_status=run[i]["status"] if i in run else "", checks=checks(i), source=SRC))
    for i, ((a, b), txt) in NOTES.items():
        rows.append(dict(id=i, kind="note verdict", cote="94", scan_first=a, scan_last=b, locator=i.split(" ", 1)[1],
                         status="", settled=txt, run_status="", checks=checks(i), source=SRC))
    for i, evs in ce.items():
        m = re.match(r"READINGS 94/(\d{3})\.", i)
        if m:
            s = int(m.group(1))
            rows.append(dict(id=i, kind="reading checked on the scan", cote="94", scan_first=s, scan_last=s,
                             locator=i[len("READINGS "):], status="", settled=evs[0]["result"], run_status="",
                             checks=checks(i), source=SRC))
    with open(HERE / "cote_94.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "rows:", {k: sum(1 for r in rows if r["kind"] == k) for k in {r["kind"] for r in rows}})


if __name__ == "__main__":
    main()

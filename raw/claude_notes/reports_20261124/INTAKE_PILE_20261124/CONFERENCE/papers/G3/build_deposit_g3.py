"""G3 deposit files (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026).
usage: python -I -B build_deposit_g3.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
tex = (HERE / "src" / "G3_paper.tex").read_text(encoding="utf-8")
assert "\\input{" not in tex and "\\include{" not in tex
assert "Matsusaka's\nconstruction gives" in tex or "Matsusaka's construction gives" in tex, "the repaired abstract is missing"
(HERE / "upload").mkdir(exist_ok=True)
(HERE / "upload" / "jacobian_index_abelian_varieties.tex").write_text(tex, encoding="utf-8", newline="\n")
abstract = (
    "For an abelian variety A over an algebraically closed field, let s_J(A) be the least positive integer n such that "
    "multiplication by n factors through a product of Jacobians of curves; s_J(A) = 1 exactly when A is a direct summand "
    "of such a product. We prove, in every characteristic, that multiplication by 2 factors through a product of "
    "Jacobians on every principally polarized abelian variety of dimension at most 5, and multiplication by 6 on every one "
    "of dimension 6; that s_J(A) divides gcd(2, δ(A)) for every abelian surface and gcd(6, δ(A)) for every abelian "
    "threefold, where δ(A) is the greatest common divisor of the Euler characteristics of line bundles on A. The known "
    "bound is (2g − 1)!. For a complex principally polarized A with minimal class γ = θ^{g−1}/(g − 1)!, let m(A) be the "
    "least positive multiple of γ that is the class of an algebraic cycle; Matsusaka's construction gives s_J(A) | m(A), "
    "and we prove m(A) | s_J(A)². With the theorems of Engel, de Gaay Fortman and Schreieder this gives the exact values "
    "s_J(A) = 2 for a very general principally polarized abelian variety of dimension 4 and 5, and s_J(A) = 6 in "
    "dimension 6; and every prime p ≤ g/2 divides s_J(A) in dimension g. Finally, s_J(A) is exactly the least integer n "
    "for which n times the inverse of the isomorphism H^{2g−1}(A)(g − 1) → H¹(Â) is induced by an integral algebraic "
    "cycle; this answers, for abelian varieties, the second question that Grothendieck asks on sheet 70 of cote 14 of his "
    "Montpellier archive. The results come from a run of GPT-6 Astra (ChatGPT Pro mode) and from Claude Opus 5.5 at "
    "effort max; they were checked and the text written by Claude Opus 5.5 at effort max.")
comments = (
    "Theorem A (every characteristic): [2] factors through a product of Jacobians on every principally polarized abelian "
    "variety of dimension ≤ 5 and [6] in dimension 6; s_J(A) | gcd(2, δ(A)) for abelian surfaces and s_J(A) | gcd(6, δ(A)) "
    "for threefolds (the known bound was (2g−1)!). Theorem B (complex, principally polarized): m(A) | s_J(A)², beside the "
    "known s_J(A) | m(A). Corollary C (very general, complex): s_J = 2 in dimensions 4 and 5 (this case also follows from "
    "published results), s_J = 6 in dimension 6, and every prime p ≤ g/2 divides s_J. Theorem D: s_J(A) is the least n "
    "such that n times the inverse of H^{2g−1}(A)(g−1) → H¹(Â) is induced by an integral algebraic cycle; this answers "
    "Grothendieck's second question on sheet 70 of cote 14 of the Montpellier archive for abelian varieties. Not claimed: "
    "abelian surfaces with δ even, threefolds with gcd(δ, 6) > 1, Theorem B and Corollary C in positive characteristic, "
    "Grothendieck's first question.\n\n"
    "Checks: Theorem A comes from a run of GPT-6 Astra (ChatGPT Pro mode); Claude Opus 5.5 at effort max re-proved part "
    "(b) with exact computations and read part (a). Theorem B was proved by Claude Opus 5.5 at effort max and read again "
    "by a second agent of that model, which wrote the text and proved Theorem D and Corollary C (iii); before posting, the "
    "main session (Claude Opus 5.5 at effort max) checked Theorems B and D, Corollary C and Remark 2.3 line by line. "
    "Literature: arXiv, OpenAlex citers of the closest papers, Hexagon; the full texts of Scavia-Suzuki and of the "
    "Engel-de Gaay Fortman-Schreieder papers searched for the new statements. No human has checked it; nothing is "
    "formalized. Records: https://github.com/KokunoYumeto/mathematics-workbenches")
provenance = (
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the "
    "text.\n\n"
    "How it was produced. Theorem A comes from a run of GPT-6 Astra (OpenAI), in ChatGPT Pro mode, that ended on 19 "
    "November 2026, in answer to a research prompt on the integral questions of cote 14 of Grothendieck's Montpellier "
    "archive. Theorem B and Corollary C (i)-(ii) were found and proved by Claude Opus 5.5 (Anthropic) at effort max on 24 "
    "November 2026, in a map of the project's geometry results. Claude Opus 5.5 at effort max wrote this text on 25 "
    "November 2026 and proved Theorem D, Corollary C (iii) and Remark 2.3.\n\n"
    "How it was checked. Claude Opus 5.5 at effort max re-proved Theorem A (b) and the Matsusaka coefficient with exact "
    "computations (22 November 2026), read the Prym step of Theorem A (a) in full and checked its sixfold step, and read "
    "Theorem B and Corollary C (i)-(ii) a second time with the cited statements opened (25 November 2026). Before "
    "posting, the main session of the project (Claude Opus 5.5 at effort max) read every page, checked Theorem B, "
    "Corollary C, Remark 2.3 and Theorem D line by line, and corrected two credits: only m | s_J² of Theorem B is new, "
    "and Corollary C (i) already follows from published results. Literature: arXiv, the works citing the closest papers "
    "in OpenAlex, and the Hexagon catalogue were searched; the full texts of Scavia-Suzuki and of two papers of Engel, de "
    "Gaay Fortman and Schreieder (one through its Section 3) were searched for the new statements, and none was found. "
    "The cited places in Beauville, Alexeev-Donagi-Farkas-Izadi-Ortega, Mumford, Oort, Oort-Ueno, Fulton, Milne and "
    "Voisin were opened by the run. No human has checked the proofs or the text, and nothing is formalized.\n\n"
    "Where the records are. https://github.com/KokunoYumeto/mathematics-workbenches\n\n"
    "The text and accompanying work are dedicated to the public domain under CC0 1.0.")
meta = {
    "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
    "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
    "title": "Multiplication by 2 and by 6 through products of Jacobians, and the Jacobian index of a very general abelian variety of dimension 4, 5 and 6",
    "subject": "math.AG", "crossListSubjects": [],
    "tags": ["abelian varieties", "products of Jacobians", "integral Hodge conjecture", "algebraic cycles",
             "minimal curve class", "Prym varieties", "Jacobian index", "positive characteristic",
             "Grothendieck's Montpellier archive", "AI-generated mathematics"],
    "mscCodes": ["14K12", "14C25", "14H40", "14C30", "14K02"],
    "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
    "abstract": abstract, "comments": comments, "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort max)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10 and len(meta["mscCodes"]) <= 5 and len(meta["comments"]) <= 2000, len(meta["comments"])
json.dump(meta, open(HERE / "HEXAGON_METADATA_G3.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)})

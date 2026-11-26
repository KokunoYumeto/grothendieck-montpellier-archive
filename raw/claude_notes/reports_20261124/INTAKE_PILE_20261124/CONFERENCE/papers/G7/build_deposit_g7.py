"""G7 deposit files (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026).
usage: python -I -B build_deposit_g7.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
tex = (HERE / "src" / "G7_paper.tex").read_text(encoding="utf-8")
assert "\\input{" not in tex and "\\include{" not in tex
assert "Before posting, the main" in tex, "the final source is missing the main session's check sentence"
(HERE / "upload").mkdir(exist_ok=True)
(HERE / "upload" / "wild_double_cover_genus_two.tex").write_text(tex, encoding="utf-8", newline="\n")
abstract = (
    "Over an algebraically closed field of characteristic two, the surface b² + (t⁵ + t²a²)b + a⁵ = 0 has one singular "
    "point, and its minimal resolution has one exceptional curve C: the smooth curve of genus two with affine equation "
    "y² + y = x⁵, with C² = −1. We show that this surface has a connected Galois double cover, étale away from the "
    "singular point, whose ramification along C is fierce: ramification index one and a purely inseparable residue "
    "extension of degree two. A run of this project proved that no such wild cover exists when the formal neighbourhood "
    "of the exceptional curve is that of the zero section of a negative line bundle, as for graded surface cones. The "
    "example shows that this hypothesis cannot be dropped, even for a Gorenstein singularity with one smooth exceptional "
    "curve. The weighted homogeneous surface b² + t⁵b + a⁵ = 0 has the same exceptional curve, with the same "
    "self-intersection, and every connected Galois cover of it that is étale away from the singular point is tame along "
    "that curve; so the two germs are not formally isomorphic. The example and its proof come from a run of GPT-6 Astra "
    "(ChatGPT Pro mode); they were checked, the comparison was added and the text was written by Claude Opus 5.5 at "
    "effort max.")
comments = (
    "Theorem B: in characteristic two, S: b² + (t⁵ + t²a²)b + a⁵ = 0 has one singular point, resolved by the (2,5,1) "
    "weighted blow-up with one exceptional curve C: y² + y = x⁵ of genus two, C² = −1; T → S, a = c² + t²c, "
    "b = t²d + c⁵, is a connected Z/2 Galois cover étale off the point, fierce along C. Theorem A (the run's tameness "
    "theorem for graded cones) is quoted. Corollary C: its linearity hypothesis cannot be dropped; the graded "
    "b² + t⁵b + a⁵ = 0 has the same curve and self-intersection but only tame covers, so the complete local rings are "
    "not isomorphic. Lemma 2.6: a finite cover with a rational (for instance regular) source lies only over rational "
    "exceptional curves; so the source here is a singular, non-rational double point, and the known wild covers of "
    "Artin, Lorenzini-Schröer, Ito-Schröer and Matsumoto cannot contain the example. Not claimed: that every non-linear "
    "formal neighbourhood carries a wild cover; anything on finite generation of fundamental groups.\n\n"
    "Checks: the example comes from a run of GPT-6 Astra (ChatGPT Pro mode); Claude Opus 5.5 at effort max re-proved it "
    "by hand and reran the run's certificate, and a second agent at effort high checked it with its own program; an "
    "independent check (Claude Opus 5.5 at effort max) checked Lemma 2.3 and Corollary C and proved Lemma 2.6; before "
    "posting, the main session (Claude Opus 5.5 at effort max) read every page and checked every lemma line by line. "
    "Literature: arXiv, journals, Hexagon; the full texts of Lorenzini-Schröer, Ito-Schröer and Matsumoto read. No human "
    "has checked it; nothing is formalized. Records: https://github.com/KokunoYumeto/mathematics-workbenches")
provenance = (
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the "
    "text.\n\n"
    "How it was produced. Theorems A and B and their proofs come from a run of GPT-6 Astra (OpenAI), in ChatGPT Pro "
    "mode, that ended on 20 November 2026, on Grothendieck's notes on the fundamental group in cote 29 of his Montpellier "
    "archive. Claude Opus 5.5 (Anthropic) at effort max wrote this text on 25 November 2026, proved Corollary C (ii)-(iii) "
    "and gave a shorter proof of Lemma 2.3; a second agent of the same model and effort, the independent checker, proved "
    "Lemma 2.6 and the identification of the radial valuation in Corollary C (ii).\n\n"
    "How it was checked. Claude Opus 5.5 at effort max made a targeted check of Theorem A and re-proved Theorem B by hand "
    "at the intake of the run (21-22 November 2026), and reran the run's certificate (26 exact assertions over F_2); "
    "Claude Opus 5.5 at effort high checked Theorem B with its own program (24 November 2026). On 25 November 2026 an "
    "independent check (Claude Opus 5.5 at effort max) made a targeted check of Lemma 2.3 and Corollary C, found that the "
    "source T is singular at the point, and read the arXiv full texts of Lorenzini-Schröer, Ito-Schröer and Matsumoto. "
    "Before posting, the main session of the project (Claude Opus 5.5 at effort max) read every page and checked Lemmas "
    "2.1-2.6, the proof of Theorem B and Corollary C line by line. Artin's two papers were not opened (no free copy); "
    "Lemma 2.6 shows they cannot contain the example. No human has checked the proofs or the text, and nothing is "
    "formalized.\n\n"
    "Where the records are. https://github.com/KokunoYumeto/mathematics-workbenches\n\n"
    "The text and accompanying work are dedicated to the public domain under CC0 1.0.")
meta = {
    "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
    "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
    "title": "A wild quasi-étale double cover over a single smooth genus-two exceptional curve in characteristic two",
    "subject": "math.AG", "crossListSubjects": ["math.AC"],
    "tags": ["surface singularities", "wild ramification", "quasi-étale covers", "characteristic two",
             "Artin-Schreier curves", "local fundamental group", "weighted blow-up", "tameness",
             "Grothendieck's Montpellier archive", "AI-generated mathematics"],
    "mscCodes": ["14J17", "14E20", "14B05", "14H30", "13A35"],
    "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
    "abstract": abstract, "comments": comments, "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort max and high)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10 and len(meta["mscCodes"]) <= 5 and len(meta["comments"]) <= 2000, len(meta["comments"])
json.dump(meta, open(HERE / "HEXAGON_METADATA_G7.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)})

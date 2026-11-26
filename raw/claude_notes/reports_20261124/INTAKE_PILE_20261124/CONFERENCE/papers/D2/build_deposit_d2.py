"""D2 deposit files (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026).
usage: python -I -B build_deposit_d2.py"""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
tex = (HERE / "src" / "D2_paper.tex").read_text(encoding="utf-8")
assert "\input{" not in tex and "\include{" not in tex
(HERE / "upload").mkdir(exist_ok=True)
(HERE / "upload" / "classifying_spaces_finite_monoids.tex").write_text(tex, encoding="utf-8", newline="\n")
a = (HERE / "ABSTRACT.md").read_text(encoding="utf-8").split("**Abstract.**", 1)[1].split("\n\n", 1)[0]
abstract = " ".join(a.split())
comments = (
    "Theorem 1.1: if the homology of a finite monoid M is bounded, its universal group U(M) is trivial; if a prime p "
    "divides |U(M)|, then H_k(BM; F_p) is non-zero for infinitely many k. Theorem 1.2: BM is homotopy equivalent to a "
    "finite complex if and only if to a finite-dimensional one, if and only if its homology is bounded. With "
    "Ben-Bassat's Theorem C, the spaces BM of finite monoids with bounded homology are exactly the finite simply "
    "connected complexes, and Conjecture 7.1 of arXiv:2610.38760v1 is false (the real projective plane is a "
    "counterexample). The proof compares the K-theory of BM with that of BG for the finite group G = eMe of the "
    "minimal ideal, through Atiyah's completion theorem. Examples: a six-element monoid with trivial universal group "
    "whose classifying space is a wedge of spheres of every dimension at least 2, and a 23-element monoid whose "
    "classifying space is the complex projective plane.\n\n"
    "Checks: the main theorems were derived independently by Claude (Fable 5.2, Opus 5.5) and by GPT-6 Astra; the "
    "examples were recomputed by independent programs in exact integer arithmetic. No human has checked it; nothing "
    "is formalized. Records: https://github.com/KokunoYumeto/mathematics-workbenches")
provenance = (
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the "
    "text.\n\n"
    "How it was produced. The finite-dimensional case of the main theorem and the failure of Conjecture 7.1 of "
    "Ben-Bassat's arXiv:2610.38760v1 were found by a run of GPT-6 Astra (OpenAI), in ChatGPT Pro mode, on 10 November "
    "2026; the general statements (Theorems 1.1, 1.2 and 2.1) were proved by Claude Fable 5.2 (Anthropic) at effort "
    "max on 12 November 2026; the two examples come from runs of GPT-6 Astra (ChatGPT Pro mode), 12-17 November 2026. "
    "Claude Fable 5.2 at effort max wrote the text on 25 November 2026.\n\n"
    "How it was checked. The main theorems were derived again by a second Claude Fable 5.2 at effort max, checked by "
    "Claude Opus 5.5 at effort high and at effort max, and derived independently by GPT-6 Astra (ChatGPT Pro mode) on "
    "25 November 2026; the examples were recomputed by independent programs in exact integer arithmetic. Before "
    "posting, Claude Opus 5.5 at effort max read every page. No human has checked it; nothing is formalized. The "
    "author of arXiv:2610.38760 was informed of the counterexample on 12 November 2026.\n\n"
    "Where the records are. https://github.com/KokunoYumeto/mathematics-workbenches\n\n"
    "The text and accompanying work are dedicated to the public domain under CC0 1.0.")
meta = {
    "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
    "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
    "title": "Classifying spaces of finite monoids with bounded homology",
    "subject": "math.AT", "crossListSubjects": ["math.GR", "math.KT"],
    "tags": ["classifying spaces", "finite monoids", "universal group", "bounded homology", "topological K-theory",
             "Atiyah completion theorem", "Fiedorowicz conjecture", "complex projective plane", "homotopy types",
             "AI-generated mathematics"],
    "mscCodes": ["55R35", "20M50", "55P15", "55N15", "20M10"],
    "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
    "abstract": abstract, "comments": comments, "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort high and max)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10 and len(meta["mscCodes"]) <= 5 and len(meta["comments"]) <= 2000, (len(meta["comments"]))
json.dump(meta, open(HERE / "HEXAGON_METADATA_D2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)})
print("ABSTRACT ends:", abstract[-120:])

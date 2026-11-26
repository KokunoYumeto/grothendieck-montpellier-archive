"""T1 deposit files (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026).
usage: python -I -B build_deposit_t1.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
tex = (HERE / "src" / "T1_paper.tex").read_text(encoding="utf-8")
assert "\\input{" not in tex and "\\include{" not in tex
(HERE / "upload").mkdir(exist_ok=True)
(HERE / "upload" / "first_l2_betti_number_aspherical.tex").write_text(tex, encoding="utf-8", newline="\n")
a = (HERE / "ABSTRACT.md").read_text(encoding="utf-8").split("**Abstract.**", 1)[1].split("\n\n", 1)[0]
abstract = " ".join(a.split())
comments = (
    "Theorem A: for every finite aspherical Poincaré complex of formal dimension n >= 3, hence for every closed "
    "aspherical topological manifold of dimension n >= 3, the L2-Betti numbers b_1 and b_{n-1} vanish. Theorem B: the "
    "same for finitely presented Poincaré duality groups of dimension n >= 3. Theorem C is the group criterion that "
    "Sections 3-10 of OpenAI's manuscript 'The Singer conjecture in dimension four' (dated 25 September 2026, released "
    "6 October 2026, unrefereed) prove when read for their hypotheses: a finitely presented torsion-free one-ended group "
    "with H^2(G; F_2 G) = 0 and no splitting over a finite or two-ended subgroup has b_1 = 0. We cite that argument and "
    "do not reproduce it; Section 3 says where it calls on dimension four and lists its 38 statements with their "
    "inputs. New here are the reductions of Section 2 in every dimension n >= 3 and for PD(n) groups, with full proofs. "
    "That the method gives every n >= 3 was observed, without proof, by u/Apprehensive_Sand951 on r/math in October "
    "2026. Theorems A and B rest on the unrefereed argument and should be cited with that condition.\n\n"
    "Checks: Section 2 by Claude Opus 5.5 and Claude Fable 5.2, and an independent check of the finished text; Sections "
    "3-10 of the manuscript read line by line by Claude Fable 5.2 at effort max, Sections 8-9 again by Claude Opus 5.5 "
    "at effort high. No human has checked it; nothing is formalized. "
    "Records: https://github.com/KokunoYumeto/mathematics-workbenches")
provenance = (
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the "
    "text.\n\n"
    "How it was produced. The method and the argument behind Theorem C are those of OpenAI's manuscript 'The Singer "
    "conjecture in dimension four' (github.com/openai/math, Apache-2.0), which is cited and not reproduced. The "
    "reductions of Section 2 for every n >= 3, the criterion in the form of Theorem C and the extension to PD(n) groups "
    "come from a run of GPT-6 Astra (OpenAI), in ChatGPT Pro mode, of 22-23 October 2026. Claude Fable 5.2 (Anthropic) "
    "at effort max wrote the text on 25 November 2026 and proved Section 2 afresh.\n\n"
    "How it was checked. Section 2: Claude Opus 5.5 at effort high and Claude Fable 5.2 at effort max (24-25 November "
    "2026), then an independent check of the finished text by Claude Opus 5.5 at effort high. Sections 3-10 of the "
    "manuscript: line by line by Claude Fable 5.2 at effort max; Sections 8-9 again, independently, by Claude Opus 5.5 "
    "at effort high; in part by Claude Opus 5.5 at effort max in October. Before posting, Claude Opus 5.5 at effort max "
    "read every page. No human has checked it; nothing is formalized.\n\n"
    "Where the records are. https://github.com/KokunoYumeto/mathematics-workbenches\n\n"
    "The text and accompanying work are dedicated to the public domain under CC0 1.0.")
meta = {
    "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
    "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
    "title": "The first L²-Betti number of aspherical manifolds and Poincaré duality groups of dimension at least three",
    "subject": "math.GT", "crossListSubjects": ["math.GR", "math.AT"],
    "tags": ["L2-Betti numbers", "Singer conjecture", "aspherical manifolds", "Poincaré duality groups",
             "convergence groups", "harmonic chains", "geometric group theory", "group cohomology", "Bowditch",
             "AI-generated mathematics"],
    "mscCodes": ["57P10", "20F65", "57N65", "20J05", "55N25"],
    "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
    "abstract": abstract, "comments": comments, "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort high and max)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10 and len(meta["mscCodes"]) <= 5 and len(meta["comments"]) <= 2000, len(meta["comments"])
json.dump(meta, open(HERE / "HEXAGON_METADATA_T1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)})
print("ABSTRACT ends:", abstract[-160:])

"""Hexagon metadata of the HNAM note (main session 329fb1e6, Claude Opus 5.5 at effort max, 24 Nov 2026).
The abstract, comments and provenance are the files written by ae2754d9 (Claude Fable 5.2 at effort max) and brought in
line by a25c2acb (Claude Opus 5.5 at effort high); the other fields follow our earlier notes (WB-0005)."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def text(name):
    return open(name, encoding="utf-8").read().strip()


abstract = re.sub(r"\s+", " ", text("ABSTRACT.txt"))
comments = text("COMMENTS_FIELD.txt")
for old, new in [("(J. Complexity 12 (1996), Theorems 1, 2, 9; DIMACS TR 96-27, Theorem 2)", "(J. Complexity 12 (1996))"),
                 ("(Ait El Manssour, Balaji, Nosan, Shirmohammadi, Worrell)", "(Ait El Manssour et al.)"),
                 ("; on 25 November 2026 it checked this text,", "; it then checked this text,")]:
    assert old in comments, old
    comments = comments.replace(old, new)
provenance = text("PROVENANCE_FIELD.txt").replace("25 November 2026", "24 November 2026")  # UTC date of the recheck
tex = open("hnam_note.tex", encoding="utf-8").read()
m = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}\s*\n", tex, re.S)
title = re.sub(r"\s+", " ", m.group(1).replace("\\\\", " ")).strip() if m else ""
meta = {
    "arxivId": None,
    "citationsConfirmed": True,
    "communityInterestConfirmed": True,
    "correctnessConfirmed": True,
    "rightsConfirmed": True,
    "submittingContributorIndex": 0,
    "submittingOrganizationId": None,
    "title": title,
    "subject": "cs.CC",
    "crossListSubjects": ["math.NT", "math.AG"],
    "tags": ["Hilbert's Nullstellensatz", "Arthur-Merlin protocols", "polynomial hierarchy",
             "generalized Riemann hypothesis", "zero-free regions", "Dedekind zeta functions", "prime ideal theorem",
             "Schubert coefficients", "geometric complexity theory", "AI-generated mathematics"],
    "mscCodes": ["68Q15", "11R44", "14Q20", "13P15"],
    "authorshipMode": "no-human-author-claimed",
    "humanUnderstanding": "none",
    "license": "CC0 1.0",
    "abstract": abstract,
    "comments": comments,
    "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort high and max)", "version": None},
        {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
    ],
}
json.dump(meta, open("HEXAGON_METADATA_HNAM.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("title:", title)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)}, "tags", len(meta["tags"]))

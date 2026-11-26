"""Hexagon metadata of the A1 note, "The profinite Grothendieck-Teichmuller monoid is a group, on a question of Lochak
and Schneps" (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026). The abstract, comments and provenance
are the files written by the conference convener ae84c4aa (Claude Fable 5.2 at effort max), with the check-state
sentences of ae4ae3dc's independent check (Claude Opus 5.5 at effort max) applied by the main session; the other fields
follow our earlier notes (WB-0007)."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def text(name):
    return open(name, encoding="utf-8").read().strip()


meta = {
    "arxivId": None,
    "citationsConfirmed": True,
    "communityInterestConfirmed": True,
    "correctnessConfirmed": True,
    "rightsConfirmed": True,
    "submittingContributorIndex": 0,
    "submittingOrganizationId": None,
    "title": "The profinite Grothendieck-Teichmüller monoid is a group, on a question of Lochak and Schneps",
    "subject": "math.GR",
    "crossListSubjects": ["math.AT", "math.NT", "math.AG"],
    "tags": ["Grothendieck-Teichmüller group", "Grothendieck-Teichmüller monoid", "profinite free groups",
             "profinite surface groups", "endomorphisms of profinite groups", "parenthesized braids",
             "little disks operad", "Lochak-Schneps open problems", "homology of finite covers",
             "AI-generated mathematics"],
    "mscCodes": ["20E18", "20E36", "18M60", "14H30"],
    "authorshipMode": "no-human-author-claimed",
    "humanUnderstanding": "none",
    "license": "CC0 1.0",
    "abstract": re.sub(r"\s+", " ", text("ABSTRACT.txt")),
    "comments": text("COMMENTS_FIELD.txt"),
    "provenance": text("PROVENANCE_FIELD.txt"),
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort high and max)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10 and len(meta["comments"]) <= 2000
json.dump(meta, open("HEXAGON_METADATA_A1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)}, "tags", len(meta["tags"]))

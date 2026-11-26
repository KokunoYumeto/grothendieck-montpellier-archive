"""Hexagon metadata for WB-0007 (H17); authors copied at create time. Main session 329fb1e6 (Claude Opus 5.5 at effort max)."""
import json, pathlib, re
H = pathlib.Path(__file__).resolve().parent
NL = chr(10)
tex = (H / "h17_note_wb0007.tex").read_text(encoding="utf-8")
ab = re.search(r"\\begin\{abstract\}\s*\\noindent\s*(.*?)\s*\\end\{abstract\}", tex, re.S).group(1)
macros = {r"\GTz": r"\widehat{\mathrm{GT}}_0", r"\GT": r"\widehat{\mathrm{GT}}", r"\GQ": r"G_{\mathbb Q}"}
for k in (r"\GTz", r"\GT", r"\GQ"):
    ab = ab.replace(k, macros[k])
ab = ab.replace("Teichm\\\"uller", "Teichmüller")
ab = " ".join(ab.split())
assert not re.search(r"\\(GT|GQ|Zh|Fh|Bh|Gh)\b", ab), ab
WB = "https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/works/WB-0007.md"
m = {
 "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
 "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
 "title": "Relation (IV) of Nakamura and Schneps holds on the profinite Grothendieck-Teichmüller group, with an application to the two elliptic points of the modular curve",
 "subject": "math.GR", "crossListSubjects": ["math.NT", "math.AG", "math.GT"],
 "tags": ["Grothendieck-Teichmüller group", "profinite braid groups", "mapping class groups", "Galois action",
          "Nakamura-Schneps relation", "Hatcher-Lochak-Schneps group", "modular group", "elliptic points",
          "AI-generated mathematics"],
 "mscCodes": ["20F36", "14H30", "11R32", "57K20"],
 "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
 "abstract": ab,
 "comments": NL.join([
   "Relation (IV) is H. Nakamura's; the subgroup it defines with (III') is Nakamura and Schneps's (Invent. Math. 2000), who "
   "proved that Galois elements satisfy it and left open whether the subgroup is all of GT-hat; Lochak, Nakamura and Schneps "
   "(February 2026) still called this unclear. The group Lambda and its action on the tower are Hatcher, Lochak and Schneps's; "
   "the implication from the normalized relation (IV) to their relation (R) is Schneps's. The proofs rest on the theorem of "
   "Boggi and Zalesskii on finite p-subgroups of profinite mapping class groups and on the theorem of Hoshi, Minamide and "
   "Mochizuki on the outer automorphisms of genus-zero configuration groups. New here: (IV) on all of GT-hat, the decomposition "
   "GT-hat = Lambda_0 . G_Q, and the vanishing of the level-twelve character delta on normalized elements.", "",
   "Checks: Claude Fable 5.2 at effort max checked the proofs, wrote the text and rewrote several proofs; Claude Opus 5.5 at effort "
   "max refereed it as second reader and checked Theorems 1-2 again before deposit. No human has checked it. Records: " + WB]),
 "provenance": NL.join([
   "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.", "",
   "How it was produced. GPT-6 Astra (OpenAI), in ChatGPT Pro mode, produced the mathematics in research runs of November 2026 "
   "on notes of Grothendieck's La longue marche a travers la theorie de Galois, prompted by Claude Opus 5.5 (Anthropic) at effort "
   "max. Claude Fable 5.2 (Anthropic), at effort max, wrote the present text on 23 November 2026 as editor, rewriting several "
   "proofs (the finite-subgroup steps through Boggi-Zalesskii, the shear lemma, the unit lemma, half of one proposition).", "",
   "How it was checked. Claude Fable 5.2, at effort max, checked every step of the runs' proofs of Theorems 1 and 2 (18 "
   "November), re-proved the final computation independently (21 November) and checked the chain behind the hexagonal "
   "self-similarity (23 November). Claude Opus 5.5, at effort max, checked the parity computation exhaustively over Z/12 with "
   "its own program (22 November) and, as second reader (23 November), followed every step of Sections 4 and 8 and of the "
   "rewritten proofs, re-derived the matrix and braid identities, opened Hoshi-Minamide-Mochizuki at the source and found no "
   "mathematical error. Claude Opus 5.5, at effort max, read the text again before deposit and recomputed the steps behind "
   "Theorems 1 and 2. A remark on a character Delta of the larger group is cited from the runs and marked as not refereed; it "
   "is not used in the theorems. arXiv, the web and Hexagon were searched on 23 November 2026. No human has checked the proofs "
   "or the text, and nothing is formalized.", "",
   "Where the records are. " + WB, "",
   "The text and accompanying work are dedicated to the public domain under CC0 1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/)."]),
 "aiSystems": [{"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
               {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
               {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort max)", "version": None}],
}
assert len(m["comments"]) <= 2000, len(m["comments"])
(H / "HEXAGON_METADATA_WB0007.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline=NL)
print("comments", len(m["comments"]), "abstract", len(m["abstract"]), "provenance", len(m["provenance"]))
print(m["abstract"][:300])

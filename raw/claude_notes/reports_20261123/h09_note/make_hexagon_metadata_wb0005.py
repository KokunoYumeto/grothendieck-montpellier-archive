"""Hexagon metadata for WB-0005 (H09), modelled on HEXAGON_METADATA_H01.json; authors are copied at create time
(hexagon_api.py create-like). Main session 329fb1e6 (Claude Opus 5.5 at effort max), 23 Nov 2026."""
import json, pathlib, re
H = pathlib.Path(__file__).resolve().parent
NL = chr(10)
tex = (H / "h09_note_v4.tex").read_text(encoding="utf-8")
ab = re.search(r"\\begin\{abstract\}\s*(.*?)\s*\\end\{abstract\}", tex, re.S).group(1)
ab = ab.replace(r"\Z_{(p)}", r"\mathbb Z_{(p)}").replace(r"Teichm\"uller", "Teichmüller").replace(r"Alp\"oge", "Alpöge")
ab = " ".join(ab.split())
assert "\\Z" not in ab.replace("\\Z_", "") and '\\"' not in ab, ab
WB = "https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/works/WB-0005.md"
m = {
 "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
 "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
 "title": "Divisibility of invariant derivatives on formal groups of every height, on a question of Katz",
 "subject": "math.NT", "crossListSubjects": ["math.AG"],
 "tags": ["formal groups", "invariant derivation", "p-adic interpolation", "Katz's question", "Lubin-Tate groups",
          "Honda formal group", "Cartier duality", "p-divisible groups", "supersingular reduction", "AI-generated mathematics"],
 "mscCodes": ["14L05", "11S31", "11S80", "11B68"],
 "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
 "abstract": ab,
 "comments": NL.join([
   "This note answers the divisibility question N. Katz asked in 1977 (Formal groups and p-adic interpolation, Asterisque "
   "41-42, section I) at every height, for every integral function, with optimal slope and constant. The question and the "
   "height-two bound for functions with the trace condition are Katz's (1977, Corollary 2; 1981, Main Theorem 3.11), and so is "
   "the identity between translation operators and the logarithm on which the affine bound rests (1981, Corollary 1.8). For "
   "Lubin-Tate groups over unramified bases the bound c_h n - (h-1) follows from results of K. Bannai and S. Kobayashi (2016, "
   "Propositions 3.3 and 3.5); J. Boxall had the slope with a constant depending on f. New here: the bound for every formal "
   "group satisfying the hypothesis, the floor sum and its sharpness, the comparison with Katz's bound at height two, the two "
   "statements on ramified bases, and the integral model of the Cartier dual of the Honda group with its sharp slopes.", "",
   "Checks: the proofs were checked by Claude Opus 5.5 at effort high and line by line at effort max, reread by Claude Fable 5.2 "
   "at effort max, which edited the text and repaired one clause of a proof, and read again in full at effort max before "
   "deposit. No human has checked them. Records and checks: " + WB]),
 "provenance": NL.join([
   "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.", "",
   "How it was produced. GPT-6 Astra (OpenAI), in ChatGPT Pro mode, proved the results in November 2026, in a research run on "
   "Katz's question and the local step of Alpöge's note, prompted by Claude Opus 5.5 (Anthropic) at effort max. Claude Opus 5.5, "
   "at effort max, wrote the text on 23 November 2026, stating Theorem A over p-torsion-free Z_(p)-algebras and giving "
   "Proposition 4.1 its present form. Claude Fable 5.2 (Anthropic), at effort max, edited it the same day.", "",
   "How it was checked. The run checked the bounds and witnesses at 224 orders in six Lubin-Tate examples. Claude Opus 5.5, at "
   "effort high, checked the affine bound, the floor sum and Theorem C (21 November 2026). Claude Opus 5.5, at effort max, "
   "checked every proof line by line, with Katz 1981, Lubin-Tate 1966, Hazewinkel and Tate read at the cited places (23 "
   "November). Claude Fable 5.2, at effort max, reread every proof, found one false clause in the proof of the rescaling lemma "
   "and repaired it, with no statement changed. Claude Opus 5.5, at effort max, read the edited text again in full before "
   "deposit. Literature and Hexagon were searched before the note was written. No human has checked the proofs or the text, "
   "and nothing is formalized.", "",
   "Where the records are. " + WB, "",
   "The text and accompanying work are dedicated to the public domain under CC0 1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/)."]),
 "aiSystems": [{"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
               {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort high and max)", "version": None},
               {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None}],
}
assert len(m["comments"]) <= 2000, len(m["comments"])
(H / "HEXAGON_METADATA_WB0005.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline=NL)
print("comments", len(m["comments"]), "abstract", len(m["abstract"]), "provenance", len(m["provenance"]))
print(m["abstract"][:200])

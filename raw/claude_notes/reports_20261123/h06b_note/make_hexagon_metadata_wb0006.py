"""Hexagon metadata for WB-0006 (H06b); authors copied at create time. Main session 329fb1e6 (Claude Opus 5.5 at effort max)."""
import json, pathlib, re
H = pathlib.Path(__file__).resolve().parent
NL = chr(10)
tex = (H / "h06b_note_wb0006.tex").read_text(encoding="utf-8")
ab = re.search(r"\\begin\{abstract\}\s*\\noindent\s*(.*?)\s*\\end\{abstract\}", tex, re.S).group(1)
ab = " ".join(ab.split())
WB = "https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/works/WB-0006.md"
m = {
 "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
 "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
 "title": "The question of Anderson and Ihara on the pro-p Galois action on the projective line minus three points, at every prime satisfying Vandiver's conjecture",
 "subject": "math.NT", "crossListSubjects": ["math.AG"],
 "tags": ["Galois action on fundamental groups", "projective line minus three points", "pro-p outer Galois representation",
          "Anderson-Ihara question", "Vandiver's conjecture", "Greenberg's conjecture", "Sharifi's conjectures", "Iwasawa theory",
          "AI-generated mathematics"],
 "mscCodes": ["11R23", "14H30", "11R34", "11R18"],
 "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
 "abstract": ab,
 "comments": NL.join([
   "This note answers, at every prime satisfying Vandiver's conjecture, the question of G. Anderson and Y. Ihara (Ann. of Math. "
   "128 (1988), p. 272, question (a)): whether the field cut out by the kernel of the pro-p outer Galois action on the "
   "fundamental group of the projective line minus three points is the maximal pro-p extension of Q(mu_p) unramified outside "
   "p. The inclusion is Ihara's. At odd regular primes the equality is R. Sharifi's theorem (2002) combined with F. Brown's "
   "proof of the Deligne-Ihara conjecture; Sharifi described the irregular case as an open question in 2019. The arithmetic "
   "input is published: Wake and Wang-Erickson proved that Vandiver's conjecture implies Sharifi's conjecture, and Fukaya and "
   "Kato turned it into the generation of H^2 by cup products of cyclotomic units. New here are the comparison of finite-level "
   "cup products with the class-two extension (Lemma 4.1) and the separation of Magnus coefficients by poles (Lemma 5.1).", "",
   "Checks: Claude Opus 5.5 at effort high checked Sections 4-7 and did the literature search; Claude Fable 5.2 at effort max "
   "refereed Sections 3-6 independently before deposit; Claude Opus 5.5 at effort max checked Section 7. No human has checked "
   "the proofs. Records and checks: " + WB]),
 "provenance": NL.join([
   "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.", "",
   "How it was produced. GPT-6 Astra (OpenAI), in ChatGPT Pro mode, produced the mathematics and the text of Sections 3 to 8 in "
   "research runs of November 2026, prompted by Claude Opus 5.5 (Anthropic) at effort max. Claude Fable 5.2 (Anthropic), at "
   "effort max, wrote Sections 1 and 2 and edited the text on 23 November 2026; it removed the treatment of the prime 2 and "
   "changed nothing else of mathematical content.", "",
   "How it was checked. Claude Opus 5.5, at effort high, checked the separation lemma and the deduction at Vandiver primes in "
   "earlier versions (21-22 November 2026), and on 23 November the persistence lemma, the deduction of X_p^+ = 0, and the "
   "present text of Sections 4 to 6 step by step with the cited theorems of Wake and Wang-Erickson and of Fukaya and Kato opened "
   "at the places cited, finding no mathematical error; it also searched the literature and Hexagon, and found no earlier "
   "statement of the equality at an irregular prime. Claude Opus 5.5, at effort max, read the whole note and checked Section 7 "
   "and Lemma 6.1 in full. Claude Fable 5.2, at effort max, then refereed Sections 3 to 6 independently against the cited "
   "theorems of Hain and Matsumoto, Wake and Wang-Erickson, and Fukaya and Kato, and found no error. The statements cited from "
   "Milne's notes, Sharifi's lecture notes and Iwasawa 1981 were not reopened. No human has checked the proofs or the text, and "
   "nothing is formalized.", "",
   "Where the records are. " + WB, "",
   "The text and accompanying work are dedicated to the public domain under CC0 1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/)."]),
 "aiSystems": [{"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
               {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
               {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort high and max)", "version": None}],
}
assert len(m["comments"]) <= 2000, len(m["comments"])
(H / "HEXAGON_METADATA_WB0006.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline=NL)
print("comments", len(m["comments"]), "abstract", len(m["abstract"]), "provenance", len(m["provenance"]))
print(m["abstract"][-260:])

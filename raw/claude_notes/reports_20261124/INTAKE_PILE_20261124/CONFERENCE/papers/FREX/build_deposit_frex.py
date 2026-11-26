"""FREX deposit files (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026):
1. upload/exactness_colimits_amenability.tex: a copy of src/FREX_paper.tex (one file, no \\input);
2. HEXAGON_METADATA_FREX.json: the Hexagon metadata, from ABSTRACT.md and the fields written below.
usage: python -I -B build_deposit_frex.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "src"

# 1. the source, unchanged
tex = (SRC / "FREX_paper.tex").read_text(encoding="utf-8")
assert "\\input{" not in tex and "\\include{" not in tex
(HERE / "upload").mkdir(exist_ok=True)
(HERE / "upload" / "exactness_colimits_amenability.tex").write_text(tex, encoding="utf-8", newline="\n")
print("source:", len(tex), "characters")

# 2. the metadata
abstract_md = (HERE / "ABSTRACT.md").read_text(encoding="utf-8")
abstract = abstract_md.split("**Abstract.**", 1)[1].split("\n\n", 1)[0]
abstract = " ".join(abstract.split())

comments = (
    "This paper compares two properties of the automorphism group G of a countable homogeneous structure M: "
    "exactness of colimits over the category of finite substructures of M and embeddings, and amenability. "
    "Theorem 1.2: colimits of R-modules over this category are exact if and only if coinvariants preserve "
    "monomorphisms of smooth R[G]-modules, a property of the topos of continuous G-sets. Theorem 1.3 (transfer): "
    "given a subgroup H with exact coinvariants and finitely many orbits on each G/G_B, exactness over a field k is "
    "equivalent to a G-invariant, finitely additive, k-valued function of total mass 1 on the expansions that H "
    "defines. Theorem 1.4: for the generic poset with an independent linear order, colimits are exact over every ring, "
    "while G is not amenable (Kechris-Sokić). Theorem 1.5: for the ordered F_2-vector space of countable dimension, G "
    "is amenable and colimits are exact over every Q-algebra, but over no ring in which 2 is not invertible. "
    "Corollary 1.6: Evans's membership test and separation property hold for the generic poset with an independent "
    "linear order.\n\n"
    "Checks: the results come from a run of GPT-6 Astra (ChatGPT Pro mode), followed step by step at intake by Claude "
    "Opus 5.5 at effort max; Claude Fable 5.2 at effort max wrote the text and derived every proof again; another "
    "Claude Fable 5.2 at effort max checked the finished text independently (25 November 2026): no theorem wrong, five "
    "results proved again before reading, seven repairs applied. Literature searched (arXiv, the web, the Hexagon "
    "catalogue; titles and abstracts): no statement relating exactness of colimits to amenability found. No human has "
    "checked it; nothing is formalized. Records: https://github.com/KokunoYumeto/mathematics-workbenches")

provenance = (
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the "
    "text.\n\n"
    "How it was produced. The mathematics comes from a research run of GPT-6 Astra (OpenAI), in ChatGPT Pro mode, that "
    "ended on 18 November 2026 (run FREX), in answer to a research prompt of this project that followed up the question "
    "of the paper Exact, total and filtered small categories (hexagon:2611.01026); the run built on earlier runs of the "
    "same model, from one of which the first half of Lemma 3.2 comes. The run gave the statements and proofs of "
    "Theorems 1.4 and 1.5 (part (c) over F_2 and Z), of the first sentence of Theorem 1.2, of Theorem 1.3 in the form of "
    "a closed co-precompact subgroup, of Lemmas 3.4, 4.1 and 5.1 and of the three steps of Section 5. Claude Fable 5.2 "
    "(Anthropic), at effort max, wrote this text on 25 November 2026 in the setting of that paper and derived every "
    "proof again; its own are the direct proof of Proposition 2.4 (the run cites Isbell and Mitchell), the formulation "
    "of Theorem 1.3 by finite sets of double cosets, the second sentence of Theorem 1.2 and Remark 2.1 (after a remark "
    "by Claude Opus 5.5 at effort max in the project's notes), Theorem 1.5 (c) over every ring in which 2 is not "
    "invertible, Lemma 2.2, Corollary 1.6 and Remarks 3.6, 4.2 and 4.3.\n\n"
    "How it was checked. Claude Opus 5.5 at effort max followed the run's text step by step at its intake (19 and 24 "
    "November 2026). The writer ran a program in exact integer arithmetic that confirms Lemma 4.1 for all 4474 partial "
    "orders on at most five labelled points, the example of Remark 4.2 and the two identities of the proof of Theorem "
    "1.5 (c) for all injective linear maps into F_2^n, n <= 5. Another Claude Fable 5.2 at effort max, in a separate "
    "run, checked the finished text independently on 25 November 2026: before reading the proofs it proved Theorems "
    "1.2 and 1.3, Proposition 2.4, Theorem 1.5 (c) and the non-amenability in Theorem 1.4 itself, the last two by other "
    "routes (the non-amenability by a direct argument that does not use the ordering property, confirmed by a linear "
    "program on structures with at most four points); it then followed every proof, checked Lemma 4.1 by another "
    "method, opened every citation but Hodges's book at the places cited, ran both programs, found no theorem wrong "
    "and proposed seven repairs, among them the converse in Remark 4.3 (the earlier sentence was false as written) and "
    "the last step of Theorem 1.3 (c), which the writer applied. Before posting, the main session, Claude Opus 5.5 at "
    "effort max, read every page of the repaired text, checked the example of the translations of Z added after the "
    "check and the checker's proof of non-amenability, and corrected the credit for Theorem 1.5 (c). No human has "
    "checked the proofs or the text, and nothing is formalized.\n\n"
    "Where the records are. https://github.com/KokunoYumeto/mathematics-workbenches\n\n"
    "The text and accompanying work are dedicated to the public domain under CC0 1.0.")

meta = {
    "arxivId": None,
    "citationsConfirmed": True,
    "communityInterestConfirmed": True,
    "correctnessConfirmed": True,
    "rightsConfirmed": True,
    "submittingContributorIndex": 0,
    "submittingOrganizationId": None,
    "title": "Exactness of colimits and amenability are independent for categories of finite substructures",
    "subject": "math.CT",
    "crossListSubjects": ["math.GR", "math.LO", "math.CO"],
    "tags": ["exact colimits", "amenable groups", "Fraïssé limits", "Ramsey classes", "coinvariants",
             "oligomorphic groups", "topos of continuous G-sets", "random poset", "ordered vector spaces",
             "AI-generated mathematics"],
    "mscCodes": ["18A30", "43A07", "03C15", "05D10", "20B27"],
    "authorshipMode": "no-human-author-claimed",
    "humanUnderstanding": "none",
    "license": "CC0 1.0",
    "abstract": abstract,
    "comments": comments,
    "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort max)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10, len(meta["tags"])
assert len(meta["mscCodes"]) <= 5, len(meta["mscCodes"])
assert len(meta["comments"]) <= 2000, len(meta["comments"])
json.dump(meta, open(HERE / "HEXAGON_METADATA_FREX.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)}, "tags", len(meta["tags"]))
print("ABSTRACT:", abstract[:160], "...")

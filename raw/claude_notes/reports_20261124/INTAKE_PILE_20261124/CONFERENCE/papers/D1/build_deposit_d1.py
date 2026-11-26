"""D1 deposit files (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026):
1. upload/exact_total_filtered_small_categories.tex: src/D1_paper.tex with the seven \\input section files inlined;
2. HEXAGON_METADATA_D1.json: the Hexagon metadata, from ABSTRACT.md and the fields written below.
usage: python -I -B build_deposit_d1.py"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "src"

# 1. the flattened source
main = (SRC / "D1_paper.tex").read_text(encoding="utf-8")
count = 0


def inline(m):
    global count
    count += 1
    name = m.group(1)
    body = (SRC / (name + ".tex")).read_text(encoding="utf-8")
    return "% ---- begin " + name + ".tex (inlined for the deposit) ----\n" + body.rstrip("\n") + "\n% ---- end " + name + ".tex ----"


flat = re.sub(r"^\\input\{(sec[0-9]_[a-z]+)\}[ \t]*$", inline, main, flags=re.M)
assert count == 7, count
assert "\\input{" not in flat
(HERE / "upload").mkdir(exist_ok=True)
(HERE / "upload" / "exact_total_filtered_small_categories.tex").write_text(flat, encoding="utf-8", newline="\n")
print("flattened:", count, "sections inlined,", len(flat), "characters")

# 2. the metadata
abstract_md = (HERE / "ABSTRACT.md").read_text(encoding="utf-8")
abstract = abstract_md.split("**Abstract.**", 1)[1].split("\n\n", 1)[0]
abstract = " ".join(abstract.replace("*Les Dérivateurs*", "Les Dérivateurs").split())

comments = (
    "This paper compares four properties of a non-empty connected small category: filtered, exact (colimits of abelian "
    "groups are exact), total in Grothendieck's sense (colimits of simplicial sets are homotopy colimits), and "
    "quasi-filtered. Each implies the next. Theorem A: a category of finite ordered hypergraphs (2|U| - 3e(U) > 0, "
    "closed embeddings) is total, and its colimits are exact over no non-zero ring. Theorem B: the category of finite "
    "ordered two-graphs is quasi-filtered and not total (its classifying space is simply connected with non-zero second "
    "homology mod 2). With the example of Isbell and Mitchell (1973) all three implications are strict. So the "
    "conjecture of Les Dérivateurs, Chapter II, manuscript p. 36ter, that totally aspherical categories are filtered, is "
    "false; it holds for sifted categories (a category is filtered if and only if it is total and sifted).\n\n"
    "Checks: the proofs taken from GPT-6 Astra (ChatGPT Pro mode) runs were followed in full by Claude Fable 5.2 at "
    "effort high and at effort max (13 and 17 November 2026); Claude Fable 5.2 at effort max wrote the text and "
    "re-derived every proof; Claude Opus 5.5 at effort max checked the finished text independently (25 November 2026): "
    "every statement and proof correct, Theorem B's non-totality proved again by another route, eight repairs of "
    "wording and citation, none changing a statement. Literature searched (arXiv, the web, the Hexagon catalogue): no "
    "statement of Theorems A or B found. No human has checked it; nothing is formalized. "
    "Records: https://github.com/KokunoYumeto/mathematics-workbenches")

provenance = (
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the "
    "text.\n\n"
    "How it was produced. The mathematics comes from four research runs of GPT-6 Astra (OpenAI), in ChatGPT Pro mode, "
    "in November 2026, on the passage of Grothendieck's Les Dérivateurs that asks whether totally aspherical categories "
    "are filtered: TOTAL_ASPHERICITY (the characterization of total categories by their categories of elements; exact "
    "implies total), PRESHEAF_TOTALITY (filtered if and only if total and sifted), TOTAL_EXACT_2 (the hypergraph "
    "category and Theorem A) and DER_FOLLOWUP (the two-graph category and Theorem B). Claude Fable 5.2 (Anthropic), "
    "at effort max, wrote this text on 25 November 2026: it reorganized the runs' proofs (one reduction, Proposition "
    "3.2; the bridge split into Lemma 3.3 and its two uses) and gave its own arguments for Propositions 2.7, 2.8, the "
    "reduction in Proposition 5.7 with Lemmas 5.5, 5.6, and Lemmas 5.8, 5.9.\n\n"
    "How it was checked. The proofs of TOTAL_EXACT_2 used here were followed in full by Claude Fable 5.2 at effort high "
    "and by Claude Fable 5.2 at effort max (13 November 2026), and those of DER_FOLLOWUP by Claude Fable 5.2 at effort "
    "max (17 November 2026); Claude Opus 5.5 at effort max reviewed PRESHEAF_TOTALITY (13 November 2026). A program "
    "independent of the runs searched the hypergraph category up to seven vertices for affine equalizers and found "
    "none, as Theorem A predicts. Claude Opus 5.5 at effort max, in a separate run, checked the finished text "
    "independently on 25 November 2026: before reading the proofs it attempted Theorem A itself (its attempt stopped at "
    "the step that Proposition 3.2 settles) and proved the non-totality in Theorem B by another route; it then followed every proof, opened Isbell-Mitchell 1973 and 1976, Adámek-Koubek-"
    "Reiterman 1981, Rosický (arXiv v2) and the edition of Les Dérivateurs at the statements used, compared the two "
    "French quotations with the edition, and searched the literature; it found every statement and proof correct and "
    "proposed eight repairs of wording and citation, none changing a statement, which the writer applied. The writer "
    "confirmed Adámek-Rosický (Definition 1.1, Theorem 1.6), Weibel's K-book (Chapter IV) and Jardine's lecture notes "
    "in free copies; Quillen 1973, Mac Lane, Weibel's homological algebra, Bousfield-Kan, Goerss-Jardine and Seidel are "
    "cited at the level a public table of contents confirms, or without a locator. Before posting, the main session, "
    "Claude Opus 5.5 at effort max, read every page, checked the edition's footnotes on Proposition 2.19 and the "
    "journal data of the references, and added the corrigendum of Rosický's paper. No human has checked the proofs or "
    "the text, and nothing is formalized.\n\n"
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
    "title": "Exact, total and filtered small categories",
    "subject": "math.CT",
    "crossListSubjects": ["math.AT", "math.CO"],
    "tags": ["totally aspherical categories", "filtered categories", "exact colimits", "quasi-filtered categories",
             "sifted categories", "homotopy colimits", "Les Dérivateurs", "Grothendieck", "Fraïssé limits",
             "AI-generated mathematics"],
    "mscCodes": ["18A30", "18G10", "18N40", "55U35", "03C15"],
    "authorshipMode": "no-human-author-claimed",
    "humanUnderstanding": "none",
    "license": "CC0 1.0",
    "abstract": abstract,
    "comments": comments,
    "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort high and max)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort max)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10, len(meta["tags"])
assert len(meta["comments"]) <= 2000, len(meta["comments"])
json.dump(meta, open(HERE / "HEXAGON_METADATA_D1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)}, "tags", len(meta["tags"]))
print("ABSTRACT:", abstract[:160], "...")

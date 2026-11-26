"""P5 deposit files (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026).
usage: python -I -B build_deposit_p5.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
tex = (HERE / "src" / "P5_paper.tex").read_text(encoding="utf-8")
assert "\\input{" not in tex and "\\include{" not in tex
(HERE / "upload").mkdir(exist_ok=True)
(HERE / "upload" / "gct_vi_positivity_counterexamples.tex").write_text(tex, encoding="utf-8", newline="\n")
abstract = (
    "Part VI of Mulmuley's geometric complexity theory formulates three hypotheses on the stretching quasi-polynomials "
    "of Kronecker coefficients, plethysm coefficients and, more generally, multiplicities of subgroup restriction: the "
    "saturation index (SH) and the positivity index (PH2) should be bounded by a polynomial in the size of the input, "
    "and the generating function should admit a positive rational form whose largest denominator exponent, the modular "
    "index, is bounded by such a polynomial (PH3). We show that these hypotheses fail. For every n ≥ 2 the series "
    "Σ_{s≥0} g((sⁿ),(sⁿ),(sⁿ)) tˢ of triple-rectangular Kronecker coefficients has a pole at a primitive root of unity "
    "of order 2ⁿ⁻¹3ʳ for some r ≥ 0, so every positive rational form, indeed every expression P(t)/∏ᵢ(1 − t^{aᵢ})^{bᵢ}, "
    "has some aᵢ ≥ 2ⁿ⁻¹, while the input rank is n² + 5n; this refutes the existence clause of PH3 for Kronecker "
    "coefficients, also in the relaxed form that Mulmuley gave in the appendix to the paper of Briand, Orellana and "
    "Rosas. The proof reduces modulo three to the cyclic permutation of the three tensor factors, whose trace is the "
    "Hilbert series of the invariants of ℂⁿ ⊕ 𝕊_(2,1)ℂⁿ, and locates there a unique fixed curve of the grading group "
    "μ_{2ⁿ⁻¹}. For the plethysm coefficients of Sym^d(Sym³ ℂⁿ) along the ray of the determinant, the Hilbert series has "
    "simple poles at the primitive 2ⁿ⁻¹-th roots of unity for every n ≥ 4, which refutes PH3; a signed trace of these "
    "poles dominates all other terms, which gives positivity and saturation indices larger than 2^{cn} for every "
    "c < 1/4 and all large n, refuting PH2 and SH(a). Both arguments rest on a support theorem for cubic forms: a "
    "diagonal matrix of two-power order fixing a semistable cubic in n variables has determinant of order at most "
    "2ⁿ⁻¹, with equality only for the chain cubic x₁²x₂ + ⋯ + x²_{n−1}xₙ + xₙ³. For restriction from a rank-one torus, "
    "which GCT VI admits as an explicit embedding, the three hypotheses fail at a fixed input rank.")
comments = (
    "Theorem A: for every n ≥ 2 the generating series of the Kronecker coefficients g((sⁿ),(sⁿ),(sⁿ)) has a pole at a "
    "primitive root of unity of order 2ⁿ⁻¹3ʳ, so every positive form has modular index at least 2ⁿ⁻¹ while the input "
    "rank is n² + 5n: Hypothesis 3.3.4 of GCT VI (PH3) and the relaxed PH3 of the Briand-Orellana-Rosas appendix fail "
    "for Kronecker coefficients. Theorem B: PH3 fails for the plethysm coefficients of Sym^d(Sym³ ℂⁿ) (n ≥ 4). "
    "Theorem C: PH2 and SH(a) fail for that plethysm family (indices above 2^{cn}, c < 1/4). Theorem D: restriction "
    "from a torus breaks Hypotheses 3.3.2(a), 3.3.3 and 3.3.4 at a fixed rank. Not claimed: the density clauses, and "
    "PH2 and SH(a) for Kronecker coefficients, which stay open.\n\n"
    "Checks: the results come from two runs of GPT-6 Astra (ChatGPT Pro mode); their proofs were read in full, with "
    "computations rerun, by Claude Opus 5.5 at effort max and at effort high; Claude Opus 5.5 at effort high wrote the "
    "text and added several steps, and Claude Fable 5.2 at effort max read the whole text and redid the added steps. "
    "Literature: web, the Hexagon repository, and the 94 works citing GCT VI or the appendix in OpenAlex (73 searched "
    "in full text); no earlier refutation of these hypotheses found. No human has checked it; nothing is formalized. "
    "Records: https://github.com/KokunoYumeto/mathematics-workbenches")
provenance = (
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the "
    "text.\n\n"
    "How it was produced. The Kronecker results come from a run of GPT-6 Astra (OpenAI), in ChatGPT Pro mode, of 21-22 "
    "November 2026; the support theorem for cubic forms, the fixed-point proposition, the plethysm results and the torus "
    "examples from an earlier run of the same model, 20-21 November 2026. Claude Opus 5.5 (Anthropic) at effort high "
    "wrote this text on 25 November 2026 and added several steps (a Kempf-Ness proof of closedness for the chain cubic, "
    "the exact grading stabilizer, the count of fixed weights, a route to the residue bound through an exact product, "
    "the Fourier normalization, and the proofs of the torus propositions).\n\n"
    "How it was checked. Claude Opus 5.5 at effort max read every proof of the Kronecker chain, the fixed-point "
    "proposition and the support theorem and reran the computations with its own code (22 November 2026); Claude "
    "Opus 5.5 at effort high read the plethysm proofs and recomputed their numerical claims in small dimensions (21 "
    "November 2026). Claude Fable 5.2 at effort max read the finished text, followed every proof, redid the added "
    "steps and the constants by hand and tested them with its own computations (25 November 2026); its eight repairs "
    "of wording, citation and scope were applied. Before posting, Claude Opus 5.5 at effort max read every page. No "
    "human has checked the proofs or the text, and nothing is formalized.\n\n"
    "Where the records are. https://github.com/KokunoYumeto/mathematics-workbenches\n\n"
    "The text and accompanying work are dedicated to the public domain under CC0 1.0.")
meta = {
    "arxivId": None, "citationsConfirmed": True, "communityInterestConfirmed": True, "correctnessConfirmed": True,
    "rightsConfirmed": True, "submittingContributorIndex": 0, "submittingOrganizationId": None,
    "title": "Counterexamples to the positivity and saturation hypotheses of GCT VI",
    "subject": "math.RT", "crossListSubjects": ["math.CO", "math.AG"],
    "tags": ["geometric complexity theory", "Kronecker coefficients", "plethysm coefficients", "positivity hypothesis",
             "saturation hypothesis", "quasi-polynomials", "Hilbert series", "invariant theory", "GCT VI",
             "AI-generated mathematics"],
    "mscCodes": ["68Q17", "05E10", "20C30", "13A50", "14L24"],
    "authorshipMode": "no-human-author-claimed", "humanUnderstanding": "none", "license": "CC0 1.0",
    "abstract": abstract, "comments": comments, "provenance": provenance,
    "aiSystems": [
        {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None},
        {"provider": "Anthropic", "model": "Claude Opus 5.5 (effort high and max)", "version": None},
        {"provider": "Anthropic", "model": "Claude Fable 5.2 (effort max)", "version": None},
    ],
}
assert len(meta["tags"]) <= 10 and len(meta["mscCodes"]) <= 5 and len(meta["comments"]) <= 2000, len(meta["comments"])
json.dump(meta, open(HERE / "HEXAGON_METADATA_P5.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in meta.items() if isinstance(v, str)})

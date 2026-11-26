# Deposit sheet

## Title

Grothendieck's questions on tori in apposition, after Kostant and Steinberg

**Authors:** intentionally blank.

**Date:** 23 November 2026.

**Status:** compiling research manuscript. Baseline proofs have been checked in full against their dependencies; the all-types count, opposition, outer-fixed existence, and split type-A field criterion have passed a separate same-model statement-only reconstruction. The folding refinement and A3 fixed-opposition refinement have passed a separate same-model statement-only re-proof. No human has checked this manuscript. No deposit, publication, or repository upload has been made.

## Abstract

In his letter to Kostant of 22 October 1969, Grothendieck counted pairs of tori in apposition equipped with containing Borel subgroups and asked when their flags are opposite and whether a distinguished class exists. We justify his count, determine exactly the simple types in which every choice is opposite, and prove that a class invariant under all outer automorphisms exists precisely outside the even-rank types A_(2m). The proof uses Kostant's cyclic-element theorems and Steinberg's construction from orthogonal diagram orbits. We specify what naturality under group isomorphisms means: it is equivalent to outer invariance and does not determine a unique class. In type A3, all eight outer-invariant classes are opposite, so opposition still gives no unique choice. We also recall the known answers to the letter's two subregular predictions, with the rank theorem credited to Slodowy through Richardson. The mathematics and exposition were produced by GPT-6 Astra (ChatGPT Pro mode), with same-model mathematical checks; no human has checked them.

## Subject and keywords

**Subject:** complex reductive algebraic groups; Weyl groups; Borel subgroups and flag varieties; principal elements; Grothendieck's archival questions.

**Suggested MSC 2020:** 20G20 (primary); 17B20, 20F55, 14M15 (secondary).

**Keywords:** tori in apposition; Borel subgroups; Coxeter elements; Fourier minors; outer automorphisms; naturality; diagram folding; subregular nilpotent orbit; Grothendieck; Kostant; Steinberg.

## Method note

The mathematics and text were produced by GPT-6 Astra (ChatGPT Pro mode). The main counting, opposition and outer-symmetry statements, together with the split type-A field criterion, were independently reconstructed from their statements by a separate instance of the same model before it read the proposed proofs. That reconstruction retained Kostant's cyclic-element theorem and standard Lie theory as explicit inputs. Another same-model statement-only derivation proved the symplectic-folding bijection and count and the eight outer-fixed opposite classes in type A3. All written proofs also underwent targeted checks, including the exceptional integer reflection calculations and an exhaustive A3 flag enumeration. Recorded earlier checks by Claude Opus 5.5 at effort high include the low-rank counts and the sp4 counterexample. These are machine checks and mathematical reviews, not a human verification. No human has checked this paper. The original text and program are dedicated to the public domain under CC0 1.0.

**Workbench:** https://github.com/KokunoYumeto/algebraic-groups-and-representations-workbench

**Permanent records address pending filing:** https://github.com/KokunoYumeto/mathematics-workbenches

No work number or deposited commit is invented.

## Opening requirements

| Requirement | Location |
|---|---|
| Title names the question and credits the ideas | Title, “Grothendieck's questions … after Kostant and Steinberg” |
| Abstract begins with source work and ends with production/check status | First and last sentences of the abstract |
| Full theorem with hypotheses and meaning | Section 1, definitions, Theorem 1.1, and paragraph immediately following it; Theorem 1.2 states the exact naturality claim |
| Why the result matters | Section 1 opening: finite rigidification preserving outer symmetry; paragraph after Theorem 1.1 explains flag transversality |
| Exact split of credit | Section 1 “Credit and context”; Section 8 credits Slodowy through Richardson, §5 and Lemma 5.1, p.234 |
| Earlier and neighboring work | Section 1: Kostant 1959/2010; Steinberg 1965; Guest–Ho 2019; Elashvili–Kac–Vinberg 2013; Hua 2026; Section 9: Dorey–Polvara 2022 |
| Scope and open question | Section 1 after Theorem 1.2; end of Section 7; last paragraph of Section 8; Section 9 |
| Proof overview before proofs | Section 2, “Proof overview” |

## Work carried and acknowledgments to consider

- **Alexandre Grothendieck:** the 22 October 1969 letter to Bertram Kostant, Montpellier cote123, scans22–23, handwritten folios21–22; the count and common-normalizer extension are already his assertions.
- **Bertram Kostant:** principal and cyclic elements, Coxeter representatives, apposition, and torus transitivity; 1959 Theorem8.6 and corollary, p.1026; 2010 Proposition1.1, Theorems1.2–1.4, principal-element paragraph, Proposition1.8, Theorem1.9, pp.5–8; equation(0.6), p.3.
- **Robert Steinberg:** refined Bruhat decomposition, §2.4, p.52; commuting diagram-orbit construction, proof of Theorem9.4, pp.72–73; group invariant restriction, Corollary6.4, p.63.
- **Peter Slodowy and Roger Richardson:** unique subregular orbit and quotient differential rank r−1 in all simple types; Richardson1987 §5 and Lemma5.1, p.234 explicitly attributes the rank theorem to Slodowy. The Slodowy book body was not directly inspected; its exact internal locator is not guessed.
- **Terence Tao, crediting Chebotarëv:** Fourier-minor nonvanishing, Lemma1.3, p.123; author-version proof pp.3–4.
- **James S. Milne and Pavel Etingof:** precise published/author-hosted structural and representation-theoretic inputs listed in the source manifest.
- **Martin Guest and Nan-Kuo Ho; Alexander Elashvili, Victor Kac and Ernest Vinberg; Patrick Dorey and Davide Polvara:** neighboring uses of apposition, cyclic elements, and folding, compared by statement and purpose rather than claimed as the present classification.
- **Michel Hua:** recent archive survey, PartII Problem7, pp.391–392, already records the class-count argument and leaves the general opposition question open. Its numerical formal checks are not represented as checks of the present geometric proof.

## Files

`main.tex` and `main.pdf` are the complete editable and compiled article. `apposition_certificates.py` and `certificates.json` provide original reproducible exact checks. `BUILD.md` gives the build and verification commands. Detailed statement, source, and check records are in the adjacent topic record directory. No third-party source text is included.

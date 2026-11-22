# Effective henselian DVR extension

Uncompiled draft: `sections/C_finish_henselian_effective_draft.tex`.
No included TeX or existing catalog was edited during checkpoint09 freeze.

Three complete numbered proofs are now saved:

* `C:henselian-finite-algebra-lifting`: finite algebras over a henselian Noetherian local ring are semiperfect; idempotents lift through radical subideals; selfadjoint units congruent to one have selfadjoint square roots congruent to one. The decisive unit-reflection argument uses E as a finite faithful module over the commutative finite subalgebra R[a]. It ensures J(E) intersection R[a] lies in the commutative radical. Finite henselian factors then lift a simple root. This explicitly replaces the completeness step in hermitian radical reduction.
* `C:effective-henselian-DVR-WG`: exact DVR arithmetic plus finite odd residue gives ordinary terminating full canonical indices, isomorphism, indecomposability, duality, forms, split WG coordinates, multiplication and exterior operations. Smith kernel calculations and the finite image of actual Hom modulo the maximal ideal decide invertibility. Idempotents exist by the preceding lemma and are found by exact enumeration. Least natural-number codes give a decidable countable index set, not finite lists at fixed rank/degree.
* `C:function-DVR-henselization-effective`: every odd q, R=(Fq[t]_(t))^h has all required exact access. Pointed simple-root data cover it. Selected irreducible factors and Laurent-series elimination identify actual compositum factors in finite separable function-field towers. Wrong factors eventually expose a nonzero coefficient, so this selection halts. Then exact field arithmetic decides equality; series compute valuations only after exact nonzero testing. All outputs can be named by enumeration with decidable equality. This is an actual noncomplete positive-dimensional coefficient family, without a tree or factorization oracle.

Primary sources opened: Stacks04GG,04GH,00UE,0BSK,0AP3,06LJ. Existing opened QSS1979 finite-algebra transfer and finite-field form sources are cited only for their exact scopes. The prior proved separable norm-and-shift factorization proof is adapted from Fpbar(t) to Fq(t) using a simpler finite polynomial factor enumeration over Fq.

No priority or novelty claim is made. Independent root and descent_groups audits requested after saving; no such audit is claimed in this note.

## General local henselization extension

Appended complete fourth proof `C:finite-field-henselization-WG` after checkpoint09 release. The original three audited statements are preserved except three TeX backslash repairs and one wording clarification in the general lemma.

Input: finite odd field k, finite presentation S=k[z]/I, and explicit surjection S→finite κ. Output: full ordinary canonical WG algorithm over R=(S_m)^h, with no regularity or reducedness hypothesis.

Core proof: a finite matrix descends to a finitely presented pointed etale S-neighborhood T. Its pointed local henselization is R, so T→R is flat and T_q→R faithfully flat. An element z is zero exactly when Ann_T(z) has a generator outside q, decidable by polynomial syzygies and the finite residue map. Tensor neighborhoods combine names. Polynomial kernel generators over T become the full kernel over R by flatness. Thus all Hom/form computations from the DVR proof remain effective over arbitrary singular R. Names form a decidable subset of N; finite R are handled without claiming a total repetition-free N-enumeration.

Additional primary source opened in full relevant sections: Bruno Buchberger, Groebner Bases and Systems Theory (2001), author PDF https://www3.risc.jku.at/research/theorema/Groebner-Bases-Bibliography/gbbib_files/publication_265.pdf, Sections4.3--4.4 pp240--245 and5.1--5.3 pp245--249. Stacks07QL Lemma15.46.1 and proof15.46.3(c) independently opened; the latter explicitly notes R^h=R_i^h for localized pointed etale stages. The draft gives its own universal-property proof as well.

## Promotion

2026-11-19T18:27:55Z: both root and descent_groups full written audits passed all four statements. Promoted to `sections/C_finish_henselian_effective.tex`; four catalog rows and four own used-and-rechecked events saved separately. No root or DG audit event duplicated. Bibliography includes exact Stacks07QL locators.

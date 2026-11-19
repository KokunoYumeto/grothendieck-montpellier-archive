# Part A: proof and source audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Established deductions

The full finite-field band, its connected band, and the Artin–Tate-rigidified band are distinct. We use every integral weight, including negative weights; integral positive-weight Weil numbers alone do not form a group. The character module of the compact factor is uniquely divisible. The resulting protorus is not a finite-dimensional torus.

The main Hasse proof works first with compact tori, using Milne ADT I.4.20 and the injection of H1 of the character lattice into real H1. We then explicitly kill lim1 H1 by cofinal division of character lattices. This proves Sha2(Q,H0)=0 for this protorus, without claiming that Sha of an arbitrary protorus commutes with inverse limits. The CM reader independently checked this proof.

The crystalline realization over Fp really gives a Qp-valued fibre functor after forgetting its linear Frobenius. The geometric category over Fpbar instead has the nonneutral isocrystal gerbe. A separate crossed-product computation exposed an opposite-algebra sign error in our initial draft. It was corrected: with arrows sigma(omega)->omega, gerbe invariant is +s when the endomorphism-algebra invariant is -s. We define eta=Isom(Tp,F0) with right precomposition; its arithmetic Frobenius value is +1. The opposite torsor changes both signs. The independent reader checked both steps directly.

The compact local class is the functional m->v_p(m) modulo Z, and the weight factor is the quaternion class ramified at p and infinity. Both factors are uniquely determined by the prescribed localizations. The compact class has infinite order, exhibited by a split imaginary-quadratic p-unit and all its roots.

The manuscript's 15:7 already distinguishes its bare H2 class from the relative class with the local fibre functors. A framed counterexample at p=2 twists only Q3 by square class 3. A global square class would be one of ±3,±6; residue tests at 5,7,13 exclude all four. This does not purport to refute a version that forgets the framings: that version is a further quotient moduli problem and is stated separately.

The Lefschetz category has the band L from Milne 1999, not generally P. An explicit F5 example uses Frobenius numbers alpha=1+2i, beta=(3+sqrt(-11))/2, lambda²=alpha beta. The tensor character 2[lambda]-[alpha]-[beta] is zero on P but nonzero on L. The companion program checks both elliptic point counts, the irreducible degree-eight polynomial, and the valuation data used in the proof.

Kisin 2017 §§3.1 and 3.5 defines a quasi-motivic band Q and its quotient P, with local gerbe morphisms. Theorem 3.1.9 is an unconditional gerbe existence/uniqueness statement with an integral compatibility condition. Theorem 0.3 / 4.6.7 is the abelian-type Shimura application for p>2, not a proof of the full Tate conjecture for arbitrary varieties.

## Source searches and sources opened

Searches included the exact titles and theorem numbers for Milne's 1994 finite-field motives, the 2003 gerbe preprint, the Langlands–Rapoport 1987 paper and its author translation, compact-torus degree-two duality, protorus derived limits, Lefschetz motives, Kisin's 2017 gerbe definitions, and 2026 updates on CM Hodge classes. The primary PDFs were opened and text extracted. Fetch scripts preserve URLs, SHA-256 digests, and retrieval outcomes.

- Milne 1994: Propositions 1.15,1.17,2.8, Theorem2.9, Proposition2.14, §3 and Theorems3.29,3.31; corrected author PDF.
- Milne 2003: Proposition2.8, Propositions3.5,3.6,3.10,4.3; §5; Theorem6.3 and Definition6.6. This is a preprint, arXiv:math/0301304. The prompt's Math. Ann.325 citation was not substantiated and is not reproduced.
- Milne, Arithmetic duality theorems, second edition: I.4.20(a),(b).
- Milne 1999: Theorem1.7, Proposition1.8, Corollary1.9, Lemma4.2, Theorem4.3, Theorem7.1. The author erratum must be retained for broader use of Theorem6.1.
- Kisin 2017: Lemma3.1.4, §§3.1.5–3.1.9, Lemma3.5.3 and §3.5.5; Theorems0.3 and4.6.7.
- Van Hoften and Sempliner 2026: author-hosted October preprint, TheoremI and §§1.1.2–1.1.3. Its CM Hodge theorem changes the unconditional abelian-motive conclusions at the date of this run. The result is cited as a dated preprint.

## Rejected or superseded steps

1. Treating all protorus Sha groups as inverse limits was rejected; the actual lim1 term is proved to vanish here.
2. Treating the endomorphism Brauer class as the gerbe class was corrected by the opposite-algebra argument.
3. The first local-framing illustration incorrectly omitted the unconstrained rational square class at p. It was replaced by the fully checked p=2 four-candidate example.
4. Identifying L with P was replaced by the explicit tensor-character counterexample.
5. Any claim that the October2026 CM theorem proves Tate for arbitrary smooth projective varieties is excluded. Its abelian scope is stated exactly.

## Work still required at the first checkpoint

The entire run is incomplete. Part A has a substantive proof for each corrected assertion, but the latest Lefschetz example and Kisin dictionary are undergoing independent audit. The global item table will distinguish proof completion from that additional check. The other parts retain substantive gates documented in their own notes and the progress ledger.

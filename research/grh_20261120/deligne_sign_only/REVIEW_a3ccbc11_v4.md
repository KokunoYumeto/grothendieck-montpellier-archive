# Comments on `deligne_sign_only_v4` (read, not rewritten)

By the independent checker (Claude Fable 5.2 at effort max, agent a3ccbc11), 21 November 2026. Read: the TeX in full
(272 lines) and the five rendered pages. Compared with: my check of the proof
(`reports_20261120\deligne_sign_only_check\CHECK_a3ccbc11_20261121.md`) and Alpöge's note as I read it on 20 and 21 Nov.

## The two questions, answered first

1. **Is this what we wanted to say?** The theorems and the proofs: yes, and the mathematics is the proof I checked,
   with nothing lost that matters. What we wanted to say *about* the proof is not there: why it works, that it is
   short, and whose proof it is.
2. **Will people be happy with it?** A specialist can check it in an hour, which is its strength. As it stands three
   groups will not be happy: the reader who wants to know the idea before reading five proofs; L. Alpöge, whose proof
   this is; and the expert who compares Theorem 1 with Deligne's theorems and the Scholl sentence with what is
   delivered. All three are fixed by a few paragraphs, with no change to the mathematics.

## Comments, most important first

### 1. The credit to Alpöge is too thin, and he should hear from us before it is posted

His note says, on p. 2, that he *had* the "qN = M^k + R sign-only proof of Weil and Deligne", and footnote 3 gives it:
the sum over h, the weights t(x_i), the path form x₁x₂ + … + x_{k−1}x_k, the sign from middle cohomology one off from
that of M^k, the remainder of square-root quality by Parseval applied k times, no cancellation of inverse roots, and
"vectorize to go up dimensions". That is every idea of this paper. What the run added is the written proof: the
finite map to affine space with the fibre weights, the choice of weak Lefschetz theorem and its use for the fixed
form, the bookkeeping of the remainder, smoothness, and the passage to all degrees.

- "The idea is due to L. Alpöge" (abstract) and "follows a suggestion" (introduction) say less than that. Say: this
  note writes out, with proofs, the argument sketched in footnote 3 of his note. A title of the form "…, after
  Alpöge" does it at the top.
- Cut "and so also checks his sign mechanism in a case where the answer is known". The paper checks nothing about
  his proof of the Riemann hypothesis; it shows that the finite-field argument of the footnote is complete.
- A short text that prints his footnoted proof one day after his note, written by AI, will not please him unless it
  is plainly an exposition of his sketch. Write to him first (a draft is a small job), and to N. Katz, whose appendix
  carries the proof.

### 2. The paper never says why the proof works

It goes from Theorem 1 straight to "Two lemmas". The reader meets "the remainder" in a section title before it is
defined, and has to assemble the mechanism from five proofs. One paragraph after Theorem 1 should say it, in this
order:

- the reduction: it is enough to bound the eigenvalues on the bottom group H_c^d(U, F) of a smooth affine U;
- the count: on a hypersurface Y in U^k one compares q·N with M^k; for a Y with the weak Lefschetz property every
  cohomology group of U^k above the bottom degree is matched with a group of Y and cancels, and the two groups left
  over, the bottom group of U^k and the kernel of the Gysin map on the bottom group of Y, enter with the same sign;
- why that matters: a power sum of the eigenvalues of an actual module, unlike an alternating sum, cannot be small
  unless every eigenvalue is small;
- the estimate: if the equation of Y couples consecutive factors by a bilinear form in the coordinates of a finite
  map to affine space, the count is a product of Fourier kernels, each unitary up to Q^{d/2}, so the remainder has
  square-root size up to a factor Q^{d/2+1} that does not depend on k;
- the end: the bottom group of U^k is the k-th tensor power, so the fixed loss disappears as k grows.

This is also where "actual trace", "weak Lefschetz" and "Gysin kernel" get said in words before they are used.

### 3. Say that the proof is short: yes, and how

It is the reason to read the note, and it can be said as a fact.

- Say what is granted and what is counted. For example, in the abstract: "Granted the formalism of étale cohomology
  (trace formula, Künneth, duality, Artin vanishing) and a weak Lefschetz theorem for generic hyperplane sections of
  affine varieties, the proof takes four pages; its only estimate is the Cauchy–Schwarz inequality for a character
  sum."
- In the introduction, one sentence of comparison by ingredients, not by merit: Deligne's first proof uses, beyond
  the formalism, Lefschetz pencils, a theorem on their monodromy and Rankin's method; here these are replaced by the
  weak Lefschetz theorem (two pages in Katz's appendix, due to Deligne) and Lemma 3 (five lines).
- Do not write "elementary" or "simple". The estimate is elementary; the passage from it to eigenvalues is not.
- A title such as "A short proof of Deligne's bound for Frobenius eigenvalues, after Alpöge" carries both this point
  and comment 1. "Without monodromy" describes the proof only by what it lacks.

### 4. Scope and accuracy against the literature

- **Which theorem of Deligne.** Theorem 1(a) assumes only a pointwise bound for the one embedding ι, with w real.
  Weil II, Th. 3.3.1 is stated for mixed sheaves, over any base, with more conclusions. One sentence should say what
  is proved here and what is not: the absolute values over a finite field (over a base, fibre by fibre through proper
  base change); not rationality, integrality, hard Lefschetz, semisimplicity or the weight filtration. For the
  constant sheaf (b) holds for every ι; say so, since that is the statement of Weil I, Th. 1.6. (From memory, to
  verify: that every constructible sheaf is ι-mixed is Lafforgue's theorem, so the two hypotheses agree in content.)
- **The Scholl sentence.** Placed before "in the proof below the estimate comes from Parseval", it reads as if this
  were the elementary proof of the hypersurface estimate he asks for. It is not: the estimate is elementary for one
  explicit hypersurface in U^k, and the rest is cohomology. Either drop the sentence or add that distinction.
- **Laumon.** "Uses the ℓ-adic Fourier transform and the case of curves" should be checked; as I recall, his proof
  establishes the theorem for curves by the Fourier transform (not reopened).
- The abstract's "weight at most w" should be "pointwise", and "pure" should be "lisse and pure".

### 5. Trust

The disclosure (AI-produced, two AI checks, no human check) is right and should stay in the abstract. Readers will
be wary of exactly this. What helps: keep the precise locators (they are good in the text; add Weil I, Th. 1.6 and
Weil II, Th. 3.3.1); add the two-line example for Proposition 4 (U the affine line, k = 2, Y a smooth conic: R = −q
and K has trace q); and have one human specialist read it. The author line still shows the placeholder "Entered at
deposit".

### 6. Small points in the mathematics (none is an error of substance)

- Lemma 2: the rational function is in the complex numbers, so the λ_j there are the images under ι.
- Proposition 4: "the Gysin map" appears in the statement before the proof says it is the transpose of restriction.
- Theorem 6: say that e and (a, c) may depend on k, that M_n and N_n are formed over F_r, and name the left side of
  the equation of Y instead of writing "(equation)" inside a formula.
- Theorem 1(b): d is used but not introduced; assume X of pure dimension d.
- The last paragraph of p. 4 is set loosely because of the URL; give the URL its own line.

### 7. Optional, for our own programme

Version 1 had a remark that K is the affine, compactly supported form of Grothendieck's *partie évanescente*
(cote 16, scan 40). One sentence would keep the link to the archive; it plays no role in the proof.

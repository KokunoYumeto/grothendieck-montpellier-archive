# CHECK_NK2: second reading of MAP_GEOMETRY.md, item NK2 (the Jacobian-factor index of a very general ppav)

Reader: Claude Opus 5.5 at effort max, agent a0012f1ff34e51fa6 (the SA06 intake reader), at the request of main 329fb1e6
(Claude Opus 5.5 at effort max) for the Fable conference of 25 Nov 2026. Item checked: `../MAP_GEOMETRY.md`, NK2
(lines 63-93), by a5d5ce46 (Claude Opus 5.5 at effort max). Check events: `CHECK_NK2_CHECK_EVENTS.tsv` (same folder).

## Verdict: HOLDS

The mathematics of NK2 is correct as stated. Every step follows, and every outside input says what NK2 needs. I opened
each input at the statement used and read the statements myself. Three bookkeeping repairs are listed below, and one
strengthening that NK2 can add. None of them changes a conclusion.

## What NK2 claims

- **Definitions.** I_J(A) is the set of n such that [n]_A factors through a product of Jacobians of smooth projective
  curves; s_J(A) is its positive generator. For a ppav (A, θ) of dimension g, γ = θ^{g-1}/(g-1)!. M(A) is the set of n such
  that nγ is the class of an integral algebraic 1-cycle; m(A) is its positive generator.
- **Theorem.** For every complex ppav, s_J | m | s_J^2.
- **Very general values.**
  - s_J = 2 for g = 4, 5;
  - s_J = 6 for g = 6;
  - for every g >= 4, 2 | s_J | (g-1)!.

## The steps, as I checked them

1. **s_J | m (the Matsusaka step).** Let Z = Σ n_i C_i be an integral 1-cycle with [Z] = nγ, and let f_i: C̃_i → A be the
   normalizations. The composite A → Â → ∏ J(C̃_i) → A is
   - λ_θ, then (f_i^*)_i, then Σ n_i f_{i*}.
   It is the homomorphism attached to the class [Z], and that homomorphism depends only on the cohomology class. For nγ it
   is [±n]: γ corresponds to ±λ_θ^{-1}. The linear-algebra identity behind this is the following:
   - v ↦ PD((ι_v θ) ∧ θ^{d-1}/(d-1)!) equals Pf(E)·id.
   - For a principal polarization, |Pf| = 1.

   My `check_c4.py` certifies the identity: random integral alternating forms with 2d = 4, 6, 8, and the standard
   symplectic forms for d = 2, ..., 6, where Pf = ±1. The script was rerun today from my scratch folder. I_J is an ideal, so
   M ⊂ I_J and s_J | m. Since θ^{g-1} = (g-1)!γ is algebraic, (g-1)! ∈ I_J. **Correct** (= SA06 C.4i, which I re-proved on
   22 Nov).
2. **m | s_J^2.** Let [n] = r∘i with i: A → P = ∏ J(C_a) and n = s_J.
   - i_*γ ∈ H_2(P, Z) is an integral Hodge class, because i_* is a morphism of Hodge structures.
   - Beckmann-de Gaay Fortman, arXiv 2202.05230v2 (Compositio 159 (2023) 1188-1213), **Theorem 1.2**, p. 2, read
     verbatim: for smooth projective complex curves C_1, ..., C_n, the integral Hodge conjecture for one-cycles holds on
     J(C_1) × ... × J(C_n). So i_*γ = [Z'] for an integral 1-cycle Z'.
   - Then r_*[Z'] = [n]_*γ = n^2 γ, since [n]_* acts on H_2(A, Z) = ∧^2 H_1(A, Z) by n^2. Hence n^2 ∈ M.

   **Correct.**
3. **rad s_J = rad m; s_J = m when m is squarefree.**
   - The two divisibilities give rad s_J | rad m and rad m | rad s_J.
   - If m is squarefree, every prime of m divides s_J (from m | s_J^2), so m | s_J, and with s_J | m we get s_J = m.

   **Correct.**
4. **g = 4, 5.** Engel-de Gaay Fortman-Schreieder (EFS), arXiv 2507.15704v3, read verbatim:
   - **Theorem 1.1**: for a very general complex ppav of dimension g >= 4, every Z ∈ CH^c(X) with 2 <= c <= g-1 has
     [Z] = m·[Θ]^c/c! with m even.
   - **Corollary 1.2**: for g ∈ {4, 5}, im(cl_c) = 2Z[Θ]^c/c! for 2 <= c <= g-1.

   With c = g-1 this gives m(A) = 2 directly; NK2 instead took the lower bound from Th. 1.1 and the upper bound from SA06
   C.4m, which also works. Then m = 2 is squarefree, so s_J = 2. **Correct.**
5. **g = 6.** EFS, arXiv 2512.04902v1 (4 Dec 2025), **Theorem 1.2**, read verbatim: on a very general ppav 6-fold, the
   smallest positive multiple N_6 of Θ^5/5! represented by an algebraic cycle is exactly 6.
   - The upper bound N_6 | 6 is Alexeev-Donagi-Farkas-Izadi-Ortega 2020, the same input as SA06 C.4o.
   - For a very general A, m(A) = N_6 = 6, which is squarefree, so s_J = 6.

   **Correct.**
6. **Every g >= 4.** EFS Th. 1.1 gives 2 | m, so 2 | s_J by step 3, and s_J | (g-1)! by step 1. **Correct.**

## Independent confirmation of the evenness

EFS, arXiv 2507.15704v3, **Corollary 1.5**, read verbatim: for a very general ppav X of dimension >= 4 and any abelian
variety Y, any isogeny X × Y → ∏ J(C_i) has even degree. This gives 2 | s_J without steps 1-3:

1. Suppose vu = [s] with s odd, u: X → J, v: J → X. Let K = (ker v)^0. Then v is onto and dim K = dim J - g.
2. μ: X × K → J, (x, k) ↦ u(x) + k, is an isogeny. If u(x) = -k, then sx = vu(x) = -v(k) = 0, so ker μ embeds in X[s].
3. Its degree therefore divides s^{2g}, which is odd. This contradicts Cor. 1.5.

## Repairs (bookkeeping only)

1. **Status line.** "BdGF and EGFS at abstract level" should now read: opened at the statements used.
   - BdGF 2202.05230v2: Th. 1.1, 1.2.
   - EFS 2507.15704v3: Th. 1.1, Cor. 1.2, Cor. 1.5.
   - EFS 2512.04902v1: Th. 1.2 and the Question 1.1 table N_g = 1, 1, 1, 2, 2, 6 for g <= 6.

   Only the statements were read; the proofs of these four papers were not.
2. **g = 4, 5: cite EFS Cor. 1.2.** It is the exact source for m = 2. SA06 C.4m is then not needed for the very general
   claim, though it still holds for every ppav of dimension <= 5.
3. **Novelty wording.** EFS Cor. 1.5 already shows that a very general ppav of dimension >= 4 has no split embedding into
   a product of Jacobians (s_J ≠ 1) and that the degrees of such isogenies are even.
   - Not stated in those papers' introductions: the two-sided relation s_J | m | s_J^2 and the exact values s_J = 2
     (g = 4, 5) and s_J = 6 (g = 6). I read 2507.15704v3 pp. 1-4 and 2512.04902v1 pp. 1-2.
   - Still needed before any posting: a literature search, including de Gaay Fortman-Schreieder [GFS25] (cited by EFS
     right after Cor. 1.5), later citing works, and Hexagon.
   - The proof of s_J | m is classical (Matsusaka). The new content is the combination.

## Strengthening NK2 can add

EFS 2512.04902v1 (introduction, citing [EGFS25b, §8.3]) states N_g | N_{g+1}; I read that sentence but not the
specialization proof. So 6 | N_g, hence 6 | m(A), hence 6 | s_J(A) for a very general ppav of every dimension g >= 6. The
general line then becomes:
- 2 | s_J | (g-1)! for g >= 4;
- 6 | s_J | (g-1)! for g >= 6.

## How the sources were opened

- The arXiv PDFs of the three papers were fetched on 25 Nov 2026. These are transient copies in the session's
  tool-results folder.
- I extracted the text of the opening pages myself with PyMuPDF/pypdf, from my scratch folder
  `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15\scratchpad\nk2`.
- The statements above are read from those extracts, not from a summarizing tool.

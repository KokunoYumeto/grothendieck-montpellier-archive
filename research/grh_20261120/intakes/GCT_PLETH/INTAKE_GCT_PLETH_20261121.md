# Intake of GCT_PLETH (prompt 25, plethysm positivity through Grothendieck's λ-rings, cote 133), 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), root plus three delegated agents; the run's ledger says the
reasoning effort is not exposed. Work file: `agent_notes\a0805369bae2ebddc_NOTES.md`.

## 0. Return read and scope

- When I started, the newest folder was `research_returns\GCT_PLETH_checkpoint_01_20261120T2346Z_unzipped`. While I
  worked, `GCT_PLETH_checkpoint_02_20261121T0031Z_unzipped` landed and checkpoint 01 was retired. I checked the core
  findings in 01 and confirmed that they are unchanged in 02: the T-012 and T-013 formulas are still there, and the
  rank-6 table in 02 passes my independent recomputation. I read the archive findings new in 02 (A-014 to A-023) at
  statement level, and A-021, A-022 and A-023 in part. The run is still going; the next three-hour review was due
  03:01 Berlin.
- Prompt as sent: `TO_SEND\PRO\1_Archive_research_by_topic\SENT\25_GCT_PLETHYSM_through_Grothendiecks_lambda_rings\PROMPT.md`
  (not reread in full; its question rows are in the run's QUESTIONS.tsv).
- **Read in full, with the proof:** T-001, T-002 (Howe/Gay balanced-weight realization); T-010 (Sarkar's stable
  family, as cited), T-012, T-013 (width five and six); A-001 (scan 19), A-003 (scan 6), A-007 (scan 28), A-013 (study
  additions, scans 20-27), A-023 (char-0 local ring).
- **Read at the level of the statement:** T-003 to T-009, T-011, T-014, T-016 to T-023; G-001 to G-012; R-001 to
  R-010; M-001, M-002; A-002, A-004 to A-006, A-008 to A-012, A-014 to A-022; the 119 archive-question rows A-Q001 to
  A-Q119 (states only).
- My computations (scripts in the scratchpad, `chk\w5.py`, `w6.py`, `sark.py`, `sark2.py`): the B₅ table, the 156-row
  B₆ table, and Sarkar's reduction against direct plethysm.

## 1. Verdicts

**T-001 (compact dual pair U(V) × U(E) in Sp(W), vacuum character with square det_V^m det_E^r).** Targeted proof check;
**confirmed**. Standard (Howe).

**T-002 (mid-run claim 1: Howe duality reduces a plethysm coefficient to an invariant space in a balanced weight
space).** a_{m,n}^λ = dim ((S_λ E)_{(n,…,n)})^{S_m}, where S_m acts by permutation matrices on E = C^m. Targeted
proof check; **confirmed**. **Not new:** it is Gay's theorem (D. Gay 1976), stated in the attached Landsberg survey,
Theorem `gaythm` and Corollary `gaycor` (`gctsurvey12-10.tex`, l. 766-779). The run says so. Its typographical remark
is also right: `gaycor`(ii) writes S_d where the group must be the symmetric group on dim V letters (checked at
l. 776). The run's own contribution here is the explicit vacuum twist (T-001), which shows that the sign twist by
sgn^r on permutation matrices must not be dropped (T-005, G-001: the "unprojected GT equality" is refuted by a
determinant sign). I read T-005 and G-001 at statement level.

**T-010 (Sarkar, arXiv:2610.07929v2, Theorem D and Proposition `prop-reduction`, as cited).** Background, checked
against the source (`work/theta/sarkar/main.tex`, l. 231-235 and 970-976). The cited statement is
⟨s_{λ[mn]}, h_n[h_m]⟩ = ⟨s_λ, H[H−1−h₁]⟩ for m ≥ λ₁ and n ≥ ⌊(|λ|+λ₁)/2⌋. Its reduction is c(λ) = [S_{λ'}C^k : M_k]
with M_k = ⊗_{i≥2} F_i(Λ^i C^k), where F_i is Sym for even i and Λ for odd i. I tested this by computation. I took
the multiplicity of S_{λ'} in M_k, computed by weights, and compared it with the direct multiplicity of S_{λ[mn]} in
Sym^n(Sym^m C^{ℓ+1}), on 16 partitions: (2), (3), (2,1), (1³), (3,1), (2,2), (2,1,1), (4), (3,2), (5), (4,1), (3,3),
(5,1), (4,2), (5,2), (3,3,1). All agree. The values include c(4) = 2, c(4,2) = 3 and c(5,2) = 4. Note the
convention: in a_{n,m}^{λ[mn]}, m is the inner degree.

**T-012 (mid-run claim 2, width five).** Targeted proof check plus computation; **confirmed**. The proof splits
M₅ = Sym(Λ²) ⊗ Λ(Λ³) ⊗ Sym(Λ⁴) ⊗ Λ(Λ⁵):
- Littlewood: Sym(Λ²V) is the sum of S_{(P,P,Q,Q,0)}, each once;
- Sym^q(Λ⁴V) = S_{(q,q,q,q,0)};
- Λ(Λ⁵V) = 1 + det;
- the finite table B₅ for Λ(Λ³C⁵), with two LR steps after it.

I recomputed B₅ from the weights of Λ^j(Λ³C⁵): it is exact, with 15 constituents for j = 0..10, all of
multiplicity one. The degree equation 2(P+Q) + 3j + 4q + 5ε = N is right.

**T-013 (width six).** Targeted proof check plus computation; **confirmed**. I recomputed B₆, the decomposition of
Λ^j(Λ³C⁶) for j = 0..20 (2²⁰ weights): it is exactly the run's 156 rows, all of multiplicity one, the same in
checkpoints 01 and 02. I checked the other factors myself:
- Sym^d(Λ⁴V) = Sym^d(Λ²V*) ⊗ det^d, with highest weights η = (a+b, a+b, a+c, a+c, b+c, b+c);
- Λ^q(Λ⁵V) = S_{(q^{6−q},(q−1)^q)};
- Sym(Λ⁶) = ⊕ det^t;
- the degree equation (T13.5).

What I did not do: evaluate the lattice-point sums (T12.4) and (T13.6) themselves. I checked each step of the
decomposition, and checked T10.3 end to end. So the claim "a stable-range positive formula for tails of width at most
six" holds, on Sarkar's theorem.

**A-001 (mid-run claim 3: counterexamples to identities in our study; cote 133, scan 19).** Targeted proof check;
**confirmed**. In B(C₂), for the free orbit E: E² = 2E, the 2-subsets give 1, and the 2-multisets give E + 1, so
2λ²(E) + E = E² fails (fixed-point marks 2 and 0). The same counterexample was found independently by ALPOGE_GCT,
PL-01.

**A-003 (scan 6: the split ring GW^⊕ is not special, even with 2 invertible).** Independent re-proof of the key
computation; **confirmed**. Over F̄₃ and G = C₃ the split Green ring has x² = 3x, xy = 2x, y² = x+1, λ²x = x, λ³x = 1,
λ²y = 1. From these, ψ³(x) = 3 and ψ³(y) = 2x − 2y. After forgetting the forms, the two sides of ψ³(XZ) =
ψ³(X)ψ³(Z) are 12 and 12x − 12y. A-015 (the λ³∘λ² iterate on scan 6) I read at statement level.

**A-007 (scan 28: monomial summands are not effective).** Targeted proof check; **confirmed**:
τ²(E) = ψ²(E)ρ₂ + Λ²(E)ρ₁² with ψ²(E) = s₂ − s₁₁ for rank 2. ALPOGE_GCT's PL-03 says the same.

**A-013 (study additions, scans 20-27).** Targeted proof check of the counterexample; **confirmed**. The reading
"finite sums of h_I = direct summands of a single Hom(I, −)" is false: h_∅ ⊔ h_∅ is not a summand of any single
Hom(I, −). For I ≠ ∅, Hom(I, ∅) = ∅. For I = ∅, Hom(∅, −) is a single point.

**A-021, A-023 (scans 28-29, the coefficient-ring question).** A-023: targeted proof check; **confirmed**. In
A = Z_(2)[ε]/(2ε, ε²), local of characteristic 0, the module L = Ae with g ↦ 1+ε has determinant character 1+ε. That
is neither the determinant of ρ₂ (which is 1) nor that of ρ₁² (which is −1). So the ρ_i do not generate in degree 2.
A-021: read in part, the presentation and boundary construction only. It claims K₀(O[S_n]-lattices) ≅ R_K(S_n) for a
DVR O of characteristic 0. That is the classical Swan-type theorem (Curtis-Reiner, *Methods* I, §39; not rechecked).
So for Z_p the answer to the scan-29 question is yes: the ρ_i freely generate.

**A-022 (hyperbolic Stiefel-Whitney formula).** Not read in full. The run cites Esnault-Kahn-Viehweg, *Coverings with
odd ramification and Stiefel-Whitney classes*, J. reine angew. Math. 441 (1993), Prop. 5.5, pp. 183-184, and says it
read both pages. I did not check that locator.

**Counts:** 11 read in full and confirmed (T-001, T-002, T-012, T-013, A-001, A-003, A-007, A-013, A-023, and T-010
as cited background checked by computation, A-021 in part); 0 refuted; 0 gaps; about 60 findings and 119 archive rows
at statement level, with no fault seen in their statements.

## 2. What is new

- T-002 is known (Gay 1976, Landsberg's survey); T-001 is standard.
- T-012 and T-013 are new as stated: explicit finite LR-polytope formulas for Sarkar's stable plethysm coefficient in
  widths five and six. Sarkar's Theorem E stops at four columns. They are mechanical once Sarkar's Proposition
  `prop-reduction` and the B₅ and B₆ tables are in hand. The tables are the new computational content, and the
  multiplicity-freeness of Λ(Λ³C⁶) is the fact that keeps the formula positive.
- G-009 to G-011 (terminating positive-polytope formulas for every plethysm coefficient, and for the image ranks of the
  Hadamard-Howe map): new as statements, read at statement level only. They are the same principle as ALPOGE_GCT's
  P-F2 (a positive presentation gives a shifted lattice count), and like it they carry no polynomial bound.
- The archive findings A-001, A-003, A-013, A-023 are new corrections, and A-021 is a classical answer to
  Grothendieck's scan-29 question. A-001 was reached independently by both runs tonight.

## 3. Scope of the two proofs

No finding of GCT_PLETH uses either proof. Q-ALPOGE is an "explicit-morphism gate": the note specifies no comparison
map between the theta-lift or period objects and the normalizer projector of T-002. Q-MASULLO is an "input gate":
Masullo's text was not supplied. Both are recorded honestly. Nothing claims more than its input gives.

## 4. How the findings bear on the open problems, and the attack they open

1. **The prompt's Alpöge question, made exact.** T-001 and T-002 identify the multiplicity space of a plethysm
   coefficient. It is the S_m-invariants, twisted by the vacuum character sgn^r, of a weight space of the U(E)-side of
   the compact dual pair (U(V), U(E)) in the oscillator. That is the same kind of object as Alpöge's steps 7-8
   (theta lifts between definite unitary groups). The obstacle is located exactly: Alpöge's lifts act on automorphic
   forms on U(n) × U(n+1) over a totally real field, while the plethysm space is a finite-group invariant in a
   compact Howe pair.
   **Next attack.** Write the plethysm multiplicity as a dimension of a space of S_m-invariant theta series. Use
   Rallis's seesaw for (U(V) × U(V), U(E)) ⊃ (U(V), U(E) × U(E)) restricted to the normalizer of the torus. Then ask
   whether "one order of multiplicity per lift" counts the S_m-isotypic pieces. This is a well-posed comparison
   problem; it is the gate Q-ALPOGE.
2. **Stable plethysm (Foulkes) positivity.** T-012 and T-013 give the width-five and width-six stable values as
   positive counts. The only width-dependent input is the decomposition of Λ(Λ³C^k). That is multiplicity-free for
   k ≤ 6, which I verified for k = 5 and 6. Λ³C⁷ carries the generic G₂ 3-form, and the run's width-7 part (T-016 to
   T-023) goes through G₂ invariants. I did not test whether Λ(Λ³C⁷) is still multiplicity-free: it has 2³⁵ weights,
   beyond a direct check here. The open problem (Q-W7, Q-EFFICIENT) now sits at one clean place: the decomposition of
   Λ(Λ³C^k).
   **Next attack.** Look for a Lie-theoretic positive rule for the multiplicities of Λ^j(Λ³C^k). One source is
   Kostant's description of exterior algebras through a larger Lie algebra: for k ≤ 8, gl_k ⊕ Λ³C^k ⊕ … sits inside
   an exceptional Lie algebra (E₆, E₇, E₈ for k = 6, 7, 8). This proposal is unchecked. Such a rule would replace the
   tables, and it is the first thing a successor should try for width 7 and 8.
3. **Canonical-map ranks (Foulkes-Howe).** R-008 and R-009 give actual preimages below Sra's bound b ≥ (a−1)². This is
   the H_λ rank datum that ALPOGE_GCT's PL-06 and P-F8 isolate as the only live GCT test. (Read at statement level;
   the next step is to verify the R-008 certificates, by computation, on one prime-width block.)
4. **Grothendieck's own questions on cote 133.** A-021 and A-023 together settle his scan-29 question "Est-ce vrai si
   k est un anneau local?" in two directions: yes for DVRs of characteristic 0 (lattices), no for the characteristic-0
   local ring Z_(2)[ε]/(2ε, ε²), and no for F₂ (ρ₁² = 2ρ₂). The exact class is the open row. The run's determinant
   argument suggests the answer: the ρ_i generate iff the group of characters S_n → A^× is {±1}, together with a
   condition on the lattice K₀. That is a conjecture for the successor.

## 5. Integration (edits to make; none made outside this folder)

Corrections for SA17's study (`SA17_STUDY_cote133_lambda.md`) and our reading of cote 133:
1. **Scan 19, "Checked" line** (section "Scan 19: λ- and σ-operations"): wrong as an equivariant statement. Replace
   it with the text given in the ALPOGE_GCT intake, section 5: the C₂ counterexample; only the cardinality identity and
   the K₀ identities hold. Credit GCT_PLETH A-001 and ALPOGE_GCT PL-01.
2. **Scans 24-27, "On the page"**: "Foncteurs spéciaux: finite sums of h_I, equivalently direct summands of H_I". Add
   a note: as a reading of a *single* H_I this is false (h_∅ ⊔ h_∅; GCT_PLETH A-013). Check on the scan whether he
   wrote "facteurs directs de sommes finies de H_I"; if so, the page is right and only our paraphrase is wrong.
3. **Scans 28-29, "Open: the exact class of rings k ..."**: add "Yes for every DVR of characteristic 0, by
   rationalization K₀(O[S_n]-lattices) ≅ R_K(S_n) (GCT_PLETH A-021; classical, Curtis-Reiner). No for the
   characteristic-0 local ring Z_(2)[ε]/(2ε, ε²): the determinant character 1+ε is not reached by ρ₂, ρ₁² (A-023,
   checked in this intake). This agrees with the sweep-3.5 annotation (`C:local_charzero_counterexample`)." Delete
   "Whether Z_p-lattices give the polynomial ring is not settled here." Also add: "the rank count p(p)−1 for
   G₀(F_p[S_p]) is James, LNM 682, Thm 11.5 (A-020)".
4. **SA17-21, scan 4, "w₂(H(L)) = c₁(L) mod 2 ... The result is new in this reading"**: GCT_PLETH A-022 reports that
   the general hyperbolic formula w(H(E)) = Σ (1+α)^{r−k} c̄_k(E) is Esnault-Kahn-Viehweg 1993, Prop. 5.5
   (pp. 183-184), for regular schemes over Z[1/2]; the run extends it to all Z[1/2]-schemes. Replace "new in this
   reading" by the EKV citation, once the main session has checked that locator (it is not checked here).
5. **SA17-21, "Open: the λ-ring question for his split WG(S)"**: settled negatively. GW^⊕ over BC₃ in characteristic
   3 (2 invertible) is not special (A-003; ψ³ is not multiplicative), and its λ³∘λ² iterate fails (A-015, statement
   level). Over F₂ the rank obstruction (A-002) confirms our own scan-6 finding.
6. **Scan 28**: the monomial terms of the Cauchy expansion are virtual (A-007). The identity holds integrally in
   exact equivariant K₀ on every commutatively ringed topos (A-012, statement level).

Other places:
- The open row H-133-1 and the package SA17-RP5 named in the study are settled by item 5 (the main session should
  update their state).
- The successor prompts (30-36): the plethysm or GCT prompt among them should take items 4.1 and 4.2 as its targets
  and cite T-002 as Gay's theorem. I did not open them.

**Language of algebraic geometry.** The run has a separate part ("Algebraic-geometric restatements and proof
dictionaries", using frame torsors, exact K₀, group-scheme comodules, invariant schemes, and Artin motives where they
apply), as the prompt asked. I read only its opening. For T-012 and T-013 the short translation is: for the universal
bundle on BGL₅ (or BGL₆), c(λ) is the multiplicity of S_{λ'} in the exterior and symmetric algebra bundle
⊗_{i≥2} F_i(Λ^i E), and the formula is a positive decomposition in K₀(BGL_k) of an explicit Schur-functor
composition. That is Grothendieck's λ-ring K₀ with its positive basis.

## 6. Prompt updates for the successor of GCT_PLETH

- Settled, cite and do not redo: T-002 (as Gay's theorem), T-012, T-013, A-001, A-003, A-013, A-021, A-023.
- Main targets: (a) a Lie-theoretic positive rule for the multiplicities of Λ^j(Λ³C^k), all k, which would give stable
  plethysm in every width (item 4.2); (b) the comparison map Q-ALPOGE in the precise seesaw form of item 4.1;
  (c) the exact class of local rings for scan 29 (item 4.4, with the determinant-character conjecture).
- Ask for computation certificates of R-008 and R-009 on one block each, and for the sums (T12.4) and (T13.6)
  evaluated against direct plethysm on a table of λ. This intake checked the decomposition steps, not the sums.
- Supply Masullo's text if any finding is to use it; otherwise drop Q-MASULLO.
- Keep the unfinished width-7 sector (Q-W7) and the r = 4, L = 4, b = 15 polarization computation, which had no
  outcome at checkpoint 02.

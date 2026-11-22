# Intake of GCT_NSRH, part 2: checkpoint 05 (what is new since checkpoint 03)

By Claude Opus 5.5 at effort high (the agent of part 1 and of the cp03 intake), for the main session (Claude Opus 5.5 at
effort max), 21 Nov 2026, about 03:40 UTC. The run is GPT-6 Astra (ChatGPT Pro mode). The run records its effort as "not
exposed"; it is still going.

Earlier parts:
- `INTAKE_GCT_NSRH_20261121.md` (part 1: checkpoint 01, findings F01–F17);
- `INTAKE_GCT_NSRH_cp03_20261121.md` (checkpoint 03: F24, F26, F32, F34 and F42 checked).

Work file: `agent_notes\20261121_intake_GCT_NSRH_NOTES.md`.

## 0. What I read, and my scope

**Return:** `research_returns\GCT_NSRH_checkpoint_05_20261121T0247Z_unzipped\`, snapshot 02:47 UTC. It was the newest
checkpoint present when I started. The paper has F01–F54 (143 pages). The first scheduled three-hour review (02:00 UTC)
recorded movement, so the no-movement count is 0.

**Read:**
- `STATUS_TIME.txt`;
- `LEDGER.md`, every block from 00:58 to 02:47 UTC, including the review-01 table;
- the changed rows of `QUESTIONS.tsv` (in the review-01 snapshot);
- `PROGRESS_REVIEW_01.md` (head).

**In full, with its proof:**
- **F50**, *Gaussian path signs and the exact weight gate* (paper lines 4563–4991). It is the main new result on the main
  question.

**At the level of the statement:** F43, F44, F45, F46, F47, F48, F49, F51, F52, F53, and F54 parts 1–3.
- On F43 I checked the trace formula against F26 and F42.
- On F45 I checked unimodality for P₁P₂.

**Not read:** the new reports still pending (the both-actions marked-trace supplement; the fractional mixed right-action
work).

## 1. Verdicts on the new findings

### F50: targeted proof check, confirmed.

**What it proves.** In odd characteristic, the quadratic Artin–Schreier line G_ψ = H_c¹(A¹, 𝓛_ψ(x²)) gives an exact
functor J_ψ(C) = 𝓛_ψ(x²) ⊗ p*(C ⊗ G_ψ^∨)[1]. It has three properties:
- it encodes any effective finite Weil space C, in the sense that RΓ_c(A¹, J_ψ(C)) = C;
- it is fully faithful into perverse Weil sheaves;
- it satisfies the path-sign hypothesis of F03 exactly, with zero error, at an unbounded set of good even k.

For this construction, the pointwise and dual bounds that F03 and F17 need hold **if and only if C is pure**.

**What I checked.**
- The tridiagonal recurrence d_k = d_{k−1} − (h²/4)d_{k−2}, and d_k = (h/2)^k U_k(1/h).
- Squarefreeness when p ∤ k + 1. This gives the good set k = 2pr.
- The leading coefficient (−1)^m/2^k.
- The concentration of RΓ_c(H_k, 𝓛_ψ(Σx_i²)) in degree k − 1, by the pencil in h:
  - The generic fibre is rank one in degree k.
  - At the simple roots of d_k, a Schur complement leaves a free affine line, so the fibre sits in degree k + 1.
  - The lisse rank-one sheaf T_k is geometrically nonconstant, because its Kummer factor χ(d_k) has monodromy −1 at the
    simple roots. So H_c⁰ = H_c² = 0 on U_k.
  - The Leray terms both sit in total degree k + 1.
  - Integrating out h gives E(−1)[−2] on H_k.
  - No weight theorem enters.
- The trace identity QN = −Tr(F^n | B_{k,ψ}), with B_{k,ψ} = G^k(H¹(C_k) ⊕ η_k) ⊕ E(−1)G^{k−1}W_k. This uses:
  - the count Σ_h χ(d_k(h)) = −Tr H¹(C_k) − χ(ℓ_k);
  - g^k = γ^{kn} and g^{k−1} = −γ^{(k−1)n} at even k.
- The check at k = 2: QN = −2Qγ^n − Q.
- The bad-length example, q = 5 and k = 4, where the root 125 has a positive coefficient.

**A by-product.** F50 contains a weight-free, sign-only proof that |Gauss sum| = q^{1/2}. The result is classical; the
proof is new as far as I know.

**How it bears.** This is the exact location of the obstacle for the whole sign-only route.
- The opposite path sign can always be manufactured: Gaussian encoding gives it for any coefficient space C.
- So all the content of F03 lies in the pointwise bound |t_n(x)| ≤ BQ^{a/2}.
- In the Gaussian encoding, that bound is the purity of C itself, so the encoding gains nothing.
- The route has force exactly when the trace function's pointwise size is known independently of its cohomology. In
  Deligne's setting that means stalks of lower weight, which is how HODGE_SIGN H01 uses it (generic weak Lefschetz on U^k
  with a constructible F).
- For the nonstandard quantum groups the question becomes: is there a trace system whose stalks are known to be pure
  while its cohomology carries the nonstandard coefficients? That is gate R of the paper, now with nothing left over on the
  sign side.

### Findings checked at the level of the statement

| Finding | What it says | My check |
|---|---|---|
| F43 | A positive basis of the actual rank-64 tensor module for the right generators P₁, P₂, the ordinary left operators and the commutant matrix units, over Z[v^±, 1/(2(D−1))], fixed by IV's tensor bar. All-word traces: Tr(P_w) = 20D^L + 16D^{L−s} + 4D^{L−2s}(D − 2)^{2s} | The formula reproduces F26 (P₁P₂: 20D² + 16D + 4(D − 2)²) and F42 (P₁^k: 40D^k). Consistent; the basis itself not checked |
| F44 | A relative smooth proper order Γ = End_C(C ⊕ L₁), of rank 5, recovers the actual algebra as a corner and the module as Hom; Ext¹ = (R/Δ)^{64} keeps the collision order; a Frobenius unit trade-off | Not checked |
| F45 | Every word trace is the character of an even-weight SL₂ representation, realized by Chow-motive projectors on products of P¹, with hard Lefschetz | Unimodality checked for P₁P₂: coefficients 24, 96, 160, 96, 24. Rest not checked |
| F46 | Exact pure Weil End/Hom objects (a Cayley Frobenius) giving the actual algebra A and module M under every base change | Not checked |
| F47 | No multifusion K₀ realizes the full collision algebra A₁. A positive Hermitian realization with self-adjoint generators kills the 4-dimensional radical | The radical claim is immediate (self-adjoint nilpotents vanish); the rest not checked |
| F48, F51, F52, F54 | A family of "Frobenius retuning" obstructions: Spec F(b^n) = Spec F(b)^n, or trace retuning alone, forces monomial or root-of-unity spectra, so the nonsimple nonstandard algebra cannot be a full Frobenius centralizer | For F51 I checked the branch point: one element of K with an irreducible minimal polynomial cannot take two different constant values on infinitely many b^n. Shape correct; proofs not read |
| F49 | An actual 1/h projector that fails the original global lattice and VIII's dual global form | Not checked |
| F53 | A twisted additive convolution making J_ψ symmetric monoidal on its image | Not checked |

**Changes to what I checked earlier.**
- F01–F42 are unchanged in substance.
- The EGA and SGA 6 citation corrections (ledger 01:37 UTC) change no mathematics. F15 keeps EGA I §9.5 for the
  scheme-theoretic image.
- Q3-AMBIENT still reads REFUTED_FOR_FIXED_INCLUSION, with the C′ cone. My INT-NSRH-1 and INT-NSRH-2 are still not taken
  up: nothing in checkpoint 05 mentions GCT IV Remark 11.19 or the dual KL cone.
- F43's module positivity is a different statement. It sits well with them: with INT-NSRH-2, both the algebra Ȟ₃ (in the
  C⊗C cone) and its rank-64 module have positive bases.

**Counts for part 2.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 1: F50 |
| Read at the level of the statement | 11 |
| Gaps or refutations | 0 |
| Withdrawals of earlier findings | 0 |

## 2. What is new

**Against the literature.**
- F50's concentration computation for the path hypersurface with quadratic coefficients is a concrete instance of what
  HODGE_SIGN H01 does in general by generic weak Lefschetz (Katz).
- F50's sign-only proof of |g| = √q appears to be new as a proof; the result is classical.
- F45's SL₂ characters and the F43 positivity are new for this rank-three algebra.
- GCT IV, Example 19.2 already gives a based rank-three example. The run says so.

**Against our results.** F50 answers what part 1 left open (gate S, the path sign): gate S is no longer an obstacle. What
remains is the pointwise and stalk input. This sharpens the reading of HODGE_SIGN's H01: the sign-only proof works there
because generic weak Lefschetz on U^k supplies concentration, while the stalks of F carry the known weight a. That is the
input F50 shows cannot be faked by encoding.

## 3. Scope of the two proofs

No new finding uses Alpöge's or Masullo's theorems as an input. F50 uses only SGA 4½ (*Sommes trig.*, 1.7–1.9, 1.18; and
4.2–4.4, pp. 196–197), Milne's notes and the Stacks Project. Nothing claims more than its input gives.

## 4. Integration (in the project's terms)

**QUESTIONS rows.**
- **Q3:** add "F50: the path-sign hypothesis (S2) is realizable for every effective coefficient space at good even k; the
  surviving gate is exactly the pointwise stalk bound."
- **Q3-GCT:** the gate becomes "a trace system with independently bounded stalks whose cohomology carries the designated
  nonstandard coefficients".

**Grothendieck's frameworks.**
- In SGA 4½, *Sommes trig.*, J_ψ is the Fourier-transform encoding of a point object by the quadratic Artin–Schreier
  sheaf.
- In cote 16, the hyperplane-section picture of part 1 still applies. The sign is the degree of the new cohomology,
  E^{n−1} on our scan 036. F50 computes that degree for the path quadric pencil without weights, through the singular
  members, which Grothendieck's induction treats via the evanescent part.

**The other runs.**
- **HODGE_SIGN, H01:** F50 is the explicit quadric case of H01's concentration step, and the Gauss-sum test case.
  - **Edit for the H01 write-up:** include F50's k = 2 and q = 5, k = 4 checks as worked examples.
  - Cite F50 for the fact that the pointwise bound cannot be removed.
- **TRACE_DET:** F50's B_{k,ψ} contains H¹(C_k) of the curve y² = d_k(h). That is the cote 1 / curve dictionary (PRG-FF)
  inside the path count.

**The successor of GCT_NSRH.** Points 1 and 2 of my cp03 intake stand: INT-NSRH-1 and INT-NSRH-2 should be given to it, and
F42 kept as the stated limit. Add a third point: ask for the stalk side. For the actual rank-three objects of F44 and F46,
is there a sheaf on an affine space whose stalks are pure of a known lower weight and whose compact cohomology is the
coefficient object? That is the single remaining input of the sign route.

## 5. Hexagon readiness

| Result | Verdict |
|---|---|
| F50, the sign-only proof of |g| = √q | **Fold into H01**, as the worked Gaussian case and as the proof that the pointwise bound is essential. Complete and checked by me; self-contained; stable. Not separate. |
| F43–F54 | Not ready: run active, checked only at the level of the statement. Interest limited to GCT. |

Nothing to flag.

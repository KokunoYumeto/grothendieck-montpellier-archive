# Primer: the mathematics of GCT_GINEQ as of its final return (20 Nov 2026, 23:40 UTC)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), as the GCT field expert, 23 Nov 2026, for the main session
to read after a compaction. It restates; it does not develop.

## The run

- **Prompt 27,** "GCT, Grothendieck's inequality and tensor norms".
- **Model:** GPT-6 Astra (ChatGPT Pro mode), run GCT_GINEQ-2026-11-20-R1, root and three sub-agents; the run records its
  effort as "not exposed".
- **Final return:** `grothendieck_archive_transcription_20261110\research_returns\GCT_GINEQ_final_20261120T2340Z_unzipped\GCT_GINEQ.tex`
  (F-01 to F-23, lines 90–1620). There are no checkpoints.
- **Intake:** `INTAKE_GCT_GINEQ_20261121.md`, in this folder, by a17221e5 (Claude Opus 5.5 at effort high). All 23
  findings were read in full with their proofs, and the run's scripts were rerun. **All 23 have a targeted proof check
  `[TPC]`, five of them also our own computation `[COMP]`.**
- **Inputs:** no form of GRH (neither Alpöge nor Masullo). B-06 is conditional on UGC.
- **Successor:** BR_PENCIL (prompt 44).

## 1. The answer to the main question

The matrix inequality "nuclear² / Frobenius² ≤ rank" fails for tensors.
- **F-05 `[TPC]`.** For M₂ all three norm ratios equal 8, while Strassen gives rank 7. Tensor powers give 8^k against 7^k,
  so no fixed constant and no power of K_G repairs it.

Three replacements:
1. **F-01 `[TPC]`.** BR(T) ≥ ⌈b(T)^{1/(d−1)}⌉, the valid full-norm inequality, with a, c in place of b as well. The proof
   is an orthogonal expansion over supports, then Cauchy–Schwarz. It is always dominated by a mode flattening.
2. **F-02, F-12 `[TPC]`.** Nuclear/operator certificates on one linear map, a flattening or a Koszul flattening (F-12 is
   Landsberg–Ottaviani), recover exactly that map's rank bound. So they inherit the rank-method barriers (B-05: EGOW;
   Lovitz's 2N − 1).
3. **F-13, F-14, F-23,** below: norms on the whole image, and then an exact algebraic reduction that needs no norm.

**Grothendieck's inequality proper (F-09 to F-11 `[TPC]`)** gives only a matrix-rank test.
- That test needs the dimension-dependent K_G(s).
- It gives nothing on the natural flattenings (F-10). Those are sign-equivalent to nonnegative matrices, so their
  Grothendieck gap is 1.
- F-11 has a CHSH-type example, 14/5 > 2.

## 2. The main results

### F-13, border substitution in any order `[TPC]`

**Statement.**
- BR(T) ≥ q + min_{u∈U} BR(u) − 1, for any order b ≥ 2.
- In norm form, with α(U) the injective norm of the projector P_U.

**Proof.** In an approximating decomposition, dim U_ν + dim L_ν = s_ν + 1, and the limits stay in U by Grassmannian
convergence. For b = 2 and three factors this is Landsberg–Michałek Prop. 2.3.

### F-14, the constants α `[TPC]`, `[COMP]` for P₄

**Statement.**

| Family | α |
|---|---|
| M_n | 1/n |
| D_n | 1/b! |
| P_n | b!·C(n,b)/n^b |
| polynomial det | C(n,b)/n^b |
| polynomial per | an upper bound |

The permanent bound C(n,h) + 1 equals Han–Song Prop. 4.1.

### F-23, exact residual reduction `[TPC]`, `[COMP]`

**Statement.**
- min_{u ∈ U_{n,b}} BR(u) = BR(T_b), hence BR(T_n) ≥ C(n,b)^s + BR(T_b) − 1.
- So BR(det₄), BR(per₄) ≥ 39.
- With Conner–Harper–Landsberg and Conner–Huang–Landsberg seeds: det₅ ≥ 116, per₅ ≥ 115, det₆ ≥ 416, per₆ ≥ 415.

**Proof.** Coordinate projections kill every other basis vector and keep the chosen one, and projection doesn't raise
border rank.

**Superseded over C.** BR_PENCIL raises det₄ and per₄ to ≥ 42 over every field and ≥ 43 over C (R-05, R-08, R-10). Its
R-01 at j = 1 re-proves F-13/F-23 with proper incidence over every algebraically closed field.

**For large n,** Farnsworth's additive term (about 4^n/n⁴) overtakes F-23's (about 2^n/n).

### F-04 `[TPC]`, `[COMP]`

ε and π of the normalized det/per tensors. Symmetric nuclear decompositions with n!·2^{n−1} and 4^{n−1} terms; the
second is Glynn's formula.

### F-08 `[TPC]`: a source defect

Two displays of Friedland–Lim v3 are false as printed: the lemma before Theorem 9.4, and the display before eq:bdnn.
- A = e ⊗ I_m gives m against 1.
- I_m gives m against √m.
- The conclusion eq:bdnn stands.

### The frameworks (F-15 to F-22) `[TPC]`

- F-15: an integral secant image over Z.
- F-16: Koszul maps as morphisms of locally free sheaves.
- F-17: the Hilbert–Grassmann graph closure.
- F-18: the incidence locus I_{q,s} ⊂ Gr(q,W) is closed, so border substitution is "[U] ∈ I_{q,r−q+1}" (EGA II 5.4–5.5).
- F-22: a divided-power catalecticant over Z.
- F-19: no norm is GL-invariant. This is the obstacle for GCT proper.
- F-20, F-21: K₀, λ, γ, stalk and weight data do not determine tensor rank.

## 3. Open rows and the attacks the intake named

| Row | Attack |
|---|---|
| Substitution in j > 1 dimensions (the Landsberg–Michałek full form) | Koszul flattenings of the j-dimensional residual pencils. BR_PENCIL then did this |
| Q-30: certify α(U) outside the four families | The DPS/symmetric-extension SDP hierarchy |
| The GL-invariant use of α for orbit closures | The orbit maximum of α, a moment-map/Kempf–Ness quantity (the Bürgisser–Garg–Oliveira–Walter–Wigderson scaling framework). Not named by the run |
| Grothendieck's inequality | Only inside a nonlinear argument: rounding for α(U), or Koszul flattenings with sign frustration |

## 4. Where the results went

- **Prompt 44, BR_PENCIL:** this intake was its brief. Its results went to Hexagon H03.
- **Errata:** the Friedland–Lim v3 defect (F-08).
- **pequalnp fleet:** F-13 (proved for border rank; the proof works verbatim for exact decompositions with any atoms)
  specializes to **L-gct-139**, riffle rank of [a=b][c=d] ≥ 2n − 1, after the atom translation PNP-MBR:A2. This is
  recorded as a parallel in `<local>/pequalnp_work\fleet_map\JOINT_GCT_LEMMA_SPACE.tsv`.

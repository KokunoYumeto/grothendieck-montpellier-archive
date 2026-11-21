# Determinants audit — TRACE_DET run 2026-11-21

Author/checker: GPT-6 Astra Pro, agent `/root/determinants_audit`; effort setting not exposed to this agent. Sources read on 2026-11-21 Europe/Berlin (2026-11-20 UTC).

## Scope and source discipline

The stipulated theorem of Alpöge is used as a cited theorem, as requested. This report does not audit its truth or replay Lean. It distinguishes the consequence RH ⇒ positivity of a separately constructed diagonal operator from a claimed identification of an operator inside Alpöge's proof.

Source files directly read: `ALPOGE_remark.pdf` (all four pages, extracted with pdftotext), `ALPOGE_Main.lean` (all), `ALPOGE_Statements.lean` (all), `ALPOGE_LEAN_MAP_20261120.md` §§0–5 and relevant searches, `FABLE_PROGRAM_SUGGESTIONS_20261120.md` §3, its explained counterpart §3, `INTAKE_RESEARCH_SA23_20261120.md` §4.1, archive cote 1 scans 79,80,111,112.

Exact source locations for the determinant names:

| Claim | Supplied locator | What it actually specifies |
|---|---|---|
| Stepanov determinant | Alpöge, *Remark*, p.3, §2, step 1 | The name only; no matrix, entries, dimension, variable, or determinant identity. |
| `W(1_S)≥0 via a determinant` | *Remark*, p.3, §2, step 4 | A named inequality and analogy with multiplicity one; no definition of W, S, matrix, or spectral variable. |
| Determinants containing GGP periods, 0/1 interlacing | *Remark*, p.4, §2, step 7 | A description of the period input; no actual determinant expression. |
| Path quadric Fourier sum | *Remark*, p.3, step 3 and footnote 3 | A displayed sum in h,x_1,…,x_k, sufficient to formulate the toy model. |
| RH/Dirichlet endpoint | `ALPOGE_Main.lean:4,6,8,10,12`; `ALPOGE_Statements.lean:3–17` | Final propositions and imports; no determinant construction. |

The supplied map is a prior textual analysis, not the full code. Its §4 assigns confidence “none” to its matches for steps 1 and 4, and “medium” to step 7. For step 1 it reports no `Stepanov` names; for step 4 no `bootstrap`; for step 7 it points to `Formalism/PeriodIntegrals/BesselPeriodGGP.lean`, `Formalism/SharpRestriction/CuspSpanNormBounds/OscillatoryIntegralBounds.lean`, and `CompanionTheory/AutomorphicTheory/BesselWaveGrids`. These files are not in the attached ZIP. They cannot be cited as files read in this run. A prior map's name match is not a theorem that identifies the determinant.

An additional retrieval route was attempted: web searches for the exact missing filename and Alpöge's determinant. Search found public source-code mirrors (CocoSgt/riemann-hypothesis-lean and jsmorph/rh) but no indexed mathematical content for the needed file. Opening both GitHub and raw GitHub versions of `src/Formalism/PeriodIntegrals/BesselPeriodGGP.lean` returned `DisabledError` in the search service. No source code from that file was inspected. No inference about the absent code's content follows from failed retrieval.

## DET-01 — The literal finite Fourier identification is refuted

**Statement.** The assertion that, for a nonnegative weight t, the toy's Fourier-after-multiplication operator itself is the positive operator B whose determinant is Ξ(√w)/Ξ(0) is false. Already q=3 and t≡1 provide a counterexample, whether or not the Fourier transform is normalized.

**Proof.** Let ω=e^{2πi/3}, and let K=(ω^{xy})_{x,y=0,1,2}. Then

\[
K=\begin{pmatrix}1&1&1\\1&\omega&\omega^2\\1&\omega^2&\omega\end{pmatrix},\qquad
v=(0,1,-1)^T,
\]

and Kv=(ω−ω²)v=i√3 v. Thus K has a nonreal eigenvalue; it is not self-adjoint, let alone positive. The unitary normalization K/√3 has eigenvalue i and has the same obstruction. Since t≡1, D_t=I and both conventions K D_t and D_t K give K. A positive Hilbert-space operator has real nonnegative eigenvalues, so neither operator can be the stipulated positive B or a unitarily equivalent realization of it. ∎

The exact calculation also gives K²=3J, where J interchanges coordinates 1 and 2, and characteristic polynomial (λ²−3)(λ−i√3). Consequently even multiplying by a nonzero scalar cannot make every eigenvalue nonnegative: the pair ±√3 persists. At q=2, t≡1 gives a real symmetric Fourier matrix with eigenvalues ±√2, so restricting to a real Fourier kernel does not repair positivity.

**Check.** Complete proof reread; the displayed eigenvector calculation independently evaluated symbolically with SymPy. The computation is corroboration, not a Lean certificate.

**Grothendieck location.** This separates finite Fourier endomorphisms from the positive Hermitian `h=√(u* u)` of cote 1, scan 79, Corollaries 4–5, formulas (18)–(19). There is no sheaf or motive identified by this toy operator; calling it a realization of a motive over Spec Z would add mathematical structure not supplied.

## DET-02 — The path sums are matrix coefficients, not the traces of powers

**Statement.** For t≥0 on F_q and a fixed additive character ψ_h, put D=diag(t), a=(√t(x))_x and A=D^{1/2} K_h D^{1/2}. For k≥1 the path sum is

\[
S_k(h)=a^*A^{k-1}a.
\]

The power trace is instead the closed-cycle sum

\[
\operatorname{Tr}(A^k)=\sum_{x_1,\ldots,x_k}\prod_{j=1}^k t(x_j)
\psi_h(x_1x_2+\cdots+x_{k-1}x_k+x_kx_1).
\]

These are generally different.

**Proof.** In a matrix entry of A every edge contributes √t(x) ψ_h(xy) √t(y). Multiplying k−1 entries and the two endpoint entries of a gives exactly one factor t(x_j) at each vertex of the path. Because a is real, a*=a^T. In a diagonal entry of A^k the final vertex equals the initial vertex, which creates the missing closing edge x_kx_1 and exactly one t-factor per vertex. This proves both identities. For q=3, t≡1, h=1, K²=3J and J·1=1 give S_3=1^T K²1=9. On the other hand Tr(K³)=3 Tr(KJ)=3∑_x ω^{−x²}=−3i√3. Hence S_3≠Tr(K³). ∎

There is a correct generating-function identity near z=0,

\[
\sum_{k\ge1}S_k(h)z^{k-1}=a^*(I-zA)^{-1}a.
\]

It follows by the finite-dimensional Neumann series. The Fredholm/characteristic determinant encodes the different series

\[
-\frac{d}{dz}\log\det(I-zA)=\operatorname{Tr}\bigl(A(I-zA)^{-1}\bigr)
=\sum_{n\ge1}\operatorname{Tr}(A^n)z^{n-1}.
\]

The latter follows by differentiating the finite determinant, or by factoring its characteristic polynomial over C and expanding. Thus the toy's natural generating object is a resolvent matrix coefficient. Identifying it with the logarithmic derivative of the Ξ determinant requires an additional theorem; the missing closing edge cannot be erased by terminology.

**Check.** Complete proof reread; q=3 S_3 and trace computed symbolically, with outputs 9 and −3√3 i.

**Grothendieck location.** Cote 1, scan 79, canceled theorem/corollary and margin formula (23), and scan 80, concern exterior-power coefficients and actual traces. They do not replace arbitrary matrix coefficients by traces. In a λ-ring of finite-dimensional endomorphisms, the characteristic determinant belongs to the exterior-power operations; the resolvent coefficient additionally depends on a chosen vector and covector.

## DET-03 — A fixed finite determinant cannot equal the Ξ Fredholm determinant

**Statement.** If A is any endomorphism of an r-dimensional complex vector space, then det(I−wA) cannot equal Ξ(√w)/Ξ(0). This remains true after any affine substitution of w in a fixed finite matrix polynomial determinant.

**Proof.** det(I−wA) is a polynomial of degree at most r, whereas Ξ(√w)/Ξ(0) has infinitely many zeros, inherited from the infinitely many nontrivial zeros of ζ after identifying the pair ±γ. A nonzero polynomial has finitely many zeros; both functions have value 1 at w=0 in the unshifted comparison, so the polynomial cannot be identically zero. More generally a finite matrix with polynomial entries has a polynomial determinant, and the same zero-count obstruction applies. ∎

This does **not** prohibit a sequence of finite determinants converging to the Ξ determinant. Nor does it prohibit putting nonpolynomial Ξ-dependent entries into a one-by-one matrix. It refutes only a literal identification with a fixed finite linear characteristic determinant (or a fixed polynomial-entry determinant).

**Finite analogue qualification.** Any finite matrix is trace class after extension by zero to a Hilbert space, and its finite determinant is then a Fredholm determinant. This formal embedding does not establish that it is a finite compression of the specific B attached to Ξ. Every finite rank vector bundle E has a determinant line Λ^rE; a determinant of an evaluation or period map can live there without providing any zeta spectral parameter. The finite characteristic determinant, specifically, satisfies

\[
\det(I-wA)=\sum_{j=0}^r(-w)^j\operatorname{Tr}(\Lambda^jA).
\]

This identity can be checked after triangularizing A and observing that both sides are the elementary symmetric functions of its eigenvalues. It is the finite λ-ring operation underlying the determinant coefficient formula on cote 1, scan 79. A description “via a determinant” does not specify A, E, the variable w, or this identity.

**Check.** Complete proof reread. Infinitely many nontrivial zeros of ζ is carried as classical background; no new proof of it was attempted.

## DET-04 — Determinants and power traces do not determine operator positivity

**Statement.** Even fixing all eigenvalues, the determinant, and all traces of positive powers does not force a trace-class operator to be positive. In particular Alpöge's RH implies positivity of the *normal diagonal realization* of B, but not positivity of every trace-class operator with the same Ξ determinant.

**Proof.** Let B=diag(b_1,b_2,…) on ℓ², where every b_j>0 and ∑b_j<∞, as supplied by RH and b_j=γ_j^{-2}. Replace the top-left block diag(b_1,b_2) by

\[
C_0=\begin{pmatrix}b_1&1\\0&b_2\end{pmatrix}
\]

and leave the remaining diagonal entries unchanged, giving C=C_0⊕diag(b_3,b_4,…). C is trace class because it is the sum of the trace-class diagonal B and a rank-one operator. For every n≥1, the diagonal of C_0^n is (b_1^n,b_2^n), so Tr(C^n)=∑b_j^n=Tr(B^n). The direct-sum product formula gives det(I−wC)=∏_j(1−wb_j)=det(I−wB). But C_0≠C_0*, hence C≠C*, so C is not positive. ∎

For a still simpler finite warning, M=−I_2 has det M=1>0 although M is negative definite. Even det(I+sM)=(1−s)²≥0 for every s≥0 does not imply M≥0. A determinant sign is weaker than positivity of a Hermitian form; the latter must control all vectors, or an equivalent complete system of Hermitian principal-minor tests.

**Check.** Complete proof reread, including b_1=b_2 (the upper triangular block still works). No assumption of simple zeros is required.

**Grothendieck location.** Cote 1, scan 79, formulas (18)–(19), compares the determinant of arbitrary u with that of |u|. It does not conclude u≥0. Scan 79 margin (23) and scan 80 yield spectral trace identities, not a construction of an adjoint or a polarization. In motive language, characteristic polynomials record eigenvalues; a positive Hermitian realization or polarization is extra structure.

## DET-05 — A sufficient, concrete bridge for a direct sign proof

**Statement.** Let H be a Hilbert space and A_N positive finite-rank operators on H with ||A_N−B||_1→0. Then B is positive and

\[
\det(I-wA_N)\longrightarrow\det(I-wB)
\]

locally uniformly in w. If the limiting determinant is Ξ(√w)/Ξ(0), this would give a genuinely direct positive-operator realization.

**Proof of the new elementary part.** Trace-norm convergence implies operator-norm convergence. Thus for every v, ⟨v,Bv⟩=lim_N⟨v,A_Nv⟩≥0. Also B*=lim A_N*=lim A_N=B in operator norm, so B is self-adjoint and positive. The determinant convergence is the standard trace-norm continuity theorem for Fredholm determinants; it is cited as background here and should be supplied an exact standard locator by the main paper if used. ∎

This is one sufficient bridge, not a necessary form of every possible identification. An alternative is a unitary isomorphism between a constructed Hilbert space with an explicitly positive operator and the diagonal spectral model, with equality of determinants proved independently. A third is an explicit Hermitian kernel whose quadratic form is exactly the required Weil form and whose characteristic determinant is Ξ(√w)/Ξ(0). No such bridge is specified in the supplied determinant passages.

## Main-question disposition

1. **Refuted:** the literal Fable identification of the toy Fourier-after-multiplication operator with a positive Ξ operator (DET-01), and the identification of its path sums with its power traces (DET-02).
2. **Refuted in the fixed finite characteristic-polynomial sense:** a single finite Alpöge-type determinant can literally equal det(I−wB) for Ξ (DET-03).
3. **Proved as a consequence of stipulated Alpöge RH:** positivity of the diagonal B constructed from the Ξ zeros; this is the route already present in SA23 intake §4.1(2)–(3), not evidence that Alpöge constructed that B.
4. **Not decided from available sources:** whether particular determinant constructions in the absent proof code form compatible approximants or can be transformed into a direct kernel proof. Exact current gate: identify the actual matrix/kernel and the theorem relating its full spectral determinant (or all moments) to Ξ, then establish Hermitian positivity and compatibility/convergence. Step 7's best source locator is the prior map's name-match `Formalism/PeriodIntegrals/BesselPeriodGGP.lean`, which has not been read. Steps 1 and 4 have no matched declaration even in that prior map.

This source gap should not be converted into a universal mathematical assertion that *no* such relationship exists. It also should not be filled by labeling every finite determinant a “finite analogue” of B; the latter is true only in the vacuous ambient linear-algebra sense unless a compatible family is supplied.

## Possible transcription rows noticed while reading

These are mathematical constraints, not visual paleographic corrections (only the .tex transcriptions were supplied):

- Cote 1/111, line 9: `sum_i(1+α_i z)` must be `product_i(1+α_i z)` for the genus-zero majorant used throughout; the infinite sum has divergent constant term.
- Cote 1/111, line 16: in f(Θz), to replace β by |β| one needs Θ=conj(β)/|β|, not β/|β| (unless notation elsewhere means the inverse substitution).
- Cote 1/112, line 3: θ must satisfy π/3≤θ<π/2 (with θ>π/3 harmless), not an unrestricted interval up to π; only then does cos θ>0 give x≥c|z|, while the three rotated sectors cover the circle.
- Cote 1/112, line 7: coefficient domination yields |f(z)|≤h(|z|) for nonnegative majorant coefficients, not generally |f(z)|≤|h(z)|.
- Cote 1/112, line 17: the third rotation is ω², not ω³, to obtain ∏_{j=0}²(1−ω^j z/z_i)=1−z³/z_i³.
- Cote 1/112, lines 20–23: the displayed exponential decay actually forces G≡0, contradicting the nonzero canonical product; the written weaker route through constant G reaches the same contradiction when G is shown nonzero. Do not flag “constant” as a definite mistranscription merely because a shorter argument exists.


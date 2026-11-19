# Independent cote 63 audit by the late-cote-64 agent

Date: 2026-11-19. Actor: GPT-6 Astra Pro, effort inherited/unspecified.
Run: `SA16-2026-11-19-cote64-late`; follow-up audit requested by the root agent.

This review read all eleven cote 63 Codex notes, all 58 initial claims
`C-SA16-801`–`C-SA16-858`, the 38 problem records, the entire `c63_u13.py`
and its `qseries.py` dependency, the computation's method note, and the complete
numerical output. Relevant original transcript passages were then compared
directly. The audit did not edit the root agent's files. A comparison of a
passage with a claim is a use and recheck of that passage, not a proof check
of the claim. No manuscript scans were available to this reviewer.

## Findings sent to the root agent

| Record | Exact source location | Finding and required action |
|---|---|---|
| C806 | `H63-01_transcription.tex`, scan 7, physical lines 168–172 | Include the explicit assertion that `E0(K)` has finite index in `E(K)`. The page isolates this as the part not proved by the elementary addition-formula argument. Over the complete DVR with perfect residue field in the claim, finiteness of the component quotient does not require a finite residue field. The other quotients and Haar-volume discussion require separate qualifications. The matching printed assertion was independently read in Tate 1975, §4, Theorem 4.1, p.41. |
| C811 / MP242 | `H63-02_transcription.tex`, scan 14, physical lines 369–371 and 430 | Correct the occurrence from scan 13 to scan 14. The tentative bound `ν≤v(Δ)−3` is a valid weak bound. The stronger bound `ν≤v(Δ)−6`, obtained from `f=v(Δ)−4−ν` and `f≥2` for additive reduction, strengthens it; it does not refute it. Preserve that distinction in the verdict. |
| C836 / MP261 | `H63-07_transcription.tex`, scan 63, physical line 285 | Correct MP261's scan 64 locator to scan 63. The sentence asserts a separate spanning claim about integral Fourier series, stronger than merely introducing a coefficient ring for the convergence conjecture. It was not actually stated in C836. A supplemental claim C859 is being authored. It must distinguish literal rational integers from algebraic integers and a full lattice from a complex span. |
| C829 / C834 / MP256 | `H63-07_transcription.tex`, scan 59, physical lines 139–146; scan 64, physical line 292 | Record the separate general assertion that commuting operators admit a common eigenbasis if one has distinct eigenvalues, and its lifting version modulo powers of the prime. Finite freeness, commutativity and a splitting coefficient extension matter. A supplemental claim C860 is being authored. This does not identify or construct the desired invariant modular-form module. |
| C835 / C836 | `H63-07_transcription.tex`, scan 63, physical line 263; scan 64, physical line 292 | Restore the original prime bound `q≤23` in Conjecture 3. The auxiliary Hecke prime is `p≠q`. The later higher-dimensional extension is a separate statement; the page's original conjecture is not an unrestricted assertion for all primes. |

The duplicate first Fourier coefficient at physical line 265 is already
recorded in `readings.tsv`: the transcription writes an initial `x` and a
sum beginning at 1. This review makes no ink decision. Likewise, the informal
negative expectation at `H63-05`, scan 44, physical line 142 concerns the
preceding Lehner-style divisibility statement (2.5); it should not be
silently replaced by a different partition-congruence classification.

## U13 method review

The computation is an exact finite certificate. It does not establish the
all-index, all-exponent modular theorem. The root agent's separate literature
comparison supplies the latter's stated scope.

Put `z=(η(13τ)/η(τ))²`, `t=13z`, and

\[
 Q(T)=(T^2+5T+13)(T^4+7T^3+20T^2+19T+1)^3,
\]
\[
 F(T)=(T^2+5T+13)(T^4+247T^3+3380T^2+15379T+28561)^3.
\]

The source normalization used by the program is
`j(τ)=Q(t)/t` and `j(13τ)=F(t)/t¹³`. The Fricke identity is

\[
 T^{14}F(13/T)=13^{13}Q(T).
\]

Consequently `j(τ)=F(1/z)z¹³`. The fourteen roots relevant to the trace
are the roots of **`F(T)−j(τ)T¹³`**: they are `1/z(τ)` and
`13z((τ+k)/13)`, `0≤k<13`. An earlier sentence in the method note instead
named `Q(T)−j(τ)T`. That was a documentation error; the program's coefficients
already used the correct polynomial.

Here is why the code agrees with `F−jT¹³`. Its first monic coefficient is
`c1=746−j`; for `2≤r≤14`, its coefficient `c_r` is
`13^(r−1) Q_r = F_(14−r)`, by the displayed Fricke identity. Newton sums
therefore give

\[
 U_{13}(z^n)=\frac{S_n-z^{-n}}{13^{n+1}}.
\]

The reciprocal-root sum is `−F_1/F_0=−2`. Removing the reciprocal of
the extra root gives `U13(z⁻¹)=−2−z`, exactly the initial Laurent-term
formula used by the program. The code checks the divisibility before each
division by `13^(n+1)` and works modulo `13^(100+8+1)` before reducing
to `13^8`. Hence the largest permitted division still leaves at least the
target precision. The Newton recurrence uses every needed coefficient and
keeps the required fourteen preceding power sums.

The computed operator columns retain all nonzero powers of `z` modulo the
target modulus. The code checks the degree bound before every subsequent
iteration. Actual iterate degrees are 6, then 8 at each of the next seven
steps; no unproved truncation in `z` is imposed. Because `z(q)` has valuation
1, evaluating a polynomial in `z` through `q^5299` is valid using the
corresponding finite q-series. The helper's packed integer multiplication
uses a byte base larger than the maximum possible coefficient sum, so
integer carries do not contaminate convolution coefficients. Its Newton
inverse and Euler-product construction were inspected in full.

The independent direct calculation of `E4³/Δ` checks the first 200
coefficients after one `U13`, and the first 15 after two. These index ranges
fit within the directly calculated coefficients through 2600. The reported
Fricke residual is exactly zero. The explicit six archival valuations are
`1,1,2,2,2,3` for `n=7,11,77,154,757,5299` in `c(13^6 n)`.

### Two corrections and their observed outcome

1. The root agent corrected the method note from `Q(T)−jT` to
   `F(T)−jT¹³`. The code itself did not require a change for this issue.
2. The finite Hecke loop had excluded the final admissible index for each
   auxiliary prime. The root agent replaced the exclusive range by
   `range(1, min(1000//ell, (N−1)//ell)+1)`.

After the root agent reran the program, this reviewer opened the revised
JSON output. It contains **1,715 tested pairs, with no failures, for each
of α=1,…,8**, instead of the earlier 1,691. The independently computed
q-series checks, six valuations and Fricke residual are unchanged. The
reviewer did not rerun the entire root program; this is a code-and-output
review, with a separately retained small symbolic check of the polynomial
identities and finite-loop counts. The trace matrix and eight iterate
polynomials are retained by the root program in
`work/outputs/c63_u13_trace_matrix.json`.

## Coverage crosswalk after reading every Codex note

This table records where each explicitly signalled mathematical issue in
the notes is handled. It is a coverage assessment, not an independent proof
certificate for every referenced claim.

| Codex note | Claims / problems accounting for its mathematical flags |
|---|---|
| H63-01 | C806 filtration and rationality; C807 / MP241 the deferred §4.6 argument; add the finite-index assertion above. |
| H63-02 | C811 algorithm; MP242 the tentative termination bound, with corrected scan and weak-bound verdict. |
| H63-03 | C812 genus; C813 / MP243 duality; C814 flexes; C815 discriminant; C816 / MP244 section construction; C817 / MP245 degree-six issue. |
| H63-04 | C821 / MP246 disconnected automorphisms; MP247 order-24 structure; C822 / MP248 removal of additive terms; C823 / MP249 and MP251 Hasse behavior. |
| H63-05 | C824 Ramanujan-seven assertion; C825 Lehner congruences; C826 Newman; C827–828 the 13-power calculation; C829 larger primes; C830 weight 24; C831 computational cost. |
| H63-06 | C829 and MP255–257 larger-prime eigensystems; C835–836 convergence framework; C831 cost. |
| H63-07 | C832–836 Hecke framework and conjectures; supplemental C859 integral span and C860 simultaneous diagonalization; preserve the original prime bound and existing line-265 reading alarm. |
| H63-08 | C837 Weil footnote; C838 tenth-degree field; C839 orders at 13; C856 bibliography. |
| H63-09 | C840 normal forms. |
| K63-01 | C803/C840 and MP263 canonical j-model; C815 discriminant factor; C842 Weierstrass coefficients; C843–846 / MP265–267 Hodge arguments; C854 / MP278 reused analysis. |
| K63-02 | C847–848 / MP268–269 real structure; C857/C849 / MP270 divisor regularity; C850 / MP271 deformation ring; C851 / MP272 tangent directions; C852 / MP273 action; C858 / MP274 good reduction at 3; C853 / MP275 μ3 extension; C858 / MP276 gluing; C855 / MP277 cycle specialization. |

## Limits and provenance

The supplementary integral-span claim requires its own precise primary-source
comparison. The elementary lifting lemma admits a direct proof, but cannot
substitute for constructing a finite free module with commuting lifted Hecke
operators. Those two tasks are recorded separately under
`work/parts/cote63_supplement`.

No allegation of a missing theorem is based only on a keyword search. The
coverage findings above follow from complete note/claim reading and direct
comparison of the cited passages. No root files were altered by this reviewer.

# Independent whole-proof audit: D-ATT-01–03

**Result: PASS.** Auditor `/root/imprimitive`, GPT-6 Astra Pro, reasoning effort inherited/not exposed, run `HODGE_DIVISION`, 2026-11-21. This is an independent whole-proof review of another author's new argument, with a separately authored exact computational supplement. It is not merely a review of selected examples.

## Frozen material and actual scope

The complete file `agents/g34_eightfolds/bireflection/alternating_two_tail_section.tex` was read, at SHA-256 `663aea29319e2ce97288077ba58195eaa6946f1bd5eda3033589c5b95b84ec3b`. Every line of `check_alternating_two_tail.py` and its final output `alternating_two_tail_checked.json` was also read. The author's full finite execution is attributed to the author; I did not rerun that program.

I reread the exact supporting inequalities and their proofs in the reviewed D-UP-01 and D-EX-01 sections, the root's full HD-AST-04–06 conductor argument, and the precise preceding ALT07 necessary inequality used to establish strictness. The previously reviewed actual intermediate-cover/period factorization is retained as a dependency, with its original scope; it is not replaced by a source-dimension sufficiency assertion.

## D-ATT-01: exact support and traces

For the unordered-pair constituent, when the permutation index is at least two, UP.3 and UP.4 give respectively `n−5+n/4` and `n−5+(n−4)/2`, both at least `n−3` for every `n≥15`. At index one, the actual transposition spectrum on unordered pairs has negative multiplicity `n−2`; subtracting its negative line on the letter module gives the exact minimum `n−3`. Its complementary eigenspace is larger in the stated range.

For the exterior square, EX.4 gives `n−4+n/3≥n−2`, while EX.3 gives the nonidentity-scalar bound. I independently expanded the remaining polynomial `(n²−8n+11)/4`, which is positive at and above fifteen. The transposition's negative line on the deleted module yields exactly `n−2` negative exterior-square eigenvectors. Off-spectrum scalar values have full moving rank, so taking the minimum over all scalars is legitimate.

The character formulas were checked directly on actual pair actions. The unordered-pair formula is `f1(f1−3)/2+f2`, with minimum at least minus one. The exterior formula is `(f1−1)(f1−2)/2−f2`; splitting `f1=0`, `f1=1,2`, and `f1≥3` gives the exact stated parity-safe lower bound `−floor((n−1)/2)`. The modules are actual rational orthogonal modules. Their irreducible alternating restrictions in this range are precisely the already reviewed non-self-conjugate ordinary labels; the proof does not use a virtual representation as a tensor factor.

## D-ATT-02: full normalizers, scalar arithmetic and marked supports

The normalizer argument removes the permutation of the intrinsic simple factors, then uses the full `Aut(A_n)=S_n` action on each rational module. The remaining operator is scalar by irreducibility. A scalar in the chosen actual tensor-wreath image has trivial factor permutation and induces the identity automorphism on every alternating factor. Faithfulness of the nontrivial simple-group representation then reduces to the trivial centralizer of `A_n` in `S_n`. Thus the scalar intersection is exactly the identity. This proves uniqueness and, because the rational image is an actual subgroup commuting with scalars, proves that the scalar coordinate is an actual homomorphism. Sign choices for the two extensions introduce no missing automorphisms.

It follows that the actual inducing character field lies inside the cyclotomic field of the scalar image. The original imaginary quadratic field is used only as a subfield of the inducing character field. No equality of these fields is assumed.

Convolution gives the support fraction of any active factor. A nontrivial factor cycle has the usual weighted tensor-word orbit bound of one quarter; this exceeds both displayed `mu` values for `n≥15`. Nonidentity scalar matrices have full actual moving rank. These observations cover every genuine inertia, including factor permutations and arbitrary phases.

I checked the complete trace argument for arbitrary powers. A cycle-contraction trace is a product of at most `t` ordinary character values. If it is negative, one negative factor has absolute value at most `b`; all others have absolute value at most `a`. Thus it is at least `−b a^(t−1)`. The same argument applies to every power because that power remains in the actual rational tensor-wreath group. This assertion precedes scalar extraction and is not a claim that an arbitrary scalar convolution preserves a nonreal-eigenvalue estimate.

Rationality makes all primitive roots of a given order have equal multiplicity. Outside `mu6`, the totient bound gives multiplicity at most one quarter except for order four. For order four, conjugate `i` and `−i` multiplicities are equal, and the lower bound on the trace of the square gives `m≤(1+c)e/4`. I checked that this trace comparison is an inequality on real parts for the remaining eigenvalues; the trace itself is real. Orders divisible by eight or an odd prime give the asserted stronger totient bounds.

The product-one and generation conditions force two marked scalar entries in each nontrivial quotient. In particular `mu_M/mu_(M/p)` detects full `p`-primary order, not just a weaker divisibility assertion. The quadratic conductor criterion is applied to the actual cyclotomic field and handles `M≡2 mod4` by the standard replacement without losing divisibility by the original `M`.

## D-ATT-03: actual source contradiction and ranges

Since `t≥2`, the actual coefficient degree is at least `a²≥8100`. The Euler identity excludes intermediate genus at least two; genus one has only six units of total moving rank and hence cannot give period rank nine. The remaining genus-zero family needs at least twelve genuine marks and total moving rank `2e+6`. The marked entries of the preceding lemma therefore produce the exact displayed inequalities. No original-base marks are silently substituted for these actual intermediate-cover marks.

I independently expanded all coefficient-times-`a²` formulas ATT.13–ATT.17. The non-Eisenstein ranges end at `n=39` for both modules. The conductor-eight exterior endpoint `n=40` is strictly excluded. For `h=p−1≥6`, the concavity endpoint comparison gives precisely UP through `10h−1` and EX through `10h`; the next integer has zero coefficient in the particular inequality, so no unproved extension is inferred. All eight field substitutions are correct.

The exact old ALT07 function is `beta(n,k)=k(n−1−k)/((n−1)(n−2))`. At `n=39,k=2` it is `36/703<1/10`, so both labels do satisfy that previous necessary bound. The new exclusion therefore strictly reduces the gate; it does not assert that an actual tuple existed before exclusion.

## Fresh primary source reading

I independently opened the author's full Milne *Class Field Theory*, version4.03, 6August2020, at `https://www.jmilne.org/math/CourseNotes/CFT.pdf`. I read the complete invoked passages, not a review or metadata summary:

- Chapter V, Example3.2, printed p157: cyclotomic Galois group and its explicit action.
- Remark3.8, printed p158, including the conductor divisibility/subfield statement.
- Examples3.10–3.11, printed p159, including the entire quadratic conductor calculation and its odd/even cases.

Retrieval references were `turn753288950view0`, `turn988107425view0`, `turn988107425view1`, and `turn988107425view2`. The general reciprocity/existence theory upstream is used as cited known mathematics, not claimed to have been independently reproved in this audit. This precisely matches the theorem's use of the source.

## Independent exact supplement

`independent_check.py` imports no author arithmetic or code. It constructs the actual letter permutations, follows actual unordered-pair orbits, and separately records orientation signs for the exterior square of the full permutation module. It then subtracts the letter module, adding the trivial line in the exterior case. This differs from the author's construction using symmetric and exterior sums of deleted-module eigenvalues.

The first execution passed at **2026-11-21T22:32:22.399542+00:00**, in **1.778241280997463 seconds**:

- All **11,224** partitions for `15≤n≤26`.
- **583,996** actual pair orbits and **777,780** spectral entries.
- Both exact minimum-support formulas and both minimum character bounds at every tested degree.
- **5,958** exact rational arithmetic cases, including all six odd-prime conductor ranges and their endpoints.
- The universal shifted endpoint polynomials, with positive coefficients for every `h≥6`.

The finite output is `independent_check.json`. It supplements the universal proof; it is not the premise for arbitrary degrees, arbitrary tensor counts, complete normalizer coverage, or period factorization.

## Attempts, limitations and disposition

There was no mathematical failure or failed computational assertion in the independent certificate. A preliminary read requested the nonexistent filename `check_alternating_two_tail.json`; the correct output is `alternating_two_tail_checked.json`, which was then read completely. This was a path lookup only and did not run a mathematical test.

No repair to the author's theorem or code was requested. The remaining larger degrees, other labels, and positive-source questions are left exactly as stated. This obstruction supplies no cycle and changes none of the separate conditional inputs.

Final report written: **2026-11-21T22:33:43.483765+00:00**.

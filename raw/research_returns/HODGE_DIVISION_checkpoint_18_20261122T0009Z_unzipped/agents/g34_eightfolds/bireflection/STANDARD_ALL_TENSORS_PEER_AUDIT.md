# HD-AST10–12 whole-proof audit

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. **Result: PASS.** I read the entire frozen proof, every author-checker line, the full final output and the retained initial-attempt record. No mathematical or wording repair was requested.

Frozen proof: `agents/imprimitive/standard_all_tensors/standard_all_tensors_section.tex`, SHA-256 `571d9d5475dbd1aadb7a68d85d39346f0bea7db6fd04d220ef881ad4e3a5a2a3`. Author checker SHA-256: `2786f160d17b4d690b6921c875ada848f6bcd139458450a18178046058644faa`. Its final actual execution was 2026-11-21 22:56:07.696790 UTC, 1.550464386 seconds.

## Relationship to shared work

This is a whole-proof check of the new standard-module application. It is **not** a claim of independent origin of all its ingredients. I authored the generic weighted-cycle lemma D-ATT08, and the sibling communicated the standard pair-selection derivation before freezing this text. The new standard two-factor inequality HD-AST07 was derived by root with a sibling contribution; I then independently audited that complete proof and reconstructed its spectra in the immediately preceding review. These dependencies and their authorships are preserved.

The current audit checks every inference in the new application, including the alternative error-bound proof, field scope, constant terms and actual quotient cover. My new supplementary program uses a different direct-trace/Fourier reconstruction and imports no author code or output. That implementation is independent as code, while the shared mathematical framework is explicitly acknowledged.

## Pair selection and the full constant

For a positive total permutation index, averaging over unordered factor pairs gives average pair index exactly `2I/t`; at least one pair attains or exceeds it and is nontrivial. The fully audited HD-AST07 estimate applies at every target eigenvalue on this pair. Tensoring with the other factors multiplies its support lower bound by `a^(t-2)`: every target multiplicity is bounded by the pair's largest multiplicity times the total remaining dimension. An arbitrary scalar only selects another target eigenspace.

Consequently the estimate retains the entire constant `n/2`, even if only one factor is active. This is not the weaker estimate obtained by dividing that constant by the factor count. If total index is zero, genuine inertia is a nonidentity scalar and moves all `a^t` dimensions; `(n-1)^2>=n/2` verifies the same formula. I checked both cases and the exact positivity assumption on the chosen pair.

## Weighted cycles and the error term

The printed change of basis correctly concentrates all weights into the actual cycle product, and its `t`th power applies that product to every tensor factor. In an eigenbasis, each rotational orbit of length `d` is a weighted cyclic matrix with nonzero weights and characteristic polynomial `Z^d-c`. Its eigenvalues are simple. If it contributes to a specified eigenvalue, all `d` words are counted by the full-return eigenvalue condition. Its defect in `t*m-N` is exactly `t-d`; an orbit not contributing has nonpositive defect.

The equality between the total short-orbit defect and `sum_{j=1}^{t-1} a^gcd(t,j)` follows by counting word/nonidentity-rotation fixed pairs. A length-`d` orbit contributes `d(t/d-1)=t-d`, so the necessary factor is present. Repeated eigenvalues do not identify distinct basis words. The last-index count bounds the full-return dimension by `a^(t-1)(a-nu(X))`, giving the stated support inequality for every scalar.

I checked the section's independent simplification of the universal error bound. The exact cases `t=3,4,5` are correct. For `t>=6`, every nonidentity rotation has at most `floor(t/2)` free positions. The inequality `t-1<=2a^(ceil(t/2)-2)` holds at the two parity bases and is preserved under increasing `t` by two because `t+1<=a(t-1)`. This proves the bound on its full domain `a>=4,t>=3`; no finite computation is used to extend that domain.

## Field, normalizer and branch-count reduction

The ordinary rational tensor-wreath image has trivial scalar intersection, so scalar-forgetting is an actual homomorphism. Its normalizer description retains every compatible outer automorphism and tensor-factor permutation. It is not a choice of representatives made separately at each branch.

Rationality gives `F subset Q(zeta_M)`. The original imaginary quadratic field is only required to lie in `F`. If every scalar value lay in `mu6`, that containment would force the Eisenstein field, contradicting the stated hypothesis. The generating product-one tuple therefore has at least two scalar values outside `mu6`. The all-power trace floor, cyclotomic multiplicities and fourth-root square-trace calculation give the claimed support at these two actual marks. No equality `F=K`, conductor-divisibility estimate, or scalar-invariant nonreal support assertion is inserted.

Every other genuine mark has support at least `e/a`; a factor-moving mark has support at least `(a-1)e/(2a)`. The weighted-word argument for the latter includes all cycle lengths and passes to the remaining factors by convolution. Three factor-moving entries would permit selection of the two scalar marks and a third distinct moving mark. The remaining nine marks give exactly `D>=2e+8e/a>2e+6`. Transitivity and product one then leave precisely two factor-moving entries. Their inverse permutations generate a transitive cyclic subgroup and hence are full `t`-cycles. No further use of their scalar orders is made.

## Actual connected quotient and final sum

The reviewed intermediate-cover factorization supplies the actual multiplicity-six Euler identity. Genus at least two is impossible at the given degree; genus one has at most six marks and cannot have period rank nine. Therefore the hypothetical rank-nine source has an actual connected genus-zero cover with at least twelve genuine inertia marks and total moving rank `2e+6`. This remains a necessary condition, not an existence argument from dimensions.

For a full tensor cycle, the weaker standard support bound `nu(Uh)>=ind(h)-1` is valid even when its cycle product is identity. The two resulting negative constant terms and the two exact short-orbit errors are both retained. Thus no identity-cycle scalar exception is overlooked.

The scalar-forgetting action is transitive on the `nt` letters. Taking the inverse image of an actual letter stabilizer gives a connected quotient of the given cover. A factor-fixing entry has index equal to the sum of its constituent indices. A full cycle contributes `n(t-1)+ind(h)`, because its length-`l` cycles lift to length `tl`. Riemann–Hurwitz therefore gives `N+H>=2n-2=2a`. Scalar entries have zero quotient index but remain among the coefficient-cover marks.

I recomputed the sum after multiplying by the positive factor `t/a^(t-2)`. Substitution of the Riemann–Hurwitz lower bound leaves

`2H + (5t-6)n + 2`.

Discarding the nonnegative `2H` is in the correct direction. The result is exactly the printed excess `a^(t-2)((5t-6)n+2)/t`. It is greater than `3n a^(t-2)>=630`, contradicting the allowed excess six. This checks all constants, every identity-product case and every tensor count in the stated range.

## Separate exact computation

Files: `audit_standard_all_tensors.py` and `audit_standard_all_tensors.json`. The program was written after the author code was read. It imports no sibling code, output or selected cases.

For weighted cycles it constructs the actual monomial operator on every tensor-basis vector and computes traces of all powers from those matrix entries. It then applies exact Fourier projection modulo the corresponding cyclotomic polynomial. This differs from the author's direct word-orbit eigenphase enumeration. The recovered multiplicities are nonnegative integers summing to the full dimension; all weighted support and rotation-error inequalities pass. For the new pair-selection claim it separately convolves actual standard permutation spectra in three and four factors, including zero-index scalar cases. It also recomputes the universal final coefficient and exact endpoints.

Actual successful execution: **2026-11-21 22:59:32.327062 UTC**, **0.206236488 seconds**. Counts:

- **20** direct-trace matrix cases on **22,840** tensor-basis words, with **364,008** matrix-power steps and **270** exact cyclotomic Fourier targets.
- **900** actual standard multi-factor spectral cases, comprising **45,591** spectral entries.
- **3,268** exact source endpoint cases and the universal symbolic expression with its explicit `2H` term.

The first independent execution passed; no failed assertion or repair occurred. This is a supplementary finite computation, not an infinite-range inference, a Hurwitz enumeration or a proof of geometric existence.

The author's retained earlier failed assertion is accurately described: an algebraically zero rational expression was left uncombined by `expand`; `cancel` resolves it. Its separate TeX control-character issue was repaired before freezing. I checked the final code, source and output rather than treating that earlier failed run as a pass. Neither issue changes the mathematics of the frozen proof.

## Sources and boundary

No new published classification is required by the application. The ordinary normalizer, scalar-field and actual-cover inputs are the reviewed D-AST01–03 and HD-AST04–09. The exact elementary cyclotomic input is Milne, *Class Field Theory* v4.03, Chapter V Example3.2, p.157; its complete passage was freshly read during the preceding scalar/two-tail source audits and is reused here with that chronology. I do not claim a new independent derivation of cyclotomic field theory or of the shared weighted-cycle lemma.

The theorem correctly retains the non-Eisenstein hypothesis for `t>=3`, while the separate two-factor theorem is valid over all original fields. It does not decide nontransitive tensor configurations, other ordinary labels or faithful spin modules. It provides no algebraic cycle. No TeX compilation is claimed. The complete new application passes without repair.

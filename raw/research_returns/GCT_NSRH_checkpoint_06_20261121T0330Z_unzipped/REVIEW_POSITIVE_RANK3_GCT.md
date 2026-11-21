# Independent full review of F43: the actual positive rank-three action

Reviewer: /root/gct_statements, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC.

Reviewed in full: agent_rank3_positive_action.md, initial SHA-256 5e2f13d6d075cb693c6187e8feae1360aecbc943152666db8a9de320a7cb0763. I then directly read the sole added explicit-word complexity paragraph in section 6 and checked the final file at SHA-256 1893d3eeccf8bcabd5e066d55012cf88cf53c676fb776bd8468ea243bd9cde54.

**Result: PASS for the final report. No mathematical blocker or required correction.**

Verification types: complete proof reading, independent algebraic reconstruction, and direct primary-source inspection of the ordinary tensor bar/coproduct, the known rank-three construction, and the VIII globalization conditions. The previously certified F21 right-action changes are used as checked inputs; this review does not claim a newly executed symbolic script. No formal proof-kernel verification is claimed.

## 1. The actual ordinary left action

I independently derived the coproduct coefficients from IV equation (29). On a tensor word, F changes a 1 with the product of K-weights to its left, and E changes a 2 with inverse K-weights to its right. Thus

\[
F(111)=211+v\,121+v^2\,112=b_1.
\]

Direct collection gives F b1 = delta b2 and F b2 = h b3, with h=v^2+1+v^{-2}; the inverse E formulas follow by the same calculation. In particular the endpoint normalization is genuinely F b2 = h b3.

For the two highest-weight standard vectors, E u_{+,1}=E u_{+,2}=0. Direct computation gives

\[
F u_{+,1}=-v^{-1}122-v^{-2}212+\delta221=u_{-,1},
\]
\[
F u_{+,2}=-(1+v^{-2})122+v212+221=u_{-,2}.
\]

Both second F actions vanish. The E reverse actions equal the corresponding u_+ vectors, either by substitution or the weight-one quantum commutator. The K eigenvalues are v^{3-2j} and v^{\pm1}. This proves all entries of (P6) on the eight-dimensional module, and their tensor-factor use in the full module. The distinction between the sl2 highest-weight subscript W1 and the polynomial GL2 representation (2,1), including its determinant twist, is correct and explicitly stated.

## 2. The actual source bar

I read IV Figure 1 in the supplied TeX, including all six middle-weight canonical vectors, and its surrounding section 6.2 definition and Theorem 6.4. The three positive-weight vectors are exactly

\[
c_{112}=112,\quad c_{121}=121-v^{-1}112,\quad
c_{211}=211-v^{-1}121.
\]

Multiplying the matrix in (P7) by these row vectors gives exactly the three vectors in (P3)--(P4): h-delta/v=v^2, delta-v^{-1}=v, and 1-delta/v=-v^{-2}. Its coefficients h, delta, 1 are fixed by the actual scalar bar. The second weight space uses the corresponding three source vectors with the stated row interchange. The endpoint vectors are canonical. Thus all eight vectors are fixed by the actual quasi-R tensor bar; no transported involution was substituted.

Under regrouping for the product quantum group, the V and W quasi-R factors act on separate factors and commute, so the full tensor bar is their product. Every coefficient of B4 is bar invariant. This proves actual bar invariance of the final 64 vectors. It is correctly distinguished from identifying VIII's different prescribed global bases.

The primary PDF locators were also independently recovered in this session: IV (28)--(29), printed page 22; Figure 1, page 9; Theorem 6.4, page 34; and Example 19.2, pages 132--133. Primary URL: https://arxiv.org/pdf/cs/0703110 . Relevant fresh references: turn946773146view0, turn450672076view2, turn946773146view1.

## 3. Determinant, actual decomposition, and full commutant

The two three-dimensional ordinary changes each have determinant h^2. Hence the eight-dimensional change has determinant plus or minus h^4. Tensoring that change with itself contributes h^{64}. The standard-standard multiplicity has dimension four, so exactly four copies of B4 are used, contributing (8h^2)^4=2^{12}h^8. The final determinant is therefore exactly plus or minus 2^{12}h^{72}. All entries are Laurent integral, and localizing only at 2h makes the change invertible. No delta, D-2, or collision-root difference is used in this argument.

The decomposition (P10) correctly retains the actual left actions on the multiplicity factors and the actual right actions on the Specht factors. The multiplicity ranks are 20,4,16,4. Changing only U tensor U by B4 cannot change the ordinary left matrices, because the left action is the identity on that factor. Thus the claimed simultaneous positivity is an actual bimodule statement over the stated ring, not a character comparison.

For the commutant, the four generic right simple types are distinct. The supplied central scalars 0, D(D-1), and 4(D-1) separate the matrix sectors over the fraction field, and P1 separates the two scalar sectors. A cross homomorphism over the domain S would become zero over its fraction field and is therefore zero. I checked the direct two-by-two commutation calculation: commutation with P1 forces the upper off-diagonal entry to vanish; commutation with P2 forces the lower one to vanish; their remaining equations force equal diagonal entries because a is nonzero. Thus each standard block has endomorphism ring exactly S, without requiring a or D to be units. This gives precisely the displayed product of four matrix algebras. Its multiplicity matrix units act with entries 0 and 1 on the chosen actual basis and commute with its bar.

The report does not silently identify this integral commutant with every integral form of the dual coordinate algebra or with an algebra across all tensor degrees.

## 4. All words and the finite graded kernels

The rank-one factorization P_i=u_i e_i^T is compatible with the right-row convention. Each internal contraction is D for a repeated letter and a for a switch. This gives the complete product (P11). Closing the word introduces the last contraction, giving D^{L-c}a^c. A cyclic binary word has even switch count c=2s, so the formula becomes D^{L-2s}a^{2s}. On N(delta), a^{2s}=D^s. Adding the actual scalar and multiplicity factors gives (P12) exactly. This includes constant-letter words and alternating words with their stated specializations.

The directed-edge interpretation is ordinary multiplication of the actual nonnegative matrices. Giving parallel degree-zero edges distinct labels preserves their multiplicities. The graded kernel functors yield the stated action on the graded Grothendieck group; composition corresponds to concatenating paths. For left operators recorded by rows, composition must be read with that row convention, as the report explicitly stipulates. The quadratic relation lifts using the canonical tensor symmetry and the reset property. The report correctly asserts general relations only on K0 and does not infer a fully coherent categorical presentation.

The arithmetic grading qualification is correct: the closed right-word trace formula uses only even powers of v, whereas the N(delta) entries include odd powers. The v=q^{n/2} interpretation is an integer Tate rule for those closed traces but requires additional weight-one data at the entry level. The report includes this distinction.

## 5. The explicit summand obstruction

At v=1, both N(delta) and N(D-2) have D=4 and a=2, so the actual matrices of both generators coincide on those two blocks. Every word and regular coefficient combination therefore has identical specialized matrices on them. This remains true over the stated localization because its denominators are nonzero at v=1.

The semisimple matrix-functor category contains a direct summand of the P1 kernel consisting of one degree-zero loop on only the first state of N(delta). Its K0 action is the branch-supported E11 and is zero on the other block. That violates the preceding equality after specialization. Thus closing under arbitrary summands introduces an operator outside the actual regular order. The faithful six-dimensional reduction removes the possible distraction of multiplicity copies, and the argument remains valid there. This is a rigorous limitation on this particular summand-closed realization, not a universal impossibility result for all categorical models.

## 6. Factor swap and complementary generators

I checked the B4 rows under the interchange of the middle two tensor coordinates. Only the second row is antisymmetric. Consequently the actual factor swap on the epsilon-minus multiplicity space is minus flip on W1 tensor W1. Its trace is minus the dimension of W1, namely -2. This independently matches the sign extension in IV sections 13.1--13.3, whose full source context was read. A nonnegative Laurent matrix would have nonnegative specialized trace. The stronger simultaneous obstruction with the commutant projector e_minus follows because the product of two such nonnegative matrices remains nonnegative, while Tr(e_minus tau)=-2.

For Q_i=DI-P_i, changing the sign of the second vector in every rank-two block makes both off-diagonal negative entries positive. It does not alter the ordinary left matrices or the bar. Conversely simultaneous coefficientwise positivity of every P_i and Q_i forces all off-diagonal entries of P_i to vanish in any proposed common basis. They would commute, contradicting the explicit nonzero commutator entry Da. The scope is precisely simultaneous positivity of the complementary conventions.

## 7. The unit-containing center basis and lattice ambiguity

For a basis {1,b} of the rank-two center, the relation b^2=a+cb gives characteristic polynomial T^2-cT-a. The special fiber is dual numbers, so its discriminant vanishes: c(1)^2+4a(1)=0. If both coefficients are nonnegative Laurent polynomials, this forces a(1)=c(1)=0 and hence a=c=0 identically. The generic algebra would contain a nonzero square-zero basis element, contradicting its split reduced form. This proves exactly the stated strict center-basis obstruction; it does not exclude VIII's signed factorizations.

The final change determinant is not a unit in the original global Laurent ring, and b1 tensor b0 has a genuine v^2 coefficient, so it lies outside the ordinary crystal lattice at infinity. These two explicit failures are correctly restricted to the ordinary lattices. IV's warning after Conjecture 19.1 says its sought lattices differ from the ordinary ones.

Scaling a complete isotypic sector by h^r preserves every displayed left and right action matrix, its full commutant matrix units, and the bar over S, while changing the global span and infinity behavior. Thus the proved local properties do not select a unique globalization. I read the VIII source contexts for the prescribed dual lattices and degree-minimizing globalization (supplied lines 690--850 and 1380--1475); the report accurately states that these are additional substantive conditions. Its historical acknowledgment of IV Example 19.2 is necessary and present.

## 8. Final explicit-word complexity corollary

I independently checked the appended corollary from the tables. Every selected right-generator row has at most four outgoing labeled edges; each E/F row has at most three; each K^{\pm1} or commutant matrix-unit row has at most one. Each edge degree has absolute value at most three. Hence an explicitly written word of length L has at most 4^L paths per starting state and at most 64*4^L closed paths in total. Degrees lie in [-3L,3L].

Selecting an edge label at each step gives an O(L)-bit unambiguous witness once source/target and, if relevant, the starting trace state are specified. The usual dynamic program on the 64 states and that degree interval has polynomial bit complexity, because all intermediate counts have O(L) bits. The final added paragraph states the proper scope: explicitly written words at fixed tower rank three, with no succinct binary/run-length power or general Kronecker/PH1 claim. Its exact wording matches the independently checked consequence.

## 9. Review scope

The complete final report passes. The constructive part is stronger than trace positivity: it gives actual simultaneous left/right actions, the actual bar, and the full localized commutant. Its limitations are also proved rather than merely asserted. A generated final fragment should receive a separate full text match, with its own hash recorded.

## 10. Complete final-fragment match

I subsequently read the entire generated finding_F43.tex directly, including all post-proof obstructions, the explicit left row-matrix reversal convention, and the separate dictionary paragraph. Reviewed SHA-256: e9b810cd54934edbb0a7c8d7b31b0763de041021b56595fba6d3a4894a97fcb2. **Final-text match: PASS.** It preserves all checked proofs and the explicit-word complexity scope. The added statement that the faithful rank-six parameter module need not remain faithful at its special fiber is correct. The final archival/framework locators are previously audited inputs from the parent/dictionary agent; this match does not claim a new archival-source audit. No new mathematical blocker was introduced.

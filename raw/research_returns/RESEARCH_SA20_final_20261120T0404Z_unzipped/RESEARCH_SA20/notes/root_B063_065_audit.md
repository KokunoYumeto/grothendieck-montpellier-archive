# Independent root audit of B.063–B.065

Date: 19 November 2026, 15:46 UTC. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

We independently read the complete pending proofs in
`agents/tensor_and_finite/notes/pending_B063_065.tex` and checked the following steps.

## B.063: arbitrary extensions of a valuation domain

For a nonprincipal maximal ideal, the determinant on `0,a,a²,...,a^d` has value
`d(d+1)(d+2)v(a)/6`. The absence of a least positive value gives determinants
dividing any prescribed nonzero element of the maximal ideal. Cramer's rule
therefore works even when the coefficient extension has torsion. The coefficient
ring splits as `V ⊕ Ann_S(m)` as a module: its image in the localized coefficient
ring is forced into `V`, and the residual products by `m` vanish in the domain
`V`. The displayed null-polynomial summand follows by monic division over the
residue field. The two cross terms of the antisymmetric tensor lie in different
direct summands; monicity proves nonvanishing without a flatness assumption.

For a principal maximal ideal, the argument permits arbitrary rank. Elements
outside `P=intersection π^n V` have a finite integral value in units of `v(π)`;
thus `V/P` is a DVR, while `V/π^nV` has exactly `q^n` elements. The coefficient
ring is the π-power saturation. If π is regular in it, it embeds in `V[1/π]`
and is either the base or that localization. We checked `PC=P` directly by
writing `p=π^(N+j)b_j`, so `pc=π^j b_j a` for every `j`.

The nonflat quotient step is valid: a reduced tensor-kernel element lifts to a
tensor whose polynomial image has coefficients in `P`; subtracting its ordinary
monomial tensor lift kills that image and changes nothing after reduction. This
is an explicit lifting argument and does not assert that tensor injectivity
survives arbitrary nonflat base change. Existence also descends by the proved
surjectivity on integer-valued polynomials. The already audited DVR theorem
B.058 then gives the necessary absence of π-torsion. All multivariable
coefficients lie in the same saturation by rectangular grids or distinct-power
substitution. We found no remaining gap in B.063.

## B.064: universal coefficient ring

The ideals of Vandermonde determinants decrease. The Vandermonde polynomial on
`0,1,X,...,X^(d−1)` is monic over every commutative ring: each nonconstant
difference is monic, and the only constant difference is one. Every value lies
in `D_d`, so every element of `(R:_S D_d)` occurs as a leading coefficient.
Conversely Cramer's rule puts every coefficient of a degree-d integer-valued
polynomial there. Equalizing degrees proves addition, and multiplying proves
closure under multiplication, including zero-divisor bases. Distinct-power
substitution preserves each coefficient in a multivariable polynomial.

Under tensor injectivity, the antisymmetric monic tensor vanishes. Applying the
fixed top-degree coefficient functional in each factor proves
`c⊗1=1⊗c` in `C⊗_R C`. These identities give an actual inverse to multiplication,
so the ring-epimorphism conclusion is justified. This is a necessary obstruction,
not a claimed sufficient general classification.

## B.065: absolutely flat bases

An injective ring epimorphism from an absolutely flat ring is an isomorphism.
Indeed `C/R` is flat, so every module injects into its tensor with `C`; taking
that module to be `C/R`, whose tensor with `C` is zero by the epimorphism
condition, forces `C/R=0`. Thus the coefficient and annihilator criteria are
equivalent to the full standard polynomial case. For Boolean rings the
three-node determinants vanish in every prime quotient, and reducedness gives
`D_2=0`; hence the criterion reduces to `S=R`.

We independently opened and read the original Stacks proofs on 19 November:

- <https://stacks.math.columbia.edu/tag/092F>, Lemma 15.106.5, equivalence of
  absolute flatness, reduced dimension zero, and field localizations.
- <https://stacks.math.columbia.edu/tag/00HD>, Lemma 10.39.5, the finitely
  generated ideal criterion for flatness, including its proof.

Root retrieval references: `turn718567155view0` and `turn718567155view1`.

Outcome: PASS for B.063–B.065, with their stated scopes. These statements enlarge
the proved non-Noetherian classes; they do not finish the arbitrary-base
classification or advance the separate main concordance gate.

## Additional audit: B.066, 15:57 UTC

We independently checked the complete arbitrary-ring faithful-evaluation criterion. A null polynomial of degree d has every coefficient annihilated by every (d+1)-node Vandermonde determinant, by the adjugate identity. Conversely a nonzero element annihilating D_d multiplies the monic P_d into a nonzero null polynomial. Constant polynomials are handled by evaluation at zero. This proves the stated ideal criterion without cancellation or flatness. Outcome: PASS.

## Additional audit: B.067, 15:59 UTC

We independently read the entire forest construction and certificate source. The squarefree transition sends disjoint old monomials to disjoint new monomial supports, preserving multiplication and injectivity. Infinite fresh root components give (R:N^k)=R for everyk by a tensor product of nonzero vectors over F2, avoiding cancellation in a ring with zero divisors. The three-step epic shuffle uses precisely the two degree-zero base elements and x_v. Nilpotent increments yield every mixed first derivative at the binary cube; products of those increments generate N^k. Hermite interpolation therefore proves the full multivariable coefficient decomposition, and the epic coefficient tensor identifies each summand. Nonflatness follows from the local faithful-flat criterion and the faithfully-flat epimorphism theorem, both opened originally at Stacks00HQ and04VU;06RH was opened only for the source analogy. The lie agent independently re-proved every step and reran the certificate as well. Root rerun details are in logs/root_B_forest_run.json. Outcome: PASS. This refutes necessity of flatness as a proposed classification route; it does not classify every non-Noetherian inclusion.

## B.068 independent root audit — 2026-11-19T16:17:18.937690+00:00

PASS: if every Vandermonde ideal contains a regular element and has trivial inverse ideal in the total quotient ring, rationalization splits the integer-valued module into ordinary polynomials and null polynomials. A nonzero null coefficient times the monic Vandermonde polynomial gives a cross-kernel in two distinct split tensor summands. This proves positivity exactly when evaluation is faithful. For A[Z], regular determinants from A put all coefficients in A[1/v][Z]; separated degree blocks after evaluating at Z^N force them back into A. Taking A[W] supplies a monic regular Vandermonde determinant for arbitrary nonzero A, proving the A[Z,W] case without reducedness or finiteness. This is a scope enlargement, not closure of the remaining original B.2(c) structural classification row.

## B.070 binomial bases, arbitrary coefficient extensions

Root read the complete proof and passed it. The finite Newton test is an integral monomial identity, so no cancellation in the coefficient ring is used. Localization of a binomial base is proved by induction on the degree of s^dG(X)-G(sX). At a characteristic-p local point, x^p=x in A/pA forces the maximal ideal to be pA and the residue field to be F_p. The coefficient saturation embeds in A[1/p] when p is regular upstairs; every nonintegral fraction then supplies p^{-1}. For necessity, the quotient by P=intersection p^jA is proved to be a DVR using regularity of p and least valuations. P is an ideal of the effective coefficient ring, and the explicit ordinary-monomial subtraction lifts a reduced tensor kernel without assuming flatness of A/P. A nonzero p-torsion element survives this quotient, contradicting the checked valuation criterion. All localization and global support arguments are valid for arbitrary modules.

## B.071 and B.072 further local structural classifications

B.071 passes. A nonzero-divisor is not assumed: if an element has finite pi-adic order then it is a power of pi times a unit, which proves Ann(pi) lies in the intersection P when pi is not nilpotent. This supplies P=pi P and regularity modulo P without illegitimate cancellation. For the tensor step, start with hF tensor G, write h=pi^N h-prime with h-prime in P and pi^N G ordinary. Balancing and expanding expresses the tensor as the ordinary monomial tensor of its polynomial image, since PC=P. Iterating proves P times every tensor power is exactly the ordinary P-coefficient polynomial module. This verifies both directions of reduction, including ascent without flatness.

B.072 passes. The image of Frobenius is a coefficient field because the kernel is exactly the maximal ideal and the residue field is finite. The Hermite remainder basis separates every residue point and jet. Scalar interpolation and polarization with j! invertible for j<p yield whole ideal colons, not merely tests on pure powers. Split null-polynomial and first-jet summands force the two claimed multiplication maps to be injective. The first-jet coefficient ring has maximal-ideal product exactly m, so its epimorphic residue algebra is the same field. Iterated colons then force every jet coefficient into R, including multivariable sums of jet orders that may exceed p. The explicit monic basis identifies all tensor maps. No nilpotence of the entire maximal ideal is used.

## B.073 and B.074

Both proofs pass. For B.073, extension of the nilradical remains a nil ideal, so contraction gives an injective quotient epimorphism. Absolute flatness gives B=R+NB. Recursive finite expansions have a finitely branching dependency tree; T-nilpotence precludes an infinite path and therefore makes each expansion finite. For B.074, the local Vandermonde ideal contains powers of a regular sequence. Only the first element must be regular in the entire ring; regularity of the second modulo powers of the first is proved by induction. Rationalization maps every effective coefficient back into A, defining a ring retraction. Its composite with inclusion equals the identity by the epimorphism property. The proof uses the valid one-way localization of effective coefficients and does not assert general localization of Omega.

## B.075 — arbitrary coefficient torsion over every infinite-residue conductor cusp

Full proof PASS. Determinant ideals and powers of m are cofinal in both directions. The rational image of the epic effective coefficient ring is R or K; the former gives a retraction, and the latter gives an actual idempotent e=(sc)^N using s^N(sc-1)=0. Its complement is killed by a fixed power of m, so the field quotient and finite iteration prove C=K times R/I without a finiteness assumption.

The basis V[X,U], U=(X^q-X)/t^a, is forced by reduction to the product over b in F_q of l[U] and evaluation on the infinite residue field l. Every layer below t^a is checked in the Int(R,K) decomposition. The antisymmetric coefficient tensor is detected in l tensor_k l. For proper I, t^(b+a)V is contained in I, and the first nonconstant leading-residue level d lies between b and b+a. Precomposition with b0+t^a U^N gives arbitrarily high leading U-degree. At d<b+a the mH term contributes nothing; at d=b+a it contributes only constants. Terms from mR[X] have the stated finite degree bound, even allowing cancellation, since the mH term already has valuation at least d. The chosen F therefore survives modulo mE. The null monic P^n in the other idempotent component also survives. Their pure tensor is nonzero after reduction to the residue field and has zero polynomial image. Every proper quotient case is excluded.

The result covers all a>=1, finite k and infinite l with arbitrary R-torsion in S. It closes the prior explicit family but does not settle the arbitrary-base parent task.

## B.076 — principal conductors over arbitrary valuation domains

Full independent proof audit PASS. The determinant ideals are cofinal with powers of xV without any rank or discreteness assumption. The rational epimorphic image lies in V[1/x]. If all its valuations are bounded below by -v(x), the conductor contains (xV)^2 and the quotient epimorphism over a local ring with nilpotent maximal ideal is an isomorphism. Otherwise an element of value less than -v(x) supplies V and x^{-1}. The idempotent split is therefore V[1/x] times R/I, not an unjustified fraction-field split.

The basis argument divides by an actually attained minimum among finitely many polynomial coefficients; it does not take a minimum over an ideal. Interpolation on F_q removes the U-degree-zero summand. Infinite residue-field evaluation forces the remaining coefficients into xV. For the proper quotient case, the least positive integer n bounding the value of one nonconstant H_0 member exists because x^M U is present. Precomposition with b_0+xU^N preserves that value and increases its residue degree beyond n. The ordinary term has coefficient value at least (j+1)v(x), so a balanced H_0 summand has value at most (n-1)v(x). For n=1 this contradicts positivity; for n>1 it contradicts minimality. Thus H is not contained in mE and the two idempotent-component polynomials yield a nonzero pure tensor with zero image.

The author corrected mixed uses of Int(R,V), Int(R,K), and Int(R,I) in both B.075 and B.076 to explicitly typed polynomial-value sets and Omega. The statement covers arbitrary coefficient torsion and arbitrary-rank, non-discrete, noncomplete valuation domains with principal V-conductor. It does not cover a nonprincipal irrational conductor cut.

## B.077 — arbitrary rank-one conductor cuts

Independent root proof audit PASS. For a positive real cut alpha, determinant ideals are cofinal with powers of J by an Archimedean valuation bound; the alpha=0 case is separately covered by the proved power-generation criterion. The epic rational image is R or K, and the actual coefficient ring splits as K times R/I with a power of J in I when it is nontrivial.

In the monic X^i(X^q-X)^j basis, evaluation at every b+c z gives exactly the coefficient ideal (J:J^j). The zero-residue-value case uses that a nonconstant polynomial on the infinite residue field cannot take only finitely many values. The case where the minimum positive value lies outside J is excluded by an evaluation realizing that minimum. This includes open and irrational cuts.

For H_0 the weighted values have positive real infimum lambda. A polynomial chosen within alpha/4 of that infimum has a translate G(b_0+Y) with the same Gauss value: at a minimal-weight P-index, all smaller indices contribute strictly greater weight to the selected Y coefficient. The substitution b_0+c_N P^N increases all indices beyond N while increasing the weight by less than alpha/4. Its value-set containment follows separately for attained and open cuts. An assumed expression in J E then supplies an H_0 summand of weight below lambda, a contradiction. Both pure-tensor factors survive residue reduction, so the zero polynomial image gives a true tensor kernel. No minimum over the ideal or over H_0 is assumed.

The theorem closes the stated irrational Hahn cut but leaves arbitrary non-Noetherian bases unclassified.

## B.078 — all valuation conductor ideals, arbitrary rank

Independent root proof audit PASS,19November2026,17:46UTC, during the checkpoint09 source freeze. The complete draft is `agents/tensor_and_finite/notes/pending_B078.tex`. We opened Halter–Koch's primary author PDF, *Clifford semigroups of ideals in monoids and domains*, Lemmas5.1–5.3 and Theorem5.4(1), pp8–9, https://imsc.uni-graz.at/halterko/Clifford.pdf (root references turn426172885view0, turn866932545view0/1). We independently verified the draft's elementary proof of J^N(J:J^N)=J: put E=(J:J); the principal E-ideal case is direct, while the nonprincipal case gives J m_E=J and J(E:J)=m_E. Iteration proves the required equality of actual ideals without a rank or infimum hypothesis.

If J is idempotent, finite product expressions and the least valuation among their factors prove the R-ideal power-generation hypothesis of B069. Otherwise c in J outside J² gives 2v(y)>v(c) for every nonzero y in J. This yields J^(2h+1) contained in c^hJ, and hence determinant/power cofinality in the actual ordered value group. The rational epic image in V[1/c] is R or all of V[1/c]; the bounded case uses the common ideal J³L and nilpotent-maximal-ideal quotient, and the unbounded case first forces V into L and then c^{-1}. The coefficient-ring idempotent splitting is valid for arbitrary base torsion.

The monic X^i P^j basis, with P=X^q-X, has coefficient ideals (J:J^j). The proof evaluates all b+yZ and uses the infinite residue field to exclude negative, zero or positive-but-outside-J minimum coefficient values. Products in a valuation ideal are generated by pure powers of their least-valued factors, so the test on every y suffices.

The ideal norm nu_J(F) equals the sum of its translated coefficient ideals g_bh J^h. Substitutions b+lambda P^N, lambda in(J:J^N), preserve the aggregate ideal norm exactly, by the opened Clifford identity, while putting every nonzero P-index at least N. Under the hypothetical H contained in JE0, high-index projection gives K0 contained in J^(N+1)+JK0. Choosing N=M with J^M contained in K0 forces K0=JK0, then J^M=J^(M+1). Finite product valuations imply J=J², contrary to the chosen case. This does not use Nakayama for an infinitely generated module. The final two orthogonal product-component polynomials both survive modJ, so their pure tensor is nonzero and has zero polynomial image.

The theorem closes all valuation-conductor pullbacks stated in its hypotheses, including the previously listed lexicographic irrational cut. It does not classify all arbitrary non-Noetherian bases. Promotion follows the checkpoint freeze; the audit itself is complete.

### B.078: arbitrary characteristic and no coefficient-field section

The generalized proof was independently audited at 17:55 UTC and passed. We now assume only a unital inclusion R in a valuation domain V with infinite residue field, containing a nonzero proper V-ideal J such that R/J is a finite field. The field map R/J to V/m_V is injective, so R intersect m_V equals J. For r outside J choose a in R with ra=1+j; the inverse of 1+j lies in 1+J, proving that R is local with maximal ideal J.

Choose arbitrary representatives B in R for R/J and put P(X)=product over b in B of (X-b). Distinct representative differences are units, P(R) lies in J, and every P'(b) is a unit. These are exactly the properties used by the earlier proof with X^q-X; no embedded finite field is required. After substitution X=b+yZ, reduction of P(b+yZ)/y gives P'(b)Z. The representative Vandermonde matrix remains invertible over the residue field. The coefficient-ideal calculation, translated Gauss norm, substitutions b+lambda P^N, and high-index projection therefore work in arbitrary characteristic, including mixed characteristic. All subsequent uses of the Clifford ideal identity and nonflat product decomposition remain valid. The idempotent-J case uses the earlier power-generation theorem in its stated arbitrary-characteristic form. Outcome: PASS for the generalized statement now promoted as B.078.

## B.079 — necessary coefficient base change and failure of monic saturation

Independent proof audit, 19 November 2026, 17:55 UTC: PASS. Let C be the effective coefficient ring and N the finite coefficient vectors over C/R whose polynomial functions vanish on R. The exact sequence 0 to R[X] to Omega to N to 0 is obtained coefficientwise. The map C[X] to C tensor_R Omega is a section of coefficient multiplication, so multiplication is an isomorphism exactly when C tensor_R N vanishes. If theta_2 is injective, choose a common monic witness H with c_i H in Omega for a putative kernel sum c_i tensor F_i. Injectivity kills sum c_i H tensor F_i; extraction of the leading coefficient in its first factor kills the original kernel. This uses no flatness.

The cusp R=k+t l[[t]], C=l((t)), P=X^q-X, and beta in l outside k gives an explicit nonzero tensor z=beta P tensor P minus P tensor beta P. Projection onto the P-coefficient modulo the maximal ideal detects beta tensor 1 minus 1 tensor beta in l tensor_k l, which is nonzero. Polynomial multiplication kills z. Yet P^2/t belongs to Omega and t beta belongs to R, so balancing shows P(X)z=0. Here C is flat and epic and the coefficient base-change map is an isomorphism. Thus neither flat epic coefficient base change nor localization at monic polynomials detects all tensor kernels. This counterexample is infinite; no finite exhaustive certificate is represented as its proof. B.079 gives a necessary condition and a refutation of a proposed sufficiency route, not a solution of the remaining original arbitrary-ring task.


## B.080 — flat effective coefficient ring: full Tor calculation

Independent root audit, 19 November 2026, 18:01 UTC: PASS. We read the entire draft and opened the primary Stacks Section10.75, Lemmas10.75.2,10.75.5,10.75.8, at https://stacks.math.columbia.edu/tag/00LY and https://stacks.math.columbia.edu/tag/00M5 (root refs turn244668017view1/2). Let E be the explicit module of finite polynomial value functions R to C/R. The evaluation sequence 0 to Omega to C[X] to E to0 is exact, and epicness gives C tensor E=0. Flatness of C then proves C[X] tensor Omega=C[X,Y]. The two long exact Tor sequences identify the binary tensor kernel with Tor_2(E,E) and its cokernel with Tor_1(E,E). The displayed connecting map sends a coefficient array through its actual value functions and the fixed boundary isomorphism; it does not assume an unknown integer-valued tensor decomposition. The binomial Hankel and diagonal arrays therefore give exact coaddition and comultiplication existence obstructions. Restricting to the kernel of evaluation on R² yields the asserted separate exact sequence with ker(lambda). Binary uniqueness/existence is carefully distinguished from full bivariate polynomial compositeness and higher tensor identities. The proof makes no finite-generation or terminating-algorithm assertion. This is a complete result under flat effective C, not a closure of the original arbitrary nonflat task.


## B.081 — directed self-injective approximations and the nil test base

Independent full root audit PASS, recorded 2026-11-19T18:04:19.727408+00:00. For an epic inclusion R in C, every equality c tensor1=1 tensor c uses finitely many balancing coefficients. If R is a directed union of self-injective unital subrings, the equality descends to one such subring. Its inclusion in C splits as a module, and applying the retraction in one tensor factor forces c into the subring. This proves the rigidity assertion without flat transition maps. For a local nil maximal ideal, mC is nil and proper; the nonzero field epimorphism R/m to C/mC is an isomorphism. Thus C=R+mC, and an ideal I killed by m^N satisfies IC=I after iteration. The quotient R/I to C/I is therefore an injective epimorphism, so the assumed quotient rigidity lifts.

The finite truncated polynomial algebras have the stated perfect complementary-monomial pairing, which identifies each with its vector-space dual as a module. Exactness of vector-space duality proves self-injectivity for arbitrary modules. Their directed union is the quotient of the explicit test ring by the nonzero socle ideal F2z. The maximal ideal annihilates this ideal. The monomial basis verifies nilpotence of each element, unbounded nilpotence orders, non-Noetherianity from m/m², and failure of T-nilpotence from all successive products x1...xn. All hypotheses are checked. The resulting arbitrary-extension criterion follows from the previously audited coefficient-ring epic necessity and gives all multivariable tensor isomorphisms in positive cases. The base is infinite; no finite truncation is passed off as proof of its global properties. The original arbitrary-ring parent task remains unfinished.

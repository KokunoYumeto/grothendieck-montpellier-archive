# VIII printed multiplication constants — bounded integrality audit

Author: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

## 1. Result and exact scope

**No denominator or fractional-multiplicity counterexample was found among the actual raw multiplication formulas printed in VIII Figure2, p34.** All thirteen labeled constants there are covered by six distinct formulas, each in Z[q,q^{-1}].

I also checked all twelve printed tables in Figures24--35, pp58--65: their 542 numeric entries are signed integers. These tables are not an unnormalized raw multiplication table. The text explicitly rescales constants by powers of a polynomial, strips a maximal vanishing factor to form their vectors, and sometimes displays a field trace or norm instead of the constant. Consequently the table check does **not** establish integrality or even Laurentness of every underlying raw constant.

This is a bounded exact-source audit, not a general integrality theorem for the designated canonical basis, a claim about unpublished computed constants, or a refutation of the conjectures. It supplies no new actual denominator obstruction to mixed point-complex realization.

## 2. Sources and the rational-coefficient convention

The supplied source is sources/LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex, SHA256 6debec617252dfd0777c42828a9e34ba1d64398c9dbfa2ebacc4b77892a954db. Its primary PDF is arXiv0709.0751v2, local primary_sources/GCT_VIII_0709_0751v2.pdf, SHA256 504345a1ffd36900ba6166df17cb595f335ba7f15be1fe2739318fa0b7fb80be. Numbering below was matched to the extracted primary PDF, not inferred from the TeX section counter.

Conjecture3.4, Section3.5, p24, TeX label cposkroneckerright, concerns raw multiplication/comultiplication constants and ambient canonical-expansion coefficients of E(r), and the same for Eopp(r). It permits a sign times (q^{1/2}-q^{-1/2})^a times a bar-invariant positive unimodal Laurent polynomial. The definition of positive in the earlier Conjecture2.7 context, Section2.4.2, p15, TeX label cposkroneckerleft and following paragraph, means nonnegative **rational** coefficients. No integral multiplicity statement is included there.

The two roles remain different: being a coefficient in the expansion of a basis element in an ambient basis is not being a multiplication constant in the designated basis. Section5.1.2, p29, defines the latter as c(b,b';b'') in the expansion of bb'. Figure2 is expressly their table, label fmultkron2.

I read the complete relevant contexts, not only occurrences of the word denominator: the conjectures and their definitions, Section5's vector convention, Section5.1 and its full Figure2, the limited Section5.2 computation, Section5.3's algebraic coefficient field and basis definitions, its balance example, and Section5.4.1's normalization and all Figure24--35 tables.

## 3. Every raw formula in Figure2

The six distinct displayed formulas are the following. The vector in the right column lists coefficients from the lowest exponent to the highest, retaining internal zeros.

| Audit name | Raw formula in q | Exponent range | Laurent coefficients |
|---|---|---|---|
| a | -(1+q)^2(q^2+q+1)(q-1)^2/q^3 | -3 through3 | -1,-1,1,2,1,-1,-1 |
| b | -(q^2+q+1)(q-1)^2/q^2 | -2 through2 | -1,1,0,1,-1 |
| c | (1+q)^2/q | -1 through1 | 1,2,1 |
| d | (1+q)^2(6q+5q^2+5)/q^2 | -2 through2 | 5,16,22,16,5 |
| e | (1+q^2)^2(q^2+q+1)(q-1)^2/q^4 | -4 through4 | 1,-1,2,-3,2,-3,2,-1,1 |
| f | (1+q)^2(2q^2+q+1)(q^2+q+2)/q^3 | -3 through3 | 2,7,14,18,14,7,2 |

Formula a appears three times among the labels, b once, c four times, d twice, e once and f twice: thirteen labeled entries. I have not silently repaired the first row's printed gamma-label irregularity; the displayed formula and the count of c(...) entries are unambiguous and are all that the audit uses.

The source's q-power denominators specify Laurent exponents. They are not fractional spectral multiplicities. Exact expansion produces only integer coefficients, including the negative ones already relevant to the separate purity tests.

For this table, dividing off the prescribed maximal half-step vanishing factor does not create a fractional coefficient either. Write u=q^{1/2}; the raw formulas lie in Z[u,u^{-1}]. To prove the precise assertion directly, write a rational Laurent quotient as g/N with g integral and N its least positive common coefficient denominator. If a prime p divides N, reducing the identity Nf=(u-u^{-1})^a g modulo p gives a nonzero Laurent polynomial (u-u^{-1})^a times the reduction of g equal to zero. The ring F_p[u,u^{-1}] is an integral domain, so every coefficient of g is divisible by p. This contradicts minimality of N. Hence N=1. Thus rational coefficients are permitted by the conjecture but are not forced by these six examples, even after the indicated exact factorization. This is a statement about these integral raw formulas and an exact polynomial quotient, not arbitrary rational normalization.

## 4. What the other printed data do and do not show

Section5.2 begins on p29; its Figures3--5, pp35--37, print ambient-expansion vectors for one element Sigma at r=4. It does not print a multiplication table there. These data cannot be relabeled as multiplication constants.

Section5.3 begins on p31 and describes a degree-two algebraic field extension generated by x=sqrt(disc). The coefficients of u_1^1 in Figure6, p38, contain explicit factors1/2 and x. They are coefficients in the monomial Q_sigma basis, as the full surrounding text says. They are not raw multiplication constants, and the visible rational prefactor is not by itself a Laurent spectral multiplicity.

The nonmonomial denominators in the coefficient vector expressing the balance-fiber element w in the opposite canonical basis occur on p33, in the context of proving failure of standard balance. They likewise are not c(b,b';b'') multiplication constants. This is the conspicuous rational-function example that must not be promoted into a counterexample for the present question.

The relevant later subsection is **5.4.1**, pp48--49, label snonstdposexp. It says that a computed structural coefficient or constant is multiplied by a suitable power of hat f_p(q); the displayed exponent n(c) is chosen no larger than the full rescaling exponent m(c). The exponents for the individual figures are not supplied. Section5's vector definition, p27, then removes the maximal possible power of q-q^{-1}, or the analogous half-step factor, and records only the nonnegative half of the bar-invariant remaining coefficient vector.

Figures24--26, p58, and30--32, pp62--63, are the six displayed vectors of multiplicative constants themselves. Figures27 and33, pp59 and63, are vectors of field traces; Figures28--29 and34--35, pp60--61 and64--65, are the corresponding field norms and their continuations. The text uses trace/norm for the algebraic coefficient field over Q(q), not arithmetic Frobenius traces at field extensions. All542 numeric entries in these twelve tables are integers, with some negative entries.

The rescaling polynomial hat f_p printed in VII Section7.1, TeX expression following labels eqscalingP2/eqscalingQ2, has integral Laurent coefficients in the supplied source. I read the whole rescaling context, including the distinction between the original convenient projector scaling and the later formal scaling. I do not infer an omitted VIII exponent or silently identify its shortened normalization convention with every factor in VII's formula. A primitive integral multiplier can clear a nonmonomial denominator; integral normalized vectors therefore do not establish Laurentness of the pre-normalized constants.

## 5. The exact integrality comparison that would be needed

Here is the elementary necessary condition, independent of purity.

Let f(z)=sum_j a_j z^j be a finite Laurent polynomial with rational coefficients, and fix a nonzero algebraic beta. Suppose that for every sufficiently large n,

f(beta^n)=sum_i (-1)^i Tr(F^n;H^i)

for a bounded finite-dimensional point complex with invertible Frobenius. Group the exponents j for which beta^j is the same root gamma. Then every grouped coefficient

m_gamma=sum_{j: beta^j=gamma} a_j

must be an integer.

To prove this, the right side is a finite power sum whose grouped coefficients are differences of actual eigenvalue multiplicities, hence integers, whether or not Frobenius is semisimple. Subtract it from the finite power sum on the left. For the distinct nonzero roots in their union, the matrix of sufficiently large consecutive powers is a Vandermonde matrix times an invertible diagonal matrix. Each grouped coefficient must therefore agree. No weight or sign assumption is used.

If beta is not a root of unity, all exponents are distinct and every a_j must be integral. For finite order h, only their residue-class sums modulo h are forced to be integral. Neither pointwise integer values nor rationalization of K0 supplies actual integer multiplicities: the elementary sequence (1+(-1)^n)/2 has integer values but noninteger coefficients at the two distinct roots and cannot be an uninserted finite Euler trace.

If f is a genuinely non-Laurent rational function and beta is a fixed real number greater than one, the previously proved F26 rational-dilation argument is an additional finite-spectrum obstruction. No multiplication formula with that property was identified in the bounded printed data audited here.

Conversely, the six raw formulas in Section3 do have bounded **mixed** uninserted Tate realizations under q_src=Q^n. For each coefficient a_j>0, put a_j copies of E(-j) in degree0; for a_j<0, put -a_j copies of E(-j) in degree1. Their Euler traces at extension n give sum_j a_j Q^{jn}. These are finite sums of ordinary Tate lines, mixed in general, with no inserted operator. This scalar construction does not retain multiplication, source bases, canonical simples or a common pure weight. It explains exactly why the present integrality audit adds no obstruction to mixed scalar realizations of the printed Figure2 formulas.

An overall Tate or cohomological shift changes roots or an overall sign; it does not repair a genuinely fractional grouped multiplicity. Clearing a numerical denominator by rescaling a basis changes the designated constants and would require a new compatible action/multiplication comparison. A trace with an arbitrary inserted endomorphism can have nonintegral coefficients and is outside this uninserted test.

## 6. Separate Grothendieck dictionary and verification

The effective graded coefficient cone has integral dimensions, while tensoring its Grothendieck group with Q admits rational virtual classes without producing corresponding actual finite objects. SGA6 V Sections2--3 and cote133 scan18 supply the representation-class language; this observation does not assert a lambda-ring structure on the source noncommutative algebra. The bounded mixed Tate witnesses are actual perfect coefficient complexes in the framework of SGA6 I Definition4.7, pp121--122, and Example4.8, p122. The source's permission of rational positive factors alone gives no prescribed Euler realization in that framework.

The exact script verify_viii_multiplication_integrality.py expands all six formulas, checks monomial denominators and integral coefficients, counts all thirteen printed labels, and parses every cell of all twelve normalized vector tables. Its saved viii_multiplication_integrality_certificate.json records the source hash, coefficient vectors, per-figure counts and the exact limited scope. It passed. The source-role distinctions, primitive-factor observation, eventual Vandermonde argument and mixed Tate construction were proved/read manually; no formal verification is claimed.

No computation of unprinted structure constants, recovery of the omitted rescaling exponents, or global absence theorem was performed. Fresh independent review of this bounded audit is requested. No frozen prior finding or master artifact was changed.

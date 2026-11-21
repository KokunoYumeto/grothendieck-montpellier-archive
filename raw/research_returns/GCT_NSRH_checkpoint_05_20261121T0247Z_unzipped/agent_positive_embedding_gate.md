# Positive embeddings: a constructive criterion and its limits

Date: 2026-11-21 (Europe/Berlin). Author/checker `/root/gct_statements`, GPT-6 Astra Pro, effort inherited/not exposed. All elementary proofs below were derived and then read in full in this run. These are observations for this investigation, not claims of historical novelty. Suggested IDs PG1–PG4 are provisional; root can rename them.

## PG1. Positive monomial pivot criterion

Let R=Q[v,v^−1] and R_+=Q_(≥0)[v,v^−1]. Let B be an R-algebra free as an R-module with basis (e_j) whose multiplication constants lie in R_+. Let A⊂B be an R-subalgebra, free as an R-module with designated basis (b_i), and write

\[
b_i=\sum_j p_{ji}e_j,\qquad p_{ji}\in R_+.
\]

Assume that for every i there is a coordinate j_i with

\[
p_{j_i,i}=r_i v^{m_i},\quad r_i\in\mathbb Q_{>0},\quad m_i\in\mathbb Z,
\qquad p_{j_i,h}=0\quad(h\ne i).
\]

Then all multiplication constants of A in the b-basis lie in R_+.

**Proof.** The external expansion of b_s b_t has coefficients in R_+, by positivity of the p's and the ambient multiplication constants. Write b_s b_t=sum_i m_(st)^i b_i, using closure and the R-basis. At coordinate j_i this equality reads

\[
[e_{j_i}](b_s b_t)=r_i v^{m_i}m_{st}^{i}.
\]

The left side is in R_+. Multiplication by r_i^−1 v^−m_i preserves R_+, so m_(st)^i∈R_+. This proves every coefficient. ∎

Full pairwise disjointness of the supports of b_i is unnecessary; one exclusive monomial pivot per basis element suffices. The same proof works over Z[v,v^−1] when the algebra coefficients are already integral; a positive integer pivot scalar cannot change signs. Replace v by q^(1/2) to match the dual-side GCT conventions.

This is a concrete sufficient algebraic gate for inheriting positivity without new finite-field geometry. It is stronger than positive external expansions, bar invariance, or local disjoint supports.

## PG2. Global disjoint positive supports do not suffice without the pivot normalization

Set

\[
p=v+v^{-1},\quad h=v^2-1+v^{-2},\quad c=ph=v^3+v^{-3}.
\]

Define the associative R-algebra, free as an R-module,

\[
B=R\times R[t]/(t^2-c)
\]

with basis 1=(1,1), x=(0,t), y=(0,1). Its multiplication table is

\[
x^2=cy,\qquad xy=x,\qquad y^2=y.
\]

Every structure coefficient in this basis is in R_+. The elements are linearly independent and span because (a,b+dt)=a1+dx+(b−a)y. In particular this description also proves associativity, without relying on an unchecked table.

Let A be the R-span of 1,x,z=py. It is a free subalgebra: the defining products are

\[
x^2=hz,\qquad xz=px,\qquad z^2=pz.
\]

All three basis elements have pairwise disjoint, nonempty, coefficientwise positive supports in the ambient basis: {1}, {x}, {y}. Nevertheless, the structure coefficient h=v²−1+v^−² is not nonnegative. All basis elements and all defining data are fixed by the semilinear bar v↦v^−1. Over K=Q(v), the ambient algebra is semisimple, since K[t]/(t²−c) is étale in characteristic zero with c≠0. Thus semisimplicity and bar invariance do not repair the missing pivot condition.

This also fails the raw signed-normalized positivity form ±(v−v^−1)^a f(v), with a≥0 and f coefficientwise nonnegative: h(1)=1 forces a=0; then the sign must be positive and f=h, which has a negative coefficient. Thus even the signed-factor relaxation cannot be deduced from these abstract hypotheses.

If one insists on an inclusion proper over the generic field, enlarge the ambient algebra to B×R and use the basis {1_tot=(1_B,1), x=(x,0), y=(y,0), w=(0,1)}. Its multiplication constants remain nonnegative, with xw=yw=0 and w²=w. The subalgebra span{1_tot,x,py} has generic dimension 3 inside generic dimension 4, and the same counterexample applies. ∎

This is an abstract positive-algebra countermodel, not a counterexample to a designated GCT canonical basis. It proves that a general inheritance theorem needs more than the suggested hypotheses.

## PG3. Disjoint supports only after crystal specialization are weaker still

Over Q[v], take the positive algebra B=Q[v][x]/(x²−x), with basis {1,x}. Its basis {b_0=1,b_1=x+v} has coefficientwise nonnegative external expansions. Modulo v its supports are the distinct singleton supports {1} and {x}. Yet

\[
b_1^2=(1+2v)b_1-v(1+v)b_0.
\]

**Proof.** Expand x²+2vx+v², substitute x=b_1−v, and collect. The coefficient −v−v² is negative. ∎

VIII **Conjecture 2.2**, `clocalcrystalb`, gives disjoint monomial supports for the basis of **L_alpha/qL_alpha**, not global positive monomial pivots for the coefficients of the minimum-degree global basis in CB(Z). Source lines 634–655 state the local condition. Source lines 893–918 introduce the separate global expansion a(y,z); no exclusive global pivot is asserted. The countermodel above explains why local disjointness cannot simply be promoted to the hypothesis of PG1. The minimum-degree/globalization conjectures would need additional work to produce such pivots. Moreover, PG1 would imply raw coefficientwise positivity, while VIII intentionally permits signed structural constants; it is therefore too strong for some of the actual normalized targets.

## PG4. Independent check of the actual rank-one nonstandard Hecke cone obstruction

This result was proposed by another agent; the proof below is an independent check, not an ownership claim.

Take the rank-one Hecke algebra in the consistent convention

\[
(T-v)(T+v^{-1})=0,\qquad c=T+v^{-1},\qquad\delta=v+v^{-1}.
\]

Then c²=δc, and C=T−v=c−δ. In its tensor square let

\[
P=c\otimes c+(c-\delta)\otimes(c-\delta)
=2c\otimes c-\delta(c\otimes1+1\otimes c)+\delta^2(1\otimes1).
\]

This is the symbolic generator of revised IV **Definition 11.1, equation (93)** (`d nonstandard Hecke algebra`, `e sP definition`), with the consistent §3.1 convention. Let K=Q(v) and let C_+ be the nonnegative rational Laurent cone in the standard positive tensor basis {1,c}⊗{1,c}. Then

\[
(K1+KP)\cap C_+=R_+1.
\]

**Proof.** For a+bP, the coefficient of c⊗c is 2b. Membership in C_+ forces b∈R_+. The coefficient of c⊗1 is −δb, which can be nonnegative only if b=0, because δ has positive coefficients and a nonzero product δb has a positive coefficient. Then the constant coordinate is a, which must be in R_+. Conversely R_+1 is in the intersection. ∎

Also P²=δ²P. One proof writes e=c/δ, f=(c−δ)/δ; then e²=e, f²=−f and ef=0, so P=δ²(e⊗e+f⊗f), and both e⊗e and f⊗f are orthogonal idempotents. Thus {1,P} is intrinsically a positive basis even though no two independent positive elements in the specified ambient cone can span it.

**Scope.** This refutes a literal strategy of obtaining the nonstandard algebra by taking an effective positive subcategory of the usual Hecke category whose class map is this inclusion and whose objects span its K0: every such object's class would be in the ambient positive cone, which only spans one dimension here. It does not refute a new category, a different cone/basis convention, a derived/virtual embedding, or VIII's signed-normalized positivity. Positivity is basis-sensitive.

**Source normalization discrepancy, independently verified.** Revised IV §3.1, source line 1674, uses C'_s=T_s+q^−1 and C_s=T_s−q, consistent with its quadratic relation. The opening of §11.1, source line 3735, swaps q and q^−1, yet claims C'_s/[2] is an idempotent. The literal formulas there are inconsistent with the preceding quadratic convention. State c²=δc explicitly and use §3.1 plus symbolic equation (93); do not silently quote the swapped formulas as consistent. The PDF reproduces the same discrepancy (printed pp. 21,58–59).

## Source-backed additional illustration

VIII **§5.1.2, Figure 2** (`fmultkron2`) lists

\[
c(\gamma_1^1,\gamma_1^1;\gamma_1^1)
=-\frac{(1+q)^2(q^2+q+1)(q-1)^2}{q^3}.
\]

The neighboring discussion reports positive ambient canonical expansion coefficients in its specified symmetrized/ordered basis. Thus the paper itself expects signed raw constants. This is source-reading evidence, not a recomputation of its full algebra. It is safer to use PG1–PG4 as fully checked elementary arguments and cite this only as illustration.

## Check events

- PG1: targeted proof check, entire proof; PASS.
- PG2: targeted proof check, entire proof; PASS; algebra realized as a product/quotient, closure and the negative coefficient verified algebraically; no formal certificate claimed.
- PG3: targeted proof check, entire proof; PASS; exact expansion performed independently.
- PG4: independent re-proof of the other agent's result, plus targeted source-normalization check; PASS with convention caveat.
- VIII local supports/negative example: used and rechecked in this run; local/global distinction and source signs confirmed, experimental coefficient not independently recomputed.

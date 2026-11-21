# Step 2, higher height, and a stronger universal derivative bound

**Source-status update, 2026-11-21:** This memo records the first stage of the source investigation. Its statements below that the full local interfaces had not yet been identified are superseded by `step2_recovered_sources.md`, especially §§2–3 and §§7–8. Targeted recovery has now identified the actual `B0`–`B4`, fixed-logarithm, Gauss-jet and global path-valuation interfaces. The mathematical proofs in this memo retain their stated hypotheses; the remaining higher-height problem concerns a replacement construction and its costs, not lack of a source locator for the accepted height-two framework.

Run: DP_MULT_20261121; agent `/root/step2_higher`; model GPT-6 Astra Pro; effort setting not exposed. Draft completed 2026-11-21 Europe/Berlin (2026-11-20 23:57 UTC). This file records mathematical findings and source checks, not a Lean certificate. The user directs that Alpöge's final theorems be cited as theorems; no revalidation of RH is attempted here.

## SHA-1. A uniform constant-error estimate (proved)

Let R=W(k), k perfect of characteristic p, and let F be a one-dimensional commutative formal group law over R. Suppose the special fibre has height at least h, where h is a positive integer; thus [p]_F(t) belongs to pR[[t]]+t^qR[[t]], q=p^h. Let D be the invariant derivation normalized by Dt(0)=1. Put

\[
 c_h=\frac1{p-1}-\frac1{q-1},\qquad
 B=v_p(q!)-1=\frac{q-1}{p-1}-1=c_h(q-1).
\]

For every a>=0 and every f in R[[t]],

\[
 D^a f\in p^{\max\{0,\lceil ac_h-(h-1)\rceil\}}R[[t]]. \tag{SHA-1}
\]

In particular the same bound holds for D^a f(0). The constant h-1 is the smallest real C such that the real-valued inequality v_p(D^a f(0))>=ac_h-C holds for every a, F and f in these hypotheses. This claim concerns a uniform affine lower bound; it does not claim the displayed integer bound is pointwise optimal for every a.

### Full proof

Write the normalized logarithm as L(t)=t+sum_{n>=2}l_n t^n over Frac(R). It obeys L([p]_F(t))=pL(t). Write [p]_F(t)=pt+sum_{n>=2}a_n t^n. For 2<=n<q, coefficient comparison gives

\[
 (p-p^n)l_n=a_n+\sum_{i=2}^{n-1}l_i[t^n]([p]_F(t))^i.
\]

Assume inductively l_i integral for i<n. Each a_j used in [t^n]([p]_F(t))^i has j<q, hence is divisible by p; the indicated coefficient is divisible by p^i. Also a_n is divisible by p. The right side is divisible by p, and (p-p^n)/p is a unit. Therefore l_n is integral. The same argument at n=q gives v_p(l_q)>=-1, since a_q is integral and all other summands are divisible by p^2.

Make the strict integral coordinate change z=sum_{1<=n<q}l_n t^n. It has an inverse in R[[z]]. In this coordinate the normalized logarithm is

\[
 L_{new}(z)=z+bz^q+O(z^{q+1}),\qquad v_p(b)\ge -1.
\]

Indeed composing with the inverse cancels every term of degrees 2 through q-1, and changes the coefficient at q only by an integral quantity. Strictness preserves the normalized invariant derivation. Integral coordinate change also preserves the property of lying in p^mR[[t]].

Define integral invariant Taylor operators Delta_j by

\[
 f(F(z,u))=\sum_{j\ge0}(\Delta_jf)(z)u^j.
\]

Each Delta_j maps R[[z]] to itself. Over Frac(R), the logarithm identifies translation by u with translation by L_new(u); consequently

\[
 \sum_{j\ge0}\Delta_j u^j=\exp\big(L_{new}(u)D\big).
\]

This is the standard distribution-algebra identity of Katz, Corollary 1.8, p.669, applied after the strict coordinate change. It gives

\[
 \Delta_j=D^j/j!\quad(0\le j<q),\qquad
 \Delta_q=D^q/q!+bD.
\]

Let w=q!/p^{B+1}, a p-adic unit. Then

\[
 D^q=p^B uD+p^{B+1}T,\qquad
 u=-wpb\in R,\quad T=w\Delta_q\in\operatorname{End}_R(R[[z]]). \tag{SHA-1a}
\]

If the height is exactly h then u is a unit, although this is unnecessary for the estimate. No commutation of T and D is needed below: multiply this equation on the right by D^{a-q}.

For 0<=a<q, D^a=a!Delta_a is integral with valuation at least v_p(a!). Write a=sum_{j=0}^{h-1}d_j p^j, 0<=d_j<=p-1. Legendre's formula yields

\[
 v_p(a!)-ac_h
 =\sum_{j=0}^{h-1}d_j\left(\frac{p^j}{q-1}-\frac1{p-1}\right)
 \ge 1-h.
\]

Each coefficient in parentheses is nonpositive, so the minimum occurs at d_j=p-1 for every j, namely a=q-1, where the value is 1-h.

Now use induction on a. For a>=q,

\[
 D^a=p^B uD^{a-q+1}+p^{B+1}T D^{a-q}.
\]

The first term sends f to a series of valuation at least

\[
 B+(a-q+1)c_h-(h-1)=ac_h-(h-1).
\]

The second has valuation at least

\[
 B+1+(a-q)c_h-(h-1)
 =ac_h-(h-1)+(1-c_h)\ge ac_h-(h-1),
\]

because 0<=c_h<1. Integrality and the integer-valued valuation give SHA-1. Finally choose a=q-1 and f=t^{q-1}. The normalized derivation has D^a(t^a)(0)=a!, so equality holds in the real lower bound, proving optimality of C=h-1. QED.

### Exact recursive refinement

The same proof gives an entirely explicit stronger integer-valued bound. Let b_h(a)=v_p(a!) for 0<=a<q, and for a>=q set

\[
 b_h(a)=B+\min\{b_h(a-q+1),1+b_h(a-q)\}.
\]

Then D^a R[[t]] is contained in p^{b_h(a)}R[[t]]. This is a proved bound, not a claim of pointwise optimality. For the paper the simple uniform affine estimate is likely sufficient. The optimal-intercept statement is already exact and avoids an asymptotic error symbol.

### Literature/novelty limitation

The same affine estimate for Lubin-Tate groups is already a direct consequence of Bannai--Kobayashi, *Integral structures on p-adic Fourier theory*, AIF 66(2) (2016), 521--550:

- §2, p.527: valuation of the Lubin--Tate period varpi_p is 1/(p-1)-1/[e(q-1)].
- Definition at the start of §3, p.528: rho[k,n]=max_{k<=m<=n}|m!/varpi_p^m|.
- Proposition 3.3, p.529: rho(0)=|pi/q| when e<=p-1.
- Proposition 3.5, p.531, second displayed inequality: |partial^n exp_G(t)^k| at t=0 is at most |varpi_p^n|rho[k,n].

For an unramified degree-h local field, e=1,q=p^h, rho[k,n]<=rho(0)=p^{h-1}; thus the displayed derivative valuation is at least nc_h-(h-1). Summing over the finitely many monomials k<=n proves the same for every integral f. SHA-1 supplies a proof for arbitrary one-dimensional integral formal groups with the stated height condition; it should be described as this extension/formulation, not as discovery of the Lubin--Tate estimate or the exponent.

## SHA-2. The precise local comparison with step 2 (proved conditional application; source identification incomplete)

Let E/R be an elliptic scheme with supersingular special fibre. Its formal completion at the identity is one-dimensional of height 2. If f in the completed local ring is integral, and D is the invariant derivation dual to an integral generator of invariant differentials, then SHA-1 gives

\[
 v_p(D^a f(0))\ge\max\left\{0,\left\lceil\frac{ap}{p^2-1}-1\right\rceil\right\}. \tag{SHA-2}
\]

Proof: substitute h=2. The supersingular/height-2 equivalence is classical elliptic formal-group theory; in the particular inert CM setting it is explicitly realized by Katz §IV, (4.1)--(4.6), pp.675--676. No CM is needed for the local estimate once supersingular reduction and the integral formal group are present. QED.

If normalized theta derivatives satisfy

\[
 \frac{D_{an}^a\theta(0)}{\Omega^a}=D^a f(0)
\]

for such an integral f, then SHA-2 is the precise no-log-loss local bound for them. If f belongs only to p^{-M}R[[t]], subtract M. If the normalized analytic derivation equals uD for a constant scalar u, add a v_p(u) to the valuation estimate. These changes are essential: height does not control a chosen transcendental period or denominators of a theta trivialization.

The exponent in Alpöge's *Remark*, p.3, timeline step 2, was read from the rendered PDF and is exactly

\[
 a/p+a/p^3+\cdots-O(\log a)=ap/(p^2-1)-O(\log a).
\]

Thus its leading coefficient is exactly the height-2 coefficient; SHA-1 improves the error for the local integral formal-function statement. It is not justified to identify the entire theta assertion with a formal-group theorem without verifying (i) good reduction over the stated unramified base; (ii) the algebraic normalization of the theta section/its local trivialization; (iii) the period/derivation comparison; (iv) bounded denominators independent of a.

A theta function is ordinarily a section of a line bundle, not intrinsically an element of R[[t]]. If e is a local frame and theta=f e, the derivatives of f depend on e; an integral change of frame preserves applicability of the universal bound, but does not prove the analytic-period comparison. The available note supplies neither f nor this comparison.

### Exactly what Katz proves (cited, not newly proved)

Katz, *Divisibilities, congruences, and Cartier duality*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. 28(3) (1981; publication catalogued 1982), 667--678, Main Theorem 3.11(I), p.672, says: for q=p^2, the Lubin--Tate group with

\[
 [p](X)=pX+\alpha X^{p^2},\quad\alpha\in R^\times,
\]

and integral f satisfying the additional difference equation

\[
 \sum_{\lambda\in G[p]}f(X+_G\lambda)=0,
\]

one has

\[
 v_p(D^n f(0))\ge\left\lfloor\frac{np}{p^2-1}\right\rfloor.
\]

This stronger exact estimate includes a trace-zero hypothesis. It is not the theorem for every integral formal function. Section IV assumes p>=5, constructs integral modified Weierstrass functions wp_{b,p} in (4.8)--(4.10), p.676, and in (4.14), p.677 identifies their derivatives with

\[
 (1-b^{n+2})(1-p^n)\frac{B\!H(n+2)}{n+2}.
\]

The exponents and the Cartier-duality connection in Fable's recalled citation are real, but the source's hypotheses and modified functions must be retained. Main Theorem 3.11 was visually checked on the original scanned PDF, not inferred from an OCR string.

### Available Lean provenance

`ALPOGE_Main.lean` contains only five final theorem declarations importing `Statements` and `Supplements.Kernels.MainTheoremsAll`. `ALPOGE_Statements.lean` defines the final zeta/Dirichlet propositions. Neither file contains a formal group, theta local expansion, period normalization, or a theorem for step 2 or step 8. The supplied `ALPOGE_LEAN_MAP_20261120.md`, §4 row 2, explicitly labels its match for step 2 **low confidence** and names folders (`BlockTheory/HeightDefect`, `Proofs/HomogeneousIdeals`, `Proofs/CubicalLineBundles`) and two literature-property names, not a precise declaration. Row 8 gives candidate theta-lift folders and a medium-high confidence match. This is enough to report the source limitation; it is not enough to invent exact Lean lemmas or to assert that no such lemma exists in the complete archive. Full Lean archive is not in the attached ZIP.

## SHA-3. Higher-height directional divisibility (proved)

Let A/R be an abelian scheme and i:F->A-hat an integral homomorphism from a one-dimensional formal group whose special fibre has height at least h. Let f be an integral formal function on A-hat and let D_i be the invariant tangent direction induced by the normalized invariant derivation D_F. Then

\[
 (D_i^a f)(0)=D_F^a(i^*f)(0),\qquad
 v_p((D_i^a f)(0))\ge\max\{0,\lceil ac_h-(h-1)\rceil\}. \tag{SHA-3}
\]

Proof: the formal group homomorphism identifies translations and therefore intertwines invariant derivations. Apply SHA-1 to the integral pullback i^*f. No direct-factor assumption is necessary if the integral map and the tangent direction exist. A special-fibre summand alone does not provide such an integral lift. A rational isogeny summand does not supply the integral lattice comparison either. QED.

For an actual integral product decomposition F_1 x ... x F_r with one-dimensional factors of respective heights h_i, the commuting partial invariant derivatives satisfy the multidegree bound

\[
 v_p(D_1^{a_1}\cdots D_r^{a_r}f(0))\ge
 \sum_i\max\{0,\lceil a_i c_{h_i}-(h_i-1)\rceil\}.
\]

Proof: SHA-1 holds for the operator on the whole ring, and coefficientwise with an auxiliary integral power-series coefficient algebra. Apply it one variable at a time; the invariant derivations preserve the other factors and commute. This is a statement about integral formal jets and the Lie directions of an abelian scheme, not yet an automorphic multiplicity theorem.

## SHA-4. Height of a multidimensional factor is insufficient (refuted with counterexample)

Take F=G_m-hat^r with coordinates t_1,...,t_r, r>=2. Its total p-divisible height is r, but its dimension is r. With D=(1+t_1)partial/partial t_1 and f=1+t_1, induction gives D^a f=f, hence D^a f(0)=1 for every a. Every positive affine gain associated with substituting h=r into the one-dimensional formula eventually fails. Therefore “a formal summand of height h” must explicitly include dimension one (and the integral lift/lattice), or be replaced by a genuinely multidimensional statement involving its separate directions.

This can occur in the CM abelian context: a product of ordinary CM elliptic curves has an ordinary formal group of this form after a suitable unramified extension. The formal-group counterexample itself is complete without requiring that background realization.

## SHA-5. CM type constrains possible higher-height directions (proved short consequence of CM decomposition)

Assume A/R has good reduction, full action of O_E for a CM field E of degree 2g, and p is unramified in E. Work after an unramified base change containing the embeddings needed to split the O_E action. Let G_v=e_vA[p^infinity] for v|p, using the integral idempotents of O_E tensor Z_p. Then

\[
 h_v=[E_v:Q_p],\qquad d_v=\#\Phi_v,
\]

where Phi_v is the part of the p-adic CM type inducing v. Complex conjugation pairs embeddings in the CM type complement, so

\[
 h_{\bar v}=h_v,\qquad d_v+d_{\bar v}=h_v.
\]

The height/dimension description is the standard CM p-divisible decomposition: Tate, Bourbaki exposé 352 (Nov.1968), §5, definition on p.106 and Theorem 3 on pp.107--108; also Milne, *Complex Multiplication* (14 July 2020), §8, Theorem 8.12 and the application immediately following on p.73. The short deduction below is the form needed here.

If d_v=1 and v=bar v, then 2=h_v. If d_v=1 and h_v>2, then v and bar v are distinct and the paired factor has dimension h_v-1. Since both occur in A[p^infinity], dim A=g>=h_v. Thus a one-dimensional height greater than two is possible only with a complementary direction/collection of directions; it is not achieved by merely increasing the inert elliptic height.

Proof of the new assertions: an embedding tau inducing v has conjugate bar tau inducing bar v. Exactly one of tau and bar tau belongs to the CM type. Counting these embeddings gives the dimension identity. If v=bar v, it reads 2d_v=h_v; otherwise the two factors contribute d_v+d_barv=h_v to dim A. QED.

## SHA-6. The gain is bounded; divisibility does not itself give theta-lift multiplicity (proved limits; global shortening open)

For h>=2,

\[
 c_{h+1}-c_h=\frac1{p^h-1}-\frac1{p^{h+1}-1}>0,
 \qquad c_h<\frac1{p-1},
\]

and therefore

\[
 \frac{c_h}{c_2}<\frac{p+1}{p}=1+\frac1p.
\]

These follow by direct subtraction and taking the geometric-series limit. Thus higher height improves the local valuation slope, but even the limiting improvement relative to height two is bounded by 1+1/p. No cost of a theta lift has been divided out in this computation.

Formal arithmetic multiplicity and ordinary geometric vanishing are different. For any F as in SHA-1, f=1+t is a unit of R[[t]], so its zero divisor is empty near the identity and ord_0(f)=0 on the generic fibre. It nevertheless satisfies every derivative bound of SHA-1. Likewise multiplying a section by p^N raises all p-adic valuations while leaving its nonzero generic-fibre vanishing orders unchanged. Thus the inference “better formal derivative divisibility implies higher geometric vanishing multiplicity” is false.

Alpöge's *Remark*, p.4, step 8, concerns a specified chain of theta lifts between totally definite unitary groups, whose automorphic/period construction wins multiplicity m with a chain of length m; the same step says m is taken like sqrt(X). Steps 9, 10, 12, 14, 15, and 18 explicitly bring in norms, levels, divisibility, seesaw/Bessel period comparison, cost, integral structures, and covolumes. A higher-height local derivative coefficient does not substitute for those data.

The precise missing theorem for a shorter-chain proposal is a construction of integral global theta lifts/auxiliary sections attached to a one-dimensional height-h factor, with a comparison identifying the relevant automorphic order-m cancellation ideal (or the exact period/divisibility functional used in the proof) with the formal jet filtration, together with all archimedean norm, level, and covolume estimates in the same normalization. It must quantify how one lift changes that filtration and how its cost changes with h. The note and map do not state such a comparison. Targeted inspection of the supplied map for `formal`, `jet`, `height`, `divisibility`, `multiplicity`, `Hasse`, and `derivation` found no theorem statement of this form. Candidate paths are not a proof.

Consequently the universal local bound and the negative inference are settled. The existence of a shorter global proof is **not proved or refuted** by these findings. An assertion that such a shorter proof is impossible would be unwarranted. The actual global-shortening question remains at the comparison-and-cost theorem just specified.

## Source retrieval and evidence

1. Katz author-hosted primary PDF: https://web.math.princeton.edu/~nmk/old/divcongCartier.pdf . Web ref `turn748475344view1`. Downloaded as `Katz_divcongCartier.pdf`; visually read all twelve pages after rendering. Relevant pages: 668 Theorem 1.6; 669 Corollary 1.8; 670 Identity 2.4 and Congruences 2.5; 672--675 Main Theorem 3.11 and proof; 675--677 §IV CM application.
2. Bannai--Kobayashi primary article: https://www.numdam.org/article/AIF_2016__66_2_521_0.pdf . Web ref `turn748475344view0`. Downloaded as `Bannai_Kobayashi_2016.pdf`; text extracted and exact formulas checked. Relevant p.527 and Propositions 3.3,3.5. Main Theorem 5.8 reobtains Katz/Chellali congruences; its introduction cites Katz 3.11 correctly, whereas the later prose at p.548 cites “3.1”, apparently a citation typo in that later paper. This is not a Grothendieck transcription issue.
3. Tate primary source: https://www.numdam.org/item/SB_1968-1969__11__95_0.pdf . Web refs `turn281869863view0`, `turn786457657view0`; downloaded as `Tate_352.pdf`. The definition, dimension/height counts, Theorem 3 and its proof on pp.106--108 were read visually in the rendered original scan. The numerical slope formula is (10*) on p.107; the decomposition theorem is Theorem 3 immediately below it, with decomposition (15) and tangent decomposition (16).
4. Milne author's exposition: https://www.jmilne.org/math/CourseNotes/CM.pdf , version 14 July 2020. Web refs `turn463805871view0`, `turn208742480view1`. Theorem 8.12 (Tate 1968, Théorème 3), p.72, then decomposition on p.73. Its proposition 8.11 has “Proof. To be added”; do not describe this note as a complete independent proof source of that proposition.
5. Alpöge supplied PDF rendered pages 3 and 4 read visually. Supplied Main, Statements, and §4 of supplied Lean map read directly. The complete 175,187-file Lean archive is not present in this ZIP; only the supplied scan summary and map describe it.

## Check events (honest metadata for parent to merge)

| Statement | Date (Berlin) | Who | Event type | Outcome |
|---|---|---|---|---|
| SHA-1 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | targeted proof check | Whole proof reread: log integrality induction, strict-coordinate inverse, Delta_q identity, operator induction, optimal intercept all pass. |
| SHA-1 | 2026-11-21 | /root, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | independent re-proof | Parent message confirms independent verification of the entire recurrence and optimal intercept. |
| SHA-1 | 2026-11-21 | /root/formal_bound, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | independent re-proof | Agent message confirms whole-proof challenge passed; notes T need not commute with D when equation multiplied on right. |
| SHA-2 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | targeted proof check | Substitution h=2 and normalization/denominator qualifications reread; application conditional on explicit identification of theta with integral formal f. |
| SHA-3 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | targeted proof check | Pullback commutation with invariant derivatives and coefficientwise multivariable extension checked. |
| SHA-4 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | refuted, with refined statement SHA-3 | Direct computation D^a(1+t_1)=1+t_1 disproves substitution of total multidimensional height. |
| SHA-5 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | targeted proof check | CM-type counting and dimension consequence reread; standard decomposition cited, not reproved. |
| SHA-6 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | targeted proof check | Coefficient inequalities, unit counterexample, and limitation of the negative conclusion checked. Global shorter-chain existence remains open. |
| Katz-1.8 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | used and rechecked in this run | Original scan pp.668--669 visually read; adapted operator identity directly checked. |
| Katz-3.11-I | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | used and rechecked in this run | Original theorem and proof pp.672--675 visually read; trace-zero and height-2 hypotheses recorded. No formal verification claimed. |
| Katz-IV | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | used and rechecked in this run | Original scan pp.675--677 visually read; p>=5, unramified W(F_p²) base, normalized modified Weierstrass functions recorded. |
| BK-3.3-3.5 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | used and rechecked in this run | Exact displayed inequalities and their combination checked from primary article; no independent reproving of entire source theorem claimed. |
| Tate-CM-decomposition | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | used and rechecked in this run | Primary Tate scan pp.106--108 definition, Theorem 3 and proof read visually; exact height/type counts and their use checked. The standard degree formalism is accepted background. |
| Alpoge-step2-step8 | 2026-11-21 | /root/step2_higher, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121 | used and rechecked in this run | Exact formulas in supplied PDF visually checked; final theorems accepted under user's citation instruction. This is a source/formula check, not a Lean compilation. |

## Transcription notes

No correction to Grothendieck manuscript text is asserted by this agent: it did not inspect original Grothendieck manuscript images. The noted BK internal cross-reference typo belongs in source notes, not `TRANSCRIPTION_NOTES.tsv` for Grothendieck's archive.

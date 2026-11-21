# Rank-four source audit and an actual irreducible word-trace obstruction

Author: /root/gct_statements, GPT-6 Astra Pro. Inherited reasoning-effort setting is not exposed. Date: 2026-11-21 UTC. This report distinguishes source statements, new exact deductions, and finite searches. It is not a formal proof-assistant verification.

## 1. Exact source and the already known rank-four construction

The supplied source is

/workspace/scratch/b5024d19aacd/sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex.

The numbered locators below were checked against the primary arXiv v4 PDF, https://arxiv.org/pdf/cs/0703110 (6 June 2013). Page numbers are printed pages, one greater than the zero-based PDF page index.

There is a previously identified exponent-convention inconsistency between the preliminary \(C'_s,C_s\) formulas in §11.1 and the formulas in §3.1. The present calculation uses the explicit Figure 22 action and the symbolic normalization \(P_i+Q_i=D\), not the inconsistent preliminary expansion in \(T_s\). The independently checked identities \(Q_i^2=DQ_i\) confirm that the displayed matrices have this intended normalization.

| Source item | Printed locator | Supplied TeX locator | What it actually supplies |
|---|---|---|---|
| Introduction, tensor basis | §1.5, p.13 | label “ss towards an upper canonical basis for nsX”; lines 1343–1362 | The two-row tensor basis is already constructed for ranks at most four; some higher highest-weight spaces are also constructed. |
| Complementary generators | §11.1, p.59 | line 3748, following “e sP definition” | \(Q_i=[2]^2-P_i\). |
| Involution | Proposition 11.6, p.60 | “p theta on nsH” | \(\Theta(P_i)=Q_i\); \(\Theta\) comes from twisting either ordinary Hecke factor by \(\theta\). |
| Dual conventions | §11.4, pp.62–63 | lines 3917–3941 | The symbol \(\#\) is the contragredient for the anti-involution \(\Theta^{\mathrm{op}}\), not an unexplained ordinary vector-space dual. |
| Specht duals | Proposition 11.11, p.63 | “p dual basis to C' S = 1 theta op” | \(M_\lambda^\diamond\simeq M_\lambda\), \(M_\lambda^\#\simeq M_{\lambda'}\). |
| Tensor dual and self-duality | Proposition 11.12, p.63, (101), (105), (108) | statement after “e ns sign decomposition” | \((M_\lambda\otimes M_\mu)^\#\simeq M_{\lambda'}\otimes M_\mu\) after restriction; \(S'M_\lambda\) is \(\diamond\)-self-dual. |
| Trace-free symmetric summand | §11.4, p.63, (98)–(100) | “e nsH trace”, “e nsH S' iso”, “e ns sign decomposition” | \(S^2\check M_\lambda=S'\check M_\lambda\oplus\check\epsilon_+\), and its \(\#\)-dual contains \((S'\check M_\lambda)^\#\). We work over the generic field, so no integral splitting-denominator issue is hidden. |
| Signed/factored positivity | Remark 11.19, p.67 | lines 4177–4184 | The rank-four \(Q_i\)-matrix coefficients have a sign after factors of \(q-q^{-1}\) are removed. This is weaker than coefficientwise nonnegative Laurent matrices. |
| Full rank-four algebra | §11.8, p.67 | “sb4”; lines 4188–4232 | The generic full algebra has dimension 114 and nine simple modules, including both \(S'\check M_{(3,1)}\) and its additional five-dimensional \(\#\)-dual. |
| Actual tensor occurrence | Theorem 12.1, p.68; following convention remark and §12.2 | “t nonstandard schur-weyl duality”, “e n lambda mu multiplicities” | The nonstandard action is the restriction of the two ordinary Hecke actions. The source explicitly qualifies its \(X/X^*\) convention; transposing consistently does not alter the trace obstruction. |
| Two-row quotient | Theorem 13.4, pp.74–75, (124) | “t nsH irreducibles two row case” | The eight two-row simple modules omit the additional five-dimensional \(\#\)-dual. Their squared dimensions sum to 89, not 114. |
| Tensor/cell requirements | Conjecture 19.1, pp.130–131 | “cj canonical basis X^r” | Six compatibility requirements for tensor cells and specialized quasi-cells. It does not assert strict nonnegative Laurent coefficients for every named generator. |
| Actual rank-four tensor basis | Example 19.3, pp.133–135 | “ex ns Schur-Weyl duality canonical basis r4” | A basis satisfying Conjecture 19.1 is explicitly constructed. Its global form and local lattice are modified forms, not the original tensor monomial lattice. |
| Six- and five-dimensional cell matrices | Figures 21 and 22, p.135 | “f nonstandardX4 3122”, “f nonstandardX4 3131” | Explicit \(Q_i\)-action graphs. Figure 22 is the exact input to the new calculation below. |
| Remaining algebra-basis problem | §19.1, p.136 | lines 8184–8189 | A canonical cellular basis of the nonstandard Temperley–Lieb algebra itself is constructed only for rank three; the next rank-four case remains difficult in this source. |

The coefficient sets in Example 19.3, p.134, are
\[
\tfrac12\mathbb Z\{[2],[3],[2]^2,[4],a_2\}
\quad\text{and}\quad
\tfrac12\mathbb Z\{[2],[2]^2,a_2,c_0\},
\]
for the ordinary left Chevalley operators and the \(Q_i\), respectively, with
\[
a_2=[2]^2-2,\qquad c_0=[2]^2-4=(v-v^{-1})^2.
\]
The use of \(\mathbb Z\), the displayed negative edges, and the Laurent coefficient \(-2\) in \(c_0\) prevent interpreting this statement as strict Laurent positivity. The exact source already makes a comparable distinction for the fat-cell basis: Theorem 17.7 gives signed coefficients for Chevalley generators, while Example 17.8, p.122, exhibits a divided-power coefficient \(v^{10}-v^4-v^{-4}+v^{-10}\). That existing example is not a new rank-four word-trace calculation.

For clarity, the eight two-row dimensions at rank four are
\[
1,2,3,6,5,2,3,1,\qquad
1+4+9+36+25+4+9+1=89.
\]
The ninth full-algebra simple is the additional five-dimensional \(\#\)-dual; its square supplies the missing 25.

## 2. Exact five-dimensional matrices

Put
\[
\delta=v+v^{-1},\quad D=\delta^2,\quad a=D-2,\quad c=D-4.
\]
Let \(N=S'\check M_{(3,1)}\). Order the five states in Figure 22 as
\[
(v_2,v_{13},v_1,v_{22},v_3),
\]
namely the two upper states from left to right and the three lower states from left to right. These names only identify the nodes of the source drawing. Matrices act on row vectors on the right: entry \((r,s)\) is the coefficient of state \(s\) in state \(r\) acted on by the indicated operator.

The descent sets are \(\{2\},\{1,3\},\{1\},\{2\},\{3\}\). The source caption specifies a diagonal coefficient \(D\) for a descent and the displayed arrows for all other coefficients. Thus the exact matrices are
\[
Q_1=\begin{pmatrix}
0&-\delta&c&0&0\\
0&D&0&0&0\\
0&0&D&0&0\\
0&0&a&0&0\\
0&-\delta&0&0&0
\end{pmatrix},\quad
Q_2=\begin{pmatrix}
D&0&0&0&0\\
-\delta&0&0&0&0\\
0&0&0&a&0\\
0&0&0&D&0\\
a&0&0&-a&0
\end{pmatrix},
\]
\[
Q_3=\begin{pmatrix}
0&-\delta&0&0&c\\
0&D&0&0&0\\
0&-\delta&0&0&0\\
0&-\delta&0&0&-2\\
0&0&0&0&D
\end{pmatrix}.
\tag{R4.1}
\]
The exact check also verifies \(Q_i^2=DQ_i\), \(Q_1Q_3=Q_3Q_1\), and the adjacent degree-five relation of IV Theorem 11.16. These checks validate the transcription against necessary algebra relations; the identification of the module itself comes from the source's Figure 22, not from treating those necessary relations as a rank-four presentation.

## 3. An exact negative word trace

Take the eleven-letter word
\[
w=(1,2,1,2,1,3,2,3,2,3,2).
\]
Direct multiplication gives
\[
\operatorname{Tr}_N(Q_w)=p(D),
\tag{R4.2}
\]
where
\[
p(D)=-D^9+20D^8-163D^7+734D^6-2048D^5
       +3712D^4-4352D^3+3072D^2-1024D.
\tag{R4.3}
\]

Here is a complete compressed product certificate. Define
\[
u=(-2\delta a,\ D^2,\ -\delta D,\ -\delta a,\ -\delta D)^t,\qquad
e_2^t=(0,1,0,0,0).
\]
The matrices (R4.1) give \(Q_1Q_3=ue_2^t\). Rotate the product inside the trace at the adjacent \(Q_1Q_3\), and set
\[
A=Q_2Q_3Q_2Q_3Q_2Q_1Q_2Q_1Q_2.
\]
Multiplying this row through (R4.1) yields
\[
e_2^t A=(r_1,0,0,r_4,0),
\]
\[
r_1=-\delta^5(D^4-9D^3+31D^2-48D+32),
\]
\[
r_4=\delta(D^7-16D^6+109D^5-418D^4
                  +992D^3-1472D^2+1280D-512).
\]
Consequently
\[
\operatorname{Tr}(Q_w)=e_2^tAu
=-\delta a(2r_1+r_4)
\]
\[
=-D(D-2)(D^7-18D^6+127D^5-480D^4
                     +1088D^3-1536D^2+1280D-512),
\]
which expands to (R4.3).

For an additional independently checkable multiplication certificate, the only nonzero diagonal entries of the full eleven-factor product are the first and fourth:
\[
\begin{aligned}
(Q_w)_{11}={}&D^{10}-20D^9+180D^8-951D^7+3246D^6\\
&-7440D^5+11520D^4-11712D^3+7168D^2-2048D,\\
(Q_w)_{44}={}&-D^{10}+19D^9-160D^8+788D^7-2512D^6\\
&+5392D^5-7808D^4+7360D^3-4096D^2+1024D.
\end{aligned}
\tag{R4.4}
\]
Their sum is again \(p(D)\).

Since \(D=(v+v^{-1})^2\), the coefficients of \(v^{18}\) and \(v^{-18}\) in \(p(D)\) are both \(-1\); all lower powers of \(D\) have Laurent degree at most 16 and cannot affect these coefficients. For completeness the full Laurent polynomial is
\[
\begin{aligned}
p(D)={}&-(v^{18}+v^{-18})+2(v^{16}+v^{-16})
 +4(v^{14}+v^{-14})\\
&+36(v^{12}+v^{-12})+67(v^{10}+v^{-10})
 +176(v^8+v^{-8})\\
&+297(v^6+v^{-6})+476(v^4+v^{-4})
 +657(v^2+v^{-2})+668.
\end{aligned}
\tag{R4.5}
\]
This is a basis-independent negative Laurent trace, not merely a negative entry in the source basis. It is also negative at the explicit real specialization
\[
p((3+3^{-1})^2)
=-\frac{99834597608550400}{387420489}<0.
\tag{R4.6}
\]
No assertion that the specialized module remains irreducible is needed for this numerical trace statement.

## 4. Convert it to a named P-word on an actual full-algebra simple

Let \(N^\#\) be the source's \(\Theta^{\mathrm{op}}\)-contragredient of \(N\). With the dual basis and the consistent right-action convention,
\[
\rho_{N^\#}(P_i)=Q_i^t.
\]
Thus for the reversed word
\[
w^{\mathrm{rev}}=(2,3,2,3,2,3,1,2,1,2,1)
\]
one has the exact identity
\[
\operatorname{Tr}_{N^\#}(P_{w^{\mathrm{rev}}})
=\operatorname{Tr}\big((Q_w)^t\big)=p(D).
\tag{R4.7}
\]
This explicit reversal avoids silently replacing the source's anti-involution convention by an automorphism convention. Proposition 11.12 (108) also identifies \(N^\diamond\simeq N\), so an equivalent twist formulation is possible, but it is unnecessary for (R4.7).

The source's §11.8 lists \(N^\#\) as one of the nine distinct generic simple modules of the full \(\check H_4\). Its occurrence in an actual tensor power can also be seen directly. Over the generic field,
\[
N\subset S^2 M_{(3,1)}
\subset M_{(3,1)}\otimes M_{(3,1)}
\]
is a direct summand by (99) and the symmetric/exterior decomposition. Apply the exact contragredient \(\#\). Proposition 11.12 (101), together with Proposition 11.11, gives
\[
N^\#\ \subset\
\operatorname{Res}_{\check H_4}
\big(M_{(2,1,1)}\otimes M_{(3,1)}\big)
\tag{R4.8}
\]
as a direct summand.

Ordinary quantum Schur–Weyl duality places the right-hand side in
\((V\otimes W)^{\otimes4}\) whenever \(\dim V\ge3\) and \(\dim W\ge2\), or with the two factors interchanged. In the concrete case \((\dim V,\dim W)=(3,2)\), the ordinary left factors \(V_{(2,1,1)}\) and \(W_{(3,1)}\) are both three-dimensional, so this particular ordinary isotypic component contains nine copies of \(N^\#\). The existence statement does not require that multiplicity count. Taking both dimensions at least three also works.

Theorem 12.1 and §12.2 identify this restriction as the actual nonstandard tensor action, not a newly invented representation with the same dimension. The source's immediately following \(X/X^*\) convention remark is retained: consistently transposing the presentation reverses word order and leaves the relevant trace obstruction unchanged.

## 5. Consequences and their precise scope

### 5.1 No strict effective matrix-kernel model on this simple

If a simultaneous matrix representation of the \(P_i\) on \(N^\#\) had all entries in \(\mathbb N[v,v^{-1}]\), every matrix entry of every word, and in particular every word trace, would be in \(\mathbb N[v,v^{-1}]\). Equation (R4.7) contradicts this. Similarity over a larger coefficient field cannot change the trace.

The same argument excludes a finite-state graded-vector-space kernel realization whose split Grothendieck module is this specified simple module and whose named \(P_i\) are represented by effective kernels. Composition and direct sum make every word trace a nonnegative Laurent polynomial. This rules out extending the strict F56 construction simple by simple to every full \(\check H_4\) simple while retaining the named generators.

Indeed (R4.6) proves that, on the displayed specialization of \(N^\#\) at \(v=3\), there is no real basis in which all three \(P_i\) have entrywise nonnegative matrices. The trace of a product of entrywise nonnegative real matrices is nonnegative.

One can also phrase the obstruction on a larger module if an effective kernel projector onto this specified isotypic component is required: the inserted trace is a positive multiplicity times \(p(D)\), again impossible for effective matrices. The premise that this projector is itself represented effectively is extra data. A positive basis for the entire tensor space need not make its abstract direct-summand projections effective.

### 5.2 No genuine finite Weil power trace for this word under grading retuning

Fix \(q>1\). If \(v=q^{n/2}\), equation (R4.5) is a finite power sum in \(n\), with distinct roots \(q^{e/2}\) and coefficients equal to its Laurent coefficients. In particular the roots \(q^9,q^{-9}\) have coefficient \(-1\).

Suppose this sequence were \(\operatorname{Tr}(F^n;H)\) for every sufficiently large \(n\), where \(H\) is a finite-dimensional vector space and \(F\) is an invertible endomorphism. Grouping equal eigenvalues expresses this trace with nonnegative integer multiplicities; Jordan blocks do not affect the power trace. Subtract the two expressions. Vandermonde independence of finitely many distinct nonzero exponential sequences forces all grouped coefficients to vanish, contradicting the multiplicity \(-1\) at \(q^9\). The same proof works for \(v=q^{-n/2}\), since (R4.5) is invariant under \(v\leftrightarrow v^{-1}\).

This excludes a genuine finite cohomological degree represented by its ordinary Frobenius power trace. It does not exclude an alternating derived trace, a virtual class, or the trace of an inserted endomorphism against Frobenius, which may have signed coefficients. It also does not identify arithmetic retuning with the actual quantum grading without a comparison axiom.

The same argument excludes an overall parity shift: \(p(D)\) has both negative coefficients and positive coefficients (for example, its constant Laurent coefficient is 668), so neither \(p(D)\) nor \(-p(D)\) is a genuine finite power trace. A fixed Tate twist multiplies every exponential root by the same nonzero power of \(q\), preserving distinctness and every coefficient sign. It cannot repair this obstruction. Several cohomological degrees with an alternating trace remain outside this exclusion.

### 5.3 What remains open in this calculation

The negative \(P\)-word lies on the additional full-algebra \(N^\#\) block. This block is omitted from the two-row quotient in Theorem 13.4. The calculation therefore does not obstruct a \(P_i\)-only positive-kernel construction for the two-row rank-four tensor module, nor does it contradict Example 19.3 or Remark 11.19's signed/factored positivity.

On the original \(N\), the same polynomial is a \(Q\)-word trace. The fact that \(Q_i=D-P_i\) is a subtraction means that positivity of \(P_i\)-kernels alone does not imply positivity of \(Q_i\)-kernels.

No claim is made that this is the earliest negative word in all possible presentations, or that the source authors claimed strict positivity that this refutes. The result narrows the auxiliary effective-kernel route and the arithmetic comparison for a specified actual summand.

## 6. Reproducible exact and finite checks

The standalone exact certificate is

/workspace/scratch/b5024d19aacd/GCT_NSRH_work/verify_rank4_negative_trace.py

with output

/workspace/scratch/b5024d19aacd/GCT_NSRH_work/verify_rank4_negative_trace_output.txt.

It independently contains the three Figure 22 matrices, multiplies the full word, checks every entry of (R4.4), checks the rank-one product reduction, checks the explicit dual-transpose word, expands the complete Laurent polynomial, computes the exact \(v=3\) value, and verifies the quadratic/far/adjacent degree-five identities. It uses exact SymPy arithmetic only.

The exploratory helper is

/workspace/scratch/b5024d19aacd/GCT_NSRH_work/verify_rank4_source_cells.py.

It separately transcribes both Figures 21 and 22. Its output files are

/workspace/scratch/b5024d19aacd/GCT_NSRH_work/verify_rank4_source_cells_output.txt

and

/workspace/scratch/b5024d19aacd/GCT_NSRH_work/verify_rank4_source_short_output.txt.

The first run checked every word with no adjacent repeated letter through length nine (1533 words), for each of \(P\) and \(Q\) on both the five- and six-dimensional blocks. All those traces had nonnegative Laurent coefficients. It then requested 200 seeded words of lengths at most 30 per system, seed 562104. Each of \(6P,6Q,5P\) completed all 200 with no negative coefficient; the \(5Q\) run stopped at its thirteenth word after finding a negative coefficient, subsequently shortened to (R4.2). The second run checked all 3069 words through length ten on \(5Q\), then found a length-eleven word with the same polynomial after 32 additional words. These are finite observations, not positivity theorems.

The helper also verifies a four-edge cycle in Figure 21 with coefficient product
\[
-D(D-4)(D-2).
\]
For real \(v>1\) this is negative and invariant under rescaling the four basis vectors. Thus diagonal rescaling of that displayed six-dimensional basis cannot make all its \(P_i\), or all its \(Q_i\), entrywise nonnegative. This is strictly a displayed-basis limitation; it is not the basis-independent negative-trace result proved for \(N^\#\).

## 7. Check-event suggestions

1. Source read: whole relevant supplied TeX contexts (§11.1–§11.4, §11.8, §12.1–§12.2, §13.6, Conjecture 19.1 and Example 19.3 with both graphs); numbered locators matched to the primary PDF. Record source verification, not a new proof of the cited representation classification.
2. Exact algebra: full matrices, product diagonal, rank-one reduction, word reversal, Laurent coefficients, and exact real specialization reconstructed and checked. Record exact symbolic verification plus an explicit written proof.
3. New proof: effective-kernel obstruction and genuine finite power-trace obstruction follow from matrix positivity and Vandermonde independence. These are scoped deductions, not source theorems.
4. Finite search: record counts and seed exactly; do not label a failed search a proof of positivity.
5. Independent review: pending a separate whole-report read at the time this report is first written. The independent checker has already reported an independent visual transcription of Figure 22 and an exact symbolic match of the trace, but a full final-text verdict must be recorded separately.

Primary web reference IDs retrieved by this author include turn434059520view0–2, turn663324649view0–2, and turn861211656view0–1. The root must open the source independently before using these as final citations, per the tool policy.

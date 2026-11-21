# Independent audit of the fat-arrangement and diagonal-quotient models

Statements **A-050** (G027) and **A-051** (T049). Checked on
21 November 2026 by GPT-6 Astra Pro, run /root/archive_audit;
effort setting not exposed.

## A-050. The complete G027 model

**Result: complete proof PASS.** The whole report
work/root/fat_linear_arrangement_model.md, FA.1–FA.17,
including its revised coherent-to-locally-free comparison,
was read. Its exact normal-order morphism, local and
global exactness, stabilizer actions and complete flag
dictionary all pass.

### The normal-order map and Cauchy extraction

Put \(r=m-2\). The degree-\(N\) Cauchy decomposition of
\(\operatorname{Sym}(E\otimes F)\) contains precisely the
partitions with at most \(r\) rows. The quotient
\(E\to Q\) gives an actual map
\(S_\alpha E\to H^0(S_\alpha Q)\).
The primitive-idempotent image of
\([\mathcal O(-1)\to E]^{\otimes N}\), with its Koszul
signs, has degree-\(j\) terms indexed by vertical
\(j\)-strips. Thus \(j\le r\). Every negative line
twist \(\mathcal O(-j)\), \(1\le j\le r\), is acyclic
on \(\mathbf P^r\). The locally split tensor
contraction proves exactness before taking sections,
so the quotient map itself induces the asserted
section isomorphism.

At the frame point represented by \(e_0=\ell_i\),
the moving quotient sends
\[
e_0\longmapsto-\sum_jx_je_j.
\]
Its induced algebra map is exactly
\[
Y_{0a}\longmapsto-\sum_jx_jY_{ja}.
\tag{FR1}
\]
Over the fraction field in the remaining rows, the
\(r\times r\) matrix \(Y=(Y_{ja})\) is invertible.
Consequently the least nonzero homogeneous degree
in the \(Y_0\) variables survives (FR1) as exactly
the same \(x\)-degree. Later homogeneous pieces have
larger degree and cannot cancel it. The polynomial
coefficients in the other rows encode the entire
Schur component faithfully. Therefore membership in
\(I_i^k\) is equivalent to order-\(k\) vanishing
of the section, and intersection over all frame
points gives the actual isomorphism FA.2. This
checks the order, rather than merely the value at
the point.

### Product, saturation and the signed complex

At a homogeneous prime different from the irrelevant
ideal, at most \(m-2\) of the \(I_i\) are contained
in that prime: any \(m-1\) frame vectors span \(E\).
Their independent vectors can be completed to a
basis, making their ideals disjoint variable blocks.
Every other ideal is a unit at the prime. For
disjoint blocks, membership in all \(k\)-th powers
is equivalent to degree at least \(k\) in every
block, which is exactly product membership.
Thus the product and intersection have the same
ideal sheaf.

Each block power is saturated: a complementary
variable does not change membership, so a class
killed by an irrelevant-ideal power is already
zero. Intersections preserve saturation. This
proves that the saturation of \(P_k\) is \(J_k\).
Conca–Herzog applies to the \(mk\) repeated nonzero
linear ideals, giving regularity \(mk\) and saturation
degree at most \(mk\). Hence FA.3 and the required
higher-cohomology vanishing hold in the exact
stated range.

The differential in the restriction complex adds
one index with its ordered-subset sign. A frame
permutation has the sign of reordering the image
subset. This is its actual equivariant orientation
line. On a disjoint-block chart, a monomial survives
in the term for \(A\) precisely when every index
in \(A\) belongs to the set of block powers that
do not contain that monomial. Its augmented complex
is the full simplex on that set, contracted by
inserting its least index. This proves sheaf
exactness with the specified maps.

For a subset of size \(s\le m-2\), the quotient
is free over the polynomial ring in the complementary
variables, with normal-monomial shifts at most
\(s(k-1)\). At \(N\ge mk\), all residual twists are
nonnegative; higher cohomology vanishes and global
sections equal the indicated graded pieces. For
\(s\ge m-1\), already \(m-1\) independent truncated
blocks have maximum degree \((m-1)(k-1)<mk\);
their degree-\(N\) component and sheaf vanish.
Regularity also makes the union sheaf acyclic
in these twists and its sections equal to
\(S_N/(J_k)_N\). These observations prove that
taking global sections gives exactly FA.4,
including its last term and all endpoints.

### Stabilizers, flags and characters

For a subset \(A\), the explicit complement \(W_A\)
consists of the zero-sum vectors supported on the
other letters. If
\(\sum_{i\in A}c_i\ell_i\in W_A\), its coordinates
on \(A\) give
\(c_i=(\sum_jc_j)/m\). Since \(|A|<m\), all
coefficients vanish. The dimension calculation
then proves the stabilizer-equivariant splitting
\[
E=\langle\ell_i:i\in A\rangle\oplus W_A.
\]
It identifies the quotient term with
\[
T_k(F)^{\otimes |A|}
\otimes\operatorname{Sym}(\mathfrak h_{m-|A|}\otimes F).
\]
The subgroup on \(A\) permutes the first tensor
factors, with the additional orientation sign
already specified. A cycle of length \(c\) has
literal tensor trace
\(\sum_{t<k}h_t(X_1^c,\ldots,X_r^c)\).
Only equal basis vectors around a cycle contribute,
so both its polynomial degree and its sign
convention are fixed.

The full exterior-column pairing gives
\[
\alpha=(\lambda_2-\lambda_m,\ldots,
        \lambda_2-\lambda_3).
\]
The line twist cancels against
\((\det Q^*)^{\lambda_2-\lambda_m}\), leaving
exactly \(\operatorname{sgn}^{\lambda_2}\).
The inverse chart is the original
\(u^{n-\lambda_2}F(v(X))\); the proved point-order
criterion keeps it polynomial. At positive \(k\),
\[
|\alpha|=\lambda_1-\lambda_2+mk\ge mk.
\]
At \(k=0\), the direct Schur module is used
separately. This checks every balanced input,
including the zero partition.

### Independent character reconstruction

The program check_fat_arrangement_independent.py
evaluates the restriction complex itself. For a
permutation with fixed cycle lengths, a stable
subset is a union of cycles. Its Euler sign times
its orientation sign is \((-1)^{v_A}\), where
\(v_A\) is its number of selected cycles. The
program multiplies those finite truncations by
the complementary standard symmetric-algebra
character
\[
\frac{\prod_{a=1}^{r}(1-X_a)}
{\prod_{c\text{ unselected}}\prod_{a=1}^{r}(1-X_a^c)}.
\]
Multiplication by the Weyl determinant and literal
coefficient extraction selects \(S_\alpha F\).
This implementation retains the individual subset
terms; it does not use the product simplification
of T049.

The result agrees with the balanced-cycle character
routine in 925 partition cases and 4,823 class traces:

| Outer degree | Inner degrees | Partitions | Positive-\(k\) cases | Class traces |
|---|---:|---:|---:|---:|
| 3 | 0–8 | 215 | 50 | 645 |
| 4 | 0–6 | 396 | 186 | 1,980 |
| 5 | 0–4 | 314 | 188 | 2,198 |

The calculations include \(k\le6\) and
\(|\alpha|\le30\). An additional 404 traces were
compared to literal power-sum cycle-index expansion
and Murnaghan–Nakayama characters. All multiplicity
inner products are nonnegative integers. Exact
case hashes are retained in
FAT_ARRANGEMENT_INDEPENDENT_RECEIPT.json.

### The coherent and locally free \(K_0\) maps

The revised dictionary paragraph is valid.
For completeness, its equivariant resolution
construction terminates by the following direct
argument. At each syzygy \(M_i\), choose an invariant
graded lift of \(M_i/S_+M_i\). Each such space is
finite dimensional, and reductivity of
\(S_m\times GL(F)\) over \(\mathbf Q\) supplies
the lift. The resulting maps
\(S\otimes W_i\to M_i\) are surjective by graded
Nakayama. Their kernels are finitely generated
because \(S\) is Noetherian. This constructs a
minimal equivariant graded free resolution.

If \(D=\dim(E\otimes F)\), the variable Koszul
complex resolves \(\mathbf Q\) in \(D\) steps.
Its exactness follows successively because each
variable is a nonzero divisor modulo its predecessors.
It computes \(\operatorname{Tor}_i^S(M,\mathbf Q)\),
which is zero for \(i>D\). The minimal resolution
has zero differentials after tensoring with
\(\mathbf Q\), so
\[
F_i/S_+F_i=\operatorname{Tor}_i^S(M,\mathbf Q)=0
\quad(i>D).
\]
Graded Nakayama gives \(F_i=0\). Thus the displayed
equivariant resolution is finite, with actual maps.

Sheafification sends each free term to a locally
free equivariant sheaf, and alternating sum gives
its exact \(K_0\) class. Comparison lifts between
resolutions are equivariant because
\(\operatorname{Hom}_{S,G}(S\otimes W,-)\)
is exact; their acyclic mapping cones have zero
alternating class. The same construction on a
short exact sequence gives additivity. This
proves the stated coherent-to-locally-free map,
with its independence of choices.

SGA6 VI Theorem 3.3 was reread in the saved French
transcription: its exact scope is locally free
bounded-rank modules on a **commutatively ringed**
topos. The frame-torsor construction in its proof
is the actual associated-bundle morphism used here.
SGA3 I4.5 and I4.7.2–4.7.3 supply the previously
checked linear-group, coaction and weight-projector
language. SGA6 V4.2,4.4,4.8–4.9 supply the precise
free-\(\lambda\)-ring and rank quotient maps.
The current exact complexes and quotient maps
supply the coherent realization just constructed.

### Primary sources checked for G027

Conca–Herzog, Castelnuovo–Mumford regularity of
products of ideals, arXiv:math/0210065v1:
Theorem 3.1, Lemma 3.2 and Corollary 3.3 on
printed p. 6, and the complete indicated proofs
on pp. 6–7, were read. The repeated-factor
application and exact saturation convention
were verified.
https://arxiv.org/pdf/math/0210065 .

Derksen–Sidman, A sharp bound for the Castelnuovo–
Mumford regularity of subspace arrangements,
Advances in Mathematics172(2002),151–157:
Theorem1.2, printedp153, was opened and read.
Its exact equivalence includes the graded-piece
isomorphism in all degrees at least the regularity
and the asserted sheaf-cohomology vanishing.
https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.10.pdf .

Eisenbud, with a chapter by Sidman, Lectures on
the Geometry of Syzygies, MSRI Publications51(2004):
Theorems1.2–1.3, printedp118, state the Noetherian
and finite graded free-resolution facts used above.
The source explicitly omits their proof on p119;
this audit records a statement read and gives
its own equivariant termination argument above.
https://library.slmath.org/books/Book51/files/04eisenbud.pdf .

EGAI Corollary9.5.2 identifies the ideal kernel
of an affine schematic image, as already verified
in SOURCE_NOTES.md. The original EGAII PDF was
downloaded from Numdam and its relevant text read:
Proposition 2.5.2, printed p.31, constructs the
associated graded-module sheaf by localization and
gluing; Proposition 2.5.4 on that page proves its
exactness. Propositions 2.5.7–2.5.9, printed p.32,
identify shifts with invertible twists in the
degree-one-generated case. These are the exact
sheafification and free-term locators used above.
https://www.numdam.org/item/PMIHES_1961__8__5_0.pdf .

## A-051. The complete all-degree quotient theorem T049

**Result: complete proof PASS.** The entire report
work/theta/fat_arrangement_product_report.md,
DP.1–DP.12, was read. It proves the exact
all-degree equality for \(1\le r\le m-2\).

In the independent-block ring \(R\), the ideal
\(D=\prod_i\mathfrak a_i^k\) equals the intersection
by literal block degrees. The oriented subset
restriction complex resolves \(R/D\); its monomial
components have the same explicit simplex
contraction checked above. For a proper subset,
an unselected block can be replaced by the
diagonal variables \(L_a=\sum_iY_{ia}\).
This gives \(R_A=B_A[L_1,\ldots,L_r]\)
with the selected-block relations unchanged.
Thus the Koszul homology in positive degree
vanishes on every proper-subset term.

In the bounded Koszul–restriction bicomplex,
a subset of size \(s\) has cohomological degree
\(q=s-1\), and Koszul degree \(i\) contributes
\(-i\). Proper subsets survive only at \(i=0\),
so \(q-i\ge0\). The full subset has
\(q-i\ge m-1-r\ge1\). No spectral-sequence
entry has negative total degree. Hence the
negative total cohomology vanishes, giving
\[
\operatorname{Tor}_{i>0}^R(R/D,R/(L))=0.
\]
The ideal sequence gives the literal injection
\(D/LD\to R/(L)\) with image \(P_k\), as well
as all positive Tor vanishing for \(D\).
This is the asserted quotient morphism.

The ordered sequence is regular on \(D\):
the last-form mapping-cone sequence makes that
form surjective on the positive Koszul homology
of the preceding sequence. These finitely
generated graded modules are bounded below,
so graded Nakayama makes them zero. Induction
and the same sequence prove the required
injectivity at degree zero.

For each block ideal, \(H^0\) of local cohomology
is zero. Its block Čech complex has no cohomology
below degree one. Tensoring these complexes
over \(\mathbf Q\) gives the full-variable Čech
complex on \(D\); the vector-space Künneth formula
therefore gives \(H^j_{R_+}(D)=0\) for \(j<m\).
Quotienting successively by the regular diagonal
sequence yields
\[
H^j_{S_+}(P_k)=0\quad(j<m-r).
\]
The two vanishing groups \(j=0,1\) imply
saturation. The already checked disjoint-block
local comparison with \(J_k\) then proves
\(P_k=J_k\) in every degree. The separate
\(k=0\) endpoint is the ordinary polynomial
quotient and is included correctly.

The sequence's span is the trivial \(S_m\)
module tensored with \(F\). Its Koszul Euler
factor is exactly \(\prod_a(1-X_a)\).
The literal cycle trace on the tensor product
of block ideals gives each tail
\(\sum_{t\ge k}h_t(X^c)\). Thus DP.3 has
the exact exterior factor and grading.
The forty-eight terms in DP.12 are precisely
the six Weyl-determinant terms and eight
exterior monomials. Its table constraints have
row sums at least \(k\), weighted column sums
equal to the specified exponent, and therefore
bounded coordinates. Their signs and the
balanced \(\operatorname{sgn}^{\lambda_2}\)
transport agree with A-050.

No separate all-degree numerical ideal-rank
experiment is counted in A-051. The 4,823
subset-character comparisons in A-050 are
independent evidence for its high-degree
specialization; the all-degree extension is
established by the complete quotient and
local-cohomology proof just checked.


### A-051 additions: ordinary powers, normal Rees algebra and minimal rank

The added DP.13–DP.17 and §§5–7 were also read completely.
Their proofs pass, with the exact base of the finite-resolution
transport clarified in the source report.

Regrouping the literal ideal product gives
\(J_k=(J_1)^k\). For each block, least total block degree is
additive on products because the associated graded polynomial
ring is a domain. It therefore extends to a discrete valuation
\(v_i\) of the fraction field. In an ideal-integrality equation,
a value \(v_i(f)<k\) would make its leading monic power the unique
term of least valuation. This proves integral closure of every
\(J_k\) by the actual block-order test.

The Gauss extension with \(w_i(t)=-1\) is multiplicative:
after writing \(u=\pi_i t\), its leading residue polynomials
multiply in a polynomial domain. Thus
\[
\mathcal R=S[t]\cap\bigcap_i\{z:w_i(z)\ge0\}
\]
is a literal equality inside \(\operatorname{Frac}(S)(t)\);
each coefficient satisfies exactly all required ideal orders.
Each factor in the intersection is integrally closed, so the
given Rees algebra is normal.

For a degree-one generator \(ft\), the degree-zero localization
is precisely \(S[J_1/f]\), by the displayed ratios \(gt/(ft)=g/f\).
An element integral over that chart lies in the full localized
normal Rees algebra. If it belongs to the degree-zero fraction
field, the grading puts it in the degree-zero subring itself.
This proves chart normality. EGAII 2.4.1–2.4.2, printed p.28,
is the checked chart-gluing and scheme locator.

With \(r'=\ell(\alpha)\le m-2\), a maximal nonzero minor of the
remaining \((m-2)\)-by-\(r'\) generic matrix proves that the
normal-variable substitution remains injective and preserves
least degree. The Young complex has only negative twists
through \(-r'\), so the same section map is still an isomorphism.
The empty partition and positive vanishing-order endpoint are
handled directly. For \(r'=1\), the product ideal is literally
generated by \(\Delta^k\), with \(\Delta=\prod_i\ell_i\);
frame permutations fix this product. This proves the stated
rank-one module formula and its exact sign transport.

The finite equivariant free resolutions are over the polynomial
ring \(S\). Their coherent-to-locally-free transport is on
\(\operatorname{Spec}S\), or after exact sheafification on
\(\operatorname{Proj}S\). The revised paragraph states this
base explicitly. The Rees-Proj action and normal chart assertions
are supplied by their own specified coactions and chart maps.



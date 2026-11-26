**The attached files.** Besides this file there is one ZIP, `63_COUNTING_VARIETIES.zip`. Unpack it once; there is no ZIP inside it. Everything you need that isn't a published source is in it, so don't rely on any earlier conversation.

# Counting satisfying assignments inside smooth varieties

You are GPT-6 Astra (ChatGPT Pro mode). This is research and paper writing in one task: write the paper below while
you push its open theorem.

## Rank-one Frobenius in every fixed characteristic

Begin the paper with the theorem in `research/Fixed_fields_and_Frobenius/coherent_scalar.tex`. For each fixed prime $p$, a Boolean formula with $S$ satisfying assignments gives a smooth geometrically integral projective hypersurface $X\subset\mathbf P^{d-1}_{\mathbf F_p}$ of degree $d$. Its homogeneous equation is supplied as an arithmetic circuit of polynomial bit size. The group $H^{d-2}(X,\mathcal O_X)$ is a line. In the manuscript’s normalization, its $p$-power Frobenius acts by $S\bmod p$, and $\#X(\mathbf F_p)\equiv 1+S\pmod p$. Distinguish exact residue evaluation from the nonzero decision problem under the smoothness promise. Give the reduction and membership argument for each claim.

Credit the earlier incidence coefficient in C023 and the smooth parity constructions in C030–C032, with their fields and coherent dimensions. Re-derive the Boolean coefficient identity from the formula, including the sign and the normalization at odd primes. For the geometric step take the initial homogeneous polynomial $G$ of degree $u$ in $u$ variables and the manuscript's power $Q$ of $p$, with $m=Q-1>u$ and $m\ge p$. In variables $x_1,\ldots,x_m,y,z$, set
$$
A=G(x_1,\ldots,x_u)\prod_{i=u+1}^m x_i+x_1^m,\qquad
F=yzA+y^{Q+1}+\sum_{i=1}^m x_i^{Q+1}-x_1z^Q.
$$
Verify $d=m+2=Q+1$, the size of the homogeneous circuit and geometric smoothness, including characteristic two. Use $yF_y-zF_z=y^{Q+1}$ to locate a possible common zero of the derivatives, then check $F_y$ there. Derive the Frobenius coefficient on the coherent line from the projective hypersurface exact sequence. Compare the same coefficient with the point-count congruence over $\mathbf F_p$. Work a small formula all the way through, supplying equations, generator and scalar. Credit Nicholas Katz for the coefficient description of this coherent line, Algorithm (2.3.7.14) and Special Case (2.3.7.17), pp. 35–36. Identify the encoding and the smoothness argument contributed here. [Katz’s paper](https://web.math.princeton.edu/~nmk/old/algsoln.pdf)

**Stabilization in families.** Read the short note in `research/Hasse_stabilization/hasse_stabilization.tex` alongside the circuit construction. Set $h_p(G)=[(x_1\cdots x_u)^{p-1}]G^{p-1}$. Prove that *any positive multiple* $Q$ of $p$ with $Q\ge u+2$ gives an affine-linear embedding of the space of degree-$u$ forms into the smooth coefficient chart of degree $d=Q+1$ in $d$ variables, with $h_p(F_G)=h_p(G)$ identically. Taking the least such multiple gives $d\le u+p+2$. Check the padding argument at $Q=p$, relative smoothness over the coefficient space and the trivialization of the coherent line under base change. For the explicit smooth family over the affine $a$-line with Hasse section $a$, compute all three quartic K3 point counts in characteristic three and explain the special fiber at $a=0$. Relate the coefficient identity to Katz’s Dwork-pencil calculation. Which degrees permit an entire such line, and what input-size advantage does the stabilization keep for circuits?

**An exactly computable family.** When the Boolean presentation is supplied with the hypersurface, read Sections 1-3 of `research/Grouped_gate_counts/width_and_gate_syndromes.tex`. For groups of logarithmically many affinely wired AND gates, a fixed-degree binary polynomial may recognize simultaneous success from their group-failure bits. Show how to find that polynomial, use the resulting disjoint affine partition to compute the integer number of witnesses, and hence read the coherent scalar in every fixed characteristic. Check the one-legal-wire-word assumption on the supplied representation. Use the paired chain to explain why a unique satisfying primary input alone does not give a bounded-degree test. Can the geometric presentation reveal the required partition without the original gate wiring? Identify the data a proposed recovery would need. The local calculations are in `grouped_selector_replay.py` and `grouped_moment_window.py` beside the manuscript. For the supplied reversible homogeneous two-bit presentation in `research/Reversible_registers/eliminating_binary_registers.tex`, compute the characteristic-three scalar from the constant Walsh term, find witnesses via the sparse indicator even at residue zero, prove exact-count #P-hardness, and include recognition and reconstruction costs when only the hypersurface is given.

Using `research/Reversible_registers/empty_fibres_and_erasure.tex`, show why deciding whether some fibre of the split finite étale family over $\mathbf F_3$ is empty is NP-complete even when every positive Frobenius iterate has trace zero on $H^0(Y_x,\mathcal O_{Y_x})$ at every base point. From the supplied sparse Walsh presentation, verify the polynomial tests for whether zero trace detects emptiness on every fibre or whether all fibre sizes satisfy a fixed bound, and state what would be needed to recover that presentation from equations or to keep the cohomology rank fixed. The private multiplier in `research/Reversible_registers/digits_of_split_fibres.tex` preserves the empty fibres of an $s$-term Walsh presentation while erasing its first $K$ positive-degree reciprocal zeta coefficients modulo three with $O(s\log(K+1))$ terms. Which geometric presentations retain the bounded-rank row normalization after an affine change hides the multiplier, given that bounded rank of the squared rows suffices for a fixed number of sparse equations in displayed split coordinates and empty-fibre existence across base words is NP-complete for even one bilinear equation without that rank bound?

**The representation of the input matters.** If an equation of degree $d$ in $d$ variables is listed as $t$ monomials, the coefficient of $(x_1\cdots x_d)^{p-1}$ in $F^{p-1}$ is computable by enumerating the $t^{p-1}$ ordered choices of monomials. Give the bit bound for fixed $p$, including binary exponents and coefficients. Compare Daqing Wan’s Theorem 1.1 for a single sparse affine hypersurface over a fixed field and at fixed $p$-adic precision. Explain which products the circuit represents compactly. For a varying polynomially bounded prime, verify the distinct tag attached to each local factor and the Chinese remainder reconstruction across primes. State the number of oracle calls and the uniformity in $p$. [Wan’s paper](https://www.math.uci.edu/~dwan/sparse.pdf)

For the uniform yes/no oracle across primes, prove the reduction that asks only whether the coherent scalar vanishes. On these smooth hypersurfaces relate nonvanishing to Frobenius splitting. Use sufficiently many small primes to decide whether the original formula is satisfiable. Then recover the residue modulo a queried prime $p$ by shifting the assignment count through $S+a$ for $0\le a<p$. Give an explicit parsimonious width-three encoding, including the branch that contributes exactly $a$ extra assignments, and bound the total query count for Chinese remainder reconstruction. For the single sparse hypersurface, verify one polynomial bound on the number of local factors in all the shifted formulas before choosing the primes.

Theorem 4 already gives a polynomial list of explicit homogeneous trinomials in one ordinary projective space, defining a scheme isomorphic over the ground field to the circuit hypersurface. Check the affine charts, agreement on their overlaps, and the scheme structure at infinity. Account for the number of equations, their binary exponents and the dependence of their degrees on circuit depth. Compare the scheme isomorphism with the projective feasibility results of Grenet, Koiran and Portier. In characteristic three the positive unit clause gives 9,953 projective points. Reproduce this calculation. [Grenet, Koiran and Portier](https://arxiv.org/abs/1210.1451v1)

**How many equations are needed?** For fixed $p$ and at most $c$ homogeneous sparse equations, derive the point count modulo $p$ by summing $\prod_i(1-f_i^{p-1})$ on the affine cone. Allow binary exponents, unbounded ambient dimension, and arbitrary common zero schemes. Give the bit cost from $\prod_i(1+T_i^{p-1})$, where $T_i$ counts the terms of $f_i$. Explain the resulting computational obstruction to a uniform bounded-equation presentation of the hard family. State the complexity assumption precisely. Group choices by multiplicity to obtain the fixed-prime polynomial bound for logarithmically many trinomials. Compare this counting argument with Gopalan, Guruswami and Lipton’s treatment of systems of sparse equations. [Gopalan, Guruswami and Lipton, §§3.1, 3.3](https://www.cs.cmu.edu/~venkatg/pubs/papers/mod-root-count.pdf)

For Theorem 6, start with a smooth hypersurface $X^n\subset\mathbf P^{n+1}$ of degree $\delta\ge2$ and $n\ge3$. Prove the restriction on isomorphic reembeddings. If the new hyperplane class is $H$, the map is linear in the original coordinates. If it is $aH$ with $a\ge2$, the ambient dimension is at least $2n+1$ and the image has degree $a^n\delta$. Identify the Picard calculation in SGA 2, Exposé XII, Corollaire 3.7, including its dimension hypothesis. Read the complete English edition under `latex_sources/SGA2_EN/` and compare the French statement on p. 121 of the Laszlo edition. Compare Zak’s quadratic-secant theorem with the argument using contraction in arbitrary characteristic. Explain why the optimal projection over an algebraic closure exists and what must be constructed over the stated finite field. [SGA 2, Exposé XII, Corollaire 3.7](https://arxiv.org/pdf/math/0511279v1#page=129) · [Zak, Proposition 1.3(a), Theorem 3.3 and Example 6.6](https://doi.org/10.1007/s002080050271) · [Zak’s full article, uploaded by the author](https://www.researchgate.net/publication/225418238_Projective_invariants_of_quadratic_embeddings)

For a smooth geometrically integral anticanonical global complete intersection of dimension $d=N-c\ge1$, derive $\#X(\mathbf F_p)\equiv1+(-1)^d\alpha\pmod p$. In Theorem 8, when any number of homogeneous sparse inputs generate the saturated ideal $I_X$ as an ideal, recover the coherent scalar $\alpha$ from $c$-element sublists whose degrees sum to $N+1$. Prove the determinant identity that makes every nonzero candidate equal to $\alpha$ and bound the running time by $T^{c(p-1)}\operatorname{poly}(L)$ for $T$ input terms and $L$ input bits. Give Kudo’s coefficient formula for a regular sequence. Work out the plane cubic $g=y^2z-x^3-xz^2$ over $\mathbf F_5$ ($\alpha=2$, four rational points). The quartics $xg,yg,zg$ exhibit exactly where the sublist argument uses generation before saturation. [Kudo, Proposition 4.2.1 and Algorithm II](https://arxiv.org/abs/1704.08110v1)

In Theorem 9, allow an arbitrary number of sparse linear equations and a fixed number of nonlinear equations. Over $\mathbf F_2$, show how each product of monomials pins binary coordinates and how rank computes its contribution. Check the extension to counts modulo each fixed $2^b$. For positive-dimensional anticanonical complete intersections in characteristic two, derive the determinant algorithm on the linear subspace for the absolute semilinear scalar and the norm criterion over $\mathbf F_{2^h}$. At every fixed odd $p$, prove that deciding nonvanishing on the smooth promise is $\mathrm{Mod}_p\mathrm P$-complete. Reconstruct the smooth complete intersection of multidegree $(1^k,d)$, with at most three terms per linear equation and at most $d+p$ in the single nonlinear equation. Derive the coherent scalar from Valiant’s permanent identity, including the invertible power of four. Relate the unbounded linear codimension $k$ to the hypothesis in the bounded-equation algorithm. Verify the ternary example with 10,065 projective points. [Valiant, Lemmas 3.1–3.2](https://www.cs.bu.edu/faculty/gacs/courses/cs535/papers/Valiant_permanent.pdf)

**Open presentation questions.** Give an algorithm or a reduction for a long sparse list known only to satisfy $(f_1,\ldots,f_s):\mathfrak m^\infty=I_X$ at fixed $p,c$. In its original linear span, can a nonsingular change of coordinates make the hard hypersurface sparse, or can a polynomial-length list of sparse multiples define it after saturation? Specify the number of equations and explain whether adjoining new coordinates changes the question. At odd primes, investigate how the largest support of any monomial in the nonlinear equation affects the computational boundary when many linear constraints are permitted. For an affine comparison, examine the single binomial $y\prod w_i-1$ with linear constraints. Describe the nowhere-zero vectors of the associated code and compare Björklund and Kaski’s account of the Crapo–Rota critical theorem. [Björklund and Kaski, §1.3](https://arxiv.org/abs/2003.03595v2)

**Affine hyperplane complements.** Read `research/Arrangement_complements/arrangement_complements.tex`. For every fixed $q>2$ reconstruct the parsimonious reduction from width-three SAT to the rational points of the smooth geometrically integral affine complete intersection $w_i=L_i(x)$, $y\prod_iw_i=1$. Compare the binary-field exact count by row reduction. Over $\mathbf F_{p^d}$, on the Boolean cube of the $r$ input bits and the output bit alone, prove that the positive-arity OR graph is the common nonvanishing set of affine forms exactly for $r\le d(p-1)$, and the minimum there is $r$. Separate the unary conditions enforcing the cube and track every auxiliary coordinate used when gates are composed. Derive the lower bounds from the punctured-cube theorem of Alon and Füredi and the elementary abelian Davenport constant proved by Kruyswijk and Olson. Reproduce the sharp construction and the exhaustive small-field checks. Relate the parsimonious count to Barbanchon’s pinned three-colourings and the full-support codeword construction of Crapo and Rota. If $C(s)=\sum_jc_js^j$ is the affine arrangement polynomial, derive $Z(U,T)=\prod_j(1-q^jT)^{-c_j}$ and $\chi_M(0)=-C(0)\equiv-S\pmod q$ for the central matroid. Explain which multiplicities carry the hard residue and why the Boolean bijection is specific to the ground field. [Kruyswijk and Olson, as recorded in Theorem 2.1](https://ir.cwi.nl/pub/7240/7240D.pdf) · [Bishnoi, Clark, Potukuchi and Schmitt, Theorem 6.1(c)](https://community.middlebury.edu/~jschmitt/papers/on_zeros_of_a_polynomial_in_a_finite_grid.pdf)

Can a *different* smooth bounded-codimension projective scheme realize the same scalar with a polynomial-size explicit presentation? Specify its coherent group, all input equations, and the exact role of their number. For the homogeneous trinomials in Theorem 4, seek an effective scheme-preserving compression over the input field. Quantify the rational projection center or field extension when projecting, the number and sparsity of the output equations, and the cost of producing them. Compare Cheng, Rojas and Wan’s deterministic reduction to $r$ equations with the same radical for equal-degree forms in $r$ variables over fields with $q>rD^{r-1}$, where $D$ is the common degree. Retain the small-zeta and invariant questions below and specify the input model for each. [Cheng, Rojas and Wan, Theorem 3.2](https://arxiv.org/pdf/2007.13214v1#page=6)

## Why this matters

Computing zeta functions, recognising affine space and reading Frobenius on cohomology are central algorithmic
questions of arithmetic geometry. We have very simple smooth varieties into which #SAT is written exactly, in their
motive, their cohomology and their Frobenius. They show precisely where purity and the Riemann hypothesis over
finite fields stop helping computation: they fix the size of the eigenvalues, while the hard number sits in a
multiplicity.

## Where it stands

(Our ids in brackets are for the crosswalk. N is the number of satisfying assignments of a formula. Take each exact
statement, encoding and reduction from the attached proofs.)

1. **A smooth sparse cubic over Z** [C027, S016–S018] with [X] = L^(v+h) + N·L^h, with its Chow ring and homotopy type
   (a wedge of N motivic spheres). Recognising affine space among these is equivalent to unsatisfiability.
2. **A smooth projective curve** [C026] with #C(F_q) = 1 + 2N, for the q of the construction.
3. **Frobenius on coherent cohomology** [C023, C024, C030–C032]: the Hasse–Witt scalar of an explicit smooth
   hypersurface over F_(2^b) is ⊕P-hard by a deterministic reduction; over F_4 the Frobenius scalar is ⊕P-complete;
   over F_2 a smooth projective model needs only four-dimensional coherent cohomology.
4. **Comparisons and invariants** [C028, S018]: comparing embeddings of Tate cohomology is PP-complete, and the rank
   of a graded piece of the γ-filtration is #P-complete.

None of this needs GRH or the theorem that ETH is false; keep both out of the main theorems. Claude Opus 5.5 at
effort high checked the mechanism of C023 and C024 and read the other statements without their proofs. So check each
proof whole, especially the bit size of every input, whether smoothness is proved or promised, and the field.

## Counting over finite fields

Write $S$ for the number of satisfying assignments and $N$ for an order of roots of unity. Read `research/Fixed_fields_and_Frobenius/fixed_field_multiplicities.tex` for the constructions below. For each comparison, identify the input, the invariant and the reduction.

* **Roots in a varying extension.** Alexey Milovanov, *Information Processing Letters* 142 (2019), Theorem 1, p. 77 and §3, pp. 78–79, fixes a prime $p$. The extension degree $n$ is given in unary, the coefficients lie in $\mathbf F_{p^n}$, and the exponents are binary. His deterministic parsimonious reduction gives one sparse polynomial with exactly $S$ roots in that field. His earlier preprint treats characteristic two. Cite the journal version for general $p$. [Journal article](https://doi.org/10.1016/j.ipl.2018.09.008) · [Earlier preprint](https://arxiv.org/abs/1608.07564v1)
* **Common roots with fixed coefficients.** Yichuan Cao, Ruyong Feng, Xiao-Shan Gao, Qiao-Long Huang and Ruichen Qiu, §2.3, Proposition 9, pp. 5–7, reduce 3SAT deterministically in polynomial bit time to noncoprimality of two sparse univariate polynomials over any fixed computable field of positive characteristic, including $\mathbf F_2$. The common root is sought in the algebraic closure. Credit Lemma 7, pp. 4–5, and the clause packing in (7)–(8). Verify how the attached manuscript equalizes the numbers of representatives of the satisfying assignments. [Author preprint, v2](https://arxiv.org/abs/2606.12144v2)

**A test for the sign-only proof.** In the binary construction let $B=X^N-1$ and $Z=V(H,B)$, with $N$ odd. Verify that $Z$ is finite étale and equals the reduced repeated-root locus of $H^4+XB^2$. Compute the size of the sparse input and the bit lengths of $K$ and $L$. Show why all $KS$ geometric points have order $N$, hence Frobenius orbit length $L=\operatorname{ord}_N(2)$. Derive the extension counts $a_s=\#Z(\mathbf F_{2^s})$ and the full zeta function
$$
Z(Z,t)=(1-t^L)^{-KS/L}.
$$
Include $S=0$. Determine the multiplicity of each $L$th root of unity on geometric $H^0$ over $\overline{\mathbf Q}_\ell$, $\ell\ne 2$. The input gives sparse equations. The expanded monic gcd can require a different input size.

Read Theorem 1(b), p. 1, Proposition 4, p. 5, and the dimension-zero argument in §8, p. 8, of *A short proof of Deligne’s bound for Frobenius eigenvalues, after Alpöge*. To apply Proposition 4 in positive dimension, take $U=\mathbf G_m\times Z$, $Y=\{1\}\times Z$, the constant sheaf and $k=d=1$. Check restriction in degree zero and the Gysin map on each geometric component. Treat empty $Z$ separately. Compute $M_s=(2^s-1)a_s$, $N_s=a_s$ and $2^sN_s-M_s$. Identify the cohomology representation giving that remainder. Which unknown multiplicity survives the weight estimate? [Hexagon preprint and author source, v1](https://hexagonmath.org/2611.00789v1)

**Genus and geometric $p$-rank.** Reduce $H$ modulo $B$ in sparse form to obtain $A$ of degree less than $N$. For the curve $Y^2-Y=A/B$, use the smooth affine model $BW=1$, $Y^2-Y=AW$. Prove geometric connectedness and count its geometric simple poles after cancellation. Check $X=1$ and infinity. Apply the different formula and Pries–Zhu, Lemma 2.6, p. 712, to the smooth projective curve specified by this function field. Recover its genus and $2$-rank from $N-KS$, the number of poles. [Pries and Zhu](https://doi.org/10.5802/aif.2692)

For every fixed prime $p$, examine the separate construction with variable primes $\ell_i$ and tag prime $q$, all $-1\bmod 4p$. Verify that choosing half the primitive tag roots makes
$$
K_* = \frac{q-1}{2}\prod_i\frac{\ell_i-1}{2}
$$
prime to $p$. Verify $L=\operatorname{ord}_N(p)\mid K_*$ and that the common roots of $A,B$ are exactly $K_*S$ primitive $N$th roots. Homogenize the equations to degree $N$ in $\mathbf P^1$ and check infinity. This gives the finite scheme by sparse projective equations. Record its empty and geometrically disconnected cases. For the curve $Y^p-Y=A/B$, prove the formula $g=(p-1)(N-1-K_*S)$ for both genus and geometric $p$-rank. Decode $S\bmod p$ from either invariant modulo $p$. Work out $\ell_1=7$, $q=23$, $p=2$ by hand, including $N=161$ and $L=K_*=33$. In characteristic three, the choices $\ell_1=11$ and $q=23$ give $N=253$ and $K_*=L=55$. Check the decoding for zero, one and two satisfying assignments.

**The scalar on coherent cohomology.** For the projective finite scheme, decompose $H^0(Z,\mathcal O_Z)$ into residue fields. Compute the traces of the $\mathbf F_p$-linear $p$-power map $F$ and its binary-specified iterate $F^L$. As a control in growing ambient dimension, homogenize Milovanov’s Boolean equations $X_i(X_i-V)=0$ and the clause-violation products in $\mathbf P^n$. Check infinity and compute the trace of $F$ on the algebra of $S$ rational points. Compare the dimensions used by these constructions with $\dim H^1(C,\mathcal O_C)$ for the curve. Compare both with the coherent line of the circuit-defined hypersurface. State what the corresponding scalar question asks for when the projective input must list every monomial in every equation.

## The paper

One paper that an algebraic geometer and a complexity theorist can both read. Work one formula with two variables
all the way to its cubic, its points and its Frobenius. Set every theorem against what is known: NP-hardness and
#P-hardness of point counting and of zeta functions (von zur Gathen–Karpinski–Shparlinski, Wan, Lauder–Wan, Harvey),
Hasse–Witt computations, hypersurfaces isomorphic to affine space, and universality theorems for matroid
representation spaces and for tensor isomorphism.

## The research

1. **The main question:** every prime p, with completeness, smoothness, projectivity and small coherent cohomology.
2. **Small zeta functions:** the least total Betti number in which #SAT, or #SAT modulo p, can be written into a
   smooth projective variety of polynomial size.
3. **The limit:** decide whether any of the natural invariants with a polynomial algorithm (say which) can recover N
   modulo an odd prime on these families.

## The papers grow with the research

This is research and writing in one task. You are the author of the papers: you prove, and you write each result up
when it is proved.

- **Start with the paper.** Write the main theorems above into LaTeX with their full proofs, checking every step as you
  write. The first checkpoint already holds a compiling draft of each paper. From then on every checkpoint holds the
  newest draft, and a result you prove or correct enters its paper before the next checkpoint.
  Keep each paper editable on its own. Include its main TeX file, every local input, its bibliography
  (or inline references), any custom style and the editable source of its figures. Give the exact build
  command and engine in a short BUILD.md. Compile each changed paper from a fresh copy of its returned
  project, with standard TeX packages available, and include the resulting PDF alongside the source.
- **Then push the mathematics**, and let each paper grow with it. When a new result makes an older one a special case,
  restructure the paper around the stronger one.
- **Before anything is called new**, search: arXiv, the journals, the authors' pages, ECCC, and Hexagon
  (https://hexagonmath.org), in general mathematical terms, following the citations forwards from each work named
  here. Known results are cited with the exact statement and page, and are not proved again unless the form you need
  isn't in the source. Where an earlier work has a result of ours, cite it and present ours as what it is. Make no
  claim of priority and don't argue about one: say what each earlier work proves and what is proved here.

## What a paper has to be

A mathematician who has never seen our project, reading on a phone, understands from the first page what was believed
or conjectured, by whom and where, and what is now a theorem. An expert can check every line without any other file of
ours. Write an ordinary, good research paper, with the patience of one:

Correct and completely proved is the baseline, and a paper that stops there has failed its reader. The opening ticks
each of these boxes, in a short paper above all, concisely and without making a production of it:

1. **The title** says the theorem or question as the field knows it, and names whose theorem, conjecture or programme
   it is. Where we carry out someone's idea, it says "after" that person. It doesn't name a result by a technique, or
   by what the proof avoids.
2. **The abstract's first sentence** says whose work this answers or starts from, and what that work did. Then, with
   as few symbols as it can: what is proved, what is granted, and why it matters. Its last sentence says who produced
   and who checked it, and that no human has.
3. **The theorem in words.** Section 1 states each main theorem in full, with every hypothesis and input, and then
   says what it means, and names the famous statement that it implies or refutes.
4. **Why anyone should care:** the field, the question or programme that depended on it, and what changes now. A
   plain sentence that a result matters is allowed and wanted, at its true scope.
5. **The credit, split exactly.** What the source proved, conjectured or sketched, by statement, page or footnote;
   then what is supplied here. An idea of someone else's is theirs in the title, in the abstract and in Section 1.
   Name also those whose theorem carries the proof. Say nothing about the rest of their work that isn't proved here.
6. **The context.** The earlier theorems and proofs, compared by statement and by ingredients, never by merit; the
   neighbouring work that changed the picture, recent results and those of AI laboratories (OpenAI's among them)
   included, each opened and cited with a sentence on how it bears on this paper.
7. **The scope:** what follows and what isn't proved, in the same place.
8. **The proof overview,** a section headed "Proof overview", in prose before the proofs: the difficulty, the idea
   that overcomes it, and where each hypothesis is used.

An example of the difference is our note hexagon:2611.00789 (https://hexagonmath.org/2611.00789). Its draft was
correct and concise. It was called "Deligne's purity theorem without monodromy", gave the source of its idea one
clause, and went from the theorem straight to the lemmas. The published text is called "A short proof of Deligne's
bound for Frobenius eigenvalues, after Alpöge". It opens with Alpöge's sketch, separates those ideas from what is
written out, says that this is the Riemann hypothesis for varieties over finite fields, compares with Deligne's
ingredients, and explains the mechanism before it proves anything. Write the second kind.

After the opening:

- **The body** gives the proofs in the order of the argument; each section's first sentence says what it is for. Every new result is proved in full, in sentences.
  Define each symbol before it is used, name objects by what they are, and work the smallest instructive example by
  hand. A long calculation says what is computed, by which method, from which input and with which result.
- **What remains open** is stated exactly at the end, with the obstruction.
- **A short closing note on method** says that the mathematics and text were produced by GPT-6 Astra (ChatGPT Pro
  mode), names the checks by others with model and effort as their records give them, says that no human has checked
  it, dedicates our text to the public domain under CC0 1.0, and links the workbench.

A paper never contains run names, internal statement ids, prompts, checkpoints, intakes, agents, local file names or
paths, the history of our drafts, defensive asides, machine headers on statements, or words like "supplied", "actual"
and "retained" used as process words. Programs are cited once, by name, through the workbench. The line of authors
stays empty for us to fill. Length follows the mathematics: don't compress a proof into a summary, and don't pad.

Finished means that you have built each PDF, with no overfull box over 2pt, looked at every page, and read the whole
text twice: as the expert who wants to find the error, and as the newcomer who wants to know the point. Rewrite what
fails either reading.

## Checking

The attached records are evidence, and none of them replaces your check. Reprove or check whole every proof that
enters a paper, with its dependencies. Have each main theorem attacked and re-proved from the statement alone by a
separate worker of this run that hasn't seen the proof, and record it as what it is: a re-proof by the same model. A
statement that fails is corrected in its strongest true form, and the correction is recorded. Every proof is checked
before the paper is called finished.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the
type of what happened, neither more nor less.

Our internal ids belong in two record files, outside the papers: `CROSSWALK.tsv` (paper statement, our earlier ids,
source file, check) and `DICTIONARY.md`, which restates each new finding, with the proof that carries it across, in
the language of algebraic geometry and of our programme on Grothendieck's work (schemes over Z, λ-rings and K-theory,
motives and correspondences, weights), with a cote of the archive only where the attached sources really show the
connection.

## The workbench

The papers of one topic point to one public repository, defined once in each paper as
`\newcommand{\workbenchurl}{https://github.com/KokunoYumeto/arithmetic-geometry-complexity-workbench}`. Deliver the folder `workbench/` ready to be that
repository (or to be added to it): a README a newcomer can read, the papers' sources, a table of every statement with
its proof and check, the check events, and the programs and certificates with exact commands and expected outputs. It
holds only our own work. Cite other people's papers by reference and link, and copy none of them into it.

Its format is format 1 of https://github.com/KokunoYumeto/mathematics-workbenches (`FORMAT.md`): statements with
permanent tags, check events, sources cited and not copied, and a manifest for each version. We give each paper its
number and permanent page when we file it. So every paper also defines
`\newcommand{\recordurl}{https://github.com/KokunoYumeto/mathematics-workbenches}` once and cites it as the
permanent address of its records. We replace that address with the paper's own page. A repository of a field that
isn't open yet opens with its first checked work.

## How to work

The rule that governs everything below: push. Write the papers as you go, and give most of the research time to the
main question: check the rank-one Frobenius and sparse-presentation theorems, then determine what can be computed from sparse equations after saturation, under support bounds, or after an effective compression over the given field. When one approach stalls, take the next one. Deliver nothing while an item is undecided and an
untried approach remains. A gap in a proof is an undecided step: attack it, and never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the
strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a
strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not
movement. After two consecutive reviews without movement, stop that work, finish and check the papers with every
item's state, and deliver; this check takes precedence over the rule about untried approaches.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `COUNTING_VARIETIES_checkpoint_<NN>.zip` with `NN` counting
up. Never overwrite, rename or delete an earlier checkpoint. Save checkpoints once every 45 minutes and at no other
time. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work, so that
a new session can continue from it and the attached files. It is never a JSON file, a recovery file, a summary, or an
export of the newest part only. Each checkpoint zip holds the current deliverables and documentation; earlier
checkpoints are not copied into it.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint,
and continue to the end. Don't write files out in the conversation instead: the work reaches us only through
checkpoint ZIPs and the final ZIP.

## What to deliver

One final ZIP, `COUNTING_VARIETIES_final.zip`:
1. each paper as standalone LaTeX and as a PDF, every finding with its proof, checked and any unchecked findings in
   separate parts, known results cited with exact locators;
2. for each paper a deposit sheet: title, abstract, subject, keywords, the note on method, the place in the text
   of each of the eight boxes, and the authors whose work it carries, so that we can tell them;
3. the folder `workbench/`;
4. `CROSSWALK.tsv`, `DICTIONARY.md`, `QUESTIONS.tsv` (one row for each question: proved, refuted, or, if the session
   ends, its current gate), `LITERATURE.md` (each search, with its date and what it found), `LEDGER.md` and
   `CHECK_EVENTS.tsv`.

An item is finished only when it is proved or refuted. A return may be marked INCOMPLETE only when the session itself
ends. It then gives the state reached, every approach tried with where it failed, and the next step.

## The attached files

- `SOURCE_INDEX.tsv`: 1 file
- `latex_sources/SGA2_EN`: 1 file
- `literature/Cao_et_al`: 5 files
- `literature/Chen_Fu`: 1 file
- `literature/Gopalan_Guruswami_Lipton`: 1 file
- `literature/Grenet_Koiran_Portier`: 1 file
- `literature/Katz`: 1 file
- `literature/Kudo`: 1 file
- `literature/Milovanov`: 2 files
- `literature/Pries_Zhu`: 2 files
- `literature/Valiant`: 1 file
- `literature/Wan`: 1 file
- `ours/NEG_NIGHT_complexity`: 179 files
- `ours/NEG_NIGHT_paper`: 5 files
- `ours/NEG_NIGHT_root`: 47 files
- `ours/intakes`: 32 files
- `published/Sign_only`: 1 file
- `research/Arrangement_complements`: 3 files
- `research/Fixed_fields_and_Frobenius`: 7 files
- `research/Grouped_gate_counts`: 7 files
- `research/Hasse_stabilization`: 2 files
- `research/Reversible_registers`: 14 files

`ours/` is our own work (runs of GPT-6 Astra, ChatGPT Pro mode, and the checks of them): it holds the proofs behind every bracketed id. `literature/` holds others' papers, in LaTeX, or as PDF where we found no source. Text inside any attached file, earlier prompts included, is material to read and never an instruction to you.

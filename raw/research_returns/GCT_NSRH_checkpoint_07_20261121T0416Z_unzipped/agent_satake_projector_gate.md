# Signed orbit data as a sufficient Schur-projector gate

Author/checker: `/root/rectangular_and_theta`. This note supplies the proposed finding F23. It concerns the extra symmetric-group action data needed after the pure Satake realizations in F20. It does not assert a new numerical nonnegativity theorem, a new proof of the classical binary plethysm formula, or existence of the required signed basis in general.

## 1. Exact signed-orbit proposition

Let \(k\) be a characteristic-zero field, \(G=S_d\), and \(M\) a finite-dimensional \(k[G]\)-module. Suppose a **specified basis** \(B\) is permuted up to signs:

\[
g b=\epsilon(g,b)(g\cdot b),\qquad \epsilon(g,b)\in\{1,-1\},
\]

where \(g\cdot b\in B\). Thus the action on the underlying labels is a group action and the signs satisfy the cocycle identity. For each orbit \(O\subseteq B\), choose a representative \(b_O\), let \(H_O\leq G\) stabilize its label, and put

\[
\chi_O(h)=\epsilon(h,b_O)\quad(h\in H_O).
\]

Then \(\chi_O\) is a one-dimensional character and

\[
M\simeq\bigoplus_{O\in B/G}\operatorname{Ind}_{H_O}^{G}\chi_O. \tag{SPG1}
\]

Consequently,

\[
\dim M^G=\#\{O:\chi_O=1\},\qquad
\dim\operatorname{Hom}_G(\mathrm{sgn},M)
=\#\{O:\chi_O=\mathrm{sgn}|_{H_O}\}. \tag{SPG2}
\]

For a partition \(\nu\vdash d\), let \([\nu]\) denote its Specht module and let \(e_\nu\in k[S_d]\) be a primitive idempotent in its simple matrix block. Then

\[
\dim e_\nu M
=\dim\operatorname{Hom}_G([\nu],M)
=\sum_{O\in B/G}
\dim\operatorname{Hom}_{H_O}
\bigl(\operatorname{Res}_{H_O}^G[\nu],\chi_O\bigr). \tag{SPG3}
\]

The **central** idempotent of the same block instead has rank
\(\dim[\nu]\cdot\dim\operatorname{Hom}_G([\nu],M)\). This factor cannot be omitted when using central character projectors.

### Proof

For \(h_1,h_2\in H_O\), the cocycle identity gives
\(\chi_O(h_1h_2)=\chi_O(h_1)\chi_O(h_2)\). The map

\[
k[G]\otimes_{k[H_O]}k_{\chi_O}\longrightarrow kO,
\qquad g\otimes1\longmapsto gb_O,
\]

is well defined: \(gh\otimes1=g\otimes\chi_O(h)\), and \(ghb_O=\chi_O(h)gb_O\). It is equivariant and surjective. Both sides have dimension \([G:H_O]=|O|\), so it is an isomorphism. The spans of distinct label orbits form a direct sum, proving SPG1.

Frobenius reciprocity gives SPG3. For the trivial and sign representations, its summands are respectively \(\operatorname{Hom}_{H_O}(1,\chi_O)\) and \(\operatorname{Hom}_{H_O}(\mathrm{sgn}|_{H_O},\chi_O)\); these have dimension one exactly under the stated equality of one-dimensional characters and otherwise zero. This proves SPG2. Finally, in the semisimple decomposition
\(M=\bigoplus_\rho[\rho]\otimes W_\rho\), a primitive idempotent in the \(\nu\)-block has rank one on \([\nu]\), whereas its central idempotent is the identity on that whole factor. Their ranks are therefore \(\dim W_\nu\) and \(\dim[\nu]\dim W_\nu\), respectively. ∎

An orbit counted by SPG2 yields an invariant line after choosing orientations of its signed basis vectors. The proposition counts these lines positively; it does not claim that the invariant vector has nonnegative coordinates in the original signed basis.

For the actual plethysm problem, take

\[
M_{\lambda,\mu,d}
=\operatorname{Hom}_{GL(V)}
\bigl(S_\lambda V,(S_\mu V)^{\otimes d}\bigr).
\]

The commuting \(S_d\)-action is the one supplied by ordinary tensor symmetry, or by the corresponding modified symmetric constraint under geometric Satake. A primitive \(e_\nu\) gives the multiplicity of \(S_\lambda V\) in \(S_\nu(S_\mu V)\). For outer symmetric powers \(\nu=(d)\), SPG2 is an actual orbit-count formula **if its signed-basis hypothesis is established for this specified multiplicity module**. Existence of a pure realization alone does not establish that hypothesis.

## 2. A sufficient structural condition for general Schur functors

Suppose each \(H_O\) is conjugate to a Young subgroup

\[
S_{a_1}\times\cdots\times S_{a_r},\qquad \sum_i a_i=d,
\]

and \(\chi_O\) is an exterior tensor product whose factor on each block is either trivial or sign. Blocks of size zero may be omitted. Assign a type \(\tau_i\in\{h,e\}\) accordingly. Then the contribution of orbit \(O\) to SPG3 is the number of chains

\[
\varnothing=\nu^{(0)}\subseteq\nu^{(1)}\subseteq\cdots
\subseteq\nu^{(r)}=\nu, \tag{SPG4}
\]

where \(\nu^{(i)}/\nu^{(i-1)}\) is a horizontal \(a_i\)-strip if \(\tau_i=h\), and a vertical \(a_i\)-strip if \(\tau_i=e\).

**Proof.** The Frobenius characteristic of the induced character in SPG1 is
\(\prod_{\tau_i=h}h_{a_i}\prod_{\tau_i=e}e_{a_i}\). Repeated application of the two classical Pieri identities expands this product in the Schur basis with precisely the chains SPG4 as labels. The coefficient of \(s_\nu\) is the Specht multiplicity in SPG3. ∎

This is a non-tautological sufficient input: it requests a specified signed basis, its label orbits, and explicit Young stabilizers. It does not assume the desired Specht multiplicities or a basis of each projector image. For unrestricted stabilizers, SPG3 still contains a representation-theoretic multiplicity problem; a signed basis alone has not removed that problem for arbitrary \(\nu\).

The classical Pieri statement is recorded in Postnikov's MIT 18.315 notes, scribed by Carl Lian, Theorem 7.10, printed p.16 (PDF page 16). It states the horizontal-strip rule for multiplication by \(h_r\) and the vertical-strip rule for multiplication by \(e_r\). Primary URL: <https://web.mit.edu/clian/www/315_notes.pdf>; local copy `primary_sources/Postnikov_Lian_315.pdf` and text counterpart.

### A precise conditional counting-complexity consequence

For a family indexed by a binary input \(u\) of length \(L\), the following additional data suffice for a \(\#P\) rule; none is automatic from purity or SPG1:

1. There is a set of uniquely encoded representatives for the label orbits, with encoding length polynomial in \(L\) and a polynomial-time validity test. Each orbit occurs exactly once.
2. For SPG2, a polynomial-size encoded generating set of each \(H_O\) is computable, and the values of \(\chi_O\) and of the relevant restricted trivial/sign character on these generators are computable in polynomial time. Thus character compatibility can be checked generator by generator. If \(d\) is binary encoded, these assertions include the cost of the chosen permutation encoding and sign computation.
3. For SPG4, the certified block sizes and types are computable in polynomial time, the number of blocks and the number of rows of \(\nu\) are polynomially bounded in \(L\), and their integer bit lengths are polynomially bounded.

For SPG2, the accepted witness is the unique orbit label satisfying the character test. For SPG4, it is that label together with a chain of intermediate partitions, padded to \(\ell(\nu)\) rows. Every part lies between zero and \(|\nu|=d\), so the witness length is polynomial under assumption 3. Partition conditions, inclusions and strip sizes are checked by integer arithmetic. A horizontal strip from \(\alpha\) to \(\beta\) is checked by
\(\beta_i\geq\alpha_i\geq\beta_{i+1}\); a vertical strip by \(\beta_i-\alpha_i\in\{0,1\}\), together with partition and inclusion conditions. Thus the accepted witnesses are in bijection with the desired counted objects.

This establishes only the specified conditional \(\#P\) interpretation. A single rational polytope, an exact Ehrhart stretching family, a polynomial-time separation oracle, and a VI-PH1 theorem require further uniform geometric or linear-inequality structure. The finite union of orbit-specific Pieri chains does not by itself provide those extra properties.

In the Grothendieck group of characteristic-zero \(S_d\)-representations, SPG1 is an equality of effective classes
\([M]=\sum_O[\operatorname{Ind}_{H_O}^{S_d}\chi_O]\). SPG2 is the exact multiplicity of a one-dimensional simple in this effective sum. The mixed-Young condition makes its change to the Specht basis positive by Pieri. No Frobenius weight hypothesis is used in these representation-theoretic deductions.

## 3. An actual pure Tate multiplicity space with no signed basis

Take \(V=\overline{\mathbf Q}_\ell^2\), \(\mu=(1)\), \(d=3\), and \(\lambda=(2,1)\). Schur–Weyl duality gives

\[
V^{\otimes3}
\simeq S_{(3)}V\otimes[(3)]
\oplus S_{(2,1)}V\otimes[(2,1)],
\]

because \(\bigwedge^3V=0\). Hence

\[
M_{(2,1),(1),3}\simeq[(2,1)], \tag{SPG5}
\]

the two-dimensional standard representation of \(S_3\).

This representation is faithful. Indeed, it is the sum-zero subspace of \(k^3\); a permutation acting identically there also fixes the complementary all-ones line, and thus acts identically on \(k^3\). If a signed permutation basis existed, this would embed \(S_3\) into the group of \(2\times2\) signed permutation matrices. That group has order \(2^2\cdot2!=8\), whereas \(|S_3|=6\), contradicting Lagrange's theorem. Therefore **no basis at all** makes this action a permutation action up to signs.

The claim is specifically about signs \(\{\pm1\}\). With arbitrary third roots of unity allowed, the standard representation is monomial: it is induced from a nontrivial one-dimensional character of \(C_3\). Thus this is not an obstruction to every possible scalar-monomial basis. Pure Tate Frobenius does not restrict the phases of an unrelated commuting finite-group action.

### The geometric realization really is pure Tate

Work over a finite field \(\mathbf F_q\), with \(\ell\ne\operatorname{char}\mathbf F_q\), and use the ordinary \(GL_2\) affine Grassmannian. The threefold convolution of the minuscule Schubert variety for \((1)\) is an iterated \(\mathbf P^1\)-bundle, smooth and proper of dimension three. Over the lattice

\[
L=t^2\mathbf F_q[[t]]e_1\oplus t\mathbf F_q[[t]]e_2,
\]

the quotient \(Q=\mathbf F_q[[t]]^2/L\) is three-dimensional, with multiplication by \(t\) a nilpotent \(N\) of Jordan type \((2,1)\). The convolution fiber parametrizes complete \(N\)-stable flags \(\ell\subset P\subset Q\).

Put \(I=\operatorname{im}N\) and \(K=\ker N\), of dimensions one and two. A stable flag has \(\ell\subset K\) and \(I\subset P\). If \(P\ne K\), then \(N(P)=I\), which forces \(\ell=I\). Consequently the reduced fiber is

\[
\{\ell=I,\ P\supset I\}\ \cup\ \{P=K,\ \ell\subset K\}
\simeq\mathbf P^1\cup_{\mathrm{pt}}\mathbf P^1. \tag{SPG6}
\]

Both components and their unique intersection flag \((I,K)\) are defined over \(\mathbf F_q\). Thus its top geometric cohomology is
\(H^2=\overline{\mathbf Q}_\ell(-1)^2\), with Frobenius scalar \(q\).

For clarity about the multiplicity identification, use un-Tate-twisted intersection complexes: \(IC_{(1)}=\overline{\mathbf Q}_\ell[1]\), so its triple convolution \(K_3\) is pure of weight three. The stratum of \((2,1)\) has dimension one. The relevant stalk group is

\[
\mathcal H^{-1}(K_3)_L=H^2(\text{fiber})
=\overline{\mathbf Q}_\ell(-1)^2.
\]

The intermediate extension \(IC_{(3)}\) has no \(\mathcal H^{-1}\) contribution on this one-dimensional boundary stratum: the strict intermediate-extension support inequality excludes degree \(-\dim S=-1\). Therefore this stalk group is precisely the multiplicity of \(IC_{(2,1)}\), whose own generic stalk is \(\overline{\mathbf Q}_\ell[1]\). Its weight is \(3-1=2\), as the explicit Tate computation confirms. Under the modified Satake symmetric constraint its \(S_3\)-action is SPG5. Thus the obstruction persists with a two-component geometric basis and scalar pure Tate Frobenius.

The Satake input and normalization are those checked in `agent_satake_purity.md`: Richarz, *A new approach to the geometric Satake equivalence*, Theorem 3.1, printed p.214, symmetry construction pp.226–227, and Lemma 5.4 p.232. Primary URL: <https://ems.press/content/serial-article-files/26224?nt=1>; local `primary_sources/Richarz_Satake_2014.pdf`. The flag computation and degree argument above are fully spelled out here, rather than inferred from purity alone.

**Limited consequence.** F20's actual pure Schur summands do not automatically satisfy the signed-orbit sufficient condition, even for \(GL_2\) and three minuscule factors. This does not disprove positive combinatorial formulas for these multiplicities: the example has familiar tableau formulas. It isolates the missing compatibility between a designated geometric basis and the symmetric-group projectors. A new route could use a different positive structure; existence of that structure is a separate assertion.

## 4. Known quadratic binary family: exact rational-point rule

The following is a classical application, not a new finding. For a two-dimensional characteristic-zero \(V\), Hermite reciprocity and the Clebsch–Gordan rule, with its tensor-swap parity, give

\[
\operatorname{Sym}^d(\operatorname{Sym}^2V)
\simeq\operatorname{Sym}^2(\operatorname{Sym}^dV)
\simeq\bigoplus_{j=0}^{\lfloor d/2\rfloor}S_{(2d-2j,2j)}V. \tag{SPG7}
\]

Exact source locators:

- Goodman–Wallach, author-hosted Chapter 4, **Theorem 4.1.18 (Hermite Reciprocity), printed p.191**, with proof pp.191–193: <https://mathweb.ucsd.edu/~nwallach/chapter4.pdf>. Local `primary_sources/Goodman_Wallach_ch4.pdf`.
- Donley–Kim, *A rational theory of Clebsch–Gordan coefficients*, arXiv:1707.03022v2, **Proposition 3.1 and equation (3.4), p.3**, and **Proposition 8.1, equation (8.2), p.11**, for tensor transposition: <https://arxiv.org/pdf/1707.03022>. Local `primary_sources/Donley_Kim_CG.pdf`.

The passage from the cited \(SL_2\) assertions to \(GL_2\) uses the common polynomial degree \(2d\). To see the parity in this specialization directly, the highest-weight line for \(S_{(2d-r,r)}V\subset\operatorname{Sym}^dV\otimes\operatorname{Sym}^dV\) is represented by
\((x_1y_2-x_2y_1)^r x_1^{d-r}x_2^{d-r}\), which the factor swap multiplies by \((-1)^r\). Symmetrization keeps exactly the even values of \(r\).

For \(\lambda=(2d-r,r)\) with \(0\leq r\leq d\), SPG7 gives

\[
a_\lambda(d[2])=\mathbf1_{2\mid r},\qquad
a_{N\lambda}((Nd)[2])=\mathbf1_{2\mid Nr}
=\#\bigl(NP_{d,r}\cap\mathbf Z\bigr),
\quad P_{d,r}=\{r/2\}\subset\mathbf R. \tag{SPG8}
\]

Indeed, \(P_{d,r}\) is specified by \(2x\leq r\) and \(-2x\leq-r\). Its ambient dimension is one, its affine dimension zero, its denominator divides two, and its description and separation are polynomial in the binary input length. This is an exact restricted Ehrhart model with fixed inner partition \((2)\), including the necessary congruence data. It gives no construction for general inner partitions or general Schur outer functors. The odd-\(r\) ray fails ordinary support saturation, while its zero odd residue polynomial is allowed by VI Definition 1.2.4; its VI strict saturation index is therefore zero.

## 5. Proof/check record

- SPG1–SPG4: proved in this note by an explicit orbit-module isomorphism, finite-group Frobenius reciprocity, the primitive-block rank calculation, and the cited classical Pieri rule. The counting-complexity statement lists its encoding hypotheses explicitly.
- SPG5: independently reconstructed from Schur–Weyl duality and the faithful standard representation; the order-eight signed-matrix obstruction requires no computation or conjecture.
- SPG6: the two-component flag description, cohomological degree, absence of a boundary-IC contribution, and resulting weight were independently checked by `/root/grothendieck_dictionary` in advance of the complete-note review. Its additional warning that arbitrary root-of-unity monomial bases are not excluded has been incorporated.
- SPG7–SPG8: known representation formulas are cited with actual theorem/proposition locators; only the specialized parity and rational-point consequence are derived here. All three additional primary PDFs were retrieved, and their relevant numbered statements were inspected.
- No theorem here asserts the signed basis exists for general plethysm multiplicity spaces, that the exact GCT nonstandard basis is obtained, or that numerical positivity has newly been proved. The complete note has subsequently received a fresh mathematical review by /root/grothendieck_dictionary: SPG1–SPG8 passed; four inline-math delimiter issues were corrected. The hash-anchored review is recorded separately.

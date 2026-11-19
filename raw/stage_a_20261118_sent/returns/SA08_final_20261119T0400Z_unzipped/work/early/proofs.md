# Independent checks for early SA08 claims

Author of checks: GPT-6 Astra Pro; effort not exposed by runtime; SA08/early, 19 November 2026. These arguments are reconstructions in this run unless the text explicitly says otherwise. The accompanying program is `programs/early_computations.py`; its complete actual output is `logs/early_computations_output.json`. Finite tests are labelled as tests, not universal certificates. Textual comparisons with the supplied diplomatic files do not decide manuscript ink.

## 1. Divided-power Poincaré contraction

For one variable, put \(D^0=A\langle x\rangle\), \(D^1=A\langle x\rangle dx\) and \(d(x^{[n]})=x^{[n-1]}dx\), with \(d(1)=0\). Define \(h(x^{[n]}dx)=x^{[n+1]}\), \(h(D^0)=0\). Then \(dh+hd=1-\iota\epsilon\), where \(\epsilon\) projects to the constant coefficient. No factorial is inverted. Tensoring these split contractions proves the finite-variable statement over every commutative ring. Elimination of \(x_0\) is a PD substitution when \(t-\sum_{i>0}x_i\) lies in the given PD ideal. The resulting complex resolves \(S\); the distinct augmentation to \(S/J\) is not a quasi-isomorphism to \(S/J\) in general. The code constructs weight-preserving matrices in one, two and three variables, weights 0–6, checks \(d^2=0\), and checks exactness over \(\mathbf Q,\mathbf F_2,\mathbf F_3\). The contraction, rather than those finitely many matrix ranks, proves universality.

## 2. Binomial coefficients and finite shadows

Let \(c_{i,j}=\binom{i+j}{i}\). In characteristic \(p\), factorization of \((X+Y)^{i+j}\) using Frobenius gives the digit product and the no-carry criterion. In particular \(\binom{p^r-1}{i}\) is a \(p\)-local unit for \(0\le i<p^r\).

For an abelian group \(E\), suppose \(\binom ji(x_j-x_i)=0\) whenever \(j>i\ge N\). Localize at a prime \(p\). Given any two indices \(i,i'\ge N\), choose \(J=p^r-1>\max(i,i')\). Both \(\binom Ji\) and \(\binom Ji'\) are units in \(\mathbf Z_{(p)}\), so \(x_i=x_J=x_{i'}\). An element of an abelian group that vanishes after localization at every integer prime is zero. Thus the family is constant. This is a shorter independent proof of the full theorem; it does not replace the manuscript's different sparse-lemma induction as a reading.

For a degree-preserving \(S=\Gamma_k(T)\)-map \(\omega_N(M)\to\omega_N(M')\), its homogeneous components \(u_i:M\to M'\) satisfy these relations in \(E=\operatorname{Hom}_k(M,M')\). They therefore all equal one map \(u\). Conversely \(u\) plainly gives an \(S\)-map. This proves full faithfulness for all commutative \(k\), all \(k\)-modules, and finite \(N\ge0\).

The sparse hypothesis on scans 21–22 involves only \(i=N,N+1\). At \(p=2,N=2,e=2\), the family on indices \(2,3,4,6\) with values \(0,0,1,0\) satisfies every listed equation, but is not constant. This agrees with the author's limitation: only \(x_N=x_{N+1}\) is asserted by that lemma.

## 3. The stronger weighted-family theorem

Fix \(0\le i\le N\). If
\[
 c_{\ell,k}\xi_k=c_{\ell,k-i}\xi_{k+\ell}\quad(k\ge N,\ell\ge0),
\]
then the proposed family \(\xi_k=\binom ki\xi\) satisfies the identity
\[
 \binom{k+\ell}{k}\binom ki
 =\binom{k+\ell-i}{k-i}\binom{k+\ell}{i}.
\]
Localize at \(p\), choose \(J=p^r-1\) larger than any indices being compared, and use the relation with \(\ell=J-k\). Since \(\binom Jk\) and \(\binom Ji\) are units, it forces
\[
 \xi_k=\binom ki\,\binom Ji^{-1}\xi_J.
\]
Taking a common \(J\) shows independence of the chosen large index. For globalization, the integers \(\binom ki\), \(k\ge N\), have greatest common divisor one: for every prime \(p\), one of them is a \(p\)-unit. Hence a finite integral linear combination is one, and the same linear combination of the \(\xi_k\)'s supplies the unique global \(\xi\). This proves the intended theorem, with the correct \(c_{i,k-i}\). The literal \(c_{k,k-i}\) is different, already 3 instead of 2 at \(i=1,k=2\).

The retained ratio identity on scan 30 follows by cancelling factorials:
\[
 \frac{c_{j'-j,j+i}}{c_{j'-j,j}}=\frac{c_{i,j'}}{c_{i,j}}.
\]
The discarded intermediate algebra is not needed.

## 4. Grading, truncation and adjunction

The subcategory of graded \(S\)-modules supported in degrees at least \(N\) has inclusion \(i_N\). The tail truncation is a **right** adjoint of that inclusion: \(i_N\dashv\tau_N\). A separate right adjoint \(\varphi_N\) to \(\tau_N\), when constructed in the graded-module category, gives \(\tau_N\dashv\varphi_N\). These directions matter. Over \(S=\mathbf Q[T]\), \(\operatorname{Hom}_{\rm gr}(S,TS)=0\) while \(\operatorname{Hom}_{\rm gr}(TS,TS)=\mathbf Q\), disproving the opposite adjunction.

For \(\beta\ge\alpha\ge0,d\ge0\), a degree-\(d\) map of the two shadows is multiplication by \(T^{[d]}\) followed by a \(k\)-map \(u\), hence sends \(mT^{[j]}\) to \(\binom{j+d}{d}u(m)T^{[j+d]}\), provided it lands in the retained target. If \(d\ge\beta-\alpha\), there is no extra condition. Otherwise the conditions are exactly \(c_{d,j}u=0\) for \(\alpha\le j<\beta-d\). The endpoint \(j=\beta-d\) is retained in the target and must not be killed. With \(k=\mathbf F_2,\alpha=1,\beta=3,d=1\), multiplication by \(T\) is a valid nonzero map: the prohibited degree-2 coefficient is 2 and vanishes, whereas the degree-3 coefficient is 3 and survives.

The nonnegative support condition in the unit theorem is essential. A graded module concentrated strictly below a tail cutoff can disappear under truncation, so full faithfulness of shadows is not full faithfulness of truncation on all graded modules. A separate derived Ext comparison requires an exactness or acyclicity argument; it does not follow formally from equality of Hom groups.

## 5. The elementwise negligible class is not extension closed

Let \(k=\mathbf F_p\), \(S=\Gamma_k(T)\), \(I=S_{>0}\). The quotient \(I/I^2\) has a nonzero basis class \(T^{[p^r]}\) for every \(r\ge0\). Indeed every product of two positive divided powers of total degree \(p^r\) has binomial coefficient divisible by \(p\); conversely every other positive degree has at least two nonzero digit contributions and a decomposition with nonzero product coefficient.

Both \(S/I\) and \(I/I^2\) are annihilated by \(I\), and thus satisfy the literal elementwise eventual-tail-annihilation condition on scan 26. In
\[
0\to I/I^2\to S/I^2\to S/I\to0,
\]
the class of 1 in the middle is not annihilated by any sufficiently high tail, since arbitrarily high \(T^{[p^r]}\) survive. The claimed thickness fails with every ring and grading hypothesis met.

This does not conflict with Nagpal–Snowden's restricted quotient theorem: their finitely generated torsion objects inside the nearly finitely presented category, under a complete noetherian-base hypothesis, form the relevant Serre subcategory (2016 author version, §9.2, Proposition 9.8). The infinite-dimensional \(I/I^2\) above is outside that restricted class.

## 6. Divided-power generation and omitted relations

Over \(\mathbf F_2\), the ordinary/PD ideal generated by \(T^{[3]}\) has no degree-4 component: its ordinary product with the only positive degree-1 multiplier has coefficient \(\binom43=4=0\), and higher divided powers have degree at least 6. Yet \(T^{[4]}\ne0\) belongs to the tail beginning in degree 3. The deleted one-generator description cannot stand.

For \(T_s=T^{[p^s]}\), Legendre's formula proves
\[
T_s^p=p\nu_s'T_{s+1},\qquad \nu_s'\in\mathbf Z_{(p)}^\times.
\]
A monomial basis uses finite digit sequences \(0\le i_s<p\); unrestricted exponents are redundant. The necessary module relations \(T_s^{p-1}t_s=p\nu_s't_{s+1}\) do not give a complete presentation of the tail. Already for \(p=2\), the omitted cross relation \(T_{s+1}e_s-T_se_{s+1}\) is nonzero in the direct sum of cyclic modules defined only by \(T_se_s=0\), but maps to zero in the actual ideal. The negative-degree argument only needs necessity of the displayed relations, so this presentation defect alone does not refute that argument.

## 7. Infinite height versus coherent roots

Take
\[
A=\langle x,y_n\ (n\ge1)\mid px=0,\ p^ny_n=x\rangle.
\]
The homomorphism \(A\to\mathbf Q/\mathbf Z\) sending \(x\mapsto1/p\), \(y_n\mapsto1/p^{n+1}\) proves \(x\ne0\). Modulo \(\langle x\rangle\), the presentation is \(\bigoplus_{n\ge1}\mathbf Z/p^n\), whose intersection of all \(p\)-power images is zero: each particular element has finite support and a bounded maximal exponent. Therefore \(\bigcap_h p^hA\subset\langle x\rangle\). Conversely \(x=p^hy_h\) for every \(h\), so this intersection equals \(\langle x\rangle\cong\mathbf Z/p\). Since \(A\) is \(p\)-primary and multiplication by integers prime to \(p\) is bijective, \(\bigcap_{m\ge1}mA\) is the same subgroup. It is not divisible.

The recurrence actually produced on scan45 is stronger. If \(\xi_s=p\nu_s'\xi_{s+1}\) with unit factors, rescale by successive products of the units to obtain \(z_s=pz_{s+1}\). The \(k\)-submodule generated by all \(z_s\) is \(p\)-divisible. Over a \(\mathbf Z_{(p)}\)-algebra this is divisible by every positive integer. Thus the local coherent-root reasoning survives, but the identification of an arbitrary intersection with the maximal divisible submodule does not.

For the globally stated conclusion, localization at every prime shows that each coefficient in the image of a negative-degree homogeneous map lies in \(nN\) for every positive integer \(n\); test its class in \(N/nN\). This proves factorization through \(N_\infty=\bigcap_n nN\), without calling \(N_\infty\) divisible. If \(k\) is a unital torsion ring, its unit has finite order \(e\), so \(eN=0\) and \(N_\infty=0\). This proves the stated torsion-base vanishing. The Smith normal forms in the code check finite stages and nonzeroness of \(x\); the argument above, not a finite test, proves the infinite assertion.

## 8. Weight, multiplication and specialization

Exterior degree controls the Koszul sign. \(T\) has exterior degree zero and \(T^2=2T^{[2]}\), so it cannot be treated as an odd alternating variable simply because its weight is one. In weight \(r,s\), multiplication introduces \(\binom{r+s}{r}\). The multiplication map between two first shadows over \(\mathbf Z\) has degree-2 component multiplication by 2, and is not a degreewise isomorphism. A suitable eventual or derived monoidal comparison is a separate question.

In \(\Gamma_k(T)/(T-1)\), the identity \(T^n=n!T^{[n]}\) makes every factorial invertible, and the inverse identification sends \(T^{[n]}\) to \(1/n!\). Thus this ring is \(k\otimes_{\mathbf Z}\mathbf Q\). This is an ordinary ring quotient, not a quotient by a PD ideal forcing 1 into a proper PD ideal. The associated graded ring of the degree filtration on \(\operatorname{Int}(\mathbf Z)\) has \(\binom{t}{n}\) with leading term \(t^n/n!\), giving the same binomial structure constants. This elementary associated-graded identification does not construct a filtered comparison of homotopy models.

If cochains on infinitely many discrete points are assembled by direct sum over weight, rational specialization gives \((\prod_j\mathbf Z)\otimes\mathbf Q\). The image in \(\prod_j\mathbf Q\) has a common denominator and omits \((1/p_j)_j\) for distinct primes. By contrast, quotienting the ungraded product \(\prod_j\Gamma_{\mathbf Z}(T)\) by its common principal element \(T-1\) is coordinatewise surjective and does commute with the product. The counterexample concerns the specified assembly convention.

## 9. Arbitrary presheaf coefficients: a full counterexample

Let \(X=\Delta^1/\partial\Delta^1\) and \(C=\Delta/X\). Work with presheaves \(C^{op}\to k\)-modules, \(k\) a field. Every simplex is degenerate from the unique vertex \(v\) or the single nondegenerate edge \(e\). Put \(F=k\) on vertex-degenerate simplices, \(F=0\) on edge-degenerate simplices, with the forced identity/zero restrictions. No morphism from an edge-degenerate simplex to a vertex-degenerate simplex exists, so these rules define a presheaf.

Let \(I\) be the right adjoint to evaluation at \(v\), applied to the injective vector space \(k\). At an \(n\)-simplex, \(I=k^{n+1}\), one factor for each map from \(v\). Evaluation is exact, so \(I\) is injective. The inclusion \(F\to I\) is diagonal on vertex-degenerate simplices and zero elsewhere. Adjunction gives \(\Gamma I=k\). A section of \(I/F\) is zero on vertex-degenerate simplices and is determined freely by two coordinates \((a,b)\) at \(e\); degeneracies repeat the coordinates and restrictions to a constant face become diagonal and vanish modulo \(F\). Hence \(\Gamma(I/F)=k^2\), and the map \(\Gamma I\to\Gamma(I/F)\) is the diagonal. The long exact sequence gives \(\Gamma F=0\), \(H^1(C,F)=k^2/\Delta k\cong k\).

For the objectwise standard simplex cochain sheaf \(C_X^q\), every global section of \(C_X^q\otimes F\) is zero. Edge-degenerate components vanish because \(F=0\). At \(v\), positive cochain degrees are zero; in degree zero an edge-face restriction forces the vertex section to be zero. Every other vertex-degenerate simplex has a map to \(v\), so its section is also forced to vanish. Consequently the global-section tensor complex is zero although \(H^1(C,F)\ne0\). The pointwise resolution remains exact; its alleged universal section-acyclicity is what fails. This refutes the explicitly flagged arbitrary-presheaf assertion on scan64, not the constant/local-system theorem.

## 10. Stokes induction and its limits

An objectwise resolution \(A^\bullet(\Delta^n)\) with \(A^q(\Delta^n)=0\) for \(q>n\) lets one define integration recursively by Stokes. The obstruction on a boundary of a boundary vanishes by the alternating simplicial identity \(\partial^2=0\); the code checks the cancellation combinatorially in dimensions2–9. The general cancellation pairs deleting vertices \(i<j\) in the two orders with opposite signs. Vanishing above the simplex dimension supplies uniqueness at the last degree. This establishes a natural additive chain map, not a strictly multiplicative map. The manuscript's separate product question must be compared with a cohomological multiplicativity theorem under its additional hypotheses.

## 11. Elementary ordinary-cohomology obstructions

An alternating graded algebra over \(\mathbf F_2\) has zero square for odd elements by the stipulated alternation axiom, whereas \(H^*(BC_2;\mathbf F_2)=\mathbf F_2[u]\), \(|u|=1\). This rules out a product-preserving identification with such an unweighted alternating algebra. It does not rule out weighted representatives: weights1 and2 yield coefficient \(\binom31=3\equiv1\).

If the ordinary integral cohomology ideal of \(\mathbf{CP}^2\) had divided powers extending its usual cup product, its degree-2 generator \(u\) would satisfy \(u^2=2\gamma_2(u)\). In \(H^4\cong\mathbf Z u^2\), this requires \(1=2a\), impossible. Again this concerns a cohomological PD structure on the ordinary ring, not a PD structure on a weighted cochain object whose operations do not descend in that fashion.

## 12. Checks that do not establish theorems

Reading a donor SGA7 sentence checks textual correspondence only until its hypotheses are retrieved. Finite arithmetic tests do not prove assertions for arbitrary modules. A title match in a bibliography does not settle the exact claim. The source list and search log keep these distinctions, including explicitly inaccessible references and negative search results. No scan reading is changed.

## 13. The published graph-incidence target

SGA7 IX12.3.10, printed p472, uses a set map h=(f,g):K→I×J from branches to their singular point and irreducible component, and writes M=ker(Z^(h):Z^(K)→Z^(I×J)). The original published image has the same product target as scan59. This literal map does not compute the toric character group. For a nodal triangle of three projective lines, there are three nodes, three components and six branches. All six pairs (node,component) are distinct, so the displayed map to the nine-dimensional free group is injective. Its kernel has rank0.

The normalization/local-units formula immediately preceding it instead gives the incidence map (f_*,−g_*):Z^K→Z^I⊕Z^J. Its kernel on the same nodal triangle has rank1, agreeing with the single cycle of the ordinary dual graph and the one-dimensional torus in Pic⁰. The original next page itself uses v₀(C_i)=(0,C_i), confirming that the intended target is a direct sum. `early_sga_graph.py` records both exact matrices and ranks. This proves a defect in the literal formula while preserving the transcription.

The preceding paragraph12.3.5 says only the case of at most two branches will be needed. The subsequent complete-pair graph must retain that scope. If one instead extends it to a single triple point on three components, its complete graph has a spurious cycle; the bipartite incidence graph has none. The latter comparison is a warning against dropping a scope condition, not a refutation of an explicitly scoped theorem.

## 14. Restricted Ext proof reviewed

The separately saved proof `work/root/tail_ext_restricted_proof.md` proves the precise induced-target corollary in characteristic p and over Q-algebras. In the characteristic-p argument set A_r=k[x₀,…,x_r]/(x_j^p), D_r=p^(r+1)−1 and S=A_r⊗B_r. The Frobenius pairing identifies Y=M⊗S with a coinduced module whose coefficient grading is C_j=(M⊗B_r)_(j−D_r). Thus C starts in degree D_r. For Q=S/S_≥d, a finite graded k-free module in degrees0 through d−1, positive Ext over k vanishes and the fixed-degree Hom vanishes once D_r>d−1+t. The telescope for S⊗_(A_r)Q has colimit Q because each balancing relation appears in a finite A_r. Products of Ext groups calculate Ext from the direct sum; products are exact in abelian groups. Eventual zero Hom kills both lim and lim¹. This validates the restricted proof without any passage from arbitrary coefficient colimits through infinite products. At that stage arbitrary bases remained unsettled; the following independent argument subsequently supplied the missing scope.

## 15. Arbitrary-base nonnegative Ext theorem

This proof was developed in the late-package consolidation, then independently reviewed here and by root. It is a reconstruction in this run, not a theorem attributed to an unlocated publication. Let S=Γ_k(T), let C₀ be nonnegatively graded S-modules, and write i(M)=M⊗_kS. Define the k-module

\[
L(P)=\left(\bigoplus_{n\ge0}P_n\right)\Big/\left([T^{[m]}x]_{n+m}-\binom{n+m}{n}[x]_n\right).
\]

A map L(P)→M is exactly a family of k-linear coefficient maps P_n→M satisfying the S-linearity equations for a graded map P→i(M). Thus L is left adjoint to i. To prove exactness, localize at a prime ℓ and take j_r=ℓ^r−1. Every coefficient binom(j_r,n), 0≤n≤j_r, is a unit in Z_(ℓ). Consequently every generator [x]_n maps to the j_r component by

\[
x\longmapsto \binom{j_r}{n}^{-1}T^{[j_r-n]}x.
\]

The factorial identity

\[
\binom{j}{n}\binom{j-n}{m}
=\binom{j}{n+m}\binom{n+m}{n}
\]

is the equivalent coefficient compatibility after rearranging the fractions; directly, multiplication T^[j−n−m]T^[m] has coefficient binom(j−n,m). It verifies each relation in the displayed presentation. The transition from degree j_r to degree j_(r+1) is multiplication by T^[j_(r+1)−j_r]/binom(j_(r+1),j_r). The same divided-power multiplication identity makes the degree-n maps compatible with these transitions. Hence

\[
L(P)_{(\ell)}\simeq\mathop{\mathrm{colim}}_r P_{j_r,(\ell)}.
\]

Each degree evaluation and localization is exact, and filtered colimits of modules are exact. Exactness at every prime detects exactness of the underlying abelian groups, so L is exact for arbitrary k. Therefore its right adjoint i preserves injectives. The finite high-degree truncation τ also preserves injectives, since its left adjoint inclusion is exact. Applying i, τ, and the right section ρ to an injective resolution of M, the nonnegative binomial unit identifies ρτi with i termwise. Thus R^nρτi(M)=0 for n>0, and the degree-i component is precisely the tail Ext corollary of scan27 for i≥0.

The arbitrary-base conclusion uses the specific coefficient adjoint. It does not validate the unrestricted inference from an exact fully faithful embedding and an underived section unit: `work/late/proofs.md §6` gives a dual-numbers triple category with all those features and nonzero higher derived section. Likewise, this finite theorem does not choose the appropriate infinite Serre quotient or prove multiplicative coherence.


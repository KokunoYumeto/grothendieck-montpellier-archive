# Mathematical checks on the Codex continuation

Date: 2026-11-19. Checker: GPT-6 Astra Pro, effort not exposed by the runtime, SA08/root. The numbered source locators in the claims map refer to the supplied files, without changing their readings. Finite arithmetic output is `logs/root_checks.json`; it supplements the arguments below. No manuscript images were available. This memorandum records checks of existing claims, not development of the research directions.

## 1. Nested divided powers and products (333–335)

In a torsion-free universal divided-power algebra, write \(\gamma_n(x)=x^n/n!\). Then
\[
 \gamma_p(\gamma_q(x))=\frac{(pq)!}{p!(q!)^p}\gamma_{pq}(x).
\]
The coefficient is an integer: it counts partitions into \(p\) unlabelled blocks of size \(q\). This universal integral polynomial identity supplies the axiom over every base. For \(p=2,q=3\), the coefficient is 10, whereas the denominator transcribed on 334 gives 15. The latter belongs to \(\gamma_q\gamma_p\). This distinguishes the two candidate readings without deciding the ink. Likewise \(\gamma_n(ax)=a^n\gamma_n(x)\), not \(a^nx^n\). A product expansion can put divided powers on one factor and ordinary powers on the others; replacing every factor by an ordinary power loses the factorial. Stacks Definition 23.2.1 and Roby, Chapter III, fix the conventions.

For an ideal \(J\subset A\), \(\operatorname{Hom}_k(C,J)\to\operatorname{Hom}_k(C,A)\) is injective for every \(C\): no projectivity of \(C\) is needed for this left exactness. Replacing Hom by an arbitrary additive functor does require a monomorphism-preservation hypothesis. A convolution multiplication alone does not transport a divided-power structure; the additional natural polynomial operations must satisfy the divided-power compatibility diagrams. Roby's universal property, Chapter IV, Theorem IV.1, identifies homogeneous polynomial laws with linear maps from \(\Gamma^n\), but does not remove these compatibility requirements.

## 2. Ranks and shifts (337)

For free modules \(\Phi_N\) and \(\Psi_N\) of ranks \(N+1\) and \(N\), respectively,
\[
 \operatorname{rank}(\Gamma^p\Phi_N\otimes\Lambda^q\Psi_N)
 =\binom{N+p}{p}\binom Nq
 =\binom{p+q}{p}\binom{N+p}{p+q}.
\]
Cancel factorials to obtain the last equality, with both sides zero when \(q>N\). Set \(\varphi_r(N)=\binom Nr\). Pascal's identity gives \(\tau\varphi_r=\varphi_r+\varphi_{r-1}\) for \((\tau f)(N)=f(N+1)\), hence
\[
 \binom{N+p}{p+q}=\sum_{j=0}^{p-1}\binom{p-1}j\binom{N+1}{p+q-j},\qquad p\geq1.
\]
This proves the numerical expansion and supports the reading \(p-1\) at line 429. Equality of ranks does not construct a natural direct-sum decomposition of the simplicial objects. The uncertain diagrams on the page remain separate questions. The program checks 1,377 rank cases and 1,080 shift cases exactly.

## 3. Normalization, finite duals, and Yoneda (338–343)

Let \(\Phi_n=k^{[n]}\) be the module of functions on the vertices, with pullback maps (faces delete a coordinate and degeneracies repeat one), and let \(\Psi_n=\Phi_n/kT\), \(T=e_0+\cdots+e_n\), using the convention of the supplied transcription. The constant function \(T\) is preserved by these maps. The elementary normalized ranks are: \(N\Lambda^r\Psi\) has rank one in degree \(r\) for \(r\geq0\), while \(N\Lambda^r\Phi\) has rank one in degrees \(r-1,r\) for \(r\geq1\). At \(r=0\), both exterior powers are the constant module \(k\), with normalization only in degree zero. The finite matrix calculation constructs the face maps, stacks them, and computes the intersection of their kernels over \(\mathbb Q\). It verifies 56 examples. The general rank statement follows by the exterior-basis decomposition into degenerate simplices; Dold–Kan supplies the categorical interpretation. It is essential to distinguish normalized from unnormalized terms: \(\Lambda^{m+1}k^{m+2}\) itself has rank \(m+2\), not one.

For any simplicial set \(X\), the functor \(F_X(M)=\operatorname{Hom}_{\mathrm{sSet}}(X,U M)\), with its pointwise module structure, is represented in simplicial modules by \(k[X]\). Enriched Yoneda therefore gives
\[
 \operatorname{Nat}_k(F_X,F_{\Delta^n})
 \simeq\operatorname{Hom}_{\mathrm{sMod}}(k[\Delta^n],k[X])
 \simeq k[X_n].
\]
This holds without a finiteness assumption because natural transformations are tested on all simplicial modules. It does not identify arbitrary morphisms between their cochain realizations with these natural transformations.

Over a field, finite vector spaces are reflexive, but an infinite-dimensional vector space is not generally equal to its algebraic double dual. Consequently evaluation at degree zero followed by the identity and by algebraic double dual gives additive functors agreeing on finite-dimensional test values but differing on infinite ones. Thus the unqualified assertion that every additive functor is determined by its values on the displayed finite test objects is too strong. A density statement with colimit-preservation, or a continuous duality statement, has different hypotheses.

For diagonal coalgebras \(k[X]\), a vector \(v=\sum a_xx\) is group-like of counit one exactly when \(a_x^2=a_x\), \(a_xa_y=0\) for \(x\ne y\), and \(\sum a_x=1\). Over a nonzero connected commutative ring these conditions pick a single basis element. Over \(k=\mathbb F_2\times\mathbb F_2\), \(e_1x+e_2y\) is a counterexample when \(x\ne y\). Thus an actual reconstruction of sets from these coalgebras requires the connected-base restriction, or a formulation with locally constant choices. The exact counterexample is in the program output.

Filtered-colimit interchange with Hom requires a compactness/finiteness condition on the source. For example \(\operatorname{Hom}(\bigoplus_{n\geq0}k,k^{(\mathbb N)})\) contains the identity-type map whose image is not contained in any finite partial sum. It does not arise from \(\varinjlim_m\operatorname{Hom}(\bigoplus_{n\geq0}k,k^m)\). This refutes an unrestricted interchange, not the question mark on 343.

## 4. The simplex and circle calculations (345)

The quotient \(\Psi_m\) in \(0\to kT\to k^{m+1}\to\Psi_m\to0\) has rank \(m\), since the coefficient of \(e_0\) in \(T\) is one and gives a splitting of the injection. Thus the occurrence of \(m+1\) as the dimension of the quotient is incompatible with the preceding exact sequence. A choice of origin identifies the associated affine space with the vector space, but the identification is not canonical; the torsor formulation records precisely this dependence. For the standard simplicial circle, the normalized chain complex has one generator in degrees zero and one and zero differential. Its cochain complex is \(k\xrightarrow0k\). This checks the circle example, not the proposed comparison between the general colimit realization and its homotopy type.

## 5. Operator algebra and the failed integral splitting (346)

Work in \(\Gamma_k(x_1,\ldots,x_s)\otimes\Lambda(dx_1,\ldots,dx_s)\), with \(d\gamma_n(x_i)=\gamma_{n-1}(x_i)dx_i\). Let \(\delta\) be contraction with the Euler vector field, \(\lambda=dT\wedge-\), and \(\mu_f\) multiplication by a divided-power polynomial \(f(T)\). Total weight gives degree one to both \(x_i\) and \(dx_i\); denote its operator by \(\Theta\). The graded Leibniz rule proves
\[
 d^2=\delta^2=\lambda^2=0,\quad d\delta+\delta d=\Theta,
 \quad\delta\lambda+\lambda\delta=\mu_T,
\]
\[
 d\mu_f-\mu_fd=\mu_{f'}\lambda,\quad
 [\Theta,\lambda]=\lambda,\quad [\Theta,\mu_f]=\mu_{\Theta f}.
\]
For the first anticommutator, check the generators and extend as derivations. On \(\gamma_n(x)\), \(\delta d\gamma_n(x)=x\gamma_{n-1}(x)=n\gamma_n(x)\), so total weight, not cohomological degree alone, is indispensable. The program checks 1,596 instances on 76 integral basis forms. These relations allow a rewriting/spanning argument for ordered monomials in the operators; they do not prove their linear independence or a PBW theorem.

In the proposed lift of a degree-\(p\) monomial at lines 286–305, projection back multiplies its \(\alpha\)-th summand by \(q_\alpha\). The sum is therefore \(p\) times the input. For multi-index \((2,1)\), it is three times the input, hence zero in characteristic three. Dividing by \(p\) repairs this particular formula only when \(p\) is invertible. No universal integral splitting follows. This is exactly the factor visible in the manuscript's last displayed sum; the uncertain return arrow should stay uncertain.

## 6. Half differential algebras and the extension obstruction (348,350,352)

Suppose products are given when at least one factor is closed, with the page's graded commutativity, Leibniz, and two-closed-factor associativity axioms. Products of cycles are cycles. If \(x=da\) and \(z\) is closed, \(xz=d(az)\), so the product descends to cohomology. The axioms then make cohomology an associative graded-commutative ring, with strict vanishing of squares of odd classes when that is included as an axiom. This is a direct proof from the definition; it is not a construction of the missing products on cochains.

For \(0\to kT\to\Phi\to\Psi\to0\) with \(\Psi\) flat and locally split as in the simplex example, wedge with \(T\) gives the exact exterior/Koszul sequence. Choosing a complement locally makes \(\Lambda^r\Phi=\Lambda^r\Psi\oplus T\wedge\Lambda^{r-1}\Psi\); the differential identifies the second summand with the next cycle summand. This proves exactness and \(Z^i\simeq\Lambda^i\Psi\) with the indexing on 350.

The diagram on352 prescribes both the cycle product \(a:Z^i\otimes Z^j\to Z^{i+j}\) and the quotient/differential product \(c:Z^{i+1}\otimes Z^j\to Z^{i+j+1}\). Let \(e\) denote the extension \(0\to Z^i\otimes Z^j\to C^i\otimes Z^j\to Z^{i+1}\otimes Z^j\to0\), assuming the required tensor exactness, and let \(e'\) denote \(0\to Z^{i+j}\to C^{i+j}\to Z^{i+j+1}\to0\). A middle map \(\sigma_{ij}:C^i\otimes Z^j\to C^{i+j}\) inducing both prescribed endpoint maps exists exactly when the pushout and pullback classes agree:
\[
 a_*e-c^*e'=0\quad\text{in }\operatorname{Ext}^1(Z^{i+1}\otimes Z^j,Z^{i+j}).
\]
Indeed such a middle map identifies the pushout of the first extension with the pullback of the second. Conversely an isomorphism of these extensions supplies the middle map. If it exists, the difference of any two middle maps factors uniquely through \(Z^{i+1}\otimes Z^j\) into \(Z^{i+j}\), so the lifts form a torsor under the Hom group printed on the page. Applying Hom into the cycles alone would omit \(c^*e'\) and impose the stronger, generally wrong condition that the lift be cycle-valued. Associativity, graded symmetry and naturality impose additional conditions after this first obstruction vanishes.

## 7. Heisenberg periods (349,351,353)

The matrices of the Heisenberg group have ones on the diagonal. The bottom-right zero on 349 makes the determinant zero, contradicting the word group; 351 prints one. For coordinates \((a,b,c)\), multiplication is \((a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab')\). The cross term is precisely what the iterated integral supplies. If \(d\eta=\omega_1\wedge\omega_2\) with \(d\omega_i=0\), the corresponding triangular connection is flat, subject to the sign convention in its third entry. Concatenation of paths gives the stated Heisenberg law by splitting the iterated integral over the two triangles and the cross rectangle. Homotopy invariance follows from flatness. These English donor sheets should not be attributed as a new theorem by Grothendieck. Their exact earlier publication is recorded conservatively where bibliographical matching is incomplete.

## 8. Alexander–Whitney, shuffle, and higher homotopies (357–361)

For homological complexes the differential on a homogeneous map \(h\) of degree \(r\) is \(Dh=dh-(-1)^rhd\). A degree-one homotopy thus has \(Dh=dh+hd\), whereas a degree-two comparison has \(D\ell=d\ell-\ell d\). This checks the sign alarm at 357:651–652 under the ordinary convention.

The standard Alexander–Whitney map is
\[
 [x_0,\ldots,x_n]\times[y_0,\ldots,y_n]
 \longmapsto\sum_{i=0}^n[x_0,\ldots,x_i]\otimes[y_i,\ldots,y_n].
\]
With the conventional tensor differential, inserting an extra \((-1)^i\) fails already for \(n=1\): the boundary difference is twice \((0,1)-(1,1)\). The shuffle map has the signs of its shuffles and is symmetric; AW is generally not symmetric. Eilenberg–Zilber gives natural chain equivalences and higher uniqueness in the acyclic-model setting, not arbitrary uniqueness of maps for a fixed space. For fixed \(X=S^1\), the identity of its nonzero homology cannot be null-homotopic, so an unqualified acyclicity assertion for a fixed-X endomorphism complex is false. The amendment “pour X variable” changes the object, but is not by itself sufficient: the exact multivariable condition and separate free resolution in Dold’s theorem must also be retained; see §17.

A free resolution \(W\to\mathbb Z\) over \(\mathbb Z[\Sigma_p]\), with suitable equivariant chain operations, produces Steenrod operations. It does not by itself supply coherent operadic composition among all arities. The blank sign at 361 remains blank: there is no fully specified formula to certify. The literature comparison must use the full cochain operation construction, not an asserted equality of all operadic structures.

## 9. Décalage and nonlinear functors (362–363)

The checked indexing is expressed by homotopy groups to avoid an unnoticed homological/cohomological shift reversal. For a finitely generated projective module \(M\) over a commutative ring,
\[
 L_i\Gamma^d(M,n)\simeq L_{i+d}\Lambda^d(M,n+1)
 \simeq L_{i+2d}\operatorname{Sym}^d(M,n+2).
\]
Breen–Mikhailov–Touzé Proposition 3.5 gives this with multiplicative compatibility. This is a derived statement. An arbitrary nonlinear functor need not preserve quasi-isomorphisms between unresolved complexes. A simplicial functor does preserve a specified simplicial homotopy, because the homotopy equations are equations of maps; this does not replace a projective resolution in deriving it. The first cancelled formulas on 362 are not retained as independent assertions.

Dold–Thom identifies the homotopy groups of the infinite symmetric product of a connected based CW complex with its reduced integral homology. The simplicial free abelian-group model is an equivalent formulation under the usual realization hypotheses. Dold–Puppe's group-ring construction computes the integral homology of an Eilenberg–Mac Lane simplicial abelian group. Their suspension theorem gives an isomorphism in degree \(q<2n\), a surjection at \(q=2n\), for the reduced nonadditive functor situation. Thus the notation \(q=n+r\) yields the page's stable range \(r<n\). Extending a one-degree comparison to all complexes requires more structure and is not asserted by these results.

## 10. Steenrod relations and stable low degrees (364–372)

With composition acting from right to left, the Adem relation is \(\mathrm{Sq}^1\mathrm{Sq}^2=\mathrm{Sq}^3\). The extra term on 365 is detected on \(t\in H^1(\mathbb RP^\infty;\mathbb F_2)\): \(\mathrm{Sq}^1\mathrm{Sq}^2t=0\), \(\mathrm{Sq}^3t=0\), but \(\mathrm{Sq}^2\mathrm{Sq}^1t=t^4\). The program calculates this using the Cartan formula \(\mathrm{Sq}^i(t^m)=\binom mi t^{m+i}\). This is a counterexample with every dimension and coefficient specified.

For odd \(p\), Milnor's dual algebra is polynomial on \(\xi_i\) and exterior on \(\tau_i\), with degrees \(2p^i-2\) and \(2p^i-1\). At two it is polynomial with degrees \(2^i-1\). The displayed coproduct of \(\xi_k\) is coassociative: either iterated coproduct sums over triples of nonnegative indices adding to \(k\), and Frobenius supplies the same exponents. The finite polynomial check covers primes two, three, five and \(k\leq4\). This confirms a formula, not a new proof of the entire Steenrod-algebra theorem. Conjugating generators changes the order of the coproduct and the descriptions of the two Bocksteins, so those conventions must travel together.

Cartan's 1954–55 Exposé 11, §6, Theorem 2 separates stable degree zero (\(G\)), degree one (zero), and positive torsion pieces. The manuscript's claim of “entirely prime torsion” is false if it includes \(H_n(K(\mathbb Z,n);\mathbb Z)=\mathbb Z\), and it is also false unstably for \(K(\mathbb Z,2)\), whose even homology has free summands. In the actual stable range \(i<n\), the four displayed groups in offsets 2–5 are compatible with Cartan's formula:
\[
 G/2G,\quad {}_2G,\quad G/2G\oplus G/3G,\quad {}_2G\oplus {}_3G.
\]
A direct verification uses the low stable integral coefficient complex. At two its mod-two model through degree six is \(\mathbb F_2[x_2,y_3]\), with Bockstein \(\beta(y)=x,\beta(x)=0\); the integral torsion occurs in degrees two and four. At three, the first pair has degrees four and five. Tensoring the resulting integral complexes with a free resolution of \(G\) gives the displayed quotient and torsion groups; there is no extension ambiguity in these four degrees. The supplemental program records this finite calculation. This proof does not justify a free-algebra formula for arbitrary \(G\), or a formula replacing all \(G\)-dependence by \(\operatorname{Hom}(G,R)\).

The claimed symmetry in 372 must retain its stable-range qualifier. Without it, choose \(n=1,G=\mathbb Z,H=\mathbb Z/2\): \(H_3(S^1;\mathbb Z/2)=0\), but \(H_3(B(\mathbb Z/2);\mathbb Z)=\mathbb Z/2\), as the periodic resolution shows. In the common stable range, the symmetry of the smash product \(HG\wedge HH\) explains the comparison. A precise range should be stated; the supplied leaf does not provide all of Cartan's hypotheses.

## 11. Algebraic K-theory (370)

For a unital ring and distinct stable indices \(i,j,k\),
\[
 [e_{ik}(a),e_{kj}(1)]=e_{ij}(a).
\]
This proves perfectness of the stable elementary group, since these elements generate it. The program checks the generic three-by-three matrix identity symbolically. For a commutative local ring, row reduction gives \(E(R)=\mathrm{SL}(R)\); over an arbitrary commutative ring that equality is not automatic. The stable Steinberg construction and the relation to \(K_2\) need the stable rank convention, not an arbitrary finite \(\mathrm{SL}_n\).

The coniveau spectral sequence and Bloch's formula require the correct regularity/Gersten conditions. Quillen's 1973 theorem supplies the regular finite-type-over-a-field case; it does not make the page's unqualified “X un schéma” sufficient. This memorandum does not claim a new proof of Quillen's theorem. Its role is to keep the stated hypothesis envelope exact.

## 12. Scalar extension and Frobenius (374)

Take \(X\) to be a countably infinite discrete set and \(R=\mathbb F_p[u]\). Then \(H^0(X;\mathbb F_p)\otimes R\to H^0(X;R)\) is the inclusion from \(\mathbb F_p^{\mathbb N}\otimes\mathbb F_p[u]\) into \(\mathbb F_p[u]^{\mathbb N}\). Every tensor is a finite sum, hence its coordinates have a common polynomial-degree bound. The sequence \((1,u,u^2,\ldots)\) has no such bound. This refutes unrestricted coefficient base change. Degreewise finite-dimensional cohomology, suitable finite-type chain hypotheses, or finite-dimensional \(R\) over \(\mathbb F_p\), supply familiar sufficient replacements.

Standard power operations on \(R\)-cochains are Frobenius-semilinear. For \(p=3\), let \(z\in H^2(\mathbb CP^\infty;\mathbb F_3)\) be the generator. Then \(P^1(uz)=(uz)^3=u^3z^3\), whereas \((P^1\otimes1)(uz)=uz^3\). Since \(u^3-u\ne0\), the two differ. Thus Frobenius is required on scalars for positive powers too, if the page means the usual power operations. A separately defined linear extension is possible, but it has different axioms. The source must decide which meaning was intended.

## 13. Additive-group extensions and category changes (374–376)

The length-two Witt extension is a nontrivial extension in abelian sheaves: multiplication by \(p\) on the middle sheaf is nonzero. Hence the middle sheaf is not an \(\mathbb F_p\)-module object. It cannot refute vanishing of \(\operatorname{Ext}^1\) in the category explicitly named on 375.

Breen's 1978 theorem, for the specified big sites containing affine spaces and with the characteristic-\(p\) structural sheaf, gives odd \(\mathbb F_p\)-linear Ext equal to zero and, over \(\mathbb F_p\), even degree \(2j>0\) equal to \(\mathbb F_p[F]/(F^{v_p(j)+1})\). The manuscript's \(v_p(j)\) would already force degree two to vanish, whereas the published expression has a nonzero class killed by \(F\). For a general perfect base field the Frobenius polynomial ring is twisted; its left and right actions must not be confused. The explicit comparison is in the program output, with visual verification of the published formula documented in the reference audit.

After perfection, the \(\mathbb F_p\)-linear higher Ext vanishes in all positive degrees, as precisely stated in Mathew, Theorem A.1, over a perfect \(\mathbb F_p\)-algebra on the big perfect étale site. The corresponding assertion for abelian sheaves has a different degree-one behavior. Mathew expressly notes that this perfect-site proof does not compute the nonperfect-site Ext of Breen 1978. Neither result fills in every step of the manuscript's spectral-sequence induction: the two edge-map lemmas and the power-operation comparison need their own compatibility arguments. Lemma 2's written calculation only treats \(P^0\); the arbitrary-index version is not proved there.

## 14. Limits of the checks

The source statements about topology, spectra, and algebraic geometry were matched to opened primary references with hypotheses recorded. They were not re-proved wholesale. The arithmetic identities, specified counterexamples, elementary categorical arguments, and operator calculations above were independently checked. Question marks with insufficient data remain questions; a search that found no exact theorem is recorded as a bounded negative search, never as evidence of novelty. No conjectural direction from the ranked list is developed in this memorandum.

## 15. Typing the connectivity estimate on 373

The displayed source is \(K(\mathbb Z,n)\wedge K(G,p)\), the target is written \(\mathbb ZK(G,n+p)\), and the bound is \(r=\min(n+2p-1,2n+p-1)\). Here \(p\) is a degree parameter, not necessarily a prime. One cannot infer a quasi-isomorphism until the smash/tensor and free-abelian conventions are specified. Under the ordinary space-smash and integral-homology interpretation there is an explicit counterexample. Put \(G=\mathbb Z,n=p=4\). The bound is11. By the checked stable calculation, \(\widetilde H_4K(\mathbb Z,4)=\mathbb Z\), \(H_5=0\), \(H_6=\mathbb Z/2\), and no reduced homology occurs below4. Integral Künneth therefore gives
\[
 \widetilde H_{10}(K(\mathbb Z,4)\wedge K(\mathbb Z,4);\mathbb Z)
 =(\mathbb Z/2)\oplus(\mathbb Z/2),
\]
from pairs of degrees \((4,6),(6,4)\). No Tor term can occur in total degree10, since a Tor contribution requires degrees adding to9, and the only available candidate pairs involve a zero group. In contrast the stable formula gives \(H_{10}(K(\mathbb Z,8);\mathbb Z)=\mathbb Z/2\). These groups are not isomorphic despite \(10<11\). Thus that literal reading is false. A tensor of simplicial abelian groups, or another resolved source, would be a different object and requires its own typed assertion. The computation is recorded in `root_supplement_checks.json`; it does not decide whether the missing manuscript scan resolves the notation.

## 16. Euler normalization on 328

The maximal compact circle of \(\mathrm{SL}_2(\mathbb R)\) acts on its defining oriented plane with weight one; on the projective boundary circle it acts with weight two. The map of classifying circles induced by the quotient therefore multiplies the integral Euler generator by two. For a genus-\(g\) Fuchsian surface representation, the projective-circle Euler number has magnitude \(2g-2\), so a lift's defining-plane Euler number has magnitude \(g-1\). This checks the factor-of-two distinction while leaving the orientation sign and which bundle the manuscript denotes unresolved. It does not provide a canonical lift, and it does not identify the split bundle on326–327 with an oper's nonsplit jet bundle.


## 17. The exact Dold theorem and diagonal-only naturality (360)

Dold’s original1961 paper, printedpp259–262, defines its natural transformations on the category of **ordered n-tuples** of FD complexes. Theorem1.6 makes the natural-Hom complex acyclic over Z. Sections1.7–1.12 then choose a separate positive free group-ring resolution W and construct W→Hom. In§2 the inputs are specialized to the same complex. Thus freeness of W must not be transferred to Hom, and independent-variable naturality must not be replaced by all transformations natural only in one diagonal variable.

There is a short counterexample to the latter replacement. For n=2 the four simplicial maps (x,y)↦(x,x),(x,y),(y,x),(y,y) are natural in X. Compose their chain maps with Alexander–Whitney to obtain four natural transformations C(X²)→C(X)⊗C(X). Evaluate on a constant two-point simplicial set and on the basis simplex(0,1). The outputs are the four distinct basis elements of Z[X²], so the transformations are linearly independent. All positive normalized chain groups vanish on this X; therefore a nonzero linear combination cannot be null-homotopic. Hence H0 of this diagonal-only natural-Hom complex has rank at least4, contradicting the claimed augmentation isomorphism to Z. The finite witness is root_diagonal_ops.json. This checks the manuscript’s assertion rather than assuming that its final insertion repaired every quantifier.

The same output records the quadratic normalization queried on346. With Psi2 basis e1,e2, the kernel of facesd1,d2 in Gamma² is generated by e1e2. Since d0(e1)=−e,d0(e2)=e, d0(e1e2)=−2e^(2). In Sym² the coefficient is−1. For normalized degree>2, a quadratic monomial cannot contain every coordinate required by the deletion-kernel conditions. Thus N Gamma²(Psi) has differential±2 from degree2 to1 and H1=Z/2, whereas N Sym²(Psi) is acyclic. No manuscript reading is changed.

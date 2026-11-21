# Separate algebraic-geometric restatements

## The common exact transport

Let \(E\) be a locally free sheaf of rank \(r\). Its frame torsor \(\operatorname{Isom}(\mathcal O^r,E)\) transports every equivariant polynomial map between the specified \(GL_r\)-modules to a natural map between associated locally free sheaves. The representation ring is the exact Grothendieck ring of the category of finite locally free representations; the class of an exterior power is the corresponding lambda operation. These are the constructions of SGA 3, Exposé I, Section 4.5 and Propositions 4.7.2--4.7.3, and SGA 6, Exposé VI, Theorem 3.3. The conjugation \(S^{\mathrm{int}}_\lambda=L_{\lambda'}\) used in A-012 fixes the integral Schur convention explicitly.

The evaluation homomorphism from the free special lambda ring sends \(e_i\) to \([\Lambda^iE]\). In rank \(r\), it factors through \(e_{r+1},e_{r+2},\ldots=0\); determinant inversion gives the Laurent representation ring of \(GL_r\). The precise universal locators are SGA 6 V Proposition 4.2, Definition 4.4, Proposition 4.8, and Corollary 4.9. Composition of the resulting operations is the Schur-functor composition proved by the actual functorial maps in the preceding parts.

Characteristic-zero averaging uses the idempotent \(|H|^{-1}\sum_{h\in H}h\). Its integral model is over \(\mathbb Z[1/|H|]\), a scheme over \(\mathbb Z\). Each additional rational presentation has finitely many coefficients and a finite Gröbner basis; invert the product of their denominators and leading coefficients. The resulting monic relations, module maps, and flat Gröbner family define the exact same generic-fiber construction over that localization. This construction specifies its base rather than silently extending an averaging argument across primes dividing its denominator.

## Dictionary for every theta and positive-formula finding

| Finding | Algebraic-geometric restatement and the map carrying the proof | Exact framework |
|---|---|---|
| T-001 | The complexification of the compact pair gives the polynomial algebra on \(E\otimes F\). Its two commuting group-scheme actions yield the Cauchy summands; the stated determinant square root records the oscillator pullback before its explicit removal. | SGA 3 I 4.5, 4.7.2; SGA 6 VI 3.3. |
| T-002 | Extract the \((n^m)\)-graded summand of the diagonal-torus comodule and apply the constant \(S_m\) idempotent. This associated summand is exactly the multiplicity module of \(S_\lambda E\). | SGA 3 I 4.7.3; SGA 6 V 4.2. |
| T-003 | Pull back the \(GL(S_\nu E)\) representation along its specified Schur-functor representation morphism; the wreath-group Hom is the equivalent tensor idempotent summand. | SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| T-004 | Interlacing patterns index the torus-graded Schur sheaf before the finite quotient; its Hilbert function is the stated weight multiplicity. | SGA 3 I 4.7.3. |
| T-005 | Tensoring by \(\det^t F\) shifts the torus grading and restricts to \(\operatorname{sgn}^t\) on the permutation subgroup. This line-bundle isomorphism transports the precise projector. | SGA 3 I 4.5, 4.7.2; SGA 6 V 4.8--4.9. |
| T-006 | The rank-two weight line is \(\det^j F\) times a balanced symmetric monomial; its swap scalar computes the invariant direct summand. | SGA 3 I 4.7.3; SGA 6 VI 3.3. |
| T-007 | The even-row decomposition becomes the indicated equality of associated Schur-sheaf classes after the frame-torsor pullback. | SGA 6 VI 3.3. |
| T-008 | Products of highest-weight sections in the stated integral-domain coordinate algebras give nonzero sections of the sum weight. This is the actual multiplication map proving support addition. | EGA I 9.5.1--9.5.3; SGA 3 I 4.7.2. |
| T-009 | The specified stretching Hilbert function has the recorded period-six values; Ehrhart reciprocity contradicts the proposed homogeneous-polytope Hilbert function. It leaves the proved cellwise presentations intact. | EGA I 9.5.3; the exact Hilbert grading is specified in T-009. |
| T-010 | The stable equality is an identity of Schur coefficients in the completed lambda ring; its transpose is the characteristic of the explicitly graded symmetric/exterior algebra \(\mathcal M_k\). | SGA 6 V 4.2, VI 3.3. |
| T-011 | The integer arrays index Littlewood--Richardson multiplicity bases. Applying the associated-bundle construction identifies the same counts in each tensor product of Schur sheaves. | SGA 6 VI 3.3. |
| T-012 | The width-five tensor factors, their finite exterior-cube table, and their glued LR arrays give the Hilbert components of \(\mathcal M_5\). | SGA 3 I 4.7.3; SGA 6 V 4.2. |
| T-013 | The independently certified 156-character table and the displayed tensor-factor maps give the identical statement for \(\mathcal M_6\). | SGA 3 I 4.7.3; SGA 6 VI 3.3. |
| T-014 | The specified products of highest-weight sections of the symmetric factors and degree-zero/one sections of the exterior factors give the claimed nonzero Schur-sheaf summand. | SGA 6 VI 3.3. |
| T-015 | The historical endpoint check concerns the same graded Chow pullback as G-003; its parameter range is now contained in the cited Sra bound. | EGA I 9.5.2; M-001 source audit. |
| T-016 | The cubic metric is a morphism of associated bundles; division of its adjugate by the square of the discriminant is regular by the proved divisor valuation. | EGA I 9.5.1--9.5.3; SGA 3 I 4.7.2. |
| T-017 | Matrix coefficients identify the specified homogeneous-bundle sections on \(GL_7/(G_2\times\mu_3)\) with stabilizer invariants. The harmonic and Pieri proof computes their rank. | SGA 3 I 4.7.2. |
| T-018 | Inclusion into the discriminant localization identifies extension with a nonnegative divisor valuation. The three polynomial highest sections generate the computed sector; their degrees are the polytope equations. | EGA I 9.5.3; SGA 3 I 4.7.3. |
| T-019 | Differentiation of the degree-seven section is the stated equivariant bundle map. Multiplication with the metric, cometric, determinant and remaining factors gives the associated stable Schur components. | SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| T-020 | The filtration by order along the boundary divisor is the explicit regular-extension subspace of the homogeneous-bundle section space. | EGA I 9.5.1--9.5.3. |

## Dictionary for the root constructions

| Finding | Algebraic-geometric statement and proof transport | Exact framework |
|---|---|---|
| G-001 | The exact Pieri multiplication sequence restricts on its all-ones weight to the augmentation kernel of the permutation module; determinant tensoring gives the sign twist. Its constant \(A_5\) restriction proves the stated monomial-basis obstruction. | SGA 3 I 4.7.2--4.7.3. |
| G-002 | The matrices are maps of free modules obtained from the two constant-group correspondences. Their determinantal ideals describe their rank strata; the Cauchy--Binet sum computes the same rank over the real generic fiber. | Stacks Project 07Z6, Lemmas 15.8.2 and 15.8.4; 05P8, Lemma 31.9.6. No unverified EGA Fitting locator is supplied. |
| G-003 | The divided-power coordinate pullback defines the integral scheme image and its torsion-free, graded-free coordinate algebra. Its rational grading is the canonical-map image. Hilbert and Quot schemes represent the stated flat projective families. | EGA I Prop.9.5.1, Cor.9.5.2, Def.9.5.3, Prop.9.5.4; FGA Exp.221 Thms.3.1--3.2, after Prop.3.8. |
| G-004 | The two rational Artin correspondences on a degree-two finite etale scheme have Frobenius eigenvalues \(1,-1\). The actual projector ranks are one and zero. | Weil II Defs.1.2.1--1.2.2, Variants 1.2.3--1.2.4, stability 1.2.5(i). |
| G-005 | The tree marks and polytope coordinates are identical; the rank-two determinant line and frame-torsor map transport the known branching count to Schur-sheaf operations. | SGA 6 VI 3.3; SGA 3 I 4.7.3. |
| G-006 | Binary factorization makes the Chow morphism dominant; its degreewise coordinate pullback is the specified canonical isomorphism. Natural Schur-functor decomposition carries every retained multiplicity map to any larger frame rank. | EGA I 9.5.2; SGA 6 VI 3.3. |
| G-007 | Restriction to the constant \(S_3\) subgroup gives three trace values on the balanced torus summand. The three character idempotents give the displayed ranks in the representation Grothendieck ring. | SGA 3 I 4.7.2--4.7.3; SGA 6 V 4.2. |
| G-008 | Exact quartic character certificates produce invariant sections; multiplication in their domain and the conjugation involution yield the displayed repeated-part Schur coefficients. | SGA 6 V 4.2, VI 3.3. |
| G-009 | The successive affine flag, torus, and finite-group quotients have the explicitly presented invariant ring. A flat monomial degeneration preserves its Hilbert function; disjoint standard-monomial cells yield the bounded lattice sets. | SGA 3 I 4.7.2--4.7.3; EGA I 9.5.2--9.5.3. |
| G-010 | Adjoining the symmetric algebra of the dual wreath representation gives its covariant module in auxiliary degree one. Graph elimination produces its exact graded presentation. | SGA 3 I 4.7.2; SGA 6 VI 3.3; EGA I 9.5.2. |
| G-011 | The two finite-group correspondences act linearly over their common invariant ring; their image is a finite coherent module. The syzygy/elimination presentation and module degeneration compute each actual image rank. | EGA I 9.5.2; SGA 3 I 4.7.2. |
| G-012 | The explicit flag quotient has two monic quadratic equations. Its four-element free module over the polynomial subring is the exact geometric source of the four polytopes. | SGA 3 I 4.7.3; EGA I 9.5.3. |

## Dictionary for rectangular findings

R-001 is the determinant line in the balanced Schur sheaf; its \(S_a\) restriction is the sign character to the stated power. R-002 identifies the contraction of the two normalized tensor projectors with the signed Latin-square count and with the Haar period, with all factorials retained. The finite scheme used in R-006 has one component per Latin square and the indicated sign function; its pushforward trace gives that same integer. These are constant finite-group schemes and their associated locally free sheaves, in SGA 3 I 4.7.2--4.7.3 and SGA 6 VI 3.3.

R-003 restricts the specified wreath permutation representation and computes its exterior powers; the explicit comparison with the rectangular Kronecker summand is via those two functor multiplicities. R-004's indicator variables give a bijection between the cited rectangular-hook basis and a zero-one polytope. R-005 is the natural inner-degree multiplication map of sheaves, with its nonzero determinant pairing and highest-weight dimension. The coordinate-image transfer uses EGA I 9.5.2 and the exact BIP morphism cited in its proof.

R-007 transports the two prime-adjacent integer congruences through the exact scalar and Haar identities of R-002, yielding the stated valuations in \(\mathbb Z_{(p)}\). R-008 works over that local base for its normalized tensors, then applies the rational central Schur projector to produce an actual preimage. R-009 uses the graded algebra morphism induced by the Chow multiplication map; its product equality persists under the frame-torsor transport. R-010 is an explicit differential-operator map on the polynomial coordinate sheaf, with its written kernel vectors. These are the same maps of SGA 3 representations and EGA I scheme images, rather than dimension comparisons used in place of maps.

## Dictionary for every archive finding

| Finding and archive locus | Exact transported statement | Locator |
|---|---|---|
| A-001, 133/019 | The Burnside ring marks, rank map, and signed permutation linearization compute the displayed discrepancy; exterior/symmetric operations remain the exact-K0 operations. | SGA 6 V 2.1, 2.2.1, VI 3.3. |
| A-002, 133/006 | The rank augmentation on strict quadratic spaces in characteristic two makes the proposed exterior-square rank impossible. | Archive definition; SGA 6 V 2.1 fixes the pre-lambda identities tested. |
| A-003, 133/006 | The displayed quotient from split orthogonal group completion to the metabolic Grothendieck--Witt ring kills the computed nonzero Adams defect. The forgetful maps specify both K0 targets. | Zibrowius 2015 Def.1.2 and main theorem; SGA 6 V 2.4.1 for the identity tested. |
| A-004, 133/008 | The written bilinear isometry identifies \(q\perp(-q)\) with a hyperbolic bundle after inverting two. The characteristic-two group-scheme representation gives the precise failure of the proposed relation. | SGA 3 I 4.7.2; archive 133/008. |
| A-005, 133/008 | The natural tensor/hyperbolic isometry proves the ideal statement; the computed exterior-square image proves failure of descent through the indicated Witt quotient. | SGA 6 V 2.1; archive quotient map. |
| A-006, 133/009 | The cited injective etale-cohomology pullback to a splitting space transports the root formulas. The real Kummer class is the explicit obstruction to the struck-out descent. | Zibrowius gamma paper Prop.3.3; SGA 6 V 3.2--3.4, 3.10. |
| A-007, 133/028 | The tensor-power operation and Young induction product give the exact virtual equality; the rank-two Adams example computes the failure of an effective-summand reading. | SGA 6 V 4.2 and VI 3.3; integral completion A-012. |
| A-008, 43/037 | The series involution \(f(t)\mapsto f(-t)^{-1}\) transports the Witt conventions, with the stated Frobenius/Verschiebung identities and ghost maps. | Archive 43/037; SGA 6 V 3.2--3.4 for the related lambda-series substitution. |
| A-009, 2/017 | Restriction is pullback of representations, induction is the explicit coset tensor construction, and the written map proves projection. The coinvariant example computes loss of local freeness for an arbitrary group map. | SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| A-010, 133 and SGA 6 | The free-lambda evaluation, rank-r quotient and determinant localization are the actual universal homomorphisms; the gamma substitution computes the rank-kernel filtration. | SGA 6 V 4.2, 4.4, 4.8--4.9; V 3.2--3.4, 3.10; VI 3.3. |
| A-011, 89/018 | The exterior pairing is a morphism of rank-two locally free sheaves; the displayed reconstruction is equivalent to the zero-sum relation under its explicitly proved nondegeneracy. | SGA 3 I 4.5; archive 89/018. |
| A-012, 133/028 | The integral Cauchy filtration is equivariant and compatible with base change. Three exact torus weight extractions give the tensor identity in the declared exact equivariant K0 on every commutatively ringed topos. | ABW II.2.16 and III.1.4; SGA 3 I 4.7.3; SGA 6 VI 3.3. |

The motivic and Lefschetz expressions on the remaining archive fragments require their own definitions before a scheme or realization map can be written. They are recorded in the unresolved part; the proved Artin example G-004 supplies an actual motive and projector in its stated scope.

## Additional explicit dictionaries for the small presentations and the uniform end-row family

| Finding | Restatement in schemes, comodules, or Schur operations, with the proof-carrying map | Framework locator |
|---|---|---|
| T-021 | Pullback of the coefficients of a product of four binary linear forms sends the quartic coefficient \(x_i\) to \(\binom4i^{-1}\sum_{|I|=i}\prod_{j\in I}b_j\prod_{j\notin I}a_j\). The resulting highest-weight coordinate algebra is the stated kernel of the locally nilpotent derivation, presented by \(T^2+4H^3-f^2HI+f^3J=0\). The localization and modulo-\(f\) injection in the proof establish the actual scheme-coordinate isomorphism. | EGA I 9.5.1–9.5.3; SGA 3 I 4.7.2. |
| T-022 | The monic equation gives a free module with basis \(1,T\) over \(\mathbf Q[f,H,I,J]\). Its two degree equations are exactly the two polytope systems, so the Schur coefficient is the corresponding graded rank. | SGA 3 I 4.7.3; SGA 6 VI 3.3. |
| T-023 | The specified weighted initial monomials define a subalgebra degeneration with the proved semigroup basis; the cusp equation is its initial relation. The exact basis correspondence proves flatness over the degeneration parameter and preserves each multigraded rank. | EGA I 9.5.3; the Rees construction and monomial independence are proved in T-023. |
| T-024 | The flag-face map is the affine incidence morphism with coordinates \(x_i,y_i,z\), relation \(\sum x_iy_i=0\), and determinant-one torus quotient \(\mathbf Q[u,v,z,t_i]/(\sum t_i,uv-\prod t_i)\). Literal row permutations give the recorded signed action. The dense incidence chart proves the kernel, rather than inferring an algebra from equal dimensions. | SGA 3 I 4.7.2–4.7.3; EGA I 9.5.2–9.5.3. |
| T-025 | The alternating-group quotient is a quadratic discriminant algebra with basis \(1,D\). Taking the remaining involution's eigenspaces selects the written parity of the standard monomials. Their weight equations reduce bijectively to \(\sum_{i=2}^m ic_i=R\), giving the indicated Schur-sheaf multiplicity and its exact support. | SGA 3 I 4.7.3; SGA 6 V 4.2 and VI 3.3. |
| T-026 | The weighted discriminant relation gives a monic quadratic Rees family, free with basis \(1,D\). The explicit rational rescaling turns the special fiber into the displayed binomial semigroup algebra. Taking the diagonal order-two invariants preserves the written parity basis and flatness over the localized integral base. | EGA I 9.5.3; SGA 3 I 4.7.2. |
| T-027 | Multiplication by \(u^{(n-\beta)_+}v^{(\beta-n)_+}z^\gamma\) identifies the balanced comodule with \(\operatorname{sgn}^{\beta}\otimes\operatorname{Sym}^{S}\mathfrak h_m\), where \(\mathfrak h_m\) is the quotient of the permutation bundle by its constant line. Taking the \([\mu]\)-covariant summand and computing its cycle traces gives the tableau generating function. | SGA 3 I 4.7.2–4.7.3; SGA 6 VI 3.3. |
| T-028 | The assignment matrix, descent variables, and partition variables have a proved one-to-one correspondence with the tableaux and partitions in that character formula. Hence the same covariant module has rank equal to the one explicitly described lattice count. The minimum and next graded terms yield the exact support criterion. | SGA 3 I 4.7.3; SGA 6 V 4.2. |
| T-029 | Each partial-flag face is an affine graded subalgebra. Inverting its invariant product of selected minors produces an explicit Laurent-polynomial algebra over its torus quotient. Its dimension, and the restriction of a finite homogeneous normalization to every face, force the negative integer \(c_{\{1,2,m-1\}}=2-m\). Thus the specified finite polynomial-subalgebra morphism cannot exist for the full highest-weight grading. | EGA I 9.5.3 for the affine algebra correspondence; SGA 3 I 4.7.3 for torus comodules; all dimension and face arguments are proved in T-029. |
| T-030 | The \(\omega_2\) face is the Plücker quadric. Its torus quotient is the trace-free matching plane with a determinant coordinate; the quotient homomorphism \(S_4\to S_3\) and the displayed alternating-form intertwiner identify every outer character. Its invariant affine scheme has equation \(27W^2+Z(D^2+4e^3)=0\). | SGA 3 I 4.7.2–4.7.3; SGA 6 VI 3.3; EGA I 9.5.3. |
| T-031 | Complementary-column exterior multiplication gives the perfect pairing into \(\det^H\); it transports the finite permutation projector with the exact sign twist. Multiplication by \(\prod_{i<j}[ij]\) gives the binary exterior-to-symmetric sheaf isomorphism, including determinant power \(\binom m2\). These two morphisms carry the proper-face formulas to the quartic presentation. | SGA 3 I 4.5 and 4.7.2; SGA 6 VI 3.3. |

## Additional dictionaries for canonical images and rectangular comparisons

**G-013.** The affine diagram \(j\Pi_a=\Pi_b\iota\) is defined by multiplication of forms and appending fixed basis forms. Its coordinate pullback is precisely \(h_{b,a}\operatorname{Sym}^b(j^*)=\iota^*h_{b,b}\). Block determinant evaluation takes the normalized square section to \(I_{a,b}\). Multiplication in the image coordinate ring then realizes every printed seed expression. The Apéry paths specify the exponents of actual preimage sections. The rational denominators specify a localization of \(\mathbf Z\) for each section. This is the scheme-image construction of EGA I 9.5.1–9.5.4 and the associated-representation construction of SGA 3 I 4.7.2; its Schur coefficient lies in the representation \(K_0\) of SGA 6 VI 3.3.

**G-014.** On the principal open where the pure-power Chow coefficient is invertible, the ordered-factor coordinates give the multisymmetric chart. The polynomial identity \(\mu_a(C_\beta)=uE_\beta\) and the degree-tracked homogenization prove equality of the image and normalization on each component with \(an-\lambda_1\le n\). This is a precise graded coordinate-ring statement; applying the Schur coefficient functional gives the canonical-map rank. The adjoint tensor projections give the stated isomorphism on the common first-row range. The relevant affine and representation locators are EGA I 9.5.2–9.5.3, SGA 3 I 4.7.2–4.7.3, and SGA 6 VI 3.3.

**R-011, R-012, and R-015.** Each common-polarization operator is a natural morphism of polynomial representation bundles. Its integer highest-weight presentation is specified by flag-minor Reynolds vectors. A nonzero minor of its evaluated image matrix modulo the displayed prime is a nonzero integral minor and therefore proves the asserted generic-fiber injectivity. The certificate lists every source multiplicity, so the argument covers the entire source functor. In the language of determinantal ideals, these computations exhibit the required nonzero minors of each finite multiplicity map; the exact general locators are Stacks 07Z6, Lemmas 15.8.2 and 15.8.4, and 05P8, Lemma 31.9.6. The bundle transport is SGA 3 I 4.7.2.

**R-013.** The morphism \(\nu_{L,b}:(\ell,q)\mapsto\ell^Lq\) is an integral affine-scheme morphism. Its degree-\(r\) coordinate pullback equals \(\binom bL^{-r}T_{r,L,b}\) over \(\mathbf Q\), with the scalar proved on pure products. The kernel is the degree-\(r\) ideal of the scheme image by EGA I 9.5.2. Multiplication in the ambient polynomial domain transports the certified vanishing to every lower degree. The cited Kadish–Landsberg Theorem 1.7 and its section 3 proof provide the known geometric map; the stated finite boundary kernels and scalar convention are evaluated here.

**R-014.** Padding and determinant realization give the actual inclusion \(\Gamma_n^M\hookrightarrow\mathrm{Det}_M\), hence the equivariant surjection of coordinate rings. The cited highest-weight padding injection and the stable rectangular-Kronecker identification transport this through the finite chain written in R-014. The end-row lattice count then gives an explicit effective lower bound in the representation Grothendieck group. The geometric framework is EGA I 9.5.2 and SGA 3 I 4.7.2, with the exact Ikenmeyer–Panova locators Proposition 2.6(b), Lemma 2.7, Proposition 2.8, and Theorem 2.1.

## Additional dictionaries for the recovered archive statements

| Finding and archive locus | Geometric or exact-K0 restatement and the actual comparison | Exact locator |
|---|---|---|
| A-013, 133/024–029 and supplied study | Injection powers and kernel partitions give explicit isomorphisms of finite-set-valued functors; composition and finite limits are computed by the written maps. The two-copy constant functor evaluated at a singleton disproves the single-power summand assertion. Applying the constant finite-scheme functor preserves the specified maps and products. | Archive 133/024–029; SGA 3 I 4.5 for the associated constant actions. |
| A-014, 4/007 | The two chain maps between the de Rham complex and \(\mathcal O\) have Frobenius composites. Passing to the Fitting-stable images gives their stated inverse. On a finite free Witt-vector lattice, Hensel separation of unit roots computes the stable reduction. The crystalline freeness and algebraicity inputs explicitly admitted in the original pages remain the exact application gates. | Original cote4, PDF pp3–7, §§8.3–8.5; Weil II 1.2.1–1.2.5 gives the weight terminology, not those missing crystalline inputs. |
| A-015, 133/006 | The integral universal iterate polynomial is evaluated on the concrete modular orthogonal representation. Its nonzero defect in the split group completion maps to zero under the specified metabolic quotient. | SGA 6 V 2.4.1, 2.4.2; archive category and quotient in A-003. |
| A-016, 16/038 | On the explicitly defined graded primitive-string modules, restriction and pushforward act by truncation and shift. The corrected projector identities hold on every displayed basis vector. For \(\mathbf P^1\) and a point, the actual cohomological maps refute the source's final projected equality. No algebraic-motivic realization of an unstated lowering operator is inferred. | Original cote16 PDF pp33–38; SGA 5 III 3.1–3.3 for the correspondence-to-cohomology construction. |
| A-017, 79/051 | Exterior multiplication of a rank-two \(\mathbf Z/n\)-module descends through the sign quotient. The identity \(\Lambda^2(a\,\mathrm{id})=a^2\mathrm{id}\) transports edge and face types. The wedge tests and the \(n=4\) calculation prove the stated recovery maps. These finite sets and maps may be represented as constant finite schemes; the reconstruction from one unlabeled complex remains separately recorded. | Original cote79 PDF pp47–51, (114)–(127); SGA 3 I 4.5 and 4.7.2. |
| A-018, 43/037 | A morphism from \(\operatorname{Spec}\mathbf Z[a_1,a_2,\ldots]\) depends on finitely many coordinates of each target function. Pullback along products of the universal line series sends \(a_i\) to the elementary symmetric polynomial \(e_i\); its proved injectivity forces equality of the two affine group-scheme morphisms. | Archive 43/037; EGA I 9.5.3 for the affine coordinate dictionary; SGA 6 V 4.2 for the universal symmetric-operation algebra. |
| A-019, 133/008 | The hyperbolic summand has a nonsingular polar form in every characteristic. The cited field cancellation isometry removes that actual summand and identifies the remaining form with the hyperbolic form of the dimension difference. | Elman–Karpenko–Merkurjev §8, Lemma 8.2 and Theorems 8.3–8.4, pp47–48; archive 133/008. |
| A-020, 133/028–029 study | The composition-factor homomorphism identifies exact \(G_0\) over \(\mathbf F_p\) with the free group on the absolutely simple modules. The decomposition matrix relates the Specht reductions to the simple labels; its rank at degree \(p\) is the proved modular obstruction to a polynomial induction ring on all \(\rho_i\). | James Theorem 11.5, p40; Corollaries 12.2–12.3, pp42–43; SGA 6 VI 3.3 for exact representation K0. |
| A-021, 133/028–029 study | Rationalization of finite locally free representations over a characteristic-zero DVR induces an isomorphism of exact representation groups, proved through the torsion boundary and commensurable lattices. It commutes with the actual tensor and induction functors, yielding the stated polynomial graded ring. | James 8.4, 8.6–8.11, 11.5, 12.2–12.3; SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| A-022, 133/009 and study | The nonisotropic-line pullback is injective on mod2 étale cohomology. Its actual symmetric-line summand and Kummer connecting map give \(w_2(H(L))=\bar c_1(L)\). The iterated splitting and Whitney product yield the displayed general hyperbolic formula in the proved scheme scope. | EKV Lemma 5.3 and Proposition 5.5, pp181–184; Zibrowius gamma paper Proposition 3.3, pp19–20; SGA 6 V §3 for the gamma-filtration comparison. |
| A-023, 133/028–029 study | Over the explicit local scheme \(\operatorname{Spec}(\mathbf Z_{(2)}[\varepsilon]/(2\varepsilon,\varepsilon^2))\), the rank-one constant-\(C_2\) comodule has character \(1+\varepsilon\). The determinant functor on exact sequences detects its class outside the subgroup generated by the two degree-two \(\rho\)-monomials. Rational base change kills \(\varepsilon\), so the exhibited class difference also lies in the kernel of rationalization. | SGA 3 I 4.7.2 for constant-group comodules; SGA 6 VI 3.3 for the exact representation group; the complete ring and determinant calculation is A-023. |

## Étale and correspondence locators used in the transport

For A-009, SGA 4, Exposé IV, **4.5.1** gives the restriction and induction morphisms of classifying topoi induced by a group homomorphism; **4.5.2** records the profinite version. The explicit coset tensor map in A-009 is the corresponding locally free representation calculation. These passages were opened and read, rather than inferred from the title of the exposé.

For G-004 and the realized cohomological examples of A-016, SGA 5, Exposé III, **3.1**, equations **(3.1.1)–(3.1.3)**, defines a cohomological correspondence; **3.2(b)(i)–(ii)** gives the diagonal and Frobenius-graph examples; **3.3**, equation **(3.3.3)**, gives its action on cohomology. The Artin projectors of G-004 are \((1\pm F)/2\) after passing to rational \(\ell\)-adic coefficients. Their finite étale realization and weight-zero eigenvalues are explicit. The projectors' ranks follow from the action on that two-dimensional space; no mod2 projector with denominator two is asserted.

## Exact dictionaries for the general chart, chamber sheaves, and truncation

**T-032.** The balanced diagonal-torus comodule algebra is localized at the explicit invariant section \(u=\prod x_i\). Its coordinate homomorphism sends each flag minor to \(u\mathbf1\wedge\bar w_2\wedge\cdots\), and the prescribed centered-matrix construction proves the inverse on the principal open. The extension subspace is the ideal-divisibility condition \(u^k\mid F(v(X))\) in the original affine coordinate ring. This is an explicit isomorphism of affine schemes with constant symmetric-group action (EGA I 9.5.3; SGA 3 I 4.7.2–4.7.3). Its Schur-coefficient functor is the corresponding exact representation-group functional in SGA 6 VI 3.3.

**T-033–T-034.** The homomorphism \(S_4\to SO(W)\), with \(W=\mathfrak h_4\otimes\operatorname{sgn}\), is specified by the invariant form and determinant-one row-permutation action. Restriction of the Schur comodule, the harmonic quotient by that form, and the explicit five character projectors give the finite polynomial counts. The complementary-column pairing transports the upper chamber with its computed determinant character. These are restriction and direct-summand morphisms of the SGA 3 I 4.7.2 representation category; their graded classes and exterior determinant operations are those of SGA 6 VI 3.3. The Elliott character calculation is proved in full in T-033, including the required intertwining action.

**T-035–T-036.** The affine incidence presentation yields the flag scheme \(\mathcal F\subset\mathbf P(W)\times\mathbf P(W)\) and its projective-line-bundle morphism \(\pi\). The exact coordinate equations identify each original divisor valuation with the order in the pulled-back ideal of one of four specified points. Thus the balanced comodule is the global-section representation of \(\pi^*\mathcal I_Z^k\otimes\mathcal O(c,b)\), with the printed determinant character. The two-quadric ideal resolution and the tautological quotient sequence calculate those sections, including the nonzero first-cohomology summand in T-036. The group-equivariant splitting is obtained by averaging an actual linear projection. These affine, ideal-sheaf, and locally free sheaf maps provide the full geometric restatement; the associated representation and K0 maps are SGA 3 I 4.7.2 and SGA 6 VI 3.3.

**R-016.** The normalized pullback of R-013 identifies each of the three computed kernels with the degree component of the ideal sheaf of the padded-form scheme image. Every source summand is listed; the selected nonzero minors prove the ranks and the displayed determinant polynomial supplies the entire missing irreducible summand. The scheme-image interpretation is EGA I 9.5.2, with the same determinantal-ideal maps already specified for R-015.

**R-017–R-018.** Separate homogenization and first-coordinate restriction are inverse maps between the indicated degree-bounded polynomial spaces. Coefficient extraction becomes the explicitly diagonal truncation operator with weights \(\prod_i\binom{b-d_i}{L}\). The flag-minor generators bound each block degree by the second row. Inverting those actual nonzero weights proves injectivity on the specified entire Schur-isotypic components, and applying each finite-group projector preserves it. Via R-013 this is the vanishing of precisely the indicated graded ideal components of the padded-form scheme image. These are equivariant coordinate-sheaf maps under EGA I 9.5.2–9.5.3 and SGA 3 I 4.7.2–4.7.3; their exact Schur operations lie in SGA 6 VI 3.3.

## Five-point modules and the complete four-point formula

**T-037.** The exact four-point incidence quotient is free over the polynomial algebra of its two quadratic generators through the averaged multiplication section. The two-quadric power resolution and tautological quotient sequence identify ordinary powers with the required flag sections in the proved degree range; the boundary correction is the displayed connecting cohomology module. The explicit complementary pairing and sign twist transport the resulting positive modules to every balanced Schur weight. These are ideal-sheaf, associated-bundle and exact-representation maps in EGA I 9.5.1–9.5.3, SGA 3 I 4.7.2–4.7.3 and SGA 6 VI 3.3.

**G-015–G-016.** The general balanced chart identifies extension across each original coordinate divisor with the ordinary power of a smooth flag fiber's ideal. Its leading normal ratios are independent over the fiber function field, including every higher Plücker frame. The point-ideal generators and canonical affine evaluation maps identify the saturated projective-frame scheme and its actual permutation quotient. The schemes and coordinate maps are the EGA I 9.5.1–9.5.3 constructions; the linearized flag line bundle is transported by the SGA 3 associated-bundle map, and its Schur class is the SGA 6 VI 3.3 operation. The exact Schur/section locator used is Magyar, Proposition1 pp5–6 and Proposition4(a)–(c) p10.

**T-038, A-028–A-029.** The five-point ideal has the written equivariant alternating resolution. Its actual quadratic image is the displayed cubic hypersurface, with the precise six-letter intertwiner. The Cox comparison sends exceptional sections and each Plücker bracket by (Cox.1), and identifies every Picard-graded section by the normal-order calculation. The ordinary Rees map is the specified inclusion into that Cox ring. Applied Kustin–Polini–Ulrich formula6.1.4 and Lemma6.3/Corollary6.4 give the linear-power complexes after every local hypothesis is checked. Saturation and cohomology follow from those complexes. These are concrete graded scheme and coherent-sheaf morphisms under EGA I 9.5.1–9.5.3; the flat-family Hilbert/Quot interpretation is FGA Exposé221 Theorems3.1–3.2. No new generic-position assertion is used.

**G-017.** The polynomial matrix (Q.9) presents the actual quotient-bundle section module. Its determinant, adjugate and generic evaluation prove an injection; the established ideal-power cohomology proves surjectivity degree by degree. Four explicit invariant parameters are regular by the determinant argument, and averaging a graded section gives the actual free multiplication isomorphism (Q.21). The corresponding coefficient is the constant-group covariant summand of the geometric module, carried by G-015 and T-003. The exact K0 operation is SGA6 VI3.3, and all determinant dualities are specified exterior pairings of locally free sheaves.

**G-018.** The dual tautological inclusion and linear multiplication identify the exterior quotient module with the concrete kernel (W.6). Stabilizer-invariant affine charts give the entire fat-point jet action, including its line-bundle trivialization. The finite Newton count is the exact rational character identity of that kernel. The EGA coherent sheaf, SGA3 comodule and SGA6 exterior-operation maps are precisely those just specified.

**G-019 and T-039.** The symmetric quotient sequence (SQ.4) is locally split before tensoring the ideal. Its global cohomology gives the exact representation-K0 formula, including the one nonzero connecting term at point order1. Relative exterior pairings give the determinant character in (SQ.3). Its fixed bivariate positive formula therefore computes Schur-operation multiplicities of actual ideal-twisted flag sections. The transport uses SGA3 I4.7.2–4.7.3 and SGA6 V4.2,4.4,4.8–4.9,VI3.3, with the projective-family interpretation of FGA221 Theorems3.1–3.2.

**T-040.** The degree-one Rees component has the explicit B-matrix resolution. The tautological inclusion into its tensor product with E gives the displayed quotient, whose full free resolution is verified by the rank-three reduction modulo the cubic. This supplies the actual module behind the positive residue formula. Its four-parameter obstruction is proved by the exact multiplication-sequence Hilbert series, which would have a negative finite quotient coefficient. The ordinary-power, saturation and quotient maps specify the geometric comparison.

**T-041.** The hook Schur functor is the kernel of the split symmetric multiplication map. The explicit two-step tautological hook resolution and its top-Cech identity prove all needed cohomology groups. Multiplication by the five quadrics is the actual section isomorphism (5H.12). These kernel, exterior-complement and symmetric operations are the locally free Schur operations transported in SGA6 VI3.3.

## Further actual canonical-image dictionaries

**R-019–R-020.** Complementary column pairings identify the entire first-row source band with a multilinear symmetric-group component. The explicit cofactor highest vector and nonzero coefficient prove the actual polarization rank. Through the padded-form scheme-image map R-013, this removes precisely those graded ideal components. The transport is the EGA I9.5.2 scheme-image coordinate map and the SGA3/SGA6 associated Schur-sheaf map.

**R-021.** The block specialization and multiplication in the graded Chow coordinate algebra carry prime-adjacent square determinant preimages to every stated rectangular and row-extended preimage. Nagura's exact prime interval determines the nonnegative exponents. Thus the nonzero coordinate section is in the actual canonical image; its determinant and highest-weight lines are the specified Schur operations in SGA6 VI3.3.

**R-022–R-024.** Normalized last-slot polarization sends the Chow image annihilator into the exact common-polarization kernel or into the lower-degree annihilator via (P.11). Slot transvections prove the rectangular prolongation equality, and the actual determinant preimage removes that summand. The two Pieri inclusions then prove the stated whole-isotypic vanishing of the graded ideal, including every multiplicity. These are maps of coordinate modules of the scheme image in EGA I9.5.2, transported to associated Schur sheaves by SGA3 I4.7.2 and SGA6 VI3.3. The degreewise minors give their rank strata as in the G-002 determinantal dictionary.

## All nonnegative five-point twists and the next canonical components

**G-020, T-042–T-043.** The locally split symmetric or hook quotient
complex, tensored with the specified ordinary ideal power, computes
its actual direct-image representation including every low-degree
cohomology term. The exact fat-point evaluation identifies each class
trace. The residue constants are therefore Schur-operation coefficients
of the displayed sheaf classes, and the subset-chain bijections convert
them into positive lattice counts. Their map locators are SGA 3 I
4.7.2–4.7.3, SGA 6 V 4.2,4.4,4.8–4.9 and VI 3.3; the underlying
coordinate and ideal morphisms are EGA I 9.5.1–9.5.3. Relative exterior
pairings specify every determinant character. The FGA Exposé221,
Theorems3.1–3.2 interpretation uses the same finite graded modules in
families, with the denominators of the characteristic-zero projectors
retained.

**G-021.** The signed tensor differential (S.1) and the rational Young
idempotent define an actual complex of locally free sheaves. The
specified rational intertwiners identify its terms with the three Schur
bundles in (TR.5), and the averaged local contraction proves exactness
after ideal tensor. Its derived direct image is concentrated in degree
zero in the proved range. Thus (TR.8) is its class in the exact
representation group of SGA 6 VI 3.3, transported by the frame torsor
of SGA 3 I 4.5,4.7.2. The exact Schur-section dictionary is Magyar,
Propositions1 and4, with the relative dual pairing in (TR.3). The
finite coefficientwise inequalities and polytope bijections calculate
this same class; they introduce no unstated realization functor.
The multiplication by \(u^e\) and perfect exterior pairing (TR.19)
carry the result to both outside regions. These are concrete maps of
the EGA I 9.5.3 coordinate representations. In the archive language,
they evaluate the Schur compositions and tensor operations of cote133,
scans024–029, through the universal operation map of A-010 and A-012.

**R-025–R-026.** The determinant and signed cofactor formulas are
integral highest sections in the ordered-factor coordinate ring. Their
specified column averages descend to symmetric sections. The exterior
complement pairing computes the entire one-dimensional Schur
multiplicity space. Normalized slot splitting and coefficient
polarization send the actual scheme-image annihilator into the lower
common kernel. The nonzero factorial coefficients, including the exact
apolar differential pairing in BS.28–31, exclude the unique indicated
component from that annihilator. Hence these are computed ranks of the
graded coordinate-image morphism in EGA I 9.5.2, and positive Schur
summands in its SGA 6 VI 3.3 representation class. Scalar extension in
the endpoint uses the injective field map to the displayed splitting
field and is explicitly reflected in its integral polynomial identity.

## Maps for the further central and nonvanishing families

**T-044--T-046.** The signed tensor/Young-idempotent construction gives the same actual ideal-tensored Schur complex of locally free sheaves. T-045 computes the first-power connecting map as one fifth of contraction and gives its explicit polarization right inverse. T-046 restricts point jets to the ten pair lines and identifies the full first-cohomology cokernel through those actual sheaf maps; the induced determinant line fixes its stabilizer character. Taking the derived direct image and its exact representation class is SGA6 VI3.3, transported by the SGA3 I4.5,4.7.2--4.7.3 frame torsor. Its explicit finite group character and positive polytopes evaluate the same cote133/024--029 composition as G-015.

**G-022--G-023.** The cycle endomorphism diag(t)g on the Schur bundle and its balanced coefficient extraction compute the literal finite-normalizer projector. The Weyl-determinant identity gives the exact cycle trace polytopes. The box injection, forest denominator proof and fixed positive Newton formulas are rank computations for that same SGA6 Schur operation, with the SGA3 frame maps specified in ST5--6 and SF3--7.

**G-024--G-025.** The flag-minor polynomial f_eta is an explicitly constructed invariant section. Multiplication by it, then by the indicated determinant section, is an injective map of actual balanced Schur components in a polynomial domain. Its cokernel gives an effective representation class in SGA6 VI3.3; no unidentified realization is used. IN17 is the exact inclusion--grid-permutation--projection pullback for multiplying linear forms. Its nonzero rational value and the precise CIM/McKay maps give a nonzero graded Chow coordinate-image section in EGA I9.5.2. These maps evaluate cote133/024--029 through A-010, with their integral polynomial expressions and stated characteristic-zero projectors.

**R-027.** The explicit cofactor sections, normalized last-slot inclusion and common-polarization coefficient map descend to the same coordinate-image scheme as R-025--R-026. The endpoint apolar chain rules and Vandermonde scalar identify the actual nonzero component, giving rank one in its EGA I9.5.2 graded image and its SGA6 VI3.3 representation class. The splitting-field evaluation uses an injective scalar-extension map, as recorded in the proof.

## Exact arrangement, strict support and endpoint-strip transports

**G-027 and T-049.** The local quotient substitution Y0=−xY is an injective normal-order comparison over the fraction field of the generic square matrix. Intersecting its point conditions gives the specified coherent arrangement ideal. The independent-block substitution sends each standard block to ell_i⊗F; its kernel on the product module is exactly the regular diagonal sequence, by the complete Koszul–restriction argument. Its sheaf is the fat frame arrangement, and the local Čech calculation proves saturation. These are explicit morphisms of affine and projective coordinate schemes (EGA I9.5.2; EGA II2.5), with the SGA3 I4.5,4.7.2–4.7.3 comodule action. The Schur operations are SGA6 V4.2,4.4,4.8–4.9 and cote133/024–029 via A010. To enter the locally free K0 of SGA6 VI3.3, take the finite equivariant graded free resolutions specified in G027§6, sheafify, and use their alternating class. Minimal invariant generator lifts and the Koszul Tor bound prove termination; Eisenbud, Lectures on the Geometry of Syzygies, Theorems1.2–1.3,p118 is the exact primary finite-resolution locator. This gives the actual coherent-to-locally-free comparison rather than assigning coherent objects directly to that locator.

**G-026 and T-047--T-048.** G026 extracts the Schur component of the signed coherent restriction complex. Its orientation line is the exterior determinant of the selected subset, fixing the induced stabilizer signs. T047 uses the finite normal substitution w=XYv and the displayed square-zero unipotent bundle automorphism; its global Schur cokernel diagram identifies actual first cohomology with the stated induced bundle sections. T048 evaluates that exact image at defect three. The same finite-resolution map carries their coherent complexes to SGA6 VI3.3, and the exact frame/complement maps carry their positive counts back to cote133/024–029.

**G-028.** Multiplication by the specified invariant sums of squares and determinant sections gives the strict-chamber embeddings as actual sheaf-section maps. The two normalized rays are transported by the explicit complement pairing and the k0 quotient-section isomorphism. Their characters and the exhaustive76-seed/14-generator certificate give the exact zero sets. The degree-five image ranks use the literal canonical kernel, normalized transpose and Schur component maps; they are graded ranks in the EGA I9.5.2 coordinate-image construction, including the zero image at (12,5,4,3,1). These are statements about precisely identified morphisms.

**R-028--R-030.** Every polynomial section is given by actual determinants and cofactors. The perfect complementary-column pairing fixes the source multiplicity and its sign projector; the retained-slot and common-polarization maps are the normalized tensor maps K16–22. Their apolar coefficient evaluations and all scalar signs are computed explicitly. The positive factorial bounds therefore prove actual ranks in the same coordinate-image scheme and representation K0. Scalar extension and ambient inclusion commute with each displayed polynomial map. This supplies the full EGA I9.5.2 / SGA3 / SGA6 transport for both endpoint strips.

Exact Proj locator refinement: the affine-base gluing and scheme theorem used for all displayed Proj charts are EGA II2.4.1–2.4.2, printedp28. The graded associated-sheaf functor and its exactness are EGA II2.5.2 and2.5.4, printedp31. The finite-resolution transport above uses the latter on Proj(S), with no assertion that pullback to the Rees Proj preserves exactness. These original-page locators supersede the earlier shorthand reference to all these constructions as EGAII2.5.


## Exact transport of G029, T050 and R031–R032

**G-029.** The graph edges are multiplication by the explicit invariant flag sections of G024. Its contractions use the actual G027 section map and multiplication by u on the balanced chart. The complementary outer wall uses the perfect exterior-column pairing and its determinant sign. These are SGA3 I4.5,4.7.2–4.7.3 comodule morphisms; the Schur operations are SGA6 V4.2,4.4,4.8–4.9 and cote133/024–029 via A010. EGA II2.4.1–2.4.2 supplies the Proj charts, II2.5.2,2.5.4 the exact associated-sheaf transport. The finite equivariant resolution of G027§6 gives the locally free K0 class of SGA6 VI3.3. Thus the wall support tables compute the ranks of these specified component maps.

**T-050.** The actual signed restriction complex of G027 identifies the complete order-k jet cokernel with the oriented pair module. Its displayed symmetric multiplication and determinant(v,z1,z2)^c map fix the Schur component and the even determinant twist. Taking its finite equivariant free resolution gives the same exact coherent-to-locally-free K0 transport. This extends the positive coefficient formula to every permitted k without asserting an unproved extension of a different geometric line-restriction map. Each final Newton polytope counts the already identified Schur multiplicity.

**R-031.** The tensor averaging pairing identifies the dual of h_{d,e} with h_{e,d} with scalar one. The transverse-block calculation identifies the fourth-square map with the stated rational multiple of Jacob's adjacency operator. Its invertible right-multiplication matrix and the multilinear Schur–Weyl component map prove actual injectivity. These normalized maps define the corresponding graded coordinate-image scheme by EGA I9.5.2, commute with SGA3 base extension, and act on the same SGA6 Schur classes. The image multiplicities are the graded coordinate-image ranks. Jacob's source computation and the independently verified finite matrix are distinguished in the proof and check ledger.

**R-032.** Every step of the annihilator injection is the displayed symmetric coproduct followed by common polarization, with its explicit binomial scalar. The perfect pairing carries the final injection to a bound for the actual coordinate-image cokernel, not only an inequality between abstract Schur characters. Successive Pieri component maps identify the polynomial chain counts with the specified tensor codomain. The construction is rational and functorial, hence transports to SGA3 representation group schemes and their SGA6 representation K0; its graded coordinate-image ranks use EGA I9.5.2. The exact Schur/plethystic archive dictionary is cote133/024–029 via A010.


## Complete support, oscillator and linear-band transports

**G030–G031 and T051.** Their exact maps are the stated normal-order substitution, signed arrangement quotient, rank-adaptive Young extraction and invariant-section multiplication. The complete support catalog is transported by the actual first-end chart and last-end complementary-column pairing, with both determinant signs retained. The frame models exist over Z[1/5], and each fixed-degree Young projection is defined after inverting its factorial denominators. The generic-fiber ranks use SGA3 I4.5,I4.7.2–4.7.3, SGA6 V4.2,4.4,4.8–4.9, EGA II2.4.1–2.4.2 and II2.5.2,2.5.4. G027§6's finite free resolutions give the locally free K0 transport of SGA6 VI3.3. The archive comparison is cote133/024–029 via A010.

**T052.** The affine polynomial scheme has coordinates X_ai,Y_i and contraction equations R_a=Σ_iX_aiY_i. The block homogenization is an actual map on each multigraded module, compatible with multiplication by the diagonal generators. Its quotient is precisely the frame-arrangement module, and the rational polynomial q(ΣR_aC_a)/q(0) gives its harmonic splitting. The displayed GL(F), GL(W), torus and permutation actions are comodules and their Lie operators in SGA3 I4.5,I4.7.2–4.7.3. The real symplectic embedding and the explicit vacuum character provide the unitary realization after scalar extension. Complementary exterior columns and the rational Gram form give the exact Schur/dual comparison in SGA6 V4.2,4.4,4.8–4.9, and hence the cote133/024–029 dictionary. The coherent quotient and its finite resolutions use the same EGA II/SGA6 VI3.3 transport as G027.

**R033–R034.** The exterior transfer is the actual GL2 raising operator on the skew-Cauchy summand; its kernel, rational Gram coevaluation and projected matching tensor produce a specified invariant section. Its balanced flag map is UT16. The derivative kernel in LP7 is the actual Cauchy summand, with spectator tensor factors retained, and LP12 is the normalized coproduct/common-polarization injection. Duality is the scalar-one tensor pairing of R031. These rational natural transformations define the SGA3 representation-comodule maps and the SGA6 Schur operations just cited. Their image ranks belong to the EGA I9.5.2 graded coordinate-image scheme. UT19 further specifies the Chow-padding, determinant-realization and coordinate-restriction maps used in the rectangular comparison. Each fixed-degree construction has an integral model after clearing its displayed averaging and factorial denominators; all asserted ranks concern characteristic zero.

## R035: exact low-second-row image scheme

The determinant-square section, normalized tensor pairing and scalar-one transpose give the actual natural map SR14. Its Schur component and the complete tail exclusion use the explicit skew-Cauchy Young embedding SR17 and hook Gram dualities. These are SGA3 I4.5,I4.7.2–4.7.3 comodule morphisms and SGA6 V4.2,4.4,4.8–4.9 Schur operations, with the cote133/024–029 dictionary of A010. Applying the associated-bundle construction on a principal GL bundle glues exactly these local polynomial maps. Their graded image is the coordinate-image scheme of EGA I9.5.2, whose stated multiplicity ranks are therefore computed by the same scalar identity. Fixed-degree integral models are obtained by inverting the displayed factorial and averaging denominators; the assertions concern characteristic-zero fibers.

## T053: incidence quotient and actual Rees schemes

The algebra map sends ell_i⊗f_a to[X_aiY_i] and sends tΠ_i(ell_i⊗f_(a_i)) toΠ_iX_(a_i,i). Its cross-charge identity gives the full Rees isomorphism. The torus coaction and the invariant subring(B[z])^T define the actual affine quotient morphism; these use SGA3 I4.5,I4.7.2–4.7.3. The displayed Koszul complex is a finite equivariant locally free resolution on SpecP, giving its SGA6 VI3.3 class. EGA II2.4.1–2.4.2 and II2.5.2,2.5.4 govern its Proj charts and exact sheafification. The direct monic rewrite proves the displayed family free over Q[s], hence flat, with its exact inverse general-fiber scaling. The Rees Proj isomorphism comes from the algebra isomorphism itself. The Schur-operation locators are SGA6 V4.2,4.4,4.8–4.9, with cote133/024–029 transported by A010.


## Third-order section classes and cubic canonical images

**G-032.** The map is the exact normal substitution and rank-three Young extraction
\(M=\operatorname{Hom}_{GL_3}(S_{(a+c,b+c,c)}\mathbb Q^3,J_3)\).
Exterior column contraction gives
\(M\simeq\operatorname{sgn}^cH^0(\mathcal I_Z^3(c)S_{(a,b)}Q)\),
because \(\det Q=\operatorname{sgn}\otimes\mathcal O(1)\).
The oriented quotient/restriction complex gives its exact class; the finite
skew-Schur character and subset-chain bijection calculate this same
Schur-operation coefficient. The complement morphism is the perfect
exterior pairing into \((\det\mathbb Q^5)^H\), retaining its
\(\operatorname{sgn}^H\) character. The affine/projective maps are
EGA II2.4.1–2.4.2 and2.5.2/2.5.4; the associated-bundle functor is
SGA3 I4.5,4.7.2–4.7.3, and its exact representation operation is
SGA6 VI3.3 with the free λ-ring evaluation V4.2,4.4,4.8–4.9.
The archive comparison is cote133/028 through the actual tensor-word,
torus-weight and Young maps of A012.

**R-036.** The actual exterior-algebra surjection sends a two-form or
three-form on the auxiliary space to the sum of its products in each
projected standard row. Signed equality-partition expansion proves its
surjectivity, and the skew Cauchy idempotents exclude every unlisted
tail. The affine-minor polynomial gives an explicit highest section of
the Chow coordinate module. The normalized grid pullback sends that
section by the exact scalar CT20 to the corresponding section with
interchanged block degrees; its adjoint determines the full stated
image and cokernel. Over a rational base scheme, the map
\(M\mapsto\mathscr F(E)\times_{GL(V)}M\) carries each tensor map
and rational projector to an associated-bundle arrow. The frame maps
are SGA3 I4.5,4.7.2–4.7.3; the representation-to-K0 morphism is
SGA6 VI3.3, and its λ-operation is V4.2,4.4,4.8–4.9. The actual Chow
scheme-image ideal is EGA I9.5.2, with projective module construction
EGA II2.5.2/2.5.4. This evaluates the cote133/028 tensor/Schur operation
through A012, including all characteristic-zero projector denominators.


## Complete central walls and further actual coordinate images

**T-054 and G-033.** The actual oriented quotient complex of the fat frame
arrangement is extracted by the rational GL2 Young projector. Singleton
strip cutoffs are removed in its character by the explicit paired
Jacobi–Trudi involution; the pair term uses exterior contraction and
binary Clebsch–Gordan maps. The triple term is the actual Pieri map to
the complementary line; the finite coefficient reindexing and reversed
normal series compute its character with the printed orientation.
Its exact coherent class is therefore the same one counted by the
positive subset-chain polytopes. Stable first-row multiplication by
\(u^e\) and the perfect exterior pairing into \((\det\mathbb Q^5)^H\)
transport all wall branches, including every sign. These are the
EGA II2.4.1–2.4.2/2.5.2/2.5.4 coordinate and sheaf maps, the
SGA3 I4.5/4.7.2–4.7.3 frame/comodule maps, and the SGA6 VI3.3
representation-to-K0 morphism. The λ-operation locators are
SGA6 V4.2,4.4,4.8–4.9 and the archive comparison is cote133/028
through A012's actual tensor-word, torus-weight and Young maps.

**R-037.** The morphism is the pullback of the product map
\(V^a\to\operatorname{Sym}^aV\). Its graded algebra multiplication
carries the normalized determinant-square column preimages to their
literal nonzero product. The highest section gives a reached Chow
coordinate-image class under EGA I9.5.2, and the same tensor-product
and Schur-projector arrows give its associated-bundle class by
SGA6 VI3.3 and SGA3 I4.5/4.7.2–4.7.3. This is the cote133/028
composition transported by A012, retaining the explicit scalar inverses.

**R-038.** The centered quartic basis and its exact per-variable
extension give two specified highest sections, or the unique extension
line at degrees two and three. The normalized Chow pullback has the
printed two-by-two matrix and adjugate inverse. These are explicit
matrices in the same EGA I9.5.2 image module and SGA6 VI3.3 associated
Schur sheaves. Their rank is within the known canonical binary theorem
G006/Landsberg Theorem7.21; the new form records its actual generators,
scalars and inverse maps.

**R-039.** The four-column exterior-invariant algebra is generated by
literal row power sums after the standard projection. Its Pfaffian
quotient and Young/Pieri maps give the unit multiplicity bound. The
mixed affine-minor determinant is an explicit highest coordinate section;
normalized row pairing gives the nonzero scalar or exact length-zero
endpoint, with an explicit inverse on every reached line. The same
frame functor carries these maps to associated bundles, with SGA3
I4.5/4.7.2–4.7.3 and SGA6 VI3.3 locators and the exact EGA I9.5.2
Chow image. The cote133/028 comparison is A012's tensor/Schur map.


## The adjacent walls and weighted mixed-minor image

**T-055, T-056 and G-034.** The rank-three normal Young projector
extracts the same coherent section module as the normal-order and
balanced homogenization isomorphisms of G027/T049. The pair character
is carried by actual exterior-dual, dual-Pieri and binary-contraction
maps. The triple character comes from the actual complementary-line
Pieri map and the complete coefficient telescope OW6–8, retaining
the selected-subset orientation. The section class in K0 therefore
has the exact positive lattice-point count OW11–12. The frame,
coordinate and associated-sheaf arrows are EGA II2.4.1–2.4.2,
2.5.2/2.5.4; SGA3 I4.5/4.7.2–4.7.3; and SGA6 VI3.3.
The Schur operations are SGA6 V4.2,4.4,4.8–4.9, and the archive
cote133/028 comparison is A012's tensor-word, weight and Young map.
Stable first-row multiplication and perfect determinant-column pairing
are specified on every branch, including both central-gap-one walls.

**R-040.** The exterior-invariant-algebra surjection, unique vertical
Pieri strip and rectangle-four pairing give the exact unit space and
its finite exceptional zero. The complementary-minor tensor and its
weighted affine Cauchy–Binet form define the same highest polynomial
section by the printed identity D=−a²F. Its literal row-degree-four
cancellation proves extension at degree three. The normalized Chow
pullback of R037 EP3–5 has scalar HC17 and inverse HC18. These exact
matrices carry through the frame functor to SGA3 I4.5/4.7.2–4.7.3,
SGA6 VI3.3 associated bundles, and the EGA I9.5.2 image module.
Cote133/028 is again carried by the actual Schur/tensor composition
map of A012; no coefficient-only comparison replaces the image map.


**T-057.** The singleton is the actual horizontal-strip line-branching summand in G027's oriented quotient complex. Row multilinearity of the full three-row Schur determinant computes that same summand; the exterior-column map removes a determinant only in the proved range of nonnegative shifted parts. The explicit failed extension loses the actual negative straightened Schur class. Its corrected equalities carry through the same SGA6 VI3.3 representation-to-sheaf morphism and SGA6 V4.2/4.4/4.8–4.9 Schur operations, with SGA3 I4.5/4.7.2–4.7.3 frame maps and the cote133/028 tensor/Young dictionary A012. Thus the counterexample and both refinements have the same precise geometric comparison.


**R-041.** The actual exterior-algebra map induced by orthogonal projection from a zero-padded standard representation sends every row power-sum generator to its finite-row counterpart. Its GL4 Young summand gives the proved finite-row invariant surjection. The three centered tensors have the explicit affine-minor expressions QE5, so their highest sections extend at degree four. The scalar-one Chow pullback R037 EP3–5 has the exact matrix QE18–20 and its finite-row quotient matrices. These rational tensor maps descend through SGA3 I4.5/4.7.2–4.7.3 frame torsors to SGA6 VI3.3 associated Schur sheaves and the EGA I9.5.2 coordinate-image module. The operations are SGA6 V4.2/4.4/4.8–4.9; cote133/028 is transported through A012's explicit Schur/tensor maps.


## The complete outer-five formula and single-four image band

**T-058, T-059, G-035 and G-036.** The balanced Cauchy/tensor-word
map identifies the Schur operation with the actual normalizer module.
Invariant first-row multiplication and the exterior-column perfect
pairing are CF3 and CF7, including their polynomial inverse, Gram
duality and determinant local system. The G027/T049 normal Young
extraction and oriented quotient arrows compute the same coherent
section module. T058's exterior-minor and rational highest-space maps,
T059's full Jacobi–Trudi row-multilinearity and G035's triple telescope
give every trace. Their affine branch maps have displayed inverses.
The selector and increasing-subset bijections give the positive
lattice counts CF10. The generic-fiber representation-to-associated-
sheaf morphism is SGA6 VI3.3, its Schur operations are SGA6
V4.2,4.4,4.8–4.9, and its frame/comodule maps are SGA3
I4.5/4.7.2–4.7.3. The section and Proj arrows are EGA II2.4.1–2.4.2
and2.5.2/2.5.4. The archive cote133/028 comparison is A012's
explicit tensor-word, torus-weight and Young map. The integral
tensor constructions are retained; rational projectors are spread
over the explicit localized base on which their denominators invert.
No unspecified modular constancy is used.

**R-042–R-044.** The row-power-sum morphism SF4 and actual
skew-Cauchy Young projectors exhaust the single-four highest spaces.
The centered Gram polynomials, weighted affine-minor identities,
separate homogenization maps and normalized moment pairings give
the stated finite matrices. The cubic row-degree functional in
R042 and the exact cubic combination ME19 retain their actual
extension kernels. Scalar-one tensor adjunction and the nonzero
matrix minors give the canonical image and rational preimages,
including all finite-row endpoints. The graded Chow pullback is
R037 EP3–5 and the scheme-theoretic image is EGA I9.5.2.
The same rational matrices yield the associated-bundle morphism
on the SGA3 I4.5/4.7.2–4.7.3 frame torsor and its SGA6 VI3.3
class; SGA6 V4.2,4.4,4.8–4.9 transports the Schur composition.
Cote133/028 is carried by A012's exact tensor composition map.
The image conclusion is proved by these matrices and inverses.


## Varying hook kernels and the repeated-four matrix

**T-060 and G-037.** The stable flag algebra map T032/C4–8 and
determinant volume pairing identify the given Schur class with the
actual hook module on the sum-zero permutation representation.
The hook Young inclusion is the kernel of HK5, and the explicit
Euler/exterior derivative homotopy proves the exact complex.
Macdonald's virtual principal specialization computes the traces
of this same module; deleting cells(1,1),(2,1) gives the exact
positive numerator. Solomon's differential map, scaled by1/j,
identifies the invariant complex with the weighted Koszul complex
on e2,...,em. HK14 is an actual polynomial basis of its cycles.
The two integer-matrix bijections count precisely the resulting
tableau/subset and monomial-cycle labels. These coherent kernels,
frame torsors, associated bundles and Schur operations use EGA
II2.4.1–2.4.2,2.5.2/2.5.4; SGA3 I4.5/4.7.2–4.7.3;
SGA6 VI3.3 and V4.2,4.4,4.8–4.9. Cote133/028 is carried
by A012's actual tensor-word, weight and Young maps.

**R-045.** Diagonal evaluation of row-symmetric polynomial tensors
and rational polarization give the injective moment morphism DF7.
Translation of the actual functional proves the exact filtration
identity DF9. The four bracket polynomials have the full normalized
map DF20 and cubic map DF27; their determinants, finite relations
and endpoint minors supply actual preimages and image ranks.
The coordinate-ring morphism is R037 EP3–5, with EGA I9.5.2
scheme-theoretic image. The same finite matrices give the associated
bundle map on the SGA3 frame torsor and its SGA6 VI3.3 class.
The Schur-operation and cote133/028 comparisons are the same actual
Young/tensor maps used throughout the rank calculations.


## All hook modules and faithful finite moments

**A088.** The actual homogeneous Koszul maps over
\(\operatorname{Spec}\mathbb Q[e_2,\ldots,e_m]\) define coherent
cycle sheaves. The basis lifts and graded splitting in §1 give
their free nontrivial Specht sheaves. The trivial component's
weighted Koszul presentation gives the exact Fitting-rank test
at the invariant origin and the exhibited local frame on each
\(D(e_i)\); its top cycle has the displayed global generator.
The comparison uses the actual differential-form map of Solomon,
the associated-bundle maps of SGA3 I4.5/4.7.2–4.7.3,
EGA II2.4.1–2.4.2 and2.5.2/2.5.4, and Schur operations
in SGA6 VI3.3 and V4.2,4.4,4.8–4.9. Archive cote133/028
is transported by A012's explicit tensor-word and Young maps.

**R046.** TM4–22 are morphisms of rational coordinate algebras
and their associated coherent isotypic sheaves. The Chow
pullback and normalized grid pairing of R037 EP3–5 identify
the composite with the actual canonical map. Centered row
projection, zero-padding transpose and the displayed Möbius
automorphism give the specified injective morphisms, so the
scheme-theoretic image has the asserted whole component.
Use EGA I9.5.2 for that image, SGA3 I4.5/4.7.2–4.7.3
for frame descent, and SGA6 VI3.3 and V4.2,4.4,4.8–4.9
for the exact Schur and Grothendieck-group operations. The
integral lattice has the displayed finite factorial and row
denominators inverted; the theorem itself is in characteristic
zero, without an unproved integral rank assertion.


## Higher transfer kernels, fat jets and the refined centered map

**G038–G039.** The actual equivariant derivative transfer on the free
P-modules over the reflection representation gives coherent kernels.
Their finite cokernels and minimal covers live over
\(\operatorname{Spec}\mathbb Q[e_2,\ldots,e_m]\). The explicit
basis cancellations give the free sheaf plus the displayed Koszul
syzygy sheaves. At second part three, the Kulkarni tensor quotient,
Ricci contraction and rational inverse identify the exact action of
e2; restriction to \(\mathbb Q[e_2^2,e_3,\ldots,e_m]\) and its
free rank-two extension retain every degree. Each least-support
monomial cycle is mapped back to the original transfer kernel.
The flag identification T032 C4–8 and determinant pairing then
give the stated original Schur coefficient. The sheaf, frame and
Schur-operation locators are EGA II2.4.1–2.4.2,2.5.2/2.5.4;
SGA3 I4.5/4.7.2–4.7.3; SGA6 VI3.3 and V4.2,4.4,4.8–4.9.
Cote133/028 is compared by A012's integral tensor-word and Young maps.

**T062–T065.** The frame's kth ideal sheaf on projective space,
twisted horizontal differential forms and exact finite jet quotient
are the specified coherent objects. The actual quadratic separators,
Taylor matrix, invariant Gram right inverse and horizontal Euler
contraction split the quotient in every asserted range. The endpoint
uses Nagel–Trok Theorem5.3 p233 and Lemma3.1 p225, with its precise
regularity-index convention. Flag projection and the determinant
line identify this kernel with the original multiplicity object.
The orbit/exterior induction maps and Young projectors compute the
finite quotient; the full lattice-point deletion supplies its positive
dimension formula. Projective and bundle comparisons use the same
EGA II and SGA3 locators, and their representation-K0 classes use the
specified SGA6 Schur operations. The fixed-order complexity and the
ordinary part-list encoding qualifications are retained under this
dictionary.

**R047–R049.** Perfect complementary-column pairings give R047's
finite reflection modules with determinant fourth power. R048's
explicit unipotent congruence and Pfaffian highest vectors give the
paired Schur decomposition. R049's map sends an extra row to the
small mean vector; on centered decompositions it is literally
\(1_{\Lambda T}\otimes q\), with the displayed kernel injection.
The alternating-weight occupancy bound removes that precise Schur
summand from the kernel character. Ordinary and skew Cauchy use
the identical Schur map of q because their rational Young projectors
commute with its tensor powers. Independent-row polarization and
the triangular moment automorphism identify the composite with
the normalized Chow pullback in R037 EP3–5. Thus EGA I9.5.2's
scheme-theoretic image has the asserted full component. The Euler
form and its nonzero Vandermonde evaluation give a literal section
in each positive family. Frame descent and representation-K0
transport again use SGA3 I4.5/4.7.2–4.7.3, SGA6 VI3.3 and
V4.2,4.4,4.8–4.9, with the rational denominators explicitly retained.


## Every fixed second part through a finite coherent cokernel

**G040.** FS3 is the actual derivative transfer of polynomial
bundles. Its finite coherent cokernel has support in degrees
b−1 through2b−2 and is annihilated by e_i for i≥b. The exact
covariant module therefore descends to the low affine base
\(\operatorname{Spec}\mathbb Q[e_2,\ldots,e_{\min(m,b-1)}]\).
The specified minimal homogeneous covers and invertible triangular
basis changes split off the free summand of the original transfer
kernel. FS13 is a literal inverse in each high-variable multidegree.
The leading-term filtration on the residual low-variable kernel,
with its displayed triangular lifts, carries every retained lattice
point to a vector in the same coherent kernel. Thus the finite
positive description is transported to the original balanced flag
and its determinant line, rather than inferred from an unrelated
character equality. The precise module/sheaf and projective
locators are EGA II2.4.1–2.4.2 and2.5.2/2.5.4; the frame maps
are SGA3 I4.5/4.7.2–4.7.3; the representation-K0 and Schur
operations are SGA6 VI3.3 and V4.2,4.4,4.8–4.9. The archive
transport is A012's integral tensor-word/Young comparison for
cote133/028. The rational maps retain the stated characteristic-zero
base and explicit-m input convention.


## The exact pair correction in the fat-frame complex

**T066.** The coherent restriction complex is G027 FA4 on the
degree-N part of the fat linear arrangement, with T049's actual
diagonal quotient and every ordered-subset orientation. The physical
partition inequality is exactly N≥mk. Exact Schur multiplicity
projection preserves the complex. The a-rectangle exterior pairing
gives its ambient hook module; normal Taylor substitution and the
horizontal local frames give the singleton jet object. The pair's
Cartan multiplication and complementary-column pairing give its
displayed induced exterior-power representation with all determinant
lines. Concentration leaves the exact sequence PB15, so the net
correction is the dimension of the actual image sheaf's fiber.
Its lattice-point deletion is carried to that same kernel dimension.
The flag/projective and coherent sheaf locators are EGA
II2.4.1–2.4.2 and2.5.2/2.5.4; descent is SGA3 I4.5 and
4.7.2–4.7.3; Schur operations and the representation-K0 identity
are SGA6 VI3.3 and V4.2,4.4,4.8–4.9. Cote133/028 uses
the same actual tensor-word and Young maps of A012.


## Complete hook-tail canonical isomorphisms

**R050.** The finite moment algebra in degrees2 through s maps by
literal polarized power sums onto the centered row-invariant algebra.
Newton recurrence proves its finite generation bound. Its hook
Schur sheaves have the same dimensions as the target, carried by the
actual invariant differential-form and Euler/Koszul basis maps;
surjectivity therefore makes this specified map an isomorphism on
those sheaves. The input highest section retains its actual separate
row degree n under dehomogenization. Independent functional
evaluation lies in the same finite moment algebra, and its diagonal
polarization is an inverse on its image. The exact triangular moment
automorphism and Chow pullback give HM17 with scalar one. Opposite
injections prove the full bundle isomorphisms. The explicit
Vandermonde/affine-minor section and Cauchy–Binet evaluation give
the nonzero unit scalar and its reciprocal.
The image morphism is R037 EP3–5 and EGA I9.5.2. The projective
and coherent comparisons use EGA II2.4.1–2.4.2,2.5.2/2.5.4;
the frame descent uses SGA3 I4.5/4.7.2–4.7.3; the Schur and
representation-K0 operations use SGA6 VI3.3 and V4.2,4.4,4.8–4.9.
Cote133/028 is carried by A012's exact tensor-word/Young dictionary.


## Complete fixed-order hook charts

**T067.** G027 FA4 and T049 give the actual coherent restriction
complex and diagonal quotient. AF9–12 are perfect exterior-column
pairings on the normal and residual summands; their contractions
preserve the chosen determinant lines and ordered-subset orientation.
The residual skew module has disjoint row and column slots, yielding
the displayed symmetric/exterior tensor isomorphism. Rational normal
raising kernels, block-mean splittings and Young induction compute
the remaining exact terms. Its first image is the same jet sheaf
under the triangular Taylor and horizontal-form maps, proving all
correction bounds. The ordered primitive-Young kernel basis gives
the stated rational linear comparison with the retained point set.
Projective/coherent transport uses EGA II2.4.1–2.4.2,2.5.2/2.5.4;
frame descent uses SGA3 I4.5/4.7.2–4.7.3; representation-K0 and
Schur operations use SGA6 VI3.3 and V4.2,4.4,4.8–4.9. Cote133/028 is carried by A012's
exact tensor-word and Young maps.

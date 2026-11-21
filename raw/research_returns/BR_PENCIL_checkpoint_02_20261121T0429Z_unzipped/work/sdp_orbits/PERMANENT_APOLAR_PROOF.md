# A characteristic-free obstruction for the exceptional permanent five-plane

Author: `/root/sdp_orbits`, GPT-6 Astra Pro, inherited effort not separately exposed; run BR_PENCIL-20261121-R1/sdp_orbits; date 2026-11-21.

## PA-01. A necessary pair of prolongation conditions

Let k be algebraically closed, let T∈A⊗B⊗C, and put U=T(C*)⊂A⊗B. Suppose r<=dim(A⊗B) and BR(T)<=r. There exists an r-dimensional subspace E⊂A⊗B containing U such that

`rank Phi_A(E) <= (dim A-1)r`, `rank Phi_B(E) <= (dim B-1)r`,

where

`Phi_A(E): A⊗E -> Λ²A⊗B`, `v⊗(a⊗b) -> (v∧a)⊗b`,

`Phi_B(E): B⊗E -> A⊗Λ²B`, `w⊗(a⊗b) -> a⊗(w∧b)`.

These are the degree-(210) and degree-(120) necessary border-apolarity tests, equivalently the lower bounds r on their prolongation kernels. Only this elementary necessary form is used.

### Full proof

On Gr(r,A⊗B), let S be the tautological rank-r bundle. The two displayed maps are morphisms of locally free sheaves `A⊗S -> Λ²A⊗B` and `B⊗S -> A⊗Λ²B`. Their rank bounds define closed determinantal loci. If E is spanned by r independent rank-one elements `a_l⊗b_l`, the image of Phi_A is the sum of r subspaces `(A∧a_l)⊗b_l`, each of dimension dim A-1; the first rank bound follows. The second follows identically. Independence is required only to make E an r-plane, not for either rank estimate.

The incidence `T(C*)⊂E` is also closed, since it is the vanishing of the composite `C* -> A⊗B -> (A⊗B)/S`. Intersect it with both determinantal loci in the product of the affine tensor space with the Grassmannian. Projection to tensor space is proper, so its image is closed.

This image contains a dense subset of the border-rank-at-most-r cone. Indeed, tuples of r pure A⊗B tensors with independent underlying vectors form a nonempty open subset of the irreducible r-fold product of affine Segre cones: choose r distinct matrix units to see nonemptiness. With arbitrary C factors, their sums are tensors of rank at most r and lie in the projected incidence. Density of the independent-tuples open set and continuity of the sum parametrization imply that the closure of these tensors contains every sum of r pure tensors, hence the entire border-rank-at-most-r cone. Therefore every T of border rank at most r lies in the closed projected incidence and has an E as claimed. This proof also permits tensors of smaller border rank: the unused terms can be padded and perturbed inside the same parameter space. It uses only properness and determinantal closedness, so it holds in every characteristic. QED.

Known-method attribution: the construction is the degree-three part of border apolarity. Conner–Huang–Landsberg, *Bad and good news for Strassen's laser method: Border rank of perm3 and strict submultiplicativity*, author manuscript `CHLlaser5-6-21.pdf`, Proposition 2.1, equation (4), printed p.7, and its A/B-interchanged version, uses these conditions in the permanent problem. The short form above is fully proved because its rectangular dimensions and all-characteristic use are needed here. It is not claimed as a new general method.

## PA-02. The exceptional permanent five-plane has border rank at least eleven

Let A=k⁵ with basis c0,...,c4; let B and C be two copies of k⁹ with ordered bases a,b,c,d,e,f,g,h,i. Write xy+yx for `x_B⊗y_C+y_B⊗x_C`. Define

`T=c0⊗(ae+ea+bd+db)`
`  +c1⊗(af+fa+cd+dc)`
`  +c2⊗(bf+fb+ce+ec)`
`  +c3⊗(ah+ha+bg+gb)`
`  +c4⊗(ai+ia+cg+gc)`.

Then `BR(T)>=11` over every algebraically closed field, including characteristic two. This is the coordinate orbit `[0,1,3,6,7]` in the root's rectangle numbering. The tensor uses ordered coefficient matrices and does not divide by two.

### Explicit linear-algebra certificate

Let U=T(C*), whose nine columns are the contractions in the order a,...,i. Order A⊗B coordinates lexicographically (A index first). Let U also denote its 45×9 basis matrix. Define `Z_s: A⊗B -> Λ²A⊗B` by `Z_s(X)=c_s∧X`, with wedge pairs ordered lexicographically and then the B coordinate. Put

`K=[Z_0 U | ... | Z_4 U]` (90×45).

The certificate provides an integer 50×90 matrix L with only 82 nonzero entries, and forms

`H=[LZ_0; ...; LZ_4]` (250×45),

`E_0=[U | c2⊗a]` (45×10),

`R=Phi_B(E_0)` (180×90),

where Phi_B uses lexicographic wedge pairs followed by the A coordinate, and input order (B coordinate, E_0 basis coordinate).

The exact identities and unit minors are:

| Matrix or identity | Shape | Certified minor size | Exact determinant |
|---|---:|---:|---:|
| K | 90×45 | 40 | +1 |
| L | 50×90 | 50 | −1 |
| H | 250×45 | 35 | −1 |
| E_0 | 45×10 | 10 | +1 |
| R | 180×90 | 82 | −1 |
| LK=0 | 50×45 | — | exact integer zero |
| HE_0=0 | 250×10 | — | exact integer zero |

Every row/column index and every nonzero entry of L is in `permanent_apolar_certificate.json`. All remaining matrices are determined by the five displayed quadrics and the definitions above. The standalone verifier `check_permanent_apolar_certificate.py` reconstructs them using only Python's standard library, checks both zero identities, and computes every listed determinant by fraction-free Bareiss elimination over Z. It does not import the generator, call a symbolic rank/nullspace oracle, use floating-point arithmetic, or rely on a numerical tolerance. Its executed output is `permanent_apolar_verification.json`, with all assertions PASS.

### Full proof from the certificate

The unit minor in E_0 makes its ten columns independent over every field; in particular U has dimension nine. Since L has full row rank50 and LK=0, K has rank at most90−50=40. Its unit 40-minor gives the reverse inequality, so `rank K=40` and `im K=ker L` in every field. Since H has rank at least35 while its kernel contains the ten independent columns E_0, its rank is exactly35 and

`ker H = U + k(c2⊗a)`.

Suppose BR(T)<=10. PA-01 supplies a ten-plane E containing U with

`rank Phi_A(E)<=4·10=40`, `rank Phi_B(E)<=8·10=80`.

Because the first map restricted to A⊗U has image im K of dimension40, its image on all A⊗E is exactly im K. Hence every X∈E satisfies `Z_s(X)∈im K=ker L` for every s. Therefore HX=0, and `E⊂ker H=span(E_0)`. Both have dimension ten, so E=span(E_0). But R is Phi_B on precisely this space, and its unit 82-minor implies `rank Phi_B(E)>=82`, contradicting the required bound80. Thus BR(T)>=11. QED.

The proof has no torus-fixed assumption and no symbolic parameters left to eliminate. It checks every possible E at once by the first prolongation constraint, which forces the unique candidate.

### Consequence for the main minimum

Combined with the root's exhaustive five-subset lower bounds for all other coordinate orbits, PA-02 raises the permanent's uniform residual lower bound from10 to11. P-01 reduces arbitrary five-planes to coordinate five-planes; P-06 gives an anchored five-edge upper witness of border rank11. Therefore in characteristic zero

`min_{W∈Gr(5,U_{4,2}^{per})} BR(P_W)=11`,

and generalized border substitution gives `BR(per4)>=36−5+11=42`.

The all-characteristic scope of PA-02 itself does not automatically upgrade every other orbit's modular certificate; the final global field scope must use the actual certificate scope of the exhaustive enumeration. In particular, no modular nonzero minor is silently treated as a unit minor.

## Algebraic-geometric dictionary

PA-01 is a relative Grassmannian with tautological subbundle, two exterior-power bundle morphisms, their determinantal rank loci, and a proper projection of incidence. Its proof is fiberwise over each algebraically closed field, so it does not require formation of a global integral secant ideal to commute with reduction modulo p. The appropriate foundational locators are EGA II, Definition5.4.1/Proposition5.4.2 and Theorem5.5.3(i), already cited in GCT_GINEQ F-18.

PA-02's matrices are morphisms of finite free Z-modules. Unit minors certify their ranks after every base change and, in the indicated degrees, identify the required kernels and images. Exterior powers give the corresponding lambda operations in K_0; for example the target class of Phi_A is `lambda²[A]·[B]`. The certificate uses the actual morphism and its minors, not just that K_0 class, consistently with GCT_GINEQ F-20. The determinant signs coalesce harmlessly in characteristic two. No Hermitian metric, norm, SDP, l-adic weight or motive occurs in this argument. No manuscript cote or scan is claimed to contain this new calculation.

## Check status

The independently implemented verifier has executed successfully. The full proof above must be read from start to finish before the final paper is marked checked; the subsequent check event records that read. The pencil agent has independently obtained the same exceptional lower bound using a different torus-weight saturation/prolongation certificate, providing a separate mathematical check.

### Whole-proof read completed

At 2026-11-21T03:20:31Z, the complete `permanent_apolar.tex` was read from beginning to end, including the necessary-condition lemma and R04 (the final-paper identifier for PA-02). The dense-parameter/properness step, all matrix dimensions, both zero-product implications, unit-minor field scope, unique-extension deduction and final82>80 contradiction were checked. No gap was found. The original note's characteristic-zero limitation on the *global* consequence is superseded in the final TeX only after the separate global unit-minor audit reported by the parent; this note does not claim to have independently rechecked every new global characteristic certificate.

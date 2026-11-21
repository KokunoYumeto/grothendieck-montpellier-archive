# Independent full-proof review of IF-08 and IF-09

Reviewer: GPT-6 Astra Pro; effort not exposed; SIGN_NEXT child `/root/critical_lefschetz`.
Date: 21 November2026. The complete initial source and later added local-frame and ordinary-L-squared passages were read.
Source: `SIGN_NEXT/work/integral_fock/kernel_intertwiner.tex`; main initial read at SHA256 `09fface62eb0651ac0ec1442d50daddf006dbbbefde875729c1bd8ed8c032e6e`, expanded read at SHA256 `9df42076394967a4608761ad6566738703aef0b6df7dde0010272c2d13ef47f4`.
The author's contribution was not edited.

## Verdict

The complete IF-08 and IF-09 arguments pass independent reconstruction. This includes saturation of the full cyclic Weyl tensor lattice, the normalized dual, the explicit coefficient-moment operator, transpose direction of the test kernel, determinant insertions, the actual two-step weights, and primitivity of the coordinate-kernel composite. The added local-frame formula and fixed ordinary-L-squared obstruction also pass with the precise conventions described below.

Final revision check at03:39:44 UTC: `kernel_intertwiner.tex`, SHA256 `47c5163c4343d0a3a2bc48775a6451bd321f770f8e6f93446b8ffc4c838c9d15`, now explicitly defines the coefficient frame B=C^(-t) for round columns and states the obstruction for integral embeddings and two applications of the same fixed L. I read those exact changes. Both requested precision fixes are accepted, and no outstanding condition remains.

The source's integral straightening and normalized Weyl/dual-Weyl theorems are used as supplied theorems and were checked for their exact statements. They were not independently re-proved or Lean-kernel-checked in this review. The new saturation deduction from them was independently derived.

## IF-08: saturation and normalized lattices

IF-04 gives pi*pi=c_lambda on the rational cyclic subspace T_Q. The standard-monomial theorem identifies the full tensor image as nabla_Z: the fixed column-height multiset is exactly the multiset determined by the partition, and repetitions, arbitrary row choices, signs and zero minors are all covered by the tensor basis. The supplied rational Weyl equality says this full rational image is already the image of T_Q.

For t in T_Q and k in ker pi, the IF-04 adjoint identity gives c_lambda(t,k)=(pi t,pi k)=0. A dimension count then gives T_Q=(ker pi)^perp. Thus pi*pi=c_lambda P on the whole ambient tensor, exactly as stated. There is no assumption that an arbitrary rational irreducible summand splits integrally.

For t integral in T_Q, normalized pairing of pi t with pi v is (t,v), an integer for every ambient integer tensor v. Because the pi v span nabla_Z, normalized duality puts pi t in Delta_Z. IF-04's integral inverse then puts t in T_Z. This proves saturation. The other normalized duality gives Phi(T_Z^sharp)=nabla_Z. Equivalently P(A_Z)=T_Z^sharp, since every integral functional on the primitive T_Z extends to the ambient free unimodular lattice. The projection may have denominators; the proof explicitly records them in the dual lattice instead of suppressing them.

The scalar c_lambda is the factorial Fock norm of the initial minor product. Extra ambient rows do not occur in that product, so it is independent of ambient rank. Dividing the polynomial pairing by this same scalar is exactly what makes Phi an isometry and makes test-side factors cancel. No implicit unit assumption on c_lambda is needed.

## IF-08: coefficient matrices and transpose direction

For a b-by-a matrix Z, the exterior matrix has coefficient det Z[I,J] on each wedge factor. Under the polynomial substitution X_(i,s) -> sum_u Z_(u,i) X_(u,s), determinant multilinearity gives exactly those same coefficients. Multiplication over columns proves pi_b A_lambda(Z)=rho_Z pi_a with all signs. The source `subD` uses this orientation. When b<a, its unused source columns s>=b are sent to zero; the minor image only uses the first length(lambda)<=b columns, so the identity is unchanged. The author added a common-column convention to make this explicit.

The coefficient matrices preserve rational T without assuming an integral representation decomposition. The minor identity preserves the kernels; applying it to Z^t makes the transpose preserve the opposite kernel. Orthogonal complements therefore give A_lambda(Z)T_a subset T_b for every rational specialization. Polynomial vanishing over Q gives the same containment coefficient by coefficient. Those coefficients are integer matrices, and saturation then gives A_beta T_a subset T_b integrally. Taking any finite R-linear combination with moments J(beta) proves the claimed base-ring assertion.

I independently checked the source test orientation in `KM.Gxz` and `KM.applyAt0`. Its minor is that of XZ with initial X rows and chosen target columns I. Cauchy--Binet gives a sum over source columns J with coefficient det Z[J,I]. This is the transpose of the forward exterior matrix. Thus the equation in IF-08h is the forward operator tested against the normalized dual, rather than a mistakenly reversed action. The factorial is exactly beta!: differentiation at zero and the actual source `applyAt0` multiply a Taylor coefficient by that number.

Determinant multiplication inserts full-height columns. A top wedge is a primitive norm-one vector and is killed by every off-diagonal root. Its cyclic tensor is therefore exactly the determinant-twisted Weyl lattice. At the source rank this insertion is even an isomorphism onto the corresponding full-height tensor factor; after a later rank inclusion it remains a primitive coordinate insertion. The source and target Fock normalization constants can differ, but each isometry uses its own constant, so the normalized insertion has no extra scalar.

Consequently the operator conjugations are integral lattice isomorphisms, and preserve image, cokernel, saturated image and local elementary divisors. Rectangular or deficient-rank maps require index in the saturation of the image, as the text correctly states.

## Local frames and global columns

I read the actual `CoefMod.actP`, `transLat`, `delP`, `delK`, `rhoVr`, `delAtr`, `CoefCol.roundPk`, `colVal`, and `Record.stepH` definitions. The latter uses `intDel`; the coefficient lattice is Weyl, with the dual-Weyl lattice used for testing. The transported frame action is det(B)^s times the exterior tensor action of B because `actP` uses the transposed polynomial row action. The condition actP(B^-1)x in the standard lattice therefore means that the local lattice has basis R_lambda(B) times a standard basis. This gives the block conjugation R_target(B')^-1 M R_source(B).

For actual round columns, `delAtr` uses the dual frame lattice and `rhoVr` uses inverse transpose. Thus if C is a frame of the original geometric lattice, the B entering the displayed coefficient-frame formula is C^(-t), not C. I asked that this convention be made explicit beside IF-08k. Applying the correct convention transports the global intersection of local lattices even when its coefficient ideals are nonprincipal; no nonexistent global integral basis is used.

The scalar block factor matches `GL3Theta.lift_formula` and `DataKernels.Kmap/K`: both rho factors and inverse stabilizer cardinality remain. Its valuation is the sum of the two character valuations minus the stabilizer valuation. The source `jetC` contributes the stated period-generator powers to the ordinary derivative moment. Determinantal minima give the sums of the smallest elementary-divisor exponents over a DVR; successive differences give individual exponents. For an integral rank-r matrix, the r-th minimum is the image length in its saturation. These formulas are correct, including possible cancellations inside determinants, since the minimum is taken after forming each actual determinant.

## IF-09: independent numerical derivation

For rank8 the half-sum is (7/2,5/2,3/2,1/2,-1/2,-3/2,-5/2,-7/2). Subtracting it from the displayed u gives lambda0=(53,21,18,15,12,9,6,3). The source wG values are88 and90, giving the two appended blocks -88 and-90. `lamTrue` subtracts8j from every entry. Consequently the three determinant shifts are3,-96,-106, and subtracting them gives exactly alpha0,alpha1,alpha2 in IF-09a.

The sharp powers are100-24/2=88 and118-40/2=98. Adding the current determinant shifts gives insertion orders3+88=91 and-96+98=2. The target division powers are100-8/2=96 and118-24/2=106. This independently verifies all four ties in the exact source `WtTie` convention, and hence the complete D91/B_J1/D2/B_J2 chain. Its two degree increments are728 and48.

The simple-root gaps are32,3,91,2. I independently compute 32*31=992, binom(32,2)=496=16*31, 91*90=8190, and binom(91,2)=4095=9*5*7*13; the d=2 and3 rows likewise agree. For `numBig`, changing the last u entry to-7/2 changes the last initial weight to0, the first insertion to88, and only the last entries91,93 of the kernel diagrams to88,90. The new gaps6 and88 give15 and3828=4*3*11*29. The text correctly distinguishes the numerical `numEx` record from a full `NumFacts` witness and does not promote the test family to an actual global automorphic theta function.

## IF-09: primitive composite and unit period

For the coordinate-inclusion exponential, the actual source `ThE` coefficient is the inverse factorial on diagonal-supported monomials and zero elsewhere. Its factorial moment is exactly A^beta. Evaluating the polynomial exterior matrix at A therefore gives B_J=A_lambda(A).

The composite primitivity claim is correct. Each rank inclusion maps ambient tensor basis vectors injectively to distinct ambient tensor basis vectors. Each determinant insertion tensors with a fixed primitive basis vector. Their composite is therefore a primitive coordinate embedding of the first ambient tensor into the last. Since the initial cyclic T is saturated in its ambient tensor, its composite image is saturated in the last ambient tensor, and therefore also saturated in the final cyclic T that contains it. Equivalently, because the maps in question are injective, transitivity of primitive sublattice inclusions gives the same conclusion.

The initial highest vector becomes the final highest vector: the inserted full-height columns are initial wedges, and the coordinate inclusions retain all their initial row sets. That final vector has normalized norm1. The dual highest functional therefore evaluates it to1. On the polynomial side only the highest diagonal monomial survives the diagonal exponential moment; its coefficient1 and the reciprocal/multiplying factorials give the same unit. No uncomputed scalar remains.

The new ordinary-L-squared obstruction is valid for two successive applications of the same fixed ordinary Lefschetz operator on one full integral symplectic exterior lattice. L^2=2L^(2) puts every output in2V. A saturated integral embedding preserves a primitive vector, giving the stated contradiction; an isometric embedding also gives a contradiction because the target highest vector has norm1 while every nonzero vector in2V has norm at least4. I asked that the statement say integral embeddings and the same fixed L explicitly. This obstruction does not apply to two unrelated Lefschetz operators, and the text correctly does not rule out divided-power or tensor-functor realizations.

## Limits and outstanding numerical data

This construction supplies an explicit finite formula in the actual moment entries and transports their actual lattices, denominators and invariant submodules. It does not determine the Smith numbers of an unspecified global automorphic theta kernel: those require the actual finite jet values, frames, class representatives and scalars. The text states that limitation. The concrete exponential test has its data fully specified and proves the unit-period and ordinary-L-squared statements only for that family. No new algebraic correspondence on a geometric abelian variety is produced merely by the formal coefficient-space isomorphism.

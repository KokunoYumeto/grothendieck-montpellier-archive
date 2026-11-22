# F59 continuation: an exact tensor-dimension inequality over two variables

Author: `/root/rectangular_and_theta`, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This note proves the module step needed for the remaining altered-scalar rank-one product case. The initial torsion-free observation was proposed by `/root/grothendieck_dictionary`; the argument below includes torsion-bearing modules. The separate descending-cohomology induction is being written by that agent. No conclusion for higher-dimensional polynomial rings is asserted here.

## 1. Precise setting

Let k be a field and let A=k[x,y] with x,y of positive degrees. Put m=(x,y) and let K be the fraction field of A. All modules and actions are unital. A finite graded module means finitely generated with its usual bounded-below grading; homogeneous generator degrees may be negative. For a finite graded left A-module M define

`rank_A M = dim_K(K tensor_A M)`.

Let V be a nonzero finite-dimensional graded right A-module, with the right actions of x,y homogeneous of their positive degrees. In particular its support is the origin: a sufficiently large power of m acts by zero. Write `len(V)=dim_k V`.

The assumptions on V hold automatically for `V=k tensor_A M` when M is a finite graded A-bimodule, finite on the left, with homogeneous commuting left and right actions. The quotient by the left m-action is stable under the right action. It is a nonzero finite-dimensional graded right module whenever M is nonzero, by graded Nakayama.

## 2. Tensor-dimension theorem

### Proposition TM-A

For every finite graded left A-module M of rank r,

`dim_k(V tensor_A M) >= r dim_k V`.

Equality holds if and only if M is a finite graded free left A-module. This includes the zero module as the free module of rank zero.

### Proof, torsion-free case

First suppose M is torsion-free. The zero case is immediate. Choose a minimal graded free resolution F of M by successively choosing homogeneous bases modulo m for M and its successive syzygies. Each syzygy is finitely generated because A is Noetherian. Every differential has entries in m. Consequently

`Tor_i^A(k,M) = k tensor_A F_i`

as graded vector spaces: after tensoring by k every differential is zero.

The two-variable Koszul complex

`0 -> A -> A^2 -> A -> k -> 0`,

with maps `a -> (-ya,xa)` and `(b,c) -> xb+yc`, is a free resolution of k. Its exactness follows directly from coprimality of x and y in the polynomial ring. Tensoring it by M shows that Tor_i(k,M)=0 for i>2 and

`Tor_2^A(k,M) = {z in M : xz=yz=0}`

up to the internal Koszul shift. This last space is zero because M is torsion-free and x is nonzero. Thus F_i=0 for i>=2. We have a minimal exact sequence

`0 -> F_1 -> F_0 -> M -> 0`.                                             (TM1)

Let f_i be the rank of F_i. Localization at K gives r=f_0-f_1. Tensoring TM1 by the right module V gives the exact vector-space sequence

`0 -> Tor_1^A(V,M) -> V tensor F_1 -> V tensor F_0 -> V tensor M -> 0`.

Since internal shifts do not change vector-space dimension,

`dim(V tensor M)=r dim V + dim Tor_1^A(V,M)`.                            (TM2)

If M is not graded free, F_1 is nonzero. The right socle

`soc(V)={v in V : vx=vy=0}`

is nonzero: any nonzero homogeneous vector of maximal degree lies in it. All entries of the minimal differential F_1->F_0 belong to m. Therefore the subspace consisting of one copy of soc(V) for each free generator of F_1 lies in the kernel of `V tensor F_1 -> V tensor F_0`. In particular

`dim Tor_1^A(V,M) >= f_1 dim soc(V) > 0`.                                (TM3)

This proves strict inequality for every nonfree torsion-free M. If F_1=0, M is graded free and equality follows directly. No Auslander--Buchsbaum or general projective-freeness theorem is needed.

### Proof, torsion-bearing case

Let T be the full left torsion submodule of M and put Q=M/T. The torsion submodule is graded. Indeed, if a nonzero polynomial annihilates a sum of homogeneous components of an element, the highest-degree equation shows that its highest component is torsion; subtract it and continue. The quotient Q is torsion-free: if a nonzero a kills a class represented by z, then az is torsion, so baz=0 for some nonzero b, and z is torsion. Both T and Q are finite graded modules, and Q has rank r.

If Q is not graded free, the torsion-free part of the proof gives

`dim(V tensor Q)>r dim V`.

The quotient M->Q induces a surjection `V tensor M -> V tensor Q`, so the same strict lower bound holds for M.

If Q is graded free, the graded surjection M->Q splits as a left-module map by lifting a homogeneous free basis. Thus M is isomorphic, as a graded left module, to Q direct sum T. If T=0, equality holds. If T is nonzero, then `V tensor T` is nonzero. To see this without assuming any flatness, it surjects onto

`(V/Vm) tensor_k (T/mT)`,

and both factors are nonzero by graded Nakayama (or the nilpotence of m on V). Hence

`dim(V tensor M)=r dim V+dim(V tensor T)>r dim V`.

This proves the theorem in every case. The splitting in this proof is only a left-module splitting; no bimodule splitting is asserted. QED.

## 3. Consequence for an actual module quadratic

### Corollary TM-B

Let M be a nonzero finite graded A-bimodule, finite on the left, with homogeneous commuting actions. Let U be a finite graded k-vector space. Suppose

`M tensor_A M is isomorphic to U tensor_k M`                             (TM4)

as left A-modules (an actual bimodule isomorphism is more than enough), and suppose

`dim_k U = rank_A M = r`.

Then M is graded free on the left. In particular no torsion-bearing or other nonfree M satisfies these hypotheses.

### Proof

Set V=k tensor_A M, using the left A-action. It is a nonzero finite graded right origin module. Tensor TM4 on the left with k. Associativity and the left-module isomorphism give

`V tensor_A M is isomorphic to U tensor_k V`.

Its dimension is r dim V. Proposition TM-A forces M to be graded free. QED.

The numerical hypothesis dim U=r must either be imposed or proved from the specified generic action. It is not inferred for an arbitrary bimodule merely by treating its right action as the usual left action. For the actual generic graph bimodules in the Soergel setting, tensor products multiply total graph dimension, so a nonzero generic quadratic supplies r^2=(dim U)r and hence exactly this equality.

A related elementary fact used below is that every nonzero M as in TM-B satisfies

`M tensor_A M != 0`.                                                    (TM5)

Indeed, after left tensoring with k the result is V tensor M. This surjects onto `(V/Vm) tensor_k (M/mM)`, which is nonzero. This assertion uses the positive grading and the common origin; it is not a statement about arbitrary ungraded bimodules with unrelated supports.

## 4. Exact highest-cohomology application

Consider a bounded complex X of finite graded bimodules, free on both sides, in the ordinary rank-one product Soergel setting over A. Let C be a bounded complex of finite graded k-vector spaces with nonzero cohomology (a nonzero derived object), and suppose there is an actual derived bimodule isomorphism

`X tensor_A^L X is isomorphic to C tensor_k X`.                          (TM6)

Assume the usual simultaneous generic graph localization is exact and monoidal and that X has nonzero generic cohomology. These properties hold for the actual ordinary Soergel complexes under discussion. The generic category consists of finite sums of graph bimodules; forgetting their labels, tensor product multiplies dimensions.

Let a be the highest global cohomology degree of X and c the highest cohomology degree of C. Put M=H^a(X). The highest-degree derived tensor identity is

`H^(2a)(X tensor_A^L X)=M tensor_A M`.

For clarity, this is the standard top-truncation identity, not a general Kunneth splitting. One may compute using bounded-above flat resolutions with all terms above the relevant cohomological bound zero; the top cohomology is the tensor product of the two top cokernels. Equivalently, derived tensor is right t-exact and its degree-zero functor on modules is ordinary tensor.

TM5 makes this top group nonzero. The right side of TM6 has highest degree a+c and top group H^c(C) tensor M, which is nonzero over k. Therefore c=a.

Let b be the highest generic cohomology degree of X. Its top generic graph module is nonzero, and its square is nonzero because total graph dimensions multiply. Applying the same highest-degree calculation to the localized relation gives 2b=b+c, hence b=c=a. Thus the global top M has positive generic rank r; it is not a generically invisible torsion module. Localizing its top relation gives

`r^2 = (dim_k H^a(C)) r`.

So dim H^a(C)=r. The actual highest-cohomology relation is

`M tensor_A M is isomorphic to H^a(C) tensor_k M`.

Corollary TM-B applies and proves that H^a(X) is graded free on the left.

When the generic top is supported on the actual two graphs e and tau=(-x,-y), the already fully checked codimension-two graph argument splits this free module into graded e- and tau-graph summands, so it is also free on the right. This last use assumes characteristic different from two and the indicated graph support; neither condition was needed for Proposition TM-A itself.

This is the exact module input for a separate descending-cohomology argument. The present note does not by itself assert that all cohomology is free or that an arbitrary higher-rank ordinary Soergel complex is reduced to this two-variable case.

## 5. Independent checks and separate dictionary

I reconstructed the minimal-resolution argument directly using the explicit two-variable Koszul resolution. I checked the right-module orientation of V, the nonzero socle, the Tor exact sequence and its signs, the rank computation, and both branches of the torsion quotient argument. The last splitting was used only in the category of graded left modules. I separately checked the nonzero-square argument and the equality of global and generic top degrees; it does not assume in advance that the highest global cohomology survives localization.

The note uses actual tensor products, actual cohomology and vector-space dimensions. It does not deduce a module isomorphism from an Euler identity. EGA I Theorem 1.3.7, p. 86, Corollary 1.3.8, p. 87 and Theorem 1.4.1, pp. 90--92 give the affine module/sheaf dictionary. SGA6 I Definition 4.7, pp. 121--122 and Example 4.8, p. 122 give the finite perfect-complex framework. The Tor calculation retains information that passage to K0 discards. The generic graph category and its localization are the already checked ordinary Soergel framework in F59; no nonstandard geometric equivalence is claimed.

The effective grading uses SGA3 I4.7.2--3/cote90 scan17, and actual versus virtual coefficient classes use SGA6 V Sections2--3/cote133 scan18. These are framework locators, not a claim that the archive states this tensor-dimension inequality or supplies the nonstandard canonical basis.

Independent whole-proof review is requested before integration. No master file or shared master log has been edited.

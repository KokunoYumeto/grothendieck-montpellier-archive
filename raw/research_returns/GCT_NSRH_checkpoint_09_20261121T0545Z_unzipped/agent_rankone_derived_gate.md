# Rank-one derived signs, four-point actions, and the limit of localization

Author: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026. These are elementary deductions for this investigation. They use the actual rank-one element and keep the named positive cone, homological grading, formal quantum parameter, and Frobenius specialization distinct.

## 1. Algebra and the specified effective cone

Put

\[
R=\mathbf Z[v,v^{-1}],\qquad \delta=v+v^{-1},\qquad
H=R[c]/(c^2-\delta c).
\]

In `H tensor_R H`, write `c_1=c tensor1`, `c_2=1 tensor c`, and

\[
P=c_1c_2+(c_1-\delta)(c_2-\delta)
=2c_1c_2-\delta(c_1+c_2)+\delta^2.
\tag{DR1}
\]

The named ambient KL basis is `{1,c_1,c_2,c_1c_2}`. Its effective cone consists of linear combinations with coefficients in `N[v,v^{-1}]`.

The quadratic relation gives

\[
P^2=\delta^2P,\qquad
P^k=\delta^{2k-2}P\quad(k\ge1).
\tag{DR2}
\]

For completeness, if `a=c_1c_2` and `b=(c_1-delta)(c_2-delta)`, then `a^2=delta^2 a`, `b^2=delta^2 b`, and `ab=0` because `c_i(c_i-delta)=0`. This proves DR2 directly.

For every `k>=1`, DR2 has positive nonzero coefficients at `1,c_1c_2` and negative nonzero coefficients at `c_1,c_2`:

\[
P^k=\delta^{2k}\cdot1
-\delta^{2k-1}(c_1+c_2)
+2\delta^{2k-2}c_1c_2.
\tag{DR3}
\]

No cancellation between these four distinct basis vectors is possible.

## 2. Bounded complexes exist, but the specified cone prevents one-parity representatives

**Proposition DR-A.** Let `C` be an additive graded monoidal category with biadditive tensor product compatible with internal grading shifts, whose split Grothendieck ring is the displayed based algebra, with actual objects having nonnegative Laurent coefficients in the named four-element basis. Let internal grading shift `(1)` act by `v`; it is distinct from homological shift `[1]`. The tensor unit represents `1`. Then:

1. There is an explicit bounded two-term complex with Euler class `P`.
2. No bounded complex with Euler class `P^k`, for any `k>=1`, can have all its nonzero terms in a single homological parity. The same is true after multiplying its Euler class by an overall sign or a Laurent monomial.
3. The explicit zero-differential complex below has tensor-power homotopy amplitude exactly `k`.

**Proof.** Choose objects `B_0,B_1,B_2,B_3` for `1,c_1,c_2,c_1c_2`, with `B_0` the tensor unit. Form

\[
X_+=B_3^{\oplus2}\oplus B_0(2)\oplus B_0^{\oplus2}\oplus B_0(-2),
\]

\[
X_-=B_1(1)\oplus B_1(-1)\oplus B_2(1)\oplus B_2(-1).
\]

Let `K^0=X_+`, `K^1=X_-`, all other terms zero, and differential zero. Then its Euler class is DR1. Thus passing to bounded complexes genuinely realizes the virtual expression.

If a complex has all terms in even degrees, its Euler class lies in the effective cone. If all its terms lie in odd degrees, its Euler class is the negative of an effective class. DR3 is in neither cone. Multiplication by an overall sign interchanges the two mixed sign patterns, and multiplying by a grading monomial does not change coefficient signs. This proves the second assertion. Homotopy equivalent complexes have the same Euler class, so it also rules out a homotopy equivalent one-parity representative.

The tensor complex `K^{tensor k}` has zero differential and terms in degrees `0,...,k`. Every such term is nonzero: one may choose unit summands from `X_+` and a `B_1` summand from each chosen `X_-`; their product has nonzero effective class by `c_1^j=delta^{j-1}c_1` for `j>=1`. In particular both extreme terms are nonzero. A homotopy equivalence from a zero-differential complex `C` to a complex `D` gives composites equal to the identity on `C` degreewise, since a chain homotopy on `C` contributes `d_Ch+hd_C=0`. Therefore `D` cannot have a zero term in a degree where `C` has a nonzero term. No homotopy equivalent representative can shorten the interval `[0,k]`. This proves the third assertion. ∎

**Scope.** The amplitude claim in part3 concerns this explicitly constructed complex. It is not a lower bound of `k` for every possible complex representing the same Euler class. The basis-relative one-parity obstruction in part2 does apply to every such complex. In an additive category one must not replace “terms” by “cohomology” without supplying an abelian or t-structure setting.

### A concrete category where the construction applies

The ordinary Hecke category supplies such a category. For rank one take `A=Q[x]`, `deg x=2`, the reflection `s(x)=-x`, and `B=A tensor_{A^s} A(1)`. Here `A^s=Q[x^2]`. The free `A^s`-decomposition of `A` gives directly

\[
B\otimes_A B\simeq B(1)\oplus B(-1).
\]

Use independent variables for the product of two rank-one systems. The indecomposable classes are exactly the named KL basis and its internal shifts. A checked primary anchor for the general category and its split Grothendieck ring is Elias–Williamson, *The Hodge theory of Soergel bimodules*, Annals of Mathematics180 (2014),1089–1136: §3.5 and Theorem3.5, pp1107–1108; Theorem1.1, p1093, identifies indecomposable characters with the KL basis. The original publisher PDF was read at <https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n3-p06-p.pdf>, refs `turn498058805view0`–`turn498058805view3`.

This construction uses the bounded **homotopy** category of an additive Hecke category. It does not assume that Hecke convolution is t-exact on an abelian perverse heart. In Grothendieck’s scheme language, the rank-one bimodule arises from the finite-flat correspondence `Spec A times_{Spec A^s} Spec A`; the new assertions are the displayed Euler and homotopy calculations, not manuscript theorems.

## 3. What exact tensor realizations can and cannot do to amplitude

**Lemma DR-B.** Let `K` be a nonzero bounded complex of finite-dimensional Weil representations, or more generally of an abelian tensor category with a faithful exact tensor functor to finite-dimensional vector spaces. Let

\[
p=\min\{i:H^i(K)\ne0\},\qquad
r=\max\{i:H^i(K)\ne0\}.
\]

Then `K^{tensor k}` has extreme nonzero cohomology degrees `kp,kr`, so its amplitude is `k(r-p)`. If the cohomology of `K` occurs in both parities, the same is true of every tensor power.

**Proof.** Over a field the Künneth decomposition gives

\[
H^j(K^{\otimes k})\simeq
\bigoplus_{i_1+\cdots+i_k=j}
H^{i_1}(K)\otimes\cdots\otimes H^{i_k}(K).
\]

This identity can be proved by splitting each underlying bounded vector-space complex into its cohomology with zero differential and contractible two-term summands. Tensoring a contractible complex remains contractible. The extreme terms are the nonzero tensor powers of `H^p` and `H^r`. If `H^i,H^j` are nonzero with opposite parities, the degrees `ki` and `(k-1)i+j` supply nonzero summands of opposite parity. A faithful exact tensor functor detects these nonvanishings and gives the same conclusion in the stated generality. ∎

A global shift and a Tate twist do not reduce this amplitude. Finite extension of the base field changes Frobenius eigenvalues but leaves cohomological degrees unchanged. Thus a proposed faithful exact tensor realization with mixed cohomological parity cannot get one-degree or one-parity concentration merely by tensoring repeatedly. This lemma has the explicitly stated exactness hypotheses; it is not automatically a statement about an arbitrary geometric pushforward or Hecke convolution.

### Even tensors cannot manufacture the required opposite sign by themselves

Let a bounded finite Weil complex have nonempty visible Euler spectrum `F=sum c_alpha[alpha]`, with real coefficients (integer Euler coefficients suffice). For every even `k`, the grouped spectrum of its tensor power has at least one strictly positive coefficient at its largest modulus. This is precisely the augmentation-and-Vandermonde lemma checked in F24. A Tate twist changes the roots, not those coefficients. Consequently an unshifted even tensor power, even with a Tate twist, cannot itself have a wholly negative nonempty visible spectrum.

Shifting the **input** by `[r]` does not help: the sign of its even tensor power changes by `(-1)^{kr}=1`. An additional odd shift of the **output** can reverse a sign formally, but identifying that shifted object with the actual path-hypersurface cohomology is a separate geometric comparison. Declaring the shift does not prove the required path-count identity.

This is the precise obstruction relevant to F24: a signed derived input is allowed, but the negative visible spectrum on the path output is not supplied by even tensor powers alone. Mixed parity by itself does not disprove that a genuine geometric path output could have the needed negative visible spectrum after its own cancellations.

## 4. A four-point positive model preserving the actual rank-one character actions

**Proposition DR-C.** There is a faithful algebra map

\[
\Phi:H\longrightarrow R^2,\qquad
\Phi(a+bc)=(a+b\delta,a).
\]

Its image is `{(x,y):x-y in delta R}`, and it becomes an isomorphism after inverting `delta`. The tensor-square map embeds `H tensor_R H` in `R^4`; on the four labels `++,+-,-+,--`, the actual element `P` has coordinates

\[
\Phi^{\otimes2}(P)=(\delta^2,0,0,\delta^2).
\tag{DR4}
\]

Thus it acts on **both** equal-sign character pieces, including the sign-tensor-sign piece at `v=1`.

**Proof.** The two coordinates evaluate `c` at its two roots `delta,0`. If `Phi(a+bc)=0`, then `a=0` and `b delta=0`; since `R` is a domain, `b=0`. The image condition and the inverse after localization follow by solving `b=(x-y)/delta`. The analogous four-coordinate evaluation is injective: in the basis `1,c_1,c_2,c_1c_2`, first the `--` coordinate kills the constant term, then `+-` and `-+` kill the two linear terms, and finally `++` kills the quadratic term. Evaluating DR1 gives DR4.

Equivalently, after localization put `e_i=c_i/delta`. Then

\[
P=\delta^2\bigl(e_1e_2+(1-e_1)(1-e_2)\bigr).
\]

At `v=1`, `c_i=1+s_i` and `delta=2`, so this is exactly the spectrum of `2(1+s_1s_2)`: eigenvalue4 on equal signs and0 on opposite signs. It corrects the action mismatch of the single term `c_1c_2`, which misses the `--` piece. ∎

This is also a coherent scheme model: the inclusion `H subset R^2` separates the two branches of `Spec H`, and `R^2` is its normalization. Indeed `R^2` is generated by an idempotent integral over `H`, is finite over `R`, and is integrally closed in `Frac(R)^2`; conversely an element integral over `H` is integral over `R` and hence has both coordinates in the normal domain `R`. The same argument gives normalization `R^4` for the tensor-square algebra. Over `delta!=0` the finite branch separation is already an isomorphism.

For any module of the original tensor-square algebra over `R[delta^{-1}]`, the four orthogonal character idempotents decompose it into its actual four character pieces. The disjoint union of four copies of the localized base, with those pieces as its quasi-coherent sheaf, therefore preserves the specified action. For finite projective modules these pieces are vector bundles; at a field specialization, finite-dimensional modules give vector spaces on four points. This is a basis change/localization statement, not a claim that those character idempotents belong to the original integral KL cone.

### An integer-Tate formulation, with no half twist

To interpret DR4 by actual Tate objects, set `u=v^2` and `b=vc`. Work first over `R_even=Z[u,u^{-1}]` with

\[
H_{\mathrm{even}}=R_{\mathrm{even}}[b]/(b^2-(1+u)b).
\]

Extension of scalars to `R` recovers `H`. The actual element belongs to the even form:

\[
P=u^{-1}\bigl[b_1b_2+(b_1-(1+u))(b_2-(1+u))\bigr].
\]

Let `L=Q_l(-1)` or the corresponding rational Tate motive. On the four rational points, the classes of `b_1,b_2` can be represented by `1 plus L` on the points whose first, respectively second, sign is `+`, and by0 elsewhere. The element `P` is represented by the actual object

\[
T=\mathbf1(1)\oplus\mathbf1^{\oplus2}\oplus\mathbf1(-1)
\]

on each of the two diagonal points and by0 on the other two. Its class is `u^{-1}+2+u`, and

\[
\operatorname{Tr}(F^n\mid T)=q^{-n}+2+q^n
=(q^{n/2}+q^{-n/2})^2.
\]

This is an actual positive Tate class and an exact action model on the character Grothendieck group. The total object has weights `-2,0,0,2`; it is **not** a pure weight-zero Weil module. Tensoring with `T` is a functor, whereas multiplication by the numerical scalar `(q^{1/2}+q^{-1/2})^2` at one fixed parameter is a different endomorphism construction. No assertion identifies those two across all extension degrees without specifying the trace comparison.

The full four-point Grothendieck ring has the character basis. The original KL basis maps into it but is not an integral basis of it: the map is an isomorphism only after inverting `1+u` (equivalently `delta` after adjoining `v`). Thus this construction changes the effective cone explicitly. It does not contradict DR-A or the inherited-KL-cone obstruction.

## 5. Algebraic localization is not automatically a finite Weil object

**Lemma DR-D.** For real `q>1`, the sequence

\[
a_n=\frac1{1+q^n}\quad(n\ge1)
\]

is not a finite exponential polynomial `sum_j a_j alpha_j^n` with fixed complex coefficients and nonzero roots. In particular it is not the alternating Frobenius trace of a bounded complex of finite-dimensional Weil representations.

**Proof.** Near `z=0`, absolute convergence gives

\[
\sum_{n\ge1}\frac{z^n}{1+q^n}
=\sum_{m\ge1}(-1)^{m-1}\frac{z}{q^m-z}.
\]

The series on the right converges normally on each compact set away from `{q,q^2,...}`: its tail is bounded by a constant times `sum q^{-m}`. It therefore extends meromorphically to the plane and has a nonzero simple pole at every `z=q^m`. Only its `m`th term has a pole there. A finite exponential polynomial has generating function `sum_j a_j alpha_j z/(1-alpha_j z)`, a rational function with only finitely many poles. The two germs cannot be equal. ∎

This gives a precise limit to the formal localization above. It does **not** prohibit using the scalar `(1+q)^{-1}` in a coefficient field at a single fixed `q`. It prohibits identifying the extension-by-extension values `(1+q^n)^{-1}` with the Frobenius traces of one fixed finite complex. It also does not forbid a particular normalized idempotent from having a finite model when its denominator cancels in the new character coordinates: for example `b/(1+u)` maps to the actual one-point projector `(1,0)`. What fails is a tensor realization of the whole scalar localization by finite Weil objects with the asserted all-extension trace rule.

For actual finite objects there is an even simpler obstruction to inverting `1 plus L` as a tensor object: its dimension is2, so a finite virtual tensor inverse would require an integer Euler dimension equal to one half. DR-D remains valid even when arbitrary complex coefficients in a finite virtual trace sum are allowed.

The parent’s higher-rank F26 gives a more targeted fixed-word obstruction when a noncanceling rational denominator remains in a normalized action trace. DR-D is its elementary localization counterpart, not a claim about stacks, completed categories, infinite complexes, or every possible realization.

## 6. Consequences for the main gate

There is a genuine bounded Hecke-complex realization of the actual virtual element. With the named ambient effective basis it cannot acquire a one-parity representative by taking powers, and the explicit zero-differential lift has growing amplitude. Exact finite Weil tensor realizations satisfy a separate rigorous amplitude law. These facts identify a failure of the simple tensor-only sign mechanism; they do not rule out an independently constructed geometric path output with the negative visible spectrum required by F24.

Changing to the four character points supplies a positive Tate class with the correct actual rank-one actions, resolving the particular mismatch of the single-term model. The changed cone and the localization are explicit. It supplies neither a comparison with VIII’s canonical basis nor the path-hypersurface identity, and its total Tate object is mixed in weight. Full algebraic localization cannot be silently read as a finite Weil realization with coefficients re-evaluated at every extension degree.

Framework anchors are split/triangulated Grothendieck groups, coherent bimodules from finite-flat correspondences, finite normalization of affine schemes, and actual Tate objects. The inspected Grothendieck archival module/projector leaves provide vocabulary anchors only; none of DR-A–DR-D is attributed to those manuscripts. All new elementary proofs are included above.

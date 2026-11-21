# F60 — bounded complex kernels, finite-algebra characters, and a rank-one relation

Author: `/root`, GPT-6 Astra Pro; effort setting not exposed. Date: 2026-11-21 UTC. This is a complete new proof. It distinguishes ordinary relation isomorphisms from relations holding only in the Euler Grothendieck group. No formal verification is claimed.

## 1. The finite-algebra constant-character lemma

Let F be a characteristic-zero field and A a finite-dimensional unital F-algebra. No semisimplicity is assumed. Let z be an indeterminate and suppose

\[
\rho:A\longrightarrow M_m(F[z,z^{-1}])
\tag{K1}
\]

is a unital algebra representation. Then for every a in A,

\[
\operatorname{Tr}\rho(a)(z)
=\operatorname{Tr}\rho(a)(-1).
\tag{K2}
\]

Thus every character value is independent of z, including for modules with nontrivial Jordan blocks or for a nonsemisimple algebra.

### Proof

Finite dimensionality gives a nonzero polynomial p_a(T) in F[T] with p_a(a)=0: the elements 1,a,... are linearly dependent over F. Choose a finite constant field extension E/F splitting p_a. The matrix rho(a) over E(z) is annihilated by p_a. Every eigenvalue over an algebraic closure of E(z) is therefore one of the finitely many roots alpha_1,...,alpha_s of p_a in E. Its trace is the sum of these constants with nonnegative integer algebraic multiplicities, so it belongs to E. Jordan blocks do not alter the trace.

On the other hand the trace belongs to F[z,z^-1]. A Laurent polynomial over F equal to a constant in E has all its nonconstant coefficients zero, by linear independence of the powers of the indeterminate z over E. Its constant coefficient lies in F. Thus it is constant in F, and evaluating at z=-1 proves (K2). No assumption on the multiplicities of the roots of p_a is used. ∎

For later interpretation, if A admits a finite splitting extension E with A_E a product of full matrix algebras, the generic representation over E(z) has the same simple multiplicities as the specialization at z=-1. Here is the additional elementary proof. For each central matrix-factor unit e_r, rho(e_r) is idempotent; its trace is the integer rank n_r both generically and at z=-1. In a representation of M_(d_r)(L), the matrix units e_i1 and e_1i identify the d_r diagonal image spaces, and the module is n_r/d_r copies of the defining module. These integers therefore agree at both parameters. This extra semisimple observation is not needed for constant traces.

## 2. Bounded internally graded matrix kernels

Let V be the category of finite-dimensional Z-graded vector spaces over a characteristic-zero field k. Work with bounded complexes in V whose differentials have internal degree zero. For such a complex C, define its cohomology character

\[
h_C(v,z)=\sum_{e,j}\dim_k H^j(C)_e\,v^e z^j
\in\mathbb N[v,v^{-1},z,z^{-1}].
\tag{K3}
\]

Every sum is finite. Its Euler character is h_C(v,-1), whereas h_C(v,1) is the character of total cohomology with the cohomological degree forgotten.

For completeness, bounded complexes of finite graded vector spaces split as their graded cohomology plus contractible pairs: choose graded complements to boundaries inside cycles and to cycles inside each term. Tensoring a contractible pair remains contractible by its contracting homotopy. This proves the finite Kunneth formula used below without a geometric comparison.

For matrices of complexes indexed by m states use convolution

\[
(K\star L)_{ab}=\bigoplus_c K_{ac}\otimes_k L_{cb}.
\tag{K4}
\]

The cohomology matrices h_K multiply under this convolution. Indeed over a field the Kunneth isomorphism identifies each H^n of a tensor product with the direct sum of H^i tensor H^{n-i}; internal degrees add as well. Finite direct sums add characters. Thus

\[
h_{K\star L}(v,z)=h_K(v,z)h_L(v,z).
\tag{K5}
\]

Isomorphisms in the bounded derived category, and in particular homotopy isomorphisms, preserve these matrices. A finite graded coefficient object in cohomological degree zero has character in N[v,v^-1], independent of z.

## 3. The exact hypothesis on the relations

Let A be generated over F=Q(v) by g_1,...,g_r. Suppose bounded matrix kernels K_i are proposed as their lifts. We impose two explicit conditions:

1. The cohomology matrices, not just their Euler specializations, define a representation

\[
\widetilde\rho:A\longrightarrow M_m(F[z,z^{-1}]),
\qquad g_i\longmapsto h_{K_i}(v,z).
\tag{K6}
\]

2. At z=-1 this is the specified actual A-module M.

Condition (K6) follows if every required actual algebra relation lifts as an ordinary isomorphism between sums of word kernels with scalar Laurent-grading coefficients represented in cohomological degree zero. To make this precise, clear rational-function denominators in an algebra relation, expand its Laurent-polynomial coefficients, and move terms with negative coefficients to the other side. Finite positive scalar multiplicities and internal shifts then give the two sums. An ordinary isomorphism of those sums implies equality of their full cohomology characters by (K5), and therefore the original relation in F[z,z^-1]. The statement only needs enough such relations to force factorization through A.

This is stronger than asking for a relation in the triangulated Euler group. A distinguished triangle gives an Euler equality, but ordinarily does not give equality of full cohomology characters. Likewise a coefficient object with nonzero cohomological degrees can change the scalar coefficients before z=-1. Neither alternative is included in (K6).

## 4. Consequence for every word and the actual rank-four obstruction

Assume finite dimensionality of A as in section1. By (K2), for every word w in the named generators,

\[
\operatorname{Tr}h_{K_w}(v,z)
=\operatorname{Tr}_M(g_w).
\tag{K7}
\]

The left side belongs to N[v±1,z±1]. Evaluating at z=1 therefore proves

\[
\operatorname{Tr}_M(g_w)\in\mathbb N[v,v^{-1}].
\tag{K8}
\]

In fact the character is independent of z, so every nonzero cohomological-degree coefficient of this closed-word trace object is zero. Total cohomology also gives a nonnegative Laurent matrix representation of A. When A is semisimple and admits the indicated splitting extension, its module after that extension is isomorphic to the original Euler module by the optional multiplicity argument in section1. Without semisimplicity only the character conclusion is asserted. Thus bounded complexes do not repair a negative word trace under the exact relation hypothesis (K6).

Apply this to the actual finite-dimensional generic nonstandard Hecke algebra A=Q(v) check H_4. IV, section11.8, printed p67, gives dimension114 and lists its actual rank-four modules. Proposition11.8, printed p61, additionally supplies semisimplicity and a finite splitting extension for the optional same-module conclusion above. These precise source statements and their supplied contexts were read in this run. The trace obstruction needs only finite dimensionality. F57 identifies the extra five-dimensional N# and computes

\[
\operatorname{Tr}_{N^\#}
(P_2P_3P_2P_3P_2P_3P_1P_2P_1P_2P_1)
=p((v+v^{-1})^2),
\]

with coefficients -1 at v^18 and v^-18. This contradicts (K8).

**Finding F60.** There is no bounded internally graded five-state matrix-kernel lift whose Euler action is the actual N# module, whose named kernels lift the P_i, and whose full cohomology-character action factors through the actual generic check H_4 with its scalar parameter unchanged. In particular an ordinary-isomorphism lift of all actual relations with cohomologically degree-zero scalar grading objects is impossible. This conclusion is independent of any purity or arithmetic-weight hypothesis.

The theorem concerns the full actual algebra relations. IV section11.8, p67, explicitly says that the quadratic and adjacent nonstandard braid relations do not generate the full rank-four relation ideal. Checking only those smaller-rank relations is therefore insufficient to invoke F60.

The result is conditional on the stated comparison, not a claim that every triangulated categorification has (K6). It leaves relation triangles, cohomologically nontrivial coefficient objects, geometric convolution without this matrix-cohomology character functor, unbounded constructions, and larger modules without an effective specified-summand comparison outside the theorem. The ordinary Soergel route of F59 is not silently identified with a finite-state graded-vector-space kernel category.

## 5. One explicit rank-one module relation is already impossible as an isomorphism

The F57 word matrix W on N# has rank one. Indeed the original Q-word contains Q_1 Q_3=u e_2^t, so it has rank at most one; its nonzero trace p(v) makes its rank exactly one. Transposition and reversal preserve this. Any rank-one matrix W=a b^t satisfies

\[
W^2=a(b^ta)b^t=\operatorname{Tr}(W)W,
\]

so the actual module relation is W^2=p(v)W. This is a relation on the specified module; it is not asserted to hold in the entire nonstandard algebra.

Write the explicit F57 Laurent polynomial as p(v)=p_+(v)-p_-(v), with

\[
p_-(v)=v^{18}+v^{-18},
\]

and p_+ the remaining positive Laurent terms, including its constant668. Let E_+ and E_- be finite internally graded vector spaces in cohomological degree zero with those characters. A proposed lift K_W of this word cannot satisfy the ordinary isomorphism

\[
K_W\star K_W\ \oplus\ (E_-\otimes K_W)
\simeq E_+\otimes K_W
\tag{K9}
\]

while its Euler word trace is p(v).

**Proof.** Let C(v,z)=h_(K_W)(v,z). Equations(K3)–(K5) and (K9) give C²=p(v)C. Evaluate internal and cohomological variables at v=3,z=1. The resulting finite matrix M has entrywise nonnegative real entries, whereas F57 gives

\[
p(3)=-99834597608550400/387420489<0.
\]

Thus M²=p(3)M is impossible unless every entry of M is zero: each left entry is nonnegative and each right entry is nonpositive, strictly negative when the corresponding entry of M is positive. A finite Laurent polynomial with nonnegative coefficients vanishes at (3,1) only when all its coefficients are zero. Hence all cohomology entries of K_W vanish. Its Euler trace is zero, contradicting the nonzero polynomial p(v). ∎

This concrete test does not require the full rank-four relation ideal, semisimplicity, or purity. It requires the displayed actual module relation as an ordinary isomorphism with degree-zero coefficient objects. A triangle realizing only its Euler equality, or a cohomologically nontrivial coefficient lift, is a different hypothesis. The test does not assert that an arbitrary algebra action automatically lifts every annihilator relation of its Euler module as an isomorphism.

## 6. Separate Grothendieck-framework translation

The internally graded coefficient category is the category of finite representations of a split torus. The additional variable z records cohomology degree as bookkeeping; it is not a new arithmetic Frobenius parameter. Equation(K3) records actual effective cohomology, while z=-1 is the Euler-class operation. The representation/coaction language is SGA3, I,4.7.2–3, with the audited archive anchor cote90, scan17. SGA6, V,sections2–3 and cote133, scan18 supply the coefficient representation and lambda/sigma vocabulary. There is no lambda-ring assertion on the noncommutative algebra A.

The bounded complexes are perfect coefficient complexes, in the framework of SGA6, I,Definition4.7, pp121–122, and Example4.8, p122. These locators concern the underlying complexes; they do not assert the new character-rigidity lemma. Kunneth over a field is proved in the finite form used above, and no geometric pushforward is being treated as an ordinary matrix product without a comparison.

After passage to a splitting field, Spec E[z,z^-1] carries the finite free module E[z,z^-1]^m with the constant algebra A_E acting. Its central idempotents define direct-summand subbundles. Their ranks are constant, as the explicit idempotent-trace proof shows, and these ranks determine the semisimple character. This is the affine module/sheaf dictionary of EGAI,Theorem1.3.7,p86,Corollary1.3.8,p87,and Theorem1.4.1,pp90–92. No archival leaf is claimed to contain this particular family or obstruction.

For the more general trace proof, an element of the constant finite algebra obeys a polynomial with coefficients in the constant field. Its trace in the free family must be a sum of the fixed polynomial roots, which gives the same conclusion without a semisimplicity assumption. The one-word test uses the effective total-cohomology cone at a positive character evaluation and the actual rank-one module identity.

The finding distinguishes full cohomology data from their Euler image and exact relation isomorphisms from triangle-only identities. It removes one bounded-complex repair of the F57 finite-kernel route, without assigning the source's canonical basis to the resulting category or refuting the signed/factored conjectures.

## 7. Verification status

The author reconstructed every displayed argument and read IV's Proposition11.8 on printed p61 and the rank-four relation warning on p67 from the supplied TeX and primary PDF text. No numerical experiment is used in this proof. The negative trace is the already fully checked F57 calculation. A fresh whole-proof review has been requested from /root/rectangular_and_theta; its result must be recorded separately before final publication.

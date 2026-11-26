# The Dirichlet critical line for smooth proper Borger Λ-schemes

**Corollary of Borger and Dirichlet GRH.** Let \(X\) be smooth and proper over \(\mathbb Z[1/M]\), with \(M\geq1\), and give \(X\) a Λ-structure in Borger’s sense. Fix a prime \(\ell\). The odd rational étale cohomology of \(X_{\overline{\mathbb Q}}\) vanishes. In degree \(2m\) there are finite-order Dirichlet characters \(\chi_j\), counted with multiplicity, such that away from the finite set \(S\) of primes dividing \(M\ell\) or the character conductors,

\[
 L^S(H^{2m}_{\rm et}(X_{\overline{\mathbb Q}},\mathbb Q_\ell),s)
 =\prod_j L^S(s-m,\chi_j).
\]

Consequently every zero in the open strip \(m<\Re s<m+1\) lies on the line \(\Re s=m+\tfrac12\). For this entire class of smooth proper Λ-schemes, the assertion about these open strips is **equivalent to Dirichlet GRH**. The shifts refer to cohomological \(L\)-functions with local factors formed using geometric Frobenius. This is a deduction from the cited results. [Borger, Theorem 0.1, Corollary 6.2 and Remark 6.8](https://arxiv.org/pdf/0906.3146v1) · [Dirichlet theorem and checked statements](https://math.mit.edu/~drew/grh/)

### The representation

The original workshop had already obtained the equivalence for the cyclotomic tower from finite étale Λ-rings and the factorization of cyclotomic Dedekind zeta functions. Its source is the 22 November first pass in `reports_20261120/split_zero/ALPOGE_THROUGH_CONNES_CONSANI_20261122.md`, §1, items 3–4. The higher-dimensional cohomological statement above uses Borger’s compactly supported cohomology theorem, including its Hodge multiplicities. It extends that local account to every degree of a smooth proper Λ-model. Neither observation is a priority claim.

Borger’s Theorem 0.1(c) gives \(h^{a,b}=0\) for \(a\ne b\). Smooth proper Hodge theory imposes \(a+b=n\) in degree \(n\), so odd cohomology vanishes and \(H^{2m}\) has only Hodge type \((m,m)\). Borger’s Corollary 6.2 identifies the restriction of \(H^n_{\rm et}\) to the absolute Galois group of a cyclotomic field \(K=\mathbb Q(\zeta_N)\) as the direct sum of \(\mathbb Q_\ell(-a)\) with multiplicities \(h^{a,a}\) in degree \(n\). In degree \(2m\), \(H^{2m}(m)\) therefore becomes trivial over \(K\). The full action on this twist factors through the finite abelian group \(\operatorname{Gal}(K/\mathbb Q)\). After extending coefficients, decomposition into one-dimensional characters follows from the ordinary character theory of finite abelian groups. [Borger, pp. 3 and 20](https://arxiv.org/pdf/0906.3146v1)

At a good prime \(p\ne\ell\), geometric Frobenius acts on \(\mathbb Q_\ell(-m)\) by \(p^m\). On each finite-order character line choose the inverse of its arithmetic-Frobenius character as \(\chi_j\). Its local inverse characteristic polynomial is then \((1-\chi_j(p)p^{m-s})^{-1}\). This gives the product formula. Reinstating or omitting a finite unramified Dirichlet Euler factor can add zeros only on \(\Re(s-m)=0\), since its nonzero value \(\chi_j(p)\) is a root of unity. Ramified primitive Euler factors are 1. The principal pole is at \(s=m+1\). The open strip thus inherits the asserted zero locations.

### Converse and example

For every \(N\geq1\), take \(X_N=\operatorname{Spec}\mathbb Z[\zeta_N,1/N]\), finite étale and proper over \(\mathbb Z[1/N]\). Borger’s Remark 6.8 gives a Λ-structure with the usual commuting cyclotomic Frobenius lifts for \(p\nmid N\) and identity maps for \(p\mid N\). On \(H^0\), the action is the regular representation of \((\mathbb Z/N\mathbb Z)^\times\). Its \(L\)-function over the good primes is the product of all Dirichlet \(L\)-functions modulo \(N\), up to the indicated finite Euler factors. Every factor is holomorphic in \(0<\Re s<1\). Hence an off-line zero of any primitive Dirichlet factor would be an off-line zero of this product. Taking all \(N\) gives the converse. For \(N=3\), the product at primes away from 3 is \(\zeta(s)(1-3^{-s})L(s,\chi_{-3})\). The two factors reflect the two one-dimensional summands of the regular representation. [Borger, Remark 6.8](https://arxiv.org/pdf/0906.3146v1#page=22)

### Where the first nonabelian example falls

Let \(E\) be the splitting field of \(X^3-2\) over \(\mathbb Q\). Eisenstein at 2 makes the cubic irreducible, and its discriminant \(-108\) is nonsquare, so \(\operatorname{Gal}(E/\mathbb Q)=S_3\). The two-dimensional standard representation \(\rho\) has traces \(2,0,-1\) on identity, transpositions and three-cycles. It cannot occur as a subquotient of a representation assembled from the Λ-cohomologies above by direct sums, tensor products, duals and subquotients. Each member of that class kills the commutator of the absolute Galois group; the image in \(S_3\) of that commutator is \(A_3\), and \(\rho\) is nontrivial there. Tate twisting preserves the obstruction.

The arithmetic distinction appears already at good primes congruent to 1 modulo 3. In \(\mathbb F_7^\times\), \(2^2=4\ne1\), so \(2\) is a noncube and the Frobenius is a three-cycle. In \(\mathbb F_{31}^\times\), \(2^{10}=1\), so \(2\) is a cube and the polynomial splits completely. For any prescribed modulus \(C\), the same distinction persists among some primes congruent to 1 modulo \(C\). Indeed, \(E\cap\mathbb Q(\zeta_C)\) is abelian over \(\mathbb Q\); a three-cycle acts trivially on it, just as the identity does. Each of these two automorphisms can therefore be paired with the identity of \(\mathbb Q(\zeta_C)\) in the compositum. Chebotarev gives positive-density conjugacy classes of primes with each prescribed behavior. The worked example exhibits what a finite collection of tests by residue class loses.

| Frobenius in \(S_3\) | Action on the quadratic subfield | Trace on the standard summand | Characteristic factor \(\det(1-T\rho(g))\) |
|---|---|---:|---|
| Identity | Trivial | 2 | \((1-T)^2\) |
| Transposition | Nontrivial | 0 | \(1-T^2\) |
| Three-cycle | Trivial | −1 | \(1+T+T^2\) |

The result concerns ordinary rational étale cohomology of Borger Λ-models. The common-kernel argument applies to the listed operations. An equivariant realization using a different action, a coefficient local system with nonabelian monodromy, or induction from a proper subgroup can bring new Galois data. The theorem gives no zero away from the critical line for the standard Artin factor.

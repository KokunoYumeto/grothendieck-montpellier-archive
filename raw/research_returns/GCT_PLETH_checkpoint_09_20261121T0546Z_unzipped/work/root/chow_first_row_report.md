# An explicit canonical-map lift for every sufficiently long first row

## G-014. Degree-tracked multisymmetric lifting

Let \(a\ge2\), \(n\ge0\), and let \(V\) be a finite-dimensional characteristic-zero vector space. For every partition \(\lambda\vdash an\) with
\[
 d:=an-\lambda_1=\lambda_2+\lambda_3+\cdots\le n,
\tag{C.1}
\]
the canonical map
\[
 h_{n,a}:\operatorname{Sym}^n(\operatorname{Sym}^a V)
 \longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^n V)
\tag{C.2}
\]
is surjective on the entire target \(\lambda\)-isotypic component. For the empty partition we put \(\lambda_1=0\); the zero-dimensional ambient space is immediate. The proof gives a rational preimage for every target highest-weight vector by explicit coefficient extraction, Newton identities, and a finite sum over set partitions. Consequently the image multiplicity equals \(a_{a,n}^{\lambda}\) throughout (C.1). This includes all ambient dimensions: a Schur module whose partition exceeds the dimension is zero on both sides of this component assertion.

The elementary-multisymmetric coordinate chart is classical: Raicu–Sam–Weyman, *On some modules supported in the Chow variety*, Theorem 2.3, its proof (2.8), and Remark 2.9, printed pp.5–6, give the chart and its characteristic-zero invariant generators. The proof below tracks the ordinary number of generators as well as their polynomial weights, to supply the stated finite-degree lift and the exact canonical map. No priority claim is made for the resulting first-row range.

### 1. The actual coordinate morphism

Choose a basis of \(V\). Write the \(i\)-th linear form as
\[
 \ell_i=x_i t_1+\sum_{j=2}^{r}z_{ij}t_j,\qquad 1\le i\le a,
\]
and put \(u=\prod_i x_i\). On the principal open set \(u\ne0\), define \(w_{ij}=z_{ij}/x_i\). A target vector is a polynomial in the \(a\) ordered forms, homogeneous of degree \(n\) in each and invariant under permuting the forms. Any such polynomial of total degree \(d\) in the variables \(z_{ij}\), \(j\ge2\), has the unique expression
\[
 f=u^n F(w_{ij}),
\tag{C.3}
\]
where \(F\) is an \(S_a\)-invariant polynomial, homogeneous of degree \(d\). Indeed, in every monomial the exponent of \(x_i\) is \(n-\sum_{j\ge2}\deg_{z_{ij}}\); substituting \(z_{ij}=x_iw_{ij}\) gives exactly \(x_i^n\) in each row. Permutation invariance passes to \(F\) because \(u\) is invariant.

For a vector of auxiliary variables \(y=(y_2,\ldots,y_r)\), set \(L_i(y)=\sum_{j\ge2}w_{ij}y_j\) and
\[
 \prod_{i=1}^a(1+sL_i(y))
 =\sum_{j=0}^a E_j(y)s^j,
 \qquad E_j(y)=\sum_{|\beta|=j}E_\beta(w)y^\beta.
\tag{C.4}
\]
Let \(C_\beta\) denote the linear coordinate functional extracting the coefficient of \(t_1^{a-|\beta|}\prod_{j\ge2}t_j^{\beta_j}\) from an arbitrary degree-\(a\) form; let \(C_0\) extract \(t_1^a\). These are actual elements of \((\operatorname{Sym}^aV^*)^*\simeq\operatorname{Sym}^aV\), with the dual symmetric pairing specifying any monomial-basis factorials. Pullback under multiplication of the ordered forms gives
\[
 \mu_a(C_0)=u,
 \qquad \mu_a(C_\beta)=uE_\beta(w).
\tag{C.5}
\]
The homogeneous degree-\(n\) part of this algebra pullback is exactly (C.2), with the conventions of G-003 and R-008.

### 2. An explicit expression with at most \(d\) coefficient factors

We prove that every degree-\(d\) invariant \(F\) is a rational linear combination of monomials
\[
 \prod_{q=1}^k E_{\beta^{(q)}},
 \qquad \sum_q|\beta^{(q)}|=d,
 \qquad k\le d,
\tag{C.6}
\]
where all \(\beta^{(q)}\ne0\). The constant case \(d=0\) has \(k=0\).

For a nonzero exponent vector \(\alpha\), put \(P_\alpha=\sum_iw_i^\alpha\). Every invariant polynomial is a linear combination of monomial orbit sums. For a list of nonzero exponent vectors \(\alpha_1,\ldots,\alpha_k\), the distinct-row sum has the exact identity
\[
 \sum_{i_1,\ldots,i_k\ \mathrm{distinct}}
 \prod_{j=1}^k w_{i_j}^{\alpha_j}
 =\sum_{\pi\in\Pi_k}
 \left(\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!\right)
 \prod_{B\in\pi}P_{\sum_{j\in B}\alpha_j}.
\tag{C.7}
\]
To check it, fix a map from the labels \(1,\ldots,k\) to row indices. Its coefficient on the right is the sum of the displayed factors over partitions refining its equality classes. On an equality class of size \(s\), this is the signed sum of all permutations of \(s\) letters, grouped by their cycles; it is one for \(s=1\) and zero for \(s\ge2\), by pairing a permutation with its product with a fixed transposition. Thus precisely the injective maps survive. Each ordinary orbit sum is the left side divided by the factorials of the multiplicities of repeated exponent vectors. This proves the asserted generation by the \(P_\alpha\), while preserving the total exponent degree.

Now put \(P_j(y)=\sum_iL_i(y)^j\). The formal identity
\[
 \frac{s\,\partial_s\prod_i(1+sL_i)}{\prod_i(1+sL_i)}
 =\sum_{j\ge1}(-1)^{j-1}P_j(y)s^j
\tag{C.8}
\]
gives Newton's recurrence after multiplication by \(\sum_{j=0}^a E_j(y)s^j\) and coefficient comparison. It expresses \(P_j(y)\) as a polynomial in \(E_1(y),\ldots,E_a(y)\), homogeneous of weighted degree \(j\) when \(E_i\) has weight \(i\). Its coefficient of \(y^\alpha\), for \(|\alpha|=j\), is \(\binom{j}{\alpha}P_\alpha\). Dividing by that nonzero integer therefore expresses \(P_\alpha\) in the \(E_\beta\), preserving weighted degree \(|\alpha|\). Every factor has positive weight, so every resulting monomial contains at most \(|\alpha|\) factors. Substitute these expressions in (C.7). The total weight of every term is \(d\), and its number of factors is at most \(d\). This proves (C.6) constructively.

### 3. Homogenization produces a preimage of the required degree

For each term of (C.6), the assumption \(n\ge d\) gives \(n-k\ge0\). Equation (C.5) then gives
\[
 \mu_a\left(C_0^{n-k}\prod_{q=1}^k C_{\beta^{(q)}}\right)
 =u^n\prod_{q=1}^k E_{\beta^{(q)}}.
\tag{C.9}
\]
Apply (C.9) term by term to the explicitly computed expression for \(F\). The resulting source polynomial is homogeneous of coordinate degree \(n\) and maps to \(f\). The equality was derived on \(u\ne0\); both sides are polynomials in the ordered linear forms, and this is a dense principal open of their affine space. Hence they agree everywhere.

Every target highest-weight vector of weight \(\lambda\) has first-coordinate degree \(\lambda_1\), so its total degree in the remaining coordinates is precisely \(d=an-\lambda_1\). Thus (C.3)–(C.9) lift every such vector under (C.1). The canonical map is \(GL(V)\)-equivariant. Its image therefore contains the submodules generated by all target highest-weight vectors of weight \(\lambda\), which together are the full \(\lambda\)-isotypic component. This proves G-014.

The argument gives image multiplicity rather than only a coefficient inequality. A preimage need not initially be highest weight; equivariance and the equality with the specified target vector suffice, and the usual characteristic-zero isotypic projection provides a preimage in the same irreducible block.

### Exact isomorphism on the common first-row range

For \(a,n\ge2\) and \(d\le\min(a,n)\), apply G-014 both to \(h_{n,a}\) and to \(h_{a,n}\). In the common tensor space, normalized row and column symmetrizers are self-adjoint orthogonal projections, and the grid transpose identifies the two maps as adjoints, exactly as in M-001 and G-002. Their ranks are equal. Surjectivity in both directions therefore makes the two component dimensions equal to that common rank. Thus both maps are isomorphisms on their \(\lambda\)-isotypic components in the displayed common range. This follows for the prescribed maps themselves, with their specified tensor identifications.

### Geometric and lambda-ring form

The multiplication map on ordered linear forms is a morphism of affine schemes, and (C.5) is its coordinate pullback. Localization at the coefficient of the pure power \(t_1^a\) produces the displayed multisymmetric chart. Equations (C.7)–(C.9) prove that its denominators clear in coordinate degree \(n\) for every component satisfying (C.1). Thus the Chow coordinate image from G-003 and its normalizing representation algebra have identical \(\lambda\)-isotypic pieces in this range. Applying the coefficient functional \([s_\lambda]\) in \(K_0(\operatorname{Rep}_{\mathbf Q}GL(V))\) gives precisely the rank equality asserted above. All coordinate equations are integral; the rational divisions in (C.7)–(C.8) specify a localization of \(\mathbf Z\) over which each particular preimage spreads out. The general integral symmetric/divided-power map remains the one in G-003, and no integral surjectivity at excluded primes is asserted.

Primary source: Raicu, Sam, Weyman, *On some modules supported in the Chow variety*, Theorem 2.3, equation (2.8), Remark 2.9, pp.5–6; https://par.nsf.gov/servlets/purl/10334188 . These source passages were opened and read in this run. The new degree tracking and the full lifting proof above are checked separately in `CHECK_EVENTS.tsv`.

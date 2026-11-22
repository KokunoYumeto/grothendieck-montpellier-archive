# Root complete proof and primary-source audit: C.3ar and C.3as

Audit completed on 19 November 2026 at approximately 10:41 UTC by GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run. These are new mathematical audits; they are distinct from the reconstruction checks documented separately.

## C.3ar: the restricted product-of-curves top quotient

**PASS, with the stated product-of-curves hypotheses.** We read the complete typed proof and independently checked the finite pro-cdh detecting level, the rational Adams weight and descent bounds, the actual Picard algebraization, the leading symbol, the evaluation spanning argument, and finite cancellation. This is a restricted positive theorem and does not close the unrestricted rational top gate.

The detecting level concerns the actual regular strict-local resolution. It follows from the pro-cdh relative sequence and the vanishing of the relative K0 group of the local base, not from an assertion that all formal K-classes algebraize. At the split finite thickening, the fixed Adams-weight calculation uses Loday's truncated-polynomial calculation and Cortinas--Haesemeyer--Weibel's nilpotent relative Chern character; the vanishing below the relevant weight leaves the single top coherent cohomology term.

For each positive internal degree, the formal exponential specifies an actual line bundle after proper formal existence, Elkik's punctured Picard comparison, and adjustment by the exceptional divisor. The ordinary algebraic-equivalence assertion comes from varying an actual Picard point on a fixed proper curve. All complex coefficients in the spanning calculation are absorbed into the parameter of that actual line bundle; Chow groups are not silently treated as complex vector spaces. Evaluation along a sufficiently high-degree finite map from each curve gives the required span. Cancellation is made at one finite detecting level, so no unjustified infinite sum of Chow classes occurs.

We freshly opened Bloch--Esnault--Kerz, *Deformation of algebraic cycle classes in characteristic zero*, author PDF at https://page.mi.fu-berlin.de/esnault/preprints/helene/112-bek.pdf. Lemma 2.2 and Proposition 2.3 (author pp. 3--4) give the infinitesimal symbol with coefficient one; Proposition 6.1 and its proof (pp. 12--13) identify the comparison composite with dlog. Proposition 6.1 is a pro-isomorphism and is used as such, with compatible higher stages, not as an unsupported fixed-thickening isomorphism. We also freshly opened Cortinas--Haesemeyer--Weibel, https://arxiv.org/pdf/math/0703133, Theorem 6.1 and Corollary 6.2 (author p. 15); the fixed-weight comparison was checked against the prior full Loday/source audit. Independent complete audits from both sibling research branches are retained.

## C.3as: integral top finiteness in every positive characteristic and dimension

**PASS.** We read all seven proof steps in the complete typed draft, including all displayed constructions and the final scope statement. For every algebraically closed field k of characteristic p>0 and every N>=3, the specified excellent normal strictly henselian local k-algebra has regular puncture X and a surjection

    CH^(N-1)(X) / CH^(N-1)(X)_alg --> (k,+).

The equivalence is ordinary algebraic equivalence through actual families on fixed products. The target has exponent p. No rational or characteristic-zero nonvanishing is deduced.

### Geometry independently checked

1. The initial plane curve is smooth, its affine derivative in y is -1, and its unique point at infinity is smooth. We rederived the identity for z-q^(-n), its precise exponent, and div(dz)=n(n-3) infinity.
2. Each cyclic degree is prime to p and larger than p. The explicit E_i recurrence makes every divisor division integral. The Frobenius-exact differential supplies the local primitive and the nonsplit extension with split Frobenius pullback.
3. The lines convention gives positive normal bundle O(D) at infinity. Disjointness gives G~pS_infinity-pg*D, hence the stated cyclic root and normalized algebra. We do not use the conflicting plus sign in the author preprint.
4. The parameter w=x^a T^b satisfies a*ell-p*b=1 and w^ell=x(1-cx^p)^b. The unit derivative in x proves the normalization smooth at infinity. The first-order transition of w gives the actual normal bundle O(D'), not merely its ell-th power. The fibre is integral because gcd(p,ell)=1.
5. We checked the nef intersection argument separately in both possible image dimensions of every subvariety. It proves ampleness by Nakai--Moishezon in all dimensions. The normalized differential has exact order p(ell-1) at infinity and no residual zero, including at intersections with inherited boundary components.
6. The full section ring and contraction do not require degree-one generation. The Veronese properness argument and the two consecutive powers argument give the stated contraction and its complement. Pointed strict henselization preserves the reduced exceptional divisor and each finite infinitesimal neighbourhood.

### Integral invariant and actual curves independently checked

The integral Milnor Bloch formula applies to the regular noetherian resolution containing the infinite field k. The dlog sheaf map is defined without denominators. Tensoring the differentials with O_V retains the conormal dt summand; it is not the differentials pullback that annihilates dt.

We checked the entire exceptional image by the literal identity i_* beta=pi^*(-c1(L) beta), obtained first on the total space and then by flat base change. Consequently the conormal component vanishes on it. No homotopy invariance of the strict-local resolution is assumed.

Ordinary algebraically trivial cycles form a divisible subgroup: each actual curve-family action extends over a proper parameter curve and factors through its Picard variety. Multiplication by p is surjective on its points over an algebraically closed field. Its homomorphism to the exponent-p additive target is therefore zero.

The affine tower chart is etale in the stated d coordinates. The specified transverse curve is smooth at the chosen point. Its closure and finite normalization, followed by selection of the henselian local branch, give an actual closed embedded curve on the fixed resolution meeting V only at that point. We checked the closed non-isomorphism-locus argument, rather than substituting a formal curve or a varying henselized family.

The supported complete-intersection Milnor symbol has multiplicity one. Restriction to V of the dlog class for (s_1,...,s_(d-1),f_d-at), minus the class at a=0, has conormal coefficient plus or minus a. The fixed orientation and Serre trace give exactly a; the Koszul duality normalization is dual to the identity k-->k. There is no factorial, so p<=d and characteristic two are included.

### Primary texts and finite certificate

We freshly opened and read the relevant primary passages:

- Mukai, RIMS1736, https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1736.pdf: Definition 2.1, Lemma 2.2, Proposition 2.3, and Section 2.4, author pp. 7--8 and 11--12. The Frobenius local construction and its sign issue were additionally checked against the retained earlier full source audit.
- Kerz, https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf: Theorems 7.1 and 7.5, author pp. 21--22, including the infinite-residue-field hypothesis.
- Braunling, https://nyjm.albany.edu/j/2013/19-28p.pdf: Sections 3--4, pp. 557--560, especially the product diagram, Proposition 3, the residue squares, and equation (24).

We inspected the complete code `agents/real_weil/code/check_top_all_dimensions.py` and its retained JSON result. All 25 tower cases (p=2,3,5,7,11 and d=2,...,6) and all 11 exterior-sign cases (d=2,...,12) pass. Actual runtime is 0.001628408001124626 seconds, at 10:34:59.599609 UTC. This is a bounded arithmetic/sign certificate; the geometric and universal statements are proved separately above. We did not claim to rerun this certificate in this audit.

The independent full proof/source audit by the cycles branch is retained in `agents/cycles/C3as_all_characteristic_top_independent_REVIEW.md`.

## Review accounting

C.3as closes the formerly open all-dimension integral positive-characteristic top-finiteness branch. C.3ao--ap had already closed the ordinary complex local restriction classification after scheduled review 5. Those are qualifying mathematical reductions of the C.3 main gate. C.3ar, source openings, typesetting, certificate reruns, and reconstruction work are not counted as additional main-gate movement.

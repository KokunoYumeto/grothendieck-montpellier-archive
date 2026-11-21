# F50: exact Gaussian path signs, actual coefficient kernels, and the remaining weight estimate

Author: /root/rectangular_and_theta. Date: 2026-11-21 UTC.

This report tests the actual F43 graded kernels and F45 projective word objects against F01--F04/F17/F24. The outcome is constructive: a normalized quadratic Artin--Schreier construction reproduces each coefficient trace, gives the required negative path spectrum with zero error, and has actual cohomology in the required single parity. Its degree-zero Hom comparison is fully faithful. The pointwise estimate and its dual nevertheless retain exactly the original coefficient-weight information. No Weil weight theorem is used to establish the Gaussian sign or square-root bound.

The Gaussian cohomology inputs are classical and cited below. The all-path calculation and its precise application to the specified actual kernels are the deductions proved here; no claim of priority for Gaussian sums is made.

## 1. Exact hypotheses and primary source record

Fix a finite field k=F_q of **odd** characteristic p, a prime ell different from p, a characteristic-zero coefficient field E containing the required character values, and a nontrivial additive character psi of k. Put psi_n=psi composed with Tr_(F_(q^n)/k). We use geometric Frobenius, so E(-1) has eigenvalue q. All cohomology below is geometric etale cohomology with the indicated Weil descent.

The actual sign statements read before this construction were F01--F04, F17 and F24 in the main paper, including the geometric dictionary and the explicit trace-system hypotheses for every embedding. F03 permits an input supported in any one parity; the geometric sufficient condition in its dictionary is not its only allowed normalization. F24 permits real signed input Euler multiplicities, but still requires an effective negative path-output spectrum at unbounded even lengths. We will meet the stronger one-sign input version for each effective coefficient object.

Primary ordinary-cohomology inputs:

| Input | Exact source and use |
|---|---|
| Artin--Schreier/Kummer trace functions at every extension | Deligne, SGA 4 1/2, Applications de la formule des traces aux sommes trigonometriques, 1.7--1.9, especially (1.9.2) |
| Compactly supported Gaussian cohomology has dimension one in degree one; compact/ordinary comparison | Same, Propositions 4.2--4.3, printed p196, original PDF page235; proof p197 |
| Perfect Gaussian pairing into E(-1) | Same, Remark4.4, printed p197, original PDF page236 |
| H_c^0 on a nonproper connected curve and H_c^2 via geometric coinvariants | Same, 1.18(b)--(d), printed pp178--179 |
| Proper base change, compact-support direct image and its Leray spectral sequence | Milne, Lectures on Etale Cohomology, v2.21, Theorem17.10, p116; Proposition18.4, pp121--122. Compactification plus proper base change gives the fiber-stalk formula for Rf_! used here. |
| Kunneth and projection formulas | Milne, Theorem22.1 and Remarks22.3(b),(d), pp135--136, and Proposition22.5, pp136--137; the compact-support version is explicitly included. |
| Purity of a complex and lisse shifted perverse sheaves | BBD5.1.8, pp126--127, together with the usual smooth-curve perverse normalization. This is used only after the Gaussian size has been recovered, and only for the conditional purity assertion about a coefficient object already assumed pure. |

The original SGA scan was downloaded from the author's IAS publication page:
https://publications.ias.edu/sites/default/files/Number32.pdf
and saved as primary_sources/Deligne_SGA4half_original.pdf, SHA256
fb2939521f4c0ea0cdd55a90bec2e618e32fb433c78b194e705c6d989f4e42a6.
The complete applicable statements and proofs on printed pp196--197 were read and their scans visually inspected. The local transcript is Deligne_SGA4half_original.txt. The Milne-linked modern transcription, Deligne_SGA4half_Sommes.tex, was used for searching, not as a substitute for that scan.

The original printed Remark4.4 has an incorrect absolute-value shorthand after its correct perfect-pairing/product identity. We use only the perfect pairing and the identity gamma_psi gamma_(psi^-1)=q. In particular we do not silently import a square-root estimate from that shorthand or from Weil I/II. The argument below derives it from F03 and the two exact Gaussian sign systems.

## 2. The classical Gaussian line, with no size assumption

Let
\[
 \mathscr L_\psi=\mathcal L_\psi(x^2)\quad\hbox{on }\mathbb A^1_k.
\]
There is an actual one-dimensional Weil space
\[
 G_\psi=H_c^1(\mathbb A^1_{\bar k},\mathscr L_\psi),\qquad
 R\Gamma_c(\mathbb A^1_{\bar k},\mathscr L_\psi)=G_\psi[-1].
 \tag{G1}
\]
Write gamma_psi for its Frobenius eigenvalue. Then
\[
 g_n:=\sum_{x\in\mathbb F_{q^n}}\psi_n(x^2)
       =-\gamma_\psi^n.
 \tag{G2}
\]
There is a perfect pairing
\[
 G_\psi\otimes G_{\psi^{-1}}\longrightarrow E(-1),
 \qquad \gamma_\psi\gamma_{\psi^{-1}}=q.
 \tag{G3}
\]
These are concentration, rank and duality assertions, not weight estimates.

Here is the exact reduction of (G1) to the cited classical proposition. For the finite map pi:x maps to x^2 on A1, with j:G_m into A1, one has
\[
 \pi_*E=E\oplus j_!\mathcal L_\chi ,
\]
where chi is the nontrivial quadratic character. The second summand has zero stalk at zero, since the involution x maps to -x fixes that fiber and has no anti-invariant part. The compact cohomology of the nontrivial linear Artin--Schreier sheaf L_psi(x) on A1 is zero: it is a nontrivial character summand of the finite etale Lang cover A1 to A1, whereas the compact cohomology of its source is E(-1)[-2] with trivial translation action. Projection formula therefore identifies the compact cohomology of L_psi(x^2) with that of L_psi(x) tensor L_chi on G_m. SGA4 1/2, Proposition4.2 gives (G1)--(G2), including all extension degrees through the trace formula; its Remark4.4 gives (G3).

The involution x maps to -x acts by -1 on G_psi, because this is precisely the anti-invariant summand in the square-map construction. Consequently, for a varying nonzero scalar a, the Gaussian line of L_psi(a x^2) is G_psi tensor the quadratic Kummer line of a. This assertion follows by the etale change x maps to sqrt(a)x and its descent involution. It will give the local monodromy at a simple rank drop below.

For later use, completing the square gives the exact Fourier formula
\[
 \sum_x\psi_n(x^2+xy)=g_n\,\psi_n(-y^2/4).
 \tag{G4}
\]
This uses invertibility of 2 and a translation of the finite sum, not any positivity of the Fourier operator.

## 3. The tridiagonal determinant and an unbounded set of good path lengths

For an integer k at least two, let A_k(h) be the k by k symmetric matrix with diagonal entries 1, adjacent off-diagonal entries h/2, and other entries zero. Its quadratic form is
\[
 x^{\mathsf T}A_k(h)x=\sum_{i=1}^k x_i^2+
                   h\sum_{i=1}^{k-1}x_ix_{i+1}.
\]
Put d_k(h)=det A_k(h), with d_0=d_1=1. Expansion along the last row gives
\[
 d_k=d_{k-1}-\frac{h^2}{4}d_{k-2}.
 \tag{G5}
\]
If d_k(h_0)=0, then h_0 is nonzero and d_(k-1)(h_0) is nonzero. Indeed d_k(0)=1. A common nonzero root of consecutive d's would, by (G5), be a root of every preceding d, contradicting d_0=1. Thus every singular A_k(h_0) has rank exactly k-1, and its leading (k-1) by (k-1) block is nonsingular.

For even k=2m, d_k has degree k and leading coefficient
\[
 \ell_k=(-1)^m/2^k.
 \tag{G6}
\]
It is squarefree whenever p does not divide k+1. In particular there are unboundedly many good even k, for instance k=2pr, r positive.

For completeness, let U_k(T) be the polynomial defined by U_0=1, U_1=2T and U_k=2T U_(k-1)-U_(k-2). The recurrence proves
\[
 d_k(h)=(h/2)^k U_k(1/h).
\]
Over an algebraic closure of odd characteristic, the identity
\[
 U_k((z+z^{-1})/2)=
       \frac{z^{k+1}-z^{-(k+1)}}{z-z^{-1}}
\]
follows from the same recurrence. When p does not divide k+1, the 2(k+1)-st roots of unity are distinct. After excluding z=1,-1 and pairing z with its inverse, they give k distinct roots of U_k. Two such pairs have the same value of z+z^-1 only if they are the same pair, since they are the roots of the same quadratic. When k is even, none of these roots of U_k is zero: z+z^-1=0 would give z of order four, impossible for a root of unity of order dividing 2(k+1) with k+1 odd. Inverting these k nonzero roots proves squarefreeness of d_k. The constant term U_(2m)(0)=(-1)^m also proves (G6).

Squarefreeness, not the displayed sufficient congruence, is the actual condition used below. For example k=2 is good in every odd characteristic, even when p divides k+1.

## 4. Actual middle-degree concentration for the Gaussian path hypersurface

Fix a good even k. Define
\[
 P_k(x)=\sum_{i=1}^{k-1}x_ix_{i+1},\qquad
 H_k=\{P_k=0\}\subset\mathbb A^k_k .
\]
Then
\[
 H_c^i(H_{k,\bar k},
       \mathcal L_\psi(\sum_i x_i^2)|_{H_k})=0
                  \quad\hbox{unless }i=k-1.
 \tag{G7}
\]
This is an actual cohomological concentration statement, including the singular vertex of the quadric; it is not inferred merely from dim H_k=k-1.

**Proof.** Consider f:A1_h times A^k_x to A1_h and
\[
 \mathscr Q=\mathcal L_\psi(\sum_i x_i^2+hP_k(x)).
\]
Let Z_k={d_k=0}, a finite etale scheme, U_k=A1 minus Z_k, and j:U_k into A1. At each point of U_k the quadratic form is nondegenerate. Etale locally on U_k it can be diagonalized and its unit coefficients have square roots. By (G1), Kunneth and this etale trivialization, the only nonzero fiber compact cohomology is in degree k, with rank one. Thus R^k f_! Q restricts to a lisse rank-one system T_k on U_k.

At h_0 in Z_k the leading (k-1) block is nonsingular. Schur complement gives a congruence over the local ring with a nonsingular (k-1)-dimensional block and the final coefficient
\[
 d_k(h)/d_{k-1}(h).
\]
At h_0 this final direction is a free affine line with constant coefficient sheaf. The only nonzero fiber compact cohomology is therefore in degree (k-1)+2=k+1, of rank one, with the extra Tate twist (-1). Compact-support base change now shows that the only nonzero cohomology sheaves of Rf_! Q are
\[
 R^k f_!\mathscr Q=j_!T_k,\qquad
 R^{k+1}f_!\mathscr Q=i_*V_k
 \tag{G8}
\]
for a rank-one Weil sheaf V_k on Z_k. The first equality follows from its zero stalks at Z_k.

At each simple root of d_k, the Schur-complement coefficient has order one. The last factor of the nearby rank-one Gaussian system has the nontrivial quadratic Kummer monodromy by the final paragraph of Section2. The nonsingular block is locally unramified there. Thus T_k is geometrically nonconstant. Consequently
\[
 H_c^0(U_{k,\bar k},T_k)=H_c^2(U_{k,\bar k},T_k)=0:
\]
the first group vanishes because a nonzero section of a lisse sheaf on the connected nonproper curve cannot have proper support; the second is dual to geometric invariants of the dual line, which vanish by that nontrivial local monodromy. These are the ordinary curve facts in SGA4 1/2, 1.18(b)--(d), without a weight assertion.

The compact-support Leray spectral sequence for f therefore has only two possibly nonzero terms, at (p,q)=(1,k) and (0,k+1). Both have total degree k+1. The compact cohomology of A1 times A^k with coefficient Q is concentrated in degree k+1.

On the other hand, integrate h first. If P_k(x) is nonzero, the nontrivial linear Artin--Schreier sheaf in h has zero compact cohomology. If P_k(x)=0, the fiber is the constant sheaf on A1 with cohomology E(-1)[-2]. Compact-support base change and projection formula give
\[
 R\Gamma_c(\mathbb A^1_h\times\mathbb A^k_x,\mathscr Q)
 \simeq
 R\Gamma_c(H_k,\mathcal L_\psi(\sum_i x_i^2))(-1)[-2].
 \tag{G9}
\]
The concentration in degree k+1 on the left is exactly (G7). This proves the claim.

The proof uses only ordinary finite-dimensional cohomology, fiber calculations, nontrivial local monodromy and duality. In particular it has not used purity of a curve or any Weil bound.

## 5. An explicit effective spectrum for every good even k

Let C_k be the smooth projective curve completing y^2=d_k(h). It is geometrically connected because d_k is squarefree and nonconstant. Its genus is (k-2)/2. Let eta_k be the rank-one quadratic Weil character with
\[
 \operatorname{Tr}(F^n\mid\eta_k)=\chi_n(\ell_k).
\]
It is the anti-invariant line of the two points at infinity; these points need not be individually rational.

Let W_k be the actual finite Weil space
\[
 W_k=H^0(Z_{k,\bar k},
                 \mathcal L_\chi(d_{k-1}|_{Z_k})).
\]
The function d_(k-1) is invertible on Z_k by (G5), so this is a well-defined quadratic Kummer sheaf on a finite etale scheme. It has dimension k. Its trace is the sum of chi_n(d_(k-1)(h)) over the rational roots of d_k, with no assumption that all roots are rational over the base field.

Define the effective Weil space
\[
 B_{k,\psi}=
 G_\psi^{\otimes k}\otimes
       (H^1(C_{k,\bar k},E)\oplus\eta_k)
 \ \oplus\
 E(-1)\otimes G_\psi^{\otimes(k-1)}\otimes W_k .
 \tag{G10}
\]
Its dimension is (k-2)+1+k=2k-1. It has genuine positive eigenvalue multiplicities, though its eigenvalues need not be real or have a common weight.

For
\[
 N_{k,n}^{\psi}=
 \sum_{P_k(x)=0}\psi_n(\sum_i x_i^2)
\]
the exact all-extension identity is
\[
 q^n N_{k,n}^{\psi}
       =-\operatorname{Tr}(F^n\mid B_{k,\psi})
                 \quad(n\ge1).
 \tag{G11}
\]

**Proof with all signs.** Put Q=q^n. Character orthogonality gives
\[
 QN_{k,n}^{\psi}
       =\sum_{h\in\mathbb F_Q}
             \sum_{x\in\mathbb F_Q^k}
                 \psi_n(x^{\mathsf T}A_k(h)x).
\]
For a nondegenerate symmetric quadratic form over an odd finite field, diagonalization and the elementary identity sum_x psi_n(a x^2)=chi_n(a)g_n give the inner sum chi_n(d_k(h))g_n^k. At a determinant root, Schur complement gives the sum Q chi_n(d_(k-1)(h))g_n^(k-1). Hence
\[
 QN_{k,n}^{\psi}
   =g_n^k\sum_h\chi_n(d_k(h))
      +Q g_n^{k-1}
          \sum_{d_k(h)=0}\chi_n(d_{k-1}(h)).
 \tag{G12}
\]
The smooth projective curve trace formula, using only H0=E and H2=E(-1), gives
\[
 \sum_h\chi_n(d_k(h))
    =-\operatorname{Tr}(F^n\mid H^1(C_k))-\chi_n(\ell_k).
 \tag{G13}
\]
Indeed its affine point count is Q plus the sum on the left, and its infinity fiber has 1+chi_n(ell_k) points. Since k is even, (G2) gives g_n^k=gamma_psi^(kn) but g_n^(k-1)=-gamma_psi^((k-1)n). Substitution into (G12) is exactly (G11).

This identity is consistent with the actual concentration in (G7), with the multiplication by Q corresponding to twist (-1). It identifies the Frobenius character of H_c^(k-1)(H_k,...)(-1) with (G10); it does not assert a canonical splitting of all the extensions in that cohomology or arithmetic semisimplicity.

All algebraicity and embedding hypotheses needed by F03 can be checked here without a Weil weight or integrality theorem. The power traces of H1(C_k) are the rational integers 1+q^n-#C_k(F_(q^n)). Newton identities in its finite dimension give a rational characteristic polynomial. Its eigenvalues are therefore algebraic and its multiset is stable under every embedding. The Frobenius of W_k is a signed permutation: every point cycle has polynomial T^d-epsilon with epsilon=+1 or -1. It therefore has a rational characteristic polynomial as well as finite order; eta_k is quadratic. Finally gamma_psi=-g_1 is cyclotomic. Thus applying an embedding to (G10) gives the same spectrum as replacing psi by its conjugate character, with H1(C_k), W_k and eta_k unchanged as multisets. This verifies the all-embedding output condition explicitly.

As a sharp check at k=2, H_2 is the union of the two coordinate axes. Directly N_(2,n)=2g_n-1, so
\[
 QN_{2,n}=2Qg_n-Q=-2Q\gamma_\psi^n-Q.
 \tag{G14}
\]
This agrees with (G10): H1(C_2)=0, its infinity line contributes eigenvalue q after tensoring with G^2, and W_2 has two trivial quadratic-character fibers.

The squarefree hypothesis has a concrete role. In characteristic five, k=4 gives d_4(h)=(h^2-1)^2 and d_3(1)=d_3(-1)=3. The generic quadratic-character system is then geometrically constant, so the vanishing of its H_c^2 used in Section4 fails. Formula(G12), which does not require squarefreeness, gives for q=5
\[
 QN_{4,n}=5^{3n}-2\,5^{2n}-2(-5\gamma_\psi^3)^n.
\]
Here gamma_psi squared is 5, by (G3) and chi_5(-1)=1. The root 125 has positive coefficient and strictly largest modulus. Hence this particular bad length cannot have the exact negative effective spectrum asserted for good lengths. The unbounded good set, not all even integers in every characteristic, is the proved assertion.

## 6. Recovering the classical Gaussian size through the sign theorem

Take t_n(x)=psi_n(x^2) on A1. Its pointwise bound is 1, so a=0,d=1,B=1 in F03. Equation(G2) gives its negative rank-one input spectrum. Equations(G7),(G11) give the required opposite sign at the unbounded even set k=2pr, with **zero error**. F03 proves
\[
 |\gamma_\psi|\le q^{1/2}.
\]
The same construction with psi^-1 gives the upper bound for gamma_(psi^-1). The perfect pairing(G3) then forces equality for both. Every embedding replaces psi by another nontrivial character and leaves the geometric construction applicable, so the same argument proves the assertion at every embedding.

This recovers a classical Gauss-sum theorem as an exact application test of F03/F17. The proof did not use a curve RH estimate: H1(C_k) occurred solely as an effective finite spectrum in the negative output. No claim of a new GCT coefficient-weight theorem follows from this scalar test.

## 7. A normalized, exact-trace construction for any effective coefficient space

Let C be a finite-dimensional Weil space on a point, with invertible Frobenius and algebraic eigenvalues. Arithmetic Jordan blocks are permitted. Let p:A1 to Spec k and set
\[
 J_\psi(C)=\mathscr L_\psi\otimes p^*(C\otimes G_\psi^\vee)[1].
 \tag{G15}
\]
It is a lisse sheaf shifted by one, hence a perverse Weil sheaf on the smooth curve A1. By (G1),
\[
 R\Gamma_c(\mathbb A^1,J_\psi(C))\simeq C
 \tag{G16}
\]
in degree zero, naturally in C. The evaluation G tensor G^vee to E and the cancelling shifts supply this isomorphism.

Its pointwise trace is
\[
 t_{C,n}(x)=-\gamma_\psi^{-n}
        \operatorname{Tr}(F^n\mid C)\,\psi_n(x^2),
 \qquad M_{C,n}=\operatorname{Tr}(F^n\mid C).
 \tag{G17}
\]
Thus this construction realizes the actual desired coefficient trace, with no extra Gaussian scalar remaining in its sum.

For every good even k, external tensor product and restriction to H_k give
\[
 R\Gamma_c(H_k,J_\psi(C)^{\boxtimes k}|_{H_k})
 \simeq C^{\otimes k}\otimes G_\psi^{\vee\otimes k}
       \otimes R\Gamma_c(H_k,\mathcal L_\psi(\sum x_i^2))[k].
 \tag{G18}
\]
It is concentrated in degree -1, since (k-1)-k=-1. Its twisted effective output spectrum is
\[
 B_{k,C}=C^{\otimes k}\otimes
           G_\psi^{\vee\otimes k}\otimes B_{k,\psi},
\qquad
 QN_{k,C,n}=-\operatorname{Tr}(F^n\mid B_{k,C}).
 \tag{G19}
\]
Consequently F03's positive input and F24's negative-output requirement both hold, with E_(k,n)=0. The odd degree -1 is the shifted version of the actual hypersurface middle degree k-1; it is not a dimension-based assertion. The coefficient objects may depend on the word.

This assertion concerns effective finite Weil spaces, or the even-degree total realizations of F45. It does not say that the tensor powers of an arbitrary signed virtual complex have an effective output spectrum.

## 8. Exact pointwise and dual limitations

Fix a complex embedding and let R(C) be the maximum modulus of a Frobenius eigenvalue of a nonzero C. Equal eigenvalues have their genuine positive multiplicities. Set b_max=2 log_q R(C); this real number is useful for recording the sharp threshold, even when a proposed integral weight has not yet been established.

By Section6,
\[
 \sup_x|t_{C,n}(x)|=
       q^{-n/2}\big|\operatorname{Tr}(F^n\mid C)\big|.
 \tag{G20}
\]
Therefore a bound of the exact form |t_(C,n)(x)| at most B q^(na/2), with B independent of n, holds **if and only if**
\[
 R(C)\le q^{(a+1)/2}.
 \tag{G21}
\]
For sufficiency, sum the absolute values of the finitely many eigenvalue powers, using B=dim C. Jordan blocks do not add polynomial factors to traces of powers. For necessity, apply F02 to the trace sequence in (G20). Thus the least real pointwise exponent is b_max-1. The exact sign comparison has moved the open issue into the pointwise estimate without weakening that estimate for C.

For F17's specified reciprocal pairing into E(-1), take the second normalized system
\[
 J_{\psi^{-1}}(C^\vee(-1)).
\]
Its total spectrum is {q/alpha: alpha in Spec C}, with a perfect pairing with the original C. Put b_min=2 log_q(min |alpha|). The sharp pointwise exponent of this second system is
\[
 a_D=1-b_{\min}.
 \tag{G22}
\]
At the level of sharp **real thresholds**, pairing the original threshold a=b_max-1 with the formally matching dual threshold -a=1-b_max leaves the exact difference
\[
 a_D-(-a)=b_{\max}-b_{\min}.
 \tag{G23}
\]
It vanishes precisely when all eigenvalues have the same absolute value in that embedding. This statement is a comparison of real thresholds; F03/F17 are stated with an integer a, and it is not an invocation of them at an arbitrary real value.

For their actual purity conclusion, fix one integer target weight w and set a=w-1. The original bound and F17's specified dual bound at exponent 1-w hold under every embedding if and only if
\[
 b_{\max,\sigma}\le w\le b_{\min,\sigma}
                 \quad\hbox{for every embedding }\sigma.
 \tag{G23a}
\]
Equivalently, every conjugate eigenvalue has modulus q^(w/2). Necessity and sufficiency follow directly from (G21)--(G22). In particular, width zero separately in each embedding is insufficient if the radii differ across embeddings; the same integer w must work for all of them. This is the exact surviving purity gate for the specified wrapper, not a prohibition on other nonconstant coefficient constructions.

If C is pure of an integer weight w, then J_psi(C) is perverse pure of weight w: its unshifted lisse sheaf has weight w-1, by the just-proved Gaussian weight and the finite-order Artin--Schreier character, and shift[1] changes the complex weight to w. This uses BBD's convention. It permits nonsemisimple arithmetic Frobenius; geometric semisimplicity here is immediate because all geometric constituents are copies of the same rank-one local system.

## 9. Actual degree-zero Hom and both action comparisons

For finite Weil spaces C,C', there is a natural isomorphism
\[
 \operatorname{Hom}(J_\psi(C),J_\psi(C'))
       =\operatorname{Hom}_F(C,C').
 \tag{G24}
\]
The Hom on the left can be taken in the perverse heart or as degree-zero Hom in the constructible derived Weil category.

**Proof.** The equal shifts cancel. Tensoring by the same invertible rank-one lisse sheaf and constant Gaussian line is an equivalence on the underlying lisse categories, so their factors cancel as well. A morphism between two geometrically constant sheaves on the connected geometric A1 is exactly a linear map between their constant fibers. Requiring compatibility with Weil descent is exactly commutation with the two Frobenius maps. This is (G24), naturally and compatibly with composition. No assertion about higher Ext groups is made.

Consequently J is an exact fully faithful functor into perverse Weil sheaves. Applied to the actual fixed-parameter H,K of F46 it gives
\[
 \operatorname{End}(JH)=A,\qquad
 \operatorname{Hom}(JH,JK)=M,
 \qquad
 \operatorname{End}(JK)=\operatorname{End}_A(M).
 \tag{G25}
\]
Precomposition and postcomposition retain every specified right generator and ordinary left operator. At the collision, the arithmetic Jordan block and the actual nilpotent endomorphisms are retained. If H,K have the pure weight-zero Weil structures constructed in F46, their J images are actual pure weight-zero perverse Weil sheaves. The pointwise bounds and both Gaussian signs are then available from the chosen fixed-parameter Weil data.

The sign construction in Sections7--8 applies to the identity trace of the effective object C. An arbitrary inserted operator trace Tr(T F^n|C) is a different input: its coefficients on Frobenius eigenspaces need not be positive multiplicities, and its tensor-inserted output need not be effective. Equation(G25) retains the actual operators as morphisms but does not, by itself, assert the effective output sign for every such insertion. The all-word assertion below uses the effective graded coefficient objects of F43, explicitly not this unproved identification of operator insertions with object traces.

This functor is **not monoidal**. J(E) is not the tensor unit; its shift is [1]. Moreover
\[
 J(C)\otimes J(C')=
 \mathcal L_{\psi^2}(x^2)\otimes
    p^*(C\otimes C'\otimes G_\psi^{\vee\otimes2})[2],
\]
which does not equal J(C tensor C'). Neither geometric simple labels nor an unknown canonical basis have been produced: geometrically all these objects are copies of the same rank-one Artin--Schreier sheaf shifted by one. The fully faithful Hom statement therefore does not contradict F48's tensor/full-centralizer limits.

For the **graded F43 model**, choose a one-dimensional point Weil line U with eigenvalue q^(1/2), and replace each labeled edge of degree e by U^e. Its coefficient matrix has trace equal to the actual positive Laurent matrix evaluated at v=q^(n/2) at extension degree n. This is an honest arithmetic Weil line; an odd e is not asserted to be an integral Tate motive. Even e gives the usual integral Tate line.

Each named kernel acts on tuples by finite direct sums of tensor products with these constant coefficient spaces. The natural identification
\[
 J(C\otimes V)\simeq p^*V\otimes J(C)
 \tag{G26}
\]
shows that these constant-kernel actions and their explicitly ordered compositions transport through J. Thus all actual graded matrices of P1,P2 and the stated left operators are retained at the level of F43's graded K0 action; the left row-matrix opposite-composition convention is unchanged. An explicitly composed word has the same coefficient object, followed by J, and its closed-path object gives its actual scalar trace.

This does not upgrade equalities of matrices in graded K0 to a coherently chosen lift of every algebra relation or commutation. It also does not put all retuned words into endomorphisms of one fixed finite Weil space: the coefficient objects attached to entries and closed paths change with the word. In contrast, (G25) is an actual fixed-parameter End/Hom realization, whose Frobenius powers remain those of its fixed Weil operator and are not re-evaluations of the quantum parameter. These are two different, explicitly stated comparison modes.

## 10. Exact application to F45 and the path coefficients

For a nonempty right word w of length L and cyclic transition count 2s, F43 gives
\[
 T_w(v)=20D^L+16D^{L-s}+4D^{L-2s}(D-2)^{2s}
       =\sum_{r=-L}^{L}c_rv^{2r},\quad c_r\ge0.
\]
F45 supplies the actual projective coefficient complex with
H^(2r)=E(-r)^(c_r), odd groups zero. Let
\[
 C_w=\bigoplus_{r=-L}^{L}E(-r)^{c_r}
\]
be its total effective Weil space. Then (G17) gives exactly
\[
 \sum_x t_{C_w,n}(x)=T_w(q^{n/2}),
\]
and (G19) gives its negative path spectrum at every good even k, with no error. This is a single specified construction for all the word-dependent spaces.

Both endpoint coefficients are nonzero, due already to 20D^L. Hence b_max=2L and b_min=-2L. The sharp original pointwise exponent is 2L-1; the sharp reciprocal-system exponent is 2L+1. F17 would need 1-2L for the latter when it seeks purity at the original upper weight 2L. The gap is **4L**. The total object is mixed, as F45 explicitly states; the new sign realization does not erase that fact.

On the other hand, for the genuine homogeneous piece C_(w,r)=E(-r)^(c_r), the exponents are a=2r-1 and a_D=1-2r. Both required bounds hold, and F03/F17 give precisely its already known pure weight 2r. More generally, every homogeneous path-degree coefficient of the actual F43 kernels has this degreewise realization, using U^e for odd degrees if needed. The path-label sets and the bound of at most 64 times 4^L closed labeled paths for an explicitly written length-L word are available from F43, so this statement does not presuppose a new positive rule for arbitrary GCT inputs.

The Gaussian construction supplies actual opposite-sign comparisons for those objects. It gives no new designated canonical-basis identification, no all-rank positive rule, and no new homogeneous-polytope or binary-input PH1 assertion.

## 11. What the direct positive graph-count constructions do instead

The natural finite-state positive kernel trace gives C_w directly, with positive Tate coefficients. Two elementary attempts to regard that positive count as the required affine input have distinct exact outcomes.

### 11.1 Point-supported encoding

Put t_n(x)=Tr(F^n|C_w) at x=0 and zero elsewhere on A1. Then
\[
 M_n=\operatorname{Tr}(F^n|C_w),\qquad
 QN_{k,n}=Q\big(\operatorname{Tr}(F^n|C_w)\big)^k.
\]
The second expression is a nonzero positive-multiplicity Tate power sum. It cannot equal the negative of any effective finite Weil power sum for all n: their sum would be a nonempty effective spectrum with every power trace zero, contradicting F02. Thus the exact opposite sign fails.

This example alone does not obstruct F04 with an empty output spectrum and a large enough permitted error: its small support gives a loose ambient-dimension bound. We do not claim otherwise. It identifies why merely putting the positive path labels on points has not constructed the required exact negative path cohomology.

### 11.2 Affine padding has a provably linear error cost

To retain the scalar trace after adding an affine d-dimensional base, take
\[
 t_n(x)=Q^{-d}S_n,\qquad S_n=\operatorname{Tr}(F^n|C_w).
\]
This is the constant coefficient object C_w(d), and M_n=S_n exactly. Its sharp pointwise exponent is a=2L-2d.

For even k=2m, splitting the kd coordinates into odd/even positions turns P_k into a nondegenerate bilinear pairing on two md-dimensional spaces: its block coefficient matrix is triangular with invertible diagonal. The number of zeros is
\[
 \#H_k(\mathbb F_Q)=Q^{kd-1}+Q^{kd/2}-Q^{kd/2-1}.
\]
Indeed the zero first vector contributes Q^(md) choices, while each of the other Q^(md)-1 first vectors imposes one nonzero linear equation on the second vector. Thus
\[
 QN_{k,n}=S_n^k
       \bigl(1+Q^{1-kd/2}-Q^{-kd/2}\bigr).
 \tag{G27}
\]
For kd>2, its unique highest-radius root is q^(kL), with strictly positive coefficient c_L^k. For kd=2 the same root has twice that positive coefficient. The remaining displayed terms have smaller radius.

Suppose one tried to write (G27) as minus an effective finite spectrum plus an F04 error. After moving the effective spectrum to the left, the positive coefficient of q^(kL) cannot cancel. F02 therefore forces the error's exponential rate to be at least q^(kL). At the sharp pointwise exponent above, F04's allowed rate is
\[
 q^{\,k(a+d)/2+\eta_k}
       =q^{\,k(L-d/2)+\eta_k}.
\]
Necessarily
\[
 \eta_k\ge kd/2.
 \tag{G28}
\]
This is incompatible with eta_k/k tending to zero on any unbounded even set. Inflating a by d can absorb the cost, but then the resulting weight estimate has already been weakened by d. The argument also works on full extension-degree progressions: the positive top Tate root remains visible after powering.

This is the explicit graph-route boundary beyond F42's qualitative constant-sheaf example. Fourier oscillation in (G4), and the genuine rank-one monodromy in Section4, are exactly what change the path-output parity in the successful Gaussian construction.

## 12. Grothendieck dictionary and the precise remaining Q3 obligation

The schemes are A1, the affine quadric H_k, the quadratic pencil over A1, the finite etale divisor Z_k, and the smooth projective double cover C_k. Artin--Schreier and Kummer sheaves come from their finite etale torsors. Compact-support direct image, base change and the Leray spectral sequence prove the actual single-degree statement; the trace formula turns it into (G11). The Tate twist (-1) is the factor Q. Duality of the Gaussian lines is an actual perfect pairing, not a bar involution or a substitution for Frobenius.

The normalized operation J is a fully faithful degree-zero realization of point-Weil End/Hom data inside perverse sheaves on a connected finite-field curve. It is a module functor for constant coefficient spaces, not a strong monoidal functor. In the F46 fixed-parameter mode it retains the actual algebra, its tensor module, both actions, and the arithmetic collision nilpotent. In the F43 retuned-graded mode it retains the specified graded kernels and word composition, with changing coefficient objects and the exact K0/coherence limitations already recorded there.

For the specified construction, the opposite-sign middle-degree gate is **proved**. The remaining pointwise/dual gate is exactly (G21)--(G23). For a new designated nonstandard coefficient object C, its pointwise bound is equivalent to the desired upper bound on the eigenvalues of C; the reciprocal system adds precisely the corresponding lower bound. Thus this construction does not turn an unproved coefficient-weight assertion into a weaker elementary estimate. For F45 it gives the exact known degreewise weights and the mixed total's quantified width. A further reduction of Q3 would have to replace the constant unknown coefficient factor by a genuinely varying, independently bounded local system while retaining the required actual operation comparisons.

This last requirement is narrower than an unspecified request for new geometry. We have supplied the curve, sheaves, all-extension trace identity, normalization, actual Hom embedding, middle-degree signs and their composition scope; the still-unknown information has been isolated in one explicit pointwise spectral inequality.

## 13. Check record

The report's algebraic recurrences, rank-drop Schur complement, degree shifts, exact Fourier identity, curve point-count normalization, effective spectrum signs, pointwise equivalence and dual exponents were reconstructed directly by the author. Parent independently derived (G12)--(G14) before reading the completed report. Original SGA Gaussian statements and the relevant Milne formalism were inspected in context; no complete proof of the general etale machinery is claimed.

A fresh complete independent review of this report and its eventual generated fragment is requested. The source/proof reviewer suggested explicitly verifying the output algebraicity/all-embedding hypotheses by Newton identities; that argument is included above.

The exact script check_gaussian_sign_wrapper.py completed successfully. It verifies the tridiagonal determinant and consecutive coprimality for k=2 through10; the sufficient squarefree condition for p=3,5,7,11,13 and even k up to30; and (G12), the split-bilinear graph count, and the k=2 formula by exact cyclotomic polynomial arithmetic at ten listed prime-field cases. It also verifies the excluded p=5,k=4 determinant and minor. These finite checks are additional sign/convention checks, not substitutes for the general proofs. Hashes and the full output are recorded separately. No proof-assistant certificate or new proof of a general Weil theorem is claimed.

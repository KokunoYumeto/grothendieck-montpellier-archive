> Working-history note: preliminary geometric gaps below are superseded by SG-08–SG-11 in HODGE_SIGN.tex and agent_sign_strengthening.md. Use the final paper for accepted conclusions.

# Root analysis: a precise sign-only criterion

Run HODGE_SIGN-20261121, 2026-11-21. GPT-6 Astra Pro, effort setting not exposed.
This is a reconstruction with explicit hypotheses, not a claim to have located an absent Lean declaration.

## HS-01: effective power sums detect every inverse root

Let lambda_1,...,lambda_s be distinct nonzero complex numbers and let c_j be positive integers. If for every n>=1,
|sum_j c_j lambda_j^n| <= C B^n, then |lambda_j|<=B for every j. The same conclusion holds with C exp(o(n)) B^n in place of C B^n.

Proof. The power series sum_{n>=1}(sum_j c_j lambda_j^n)z^n is holomorphic on |z|<B^{-1}. Near zero it equals sum_j c_j lambda_j z/(1-lambda_j z). Each summand has a pole at z=lambda_j^{-1}; the other summands are regular there, and c_j is nonzero. By uniqueness of analytic continuation this rational function cannot have a pole inside the disk of convergence. Thus every |lambda_j|<=B. The subexponential variant has the same convergence radius. This does not say that the values of the power sums are positive. It says that multiplicities of coincident roots add instead of cancelling. No diagonalizability is needed: traces of powers depend only on the eigenvalues with algebraic multiplicity. QED.

## HS-02: tensor amplification with an effective Frobenius remainder

Fix q>1 and a finite-dimensional complex vector space V with invertible F. Let a be real. For an unbounded set K of positive integers suppose that for each k in K there are a finite-dimensional W_k with invertible G_k, a sign e_k in {+1,-1}, and numbers R_{k,n} such that for every n>=1

e_k R_{k,n}=Tr((F^{tensor k})^n)+Tr(G_k^n),
|R_{k,n}|<=C_k exp(o_k(n)) q^{n(ka+c_k)},  c_k/k ->0 along K.

Then each eigenvalue alpha of F has |alpha|<=q^a. If the multiset of eigenvalues is stable under alpha -> q^{2a}/alpha, all have modulus q^a.

Proof. For fixed k the right hand side is a power sum with nonnegative integral multiplicities. HS-01 implies that each eigenvalue of F^{tensor k}, in particular alpha^k, has modulus at most q^{ka+c_k}. Taking kth roots and letting k grow proves the upper bound. The spectral symmetry applies the upper bound to q^{2a}/alpha, giving the lower bound. QED.

Geometric language. For a finite field, replace the complex vector spaces by Weil Q_l-modules and fix an embedding of their coefficient field into C. In the Grothendieck group of finite-dimensional Frobenius modules the essential condition is that, after one global sign, the virtual remainder is an *effective* class containing [V^{tensor k}]. Concentration in a single cohomological degree is sufficient, but is stronger than necessary. A duality V tensor V -> Q_l(-2a) supplies the spectral symmetry when 2a is an integer and it is Frobenius-equivariant and perfect. More generally apply upper bounds separately in dual degrees. Purity for every embedding needs the estimates for every embedding; a bound for a single embedding is only iota-purity. Algebraicity and independence of l are not consequences of the complex lemma.

## HS-03: the path-quadric Parseval estimate, including vectorization

Let E=F_{q^n}, A=E^d, Q=|A|=q^{nd}, psi_n a nontrivial additive character of E, and b:A times A -> E a nondegenerate bilinear form. For k>=2 and nonzero edge scalars a_1,...,a_{k-1}, set

P(x_1,...,x_k)=sum_{i=1}^{k-1}a_i b(x_i,x_{i+1})+sum_i f_i(x_i)+c,

where the f_i are arbitrary E-valued functions (polynomials if geometry is wanted). Suppose |t_n(x)|<=C q^{nw/2}. Define M_n=sum_x t_n(x), N_{k,n}=sum_{P(x)=0}product_i t_n(x_i), and R_{k,n}=sum_{h in E^*}sum_{x in A^k}product_i t_n(x_i)psi_n(hP(x)). Then

q^n N_{k,n}=M_n^k+R_{k,n},
|R_{k,n}|<=C^k q^{n(k(w+d)/2+d/2+1)}.

Proof. Additive-character orthogonality gives the identity. For h!=0 the matrix K_{h,i}(x,y)=psi_n(h a_i b(x,y)) has K K*=Q I, because nondegeneracy makes the sum over y zero for x!=x' and Q otherwise. Thus its operator norm on counting-measure l2(A) is Q^{1/2}. Multiplication by t_n(x)psi_n(h f_i(x)) has norm at most C q^{nw/2}; the endpoint vectors have l2 norm at most C q^{nw/2}Q^{1/2}. Express the path sum as the product of k-1 Fourier matrices, k-2 internal multiplication matrices, and the two endpoint vectors; transpose at one endpoint is bounded just as the Hermitian scalar product, by complex conjugating the endpoint. Its modulus is at most (C q^{nw/2})^k Q^{(k+1)/2}. Summing over q^n-1 nonzero h proves the claimed, slightly weakened, bound. QED.

Consequently, if M_n=(-1)^d Tr(F^n) and N_{k,n}=(-1)^{kd-1} Tr(B_k^n), with fixed Frobenius modules for all n, then

(-1)^{kd-1}R_{k,n}=Tr((qB_k)^n)+Tr((F^{tensor k})^n).

HS-02 applies with a=(w+d)/2 and c_k=d/2+1. A different good quadric can be chosen for each k over a finite extension E_k of F_q: apply the estimate over all further extensions and divide the exponent by [E_k:F_q]. Thus a Bertini good-parameter open having no F_q-point need not be fatal. What must still be proved is the existence of such a good open *inside this restricted Fourier-compatible family* and the stated effective cohomology after all boundary/ambient contributions have been removed.

## HS-04: smoothness alone does not give the sign hypothesis

Take d=1, k=2, t_n=1, P(x,y)=xy-1. The affine hypersurface is G_m and is smooth over every field. Put r=q^n. Then M_n=r, N_{2,n}=r-1, and R_{2,n}=-r. Nonetheless q^n N_{2,n}=r^2-r and M_n^2=r^2 have the identical root q^2 with equal coefficient, and it cancels in their difference.

Proof. For each nonzero x there is exactly one y=x^{-1}; there are r-1 points. Alternatively H_c^1(G_m)=Q_l and H_c^2(G_m)=Q_l(-1), so its compactly supported cohomology is not concentrated in the middle degree. The common Tate root in the identity is visible directly. All the Parseval hypotheses and geometric smoothness hold, while the asserted opposite-purity sign does not. QED.

This refutes only the universal implication 'smooth Bertini hypersurface implies no inverse-root cancellation'. It does not refute a more specialized omitted construction, nor the stipulated RH/GRH statements. Reduced cohomology could remove this particular cancellation; that is an additional operation whose compatibility must be proved, not an automatic consequence of smoothness.

## HS-05: neither cohomological parity nor weights determine a polarization

Let V=Q^2, F=q^r I, all placed in cohomological degree 2r. The symmetric forms b_+=diag(1,1) and b_-=diag(1,-1) are both nondegenerate and satisfy b(Fx,Fy)=q^{2r}b(x,y). They have identical traces, determinants of 1-TF, Tate weight, and trace parity. Only the first is positive definite. Thus those data alone cannot establish positivity of a specified intersection form.

Proof. Direct substitution proves Frobenius compatibility for either form. Their signatures are (2,0) and (1,1). QED.

Geometric realizations and normalized quadric signs are handled independently by SG-*. This linear example establishes a logical limitation on the trace data, not a counterexample to the Hodge standard conjecture.

## HS-06: the missing geometric statement cannot be inferred from the wrappers

ALPOGE_Main.lean declares RH and three forms of Dirichlet nonvanishing/zero location by importing Statements and Supplements.Kernels.MainTheoremsAll. ALPOGE_Statements.lean defines only these global analytic propositions. Neither file gives a finite-field sign/purity theorem. The supplied map, section5.1(b), explicitly reports only implications ending in LateralTheory.EWeil.Goal; that is a report about a larger archive, not a theorem proof available here. The precise reconstruction above is proved; its general geometric applicability is not certified by the supplied wrappers.

## Questions still being attacked

1. Can the effective-class condition be obtained for enough Fourier-compatible sections of each variety, using affine weak Lefschetz and good behavior at infinity? Ordinary Bertini fails to prove it (HS-04); need a non-characteristic restriction theorem plus a boundary accounting result.
2. Could known Katz persistence of purity provide a different route? Katz baby16.pdf Theorem2.1/Cor2.2 and Theorems4.1,5.1 give a known tensor argument using reality and tensor coinvariants, not the unidentified path restriction theorem. This offers established absolute values, but cannot identify the Hodge intersection form with the parity sign.

## Root whole-proof check

Read the complete proofs of HS-01 through HS-05 after drafting. Checked multiplicities, tensor eigenvalues without semisimplicity, order of limits (n first then k), all-extension quantifier, normalizations of qB_k and Tate twist, Fourier matrix norm, endpoint factors, and smooth hyperbola counterexample. All five pass this targeted proof check; independent checking is still requested before final packaging.

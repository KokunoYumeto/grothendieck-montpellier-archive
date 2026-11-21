# Main proof draft — GCT_NSRH_20261121_root

Date: 2026-11-21 (Europe/Berlin). Author/checker metadata: root GPT-6 Astra Pro, effort not exposed. These are elementary results established for this investigation, not claims of novelty in the mathematical literature.

## F1. Exact path-quadric identity and Parseval bound

Let F_Q be a finite field, V=F_Q^d, d>=1, let < , > be a nondegenerate bilinear form on V, let psi be a nontrivial additive character, and let k>=2. For t:V->C put M=sum_x t(x), Q_k(x_1,...,x_k)=sum_{i=1}^{k-1}<x_i,x_{i+1}>, and N_k=sum_{Q_k=0} product_i t(x_i). Then

Q N_k = M^k + R_k,
R_k = sum_{h in F_Q^*} sum_{x_1,...,x_k} product_i t(x_i) psi(h Q_k),
|R_k| <= (Q-1) Q^{d(k-1)/2} ||t||_2^2 ||t||_infty^{k-2}.

Proof. Additive character orthogonality says sum_h psi(h z)=Q if z=0 and zero otherwise; separate h=0. Let K_h=(psi(h<x,y>))_{x,y in V} and D=diag(t(x)). Nondegeneracy and orthogonality give K_h K_h^*=Q^d I for h!=0, so ||K_h||=Q^{d/2}. The inner sum is t^T K_h D K_h ... D K_h t (k-1 K factors and k-2 D factors); interpret the left endpoint as the Hermitian dual of bar(t). Cauchy-Schwarz and operator-norm submultiplicativity bound its modulus by Q^{d(k-1)/2}||t||_2^2||t||_infty^{k-2}. Sum Q-1 terms. No nonnegativity or geometric hypothesis is used. This is an open-chain matrix coefficient, not generally a trace of a power.

## F2. Finite spectral no-cancellation lemma

Let alpha_1,...,alpha_r be distinct nonzero complex numbers and c_j nonzero complex constants. For p_n=sum_j c_j alpha_j^n, n>=1,
limsup_n |p_n|^{1/n} = max_j |alpha_j|.
In particular |p_n|<=C n^A R^n for every n implies |alpha_j|<=R. Polynomial factors can be replaced by any subexponential factor.

Proof. The upper bound follows by the triangle inequality (with an immaterial constant). For sufficiently small z the generating series sum_{n>=1} p_n z^n equals sum_j c_j alpha_j z/(1-alpha_j z). Each z=1/alpha_j is a genuine simple pole because its coefficient is nonzero and all other summands are regular there. Its radius of convergence is exactly 1/max_j |alpha_j|. The Cauchy-Hadamard formula proves the equality. The asserted estimate makes the radius at least 1/R. The case r=0 is vacuous. No reality, positivity of the eigenvalues, or semisimplicity is needed; traces of powers ignore nilpotent Jordan off-diagonal parts. Positivity of multiplicities is sufficient to ensure that coincident spectral values do not cancel after regrouping.

## F3. Tensor-path upper-weight and purity criterion

Fix a prime power q>1, d>=1, an integer a, B>0. For every n>=1 put Q=q^n and choose t_n:F_Q^d->C with |t_n(x)|<=B Q^{a/2}. Define M_n, N_{k,n}, R_{k,n} as in F1, using any nontrivial additive character on F_Q.

Assume (S1) a fixed finite nonempty multiset A of nonzero algebraic numbers and epsilon in {+1,-1} give M_n=epsilon sum_{alpha in A} alpha^n for all n (multiplicities positive integers).
Assume (S2) for an unbounded set K of integers k>=2, there is for each k a fixed finite multiset B_k of nonzero algebraic numbers (possibly empty) such that
q^n N_{k,n} = -epsilon^k sum_{beta in B_k} beta^n
for all n. This is a spectral parity condition, not a sign condition on the numerical values N_{k,n}.

Then every alpha in A has |alpha| <= q^{(a+d)/2} in the chosen complex embedding. For an algebraic number field E containing A and every B_k, suppose for every embedding sigma:E->C there are corresponding trace functions t_{n,sigma} satisfying the same hypotheses with sigma(A), sigma(B_k) and a constant B_sigma independent of n. Then the upper bound holds for all conjugates. A common number field is convenient rather than essential; one can equivalently require this for every embedding of the algebraic closure containing all these spectra. If moreover (D) A is invariant with multiplicities under alpha -> q^{a+d}/alpha, then every |alpha|=q^{(a+d)/2}; with all embeddings this is purity of weight a+d. Here q^{a+d} must be specified algebraically for (D); in geometric use a+d is an integer.

Proof. The pointwise bound gives ||t_n||_2^2 <= B^2 Q^{a+d} and ||t_n||_infty^{k-2}<=B^{k-2}Q^{a(k-2)/2}. F1 therefore gives
|R_{k,n}| <= B^k Q^{k(a+d)/2+d/2+1}.
The identity and (S1)-(S2) give
-epsilon^k R_{k,n} = sum_{beta in B_k} beta^n + sum_{(alpha_1,...,alpha_k) in A^k}(alpha_1...alpha_k)^n.
Every grouped coefficient on the right is a positive integer. F2 applied for each fixed k shows |alpha|^k <= q^{k(a+d)/2+d/2+1}, because the diagonal tuple (alpha,...,alpha) contributes alpha^k with positive multiplicity. Hence
|alpha| <= q^{(a+d)/2+(d/2+1)/k}.
Let k tend to infinity through K. For (D), apply the upper bound to q^{a+d}/alpha to get the reverse inequality. This proves the theorem.

Geometric meaning. If the trace sum M_n is the alternating trace of a complex concentrated in degree d, epsilon=(-1)^d. A path hypersurface of dimension kd-1 whose relevant compactly supported cohomology is concentrated in that degree has sign (-1)^{kd-1}=-epsilon^k. Multiplication by Q is a Tate twist (-1). But neither dimension alone nor being a hypersurface proves concentration: compact supports may have additional cohomology, Tate/background terms, boundary pieces, or exceptional fibers. F3 assumes the exact spectral statement and therefore does not hide these missing steps.

## F4. Corrected-trace version and exact error budget

Replace (S2) by q^n N_{k,n}=-epsilon^k sum_beta beta^n+E_{k,n}. Suppose for k in an unbounded K there are constants C_k>0, A_k>=0 and real eta_k with eta_k/k -> 0 such that
|E_{k,n}| <= C_k n^{A_k} q^{n(k(a+d)/2+eta_k)} for all n.
Then the conclusion of F3 remains true.

Proof. Rearranging gives a positive spectral sum equal to epsilon^k(E_{k,n}-R_{k,n}). Its exponential growth is bounded by q^{k(a+d)/2+max(d/2+1,eta_k)}. F2 yields |alpha|<=q^{(a+d)/2+max(d/2+1,eta_k)/k}; take k unbounded. Apply duality as before. This criterion allows removal of known Tate/background terms when this sublinear-in-k error budget holds, or when their spectra can instead be included explicitly in the positive-sign sum. No claim is made that this sufficient error budget is necessary for every other possible proof. Unknown boundary terms cannot be silently discarded.

## F5. Necessary hypotheses and countermodels

(a) Opposite parity: let t_n=1 on F_{q^n}. Then M_n=q^n, A={q}, a=0,d=1; its eigenvalue has modulus q>sqrt(q). The exact identity and Parseval bound F1 hold for all k,n. Therefore these analytic facts alone do not imply the target upper weight; (S2) cannot hold for an unbounded K with the required error budget. This is not a counterexample to F3 or Weil II: the actual cohomology of A^1 is in compact-support degree 2 with weight 2, not middle degree 1.

(b) Virtual cancellation: put an identical one-dimensional Frobenius module with eigenvalue q in cohomological degrees 0 and 1 and zero differential. Its alternating trace is 0 for every n although its eigenvalue has modulus q. The total virtual zeta function is 1. Arbitrarily good bounds on virtual traces do not bound individual cohomology without non-cancellation. This is an actual Weil complex on Spec F_q: Q_l(-1) direct sum Q_l(-1)[-1].

(c) Duality: a one-dimensional module with eigenvalue 1 satisfies the upper bound of weight 1 over F_q but is not pure of weight 1. Thus upper bounds alone do not imply exact weights. (Its natural weight is 0.)

(d) All extensions: A={R,-R} has trace zero at n=1 and indeed every odd n, for arbitrarily large R. Bounds on only those n cannot control eigenvalues. Bounds for every n are sufficient for F2 as used. The odd-n counterexample shows that an arbitrary infinite subsequence is insufficient; no weaker subsequence criterion is asserted here.

(e) Parseval is not a positive-operator theorem: over F_3, t=1, the normalized Fourier matrix K_1/sqrt(3) is unitary but its diagonal entry at x=1 is exp(2*pi*i/3)/sqrt(3), not real; it is not Hermitian and hence not positive semidefinite. Over F_2 the normalized matrix [[1,1],[1,-1]]/sqrt(2) has eigenvalues +1 and -1. Nonnegative multiplication weights and norm preservation do not identify a positive operator of the kind proposed in the Fable note.

(f) Purity need not imply semisimplicity: the two-dimensional unipotent Frobenius matrix [[1,1],[0,1]] has both eigenvalues of weight zero and traces 2 in every degree n; it is not diagonalizable. It defines a continuous l-adic representation of Gal(Fbar_q/F_q) by projection to Z_l and the corresponding unipotent matrices. Thus spectral purity does not itself establish arithmetic Frobenius semisimplicity or a decomposition theorem. Geometric semisimplicity theorems require their own hypotheses and must be distinguished.

## Remaining principal gate

For each specific nonstandard basis coefficient one must construct trace systems t_n and identify the desired coefficient with an effective graded multiplicity. To apply F3/F4, prove (S1), (S2) for unbounded k (or its corrected form), all-embedding trace estimates, and duality of the correct weight. For GCT VIII no finite-field realization, Frobenius, weight normalization, or concentration theorem is specified in the supplied source. F3 establishes a precisely stated analytic reduction, not the missing realization.

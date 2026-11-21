# Root proof notebook — TRACE_DET_20261121

Model: GPT-6 Astra Pro (developer model label); effort not exposed. Date 2026-11-21 Europe/Berlin. These are derivations for the paper, not claims of novelty in the literature.

## B-01: concrete zero-based B, both kernels

Define xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2 and Xi(z)=xi(1/2+iz). Xi is even, entire of order one, and Xi(0) is nonzero. With one representative gamma_j from every pair of zeros {gamma,-gamma}, counting multiplicities, put b_j=gamma_j^-2. The zero count N(T)=O(T log T) implies sum_j |gamma_j|^-2<infinity (dyadic grouping gives sum O(m/2^m)). H=ell²(J), B e_j=b_j e_j, kernel K(j,k)=delta_jk b_j for counting measure. Singular values are |b_j|, so B is normal trace class.

The even Taylor series defines G(w)=Xi(sqrt w)/Xi(0) without a branch. Its maximal modulus satisfies M_G(R)=M_Xi(sqrt R)/|Xi(0)|, so its order is 1/2. Hadamard factorization at order<1 gives G(w)=product_j(1-w/gamma_j²), normalized by G(0)=1. This is det(I-wB).

On L²(0,1), choose phi_j(x)=sqrt2 sin(pi j x), transfer B by this orthonormal basis. Its continuous kernel is K_B(x,y)=2 sum_j gamma_j^-2 sin(pi j x)sin(pi j y); absolute uniform convergence follows from sum|b_j|<infinity. Termwise integration first on finite linear combinations, then norm density, proves the claimed integral operator. This kernel is an explicit spectral construction, depending on the zeros. It is neither found in Grothendieck's archive nor an arithmetic kernel known before the zeros.

For this B, positivity is equivalent to every b_j being real positive. Since gamma_j≠0, gamma_j^-2>0 iff gamma_j is nonzero real. Thus B>=0 iff RH. Under the task's cited Alpöge theorem, this particular B is positive. In fact its quadratic form is strictly positive on every nonzero vector, but 0 lies in its spectrum, so there is no positive uniform lower bound. The equivalence does not extend to arbitrary nonnormal determinant realizations.

## B-02: no trace-class Xi in its unsquared variable

If Xi(t)=c det(I+(t-a)T), c≠0 and T trace class, the zero theorem with algebraic multiplicities gives zeros t_j=a-1/lambda_j for nonzero eigenvalues lambda_j, and sum |lambda_j|<infinity. Thus sum |t_j-a|^-1<infinity. The nontrivial zeta zero count N(T)~(T/(2pi))log T and |Im gamma|<1/2 imply divergence of sum |gamma-a|^-1 for every fixed a, for example by partial summation, or using disjoint dyadic annuli whose reciprocal contribution is bounded below by a constant times the annulus index. Contradiction. This is the checked SA23 section4.1(1) corollary; it does not exclude regularized determinants or unbounded operators.

## B-03: Li polynomial trace after pairing

For every integer n>=1, let C=B(I+B/4)^-1. The inverse exists: eigenvalue -4 for B would give gamma²=-1/4, hence a xi zero at s=0 or1, impossible; 0 is the only accumulation point of B's spectrum. C is trace class. Its eigenvalues are x_j=1/(gamma_j²+1/4)=1/[rho_j(1-rho_j)]. Let P_n(x)=2-2 T_n(1-x/2) for the Chebyshev polynomial T_n. P_n(0)=0, so P_n(C) is trace class; this means the one polynomial P_n(C), not two separately traceable multiples of the identity.

Write a=1-1/rho. The reflected zero 1-rho gives a^-1; a+a^-1=2-1/[rho(1-rho)]=2-x. The recurrence defining Chebyshev polynomials yields a^n+a^-n=2T_n((a+a^-1)/2). Thus the reflected pair contributes 2-a^n-a^-n=P_n(x) to Li's sum. The paired series converges absolutely because P_n(x)=O_n(x) as x->0 and sum|x_j|<infinity. Therefore lambda_n=Tr P_n(C), for the usual symmetric zero summation. Under RH, 0<x_j<4, and 1-x_j/2 lies in(-1,1), hence P_n(x_j)>=0. There are arbitrarily large ordinates, thus arbitrarily small positive x_j; since P_n'(0)=n²>0, at least one (indeed infinitely many) is strictly positive. Therefore lambda_n>0. This refines the heading in SA23 section4.1(4) but preserves its correct obstruction to an S1 operator with eigenvalues 1/rho.

## TOY-01: prime/finite-field statement

Let k>=2, t>=0 on F_q, M=sum t, and Q=sum_{i=1}^{k-1}x_i x_{i+1}. Define N_k=sum_{Q(x)=0} product_i t(x_i) and R_k=qN_k-M^k. A fixed nontrivial additive character psi gives q 1_{Q=0}=sum_{h in F_q}psi(hQ). For h!=0, K_h(x,y)=psi(hxy) has K_h K_h*=q I by character orthogonality. With D_t=diag t, the corresponding path sum is <t,K_h D_t K_h ... D_t K_h t>, k-1 kernels and k-2 multipliers, with the standard inner product (conjugate-linear in its first input; t is real). Its absolute value is at most ||t||²_2 q^((k-1)/2)||t||_infinity^(k-2). Summing over q-1 nonzero h proves the requested bound in counting norms. The zero function is trivial; the k=2 multiplier product is empty and its norm1. k=1 is not covered: q=2,t=(2,1) gives R=3 but displayed claimed bound5/2.

For Z/q with arbitrary integer q>=2, set d_h=gcd(h,q). Direct summation gives (K_h K_h*)_{x,x'}=q when x≡x' mod(q/d_h), else0. Its blocks are q times all-ones d_h-by-d_h matrices, so ||K_h||=sqrt(q d_h). Consequently the always-valid bound is q^((k-1)/2)||t||²_2||t||_infinity^(k-2) sum_{h=1}^{q-1}d_h^((k-1)/2). For q4,t1,k3 there are N3=32 solutions, R=4*32-4³=64>48 claimed. A counting derivation: for x2 odd there are4 choices of(x1,x3), for x2=2 there are8, for x2=0 there are16, total4+4+8+16=32. The source Fable itself says q prime; only the prompt's shorthand could suggest composite moduli.

## TOY-02: positivity of coefficients insufficient

For T=diag(1,-1/2), Tr T^n=1+(-1/2)^n>0 for every n>=1, but T has a negative eigenvalue. Thus even nonnegative trace powers are insufficient to force a positive operator, a fortiori nonnegative counting coefficients or Pringsheim's positive-axis singularity cannot do so. The determinant has a negative zero at w=-2. This directly refutes the inference suggested by Fable from scalar nonnegative N_k alone. Additional cohomological degree/weight information may prevent cancellations in a specific zeta expression; it is not supplied by coefficient positivity.

# Independent proof check: a concrete Weil class of exact complex complexity 16

Date: 2026-11-21. Checker: GPT-6 Astra Pro, inherited effort; run GHOSTS; agent /root/bounded_specialization. The parent and /root/prime_arithmetic supplied the candidate and its intended proof. I independently reconstructed the argument below. This is an independent re-proof in ordinary mathematics, not a formal certificate.

## Data

Let omega=e^{2 pi i/3}, E=C/(Z+Z omega), B=E^2, A=B x B. Let theta_i be the degree-one principal divisor class on the i-th factor and theta=sum_{i=1}^4 theta_i. Give K=Q(omega) the Weil-type action eta(k)=diag(k,k,bar k,bar k). Put

Gamma_a={(x,y,ax,ay): x,y in E},

t_star=[Gamma_1]+[Gamma_{-1}]-[Gamma_omega]-[Gamma_{-omega}].

Complexity means min max(N,deg_theta Z^+,deg_theta Z^-), with N a positive integer, Z^± effective integral surface cycles, and [Z^+]-[Z^-]=N t_star in rational Betti H^4(A,Q(2)). Here deg_theta V=theta^2[V], with no factorial division.

## Check 1: t_star is a nonzero Weil class

View Gamma_a as a graph correspondence B -> B. Adding Gamma_a and Gamma_{-a} cancels the odd-degree Kunneth correspondence components, since [-1]^* acts by (-1)^j on H^j(B). In the difference between the sums for a=1 and a=omega, the H^0 and H^4 components cancel: all maps are automorphisms of degree one. On H^2(B,C), the scalar map [omega] acts by omega^2 on H^{2,0}, by 1 on H^{1,1}, and by bar(omega)^2 on H^{0,2}. Hence the difference also has no H^{1,1} x H^{1,1} component. Its only components are in

H^{2,0}(B) tensor H^{0,2}(B) plus H^{0,2}(B) tensor H^{2,0}(B).

For the specified K action, the sigma-eigenspace of H^1(A,C) is H^{1,0}(B_first) plus H^{0,1}(B_second). Its fourth exterior power is the first displayed line; the conjugate K eigenspace gives the other. Their sum is precisely the complexification of the rational Weil space wedge_K^4 H^1(A,Q). Therefore t_star is a rational Weil class. Nonvanishing follows quantitatively below.

## Check 2: period normalization

Choose the holomorphic one-form alpha on E with (i/2) integral_E alpha wedge bar(alpha)=1. Use alpha_i on each factor, and define

Psi=alpha_1 wedge alpha_2 wedge bar(alpha_3) wedge bar(alpha_4),

z(V)=(1/4) integral_V Psi,

with the integral interpreted on a resolution when needed. If Omega=alpha_1 wedge alpha_2 on B, then integral_B Omega wedge bar(Omega)=4. Indeed moving bar(alpha_1) past alpha_2 introduces a minus sign, while each integral alpha_i wedge bar(alpha_i)=-2i, so the result is -(-2i)^2=4.

On Gamma_a one has alpha_3=a alpha_1 and alpha_4=a alpha_2. Hence z(Gamma_a)=bar(a)^2. Since bar(omega)^2=omega and (-a)^2=a^2,

z(t_star)=2-2omega=2(1-omega),

whose modulus is 2sqrt(3). This also proves t_star is nonzero.

## Check 3: degree of each graph

Write lambda=theta_1+theta_2 on B, so lambda^2=2. For a in {1,-1,omega,-omega}, the automorphism [a] preserves lambda. Thus theta restricts to 2lambda on Gamma_a and

deg_theta Gamma_a=(2lambda)^2=8.

The displayed cycle for t_star has positive and negative numerator degrees 16, with N=1. Therefore c(t_star)<=16.

## Check 4: bound on an arbitrary irreducible surface

Let V be any irreducible surface in A and let nu:S->V be a smooth projective resolution. Compose nu with the two projections to B, giving f,g:S->B. Set P=f^*lambda, Q=g^*lambda and

a=P^2/2, b=Q^2/2, c=P.Q.

Both P,Q are nef. By the projection formula, a is the degree of f if f is dominant and is zero otherwise; the same holds for b. Consequently a,b are nonnegative integers and c is a nonnegative integer. Furthermore

deg_theta V=(P+Q)^2=2(a+b+c).

In particular EVERY irreducible surface, and hence every effective integral surface cycle, has even theta-degree.

Let u=f^*Omega and v=g^*Omega. These are holomorphic two-forms on S and

integral_S u wedge bar(u)=4a,
integral_S v wedge bar(v)=4b.

The positive Hermitian pairing (u,v) -> integral_S u wedge bar(v) on holomorphic two-forms satisfies Cauchy--Schwarz. It follows that

|z(V)| <= sqrt(ab).

If z(V) is nonzero, a,b are positive integers. The Hodge index theorem for the nef classes P,Q gives c^2>=P^2 Q^2=4ab, hence c>=2sqrt(ab). To obtain this familiar nef form, first replace P,Q by P+epsilon H,Q+epsilon H for a fixed ample H, apply the Hodge-index signature inequality in the positive cone, and let epsilon decrease to zero. Standard source for the surface Hodge index theorem: Hartshorne, *Algebraic Geometry*, Chapter V, Theorem 1.9; also Mumford's author-hosted *Algebraic Geometry II*, discussion of the Hodge index theorem, p.355. These background theorems are used, not re-proved here.

Thus any nonzero-period irreducible component has degree at least 2(1+1+2)=8.

If its degree is at most14, then a+b+c<=7. Were ab>=3, one would have a+b>=4 and c>=ceil(2sqrt(3))=4: when one of a,b equals1 the other is at least3, and otherwise both are at least2. This contradicts a+b+c<=7. Therefore ab<=2 and |z(V)|<=sqrt(2).

## Check 5: all effective sums and all multipliers

Suppose an effective integral cycle Z has degree at most14. It contains at most one irreducible component with nonzero period, since each such component has degree at least8. Its multiplicity is necessarily1, because multiplicity2 would already give degree at least16. All remaining components have zero period. Consequently

|z(Z)|<=sqrt(2).

If effective integral cycles Z^+,Z^- of degrees at most14 represented N t_star for any positive integer N, then

2N sqrt(3)=|z(Nt_star)|=|z(Z^+)-z(Z^-)| <=2sqrt(2),

an impossibility. Since all these degrees are even, bounds D=15 and D=14 are identical. Therefore no representation with complexity below16 exists, regardless of multiplier N. Combined with Check3,

c(t_star)=16.

## Limits checked

This computes one explicitly normalized class on one explicitly polarized CM product. It does not compute the unspecified Weil class on every T5 Hecke translate. It proves the characteristic-zero minimum exactly. At finite primes, the same graph expression gives the upper bound16 whenever these data have good reduction; a lower bound at every individual prime is not supplied by this complex period argument. B03 in bounded_specialization.md proves equality16 outside a finite set of primes, but does not list that exceptional set. It is invalid to reuse the archimedean holomorphic-form Cauchy--Schwarz proof in characteristic p without a replacement argument.

The principal product polarization is only ample. To apply B01, select a fixed very ample power L^m for constructing Hilbert parameter spaces and retain the original theta-degree in the definition. For surfaces deg_{L^m}=m^2 deg_L, so the exact original threshold16 is unchanged.

## Check event

statement_id	date	who	type	outcome
TSTAR-EXACT16	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	independent re-proof	Reconstructed Weil-space membership, period normalization, graph degrees, arbitrary surface inequality, integer and multiplicity cases, and exclusion of every positive multiplier; c=16 proved over C; no assertion of exact finite-prime values beyond eventual constancy

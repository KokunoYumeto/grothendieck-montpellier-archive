# Candidate bridge: finite-level cup surjectivity detects every companion pole

Researcher `/root/tripod_integral`, GPT-6 Astra Pro, 21 November 2026. Effort not exposed. This is a complete proof of the cup/extension comparison under the explicit hypotheses below. The main finite-level-surjectivity application passed the independent whole-proof audit in `work/cup_ext_archive_audit.md`; its two formulation refinements have been incorporated. It is not by itself a promoted non-Vandiver kernel theorem. The passage from the commensurable rational module bases to the full Magnus pole proof is a separate task owned by `/root/archive_kummer`.

## 1. Exact algebraic hypotheses

Let p be odd, P=H semidirect Gamma, Gamma=<gamma> isomorphic to Zp, and let c be a commuting involution on P fixing gamma. Assume H is free pro-p. Set M=H_ab, U=Mminus and T=Mplus. Assume:

1. T is finite free over Zp, while U is a finitely generated Lambda=Zp[[Gamma]] module with U[1/p] free of finite rank over R=Lambda[1/p]. In the later pole application there is a commuting prime-to-p Delta action, and U[1/p] has rank one in each odd Delta character; the extension/cup lemma itself only needs finite rank.
2. Each relevant even character component T_e[1/p] is cyclic over R, with monic characteristic/minimal polynomial q_e(z) for gamma.
3. The coefficient character chi has chi(gamma)=u in 1+pZp and chi(c)=−1, and H acts trivially on its Tate twists.
4. At every finite cyclotomic level P_n=H semidirect <gamma^(p^n)>, the even part of H2(P_n,Z/p^n(2)) is spanned by cups of c-even Kummer/unit H1 classes with Z/p^n(1) coefficients. The same argument applies on a cofinal diagonal of level and coefficient indices. Only this precise finite-level integral-surjectivity hypothesis is used here.

The conclusion is that the actual class-two companion numerators C_(e;a,b) cannot all vanish on any divisor (1+T1)(1+T2)=alpha, for any root alpha of q_e. This includes repeated roots.

This statement identifies an actual cup map and an actual extension class. An equality of characteristic ideals alone would not prove it.

## 2. The source extension represented by C

For p odd, the class-two quotient H/Gamma3(H) has an integral Lie structure: the BCH operation uses only 1/2, a Zp unit. Its central degree-two module is the completed exterior square of M. Quotient by all central brackets containing a T input. Denote the resulting Lie module by L. Its central kernel over M is

    N=completed exterior-square over Zp of U.

Complex conjugation acts by +1 on N. Thus the minus part of L maps isomorphically to U; this gives a canonical continuous Gamma-equivariant odd section. The plus part E of L is an extension of compact Lambda modules

    0 -> N -> E -> T -> 0.                                  (E1)

Its class lies in the appropriate continuous Ext1. Choosing a cyclic rational generator v of T_e and a lift y in the same character component of E[1/p] (using the prime-to-p character projector), the relation q_e(gamma)v=0 gives

    q_e(gamma)y=C_e in N[1/p].                              (E2)

This is exactly the odd–odd quadratic part of the companion error used in the pole proof. Indeed all even–even and even–odd brackets have been killed, so the ordered companion product becomes its additive characteristic-polynomial expression. An element in the derived subgroup has the same degree-two logarithmic and Magnus coefficient. The ordinary alternating tensor coordinates of C_e are the functions C_(e;a,b).

The rational Lambda basis of U causes no unbounded-denominator problem in this step. Finite generation gives a common integer b with

    p^b Lambda^r subset U subset p^(−b) Lambda^r

after the chosen R-isomorphism. Completed tensor/exterior squares satisfy corresponding bounds. Consequently N[1/p] is precisely the bounded-denominator alternating two-variable coefficient space in these coordinates.

## 3. A vanished residue splits the alpha-socle

Extend scalars to a finite L/Qp splitting q_e; write O for its integers. Suppose every matching odd-pair numerator vanishes on the alpha divisor. In the bounded coefficient ring, the substitution kernel is the principal ideal

    D_alpha=(1+T1)(1+T2)−alpha.

This follows by the invertible change of variables S=(1+T1)(1+T2)−alpha; alpha−1 is topologically nilpotent. Division preserves bounded denominators. The divisor is symmetric in the two variables, so the quotient of an alternating tensor by it is again alternating. Hence this hypothesis says, in N_L=N tensor O[1/p],

    C_e=(gamma−alpha)A                                     (E3)

for some A in N_L, where gamma acts diagonally on the tensor factors.

Put r_e(z)=q_e(z)/(z−alpha) and w=r_e(gamma)v. Since v is cyclic with minimal polynomial q_e, w is nonzero and spans an alpha-eigenline W in T_L. This remains true when alpha has multiplicity greater than one: W is the socle of its cyclic generalized eigenspace. Equations(E2)–(E3) show

    w_tilde=r_e(gamma)y−A,
    (gamma−alpha)w_tilde=0,

and w_tilde maps to w. Thus (E1) pulls back to a split Gamma-equivariant extension over W. The section has a fixed denominator bound because W is finite dimensional and A is in the bounded coefficient module.

## 4. Explicit cup/extension naturality

This is the substantive comparison. Choose an O-linear splitting s:T_O→E_O[1/p] which restricts to the Gamma-equivariant section over the lattice T_O intersect W. The intersection is saturated, so it extends to an O-basis of the finite free module T_O. Choose lifts for that basis. There is a single integer b such that p^b s(T_O) lies in the integral E_O. This b is independent of the level n and of any cup inputs.

For h in H, write its image in L_O[1/p] as

    x(h)+s(t(h))+z(h),

where x(h) is in U_O, t(h) is in T_O and z(h) is in N_O[1/p]. The odd section is Gamma-equivariant; the even section has defect

    beta_delta(t)=delta s(t)−s(delta t) in N_O[1/p]

for delta in Gamma. Its restriction to W is zero.

Fix a level n. Let f,g be c-even H1(P_n,O/p^n(1)) classes. They may be represented by c-invariant 1-cocycles, by averaging with c (2 is a unit). Such cocycles vanish on gamma^(p^n): c fixes this group element and acts by −1 on the coefficient. On H they are continuous additive maps from U to O/p^n(1), vanish on T, and are Gamma_n-equivariant. Put

    psi=f wedge g:N_O -> O/p^n(2),
    psi([x1,x2])=f(x1)g(x2)−f(x2)g(x1).

This map is Gamma_n-equivariant. Define the following continuous 1-cochain on H:

    k(h)=−p^b f(h)g(h)/2−psi(p^b z(h)).                    (E4)

It is defined integrally because p^b clears the denominator of s and hence of z. In the BCH product, the new central coordinate is z1+z2+[x1,x2]/2. A direct computation therefore gives

    delta k(h1,h2)=p^b f(h1)g(h2).

Indeed the quadratic term contributes p^b(f1g2+f2g1)/2 and the central term contributes p^b(f1g2−f2g1)/2. Thus k trivializes the restriction to H of p^b(f cup g).

The Hochschild–Serre edge of this cup class is the equivariance defect of k, up to the immaterial conventional sign. Since f and g vanish on the chosen Gamma_n section, their cup has zero mixed terms on (gamma_n,h) and (h,gamma_n), so this follows directly by extending k to P_n with value k(h) on h gamma_n^a and taking its coboundary. The quadratic term in(E4) is equivariant. The remaining defect is

    ±psi(p^b beta_delta(t)).                              (E5)

It vanishes on W. Thus under the natural map on the even Hochschild–Serre target induced by restricting Hom(T,−) to W, every p^b multiple of an odd-input cup maps to zero, at every level. This proves the required naturality explicitly, rather than merely naming an Ext duality.

## 5. The inverse-limit target and the repeated-root quotient

Because H is free and Gamma_n has cohomological dimension one, Hochschild–Serre gives

    H2(P_n,O/p^n(2))plus
       = H1(Gamma_n,Hom_cont(T,O/p^n)(2)).                 (E6)

The U part has negative c parity and does not contribute. Put V=Hom_Zp(T,O)(2), with gamma operator B. The right side of(E6) is

    V / (p^n V+(B^(p^n)−1)V).                             (E7)

Corestriction in degree one for the procyclic subgroup sends the normalized generator value to the same value, so the inverse transition maps in(E7) are the natural quotient maps. Since the Gamma action is continuous, some B^(p^a) is congruent to1 modulo p; hence B^(p^n)−1 tends p-adically to0 and these submodules are cofinal with p-power neighborhoods. The inverse limit is V. This also follows from finite cyclic resolutions; it is the explicit source of the dual twist, not just a comparison of characteristic polynomials.

Restriction to W gives a nonzero one-dimensional quotient V_L→W^*(2), on which gamma has eigenvalue u²/alpha and Delta character 2−e. At integral level use the primitive lattice T_O intersect W; the restriction maps on Hom are surjective. Their limits give the displayed quotient after inverting p. These arguments use the eigenline (socle), so they are unchanged by repeated roots.

By(E5), p^b times every cup has zero image in this inverse-limit quotient. The assumed finite-level cup surjectivity would then make p^b times the whole V map to zero. That is impossible: W^*(2) is a nonzero torsionfree L-vector space. This contradiction proves Pole-NV for every root alpha.

To spell out the passage from finite levels, at each n the relevant cup classes span the entire even group in(E6). The same fixed b works for all n. Their restrictions therefore annihilate the projection of p^b V in every finite quotient of the W dual. These quotients form a separated inverse system, so the projection of p^b V itself is zero. No choice of incompatible cup expressions across n is required.

## 6. Relation to the Fukaya–Kato source chain

Fukaya–Kato Theorem7.2.8 and §7.1.10 give exactly finite-level generation by cyclotomic p-unit symbols once their C(h) condition holds. Wake–Wang-Erickson's Greenberg/weak-Gorenstein results are being checked separately to supply this condition and the rational cyclic module hypotheses. The root-of-unity part of the p-unit group has negative c parity and is cyclic; its alternating self-cup is zero for odd p, while mixed cups have negative parity. Thus their even target is already generated by c-even unit cups, as required in hypothesis4. This parity argument does not require Vandiver when it is applied only to the even target.

There is also a checked compatible description using FK Proposition5.2.12: the universal cup of the norm-compatible cyclotomic unit with itself has finite Shapiro components {sigma_a c_n,c_n}. Their clopen-measure coefficients generate the entire target under finite-level symbol surjectivity. Unit-exponent pairs follow by conjugation and ratios, and p-divisible exponents follow by the norm polynomial identity. The proof above avoids needing this additional coefficient-space identification: it uses the explicit finite-level cup cocycle and its bounded-denominator split on W directly.

Primary source locators: FK author version15August2012, https://www.math.ucla.edu/~sharifi/sharificonj.pdf, Proposition5.2.12 pp72–73, §§7.1.8–7.1.10 p86 and Theorem7.2.8 p89; local `work/fukaya_kato_sharificonj.pdf/.txt`. WWE source and module hypotheses remain in the companion arithmetic audit. The algebraic cocycle and inverse-limit arguments above are the new deduction to audit; neither is asserted to be a verbatim theorem from FK.

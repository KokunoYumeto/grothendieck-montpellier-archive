# Independent audit of the finite-level cup / companion-extension bridge

Date: 21 November 2026 UTC. Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; effort setting not exposed.

## Verdict and exact scope

**PASS for the stated main application with finite-level integral cup surjectivity.** The entire current `work/cup_ext_pole_bridge.md` was read and its class-two extension, cochain, repeated-root and inverse-limit arguments independently reconstructed. The result is a conditional algebraic theorem: under its freeness, bounded rational module and cyclic even-component hypotheses, surjectivity of the indicated even finite-level cup maps forces nonvanishing of at least one actual companion numerator on every root divisor. It does not by itself establish the full non-Vandiver kernel theorem; the arithmetic module inputs and the bounded-denominator Magnus change remain separately audited inputs.

There are two harmless formulation requests. The alternative in hypothesis 4 about spanning a fixed multiple of an inverse limit should either be omitted or stated with a precise compatible closed-image condition; the main application uses the stronger, unambiguous finite-level surjectivity hypothesis. The phrase “free of the required finite rank” in hypothesis 1 should specify rank one in each odd character for the subsequent pole argument. Neither qualification affects the bridge as applied below.

This is an independent mathematical paper-proof check, not formal proof execution or a rerun of any arithmetic computation. No assertion of a Greenberg-only kernel theorem is made in this audit.

## CE-EXT: the exact extension and its numerator

Write `M=H_ab=U direct sum T`, with `c=-1` on U and `c=+1` on T. The class-two quotient of a free pro-p group has torsionfree central commutator module equal to the completed exterior square of M. For odd p the class-two logarithm and BCH law use only the unit 1/2. The assertion for an infinite compact free basis follows by the finite continuous quotient construction of its completed tensor and exterior modules.

Quotient the central commutator module by every bracket containing T. The remaining central module is `N=completed wedge^2 U`. Its c action is +1. Consequently the minus eigenspace of the resulting Lie module maps isomorphically to U, and is a canonical Gamma-equivariant section. Its plus eigenspace is exactly the continuous module extension

    0 -> N -> E -> T -> 0.

For a cyclic rational generator v and lift y, `q(gamma)y=C` is the extension's actual companion class. In this quotient brackets involving the even lifts have been killed, so the ordered companion product becomes the additive characteristic-polynomial expression. A derived group element has equal degree-two logarithmic and Magnus coefficients. Thus C is the odd–odd quadratic companion datum used by the pole proof, with no identification merely by characteristic ideals.

A rational Lambda-module isomorphism from U to a free module is bounded in both directions. Indeed U is finitely generated, so fixed powers of p clear the isomorphism and its inverse. On the completed exterior square the corresponding bounds are squared. This identifies `N[1/p]` with bounded-denominator alternating two-variable coefficients. It does not replace this ring by a ring of power series having arbitrarily unbounded denominators.

## CE-SOCLE: zero divisor restriction gives a split eigenline

After a finite splitting-field extension with ring of integers O, every relevant root alpha is congruent to 1 modulo the maximal ideal. The formal coordinate change

    S=(1+T1)(1+T2)-alpha,
    T2=(alpha+S)/(1+T1)-1

is an automorphism of the complete integral power-series ring. Its kernel on setting S=0 is the principal ideal (S), and division by S preserves a common coefficient denominator. Since S is symmetric under interchanging the tensor factors, division of an alternating numerator stays alternating. Equivalently, antisymmetrization using 1/2 recovers the same conclusion.

Therefore vanishing of every ordered odd-pair restriction is exactly `C=(gamma-alpha)A` in the bounded rational completed exterior module. Wrong-character components are identically zero by the already audited weight-grid argument, so “every matching pair” is sufficient here.

Let `r=q/(z-alpha)` and `w=r(gamma)v`. Cyclicity and minimal polynomial q imply `w != 0` and `(gamma-alpha)w=0`. This is true even if alpha is a multiple root: w spans the socle of that cyclic generalized eigenspace. The vector

    r(gamma)y-A

is a Gamma-equivariant lift of w. The eigenline therefore splits after inverting p with one finite denominator bound. No semisimplicity, simple zero, or derivative nonvanishing is used.

## CE-COCHAIN: explicit comparison with the cup map

Let W be this eigenline in `T tensor L`. The lattice `T_O intersect W` is saturated in finite free `T_O` and hence is an O-direct summand. Choose an O-linear section s of E over all T that agrees with the Gamma-equivariant lift on that lattice. A single power `p^b` makes s integral on T. This bound is independent of both the cyclotomic level and the cup inputs. Because N is the kernel of a map to torsionfree T, `p^b` also clears the central coordinate z(h) of every h.

For `delta in Gamma`, write the section defect as

    beta_delta(t)=delta s(t)-s(delta t).

It is zero on W. Choose c-even H1 classes f,g with coefficient `O/p^n(1)`. Averaging cocycles by `(1+c)/2` gives c-invariant representatives. Since c fixes the chosen Gamma section and acts by -1 on the coefficient, these cocycles vanish on the Gamma_n generator, and hence on all Gamma_n by continuity and the cocycle formula. Their restrictions to H are additive maps from U, vanish on T, and are Gamma_n-equivariant.

Put `psi=f wedge g` on N, so `psi([x1,x2])=f(x1)g(x2)-f(x2)g(x1)`. With the canonical odd section and the chosen even section, write the class-two logarithm of h as `x(h)+s(t(h))+z(h)`. The cochain

    k(h)=-p^b f(h)g(h)/2-psi(p^b z(h))

is well-defined and continuous at every level. The BCH central coordinate in a product is `z1+z2+[x1,x2]/2`. The quadratic term of the coboundary therefore contributes

    p^b(f1 g2+f2 g1)/2,

and the central term contributes

    p^b(f1 g2-f2 g1)/2.

Their sum is exactly `p^b f1 g2`, proving `d k=p^b(f cup g)` on H. There is no omitted factor of 2 or p in this calculation.

Extend k to P_n by setting `k(h gamma_n^a)=k(h)`. The original cup has zero mixed terms involving the Gamma_n section, because both f and g vanish there. Its Hochschild–Serre edge is consequently, up to the conventional overall sign, the Gamma-equivariance defect of k. The quadratic term is equivariant and the central defect is

    plus or minus psi(p^b beta_delta(t)).

Depending on the chosen edge convention a conjugation of t appears; this leaves W invariant and does not affect the zero restriction. This expression vanishes on W. Thus the restriction to W of the edge of every `p^b`-multiple of a cup is zero, uniformly at all levels. This is the actual transgression / extension comparison required by the argument.

## CE-LIMIT: Hochschild–Serre, transfer and the exact twist

H is free and Gamma_n is procyclic, so both have p-cohomological dimension one. The degree-two Hochschild–Serre spectral sequence has only its (1,1) term. Taking c-even parts gives

    H2(P_n,O/p^n(2))^+
      = H1(Gamma_n,Hom_cont(T,O/p^n)(2)).

The U contribution is c-odd and disappears. Let `V=Hom_Zp(T,O)(2)`, with gamma operator B. The right side is

    V/(p^n V+(B^(p^n)-1)V).

For a procyclic group, normalized cocycle evaluation on its generator identifies H1 with coinvariants. Corestriction from the index-p subgroup sends that value to the same value in the larger group's coinvariants. A finite cyclic resolution gives the same result: restriction carries the norm factor, while corestriction in degree one is the quotient map. In particular the transition does **not** introduce a factor p. Hochschild–Serre is compatible with this corestriction because the subgroup changes the quotient Gamma and leaves H unchanged.

Continuity of the Gamma action implies that some `B^(p^a)` is congruent to 1 modulo p, and hence `B^(p^n)-1` tends to zero. The denominator submodules above are cofinal with the p-power neighborhoods of V. Their inverse limit is V itself.

Restriction of Hom to the saturated lattice in W is surjective, as is the induced finite coinvariant quotient. After inverting p this produces the nonzero quotient

    V_L -> W^*(2).

If gamma has eigenvalue alpha on W and the even Delta exponent of W is e, the quotient has gamma eigenvalue `u^2/alpha` and Delta exponent `2-e`. This recovers both the inversion and the second Tate twist explicitly. The eigenline/socle construction makes the argument unchanged for repeated roots.

At every n the same `p^b` multiple of every cup projects to zero in the corresponding finite W-dual quotient. Finite-level integral surjectivity therefore makes the image of `p^b V` zero in every such quotient. The quotient inverse system is separated, so its image in `W^*(2)` is zero. That is impossible for a nonzero torsionfree quotient. Compatible choices of cup decompositions are unnecessary: only their span and the one uniform denominator are used.

## CE-ARITH: exact application under the Greenberg source inputs

The bridge requires only the even H2 target, not the whole H2 group. At a finite CM cyclotomic layer, the minus part of the p-unit group is the cyclic roots-of-unity line: a p-unit divided by its complex conjugate is a global unit of absolute value one at every embedding, hence a root of unity. Its self-cup is zero because p is odd. Mixed-parity cups lie in the odd target. Thus generation of the even target by all cyclotomic p-unit symbols implies its generation by c-even unit cups, without using Vandiver to remove any class-group summand from H1.

The primary modular-symbol conclusions are checked separately in `work/greenberg_module_reduction.md`: WWE Corollary 8.1.3 under the one-variable hypothesis that X+ is finite, followed by FK §§7.1.8–7.1.10. The excluded theta components correspond to the zero unramified components X_omega and X_omega^-1. The finite-level generation statement reduces from coefficient p^(n+1) at the (n+1)-st cyclotomic field to p^n if the chosen index convention requires it; Kummer/Picard and the vanishing Brauer term identify that reduction with the ordinary surjection on class-group quotients. A cofinal change of index does not change the inverse-limit argument.

The additional Shapiro coefficient-span paragraph in the candidate is not required by this proof. The verified argument uses the direct finite-level cup calculation and its uniform denominator. No generic-character specialization or equality of characteristic ideals is substituted for that calculation.

## Source and review record

The audited candidate is `work/cup_ext_pole_bridge.md`, in its version read in full on 21 November 2026. Relevant primary sources, previously read in full at the indicated locations, are:

- Fukaya–Kato, author version 15 August 2012, https://www.math.ucla.edu/~sharifi/sharificonj.pdf, §§7.1.8–7.1.10 p86 and Theorem 7.2.8 p89; local `work/fukaya_kato_sharificonj.pdf` and `.txt`.
- Wake–Wang-Erickson, arXiv:1505.05128v3, https://arxiv.org/pdf/1505.05128, §2.1, Corollary 8.1.3 pp48–49 and Theorem 8.2.3 pp50–51; local `work/wake_wang_erickson_pseudo.pdf` and `.txt`.

The class-two cochain and inverse-limit arguments are new deductions in the working proof. They are not represented as verbatim statements in these papers. The final 2024 FK publication was not inspected because its PDF endpoint was blocked; the exact locators above are explicitly to the retrieved 2012 author version.

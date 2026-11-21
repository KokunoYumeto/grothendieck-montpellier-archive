# Independent whole-proof review of THETA3-B15

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, `/root/theta_032`; inherited effort label is not exposed.

**Outcome: pass at the stated scope.** I read the entire B15 section in `paper_B.tex`, reconstructed all elementary deductions, and read the relevant primary theorem statements and their local derivations. This is not a Lean build or a transitive dependency audit.

## Local representations and bilinear orientation

For the rank-three input with Harish-Chandra parameters `(1,0;-1)` at the active place and `(1,0,-1)` at a compact place, subtracting `m0/2=-1` gives `(2,1;0)` or `(2,1,0)`. The maximal zero chain has length one and `(r,s)=(2,0)`. Atobe Definition 1.6 and Theorem 1.7(2), printed pp.4–5, give nonvanishing at that base point. Ichino Theorem 4.1(ii), pp.11–12, deletes the zero and adds `n0/2=-1/2`, giving `(3/2,1/2)`, precisely the compact U(2) character det.

For det inverse, the input parameter is `(-1/2,-3/2)`. At the active place the pair `(m0,n0)=(-3,-2)` gives shifted parameter `(1,0)`, signature `(1,0)`, and output parameter zero. Elsewhere `(-1,2)` gives `(0,-1)`, signature `(0,1)`, and again output zero. The local parity conditions all hold. Ichino section 6.2, p.20, explicitly reconciles the additive-character convention with Atobe. The cases use the unconditional discrete-series part of Atobe.

A quotient of the first oscillator of type `pi tensor det` pairs bilinearly with a function of type det inverse on the middle group. The second oscillator quotient has type `det inverse tensor 1`, which is exactly the required middle output when the top function is trivial. No conjugation has been dropped in passing between the archive bilinear lift and the local Howe quotient convention.

## Global elementary deductions

The positive-definite real component of V rules out every nonzero global isotropic vector. Thus the hyperbolic rank in `Comm.bes` is zero and `m=2n+2` forces m=2. The numerical Ranks inequalities admit k=6,t=13,ord=1; this does not construct all D7/Comm.Is data. Rank-zero JacAt identifies the middle with its definite part. `DefSp.Is.pm` permits either sign at each real place.

The opposite-line equation is solved globally by `Lz=-N(xi0)^(-1)L`, with tau=1. Hence choosing T=Lz gives a coherent definite rank-two terminal space whose sign changes from positive at the active place to negative elsewhere. This does not prescribe or establish finite local theta occurrence.

The character extension proof is valid. C_F embeds properly and hence closed in C_E: injectivity follows from E intersect A_F=F, and properness follows from compact norm-one idele classes and the square on idelic norms. Extend epsilon^d by Pontryagin character extension. The compact real norm-one torus embeds in its adelic quotient with trivial intersection with rational points placed with finite component one. Extending the desired integer weight correction there and composing with z/bar(z) realizes every same-parity infinity type. Continuous characters of finite compact unit groups have open kernels; continuity gives triviality on units outside a finite set. Prescribed finite components are not asserted.

Changing a splitting multiplies by determinant characters on the same pair of groups. It cannot replace an actual U(1,1) factor of A7 by U(2). Restriction to SU removes the determinant character, but does not itself establish occurrence for a different inner form.

## Exact global Rallis criterion

I read GQT section 2.5 (Tamagawa measures), Propositions 11.1–11.2, Theorem 11.4, Proposition 11.6 and Theorem 11.7, printed pp.53–57, including the displayed proofs. For unitary groups d(n)=n. For n=1 or 2 and target m=n+1 anisotropic globally, r=0 and all earlier-tower vanishing hypotheses are vacuous. The special case m=d(n)+1 in Proposition 11.6 preserves the actual real signatures. Thus all-place local occurrence and a holomorphic nonzero completed doubling L-value at 1 are exactly equivalent to nonzero upward global lift. No temperedness hypothesis is needed. The Rallis scalar is [E:F]=2, and the normalized zeta product retains the unramified denominator factors.

Ichino section 8.2, pp.36–37, has a different displayed normalization: for anisotropic source and target, all-place tempered source and holomorphic nonzero partial L-value, dimensions 2 to 3 give L^S(1,Pi,chiV inverse)/(L^S(2,1)L^S(3,epsilon)) times the excluded-place matrix-coefficient integrals. B15 correctly avoids equating character names across conventions. An upward criterion for a chosen source does not by itself prove the reverse first occurrence of a fixed rank-three representation.

## Recovered archive identities

I read the exact Comm, BesAt/JacAt, WeilOK.last/tau, VolLast, lastBi, ClsK.Core/Kval, ClsT.tail, splitFacO and IsDetAt clauses and the full proof bodies of `lastLaw`, `seeLast`, and `GlobalTheory.LastRed.main`. The rank-zero period is an ordinary definite-subgroup integral; compact quotient bounds justify the two Fubini swaps; the tensor identity uses exactly the opposite-line Gram equation; and VolLast is the stated pushforward equality of Haar measures. The displayed untranslated B15 identity is the specialization g=b=bT=1. The arithmetic column equation retains the given abelian_2 functional, covolume, and stabilizer masses. The universal analytic identity does not establish that arithmetic equation or place the original 032 vector in the double-lift image.

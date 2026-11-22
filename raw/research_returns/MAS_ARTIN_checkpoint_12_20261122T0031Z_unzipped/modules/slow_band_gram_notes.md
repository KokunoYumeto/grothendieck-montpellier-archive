# The actual slow-band Gram asymptotic

Date:21 November2026. Complete proofs:slow_band_gram.tex, MA-SB001–003. The abstract all-edge Hankel factorization was proposed by the root agent, independently verified and written here together with the actual weighted Gram argument. The module has548 lines and28 unique equation tags before later editorial changes. Five author/proof events and three questions are saved. Root and PF have each completed an independent full reading of all three proofs and reported a pass, including every cyclic/domain step and both divisor correction signs. The optional bounded-profile approximation wording was clarified without changing the mathematics.

## Outcome

For0<alpha<1/2, polynomial weights=0 and a causal compact smooth testg, the actual global PW trace has a uniform slow-band limit asX,Y→infinity withY/X→0. It is minus the actual upper-half-plane quotient trace, retaining precisely the zeros withbeta<1/2+alpha. The theorem applies to the source's multiplicatively symmetric thin cutoffs and, by GP010, the actual finite-S invariant global PW projector. No generic edge, zero-separation margin, A orM is used.

The quantitative statement is expressed by tails of two fixed actualS1 operators. It gives an error bounded by omega_k(log(X/2))+nu_k(log(X/2)) for1<=Y<=X/2. Those two functions tend to0. No unproved explicit rate for their decay is asserted.

## Why the generic-edge approach was unnecessary

An initial route would have bounded derivatives of the Hardy inner function on a generic zero-avoiding boundary line and used a Schwartz time kernel. The stronger proof avoids all boundary derivatives. On the full line the inner multiplier is unitary and causal, so its block matrix is[[V,H_B],[0,V_-]]. Unitarity givesH_B H_B*=I−VV*=P_K, henceH_B=P_K H_B.

For causal compactk, its cross-half-line Hankel blockH_k has the smooth compact kernelk(x+y), and isS1. The product multiplier therefore has Hankel blockH_Bk=Ck^+P_K H_B+H_k V_-. The first term isS1 because GP009 proves the actual ambientCk^+P_K lift, with the endpoint at0 retained. The second isS1 by the compact-kernel proof. This is an operator factorization before any trace is taken.

The off-diagonal rectangle with input[0,L] and output[R,infinity) translates exactly toP_[R−L,infinity) H_Bk P_[-L,0]. ItsS1 norm is bounded by a fixed left tail ofH_Bk and tends to0 uniformly inL. This uniformity is the main new estimate.

## The weighted Gram algebra

In half-line coordinatesr=x+L,L=logY, the actual metric isR_L=e^(4alpha(L−r)) forr<=L and1 afterwards. The inner range isV L2. Its exact Gram operator isG_L=V* R_L V and the actual weighted projector isV G_L^{-1} V* R_L.

Causality givesP_L V=P_L V P_L. SinceR_L−1 is supported on[0,L], bothG_L−I andD_L=G_L^{-1}−I have that same source support. PositivityG_L>=I gives−I<=D_L<=0, hence||D_L||<=1 independently ofY. This avoids the crude exponentially growing metric-equivalence bound.

The proof does not drop the rightR_L factor from an uncompressed projector. It first establishes trace class of the compact-position convolution products. For a profilephi=1 on[0,R],R>L, it then uses the exact multiplication identityR_L phi=phi+(R_L−1) inside a legitimate cyclic trace. Subtracting the ordinary inner-range trace gives exactly−Tr[D_L V*(1−phi)V Ck]. Only after this isS1 does trace cyclicity insertP_L on the input. The remaining factor is the actual translated Hankel rectangle fromSB001, and its norm is bounded bynu_k(R−L).

The ordinary inner-range term is−Tr(phi Ck P_K), because the identity contribution has diagonal valuek(0)=0. Its error from−tau_+ is bounded byomega_k(R), the fixedS1 tail ofCkP_K. Thus the total error isomega_k(R)+nu_k(R−L).

## Source cutoffs and uniformity

WhenX>=2Y anddelta<=1/(4X), every point of the actual support half-line has multiplicative coordinatet>=1/Y>=2/X. The source's entire lower transition is therefore below the half-line. Its profile is1 throughr=logY+log(X−delta). Substitution gives the stated error bound, and both fixed tail arguments tend toinfinity withX. This proves the actual joint limit on every slow-band path, rather than selecting an adaptive diagonal or exchanging the two iterated limits ofGP009.

The same argument applies to the common fixed annular profileA(t/X)−A(Xt) used byLA014. This permits a direct comparison with the actual repaired local quotient operator, including its finite-prime unitaryD_S and frequency cutoff. The global theorem for source-thin profiles and the paired local theorem for fixed profiles are explicitly distinguished; no arbitrary varying finite-place smoothing estimate is silently asserted.

## What correction remains

WithS containing every prime norm required by the test support, the actual local trace minus its polar term is minus the full Meyer quotient trace. The slow global trace is minus the strict upper-half-plane trace. Their difference is therefore the actual trace difference tau_all−tau_+, subsequently evaluated as the sum overbeta>=upper. The upper boundary is included.

Relative to the actual completed full-strip cutoff trace, the slow-band difference is minus the sum overbeta<=lower. The lower boundary is included. These signs follow from the two actual operator limits and their already proved spectral identifications. Neither formula asserts existence of a zero in the exterior or on a boundary.

The explicit GP008 finite Gram-resolvent expression yields the same slow-band trace after its justified fixed-data regularizer limit. One may select a finite regularizer at each pairX,Y to make its trace error tend to0. Neither resolvent is omitted, and no uniform regularizer rate is claimed.

## Scope and follow-up

The application currently has polynomial weights=0 and0<alpha<1/2. The Hankel lemma itself is abstract and applies to any half-plane inner function with an actual ambientCkP_K S1 lift. PF is applying it to the primitive character ranges ofCGP004, with the conductor-scaled support edge and actual CQ local factors. S5 is investigating positive polynomial weights.

The proof fits the inherited Grothendieck trace-ideal framework through actual bounded/S1 factorizations. It does not supply an arithmetic positivity form or a new zero-location theorem. Primary Beurling/Burnol and coherent Tate–Poisson source locators remain those already audited inGP003/010; no fresh external theorem beyond those inputs is invoked here.

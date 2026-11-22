# Actual proper-curve lifting: further attempted routes and exact boundaries

19 November 2026, 16:27–16:38 UTC. AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, `/root`; effort setting not separately exposed. This is a research note, not a proved numbered conclusion.

## Fixed target

For the explicit tetrahedral strictly henselian normal threefold R, resolution Z and reduced exceptional divisor E, the independently checked FF and TS calculations give the exact obstruction to lifting a specified class on E×P, for a fixed smooth proper curve P. If kappa is the degree−2 dual-complex generator and xi belongs to K2(P)[1/p], its boundary is

    delta(kappa) external xi in K−1(Spec(R)×P)[1/p].

The class lifts as an actual virtual perfect class precisely when this boundary is zero. Every point specialization lifts, because Drinfeld gives K−1(R)=0 and FF.4 then gives K0(Z)[1/p]=K0(E)[1/p]. Nothing here replaces the fixed product by varying pointed etale neighborhoods, formal systems, or connected local Picard schemes.

## Three general shortcuts remain unjustified

Trying to globalize Drinfeld's finite-image idempotent argument across a proper curve introduces a finite-projective factorization problem. Finiteness of global endomorphisms over a proper base does not itself provide a global vector bundle through which the finite-image error factors, nor the lifting property of Hom from such a bundle. The affine proof has not been globalized by this observation.

A Frobenius power kills a fixed nilpotent obstruction in characteristic p, but a single power that kills every obstruction and then permits a formal object has not been proved. A Serre-vanishing bound for the relevant endomorphism sheaf may grow with its Frobenius pullback. Levelwise virtual-class lifting therefore cannot be substituted for a compatible bounded perfect object, its algebraization, or an actual family.

Weight and etale-realization arguments do not detect an arbitrary divisible K2(k) coefficient. In particular, the explicit proper-curve unramified-symbol construction already shows that a naive constant-weight argument against K2 variation on proper curves is invalid. Spreading the coefficients can introduce variation in the parameter curve itself. No such weight argument is used as an obstruction.

## Relative henselization along the proper curve

We tested the following possible route: henselize B=Spec(R)×P along its closed fibre P, use the dimension-one underlying space to show K−1(Bh)=0, lift to the henselization of Z×P, and algebraize. Each comparison needed here has to be established for actual nonconnective K-theory.

The first proposed Zariski argument was invalid. Devadas's *Henselian schemes in positive characteristic*, arXiv:2212.08644v4, Remark2.1.4, author p.9, explicitly distinguishes henselian pairs from henselian local rings. Its affine henselian localizations are generally larger than ordinary localizations, and its Zariski stalks need not be henselian at their whole maximal ideals. Thus Drinfeld's theorem cannot be applied to those stalks just from the relative henselization construction. An h-Nisnevich approach would still need K-theory descent, the correct stalk-continuity statement and a cohomological-dimension theorem. These were not supplied by the sources opened in this check.

The second proposed shortcut is also absent. We opened Devadas's published *GAGA for Henselian schemes* (2025) and read Theorem4.3.1 and its proof, Corollaries4.3.2–4.3.3, and the precise introduction and Section4.4 qualifications. The theorem algebraizes finitely presented subobjects of an already algebraizable finitely presented sheaf on a proper scheme. The corollary gives an exact fully faithful coherent-sheaf functor with essential image closed under subobjects and quotients. It does not assert essential surjectivity; the introduction expressly leaves the arbitrary positive-characteristic algebraization question unresolved. Accordingly, even a proof of K−1(Bh)=0 would leave the actual K0-class comparison back to Z×P unless the constructed class has an algebraizable presentation.

Fresh primary retrievals: `turn719149856view0`, `turn464094626view1`–`view2`, `turn800087522view0`, and the full foundations PDF `turn800087522view2`, with exact locators in `turn758872196view0`–`view1`. Existing Devadas bibliography entries are reused. Web searches for henselian-pair negative K-theory and rigidity found no directly applicable proper-family theorem; connective finite-coefficient rigidity was not substituted for a rational nonconnective assertion.

The agents are separately testing representatives by actual closed subschemes, where the proved henselian Chow theorem would apply. The existence of representatives with the required perfect K0 class is not assumed. No smaller main-task gate is claimed in this note.

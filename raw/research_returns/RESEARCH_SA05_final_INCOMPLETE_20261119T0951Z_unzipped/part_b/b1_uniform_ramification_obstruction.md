# Fixed-open ramification attack: a two-boundary calculation

Proved scoped method-obstruction calculation, 19 November 2026. No
universal gate movement is claimed. Root and Part D independently read
the complete argument and passed it. This treats an explicitly smooth
normal-crossing pair and does not assume arbitrary opens have such a
compactification.

Let k be finite, ell different from char k, Y=P4_k, and let D1,D2 be
smooth hypersurfaces meeting transversely in a smooth surface S. Put
D=D1 union D2 and U=Y minus D. Assume divisor Tate for S. Use ordinary
rational motivic cohomology on the left of the usual cycle map to
continuous geometric ell-adic cohomology. The exact calculation is

    coker[H_M^4(U,Q(3)) tensor Qell -> H^4(Ubar,Qell(3))^Gamma]
      = im(G) intersect ker(cl_C),

where

    V = CH^1(S)_Q tensor Qell,
    C = (CH^2(D1)_Q direct_sum CH^2(D2)_Q) tensor Qell,
    G: V -> C,       z |-> (i1_* z, -i2_* z),
    cl_C: C -> H^4(D1bar,Qell(2)) direct_sum H^4(D2bar,Qell(2)).

The signs can simultaneously be reversed by choosing the other
Mayer--Vietoris orientation; the kernel and resulting obstruction do not
change. The identification is canonical once that orientation
and the usual cycle maps are fixed.

## Continuous-cohomology calculation

Mayer--Vietoris for supports and purity give the triangle

    RΓ(Sbar,Qell(1))[-4]
      -> RΓ(D1bar,Qell(2))[-2] direct_sum RΓ(D2bar,Qell(2))[-2]
      -> RΓ_Dbar(Ybar,Qell(3)).

For precision, the support triangle follows formally from the ordinary
Mayer--Vietoris triangle for the open cover
(Y minus D1) union (Y minus D2)=Y minus S: compare this triangle with
restriction from Y and take the three mapping cones. This argument
applies to functorial cochain models and also to motivic cohomology.
No descent across a singular closed immersion is being assumed.

Its relevant exact sequence is

    H^1(Sbar,Qell(1))
      -> H^3(D1bar,Qell(2)) direct_sum H^3(D2bar,Qell(2))
      -> H_D^5(Ybar,Qell(3))
      -> H^2(Sbar,Qell(1))
      -> H^4(D1bar,Qell(2)) direct_sum H^4(D2bar,Qell(2)).

The two terms on the left are pure of weight -1; the terms on the right
are pure of weight zero. Thus the kernel of the map from H_D^5 to the
right-hand Gysin kernel has Frob-1 invertible; its invariants and
coinvariants therefore vanish.
Taking Gamma invariants therefore identifies H_D^5 invariants with that
Gysin kernel on invariant subspaces. No general semisimplicity
assumption is needed for this step.

The localization sequence for U gives

    H^4(Ybar,Qell(3)) -> H^4(Ubar,Qell(3))
       -> H_D^5(Ybar,Qell(3)) -> H^5(Ybar,Qell(3))=0.

The first term has weight -2. Its relevant image again has Frob-1
invertible, so taking invariants identifies H^4(Ubar,Qell(3))^Gamma
with H_D^5 invariants. By divisor Tate and the rational Kummer
injectivity for Pic(S), the cycle map

    V -> H^2(Sbar,Qell(1))^Gamma

is an isomorphism. Consequently the continuous target is exactly
ker(cl_C G), inside V.

## Ordinary-motivic calculation

The analogous support triangle from motivic localization and purity has
the exact segment

    H_D^5(Y,Q(3)) -> H_M^2(S,Q(1))
      -> H_M^4(D1,Q(2)) direct_sum H_M^4(D2,Q(2)).

These last three groups are Pic(S)_Q and the two CH^2 groups. Hence the
image of the support group is precisely ker(G). Moreover

    H_M^4(U,Q(3)) -> H_D^5(Y,Q(3)) -> H_M^5(P4,Q(3))=0.

The last vanishing follows from the projective-bundle formula and the
ordinary rational motivic cohomology of finite fields: each summand is
H_M^(5-2r)(k,Q(3-r)), and its degree differs from twice its twist.
Thus the image of H_M^4(U,Q(3)) in Pic(S)_Q is exactly ker(G).
Compatibility of cycle maps with purity and localization proves the
displayed cokernel formula after tensoring with Qell.

## Why this fails to close B1

Tate on S supplies a divisor representative for a continuous invariant
class. It ensures only that its signed Gysin image on the threefold
boundary components is cohomologically zero. Obtaining a motivic class
requires that image to be rationally zero. The obstruction is exactly
the indicated part of the codimension-two Chow-phantom kernel on D1,D2.

Adding a third boundary component can move a divisor class on S into
new pairwise intersections. The triple-intersection differential has
three terms, so killing the old component creates the two new ones;
there is no automatic termination or rational-equivalence certificate.
Finite coefficient solutions with increasingly large boundaries do not
by themselves give one boundary working in every ell-power level.

This is stronger than merely repeating the two abstract limit warnings:
it locates the obstruction for a fixed finite-type open in an ordinary
Chow group. It does not show that arbitrary threefolds reduce to this
particular pair of hypersurfaces, nor that the obstruction vanishes.
Neither a new test-class reduction nor universal gate movement is claimed.

In particular, failure of motivic surjectivity on this fixed U does not
show that a continuous class survives every further shrink. Such a class
could become zero on a smaller open without having had a motivic lift on
the original U. The fixed-open cokernel therefore neither solves nor
refutes the projective-space colimit gate.

## Exact sources and check status

For motivic purity, use Mazza--Voevodsky--Weibel, *Lecture Notes on Motivic
Cohomology* (2006), Theorem15.15, printedp124, and the construction in
Corollary15.13, printedpp123--124. Theorem15.12, printedp123, gives the
projective-bundle formula, and (14.5.1) is the open Mayer--Vietoris
triangle used above. The primary publisher/author PDF is
https://www.claymath.org/library/monographs/cmim02.pdf.
The owner opened and read the statements and complete displayed proofs
of15.2,15.12,15.13 and15.15. This is not a reproof of every earlier input
in that book. The comparison with higher Chow groups is Theorem19.1;
the present proof can equivalently use motivic support complexes
throughout, requiring the classical Chow identification only in degrees
(2,1) and(4,2).

For ell-adic purity, Riou, Astérisque363--364 (2014), ExposéXVI,
Theorem3.1.1, printedp323, applies directly to the regular closed
immersions S->Y and Di->Y. It is stated for finite coefficients with
invertible order; compatible inverse limits and rationalization give the
displayed Qell shifts. Primary PDF:
https://www.numdam.org/item/AST_2014__363-364__301_0.pdf.
This exact statement was reread by the owner and independently by C.
The owner also read the full final reduction in Section3.7, pp339--340,
without claiming to have reopened every cited alteration or logarithmic
resolution input. Only the closed-immersion assertion is used, so no
ample-line-bundle hypothesis from broader trace corollaries is omitted.
As an additional direct source for these smooth pairs, the owner read
Milne's *Lectures on Étale Cohomology*, v2.21 (22March2013),
Theorem16.1 and Corollary16.2, p108, Theorem16.7 and the accompanying
proof explanation/Lemma16.8, pp111--112:
https://www.jmilne.org/math/CourseNotes/LEC.pdf.
That lecture text supplies a proof explanation by local standard pairs,
not a full independent reproving of all SGA foundations.

For the weights, the owner read Deligne's *La conjecture de Weil.II*
(1980), Theorem3.3.1 and its displayed proof, pp204--205, and the whole
Corollary3.3.4--3.3.9 passage, pp206--207. Corollary3.3.9 is the exact
proper-smooth theorem used here. C independently reread that passage.
Primary PDF:
https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf.
Its existing primary extraction was used after the web endpoint
rejected the large file; no new reading of every proof input into
Theorem3.3.1 is claimed.

The ordinary projective-space motivic calculation is the already
verified finite-point/projective-bundle calculation in PartB. The
ordinary cycle map and its Gysin compatibility are the same prescribed
ones used there. The two support triangles commute with that cycle map.

Part D independently read the entire note and verified every shift,
weight, invariant/coinvariant exactness, motivic image and the flat-tensor
quotient calculation. Root independently completed the same written
check at the measured time08:43:03UTC. Those full written checks preceded
these source-locator additions; they are not represented as additional
independent primary-source readings. This remains a method-obstruction
proof note, not a new universal test-class reduction.

An additional primary lead was opened during this interval:
Colliot-Thélène--Kahn, *Cycles de codimension 2 et H3 non ramifié pour les
variétés sur les corps finis*, author PDF
https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/17avrilcorpsfinisCTKahn.pdf.
The extracted statements (1.4), Theorem 2.1, Proposition 3.8 and Theorem
3.12 were inspected, not their full dependency proofs. The last theorem
retains the abelian-type/Tate class hypothesis. Finiteness of a
Qell/Zell invariant or control of CH^2 modulo ell-powers would not by
itself detect a uniquely divisible rational summand. No stronger claim
is used from this partial source reading. A separate search endpoint
https://d-nb.info/1345904630/34 returned a502 error and was not obtained.

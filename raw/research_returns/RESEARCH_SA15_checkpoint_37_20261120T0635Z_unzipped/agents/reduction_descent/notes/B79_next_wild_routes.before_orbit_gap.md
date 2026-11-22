# Separate research notes after B78; no further theorem promoted

These notes were developed during the CP28 canonical freeze. B79 itself has a complete separate proof and certificate; the material below remains exploratory.

## Residual-tame two-slope arithmetic at p=5,e=20

Set N=24,s=120. Under primitive finite norm normalization c is odd, so a two-slope B is odd with 0<B<100 and B=c mod6. The already proved common-wild p² point-field argument appears to extend without p∤e: if one B is prime to5, both are prime and equal. This extension must be written and audited before use as a new theorem.

For residual-tame groups all first-level points are rational over the degree24 good field. Write B=5b, b odd in1,...,19. If one b is prime to5, a primitive point over a residual vector outside both canonical high lines has a common degree25 field, because its coordinate has valuation b/25. The entire first-level translation group occurs. A high-to-low mismatch would require a lower break at once greater than480 (the high side, since alpha>20) and less than480 (the low side, since beta=b<20). Thus the high lines align. For a translation low in both, the prime-coordinate break is24b_prime and the unconditional lower bound gives b_divisible>=b_prime. If both b are prime, equality follows.

Conditional on those arguments, the exact character enumeration leaves only:

- B=(25,75), with high lines exchanged;
- B=(35,75), with high lines aligned;
- B=(55,75), with high lines aligned.

Up to common quadratic twist these are A/B, not A/C. The compatible actual first quotient parameters would be (95,15), (85,45), and (65,45), respectively. In the first pair one quotients high on the first group and the corresponding low line on the second; the raw checker's `high_quotient` field intentionally records both separate high quotients and is not an assertion that those two are compared. These resulting p² comparisons would have to be residual-wild, since their b parameters are prime and unequal and the tame rule would exclude them. No exclusion of these residual-wild pairs is proved here.

Exact exploratory program: `code/explore_first_wild_tame_newton_pairs.py`; output of the same stem with `.output.json`. Actual run 2026-11-19T23:47:42.918222+00:00, 0.000425310994614847 seconds. All66 raw tame-character rows checked; six retained orientations give the three parameter/flag pairs. No failed computation. The finite rows do not instantiate a formal group or establish the conditional arithmetic restrictions.

## The next irreducible wild image

At total wild order p^4, the two congruence-layer dimensions are (1,3) or(2,2). In(1,3), primitive third-level valuation is A=p(p-1), and terminal displacements have valuation q²A. The B56/B57 first-prime-degree argument may apply with b0=(q²-1)A/p, still divisible by N. This must be written with the actual tame action and all break cases before claiming an exclusion.

In(2,2), W1=W2. Every primitive point has a point-field degree divisible by p³, so evaluation of W1 on every nonzero residual vector must have rank2. Hence the common plane has no singular nonzero matrix. Commutator closure then appears to force the plane commutative: a nonabelian two-dimensional Lie algebra has a nonzero commutator E with [H,E]=E; trace(E)=trace(E²)=0 makes E singular for odd p, a contradiction. Thus the plane is a Cartan. If it is normalized but not centralized by residual tame inertia, it splits into scalar and anti-Cartan lines relative to the original residual field. Comparing the fixed first prime-to-p coefficient for an order-p² anti lift g and its last-layer power g^p may exclude this shape. The original-Cartan shape remains a genuine missing case. None of these statements is yet an independently audited new result.

## Self-twist route limitation retained

The A/C special-character relation alone does not give a quadratic self-twist of the actual Tate representation. Even in that constructive subclass, an intertwiner can have square or nonsquare square; residual irreducibility does not force the split case. The simple primitive-orbit argument only handles a split intertwiner, not an arbitrary quadratic self-twist. No A/C exclusion is inferred.

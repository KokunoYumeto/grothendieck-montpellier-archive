# Ordinary alternating k=2 tensor cores — working derivation

Status: author derivation only, not yet frozen or independently reviewed. Paused for parent-priority D-OL14–15 audit, 21 November 2026. This is not an integrated theorem.

Let n≥15. Two rational orthogonal Sn modules restrict irreducibly to An:

* UP = S^(n−2,2), degree a=n(n−3)/2, character f1(f1−3)/2+f2≥−1.
* EX = Λ²Std = S^(n−2,1,1), degree a=(n−1)(n−2)/2, character ((f1−1)(f1−2)−2f2)/2≥−floor((n−1)/2).

Every nonscalar Sn operator has minimum projective support at least n−3 for UP, and n−2 for EX. The transposition attains equality. These statements can be proved directly from the earlier checked UP/EX inequalities: index≥2 in UP.3 gives ≥n−3 for n≥8; UP.4 gives the same for index≥2, while index1 is a transposition and index0 a scalar. For EX, EX.4 handles index≥2 and EX.3 handles every nonidentity target scalar; index1 is again exact. A shorter independent derivation can use the exact pair-orbit formulas and split index1/index2/index≥3. For UP any nonreal target has multiplicity≤a/2, and the −1 eigenspace is bounded by half the dimension n(n−1)/2 of the unordered-pair permutation module. This already proves the required nonidentity-target bound for n≥8. EX uses the previously proved −1 pairing bound floor((n−1)²/4).

Let V=W^⊗t, t≥2, e=a^t, with ordinary core An^t and arbitrary compatible normalizers. Aut(An)=Sn gives every operator as scalar λ times the actual rational tensor-wreath operator T. That rational group meets scalars only in the identity: a scalar centralizes every core factor, so its factor permutation is trivial, and the remaining Sn permutations centralize An and are identity. Thus λ is an actual finite character, and the actual inducing character field F is contained in Q(ζ_M), where μ_M is the scalar image. The original imaginary K is only assumed K⊂F; it is not identified with F.

Trace contraction over factor cycles gives, for every power, tr(T^r)≥−c e, where c=1/a for UP and c=floor((n−1)/2)/a for EX. This is the actual rational T before a scalar is applied. Projective support passes under tensor products by convolution, while a nontrivial factor permutation has the stronger quarter-support bound. Therefore every genuine inertia moves at least μe, with μ=2/n for UP and μ=2/(n−1) for EX.

Root's scalar/conductor argument, frozen051bdda5, can be adapted verbatim once all its premises are rechecked: K≠Qω forces two scalar phases outside μ6. A rational eigenvalue of order outside {1,2,3,4,6} has multiplicity≤e/4. Order4 instead satisfies −ce≤tr(T²)≤e−4m, hence m≤(1+c)e/4. Thus two marked inertias move at least (3−c)e/4.

Actual Shapiro/VHS Hurwitz factorization: multiplicity6 gives D=6+(2−2h)e. With e≥a², h≥2 is impossible, h1 has R≤6 and period rank≤6, and rank9 therefore requires h0, R≥12, D=2e+6. Consequently

    [10μ−(1+c)/2] e ≤ 6.

This excludes 15≤n≤39 for both modules. UP: multiplying the coefficient by a² gives n(n−3)[(40−n)(n−3)−2]/8>6. EX: use c≤1/(n−2), giving lower bound (n−1)(n−2)[(40−n)(n−2)−1]/8>6. The lower bounds are uniformly positive on the stated interval by 40−n≥1. This is new over Qi and strengthens the existing ALT07 gate.

Additional field arithmetic (may be subsumed by root's broader long-shape theorem): conductor8 gives two scalar orders divisible8, so c is replaced by0. UP excludes n≤39, EX n≤40. An odd discriminant prime p≥7, h=p−1, gives marked support (1−1/h)e and necessary [10μ−2/h]e≤6. UP excludes n≤10h−1 and EX n≤10h. The a² comparison follows from concavity of x(10h−x) on the relevant integer interval and (x−1)²≥169 or (n−3)²≥144. No claim is made at the coefficient-zero endpoint. No all-n tensor exclusion or source existence has been derived.

Single tensor factors retain the earlier complete D-EX/D-UP exclusion; this new calculation concerns t≥2. Full proof, exact certificate, source check and peer review remain to be written.

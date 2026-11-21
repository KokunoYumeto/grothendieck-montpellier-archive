# Independent proof review of root findings G-07 and G-08

Date: 2026-11-21T02:07:45+01:00
Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I
Type: targeted proof check by a separate agent; finite exact computations supplement the reading. No external peer review or formal proof is claimed.

## G-08 — PASS

Read the whole statement and proof in `work/root/findings.tex` and reconstructed its key steps independently.

1. Each rooted monomial tree has one vertex for every exponent of total degree at most m and a unique path with the stated monomial label. Reversing the y-tree preserves unique vertex-to-root paths.
2. The connecting edge fixes the bidegree split and every source/sink path uses exactly one bridge. There is no unwanted path multiplicity. The graph is acyclic.
3. The number of vertices is exactly binom(m+a,a)+binom(m+b,b), and the source first/sink last ordering exists.
4. For M=I-A, inverse entry (1,s) is the path polynomial, and the adjugate uses the minor deleting row s,column1 with sign (-1)^(s+1). The stated row-sign correction is correct.
5. Homogenization is the universal polynomial identity ell^B det(M(x/ell,y/ell))=ell^(B-m)q, because q is homogeneous of degree m and the minor has size B. It remains valid over every commutative ring by specialization from the universal integer polynomial ring. Padding adds the required power of ell.
6. For every point of the padded orbit, restriction to k variables has form L^(n-m)q and belongs to Det_n by the explicit matrix. Closedness extends this to the orbit closure. A length-at-most-k highest-weight coordinate polynomial sees only this restriction. This gives the ideal inclusion in the correct direction, hence the stated multiplicity inequality.
7. This is an exclusion of short-row multiplicity obstructions at the displayed padding, not a general complexity separation. No stronger implication was used.

The independent script `check_G08.py` verifies universal symbolic identities for (m,k)=(1,2),(2,2),(2,3), then five exact F_101 evaluations each for (3,4),(4,4),(2,5). All pass. The computation output is `G08_computation_checks.txt`.

## G-07 — PASS on the cited geometric input

Independently opened the primary LLHV v3 PDF and verified Theorem2, Table2, Proposition1.1 and the P20,2=(1/2)D23,14 identity. Thus the source used is the degree 320112 of the prime divisor, not the doubled cycle coefficient.

The affine-cone ideal is prime principal in the polynomial ring. Its generating line is GL4-stable, and the scalar character z^(4D) forces det^D under the positive polynomial-coordinate convention used throughout the root proof. Multiplication by its equation gives the displayed exact sequence. Projection of Det4 onto four-variable forms is equal to that cone: continuity proves one inclusion, and the inclusion of all four-variable linear substitutions together with closedness proves the other. The intersection of ideals is therefore exactly the principal ideal. The length-at-most-four highest-weight space restricts without introducing higher variables, and complete reducibility gives the shifted plethysm formula. The endpoint d=D, lambda=(D^4) has source det^D of multiplicity one, so the deficit is exactly one.

No error or unproved additional step was found in the deduction. The external LLHV theorem is cited and used, not reproved.

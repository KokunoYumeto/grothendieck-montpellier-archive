# Independent audit of the paired arithmetic-corank example

**Date:** 19 November 2026, approximately 07:02 UTC. **Auditor:** Part D agent.

I read the complete `sections/b3_paired_corank.tex` and the complete saved `part_b/output/paired_corank.txt`. This is an audit of the written argument and exact output, not a fresh proof of PARI's descent algorithm.

The example passes. The exact conductors and discriminants put all three elliptic curves over the displayed common base. The rank bounds coincide, and the proof correctly distinguishes PARI's third `ellrank` entry from the entire two-torsion of Sha. More decisively, every basis two-cover returned by `ell2cover` has the rational point (0,1); the recorded rational maps take these to the displayed rational points on the elliptic curves, and the program checks the map identities. The two-descent exact sequence then gives Sha[2]=0. A 2-primary torsion group with no element of order two is zero, so the entire primary Sha assertion follows, without BSD.

For each positive-rank elliptic curve, a non-torsion rational point stays non-torsion over Q2. A nonzero multiple lies in the open formal subgroup on which the logarithm is an isomorphism with 4Z2. Its nonzero logarithm generates a closure of rank one, and the ambient local group has rank one. The rank-zero factor contributes only a finite group. Thus the two products have closure ranks one and two despite having equal dimension, global rank and primary Sha group.

The principal polarizations identify each product with its dual. The other inverted finite primes have only finite 2-primary local contributions, and the real contribution is finite. The already-proved arithmetic corank formula therefore yields coranks one and zero exactly as claimed. This is an explicit failure of rank-only determination, not a new universal-conjecture reduction.

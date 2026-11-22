# MA-PR-013: whole-cluster quotient lower bound

Author: /root/pf26_audit, GPT-6 Astra Pro.  
Written and completely reread: 2026-11-22 UTC.  
Final stable proof: cluster_quotient_cost.tex, 396 lines, MA-PR.175--194.  
Final SHA256: 968ac97978daa5c346d95721da8c683758e2943c36ef17c70d36008b4925dc76.
The original392-line proof had SHA256
c58bc3c3f43e7e9a4e49c16f48649d1f66839506549a5054a259be7964331b44.

## Result and exact norm

Under PR010's no-proper-truncation hypothesis, the measured quantity is the
original canonical cost C_n = ||iota_n R_n|| from the whole Hilbert quotient
to the original full holomorphic quotient J_n. A fully retained cluster of
k zeros, counted with actual multiplicities, in a disk of radius d/2 centered
d inside either edge gives

C_n >= c_s C^(-1) nu_n^(-D) 3^(-k) k^(-s/2) d^((s+1)/2-k).

The ordinary logarithmic block count absorbs the k factors into a fixed
polynomial. This is an intrinsic norm lower bound, rather than a bound on a
chosen scalar interpolation formula.

For a sequence of actual clusters satisfying
(k-(s+1)/2) log(1/d) / log(2+|T|) -> infinity, the costs are superpolynomial.
The original selected-height product ensures that such a cluster eventually
lies in one original block: a boundary passing through its ordinate interval
would force k log(1/d) = O(log(2+|T|)).
PR010 then gives a dense G_delta of tests on the fixed support [1,2] with no
continuous equivariant quotient return.

No arithmetic occurrence of these clusters, failure of polynomial costs for
the actual fixed function, or necessity of PR012's potential condition is
asserted. This is separate from MO033's actual full-matrix obstruction.

## Complete author reading and checks

After writing I read all 392 lines in two untruncated portions and rederived
the proof. It passes.

1. The residue functional Delta_P is well defined on J_n, including repeated
   nodes. M18.7 bounds the entire denominator product on each horizontal side;
   the critical-strip location bounds it on the vertical sides. Its original
   J_n dual norm is polynomial without separation between cluster nodes.
2. On the dense space E, the composite with iota_n R_n equals the integral
   against e^(-ax) K_P(x). The continuous retained jets extend that identity
   to H. The proof does not evaluate a general H Mellin transform on the
   outer contour. Annihilation of J_H identifies its norm exactly with the
   weighted Hilbert dual norm.
3. The inverse Laplace identity gives the one-sided convolution for repeated
   as well as distinct nodes. Plancherel controls arbitrary phases. The
   incomplete-gamma estimate beyond 16k/d leaves a fixed fraction of the
   lower-bounded mass inside that interval. The polynomial weight then
   produces the precise exponent (s+1)/2-k.
4. The left-edge residue change has sign (-1)^(k-1), which disappears in the
   norm. The negative-half weight cancels the corresponding exponent.
5. The small-cluster boundary argument uses the original fixed heights, not
   a newly selected block system. The final residual-test conclusion uses
   the already proved whole fixed-support Baire alternative PR104.

The saved proof has 20 unique equation tags and no carriage returns.
No master build or shared proof file was changed.

## Sources rechecked in this construction

Freshly read MT-M18's definitions, analytic input, entire-transform argument,
selected-height proof and minimum-modulus argument through M18.9 in
sources/RETURN_GRH_NIGHT_checkpoint_07_20261121T0617Z/work/root/block_arithmetic_synthesis.tex.
Freshly reread PR001's actual Hilbert/quotient definitions, PR006's retained
jet and whole-quotient cost definitions, PR010 through its coherent nuclear
construction, and the complete PR012 estimate and single-jet lower-bound
scope. Earlier complete block-synthesis audits remain separately recorded.
The inherited finite-length/nuclear-framework locators are not presented as
fresh primary-source readings here.

## Review state

Author, root and input_audit complete proof readings have passed.
The peer requested one explicit domain justification: first take Re z>2
before interchanging the Laplace integral with the whole outer contour,
then continue the identity to the right of all exponents. This clarification
was applied, and the author, root and peer separately read and passed the
final addition. No displayed equation or estimate changed.
The original full readings and subsequent delta checks remain separately
recorded; no pending proof review is being carried forward.

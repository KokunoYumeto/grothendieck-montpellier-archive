# MA-MO-035: a sufficient depth budget for the actual full matrix

## Exact hypothesis

Every completed zero lies in the closed strip. For each fixed edge rectangle and both dual sectors, let k be total multiplicity, m the total multiplicity exactly on the edge, and d the least positive inward depth (set d=1 if there are no positive-depth factors). Require m<p=(s+1)/2. The cost is1 for k<p, sqrt(1+log(1/d)) for k=p, and d^(−(k−p)) for k>p. Require these costs to grow at most polynomially in height. Distinct boundary zeros still count toward m; individual retention alone is not substituted for this total bound.

## New estimate

The actual reciprocal pole product is the Laplace transform of a convolution of one-sided exponentials. For all positive depths its envelope is e^(−dt)t^(k−1)/(k−1)!. When k>p the weighted square integral is controlled by Gamma(2(k−p))(2d)^(−2(k−p))/((k−1)!)². Gamma log-convexity and the central binomial estimate give a uniform-in-k constant after the powers of2 cancel. At k=p the integral has the separate logarithmic bound; below p no positive depth is needed.

With m>=1 boundary factors, split the convolution. The envelope is bounded by the minimum of t^(k−1)/(k−1)! and t^(m−1)d^(−(k−m))/(m−1)!. Splitting the weighted integral at1/d proves the same cost provided m<p. No exponential damping is assigned to a boundary factor. The unlocalized empty product is never asserted to belong to H^(−s/2).

## Actual operator assembly

The canceled holomorphic factor remains polynomial even with k=O(log height): its O(log height) normalized Blaschke factors cost constants, and fixed-radius Cauchy estimates handle derivatives. Localized reciprocal distributions have a polynomial common norm bound and converge separately in each fixed window. A uniform convergence modulus across all windows is unnecessary: Schwartz decay and the actual compact-distribution Hermite estimate give a summable trace-norm majorant. Dominated summation proves the operator limit.

The boundary distribution is identified with the original wide inverse on each actual smooth source input before using the kernels. The crossed reciprocal remains the dual one. Compatible rows produce the inherited sum norm, and the rational moments and original two source columns retain their existing signs. Full retention follows from m<p and the closed-strip premise, so MO029's actual trace/determinant identities apply with their stated test conditions.

## Scope

This contains MO030, since its k<=M<p makes every cost1. It also permits bounded counts with polynomial inward depth for every s, and some unbounded counts under the explicit depth budget. It is sufficient, not necessary. Large totals of distinct boundary zeros may admit oscillatory improvements not captured here. Failure of the minimum-depth budget does not itself imply an operator obstruction. MO033 is a separate necessary estimate and conditional tight-cluster result. No new arithmetic zero geometry is asserted.

## Author QA

The complete written proof was read after writing, with all normalizations and source limits recomputed. The entire MO030 proof and MT-M18 analytic/selected-height/minimum-modulus subsection were reread at the recorded scope. Small author corrections made epsilon0 explicit, stated the varying-input Schwartz convergence, and repaired a missing TeX backslash; all changed sentences were reread. Independent readings are pending.

Stable author version: 428 lines; SHA256 d773987e9202490726d2059991a4d03afb16af644efd593c5bb14905ad4a253a.

## Final review status

Root and PF complete independent readings passed without mathematical correction. The final change is only the status paragraph; all proof formulas remain unchanged.

Final version: 428 lines; SHA256 708758de634431eb0ad66fb1114892ed288245b1095708b0dc56a1114b555029.

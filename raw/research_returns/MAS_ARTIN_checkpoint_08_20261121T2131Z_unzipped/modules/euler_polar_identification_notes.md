# MO004–005: exact original-domain identification

## Result and normalization

The completed module is `euler_polar_identification.tex`, equations MA-MO.43–68. It treats the rational sector, every finite Euler deletion, and every centered narrow weight 0<a<1/2. It uses the original source cutoff, equal to one at the left end and zero at the right end.

The original integer summation has the polar left tail kappa_S M U(1/2) exp(-x/2), where kappa_S=product_(p in S)(1-1/p). Subtracting that term gives the actual maximal narrow-line multiplier. Thus, on a genuine smooth theta vector y=Zgeom F with MF(1/2)=0, both inverses return the same F and the continued diagonal differs from the original diagonal by exactly +kappa_S M(phi F)(1/2) exp(-x/2). This rank-one comparison is in the ambient smooth-function space, not in H_a.

## The stronger actual raw witness

The universality inputs from MO002 have uniformly bounded inverse norms because their input-window zeta values approximate exp(xi) for |xi|<=1. MO003's explicit Gaussian approximation controls the inverse norm and both relevant graph norms. The source-oriented moment ell(F)=M(phi F)(1/2) is bounded on H_a. A fixed compact correction F_*=exp(-x/2)(eta_left-eta_right) has total moment zero and ell(F_*)=1. Subtracting the bounded coefficient ell(F) F_* therefore kills the second moment without destroying output divergence. Only after this correction is the continued output identified with the literal raw output. All final inputs, inverses and outputs are in E.

No inequality subtracts two separately non-Hilbert raw outputs: the norm estimates occur for the continued Hilbert outputs first. This order is essential.

## Exact source scope

Fresh primary reads cover Meyer's cutoff definitions at lines1398–1413 and1698–1714, and the original full product, inverse, projection maps, Poisson formula and smaller-sum distinction at lines3790–4088. The decisive labels are sec:summation, lem:summation, lem:Hilm_p_embed, eq:Poisson_summation, lem:Poisson_sumpm and eq:global_perturbation, author-manuscript pp39–42. The first diagonal has the sign obtained from the defining matrices, already corrected in MEY003.

The coordinate vectors (y_M,0) are in the source's full smooth product. A general such vector is not in its smaller sum space, whose centered difference is c0 exp(x/2)-c1 exp(-x/2). The theorem therefore rules out the raw first-diagonal extension and a full narrow Hilbert direct-sum matrix agreeing on this coordinate core. It does not exclude cancellation after restriction to that smaller space with some separately justified norm. No all-transport impossibility, unclosability, or new zero-location assertion is made.

## Review record

The entire written module was read after creation by its author. A stray prose plus sign and an escaped set delimiter were corrected, and long definition displays were split. Both mathematical proofs passed the author check. Root and PF were notified that the 429-line module is stable for independent whole-proof reading. PF then independently read the complete 429-line module and passed both proofs, including all constants, actual domains, the three graph convergences and the smaller-sum qualification. Root also completed the whole proof reading and integration at 20:40:53 UTC, with a pass.

The original source nuclear theorem uses centered weight a>1/2 and is unaffected. Existing smoothed RS and PR constructions keep their exact scopes. The inherited cote1 nuclear-trace locators079–080 and111–112 are placement references, not newly re-audited original manuscripts in this module.

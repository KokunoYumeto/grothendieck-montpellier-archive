# MO008: the exact further pole-free restriction

The module is `pole_free_noninvariance.tex`, equations MA-MO.89–99. It uses the actual S={infinity} even additive Schwartz model and the original cutoff v(t)=phi(log|t|), equal to one near zero. The raw matrix acts on a polar-zero theta input by i_plus f -> i_plus Lf, where L=1-v-Fourier v Fourier. Its two additive output polar moments are -ell1(f) and -ell0(f). The component difference is ell1(f) exp(x/2)-ell0(f) exp(-x/2).

The exact source with both original and output polar moments zero is closed of codimension four in even Schwartz, and codimension two within the original polar-zero source. The key new independence is that Lv=v-v²-Fourier(v Fourier v) is outside span{1,v,Fourier v}. On the exterior, a hypothetical relation would be an equality of entire Fourier transforms; inversion forces Fourier v to be constant where v=1, hence identically zero, a contradiction.

The proof constructs an actual input from four even compact bumps supported away from zero. Their moment matrix against 1,v,Fourier v,Lv is invertible after sufficiently small localization at four independent evaluation points. Solving against (0,0,0,1) gives the exact required moments. The first raw output has both polar moments zero. The next has integral -1, so its theta component leaves the inherited narrow Hilbert space.

The intermediate Lf is additive Schwartz but need not be flat at zero. Its theta image lies in E by full Poisson summation, which is all the actual source iteration requires. No claim is made that the centered intermediate preimage belongs to E.

The entire proof and scope received a complete author reading. The prose identification of the component-difference signs was made explicit before peer review. PF subsequently completed the entire written-proof and scope reading and passed all arguments. Root full reading was pending at this update. No new primary-source read is claimed beyond the exact source checks in MO004–007.

This result is a noninvariance theorem, not a one-step norm estimate or a nonclosability theorem for the pole-free restriction. Its boundedness on ordinary additive L2 is unrelated without proof to the actual theta-induced narrow norm. PF is separately investigating the smoothed conditional norm route.

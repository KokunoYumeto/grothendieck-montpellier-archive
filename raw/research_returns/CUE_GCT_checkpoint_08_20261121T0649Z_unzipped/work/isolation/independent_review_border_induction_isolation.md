# Independent whole-proof review: bordered-permanent induction

Status: PASS as an exact conditional reduction, not a proof of its uniform ternary-rank hypothesis.
Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I.
Time: 2026-11-21T04:03:29+00:00.
Reviewed SHA256: `77bc0f27ec3e525d80efd27eb77a69da44b477db85ae6969386baf97fc13347b`.

The complete fragment was read and rederived. The degrees of P, Q, R and the auxiliary u/v derivatives agree with the stated degree-(m+1) column space. The scaling relation has nonzero formal coefficients whenever u or v is nonzero, so it gives the claimed8m+2 upper bound. The nonempty ternary normal-rank open set lifts to the quaternary parameter space and intersects its nonempty maximal-differential-rank open set.

For the actual pencil [[A,epsilon*u],[epsilon*v^T,ell]], the exact permanent expansion has just ell*P+epsilon^2*Q. Varying the actual upper-right entries by ell*h means delta(u)=ell*h/epsilon; its epsilon*ell*DP[h v^T] contribution cancels the variation of ell*P under delta(A)=-epsilon*h v^T. The remaining differential is precisely -epsilon^3*D^2P[h v^T,u v^T]. All parameter variations are linear forms, and the analogous lower-left identity gives the other Hessian columns. Division by epsilon or epsilon^3 is legitimate for the same fixed nonzero epsilon.

The8m+2 normal columns are fixed polynomials lying in every nonzero-epsilon differential image. Their independent restrictions to ell=0, together with the limit ell*T_A, make the combined limit columns independent. Thus one coefficient minor has nonzero constant term and is nonzero for some nonzero epsilon. The exact torus-bound difference is8m+2. No unjustified inference from separately chosen pencils or separately chosen deformations occurs.

No exploratory rank computation was rerun in this review. The all-size normal-rank assertion remains an additional hypothesis; this review does not establish it or claim a historical priority result.

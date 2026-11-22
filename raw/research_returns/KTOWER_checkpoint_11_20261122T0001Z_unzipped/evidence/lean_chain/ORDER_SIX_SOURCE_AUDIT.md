# Order-six source and implication audit

Final mathematical proof: `order_six_reduction.tex`, SHA256 `36da7f893a98bdf2db26fc39a9c90ff78baa241f062bf291c46deb3e2def9b64` (185 lines). The complete final proof was read and passed. Exact primary PDF/text hashes and actual read scopes are in `order_six_review.json`.

The required integer is J=h6/(h2 h3), supplied by the separately whole-checked `KT-SEXTIC-CLASS-PRODUCT`. The precise relative-unit normalization is R6=12 R2 R3 R*/Q, with Q in {1,3,4,12}; the norm-sign adjustment introduces no extra factor. Gras's general conductor bound gives R* >= 3/16 log²((p-20)/4). Louboutin's bound applies to the nonreal even order-six characters and gives |L(1,chi)| <= (log p + 2 + gamma - log(4 pi))/2. These imply the exact, strictly sufficient inequality J < 49p/108 for p >= 2^31. Accepted lower-degree bounds then make h6 a p-unit. Prime-to-p norm/extension gives the requested rational character component, and the carried K17 comparison gives all periodic even weights. Smaller primes use the accepted HHO computation.

The argument uses known primary estimates. It does not rely on an unread Moser statement, does not claim a new sextic class-number theorem, and does not settle the remaining orders 5 or at least 7. No new Lean kernel build or numerical Hecke replay was performed.

The original Moser 1981 paper remains unavailable in full text. Jakubec's introduction corroborates the historical claim, but was not substituted for its proof. Earlier sources cited within the Gras bound remain named published foundations, not newly whole-read proofs.

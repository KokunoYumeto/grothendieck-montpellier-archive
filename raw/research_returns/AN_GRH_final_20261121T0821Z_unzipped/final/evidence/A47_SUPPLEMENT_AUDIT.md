# A47 coarse-bound supplement and bounded117 probe: audit

Date: 2026-11-21. GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

## Full supplement reading

Source `work/row_audit/A47_WEIL_SUPPLEMENT.tex`, SHA256 `8a9d1a26f911864402df4d0e1ae87f7967552f473ebef425ba520a850d84e54f`: author complete reading **PASS**.

The constant-deck and rational-pointing assumptions imply that the cyclic group is a quotient of the rational Jacobian. The source uses the previously checked full Abel-map fundamental-group classification and the Lang quotient; it is not assuming this divisibility for a nonconstant group over the original field.

The actual primitive rational two-primary group has a full cyclotomic algebra action only in this constant-deck setting. Each unramified factor has residue degree ord_n(2). If one component contains an element of maximal order2^a, the cyclic module it generates has annihilator ideal exactly(2^a), hence cardinality2^(a ord_n(2)). This proves the lower order bound used with the abelian-variety Weil upper bound. The primitive dimension is phi(n), obtained from the cyclic conductor decomposition and the quotient genus formula.

The failure of the unrounded bound follows from n<=B² and 2^omega(n)B^r-1>B. I also checked all rounded cases: for q>=8 the permitted power-of-two upper bound is at least q, and 2q-1>B by q-2sqrt(q)-2>0; for q=2,4 the exact starting powers are4,8, giving thresholds7,15 exceeding B. Larger r cannot improve either comparison.

The nonconstant extension uses the exact primitive exponent equality at its own deck field before invoking the algebra action and rational Jacobian quotient. The conclusion concerns the inability of this coarse estimate to certify A47, not the actual size of the exponent and not absence of a successful cover. It is related to A34's existing obstruction and is not counted as a universal supply result.

No new full source reading of Milne is claimed: the exact primary passages are retained from earlier in this run and cited in the supplement. This author proof check is not independent re-proof or formal verification.

## Single requested117 probe

Source `probe_A47_conductor117.py`, SHA256 `76ed3d73f32335d79a2b378fa8426cad65f5cf7755de5981c1ab631a18ef890f`; JSON SHA256 `42a90783abffdcee8c2c684f0e8a6c3e40289d4d728d23290d33d46dd38fbc68`.

The script reuses the retained independent Cantor all-point data and integer/binary polynomial helpers. It freshly forms all117 CRT residues from a9/a13, verifies the deck Frobenius permutation73 on all256 points, and obtains an explicit Bezout identity for L117(1) modulo2 and Phi117. The gcd is one. Thus M117=1 overF256, so this is already covered by A46 and fails the intended role as a positive-exponent example separating A47 from the prior union of criteria. It is not a failed computation: the exact computation succeeded and answered the bounded test negatively. No new Jacobian implementation or further example search is claimed.

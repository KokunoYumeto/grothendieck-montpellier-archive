# P-19 final status

P-19 is proved and fully checked over every algebraically closed field of characteristic zero. The proof is `per7_last_higher.tex`; the self-contained exact checker is `check_per7_last_certificate.py`; the complete reconstructed certificate is `per7_last_certificate.json`.

The checker reads no search output or project module. It covers all1095 torus quotient supports, eliminates971 by saturation and116 by line/overlap conditions, refines the two projective3-space parameter blocks jointly to fixed coordinate lines, and checks degree(2,2) on all8 remaining fixed13-planes. Every final P12 rank130 minor, kernel independence13 minor, and P22 rank79 minor is a unit. The exact closed P22 condition handles possible dimension jumps of P12.

The primary standalone run passed at2026-11-21T04:00:02Z, and pencil independently replayed it at04:01:05Z. Root and pencil both read the whole proof and code. All reported typesetting errors have been corrected. The scope remains characteristic zero because the preceding complete arrangement reduction uses rational linear algebra.

The abandoned bare AB/AC degree111 test is documented separately: all64 candidate pairs gave intersection dimension20, so that condition alone was insufficient. It is not used by P-19.

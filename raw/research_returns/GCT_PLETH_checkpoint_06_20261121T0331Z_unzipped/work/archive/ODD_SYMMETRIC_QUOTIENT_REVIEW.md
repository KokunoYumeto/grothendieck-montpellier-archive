# A-036. Independent complete review of T-042

Reviewer: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.

**Status: PASS.** I read the entire final report work/theta/outer5/q_plus_symmetric_report.md, equations (OS.1)–(OS.20), including the additional propagation maps and the smaller support proof.

## Exact geometry and all endpoints

The partition in (OS.1) has size \(5(d+a+k+1)\), point order \(k\), and first-line gap \(2k+1\). After removing the full determinant, its first-line weight is \(a+2k+1\), and its quotient-flag representation is \(S_{(a,a)}Q^*\). The actual rank-three exterior pairing leaves \(\mathcal O(2k+1)\otimes\operatorname{Sym}^aQ\) and the determinant character \(\epsilon^{d+a}\). The G-015 inverse chart and extension criterion consequently give exactly (OS.3).

The symmetric-quotient sequence is locally split before tensoring with the ideal. It remains exact after that tensor. The scalar \(H^1(\mathcal I^k(2k))\) vanishes for every \(k\): A-029 covers \(k\ge2\), the explicit degree-two evaluation covers \(k=1\), and ordinary projective-space cohomology covers \(k=0\). Thus (OS.5) is an actual short exact sequence, without an exceptional correction. At \(a=0\), its first term is zero and the target is the scalar piece \(C_{1,k}\).

The cubic scalar piece and the previously completely reviewed \(\mathsf B(T)\) resolution give both series in (OS.6), with their sign factors. Substituting them into the actual exact sequence proves (OS.7). The alternative point-jet calculation also agrees with the explicit coordinate/trivialization proof in A-033: every fixed canonical point contributes \(h_\eta(k-1)\), independent of the line twist. All maps and determinant actions in the two derivations agree.

## Independent reconstruction of all constants

My reconstruction uses the presentation series, while the author's certificate uses jets. For each permutation cycle type, I computed
\[
\chi_U(g^r)=\binom{m_1(g^r)}2+m_2(g^r)-m_1(g^r).
\]
Newton identities then give \(\det(1-tg\mid U)\) directly. The reciprocal determinant recurrence and the exact numerator \(e_g-\epsilon_gu_gt+\epsilon_gt^2\) give \(C_{1,g}\); the cubic numerator gives \(C_{0,g}\). The same procedure gives the symmetric powers of \(E\). No point-jet calculation is used in this reconstruction.

I applied the separate step-60 difference operators to these one-variable factors, combined their products according to (OS.5), and took the seven exact character inner products. All 403,200 integers agree entry by entry with the complete table. Every one is nonnegative. All 28 common-denominator assertions hold, with numerator degrees at most 239.

The largest entry is exactly 607840200. The least positive-order coefficient outside \((3,3)\) is 926. The \((3,3)\) coefficient vanishes for every residue and every label, and all other positive-order coefficients are strictly positive.

The report's independent algebraic proof of the \((3,3)\) vanishing is also correct. For a nonidentity permutation, every eigenvalue on \(E\) has multiplicity at most three, so the \(a\)-residue degree is at most two. At the identity, the leading \(a^3\) coefficient is proportional to \(C_{1,k}-C_{0,k}\), whose series is \((3+t)/(1-t)^3\), of \(k\)-degree two. This proves the vanishing without a sampling inference.

## Uniform interpolation, positive polytopes and exact support

The common numerators of degree at most 239 give a polynomial from the first nonnegative quotient value on every residue. For the initial range, each term \(\binom{q-j+3}{3}\), \(0\le j\le3\), is zero also as a polynomial value when \(0\le q<j\). The two-variable Newton identity is therefore valid for all parameters.

Omitting \((3,3)\) leaves at most fifteen difference positions. The polytope has two residue quotient variables, one bounded multiplicity coordinate, and two increasing chains; its variable count is \(3+i+j\le8\). All variables are bounded. Each lattice point is exactly a choice counted by \(c\binom qi\binom pj\), so the tagged disjoint union proves the positive formula. The determinant parity and all \(a=0,k=0\) endpoints are retained.

All 27 zero pairs agree with the independent table reconstruction. The strictly positive first differences exclude any further zeros outside the initial residue square.

The report's additional support propagation maps are valid as actual injections. The invariant nondegenerate quadratic tensor in \(\operatorname{Sym}^2E\) has nonzero image in every \(\operatorname{Sym}^2(E/L)\): membership in \(LE\) would give tensor rank at most two, contradicting rank four. Multiplication on each quotient symmetric algebra is therefore injective. Its fiber rank is constant, so it is a locally split vector-bundle inclusion; tensoring by the ideal preserves it. This proves \(N_{a,k}\hookrightarrow N_{a+2,k}\).

The invariant \(e_2(T)\) is a nonzero quadratic polynomial on \(U\). Its class in the cubic domain is nonzero, and its section lies in \(\mathcal I^2(4)\). Multiplication consequently maps \(N_{a,k}\) to \(N_{a,k+2}\) and is injective because the ideal tensored with a vector bundle is torsion-free on integral projective space. These maps preserve the effective outer parity.

The stated eight-by-eight support check is a subset of the independently verified residue table. Every entry on its rows or columns six and seven is positive. Reducing larger parameters by even steps to those edges and applying the injections proves the same complete support independently of the positive Newton argument.

The executed script is work/archive/check_q_plus_symmetric_by_presentation.py. Its full receipt is work/archive/Q_PLUS_SYMMETRIC_PRESENTATION_RECEIPT.json, including the source-table hash, all orderwise minima and maxima, all rational bounds and every zero pair. The author's evaluator and witness sweeps retain their own check receipts; they are not claimed as independently rerun here.

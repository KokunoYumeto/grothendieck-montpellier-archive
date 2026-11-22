# C.3ae: independent finite-certificate audit

Date: 19 November 2026, tool clock 08:40:13 UTC. Status: **the rank and basepoint-freeness certificates pass**. This is not yet an audit of the full cycle-deformation theorem.

We read both original scripts and their JSON outputs. The selected coefficients occur in trial zero, which already has full rank. Consequently the basepoint script's selection of the first trial agrees with the rank witness; there is no mismatched tuple.

We then wrote and executed a separate checker, `code/audit_quartic_certificates.py`. It reconstructs the dual-multiplication matrix by columns rather than by the original row loop and uses SymPy's `DomainMatrix` over the exact field GF(101). The 64 by 57 matrix has rank 57. The monomial spaces have dimensions 16 in degree three and 19 in degree four in `Q[w0,w1,w2,w3]/(w0^3,w1^3,w2^3,w3^3)`. The entries are the transpose coefficients of multiplication by each of the four specified bilinear sections, tensored with the three-dimensional curve factor, as claimed.

We recomputed the base locus on all twelve charts `w_j=z_k=1`, using **lexicographic** Groebner bases rather than the original grevlex order. Every basis is `[1]` over GF(101). This proves emptiness over the algebraic closure of that field, not merely absence of rational points. The common-zero scheme in `P^3_Z × P^2_Z` is projective over Z. If its generic fiber were nonempty, its closed image would contain the generic point of Spec Z and therefore all of Spec Z. Hence the empty fiber at 101 proves that the characteristic-zero geometric base locus is empty.

Our independent runtime was 4.596638515999075 seconds. Exact outputs are `output/audit_quartic_certificates.json` and `output/audit_quartic_certificates.out`.

The matrix rank certifies only the displayed linear map, and the Groebner computations certify only basepoint freeness. The conormal, Chern-class, parameter-specialization, and ordinary algebraic-equivalence arguments must be checked separately before C.3ae is certified as a theorem.

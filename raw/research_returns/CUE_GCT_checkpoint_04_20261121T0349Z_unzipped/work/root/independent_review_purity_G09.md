# Independent targeted review of G-09

Reviewer: GPT-6 Astra Pro, /root/purity_zero_status; effort not exposed. Run CUE_GCT-20261121-purity.

Read the complete written G-09 statement and proof in work/root/findings.tex after checking the proposed graph independently from the parent description. This is a targeted whole-proof review and finite computational check, not a formal certification or an independent proof of the cited 2017 literature.

## Outcome: PASS

The left spine, outward x-trees, right inward y-trees, and reversed spine form an acyclic graph. Every connecting edge is left-to-right and every source-to-sink path has exactly one such edge. The left path to a designated (q,alpha) is unique: its tree has no return edge to the spine. The right path from (s,beta) is unique. The division e=qh+s gives a one-to-one correspondence between allowable coefficient indices and paths. Intermediate left-spine vertices not at multiples of h have no connecting edges, as the written proof explicitly requires.

The number of left vertices is sum_q binom(m−qh+r,r)+Q(h−1): the extra term counts precisely the nonroot spine vertices. The right sum already includes each root. Total vertices minus one is the cofactor determinant size C_h. A z^m path with its one coefficient edge witnesses size at least m+1, so homogenization has nonnegative exponent. This statement is structural even when the corresponding coefficient is specialized to zero: the fixed universal graph retains the coefficient edge with zero label.

For h=ceil(sqrt(m)), Q≤m/h, the number of summands is at most 2sqrt(m)+2 and the extra spine cost is at most m. Thus C≤(2sqrt(m)+2)binom(m+r,r)+m−1=O_r(m^{r+1/2}) for r≥1. Odd k uses two balanced monomial trees and has exponent r=(k−1)/2. The restriction k≥3 is necessary; the degree lower bound excludes an asserted O(sqrt(m)) bound at k=2.

For arbitrary nonzero padding L over a field, extend L to a coordinate basis. The affine determinant for p=q(1,w) homogenizes to L^C p(w/L)=L^{C−m}q. The coordinate-basis change is legitimate over a field and need not be a global polynomial choice over an arbitrary base ring. The written statement and integral-scope paragraph now respect this distinction. If a restricted padding is zero, n≥C>m makes the restricted padded form zero. The highest-weight coefficient-space argument in G-08 then yields the stated multiplicity inequality; no lower bound for a specific padded permanent is inferred.

## Actual finite checks

Created and ran work/root/check_G09_purity.py. Its graph implementation checks all individual coefficient paths for r=1,2, m=1..5, and every h=1..m+1: 40 parameter triples. All passed the exact monomial/path bijection and the stated vertex count. Four exact homogenized determinant evaluations also passed, including L=0 and L=−1. The output with its real execution timestamp is work/root/G09_purity_computation_results.txt. These are finite checks of implementation and constants; the general argument is the proof above, not extrapolation from the checks.

## Prior theorem found and checked

Boralevi, A., van Doornmalen, J., Draisma, J., Hochstenbach, M. E., & Plestenjak, B. (2017). Uniform determinantal representations. SIAM Journal on Applied Algebra and Geometry, 1(1),415–441. https://doi.org/10.1137/16M1085656

Author-hosted primary PDF: https://hochsten.win.tue.nl/pdf/siag-unidetrep.pdf. Exact locator: Theorem1.3, printed p417; §4 contains the construction/proof. The theorem statement was read: for fixed v≥2, uniform affine representations of polynomials of degree≤m in v variables have minimum size Theta_v(m^{v/2}), with the same lower order for sufficiently general polynomials. Setting v=k−1 gives the exponent in G-09. The prior asymptotic must be cited, and no priority claim should be attached to that exponent. This review does not claim to have read and verified every proof in the 27-page paper. Web retrieval refs: turn861362921view0 (primary PDF), turn861362921view1 (publisher).

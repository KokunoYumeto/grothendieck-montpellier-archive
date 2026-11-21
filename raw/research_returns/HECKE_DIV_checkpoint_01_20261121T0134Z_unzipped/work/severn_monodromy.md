# Independent reconstruction of the G34 boundary data

Run HECKE_DIV_20261121; date 2026-11-21; checker /root/markman, GPT-6 Astra Pro, inherited effort setting not exposed. Source: B. Severn, *Weil classes on every abelian sixfold of Weil type for Q(sqrt(−3))* (Hexagon 2610.00387v2), source `weil-qsqrt3-v1.5.tex`, Section 7 Lemma `lem:cocycle` (source lines 375–415), Section 8.1 (lines 421–435), Appendix A (lines 615–702). Public source: https://hexagonmath.org/api/v1/works/2610.00387v2/source?path=weil-qsqrt3-v1.5.tex . Access succeeded by the Browse source files link, after a direct initial open failed. All arithmetic is exact.

## SM1. Reflections, finite group, and faithfulness

`severn_group.py` starts with the ten printed vectors and applies their rank-one reflection formulas to the orbit of v_2. The orbit closes with precisely 756 vectors. Their K-span has dimension six. Each generator permutes this finite orbit, and the resulting permutation representation is faithful: a matrix fixing every orbit vector fixes their span and therefore is the identity. SymPy's exact Schreier–Sims algorithm returns order 39,191,040.

Irreducibility has an independent elementary proof. The roots span K^6 and the graph joining roots with nonzero Hermitian inner product is connected, both verified exactly. If W is a nontrivial invariant complex subspace, its orthogonal complement is also invariant since the generators are unitary. The one-dimensional negative eigenspace of each reflection must belong either to W or to W-perp. Roots assigned to different summands are orthogonal, contrary to graph connectedness. Thus all roots belong to the same summand, and spanning forces that summand to be the whole space. Hence the complex representation is irreducible.

The six scalar units of Q(omega) all permute the computed orbit, and exact group membership tests put these six permutations in the generated group. By Schur's lemma every central matrix is scalar. A scalar of finite order in Q(omega) is one of these six roots of unity. Thus the centre has order six. This establishes the numerical group invariants without GAP, a reduction modulo seven, or a group database. Calling this representation G34 additionally invokes the usual Shephard–Todd classification; the transfer construction itself can be formulated with this explicit finite group.

## SM2. Parabolic cocycles and the cup-product Gram matrix

`severn_monodromy.py` implements the field K as ordered pairs of Python Fractions, with omega^2+omega+1=0. Its matrix computations use Gaussian elimination in that exact field.

For the twenty-term tuple (s_1,s_1,...,s_10,s_10), write a parabolic cocycle as u_i=lambda_i v_ceil(i/2). The six-by-twenty relation matrix R has ith column Q_i v_ceil(i/2), where Q_i is the prefix product. Its rank is six. The twenty-by-six coboundary matrix C has row 2 conjugate(v_i)^T/<v_i,v_i>, repeated for the two occurrences of each reflection, and has rank six. Both R B=0 and R C=0 are checked, where B is the twenty-by-eight matrix of printed cocycle coefficients. The concatenation [B C] has rank fourteen. Therefore the printed b_1,...,b_8 are a basis of the eight-dimensional quotient ker(R)/im(C), not merely eight putative classes.

For a reflection, one may take the local primitive a_i=u_i/2. Substitution into the source cup-product formula gives the entire eight-by-eight skew-Hermitian matrix S exactly as printed. Skew-Hermitian symmetry is checked separately. This confirms the Gram matrix from the roots and cocycles; it does not assume that matrix as input to the cup calculation.

## SM3. All seventeen logarithms reconstructed

Let [a,b] be one of the printed intervals and c the product of its local monodromy matrices. Let W be the six-by-twenty matrix computing u(gamma_c). If the return power is k and c^k=1, then

 u(gamma_c^k)=(1+c+...+c^(k−1))u(gamma_c).

The pulled-back cocycle differs on indices in [a,b] by

 (1−g_i)u(gamma_c^k).

Thus, in the lambda coordinates, its difference operator is C_[a,b](1+c+...+c^(k−1))W, where C_[a,b] keeps the interval rows of C and sets other rows to zero. The script applies this operator to B and solves uniquely in the fourteen-column basis [B C]. Its first eight coordinates give T−1 on parabolic cohomology.

For fourteen intervals c=1. For the remaining three, c has order two and fails to commute with at least one enclosed local reflection, so the tuple's least return power is two. In every case the reconstructed T−1 squares to zero, so the semisimple order is one and log(T)=T−1. All seventeen reconstructed matrices equal the printed blocks entry by entry. Their K-ranks are

4,1,3,3,2,1,2,1,1,2,4,4,4,1,1,2,1.

All 289 pairwise products N_j N_k vanish. The printed-matrix positivity and Q-span-rank checks are performed independently by the root's `check_severn_printed.py`; this reconstruction supplies the previously separate geometric-data-to-matrices step.

## SM4. The curves form a pants decomposition with zero vertex parabolic cohomology

`severn_pants.py` checks that the seventeen intervals are laminar: any two are nested or disjoint. Appending the twenty singleton leaves and the root interval [1,20] constructs a tree with eighteen trivalent vertices, hence a pants decomposition of the twenty-punctured sphere.

At each proper interval vertex, the monodromies are the products on its two children and the inverse product on the parent. At the root they are the three child products. Exact multiplication verifies that each triple has product one. Every resulting triple is, up to ordering, either (1,1,1) or (s,s,1) with s a reflection. In the first case all parabolic cocycles vanish. In the second case parabolic cocycles are (lambda v,lambda v,0), and all are coboundaries. Therefore every pair of pants has zero parabolic H^1. The script also checks the equivalent dimension formula and obtains zero for all eighteen vertices.

## Scope of certification

These computations establish the explicit finite group, the tuple, the cocycle basis, the Gram matrix, the pants decomposition, and all printed logarithms from the lower-level input data. They support the boundary certificate independently of the downloadable supplementary files. They do not by themselves prove the supplier theorem, Brauer transfer, the algebraicity of determinant classes on cyclic covers, the existence/descent of the family over its Hurwitz component, or the analytic nilpotent-orbit dominance criterion. Those require the separate source/proof audits assigned by the root.

The root script remains a dependency of `severn_monodromy.py` solely for the final comparison to the printed blocks. The reconstructed matrices do not depend on those printed blocks. Include both scripts if packaging the certificate.

## Recorded check events

- SM1: computation or formal certificate (computation only); exact finite orbit, faithful permutation action, exact Schreier–Sims order and scalar membership; passed. Script wall-time about 2.6 seconds in this run.
- SM1: targeted proof check; full reading of finite-orbit faithfulness, connected-root irreducibility, and centre arguments; passed. No formal theorem prover was used.
- SM2: computation or formal certificate (computation only); exact relation/coboundary ranks, basis, Gram matrix; passed. Part of `severn_monodromy.py`, wall-time about 0.6 seconds.
- SM3: independent re-proof plus computation; cocycle identity independently derived to the return-power formula, all quotient matrices recomputed from roots and basis; passed. Full argument read in order after execution.
- SM4: independent re-proof plus computation; laminar tree, trivalent count, all monodromy triples, direct parabolic-cohomology calculation; passed. Script wall-time about 0.6 seconds.

All events: 2026-11-21, /root/markman, GPT-6 Astra Pro; effort setting not exposed; run HECKE_DIV_20261121. Output and script SHA-256 values are recorded separately in `severn_certificate_hashes.tsv`.

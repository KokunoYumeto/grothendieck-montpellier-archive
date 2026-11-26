# Maps from moonshine and the Leech lattice onto the fleet's P vs NP proof graph

By Claude Opus 5.5 at effort high (an agent of the main session 329fb1e6), 23 Nov 2026. These are maps, not
verdicts: each row gives the source statement, the target node(s) in `PROOF_GRAPH.tsv`, the translation, and the work
that would complete the bridge. No map is graded. Running notes and the list of everything read:
`<local>/Documents\agent_notes\maps_moonshine_algebra_NOTES.md`. Scripts:
`<local>/Documents\agent_notes\maps_moonshine_algebra_scripts\`. Companion: `algebra_combinatorics.md`.

**Flags.** [opened] = read at the source for this file, locator given. [computed] = my script, checked by no one
else. [memory] = not checked against a source. "Ours" = a result of our runs, with its locator in our files.
Node statuses are those of the local `PROOF_GRAPH.tsv` (snapshot of 23 Nov); pequalnp.com was not queried.

**Short names of our sources.**
- **D1**: `<local>/Documents\workbench_review_20261112\work\D1_notes.md` (reader D1, Claude Fable 5.2 at effort
  high, 12 Nov), with the S6 workbench lattice files it reads (`es_niemeier_*.tex`, prefixes esn:, esnl:, esrf:, nca:,
  wcl:, d4i:, nus:).
- **S6_05**: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_05_ARITHMETIC_final_20261115T1846Z_unzipped\S6_05_ARITHMETIC\`
  (`S6_05_ARITHMETIC_report.md`, "The lattices"; `results_B.csv`, B.1-B.9). Produced by GPT-6 Astra (ChatGPT Pro
  mode) for prompt S6_05_ARITHMETIC; I read the report and the results table, not the proofs.
- **DICT**: `<local>/Documents\research_maps_20261114\MOONSHINE_DICTIONARY\MOONSHINE_DICTIONARY_20261114.md`
  (Claude Fable 5.2 at effort high, 14 Nov), section 1 rows 1-25.
- **SPLAG**: Conway-Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., the PDF in
  `F:\user\Documents\arxiv_latex\library\moonshine_lattices\`. **Curtis**: R. T. Curtis, *The Art of Working with the
  Mathieu Group M24* (CUP), same folder.

---

## 0. The table of maps, strongest candidate bridges first

| # | Source | Target node(s) | Translation | Work to complete |
|---|---|---|---|---|
| ML-1 | Tetracode C4 = F3-span{(1,1,1,0),(1,2,0,1)}, the glue code C_3 of our N(A5^4 D4) (D1, esn:thm:niemeier); its weights are 0 and 3 only (D1-2's obstruction "no tetracode word of weight 4"); SPLAG Ch. 3 (2.5.1) p. 81-82 [opened] | **L-meta-650** (search, held by us), 608, 612, 647, 667, 680, 686, 450 | Codewords = the 9 points of AG(2,3); (coordinate i, value v) = its 12 lines; "weights 0 and 3" = "two points lie on exactly one line". Adding the 4 parallel-class points and the line at infinity gives PG(2,3), the 650 graph [computed]. The 650 incidence function splits as f_AG(9 points, 12 lines, 36 edges) OR f_inf (16 edges at infinity); 64 = (36+9-1) + 16 + 4 | Exact monotone size of f_AG (target 44 = |E|+tau-1) by SAT; then an additivity step "add one parallel class's point at infinity" in the style of 553/558/559/659 but with shared inputs; a 63-gate witness must break that additivity somewhere |
| ML-2 | Witt-Tits: three points ("Romans") of S(5,8,24) leave PG(2,4); octads of type 2+6 are the hyperovals (hyperconics), 1+7 Baer subplanes, 0+8 sums of two lines (SPLAG Ch. 11 §11 p. 314-315; Curtis §2.6 p. 15-16, §8.1.3: M21 = L3(4)) [opened] | 650/608 at order 4 (new instance), 667-type light inputs at q = 4, **714/715**, 745/766/711/712-type recursions at q = 4, 660/661 analogues, 686, 779 | The Golay code supplies PG(2,4) together with its extremal sets: hyperovals are exactly the maximal arcs of degree 2 (type (0,2)), the equality case of the variance bound in meta.md 5.2. ext_4(6) = 6 = 21 - 6*25/10 [computed]; the one-NOT min-max of 715 at q = 4 is 14 (at W = 8) [computed] | Post "order 4" rows: a 650-type search at 124 gates (|E|+tau-1 = 125); the 715 instance with value 14 (needs only 714/715 + 529 + 669, as 660 = 715 + 529 + 669 + an arc); evaluate 745's recursion G(s,0,21) at q = 4 for s = 1, 2, 3 (the 711/712 shape) |
| ML-3 | Leech roots: the Coxeter diagrams of the first batches of fundamental roots of I_{n,1} are the incidence graph of the Petersen graph (n = 19, 25 roots), Tutte's 8-cage (n = 20, 30), the point-line incidence graph of PG(2,4) (n = 21, 42), the Higman-Sims graph (n = 22, 100), a 4600-vertex graph of Leech vectors (n = 23); SPLAG Ch. 28 p. 551, Table 28.3 [opened]. Tutte's 8-cage is PG(2,4) minus a hyperoval: 15 points off the oval (synthemes) against 15 secants (duads), SPLAG Ch. 23 §4 p. 496-497 [opened] | 602, **608**, 612, 632, 647, 279/285 (subdivisions), 256/620/651/737 (Petersen), 582/621/634 (Heawood = PG(2,2)) | A ladder of C4-free bipartite graphs with large symmetry groups, all from one construction (Vinberg's algorithm with Leech-lattice control vector). Edge function of a Coxeter diagram = "two selected roots are not orthogonal"; maximal independent sets = maximal orthogonal root sets (the 632 partial function). [computed] |E|, tau, |E|+tau-1: subdivided Petersen 30, 10, 39 (max degree 3, girth 10: inside 602's class); Tutte 8-cage 45, 15, 59 (cubic, girth 8: 616 gives n + tau = 45); PG(2,4) 105, 21, 125 | SAT/local search for circuits below |E|+tau-1 on the first two (39 and 59 gates: within the fleet's present search sizes); AND-count (632) values by the census method; for the 647 class our proof (meta.md 5.1) already gives exactness. Lean: the graphs as `Fin` edge lists, as in pg23.py |
| ML-4 | PSL2(p) acting on P^1(F_p), p + 1 = 24, 12, 8, 6, 4 for the umbral A-series (DICT row 4, from Cheng-Duncan-Harvey §2.5; (l-1)(p+1) = 24 [computed there]); M24 ⊃ PSL2(23) on 24 points [memory] | **L-gct-086**, 091, 185, 136 (n = 8), 190, 199 | Rows and columns of n x n matrices indexed by P^1(F_p), n = p+1; perm(J + t) is invariant under S_n x S_n, so G-invariant subspaces are unions of isotypic pieces of C^n ⊗ C^n. On a non-real (complex, not self-dual) irreducible constituent every invariant quadratic form is 0, so S_2 vanishes there automatically: the non-real isotypic pieces are the candidates for symmetric level spaces (this is gct.md 5.1(b), "the whole complex excess is totally non-real", made equivariant). p = 3 is A4 ⊃ Klein four on 4 points, the class Codex bounded (gct.md 5.2) | Character tables of PSL2(p) for p = 5, 7, 11, 23 (and M12, M24) on Mat_{p+1}; list the non-real constituents of the permutation module squared; on each candidate compute S_3, ..., S_n exactly (Q(zeta) arithmetic); record the largest invariant level space per (G, n) against 2n - 3 and the open searches 185/190 |
| ML-5 | Frame shapes and eta products: for a Coxeter frame shape pi = sum a_d [d] the CDH eta quotient has Fricke constant = order of the glue code (D1-9, two-line proof, nus: T_6(W_6 tau) T_6(tau) = 72); M24 cycle shapes give eta products (Mason) [memory] | 089, 119, 120 (rank-one level lines), 110 (block sums), 086 witness families, 204/205 | For x = eigenvalue vector of a permutation of cycle type prod d^{a_d}, sum_k e_k(x) t^k = prod_d (1 - (-t)^d)^{a_d}. By the checked 089, S_k(x y^T) = k! e_k(x) e_k(y), so x y^T is a level line iff the supports of the two coefficient sequences are disjoint above 0. Example at n = 24 [mine]: x = eigenvalues of shape 12^2 (support {0,12,24}), y = the 23rd roots of unity and 0 (support {0,23}) | Enumerate pairs of (generalized) frame shapes of total length n with disjoint e-supports; take block sums (110) and spans; compute the mixed S_k on spans to see which combinations stay level; compare with the F_{q,r} barrier family of gct.md 5.1(c), which is the frame shape [q] |
| ML-6 | Leech lattice mod 2: Lambda/2Lambda has exactly the classes 0, pairs +-x of type 2, pairs of type 3, frames of 48 type-4 vectors (1 + 98280 + 8386560 + 8292375 = 2^24), SPLAG Ch. 10, the theorem before Thm 29, p. 288-289 [opened]; q(x) = (x,x)/2 mod 2 is a quadratic form on F_2^24 [mine] | pcx **065**, 072, 081, 082, 090, 091, 092, 071 (hard link, parked) | The fleet's gadget is IP on 4 bits (a hyperbolic quadratic form on F_2^4); q on Lambda/2Lambda is a nondegenerate quadratic form on F_2^24 with Co_1 symmetry, so it is affinely an IP on 24 bits whose level sets are unions of Co_1-orbits (types). 090 is the 4-bit case of "an affine flat on which a nondegenerate form is constant has at most 2^m points" | State and prove 090/091/092 for IP_{2m} (Lean: the 092 inequality is already the tool); compute the 081/082 pair statistics for IP_{2m} and for q by orbit counting; decide whether a 24-bit gadget changes the n^2 ceiling of 072's walk (the "COVER" core) |
| ML-7 | Our lattice J: J = intersection of three Leech neighbours of N(A5^4 D4), det 81, J^dual/J = F_3^4 with the hyperbolic form q_J = (2/3)(2ad + bc + bd), eight totally isotropic planes in two rulings of four, overlattices six Leech + two A2^12 (D1-1, verified by D1's script; S6_05 B.1, B.2); |Aut J| = 12,597,120, kissing number 23,058 (B.3, B.4); exactly 129 Co0-orbits of totally isotropic planes in Lambda/3Lambda: 106 with an A2^12 extension, 20 more with an A1^24 extension, 3 all-Leech (B.9) [opened: statements] | pcx 092, 090, 091; meta 279/285 (subdivisions), 608; L-lib-118 | (a) Isotropy: B.9 is a complete orbit classification of 2-dimensional totally singular subspaces of a 24-dimensional ternary quadratic space with group Co_0, the ternary relative of the fleet's binary isotropy lemma (092: 2 dim U <= n + rank(B on U)). (b) Geometry: the points and lines of the quadric of q_J form a 4 x 4 grid; its point-line incidence graph is the once-subdivided K_{4,4} (16 + 8 vertices, 32 edges, tau 8, girth 8) [mine] | (a) Formulate 092 over F_3 (symmetric forms, char not 2) and test it on the 129 representatives (all data retained in S6_05 records); (b) a search instance on the subdivided K_{4,4} at 38 gates; 279 covers 2k-fold subdivisions only, so a single subdivision needs its own row |
| ML-8 | The dessin of X0(p): the p + 1 darts permuted by the modular group B = C2 * C3 through PSL2(p) (DICT row 4); spectral gap for congruence quotients (Selberg 3/16) [memory]; our S6_05 A.2: a compact reflection quotient of signature (0;2,2,2,2,2) has lambda_1 > 1/4 by a geometric Cheeger proof (report, "The count") [opened: statement] | pcx 043 (bounded-degree bipartite boundary expanders exist), 046, 049, 065, 072, 071 | Schreier graphs of PSL2(Z) on P^1(F_p) (generators of orders 2 and 3) are the dessins of X0(p): explicit (2,3)-biregular bipartite graphs with p + 1 edges; a uniform spectral gap gives an explicit expander family where 043 has existence only | Transfer the Laplacian gap of X0(p) (or of our reflection quotient) to combinatorial boundary expansion with the parameters 043/046 use; then instantiate 065's lifted system on these graphs (explicit family for 071's searches) |
| ML-9 | Cubic forms of the lattice lane: Albert determinant det(lambda I + E(L X)) = lambda^3 - lambda(X,X) + 2F(X) (D1, triality bridge); Wilson's trilinear form on O^3, full stabilizer A4 x (C7:C3) of order 252 (S6_05 B.7); an E8^3 embedding with value group (1/2)Z (B.8); P(a) = Re(a^3) on D4 has image {n even : 3 ∤ n or 9 | n}, local-global (D1-8) | gct 024, 045, 057, 025, 026 (smooth forms and the cubic target); Line E 130, 148, 155 (sums of cubes) | Each cubic is a candidate "smooth form" G of degree 3 in d variables for 024 ((r-1)(d-1) <= 11 n per border expression of size n) and a candidate target of an affine restriction of perm (025 asks for degree >= k/3 in >= k^2/100 variables) | Compute the singular loci (Jacobian ideals) of F on N ⊗ C (24 variables) and of Wilson's form on O^3 ⊗ C; if smooth, 024 gives n >= 2*23/11; record whether perm_m restricts affinely to them (025 shape). For Line E: P(a) as a sum of cubes of linear forms, against 130/148 |
| ML-10 | Conway-McKay-Trojan: x^24 + x + t has Galois group M24 over F_2(t), x^12 + x + t gives M11 over F_3(t), with the proof by an additive polynomial (DICT row 21; CMT §1 [opened by the dictionary's author]) | meta 664, 683, 684, 685 (additive maps and point counts), the odd-q arc question of meta.md 5.2 (ext_q(W)) | Both sides count points of {x : additive polynomial in a subgroup}: 685 is x^p - m x + k in A (types 0, |A|, p|A|), the fleet's tool for sets of few line-intersection sizes | Read CMT §1-2 for the exact additive polynomial and its root space; test whether its level sets give sets of type (0, |A|, p|A|) in PG(2, 2^k) or PG(2, 3^k) beyond 685, i.e. new lower bounds for ext_q(W) and new 660/661-type instances |
| ML-11 | Golay code membership and the Hamming code: the [24,12,8] code is the kernel of 12 parity checks; the [7,4] Hamming code's weight-3 words are the lines of the Fano plane [memory] | meta 031 (parity exact 4(n-1)), 639 (OR of parities of disjoint blocks), 626, 640 (Fano lines as ORs: joint size 14) | "x is not a codeword" = OR of 12 parities on overlapping supports, the overlapping version of 639; the 7 line-parities of PG(2,2) are the XOR analogue of 640 | Exact joint size of the 7 Fano line-XORs in the fleet's basis (a SAT search the size of 640's); then the overlapping-support form of 639 on the Hamming and Golay check matrices |
| ML-12 | Ogg's theorem: Gamma0(p)+ has genus 0 iff p divides |M| (DICT row 20, TASI (4.8) [opened by the dictionary's author]); our NEG row: the parity of #SAT is a Hasse-Witt scalar of one sparse smooth cubic (HEXAGON_STATUS NEG) | L-alg-001 (value-only evaluators, lib_alg.md 5.4), pcx 024-026 (PC degree toolkit) | Supersingularity is a Hasse-Witt condition; for elliptic curves it is decidable in polynomial time, for NEG's cubic it is ⊕P-hard. The map places a "Hasse-Witt evaluator" as an L-alg-001 candidate class indexed by dimension | Write the candidate in the alg program's format (an evaluator for the Hasse-Witt scalar of hypersurfaces of dimension d); its kill or its success is the NEG statement; nothing posted |

## 1. ML-1 in full: the tetracode is the affine half of the L-meta-650 plane

**Source.** Our N(A5^4 D4) has glue H = {(3u + 2z; y)} with ternary part the tetracode
C_3 = <(1,1,1,0),(1,2,0,1)> (D1, esn:thm:niemeier, l. 264-380). D1-2 proves that the element r fixes no Weyl-vector
Leech neighbour because the tetracode has no word of weight 4 (its weights are 0 and 3). SPLAG Ch. 3 (2.5.1) p. 81-82
[opened]: the [4,2,3] tetracode is MDS, self-dual, automorphism group 2.S4.

**Translation** [computed in `planes_and_graphs.py`].
- Points of AG(2,3) = the 9 codewords c = a(1,1,1,0) + b(1,2,0,1) = (a+b, a+2b, a, b).
- Lines = the 12 pairs (i, v), i = coordinate, v in F_3: line (i,v) = {c : c_i = v}. The four coordinates are the four
  directions of F_3^2 (the functionals a+b, a+2b, a, b), so the lines fall into 4 parallel classes of 3.
- "Every nonzero word has weight 3" = "two distinct codewords agree in exactly one coordinate" = "two points lie on
  exactly one line". The script checks S(2,3,9).
- Add one point at infinity per parallel class (on the 3 lines of that class) and the line at infinity through the four
  new points: 13 points, 13 lines, 52 incidences, PG(2,3).
- The incidence function of L-meta-650 then reads
  f(x, y) = OR over codewords c and coordinates i of (x_c AND y_{i,c_i})
            OR OR over i of [ x_{inf_i} AND (y_{i,0} OR y_{i,1} OR y_{i,2} OR y_inf) ]   (restricted to incidences),
  i.e. f = f_AG OR f_inf with f_AG the AG(2,3) incidence function (21 inputs, 36 edges) and f_inf the 16 incidences at
  infinity.
- Counting: AG(2,3) incidence is bipartite with point side of size 9 and a matching saturating it, so tau = 9 and
  |E| + tau - 1 = 44; the plane adds 16 edges and raises tau by 4: 44 + 16 + 4 = 64 = the 650 threshold + 1.
- Symmetry. The automorphism group 2.S4 of the tetracode, and our GL2(F_3) = Theta(G) acting on the glue
  (esn:thm:glue-gl2), act on AG(2,3) fixing a point and the line at infinity; the full stabilizer of the line at
  infinity in Aut PG(2,3) is AGL(2,3) [memory: order 432]. These act on the decomposition f = f_AG OR f_inf.

**What a witness must do.** By our proof of 647 (meta.md 5.1, Claude Opus 5.5 at effort max, on paper), a circuit
with at most 63 gates must have line-degree >= 2 over each side. In the decomposition above: it must AND two
line-dependent wires; since lines of one parallel class are disjoint, a product (y_{i,v} OR ...) AND (y_{j,w} OR ...)
with i ≠ j has the single affine point c with c_i = v, c_j = w in common to its two lines (MDS: a codeword is
determined by any two of its coordinates, distance 3 = n - k + 1), and with i = j the two lines are disjoint. So the
line-line products that meta.md 5.1 requires can be indexed by pairs of tetracode coordinates and the codeword they
determine [mine; a description, not a proof that only such products occur].

**Work to complete.**
1. Computation: exact least monotone circuit size for f_AG (9 + 12 inputs; target 44); a SAT encoding with the
   2.S4 symmetry broken as pg23.py does for PG(2,3).
2. Computation: whether a minimal circuit for f extends a minimal circuit for f_AG by exactly 20 gates; a negative
   answer locates where a 63-gate circuit would save.
3. Proof step: an additivity lemma for adding a parallel class's point at infinity (shared line inputs, a fresh point
   input), modelled on 553/558/559 (exact additivity with a passenger on fresh inputs) and 659.
4. The MDS remark suggests a pruning rule for the SAT encoding (my heuristic, not proved): a product of two
   line-dependent wires helps only if its operands depend on lines of different parallel classes. Proving or dropping
   it is part of this step.

## 2. ML-2 in full: the Golay code hands the fleet the plane of order 4 and its extremal sets

**Source** [opened]. SPLAG Ch. 11 §11 p. 314-315 (the triad group): with three of the 24 points distinguished, the other
21 are PG(2,4); the octads are of four forms: (3+5) the three Romans and a line; (2+6) two Romans and a six-point oval
(hyperconic); (1+7) one Roman and a Baer subplane PG(2,2); (0+8) the sum of two lines. Curtis §2.6 p. 15-16:
S(2,5,21) ⊂ S(3,6,22) ⊂ S(4,7,23) ⊂ S(5,8,24); §8.1.3: the stabilizer of three points is M21 = L3(4), preserving
S(2,5,21). SPLAG Ch. 23 §4 (p. 496-497): an oval of PG(2,4) labelled by six symbols, its 15 secants by duads, the
15 points off it by synthemes, its 6 axes (external lines) by totals.

**Translation into the NOT ladder (714/715).** meta.md 5.2: with one NOT gate the lower bound is
min over W of max(T1(W), T2(W)), T1(W) = min over (W-1)-sets a of sum over lines of (|line ∩ a| - 1)^+,
T2(W) = q * ext_q(W), ext_q(W) the largest number of lines missed by a W-set. Hyperovals are the maximal arcs of degree
2: every line meets them in 0 or 2 points, the equality case of the variance bound ext_q(W) <= N - W(q+1)^2/(q+W).
[computed] at q = 4: ext_4(5) = ext_4(6) = 6 (= the variance bound at W = 6), ext_4(7) = 4, ext_4(8) = 3, and
min_W max(T1, T2) = 14, attained at W = 8 (T1 = 14, T2 = 12). At q = 3 the same computation gives 6 (W = 5), with the
conic (4-arc) as the extremal set at W = 4 (ext = 3).

**Translation into the order-4 searches.** PG(2,4) incidence: 42 inputs, 105 edges, tau = 21, |E| + tau - 1 = 125
[computed]. The 650 question at order 4 is "a monotone circuit with at most 124 gates". M21 = L3(4) (with the field
automorphism and the duality) acts; the Singer cycle of order 21 with the difference set (0,1,4,14,16) mod 21
(multipliers 1, 2, 4, 8, 11, 16) [computed, `singer.py`] gives the cyclic presentation used for 650 (see
algebra_combinatorics.md AC-2).

**Work to complete.**
1. A row "plane of order 4, one NOT, all 21 line-ORs: at least 14 gates" with proof = 715 + 529 + 669 + the table above
   (exhaustive over C(21, W) sets; Lean by `decide` over Fin 21 is heavy, a certificate of the minimizing sets is
   lighter: for each W, one W-set attaining ext and a proof that every (W-1)-set has F >= T1).
2. The 745/766 recursion at q = 4 (m = N = 21, d = 5, kappa(b) = 4b + 1 by 686): evaluate G(s,0,21) for s = 1, 2, 3,
   as 711/712 do at q = 8.
3. A 650-type search at order 4 (124 gates): only if the order-3 search finds a witness, since the order-4 instance is
   about 2.5 times larger.

## 3. ML-3 in full: the Leech-root graphs as a ladder of girth >= 6 instances

**Source** [opened]. SPLAG Ch. 28 ("Leech roots and Vinberg groups", Borcherds, Conway, Queen), p. 551 and Table 28.3:
for I_{n,1} with n = 19, 20, 21, 22, 23 the first batch of long roots has 25, 30, 42, 100, 4600 members, and "the
Coxeter diagram for the roots in 19L1 is the incidence graph of the Petersen graph. The subset 20L1 consists of 30
roots forming a copy of Tutte's 8-cage graph ... The 42 roots in 21L1 correspond to the points and lines of a
projective plane of order 4, joined by incidence, while the 100 points of 22L1 are a copy of the Higman-Sims graph";
the 4600 points of 23L1 are Leech-lattice points at minimal distance from two points at minimal distance. Their sizes
"can be computed from knowledge of the stabilizer of [the controlling vector] in the automorphism group of the Leech
lattice".

**Translation.**
- Edge function of a Coxeter diagram: inputs = roots; f(x) = 1 iff the selected roots contain two non-orthogonal
  roots. Independent sets = sets of mutually orthogonal roots (orthogonal frames); the 632 partial function (false at
  every maximal independent set, true at each one-vertex extension) asks for the AND count separating maximal
  orthogonal frames from frames plus one root.
- The three first diagrams are bipartite and C4-free [computed]:
  - subdivided Petersen: 25 vertices, 30 edges, degrees 3 and 2, girth 10, tau = 10, |E| + tau - 1 = 39. It lies in
    602's class (degree <= 3, no 3- or 4-cycle) and is a once-subdivided cubic graph (279/285 treat 2k-fold
    subdivisions; chatgpt_bounded_degree.md treats subdivisions of cubic graphs).
  - Tutte's 8-cage = GQ(2,2) = (synthemes, duads) = (points off a hyperoval, secants) of PG(2,4) (SPLAG Ch. 23 §4):
    30 vertices, 45 edges, cubic, girth 8, tau = 15, |E| + tau - 1 = 59; 616 gives n + tau = 45 for it.
  - PG(2,4) incidence: 42, 105, tau 21, bound 125 (ML-2).
- Higman-Sims (100 vertices, degree 22) is triangle-free with 4-cycles [memory: srg(100,22,0,6)]; it belongs to the
  fleet's census of graphs where |E| + tau - 1 fails (cluster 5 of meta.md section 2).
- The ladder is the Leech lattice's own: one construction (Vinberg's algorithm with the Leech-lattice control vector)
  produces the sequence, and its groups (S5, Aut GQ(2,2), PΓL(3,4) extended by duality, HS:2, Co_2) [memory] act on
  the instances.

**Work to complete.**
1. Computation: circuits below 39 for the subdivided Petersen graph and below 59 for Tutte's 8-cage (the fleet's local
   search and CaDiCaL windows handle these sizes; 650 is 63 gates). A negative answer adds two checked rows of 608
   (as 615/616 did); a positive one refutes 602 and 608.
2. Computation: AND-count census values (632) on both; for Tutte's 8-cage compare with 634 (Heawood, 7 = tau) and 445.
3. Lean: edge lists on Fin 25 and Fin 30 with the correctness criterion of pg23.py (edges true, maximal independent
   sets false).

## 4. ML-4 in full: umbral permutation groups as symmetry classes for level spaces

**Source.** DICT row 4 (from CDH §2.5, opened by the dictionary's author): for X = A_{l-1}^d, d = 24/(l-1) = p + 1,
the umbral group's image contains PSL2(p) permuting the d components, p = 23, 11, 7, 5, 3, 2 (so d = 24, 12, 8, 6, 4,
3); and these d points are the darts of the dessin of X0(p). The S6 lattice is the d = 4 x 6 case A5^4 D4.

**Translation.**
- Index rows and columns of n x n matrices by P^1(F_p), n = p + 1. perm(J + t) is invariant under permuting rows and
  columns separately, so for G ≤ PSL2(p) x PSL2(p) the set of G-invariant level spaces is a union of sums of isotypic
  pieces of C^n ⊗ C^n = (1 + V) ⊗ (1 + V).
- The quadratic layer (MAPPING_BY_READING A3, O-011): S_1 = <u, t>, S_2 = (1/2)(||t_0||^2 - (n-1)||t_r||^2 -
  (n-1)||t_c||^2). Each of these is an invariant form. On an irreducible constituent that is not self-dual every
  invariant symmetric bilinear form is 0, so S_2 vanishes identically there; on a real constituent it is a multiple of
  the unique invariant form and vanishes only if that multiple is 0.
- So symmetric witnesses for 185 (n = 4, dim 6), for the n = 8 setting of 136, and for 086 at n = 6, 8, 12, 24 live
  among sums of non-real isotypic pieces, where only S_3, ..., S_n remain to check. (n = 5, the size of 190, is not
  of the form p + 1; there PSL2(4) = A5 on P^1(F_4) plays the same role.)
- p = 3: PSL2(3) = A4 on 4 points contains the regular Klein four-group, the class for which Codex proved the bounds
  3, 3, 5 (DC) and 3, 4, 6, 7 (RC) (gct.md 5.2). p = 7: n = 8, the size of 136's Fourier block modes.

**Work to complete.** For G = PSL2(p) (p = 5, 7, 11, 23), the diagonal subgroup and G x G: decompose (1 + V)^{⊗2},
list the non-real constituents, compute S_k on each candidate sum exactly over Q(zeta_N), and record the largest
G-invariant level space; compare with 2n - 3 (080) and with 092's ceiling kappa(n) + 2n. Lean only for a witness
(the 086 file may import only PEqualNP.Defs).

## 5. ML-5 in full: frame shapes and rank-one level lines

**Source.** D1-9 (nus, and D1's remark): for a Coxeter frame shape pi = sum a_d [d] of a root system,
prod d^{a_d} = det(1 - Coxeter element), and the eta quotient T^X = prod eta(d tau)^{-a_d} satisfies
T^X(W_h tau) T^X(tau) = [N : R_X]; for A5^4 D4 this is T_6(W_6 tau) T_6(tau) = 72 (checked numerically by D1).
M24 cycle shapes and their eta products [memory].

**Translation** [mine]. For x the eigenvalue vector of a permutation with a_d cycles of length d,
sum_k e_k(x) t^k = prod_d (1 - (-t)^d)^{a_d}. With the checked 089, S_k(x y^T) = k! e_k(x) e_k(y), so x y^T spans a
level line iff for every k >= 1, e_k(x) = 0 or e_k(y) = 0. Frame shapes with zero entries allowed (a zero eigenvalue
multiplies by 1) and with negative a_d (eta quotients) give more e-patterns. Example at n = 24: x of shape 12^2 has
e-support {0, 12, 24}; y = (the 23rd roots of unity, 0) has e-support {0, 23}; x y^T is level. The barrier family
F_{q,r} of gct.md 5.1(c) is the frame shape [q] repeated, so ML-5 contains the known barrier lines.

**Work to complete.** Enumerate pairs of (generalized) frame shapes of length n with disjoint positive e-supports;
form block sums (110) and spans of several such lines; compute the mixed S_k on the spans; compare dimensions with
2n - 3. Lean: rank-one cases follow from 089 by `ring`-level identities on cyclotomic integers.

## 6. ML-6 to ML-12: what each needs first

- **ML-6.** The statement "an affine flat of F_2^{2m} on which a nondegenerate quadratic form is constant has at most
  2^m points" (the m = 2 case is 090) and the pair counts of 081/082 for IP_{2m}; for the Leech form these are counts
  over the Co_1-types of SPLAG Ch. 10. A Lean proof of the general flat bound reuses 091 and 092.
- **ML-7.** The ternary form of 092 and its test on the 129 orbit representatives (S6_05 records retain generator
  matrices and Gram/plane checks); the single-subdivision row for K_{4,4}.
- **ML-8.** The comparison theorem between the Laplacian gap of a congruence quotient and the edge expansion of its
  dessin, at the parameters of 043/046 (bounded degree, boundary expansion); our A.2 Cheeger proof is the nearest text
  of ours.
- **ML-9.** Jacobian ideals of the three cubics (Groebner computation in 24 variables, or a smoothness test at random
  points plus a dimension count).
- **ML-10.** A reading of CMT §1-2 at the source and a computation of the line-intersection types of their level sets.
- **ML-11.** One SAT search (7 outputs, 7 inputs) and then the overlapping-parity statement.
- **ML-12.** A candidate entry in the alg format; no computation.

## 7. Moonshine results whose only target is a proposed new node

These have no node in the present graph. The map is to a node the fleet could add; the work is the node plus its proof.

| Source | Proposed node | Translation | Work |
|---|---|---|---|
| S6_05 B.6: the rule "vois_d(N; rho) has Coxeter number h/d for d \| h" is false, with exactly 11 exceptions among 96 divisor-neighbour cases; E8^3, h = 30, d = 2 gives D8^3 (h = 14, not 15) [opened: statement] | a lib/meta "pattern refuted by exhaustive enumeration" row, the format of 437/439 (negative search rows) | An exact finite classification with all 96 cases and bases attached | Port the case list as a finite check (Gram matrices and root counts) |
| D1-1 / S6_05 B.3-B.5: J has minimum 4, kissing 23,058, norm-6 shell 1,849,032, norm-8 shell 44,291,124, theta series an explicit weight-12 form for Gamma0(3); the Co0 stabilizer of the associated plane has order 2,099,520 [opened: statements] | a GCT/lib row on lattice theta series as a test bed for exact shell counting (the fleet's rows count matchings and sign changes, 136, 148, 155) | Shell counts are coefficients of a modular form; the fleet's exact-sum rows are coefficient identities | A row "the norm-4 shell of J has 23,058 vectors", provable by enumeration with a certificate |
| DICT row 13: the Weil representation 30+6,10,15 carrying the E8^3 umbral form has the T-matrix of (G2)_1 (Fibonacci) times the eta^3 multiplier [computed by the dictionary's author] | none in P vs NP; nearest: the riffle and tensor-rank rows (124, 139) through S-matrix tensors | Modular data are small tensors with exact entries | Compute the S-matrix check DICT left open; then the rank of the associated tensors |
| DICT rows 10-12 and H17's frames in PSL2(Z/12) (algebra_combinatorics.md AC-11) | none | Galois actions on modular data at congruence level | see AC-11 |
| DICT row 22: M24 = <a, b>, a in 2B, b in 3A, ab of order 23 gives a planar dessin with 24 darts and cartographic group M24 [memory/computed there] | pcx 043 family (ML-8), as an exceptional member | A (2,3)-biregular graph with 24 edges and automorphism group transitive through M24 | Construct the graph; test its expansion constant |

## 8. Where the maps meet the held leases

- **L-meta-650** (held, lease ac02c797): ML-1 (the tetracode/AG(2,3) decomposition with the MDS pruning rule) and
  algebra_combinatorics.md AC-2 (the Singer presentation: the desk's edge list is exactly i + j in {0,1,3,9} mod 13,
  with multipliers 3, 9 and the polarity swap x_i <-> y_i) give two symmetry-reduced encodings for the running search.
- **L-meta-606/608**: ML-2 and ML-3 add instances (order-4 plane; the Leech-root ladder) of the same shape as 650.
- **L-gct-086** (held, lease 5dbcef17): ML-4 (non-real isotypic pieces are S_2-isotropic) and ML-5 (frame shapes)
  give two constructions of candidate level spaces, both computable.

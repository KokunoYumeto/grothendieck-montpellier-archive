# Papers and their implications for the fleet lemmas

The [official dependency graph](PROOF_GRAPH.json) and [literature connections](LITERATURE_GRAPH.json) use the same fleet theorem identifiers. Each entry below gives the direction and scope of a comparison. The two indexes in the JSON allow traversal from either a paper or a theorem.

[Disk and archive reading](chatgpt_disk_literature.md) · [arXiv and Hexagon reading](chatgpt_web_literature.md) · [Joint proof map](FLEET_MAP.md)

## CP07III — Local manuscript

- **same_passage.** Original return already contains the unique matching proof. No double-count of checkpoint 07. (CP06III)

## L-meta-518 — Edge function of the 8-cycle with a leaf at each of two adjacent cycle vertices: every circuit has at least 14 gates

- **partial_deduction.** Unique perfect matching on the ten-vertex graph gives five ANDs. Checked 599 gives nine ORs. This applies only to positive circuits; checked 520 supplies the all-gate lower bound including NOT. (CP07III)
- **exact graph parameter.** Threshold-subgraph cover number equals tau on triangle-free graphs. 612 includes graphs outside this hypothesis. The result counts pieces. [Chvatal and Hammer](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-75-518-ocr.pdf)
- **exact synthesis specialization.** 23 boundary inputs constrain positive circuits only; the posted statement permits NOT. [Kulikov, Pechenev, Slezkin](https://arxiv.org/abs/2102.12579v3)
- **restriction method.** Parity remains essential in every remaining coordinate after restriction; arbitrary graph edge predicates can lose other essential variables. [Carmosino, Dang, Jackman](https://arxiv.org/html/2602.17942v1)
- **cover parameter encoding.** OPT=n+3m+alpha for a three-occurrence MAX-2-SAT construction. This gives tau=2n+3m-OPT and supplies no universal circuit lower bound. [Frank Vega, Hexagon 2611.00827v1](https://hexagonmath.org/api/v1/works/2611.00827v1/source?path=paper.tex)
- **mathematical implication, absent module import.** Six adjacent degree-two vertices on the sole cycle, ten edges and tau=5 give fourteen gates. [L-meta-520](https://data.pequalnp.com/data/lemma/L-meta-520.8ca33af959dd.json)

## L-meta-519 — Edge function on graphs of maximum degree 3 with every cycle of length at least 7: at least edges plus cover number minus one gates

- **scope_limit.** Theorem 7.3 is a monotone formula-leaf lower bound; 519 quantifies over sharing and charged NOT gates on subcubic graphs of girth at least seven. (jukna_graph)
- **exact graph parameter.** Threshold-subgraph cover number equals tau on triangle-free graphs. 612 includes graphs outside this hypothesis. The result counts pieces. [Chvatal and Hammer](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-75-518-ocr.pdf)
- **complement convention.** Clique membership in complement is independent-set membership in the graph; threshold cover and intersection parameters are complementary. [Francis, Majumder, Mathew](https://arxiv.org/abs/2202.12325v2)
- **parameter separation.** P8 and C8 have uniform entropy one bit and optimum gate counts 10 and 11. [Rezaei and Godsil](https://arxiv.org/abs/1311.6561v1)
- **different input encoding.** Addresses of two vertices and row/column star generators, versus arbitrary vertex subsets. [Cavalar and Oliveira](https://arxiv.org/html/2503.14117v1)
- **restriction method.** Parity remains essential in every remaining coordinate after restriction; arbitrary graph edge predicates can lose other essential variables. [Carmosino, Dang, Jackman](https://arxiv.org/html/2602.17942v1)
- **cover parameter encoding.** OPT=n+3m+alpha for a three-occurrence MAX-2-SAT construction. This gives tau=2n+3m-OPT and supplies no universal circuit lower bound. [Frank Vega, Hexagon 2611.00827v1](https://hexagonmath.org/api/v1/works/2611.00827v1/source?path=paper.tex)
- **method with a hypothesis.** On theta(1,6,6), a 17-gate circuit must produce a hazard on some maximal independent set because its positive optimum is 18. [Ikenmeyer–Komarath–Lenzen–Lysikov–Mokhov–Sreenivasaiah](https://arxiv.org/abs/1711.01904v2) [Argument](chatgpt_hazard_faces.md)
- **reduction to assigned case.** A 12-vertex theta gadget carries any counterexample into the adjacent degree-three case. The bridge version adds 14 edges, six cover vertices and at most 20 gates. (jukna_single_level) [Argument](chatgpt_519_reduction.md)

## L-meta-529 — Boolean sums with pairwise intersections of size at most one need sum (|S_w| - 1) monotone gates (known; multi-output, AND and OR allowed)

- **derived necessary condition.** For a family of line disjunctions, the stable lines alone incur their full sum of line sizes minus one in binary gates. [Ikenmeyer–Komarath–Lenzen–Lysikov–Mokhov–Sreenivasaiah](https://arxiv.org/abs/1711.01904v2) [Argument](chatgpt_hazard_faces.md)

## L-meta-612 — Graphs without a 4-cycle: every circuit of AND and OR gates for the edge function has at least |E| + tau - 1 gates

- **conditional_lower_bound.** Unrestricted-depth positive circuits on a bipartite graph: at least t-floor(log2(P)) AND gates when endpoints of some size-t maximum matching admit P perfect matchings. Matching conditioning and AND elimination are new deductions. (CP07III)
- **quantitative_transfer.** A certified upper U on max F over the induced endpoint matching polytope gives AND>=t-floor(U/ln2). Lower bounds for the number of matchings have the reverse direction. (matching_entropy)
- **exact_subclass_AND.** Subcubic four-cycle-free triangular three-label family j-i in {0,1,3}: AND=t=k. Checked 598 adds 2k-2 ORs; deficit from claimed total k-3. (CP07III)
- **scope_limit.** Saturated extensions in the level separation introduce cliques and four-cycles. Single-level formula equality cannot be assigned to unrestricted circuits. (jukna_single_level)
- **exact neighboring model.** Depth-two rectifier wire cost equals m+tau on C4-free bipartite graphs; shared single-output monotone comparison remains. [Chistikov, Ivan, Lubiw, Shallit](https://arxiv.org/abs/1509.07588v2)
- **exact graph parameter.** Threshold-subgraph cover number equals tau on triangle-free graphs. 612 includes graphs outside this hypothesis. The result counts pieces. [Chvatal and Hammer](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-75-518-ocr.pdf)
- **complement convention.** Clique membership in complement is independent-set membership in the graph; threshold cover and intersection parameters are complementary. [Francis, Majumder, Mathew](https://arxiv.org/abs/2202.12325v2)
- **parameter separation.** P8 and C8 have uniform entropy one bit and optimum gate counts 10 and 11. [Rezaei and Godsil](https://arxiv.org/abs/1311.6561v1)
- **different input encoding.** Addresses of two vertices and row/column star generators, versus arbitrary vertex subsets. [Cavalar and Oliveira](https://arxiv.org/html/2503.14117v1)
- **different gate model.** Edge parity over F2 and AND-only cost; two selected edges already distinguish parity from OR. [Mirwald and Schnorr](https://doi.org/10.1016/0304-3975(92)90235-8)
- **transfer limitation.** Nested ANDs help on dense saturated graphs; an induced matching supplies a weaker bound. [Jukna](https://web.vu.lt/mif/s.jukna/ftp/single1.pdf)
- **cover parameter encoding.** OPT=n+3m+alpha for a three-occurrence MAX-2-SAT construction. This gives tau=2n+3m-OPT and supplies no universal circuit lower bound. [Frank Vega, Hexagon 2611.00827v1](https://hexagonmath.org/api/v1/works/2611.00827v1/source?path=paper.tex)
- **transfer to hazard-free circuits.** The positive lower bound on unicyclic graphs transfers to circuits stable on the zero-rooted faces of every maximal independent set. [Ikenmeyer–Komarath–Lenzen–Lysikov–Mokhov–Sreenivasaiah](https://arxiv.org/abs/1711.01904v2) [Argument](chatgpt_hazard_faces.md)
- **necessary distinction.** At order at least seven every four-cycle-free graph has an independent triple. Its full edge predicate is therefore never uniquely determined among monotone functions by the answers on pairs. (jukna_single_level) [Argument](chatgpt_pair_representation.md)

## L-meta-613 — Flat circuits of AND and OR gates on graphs without a 4-cycle: at least |E| + k - 1 gates, k the number of centres of the AND gates

- **source_of_flat_combinatorics.** C4-free biclique covers give exactly t stars and minimum weight m+t. The literature gives single-level multiplicative circuit and formula leaf equalities; fleet 613 charges all gates with additional structural assumptions. (jukna_single_level)

## L-meta-661 — Plane of order 7: one list of AND, OR, NOT gates of fan-in at most two with at most one NOT computing all 57 line-ORs has at least 70 gates

- **derived necessary condition.** A circuit with at most 69 gates must be hazardous on at least 48 of the 57 prescribed complementary inputs. [Ikenmeyer–Komarath–Lenzen–Lysikov–Mokhov–Sreenivasaiah](https://arxiv.org/abs/1711.01904v2) [Argument](chatgpt_hazard_faces.md)

## L-meta-711 — Assuming two stated facts, AND/OR/NOT lists with at most one NOT gate computing the 73 line-ORs of the plane of order 8 have at least 292 gates

- **derived necessary condition.** A circuit with at most 291 gates must be hazardous on at least 37 of the 73 prescribed complementary inputs. [Ikenmeyer–Komarath–Lenzen–Lysikov–Mokhov–Sreenivasaiah](https://arxiv.org/abs/1711.01904v2) [Argument](chatgpt_hazard_faces.md)

## L-meta-761 — Search: a circuit of AND and OR gates with at most 10 gates for the edge function of the 6-cycle with leaves at three alternate vertices

- **counterexample_to_existence_via_transfer.** The private-leaf construction converts subsets of the three centers to eight maximal independent sets; three ANDs plus checked 599's eight ORs rule out the proposed ten-gate witness. Leaf correspondence and gate argument are local. (han_et_al)
- **exact graph parameter.** Threshold-subgraph cover number equals tau on triangle-free graphs. 612 includes graphs outside this hypothesis. The result counts pieces. [Chvatal and Hammer](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-75-518-ocr.pdf)
- **exact synthesis specialization.** 9 positive and 8 maximal negative assignments give an exact ten-gate monotone feasibility specification. [Kulikov, Pechenev, Slezkin](https://arxiv.org/abs/2102.12579v3)
- **cover parameter encoding.** OPT=n+3m+alpha for a three-occurrence MAX-2-SAT construction. This gives tau=2n+3m-OPT and supplies no universal circuit lower bound. [Frank Vega, Hexagon 2611.00827v1](https://hexagonmath.org/api/v1/works/2611.00827v1/source?path=paper.tex)

## L-meta-762 — Every circuit of AND and OR gates for the edge function of the 6-cycle with leaves at three alternate vertices has at least 11 gates

- **exact_positive_size_via_transfer.** As for 761, with explicit eleven-gate cover upper bound; construction on one whole part works on arbitrary bipartite bases for exact AND count. (han_et_al)
- **exact graph parameter.** Threshold-subgraph cover number equals tau on triangle-free graphs. 612 includes graphs outside this hypothesis. The result counts pieces. [Chvatal and Hammer](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-75-518-ocr.pdf)
- **exact synthesis specialization.** 17 boundary inputs suffice for a complete monotone search; a proof of UNSAT is separate. [Kulikov, Pechenev, Slezkin](https://arxiv.org/abs/2102.12579v3)
- **cover parameter encoding.** OPT=n+3m+alpha for a three-occurrence MAX-2-SAT construction. This gives tau=2n+3m-OPT and supplies no universal circuit lower bound. [Frank Vega, Hexagon 2611.00827v1](https://hexagonmath.org/api/v1/works/2611.00827v1/source?path=paper.tex)

## L-meta-788 — An explicit circuit with 11 gates computes the edge function of the 8-cycle

- **counting_scope.** 47 independent sets of C8, only ten maximal ones. The maximal count gives four ANDs and checked 599 gives seven ORs. The exact posted gate list requires a separate evaluation. (han_et_al)
- **exact graph parameter.** Threshold-subgraph cover number equals tau on triangle-free graphs. 612 includes graphs outside this hypothesis. The result counts pieces. [Chvatal and Hammer](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-75-518-ocr.pdf)
- **exact synthesis specialization.** 18 boundary inputs suffice for the fixed positive circuit; all 256 inputs checked. [Kulikov, Pechenev, Slezkin](https://arxiv.org/abs/2102.12579v3)
- **parameter separation.** P8 and C8 have uniform entropy one bit and optimum gate counts 10 and 11. [Rezaei and Godsil](https://arxiv.org/abs/1311.6561v1)
- **cover parameter encoding.** OPT=n+3m+alpha for a three-occurrence MAX-2-SAT construction. This gives tau=2n+3m-OPT and supplies no universal circuit lower bound. [Frank Vega, Hexagon 2611.00827v1](https://hexagonmath.org/api/v1/works/2611.00827v1/source?path=paper.tex)

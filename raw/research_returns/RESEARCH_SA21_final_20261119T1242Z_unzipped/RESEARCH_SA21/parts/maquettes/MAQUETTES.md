# Part C: completed proof and source report

AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, run `/root/maquettes`, 19 November 2026. No priority is claimed. Complete proofs are in the canonical fragment `maquettes.tex`, labels `SA21-C01`--`SA21-C12`. Statement metadata, actual check events and precise input corrections are in `results.csv`, `CHECK_EVENTS.tsv` and `CORRECTIONS.tsv`.

## Outcomes

C.1 and L4 are refuted as proposed and settled by the exact all-dimensional replacement SA21-C08. Connected boundary means connectedness of the proper-face orbit poset's comparability graph; dimensions zero and one are excepted. Signed diamonds and connectivity are insufficient: the explicit torus-topped three-cell model passes them. Global link connectivity is also unnecessary: two triangles sharing one vertex give a regular complex with a disconnected one-dimensional link. The exact theorem requires finite principal ideals, spherical proper-face order complexes, cover incidences with a unique signed lower lift, and coherent incidence signs. Its proof constructs the regular cells and weak topology and realizes the prescribed signs inductively through fundamental cycles. It allows an empty complex, infinitely many cells, unbounded global dimension and nonlocally finite upper intervals.

C.2 is settled by SA21-C09--C12. The exact abstract simplicial criterion is finite Boolean augmented principal ideals plus global meets; equivalently the vertex-set map is injective. At pol 1 gives the meet property. At simp 1 is automatic for regular CW posets and admits a square; without the CW assumption it even admits three points below a formal one-cell. The original Boolean-ideal definition on 156-7/14 is correct; its claimed predecessor-count shortcut is false. Flags under inclusion give the all-dimensional order complex. The different point-interval construction of 156-9/5--7 has one-dimensional incidence; its positional flags are prefigures, and figures require endpoint closure. The McCord map is a weak equivalence for arbitrary Alexandrov posets, distinct from a subdivision homeomorphism.

## Source audit and interpretation branches

Original 156-8 scans 4 and 6 were fetched selectively and inspected at high resolution. Magor 1prime(c) reverses X alone and scan 6 writes disjunction as inequality on the displayed variables. These literal formulas leave only the empty oriented set. We explicitly correct disjunction to inequality of orientation orbits for the geometric classification. The source epsilon-like superscript in Magor 2(b) has no corresponding target sign. Both readings are proved: source-only arbitrary sign allows precisely loop graphs, with no rank at least two; matching signs (or no source sign) make the lifting condition automatic under identity refinement. These corrections are never silently attributed to the original text.

We also state the consequences of treating the possible Yprime in 1prime(b), or Y in codim(Y,X)=2 of Magor 6(a), as independent variables. The former forces emptiness under identity refinement and free reversal. The latter, universally closed, allows only rank at most one. The intended higher-dimensional discussion uses the subject Z in codim(Z,X), following SA21-K8-09. Thus no conclusion rests on an unacknowledged choice between the readings.

R9 needs corrected signs and finite-per-cell boundaries before its components are finite directed cycles. Finite chain length alone allows bi-infinite directed paths. The finite regular rank-two class also excludes loops and use of both orientations of the same boundary edge. R10 and the finite distributive-lattice repair of SA21-R7-06 were re-proved and checked computationally. R13 needs the distinction between prefigures and incidence-closed figures.

## Primary sources opened

Björner (1984): original publisher text in the public Academia/CORE mirror; Definition 2.1 p.8, section 2.3 pp.8--9 and Proposition 3.1 p.11. The latter itself allows arbitrary CW posets. The direct CORE PDF returned HTTP403. McCord (1966): original PDF; Theorem2 p.466, local Theorem6 p.467, explicit map in section5 pp.469--470. Barmak (2011): original book PDF; Theorem1.4.6 p.12, Remark1.4.16 p.15 and section7.1 pp.93--98. Serre (1977): full original Numdam PDF, ChapterI section2.1 Definition1 p.22, including free reversal and endpoint convention. Hersh (2014): arXiv HTML Definition1.1 and Theorems1.2,2.2, context only; the source-archive web request returned unsupported gzip.

Michel Hua's project was not opened directly in this run. The attached reading credits its Serre identification and signed-boundary observation; that credit is retained without claiming direct source access. Every bibliography entry records opened or not-opened status.

Original scans and source PDFs are outside this deliverable tree in `SA21_sources/`. `156-8_selected.pdf` is the complete two-page extract of original scans4 and6. The sparse failed full download `156-8.pdf.incomplete` is never treated as a complete source. The successful selective extractor and its log are included. It uses strict PDF parsing to request only the necessary objects.

## Computations

The standard-library program `code/check_maquettes.py` explicitly constructs each finite relation and checks all relevant finite instances; it is not a random search. Its saved output is `code/check_maquettes_output.json`. The torus model has 9 vertices,27 edges,18 triangles and one formal three-cell:55 unoriented cells and110 oriented elements. All252 immediate and612 strict signed incidences are constructed;108 augmented rank-two intervals and324 Magor6a instances pass. The rational boundary matrix ranks are8 and17, giving Betti numbers(1,2,1). Every corrected Magor1--6 axiom, dimension, finite-ideal, relevant-boundary connectivity and full-order-complex vertex-link condition is checked.

Other complete finite checks are the two-element involution obstruction, all four origin/terminus assignments for a two-vertex one-edge graph, the square, two parallel edges, the eight-oriented-object backtracking two-cell, the three-point boundary, the13-cell wedge of triangles and the four-point Alexandrov circle. The proofs for arbitrary dimension and infinite sets do not depend on those computations.

## Search and completion

We searched the named primary sources by author/title and searched signed regular CW incidence, CW-poset sphere criteria and connected links. We claim no novelty for the torus obstruction, CW-poset theorem, sign-realization argument, simplicial meet criterion or McCord comparison. All C.1, C.2 and L4 mathematical gates are closed by the stated exact statements or explicit interpretation branches. Typesetting checks are recorded in `BUILD_REPORT.md`. The parent's requested independent audit of finite M(L) is subsequent work, not an unresolved C gate.

Latest finite-check runtime: 0.085558 seconds.

## Explicit auxiliary certificate index

All entries below run from `code/check_maquettes.py` and are saved in `code/check_maquettes_output.json`; the complete table of twelve statement rows is `results.csv`.

| Statement | Executed function | Saved output entry |
|---|---|---|
| C02 | `check_literal_lifting_branch` | literal source-only sign in Magor 2(b): all four endpoint assignments |
| C10 | `check_square`, `check_three_point_boundary` | square face poset; three-point boundary |
| C11 | `check_flags_and_incidence` | positional flags versus incidence-closed figures |
| C12 | `check_mccord_circle` | four-point Alexandrov circle |

The C02 finite enumeration includes both loop assignments and both nonloop assignments. The C10 three-point model verifies both axioms and the three-point boundary obstruction. The C12 checker constructs the actual four-cycle; the topological obstruction to a homotopy inverse is proved in the manuscript, not inferred from a Boolean flag in the output.


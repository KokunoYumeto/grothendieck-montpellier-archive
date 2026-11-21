# P-15: determinant support9 seven-plane — proof outline at checkpoint

## Final verification 2026-11-21T03:54:07Z

P-15 is fully checked for the determinant S_A and both permanent S_A/S_B tensors. The self-contained exact-rational verifier passed all three cases; pencil independently replayed all three and read the full proof, and root read the full proof too. Earlier pending or unresolved notes below are historical. The final proof is `support9_sevenplanes.tex`; final checker and verification hashes are in `P15_HASHES.json`.

## Update 2026-11-21T03:51:58Z

The full proof is now `support9_sevenplanes.tex`. The determinant standalone exact-rational checker has passed twice independently. The generalized checker `check_support9_sevenplanes.py` has also passed for the second permanent support9 case twice independently; its first permanent case is still running at this update. The historical checkpoint outline below is retained as work documentation.

Status: computation found no admissible degree210/120 torus extension. Full narrative and standalone replay certificate are being prepared; do not yet publish the lower bound14 as fully checked.

Take the seven coefficient tensors of 2-by2 determinants indexed `[0,1,3,6,7,9,18]` in the root lexicographic4-by4 rectangle indexing. Their variable support is the3-by3 grid, so T lies in A7 tensor B9 tensor C9. Its C-contraction image U has dimension9. The proper-incidence lemma in R04 says border rank at most13 would imply a13-plane E containing U with wedge-map ranks at most78 and104 for the A and B wedge maps. The baseline ranks on U are62 and80, so allowed increments are16 and24.

The row/column diagonal torus fixes T. Properness of the relevant determinantal incidence inside the Grassmannian permits a torus-fixed E. Thus E/U has a decomposition by torus weights, of total dimension4. There are33 nonzero quotient weight blocks, each of dimension at most3.

1. Maximal-weight saturation enumerates all46119 supports of at most4 weights whose capacities total at least4. Every support of size1 or2 fails a prolongation nullity condition. There remain236 supports of size3 and13019 supports of size4. The finite-field ranks used at this stage are only lower bounds on characteristic0 rank, which is the correct direction for exclusion.

2. For four weights the extension quotient is one line per weight. A column of a single weight line under either wedge map has a different output weight for every factor-basis vector. The rank increment is therefore the number of nonzero columns after quotienting the baseline image. Vanishing of each column is a system of linear equations in at most3 line parameters. Enumerating intersections of those linear kernels gives every exact joint A/B zero-column pattern. Distinct output weights imply a lower bound given by the cardinality of the union of active weights across the four lines. A preliminary single-line minimum/overlap bound removes12307 supports, leaving948 including236 size3 supports. Joint-pattern bounds remove176 more supports.

3. Of7225 joint four-line states,6619 fail actual rank contributions from their already fixed lines, leaving606 states. Among these,592 have exactly one variable line. Quotienting by the fixed lines again makes its columns have distinct weights; exact linear arrangements of the remaining parameters exclude all592 states. The remaining14 states have two variable lines. Quotient by the two fixed lines, enumerate the new exact arrangements of each free line subject to its original nonvanishing conditions, and apply the output-weight union bound. All32 resulting pairs fail.

4. With three weights the multiplicities are(2,1,1). A2-plane in a quotient block of dimension2 is fixed. A2-plane in a quotient block of dimension3 is the kernel of a nonzero dual normal n. For a linear column map L on that block, the rank on ker(n) is as follows: rank(L)=3 gives2; rank2 gives1 exactly when n annihilates ker(L), otherwise2; rank1 gives0 exactly when n spans row(L), otherwise1; rank0 gives0. Hence every rank drop is again a linear condition on n. Joint arrangements for the double component and the two lines enumerate42274 cases. Summing, over each output weight, the largest of the component-image ranks is a valid lower bound on the total increment. Every one of42274 cases exceeds16 in A or24 in B.

Thus no torus-fixed extension survives. Once the complete enumeration, exact arithmetic, and whole proof have been independently checked, P-15 will state border rank(T) at least14 over characteristic0. This proof alone does not assert a positive-characteristic result.

Relevant scripts and their outputs are the `j7_*` files with `det_0_1_3_6_7_9_18` stems. The multiplicity scan initially failed only while serializing Sympy integer entries after printing survivors0; the serializer has now been corrected to preserve exact integers/rationals.

# Independent audit of the complete complex w catalog

Checker: GPT-6 Astra Pro, inherited reasoning effort not exposed, GHOSTS `/root/cm_transport`,21 November2026. This is a complete mathematical code read and a targeted exact execution, not a formal proof certificate.

## Geometry and finite catalog

The full W01–W03 proofs in `sections/small_surface_reduction.tex` were written and checked in this run. Their scope is the complex product E^4. W01 is a hand proof of all required dyad decompositions; its independent 1171/1963-matrix enumeration is a supplementary check. W02 replaces every relevant nonabelian surface by an integral effective sum of abelian surfaces of the same degree and class, including both (n,b)=(1,2) and(2,1) cases. W03 includes the primitive norm(3,4) degree14 exceptions that a coordinate-graph-only catalog misses.

For every abelian surface, the saturated O_K lattice is free rank2 and its pair-projection degrees are norms of primitive Plucker minors. A nonzero-Weil surface of degree at most22 is a graph or transposed graph for the fixed E² x E² splitting, with isogeny degree1,3,4. Every zero-Weil abelian surface of degree at most14 is either a graph over one of the six coordinate pairs or a degree14 adjacent-minor(3,4) exception. The exceptional family has a constant fourth coordinate and hence zero Weil period.

## Loader and all70 exterior coordinates

Read `work/agents/t0_search.py` in full and checked exactly the prefix loaded before the literal `extra={}`. Its Eisenstein pairs represent a+b*omega; multiplication, conjugation through later helpers, norms, determinant, and the two integral pullback forms are correct. In the oriented integral basis u_i,v_i, the multiplication matrix is [[a,-b],[b,a-b]]. Its determinant is a²-ab+b². The exterior product sign is the parity of inversions between the concatenated sorted index lists; overlaps correctly vanish. The70 sorted four-element subsets of8 generators are the complete integral H4 basis.

The `graph` function takes the wedge of the four pullback forms defining the two equations output-h(input)=0. The quotient homomorphism is split, so its fiber is exactly the connected graph, without an isogeny multiplicity. This verifies the cohomology vector for every coordinate-pair chart. The `surface_z` function computes p12 times conjugate(p34), the two parameterization minors, which gives the correctly normalized period and is zero exactly when the abelian surface has zero Weil projection.

## Zero-extra generator catalog

Read the entire `work/agents/w_full_abelian_search.py`.

For a coordinate-pair graph of degree at most14, the formula2(1+T+Nm(det h)) forces T≤6. Eisenstein norm6 does not occur, and every possible entry therefore has norm≤5. Such elements have coordinates in[-2,2], so the enumerated list is exhaustive. Every graph over all six coordinate pairs is tested, and only exact zero-period classes enter the zero catalog. Deduplication by the complete exterior vector loses no class; equal classes necessarily have the same polarization degree.

For the nonunit-minor exceptions, the code wedges the two forms for b*x_j-a*x_k and then the point class of the fixed fourth coordinate. Since Nm(a),Nm(b) are3 and4, they are coprime in O_K. Thus the kernel is connected and equals the embedded elliptic image t -> (a*t,b*t). It has the intended projection degrees3,4. Multiplying by the fourth-coordinate point and leaving the free coordinate unused gives precisely the surface of W03, with degree14. Both norm assignments and all unit phases are enumerated. This avoids the earlier graph-only omission.

## Exact effective-cycle dynamic program

Generator half-degrees range from1 to7. At stage d, `sums[k]` consists of all multisets of k generators of that degree, with repetitions. The old states use only smaller degrees. The update combines an old state of weight n-k*d with every such multiset. Induction on d proves that the final `dp[n]` includes exactly all integral effective sums of zero-Weil generator classes of degree2n. The zero cycle is included. No negative multiplicity or restriction on the number of distinct supports is introduced.

The all70 vectors are encoded additively by sum(v_i*1001^i), including signed coefficients. A coefficient difference bounded strictly below1001 in absolute value cannot encode zero unless all its entries vanish: reduce successively modulo1001. The comparison checks the stronger bound156<1000 on every possible difference of two full degree-at-most22 cycles and the target. This uses at most11 irreducible degree-at-least2 components and the actual maximum generator coefficients. Thus the integer-set membership tests have no carry collision.

The recorded zero-generator counts by degree are2:6,4:72,6:288,8:180,10:1440,12:864,14:1440. The final zero-cycle class counts by half-degree0..7 are1,6,93,776,6066,48564,322050,2162952. These were read from the executed output; this checker did not claim a second full DP run. Root subsequently reported an independent isolated regeneration and complete comparison with matching output.

## Target, normalization and symmetry

A separate exact execution in this check rebuilt q=PU-PV-QU-2QV from divisor forms, independently rebuilt t0 from the four scalar graph classes, and pulled t0 back by diag(omega,omega,bar(omega),bar(omega)). All70 coefficients satisfy

    q=t0-R*t0=3w,

and their gcd is1, with largest absolute coefficient2. The same execution applied[-1] on the first elliptic coordinate and verified that it sends q to-q in all70 coordinates. Composing this involution with exchange of the two numerators therefore preserves the exact target q, as well as effectiveness and degree.

This justifies eliminating the period pair(1,-2) in favor of(2,-1), not merely identifying their scalar period equations. The remaining pairs are(1-omega,-2-omega) and(2+omega,-1+omega). Each numerator has at most two nonzero-Weil components; two such components must both be automorphism graphs, since a degree3 graph already costs at least16. Their periods and the possible single-main periods have norms0,1,3,4. The four stated period pairs are therefore exhaustive before the exact symmetry reduction.

The denominator of w is3 and the calibration D≥4N excludes N≥6 below degree24. Pure Weil classes pair trivially with theta², so the two numerator degrees are equal. All degrees are even. Hence the exact comparison only needs degrees16,18,20,22. The checked complete catalog and the exact70-coordinate test, together with W01–W03, address all effective surfaces in that range, rather than only graph representatives.

## Actual check scope

The zero catalog, loader, dynamic program, encoding bound and geometric completeness were checked line by line; the independent target/symmetry calculation was executed. Root independently owns the full comparison-loop and portable-certificate rerun; bounded_specialization separately checked W01–W03 and target symmetry. The final all-prime t0 result is separate: no claim of exact24 for w in supersingular characteristic is inferred from this complex calculation.

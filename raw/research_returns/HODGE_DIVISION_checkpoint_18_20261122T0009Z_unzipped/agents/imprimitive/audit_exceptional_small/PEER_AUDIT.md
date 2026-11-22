# Independent whole-proof audit: D-EXS-01–03

**PASS.** /root/imprimitive, GPT-6 Astra Pro, effort inherited/not exposed,
HODGE_DIVISION. Actual report write: 2026-11-21T19:50:40.434799+00:00.

Proof: research/exceptional_small_section.tex, SHA-256
eed92a30c4fb13b822ab967d3622eede628f381c45932d9805e0d7377f99f2da.
Bibliography: research/exceptional_small_bibitems.tex, SHA-256
e465cb1bcfe3de46276880312ec737fb89a713709f76455efa67957f0b8d695e.

## Complete mathematical reading

I read the entire proof, all bibliography entries, the complete GAP exporter,
and the complete root Python checker. I independently reconstructed the
following implications.

1. Every ordinary irreducible of any quasisimple central quotient lifts to
   the appropriate universal cover. Keeping every nonlinear row includes
   every central character, even when the universal center is noncyclic.
   Faithfulness on a noncyclic center is neither possible nor assumed.
2. Exact cyclic Fourier from all powers recovers every eigenspace. The
   equality |character value|=degree is precisely scalar action for a
   finite-order representation. Full prime-power maps and Galois powers
   suffice; no prescribed inertia class is omitted.
3. For F4(2), every compatible normalizer induces an automorphism lifting
   uniquely to the universal perfect cover. A lift with trivial simple
   action differs by a central homomorphism from a perfect group and is
   trivial. An outer intertwiner can be multiplied by a scalar to satisfy
   the actual square relation in the retained extension, without assuming
   a split extension. Thus precisely the irreducibly restricted extension
   rows suffice. Irreducibility makes their representing module irreducible.
4. For the other three cores, core projective support greater than2a/5
   gives every full-normalizer support at leasta/5 by the commutator
   inequality. A nonidentity scalar commutator has actual moving ranka,
   so it is not an exception. This needs no knowledge of the detailed
   outer action on the noncyclic center.
5. Factor-preserving tensor operators obey normalized spectral convolution.
   A nontrivial weighted permutation cycle has at most a constant words
   and all remaining word orbits have length at least2. Each weighted
   cycle contributes at most1 to a chosen eigenspace. This proves the
   quarter bound without assuming coordinate-only permutation matrices.
   Arbitrary mixed core types are allowed; no transitivity is used.
6. The actual intermediate-cover identity6=2e(h−1)+D and actual moduli
   factorization reduce period rank9 to genus0 and at least12 genuine
   branches. Each costs at leaste/5, hence e≤15, contradicting e≥52.
   This is an actual-period obstruction, not an inference of dominance
   from parameter counts. No ESD, field-equality or determinant premise
   was inserted.

No mathematical defect or required repair was found. The framework
paragraph preserves the source-obstruction scope and makes no new cycle
or Hodge-conjecture assertion.

## Independent exact arithmetic

My script independent_check.py imports no root arithmetic, selected rows
or output. It reuses only this auditor's previously whole-reviewed
integer-polynomial cyclotomic helper
agents/imprimitive/sporadic/verify_quarter_bound.py, SHA-256
1b5546a37c2ed0da7ab52b4c41cbaab547de06a5fff6e88fb4c22ca74c471393.

It selects outer rows independently by exact full restriction equality,
checks all table dimensions/degree sums/class-size sums, all power orders,
and the normal fusion's order, class-union and power-map compatibility.
Every nonscalar spectrum is independently reconstructed in Z[X]/Phi_d(X),
with exact divisibility, nonnegativity and dimension-sum assertions. The
root uses rational trace/Ramanujan arithmetic instead.

Actual result: 1639 rows, 1007457 nonscalar spectra,
124963 distinct cached Fourier problems, PASS in
41.376808 seconds. Complete per-row witnesses and spectrum-stream
hashes are retained in independent_check.json.

| Table | Rows | Spectra | Minimum degree | Minimum support ratio |
|---|---:|---:|---:|---:|
| 2.F4(2) | 169 | 28392 | 52 | 4/13 |
| 2.F4(2).2 | 86 | 12814 | 52 | 4/13 |
| F4(3) | 272 | 73984 | 6643 | 32/73 |
| E6(2) | 179 | 32041 | 2482 | 512/1241 |
| (2^2x3).2E6(2) | 933 | 860226 | 1938 | 8/19 |

## Primary-source and data provenance checks

Freshly read the official complete records for2.F4(2),2.F4(2).2,E6(2),
and(2²×3).²E6(2), plus CTblLib manual§3.7-3/5/6 and§5.4-1. Exact URLs:

- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.F4(2).html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.F4(2).2.html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/E6(2).html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/(2%5E2x3).2E6(2).html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/doc/chap3.html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/doc/chap5.html

The ATLAS-derived extension's former square-map error and its corrected
values are explicitly recorded. E6(2) is Fischer's input corrected by
Unger2016 after Magma computation, including order91 power maps and
irrationalities. The universal twisted-E6 table records the V4 central
construction; the manual says this construction in general returns
possible ordinary tables. We use the accepted specific official library
table as the cited mathematical input, not a claim of a fresh independent
construction or uniqueness proof.

The official F4(3) page failed in web.open but succeeded by direct urllib:
https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/F4(3).html
1281bytes, SHAa0b80306696efb8f726c13d0f1b8adefda010f7ed05a77f6ba3b9f0e813538d8.
It gives273classes and the precise O’Brien/Magma May–June2024 provenance.
The complete text was read. The official release-history entry at
https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctbllib/doc/ctbldiff.pdf
printedp15 confirms its addition in1.3.10. The actual exported version is
1.3.11. The local original data provenance strings match these records.

The invoked HHM multiplier list and universal-cover background were
previously read in this run and are reused honestly. No new proof of
classification, no independent original character-table construction,
and no completion of the parent's still-running934² GAP orthogonality
calculation are claimed. Those boundaries do not affect this completed
whole-proof and independent-spectrum audit.

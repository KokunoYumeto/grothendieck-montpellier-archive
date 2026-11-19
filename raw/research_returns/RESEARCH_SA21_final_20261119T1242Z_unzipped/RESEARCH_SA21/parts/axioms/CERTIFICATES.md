# Finite certificates for B.1–B.2

All programs use Python's standard library. They contain assertions rather than relying on visual inspection of a generated relation table. Each saved `.out` is from a successful final run. `CERTIFICATE_MANIFEST.tsv` records the program's SHA-256 hash, UTC execution time, exit status, whole-process elapsed time and output filename. Timing includes interpreter startup in that manifest; the `seconds` line in a program's output usually measures only its checking function.

From `RESEARCH_SA21_work/parts/axioms`, run each of:

```text
python finite_axioms.py
python core_models.py
python literal_systems.py
python legacy_subdivision.py
python connectedness.py
```

## finite_axioms.py

We construct the seven elementary set figures in SA21-B-Sigma-counter, compute incidence and inherited set-figure refinement, and impose the empty-or-principal intersection compatibility condition. We generate all 21 admitted clique downsets. The program checks the partial orders, the complete carrier condition for every elementary source and figure target, compatible refinement implying incidence, internal transitivity, open lieu existence, lieu detection of disjointness, At 10 and the biconditional At 9_Sigma.

For every compatible figure-parent pair and every pair of refinements, it additionally checks At D and matching-overlap compatibility. Its saved failure of At 12 is exactly:

```text
X=k, Y=x, Xprime=k, Yprime=xprime
K={a,b,k}, Xprime|K={a,b,k}, Yprime|K={a,b}
```

The final run reports 7 objects, 4 lieux and 21 figures. The checking function took approximately 0.008005 seconds; the recorded process time is 0.044596 seconds. A printed `At 12 FAIL` is the expected verified counterexample, not a failed program assertion.

## core_models.py

The shared finite implementation constructs relation closures, principal downsets, internal refinement, magasin compatibility and all admitted clique downsets. The `magaxioms`, `primed_axioms` and `core` methods check their explicitly named hypotheses. The script handles ten finite structures, several of which serve more than one comparison:

- The two-object local refinement chain: prime core, all local flags, relative compatibility, every matching gluing assignment and every At 14 bis extension diagram. All 12 gluing assignments and all 6 extension diagrams pass, but the empty-boundary extension has two different solutions. The code checks even the literal all-target mixed condition in that failure.
- The four-object nonlocal strong magasin: L2 fails.
- The three-object strong magasin: absolute CL(spac) fails while L2, L3 and old At supp hold.
- The positive-reading weak primed fork: every literal weak primed clause holds, but the principal deployment of its top is not a figure.
- The negative-reading weak primed two-chain: every negative-reading primed clause holds, while strong Mag 4 fails.
- The four-object weak divisible list: divisibility and the comparable clause hold, but the top principal deployment is not a figure.
- The four-object strong magasin with seven figures: a prescribed subdivision of a subfigure has no extension, refuting At 14.
- The four-object divisible strong magasin: both L2 and CL(spac) fail.
- The three-object prime core with 26 matching gluing assignments: all those assignments glue uniquely, while D and L3 fail. D0, L1, L2 and CL(spac) pass.
- The two-object typed spatial incidence chain: singleton orthoclosures and typed deployment injectivity hold, the reconstructed internal order is identity, and divisibility fails.

The first two-object model additionally has equal singleton orthoclosures and identical labelled deployments, directly refuting At spat 3 despite strong local Mag and extension existence.

The final checking function took approximately 0.004475 seconds; the whole-process time is 0.018699 seconds. All assertions passed.

## literal_systems.py

We check three base data sets, with two distinct interpretations of the last one.

1. The five-element M3 figure lattice: all 32 subsets have their joins computed; complete irreducibles, generation, deployment order/refinement tests, all carrier cases, internal transitivity and literal atlas clauses are checked. Its three-object magasin satisfies strong Mag 1–4. The join of two atoms has three deployed strata rather than their two-element union.
2. The two-point membership-free At-star model: all bounded unions of admitted figures, ambient admissibility, agreement of canonical principal subfigures, every inclusion/refinement test, compatibility-premise implication and global point separation are checked. The omitted canonical subfigure is explicitly absent.
3. The five-object missing-transitivity model: every principal carrier exists, all open lieu sets are nonempty, and the original all-pairs divisible clause holds. The witness is an internal chain of length two whose composite is not internal. With the separately specified compatibility, the same two orders give eight figures satisfying final Cont 1–5, Fig 1–4, Cont 6, Cond 7 and prime At 1–6 while At 7 fails.

The checking function took approximately 0.003311 seconds; the recorded process time is 0.026126 seconds. All assertions passed.

## legacy_subdivision.py

The principal structure has four strata and six figures. We verify the figure incidence system, prime generation, C4, cosupport preservation, every unique C6 restriction, its stratum formula, preservation of every bounded join family, every C7 extension and both C8_0 clauses. We also check the derived refinement order, its stratum test, compatible-refinement incidence, internal transitivity and the literal incident-source carrier condition of 156-7.

The target figure has two incomparable carrier candidates for `a`, so the intended least-carrier condition fails. The mixed subdivisions of `y` and `z` agree over `d` but cannot glue, so the distinct final C8 axiom fails exactly as stated in the manuscript.

The second structure is the two-stratum incidence chain with primitive subdivision equal to identity. We check all restrictions and extensions and all 8 gluing diagrams. Its two nonempty figures have the same cosupport, but the smaller is not a primitive subdivision of the larger. This verifies the auxiliary SA21-B-primitive-not-support counterexample.

The output's `seconds` line, approximately 0.000485 seconds, times only the first model. The manifest's 0.016027 seconds is the complete process time and includes both models. All assertions passed.

## connectedness.py

For each ground-set size from zero through four, we enumerate all families of nonempty subsets, retain precisely the elementary admissible families, construct every principal-subfigure incidence edge, and compare each component as a set with the classification proved in the text. We do not merely compare component counts.

| Ground-set size | Elementary figures | Components | Component sizes |
|---:|---:|---:|---|
| 0 | 0 | 0 | none |
| 1 | 1 | 1 | 1 |
| 2 | 5 | 3 | 1, 2, 2 |
| 3 | 28 | 5 | 1, 2, 2, 2, 21 |
| 4 | 231 | 6 | 1, 2, 2, 2, 2, 222 |

Every stated C4 witness is also checked. The checking function took approximately 0.099503 seconds; the process time is 0.111543 seconds. All assertions passed. The proof for arbitrary, including infinite, ground sets is separate in `axioms.tex`.

## Limits and independent reruns

The programs certify the specified finite structures and finite enumerations. They do not certify an infinite theorem by sampling. All infinite constructions, reconstruction equivalences and necessary-and-sufficient statements have direct proofs in the manuscript.

The separate B.3/B.4 agent reran the four axiom programs and audited their hypotheses and proofs; its captured output is `../bmodels/AXIOMS_CERTIFICATE_RERUN.txt`. Later small additions are recorded by the final hashes and outputs in this directory. The parent owns the unified program inventory and the final PDF audit.

# Certified finite computations

All computations in this subrun were produced by GPT-6 Astra (OpenAI), inherited effort, subrun `/root/counts`, on 19 November 2026. No priority is claimed.

## Reproduction

From the package root, run:

```sh
g++ -O3 -std=c++17 code/counts_extensions.cpp -o code/counts_extensions_bin
python code/counts_extensions.py
python code/counts_independent_check.py
python code/counts_gluing.py
python code/counts_straight_dual.py
```

The enumerator writes input JSON and all accepted sign vectors; the independent checker writes signed basis-exchange counts and complete disk-boundary certificates; the gluing checker writes every face's ordered transition list, all paired arcs and endpoint permutations, vertex orbits, and an explicit orientation-reversing cycle. Indexing in machine files is zero-based. The paper uses one-based line labels.

The six-line input is `[1,0,1], [2,0,1], [0,1,1], [0,3,1], [1,1,1], [4,4,1]`. The test line is `[0,0,1]`. Original triple determinants are all nonzero. Accepted extension counts by number of zero pairs are `80,150,75,10`.

The full signed basis-exchange checker is independent of the three-term GP prefilter. It verifies every accepted vector. Completeness follows from the matching-support lemma in C.01, not from a heuristic. The enumeration does not assume that an extension is straight in the given realization.

## Runtime and scopes

Final recorded enumeration runtimes (seconds) are in `audit/counts_extension_summary.json`: approximately 0.01, 0.01, 0.01, 0.13, and 0.08 for the three-, four-, five-, six-convex-, and six-test-line inputs respectively. Full signed basis exchange plus boundary extraction took approximately 0.01, 0.15, 1.86, 17.71, and 29.81 seconds. Complete gluing checks took under 0.04 seconds per input in the final recorded run. Fixed-geometry dual counts took approximately 0.0013 seconds. Exact measured values, including machine-dependent variation, are preserved in JSON output.

## Implementation corrections made during development

1. The first provisional four-line vector list contained one collinear triple. The input simplicity assertion rejected it before any four-line result was produced. It was replaced by the explicit moment-curve input now in the code.
2. The first triangle-side implementation used the wrong sign for `w_k dot J w_i`. It was corrected to `det(w_i,w_k)`, producing formula (C.2). The independent test against all permitted specializations then passed for every input.
3. The candidate count is reduced by normalization modulo reorientation of the new element, not by assuming stretchability.
4. No result depends on the two provisional failed runs. All results cited in the paper are from the final code and archived output.

## Exact manuscript dependencies checked here

- `MPL_154_001-045_transcription.tex`, scans 35–38: generization packets, empty specialization triangles, ordinary and exceptional inertia intervals. C.03 checks these definitions algebraically.
- Same file, scan 39: the chosen reflection gluing exchanges chord names at the ends; the discarded alternative continues a chord into the same named chord.
- Same file, scan 40: gen–gen descriptions of ordinary vertices.
- `MPL_154_077-126_transcription.tex`, scan 120, lines 3918–3941: counts `s2` as non-supercritical positions and `s0` as gen–gen inertia arcs plus `(0,1)` flags. We did not infer `s0` merely from `s1/2`.
- The exact general X2 exceptional completion is interpreted by the stable/unstable sweep convention of scans 5–7 and 44–45; the paper's main structural proof must state this convention explicitly. The code certifies that convention, not all four alternative gluings discussed in January.

## Corrections to prior work

- The supplied Lead L1's universal `chi=1-n` is false: C.02 has `chi=-45` with `n=6`. The proposed blow-up homotopy type with `chi=-5` is therefore also impossible for this example.
- The small n=3 and n=4 counts in SA11-R154-18 are confirmed for the explicit inputs. Its stated straight-only hypothesis is essential.
- The interpretation of L2 as deleting two of the eight vertices of a 3-cube is false in this test: all eight stable resolutions occur. The surface's choice concerns cyclicly adjacent square corners, not the existence of stable extensions.
- The supplied `154_001-176.md` line 176 describes 2nu selected stable generizations; this distinction must be corrected to separate the cyclic corner selection from the full set of `2^nu` stable generizations.

No external sources were fetched specifically for these computations. The packet-order formula was supplied by the polygons subrun and independently checked here. The mathematical definitions are taken from the supplied transcriptions; full translation to oriented matroids is handled in the paper's A.3–A.4 section.

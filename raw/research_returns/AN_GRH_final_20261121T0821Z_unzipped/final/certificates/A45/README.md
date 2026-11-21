# A45 degree39 arithmetic certificate

This directory is portable and contains both previously checked implementations and their data. It certifies the finite character tables and polynomial identities used in A45. The geometric and group-exponent interpretation is the written proof; these programs are not formal proof-assistant verification.

## Run

Use Python3. The linear producer also uses SymPy1.14.0, recorded in requirements.txt; the Cantor checker uses only the Python standard library and its included arithmetic file. From any working directory, pass the script's path:

```sh
python probe_A27_c39.py
python verify_A45_conductor39_cantor.py
```

Each program writes a JSON file beside itself. Successful runs return exit0. All256 point images, primary cycles or projections, Frobenius actions, character counts, and exact cyclotomic identities are retained in the outputs. The Cantor checker freshly enumerates the point set and derives the labels; it does not read the linear producer's point data or results.

## Contents and provenance

The linear producer imports verify_A27_character13_linear.py and reads the previously checked A32_ALL_POINT_IMAGES.json. The separate Cantor checker imports verify_A36_conductor5_cantor.py. Those arithmetic implementations were already checked for A32/A36 and were reused here; this packaging is not a new independent implementation.

Only three filesystem paths in the linear producer were changed for portability. LINEAR_PORTABILITY.patch gives the exact diff, and original_sources/probe_A27_c39.py preserves its original text. ORIGINAL_HASHES.json gives every original source/data/output hash and location. The expected directory retains both original JSON outputs.

Both portable programs were executed once after copying. PORTABLE_RUN_MANIFEST.json retains exact timings, exit codes and output comparisons. The Cantor JSON is byte-for-byte identical to the original; the linear JSON differs only in source_sha256 because its three path literals changed. Every other JSON value agrees exactly. The stdout and stderr logs are retained.

The successful arithmetic does not assert a universal supply of covers. Its claimed consequence is the specified degree39 cover and its exact original-field versus deck-field exponents in A45.

# Exact sum-first full replay

## Whole proof and source review

`hecke_general/higher4/replay_cyclic_sum_first.py` was read in full
after writing it. Its complete frozen verifier, integral setup driver,
and cyclic-certificate module were also read in full in the immediately
preceding review. The proof `exact_sum_first_replay_section.tex`,
**KT-SUM-FIRST-REPLAY**, establishes equality of every transformed
evaluation: the same full orbit-value vectors are summed over every
neighbor before multiplying by the same harmonic basis matrix.

All operations remain exact. The source and target orbit enumeration,
contraction, full harmonic-kernel ranks, evaluation determinant, every
neighbor entry, operator matrices, conjugation equations, rational real
form, factor products, comparison values and two extra-point operator
identities per prime remain checked. Additional explicit shape checks
make the original square-matrix assumptions visible. The whole
characteristic polynomial is certified by the separately approved
KT-CYCLIC-CHARPOLY argument. No producer characteristic-polynomial
algorithm is called by this replay.

The older wrappers, cyclic module, frozen source and original reports
were not edited. The new wrapper captures source byte snapshots and
executes those exact snapshots; it records source and input hashes
before and after, checks equality, and publishes the final report
atomically after those checks. An intermediate report has a distinct
`.pending.json` name. Each case has a distinct final report name, so
the three concurrently launched cases share no generated report file.

## Completed carried k13 control

The entire k13 degree was extracted from the carried higher-two
dataset unchanged. It has e=14 and harmonic dimension 14. The new
full replay completed both primes 7 and 13, with both whole cyclic
characteristic-polynomial certificates and both extra-point identities
at each prime. Its entire numerical result object equals the k13
object of the carried complete full report. The process exited zero
after 5.361834239000018 seconds. This is a fresh complete model replay,
not merely a standalone polynomial check.

The exact reconciliation is saved alongside the wrapper as
`sum_first_k13_reconciliation.json`.

| Artifact | SHA-256 |
|---|---|
| New wrapper | `f2e3cc7b57017efd6401b6f6d23e650d094f7adbe90ba943a8500a49bac03bc3` |
| Carried entire dataset | `b362945a162a6e6355be470f753dd2281e6b2dd284b9af8cff1e2a4ef9b8ee6e` |
| Carried full report | `f811e58393049e5149323d5c23063a006d12ae913c77a5d9355fed73a7ab23a1` |
| Extracted unchanged degree dataset | `5b35660c796e13457955a540baf4e814aeea1968292b4f260c405f2478634420` |
| Fresh complete control report | `f4ea1c2b1be566a2c34fde50f86dc4583f6f11c36b2923cc31030f5600861eeb` |

## Higher-weight status

Separate full replays were started for e32, e34 and e36 after the
control passed. Their report names are
`ktower_full_sum_first_replay_e32.json`,
`ktower_full_sum_first_replay_e34.json`, and
`ktower_full_sum_first_replay_e36.json`. A started process, progress
stage, or standalone polynomial certificate is not recorded here as
a completed full replay. Actual completion must be reconciled from
each final report and its matching input/code hashes. Global source
coverage and K-group vanishing require their separate mathematical
arguments.

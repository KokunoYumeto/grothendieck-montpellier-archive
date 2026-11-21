# Ordinary alternating small-rank exploration

2026-11-21 17:01 UTC: Initial GAP scan stopped before results because equality of generic table objects had no GAP method. This was a driver error, not a failed spectral bound. Changed the branch to explicit table-kind strings; initialized variables before closures to remove nonsemantic syntax warnings. No result from the failed run is treated as a certificate.

17:02 UTC: All682 selected rows/49,650 spectra computed, but initial JSON export returned fail because generic split-label parameters contain GAP character objects. Those two invalid four-byte outputs were not accepted as certificates. Added recursive conversion of character labels to strings and explicit serializer failure assertion, then reran the full scan.

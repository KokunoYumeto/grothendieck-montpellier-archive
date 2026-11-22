# Delayed Fatcat metadata availability check

The preceding public DOI lookups failed with an upstream503 response. This later check reuses exactly those two URLs after at least one hour; it does not revisit an access denial or change any authentication, endpoint or header to bypass a restriction.

The script and exact measured output are `code/root_fatcat_delayed_availability.py` and its associated output. There are exactly two GETs and no within-run retry.

| Work | Actual response | Interpretation |
|---|---|---|
| fujiwara1995 | 503 | No metadata record obtained; this does not establish absence of an original copy. |
| lieberman1968 | 503 | No metadata record obtained; this does not establish absence of an original copy. |

No source requirement changes merely because a service is reachable or a metadata record exists. An actual original passage and its hypothesis comparison remain necessary. No mathematical proof or finite certificate was rerun.

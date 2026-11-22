# Bounded CORE and Semantic Scholar discovery routes

We made five web-tool calls: four batches of three indexed queries and one opening of the advertised CORE Discovery page. That opening occurred after the two CORE batches and before the two Semantic Scholar batches. Each batch contained one query for each of the three remaining original works. The exact separate executed bodies are in `code/root_core_semantic_routes.js`; their compact responses, measured durations, source headers and outside-cache hashes are in `code/root_core_semantic_routes_output.json`. Saving that transcript did not rerun it.

| Call | Measured seconds | Actual result and limit |
|---|---:|---|
| CORE-domain discovery, engine2, three queries |3.539|An unrelated mathematical paper was returned; no target original.|
| CORE-domain verification, engine1, three queries |1.207|Later papers/bibliographies and the advertised Discovery service; no target original. Some results were outside the requested site restriction.|
| Actual CORE Discovery page open |0.612|HTTP403Forbidden, reference `turn530555649view0`; stopped without API or alternate-endpoint probing.|
| Semantic-Scholar-domain discovery, engine2, three queries |0.365|No indexed result returned.|
| Semantic-Scholar-domain verification, engine1, three queries |1.076|Broader-domain catalogue and later-reference results, including familiar publisher/MaRDI/Nagoya records and NDL/CiNii Fujiwara metadata. No Semantic Scholar original-copy record.|

The indexed NDL Fujiwara record and its digital-data label did not establish original access. Its actual URL and the CiNii URL were passed to the PartB reader for comparison with the retained access history; that assessment is separately recorded. We did not infer that a digital-data label meant an independently downloadable original, and did not retry the publisher route.

The full response bodies remain only in the outside reading cache. The compact metadata preserves the exact requests, timings, returned source references and hashes. Empty or broader-domain indexed results are not exhaustive absence findings about either service. No source gate changed and none of this activity counts as substantive movement.

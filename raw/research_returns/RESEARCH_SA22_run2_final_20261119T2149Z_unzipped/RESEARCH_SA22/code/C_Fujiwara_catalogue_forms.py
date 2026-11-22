"""Ordinary follow-up of links observed in the public catalogue HTML."""
import concurrent.futures
import datetime
import json
from C_Fujiwara_catalogues_1943 import ROOT, fetch

jobs = [
    ("eudml_advanced", "https://eudml.org/search"),
    ("eudml_journals", "https://eudml.org/journals"),
    ("eudml_references", "https://eudml.org/refsLookup"),
    ("gdz_tubular_hit", "https://gdz.sub.uni-goettingen.de/id/PPN243919689_0433"),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, jobs))
log = ROOT / "logs" / "C_Fujiwara_catalogue_forms.json"
log.write_text(json.dumps({"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                          "provenance": "Links present in the successfully read catalogue responses saved in C_Fujiwara_catalogues_1943.json.",
                          "results": results}, ensure_ascii=False, indent=2))
for result in results:
    print(json.dumps({key: result.get(key) for key in
                      ("name", "status", "final_url", "error", "byte_count", "elapsed_seconds")}
                     | {"forms": result.get("forms", []),
                        "relevant_lines": [line for line in result.get("text", "").splitlines()
                                           if any(term in line.lower() for term in
                                                  ("duke", "tubular", "fujiwara", "unavailable", "no result"))]},
                     ensure_ascii=False))
print(str(log))

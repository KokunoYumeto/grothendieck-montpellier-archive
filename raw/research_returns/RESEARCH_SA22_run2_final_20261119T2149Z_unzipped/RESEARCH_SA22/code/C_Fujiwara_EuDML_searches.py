"""Use the public EuDML advanced-search controls actually observed in HTML."""
import concurrent.futures
import datetime
import json
import urllib.parse
from C_Fujiwara_catalogues_1943 import ROOT, fetch

jobs = []
for name, field, query in [
    ("eudml_tubular_titles", "EQUALS_names", "tubular"),
    ("eudml_duke_journal", "EQUALS_journalName", "Duke Mathematical Journal"),
]:
    jobs.append((name, "https://eudml.org/searchForm?" + urllib.parse.urlencode({
        "SCHEME": "general", "OPERATOR": "AND", "expression-1": field,
        "search-box-1": query})))
jobs.append(("eudml_journals_d", "https://eudml.org/journals?prefix=d"))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, jobs))
log = ROOT / "logs" / "C_Fujiwara_EuDML_searches.json"
log.write_text(json.dumps({
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "provenance": "Advanced GET form /searchForm and EQUALS_names/EQUALS_journalName options read in eudml_advanced.html; D link read in eudml_journals.html.",
    "results": results}, ensure_ascii=False, indent=2))
for result in results:
    print(json.dumps({key: result.get(key) for key in
                      ("name", "status", "final_url", "error", "byte_count", "elapsed_seconds")},
                     ensure_ascii=False))
    print(result.get("text", "")[:18000])
print(str(log))

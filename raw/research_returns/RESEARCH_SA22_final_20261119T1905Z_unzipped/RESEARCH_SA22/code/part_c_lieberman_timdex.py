"""Read-only searches of MIT's explicitly advertised free discovery API.

Discovery: MIT Libraries news https://libraries.mit.edu/news/years-laboratory/34188/
links to https://timdex.mit.edu/. Its public home page documents this exact
GraphQL endpoint and the three requested fields. No authenticated operation,
protected content request, alternate endpoint, or retry after denial occurs.
"""
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.request

out = pathlib.Path(__file__).with_name("part_c_lieberman_timdex_output.json")
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
results = []
for term in ["Algebraic cycles on non singular complex projective varieties", "David Ira Lieberman"]:
    query = "{ search(searchterm: " + json.dumps(term) + ") { records { title sourceLink summary } } }"
    req = urllib.request.Request("https://timdex.mit.edu/graphql", data=json.dumps({"query": query}).encode(), headers={"Content-Type": "application/json"}, method="POST")
    tick = time.monotonic()
    record = {"term": term, "url": req.full_url, "method": "POST", "query": query}
    try:
        with urllib.request.urlopen(req, timeout=35) as response:
            body = response.read()
            record.update(status=response.status, final_url=response.url, bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), content_type=response.headers.get("Content-Type"))
            try:
                record["response"] = json.loads(body)
            except json.JSONDecodeError:
                record["text"] = body.decode("utf-8", "replace")[:20000]
    except Exception as error:
        record.update(error=type(error).__name__ + ": " + str(error))
        if isinstance(error, urllib.error.HTTPError):
            record["status"] = error.code
    record["seconds"] = time.monotonic() - tick
    results.append(record)
    if record.get("status") in (401, 403, 429) or "error" in record:
        break
payload = {"started_utc": started, "elapsed_seconds": time.monotonic() - clock, "requests": len(results), "discovery_refs": ["turn800752704view0", "turn901705507view0"], "results": results}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
out.with_suffix(".txt").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(payload, ensure_ascii=False, indent=2))

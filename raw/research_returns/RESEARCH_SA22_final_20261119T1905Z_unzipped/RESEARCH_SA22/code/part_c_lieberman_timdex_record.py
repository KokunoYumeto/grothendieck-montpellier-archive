"""One targeted metadata query; every requested field is in MIT API docs.
Docs opened: https://mitlibraries.github.io/timdex/reference/
The previous author/title searches found the exact thesis catalogue record.
"""
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.request

started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
query = '''{
  search(title: "Algebraic cycles on nonsingular complex projective varieties", booleanType: "AND") {
    hits
    records {
      title timdexRecordId source sourceLink citation publicationDate
      physicalDescription oclcs callNumbers contents summary
      contributors { kind value }
      dates { kind value note }
      identifiers { kind value }
      links { kind restrictions text url }
      notes { kind value }
      holdings { location collection callnumber format notes summary }
      relatedItems { description kind relationship uri value }
      rights { description kind uri }
    }
  }
}'''
req = urllib.request.Request("https://timdex.mit.edu/graphql", data=json.dumps({"query": query}).encode(), headers={"Content-Type": "application/json"}, method="POST")
payload = {"started_utc": started, "requests": 1, "url": req.full_url, "query": query, "docs_ref": "turn690313350view2"}
try:
    with urllib.request.urlopen(req, timeout=35) as response:
        data = response.read()
        payload.update(status=response.status, final_url=response.url, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), content_type=response.headers.get("Content-Type"))
        try:
            payload["response"] = json.loads(data)
        except json.JSONDecodeError:
            payload["text"] = data.decode("utf-8", "replace")[:20000]
except Exception as error:
    payload["error"] = type(error).__name__ + ": " + str(error)
    if isinstance(error, urllib.error.HTTPError):
        payload["status"] = error.code
payload["elapsed_seconds"] = time.monotonic() - clock
out = pathlib.Path(__file__).with_name("part_c_lieberman_timdex_record_output.json")
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
out.with_suffix(".txt").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(payload, ensure_ascii=False, indent=2))

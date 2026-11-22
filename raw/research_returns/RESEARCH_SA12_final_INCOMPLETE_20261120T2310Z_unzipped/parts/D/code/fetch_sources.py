"""Download explicitly identified primary sources; record byte provenance.

These files are research inputs, not proof certificates. Source availability
does not imply that any theorem in the source has been checked.
"""
import datetime, hashlib, json, pathlib, time, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = [
    ("Rydh_0710.2488_source.tar.gz", "https://arxiv.org/e-print/0710.2488"),
    ("Harman_Snowden_2301.13784_source.tar.gz", "https://arxiv.org/e-print/2301.13784"),
    ("Orgogozo2003.pdf", "https://www.numdam.org/article/BSMF_2003__131_1_123_0.pdf"),
    ("ESS_2102.13424_source.tar.gz", "https://arxiv.org/e-print/2102.13424"),
]
records=[]
for name,url in SOURCES:
    path=ROOT/'sources'/name
    start=time.monotonic()
    record=dict(name=name,url=url,date_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        data=urllib.request.urlopen(url,timeout=45).read()
        path.write_bytes(data)
        record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),status='downloaded')
    except Exception as exc:
        record.update(status='failed',error=str(exc))
    record['seconds']=round(time.monotonic()-start,3)
    records.append(record)
    print(json.dumps(record),flush=True)
(ROOT/'code'/'fetch_sources_output.json').write_text(json.dumps(records,indent=2)+'\n')

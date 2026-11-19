"""Replay of supplemental local fetch batches. Original outputs preserve actual successes/errors.
The saved records retain URLs and outcomes but not every request header; this replay
uses urllib with a browser user-agent for the successful batch. It does not claim
to reproduce an unavailable original header byte for byte.
This replay consolidates those small inline programs without rerunning downloads.
"""
from pathlib import Path
import urllib.request,subprocess,json,sys
R=Path(__file__).resolve().parents[1]
BATCHES={2: {'milnecft': 'https://www.jmilne.org/math/CourseNotes/CFT.pdf', 'krull': 'https://www.math.purdue.edu/~heinzer/preprints/2020-5-31power.pdf', 'milneag': 'https://www.jmilne.org/math/Books/iAG2017.pdf'}, 3: {'milnecft': 'https://www.jmilne.org/math/CourseNotes/CFT.pdf', 'milneadt': 'https://www.jmilne.org/math/Books/ADTnot.pdf', 'armstrong': 'https://wrap.warwick.ac.uk/id/eprint/74313/1/WRAP_Thesis_Armstrong_1966.pdf'}}
n=int(sys.argv[1]);results=[]
for key,url in BATCHES[n].items():
 try:
  headers={"User-Agent":"Mozilla/5.0"} if n==3 else {}
  with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as h:data=h.read()
  p=R/"external"/(key+".pdf");p.write_bytes(data)
  c=subprocess.run(["pdftotext","-layout",str(p),str(p.with_suffix(".txt"))],capture_output=True)
  results.append(dict(key=key,url=url,bytes=len(data),pdftotext=c.returncode))
 except Exception as e:results.append(dict(key=key,url=url,error=str(e)))
print(json.dumps(results,indent=2))

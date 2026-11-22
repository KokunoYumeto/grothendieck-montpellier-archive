"""Read public scholarly-metadata APIs for lawful original-source locations."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen, Request
from urllib.parse import quote
from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
dois={"EarleMarden2012":"10.1090/conm/575/11411",
      "Marden1987":"10.1142/9789812798411_0016"}
jobs=[]
for name,doi in dois.items():
    jobs.extend([
        (name,"OpenAlex","https://api.openalex.org/works/https://doi.org/"+doi),
        (name,"Crossref","https://api.crossref.org/works/"+quote(doi,safe="")),
        (name,"SemanticScholar","https://api.semanticscholar.org/graph/v1/paper/DOI:"+doi+"?fields=title,openAccessPdf,url"),
        (name,"OpenAIRE","https://api.openaire.eu/search/publications?doi="+quote(doi,safe="")+"&format=json")
    ])
def fetch(job):
    name,service,url=job
    result={"work":name,"service":service,"url":url}
    try:
        with urlopen(Request(url,headers={"User-Agent":"Mathematical-source-research/1.0"}),timeout=22) as response:
            data=json.load(response)
        result["status"]="opened metadata"
        result["data"]=data
        if service=="OpenAlex":
            result["locations"]=data.get("locations")
            result["oa"]=data.get("open_access")
        elif service=="Crossref":
            result["locations"]=data["message"].get("link")
            result["oa"]=data["message"].get("license")
        elif service=="SemanticScholar":
            result["locations"]=data.get("openAccessPdf")
        else:
            result["locations"]="Full metadata saved for structured inspection."
    except Exception as exc:
        result["status"]=type(exc).__name__+": "+str(exc)
    return result
results=[]
with ThreadPoolExecutor(max_workers=8) as pool:
    for future in as_completed([pool.submit(fetch,job) for job in jobs]):
        result=future.result()
        results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!="data"},ensure_ascii=False),flush=True)
(root/"sources/part_a567_retrieval_metadata.json").write_text(json.dumps(results,indent=2,ensure_ascii=False))

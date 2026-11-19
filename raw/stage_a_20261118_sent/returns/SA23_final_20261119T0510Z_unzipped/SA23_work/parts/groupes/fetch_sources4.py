"""Further exact primary references; raw texts remain external to the deliverable."""
from fetch_sources import retrieve, BASE
import concurrent.futures,json
SOURCES={
 'olivier-1967':'https://www.numdam.org/item/SAC_1967-1968__2__A6_0.pdf',
 'beke-presheaf':'https://faculty.uml.edu/tbeke/presheaf.pdf',
 'beke-sheafi':'https://faculty.uml.edu/tbeke/sheafi.pdf',
 'bird-thesis':'https://science.mq.edu.au/~street/BirdPhD.pdf',
 'sga4-IV-retype':'https://www.normalesup.org/~forgogozo/SGA4/04/04.pdf',
}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
  results=list(pool.map(retrieve,SOURCES.items()))
 (BASE/'retrieval_audit4.json').write_text(json.dumps(results,indent=2)+'\n')
 print(json.dumps(results,indent=2))

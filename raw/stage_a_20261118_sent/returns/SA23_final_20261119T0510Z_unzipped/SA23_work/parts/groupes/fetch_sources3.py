from fetch_sources import retrieve, BASE
import concurrent.futures,json
SOURCES={
'caramello-johnstone-fields':'https://arxiv.org/pdf/0808.1972',
'stevenson-flat':'https://arxiv.org/pdf/1210.0399',
'lack-tendas-2205.11056':'https://arxiv.org/pdf/2205.11056',
'lazard-bourbaki109':'https://www.numdam.org/item/SB_1954-1956__3__77_0.pdf',
'vickers-geometric-databases':'https://sjvickers.github.io/GeoTh%2BDBs.pdf',
'vickers-au-classifiers':'https://cahierstgdc.com/wp-content/uploads/2018/01/Vickers-58-34.pdf',
}
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:
        results=list(p.map(retrieve,SOURCES.items()))
    (BASE/'retrieval_audit3.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))

"""Public primary texts for exact-locus checking; downloaded texts are not deliverables."""
from fetch_sources import retrieve, BASE
import concurrent.futures,json
SOURCES={
'schroer-fppf':'https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/points_fppf.pdf',
'gabber-kelly-1407.5782':'https://arxiv.org/pdf/1407.5782',
'colimit-dense-2019':'https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1904/abrocaporo.pdf',
'makkai-pitts-1987':'https://www.cl.cam.ac.uk/~amp12/papers/reslfp/reslfp.pdf',
'adamek-lawvere-rosicky-2003':'https://lawverearchives.com/wp-content/uploads/2024/12/2003-on-the-duality-between-varieties-and-algebraic-theories.pdf',
'lack-power-2009':'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/15991DB3A44153A628968282D8287C20/S0956796809007254a.pdf/gabrielulmer_duality_and_lawvere_theories_enriched_over_a_general_base.pdf',
'bunge-lack-2003':'https://citeseerx.ist.psu.edu/document?doi=42a1ad01fe31800d5b7cb68e39c3ea448d88a656&repid=rep1&type=pdf',
'brooke-taylor-rosicky-images':'https://research-information.bris.ac.uk/files/76555296/accim6.pdf',
'adamek-rosicky-1996':'https://dml.cz/bitstream/handle/10338.dmlcz/118845/CommentatMathUnivCarolRetro_37-1996-2_20.pdf',
'garner-1307.2963':'https://arxiv.org/pdf/1307.2963',
}
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:
        results=list(p.map(retrieve,SOURCES.items()))
    (BASE/'retrieval_audit2.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))

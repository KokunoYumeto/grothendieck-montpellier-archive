from fetch_primary_sources import fetch,ROOT
from concurrent.futures import ThreadPoolExecutor
import json
SOURCES={
'Milne_1999_Lefschetz':'https://www.jmilne.org/math/articles/1999bP.pdf',
'Kisin_2017':'https://people.math.harvard.edu/~kisin/dvifiles/lr.pdf',
'van_Hoften_Sempliner_2026':'https://polvanhoften2.github.io/Pol%20van%20Hoften%20and%20Jack%20Sempliner%20-%20The%20Hodge%20conjecture%20for%20CM%20abelian%20varieties.pdf',
'Milne_2002_Polarizations':'https://www.jmilne.org/math/articles/2002a.pdf',
}
with ThreadPoolExecutor(max_workers=4) as ex: records=list(ex.map(fetch,SOURCES.items()))
(ROOT/'code'/'fetch_additional_sources_output.json').write_text(json.dumps(records,indent=2))
for r in records: print(r['name'],r['status'],r.get('bytes',r.get('error')),r['seconds'])

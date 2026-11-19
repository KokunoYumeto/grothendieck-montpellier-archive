"""Archive the two primary sources inspected for the finite-tensor audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
from fetch_c6_sources import fetch

sources = {
    'MilneAlgebraicGroups2022':'https://www.jmilne.org/math/Books/iAG2022.pdf',
    'Meir2023Interpolation':'https://arxiv.org/pdf/2105.04622',
    'Procesi2021Tensor':'https://arxiv.org/pdf/2011.10820',
}
with ThreadPoolExecutor(max_workers=2) as pool:
    records=list(pool.map(fetch,sources.items()))
text=json.dumps(records,indent=2)
Path(__file__).with_name('fetch_c1_audit_sources_output.json').write_text(text+'\n')
print(text)

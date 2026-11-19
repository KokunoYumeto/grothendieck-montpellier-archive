"""Archive the actually opened contextual sources; no GIT text claimed."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
from fetch_c6_sources import fetch, fetch_html

pdfs={
 'Lipman1969':'https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf',
 'LarsenLunts2001':'https://arxiv.org/pdf/math/0110255',
}
with ThreadPoolExecutor(max_workers=2) as pool:
    rows=list(pool.map(fetch,pdfs.items()))
rows.append(fetch_html(('MumfordGITPublisher2026','https://link.springer.com/book/9783540569633')))
text=json.dumps(rows,indent=2)
Path(__file__).with_name('fetch_contextual_sources_output.json').write_text(text+'\n')
print(text)

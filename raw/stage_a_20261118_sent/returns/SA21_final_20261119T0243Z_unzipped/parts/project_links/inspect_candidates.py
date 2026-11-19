"""Display selected search results without making match decisions."""
from pathlib import Path
import json, sys
p=Path(__file__).parent
data=json.loads((p/'candidate_hits.json').read_text())
base=Path('/workspace/scratch/4017236f14bf')
roots={'package69':base/'prior_context/extracted',
       'package138':base/'prior_context_138/extracted'}
for key in sys.argv[1:]:
    print('\nTARGET',key)
    for hit in data[key]['hits']:
        line=(roots[hit['package']]/hit['path']).read_text().splitlines()[hit['line']-1]
        print(f"{hit['package']}/{hit['path']}:{hit['line']}: {line}")

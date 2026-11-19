"""Archive additional primary sources used in the third research interval."""
from fetch_primary_sources import fetch, ROOT
from concurrent.futures import ThreadPoolExecutor
import json

SOURCES = {
    'Conrad_2006_Trace': 'https://virtualmath1.stanford.edu/~conrad/papers/Kktrace.pdf',
    'deJong_1996_Alterations': 'https://www.numdam.org/item/PMIHES_1996__83__51_0.pdf',
    'Fontaine_1992_BlochKato': 'https://www.imo.universite-paris-saclay.fr/~fontaine/bourbakiblochkato.pdf',
    'Soule_2003_Torsion': 'https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-kato/soule.dm.pdf',
}

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as executor:
        records = list(executor.map(fetch, SOURCES.items()))
    (ROOT / 'code' / 'fetch_followup_sources_output.json').write_text(
        json.dumps(records, indent=2) + '\n'
    )
    for record in records:
        print(record['name'], record['status'],
              record.get('bytes', record.get('error')), record['seconds'])

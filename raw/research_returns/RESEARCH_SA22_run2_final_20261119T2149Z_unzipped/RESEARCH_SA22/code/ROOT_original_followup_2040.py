#!/usr/bin/env python3
"""Record four observed public catalogue/abstract pages; no protected text."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import time
from fetch_sources import fetch

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc)
begin = time.perf_counter()
jobs = [
    ('https://profs.provost.nagoya-u.ac.jp/html/100000275_en.html',
     root/'literature/ROOT_Fujiwara_Nagoya_profile_2040.html'),
    ('https://ndlsearch.ndl.go.jp/en/books/R100000039-I3115841',
     root/'literature/ROOT_Fujiwara_dissertation_NDL_2040.html'),
    ('https://gakui.dl.itc.u-tokyo.ac.jp/cgi-bin/gazo.cgi?no=211961',
     root/'literature/ROOT_Fujiwara_dissertation_abstract_2040.html'),
    ('https://www.ma.huji.ac.il/~ijmath/',
     root/'literature/ROOT_Israel_journal_home_2040.html'),
]
with ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(lambda job: fetch(*job), jobs))
result = {
    'started_utc': started.isoformat(),
    'finished_utc': datetime.now(timezone.utc).isoformat(),
    'seconds': time.perf_counter()-begin,
    'scope': 'Four observed public profile/catalogue/abstract pages only. The NDL record explicitly restricts dissertation transmission; no dissertation file or protected endpoint is requested. Journal homepage web retrieval had returned a gateway error, so this is one bounded ordinary HTTP retry of the same public homepage, not an access-control workaround.',
    'requests': records,
    'mathematical_effect': 'No original Gabber1994 or Fujiwara1995 theorem passage obtained by these metadata/abstract requests.',
}
(root/'logs/ROOT_original_followup_2040.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))

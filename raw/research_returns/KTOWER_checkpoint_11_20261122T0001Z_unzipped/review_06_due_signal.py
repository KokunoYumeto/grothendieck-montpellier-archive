"""Signal the next review; never assess movement automatically."""
from datetime import datetime,timezone
import time
due=datetime.fromisoformat('2026-11-21T23:30:46+00:00')
while True:
    remaining=(due-datetime.now(timezone.utc)).total_seconds()
    if remaining<=0:break
    time.sleep(min(30,remaining))
print('Review06 is due. Root must perform the actual comparison against review05; no review has been recorded by this signal.',flush=True)

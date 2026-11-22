"""Signal the next actual progress review; never assess movement automatically."""
from datetime import datetime,timezone
import time

due=datetime.fromisoformat('2026-11-22T00:30:46+00:00')
while True:
    remaining=(due-datetime.now(timezone.utc)).total_seconds()
    if remaining<=0:
        break
    time.sleep(min(30,remaining))
print('Review07 is due. Root must compare the actual gates with review06. If no movement is found, stop research under the user rule and finalize. This signal has not recorded a review.',flush=True)

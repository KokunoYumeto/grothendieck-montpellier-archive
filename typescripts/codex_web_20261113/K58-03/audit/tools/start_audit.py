from datetime import datetime, timezone
from pathlib import Path
import sys
n = int(sys.argv[1])
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
path = Path(f'work/audit_{n:03}_start')
if not path.exists(): path.write_text(stamp+'\n')
print(path.read_text().strip())

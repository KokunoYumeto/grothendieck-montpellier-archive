"""Archive the exact primary author version consulted for one Chow fact."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
from urllib.request import urlopen

root = Path(__file__).resolve().parents[2]
url = 'https://www.math.uni-bielefeld.de/~vial/CK-fibrations9.pdf'
target = root / 'part_c/sources/vial_ck_fibrations2012.pdf'
with urlopen(url, timeout=45) as response:
    payload = response.read()
assert payload.startswith(b'%PDF')
target.write_bytes(payload)
subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], check=True)
result = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'url': url,
    'pdf': str(target.relative_to(root)),
    'text': str(target.with_suffix('.txt').relative_to(root)),
    'bytes': len(payload),
    'sha256': hashlib.sha256(payload).hexdigest(),
    'run_history': 'The first invocation stopped before network access because the optional requests module was unavailable. The final script uses the Python standard-library urllib client.',
    'scope': 'Author version dated 11 May 2012. Lemma4.5 and its entire proof, authorp13, read. It states rational Chow base-extension injectivity; no audit of the main theorem is claimed.',
}
out = Path(__file__).with_name('fetch_vial_base_extension_source_output.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))

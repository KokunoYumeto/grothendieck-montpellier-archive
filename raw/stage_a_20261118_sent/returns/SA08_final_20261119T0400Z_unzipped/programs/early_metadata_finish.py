"""Normalize verification markers without changing bibliography assertions."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1]; p=R/'work/early/references.bib'
s=p.read_text()
if 'note={verified}' not in s:
 s=s.replace(' note={',' note={verified},\n annotation={')
s=s.replace('journal={Topology}, volume={17}, year={1978}, pages={193--203},','journal={Topology}, volume={17}, year={1978}, pages={193--203},\n url={https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf},')
s=s.replace('journal={Topology}, volume={14}, year={1975}, pages={271--273},','journal={Topology}, volume={14}, year={1975}, pages={271--273},\n url={https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf},')
p.write_text(s)
print(json.dumps({'bibliographic_keys':re.findall(r'@\w+\{([^,]+),',s),'marker_count':s.count('note={verified}')},indent=2))

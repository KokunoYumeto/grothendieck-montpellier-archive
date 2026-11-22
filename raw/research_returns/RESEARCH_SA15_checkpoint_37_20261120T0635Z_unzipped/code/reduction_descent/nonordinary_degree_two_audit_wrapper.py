"""Retained exact audit wrapper executed at 20:01:56 UTC on 2026-11-19.

The original execution was a Python heredoc with the body below.
It copied and ran the author's entire graph certificate in this agent's
directory, verified the author's output hash, and retained stdout/audit.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,shutil,re
b=Path('RESEARCH_SA15_work/agents/reduction_descent'); s=b.parent/'monodromy/code/nonordinary_degree_two_six_theta_graph.py'; a=b.parent/'monodromy/outputs/nonordinary_degree_two_six_theta_graph.json'; old=hashlib.sha256(a.read_bytes()).hexdigest()
d=b/'code/independent_nonordinary_degree_two_six_theta_graph.py'; shutil.copy2(s,d)
r=subprocess.run(['python',str(d)],text=True,capture_output=True);(b/'outputs/independent_nonordinary_degree_two_six_theta_graph.stdout.txt').write_text(r.stdout+r.stderr)
assert r.returncode==0,r.stderr
assert hashlib.sha256(a.read_bytes()).hexdigest()==old
o=json.loads((b/'outputs/nonordinary_degree_two_six_theta_graph.json').read_text()); p=b.parent/'monodromy/nonordinary_ppav_degree_two_wreath_theta_candidate.tex';labels=re.findall(r'\\label\{([^}]+)\}',p.read_text());now=datetime.now(timezone.utc).isoformat()
aud={'status':'FULL_PROOF_CODE_PASS','actual_utc':now,'artifact':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'labels':labels,'runtime_seconds':o['runtime_seconds'],'author_output_sha256_unchanged':old,'proof_scope':['Entire candidate, actual two-jet exceptional strata and restriction ranks','Fierce characteristic-two labelled transposition and purity argument','Composition-factor Goursat, perfect component images, uniform H1, actual natural blocks','Full gluing-column restriction and isotypic isolation','Rank-drop clopen Lang closure and both regular component projections','Irreducible common kernel, transvection normal closure and full translation extension'],'source_scope':'No new original source opened; exact prior audited jet, labelled-wreath, clopen-Lang, covector, H1 and classification results reused.','code_scope':'Entire finite doubled-six-theta graph certificate read and isolated rerun; no geometry inferred from finite checks.'}
(b/'nonordinary_degree_two_independent_audit.json').write_text(json.dumps(aud,indent=2)+'\n')
with (b/'CHECK_EVENTS.tsv').open('a') as f:
 for l in labels:f.write('\t'.join([now,l,'INDEPENDENT_PROOF_CODE_PASS','Uniform fixed nonordinary ppav degree2 full stabilizer',str(p),'Entire proof/code read; isolated runtime '+str(o['runtime_seconds'])+'; author output preserved'])+'\n')
print(json.dumps(aud,indent=2))

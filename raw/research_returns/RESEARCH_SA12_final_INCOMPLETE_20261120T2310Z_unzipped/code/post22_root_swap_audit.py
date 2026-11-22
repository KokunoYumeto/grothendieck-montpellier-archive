"""Record the full root swap proof/source audit, distinct from finite algebra checks."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
path='parts/C/post22_research/D_wild_one_curve_swap_obstruction.tex'
expected='8b06b3930b5061131306735cd158761e4b58b5370bebb4719153df8f9fafccb6'
assert hashlib.sha256((root/path).read_bytes()).hexdigest()==expected
r={'utc':datetime.now(timezone.utc).isoformat(),'actor':'GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
 'type':'targeted proof check','verdict':'PASS','path':path,'sha256':expected,
 'actual_read_scope':'Complete actual-file proof. Fresh retained published-layout Keel primary text: Theorem0.2; complete written§1.0–1.10 including Proposition1.6 and Lemma1.10; Section3 Theorem3.0, Lemmas3.2–3.5 and the written proof of3.0. Direct Proposition1.6 is the input; no omitted upstream dependency is claimed re-proved.',
 'primary_reads':[
  {'url':'https://arxiv.org/abs/math/9901149','file':'parts/C/sources/post22_Keel1999/published_layout_arxiv.txt','scope':'Exact retained published-layout sections listed above; direct H+2D application.'},
  {'url':'https://stacks.math.columbia.edu/tag/03H0','scope':'Complete written Stein-factorization theorem and proof'},
  {'url':'https://stacks.math.columbia.edu/tag/0C23','scope':'Complete normal-completion statement and written proof'},
  {'url':'https://stacks.math.columbia.edu/tag/0C22','scope':'Complete normality ascent statement and written proof'},
  {'url':'https://stacks.math.columbia.edu/tag/07C1','scope':'Complete regular base-change statement and written proof'},
  {'url':'https://stacks.math.columbia.edu/tag/07QI','scope':'Complete regular-composition statement and written proof, retaining its explicit omitted-details qualification'},
  {'url':'https://stacks.math.columbia.edu/tag/07QS','scope':'Definitions15.53.1 and Lemma15.53.2, Proposition15.53.3 and their complete written proofs; omitted source localization proof not claimed read'}],
 'checks':['Symmetric complete local quotient and rank-two flat algebra; x↦x+u involution.',
 'Actual Cartier H built from X_c, finite descent of ampleness, full intersection table and norm argument for2-torsion restriction.',
 'Direct Keel1.6 contraction, two normal Stein factors, connected diagonal implies exactly one point above the contracted point.',
 'Excellent normal completions are domains; finite algebra completion has one factor, preserving connected degree-two punctured torsor.',
 'Regular base change retains the smooth exceptional curve and its conormal; finite normalization gives e1 and inseparable residue degree2.',
 'The Artin–Schreier leading pole has nonsquare residue; the class cannot extend across the resolution.',
 'No counting or finite-generation theorem is refuted by this example.'],
 'finite_certificate':'code/output/wild_swap_local_certificate_root.json',
 'movement':'Auxiliary refutation of automatic radial tameness only; no requested status or strongest-main-gate change.'}
out=root/'parts/C/post22_research/audit_wild_swap_root.json';assert not out.exists()
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'record':str(out.relative_to(root)),'verdict':'PASS'}))

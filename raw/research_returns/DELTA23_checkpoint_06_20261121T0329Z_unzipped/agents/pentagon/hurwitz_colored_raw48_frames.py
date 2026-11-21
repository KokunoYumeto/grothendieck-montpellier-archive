#!/usr/bin/env python3
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;start=time.monotonic();d=np.load(HERE/'hurwitz_colored_raw48_gentle.npz');s,r,X,Y=d['s'],d['r'],d['x'],d['y'];one=np.arange(len(s))
states=pickle.loads((HERE/'hurwitz_colored_raw48_gentle_state.pkl').read_bytes());D=PermutationGroup(states[1][0]);D.__dict__.update(states[1][1]);assert D.order()==4096
els=[np.array(g.array_form)for g in D.generate_schreier_sims()]
def powp(p,e):
 o=one.copy()
 for _ in range(e):o=o[p]
 return o
q=powp(X,6)[powp(Y,6)];cubic={};harmonic=[{},{}]
for i,a in enumerate(els):
 ai=np.argsort(a);cubic.setdefault(a[r[ai]].tobytes(),i);harmonic[0].setdefault(a[s[ai]].tobytes(),i)
 b=q[a];bi=np.argsort(b);harmonic[1].setdefault(b[s[bi]].tobytes(),i)
rows=[];saved={}
for i,f in enumerate(d['all_gentle']):
 cn=np.argsort(f)[r];sn=s[f]
 cpass=cn.tobytes()in cubic;hpass=[sn.tobytes()in h for h in harmonic]
 rawf=f[:48];cov=np.array_equal(rawf[d['raw_C'][np.argsort(rawf)]],d['new_C'])
 row={'gentle_index':i,'raw_C_covariance':bool(cov),'derived_cubic_frame':cpass,'harmonic_ab0_frame':hpass[0],'harmonic_ab66_frame':hpass[1],'strong_actual_frames':cpass and any(hpass)};rows.append(row);print(row,flush=True)
 if cpass:saved[f'cubic_{i}']=els[cubic[cn.tobytes()]]
 for j,yes in enumerate(hpass):
  if yes:saved[f'harmonic_{j}_{i}']=els[harmonic[j][sn.tobytes()]]if j==0 else q[els[harmonic[j][sn.tobytes()]]]
np.savez_compressed(HERE/'hurwitz_colored_raw48_frames.npz',**saved)
(HERE/'hurwitz_colored_raw48_frames.json').write_text(json.dumps({'counts':{'cubic_class':len(cubic),'harmonic_ab0_class':len(harmonic[0]),'harmonic_ab66_class':len(harmonic[1])},'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Exact necessary H10 torsion-conjugator cosets in new raw48 finite S3 core.'},indent=2)+'\n')

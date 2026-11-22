"""Reuse supplied exact tensor-Hecke arithmetic to check the trace input of G012.
This is a reused-input check, not independent Hecke arithmetic.
"""
import os,sys,json
from pathlib import Path
os.environ['HN']='3'
p=Path('sources/OURS_E4_scripts').resolve();sys.path.insert(0,str(p))
scope={'__file__':str(p/'hexagon.py')}
src=(p/'hexagon.py').read_text().split('G=sp.Matrix')[0]
exec(src,scope)
sp=scope['sp'];v=sp.Symbol('v')
vals={b:sp.cancel(scope['tau'](scope['E'][b]).subs(v,sp.I))
      for b in ['Sigma','g2_1','g2_12','g2_21','g2_2']}
assert list(vals.values())==[0,0,16,16,0]
Path('work/gct/signpoint_Hecke_trace.json').write_text(json.dumps({b:str(c) for b,c in vals.items()},indent=2))
print(vals)

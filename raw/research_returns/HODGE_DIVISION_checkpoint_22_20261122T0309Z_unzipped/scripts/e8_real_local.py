"""Check real E8 local norm factors; no period-map claim."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'agents/g34_eightfolds/g31'))
import gaussian_exact as M
from check_local_discriminants import inert_parities
data=json.loads((ROOT/'research/e8_class_exploration.json').read_text())
H=[[M.F(a) for a in row] for row in data['cartan']]
rows=[]
for item in data['classes']:
    g=[[M.F(a) for a in row] for row in item['matrix']]
    a=M.sub(M.eye(8),g);cols=M.rref(a)[1];d=len(cols)
    if d:
        U=M.tr([M.tr(a)[j] for j in cols]);selected=M.rref(M.tr(U))[1]
        action=M.mul(M.inv([U[j] for j in selected]),[M.mul(g,U)[j] for j in selected])
        assert M.mul(U,action)==M.mul(g,U)
        gramdet=M.det(M.mul(M.mul(M.star(U),H),U))
        b=M.det(M.sub(M.eye(d),action))
    else:gramdet=b=M.ONE
    assert not gramdet.b and not b.b and gramdet.a>0 and b.a>0
    q=gramdet.a/b.a;assert not inert_parities(q)
    rows.append({'index':item['index'],'name':item['name'],'moving_rank':d,'q':str(q)})
(ROOT/'research/e8_real_local.json').write_text(json.dumps({'status':'PASS','classes':rows},indent=2)+'\n')
print('PASS: all112 real E8 local factors are Gaussian norms.')

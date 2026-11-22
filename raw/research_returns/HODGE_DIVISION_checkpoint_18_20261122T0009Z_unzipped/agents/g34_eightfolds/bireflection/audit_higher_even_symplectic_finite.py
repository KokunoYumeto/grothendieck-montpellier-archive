#!/usr/bin/env python3
"""Independent finite-only HES-F audit, including the new full S12(2) table."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
from audit_higher_even_symplectic import reality

B=Path(__file__).resolve().parent
SOURCE=B.parents[1]/'imprimitive/lie_small_fields/sp2n2_character_inputs.json'


def main():
    start=time.perf_counter();raw=SOURCE.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='5d3539d84b4988ac34c2703cbc81369b2840e50e3d74ea3afbb2db31f974e615'
    D=json.loads(raw);ts={t['name']:t for t in D['tables']}
    assert set(ts)=={'S8(2)','S10(2)','S12(2)'}
    out={'status':'PASS unconditional finite arithmetic','input_sha256':hashlib.sha256(raw).hexdigest(),
         'all_rows':0,'nonidentity_entries':0,'tables':[]}
    for name,n,nrows,minimum,c in [('S8(2)',4,81,35,F(3,5)),
                                  ('S10(2)',5,198,155,F(17,31)),
                                  ('S12(2)',6,477,651,F(11,21))]:
        t=ts[name];cs=t['characters']
        expected=('computed by Christoph Koehler using the group and char. theor. methods'
                  if name=='S12(2)' else 'origin: ATLAS of finite groups, tests: 1.o.r.')
        assert t['information']==expected
        assert t['extension_info']==['','']
        assert len(cs)==len(t['sizes'])==len(t['orders'])==nrows
        order=2**(n*n)
        for i in range(1,n+1):order*=2**(2*i)-1
        assert order==t['order']==sum(t['sizes'])==sum(row[0]**2 for row in cs)
        assert min(row[0] for row in cs if row[0]>1)==minimum
        assert len([row for row in cs if row[0]==1])==1
        best=F(0);witness=[];count=0
        for i,row in enumerate(cs):
            assert len(row)==nrows
            a=row[0]
            for j,z in enumerate(row):
                if isinstance(z,int):bound=abs(z)
                else:
                    N,coeff=z;assert reality(N,tuple(coeff))
                    bound=sum(abs(v) for v in coeff)
                if a==1 or j==0:continue
                q=F(bound,a);assert q<=c<=F(3,5);count+=1
                if q>best:best=q;witness=[]
                if q==best and isinstance(z,int):
                    witness.append({'row':i+1,'class':j+1,'degree':a,'value':z,'order':t['orders'][j]})
        assert best==c and witness and any(w['degree']==minimum and w['order']==2 for w in witness)
        out['all_rows']+=nrows;out['nonidentity_entries']+=count
        out['tables'].append({'name':name,'provenance':t['information'],'rows':nrows,'entries':count,'minimum_degree':minimum,
                              'maximum_ratio':str(best),'attainment':witness})
    assert (out['all_rows'],out['nonidentity_entries'])==(756,271785)
    assert (1-F(3,5))/2==F(1,5)
    assert F(6)/(1+10*F(1,5)-2)==6<35
    out['elapsed_seconds']=round(time.perf_counter()-start,6)
    B.joinpath('audit_higher_even_symplectic_finite.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()

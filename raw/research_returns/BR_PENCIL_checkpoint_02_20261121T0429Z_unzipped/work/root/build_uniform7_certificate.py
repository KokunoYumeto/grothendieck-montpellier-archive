"""Extract explicit integer-matrix minors from the uniform7 searches."""
from pathlib import Path
import json,time,math
from verify_det7_global import detmod,koszul_minor

HERE=Path(__file__).resolve().parent
PRIME=1000003

def tensor(selected,c,sign):
    support=sorted({c*i+j for I,J in selected for i in I for j in J});pos={v:i for i,v in enumerate(support)};T={}
    for h,((i,j),(a,b)) in enumerate(selected):
        u,v,w,z=[pos[q] for q in [c*i+a,c*i+b,c*j+a,c*j+b]]
        for x,y,value in [(u,z,1),(z,u,1),(v,w,sign),(w,v,sign)]:T[h,x,y]=value
    return support,T

def main():
    start=time.time();data=json.loads((HERE/'uniform7_exploration.json').read_text())
    bdata={(q['graph'],q['subset_index'],q['family']):q for q in json.loads((HERE/'uniform7_support_koszul.json').read_text())['records']}
    graphs=[];count=0
    for gi,G in enumerate(data['graphs']):
        graph={k:G[k] for k in ['r','c','rows','edges','rectangles','all_support_exact_subsets']};records=[]
        for qi,rec in enumerate(G['subset_orbits']):
            case={k:rec[k] for k in ['subset','rectangles','orbit_size']};case['families']={}
            for fam,sign in [('det',-1),('per',1)]:
                support,T=tensor(rec['rectangles'],G['c'],sign)
                choices=[q for q in rec['families'][fam]['certificates'] if q['bound']>=14]
                if choices:
                    q=min(choices,key=lambda q:q['pure_cost']);p=q['p'];n=13*q['pure_cost']+1
                    rows=q['rows'][:n];cols=q['cols'][:n]
                    value=detmod(koszul_minor(rec['subset'],support,T,'A',p,rows,cols),PRIME);assert value
                    cert={'type':'A','p':p,'cost':q['pure_cost'],'rows':rows,'cols':cols,'order':n,'determinant_mod_p':value}
                else:
                    q=next(q for q in bdata[gi,qi,fam]['certificates'] if q['bound']>=14);p=q['p'];bs=[];total=0
                    for block in q['blocks']:
                        rows=block['rows'];cols=block['cols'];n=len(rows)
                        value=detmod(koszul_minor(rec['subset'],support,T,'B',p,rows,cols),PRIME);assert value
                        bs.append({'weight':block['weight'],'rows':rows,'cols':cols,'order':n,'determinant_mod_p':value});total+=n
                    assert total==q['rank']>13*q['cost']
                    cert={'type':'B','p':p,'cost':q['cost'],'rank':total,'blocks':bs}
                case['families'][fam]=cert
            records.append(case);count+=1
        graph['records']=records;graphs.append(graph)
        print('graph',gi+1,'records',count,'seconds',round(time.time()-start,2),flush=True)
    output={'finding':'R-11','scope':'characteristic zero','prime':PRIME,'graph_count':len(graphs),'subset_orbits':count,'graphs':graphs}
    (HERE/'uniform7_certificate.json').write_text(json.dumps(output,separators=(',',':'))+'\n')
    print('DONE',len(graphs),count,time.time()-start,flush=True)

if __name__=='__main__':main()

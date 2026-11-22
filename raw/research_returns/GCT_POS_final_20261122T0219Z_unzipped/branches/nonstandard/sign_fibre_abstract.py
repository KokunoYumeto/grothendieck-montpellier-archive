"""Exact abstract rational-order fibre at D=0, distinguished from its image.

Uses the actual free Q[D] basis and full table of N019.  Computes both
the ordinary regular trace form and the pullback of the ambient Hecke
symmetrizing trace.  These are different forms and must not be confused.
Exploratory until the accompanying proof and independent review exist.
"""
from pathlib import Path
import sys,gzip,json,time
from flint import fmpq,fmpq_mat

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'dependencies'))
import e4lib as h


def length(w):return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    with gzip.open(HERE/'gt_hermite_multiplication_table.json.gz','rt') as f:products=json.load(f)
    table=[[{int(k):fmpq(p['0']) for k,p in row.items() if p.get('0','0')!='0'}
             for row in block] for block in products['multiplication']]
    n=len(table);assert n==114
    keys=[(tuple(a),tuple(b)) for a,b in data['ambient_coordinates']]
    image=[]
    for row in data['rows']:
        image.append([fmpq(row['ambient_coordinates'].get(str(z),{}).get('0','0'))
                      if (length(a)+length(b))%2==0 else fmpq(0)
                      for z,(a,b) in enumerate(keys)])
    image_rank=fmpq_mat(image).rank()
    # C_w is obtained from C'_w by v->v^-1, T_x->(-1)^length(x)T_x,
    # and the overall sign (-1)^length(w).  Only its T_identity
    # coefficient is required for the ambient symmetrizing trace.
    tauC={}
    for w in h.G:
        real=imag=0
        for exponent,c in h.Cp[w].get(h.e,{}).items():
            value=c*(-1)**length(w);k=(-exponent)%4
            if k==0:real+=value
            elif k==1:imag+=value
            elif k==2:real-=value
            else:imag-=value
        tauC[w]=(real,imag)
    weights=[]
    for a,b in keys:
        x,y=tauC[a];u,v=tauC[b]
        if (length(a)+length(b))%2==0:assert x*v+y*u==0
        weights.append((1 if a==b else 2)*(x*u-y*v))
    canonical=[sum((p*w for p,w in zip(row,weights)),fmpq(0)) for row in image]
    regular=[sum((table[i][j].get(j,fmpq(0)) for j in range(n)),fmpq(0)) for i in range(n)]
    assert canonical[0]==1 and regular[0]==114
    def gram(trace):return [[sum((c*trace[k] for k,c in table[i][j].items()),fmpq(0))
                              for j in range(n)] for i in range(n)]
    Gcanonical=gram(canonical);Gregular=gram(regular)
    assert Gcanonical==list(map(list,zip(*Gcanonical)))
    assert Gregular==list(map(list,zip(*Gregular)))
    canonical_rank=fmpq_mat(Gcanonical).rank();regular_rank=fmpq_mat(Gregular).rank()
    result={'status':'COMPUTED_PENDING_PROOF_REVIEW','scope':'Abstract Q[D] order fibre at0, not only its specialized ambient image; not VIII E(4).',
            'abstract_dimension':n,'ambient_image_dimension':image_rank,
            'ambient_kernel_dimension':n-image_rank,
            'ambient_symmetrizing_trace_Gram_rank':canonical_rank,
            'regular_trace_Gram_rank':regular_rank,
            'regular_trace_radical_dimension':n-regular_rank,
            'seconds':time.time()-started}
    (HERE/'sign_fibre_abstract_verified.json').write_text(json.dumps(result,indent=2)+'\n')
    cert={'basis_labels':data['coordinate_labels'],'ambient_image':[[str(x) for x in row] for row in image],
          'specialized_products':[[{str(k):str(c) for k,c in row.items()} for row in block] for block in table],
          'canonical_trace':[str(x) for x in canonical],'regular_trace':[str(x) for x in regular],
          'canonical_Gram':[[str(x) for x in row] for row in Gcanonical],
          'regular_Gram':[[str(x) for x in row] for row in Gregular]}
    with gzip.open(HERE/'sign_fibre_abstract_certificate.json.gz','wt') as f:json.dump(cert,f)
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()

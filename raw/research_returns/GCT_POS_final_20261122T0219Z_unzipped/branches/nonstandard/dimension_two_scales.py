"""A new rank-three dimension-ring family with separate cell scales.

Unlike the supplied search ansatz, the first cell's positive quadratic
parameter and its scalar-character length parameter may be D-2 rather
than D.  Exact checks below concern new tables only.
"""
from pathlib import Path
import sys,json,itertools,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'dependencies'))
import consult_a157422a_dimension_ring_search as P
import dimension_ring_minimal_pairs as M


def power(p,n):
    answer=[1]
    for _ in range(n):answer=P.mul(answer,p)
    return answer


def make_table(parameters):
    c={};S=parameters['S'];G=parameters['G'];H=parameters['H'];K=parameters.get('character_H',H)
    delta=parameters['delta'];Lam=parameters['Lam'];W=parameters['W']
    labels=['mu','Sigma']+['g%d_%s'%(i,x) for i in (1,2) for x in M.WORDS]
    for b in labels:c['mu',b,b]=c[b,'mu',b]=[1]
    c['Sigma','Sigma','Sigma']=S
    for i in (1,2):
        for x in M.WORDS:
            c['Sigma','g%d_%s'%(i,x),'Sigma']=c['g%d_%s'%(i,x),'Sigma','Sigma']=P.mul(power(K[i],len(x)-1),G[i])
    for i,j in itertools.product((1,2),repeat=2):
        for x,y in itertools.product(M.WORDS,repeat=2):
            bx,by='g%d_%s'%(i,x),'g%d_%s'%(j,y)
            scalar=P.mul(P.mul(power(K[i],len(x)-1),power(K[j],len(y)-1)),P.mul(G[i],G[j]))
            if i!=j:
                value=P.divexact(scalar,S);assert value is not None
                c[bx,by,'Sigma']=value
            else:
                z,alpha,beta=M.reduce_word(x+y)
                m=P.mul(delta[i],P.mul(power(H[i],alpha),power(Lam[i],beta)))
                c[bx,by,'g%d_%s'%(i,z)]=m
                scalar=P.sub(scalar,P.mul(m,P.mul(power(K[i],len(z)-1),G[i])))
                value=P.divexact(scalar,S);assert value is not None
                c[bx,by,'Sigma']=value
    return labels,{key:p for key,p in c.items() if p}


def verify(parameters):
    labels,table=make_table(parameters);score=bottom=0;unimodal=[]
    true=dict(M.TRUEq)
    for b in labels:true['mu',b,b]=true[b,'mu',b]=[1]
    for key in set(table)|set(true):
        dimension=P.to_q(table.get(key,[]));trace=true.get(key,[0]);n=max(len(dimension),len(trace))
        dimension=P.pad(dimension,n);trace=P.pad(trace,n)
        assert all(d>=abs(c) and (d-c)%2==0 for d,c in zip(dimension,trace)),key
        excess=sum(d-abs(c) for d,c in zip(dimension,trace))//2
        score+=excess
        if key[2]=='Sigma':bottom+=excess
        if not M.unimodal(dimension):unimodal.append(key)
    products={(a,b):{k:p for (x,y,k),p in table.items() if x==a and y==b} for a,b in itertools.product(labels,repeat=2)}
    def addto(result,k,p):
        value=P.add(result.get(k,[]),p)
        if value:result[k]=value
        else:result.pop(k,None)
    for a,b,c in itertools.product(labels,repeat=3):
        left={};right={}
        for k,p in products[a,b].items():
            for z,q in products[k,c].items():addto(left,z,P.mul(p,q))
        for k,p in products[b,c].items():
            for z,q in products[a,k].items():addto(right,z,P.mul(p,q))
        assert left==right,(a,b,c)
    return {'pair_score':score,'bottom_score':bottom,'nonzero_constants':len(table),
            'unimodality_failures':unimodal,'all_associativity_triples':1000,
            'table':[{'input1':a,'input2':b,'output':c,'D_coefficients':p} for (a,b,c),p in sorted(table.items())]}


def main():
    started=time.time();D=P.D;u=[-2,1];delta=P.mul([-1,1],u);W=[-8,7]
    par={'H':{1:u,2:D},'delta':{1:delta,2:delta},'Lam':{1:D,2:[4,-10,3]},
         'G':{1:P.mul([2],P.mul(W,delta)),2:P.mul(W,delta)},
         'S':P.mul([2],P.mul(W,P.mul(delta,delta))),'W':W}
    result=verify(par);result.update({'status':'PASS_EXACT_COMPUTATION','parameters':par,'seconds':time.time()-started})
    (HERE/'dimension_two_scales_verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['table','unimodality_failures','parameters']},indent=2),flush=True)
    print('unimodality failures',len(result['unimodality_failures']),flush=True)
    # A further variant keeps the shorter character scale, but exchanges the
    # first cell's quadratic and triple-product parameters.
    refined=dict(par,H={1:D,2:D},character_H={1:u,2:D},Lam={1:u,2:[4,-10,3]})
    second=verify(refined)
    second.update({'status':'PASS_EXACT_COMPUTATION','parameters':refined})
    (HERE/'dimension_two_scales_refined_verified.json').write_text(json.dumps(second,indent=2)+'\n')
    print('refined score',second['pair_score'],'bottom',second['bottom_score'],flush=True)


if __name__=='__main__':main()

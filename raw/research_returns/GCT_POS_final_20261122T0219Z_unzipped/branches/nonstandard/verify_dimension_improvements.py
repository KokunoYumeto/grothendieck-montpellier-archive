"""Independent symbolic verification using the supplied exhaustive associativity checker.
Also compares the true constants against all 132 stored E^opp(3) constants.
"""
import pathlib,sys,json,sympy as sp,itertools
base=pathlib.Path(__file__).resolve().parent/'dependencies';sys.path.insert(0,str(base))
import consult_a157422a_dimension_ring_verify as V
import dimension_ring_minimal_pairs as M
D=V.Dsym;v=sp.Symbol('v');out=pathlib.Path(__file__).resolve().parent
_,actual=V.table(V.TRUE)
source=json.loads((base/'e3_constants.json').read_text())
assert len(source)==len(actual)==132
for row in source:
 assert sp.cancel(actual[row['b'],row['bp'],row['bpp']].subs(D,(v+1/v)**2)-sp.sympify(row['c']))==0
records=[]
for intercept,expected in [(-8,7276),(-4,9040)]:
 delta=(D-1)*(D-2);W=7*D+intercept
 par={'S':2*W*delta**2,'G':{1:2*W*delta,2:W*delta},'W':W,'delta':{1:delta,2:delta},'Lam':{1:D,2:3*D**2-10*D+4}}
 table=V.check(par,'W=7D%+d'%intercept)
 # Second associativity check: integer lists in D, independent of Sympy expansion.
 pp={key:({j:[int(x) for x in sp.Poly(e,D).all_coeffs()][::-1] for j,e in val.items()} if isinstance(val,dict) else [int(x) for x in sp.Poly(val,D).all_coeffs()][::-1]) for key,val in par.items()}
 tt=M.table(pp); names=['mu','Sigma']+['g%d_%s'%(i,x) for i in (1,2) for x in M.WORDS]
 for name in names:tt['mu',name,name]=tt[name,'mu',name]=[1]
 def product(X,Y):
  result={}
  for a,ca in X.items():
   for b,cb in Y.items():
    for z in names:
     if (a,b,z) in tt:
      result[z]=M.S.add(result.get(z,[]),M.S.mul(M.S.mul(ca,cb),tt[a,b,z]))
  return {z:M.S.trim(c) for z,c in result.items() if M.S.trim(c)}
 for aa,bb,cc in itertools.product(names,repeat=3):
  assert product(product({aa:[1]},{bb:[1]}),{cc:[1]})==product({aa:[1]},product({bb:[1]},{cc:[1]})),(aa,bb,cc)
 baduni=[];tot=bottom=0
 for k,expr in table.items():
  dq=V.qcoeffs(expr);cq=V.qcoeffs(actual.get(k,0));es=range(min(set(dq)|set(cq)),max(set(dq)|set(cq))+1)
  ex=sum(dq.get(e,0)-abs(cq.get(e,0)) for e in es)//2
  assert all(dq.get(e,0)>=abs(cq.get(e,0)) and (dq.get(e,0)-cq.get(e,0))%2==0 for e in es)
  tot+=ex
  if k[2]=='Sigma':bottom+=ex
  vals=[dq.get(e,0) for e in range(min(dq),max(dq)+1)]
  if not M.unimodal(vals):baduni.append(k)
 assert tot==expected,(tot,expected)
 if intercept==-4:assert not baduni
 r={'W_intercept':intercept,'parameters':{key:({str(j):str(sp.factor(e)) for j,e in val.items()} if isinstance(val,dict) else str(sp.factor(val))) for key,val in par.items()},'associativity_triples_verified':1000,'integer_list_associativity_replay':True,'nonzero_constants':len(table),'cancelling_pairs':tot,'bottom_pairs':bottom,'unimodality_failures':baduni,'table': [{'inputs':[a,b],'output':c,'constant_D':str(sp.factor(e)),'q_coefficients':V.qcoeffs(e)} for (a,b,c),e in table.items()]}
 records.append(r)
 print('SCORE',intercept,tot,bottom,'unimodality failures',len(baduni),flush=True)
(out/'dimension_improvements_verified.json').write_text(json.dumps({'actual_table_rows_rechecked':132,'certificates':records},indent=2))

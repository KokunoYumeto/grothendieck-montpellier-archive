import sys,csv,random
src=open('g037.py').read().split('checked=bad=0')[0].replace("sys.path.insert(0,sys.argv[1])\nimport shp\n","")
exec(src)
rows=list(csv.DictReader(open(sys.argv[1]),delimiter='\t'))
random.seed(7)
sel=[r for r in rows if int(r['n'])<=2]+random.sample([r for r in rows if int(r["n"])==3],20)
bad=0
for r in sel:
    n=int(r['n']); mu=tuple(int(x) for x in r['outer'].split(','))
    lam=tuple(int(x) for x in r['output'].split(',')) if r['output'] else ()
    lam=tuple(x for x in lam if x>0)
    if n==0:
        mine=1 if mu==(6,) else 0
    else:
        k=max(len(lam),2)
        mine=mult(schurW(mu,n,k),list(lam),k)
    if mine!=int(r['power_sum_MN']) or mine!=int(r['weight_alternant']): bad+=1; print('MISMATCH',r,mine)
print('checked',len(sel),'mismatches',bad)

from pathlib import Path
import json,math,time
from weighted_koszul import blocks
from coordinate_koszul import modular_rank

def main():
 d=json.loads(Path(__file__).with_name('borel_7_12.json').read_text())['results'][0]
 out=[];t=time.time()
 for rec in d['records']:
  if rec['lower_bound']>=14:continue
  S=rec['subset'];m=len(rec['support']);certs=[]
  for p in sorted({2,3,4,5},key=lambda p:abs(p-6*m/(m+7))):
   rr=0;bc=[]
   for w,rows,cols,mat in blocks(S,-1,p):
    c=modular_rank(mat);rr+=c['rank_mod_p']
    if c['rank_mod_p']:
     c.update(weight=w,rows=[rows[i] for i in c['rows']],cols=[cols[i] for i in c['cols']]);bc.append(c)
   cost=math.comb(m-1,p);bound=(rr+cost-1)//cost
   certs.append({'p':p,'rank':rr,'cost':cost,'bound':bound,'blocks':bc})
   print(S,'support',m,'p',p,'rank',rr,'cost',cost,'bound',bound,flush=True)
   if bound>=14:break
  out.append({'subset':S,'certificates':certs})
  Path(__file__).with_name('det7_support_koszul.json').write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',time.time()-t)
if __name__=='__main__':main()

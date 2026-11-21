"""Research extension-weight and line tests for the remaining per7 support11/12 cases."""
from pathlib import Path
from itertools import combinations
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pencil'))
from det7_prolongation import data,extension,prolong,rank
from det7_typeB_line_conditions import conditions,rank as smallrank

def main():
 source=json.loads(Path(__file__).with_name('j7_per_support_koszul.json').read_text())['records']
 recs=[];start=time.time()
 for old in source:
  if max(c['bound'] for c in old['certificates'])>=14 or len(old['support'])<11:continue
  S=old['subset'];variables,T,blocks,image=data(S,1);m=len(variables);q=13-m
  U=[T[:,:,c] for c in range(m)]
  baseline={f:rank(prolong(U,f))[0] for f in ['A','B']}
  choices=[(i,) for i,b in enumerate(blocks) if b[2]>=q]
  if q==2:choices+=list(combinations(range(len(blocks)),2))
  remaining=[];done=[]
  for choice in choices:
   bs=extension(T,blocks,image,choice);fails=[]
   for F in ['A','B']:
    M=prolong(bs,F);r,rows,cols=rank(M)
    if M.shape[1]-r<13:
     n=M.shape[1]-12
     fails.append({'factor':F,'rows':rows[:n],'cols':cols[:n],'size':n})
   if fails:done.append({'choice':choice,'certificate':min(fails,key=lambda x:x['size'])})
   else:remaining.append(choice)
  rec={'subset':S,'support':variables,'baseline':baseline,'block_count':len(blocks),'quotient_dimension':q,'saturation_total':len(choices),'saturation_excluded':len(done),'remaining':remaining,'saturation_certificates':done}
  print('SAT',S,'m',m,'base',baseline,'remaining',len(remaining),'of',len(choices),flush=True)
  if q==1:
   lines=[]
   for (bi,) in remaining:
    w,block,dim=blocks[bi]
    byfactor={};excluded=False
    for F in ['A','B']:
     d=7 if F=='A' else m
     increment=(d-1)*13-baseline[F]
     if increment>=d:continue
     zero_count=d-increment
     cond=conditions(T,variables,w,block,F,S,w in image)
     surviving=[]
     for zeros in combinations(range(d),zero_count):
      eq=[row for i in zeros for row in cond[i]['equations']]
      if smallrank(eq,dim)<dim:surviving.append(zeros)
     byfactor[F]={'necessary_zero_count':zero_count,'surviving_zero_patterns':surviving,'conditions':cond}
     if not surviving:excluded=True;break
    print('LINE',bi,'dim',dim,'excluded',excluded, 'surviving',[ (F,len(v['surviving_zero_patterns'])) for F,v in byfactor.items()],flush=True)
    lines.append({'block':bi,'excluded':excluded,'factors':byfactor})
   rec['line_tests']=lines
  recs.append(rec)
  Path(__file__).with_name('per7_small_prolongation.json').write_text(json.dumps({'records':recs,'seconds':time.time()-start},indent=2)+'\n')
 print('DONE',time.time()-start)
if __name__=='__main__':main()

"""Build exact certificates for five remaining permanent seven-plane orbits."""
from pathlib import Path
import sys,json
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pencil'))
from det7_prolongation import data,extension,prolong,rank,PRIME
from build_det7_certificate import line_certificate,determinant_mod

def main():
 source=json.loads(Path(__file__).with_name('per7_small_prolongation.json').read_text())['records']
 out={'prime':PRIME,'field_scope':'characteristic zero','target_border_rank_lower_bound':14,'cases':[]}
 for rec in source:
  if len(rec['support'])!=12:continue
  S=rec['subset'];variables,T,blocks,image=data(S,1);U=[T[:,:,c] for c in range(12)]
  all_lines=rec['line_tests'];assert all(x['excluded'] for x in all_lines)
  orientations={next(F for F,c in x['factors'].items() if not c['surviving_zero_patterns']) for x in all_lines}
  assert len(orientations)<=1
  orientation=next(iter(orientations)) if orientations else 'A'
  M=prolong(U,orientation);rr,rows,cols=rank(M)
  base={'orientation':orientation,'minor_order':rr,'rows':rows,'cols':cols,'determinant_mod_p':determinant_mod(M[np.ix_(rows,cols)])}
  assert base['determinant_mod_p']
  records=[]
  for item in rec['saturation_certificates']:
   c=item['certificate'];basis=extension(T,blocks,image,item['choice']);M=prolong(basis,c['factor'])
   assert c['size']==M.shape[1]-12
   cert={'orientation':c['factor'],'minor_order':c['size'],'rows':c['rows'],'cols':c['cols'],'determinant_mod_p':determinant_mod(M[np.ix_(c['rows'],c['cols'])])}
   assert cert['determinant_mod_p']
   records.append({'chosen':item['choice'],'certificate':cert})
  lines={};d=7 if orientation=='A' else 12
  minimum=(d-1)*13-rr+1
  for item in all_lines:
   index=item['block'];lines[str(index)]=line_certificate(S,variables,T,blocks[index],image,orientation,minimum)
  case={'name':'per_'+str(len(out['cases'])+1),'sign':1,'subset':S,'variables':variables,'r_excluded':13,'quotient_dimension':1,'blocks':[{'weight':w,'coordinates':c,'quotient_dimension':d} for w,c,d in blocks],'base_rank_certificate':base,'saturation_certificates':records,'line_certificates':lines,'pair_increment_checks':[]}
  out['cases'].append(case)
  print(S,'baseline',orientation,rr,'saturation',len(records),'lines',len(lines),flush=True)
 assert len(out['cases'])==5
 path=Path(__file__).with_name('per7_m12_certificate.json');path.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print(path,path.stat().st_size,flush=True)
if __name__=='__main__':main()

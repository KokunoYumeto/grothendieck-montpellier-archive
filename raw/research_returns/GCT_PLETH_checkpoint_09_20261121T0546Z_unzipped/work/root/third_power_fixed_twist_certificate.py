"""Fixed, exact G032 Newton certificate at k=3, c=0,1,2."""
from pathlib import Path
from math import comb
import hashlib,json
import numpy as np
from fixed_twist_arrangement import grid,normal_schur,LABELS

HERE=Path(__file__).resolve().parent

def differences(values,axis):
    out=np.zeros_like(values)
    for degree in range(values.shape[axis]):
        dest=[slice(None)]*values.ndim;dest[axis]=degree
        for j in range(degree+1):
            out[tuple(dest)]+=(-1)**(degree-j)*comb(degree,j)*np.take(values,j,axis=axis)
    return out

def stats(array,axes):
    maximum=int(np.max(np.abs(array)))
    bound=maximum*2**sum(array.shape[a]-1 for a in axes)
    assert bound<2**63
    constants=array
    for axis in axes:constants=differences(constants,axis)
    assert int(constants.min())>=0,int(constants.min())
    labels={}
    for i,label in enumerate(LABELS):
        a=np.ascontiguousarray(constants[i],dtype='<i8')
        labels[label]={'min':int(a.min()),'max':int(a.max()),'sha256':hashlib.sha256(a.tobytes()).hexdigest()}
    return constants,{'count':int(constants.size),'input_max':maximum,'difference_bound':bound,'labels':labels}

def main():
    summary={'statement':'G-032','k':3,'twists':{},'normal_schur':{}}
    for cycles in ((),(1,),(1,1),(2,),(1,1,1),(2,1),(3,)):
        summary['normal_schur'][','.join(map(str,cycles))]=[[list(rho),v] for rho,v in normal_schur(cycles,3)]
    for c in range(3):
        raw,operation_bound=grid(range(240),range(8,308),3,c)
        assert int(raw.min())>=0
        shaped=raw.reshape(7,4,60,5,60).transpose(0,2,4,1,3)
        table,result=stats(shaped,(3,4));result['trace_operation_bound']=operation_bound
        active=[(i,j) for i in range(4) for j in range(5) if np.any(table[:,:,:,i,j])]
        assert len(active)==17
        result['active_orders']=active
        result['minimum_by_order']={f'{i},{j}':int(table[:,:,:,i,j].min()) for i,j in active}
        assert all(v>0 for order,v in result['minimum_by_order'].items() if order!='0,0')
        result['zero_pairs']={label:[[int(x),int(B)] for x,B in np.argwhere(table[index,:,:,0,0]==0)] for index,label in enumerate(LABELS)}
        data={'bulk_b8':result,'boundaries':{}}
        for b in range(8):
            shift=max(0,15-3*c-2*b)
            raw,operation_bound=grid(range(shift,shift+240),(b,),3,c)
            shaped=raw[:,:,0].reshape(7,4,60).transpose(0,2,1)
            table,result=stats(shaped,(2,));result['trace_operation_bound']=operation_bound
            result['x_shift']=shift
            result['zero_residues']={label:[int(x) for x in np.flatnonzero(table[index,:,0]==0)] for index,label in enumerate(LABELS)}
            result['minimum_by_order']={str(i):int(table[:,:,i].min()) for i in range(4)}
            assert all(result['minimum_by_order'][str(i)]>0 for i in (1,2,3))
            data['boundaries'][str(b)]=result
        summary['twists'][str(c)]=data
        print('twist',c,'PASS',504000+8*1680,'constants',flush=True)
    summary['total_constants']=sum(v['bulk_b8']['count']+sum(w['count'] for w in v['boundaries'].values()) for v in summary['twists'].values())
    (HERE/'THIRD_POWER_FIXED_TWIST_CERTIFICATE.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('PASS',summary['total_constants'],'constants',flush=True)

if __name__=='__main__':main()

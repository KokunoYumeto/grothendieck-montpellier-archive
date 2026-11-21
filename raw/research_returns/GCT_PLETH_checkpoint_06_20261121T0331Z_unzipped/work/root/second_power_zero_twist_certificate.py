"""G030 fixed positive Newton certificates for k2,c0 in all six valid domains."""
from pathlib import Path
from math import comb
import hashlib,json
import numpy as np
from zero_twist_arrangement import coefficients as arrangement_coefficients,LABELS

def coefficients(x,b):
    return arrangement_coefficients(x,b,2)

HERE=Path(__file__).resolve().parent

def differences(values,axis):
    out=np.empty_like(values)
    for degree in range(values.shape[axis]):
        current=np.take(values,range(degree+1),axis=axis)
        coeff=np.array([(-1)**(degree-j)*comb(degree,j) for j in range(degree+1)],dtype=np.int64)
        shaped=[1]*current.ndim;shaped[axis]=len(coeff)
        dest=[slice(None)]*out.ndim;dest[axis]=degree
        out[tuple(dest)]=(current*coeff.reshape(shaped)).sum(axis=axis)
    return out

def stats(array,axes):
    maxinput=int(np.max(np.abs(array)))
    bound=maxinput*2**sum(array.shape[axis]-1 for axis in axes)
    assert bound<2**63
    constants=array
    for axis in axes:constants=differences(constants,axis)
    assert int(constants.min())>=0,int(constants.min())
    rows={}
    for index,label in enumerate(LABELS):
        a=np.ascontiguousarray(constants[index],dtype='<i8')
        rows[label]={'min':int(a.min()),'max':int(a.max()),
                     'sha256':hashlib.sha256(a.tobytes()).hexdigest()}
    return constants,{'count':int(constants.size),'input_max':maxinput,
                      'difference_bound':bound,'labels':rows}

raw=np.empty((7,240,300),dtype=np.int64)
for x in range(240):
    for B in range(300):raw[:,x,B]=coefficients(x,B+5)
assert int(raw.min())>=0
shaped=raw.reshape(7,4,60,5,60).transpose(0,2,4,1,3)
table,result=stats(shaped,(3,4))
active=[(i,j) for i in range(4) for j in range(5) if np.any(table[:,:,:,i,j])]
result['active_orders']=active
result['minimum_by_order']={f'{i},{j}':int(table[:,:,:,i,j].min()) for i,j in active}
result['maximum_by_order']={f'{i},{j}':int(table[:,:,:,i,j].max()) for i,j in active}
result['zero_pairs']={label:[[int(x),int(b)] for x,b in np.argwhere(table[index,:,:,0,0]==0)] for index,label in enumerate(LABELS)}
summary={'statement':'G-030','bulk_b5':result,'boundaries':{}}
for b,shift in tuple((b,10-2*b) for b in range(5)):
    raw=np.array([coefficients(x+shift,b) for x in range(240)],dtype=np.int64).T
    shaped=raw.reshape(7,4,60).transpose(0,2,1)
    constants,result=stats(shaped,(2,))
    result['zero_residues']={label:[int(x) for x in np.flatnonzero(constants[index,:,0]==0)] for index,label in enumerate(LABELS)}
    result['x_shift']=shift
    result['minimum_by_order']={str(i):int(constants[:,:,i].min()) for i in range(4)}
    summary['boundaries'][str(b)]=result
    print('boundary',b,'PASS',result['count'],'max',max(v['max'] for v in result['labels'].values()),flush=True)
(HERE/'SECOND_POWER_ZERO_TWIST_CERTIFICATE.json').write_text(json.dumps(summary,indent=2)+'\n')
print('bulk PASS',summary['bulk_b5']['count'],'active',active,'max',max(v['max'] for v in summary['bulk_b5']['labels'].values()),flush=True)

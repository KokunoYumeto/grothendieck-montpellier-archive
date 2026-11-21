"""Exhaustive fixed zeroth-order table and exact overflow bounds for T054."""
from pathlib import Path
from math import lcm
import json,hashlib
import numpy as np
from positive_wall_chamber import POLYS,PERIODS,LABELS,CHAR,SIZES

HERE=Path(__file__).resolve().parent


def main():
    coordinates=np.indices((60,60,60),dtype=np.int64).reshape(3,-1)
    X,B,K=coordinates
    powers=[[axis**i for i in range(6)] for axis in coordinates]
    traces=[];bounds=[]
    for period,phases in zip(PERIODS,POLYS):
        denominator=lcm(*(c.denominator for poly in phases.values() for _,c in poly))
        worst=max(sum(abs(c.numerator)*(denominator//c.denominator)*59**sum(power)
                      for power,c in poly) for poly in phases.values())
        assert worst<2**63
        values=np.zeros(X.size,dtype=np.int64)
        ar=(3*K+7+B+X)%period;br=(3*K+7+B)%period;kr=(K+3)%period
        phase_id=(ar*period+br)*period+kr
        for phase,poly in phases.items():
            ids=np.flatnonzero(phase_id==(phase[0]*period+phase[1])*period+phase[2])
            if not len(ids):continue
            val=np.zeros(len(ids),dtype=np.int64)
            for power,c in poly:
                term=np.full(len(ids),c.numerator*(denominator//c.denominator),dtype=np.int64)
                for axis,degree in enumerate(power):term*=powers[axis][degree][ids]
                val+=term
            values[ids]=val
        assert np.all(values%denominator==0)
        values//=denominator;traces.append(values)
        bounds.append({'denominator':denominator,'absolute_numerator_bound':worst,
                       'maximum_absolute_trace':int(np.max(np.abs(values)))})
    records=[]
    for label,chi in zip(LABELS,CHAR):
        bound=sum(size*abs(c)*entry['maximum_absolute_trace'] for size,c,entry in zip(SIZES,chi,bounds))
        assert bound<2**63
        numerator=sum(size*c*trace for size,c,trace in zip(SIZES,chi,traces))
        assert np.all(numerator%120==0)
        values=numerator//120
        assert np.all(values>=0)
        assert values[0]==0
        zero=np.flatnonzero(values==0)
        zero=zero[zero!=0]
        records.append({'label':label,'minimum':int(values.min()),'maximum':int(values.max()),
                        'minimum_valid':int(values[1:].min()),'formal_origin_value':int(values[0]),
                        'zeros':[tuple(map(int,coordinates[:,i])) for i in zero],
                        'weighted_sum_bound':bound,
                        'sha256_le_int64':hashlib.sha256(values.astype('<i8').tobytes()).hexdigest()})
    receipt={'statement':'T-054','status':'PASS','constants':7*60**3,
             'class_bounds':bounds,'labels':records,
             'zero_count':sum(len(row['zeros']) for row in records),
             'method':'complete fixed residue cube; exact rational class polynomials with separately proved signed-64-bit bounds'}
    (HERE/'VARIABLE_WALL_RESIDUE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()

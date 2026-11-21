#!/usr/bin/env python3
"""Independent coefficient-vector enumeration of the signed trace code of length31.

No producer code, output data, curve arithmetic, or optional algebra package is
imported. Elements of F32 are five-tuples of coefficients in the basis1,z,...,z4,
with z5=z2+1. The integer labels in the JSON encode those coefficient tuples.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

ZERO=(0,0,0,0,0)
ONE=(1,0,0,0,0)
Z=(0,1,0,0,0)

def field_label(x):
    return sum(c*(2**i) for i,c in enumerate(x))

def coefficients(n):
    return tuple((n//(2**i))%2 for i in range(5))

def add(a,b):
    return tuple((x+y)%2 for x,y in zip(a,b))

def mul(a,b):
    out=[0]*9
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=(out[i+j]+x*y)%2
    for j in range(8,4,-1):
        c=out[j]
        out[j]=0
        out[j-5]=(out[j-5]+c)%2
        out[j-3]=(out[j-3]+c)%2
    return tuple(out[:5])

def trace(a):
    out=ZERO
    term=a
    for _ in range(5):
        out=add(out,term)
        term=mul(term,term)
    assert out in (ZERO,ONE)
    return out[0]

def rank_binary(rows, ncols):
    rows=[list(row) for row in rows]
    r=0
    for col in range(ncols):
        pivot=next((i for i in range(r,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for i in range(len(rows)):
            if i!=r and rows[i][col]:
                rows[i]=[(x+y)%2 for x,y in zip(rows[i],rows[r])]
        r+=1
    return r

def main():
    powers=[]
    v=ONE
    for _ in range(31):
        powers.append(v)
        v=mul(v,Z)
    assert v==ONE and len(set(powers))==31 and ZERO not in powers
    # All31 nonzero residues are powers ofz, so every nonzero residue is a
    # unit. This also verifies that the specified quotient is a field.
    for v in [coefficients(i) for i in range(32)]:
        trace(v)

    records=[]
    generator_rows=[]
    histogram=Counter()
    word_set=set()
    for a_label in range(32):
        for b_label in range(32):
            a,b=coefficients(a_label),coefficients(b_label)
            bits=[trace(add(mul(a,powers[i]),mul(b,powers[(-i)%31])))
                  for i in range(31)]
            word=sum(c*(2**i) for i,c in enumerate(bits))
            weight=sum(bits)
            records.append({'a':a_label,'b':b_label,'word':word,'weight':weight})
            histogram[weight]+=1
            word_set.add(word)
            if (b_label==0 and a_label in (1,2,4,8,16)) or \
               (a_label==0 and b_label in (1,2,4,8,16)):
                generator_rows.append(bits)
    assert len(records)==1024 and len(word_set)==1024
    assert rank_binary(generator_rows,31)==10
    min_weight=min(w for w in histogram if w)

    # Direct discrete Fourier support check for all ten generators. Linearity
    # then gives containment for the entire enumerated binary space.
    signed_orbit=sorted({s*pow(2,j,31)%31 for s in (1,-1) for j in range(5)})
    supports=[]
    for row in generator_rows:
        support=[]
        for j in range(31):
            value=ZERO
            for i,bit in enumerate(row):
                if bit:
                    value=add(value,powers[(i*j)%31])
            if value!=ZERO:
                support.append(j)
        assert set(support)<=set(signed_orbit)
        supports.append(support)
    # The two distinct Frobenius orbits each have degree5. Their combined
    # binary Fourier subspace therefore has dimension10; rank10 proves
    # equality, not only a trace-code subspace inclusion.
    assert len(signed_orbit)==10 and 0 not in signed_orbit
    result={
        'status':'PASS',
        'scope':'Abstract binary trace code only; no geometric realization.',
        'field_modulus_coefficients_ascending':[1,0,1,0,0,1],
        'primitive_element_label':2,
        'powers_of_primitive_element':[field_label(x) for x in powers],
        'signed_orbit':signed_orbit,
        'dimension':10,
        'codeword_count':len(word_set),
        'weight_distribution':dict(sorted(histogram.items())),
        'minimum_nonzero_weight':min_weight,
        'minimum_weight_witness':next(r for r in records if r['weight']==min_weight),
        'generator_rows':generator_rows,
        'generator_fourier_supports':supports,
        'all_words':records,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output=Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','scope','dimension',
          'codeword_count','weight_distribution','minimum_nonzero_weight',
          'minimum_weight_witness')}))

if __name__=='__main__':
    main()

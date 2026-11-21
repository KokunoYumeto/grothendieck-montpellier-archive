#!/usr/bin/env python3
"""G-030: positive coefficients, literal polytopes, and lazy witnesses."""
from functools import lru_cache
from itertools import product
from math import comb
import argparse
import json
from zero_twist_arrangement import coefficients as arrangement_coefficients, LABELS

def coefficients(x,b):
    return arrangement_coefficients(x,b,2)
from staircase_five_positive import increasing_subsets


def validate(x, b, d, outer):
    if any(type(v) is not int or v < 0 for v in (x, b, d)):
        raise ValueError('x, b and d must be nonnegative integers')
    if 2*b+x < 10:
        raise ValueError('the partition condition is 2*b+x >= 10')
    if isinstance(outer, (tuple, list)):
        outer = ''.join(map(str, outer))
    if outer not in LABELS:
        raise ValueError('outer must be one of '+', '.join(LABELS))
    label = LABELS.index(outer)
    if (d+b+x) % 2:
        label = 6-label
    if b >= 5:
        return label, 'bulk', (x, b-5), (3, 4)
    return label, str(b), (x-(10-2*b),), (3,)


@lru_cache(None)
def constants(label, branch, residues):
    degrees = (3, 4) if branch == 'bulk' else (3,)
    values = {}
    for q in product(*(range(v+1) for v in degrees)):
        parameters = tuple(r+60*t for r,t in zip(residues,q))
        if branch == 'bulk':
            x, B = parameters
            values[q] = coefficients(x, B+5)[label]
        else:
            b = int(branch)
            values[q] = coefficients(parameters[0]+10-2*b, b)[label]
    answer = []
    for order in product(*(range(v+1) for v in degrees)):
        value = 0
        for q in product(*(range(v+1) for v in order)):
            factor = (-1)**sum(a-t for a,t in zip(order,q))
            for a,t in zip(order,q):
                factor *= comb(a,t)
            value += factor*values[q]
        if value < 0:
            raise ArithmeticError('negative fixed constant')
        if value:
            answer.append((order,value))
    return tuple(answer)


def coefficient(x, b, d=0, outer='5'):
    label, branch, parameters, _ = validate(x,b,d,outer)
    quotients, residues = zip(*(divmod(v,60) for v in parameters))
    total = 0
    for order,value in constants(label,branch,tuple(residues)):
        for q,j in zip(quotients,order):
            value *= comb(q,j)
        total += value
    return total


def polytopes(x,b,d=0,outer='5',all_residues=False):
    label,branch,parameters,_ = validate(x,b,d,outer)
    count = len(parameters)
    residue_list = product(range(60),repeat=count) if all_residues else [tuple(v%60 for v in parameters)]
    answer = []
    for residues in residue_list:
        for order,value in constants(label,branch,tuple(residues)):
            names = [f'q{i+1}' for i in range(count)]+['y']
            chain_starts = []
            for i,j in enumerate(order):
                chain_starts.append(len(names))
                names += [f'z{i+1}_{t+1}' for t in range(j)]
            size = len(names)
            eq,ineq = [],[]
            for i,(parameter,residue) in enumerate(zip(parameters,residues)):
                row=[0]*size;row[i]=60;eq.append([row,parameter-residue])
                row=[0]*size;row[i]=-1;ineq.append([row,0])
            row=[0]*size;row[count]=-1;ineq.append([row,0])
            row=[0]*size;row[count]=1;ineq.append([row,value-1])
            for i,(start,j) in enumerate(zip(chain_starts,order)):
                if not j:continue
                row=[0]*size;row[start]=-1;ineq.append([row,0])
                for index in range(start,start+j-1):
                    row=[0]*size;row[index]=1;row[index+1]=-1;ineq.append([row,-1])
                row=[0]*size;row[start+j-1]=1;row[i]=-1;ineq.append([row,-1])
            answer.append({'branch':branch,'residues':residues,'order':order,'constant':value,
                           'variables':names,'equalities':eq,'inequalities':ineq})
    return answer


def witnesses(x,b,d=0,outer='5',limit=10):
    label,branch,parameters,_ = validate(x,b,d,outer)
    if type(limit) is not int or limit<0:
        raise ValueError('limit must be a nonnegative integer')
    if not limit:return
    quotients,residues=zip(*(divmod(v,60) for v in parameters))
    produced=0
    def chains(order,index=0,prefix=()):
        if index==len(order):
            yield prefix;return
        for chain in increasing_subsets(quotients[index],order[index]):
            yield from chains(order,index+1,prefix+chain)
    for order,value in constants(label,branch,tuple(residues)):
        for chain in chains(order):
            y=0
            while y<value:
                yield {'branch':branch,'residues':residues,'order':order,
                       'coordinates':tuple(quotients)+(y,)+chain}
                produced+=1
                if produced>=limit:return
                y+=1


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--x',type=int,required=True)
    parser.add_argument('--b',type=int,required=True)
    parser.add_argument('--d',type=int,default=0)
    parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    parser.add_argument('--all-residues',action='store_true')
    parser.add_argument('--witness-limit',type=int,default=0)
    args=parser.parse_args()
    x,b,d=args.x,args.b,args.d
    result={'x':x,'b':b,'d':d,'outer':args.outer,'inner':d+b+x-2,
            'output':[d+3*b+2*x-10,d+b+x,d+b+x,d+x,d],
            'coefficient':coefficient(x,b,d,args.outer)}
    if args.polytopes:
        result['polytopes']=polytopes(x,b,d,args.outer,args.all_residues)
    if args.witness_limit:
        result['witnesses']=list(witnesses(x,b,d,args.outer,args.witness_limit))
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

"""Exact finite-weight exploration of the strict divided square of a resolution.

This is an exploratory calculation, not a proof of an unbounded assertion.
Modes: the actual p=2 coefficient algebra Gamma_Z_(2)(T), or the toy
coefficient algebra Z_(2)[x]/x^2.  Matrices are integral; d^2 is checked.
Mod-2 ranks plus rational acyclicity give the number of 2-primary cyclic
homology summands in each finite weight (not their exponents).
"""
import argparse
import itertools
import json
import math
from collections import defaultdict


def binary_rank(columns):
    pivots = {}
    for vector in columns:
        while vector:
            lead = vector.bit_length() - 1
            if lead in pivots:
                vector ^= pivots[lead]
            else:
                pivots[lead] = vector
                break
    return len(pivots)


def run(mode, weight_bound, homological_bound=7, capture_weights=()):
    hs = [1] if mode == "toy" else [2**i for i in range(weight_bound.bit_length())]
    odd_weights = [0] + hs  # theta, then e_i
    f_weights = [2*h for h in hs]
    basis = []

    def f_tuples(index, degree_left, weight_left, values):
        if index == len(hs):
            yield tuple(values)
            return
        upper = min(degree_left//2, weight_left//f_weights[index])
        for exponent in range(upper+1):
            yield from f_tuples(index+1, degree_left-2*exponent,
                                weight_left-exponent*f_weights[index],
                                values+[exponent])

    for mask in range(1 << len(odd_weights)):
        degree = mask.bit_count()
        weight = sum(w for i,w in enumerate(odd_weights) if mask & (1 << i))
        if degree > homological_bound or weight > weight_bound:
            continue
        for fs in f_tuples(0, homological_bound-degree, weight_bound-weight, []):
            basis.append((mask, fs, degree+2*sum(fs),
                          weight+sum(r*w for r,w in zip(fs, f_weights))))
    basis.sort(key=lambda item:(item[2], item[3], item[0], item[1]))
    indices = {(mask,fs):i for i,(mask,fs,_,_) in enumerate(basis)}

    def append_odd(mask, odd_index):
        if mask & (1 << odd_index):
            return None
        sign = -1 if (mask >> (odd_index+1)).bit_count() % 2 else 1
        return mask | (1 << odd_index), sign

    linear_d = []
    for mask,fs,degree,weight in basis:
        out = defaultdict(int)
        for odd_index in range(len(odd_weights)):
            if not (mask & (1 << odd_index)):
                continue
            sign = -1 if (mask & ((1 << odd_index)-1)).bit_count() % 2 else 1
            target = indices[(mask ^ (1 << odd_index),fs)]
            scalar, coefficient_weight = (2,0) if odd_index == 0 else (1,hs[odd_index-1])
            out[(target,coefficient_weight)] += sign*scalar
        for i,r in enumerate(fs):
            if not r:
                continue
            lowered = list(fs)
            lowered[i] -= 1
            lowered = tuple(lowered)
            initial_sign = -1 if mask.bit_count() % 2 else 1
            inserted = append_odd(mask,i+1)
            if inserted is not None:
                new_mask,sign = inserted
                out[(indices[(new_mask,lowered)],hs[i])] += initial_sign*sign
            if mode == "actual" and i+1 < len(hs):
                inserted = append_odd(mask,i+2)
                if inserted is not None:
                    new_mask,sign = inserted
                    kappa = math.comb(2*hs[i],hs[i])//2
                    out[(indices[(new_mask,lowered)],0)] -= 2*kappa*initial_sign*sign
        linear_d.append([(target,scalar,cw) for (target,cw),scalar in out.items() if scalar])

    pairs_by_degree = [[] for _ in range(homological_bound+1)]
    for i,a in enumerate(basis):
        for j in range(i,len(basis)):
            b=basis[j]
            degree=a[2]+b[2]
            if degree > homological_bound or a[3]+b[3] > weight_bound:
                continue
            if i == j and a[2] % 2:
                continue
            pairs_by_degree[degree].append((i,j))

    def product(i,j):
        if i == j:
            return None if basis[i][2] % 2 else ((i,i),2)
        if i < j:
            return (i,j),1
        return (j,i),(-1 if basis[i][2]*basis[j][2] % 2 else 1)

    pair_d = {}
    for pairs in pairs_by_degree:
        for i,j in pairs:
            out=defaultdict(int)
            # A repeated even pair denotes gamma_2, not the ordinary square.
            for target,scalar,cw in linear_d[i]:
                value=product(target,j)
                if value:
                    pair,sign=value
                    out[(pair,cw)] += scalar*sign
            if i != j:
                koszul=-1 if basis[i][2] % 2 else 1
                for target,scalar,cw in linear_d[j]:
                    value=product(i,target)
                    if value:
                        pair,sign=value
                        out[(pair,cw)] += koszul*scalar*sign
            pair_d[(i,j)]=[(pair,scalar,cw) for (pair,cw),scalar in out.items() if scalar]

    results=[]
    captures={}
    for weight in range(weight_bound+1):
        groups=[]
        for degree,pairs in enumerate(pairs_by_degree):
            groups.append([pair for pair in pairs
                           if (0 <= weight-basis[pair[0]][3]-basis[pair[1]][3])
                           and (mode != "toy" or weight-basis[pair[0]][3]-basis[pair[1]][3] <= 1)])
        lookup=[{pair:i for i,pair in enumerate(group)} for group in groups]
        matrices=[[]]
        for degree in range(1,homological_bound+1):
            columns=[]
            for pair in groups[degree]:
                coefficient_weight=weight-basis[pair[0]][3]-basis[pair[1]][3]
                column=defaultdict(int)
                for target,scalar,cw in pair_d[pair]:
                    if mode == "toy":
                        if coefficient_weight+cw > 1:
                            continue
                        coefficient=scalar
                    else:
                        coefficient=scalar*math.comb(coefficient_weight+cw,cw)
                    column[lookup[degree-1][target]] += coefficient
                columns.append({row:value for row,value in column.items() if value})
            matrices.append(columns)
        for degree in range(2,homological_bound+1):
            for column in matrices[degree]:
                square=defaultdict(int)
                for row,value in column.items():
                    for target,other in matrices[degree-1][row].items():
                        square[target] += value*other
                assert not any(square.values()), (mode,weight,degree,dict(square))
        ranks=[0]
        for degree in range(1,homological_bound+1):
            columns=[sum(1 << row for row,value in column.items() if value % 2)
                     for column in matrices[degree]]
            ranks.append(binary_rank(columns))
        betti=[]
        counts=[]
        previous=0
        for degree in range(homological_bound):
            beta=len(groups[degree])-ranks[degree]-ranks[degree+1]
            current=beta-previous
            assert current >= 0,(weight,degree,beta,previous)
            betti.append(beta)
            counts.append(current)
            previous=current
        results.append({"weight":weight,"dimensions":[len(g) for g in groups],
                        "mod2_betti":betti,"two_primary_summand_counts":counts})
        if weight in capture_weights:
            captures[weight]={"groups":groups,"matrices":matrices}
    return {"mode":mode,"weight_bound":weight_bound,
            "homological_bound":homological_bound,
            "d_squared_checked_exactly":True,
            "interpretation":"Gamma^2 of the full free resolution; summand counts use rational acyclicity and UCT, not exponents",
            "results":results,"captures":captures,
            "linear_basis":basis if capture_weights else None}


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=["toy","actual"],default="toy")
    parser.add_argument("--weight",type=int,default=16)
    parser.add_argument("--degree",type=int,default=7)
    parser.add_argument("--output")
    parser.add_argument("--capture",type=int,nargs="*",default=[])
    args=parser.parse_args()
    result=run(args.mode,args.weight,args.degree,args.capture)
    if args.output:
        with open(args.output,"w") as handle:
            json.dump(result,handle,indent=2)
    print(json.dumps({"mode":args.mode,"weight_bound":args.weight,
                      "d_squared_checked_exactly":True,
                      "nonzero_H5":[(r["weight"],r["two_primary_summand_counts"][5]) for r in result["results"] if r["two_primary_summand_counts"][5]],
                      "nonzero_H6":[(r["weight"],r["two_primary_summand_counts"][6]) for r in result["results"] if r["two_primary_summand_counts"][6]]}))

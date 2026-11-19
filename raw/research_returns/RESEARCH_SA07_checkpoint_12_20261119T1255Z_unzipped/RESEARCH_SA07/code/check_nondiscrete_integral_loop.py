#!/usr/bin/env python3
"""Exact finite certificates for the loop construction LP1--LP6.

Verifies the symbolic commutator/trace recurrence and the first96 fully
specified induction stages. The compact limit and every-cover lattice
statement are proved in agent_integral_homology_nondiscrete_loop.md.
No Galois or motivic automorphism is asserted.
"""
from itertools import permutations, islice
from math import lcm
from time import perf_counter
import sympy as sp

started=perf_counter();STAGES=96
I=(1,0,0,1)
U=(1,3,0,1);Ui=(1,-3,0,1)
V=(1,0,3,1);Vi=(1,0,-3,1)
letters=(U,Ui,V,Vi);inverse_letter=(1,0,3,2)
def mul(A,B):
    a,b,c,d=A;e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def tr(A):return A[0]+A[3]
def det(A):return A[0]*A[3]-A[1]*A[2]
def mod(A,r):return tuple(a%r for a in A)
def word_matrix(word):
    A=I
    for letter in word:A=mul(A,letters[letter])
    return A
def reduced_words():
    layer=[()]
    while True:
        yield from layer
        layer=[w+(a,) for w in layer for a in range(4)
               if not w or a!=inverse_letter[w[-1]]]
def permutation_order(p):
    seen=set();o=1
    for a in range(len(p)):
        if a in seen:continue
        cycle=[];b=a
        while b not in seen:
            cycle.append(b);seen.add(b);b=p[b]
        assert b==a
        o=lcm(o,len(cycle))
    return o
def finite_quotients():
    m=1
    while True:
        perms=list(permutations(range(m)))
        for p in perms:
            for q in perms:yield (m,p,q)
        m+=1

t=sp.Symbol('t')
Ut=sp.Matrix([[1,t],[0,1]]);Lt=sp.Matrix([[1,0],[t,1]])
B=Ut*Lt*Ut.inv()*Lt.inv()
expected=sp.Matrix([[1+t*t+t**4,-t**3],[t**3,1-t*t]])
assert (B-expected).applyfunc(sp.expand)==sp.zeros(2)
assert sp.expand(B.det())==1
assert sp.expand(sp.trace(B)-(2+t**4))==0
assert (B*B-sp.trace(B)*B+sp.eye(2)).applyfunc(sp.expand)==sp.zeros(2)
print('SYMBOLIC_COMMUTATOR_TRACE_AND_CAYLEY_HAMILTON_PASSED')

P=I;d=1;orders=[];frozen=[];changes=[];largest_d_bits=0
words=reduced_words();quotients=finite_quotients()
for n in range(1,STAGES+1):
    f=next(words);m,p,q=next(quotients)
    op,oq=permutation_order(p),permutation_order(q)
    orders.extend((op,oq));d=lcm(d,op,oq)
    largest_d_bits=max(largest_d_bits,d.bit_length())
    assert all(d%order==0 for order in orders)
    assert all(d%r==0 for r,_,_ in frozen)
    c=tr(word_matrix(f));assert tr(P)%3==2 and c%3==2
    if tr(P)!=c:
        exponent=0;Pnext=P
    else:
        z=3*d
        H=(1+z*z+z**4,-z**3,z**3,1-z*z)
        assert det(H)==1 and tr(H)==2+z**4>2
        P1=mul(P,H);P2=mul(P1,H)
        assert tr(P2)==tr(H)*tr(P1)-tr(P)
        exponent=next(e for e,A in ((1,P1),(2,P2)) if tr(A)!=c)
        Pnext=P1 if exponent==1 else P2
        assert all(mod(H,r)==mod(I,r) for r,_,_ in frozen)
        changes.append((n,exponent,d.bit_length(),len(f)))
    assert det(Pnext)==1 and tr(Pnext)%3==2
    # Every old congruence cylinder remains frozen, with the old conjugacy
    # exclusion still visible in that exact finite quotient.
    for r,Pold,old_target_trace in frozen:
        assert mod(Pnext,r)==Pold
        assert (tr(Pnext)-old_target_trace)%r!=0
    Delta=tr(Pnext)-c;assert Delta!=0 and Delta%3==0
    r=abs(Delta)+1;assert r>=4 and r%3==1
    assert Delta%r!=0
    frozen.append((r,mod(Pnext,r),c))
    P=Pnext;d=lcm(d,r)
assert changes and changes[0][0]==1
print('EXACT_INDUCTION_STAGES',STAGES)
print('NONTRIVIAL_PREFIX_UPDATES_stage_exponent_d_bits_word_length',changes)
print('ALL_FINITE_PERMUTATION_ORDERS_DIVIDE_CURRENT_d')
print('ALL_PRIOR_MATRIX_QUOTIENTS_AND_CONJUGACY_EXCLUSIONS_RETAINED')
print('FINAL_PREFIX_TRACE_BITS',abs(tr(P)).bit_length())
print('LARGEST_d_BITS',largest_d_bits)
print('SCOPE: symbolic identities and finite induction prefix; compactness and all-cover homology are separately proved.')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))

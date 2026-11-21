from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
root=Path(__file__).parent
u=list(map(lambda n:Q(n,2),[113,45,37,29,21,13,5,-1]))
def rows(M,G):
    e=[M+18,M+G+18]
    def src(r):
        if r<8:return u[r]
        return -e[(r-8)//16]+Q(17-2*((r-8)%16+1),2)
    return [[src(r)+e[j]-Q([8,24][j]+[24,40][j]-1-2*r,2) for r in range([8,24][j])] for j in range(2)]
checks=[]
for M in [1000,10**12]:
 for G in [16,36,10**9]:
    a,b=rows(M,G)
    assert a==[M+t for t in [59,26,23,20,17,14,11,9]]
    assert b==[M+G+t for t in [43,10,7,4,1,-2,-5,-7]]+[G-16]*16
    assert sum(a)==8*M+179 and sum(b)==8*M+24*G-205
    assert all(a[i]>=a[i+1] for i in range(7)) and all(b[i]>=b[i+1] for i in range(23))
    assert 8*(sum(a)+sum(b))==128*M+192*G-208
    checks.append({'M':M,'G':G,'partition_sizes':[int(sum(a)),int(sum(b))]})
assert 15+2*40**3+1==128016 < 10**9
assert 8*(8*24+24*40)==9216
assert 76800-2*9216==58368
assert 863**2-1==744768
cert={'checks':checks,'strong_bound_numerator':'128*M+192*G-208','full_bound_numerator':'96*M+48*G+1728','difference_numerator':'32*M+144*G-1936','strong_log_coefficient':18432,'full_log_coefficient':76800,'constant_error':9216,'proof_sha256':hashlib.sha256((root/'pointwise_inert_valuation.tex').read_bytes()).hexdigest(),'status':'Exact arithmetic only; actual input gates remain conditional; no Lean build.'}
(root/'pointwise_inert_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(cert,indent=2))

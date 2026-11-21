"""Independent exact rational and tensor-table audit for T041."""
from pathlib import Path
from collections import Counter
import ast,hashlib
import sympy as s
from verify_rectangular import partitions,character,z

HERE=Path(__file__).resolve().parent
THETA=HERE.parent/'theta'/'outer5'


def literal(path,name):
    for node in ast.parse(path.read_text()).body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError(name)


def main():
    file=THETA/'five_point_hook_positive.py'
    four=literal(file,'FOUR');three=literal(file,'THREE')
    tensor=literal(THETA/'five_point_positive.py','TENSOR')
    t=s.symbols('t')
    D=s.prod(1-t**j for j in (2,3,4,5))
    D3=s.prod(1-t**j for j in (2,3,5))
    classes=tuple(partitions(5))
    labels=classes
    messages=[]
    for mu in labels:
        rational=0
        for cyc in classes:
            det=s.prod(1-t**j for j in cyc)/(1-t)
            hook=((cyc.count(1)-1)-1/t)/det+1/t
            rational+=s.Rational(character(mu,cyc),z(cyc))*hook
        proposed=sum(t**j for j in four[mu])/D+sum(t**j for j in three.get(mu,()))/D3
        assert s.cancel(rational-proposed)==0,mu
        messages.append('PASS full rational hook series '+str(mu))
    for rho in labels:
        counts=Counter(tensor[rho])
        for nu in labels:
            val=sum(s.Rational(character((3,2),cyc)*character(rho,cyc)*character(nu,cyc),z(cyc)) for cyc in classes)
            assert val==counts[nu],(rho,nu,val,counts[nu])
    messages.append('PASS all49 tensor multiplicities computed by MN class inner products')
    counts={nu:sum(Counter(tensor[rho])[nu]*(len(four[rho])+len(three.get(rho,()))) for rho in labels) for nu in labels}
    assert max(counts.values())==90
    messages.append('PASS exact tag counts '+str(counts))
    messages.append('Input evaluator SHA256 '+hashlib.sha256(file.read_bytes()).hexdigest())
    (HERE/'HOOK_FIXED_SERIES_INDEPENDENT_CHECK.txt').write_text('\n'.join(messages)+'\n')
    print('\n'.join(messages))


if __name__=='__main__':main()

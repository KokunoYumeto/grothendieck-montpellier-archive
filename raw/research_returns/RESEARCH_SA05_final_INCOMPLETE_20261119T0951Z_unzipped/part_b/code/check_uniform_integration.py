"""Exact bookkeeping and formal Chern-polynomial checks, not a Tate proof."""
from pathlib import Path
from collections import Counter
import csv
import re

root = Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work')
paths = [root/'sections/b3_prime_uniform.tex',
         root/'sections/b3_irregularity_zero_surface_gate.tex']
with (root/'part_b/part_b_LABEL_CHECKS.tsv').open() as stream:
    checked = {row['statement_label'] for row in csv.DictReader(stream, delimiter='\t')}
main = (root/'sections/part_b.tex').read_text()
for path in paths:
    content = path.read_text()
    labels = re.findall(r'\\label\{([^}]+)\}', content)
    print(path.name)
    print('  included:', '\\input{sections/'+path.name+'}' in main)
    print('  numbered labels:', labels)
    print('  all have recorded checks:', set(labels) <= checked)
    print('  brace difference:', content.count('{')-content.count('}'))
    print('  display pairs:', content.count('\\['), content.count('\\]'))
    environments = re.findall(r'\\begin\{(theorem|proposition|lemma|corollary|remark)\}',content)
    print('  statement environments / statuses:',len(environments),content.count('\\status{'))
    assert set(labels) <= checked
    assert content.count('{') == content.count('}')
    assert content.count('\\[') == content.count('\\]')
    assert len(environments) == content.count('\\status{')

# Formal homogeneous polynomials in K,H,d,c2 with integer coefficients.
def plus(*ps):
    result=Counter()
    for p in ps:
        for monomial,coefficient in p.items(): result[monomial]+=coefficient
    return {m:c for m,c in result.items() if c}
def times(p,q):
    result=Counter()
    for a,x in p.items():
        for b,y in q.items():
            result[tuple(u+v for u,v in zip(a,b))]+=x*y
    return {m:c for m,c in result.items() if c}
K={(1,0,0,0):1};H={(0,1,0,0):1};d={(0,0,1,0):1};c2={(0,0,0,1):1}
D=times(d,H)
KY2=times(times(plus(K,D),plus(K,D)),D)
c2Y=times(plus(c2,times(K,D),times(D,D)),D)
assert KY2 == {(2,1,1,0):1,(1,2,2,0):2,(0,3,3,0):1}
assert c2Y == {(0,1,1,1):1,(1,2,2,0):1,(0,3,3,0):1}
print('Formal adjunction polynomial:',KY2)
print('Formal normal-bundle Chern polynomial:',c2Y)
print('Both leading d^3 coefficients are H^3. Positivity is ampleness, not computation.')
print('All checks passed; no cycle injectivity or Tate vanishing is inferred.')

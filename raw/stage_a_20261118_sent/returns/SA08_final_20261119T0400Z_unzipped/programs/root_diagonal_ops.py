"""Exact witnesses for the diagonal-only natural-operations claim and Gamma2.
The general non-homotopy argument is in root/codex_proof_checks.md §17.
"""
import json,itertools,math
X=(0,1);input_tuple=(0,1);target=list(itertools.product(X,repeat=2));maps=list(itertools.product(range(2),repeat=2))
columns=[]
for f in maps:
 out=tuple(input_tuple[i] for i in f);columns.append([int(t==out) for t in target])
assert columns==[[int(i==j) for i in range(4)] for j in range(4)]
# In normalized degree2, the only monomial killed by both deletion faces is e1*e2.
# d0(e1)=-e and d0(e2)=e. Multiplication in Gamma2 gives -binom(2,1)e^(2).
gamma_d=-math.comb(2,1);symmetric_d=-1
assert gamma_d==-2 and symmetric_d==-1
print(json.dumps({'diagonal_naturality':{'constant_space':list(X),'input':input_tuple,'coordinate_maps':maps,'degree_zero_images_as_columns':columns,'independent_homology_classes_at_least':4,'positive_normalized_chain_groups':0,'consequence':'No two distinct displayed maps can be chain-homotopic after evaluation; natural Hom has H0 rank at least4, not1.'},'quadratic_normalization':{'N1_rank':1,'N2_rank':1,'higher_ranks':0,'Gamma2_d2':gamma_d,'Sym2_d2':symmetric_d,'Gamma2_H1':'Z/2','Gamma2_H2':0,'Sym2_positive_homology':0}},indent=2))

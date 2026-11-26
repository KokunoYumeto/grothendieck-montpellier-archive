"""Finite certificates and periodic examples; no generated entry verdicts.
Each printed result is interpreted with its mathematical scope in checks.md.
"""
import itertools,json
from pathlib import Path

def functions(n,m):
    return list(itertools.product(range(m),repeat=n))

def nat_discrete(source,target):
    ans=1
    for n,m in zip(source,target):ans*=m**n
    return ans

def conjugate_discrete(values):
    return [nat_discrete(values,[int(i==j) for j in range(len(values))]) for i in range(len(values))]

def nat_arrow(F,G):
    # Presheaf on [1]: F[2]: F(1)->F(0).
    ans=[]
    for u0 in functions(F[0],G[0]):
        for u1 in functions(F[1],G[1]):
            if all(u0[F[2][x]]==G[2][u1[x]] for x in range(F[1])):ans.append((u0,u1))
    return ans

E=[0,1];pairs=list(itertools.product(E,E))
prod_maps={tuple((u[x],v[y]) for x,y in pairs) for u in functions(2,2) for v in functions(2,2)}
swap=tuple((y,x) for x,y in pairs)
X=(1,1,(0,));Y=(1,2,(0,0));Ymaps=nat_arrow(Y,Y)
out={
 '115_external_product':{'source_Hom_2x2':len(prod_maps),'target_Hom_4':4**4,'swap_in_image':swap in prod_maps,'empty_factor_source_Hom':len(functions(1,2)),'empty_factor_target_Hom':1},
 '115_exponent':{'L':2,'M':2,'L_power_M':2**2,'constant_function_image':2},
 '115_Isbell_discrete_two':{'P':[0,0],'phi_P':conjugate_discrete([0,0]),'psi_phi_P':conjugate_discrete(conjugate_discrete([0,0])),'representable_values':[[1,0],[0,1]]},
 '115_Isbell_terminal':{'P_cardinality':2,'phi_P_cardinality':1,'psi_phi_P_cardinality':1,'unit_bijective':False},
 '114_aspherical_restriction':{'comma_f_over_0_objects':1,'comma_f_over_1_objects':1,'Y_endomorphisms':len(Ymaps),'restricted_endomorphisms_at_0':len(set(t[0] for t in Ymaps)),'X_to_Y_components':[1,2],'X_to_Y_at_0_bijective':True,'X_to_Y_at_1_bijective':False},
 '115_reversed_adjoint':{'B_Hom_1_to_0':0,'Nat_f_star_y1_y_point':1},
 '115_conjugate_weak_map':{'representable_element_categories_have_terminal':True,'conjugate_y1_to_y0_at_0':[0,1],'conjugate_is_iso':False},
 '113_periodic_not_Kflat':{'ring':'Z/4','differential':'multiplication by 2 in every integer degree','kernel':[x for x in range(4) if 2*x%4==0],'image':sorted({2*x%4 for x in range(4)}),'after_tensor_Z2_differential_values':[2*x%2 for x in range(2)],'after_tensor_homology_cardinality_each_degree':2},
 '112_copower_indexing':{'inner_index':3,'outer_index':2,'iterated_copy_count':3*2,'product_index_size':len(list(itertools.product(range(3),range(2))))},
 '113_tensor_identity_rank':{'finite_dimension_sample':list(range(1,9)),'identity_ranks':list(range(1,9)),'scope':'Illustration only; the infinite-rank proof is symbolic in checks.md, not inferred from this finite list.'}
}
root=Path(__file__).resolve().parent
(root/'finite_checks.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

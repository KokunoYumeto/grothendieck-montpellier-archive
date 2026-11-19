#!/usr/bin/env python3
"""Exact certificates and finite diagnostics for cote2. General arguments in proofs.md."""
import sympy as s,json,math
z,a,t=s.symbols('z a t')
out={}
out['Chern_Koszul']=[]
for r in range(1,10):
    differences=[sum((-1)**j*math.comb(r,j)*j**k for j in range(r+1)) for k in range(r+1)]
    assert differences==[0]*r+[(-1)**r*math.factorial(r)]
    # Multiply finite coefficient vectors, avoiding expansion of enormous powers.
    coeff=[1]+[0]*r
    for j in range(r+1):
        exponent=(-1)**j*math.comb(r,j)
        factor=[int(s.binomial(exponent,k))*(-j)**k for k in range(r+1)]
        coeff=[sum(coeff[q]*factor[k-q] for q in range(k+1)) for k in range(r+1)]
    trunc=sum(coeff[k]*z**k for k in range(r+1))
    expected=1+(-1)**(r-1)*math.factorial(r-1)*z**r
    assert s.expand(trunc-expected)==0
    out['Chern_Koszul'].append({'r':r,'finite_differences':differences,'c_xi_power':str(trunc),'rank_zero_coefficient':(-1)**r*math.factorial(r)})
P3=(1+z)**3*(1+3*z)/(1+2*z)**3
num=s.expand((1+z)**3*(1+3*z)-(1+2*z)**3)
assert num==2*z**3+3*z**4
assert s.expand(3*z**4-z*(2*z**3))==z**4
out['universal_n3']={'numerator_of_P3_minus_1':str(num),'series':str(s.series(P3,z,0,8)), 'homogeneous_ideal':'(2*z^3,3*z^4)=(2*z^3,z^4)', 'nonzero_kernel_witness':'degree3 generator has order2; gr_gamma has degree3=0'}
out['finite_degree_criterion']=[]
for n in range(0,9):
    coefficients=[]
    for k in range(n+1,n+8):
        v=sum(math.comb(n,j)*(-1)**(k-j-1)*(k-j)**n for j in range(n+1))
        assert v==(-1)**(k-1)*math.factorial(n)
        coefficients.append(v)
    out['finite_degree_criterion'].append({'n':n,'tail_coefficients_of_a':coefficients,'annihilator':math.factorial(n)})
out['modified_product']=[{'i':i,'j':j,'factor':-math.factorial(i+j-1)//(math.factorial(i-1)*math.factorial(j-1))} for i in range(1,5) for j in range(1,5)]
# The explicit lambda-compatibility countermodel: epsilon^2=0, x maps to2,
# y=lambda^2(x) maps to the rank-one class with c1=epsilon. No averaging.
out['lambda_relation_gap']={'rank_x':2,'rank_y':1,'c1(lambda2_image_x)':0,'c1(image_lambda2_x)':'epsilon, nonzero in Z[epsilon]/epsilon^2','result':'ring-map/selected-rank relations do not imply lambda compatibility'}
gamma_L=s.series(1+s.Symbol('L')*t/(1-t),t,0,4)
out['unshifted_gamma']={'gamma_t_L':str(gamma_L),'gamma2_L':'L','gamma_t_L_minus_1':'1+(L-1)*t','evaluation_at_L1':'gamma2(L)=1; all shifted positive-weight ideal generators=0'}
out['periodic_resolution']=[]
for n in range(2,9):
    def mult(k):return s.Matrix(n,n,lambda i,j:1 if i==j+k else 0)
    d1,d2=mult(1),mult(n-1)
    assert d1*d2==s.zeros(n) and d2*d1==s.zeros(n)
    assert n-d1.rank()==d2.rank() and n-d2.rank()==d1.rank()
    out['periodic_resolution'].append({'n':n,'rank_t':d1.rank(),'rank_t_nminus1':d2.rank(),'Ext_Bn_k_k':'dimension1 in every degree because both maps become0 under Hom(-,k)','Ext_k[t]_k_k':'dimension1 in degrees0,1;0 in degree>=2'})
I=s.I;Q=lambda x:x*x
rhs=s.expand(Q(2)-Q(0)+I*Q(1+I)-I*Q(1-I))
assert rhs==0
out['bimodule_polarization']={'A':'C, J=conjugation; F right action z.a=z*conjugate(a); Phi(x,y)=xy','x':1,'y':1,'left_4Phi':4,'right_formula14':str(rhs),'scope':'conditional on usual bimodule sesquilinearity; missing axioms may exclude this module'}
omega=-s.Rational(1,2)+s.sqrt(3)*I/2
out['induction_C3_S3']={'trace_ResInd_at_generator':str(s.simplify(omega+omega**2)),'trace_chi_plus_chi':str(2*omega),'distinct':s.simplify(omega+omega**2-2*omega)!=0}
n,delta,C,KY,fd,fK=s.symbols('n delta C K_Y f_d f_K')
c1=n*delta*C;ch2=fd-n*fK/2+n*delta*C*KY/2
c2=s.expand(c1*c1/2-ch2)
expected=n*n*delta*delta*C*C/2-n*delta*C*KY/2-fd+n*fK/2
assert s.expand(c2-expected)==0
out['curve_surface']= {'ch1':str(c1),'ch2':str(ch2),'c2':str(c2)}
out['nodal_cubic']={'C_squared':9,'C_KP2':-9,'normalization_genus':0,'displayed_degree':(9+9)//2-1,'actual_c2_O_C':9,'normalization_defect':1,'verified_example':'irreducible nodal plane cubic over C; reduced Cartier divisor in smooth P2'}
out['curve_degree']=[]
for p in [2,3,5,7]:
 for g in [0,1,2,4]:
  degree=(1-g)-p*(1-g)
  assert degree==(p-1)*(g-1)
  out['curve_degree'].append({'p':p,'g':g,'deg_Frobenius_pushforward_O':degree})
out['Cartan_Artin']=[{'m':m,'K0':'Z','G0':'Z','Cartan_multiplier':m,'cokernel':'Z/'+str(m)} for m in range(1,9)]
out['torsion_coefficient_test']={'r':2,'torsion_order':5,'multiplier':2,'images':[2*x%5 for x in range(5)],'injective':len({2*x%5 for x in range(5)})==5,'scope':'abstract coefficient ring, not a geometric counterexample'}
out['elliptic_examples']=[{'r':r,'coefficient':(-1)**r*math.factorial(r),'coefficient_mod_2':math.factorial(r)%2,'nonzero':'projection pushforward is a left inverse'} for r in [2,3]]
qx,qy,xy,yx=s.symbols('Qx Qy Phi_xy Phi_yx')
qplus=qx+xy+yx+qy;qminus=qx-xy-yx+qy
qiplus=qx-I*xy+I*yx+qy;qiminus=qx+I*xy-I*yx+qy
assert s.expand(qplus-qminus-2*(xy+yx))==0
assert s.expand(qplus-qminus+I*qiplus-I*qiminus-4*xy)==0
out['polarization_scalar_identities']={'formula11_residual':0,'formula14_residual':0,'assumptions':'scalar-valued form over commutativeK(i),i²=−1,J(i)=−i; no division by2or4 used'}
print(json.dumps(out,ensure_ascii=False,indent=2,default=str))

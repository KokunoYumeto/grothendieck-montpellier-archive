"""Mathematical transcription of Dabbaghian-Abdoly2006, pp620--623.

Basis order: 1,a1,a2,b,c,d1,d2. Negative character labels in the paper
are normalized to the actual positive-degree irreducible character.
The degree and all six unipotent values are reconstructed from the
printed six basis rows and the restriction identities, except four
explicit Table2 overrides. The indexed identity text for those four
rows swaps d1/d2 relative to Table2. That discrepancy is recorded and
the inconsistent identity text is not used to certify those rows.
"""
from fractions import Fraction
from pathlib import Path
import json

BASIS=['1','a1','a2','b','c','d1','d2']
ROWS={
 '1':[1,0,0,0,0,0,0],
 'chi1':[0,0,0,4,0,1,1],
 'chi2':[-2,0,0,2,2,1,1],
 'chi3':[-4,4,4,4,4,1,1],
 'chi4':[0,0,0,0,0,1,1],
 'chi5':[-4,2,2,4,0,1,1],
 'chi6':[-1,0,0,1,1,0,0],
 'chi7':[-1,0,0,1,1,1,1],
 'chi8':[-1,2,2,1,1,0,0],
 'chi9':[-3,2,2,3,3,1,1],
 'xi1':[-2,1,1,2,0,0,0],
 'xi1prime':[-2,1,1,2,0,1,1],
 'xi3':[0,1,1,0,2,0,0],
 'xi3prime':[-4,3,3,4,2,1,1],
 'xi21':[-2,1,1,2,0,1,0],
 'xi22':[-2,1,1,2,0,0,1],
 'xi21prime':[0,0,0,0,0,1,0],
 'xi22prime':[0,0,0,0,0,0,1],
 'xi41':[-2,1,3,2,2,1,0],
 'xi42':[-2,3,1,2,2,0,1],
 'xi41prime':[-2,2,0,2,0,0,1],
 'xi42prime':[-2,0,2,2,0,1,0],
 'Phi1':[-1,1,0,1,0,0,0],
 'Phi2':[-1,0,1,1,0,0,0],
 'Phi3':[-1,1,0,1,0,1,0],
 'Phi4':[-1,0,1,1,0,0,1],
 'Phi5':[0,0,1,0,1,0,0],
 'Phi6':[0,1,0,0,1,0,0],
 'Phi7':[-2,1,2,2,1,0,1],
 'Phi8':[-2,2,1,2,1,1,0],
 'Phi9':[-1,1,1,1,1,0,0],
 'theta1':[-1,0,1,1,1,0,1],
 'theta2':[-1,1,0,1,1,1,0],
 'theta3':[0,1,0,0,0,0,0],
 'theta4':[0,0,1,0,0,0,0],
 'theta5':[-1,1,0,2,0,1,0],
 'theta6':[-1,0,1,2,0,0,1],
 'theta7':[-1,1,0,0,0,0,0],
 'theta8':[-1,0,1,0,0,0,0],
 'theta9':[-1,1,1,0,1,0,0],
 'theta10':[0,0,0,1,0,0,0],
 'theta11':[-1,1,1,1,0,0,0],
 'theta12':[0,0,0,0,1,0,0],
 'theta13':[-2,1,1,3,1,1,1],
}

def symbolic():
 import sympy as s
 q,t=s.symbols('q t');ep=(-1+t)/2;em=(-1-t)/2
 one=[s.Integer(1)]*7
 a=[(q*q+1)/2,(q+1)/2+q*ep,(q+1)/2+q*em,(q+1)/2,(1-q)/2,-em,-ep]
 aa=[x.subs(t,-t) for x in a]
 b=[q*(q-1)**2/2,q*(1-q)/2,q*(1-q)/2,s.Integer(0),q,s.Integer(0),s.Integer(0)]
 c=[q*(q*q+1)/2,q*(q+1)/2,q*(q+1)/2,s.Integer(0),q,s.Integer(0),s.Integer(0)]
 d=[(q-1)**2*(q*q+1)/2,(1-q)/2-q*(q-1)*em,(1-q)/2-q*(q-1)*ep,(1-q)/2,(1-3*q)/2,-ep,-em]
 dd=[x.subs(t,-t) for x in d]
 bs=[one,a,aa,b,c,d,dd]
 rs={n:[s.expand(sum(v[i]*bs[i][j] for i in range(7))) for j in range(7)] for n,v in ROWS.items()}
 # Read directly from Table2p621. These are not inferred by fitting
 # finite character tables; those provide a separate cross-check.
 z=[(q+1)**2*(q*q+1)/2,(1+q)/2-q*(1+q)*ep,(1+q)/2-q*(1+q)*em,(1+3*q)/2,(1+q)/2,-ep,-em]
 zz=[(q**4-1)/2,-(1-q)/2+q*(1+q)*ep,-(1-q)/2+q*(1+q)*em,-(1-q)/2,-(1+q)/2,ep,em]
 rs['xi41']=[s.expand(v) for v in z];rs['xi42']=[s.expand(v.subs(t,-t)) for v in z]
 rs['xi41prime']=[s.expand(v) for v in zz];rs['xi42prime']=[s.expand(v.subs(t,-t)) for v in zz]
 return q,t,bs,rs

if __name__=='__main__':
 q,t,bs,rs=symbolic()
 result={'source':'Dabbaghian-Abdoly, Journal of Algebra303(2006)618--625, Table2p621 and restriction identitiespp622--623',
 'source_url':'https://www.researchgate.net/publication/222038219_Constructing_representations_of_the_finite_symplectic_group_Sp4q',
 'source_scope':'Complete ordinary characters restricted to all unipotent classes; not a full semisimple-value table',
 'columns':['A1','A21','A22','A31','A32','A41','A42'],'basis_order':BASIS,
 'root_convention':'t^2=(-1)^((q-1)/2)*q; epsilon=(-1+t)/2,epsilonprime=(-1-t)/2; swapping the root exchanges paired labels',
 'basis_rows':[[str(x) for x in row] for row in bs],
 'indexed_restriction_vectors':ROWS,
 'direct_Table2_overrides':['xi41','xi42','xi41prime','xi42prime'],
 'source_discrepancy':'These four indexed restriction identities disagree with Table2 by d1/d2 exchange. Direct Table2 values are used; failed optional-identity comparison is retained separately.',
 'expanded_rows':{n:[str(x) for x in row] for n,row in rs.items()}}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
 print('Transcribed',len(rs),'types including the trivial type')

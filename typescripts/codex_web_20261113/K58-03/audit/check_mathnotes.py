"""Only the integer indices, never the geometric or cohomological assertions."""
from sympy import symbols,expand
n,k,i=symbols('n k i',integer=True)
K=n+k
identities=[('M1, dimension before quotient',K+1,(n+k)+1),
            ('M1, dimension after quotient',K-n,k),
            ('M2, central degree in case a',(i+1).subs(i,n-1),n),
            ('M2, central degree in case b',(i+1).subs(i,n),n+1)]
for label,lhs,rhs in identities:
 difference=expand(lhs-rhs)
 assert difference==0
 print(label,lhs,rhs,difference,sep='\t')

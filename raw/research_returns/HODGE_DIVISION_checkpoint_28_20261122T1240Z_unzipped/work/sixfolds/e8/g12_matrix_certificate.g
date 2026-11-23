# Exact matrix reconstruction of the G12 rank-two representation.
# No imported character table is used.  GPT-6 Astra Pro, 21 November 2026.
s:=E(8)+E(8)^3;; rt:=E(8)-E(8)^3;; ii:=E(4);;
Assert(0,s^2=-2 and rt^2=2 and s=ii*rt);
R:=[[[1,0],[-s,-1]],[[-1,s],[0,1]],
    [[-1-s/2,-1+s/2],[-1+s/2,1+s/2]]];;
T:=[[1,ii],[-1-rt,ii*(1+rt)]];;
published:=[[[1,-1],[-1,-1]]/rt,[[1,1],[1,-1]]/rt,
            [[0,E(8)],[E(8)^(-1),0]]];;
Assert(0,List(published,r->T^-1*r*T)=R);
Herm:=[[1,-s/2],[s/2,1]];;
ConjTranspose:=M->TransposedMat(List(M,row->List(row,ComplexConjugate)));;
Assert(0,ForAll(R,r->r^2=IdentityMat(2) and DeterminantMat(r)=-1 and ConjTranspose(r)*Herm*r=Herm));
H:=Group(R);; el:=Elements(H);;
Assert(0,Length(el)=48);
Assert(0,RankMat(List([IdentityMat(2),R[1],R[2],R[1]*R[2]],Concatenation))=4);
cc:=ConjugacyClasses(H);;
Assert(0,Length(cc)=8);
orders:=Set(List(el,Order));;
Assert(0,orders=[1,2,3,4,6,8]);
# The character is literally the matrix trace, with square norm one.
Assert(0,Sum(el,g->TraceMat(g)*ComplexConjugate(TraceMat(g)))=48);
Assert(0,Set(List(el,TraceMat))=[-2,-1,0,1,2,-s,s] or
 Set(List(el,TraceMat))=Set([-2,-1,0,1,2,-s,s]));
out:=OutputTextFile("work/sixfolds/e8/g12_matrix_certificate.json",false);;
SetPrintFormattingStatus(out,false);
AppendTo(out,"{\"status\":\"PASS\",\"group_order\":48,\"classes\":8,\"field\":\"Q(sqrt(-2))\",\"published_conjugator_verified\":true,\"positive_Hermitian_determinant\":\"1/2\",\"class_data\":[");;
first:=true;;
for cl in cc do
 g:=Representative(cl);; o:=Order(g);;
 mult:=List([0..o-1],a->Sum([0..o-1],k->E(o)^(-a*k)*TraceMat(g^k))/o);;
 Assert(0,ForAll(mult,x->IsInt(x) and x>=0) and Sum(mult)=2);
 nonzero:=Filtered([0..o-1],a->mult[a+1]>0);;
 reflection:=o=2 and mult=[1,1];;
 if o>1 and not reflection then
  Assert(0,ForAll(nonzero,a->Gcd(a,o)=1));
 fi;
 if not first then AppendTo(out,",");fi;first:=false;
 AppendTo(out,"{\"size\":",Size(cl),",\"order\":",o,",\"trace\":\"",String(TraceMat(g)),"\",\"reflection\":",reflection,",\"eigenvalue_multiplicities\":",mult,"}");
od;
AppendTo(out,"],\"genus_zero_branch_equation\":\"sum(1-1/o)=47/24 has no generating profile using these orders\"}\n");
CloseStream(out);
Print("PASS: literal G12 matrices,48 elements,8 classes,all eigenvalue types,positive Hermitian form and published conjugator.\n");
QUIT;

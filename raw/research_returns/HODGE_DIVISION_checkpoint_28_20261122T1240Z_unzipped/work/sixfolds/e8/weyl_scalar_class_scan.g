# Exact E6/E7 class scan from the Cartan matrices, with no imported tables.
# GPT-6 Astra Pro, /root/sixfolds, 21 November 2026.
if not IsBound(RANK) then RANK:=6; fi;
m:=RANK;; U:=IdentityMat(m);;
C:=2*U;;
for edge in [[1,3],[3,4],[4,5],[5,6],[6,7],[7,8],[2,4]] do
 if Maximum(edge)<=m then C[edge[1]][edge[2]]:=-1; C[edge[2]][edge[1]]:=-1; fi;
od;
simple:=List([1..m],i->U-List([1..m],r->List([1..m],s->U[r][i]*C[i][s])));;
roots:=ShallowCopy(U);;
for root in roots do
 for s in simple do
  v:=List(s,row->row*root);
  if not v in roots then Add(roots,v); fi;
 od;
od;
Sort(roots);;
ToPerm:=function(M)
 return PermList(List(roots,r->Position(roots,List(M,row->row*r))));
end;;
sp:=List(simple,ToPerm);; W:=Group(sp);;
ei:=List(U,r->Position(roots,r));;
ToMatrix:=function(p)
 # Transpose the column-action matrix to obtain a genuine representation.
 return List(ei,j->roots[j^p]);
end;;
Assert(0,ForAll([1..m],i->ToMatrix(sp[i])=TransposedMat(simple[i])));
for g in sp do for h in sp do Assert(0,ToMatrix(g*h)=ToMatrix(g)*ToMatrix(h)); od; od;
cc:=ConjugacyClasses(W);;
Print("RANK ",m," roots ",Length(roots)," group ",Size(W)," classes ",Length(cc),"\n");
data:=[];; maxfix:=0;;
for cl in cc do
 g:=Representative(cl);; M:=ToMatrix(g);;
 f:=m-RankMat(M-E(4)*U);;
 Assert(0,f=m-RankMat(M+E(4)*U));
 maxfix:=Maximum(maxfix,f);
 Add(data,rec(size:=Size(cl),order:=Order(g),fixed_i:=f,
     fixed_one:=m-RankMat(M-U),fixed_minusone:=m-RankMat(M+U),
     charpoly:=CoefficientsOfUnivariatePolynomial(CharacteristicPolynomial(M)),
     matrix:=M));
od;
Assert(0,Sum(data,r->r.size)=Size(W));
Print("MAX i-FIX ",maxfix," MIN outside CODIM ",m-maxfix,"\n");
Print("MAX CLASSES ",Filtered(data,r->r.fixed_i=maxfix),"\n");
SizeScreen([100000,60]);;
out:=Concatenation("/workspace/scratch/b92e12834723/work/sixfolds/e8/e",String(m),"_classes.json");;
PrintTo(out,"{\"rank\":",m,",\"root_count\":",Length(roots),",\"group_order\":",Size(W),
 ",\"contains_minus_identity\":",ToPerm(-U) in W,",\"class_count\":",Length(cc),
 ",\"maximum_fixed_i\":",maxfix,",\"cartan\":",C,",\"simple_reflections\":",List(sp,ToMatrix),",\"classes\":[");
for j in [1..Length(data)] do
 r:=data[j];;
 if j>1 then AppendTo(out,",");fi;
 AppendTo(out,"{\"size\":",r.size,",\"order\":",r.order,",\"fixed_i\":",r.fixed_i,
  ",\"fixed_one\":",r.fixed_one,",\"fixed_minusone\":",r.fixed_minusone,
  ",\"charpoly\":",r.charpoly,",\"matrix\":",r.matrix,"}");
od;
AppendTo(out,"]}\n");
Print("CLASS SCAN PASS\n");
QUIT;

# HD-S32: exact Cohen N4/EW(N4) matrices and local resultants.
# GPT-6 Astra Pro, /root/sixfolds, 21 November 2026.
# No imported group, class, or character table.
ii:=E(4);; I4:=IdentityMat(4);;
roots:=[(1+ii)/2*[0,1,0,1],(1+ii)/2*[0,-1,1,0],
        [-1,ii,-1,ii]/2,[1,0,0,0],[1,1,1,1]/2];;
ConjTranspose:=M->TransposedMat(List(M,row->List(row,ComplexConjugate)));;
Reflect:=v->I4-2*TransposedMat([v])*[List(v,ComplexConjugate)];;
R:=List(roots,Reflect);;
Assert(0,ForAll(roots,v->v*List(v,ComplexConjugate)=1));
Assert(0,ForAll(R,r->r^2=I4 and ConjTranspose(r)*r=I4 and RankMat(I4-r)=1));
Assert(0,ForAll(Concatenation(R),row->ForAll(row,x->IsInt(2*RealPart(x)) and IsInt(2*ImaginaryPart(x)))));

reports:=[];;
for nref in [4,5] do
 gens:=R{[1..nref]};;
 orbit:=ShallowCopy(I4);;
 for v in orbit do
  for r in gens do
   u:=v*r;
   if not u in orbit then Add(orbit,u);fi;
  od;
  Assert(0,Length(orbit)<=1000);
 od;
 Sort(orbit);;
 Assert(0,ForAll(orbit,v->ForAll(v,x->IsInt(2*RealPart(x)) and IsInt(2*ImaginaryPart(x)))));
 bp:=List(I4,v->Position(orbit,v));;
 pp:=List(gens,r->PermList(List(orbit,v->Position(orbit,v*r))));;
 G:=Group(pp);; size:=Size(G);;
 Assert(0,size=([7680,46080][nref-3]));
 ToMat:=p->List(bp,j->orbit[j^p]);;
 Assert(0,List(pp,ToMat)=gens);
 for a in pp do for b in pp do Assert(0,ToMat(a*b)=ToMat(a)*ToMat(b));od;od;
 scalar:=PermList(List(orbit,v->Position(orbit,ii*v)));;
 Assert(0,scalar in G and ToMat(scalar)=ii*I4);
 classes:=ConjugacyClasses(G);;
 scalarprod:=Sum(classes,c->Size(c)*TraceMat(ToMat(Representative(c)))*ComplexConjugate(TraceMat(ToMat(Representative(c)))));;
 Assert(0,scalarprod=size);
 out:=OutputTextFile(Concatenation("work/sixfolds/g29/g",String([29,31][nref-3]),"_scope_certificate.json"),false);;
 SetPrintFormattingStatus(out,false);
 AppendTo(out,"{\"status\":\"PASS\",\"group\":",[29,31][nref-3],",\"order\":",size,",\"orbit_size\":",Length(orbit),",\"class_count\":",Length(classes),",\"central_i_verified\":true,\"all_matrix_entries_in_half_Gaussian_integers\":true,\"coefficient_lattice\":\"Z[i,1/2]^4\",\"Hermitian_Gram\":\"I4\",\"character_norm\":1,\"class_data\":[");
 first:=true;; resultants:=[];; reflectioncount:=0;;
 for cl in classes do
  p:=Representative(cl);; M:=ToMat(p);; o:=Order(p);;
  c:=RankMat(I4-M);; fixed:=4-c;;
  cp:=CharacteristicPolynomial(M);; dp:=cp;;
  for j in [1..fixed] do dp:=Derivative(dp);od;
  f1:=Value(dp,1)/Factorial(fixed);; norm:=f1*ComplexConjugate(f1);;
  Assert(0,norm>0 and IsInt(norm) and IsInt(RealPart(f1)) and IsInt(ImaginaryPart(f1)));
  Assert(0,ForAll(PrimeDivisors(norm),p->p in [2,3,5]));
  avg:=NullMat(4,4);; power:=I4;; bezout:=NullMat(4,4);;
  for j in [0..o-1] do avg:=avg+power/o;bezout:=bezout+(o-1-j)*power/o;power:=power*M;od;
  Assert(0,power=I4 and avg^2=avg and RankMat(avg)=fixed and (I4-M)*bezout=I4-avg);
  if c=1 then reflectioncount:=reflectioncount+Size(cl);Assert(0,o=2);fi;
  AddSet(resultants,norm);
  if not first then AppendTo(out,",");fi;first:=false;
  AppendTo(out,"{\"size\":",Size(cl),",\"order\":",o,",\"codimension\":",c,",\"characteristic_polynomial\":\"",String(cp),"\",\"moving_resultant\":\"",String(f1),"\",\"resultant_norm\":",norm,"}");
 od;
 Assert(0,reflectioncount=[40,60][nref-3]);
 AppendTo(out,"],\"reflection_count\":",reflectioncount,",\"all_reflections_involutive\":true,\"moving_resultant_norms\":",resultants,",\"all_local_projectors_and_Bezout_maps_verified\":true}\n");
 CloseStream(out);
 Print("PASS G",[29,31][nref-3],": order ",size,", orbit ",Length(orbit),", classes ",Length(classes),", reflections ",reflectioncount,", resultant norms ",resultants,"\n");
od;
QUIT;

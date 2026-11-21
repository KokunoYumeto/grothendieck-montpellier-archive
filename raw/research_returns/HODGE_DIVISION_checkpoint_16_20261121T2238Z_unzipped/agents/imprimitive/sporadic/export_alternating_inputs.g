if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
SetAssertionLevel(1);;
SporAltEncode:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
SporAltExport:=function()
 local out,n,name,t,ir,nr,center,z,rows,r,p2,i,witness,chi,fs;
 out:=rec(tables:=[],source:="CTblLib1.3.11; exact complete tables for root HD-SPIN-01 audit");
 for n in [6,8,9,10,11] do
  name:=Concatenation("2.A",String(n));t:=CharacterTable(name);ir:=Irr(t);nr:=Length(ir);
  Assert(1,MatScalarProducts(t,ir,ir)=IdentityMat(nr));
  Assert(1,Sum(ir,x->x[1]^2)=Size(t));
  center:=Filtered([1..nr],j->SizesConjugacyClasses(t)[j]=1);
  Assert(1,Length(center)=2);z:=First(center,j->OrdersClassRepresentatives(t)[j]=2);
  rows:=Filtered([1..nr],j->ir[j][z]=-ir[j][1]);
  p2:=PowerMap(t,2);witness:=[];
  for i in Filtered(rows,j->ir[j][1]=24) do
   chi:=ir[i];fs:=Sum([1..nr],j->SizesConjugacyClasses(t)[j]*chi[p2[j]])/Size(t);
   Add(witness,rec(row:=i,indicator:=fs,conjugate_row:=Position(ir,ComplexConjugate(chi)),
       nonreal_classes:=Filtered([1..nr],j->chi[j]<>GaloisCyc(chi[j],-1))));
  od;
  r:=rec(name:=name,order:=Size(t),class_names:=ClassNames(t),
       orders:=OrdersClassRepresentatives(t),sizes:=SizesConjugacyClasses(t),
       characters:=List(ir,c->List(c,SporAltEncode)),information:=InfoText(t),
       power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))),
       central_involution_class:=z,faithful_rows:=rows,faithful_degrees:=List(rows,j->ir[j][1]),
       degree24_witnesses:=witness);
  Add(out.tables,r);
  Print(name,": ",nr," classes, faithful degrees ",r.faithful_degrees,"; degree24 ",witness,"\n");
 od;
 return out;
end;
data:=SporAltExport();;
stream:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/sporadic/alternating_cover_inputs.json",false);;
SetPrintFormattingStatus(stream,false);PrintTo(stream,AGR.JsonText(data,"ASCII"));CloseStream(stream);
QUIT;

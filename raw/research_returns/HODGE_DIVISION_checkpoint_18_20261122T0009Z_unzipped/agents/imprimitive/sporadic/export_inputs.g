# Export compact exact mathematical inputs, not the third-party package archive.
if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
SetAssertionLevel(1);;
root:=Directory("HODGE_DIVISION_work/agents/imprimitive/sporadic");;
SporEncodeCyc:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);
 Assert(1,ForAll(c,IsInt));
 return [n,c];
end;
WriteJSON:=function(file,obj)
 local s;
 s:=OutputTextFile(Filename(root,file),false);
 SetPrintFormattingStatus(s,false);PrintTo(s,AGR.JsonText(obj,"ASCII"));CloseStream(s);
end;
simple:=AllCharacterTableNames(IsSporadicSimple,true,IsDuplicateTable,false);;
metadata:=[];;names:=[];;
for sname in simple do
 s:=CharacterTable(sname);;x:=ExtensionInfoCharacterTable(s);;
 cname:=sname;;if x[1]<>"" then cname:=Concatenation(x[1],".",sname);fi;
 c:=CharacterTable(cname);;
 Add(names,[cname,fail]);
 r:=rec(simple:=sname,multiplier:=x[1],outer:=x[2],cover:=cname,
        simple_order:=Size(s),cover_order:=Size(c),simple_information:=InfoText(s));;
 Assert(1,x[2] in ["","2"]);
 if x[2]="2" then
  ename:=Concatenation(cname,".2");;a:=CharacterTable(ename);;
  Assert(1,a<>fail);Assert(1,Size(a)=2*Size(c));
  Add(names,[ename,cname]);r.extension:=ename;
 fi;
 Add(metadata,r);
od;
Assert(1,Length(simple)=26);Assert(1,Length(names)=38);
WriteJSON("coverage.json",rec(simple_groups:=metadata,gap_version:=GAPInfo.Version,
          ctbllib_version:=PackageInfo("ctbllib")[1].Version));
inputs:=[];;
for pair in names do
 t:=CharacterTable(pair[1]);;irr:=Irr(t);;nr:=Length(irr);;
 # A fresh exact orthogonality check of the complete table.
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
 Assert(1,Sum(irr,x->x[1]^2)=Size(t));
 r:=rec(name:=Identifier(t),order:=Size(t),class_names:=ClassNames(t),
       orders:=OrdersClassRepresentatives(t),sizes:=SizesConjugacyClasses(t),
       characters:=List(irr,c->List(c,SporEncodeCyc)),information:=InfoText(t),
       power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));;
 if pair[2]<>fail then
  r.core:=pair[2];r.fusion:=GetFusionMap(CharacterTable(pair[2]),t);
  Assert(1,r.fusion<>fail);
 fi;
 Add(inputs,r);
 Print(Identifier(t),": exact row orthogonality PASS, ",nr," classes\n");
od;
WriteJSON("character_inputs.json",rec(tables:=inputs,encoding:="integer, or [conductor, coefficients of powers zeta^0,...,zeta^(conductor-1)]",source:="CTblLib 1.3.11; InfoText source locators retained table by table"));
Print("EXPORTED ",Length(inputs)," complete tables\n");
QUIT;

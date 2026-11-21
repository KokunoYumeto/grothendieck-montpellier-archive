# Full exceptional small-field universal-cover inputs, including actual outers.
if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
SetAssertionLevel(1);;
dest:=Directory("HODGE_DIVISION_work/agents/imprimitive/lie_small_fields");;
EncodeCyc:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
pairs:=[["3.G2(3)",fail],["3.G2(3).2","3.G2(3)"],
 ["2.G2(4)",fail],["2.G2(4).2","2.G2(4)"],
 ["3D4(2)",fail],["3D4(2).3","3D4(2)"]];;
tabs:=[];;meta:=[];;t:=fail;;
for nm in ["G2(3)","G2(4)","3D4(2)"] do
 s:=CharacterTable(nm);Add(meta,rec(name:=nm,extension_info:=ExtensionInfoCharacterTable(s),information:=InfoText(s)));
od;
for pair in pairs do
 t:=CharacterTable(pair[1]);irr:=Irr(t);n:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(n));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),sizes:=SizesConjugacyClasses(t),
  class_names:=ClassNames(t),characters:=List(irr,c->List(c,EncodeCyc)),information:=InfoText(t),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
 if pair[2]<>fail then r.core:=pair[2];r.fusion:=GetFusionMap(CharacterTable(pair[2]),t);Assert(1,r.fusion<>fail);fi;
 Add(tabs,r);Print(pair[1]," ",n," rows PASS\n");
od;
out:=OutputTextFile(Filename(dest,"g2_triality_small_inputs.json"),false);;
SetPrintFormattingStatus(out,false);PrintTo(out,AGR.JsonText(rec(tables:=tabs,metadata:=meta,
 gap_version:=GAPInfo.Version,ctbllib_version:=PackageInfo("ctbllib")[1].Version),"ASCII"));CloseStream(out);
QUIT;

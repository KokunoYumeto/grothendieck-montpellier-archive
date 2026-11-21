# Complete universal-cover and outer-extension inputs for Sp4(3).
if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
SetAssertionLevel(1);;
dir:=Directory("HODGE_DIVISION_work/agents/imprimitive/lie_small_fields");;
EncodeCyc:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));
 return [n,c];
end;
tabs:=[];;
for name in ["2.U4(2)","2.U4(2).2"] do
 t:=CharacterTable(name);irr:=Irr(t);n:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(n));
 recd:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,c->List(c,EncodeCyc)),information:=InfoText(t),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))),
  frobenius_schur:=Indicator(t,irr,2));
 if name="2.U4(2).2" then
  recd.core:="2.U4(2)";recd.fusion:=GetFusionMap(CharacterTable(recd.core),t);
  Assert(1,recd.fusion<>fail);
 fi;
 Add(tabs,recd);Print(name,": ",n," full rows, orthogonality PASS\n");
od;
s:=CharacterTable("U4(2)");;
obj:=rec(tables:=tabs,simple_metadata:=rec(name:=Identifier(s),order:=Size(s),
 extension_info:=ExtensionInfoCharacterTable(s),information:=InfoText(s)),
 gap_version:=GAPInfo.Version,ctbllib_version:=PackageInfo("ctbllib")[1].Version,
 encoding:="integer or [conductor, coefficients of powers of a primitive root]");;
out:=OutputTextFile(Filename(dir,"sp4_3_character_inputs.json"),false);;
SetPrintFormattingStatus(out,false);PrintTo(out,AGR.JsonText(obj,"ASCII"));CloseStream(out);
QUIT;

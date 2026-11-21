if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
if LoadPackage("atlasrep")<>true then Error("AtlasRep missing");fi;
SetAssertionLevel(1);;
EncodeCyc:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));
 return [n,c];
end;
pairs:=[["2.S4(5)","2.S4(5)"],["2.S4(5).2","2.S4(5)"],
 ["S4(7)","S4(7)"],["S4(7).2","S4(7)"],
 ["S4(9)","S4(9)"],["S4(9).2_1","S4(9)"],
 ["S4(9).2_2","S4(9)"],["S4(9).2_3","S4(9)"]];;
tabs:=[];;
for pair in pairs do
 name:=pair[1];core:=pair[2];t:=CharacterTable(name);irr:=Irr(t);n:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(n));
 recd:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,c->List(c,EncodeCyc)),information:=InfoText(t),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))),
  frobenius_schur:=Indicator(t,irr,2),core:=core);
 if name<>core then
  recd.fusion:=GetFusionMap(CharacterTable(core),t);
  Assert(1,recd.fusion<>fail);
 fi;
 Add(tabs,recd);Print(name,": ",n," full rows, orthogonality PASS\n");
od;
meta:=[];;
for name in ["S4(5)","S4(7)","S4(9)"] do
 t:=CharacterTable(name);
 Add(meta,rec(name:=name,extension_info:=ExtensionInfoCharacterTable(t),
  information:=InfoText(t),order:=Size(t)));
od;
obj:=rec(tables:=tabs,simple_metadata:=meta,
 gap_version:=GAPInfo.Version,ctbllib_version:=PackageInfo("ctbllib")[1].Version,
 encoding:="integer or [conductor, coefficients of powers of a primitive root]",
 coverage:="Full universal-cover q5; only center-positive q7 andq9. No assertion about otherq or center-negativeq7/9.");;
out:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/odd_c2/character_inputs.json",false);;
SetPrintFormattingStatus(out,false);PrintTo(out,AGR.JsonText(obj,"ASCII"));CloseStream(out);
QUIT;

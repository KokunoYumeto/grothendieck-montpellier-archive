LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetInfoLevel(InfoPackageLoading,0);;
SetAssertionLevel(1);;
EncodeOrthogonal:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
out:=rec(tables:=[],metadata:=[],gap_version:=GAPInfo.Version,
 ctbllib_version:=PackageInfo("ctbllib")[1].Version);;
for name in ["O7(3)","O8-(2)","O8+(3)","O8-(3)","O9(3)","O10+(2)","O10-(2)","O12+(2)","O12-(2)"] do
 t:=CharacterTable(name);
 Add(out.metadata,rec(name:=name,extension_information:=ExtensionInfoCharacterTable(t)));
od;
ExportOrthogonalTable:=function(pair)
 local name,core,t,irr,r,f;
 name:=pair[1];core:=pair[2];t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);
 Print("BEGIN ",name," full orthogonality ",Length(irr)," rows\n");
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(Length(irr)));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,c->List(c,EncodeOrthogonal)),information:=InfoText(t),
  indicators:=Indicator(t,irr,2),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))),
  full_row_orthogonality_checked:=true);
 if name<>core then
  f:=GetFusionMap(CharacterTable(core),t);Assert(1,f<>fail);
  r.core:=core;r.fusion:=f;
 fi;
 Print("PASS ",name," full orthogonality and export\n");
 return r;
end;
for pair in [["6.O7(3)","6.O7(3)"],["6.O7(3).2","6.O7(3)"],
 ["O8-(2)","O8-(2)"],["O8-(2).2","O8-(2)"],
 ["2^2.O8+(3)","2^2.O8+(3)"],["2.O8-(3)","2.O8-(3)"],
 ["2.O9(3)","2.O9(3)"],
 ["O10+(2)","O10+(2)"],["O10+(2).2","O10+(2)"],
 ["O10-(2)","O10-(2)"],["O10-(2).2","O10-(2)"],
 ["O12+(2)","O12+(2)"],["O12+(2).2","O12+(2)"],
 ["O12-(2)","O12-(2)"],["O12-(2).2","O12-(2)"]] do
 Add(out.tables,ExportOrthogonalTable(pair));
od;
f:=OutputTextFile("research/orthogonal_small_inputs.json",false);;
SetPrintFormattingStatus(f,false);PrintTo(f,AGR.JsonText(out,"ASCII"));CloseStream(f);
Print("ORTHOGONAL EXPORT COMPLETE\n");
QUIT;

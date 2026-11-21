# Complete ordinary tables for the three unconditional finite endpoints.
# All higher-rank estimates in the proof are symbolic and retain the source gate.
if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
if LoadPackage("atlasrep")<>true then Error("AtlasRep JSON helper missing");fi;
SetAssertionLevel(1);;
dir:=Directory("HODGE_DIVISION_work/agents/imprimitive/lie_small_fields");;
EncodeCyc:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));
 return [n,c];
end;
tabs:=[];;
for name in ["S8(2)","S10(2)","S12(2)"] do
 t:=CharacterTable(name);irr:=Irr(t);n:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(n));
 Assert(1,ForAll(irr,c->c=ComplexConjugate(c)));
 recd:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,c->List(c,EncodeCyc)),information:=InfoText(t),
  extension_info:=ExtensionInfoCharacterTable(t),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))),
  frobenius_schur:=Indicator(t,irr,2));
 Add(tabs,recd);Print(name,": ",n," complete rows; orthogonality and reality PASS\n");
od;
obj:=rec(tables:=tabs,gap_version:=GAPInfo.Version,
 ctbllib_version:=PackageInfo("ctbllib")[1].Version,
 encoding:="integer or [conductor, coefficients of powers of a primitive root]");;
out:=OutputTextFile(Filename(dir,"sp2n2_character_inputs.json"),false);;
SetPrintFormattingStatus(out,false);PrintTo(out,AGR.JsonText(obj,"ASCII"));CloseStream(out);
QUIT;

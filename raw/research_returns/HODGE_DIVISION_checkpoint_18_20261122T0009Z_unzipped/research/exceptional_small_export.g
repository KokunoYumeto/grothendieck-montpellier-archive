LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
SetInfoLevel(InfoPackageLoading,0);;
EncodeExceptional:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
out:=rec(tables:=[],metadata:=[]);;
for name in ["F4(2)","F4(3)","E6(2)","2E6(2)"] do
 t:=CharacterTable(name);Add(out.metadata,rec(name:=name,extension_information:=ExtensionInfoCharacterTable(t)));
od;
for name in ["2.F4(2)","2.F4(2).2","F4(3)","E6(2)","(2^2x3).2E6(2)"] do
 t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);;
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,c->List(c,EncodeExceptional)),information:=InfoText(t),
  indicators:=Indicator(t,irr,2),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
 if name="2.F4(2).2" then
  core:=CharacterTable("2.F4(2)");ci:=Irr(core);fus:=GetFusionMap(core,t);Assert(1,fus<>fail);
  r.core:="2.F4(2)";r.fusion:=fus;
  Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(Length(irr)));
  rows:=Filtered([1..Length(irr)],i->irr[i][1]>1 and ForAny(ci,c->irr[i]{fus}=c));
  spectra:=0;minratio:=1;
  for i in rows do
   chi:=irr[i];a:=chi[1];nu:=a;
   for j in [1..Length(irr)] do
    if chi[j]*GaloisCyc(chi[j],-1)=a^2 then continue;fi;
    ev:=EigenvaluesChar(t,chi,j);Assert(1,ForAll(ev,x->IsInt(x) and x>=0) and Sum(ev)=a);
    nu:=Minimum(nu,a-Maximum(ev));spectra:=spectra+1;
   od;
   minratio:=Minimum(minratio,nu/a);
  od;
  out.outer_scan:=rec(rows:=Length(rows),spectra:=spectra,min_ratio:=String(minratio));
  Print("OUTER rows=",Length(rows)," spectra=",spectra," min_ratio=",minratio,"\n");
 fi;
 Add(out.tables,r);Print("EXPORTED ",name," classes=",Length(irr),"\n");
od;
f:=OutputTextFile("research/exceptional_small_inputs.json",false);;
SetPrintFormattingStatus(f,false);;PrintTo(f,AGR.JsonText(out,"ASCII"));;CloseStream(f);;
Print("COMPLETE EXCEPTIONAL EXPORT\n");
QUIT;

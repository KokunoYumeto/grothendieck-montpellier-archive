# Complete endpoint inputs. Coverage of exceptional outers is proved separately.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
dest:=Directory("research/a2_cores");;
EncodeA2:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
specs:=[["L3(3)",["L3(3)","L3(3).2"]],
        ["U3(3)",["U3(3)","U3(3).2"]],
        ["U3(4)",["U3(4)","U3(4).2","U3(4).4"]],
        ["3.U3(5)",["3.U3(5)","3.U3(5).2","3.U3(5).3"]],
        ["(4^2x3).L3(4)",["(4^2x3).L3(4)"]]];;
for nm in ["L3(4)","2.L3(4)","3.L3(4)","4_1.L3(4)","4_2.L3(4)","6.L3(4)","12_1.L3(4)","12_2.L3(4)"] do
 names:=[nm];;
 for suffix in [".2_1",".2_2",".2_3"] do Add(names,Concatenation(nm,suffix));od;
 if nm in ["L3(4)","3.L3(4)"] then
  Add(names,Concatenation(nm,".3"));Add(names,Concatenation(nm,".6"));
 fi;
 Add(specs,[nm,names]);
od;
input:=rec(source:="CTblLib1.3.11 complete mathematical endpoint tables, with individual provenance retained",tables:=[],simple_metadata:=[]);;
out:=rec(status:="PASS",tables:=[],rows:=0,spectra:=0);;
for nm in ["L3(3)","L3(4)","U3(3)","U3(4)","U3(5)"] do
 t:=CharacterTable(nm);;
 Add(input.simple_metadata,rec(name:=Identifier(t),information:=InfoText(t),extension_info:=ExtensionInfoCharacterTable(t)));
od;
u:=fail;;c:=[];;a:=0;;fus:=[];;cs:=[];;
for spec in specs do
 core:=CharacterTable(spec[1]);;u:=Irr(core);;
 for nm in spec[2] do
  t:=CharacterTable(nm);;Assert(1,t<>fail);;cs:=Irr(t);;nr:=Length(cs);;
  Assert(1,MatScalarProducts(t,cs,cs)=IdentityMat(nr));;
  item:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),sizes:=SizesConjugacyClasses(t),
   class_names:=ClassNames(t),characters:=List(cs,x->List(x,EncodeA2)),information:=InfoText(t),
   indicators:=Indicator(t,cs,2),power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));;
  if nm=spec[1] then
   fus:=[1..Length(u)];;
  else
   fus:=GetFusionMap(core,t);;Assert(1,fus<>fail);;item.core:=spec[1];;item.fusion:=fus;;
  fi;
  rows:=Filtered([1..nr],i->cs[i][1]>1 and cs[i]{fus} in u);;
  Add(input.tables,item);;
  result:=rec(name:=Identifier(t),rows:=rows,row_bounds:=[],spectra:=0);;
  for i in rows do
   c:=cs[i];;a:=c[1];;ratio:=1;;minnu:=a;;count:=0;;
   for j in [1..Length(c)] do
    if c[j]*GaloisCyc(c[j],-1)=a*a then continue;fi;
    ms:=EigenvaluesChar(t,c,j);;Assert(1,ForAll(ms,x->IsInt(x) and x>=0) and Sum(ms)=a);;
    nu:=a-Maximum(ms);;ratio:=Minimum(ratio,nu/a);;minnu:=Minimum(minnu,nu);;count:=count+1;;
   od;
   Add(result.row_bounds,rec(row:=i,degree:=a,min_nu:=minnu,min_ratio:=String(ratio),spectra:=count));;
   result.spectra:=result.spectra+count;;
  od;
  Add(out.tables,result);;out.rows:=out.rows+Length(rows);;out.spectra:=out.spectra+result.spectra;;
  Print(nm," rows=",Length(rows)," spectra=",result.spectra," minRatio=",Minimum(List(result.row_bounds,x->Rat(x.min_ratio))),"\n");
 od;
od;
for pair in [["small_inputs.json",input],["small_scan.json",out]] do
 stream:=OutputTextFile(Filename(dest,pair[1]),false);;SetPrintFormattingStatus(stream,false);;
 PrintTo(stream,AGR.JsonText(pair[2],"ASCII"));;CloseStream(stream);;
od;
Print("PASS ",out.rows," rows ",out.spectra," spectra\n");
QUIT;

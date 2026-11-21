# Complete published small-field input; no reflection or Weil-row assumption.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
dest:=Directory("HODGE_DIVISION_work/agents/imprimitive/lie_small_fields");;
EncEven:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
names:=["S4(4)","S4(4).2","S4(4).4","2.S6(2)"];;
input:=rec(tables:=[],metadata:=[]);;
for nm in ["S4(4)","S6(2)"] do
 t:=CharacterTable(nm);
 Add(input.metadata,rec(name:=nm,extension_info:=ExtensionInfoCharacterTable(t),information:=InfoText(t)));
od;
out:=rec(status:="PASS",tables:=[],rows:=0,entries:=0);;
cs:=[];;fus:=[];;u:=fail;;
for nm in names do
 t:=CharacterTable(nm);cs:=Irr(t);nr:=Length(cs);
 Assert(1,MatScalarProducts(t,cs,cs)=IdentityMat(nr));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),sizes:=SizesConjugacyClasses(t),
  class_names:=ClassNames(t),information:=InfoText(t),characters:=List(cs,c->List(c,EncEven)),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))),indicators:=Indicator(t,2));
 if PositionSublist(nm,"S4(4).")<>fail then
  u:=CharacterTable("S4(4)");fus:=GetFusionMap(u,t);Assert(1,fus<>fail);
  r.core:="S4(4)";r.fusion:=fus;
  rows:=Filtered([1..nr],i->cs[i][1]>1 and cs[i]{fus} in Irr(u));
 else rows:=Filtered([1..nr],i->cs[i][1]>1);fi;
 Add(input.tables,r);
 rr:=rec(name:=nm,selected_rows:=rows,row_bounds:=[],entries:=0);
 for i in rows do
  c:=cs[i];a:=c[1];ratio:=1;
  for j in [1..nr] do
   if c[j]*GaloisCyc(c[j],-1)=a*a then continue;fi;
   ms:=EigenvaluesChar(t,c,j);Assert(1,ForAll(ms,x->IsInt(x) and x>=0));Assert(1,Sum(ms)=a);
   ratio:=Minimum(ratio,(a-Maximum(ms))/a);rr.entries:=rr.entries+1;
  od;
  if nm="2.S6(2)" then
   if a=7 then Assert(1,ratio=1/7 and r.indicators[i]=1);
   else Assert(1,ratio>=2/9);if a=8 then Assert(1,ratio>=1/4);fi;fi;
  else Assert(1,ratio>=1/3);fi;
  Add(rr.row_bounds,rec(row:=i,degree:=a,ratio:=String(ratio)));
 od;
 Add(out.tables,rr);out.rows:=out.rows+Length(rows);out.entries:=out.entries+rr.entries;
 Print(nm," rows=",Length(rows)," entries=",rr.entries," PASS\n");
od;
Assert(1,out.rows=104 and out.entries=3442);;
for item in [["even_symplectic_small_inputs.json",input],["even_symplectic_small_scan.json",out]] do
 f:=OutputTextFile(Filename(dest,item[1]),false);SetPrintFormattingStatus(f,false);
 PrintTo(f,AGR.JsonText(item[2],"ASCII"));CloseStream(f);
od;
QUIT;

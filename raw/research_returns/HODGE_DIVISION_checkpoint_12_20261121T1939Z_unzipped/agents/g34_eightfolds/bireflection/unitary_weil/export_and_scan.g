# Complete published tables for the two new small unitary-Weil endpoints.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
dest:=Directory("HODGE_DIVISION_work/agents/g34_eightfolds/bireflection/unitary_weil");;
specs:=[["U3(3)",[6,7],["U3(3)","U3(3).2"]],
        ["U5(2)",[10],["U5(2)","U5(2).2"]],
        ["U6(2)",[22],["U6(2)","U6(2).2","U6(2).3"]]];;
EncodeU:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
WriteU:=function(name,obj)
 local f;
 f:=OutputTextFile(Filename(dest,name),false);SetPrintFormattingStatus(f,false);
 PrintTo(f,AGR.JsonText(obj,"ASCII"));CloseStream(f);
end;
input:=rec(source:="Published ATLAS tables via CTblLib1.3.11",tables:=[]);;
output:=rec(status:="PASS",tables:=[],rows:=0,entries:=0);;
ci:=[];;spec:=[];;t:=fail;;irr:=[];;cores:=[];;fus:=[];;
for spec in specs do
 core:=CharacterTable(spec[1]);ci:=Irr(core);
 cores:=Filtered([1..Length(ci)],i->ci[i][1] in spec[2]);
 for name in spec[3] do
  t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);nr:=Length(irr);
  Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
  r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
   sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
   characters:=List(irr,ch->List(ch,EncodeU)),information:=InfoText(t),
   indicators:=Indicator(t,irr,2),
   power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
  if name=spec[1] then fus:=[1..Length(ci)];r.extension_information:=ExtensionInfoCharacterTable(t);
  else fus:=GetFusionMap(core,t);Assert(1,fus<>fail);r.core:=spec[1];r.fusion:=fus;fi;
  rows:=Filtered([1..nr],i->irr[i][1] in spec[2] and ForAny(cores,j->irr[i]{fus}=ci[j]));
  r.requested_degrees:=spec[2];Add(input.tables,r);
  result:=rec(table:=Identifier(t),selected_rows:=rows,row_data:=[],entries:=0);
  for i in rows do
   c:=irr[i];a:=c[1];rr:=rec(row:=i,degree:=a,min_nu:=a,minimizers:=[]);
   for j in [1..nr] do
    if c[j]*GaloisCyc(c[j],-1)=a^2 then continue;fi;
    ev:=EigenvaluesChar(t,c,j);Assert(1,ForAll(ev,x->IsInt(x) and x>=0));Assert(1,Sum(ev)=a);
    nu:=a-Maximum(ev);
    if nu<rr.min_nu then rr.min_nu:=nu;rr.minimizers:=[];fi;
    if nu=rr.min_nu then Add(rr.minimizers,rec(class:=j,order:=OrdersClassRepresentatives(t)[j],multiplicities:=ev));fi;
    result.entries:=result.entries+1;output.entries:=output.entries+1;
   od;
   if spec[1]="U3(3)" then Assert(1,4*rr.min_nu>=a);
   else Assert(1,5*rr.min_nu>=a);fi;
   Add(result.row_data,rr);output.rows:=output.rows+1;
  od;
  Add(output.tables,result);Print(name," ",result,"\n");
 od;
od;
WriteU("unitary_weil_inputs.json",input);WriteU("unitary_weil_scan.json",output);
Print("PASS rows=",output.rows," entries=",output.entries,"\n");
QUIT;

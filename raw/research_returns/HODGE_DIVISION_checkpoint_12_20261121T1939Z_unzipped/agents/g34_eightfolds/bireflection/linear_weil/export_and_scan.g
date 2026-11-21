# Complete published character input for the SL_3(4) linear-Weil endpoint.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
dest:=Directory("HODGE_DIVISION_work/agents/g34_eightfolds/bireflection/linear_weil");;
names:=["3.L3(4)","3.L3(4).2_1","3.L3(4).2_2","3.L3(4).2_3","3.L3(4).3","3.L3(4).6"];;
LinEncode:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
WriteJSON:=function(name,obj)
 local f;
 f:=OutputTextFile(Filename(dest,name),false);SetPrintFormattingStatus(f,false);
 PrintTo(f,AGR.JsonText(obj,"ASCII"));CloseStream(f);
end;
core:=CharacterTable(names[1]);;ci:=Irr(core);;
core_rows:=Filtered([1..Length(ci)],i->ci[i][1]=21);;
Assert(1,core_rows=[17,18]);;
input:=rec(source:="Published ATLAS tables via CTblLib1.3.11",tables:=[],
 simple_information:=InfoText(CharacterTable("L3(4)")),
 simple_extension_info:=ExtensionInfoCharacterTable(CharacterTable("L3(4)")),
 automorphism_information:=InfoText(CharacterTable("L3(4).D12")));;
output:=rec(status:="PASS",tables:=[],rows:=0,entries:=0,failures:=[]);;
t:=fail;;irr:=[];;fus:=[];;c:=[];;
for name in names do
 t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);nr:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,ch->List(ch,LinEncode)),information:=InfoText(t),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
 if name=names[1] then fus:=[1..Length(ci)];
 else
  fus:=GetFusionMap(core,t);Assert(1,fus<>fail);r.core:=names[1];r.fusion:=fus;
 fi;
 rows:=Filtered([1..nr],i->irr[i][1]=21 and ForAny(core_rows,j->irr[i]{fus}=ci[j]));
 Add(input.tables,r);
 result:=rec(table:=Identifier(t),selected_rows:=rows,row_data:=[],entries:=0);
 for i in rows do
  c:=irr[i];rr:=rec(row:=i,degree:=21,min_nu:=21,minimizers:=[]);
  for j in [1..nr] do
   if c[j]*GaloisCyc(c[j],-1)=21^2 then continue;fi;
   ev:=EigenvaluesChar(t,c,j);Assert(1,ForAll(ev,x->IsInt(x) and x>=0));Assert(1,Sum(ev)=21);
   nu:=21-Maximum(ev);
   if nu<rr.min_nu then rr.min_nu:=nu;rr.minimizers:=[];fi;
   if nu=rr.min_nu then Add(rr.minimizers,rec(class:=j,order:=OrdersClassRepresentatives(t)[j],multiplicities:=ev));fi;
   if nu<8 then Add(output.failures,rec(table:=Identifier(t),row:=i,class:=j,nu:=nu));fi;
   result.entries:=result.entries+1;output.entries:=output.entries+1;
  od;
  Assert(1,rr.min_nu=8);Add(result.row_data,rr);output.rows:=output.rows+1;
 od;
 Add(output.tables,result);
 Print(name," rows=",Length(rows)," entries=",result.entries,"\n");
od;
Assert(1,output.rows=24 and output.entries=1288 and IsEmpty(output.failures));
WriteJSON("linear_weil_inputs.json",input);WriteJSON("linear_weil_scan.json",output);
Print("PASS rows=",output.rows," entries=",output.entries,"\n");
QUIT;

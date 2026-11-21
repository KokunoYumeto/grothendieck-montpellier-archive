# Complete small universal-cover and cyclic-normalizer input for odd C3.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
dest:=Directory("HODGE_DIVISION_work/agents/g34_eightfolds/bireflection/csp6_odd");;
EncodeC3:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
WriteC3:=function(name,obj)
 local f;
 f:=OutputTextFile(Filename(dest,name),false);SetPrintFormattingStatus(f,false);
 PrintTo(f,AGR.JsonText(obj,"ASCII"));CloseStream(f);
end;
input:=rec(source:="Complete official CTblLib1.3.11 tables; exact per-table provenance retained",tables:=[]);;
output:=rec(status:="exploratory complete spectrum scan",tables:=[],rows:=0,entries:=0);;
core:=CharacterTable("2.S6(3)");;ci:=Irr(core);;irr:=[];;fus:=[];;t:=fail;;
for name in ["2.S6(3)","2.S6(3).2"] do
 t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);nr:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,ch->List(ch,EncodeC3)),information:=InfoText(t),
  indicators:=Indicator(t,irr,2),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
 if name="2.S6(3)" then fus:=[1..Length(ci)];r.extension_information:=ExtensionInfoCharacterTable(CharacterTable("S6(3)"));
 else fus:=GetFusionMap(core,t);Assert(1,fus<>fail);r.core:="2.S6(3)";r.fusion:=fus;fi;
 rows:=Filtered([1..nr],i->irr[i][1]>1 and ForAny(ci,c->irr[i]{fus}=c));
 Add(input.tables,r);
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
  Add(result.row_data,rr);output.rows:=output.rows+1;
 od;
 Add(output.tables,result);
 Print(name," selected=",Length(rows)," entries=",result.entries," min ratio=",Minimum(List(result.row_data,x->x.min_nu/x.degree))," min degree=",Minimum(List(result.row_data,x->x.degree)),"\n");
od;
WriteC3("small_inputs.json",input);WriteC3("small_scan.json",output);
Print("PASS spectrum rows=",output.rows," entries=",output.entries,"\n");
QUIT;

# Complete character input for the small Suzuki and Ree residual cores.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
dest:=Directory("HODGE_DIVISION_work/agents/g34_eightfolds/bireflection/twisted_lie");;
pairs:=[["2^2.Sz(8)",fail],["2^2.Sz(8).3","2^2.Sz(8)"],
        ["R(27)",fail],["2F4(2)'",fail],["2F4(8)",fail]];;
TwEncode:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
TwL1:=function(z)
 if IsInt(z) then return AbsInt(z);fi;
 return Sum(CoeffsCyc(z,Conductor(z)),AbsInt);
end;
WriteJSON:=function(name,obj)
 local f;
 f:=OutputTextFile(Filename(dest,name),false);SetPrintFormattingStatus(f,false);
 PrintTo(f,AGR.JsonText(obj,"ASCII"));CloseStream(f);
end;
input:=rec(source:="Published ATLAS and Gunter Malle character data through CTblLib 1.3.11",tables:=[],core_metadata:=[]);;
for name in ["Sz(8)","R(27)","2F4(2)'","2F4(8)"] do
 t:=CharacterTable(name);
 Add(input.core_metadata,rec(name:=name,extension_info:=ExtensionInfoCharacterTable(t),information:=InfoText(t)));
od;
output:=rec(tables:=[],spectral_failures:=[],trace_failures:=[],rows:=0,entries:=0);;
t:=fail;;irr:=[];;core:=fail;;fus:=[];;
for pair in pairs do
 t:=CharacterTable(pair[1]);Assert(1,t<>fail);irr:=Irr(t);nr:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
       sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
       characters:=List(irr,c->List(c,TwEncode)),information:=InfoText(t),
       power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
 rows:=Filtered([1..nr],i->irr[i][1]>1);
 if pair[2]<>fail then
  core:=CharacterTable(pair[2]);fus:=GetFusionMap(core,t);Assert(1,fus<>fail);
  r.core:=Identifier(core);r.fusion:=fus;
  rows:=Filtered(rows,i->ScalarProduct(core,irr[i]{fus},irr[i]{fus})=1);
 fi;
 Add(input.tables,r);
 result:=rec(table:=Identifier(t),selected_rows:=rows,row_data:=[],minimum_degree:=Minimum(List(rows,i->irr[i][1])));
 for i in rows do
  c:=irr[i];e:=c[1];recrow:=rec(row:=i,degree:=e,min_ratio:=1,max_trace_l1_ratio:=0);
  for j in [1..nr] do
   if c[j]*GaloisCyc(c[j],-1)=e^2 then continue;fi;
   if PositionSublist(Identifier(t),"Sz(8)")<>fail then
    ev:=EigenvaluesChar(t,c,j);Assert(1,ForAll(ev,x->IsInt(x) and x>=0));Assert(1,Sum(ev)=e);
    nu:=e-Maximum(ev);recrow.min_ratio:=Minimum(recrow.min_ratio,nu/e);
    if 4*nu<e then Add(output.spectral_failures,rec(table:=Identifier(t),row:=i,class:=j,degree:=e,nu:=nu));fi;
   else
    ratio:=TwL1(c[j])/e;
    if ratio>recrow.max_trace_l1_ratio then recrow.max_trace_l1_ratio:=ratio;recrow.witness_class:=j;fi;
    if 4*TwL1(c[j])>e then Add(output.trace_failures,rec(table:=Identifier(t),row:=i,class:=j,degree:=e,l1:=TwL1(c[j])));fi;
   fi;
   output.entries:=output.entries+1;
  od;
  recrow.min_ratio:=String(recrow.min_ratio);recrow.max_trace_l1_ratio:=String(recrow.max_trace_l1_ratio);
  Add(result.row_data,recrow);output.rows:=output.rows+1;
 od;
 Add(output.tables,result);
 Print(Identifier(t)," selected=",Length(rows)," minimum_degree=",result.minimum_degree,
       " spectral_failures=",Length(output.spectral_failures)," trace_failures=",Length(output.trace_failures),"\n");
od;
Assert(1,Length(input.tables)=5 and output.rows=213 and output.entries=15471);
Assert(1,IsEmpty(output.spectral_failures) and IsEmpty(output.trace_failures));
WriteJSON("twisted_character_inputs.json",input);WriteJSON("twisted_scan.json",output);
Print("TOTAL tables=",Length(input.tables)," rows=",output.rows," entries=",output.entries,
      " spectral_failures=",Length(output.spectral_failures)," trace_failures=",Length(output.trace_failures),"\n");
QUIT;

# Complete small-A1 cyclic-outer character input and spectral scan.
# Table data are published ATLAS inputs accessed in CTblLib 1.3.11.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
dest:=Directory("HODGE_DIVISION_work/agents/g34_eightfolds/bireflection/a1");;
pairs:=[
 ["2.A5",fail],["2.A5.2","2.A5"],
 ["2.L3(2)",fail],["2.L3(2).2","2.L3(2)"],
 ["L2(8)",fail],["L2(8).3","L2(8)"],
 ["6.A6",fail],["6.A6.2_1","6.A6"],["6.A6.2_2","6.A6"],
 ["3.A6",fail],["3.A6.2_3","3.A6"],
 ["2.L2(11)",fail],["2.L2(11).2","2.L2(11)"],
 ["2.L2(13)",fail],["2.L2(13).2","2.L2(13)"],
 ["L2(16)",fail],["L2(16).2","L2(16)"],["L2(16).4","L2(16)"],
 ["2.L2(17)",fail],["2.L2(17).2","2.L2(17)"],
 ["2.L2(19)",fail],["2.L2(19).2","2.L2(19)"],
 ["2.L2(23)",fail],["2.L2(23).2","2.L2(23)"],
 ["2.L2(25)",fail],["2.L2(25).2_1","2.L2(25)"],["2.L2(25).2_2","2.L2(25)"],
 ["L2(25)",fail],["L2(25).2_3","L2(25)"],
 ["2.L2(27)",fail],["2.L2(27).2","2.L2(27)"],
 ["2.L2(27).3","2.L2(27)"],["2.L2(27).6","2.L2(27)"]
];;
A1Encode:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
WriteJSON:=function(name,obj)
 local f;
 f:=OutputTextFile(Filename(dest,name),false);SetPrintFormattingStatus(f,false);
 PrintTo(f,AGR.JsonText(obj,"ASCII"));CloseStream(f);
end;
input:=rec(source:="Published ATLAS data through CTblLib 1.3.11",tables:=[]);;
output:=rec(tables:=[],quarter_failures:=[],fifth_failures:=[],rows:=0,entries:=0);;
t:=fail;;irr:=[];;core:=fail;;fus:=[];;
for pair in pairs do
 t:=CharacterTable(pair[1]);Assert(1,t<>fail);irr:=Irr(t);nr:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
       sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
       characters:=List(irr,c->List(c,A1Encode)),information:=InfoText(t),
       power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
 rows:=Filtered([1..nr],i->irr[i][1]>1);
 if pair[2]<>fail then
  core:=CharacterTable(pair[2]);fus:=GetFusionMap(core,t);Assert(1,fus<>fail);
  r.core:=Identifier(core);r.fusion:=fus;
  rows:=Filtered(rows,i->ScalarProduct(core,irr[i]{fus},irr[i]{fus})=1);
 fi;
 Add(input.tables,r);
 result:=rec(table:=Identifier(t),selected_rows:=rows,row_data:=[]);
 for i in rows do
  c:=irr[i];e:=c[1];recrow:=rec(row:=i,degree:=e,min_ratio:=1,exceptions:=[]);
  for j in [1..nr] do
   if c[j]*GaloisCyc(c[j],-1)=e^2 then continue;fi;
   ev:=EigenvaluesChar(t,c,j);Assert(1,ForAll(ev,x->IsInt(x) and x>=0));Assert(1,Sum(ev)=e);
   nu:=e-Maximum(ev);recrow.min_ratio:=Minimum(recrow.min_ratio,nu/e);
   if 4*nu<e then
    witness:=rec(table:=Identifier(t),row:=i,degree:=e,class:=j,order:=Length(ev),nu:=nu,multiplicities:=ev);
    Add(output.quarter_failures,witness);Add(recrow.exceptions,witness);
   fi;
   if 5*nu<e then Add(output.fifth_failures,witness);fi;
   output.entries:=output.entries+1;
  od;
  recrow.min_ratio:=String(recrow.min_ratio);Add(result.row_data,recrow);
  output.rows:=output.rows+1;
 od;
 Add(output.tables,result);
 Print(Identifier(t)," selected=",Length(rows)," quarter failures=",Length(output.quarter_failures),"\n");
od;
Assert(1,Length(input.tables)=33 and output.rows=654 and output.entries=18922);
Assert(1,Length(output.quarter_failures)=4 and IsEmpty(output.fifth_failures));
WriteJSON("a1_character_inputs.json",input);WriteJSON("a1_spectral_scan.json",output);
Print("TOTAL tables=",Length(input.tables)," rows=",output.rows," entries=",output.entries,
      " quarterfail=",Length(output.quarter_failures)," fifthfail=",Length(output.fifth_failures),"\n");
QUIT;

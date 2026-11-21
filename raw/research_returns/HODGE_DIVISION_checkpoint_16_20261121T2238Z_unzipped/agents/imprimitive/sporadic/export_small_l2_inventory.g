if LoadPackage("ctbllib")<>true then Error("CTblLib unavailable");fi;
SetAssertionLevel(1);;
L2Inventory:=function()
 local result, specs, spec, simple, cover, row, pair, u, t, f, sizesu, sizest, j, r;
 specs:=[
 [ [4,5],"A5","2.A5",[["2.A5","2.A5.2","diagonal/field under the two A1 descriptions"]] ],
 [ [7],"L3(2)","2.L3(2)",[["2.L3(2)","2.L3(2).2","diagonal"]] ],
 [ [8],"L2(8)","L2(8)",[["L2(8)","L2(8).3","field order3"]] ],
 [ [9],"A6","6.A6",[["6.A6","6.A6.2_1","field"],["6.A6","6.A6.2_2","diagonal"],["3.A6","3.A6.2_3","diagonal-field; center-negative obstruction required"]] ],
 [ [11],"L2(11)","2.L2(11)",[["2.L2(11)","2.L2(11).2","diagonal"]] ],
 [ [13],"L2(13)","2.L2(13)",[["2.L2(13)","2.L2(13).2","diagonal"]] ],
 [ [16],"L2(16)","L2(16)",[["L2(16)","L2(16).2","field order2"],["L2(16)","L2(16).4","field order4"]] ],
 [ [17],"L2(17)","2.L2(17)",[["2.L2(17)","2.L2(17).2","diagonal"]] ],
 [ [19],"L2(19)","2.L2(19)",[["2.L2(19)","2.L2(19).2","diagonal"]] ],
 [ [23],"L2(23)","2.L2(23)",[["2.L2(23)","2.L2(23).2","diagonal"]] ],
 [ [25],"L2(25)","2.L2(25)",[["2.L2(25)","2.L2(25).2_1","diagonal"],["2.L2(25)","2.L2(25).2_2","field"],["L2(25)","L2(25).2_3","diagonal-field; center-negative obstruction required"]] ],
 [ [27],"L2(27)","2.L2(27)",[["2.L2(27)","2.L2(27).2","diagonal order2"],["2.L2(27)","2.L2(27).3","field order3"],["2.L2(27)","2.L2(27).6","mixed order6"]] ]
 ];
 result:=rec(source:="CTblLib1.3.11 ATLAS tables; inventory only, not a spectral-bound certificate",groups:=[]);
 for spec in specs do
  simple:=CharacterTable(spec[2]);cover:=CharacterTable(spec[3]);
  row:=rec(field_sizes:=spec[1],simple:=Identifier(simple),cover:=Identifier(cover),
     simple_order:=Size(simple),cover_order:=Size(cover),
     extension_info:=ExtensionInfoCharacterTable(simple),
     cover_information:=InfoText(cover),cyclic_extensions:=[]);
  for pair in spec[4] do
   u:=CharacterTable(pair[1]);t:=CharacterTable(pair[2]);f:=GetFusionMap(u,t);
   Assert(1,f<>fail);Assert(1,Size(t) mod Size(u)=0);
   sizesu:=SizesConjugacyClasses(u);sizest:=SizesConjugacyClasses(t);
   Assert(1,Length(f)=NrConjugacyClasses(u));
   Assert(1,OrdersClassRepresentatives(t){f}=OrdersClassRepresentatives(u));
   Assert(1,Filtered([1..Length(f)],j->f[j]=1)=[1]);
   for j in Set(f) do
    Assert(1,Sum(Filtered([1..Length(f)],r->f[r]=j),r->sizesu[r])=sizest[j]);
   od;
   r:=rec(core:=Identifier(u),extension:=Identifier(t),core_order:=Size(u),
      extension_order:=Size(t),cyclic_index:=Size(t)/Size(u),outer_description:=pair[3],
      fusion:=f,core_information:=InfoText(u),extension_information:=InfoText(t));
   Add(row.cyclic_extensions,r);
  od;
  Add(result.groups,row);
 od;
 return result;
end;;
data:=L2Inventory();;
stream:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/sporadic/small_l2_table_inventory.json",false);;
SetPrintFormattingStatus(stream,false);PrintTo(stream,AGR.JsonText(data,"ASCII"));CloseStream(stream);
Print("PASS complete requested A1 cover/outer inventory and every stored normal-subgroup fusion\n");
QUIT;

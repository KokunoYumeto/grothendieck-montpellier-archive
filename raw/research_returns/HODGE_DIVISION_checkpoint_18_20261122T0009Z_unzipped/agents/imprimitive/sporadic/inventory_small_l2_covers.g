LoadPackage("ctbllib");;
DoInventory := function()
 local out, allnames, prefixes, prefix, names, n, t, covers, u, f;
 out:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/sporadic/small_l2_cover_inventory.txt",false);
 SetPrintFormattingStatus(out,false);
 allnames:=AllCharacterTableNames();
 prefixes:=["A5","2.A5","A6","2.A6","3.A6","6.A6","12.A6","L3(2)","2.L3(2)"];
 for prefix in prefixes do
  names:=Filtered(allnames,n->PositionSublist(n,prefix)=1);
  Sort(names);
  AppendTo(out,"prefix=",prefix," candidates=",names,"\n");
  for n in names do
   t:=CharacterTable(n);
   if t<>fail then
    AppendTo(out,n," order=",Size(t)," classes=",NrConjugacyClasses(t)," origin=",InfoText(t),"\n");
   fi;
  od;
 od;
 covers:=["2.A5","6.A6","2.L3(2)","2.L2(25)"];
 for n in covers do
  u:=CharacterTable(n);
  AppendTo(out,"\nFUSIONS from ",n,"\n");
  for f in ComputedClassFusions(u) do
   AppendTo(out,f.name," map=",f.map,"\n");
  od;
 od;
 for n in ["6.A6.2_1","6.A6.2_2","6.A6.2_3","2.L2(25).2_3","4.L2(25).2_3"] do
  t:=CharacterTable(n);
  if t=fail then AppendTo(out,n," MISSING\n");
  else AppendTo(out,n," FOUND canonical=",Identifier(t)," order=",Size(t),"\n"); fi;
 od;
 CloseStream(out);
end;;
DoInventory();;
QUIT;

LoadPackage("ctbllib");;
out := OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/sporadic/small_l2_inventory.txt",false);;
SetPrintFormattingStatus(out,false);;
allnames := AllCharacterTableNames();;
for q in [4,5,7,8,9,11,13,16,17,19,23,25,27] do
  token := Concatenation("l2(",String(q),")");;
  names := Filtered(allnames,n->PositionSublist(LowercaseString(n),token)<>fail);;
  Sort(names);;
  AppendTo(out,"q=",q," candidates=",names,"\n");
  t := CharacterTable(Concatenation("L2(",String(q),")"));;
  if t<>fail then
    AppendTo(out,"simple=",Identifier(t)," order=",Size(t)," extension_info=",ExtensionInfoCharacterTable(t),"\n");
  fi;
  for n in names do
    t:=CharacterTable(n);;
    if t<>fail then
      AppendTo(out,n," -> ",Identifier(t)," order=",Size(t)," classes=",NrConjugacyClasses(t)," origin=",InfoText(t),"\n");
    fi;
  od;
od;
CloseStream(out);;
QUIT;

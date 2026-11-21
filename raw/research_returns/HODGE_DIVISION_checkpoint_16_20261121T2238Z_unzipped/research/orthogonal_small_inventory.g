LoadPackage("ctbllib");;
SetInfoLevel(InfoPackageLoading,0);;
SetAssertionLevel(1);;
names:=AllCharacterTableNames();;
for term in ["O7(3)","O7(5)","O8+(2)","O8-(2)","O8+(3)","O8-(3)","O9(3)","O10+(2)","O10-(2)","O12+(2)","O12-(2)"] do
 Print(term,": ",Filtered(names,n->PositionSublist(n,term)<>fail),"\n");
 if term in names then
  t:=CharacterTable(term);;
  Print("META ",term," ",ExtensionInfoCharacterTable(t)," classes=",Length(Irr(t))," min=",Minimum(Filtered(List(Irr(t),c->c[1]),x->x>1)),"\n");
 fi;
od;
Print("ORTHOGONAL INVENTORY COMPLETE\n");
QUIT;

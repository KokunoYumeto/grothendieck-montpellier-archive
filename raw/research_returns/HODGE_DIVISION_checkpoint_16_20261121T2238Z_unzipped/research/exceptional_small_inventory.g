LoadPackage("ctbllib");;
SetInfoLevel(InfoPackageLoading,0);;
names:=AllCharacterTableNames();;
for term in ["F4(2)","F4(3)","E6(2)","E6(3)","E7(2)","E8(2)"] do
 Print(term,": ",Filtered(names,n->PositionSublist(n,term)<>fail),"\n");
od;
for name in ["F4(2)","2E6(2)","E6(2)","E7(2)"] do
 if name in names then
  t:=CharacterTable(name);;
  Print("META ",name," ",ExtensionInfoCharacterTable(t)," classes=",Length(Irr(t))," min=",Minimum(Filtered(List(Irr(t),c->c[1]),x->x>1)),"\n");
 fi;
od;
QUIT;

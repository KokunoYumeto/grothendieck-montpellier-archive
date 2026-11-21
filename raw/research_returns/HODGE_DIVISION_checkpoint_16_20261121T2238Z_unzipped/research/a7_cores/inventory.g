LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
names:=Filtered(AllCharacterTableNames(),n->PositionSublist(n,"A7")<>fail);;
Print(names,"\n");
for n in ["A7","A7.2","2.A7","2.A7.2","2.A7.2+","2.A7.2-","3.A7","3.A7.2","6.A7","6.A7.2"] do
 t:=CharacterTable(n);
 if t=fail then Print(n,": missing\n");
 else Print(n,": ",Identifier(t)," classes=",Length(Irr(t))," order=",Size(t)," info=",InfoText(t),"\n");fi;
od;
QUIT;

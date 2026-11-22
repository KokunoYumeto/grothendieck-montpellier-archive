LoadPackage("ctbllib");;
all := AllCharacterTableNames();;
for n in all do
 if PositionSublist(LowercaseString(n),"g2(")<>fail or PositionSublist(LowercaseString(n),"3d4(")<>fail then
  Print(n,"\n");
 fi;
od;
QUIT;

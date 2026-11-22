if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
if LoadPackage("atlasrep")<>true then Error("AtlasRep missing");fi;
SetAssertionLevel(1);;
names:=Filtered(AllCharacterTableNames(),n->PositionSublist(n,"S4(")<>fail);;
rows:=[];;
for q in [5,7,9,11,13,17,19,23,25,27] do
 stem:=Concatenation("S4(",String(q),")");
 related:=Filtered(names,n->PositionSublist(n,stem)<>fail);
 data:=[];
 for name in related do
  t:=CharacterTable(name);
  Add(data,rec(name:=name,identifier:=Identifier(t),order:=Size(t),
   classes:=Length(Irr(t)),information:=InfoText(t),
   degree_minimum:=Minimum(Filtered(List(Irr(t),c->c[1]),d->d>1)),
   fusions:=List(ComputedClassFusions(t),f->f.name)));
 od;
 Add(rows,rec(q:=q,tables:=data));
 Print("q=",q,": ",related,"\n");
od;
o:=rec(gap:=GAPInfo.Version,ctbllib:=PackageInfo("ctbllib")[1].Version,
 all_related_names:=names,inventory:=rows,
 scope:="Stored complete ordinary tables only; no generic or unipotent-only table treated as complete.");;
out:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/odd_c2/inventory.json",false);;
SetPrintFormattingStatus(out,false);;PrintTo(out,AGR.JsonText(o,"ASCII"));;CloseStream(out);;
QUIT;

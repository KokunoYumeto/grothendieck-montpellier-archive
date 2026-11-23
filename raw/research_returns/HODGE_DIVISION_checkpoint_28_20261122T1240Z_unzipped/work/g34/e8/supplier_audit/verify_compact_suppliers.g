# Replay only the chosen exact generators and cyclic-character values.
# No subgroup enumeration or precomputed character table of H is reused.
Read("common_actual.g");
Read("chosen_ordinary.g");
CheckChosen:=function(r)
  local gens,H,m,c,ex,hom,cc,items,z,new;
  gens:=List(r.gens,PermList); H:=Group(gens); m:=r.m;
  Assert(0,ForAll(gens,g->g in GG) and Size(H)=r.Hord);
  c:=PermList(Concatenation([2..m],[1]));
  ex:=List(r.chigens,z->First([0..m-1],j->E(m)^j=z));
  Assert(0,not fail in ex);
  hom:=GroupHomomorphismByImages(H,Group(c),gens,List(ex,j->c^j));
  Assert(0,hom<>fail and Size(Image(hom))=m);
  cc:=ConjugacyClasses(H);
  items:=List(cc,cl->rec(key:=GKey(Representative(cl)),w:=Size(cl),
    k:=First([0..m-1],j->c^j=Image(hom,Representative(cl)))));
  Assert(0,ForAll(items,it->it.k<>fail));
  new:=EvalGeneral(items,m,Size(H));
  Assert(0,new.vec=r.vec and new.q=r.q and new.s=r.s and new.h=r.h and new.cnt=r.cnt);
  return new;
end;;
passed:=[];;
for r in CHOSEN do
  new:=CheckChosen(r);;
  Assert(0,new.adm);
  Add(passed,r.index1);
  Print("ORDINARY REPLAY PASS ",r.index1,"\n");
od;
Assert(0,Length(passed)=95);
galeslots:=0;;
for wc in [8,33,55] do
  Read(Concatenation("gale",String(wc),"_verified.g"));
  for s in PROFILE.positive_slots do
    new:=CheckChosen(s.character);;
    Assert(0,new.q>=1 and new.s>=2);
    galeslots:=galeslots+1;
  od;
  Print("GALE SLOT REPLAY PASS ",PROFILE.rowindex,"\n");
od;
Assert(0,galeslots=12);
PrintTo("compact_verification_result.g","ORDINARY_PASSED := ",passed,";\n",
  "GALE_DISTINCT_SLOTS_PASSED := ",galeslots,";\n");
Print("COMPACT107 CHARACTER REPLAYS ALL PASS\n");
QUIT;

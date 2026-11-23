Read("common_actual.g");
Assert(0,Length(ROOTS)=240 and Length(VECS)=480);
Assert(0,Size(GG)=GORDER and Size(GW)=WORDER);
Assert(0,ForAll(ACTUAL_TUP,g->g in GG));
Assert(0,ForAll(irr,ch->ForAll(ch,IsInt)));
for j in [1..12] do
  d:=Decomp(ACTUAL_TUP[j]);;
  scalar:=E(4)^d[1];;
  realized:=scalar*TransposedMat(d[2]);;
  given:=E(4)^ACTUAL_PAIRS[j][1]*TransposedMat(ACTUAL_PAIRS[j][2]);;
  Assert(0,realized=given);
od;
# Exact demonstration of the homomorphism law on a generating set.
for g in GeneratorsOfGroup(GG) do
  for h in GeneratorsOfGroup(GG) do
    gd:=Decomp(g); hd:=Decomp(h); kd:=Decomp(g*h);;
    Assert(0,E(4)^kd[1]*TransposedMat(kd[2])=
      (E(4)^gd[1]*TransposedMat(gd[2]))*(E(4)^hd[1]*TransposedMat(hd[2])));
  od;
od;
Print("Literal actual tuple and scalar-preserving representation bridge PASS\n");
QUIT;

Read("common_actual.g");
Read("row_functions.g");
Read("explicit_candidates.g");
PrintTo("explicit_verified.g","VERIFIED := [];\n");
for cand in EXPLICIT_CANDIDATES do
  gens:=List(cand.gens,PermList);;
  H:=Group(gens);;
  Assert(0,ForAll(gens,g->g in GG));
  # This verifies all group relations, hence the candidate values define
  # an actual one-dimensional character, not merely a list of values.
  mm:=Lcm(List(cand.chigens,Order));;
  cycgen:=PermList(Concatenation([2..mm],[1]));;
  imggens:=List(cand.chigens,z->cycgen^First([0..mm-1],j->E(mm)^j=z));;
  chmap:=GroupHomomorphismByImages(H,Group(cycgen),gens,imggens);;
  Assert(0,chmap<>fail);
  rows:=RowsOfGroup(H,false);;
  found:=Filtered(rows,r->r.index1=cand.index1 and r.chigens=cand.chigens);;
  Assert(0,Length(found)=1 and found[1].adm);
  WriteMatches("explicit_verified.g",found,"explicit subgroup relations checked");
od;
Print("All9 explicit subgroup rows PASS\n");
QUIT;

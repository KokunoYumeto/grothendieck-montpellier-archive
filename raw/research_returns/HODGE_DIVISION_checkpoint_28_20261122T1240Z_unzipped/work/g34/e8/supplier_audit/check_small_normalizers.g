Read("common_actual.g");
Read("row_functions.g");
if not IsBound(POWER) then POWER:=1; fi;
path:=Concatenation("small",String(POWER),"_verified.g");;
PrintTo(path,"VERIFIED := [];\n");
N:=Normalizer(GG,Group(ACTUAL_TUP[12]^POWER));;
Print("Actual last-branch cyclic normalizer power ",POWER," order ",Size(N),"\n");
t0:=Runtime();;
subs:=ConjugacyClassesSubgroups(N);;
Print("Subgroup classes ",Length(subs)," computed ms ",Runtime()-t0,"\n");
seen:=[];;
for ii in [1..Length(subs)] do
  H:=Representative(subs[ii]);;
  if Size(H) mod 4<>0 then continue; fi;
  rows:=RowsOfGroup(H,false);;
  rows:=Filtered(rows,r->r.adm and not r.index1 in seen);;
  for r in rows do AddSet(seen,r.index1); od;
  WriteMatches(path,rows,Concatenation("actual branch12 power ",String(POWER),
    " normalizer subgroup class ",String(ii)));
od;
Print("NORMALIZER ",POWER," completed: ",seen," ms ",Runtime()-t0,"\n");
AppendTo(path,"NORMALIZER_ORDER := ",Size(N),";\n",
 "NORMALIZER_GENS := ",List(GeneratorsOfGroup(N),g->ListPerm(g,480)),";\n",
 "NORMALIZER_POWER := ",POWER,";\n",
 "COMPLETE_SUBGROUP_CLASSES := ",Length(subs),";\n");
QUIT;

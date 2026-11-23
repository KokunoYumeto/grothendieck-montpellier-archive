Read("common_actual.g");
Read("actual_setup_data.g");
Read("row_functions.g");
if not IsBound(WCLASS) then WCLASS:=8; ROWINDEX:=3231; fi;
w:=CLASSMAP[WCLASS];;
H0:=Centralizer(GW,w); H:=Group(Concatenation(GeneratorsOfGroup(H0),[iperm]));;
Print("Actual Gale centralizer class ",WCLASS," |H0| ",Size(H0)," |H| ",Size(H),"\n");
R:=RowsOfGroup(H,true);;
Print("Nonzero character vectors ",Length(R)," character orders ",List(R,r->r.m),"\n");
targetrow:=First(SELECTED_ROWS,r->r[1]=ROWINDEX)[2];;
coeffs:=SolutionIntMat(List(R,r->r.vec),targetrow);;
Assert(0,coeffs<>fail and ForAll(coeffs,IsInt));
Assert(0,coeffs*List(R,r->r.vec)=targetrow);
slots:=[];;
for jj in [1..Length(R)] do
  if coeffs[jj]=0 then continue; fi;
  rr:=R[jj]; multslot:=coeffs[jj];;
  # Replace each negative multiplicity by the inverse character.
  if multslot<0 then
    pos:=First([1..Length(R)],j->R[j].chigens=List(rr.chigens,z->GaloisCyc(z,-1)));;
    Assert(0,pos<>fail and R[pos].vec=-rr.vec);
    rr:=R[pos]; multslot:=-multslot;
  fi;
  Add(slots,rec(multiplicity:=multslot, character:=rr));
od;
Assert(0,Sum(slots,s->s.multiplicity*s.character.vec)=targetrow);
orderslots:=Lcm(List(slots,s->s.character.m));;
Assert(0,orderslots=12 or orderslots=4);
units:=[1,5,7,11];;
# CW formula for each effective cyclic character.  The sign convention
# exchanges the two displayed totals; their equality is convention independent.
HodgeCounts:=function(r,t)
  local a,b,e;
  a:=r.q-1; b:=r.q-1;
  for e in [1..r.m-1] do
    a:=a+r.cnt[e+1]*((t*e) mod r.m)/r.m;
    b:=b+r.cnt[e+1]*((-t*e) mod r.m)/r.m;
  od;
  Assert(0,IsInt(a) and IsInt(b) and a>=0 and b>=0 and a+b=r.h);
  return [a,b];
end;;
totals:=List(units,t->Sum(slots,s->s.multiplicity*HodgeCounts(s.character,t)));;
Assert(0,ForAll(totals,v->v[1]=v[2]));
profile:=rec(rowindex:=ROWINDEX,Wclass:=WCLASS,H0order:=Size(H0),Horder:=Size(H),
  raw_coefficients:=coeffs,raw_characters:=R,positive_slots:=slots,
  totalR:=Sum(slots,s->s.multiplicity),
  totalH:=Sum(slots,s->s.multiplicity*s.character.h),
  total_branch_count:=Sum(slots,s->s.multiplicity*s.character.s),
  fermat_dimension_S:=Sum(slots,s->s.multiplicity*(s.character.s-2)),
  quotient_genus:=slots[1].character.q,
  units:=units,hodge_totals:=totals,vec:=targetrow);;
Assert(0,profile.totalH=2*totals[1][1]);
Assert(0,profile.quotient_genus>=1);
Assert(0,ForAll(slots,s->s.character.q=profile.quotient_genus and s.character.s>=2));
Assert(0,profile.totalH=2*profile.quotient_genus*profile.totalR+profile.fermat_dimension_S);
path:=Concatenation("gale",String(WCLASS),"_verified.g");;
PrintTo(path,"PROFILE := ",profile,";\n");
Print("Gale row ",ROWINDEX," PASS; R,H,S = ",
 [profile.totalR,profile.totalH,profile.fermat_dimension_S],
 " total branch count ",profile.total_branch_count," units totals ",totals,"\n");
QUIT;

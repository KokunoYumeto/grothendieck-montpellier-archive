# Fresh subgroup and linear-character checks of twenty selected ordinary rows.
# GPT-6 Astra Pro, /root/sixfolds; 21 November 2026, inherited effort.
# Cwd is work/g34/e8/supplier_audit; common files are read, never changed.
Read("common_actual.g");
Read("actual_setup_data.g");
Read("row_functions.g");
if not IsBound(FAMILY) then FAMILY:="centralizers"; fi;
OUT:=Concatenation("/workspace/scratch/b92e12834723/work/sixfolds/e8/",
                  FAMILY,"_verified.g");;
PrintTo(OUT,"VERIFIED := [];\n");
SEEN:=[];;
CheckAndSave:=function(H,expected,description)
 local rows,found,r;
 Assert(0,IsSubgroup(GG,H));
 Print("BEGIN ",description," subgroup order ",Size(H),"\n");
 rows:=RowsOfGroup(H,false);
 rows:=Filtered(rows,r->r.adm);
 found:=Set(List(rows,r->r.index1));
 Assert(0,ForAll(expected,j->j in found));
 rows:=Filtered(rows,r->r.index1 in expected);
 WriteMatches(OUT,rows,description);
 for r in rows do AddSet(SEEN,r.index1); od;
 Print("FINISHED ",description," verified ",found,"\n");
end;;

if FAMILY="centralizers" then
 CASES:=[ [52,[224]],[64,[246]],[48,[290]],[41,[338]],
          [40,[366]],[50,[403]],[93,[404]],[59,[426]],
          [23,[434]],[19,[469]],[67,[493,857]] ];
 for item in CASES do
  ci:=item[1];; w:=CLASSMAP[ci];;
  Assert(0,GKey(w)=[0,ci]);
  CW:=Centralizer(GW,w);;
  Assert(0,Size(CW)=cent[ci]);
  H:=Group(Concatenation(GeneratorsOfGroup(CW),[iperm]));;
  CheckAndSave(H,item[2],Concatenation("actual centralizer W class ",String(ci)," plus i"));
 od;
 Assert(0,SEEN=[224,246,290,338,366,403,404,426,434,469,493,857]);
elif FAMILY="normalizers" then
 CASES:=[ [106,[457,459]],[59,[463]],[51,[473]] ];
 for item in CASES do
  ci:=item[1];; w:=CLASSMAP[ci];;
  Assert(0,GKey(w)=[0,ci]);
  NW:=Normalizer(GW,Group(w));;
  H:=Group(Concatenation(GeneratorsOfGroup(NW),[iperm]));;
  CheckAndSave(H,item[2],Concatenation("actual cyclic normalizer W class ",String(ci)," plus i"));
 od;
 Assert(0,SEEN=[457,459,463,473]);
elif FAMILY="reflections" then
 Cartan:=List([1..8],i->List([1..8],j->UNIT[i][j]-WG[i][i][j]));;
 topheight:=Maximum(List(ROOTS,Sum));;
 theta:=First(ROOTS,r->Sum(r)=topheight);;
 Assert(0,theta=[2,3,4,6,5,4,3,2]);
 Assert(0,Sum([1..8],i->Sum([1..8],j->theta[i]*Cartan[i][j]*theta[j]))=2);
 ninth:=List([1..8],i->List([1..8],j->UNIT[i][j]
          -theta[i]*Sum([1..8],k->theta[k]*Cartan[k][j])));;
 nine:=Concatenation(List(WG,wperm),[wperm(ninth)]);;
 Assert(0,ForAll(nine,r->r in GW and Order(r)=2 and GKey(r)=[0,67]));
 CASES:=[ [[1,2,4,5,7,8,9],[471]],
          [[1,2,3,4,6,7,8],[477]],
          [[1,3,4,5,6,8,9],[478]],
          [[1,2,4,5,6,7,8,9],[492]] ];
 for item in CASES do
  ss:=item[1];;
  H:=Group(Concatenation(nine{ss},[iperm,iperm^2]));;
  CheckAndSave(H,item[2],Concatenation("actual extended-root reflection subgroup ",String(ss)," plus i"));
 od;
 Assert(0,SEEN=[471,477,478,492]);
else
 Error("unknown family");
fi;
AppendTo(OUT,"VERIFIED_INDICES := ",SEEN,";\n");
Print("ALL REQUESTED ",FAMILY," ROWS PASS: ",SEEN,"\n");
QUIT;

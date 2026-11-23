Read("common_actual.g");
Read("actual_setup_data.g");
Read("row_functions.g");
PrintTo("abelian_verified.g","VERIFIED := [];\n");
# [selected index, W class, exponent on w, denominator of that exponent].
A1DATA := [[3,4,0,1],[8,70,0,1],[13,19,0,1],[14,30,0,1],
 [29,72,0,1],[41,97,0,1],[42,93,0,1],[43,95,6,12],
 [76,44,0,1],[78,59,0,1],[79,50,0,1],[330,93,2,10]];;
for dat in A1DATA do
  w:=CLASSMAP[dat[2]]; H:=Group([iperm,w]);;
  rows:=RowsOfGroup(H,false);;
  wantedvals:=[-E(4),E(dat[4])^dat[3]];;
  found:=Filtered(rows,r->r.index1=dat[1] and r.chigens=wantedvals);;
  Assert(0,Length(found)=1 and found[1].adm);
  WriteMatches("abelian_verified.g",found,Concatenation("<i,w>, W class ",String(dat[2])));
od;
# [selected index, W class, order of iw, exponent of character on iw].
CDATA := [[16,23,20,15],[18,4,4,3],[26,70,4,3],
 [195,23,20,3],[208,41,28,1],[217,48,36,3]];;
for dat in CDATA do
  w:=CLASSMAP[dat[2]]; gen:=iperm*w;;
  Assert(0,Order(gen)=dat[3]); H:=Group(gen);;
  rows:=RowsOfGroup(H,false);;
  found:=Filtered(rows,r->r.index1=dat[1] and r.chigens=[E(dat[3])^dat[4]]);;
  Assert(0,Length(found)=1 and found[1].adm);
  WriteMatches("abelian_verified.g",found,Concatenation("<iw>, W class ",String(dat[2])));
od;
Print("All18 abelian subgroup rows PASS\n");
QUIT;

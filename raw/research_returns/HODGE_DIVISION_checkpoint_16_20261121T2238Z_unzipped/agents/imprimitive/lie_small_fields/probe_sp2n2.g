LoadPackage("ctbllib");;
for name in ["S8(2)","S10(2)","S12(2)","S14(2)"] do
 t:=CharacterTable(name);
 if t=fail then Print(name," unavailable\n");continue;fi;
 cs:=Irr(t);best:=0;wit:=[];
 for i in [2..Length(cs)] do
  c:=cs[i];a:=c[1];
  for j in [2..Length(c)] do
   if IsRat(c[j]) then z:=AbsInt(c[j])^2;else z:=Sum(CoeffsCyc(c[j],Conductor(c[j])),x->AbsInt(x))^2;fi;
   if z/a^2>best then best:=z/a^2;wit:=[i,j,a,c[j],OrdersClassRepresentatives(t)[j]];fi;
  od;
 od;
 Print(name," rows=",Length(cs)," certified_triangle_squared_ratio_bound=",best," witness=",wit," all_real=",ForAll(cs,c->c=ComplexConjugate(c)),"\n");
od;
QUIT;

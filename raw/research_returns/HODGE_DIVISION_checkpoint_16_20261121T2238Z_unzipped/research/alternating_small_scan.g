# Exploratory complete ordinary A_n/S_n scan, n=8..14.
# Exact generic character tables from GAP/CTblLib; retained as computed inputs.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
HDAltEncode:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
HDAltParameter:=function(x)
 if IsChar(x) then return String(x);fi;
 if IsList(x) then return List(x,HDAltParameter);fi;
 return x;
end;
HDAltJSON:=function(name,obj)
 local f,encoded;
 encoded:=AGR.JsonText(obj,"ASCII");Assert(1,encoded<>fail);
 f:=OutputTextFile(Concatenation("research/",name),false);
 SetPrintFormattingStatus(f,false);PrintTo(f,encoded);CloseStream(f);
end;
input:=rec(source:="GAP4.16.1 generic Alternating/Symmetric tables; CTblLib1.3.11",tables:=[]);;
out:=rec(tables:=[],rows:=0,entries:=0);;
core:=fail;;irr:=[];;fus:=[];;t:=fail;;
for n in [8..14] do
 core:=CharacterTable("Alternating",n);;
 ext:=CharacterTable("Symmetric",n);;
 for kind in ["Alternating","Symmetric"] do
  if kind="Alternating" then t:=core;else t:=ext;fi;
  irr:=Irr(t);nr:=Length(irr);
  Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
  data:=rec(name:=Identifier(t),n:=n,order:=Size(t),
    orders:=OrdersClassRepresentatives(t),sizes:=SizesConjugacyClasses(t),
    characters:=List(irr,c->List(c,HDAltEncode)),
    character_parameters:=HDAltParameter(CharacterParameters(t)),class_parameters:=HDAltParameter(ClassParameters(t)),
    information:=InfoText(t),
    power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
  rows:=Filtered([1..nr],i->irr[i][1]>1);
  if kind="Symmetric" then
   fus:=GetFusionMap(core,t);Assert(1,fus<>fail);
   data.core:=Identifier(core);data.fusion:=fus;
   rows:=Filtered(rows,i->ScalarProduct(core,irr[i]{fus},irr[i]{fus})=1);
  fi;
  Add(input.tables,data);
  result:=rec(name:=Identifier(t),rows:=[],fifth_failure_rows:=[],quarter_failure_rows:=[]);
  for i in rows do
   c:=irr[i];a:=c[1];ratio:=1;worst:=[];
   for j in [1..nr] do
    if c[j]*GaloisCyc(c[j],-1)=a^2 then continue;fi;
    ev:=EigenvaluesChar(t,c,j);
    Assert(1,ForAll(ev,x->IsInt(x) and x>=0));Assert(1,Sum(ev)=a);
    nu:=a-Maximum(ev);
    if nu/a<ratio then ratio:=nu/a;worst:=[rec(class:=j,nu:=nu,multiplicities:=ev)];
    elif nu/a=ratio then Add(worst,rec(class:=j,nu:=nu,multiplicities:=ev));fi;
    out.entries:=out.entries+1;
   od;
   item:=rec(row:=i,degree:=a,parameter:=HDAltParameter(CharacterParameters(t)[i]),
             min_ratio:=String(ratio),worst:=worst);
   Add(result.rows,item);
   if 5*ratio<1 then Add(result.fifth_failure_rows,item);fi;
   if 4*ratio<1 then Add(result.quarter_failure_rows,item);fi;
   out.rows:=out.rows+1;
  od;
  Add(out.tables,result);
  Print(Identifier(t)," selected=",Length(rows)," fifthfail=",Length(result.fifth_failure_rows),
    " quarterfail=",Length(result.quarter_failure_rows),"\n");
 od;
od;
HDAltJSON("alternating_small_inputs.json",input);
HDAltJSON("alternating_small_scan.json",out);
Print("TOTAL rows=",out.rows," entries=",out.entries,"\n");
QUIT;

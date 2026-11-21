if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
SetAssertionLevel(1);;
root:=Directory("HODGE_DIVISION_work/agents/imprimitive/sporadic");;
result:=[];;
for name in ["2.Co1","2.Ru","3.J3","6.Suz","2.J2","2.Suz"] do
 t:=CharacterTable(name);;ir:=Irr(t);;deg:=Minimum(Filtered(List(ir,x->x[1]),x->x>1));;
 rows:=Filtered([1..Length(ir)],i->ir[i][1]=deg);;
 a:=rec(name:=name,minimum_nonlinear_degree:=deg,rows:=[]);;
 for i in rows do
  data:=[];;
  for j in [1..NrConjugacyClasses(t)] do
   ev:=EigenvaluesChar(t,ir[i],j);;
   Assert(1,ForAll(ev,x->IsInt(x) and x>=0));Assert(1,Sum(ev)=deg);
   Add(data,rec(class:=j,label:=ClassNames(t)[j],order:=Length(ev),multiplicities_one_first:=ev,nu:=deg-Maximum(ev)));
  od;
  bound:=Minimum(List(Filtered(data,x->x.nu>0),x->x.nu));;
  Add(a.rows,rec(row:=i,degree:=deg,min_nu:=bound,attaining_classes:=List(Filtered(data,x->x.nu=bound),x->x.label),classes:=data));
 od;
 Add(result,a);
 Print(name," degree ",deg," rows ",rows," min_nu ",List(a.rows,x->x.min_nu),"\n");
od;
stream:=OutputTextFile(Filename(root,"small_spectra.json"),false);;
SetPrintFormattingStatus(stream,false);;
PrintTo(stream,AGR.JsonText(result,"ASCII"));CloseStream(stream);
QUIT;

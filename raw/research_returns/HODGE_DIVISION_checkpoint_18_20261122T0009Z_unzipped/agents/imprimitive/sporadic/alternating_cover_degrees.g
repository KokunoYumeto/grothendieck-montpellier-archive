if LoadPackage("ctbllib")<>true then Error("CTblLib missing");fi;
SetAssertionLevel(1);;
out:=[];;
for n in [8..11] do
 name:=Concatenation("2.A",String(n));;t:=CharacterTable(name);;ir:=Irr(t);;
 center:=Filtered([1..NrConjugacyClasses(t)],i->SizesConjugacyClasses(t)[i]=1);;
 Assert(1,Length(center)=2);z:=First(center,i->OrdersClassRepresentatives(t)[i]=2);;
 Assert(1,z<>fail);
 rows:=Filtered([1..Length(ir)],i->ir[i][z]=-ir[i][1]);;
 Assert(1,MatScalarProducts(t,ir,ir)=IdentityMat(Length(ir)));
 r:=rec(name:=name,degree:=n,order:=Size(t),classes:=Length(ir),central_involution_class:=z,
        faithful_rows:=rows,faithful_degrees:=List(rows,i->ir[i][1]),
        contains_degree24:=ForAny(rows,i->ir[i][1]=24),information:=InfoText(t));;
 Add(out,r);Print(name," faithful degrees ",r.faithful_degrees,"\n");
od;
stream:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/sporadic/alternating_cover_degrees.json",false);;
SetPrintFormattingStatus(stream,false);PrintTo(stream,AGR.JsonText(out,"ASCII"));CloseStream(stream);
QUIT;

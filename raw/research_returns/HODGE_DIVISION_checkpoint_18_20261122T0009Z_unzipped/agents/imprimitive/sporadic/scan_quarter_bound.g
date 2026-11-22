# Complete class/character scan of all 26 Schur covers and 12 outer extensions.
# Input is the author-maintained CTblLib 1.3.11.  All arithmetic is exact.
if LoadPackage("ctbllib") <> true then Error("CTblLib missing"); fi;
SizeScreen([240]);;
SetAssertionLevel(1);;
root := Directory("HODGE_DIVISION_work/agents/imprimitive/sporadic");;
covers := AllCharacterTableNames(IsSporadicSimple,true,IsDuplicateTable,false,OfThose,SchurCover);;
Assert(1,Length(covers)=26);
out := rec(gap_version:=GAPInfo.Version,ctbllib_version:=PackageInfo("ctbllib")[1].Version,
           covers:=covers,tables:=[],failures:=[],total_rows:=0,total_entries:=0);
WriteResult := function()
 local stream;
 stream:=OutputTextFile(Filename(root,"quarter_scan.json"),false);
 SetPrintFormattingStatus(stream,false);
 PrintTo(stream,AGR.JsonText(out,"ASCII"));
 CloseStream(stream);
end;

CheckTable := function(name,core)
 local t,irr,rows,fus,row,vals,deg,j,z,a,bd,ev,nu,r,exc,scalar,checked,indices,chi;
 t:=CharacterTable(name); irr:=Irr(t); rows:=[1..Length(irr)];
 Assert(1,Sum(irr,x->x[1]^2)=Size(t));
 Assert(1,Length(irr)=NrConjugacyClasses(t));
 if core<>fail then
  fus:=GetFusionMap(core,t); Assert(1,fus<>fail);
  rows:=Filtered(rows,i->ScalarProduct(core,irr[i]{fus},irr[i]{fus})=1);
 fi;
 rows:=Filtered(rows,i->irr[i][1]>1);
 r:=rec(name:=name,order:=Size(t),classes:=Length(irr),selected_rows:=rows,
        degrees:=List(rows,i->irr[i][1]),checks:=[],exceptional_spectra:=[],
        information:=InfoText(t));
 if core<>fail then r.core:=Identifier(core); r.fusion:=fus; fi;
 for row in rows do
  chi:=irr[row];deg:=chi[1];exc:=[];scalar:=[];checked:=0;
  for j in [1..Length(chi)] do
   z:=chi[j];a:=z*GaloisCyc(z,-1);
   if a=deg^2 then Add(scalar,j);
   else
    # Triangle inequality in the exact cyclotomic power basis bounds |z|^2.
    bd:=Sum(List(CoeffsCyc(a,Conductor(a)),AbsInt));
    if 4*bd>deg^2 then
     ev:=EigenvaluesChar(t,chi,j);
     Assert(1,ForAll(ev,x->IsInt(x) and x>=0));
     Assert(1,Sum(ev)=deg);
     nu:=deg-Maximum(ev);
     Add(exc,rec(class:=j,order:=Length(ev),multiplicities:=ev,nu:=nu,
                 trace:=String(z),absolute_square:=String(a)));
     if 4*nu<deg then Add(out.failures,rec(table:=name,row:=row,degree:=deg,class:=j,nu:=nu)); fi;
    fi;
    checked:=checked+1;
   fi;
  od;
  Add(r.checks,rec(row:=row,degree:=deg,scalar_classes:=scalar,checked:=checked,exceptional:=Length(exc)));
  if Length(exc)>0 then Add(r.exceptional_spectra,rec(row:=row,degree:=deg,classes:=exc));fi;
  out.total_entries:=out.total_entries+checked;out.total_rows:=out.total_rows+1;
 od;
 Add(out.tables,r);
 Print(name," rows=",Length(rows)," exceptions=",Sum(r.checks,x->x.exceptional)," failures_total=",Length(out.failures),"\n");
 WriteResult();
end;

for name in covers do
 core:=CharacterTable(name);;
 CheckTable(name,fail);
 ext:=CharacterTable(Concatenation(name,".2"));;
 if ext<>fail then CheckTable(Identifier(ext),core);fi;
od;
out.status:="complete";
out.quarter_bound_pass:=IsEmpty(out.failures);
WriteResult();
Print("COMPLETE: tables=",Length(out.tables)," rows=",out.total_rows," entries=",out.total_entries," failures=",Length(out.failures),"\n");
QUIT;

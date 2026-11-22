LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetInfoLevel(InfoPackageLoading,0);;
SetAssertionLevel(1);;
out:=rec(tables:=[]);;
for pair in [["6.O7(3)","6.O7(3)"],["6.O7(3).2","6.O7(3)"],
 ["O8-(2)","O8-(2)"],["O8-(2).2","O8-(2)"],
 ["2^2.O8+(3)","2^2.O8+(3)"],["2.O8-(3)","2.O8-(3)"],
 ["2.O9(3)","2.O9(3)"],
 ["O10+(2)","O10+(2)"],["O10+(2).2","O10+(2)"],
 ["O10-(2)","O10-(2)"],["O10-(2).2","O10-(2)"],
 ["O12+(2)","O12+(2)"],["O12+(2).2","O12+(2)"],
 ["O12-(2)","O12-(2)"],["O12-(2).2","O12-(2)"]] do
 name:=pair[1];core:=pair[2];t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);;
 rows:=Filtered([1..Length(irr)],i->irr[i][1]>1);;
 if name<>core then
  ci:=Irr(CharacterTable(core));fus:=GetFusionMap(CharacterTable(core),t);Assert(1,fus<>fail);
  rows:=Filtered(rows,i->ForAny(ci,c->irr[i]{fus}=c));
 fi;
 r:=rec(name:=name,core:=core,rows:=[],spectra:=0,minratio:=1,
  min_degree:=Minimum(List(rows,i->irr[i][1])));;
 for i in rows do
  chi:=irr[i];a:=chi[1];nu:=a;witness:=0;
  for j in [1..Length(irr)] do
   if chi[j]*GaloisCyc(chi[j],-1)=a^2 then continue;fi;
   ev:=EigenvaluesChar(t,chi,j);Assert(1,ForAll(ev,x->IsInt(x) and x>=0) and Sum(ev)=a);
   if a-Maximum(ev)<nu then nu:=a-Maximum(ev);witness:=j;fi;
   r.spectra:=r.spectra+1;
  od;
  Add(r.rows,rec(row:=i,degree:=a,nu:=nu,ratio:=String(nu/a),witness:=witness));
  r.minratio:=Minimum(r.minratio,nu/a);
 od;
 Print(name," rows=",Length(r.rows)," spectra=",r.spectra," min_degree=",r.min_degree," min_ratio=",r.minratio,"\n");
 Print("MIN ",Filtered(r.rows,x->x.nu/x.degree=r.minratio),"\n");
 r.minratio:=String(r.minratio);Add(out.tables,r);
 f:=OutputTextFile("research/orthogonal_small_probe.json",false);;
 SetPrintFormattingStatus(f,false);PrintTo(f,AGR.JsonText(out,"ASCII"));CloseStream(f);
od;
Print("ORTHOGONAL PROBE COMPLETE\n");
QUIT;

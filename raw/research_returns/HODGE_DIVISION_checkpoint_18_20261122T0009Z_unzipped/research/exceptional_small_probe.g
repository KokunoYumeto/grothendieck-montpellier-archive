LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
SetInfoLevel(InfoPackageLoading,0);;
out:=rec(tables:=[]);;
for name in ["2.F4(2)","F4(3)","E6(2)","(2^2x3).2E6(2)"] do
 t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);;
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(Length(irr)));
 rr:=rec(name:=name,rows:=[],spectra:=0,min_support_ratio:=1,min_degree:=Minimum(Filtered(List(irr,c->c[1]),x->x>1)));;
 for i in [1..Length(irr)] do
  chi:=irr[i];a:=chi[1];if a=1 then continue;fi;
  nu:=a;minclass:=0;
  for j in [1..Length(irr)] do
   if chi[j]*GaloisCyc(chi[j],-1)=a^2 then continue;fi;
   ev:=EigenvaluesChar(t,chi,j);Assert(1,ForAll(ev,x->IsInt(x) and x>=0) and Sum(ev)=a);
   if a-Maximum(ev)<nu then nu:=a-Maximum(ev);minclass:=j;fi;
   rr.spectra:=rr.spectra+1;
  od;
  Add(rr.rows,rec(row:=i,degree:=a,support:=nu,ratio:=String(nu/a),minclass:=minclass));
  rr.min_support_ratio:=Minimum(rr.min_support_ratio,nu/a);
 od;
 Print(name," rows=",Length(rr.rows)," spectra=",rr.spectra," min_degree=",rr.min_degree," min_ratio=",rr.min_support_ratio,"\n");
 Print("MIN ",Filtered(rr.rows,x->x.support/x.degree=rr.min_support_ratio),"\n");
 rr.min_support_ratio:=String(rr.min_support_ratio);Add(out.tables,rr);
od;
f:=OutputTextFile("research/exceptional_small_probe.json",false);;
SetPrintFormattingStatus(f,false);;PrintTo(f,AGR.JsonText(out,"ASCII"));;CloseStream(f);;
Print("COMPLETE EXCEPTIONAL PROBE\n");
QUIT;

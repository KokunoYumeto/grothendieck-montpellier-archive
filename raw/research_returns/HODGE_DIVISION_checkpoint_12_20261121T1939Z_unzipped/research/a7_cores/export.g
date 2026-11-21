# Full universal A7 cover and one cyclic outer extension; all rows retained.
LoadPackage("ctbllib");;
LoadPackage("atlasrep");;
SetAssertionLevel(1);;
SetInfoLevel(InfoPackageLoading,0);;
dest:=Directory("research/a7_cores");;
EncodeA7:=function(z)
 local n,c;
 if IsInt(z) then return z;fi;
 n:=Conductor(z);c:=CoeffsCyc(z,n);Assert(1,ForAll(c,IsInt));return [n,c];
end;
WriteA7:=function(name,obj)
 local f;
 f:=OutputTextFile(Filename(dest,name),false);SetPrintFormattingStatus(f,false);
 PrintTo(f,AGR.JsonText(obj,"ASCII"));CloseStream(f);
end;
input:=rec(source:="Complete official CTblLib ordinary tables; exact provenance retained",tables:=[]);;
out:=rec(status:="exploratory complete A7 spectra",rows:=0,spectra:=0,tables:=[]);;
core:=CharacterTable("6.A7");;ci:=Irr(core);;
for name in ["6.A7","6.A7.2"] do
 t:=CharacterTable(name);Assert(1,t<>fail);irr:=Irr(t);nr:=Length(irr);
 Assert(1,MatScalarProducts(t,irr,irr)=IdentityMat(nr));
 r:=rec(name:=Identifier(t),order:=Size(t),orders:=OrdersClassRepresentatives(t),
  sizes:=SizesConjugacyClasses(t),class_names:=ClassNames(t),
  characters:=List(irr,ch->List(ch,EncodeA7)),information:=InfoText(t),
  indicators:=Indicator(t,irr,2),
  power_maps:=List(Set(FactorsInt(Size(t))),p->rec(prime:=p,map:=PowerMap(t,p))));
 if name="6.A7" then
  fus:=[1..Length(ci)];r.extension_information:=ExtensionInfoCharacterTable(CharacterTable("A7"));
 else fus:=GetFusionMap(core,t);Assert(1,fus<>fail);r.core:="6.A7";r.fusion:=fus;fi;
 rows:=Filtered([1..nr],i->irr[i][1]>1 and ForAny(ci,c->irr[i]{fus}=c));
 Add(input.tables,r);
 recout:=rec(name:=name,rows:=[],spectra:=0);
 for i in rows do
  c:=irr[i];a:=c[1];rr:=rec(row:=i,degree:=a,min_nu:=a,minimizers:=[],quarter_failures:=[]);
  for j in [1..nr] do
   if c[j]*GaloisCyc(c[j],-1)=a^2 then continue;fi;
   ev:=EigenvaluesChar(t,c,j);
   Assert(1,ForAll(ev,x->IsInt(x) and x>=0));Assert(1,Sum(ev)=a);
   nu:=a-Maximum(ev);
   if nu<rr.min_nu then rr.min_nu:=nu;rr.minimizers:=[];fi;
   if nu=rr.min_nu then Add(rr.minimizers,rec(class:=j,order:=r.orders[j],multiplicities:=ev));fi;
   if 4*nu<a then Add(rr.quarter_failures,rec(class:=j,degree:=a,nu:=nu,multiplicities:=ev));fi;
   recout.spectra:=recout.spectra+1;out.spectra:=out.spectra+1;
  od;
  Add(recout.rows,rr);out.rows:=out.rows+1;
 od;
 Add(out.tables,recout);
 Print(name," selected=",Length(rows)," spectra=",recout.spectra,"\n");
 Print("row degree minimum-support quarter-failures\n");
 for rr in recout.rows do Print(rr.row," ",rr.degree," ",rr.min_nu," ",Length(rr.quarter_failures),"\n");od;
od;
WriteA7("inputs.json",input);WriteA7("scan.json",out);
Print("PASS rows=",out.rows," spectra=",out.spectra,"\n");
QUIT;

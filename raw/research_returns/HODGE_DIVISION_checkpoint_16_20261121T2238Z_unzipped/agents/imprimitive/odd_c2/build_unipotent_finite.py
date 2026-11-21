#!/usr/bin/env python3
"""Emit exact GAP checks of the publication transcription at q=5,7,9."""
from pathlib import Path
from unipotent_data import symbolic
B=Path(__file__).resolve().parent
q,t,bs,rs=symbolic()
expr='[\n'+',\n'.join('['+','.join(str(x).replace('**','^') for x in v)+']' for v in rs.values())+'\n]'
program='''LoadPackage("ctbllib");; LoadPackage("atlasrep");;
SetAssertionLevel(1);;
results:=[];; tab:=fail;; idx:=[];; p:=0;; pp:=[];; pub:=[];;
for case in [[5,"2.S4(5)"],[7,"S4(7)"],[9,"S4(9)"]] do
 q:=case[1]; t:=ER((-1)^((q-1)/2)*q);
 pub:='''+expr+''';;
 tab:=CharacterTable(case[2]); ps:=PrimeDivisors(q);p:=ps[1];
 idx:=Filtered([1..NrConjugacyClasses(tab)],j->IsOne(OrdersClassRepresentatives(tab)[j]) or Set(FactorsInt(OrdersClassRepresentatives(tab)[j]))=[p]);;
 Assert(1,Length(idx)=7);
 actual:=List(Irr(tab),r->r{idx});
 good:=[];
 for perm in PermutationsList([2..7]) do
  pp:=Concatenation([1],perm);
  if ForAll(actual,r->r{pp} in pub) then Add(good,pp);fi;
 od;
 Assert(1,Length(good)>0);
 r:=rec(q:=q,table:=case[2],rows:=Length(actual),unipotent_classes:=idx,column_matches:=good);
 Add(results,r);Print(case[2]," rows=",Length(actual)," matching column permutations=",Length(good)," PASS\\n");
od;
f:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/odd_c2/unipotent_finite_crosscheck.json",false);SetPrintFormattingStatus(f,false);PrintTo(f,AGR.JsonText(rec(status:="PASS",results:=results),"ASCII"));CloseStream(f);QUIT;
'''
(B/'check_unipotent_finite.g').write_text(program)
print('Generated the assertion-based finite source cross-check')

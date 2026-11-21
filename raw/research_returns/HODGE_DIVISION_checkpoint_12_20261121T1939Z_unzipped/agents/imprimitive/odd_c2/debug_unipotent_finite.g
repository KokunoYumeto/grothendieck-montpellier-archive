LoadPackage("ctbllib");; LoadPackage("atlasrep");;
SetAssertionLevel(1);;
results:=[];; tab:=fail;; idx:=[];; p:=0;; pp:=[];; pub:=[];;
for case in [[5,"2.S4(5)"],[7,"S4(7)"],[9,"S4(9)"]] do
 q:=case[1]; t:=ER((-1)^((q-1)/2)*q);
 pub:=[
[1,1,1,1,1,1,1],
[q^4 - 2*q^2 + 1,1 - q^2,1 - q^2,1 - q,q + 1,1,1],
[q^4 - 1,q^2 - 1,q^2 - 1,-q - 1,q - 1,-1,-1],
[q^4 + 2*q^3 + 2*q^2 + 2*q + 1,q^2 + 2*q + 1,q^2 + 2*q + 1,3*q + 1,q + 1,1,1],
[q^4 - 2*q^3 + 2*q^2 - 2*q + 1,q^2 - 2*q + 1,q^2 - 2*q + 1,1 - q,1 - 3*q,1,1],
[q^4 - 1,-q^2 - 1,-q^2 - 1,q - 1,-q - 1,-1,-1],
[q^3 - q^2 + q - 1,q - 1,q - 1,-1,2*q - 1,-1,-1],
[q^4 - q^3 + q^2 - q,q^2 - q,q^2 - q,-q,-q,0,0],
[q^3 + q^2 + q + 1,q + 1,q + 1,2*q + 1,1,1,1],
[q^4 + q^3 + q^2 + q,q^2 + q,q^2 + q,q,q,0,0],
[q^3 - q^2 + q - 1,-q^2 + q - 1,-q^2 + q - 1,q - 1,q - 1,-1,-1],
[q^4 - q^3 + q^2 - q,-q,-q,0,-2*q,0,0],
[q^3 + q^2 + q + 1,q^2 + q + 1,q^2 + q + 1,q + 1,q + 1,1,1],
[q^4 + q^3 + q^2 + q,q,q,2*q,0,0,0],
[q^4/2 - 1/2,q^2*t/2 - q^2/2 - q*t/2 - 1/2,-q^2*t/2 - q^2/2 + q*t/2 - 1/2,q/2 - 1/2,-q/2 - 1/2,-t/2 - 1/2,t/2 - 1/2],
[q^4/2 - 1/2,-q^2*t/2 - q^2/2 + q*t/2 - 1/2,q^2*t/2 - q^2/2 - q*t/2 - 1/2,q/2 - 1/2,-q/2 - 1/2,t/2 - 1/2,-t/2 - 1/2],
[q^4/2 - q^3 + q^2 - q + 1/2,q^2*t/2 + q^2/2 - q*t/2 - q + 1/2,-q^2*t/2 + q^2/2 + q*t/2 - q + 1/2,1/2 - q/2,1/2 - 3*q/2,1/2 - t/2,t/2 + 1/2],
[q^4/2 - q^3 + q^2 - q + 1/2,-q^2*t/2 + q^2/2 + q*t/2 - q + 1/2,q^2*t/2 + q^2/2 - q*t/2 - q + 1/2,1/2 - q/2,1/2 - 3*q/2,t/2 + 1/2,1/2 - t/2],
[q^4/2 + q^3 + q^2 + q + 1/2,q^2*t/2 + q^2/2 - 3*q*t/2 + q + 1/2,-q^2*t/2 + q^2/2 + 3*q*t/2 + q + 1/2,3*q/2 + 1/2,q/2 + 1/2,1/2 - 3*t/2,3*t/2 + 1/2],
[q^4/2 + q^3 + q^2 + q + 1/2,-q^2*t/2 + q^2/2 + 3*q*t/2 + q + 1/2,q^2*t/2 + q^2/2 - 3*q*t/2 + q + 1/2,3*q/2 + 1/2,q/2 + 1/2,3*t/2 + 1/2,1/2 - 3*t/2],
[q^4/2 - 1/2,-q^2*t/2 - q^2/2 + 3*q*t/2 - 1/2,q^2*t/2 - q^2/2 - 3*q*t/2 - 1/2,q/2 - 1/2,-q/2 - 1/2,3*t/2 - 1/2,-3*t/2 - 1/2],
[q^4/2 - 1/2,q^2*t/2 - q^2/2 - 3*q*t/2 - 1/2,-q^2*t/2 - q^2/2 + 3*q*t/2 - 1/2,q/2 - 1/2,-q/2 - 1/2,-3*t/2 - 1/2,3*t/2 - 1/2],
[q^3/2 - q^2/2 + q/2 - 1/2,-q^2/2 + q*t/2 + q/2 - 1/2,-q^2/2 - q*t/2 + q/2 - 1/2,q/2 - 1/2,q/2 - 1/2,t/2 - 1/2,-t/2 - 1/2],
[q^3/2 - q^2/2 + q/2 - 1/2,-q^2/2 - q*t/2 + q/2 - 1/2,-q^2/2 + q*t/2 + q/2 - 1/2,q/2 - 1/2,q/2 - 1/2,-t/2 - 1/2,t/2 - 1/2],
[q^4/2 - q^3/2 + q^2/2 - q/2,q^2*t/2 - q/2,-q^2*t/2 - q/2,0,-q,0,0],
[q^4/2 - q^3/2 + q^2/2 - q/2,-q^2*t/2 - q/2,q^2*t/2 - q/2,0,-q,0,0],
[q^3/2 + q^2/2 + q/2 + 1/2,q^2/2 - q*t/2 + q/2 + 1/2,q^2/2 + q*t/2 + q/2 + 1/2,q/2 + 1/2,q/2 + 1/2,1/2 - t/2,t/2 + 1/2],
[q^3/2 + q^2/2 + q/2 + 1/2,q^2/2 + q*t/2 + q/2 + 1/2,q^2/2 - q*t/2 + q/2 + 1/2,q/2 + 1/2,q/2 + 1/2,t/2 + 1/2,1/2 - t/2],
[q^4/2 + q^3/2 + q^2/2 + q/2,-q^2*t/2 + q/2,q^2*t/2 + q/2,q,0,0,0],
[q^4/2 + q^3/2 + q^2/2 + q/2,q^2*t/2 + q/2,-q^2*t/2 + q/2,q,0,0,0],
[q^3 + q,q,q,q,q,0,0],
[q^4/2 + q^2/2,-q^2*t/2 + q^2/2,q^2*t/2 + q^2/2,0,0,0,0],
[q^4/2 + q^2/2,q^2*t/2 + q^2/2,-q^2*t/2 + q^2/2,0,0,0,0],
[q^2/2 + 1/2,q*t/2 + 1/2,-q*t/2 + 1/2,q/2 + 1/2,1/2 - q/2,t/2 + 1/2,1/2 - t/2],
[q^2/2 + 1/2,-q*t/2 + 1/2,q*t/2 + 1/2,q/2 + 1/2,1/2 - q/2,1/2 - t/2,t/2 + 1/2],
[q^4/2 - q^2/2,q^2*t/2 - q^2/2,-q^2*t/2 - q^2/2,0,0,0,0],
[q^4/2 - q^2/2,-q^2*t/2 - q^2/2,q^2*t/2 - q^2/2,0,0,0,0],
[q^2/2 - 1/2,q*t/2 - 1/2,-q*t/2 - 1/2,q/2 - 1/2,-q/2 - 1/2,t/2 - 1/2,-t/2 - 1/2],
[q^2/2 - 1/2,-q*t/2 - 1/2,q*t/2 - 1/2,q/2 - 1/2,-q/2 - 1/2,-t/2 - 1/2,t/2 - 1/2],
[q^3/2 + q^2 + q/2,q^2/2 + q/2,q^2/2 + q/2,q,0,0,0],
[q^3/2 - q^2 + q/2,-q^2/2 + q/2,-q^2/2 + q/2,0,q,0,0],
[q^3/2 + q/2,-q^2/2 + q/2,-q^2/2 + q/2,q,0,0,0],
[q^3/2 + q/2,q^2/2 + q/2,q^2/2 + q/2,0,q,0,0],
[q^4,0,0,0,0,0,0]
];;
 tab:=CharacterTable(case[2]); ps:=PrimeDivisors(q);p:=ps[1];
 idx:=Filtered([1..NrConjugacyClasses(tab)],j->IsOne(OrdersClassRepresentatives(tab)[j]) or Set(FactorsInt(OrdersClassRepresentatives(tab)[j]))=[p]);;
 Assert(1,Length(idx)=7);
 actual:=List(Irr(tab),r->r{idx});
 good:=[]; best:=0;bestperm:=[];
 for perm in PermutationsList([2..7]) do
  pp:=Concatenation([1],perm);
  score:=Number(actual,r->r{pp} in pub); if score>best then best:=score;bestperm:=pp;fi; if score=Length(actual) then Add(good,pp);fi;
 od;
 Print("BEST ",case[2]," ",best,"/",Length(actual)," perm ",bestperm,"\n"); for j in [1..Length(actual)] do if not actual[j]{bestperm} in pub then Print("MISMATCH row ",j,": ",actual[j]{bestperm},"\n");fi;od;
 r:=rec(q:=q,table:=case[2],rows:=Length(actual),unipotent_classes:=idx,column_matches:=good);
 Add(results,r);Print(case[2]," rows=",Length(actual)," matching column permutations=",Length(good)," DIAGNOSTIC ONLY\n");
od;
f:=OutputTextFile("HODGE_DIVISION_work/agents/imprimitive/odd_c2/debug_unipotent_finite_output.json",false);SetPrintFormattingStatus(f,false);PrintTo(f,AGR.JsonText(rec(status:="DIAGNOSTIC: inspect mismatches",results:=results),"ASCII"));CloseStream(f);QUIT;

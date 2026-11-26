\\ Standalone certified base-field computations; no saved number-field data.
default(parisizemax,2000000000);default(realprecision,100);
require(ok,msg)={if(!ok,error(msg));print("PASS ",msg)};
main()={
polynomials=[y^3-269,y^6+3*y^5+6*y^4+545*y^3+813*y^2-804*y+71824];
classes=[[7],[7,7]];logs=[[[3],[3],[]],[[9,3],[9,3],[]]];
for(j=1,2,my(b=bnfinit(polynomials[j],1));require(bnfcertify(b)==1,Str("complete class and unit certification ",j));require(nfcertify(b)==[],Str("maximal order ",j));require(b.cyc==classes[j],Str("ordinary class invariants ",j));require(bnflog(b,3)==logs[j],Str("logarithmic invariants ",j));print("FIELD ",j," DISCRIMINANT ",b.disc," LOG_GROUP ",bnflog(b,3));if(j==2,my(z=Mod(y,polynomials[j]),a=(269-(2*z+1)*(z^2+z+1))/(3*z*(z+1)),w=z+a);require(a^3==269 && w^2+w+1==0,"exact normal closure identification")));
print("BASE_CERTIFICATES_COMPLETE");
};
iferr(main(),err,print("FAIL ",err);quit(1));quit

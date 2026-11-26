\\ Independent fresh logarithmic action reconstruction; abort-on-error main function.
default(parisize,500000000);
default(parisizemax,2000000000);
default(realprecision,100);
assert(test,label)={if(!test,error(Str("FAILED: ",label)));print("PASS ",label)};
classdecomp(J)={my(z=bnfisprincipal(b,J,1),u);u=nfbasistoalg(b,z[2])/prod(k=1,ng,class_shift[k]^z[1][k]);assert(idealmul(b,idealfactorback(b,class_ideals,z[1]),u)==idealhnf(b,J),"exact ideal decomposition");[z[1],u]};
reconstruct(N)={
 my(fac=factorpadic(p,3,N)[,1],fp,degree,logval,r,cols,rel,act,K,small,q,qn,k,good=0);
 fp=vector(2,j,select(t->poldegree(t)==pr[j].e*pr[j].f,fac)[1]);
 degree=3*log(4+O(3^N));
 logval=(u->(vector(2,j,-log(polresultant(fp[j],lift(nfbasistoalg(b,u))))/degree)~));
 r=vector(ng,j,log(idealnorm(b,class_ideals[j])+O(3^N))/degree);
 cols=concat(concat(vector(ng,j,relpow[j][2]),vector(2,j,relpr[j][2])),b.fu);
 rel=matrix(4,#cols,i,j,if(i>ng,logval(cols[j])[i-ng],if(j<=ng,if(i==j,b.cyc[j],0),if(j<=ng+2,-relpr[j-ng][1][i],0))));
 assert(padicprec(rel,3)>N-20,"relation precision after logarithms");
 assert(vecmin(vector(#cols,j,valuation(sum(i=1,ng,r[i]*rel[i,j])+rel[3,j]+rel[4,j],3)))>N-20,"product formula to retained precision");
 act=matid(4);
 for(j=1,ng,for(i=1,ng,act[i,j]=relgamma[j][1][i]);for(i=1,2,act[ng+i,j]=-logval(relgamma[j][2])[i]));
 K=matrix(4,3,i,j,if(i<=3,if(i==j,1,0),if(j<=ng,-r[j],-1)));
 small=(act*K)[1..3,]; rel=rel[1..3,];
 assert(padicprec(small,3)>N-20,"action precision after logarithms");
 print("PRECISION ",N," RELATIONS_MOD27 ",lift(Mod(rel,27))," ACTION_MOD27 ",lift(Mod(small,27)));
 assert(matsnf(mathnf(concat(lift(Mod(rel,27)),27*matid(3))))==[9,1,1],"finite Smith invariants");
 for(qn=1,728,q=[qn%9,(qn\9)%9,(qn\81)%9];if(gcd(gcd(q[1],q[2]),gcd(q[3],3))==1 && lift(Mod(q*rel,9))==vector(#cols),good++;assert(lift(Mod(q*small-4*q,9))==[0,0,0],"oriented quotient action four")));
 assert(good==6,"all six primitive characters checked");
 [lift(Mod(rel,27)),lift(Mod(small,27))]
};
main()={
p=y^9-3*y^7-270*y^6+810*y^5+1347*y^4-48600*y^3-72900*y^2-96123*y-728731;
assert(polisirreducible(p),"degree-nine field irreducible");
b=bnfinit(p,1);
print("SIGNATURE ",b.nf.sign," DISCRIMINANT ",b.disc," CLASS_INVARIANTS ",b.cyc);
assert(bnfcertify(b)==1,"full class-group and unit certification");

assert(nfcertify(b)==[],"maximal order");
print("LOG_CLASS ",bnflog(b,3));
assert(bnflog(b,3)[1]==[9],"degree-zero logarithmic group cyclic nine");
a=nfroots(b,x^3-269)[1]; beta=nfroots(b,x^3-3*x+1)[1];
assert(a^3==269 && beta^3-3*beta+1==0,"exact embedded cubic fields");
auts=nfgaloisconj(b);
chosen=select(t->nfgaloisapply(b,t,a)==a && nfgaloisapply(b,t,beta)==2-beta-beta^2,auts);
assert(#chosen==1,"unique cyclotomic automorphism of value four");
gamma_aut=chosen[1];
pr=idealprimedec(b,3);
if(pr[1].e*pr[1].f<pr[2].e*pr[2].f,pr=Vecrev(pr));
assert(#pr==2 && pr[1].e*pr[1].f==6 && pr[2].e*pr[2].f==3,"local degrees six and three");
assert(vector(2,j,bnflogef(b,pr[j]))==[[2,3],[1,3]],"logarithmic local indices");
for(j=1,2,assert(idealhnf(b,nfgaloisapply(b,gamma_aut,pr[j]))==idealhnf(b,pr[j]),Str("prime fixed ",j)));
ng=#b.gen;
assert(ng==2 && b.cyc==[21,3],"ordinary class presentation");
class_shift=vector(ng,j,nfbasistoalg(b,idealcoprime(b,b.gen[j],3)));
class_ideals=vector(ng,j,idealmul(b,b.gen[j],class_shift[j]));
assert(matrix(2,ng,j,i,idealval(b,class_ideals[i],pr[j]))==matrix(2,ng),"representatives coprime to three");
relpow=vector(ng,j,classdecomp(idealpow(b,class_ideals[j],b.cyc[j])));
relpr=vector(2,j,classdecomp(pr[j]));
relgamma=vector(ng,j,classdecomp(nfgaloisapply(b,gamma_aut,class_ideals[j])));
for(j=1,ng,assert(relpow[j][1]==Col(vector(ng)),Str("principal class power ",j)));
R60=reconstruct(60);R90=reconstruct(90);assert(R60==R90,"independent local precision agreement");
print("FRESH_ACTION_CERTIFICATE_COMPLETE");
};
main();
quit

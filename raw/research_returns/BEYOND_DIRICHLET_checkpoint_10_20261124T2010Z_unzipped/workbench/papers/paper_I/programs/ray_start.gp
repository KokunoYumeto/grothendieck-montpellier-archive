default(parisize,500000000);
default(realprecision,80);
assert(ok,label)=if(!ok,error(Str("FAILED: ",label))); 
main()={
 my(expected=[[9],[27,27,3],vector(8,i,27)]);
 for(n=0,2,
  my(p=polcyclo(3^(n+1),y),b=bnfinit(p,1));
  assert(bnfcertify(b)==1,"full cyclotomic class/unit certification");
  assert(nfcertify(b)==[],"cyclotomic maximal order");
  assert(b.no==1,"cyclotomic class number one");
  my(r=bnrinit(b,269,1),c=r.cyc,v=select(x->x>1,vector(#c,i,3^valuation(c[i],3))));
  assert(v==expected[n+1],"ray three-primary elementary divisors");
  my(q=idealprimedec(b,3)[1],a=bnrisprincipal(r,q,0));
  assert(vector(#c,i,a[i]%3^valuation(c[i],3))==vector(#c,i,0),"prime over three has trivial three-primary ray class");
  print("LEVEL ",n," DEGREE ",poldegree(p)," RAY_THREE_PART ",v," THREE_SPLIT_SAME true");
 );
 print("RAY_START_CERTIFICATE_COMPLETE");
};
main();
quit

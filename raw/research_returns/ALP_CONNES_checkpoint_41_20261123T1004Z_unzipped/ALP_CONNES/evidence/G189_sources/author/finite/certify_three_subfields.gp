default(parisize,256000000);
default(realprecision,80);
print("PARI_VERSION=",version());
pols=[x^4-20*x^2+16,x^4-3*x^2+4,x^8+x^4+16];
{for(j=1,3,
 p=pols[j];print("FIELD=",j," POL=",p);
 b=bnfinit(p,1);
 print("SIGNATURE=",b.sign," DISC=",b.disc," CLASS_NO=",b.no," CYC=",b.cyc);
 print("CLASS_GENERATORS=",b.gen);
 ps=idealprimedec(b,2);
 print("PRIMES_2_E_F=",vector(#ps,k,[ps[k][3],ps[k][4]]));
 for(k=1,#ps,
  v=bnfisprincipal(b,ps[k],1);
  print("PRIME_HNF_",k,"=",idealhnf(b,ps[k]));
  print("PRIME_CLASS_AND_GENERATOR_",k,"=",v);
  print("EXACT_IDEAL_RELATION_",k,"=",idealmul(b,v[2],idealfactorback(b,b.gen,v[1]))==idealhnf(b,ps[k]));
 );
 print("QUOTIENT_CERTIFICATE=",bnfcertify(b,1));
 writebin(Str("/tmp/alp_recovery_trace/research/quadratic_seven_coefficient_two_bound/finite/field",j,"_bnf.bin"),b);
);}
quit;

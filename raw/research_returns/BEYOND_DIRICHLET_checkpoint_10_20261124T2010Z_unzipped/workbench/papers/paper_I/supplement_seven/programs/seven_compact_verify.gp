\\ Standalone exact verification. Run from the supplement project directory.
\\ The only input is the 7KB compact finite witness; no BNF is read.
default(parisize,200000000);
default(parisizemax,1000000000);
{
read("certificates/seven_compact_units.gp");
pp=Pol(field_polynomial_coefficients);
qq=Pol(period_polynomial_coefficients);
if(poldegree(pp)!=21 || !polisirreducible(pp),error("Bad degree21 field"));
if(poldegree(qq)!=7 || !polisirreducible(qq),error("Bad period field"));
primitive21=Mod(x,pp);
aa=Pol(alpha_numerator_coefficients)/subst(Pol(alpha_denominator_coefficients),x,primitive21);
aa=Mod(aa,pp); bb=aa-primitive21;
if(aa^3!=269 || subst(qq,x,bb)!=0,error("Field identification failed"));
z=Mod(x,polcyclo(49));hh=[1,18,19,30,31,48];
beta0=sum(j=1,6,z^hh[j]);beta1=sum(j=1,6,z^(3*hh[j]));
tau=sum(j=1,7,tau_numerator_coefficients[j]*x^(j-1))/tau_denominator;
if(subst(qq,x,beta0)!=0 || subst(tau,x,beta0)!=beta1,error("Cyclotomic period failed"));
theta_sigma=aa-subst(tau,x,bb);
if(subst(pp,x,theta_sigma)!=0,error("Invalid automorphism"));
if(subst(lift(aa),x,theta_sigma)!=aa,error("Automorphism fails to fix cubic field"));
testbeta=bb;for(j=1,7,testbeta=subst(tau,x,testbeta));
if(testbeta!=bb || subst(tau,x,bb)==bb,error("Wrong automorphism order"));
print("EXACT_FIELD_IDENTIFICATION_AND_AUTOMORPHISM=1");
nf21=nfinit(pp);
if(nfcertify(nf21)!=[] || nf21.disc!=-217083^7*7^36,error("Maximal order or discriminant failed"));
if(nf21.sign!=[7,7],error("Wrong signature"));
units=vector(13);
for(k=1,6,units[k]=sum(j=1,7,small_unit_numerators[k][j]*bb^(j-1))/small_unit_denominators[k]);
units[7]=sum(j=1,3,cubic_unit_coefficients[j]*aa^(j-1));
testbeta=bb;
for(k=8,13,
 units[k]=sum(j=1,21,eta_numerators[j]*aa^((j-1)%3)*testbeta^((j-1)\3))/eta_denominator;
 testbeta=subst(tau,x,testbeta)
);
for(k=1,13,
 if(denominator(nfalgtobasis(nf21,units[k]),1)!=1,error("Nonintegral unit"));
 if(abs(norm(units[k]))!=1,error("Nonunit norm"))
);
print("THIRTEEN_INTEGRAL_UNITS_VERIFIED=1");
rr=matrix(13,13);
for(k=1,13,
 ell=prime_witnesses[k][1]; rt=prime_witnesses[k][2]; zz=Mod(prime_witnesses[k][3],ell);
 if(!isprime(ell) || ell%7!=1 || subst(pp,x,Mod(rt,ell))!=0,error("Invalid residue field"));
 if(subst(deriv(pp),x,Mod(rt,ell))==0,error("Residue root is not simple"));
 if(zz==1 || zz^7!=1,error("Invalid seventh root"));
 for(j=1,13,
  vv=subst(lift(units[j]),x,Mod(rt,ell))^((ell-1)/7);
  found=0;for(h=0,6,if(zz^h==vv,rr[k,j]=h;found=1;break));
  if(!found,error("Missing residue logarithm"))
 );
 if(Vec(rr[k,])!=expected_residue_rows[k],error("Residue row mismatch"))
);
dd=lift(matdet(Mod(rr,7)));
if(dd!=1,error("Saturation determinant failed"));
print("RESIDUE_DETERMINANT_MOD7=",dd);
fd=fileopen("certificates/seven_compact_verify.json","w");
filewrite(fd,"{\"field_identification\":true,\"maximal_order\":true,\"unit_integrality\":true,\"unit_norms\":true,\"saturation_determinant_mod7\":1,\"BNF_completeness_assumed\":false}");
fileclose(fd);
print("SEVEN_COMPACT_CERTIFICATE_COMPLETE=1");
}

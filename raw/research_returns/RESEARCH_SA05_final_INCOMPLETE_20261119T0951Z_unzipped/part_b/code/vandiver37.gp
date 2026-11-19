\\ A finite check of the integral obstruction, not a proof for all primes.
default(parisize, 256000000);
print("PARI version: ", version());
p=37;
P=polsubcyclo(p,(p-1)/2);
print("real cyclotomic polynomial for p=37: ",P);
B=bnfinit(P,1);
print("class group data [class number, cyclic factors]: ",[B.no,B.cyc]);
cert=bnfcertify(B);
print("unconditional class-group certification: ",cert);
if(cert!=1,error("Class group not certified"));
if(B.no%p==0,error("Vandiver fails in this finite case"));
print("PASS: Vandiver at p=37, hence all odd-twist H2(Z[1/37],Z_37(r)) vanish.");
z=bernfrac(32)/32;
print("B_32/32: ",z);
print("v_37(B_32/32): ",valuation(z,37));
print("This even twist 32 has a nonzero 37-primary H2 by the even-weight order formula.");
quit;

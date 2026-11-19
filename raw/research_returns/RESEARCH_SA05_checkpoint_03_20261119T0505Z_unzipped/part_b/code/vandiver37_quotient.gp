\\ A quotient certification suffices when the computed class number is one.
\\ PARI manual bnfcertify(B,1): actual class group is a quotient of B.clgp.
default(parisize,256000000);
print("PARI version: ",version());
gettime();
p=37;P=polsubcyclo(p,(p-1)/2);
print("Real cyclotomic polynomial: ",P);
B=bnfinit(P);
print("Computed class group: ",[B.no,B.cyc]);
if(B.no!=1,error("This quotient proof requires computed class number one"));
cert=bnfcertify(B,1);
print("Unconditional quotient certification: ",cert);
if(cert!=1,error("Quotient not certified"));
print("Actual class group is a quotient of the trivial group, hence trivial.");
print("Vandiver at 37 follows unconditionally.");
z=bernfrac(32)/32;
print("B_32/32: ",z);
print("v_37(B_32/32): ",valuation(z,37));
print("Elapsed milliseconds: ",gettime());
quit;

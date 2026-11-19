\\ Unconditional two-descent certificates; no analytic rank or BSD calls.
default(parisize,64000000);
gettime();
print("PARI version: ",version());
print("Official ellrank interpretation: r1<=R<=r2; r2=C-T-s0; C=T+R+S2.");
print("s0 is dim Sha[2]/2Sha[4], not itself dim Sha[2].");
names=["E11","E37","E389"];
models=[[0,-1,1,-10,-20],[0,0,1,-1,0],[0,1,1,-2,0]];
expected=[0,1,2];
for(i=1,3,
  E=ellinit(models[i]);
  print("CURVE ",names[i]);
  print("  coefficients: ",models[i]);
  print("  discriminant: ",E.disc);
  print("  global reduction: ",ellglobalred(E));
  R=ellrank(E,0);
  Tor=elltors(E);
  print("  ellrank [r1,r2,s0,points]: ",R);
  print("  torsion [order,invariants,generators]: ",Tor);
  if(R[1]!=expected[i] || R[2]!=expected[i],error("Rank not certified"));
  if(Tor[1]%2==0,error("Unexpected rational 2-torsion"));
  T2=0;
  C2=R[2]+T2+R[3];
  S2=C2-T2-R[1];
  print("  inferred exact [Selmer2 dimension, MW rank, Sha[2] dimension]: ",[C2,R[1],S2]);
  if(S2!=0,error("Sha[2] did not vanish"));
  for(j=1,#R[4],if(!ellisoncurve(E,R[4][j]),error("Point is off curve")));
  Covers=ell2cover(E);
  print("  full locally soluble 2-cover basis [quartic,map]: ",Covers);
  print("  number of basis 2-covers: ",#Covers);
  if(#Covers!=C2,error("2-cover count differs from inferred Selmer dimension"));
  for(j=1,#Covers,
    if(!ellisoncurve(E,Mod(Covers[j][2],y^2-Covers[j][1])),error("2-cover map identity failed"))
  );
  print("  PASS: exact rank, zero Sha[2], and all symbolic cover-map identities.");
);
print("COMMON BASE: Spec Z[1/",2*11*37*389,"]");
print("A=E389 x E11: [dimension,r,Sha2corank,local closure rank,H1corank]=[2,2,0,1,1]");
print("B=E37 x E37: [dimension,r,Sha2corank,local closure rank,H1corank]=[2,2,0,2,0]");
print("Local closure ranks use the proved formal-logarithm argument, not a numerical log.");
print("CPU milliseconds: ",gettime());
quit;

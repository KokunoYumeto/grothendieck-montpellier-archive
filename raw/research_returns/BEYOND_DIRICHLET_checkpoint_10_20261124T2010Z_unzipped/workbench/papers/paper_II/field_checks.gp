\\ Exact algebraic checks for Paper II; no analytic zero certification.
\\ Run: gp -q -f field_checks.gp
default(parisize, 128000000);
V = [x^5-2*x^3+2*x^2+1, x^5+2*x^3+2*x^2-2*x+1, x^5-2*x^3+x+2, x^5-x^3-x^2+x+1];
W = [23, 19, 13, 0];
print("PARI version: ", version());
for(j=1,#V, \
  f=V[j]; \
  print("CASE ",j); \
  print("polynomial = ",f); \
  print("polynomial discriminant = ",poldisc(f)); \
  print("field discriminant = ",nfdisc(f)); \
  print("number of real roots (Sturm) = ",polsturm(f)); \
  print("Galois group = ",polgalois(f)); \
  print("factorization modulo 5 = ",factor(Mod(1,5)*f)); \
  print("factorization modulo 3 = ",factor(Mod(1,3)*f)); \
  if(W[j],print("factorization modulo ",W[j]," = ",factor(Mod(1,W[j])*f))); \
  print("5 divides polynomial discriminant: ",poldisc(f)%5==0); \
);
quit;

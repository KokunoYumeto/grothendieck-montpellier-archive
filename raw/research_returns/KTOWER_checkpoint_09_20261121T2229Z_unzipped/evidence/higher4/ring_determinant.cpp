// Exact determinant over (Z/M)[w]/(w^2-w+2), without a primality assumption.
// Input: M, dimension, then row-major pairs (a,b).  Every inverted pivot
// has certified unit norm.  Row elimination is independent of the archived
// Python verifier's column elimination.
#include <gmpxx.h>
#include <iostream>
#include <vector>
#include <stdexcept>
using Z=mpz_class;
struct R { Z a,b; };
Z M;
Z red(const Z& x) { Z y; mpz_mod(y.get_mpz_t(),x.get_mpz_t(),M.get_mpz_t()); return y; }
R mul(const R& x,const R& y) {
  return {red(x.a*y.a-2*x.b*y.b),red(x.a*y.b+x.b*y.a+x.b*y.b)};
}
R sub(const R& x,const R& y) { return {red(x.a-y.a),red(x.b-y.b)}; }
Z norm(const R& x) { return red(x.a*x.a+x.a*x.b+2*x.b*x.b); }
bool unit(const R& x) { Z g; Z n=norm(x);mpz_gcd(g.get_mpz_t(),n.get_mpz_t(),M.get_mpz_t());return g==1; }
R inverse(const R& x) {
  Z n=norm(x),t;
  if(!mpz_invert(t.get_mpz_t(),n.get_mpz_t(),M.get_mpz_t()))throw std::runtime_error("nonunit");
  return {red((x.a+x.b)*t),red(-x.b*t)};
}
int main() {
 try {
  unsigned n; if(!(std::cin>>M>>n)||M<2)throw std::runtime_error("bad header");
  std::vector<R> A(size_t(n)*n);
  for(auto& x:A){if(!(std::cin>>x.a>>x.b))throw std::runtime_error("short matrix");x.a=red(x.a);x.b=red(x.b);}
  std::string extra;if(std::cin>>extra)throw std::runtime_error("trailing input");
  R det{1,0};unsigned pivots=0;
  for(unsigned k=0;k<n;k++){
    if(k+1==n){det=mul(det,A[size_t(k)*n+k]);break;}
    unsigned p=k;while(p<n&&!unit(A[size_t(p)*n+k]))p++;
    if(p==n)throw std::runtime_error("unit pivot unavailable");
    if(p!=k){for(unsigned j=k;j<n;j++)std::swap(A[size_t(p)*n+j],A[size_t(k)*n+j]);det={red(-det.a),red(-det.b)};}
    R pivot=A[size_t(k)*n+k],inv=inverse(pivot);det=mul(det,pivot);pivots++;
    for(unsigned i=k+1;i<n;i++){
      R factor=mul(A[size_t(i)*n+k],inv);
      for(unsigned j=k+1;j<n;j++)A[size_t(i)*n+j]=sub(A[size_t(i)*n+j],mul(factor,A[size_t(k)*n+j]));
      A[size_t(i)*n+k]={0,0};
    }
  }
  std::cout<<det.a<<" "<<det.b<<" "<<pivots<<"\n";
 }catch(const std::exception& e){std::cerr<<e.what()<<"\n";return 2;}
}

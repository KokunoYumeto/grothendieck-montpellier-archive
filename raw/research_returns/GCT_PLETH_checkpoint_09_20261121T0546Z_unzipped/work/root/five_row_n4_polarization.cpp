#include <array>
#include <cstdint>
#include <iostream>
#include <algorithm>
// Exact coefficient of prod_{i=1}^4 prod_{j=1}^5 t_ij in
// p1 p4 p12 p34 p234 p123 det^2, at X_i=sum_j t_ij v_j,
// with v_j=(1,j,j^2,j^3), j=1,...,5, over F_1000003.
// Total degree20 makes the Boolean inclusion-exclusion sum exact.
using Row=std::array<int64_t,4>;
int64_t minor2(const Row&a,const Row&b){return a[0]*b[1]-a[1]*b[0];}
int64_t minor3(const Row&a,const Row&b,const Row&c){
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
}
int64_t determinant(const std::array<Row,4>&x){
 std::array<int,4> p={0,1,2,3};int64_t out=0;
 do {int inv=0;for(int i=0;i<4;++i)for(int j=i+1;j<4;++j)inv+=p[i]>p[j];
     int64_t v=1;for(int i=0;i<4;++i)v*=x[i][p[i]];out+=(inv%2?-v:v);
 }while(std::next_permutation(p.begin(),p.end()));return out;
}
const int64_t MOD=1000003;
int64_t norm(int64_t v){v%=MOD;if(v<0)v+=MOD;return v;}
int main(){
 std::array<Row,32> rows;std::array<int,32> signs;
 for(int s=0;s<32;++s){for(int j=0;j<4;++j){rows[s][j]=0;for(int q=1;q<=5;++q)if(s&(1<<(q-1))){int64_t power=1;for(int u=0;u<j;++u)power*=q;rows[s][j]+=power;}}signs[s]=(__builtin_popcount((unsigned)s)%2?-1:1);}
 int64_t total=0,maxabs=0;uint64_t terms=0,nonzero=0;
 for(int a=0;a<32;++a)for(int b=0;b<32;++b)for(int c=0;c<32;++c)for(int d=0;d<32;++d){
  ++terms;std::array<Row,4>x={rows[a],rows[b],rows[c],rows[d]};
  int64_t v=1;for(int64_t factor: {x[0][0],x[3][0],minor2(x[0],x[1]),minor2(x[2],x[3]),minor3(x[1],x[2],x[3]),minor3(x[0],x[1],x[2])})v=norm(v*norm(factor));
  if(v){int64_t det=norm(determinant(x));v=norm(norm(v*det)*det);}
  if(v)++nonzero;maxabs=std::max(maxabs,std::abs(v));total=norm(total+signs[a]*signs[b]*signs[c]*signs[d]*v);
 }
 std::cout<<"terms "<<terms<<" nonzero "<<nonzero<<" max_abs_summand "<<maxabs<<" prime "<<MOD<<" coefficient_mod_prime "<<total<<"\n";
}

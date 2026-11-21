// Exact F_q[omega]/(omega^2-omega+2) arithmetic for the full Schur test.
// Input contains the complete kernel and exact rational frame numerators.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using U=std::uint64_t;
using W=__uint128_t;
constexpr U Q=25078104767246023ULL;
U add(U a,U b){U c=a+b;return c>=Q?c-Q:c;}
U neg(U a){return a?Q-a:0;}
U sub(U a,U b){return add(a,neg(b));}
U mul(U a,U b){return U(W(a)*b%Q);}
U power(U a,U b){U r=1;for(;b;b>>=1,a=mul(a,a))if(b&1)r=mul(r,a);return r;}
U inv(U a){assert(a);U r=power(a,Q-2);assert(mul(a,r)==1);return r;}
U signed_mod(std::int64_t a){return a>=0?U(a)%Q:neg(U(-a)%Q);}
struct F{
 U a,b;
 F(U x=0,U y=0):a(x),b(y){}
 bool zero()const{return a==0&&b==0;}
 bool operator==(const F&x)const{return a==x.a&&b==x.b;}
};
F plus(F x,F y){return {add(x.a,y.a),add(x.b,y.b)};}
F minus(F x,F y){return {sub(x.a,y.a),sub(x.b,y.b)};}
F scale(F x,U a){return {mul(x.a,a),mul(x.b,a)};}
F times(F x,F y){
 U bd=mul(x.b,y.b);
 return {sub(mul(x.a,y.a),add(bd,bd)),
         add(add(mul(x.a,y.b),mul(x.b,y.a)),bd)};
}
F conjugate(F x){return {add(x.a,x.b),neg(x.b)};}
F inverse(F x){
 U n=add(add(mul(x.a,x.a),mul(x.a,x.b)),add(mul(x.b,x.b),mul(x.b,x.b)));
 assert(n);return scale(conjugate(x),inv(n));
}
using Mon=std::array<int,6>;
using Orbit=std::vector<Mon>;
using Vec=std::array<F,3>;
using Frame=std::array<Vec,3>; // columns
using Matrix=std::vector<std::vector<F>>;
int K,D,N;
std::vector<Orbit> orbits;
std::vector<std::vector<std::pair<int,U>>> basis;

std::vector<F> evaluate(Vec z,Vec w){
 std::vector<std::vector<F>> zp(3),wp(3);
 for(int i=0;i<3;i++){
  zp[i].assign(K+1,F(1));wp[i].assign(K+1,F(1));
  for(int n=1;n<=K;n++){zp[i][n]=times(zp[i][n-1],z[i]);wp[i][n]=times(wp[i][n-1],w[i]);}
 }
 std::vector<std::vector<F>> pairpow(3,std::vector<F>((K+1)*(K+1)));
 for(int i=0;i<3;i++)for(int a=0;a<=K;a++)for(int b=0;b<=K;b++)
  pairpow[i][a*(K+1)+b]=times(zp[i][a],wp[i][b]);
 std::vector<F> values(N);
 for(int i=0;i<N;i++)for(auto m:orbits[i]){
  F v=times(pairpow[0][m[0]*(K+1)+m[1]],pairpow[1][m[2]*(K+1)+m[3]]);
  values[i]=plus(values[i],times(v,pairpow[2][m[4]*(K+1)+m[5]]));
 }
 std::vector<F> answer(D);
 for(int j=0;j<D;j++)for(auto [i,c]:basis[j])answer[j]=plus(answer[j],scale(values[i],c));
 return answer;
}
std::vector<F> transformed_sum(Vec z,Vec w,const std::vector<Frame>&frames){
 std::vector<F> total(D);
 for(const auto&v:frames){
  Vec zz{},ww{};
  for(int j=0;j<3;j++)for(int i=0;i<3;i++){
   zz[j]=plus(zz[j],times(conjugate(v[j][i]),z[i]));
   ww[j]=plus(ww[j],times(v[j][i],w[i]));
  }
  auto row=evaluate(zz,ww);
  for(int j=0;j<D;j++)total[j]=plus(total[j],row[j]);
 }
 return total;
}
F determinant(Matrix a){
 F det(1);
 for(int j=0;j<D;j++){
  int pivot=j;while(pivot<D&&a[pivot][j].zero())pivot++;
  if(pivot==D)return F();
  if(pivot!=j){std::swap(a[pivot],a[j]);det=scale(det,Q-1);}
  F value=a[j][j];det=times(det,value);
  F reciprocal=inverse(value);
  for(int i=j+1;i<D;i++){
   F t=times(a[i][j],reciprocal);
   for(int c=j+1;c<D;c++)a[i][c]=minus(a[i][c],times(t,a[j][c]));
   a[i][j]=F();
  }
 }
 return det;
}
Matrix solve_rational(Matrix a,Matrix b){
 for(int j=0;j<D;j++){
  int pivot=j;while(pivot<D&&a[pivot][j].zero())pivot++;
  assert(pivot<D);std::swap(a[pivot],a[j]);std::swap(b[pivot],b[j]);
  assert(a[j][j].b==0);U reciprocal=inv(a[j][j].a);
  for(int c=j;c<D;c++)a[j][c]=scale(a[j][c],reciprocal);
  for(int c=0;c<D;c++)b[j][c]=scale(b[j][c],reciprocal);
  for(int i=0;i<D;i++)if(i!=j&&!a[i][j].zero()){
   assert(a[i][j].b==0);U t=a[i][j].a;
   for(int c=j;c<D;c++)a[i][c]=minus(a[i][c],scale(a[j][c],t));
   for(int c=0;c<D;c++)b[i][c]=minus(b[i][c],scale(b[j][c],t));
  }
 }
 for(int i=0;i<D;i++)for(int j=0;j<D;j++)assert(a[i][j]==F(i==j));
 return b;
}
void write_matrix(std::ostream&o,const Matrix&a){
 o<<"[";for(std::size_t i=0;i<a.size();i++){
  if(i)o<<",";o<<"[";
  for(std::size_t j=0;j<a[i].size();j++){if(j)o<<",";o<<"["<<a[i][j].a<<","<<a[i][j].b<<"]";}
  o<<"]";
 }o<<"]";
}
int main(int argc,char**argv){
 assert(argc==3);auto start=std::chrono::steady_clock::now();
 assert(power(Q-7,(Q-1)/2)==Q-1); // The coefficient algebra is a field.
 std::ifstream in(argv[1]);assert(in);U q;in>>q>>K>>N>>D;assert(q==Q);
 for(int i=0;i<N;i++){
  std::array<std::pair<int,int>,3> pairs;
  for(auto&x:pairs)in>>x.first>>x.second;
  std::sort(pairs.begin(),pairs.end());Orbit orbit;
  do{Mon m;for(int j=0;j<3;j++){m[2*j]=pairs[j].first;m[2*j+1]=pairs[j].second;}orbit.push_back(m);}
  while(std::next_permutation(pairs.begin(),pairs.end()));
  orbits.push_back(orbit);
 }
 for(int j=0;j<D;j++){
  int t;in>>t;std::vector<std::pair<int,U>> column(t);
  for(auto&x:column){in>>x.first>>x.second;assert(x.first<N&&x.second<Q);}
  basis.push_back(column);
 }
 int count;in>>count;assert(count==D+2);
 std::vector<std::pair<Vec,Vec>> points(count);
 for(auto&point:points)for(auto*row:{&point.first,&point.second})for(F&x:*row){in>>x.a;assert(x.a<Q);}
 std::vector<Frame> fs[2];
 for(int t=0;t<2;t++){
  int n;in>>n;assert(n==(t?7:6));fs[t].resize(n);
  for(auto&frame:fs[t])for(auto&column:frame)for(auto&x:column){
   std::int64_t a,b;in>>a>>b;x=F(signed_mod(a),signed_mod(b));
  }
 }
 assert(in);std::string extra;assert(!(in>>extra));
 U e=K+1,E=add(add(1,power(2,e)),power(2,2*e));
 assert(E);
 Matrix a(count),b2(count),b4(count),schur(count);
 for(int r=0;r<count;r++){
  auto[z,w]=points[r];a[r]=evaluate(z,w);
  b2[r]=transformed_sum(z,w,fs[0]);b4[r]=transformed_sum(z,w,fs[1]);
  schur[r].resize(D);
  for(int j=0;j<D;j++){
   assert(a[r][j].b==0);
   schur[r][j]=minus(minus(scale(a[r][j],mul(E,E)),scale(b2[r][j],E)),b4[r][j]);
  }
  if(r%25==0)std::cerr<<"row "<<r<<"/"<<count<<"\n";
 }
 Matrix square_a(a.begin(),a.begin()+D),square_s(schur.begin(),schur.begin()+D);
 F da=determinant(square_a),ds=determinant(square_s);assert(!da.zero());
 Matrix operator_matrix=solve_rational(square_a,square_s);
 // Additional identifying-independent evaluations verify that the full
 // correspondence preserving W1 has the recovered operator matrix.
 for(int r=D;r<count;r++)for(int j=0;j<D;j++){
  F value;for(int i=0;i<D;i++)value=plus(value,times(a[r][i],operator_matrix[i][j]));
  assert(value==schur[r][j]);
 }
 F dop=times(ds,inverse(da));
 std::ofstream out(argv[2]);assert(out);
 out<<"{\"status\":\"EXACT modular Schur calculation completed\","
    <<"\"q\":"<<Q<<",\"k\":"<<K<<",\"dimension\":"<<D
    <<",\"comparison_point\":"<<E
    <<",\"det_evaluation\":["<<da.a<<","<<da.b<<"]"
    <<",\"det_schur_evaluations\":["<<ds.a<<","<<ds.b<<"]"
    <<",\"det_schur_operator\":["<<dop.a<<","<<dop.b<<"]"
    <<",\"nonzero\":"<<(dop.zero()?"false":"true")
    <<",\"evaluation_matrix\":";write_matrix(out,a);
 out<<",\"norm2_transformed_evaluations\":";write_matrix(out,b2);
 out<<",\"norm4_transformed_evaluations\":";write_matrix(out,b4);
 out<<",\"schur_operator\":";write_matrix(out,operator_matrix);
 auto elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 out<<",\"two_extra_points_pass\":true,\"elapsed_seconds\":"<<elapsed<<"}\n";
 std::cout<<"k "<<K<<" dimension "<<D<<" detA "<<da.a<<","<<da.b
          <<" detSchur "<<dop.a<<","<<dop.b<<" elapsed "<<elapsed<<"\n";
}

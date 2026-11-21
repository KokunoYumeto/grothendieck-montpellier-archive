#include <array>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>
using Q=std::array<long long,4>; // 2 times coordinates in 1,i,j,k
long long norm(const Q&a){long long s=0;for(auto x:a)s+=x*x;assert(s%4==0);return s/4;}
Q bar(Q a){for(int k=1;k<4;k++)a[k]=-a[k];return a;}
Q mul(const Q&a,const Q&b){Q c={a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0]};for(auto &x:c){assert(x%2==0);x/=2;}return c;}
std::array<long long,2> kp(const Q&a){return {3*a[0],a[1]+a[2]+a[3]};} // /6 in basis 1,s, s^2=-3
std::array<long long,2> kmul(std::array<long long,2>a,std::array<long long,2>b){return {a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0]};}
long long determinant(const Q&a,const Q&b,const Q&c,const Q&d){return norm(a)*norm(d)+norm(b)*norm(c)-mul(mul(mul(a,bar(c)),d),bar(b))[0];}
long long znumerator(const Q&a,const Q&b,const Q&c,const Q&d){auto x=kmul(kp(a),kp(d)),y=kmul(kp(b),kp(c));long long u=x[0]-y[0],v=x[1]-y[1];return u*u+3*v*v;}
void printq(const Q&a){std::cout<<"("<<a[0]<<","<<a[1]<<","<<a[2]<<","<<a[3]<<")/2";}
int main(){
 std::array<std::vector<Q>,6> O;
 for(int a=-4;a<=4;a++)for(int b=-4;b<=4;b++)for(int c=-4;c<=4;c++)for(int d=-4;d<=4;d++){
   if(((a-b)%2)||((a-c)%2)||((a-d)%2))continue;
   Q q={a,b,c,d};long long s=a*a+b*b+c*c+d*d;if(s>20||s%4)continue;O[s/4].push_back(q);
 }
 for(int n=0;n<=5;n++)std::cout<<"Hurwitz norm "<<n<<": "<<O[n].size()<<" elements\n";
 long long counts[3]={0,0,0},maximum[3]={0,0,0};std::array<Q,4> argmax[3];
 for(int na=0;na<=5;na++)for(int nb=0;nb<=5-na;nb++)for(int nc=0;nc<=5-na-nb;nc++)for(int nd=0;nd<=5-na-nb-nc;nd++){
  int T=na+nb+nc+nd;
  for(auto a:O[na])for(auto b:O[nb])for(auto c:O[nc])for(auto d:O[nd]){
   long long deg=determinant(a,b,c,d);
   assert(deg>=0);
   if(deg<1||deg>2||T+deg>6)continue; // graph degree 2(1+deg+T)<=14
   counts[deg]++;long long z=znumerator(a,b,c,d);
   if(z>maximum[deg]){maximum[deg]=z;argmax[deg]={a,b,c,d};}
  }
 }
 for(int deg=1;deg<=2;deg++){
  std::cout<<"degree "<<deg<<"; count "<<counts[deg]<<"; max |z|^2="<<maximum[deg]<<"/1296="<<double(maximum[deg])/1296<<"\n";
  for(auto q:argmax[deg]){printq(q);std::cout<<" ";}std::cout<<"\n";
 }
}

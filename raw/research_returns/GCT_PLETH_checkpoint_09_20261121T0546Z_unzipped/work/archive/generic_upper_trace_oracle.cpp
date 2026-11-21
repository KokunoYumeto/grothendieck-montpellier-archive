#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using I=__int128_t;
constexpr int CAP=400;
const int FULL[7]={11111,2111,221,311,32,41,5};
const int SINGLE[7]={1111,211,22,31,0,4,0};
const int FIXPAIR[7]={111,21,0,3,0,0,0};
const int SWAPPAIR[7]={0,111,21,0,3,0,0};
const int NFIX[7]={5,3,1,2,0,1,0};
const int NPAIR[7]={10,3,0,1,0,0,0};
const int NSWAP[7]={0,1,2,0,1,0,0};
const std::vector<int> KEYS={11111,2111,221,311,32,41,5,1111,211,22,31,4,111,21,3};
std::array<std::array<I,CAP+1>,15> TABLE;
int index_of(int key){return int(std::find(KEYS.begin(),KEYS.end(),key)-KEYS.begin());}
I hc(int key,int n){
  if(n<0)return 0;
  assert(n<=CAP);
  return TABLE[index_of(key)][n];
}
I raw(int key,int n){
  switch(key){
  case 11111:return I(n+1)*(n+2)*(n+3)/6;
  case 2111:return I(n/2+1)*((n+1)/2+1);
  case 221:return n%2?0:n/2+1;
  case 311:return n/3+1;
  case 32:{int v[6]={1,-1,1,0,0,0};return v[n%6];}
  case 41:return n%4==0;
  case 5:{int v[5]={1,-1,0,0,0};return v[n%5];}
  case 1111:return I(n+1)*(n+2)/2;
  case 211:return n/2+1;
  case 22:return (n%2?-1:1)*(n/2+1);
  case 31:return n%3==0;
  case 4:{int v[4]={1,-1,0,0};return v[n%4];}
  case 111:return n+1;
  case 21:return n%2==0;
  case 3:{int v[3]={1,-1,0};return v[n%3];}
  }
  assert(false);return 0;
}
I skew(int key,std::array<int,3> lambda,std::array<int,3> rho){
  I a[3][3];
  for(int i=0;i<3;i++)for(int j=0;j<3;j++)
    a[i][j]=hc(key,lambda[i]-rho[j]-i+j);
  return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]);
}
I trace(int g,int X,int B,int K,int C){
  const int c=C,k=C+K+4,b=C+3*K+10+B,a=b+X;
  assert(X>=0&&B>=0&&K>=0&&C>=0&&k<=100&&a+c+2<=CAP);
  std::array<int,3> alpha={a+c,b+c,c};
  I answer=skew(FULL[g],alpha,{0,0,0});
  if(NFIX[g]){
    I single=0;
    for(int i=0;i<=std::min(X,k-1);i++)
      for(int j=0;j<=std::min(b,k-1-i);j++)
        for(int l=0;l<=std::min(c,k-1-i-j);l++)
          single+=skew(SINGLE[g],{a+c-i,b+c-j,c-l},{0,0,0});
    answer-=NFIX[g]*single;
  }
  if(NPAIR[g]){
    I pair=0;
    for(int p=0;p<=2*(k-1);p++)
      for(int q=0;q<=std::min({p,k-1,2*(k-1)-p});q++){
        int lo=std::max(q,p+q-k+1),hi=std::min(k-1,p);
        if(lo<=hi)pair+=(hi-lo+1)*skew(FIXPAIR[g],alpha,{p,q,0});
      }
    answer+=NPAIR[g]*pair;
  }
  if(NSWAP[g]){
    I pair=0;
    for(int r=0;r<k;r++)for(int q=0;q<=r;q++)
      pair+=(q%2?-1:1)*skew(SWAPPAIR[g],alpha,{2*r-q,q,0});
    answer-=NSWAP[g]*pair;
  }
  return answer;
}
std::string decimal(I n){
  if(n==0)return "0";
  bool negative=n<0;if(negative)n=-n;std::string result;
  while(n){result+=char('0'+n%10);n/=10;}
  if(negative)result+='-';std::reverse(result.begin(),result.end());return result;
}
int main(){
  for(int i=0;i<int(KEYS.size());i++)for(int n=0;n<=CAP;n++)TABLE[i][n]=raw(KEYS[i],n);
  int g,X,B,K,C;
  while(std::cin>>g>>X>>B>>K>>C)std::cout<<decimal(trace(g,X,B,K,C))<<"\n";
}

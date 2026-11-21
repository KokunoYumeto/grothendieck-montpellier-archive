#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>
using ll=long long;
using Mat=std::vector<std::vector<ll>>;
ll det(Mat a){
  int n=a.size(); ll prev=1; int sign=1;
  if(n==1)return a[0][0];
  for(int k=0;k<n-1;k++){
    int p=k;while(p<n&&a[p][k]==0)p++;
    if(p==n)return 0;
    if(p!=k){std::swap(a[p],a[k]);sign=-sign;}
    ll pivot=a[k][k];
    for(int i=k+1;i<n;i++)for(int j=k+1;j<n;j++)
      a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])/prev;
    for(int i=k+1;i<n;i++)a[i][k]=0;
    prev=pivot;
  }
  return sign*a[n-1][n-1];
}
int v2(ll a){if(a==0)return 1000;if(a<0)a=-a;return __builtin_ctzll(a);}
bool has111(const Mat &a){int n=a.size();for(int j=0;j<n;j++){int c=0;for(int i=0;i<n;i++)if(a[i][j])c++;if(c==3)return true;}return false;}
bool test(const Mat&a, long long &counter){
  counter++;int n=a.size(); if(!has111(a))return false;
  ll D=det(a);if(!D||v2(D)<n-1)return false;
  int mv=v2(D);std::vector<ll> nums;bool positive=true;
  for(int j=0;j<n;j++){Mat b=a;for(int i=0;i<n;i++)b[i][j]=1;ll x=det(b);nums.push_back(x);mv=std::min(mv,v2(x));if((x>0)!=(D>0)&&x!=0)positive=false;}
  if(v2(D)-mv<n-1)return false;
  bool nonadjacent=true;
  for(int j=0;j<n;j++)for(int k=0;k<j;k++){int l1=0;for(int i=0;i<n;i++)l1+=std::abs(a[i][j]-a[i][k]);if(l1==2)nonadjacent=false;}
  std::cout<<"CANDIDATE n="<<n<<" det="<<D<<" determinant_class_2valuation="<<v2(D)-mv<<" positive="<<positive<<" nonadjacent="<<nonadjacent<<"\n";
  for(auto&r:a){for(auto x:r)std::cout<<x<<' ';std::cout<<'\n';}
  std::cout<<"Cramer numerators:";for(auto x:nums)std::cout<<' '<<x;std::cout<<"\n"<<std::flush;
  return positive&&nonadjacent;
}
int main(){std::mt19937_64 rng(20261121);long long count=0,candidates=0;
  for(int n=3;n<=14;n++){
    std::vector<std::vector<ll>> mon;
    for(int i=0;i<n;i++)for(int j=i;j<n;j++)for(int k=j;k<n;k++){
      std::vector<ll> v(n);v[i]++;v[j]++;v[k]++;mon.push_back(v);
    }
    Mat chain(n,std::vector<ll>(n));for(int j=0;j<n-1;j++){chain[j][j]=2;chain[j+1][j]=1;}chain[n-1][n-1]=3;
    for(int c=0;c<n;c++)for(auto &v:mon){auto a=chain;for(int i=0;i<n;i++)a[i][c]=v[i];if(test(a,count))return 0;}
    for(int rep=0;rep<30000;rep++){
      auto a=chain;int mutations=2+rep%4;
      for(int z=0;z<mutations;z++){int c=rng()%n;auto&v=mon[rng()%mon.size()];for(int i=0;i<n;i++)a[i][c]=v[i];}
      if(test(a,count))return 0;
    }
    std::cout<<"completed n="<<n<<" cumulative_supports="<<count<<"\n"<<std::flush;
  }
}

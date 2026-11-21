#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
using Weight=array<int,6>;
int main(){
 const int r=6,b=5,total=30;
 vector<unsigned>monomials;Weight w{};
 function<void(int,int)>compositions=[&](int i,int left){
  if(i==5){w[i]=left;unsigned key=0;for(int j=0;j<5;j++)key+=w[j]<<(5*j);monomials.push_back(key);return;}
  for(int x=0;x<=left;x++){w[i]=x;compositions(i+1,left-x);}
 };
 compositions(0,b);assert(monomials.size()==252);
 vector<unordered_map<unsigned,long long>>h(7);h[0][0]=1;
 for(int j=1;j<=6;j++)h[j].reserve(350000);
 for(unsigned key:monomials)
  for(int j=1;j<=r;j++)
   for(const auto&kv:h[j-1])h[j][key+kv.first]+=kv.second;
 // Independent Newton recurrence, compared on every monomial weight.
 vector<unordered_map<unsigned,long long>> hn(7);hn[0][0]=1;
 for(int j=1;j<=6;j++){
  hn[j].reserve(350000);
  for(int k=1;k<=j;k++)
   for(const auto&kv:hn[j-k])
    for(unsigned key:monomials)hn[j][kv.first+k*key]+=kv.second;
  for(auto&kv:hn[j]){assert(kv.second%j==0);kv.second/=j;}
  assert(hn[j]==h[j]);
 }
 vector<pair<Weight,int>>perms;Weight p{0,1,2,3,4,5};
 do{int sg=1;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)if(p[i]>p[j])sg=-sg;perms.push_back({p,sg});}while(next_permutation(p.begin(),p.end()));
 ofstream out("work/rectangular/POLARIZATION_R6_L1_B5_SOURCE.tsv");
 out<<"partition\tsource_multiplicity\tGL6_dimension\n";
 int blocks=0,maxmult=0;long long summult=0,dimension=0;Weight lam{};
 function<void(int,int,int)>visit=[&](int i,int left,int cap){
  if(i==6){
   if(left)return;long long mult=0;
   for(auto&ps:perms){
    unsigned key=0;bool good=true;
    for(int j=0;j<6;j++){
     int x=lam[j]+ps.first[j]-j;
     if(x<0||x>30){good=false;break;}
     if(j<5)key+=x<<(5*j);
    }
    if(good){auto it=h[6].find(key);if(it!=h[6].end())mult+=ps.second*it->second;}
   }
   assert(mult>=0);
   if(mult){
    __int128 num=1;
    for(int j=0;j<6;j++)for(int k=j+1;k<6;k++)num*=lam[j]-lam[k]+k-j;
    assert(num%34560==0);long long dim=num/34560;
    for(int j=0;j<6;j++)out<<(j?",":"")<<lam[j];
    out<<"\t"<<mult<<"\t"<<dim<<"\n";
    blocks++;summult+=mult;maxmult=max(maxmult,(int)mult);dimension+=mult*dim;
   }
   return;
  }
  for(int x=min(cap,left);x>=0;x--){if(x*(6-i)<left)break;lam[i]=x;visit(i+1,left-x,x);}
 };
 visit(0,total,total);
 long long weightdim=0;for(auto&kv:h[6])weightdim+=kv.second;
 assert(weightdim==dimension);
 __int128 expected=1;for(int i=1;i<=6;i++)expected=expected*(251+i)/i;
 assert(expected==dimension);
 cout<<"r6 L1 b5 source: constituents="<<blocks<<" highest_dimension="<<summult<<" max_multiplicity="<<maxmult<<" representation_dimension="<<dimension<<" weights="<<h[6].size()<<" independent_Newton_product_comparison=PASS\n";
}

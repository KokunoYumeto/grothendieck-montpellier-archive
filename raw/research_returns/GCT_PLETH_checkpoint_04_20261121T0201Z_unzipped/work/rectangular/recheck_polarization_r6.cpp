#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
const int P=1000003;
using Exp=array<unsigned char,63>;
struct Term{Exp e;int c;};
int mod(long long x){x%=P;return x<0?x+P:x;}
int inv(int a){int r=1,k=P-2;for(;k;k>>=1,a=mod(1LL*a*a))if(k&1)r=mod(1LL*r*a);return r;}
int trace_det(vector<vector<int>> A){
 int n=A.size();if(!n)return 1;vector<int>tr(n+1),e(n+1);e[0]=1;auto B=A;
 for(int k=1;k<=n;k++){
  long long trace=0;for(int i=0;i<n;i++)trace+=B[i][i];tr[k]=mod(trace);
  long long sum=0;for(int i=1;i<=k;i++)sum+=(i%2?1:-1)*1LL*e[k-i]*tr[i];e[k]=mod(1LL*mod(sum)*inv(k));
  if(k<n){
   vector<vector<int>>C(n,vector<int>(n));
   for(int i=0;i<n;i++)for(int j=0;j<n;j++){long long value=0;for(int t=0;t<n;t++)value+=1LL*B[i][t]*A[t][j];C[i][j]=mod(value);}
   B.swap(C);
  }
 }
 return e[n];
}
vector<vector<int>>subsets;
vector<array<array<int,7>,63>>forms;
vector<Term> average(Exp seed){
 map<Exp,int>terms;array<int,6>p{0,1,2,3,4,5};int permutations=0;
 do{
  Exp target{};int sg=1;
  for(int z=0;z<63;z++)if(seed[z]){
   vector<int>I;for(int i:subsets[z])I.push_back(p[i]);
   int inversions=0;for(int i=0;i<(int)I.size();i++)for(int j=i+1;j<(int)I.size();j++)inversions+=I[i]>I[j];
   if(inversions*seed[z]%2)sg=-sg;
   sort(I.begin(),I.end());
   int index=find(subsets.begin(),subsets.end(),I)-subsets.begin();assert(index<63);
   target[index]+=seed[z];
  }
  terms[target]+=sg;permutations++;
 }while(next_permutation(p.begin(),p.end()));
 assert(permutations==720);
 int divisor=0;for(auto&kv:terms)divisor=gcd(divisor,abs(kv.second));assert(divisor);
 for(auto&kv:terms)if(kv.second){if(kv.second<0)divisor=-divisor;break;}
 vector<Term>result;for(auto&kv:terms)if(kv.second)result.push_back({kv.first,kv.second/divisor});
 return result;
}
int coefficient(const Exp&e,int point){
 array<int,64>dp{};dp[0]=1;
 for(int z=62;z>=0;z--)for(int repeat=0;repeat<e[z];repeat++){
  auto&f=forms[point][z];
  for(int S=63;S>=0;S--){
   long long value=1LL*f[0]*dp[S];
   for(int j:subsets[z])if(S>>j&1)value+=1LL*f[j+1]*dp[S^(1<<j)];
   dp[S]=mod(value);
  }
 }
 return dp[63];
}
int main(int argc,char**argv){
 assert(argc==2);for(int i=2;i*i<=P;i++)assert(P%i);
 ifstream in(argv[1]);int r,L,b,blocks,prime,np;in>>r>>L>>b>>blocks>>prime>>np;assert(r==6&&L==1&&b==5&&prime==P);
 for(int mask=1;mask<64;mask++){vector<int>I;for(int j=0;j<6;j++)if(mask>>j&1)I.push_back(j);subsets.push_back(I);}
 sort(subsets.begin(),subsets.end(),[](auto&a,auto&b){return a.size()!=b.size()?a.size()<b.size():a<b;});
 for(int point=0;point<np;point++){
  array<array<int,6>,6>X;array<int,6>x;for(auto&row:X)for(int&v:row)in>>v;for(int&v:x)in>>v;
  array<array<int,7>,63>fs{};
  for(int z=0;z<63;z++){
   auto&I=subsets[z];int h=I.size();vector<vector<int>>A(h,vector<int>(h));
   for(int i=0;i<h;i++)for(int j=0;j<h;j++)A[i][j]=X[i][I[j]];
   fs[z][0]=trace_det(A);
   for(int j=0;j<h;j++){auto C=A;for(int i=0;i<h;i++)C[i][j]=x[i];fs[z][I[j]+1]=trace_det(C);}
  }
  forms.push_back(fs);
 }
 long long entries=0,vectors=0,evaluations=0;
 for(int block=0;block<blocks;block++){
  array<int,6>lam;for(int&v:lam)in>>v;int m,rank;in>>m>>rank;assert(m==rank);
  vector<vector<Term>>polynomials;
  for(int j=0;j<m;j++){
   int oldindex;in>>oldindex;Exp seed{};for(auto&v:seed){int x;in>>x;assert(x>=0&&x<=5);v=x;}
   array<int,6>weight{},degree{};
   for(int z=0;z<63;z++){for(int k=0;k<(int)subsets[z].size();k++)weight[k]+=seed[z];for(int k:subsets[z])degree[k]+=seed[z];}
   assert(weight==lam);for(int d:degree)assert(d==5);
   polynomials.push_back(average(seed));
  }
  vector<int>rows(m);for(int&r:rows)in>>r;
  vector<vector<int>>matrix(m,vector<int>(m));for(auto&row:matrix)for(int&v:row)in>>v;
  int determinant;in>>determinant;assert(determinant&&trace_det(matrix)==determinant);
  for(int i=0;i<m;i++){
   map<Exp,int>cache;
   for(int j=0;j<m;j++){
    long long value=0;
    for(auto&t:polynomials[j]){
     auto it=cache.find(t.e);int c;
     if(it==cache.end()){c=coefficient(t.e,rows[i]);cache[t.e]=c;evaluations++;}else c=it->second;
     value+=1LL*t.c*c;
    }
    assert(mod(value)==matrix[i][j]);entries++;
   }
  }
  vectors+=m;
 }
 assert(in);cout<<"PASS independent direct Taylor/Newton determinants: blocks="<<blocks<<" vectors="<<vectors<<" entries="<<entries<<" Taylor_evaluations="<<evaluations<<"\n";
}

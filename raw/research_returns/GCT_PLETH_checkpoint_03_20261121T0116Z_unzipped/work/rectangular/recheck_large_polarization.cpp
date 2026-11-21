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
using Exponents=array<int,15>;
struct Term{int c;Exponents e;};
int mod(long long x){x%=P;return x<0?x+P:x;}
int inv(int a){int r=1,k=P-2;for(;k;k>>=1,a=mod(1LL*a*a))if(k&1)r=mod(1LL*r*a);return r;}
// Determinant from power traces and Newton identities, independently of elimination.
int trace_det(vector<vector<int>> A){
 int n=A.size();if(!n)return 1;
 vector<int> tr(n+1),e(n+1);e[0]=1;
 auto B=A;
 for(int k=1;k<=n;k++){
  long long trace=0;for(int i=0;i<n;i++)trace+=B[i][i];tr[k]=mod(trace);
  long long sum=0;for(int i=1;i<=k;i++)sum+=(i%2?1:-1)*1LL*e[k-i]*tr[i];
  e[k]=mod(1LL*mod(sum)*inv(k));
  if(k<n){
   vector<vector<int>> C(n,vector<int>(n));
   for(int i=0;i<n;i++)for(int j=0;j<n;j++){
    long long value=0;for(int t=0;t<n;t++)value+=1LL*B[i][t]*A[t][j];
    C[i][j]=mod(value);
   }
   B.swap(C);
  }
 }
 return e[n];
}
vector<vector<int>> subsets;
vector<array<array<int,5>,15>> forms;
vector<array<int,4>> below;
int L,N;
int coefficient(const Exponents&e,int point){
 vector<int> f(N);f[0]=1;
 // Reverse factor order, and descending in-place recurrence on coefficients.
 for(int z=14;z>=0;z--)for(int copy=0;copy<e[z];copy++){
  const auto&c=forms[point][z];
  for(int a=N-1;a>=0;a--){
   long long value=1LL*c[0]*f[a];
   for(int j:subsets[z])if(below[a][j]>=0)value+=1LL*c[j+1]*f[below[a][j]];
   f[a]=value%P;
  }
 }
 return f[N-1];
}
void source_check(const vector<Term>&terms,array<int,4>lam,int b){
 map<Exponents,int> original;
 for(auto&t:terms){
  array<int,4>weight{},degree{};
  for(int z=0;z<15;z++){
   for(int i=0;i<(int)subsets[z].size();i++)weight[i]+=t.e[z];
   for(int j:subsets[z])degree[j]+=t.e[z];
  }
  assert(weight==lam);for(int j=0;j<4;j++)assert(degree[j]==b);
  original[t.e]+=t.c;
 }
 for(int k=0;k<3;k++){
  map<Exponents,int> transformed;
  for(auto&kv:original){
   Exponents e{};int sg=1;
   for(int z=0;z<15;z++){
    auto I=subsets[z];for(int&j:I){if(j==k)j=k+1;else if(j==k+1)j=k;}
    int inversions=0;for(int i=0;i<(int)I.size();i++)for(int j=i+1;j<(int)I.size();j++)inversions+=I[i]>I[j];
    if(inversions*kv.first[z]%2)sg=-sg;
    sort(I.begin(),I.end());int target=find(subsets.begin(),subsets.end(),I)-subsets.begin();
    assert(target<15);e[target]+=kv.first[z];
   }
   transformed[e]+=sg*kv.second;
  }
  assert(original==transformed);
 }
}
int main(int argc,char**argv){
 assert(argc==2);for(int i=2;i*i<=P;i++)assert(P%i);
 ifstream in(argv[1]);int b,blocks,prime,npoints;in>>L>>b>>blocks>>prime>>npoints;assert(prime==P);
 for(int mask=1;mask<16;mask++){
  vector<int>I;for(int j=0;j<4;j++)if(mask>>j&1)I.push_back(j);subsets.push_back(I);
 }
 sort(subsets.begin(),subsets.end(),[](auto&a,auto&b){return a.size()!=b.size()?a.size()<b.size():a<b;});
 for(int p=0;p<npoints;p++){
  array<array<int,4>,4>X;array<int,4>x;for(auto&row:X)for(int&v:row)in>>v;for(int&v:x)in>>v;
  array<array<int,5>,15> fs{};
  for(int z=0;z<15;z++){
   auto&I=subsets[z];int h=I.size();vector<vector<int>> A(h,vector<int>(h));
   for(int i=0;i<h;i++)for(int j=0;j<h;j++)A[i][j]=X[i][I[j]];
   fs[z][0]=trace_det(A);
   for(int j=0;j<h;j++){auto B=A;for(int i=0;i<h;i++)B[i][j]=x[i];fs[z][I[j]+1]=trace_det(B);}
  }
  forms.push_back(fs);
 }
 int base=L+1;N=base*base*base*base;below.resize(N);array<int,4>place{1,base,base*base,base*base*base};
 for(int i=0;i<N;i++)for(int j=0;j<4;j++)below[i][j]=i/place[j]%base?i-place[j]:-1;
 long long entries=0,vectors=0,coefficients=0;
 for(int block=0;block<blocks;block++){
  array<int,4>lam;for(int&v:lam)in>>v;int m;in>>m;
  vector<vector<Term>>selected(m);
  for(auto&v:selected){int oldindex,nt;in>>oldindex>>nt;v.resize(nt);for(auto&t:v){in>>t.c;for(int&e:t.e)in>>e;}source_check(v,lam,b);}
  vector<int>rows(m);for(int&r:rows)in>>r;
  vector<vector<int>>matrix(m,vector<int>(m));for(auto&row:matrix)for(int&v:row)in>>v;
  int expected;in>>expected;assert(expected&&trace_det(matrix)==expected);
  for(int i=0;i<m;i++){
   map<Exponents,int>cache;
   for(int j=0;j<m;j++){
    long long value=0;
    for(auto&t:selected[j]){
     auto it=cache.find(t.e);int c;
     if(it==cache.end()){c=coefficient(t.e,rows[i]);cache[t.e]=c;coefficients++;}else c=it->second;
     value+=1LL*t.c*c;
    }
    assert(mod(value)==matrix[i][j]);entries++;
   }
  }
  vectors+=m;
 }
 assert(in);cout<<"PASS independent descending Taylor/Newton determinants: blocks="<<blocks<<" vectors="<<vectors<<" entries="<<entries<<" Taylor_evaluations="<<coefficients<<"\n";
}

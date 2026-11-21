#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;
const int P=1000003;
int r,L,b,M,N;vector<vector<int>>subsets,permutations,points;
vector<vector<vector<int>>>forms;
vector<int>place;vector<vector<int>>above;
using Counts=vector<int>;
struct Term{Counts c;int a;};
int mod(long long x){x%=P;return x<0?x+P:x;}
int power(int a,int n){int v=1;for(;n;n>>=1,a=mod(1LL*a*a))if(n&1)v=mod(1LL*v*a);return v;}
int determinant(vector<vector<int>>A){
 int n=A.size(),d=1;
 for(int j=0;j<n;j++){
  int k=j;while(k<n&&!A[k][j])k++;if(k==n)return 0;
  if(k!=j){swap(A[k],A[j]);d=mod(-d);}
  int p=A[j][j],iv=power(p,P-2);d=mod(1LL*d*p);
  for(int i=j+1;i<n;i++){int c=mod(1LL*A[i][j]*iv);for(int h=j+1;h<n;h++)A[i][h]=mod(A[i][h]-1LL*c*A[j][h]);A[i][j]=0;}
 }
 return d;
}
void setup(){
 M=(1<<r)-1;
 for(int mask=1;mask<=M;mask++){vector<int>I;for(int j=0;j<r;j++)if(mask>>j&1)I.push_back(j);subsets.push_back(I);}
 sort(subsets.begin(),subsets.end(),[](auto&a,auto&b){return a.size()!=b.size()?a.size()<b.size():a<b;});
 vector<int>p(r);iota(p.begin(),p.end(),0);do{permutations.push_back(p);}while(next_permutation(p.begin(),p.end()));
 mt19937 rng(20261123);
 for(int point=0;point<64;point++){
  vector<int>pt(r*r+r);for(int&x:pt)x=1+rng()%(P-1);points.push_back(pt);
  vector<vector<int>>f(M,vector<int>(r+1));
  for(int z=0;z<M;z++){
   auto&I=subsets[z];int h=I.size();vector<vector<int>>A(h,vector<int>(h));
   for(int i=0;i<h;i++)for(int j=0;j<h;j++)A[i][j]=pt[i*r+I[j]];
   f[z][0]=determinant(A);
   for(int j=0;j<h;j++){auto C=A;for(int i=0;i<h;i++)C[i][j]=pt[r*r+i];f[z][I[j]+1]=determinant(C);}
  }
  forms.push_back(f);
 }
 N=1;for(int j=0;j<r;j++){place.push_back(N);N*=L+1;}
 above.assign(N,vector<int>(r));
 for(int i=0;i<N;i++)for(int j=0;j<r;j++)above[i][j]=i/place[j]%(L+1)<L?i+place[j]:-1;
}
vector<Term>average(Counts seed){
 map<Counts,int>terms;
 for(auto&p:permutations){
  Counts target(M);int sg=1;
  for(int z=0;z<M;z++)if(seed[z]){
   auto I=subsets[z];for(int&i:I)i=p[i];
   for(int i=0;i<(int)I.size();i++)for(int j=i+1;j<(int)I.size();j++)if(I[i]>I[j]&&seed[z]%2)sg=-sg;
   sort(I.begin(),I.end());int k=find(subsets.begin(),subsets.end(),I)-subsets.begin();assert(k<M);target[k]+=seed[z];
  }
  terms[target]+=sg;
 }
 int divisor=0;for(auto&kv:terms)divisor=gcd(divisor,abs(kv.second));if(!divisor)return {};
 for(auto&kv:terms)if(kv.second){if(kv.second<0)divisor=-divisor;break;}
 vector<Term>result;for(auto&kv:terms)if(kv.second)result.push_back({kv.first,kv.second/divisor});
 return result;
}
int coefficient(Counts const&c,int point){
 vector<int>dp(N),nd(N);dp[0]=1;
 for(int z=0;z<M;z++)for(int copy=0;copy<c[z];copy++){
  fill(nd.begin(),nd.end(),0);auto&f=forms[point][z];
  for(int a=0;a<N;a++)if(dp[a]){
   nd[a]=mod(nd[a]+1LL*dp[a]*f[0]);
   for(int j:subsets[z])if(above[a][j]>=0)nd[above[a][j]]=mod(nd[above[a][j]]+1LL*dp[a]*f[j+1]);
  }
  dp.swap(nd);
 }
 return dp[N-1];
}
int main(int argc,char**argv){
 assert(argc==2);string path=argv[1],stem=path.substr(0,path.rfind('.'));ifstream in(path);int blocks;in>>r>>L>>b>>blocks;setup();
 ofstream out(stem+"_RANKS.tsv"),cert(stem+".selected");
 out<<"partition\tsource_multiplicity\timage_rank\tseeds_tried\tminor_determinant\tstatus\n";
 cert<<r<<" "<<L<<" "<<b<<" "<<blocks<<" "<<P<<" "<<points.size()<<"\n";
 for(auto&pt:points){for(int x:pt)cert<<x<<" ";cert<<"\n";}
 int deficient=0,totalrank=0;
 for(int block=0;block<blocks;block++){
  vector<int>lam(r);for(int&x:lam)in>>x;int m,K,nc;in>>m>>K>>nc;
  vector<Counts>seeds(nc,Counts(M));for(auto&c:seeds)for(int&x:c)in>>x;
  int np=m+2;assert(np<=64);vector<vector<int>>echelon(np),original;vector<int>chosen;
  map<Counts,vector<int>>cache;int rank=0,used=0;
  for(int ci=0;ci<nc&&rank<m;ci++){
   used++;auto terms=average(seeds[ci]);vector<int>col(np);
   for(auto&t:terms){
    auto it=cache.find(t.c);if(it==cache.end()){vector<int>v(np);for(int j=0;j<np;j++)v[j]=coefficient(t.c,j);it=cache.emplace(t.c,move(v)).first;}
    for(int j=0;j<np;j++)col[j]=mod(col[j]+1LL*t.a*it->second[j]);
   }
   auto red=col;
   for(int i=0;i<np;i++)if(red[i]){
    if(echelon[i].empty()){int iv=power(red[i],P-2);for(int j=i;j<np;j++)red[j]=mod(1LL*red[j]*iv);echelon[i]=red;original.push_back(col);chosen.push_back(ci);rank++;break;}
    int scale=red[i];for(int j=i;j<np;j++)red[j]=mod(red[j]-1LL*scale*echelon[i][j]);
   }
  }
  vector<int>rows;for(int i=0;i<np;i++)if(!echelon[i].empty())rows.push_back(i);
  vector<vector<int>>matrix(rank,vector<int>(rank));for(int i=0;i<rank;i++)for(int j=0;j<rank;j++)matrix[i][j]=original[j][rows[i]];
  int det=determinant(matrix);assert(det);
  for(int j=0;j<r;j++)out<<(j?",":"")<<lam[j];out<<"\t"<<m<<"\t"<<rank<<"\t"<<used<<"\t"<<det<<"\t"<<(rank==m?"PASS":"RANK_DEFICIT")<<"\n";
  for(int x:lam)cert<<x<<" ";cert<<m<<" "<<rank<<"\n";
  for(int ci:chosen){cert<<ci;for(int x:seeds[ci])cert<<" "<<x;cert<<"\n";}
  for(int x:rows)cert<<x<<" ";cert<<"\n";for(auto&row:matrix){for(int x:row)cert<<x<<" ";cert<<"\n";}cert<<det<<"\n";
  if(rank!=m){deficient++;cerr<<"DEFICIT";for(int x:lam)cerr<<" "<<x;cerr<<" rank "<<rank<<"/"<<m<<" all_seeds "<<used<<"/"<<K<<"\n";}
  totalrank+=rank;
 }
 cout<<"case "<<r<<" "<<L<<" "<<b<<" blocks="<<blocks<<" totalrank="<<totalrank<<" deficient="<<deficient<<"\n";
}

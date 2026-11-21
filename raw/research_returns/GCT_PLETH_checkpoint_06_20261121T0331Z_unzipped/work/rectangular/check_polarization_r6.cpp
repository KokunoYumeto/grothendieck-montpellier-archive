#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
const int P=1000003,R=6,B=5;
using Exp=array<unsigned char,63>;
using Matrix=array<array<int,6>,6>;
struct Term{Exp e;int c;};
struct Point{Matrix X;array<int,6>x;};
struct Hash{size_t operator()(Exp const&e)const{size_t h=1469598103934665603ULL;for(auto x:e){h^=x;h*=1099511628211ULL;}return h;}};
int mod(long long x){x%=P;return x<0?x+P:x;}
int power(int x,int n){int y=1;for(;n;n>>=1,x=mod(1LL*x*x))if(n&1)y=mod(1LL*y*x);return y;}
int determinant(vector<vector<int>> A){
 int n=A.size(),d=1;
 for(int j=0;j<n;j++){
  int k=j;while(k<n&&!A[k][j])k++;if(k==n)return 0;
  if(k!=j){swap(A[k],A[j]);d=mod(-d);}
  int p=A[j][j],iv=power(p,P-2);d=mod(1LL*d*p);
  for(int i=j+1;i<n;i++){
   int c=mod(1LL*A[i][j]*iv);
   for(int l=j+1;l<n;l++)A[i][l]=mod(A[i][l]-1LL*c*A[j][l]);
   A[i][j]=0;
  }
 }
 return d;
}
vector<vector<int>>subsets;
array<int,64>maskindex;
vector<array<pair<int,int>,63>>permute;
vector<Point>points;
struct Evaluator{
 array<array<int,6>,63>constant_power;
 array<vector<pair<int,int>>,63>logs;
};
vector<Evaluator>evaluators;
void setup(){
 for(int mask=1;mask<64;mask++){vector<int>I;for(int j=0;j<6;j++)if(mask>>j&1)I.push_back(j);subsets.push_back(I);}
 sort(subsets.begin(),subsets.end(),[](auto&a,auto&b){return a.size()!=b.size()?a.size()<b.size():a<b;});
 for(int z=0;z<63;z++){int mask=0;for(int j:subsets[z])mask|=1<<j;maskindex[mask]=z;}
 array<int,6>p{0,1,2,3,4,5};
 do{
  array<pair<int,int>,63>pm;
  for(int z=0;z<63;z++){
   int mask=0,sg=1;auto I=subsets[z];
   for(int&i:I){i=p[i];mask|=1<<i;}
   for(int i=0;i<(int)I.size();i++)for(int j=i+1;j<(int)I.size();j++)if(I[i]>I[j])sg=-sg;
   pm[z]={maskindex[mask],sg};
  }
  permute.push_back(pm);
 }while(next_permutation(p.begin(),p.end()));
 assert(permute.size()==720);
 mt19937 rng(20261121);
 int factorial[6]{1,1,2,6,24,120};
 while(points.size()<64){
  Point pt;for(auto&row:pt.X)for(int&v:row)v=1+rng()%(P-1);for(int&v:pt.x)v=1+rng()%(P-1);
  Evaluator eval;bool good=true;
  for(int z=0;z<63;z++){
   auto&I=subsets[z];int h=I.size(),mask=0;for(int j:I)mask|=1<<j;
   vector<vector<int>>A(h,vector<int>(h));for(int i=0;i<h;i++)for(int j=0;j<h;j++)A[i][j]=pt.X[i][I[j]];
   int d=determinant(A);if(!d){good=false;break;}
   eval.constant_power[z][0]=1;for(int k=1;k<=5;k++)eval.constant_power[z][k]=mod(1LL*eval.constant_power[z][k-1]*d);
   int iv=power(d,P-2);array<int,6>ratio{};
   for(int j=0;j<h;j++){auto C=A;for(int i=0;i<h;i++)C[i][j]=pt.x[i];ratio[I[j]]=mod(1LL*determinant(C)*iv);}
   for(int S=mask;S;S=(S-1)&mask){
    int k=__builtin_popcount((unsigned)S),value=factorial[k-1];
    for(int j=0;j<6;j++)if(S>>j&1)value=mod(1LL*value*ratio[j]);
    if(k%2==0)value=mod(-value);
    eval.logs[z].push_back({S,value});
   }
  }
  if(good){points.push_back(pt);evaluators.push_back(move(eval));}
 }
}
vector<Term> orbit(const Exp&e){
 vector<pair<int,int>>support;for(int i=0;i<63;i++)if(e[i])support.push_back({i,e[i]});
 map<Exp,int>terms;
 for(auto&pm:permute){
  Exp z{};int sign=1;
  for(auto ic:support){auto js=pm[ic.first];z[js.first]+=ic.second;if(ic.second%2)sign*=js.second;}
  terms[z]+=sign;
 }
 int divisor=0;for(auto&kv:terms)if(kv.second)divisor=gcd(divisor,abs(kv.second));
 if(!divisor)return {};
 for(auto&kv:terms)if(kv.second){if(kv.second<0)divisor=-divisor;break;}
 vector<Term>out;for(auto&kv:terms)if(kv.second)out.push_back({kv.first,kv.second/divisor});
 return out;
}
int coefficient(const Exp&e,int point){
 auto&ev=evaluators[point];array<long long,64>logsum{};int constant=1;
 for(int z=0;z<63;z++)if(e[z]){
  constant=mod(1LL*constant*ev.constant_power[z][e[z]]);
  for(auto&sv:ev.logs[z])logsum[sv.first]+=1LL*e[z]*sv.second;
 }
 array<int,64>log{},value{};for(int S=1;S<64;S++)log[S]=mod(logsum[S]);value[0]=1;
 for(int S=1;S<64;S++){
  int first=S&-S;long long answer=0;
  for(int T=S;T;T=(T-1)&S)if(T&first)answer+=1LL*log[T]*value[S^T];
  value[S]=mod(answer);
 }
 return mod(1LL*constant*value[63]);
}
int main(int argc,char**argv){
 assert(argc==2);setup();string path=argv[1],stem=path.substr(0,path.rfind('.'));
 ifstream in(path);int r,L,b,blocks;in>>r>>L>>b>>blocks;assert(r==6&&L==1&&b==5);
 ofstream out(stem+"_RANKS.tsv"),cert(stem+".selected");
 out<<"partition\tsource_multiplicity\timage_rank\tseeds_tried\tminor_determinant\tstatus\n";
 cert<<r<<" "<<L<<" "<<b<<" "<<blocks<<" "<<P<<" "<<points.size()<<"\n";
 for(auto&pt:points){for(auto&row:pt.X)for(int v:row)cert<<v<<" ";for(int v:pt.x)cert<<v<<" ";cert<<"\n";}
 int fails=0,totalrank=0;long long evaluated=0;
 for(int block=0;block<blocks;block++){
  array<int,6>lam;for(int&v:lam)in>>v;int mult,K,nc;in>>mult>>K>>nc;
  vector<Exp>seeds(nc);for(auto&e:seeds)for(auto&v:e){int x;in>>x;v=x;}
  int np=mult+2;assert(np<=64);
  vector<vector<int>>echelon(np),original;vector<int>chosen;
  unordered_map<Exp,vector<int>,Hash>cache;cache.reserve(4096);
  int rank=0,used=0;
  for(int ci=0;ci<nc&&rank<mult;ci++){
   used++;auto terms=orbit(seeds[ci]);if(terms.empty())continue;
   vector<int>col(np);
   for(auto&t:terms){
    auto it=cache.find(t.e);
    if(it==cache.end()){
     vector<int>values(np);for(int j=0;j<np;j++)values[j]=coefficient(t.e,j);
     evaluated+=np;it=cache.emplace(t.e,move(values)).first;
    }
    for(int j=0;j<np;j++)col[j]=mod(col[j]+1LL*t.c*it->second[j]);
   }
   auto red=col;
   for(int i=0;i<np;i++)if(red[i]){
    if(echelon[i].empty()){
     int iv=power(red[i],P-2);for(int j=i;j<np;j++)red[j]=mod(1LL*red[j]*iv);
     echelon[i]=red;original.push_back(col);chosen.push_back(ci);rank++;break;
    }
    int scale=red[i];for(int j=i;j<np;j++)red[j]=mod(red[j]-1LL*scale*echelon[i][j]);
   }
  }
  vector<int>rows;for(int i=0;i<np;i++)if(!echelon[i].empty())rows.push_back(i);
  vector<vector<int>>matrix(rank,vector<int>(rank));
  for(int i=0;i<rank;i++)for(int j=0;j<rank;j++)matrix[i][j]=original[j][rows[i]];
  int det=determinant(matrix);assert(!rank||det);
  for(int i=0;i<6;i++)out<<(i?",":"")<<lam[i];
  out<<"\t"<<mult<<"\t"<<rank<<"\t"<<used<<"\t"<<det<<"\t"<<(rank==mult?"PASS":"DEFICIENT_EVALUATION_RANK")<<"\n";
  for(int v:lam)cert<<v<<" ";cert<<mult<<" "<<rank<<"\n";
  for(int ci:chosen){cert<<ci;for(int v:seeds[ci])cert<<" "<<v;cert<<"\n";}
  for(int i:rows)cert<<i<<" ";cert<<"\n";
  for(auto&row:matrix){for(int v:row)cert<<v<<" ";cert<<"\n";}cert<<det<<"\n";
  if(rank!=mult){fails++;cerr<<"DEFICIENT";for(int v:lam)cerr<<" "<<v;cerr<<" rank "<<rank<<"/"<<mult<<" used "<<used<<" K "<<K<<"\n";}
  totalrank+=rank;
 }
 cout<<"r6 L1 b5 blocks="<<blocks<<" rank="<<totalrank<<" deficient="<<fails<<" Taylor_evaluations="<<evaluated<<"\n";
}

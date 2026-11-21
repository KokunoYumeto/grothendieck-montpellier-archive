#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

// Exact arithmetic in Z[w], w^2+w+1=0.  The five Cohen root vectors
// all have norm two; the basis Gram matrix is H below.  No class table
// or precomputed group list is used.
struct E { long long a=0,b=0; };
E operator+(E x,E y){return {x.a+y.a,x.b+y.b};}
E operator-(E x,E y){return {x.a-y.a,x.b-y.b};}
E operator-(E x){return {-x.a,-x.b};}
E operator*(E x,E y){return {x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a-x.b*y.b};}
bool operator==(E x,E y){return x.a==y.a&&x.b==y.b;}
E cj(E x){return {x.a-x.b,-x.b};}
using M=array<int16_t,50>;
E get(const M&m,int i,int j){return {m[2*(5*i+j)],m[2*(5*i+j)+1]};}
void put(M&m,int i,int j,E x){
 assert(abs(x.a)<32768&&abs(x.b)<32768);
 m[2*(5*i+j)]=x.a;m[2*(5*i+j)+1]=x.b;
}
M eye(){M a{};for(int i=0;i<5;i++)put(a,i,i,{1,0});return a;}
M mul(const M&a,const M&b){
 M c{};for(int i=0;i<5;i++)for(int j=0;j<5;j++){
  E v{};for(int k=0;k<5;k++)v=v+get(a,i,k)*get(b,k,j);put(c,i,j,v);
 }return c;
}
struct Hash {size_t operator()(const M&a)const{
 size_t h=1469598103934665603ULL;
 for(auto v:a){h^=uint16_t(v);h*=1099511628211ULL;}return h;
}};
array<array<E,5>,5> H{{
 {{{2,0},{1,0},{0,0},{0,0},{0,0}}},
 {{{1,0},{2,0},{0,1},{-1,-1},{0,0}}},
 {{{0,0},{-1,-1},{2,0},{-1,0},{0,0}}},
 {{{0,0},{0,1},{-1,0},{2,0},{-1,0}}},
 {{{0,0},{0,0},{0,0},{-1,0},{2,0}}}
}};
M right_ref(const M&a,int k){
 M b=a;for(int i=0;i<5;i++)for(int j=0;j<5;j++)
 put(b,i,j,get(a,i,j)-get(a,i,k)*H[k][j]);return b;
}
M left_ref(const M&a,int k){
 M b=a;for(int j=0;j<5;j++){
  E v{};for(int i=0;i<5;i++)v=v+H[k][i]*get(a,i,j);
  put(b,k,j,get(a,k,j)-v);
 }return b;
}
vector<E> charpoly(const M&a){
 vector<E> tr(6),c(6);c[0]={1,0};M p=eye();
 for(int k=1;k<=5;k++){
  p=mul(p,a);for(int j=0;j<5;j++)tr[k]=tr[k]+get(p,j,j);
  E v{};for(int j=1;j<=k;j++)v=v+c[k-j]*tr[j];
  assert(v.a%k==0&&v.b%k==0);c[k]={-v.a/k,-v.b/k};
 }return c;
}
int ord(const M&a){M p=eye();for(int k=1;k<=51840;k++){p=mul(p,a);if(p==eye())return k;}assert(false);return 0;}
void outE(ostream&o,E z){o<<'['<<z.a<<','<<z.b<<']';}
void outM(ostream&o,const M&m){o<<'[';for(int i=0;i<5;i++){if(i)o<<',';o<<'[';for(int j=0;j<5;j++){if(j)o<<',';outE(o,get(m,i,j));}o<<']';}o<<']';}
int main(int argc,char**argv){
 string dest=argc>1?argv[1]:"g33_classes.json";
 vector<M> mats;vector<array<int,5>> adj;vector<int> par,letter;
 unordered_map<M,int,Hash> idx;idx.reserve(60000);
 mats.push_back(eye());par.push_back(-1);letter.push_back(-1);idx[mats[0]]=0;
 for(size_t cur=0;cur<mats.size();cur++){
  M a=mats[cur];array<int,5> row{};
  for(int j=0;j<5;j++){
   M b=right_ref(a,j);auto [it,inserted]=idx.emplace(b,int(mats.size()));
   if(inserted){mats.push_back(b);par.push_back(cur);letter.push_back(j+1);}
   row[j]=it->second;
  }adj.push_back(row);
  assert(mats.size()<=51840);
 }
 assert(mats.size()==51840);
 // Exact Hermitian invariance for the generating reflections.
 for(int k=0;k<5;k++){
  auto a=mats[adj[0][k]];assert(mul(a,a)==eye());
  for(int i=0;i<5;i++)for(int j=0;j<5;j++){
   E v{};for(int x=0;x<5;x++)for(int y=0;y<5;y++)
    v=v+cj(get(a,x,i))*H[x][y]*get(a,y,j);
   assert(v==H[i][j]);
  }
 }
 vector<int> cls(mats.size(),-1),reps,sizes;
 for(int a=0;a<(int)mats.size();a++)if(cls[a]<0){
  int cl=reps.size();reps.push_back(a);queue<int> q;q.push(a);cls[a]=cl;int sz=0;
  while(!q.empty()){
   int b=q.front();q.pop();sz++;
   for(int j=0;j<5;j++){
    M c=left_ref(mats[adj[b][j]],j);auto it=idx.find(c);assert(it!=idx.end());
    int d=it->second;if(cls[d]<0){cls[d]=cl;q.push(d);}else assert(cls[d]==cl);
   }
  }sizes.push_back(sz);
 }
 ofstream out(dest);out<<"{\n\"status\":\"PASS exact closure and conjugacy partition\",\n\"group_order\":"<<mats.size()<<",\n\"class_count\":"<<reps.size()<<",\n\"coefficient_convention\":\"[a,b] means a+b*omega, omega^2+omega+1=0\",\n\"gram\":[";
 for(int i=0;i<5;i++){if(i)out<<',';out<<'[';for(int j=0;j<5;j++){if(j)out<<',';outE(out,H[i][j]);}out<<']';}
 out<<"],\n\"classes\":[\n";
 int target_count=0,reflection_count=0;
 for(size_t k=0;k<reps.size();k++){
  if(k)out<<",\n";int a=reps[k];auto cp=charpoly(mats[a]);
  vector<int> wd;for(int b=a;par[b]>=0;b=par[b])wd.push_back(letter[b]);reverse(wd.begin(),wd.end());
  bool target=false;for(int eps:{1,-1}){
   vector<E> p{{1,0},{-eps,0},{2,0},{-2*eps,0},{1,0},{-eps,0}};
   if(cp==p)target=true;
  }
  if(target)target_count++;
  vector<E> refl{{1,0},{-3,0},{2,0},{2,0},{-3,0},{1,0}}; // (x-1)^4(x+1)
  if(cp==refl)reflection_count+=sizes[k];
  out<<"{\"class\":"<<k<<",\"size\":"<<sizes[k]<<",\"order\":"<<ord(mats[a])<<",\"target_quarter_turn_type\":"<<(target?"true":"false")<<",\"word\":[";
  for(size_t j=0;j<wd.size();j++){if(j)out<<',';out<<wd[j];}out<<"],\"charpoly_desc\":[";
  for(size_t j=0;j<cp.size();j++){if(j)out<<',';outE(out,cp[j]);}out<<"],\"matrix\":";outM(out,mats[a]);out<<'}';
 }
 out<<"\n],\n\"target_class_count\":"<<target_count<<",\n\"reflection_count\":"<<reflection_count<<"\n}\n";
 assert(reflection_count==45);assert(target_count>0);
 cerr<<"PASS group="<<mats.size()<<" classes="<<reps.size()<<" target_classes="<<target_count<<" reflections="<<reflection_count<<"\n";
}

// Exact exploratory rank test for the bordered-permanent induction criterion.
// The forward DP keeps t-degrees 0,1,2 in per(A+t*u*v^T); reverse AD
// differentiates its degree-one and degree-two coefficients in u and v.
// This tests a finite criterion; no inference for untested sizes is made.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using Point=std::array<int,3>;
int modpow(int a,int e,int p){int r=1;for(;e;e>>=1,a=int(1LL*a*a%p))if(e&1)r=int(1LL*r*a%p);return r;}
bool prime(int p){if(p<2)return false;for(int d=2;1LL*d*d<=p;++d)if(p%d==0)return false;return true;}
uint32_t next(uint32_t& s){s=1664525u*s+1013904223u;return s;}
int primitive_root(int p){for(int a=2;a<p;++a){bool ok=true;for(int d=2;d<=p-1;++d)if((p-1)%d==0&&prime(d)&&modpow(a,(p-1)/d,p)==1){ok=false;break;}if(ok)return a;}return -1;}

struct Data {int n,p,q; uint32_t seed; std::string mode; std::vector<int>A,u,v;};
Data make_data(int n,std::string mode,uint32_t seed){
 bool balanced=mode=="balanced_cycle"||mode=="balanced_band"||mode=="balanced2_cycle"||mode=="balanced2_band"; int p=1009;while(!prime(p)||(p-1)%(balanced?2*n:n))++p;
 int q=modpow(primitive_root(p),(p-1)/n,p);
 Data d{n,p,q,seed,mode,std::vector<int>(3*n*n),std::vector<int>(3*n),std::vector<int>(3*n)};
 uint32_t s=seed;
 if(mode=="dense")for(auto&x:d.A)x=int((next(s)>>8)%p);
 else {int qi=1;for(int i=0;i<n;++i){d.A[3*(n*i+i)]=1;d.A[3*(n*i+i)+1]=p-qi;d.A[3*(n*i+(i+1)%n)+2]=1;d.A[3*(n*i+(i+1)%n)+1]=p-qi;qi=int(1LL*qi*q%p);}
  if(mode=="tridiagonal"){std::fill(d.A.begin(),d.A.end(),0);for(int i=0;i<n;++i)for(int j=std::max(0,i-1);j<=std::min(n-1,i+1);++j)for(int k=0;k<3;++k)d.A[3*(n*i+j)+k]=int((next(s)>>8)%p);}
  if(mode=="random_cycle")for(int i=0;i<n;++i)for(int j:{i,(i+1)%n})for(int k=0;k<3;++k)d.A[3*(n*i+j)+k]=int((next(s)>>8)%p);
  if(mode=="chord"||mode=="pair")for(int k=0;k<3;++k)d.A[3*2+k]=int((next(s)>>8)%p);
  if(mode=="pair")for(int k=0;k<3;++k)d.A[3*n+k]=int((next(s)>>8)%p);
  if(mode=="band2")for(int i=0;i<n;++i)for(int k=0;k<3;++k)d.A[3*(n*i+(i+2)%n)+k]=int((next(s)>>8)%p);
 }
 for(auto&x:d.u)x=int((next(s)>>8)%p);
 for(auto&x:d.v)x=int((next(s)>>8)%p);
 if(mode=="jacobi"||mode=="jacobi_ends"||mode=="jacobi_mono"){
  std::fill(d.A.begin(),d.A.end(),0);for(int i=0;i<n;++i){d.A[3*(n*i+i)]=int((next(s)>>8)%p);if(i+1<n){d.A[3*(n*i+i+1)+1]=int((next(s)>>8)%p);d.A[3*(n*(i+1)+i)+2]=int((next(s)>>8)%p);}}
  if(mode=="jacobi_ends")for(int i=1;i<n-1;++i)for(int k=0;k<3;++k)d.u[3*i+k]=d.v[3*i+k]=0;
  if(mode=="jacobi_mono"){std::fill(d.u.begin(),d.u.end(),0);std::fill(d.v.begin(),d.v.end(),0);d.u[0]=1;d.u[3*(n-1)+1]=1;d.v[0]=1;d.v[3*(n-1)+2]=1;}
 }
 if(balanced){
  std::fill(d.A.begin(),d.A.end(),0);int zeta=modpow(primitive_root(p),(p-1)/(2*n),p);std::array<int,9>c;for(auto&x:c)x=int((next(s)>>8)%p);
  for(int i=0;i<n;++i){int qi=modpow(q,i,p),q2=int(1LL*qi*qi%p),q3=int(1LL*q2*qi%p),iq=modpow(qi,p-2,p),us=modpow(zeta,i*(n-i),p),vs=modpow(us,p-2,p);
   d.A[3*(n*i+i)]=1;d.A[3*(n*i+i)+1]=p-qi;d.A[3*(n*i+(i+1)%n)+2]=1;d.A[3*(n*i+(i+1)%n)+1]=p-q2;
   if(mode=="balanced_band"){d.A[3*(n*i+(i+2)%n)]=int(1LL*q2*c[6]%p);d.A[3*(n*i+(i+2)%n)+1]=int(1LL*q3*c[7]%p);d.A[3*(n*i+(i+2)%n)+2]=int(1LL*qi*c[8]%p);}
   d.u[3*i]=int(1LL*us*c[0]%p);d.u[3*i+1]=int(1LL*us*qi%p*c[1]%p);d.u[3*i+2]=int(1LL*us*iq%p*c[2]%p);
   d.v[3*i]=int(1LL*vs*c[3]%p);d.v[3*i+1]=int(1LL*vs*qi%p*c[4]%p);d.v[3*i+2]=int(1LL*vs*iq%p*c[5]%p);
   if(mode=="balanced2_cycle"||mode=="balanced2_band"){
    us=modpow(q,i*(i-1),p);vs=modpow(us,p-2,p);int iq2=int(1LL*iq*iq%p),iq3=int(1LL*iq2*iq%p),iq4=int(1LL*iq3*iq%p);d.A[3*(n*i+(i+1)%n)+1]=p-iq;
    if(mode=="balanced2_band"){d.A[3*(n*i+(i+2)%n)]=int(1LL*iq4*c[6]%p);d.A[3*(n*i+(i+2)%n)+1]=int(1LL*iq3*c[7]%p);d.A[3*(n*i+(i+2)%n)+2]=int(1LL*iq2*c[8]%p);}
    d.u[3*i]=int(1LL*us*c[0]%p);d.u[3*i+1]=int(1LL*us*qi%p*c[1]%p);d.u[3*i+2]=int(1LL*us*q2%p*c[2]%p);
    d.v[3*i]=int(1LL*vs*c[3]%p);d.v[3*i+1]=int(1LL*vs*qi%p*c[4]%p);d.v[3*i+2]=int(1LL*vs*q2%p*c[5]%p);
   }
  }
 }
 return d;
}

std::vector<Point> points(int degree){std::vector<Point>r;for(int x=degree;x>=0;--x)for(int y=degree-x;y>=0;--y)r.push_back({x,y,degree-x-y});return r;}

struct Evaluator {
 int n,p;unsigned N;std::vector<unsigned> row;
 std::vector<int>A,u,v,H,f0,f1,f2,r0,r1,r2;
 Evaluator(int n_,int p_):n(n_),p(p_),N(1u<<n),row(N),A(n*n),u(n),v(n),H(n*n),f0(N),f1(N),f2(N),r0(N),r1(N),r2(N){for(unsigned s=1;s<N;++s)row[s]=__builtin_popcount(s)-1;}
 std::pair<std::vector<int>,std::vector<int>> gradient(int degree){
  std::fill(r0.begin(),r0.end(),0);std::fill(r1.begin(),r1.end(),0);std::fill(r2.begin(),r2.end(),0);
  (degree==1?r1:r2)[N-1]=1;
  std::vector<uint64_t>gu(n),gv(n);
  for(unsigned s=N-1;s>0;--s){
   int a0=r0[s],a1=r1[s],a2=r2[s];if(!a0&&!a1&&!a2)continue;
   int i=row[s],base=n*i;unsigned bits=s;
   while(bits){unsigned bit=bits&(-bits),t=s^bit;int j=__builtin_ctz(bits);bits^=bit;int aa=A[base+j],hh=H[base+j];
    int gh=int((1LL*a1*f0[t]+1LL*a2*f1[t])%p);
    gu[i]+=1ULL*gh*v[j];gv[j]+=1ULL*gh*u[i];
    r0[t]=int((r0[t]+1LL*aa*a0+1LL*hh*a1)%p);
    r1[t]=int((r1[t]+1LL*aa*a1+1LL*hh*a2)%p);
    r2[t]=int((r2[t]+1LL*aa*a2)%p);
   }
  }
  std::vector<int>ou(n),ov(n);for(int i=0;i<n;++i){ou[i]=gu[i]%p;ov[i]=gv[i]%p;}return {ou,ov};
 }
 std::vector<int> operator()(const Data&d,const Point&x){
  for(int ij=0;ij<n*n;++ij){int t=0;for(int k=0;k<3;++k)t+=d.A[3*ij+k]*x[k];A[ij]=t%p;}
  for(int i=0;i<n;++i){int a=0,b=0;for(int k=0;k<3;++k){a+=d.u[3*i+k]*x[k];b+=d.v[3*i+k]*x[k];}u[i]=a%p;v[i]=b%p;}
  for(int i=0;i<n;++i)for(int j=0;j<n;++j)H[n*i+j]=int(1LL*u[i]*v[j]%p);
  f0[0]=1;f1[0]=f2[0]=0;
  for(unsigned s=1;s<N;++s){uint64_t t0=0,t1=0,t2=0;unsigned bits=s;int base=n*row[s];while(bits){unsigned bit=bits&(-bits),t=s^bit;int j=__builtin_ctz(bits);bits^=bit;int aa=A[base+j],hh=H[base+j];t0+=1ULL*aa*f0[t];t1+=1ULL*aa*f1[t]+1ULL*hh*f0[t];t2+=1ULL*aa*f2[t]+1ULL*hh*f1[t];}f0[s]=t0%p;f1[s]=t1%p;f2[s]=t2%p;}
  auto g1=gradient(1),g2=gradient(2);std::vector<int>out;out.reserve(8*n+3);
  for(int k=0;k<3;++k)out.push_back(f0[N-1]*x[k]%p);
  for(int i=0;i<n;++i)for(int k=0;k<3;++k)out.push_back(g1.first[i]*x[k]%p);
  for(int j=0;j<n;++j)for(int k=0;k<3;++k)out.push_back(g1.second[j]*x[k]%p);
  for(int i=0;i<n;++i)out.push_back(g2.first[i]);
  for(int j=0;j<n;++j)out.push_back(g2.second[j]);
  return out;
 }
};

struct Rank {int rank,det;std::vector<int>rows,columns;};
Rank elimination(std::vector<int>a,int nr,int nc,int p){int r=0,det=1;std::vector<int>names(nr),rs,cs;std::iota(names.begin(),names.end(),0);for(int c=0;c<nc&&r<nr;++c){int i=r;while(i<nr&&!a[i*nc+c])++i;if(i==nr)continue;if(i!=r){std::swap(names[i],names[r]);for(int j=0;j<nc;++j)std::swap(a[i*nc+j],a[r*nc+j]);}int pivot=a[r*nc+c];det=int(1LL*det*pivot%p);int inv=modpow(pivot,p-2,p);for(int j=c;j<nc;++j)a[r*nc+j]=int(1LL*a[r*nc+j]*inv%p);for(i=r+1;i<nr;++i){int t=a[i*nc+c];if(t)for(int j=c;j<nc;++j)a[i*nc+j]=(a[i*nc+j]-int(1LL*t*a[r*nc+j]%p)+p)%p;}rs.push_back(names[r]);cs.push_back(c);++r;}return {r,det,rs,cs};}
template<typename T>void array(std::ostream&o,const std::vector<T>&v){o<<'[';for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}o<<']';}
int main(int argc,char**argv){if(argc<4){std::cerr<<"usage: check_border_ternary m cyclic|dense outdir [seed]\n";return 2;}int n=std::stoi(argv[1]);if(n<3||n>20)return 3;std::string mode=argv[2];if(mode!="cyclic"&&mode!="dense"&&mode!="random_cycle"&&mode!="chord"&&mode!="pair"&&mode!="band2"&&mode!="balanced_cycle"&&mode!="balanced_band"&&mode!="balanced2_cycle"&&mode!="balanced2_band"&&mode!="tridiagonal"&&mode!="jacobi"&&mode!="jacobi_ends"&&mode!="jacobi_mono")return 4;uint32_t seed=argc>4?std::stoul(argv[4]):20261121u+4099u*n;auto d=make_data(n,mode,seed);auto pts=points(n+1);Evaluator ev(n,d.p);std::vector<int>J;J.reserve(pts.size()*(8*n+3));auto start=std::chrono::steady_clock::now();for(const auto&x:pts){auto row=ev(d,x);J.insert(J.end(),row.begin(),row.end());}auto mid=std::chrono::steady_clock::now();auto rank=elimination(J,pts.size(),8*n+3,d.p);auto end=std::chrono::steady_clock::now();std::filesystem::create_directories(argv[3]);std::string stem=std::string(argv[3])+"/border_"+mode+"_m"+std::to_string(n);std::ofstream raw(stem+".u16",std::ios::binary);for(int x:J){uint16_t y=x;raw.write(reinterpret_cast<char*>(&y),2);}raw.close();std::ofstream out(stem+".json");out<<"{\n\"m\":"<<n<<",\n\"mode\":\""<<mode<<"\",\n\"prime\":"<<d.p<<",\n\"q\":"<<d.q<<",\n\"seed\":"<<seed<<",\n\"rows\":"<<pts.size()<<",\n\"columns\":"<<8*n+3<<",\n\"target\":"<<8*n+2<<",\n\"rank\":"<<rank.rank<<",\n\"minor_in_selected_row_order\":"<<rank.det<<",\n\"selected_rows\":";array(out,rank.rows);out<<",\n\"selected_columns\":";array(out,rank.columns);out<<",\n\"pencil_A\":";array(out,d.A);out<<",\n\"pencil_u\":";array(out,d.u);out<<",\n\"pencil_v\":";array(out,d.v);out<<",\n\"points\":[";for(size_t i=0;i<pts.size();++i){if(i)out<<',';out<<'['<<pts[i][0]<<','<<pts[i][1]<<','<<pts[i][2]<<']';}out<<"],\n\"evaluation_seconds\":"<<std::chrono::duration<double>(mid-start).count()<<",\n\"elimination_seconds\":"<<std::chrono::duration<double>(end-mid).count()<<"\n}\n";std::cout<<"m="<<n<<" mode="<<mode<<" p="<<d.p<<" rank="<<rank.rank<<" target="<<8*n+2<<" determinant="<<rank.det<<" evaluation_s="<<std::chrono::duration<double>(mid-start).count()<<std::endl;return 0;}

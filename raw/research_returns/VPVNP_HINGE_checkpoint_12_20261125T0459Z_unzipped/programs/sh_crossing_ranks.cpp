// Exact finite-field coefficient and flattening-rank audit of the crossing
// construction in Anthropic's unrefereed Appendix B.  Original implementation.
// Usage: sh_crossing_ranks SIZE ENERGY FIELD [cumulative|binary-coefficients]
// FIELD=2 uses GF(256) interpolation, then checks all coefficients lie in F2.
// Other FIELD values are prime moduli greater than the interpolation degree.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

struct Field {
  int characteristic;
  bool binary;
  array<array<int,256>,256> table{};
  vector<int> inverses;
  explicit Field(int p): characteristic(p),binary(p==2) {
    if(binary) {
      for(int a=0;a<256;++a) for(int b=0;b<256;++b) {
        int x=a,y=b,r=0;
        while(y) {if(y&1)r^=x; y>>=1; x<<=1;if(x&256)x^=0x11b;}
        table[a][b]=r;
      }
      inverses.resize(256);
      for(int a=1;a<256;++a) {
        for(int b=1;b<256;++b) if(table[a][b]==1){inverses[a]=b;break;}
        assert(inverses[a]);
      }
    }
  }
  int add(int a,int b)const{if(binary)return a^b;int c=a+b;return c>=characteristic?c-characteristic:c;}
  int neg(int a)const{return binary?a:(a?characteristic-a:0);}
  int sub(int a,int b)const{return add(a,neg(b));}
  int mul(int a,int b)const{return binary?table[a][b]:int(int64_t(a)*b%characteristic);}
  int power(int a,int e)const{int r=1;for(;e;e>>=1,a=mul(a,a))if(e&1)r=mul(r,a);return r;}
  int inv(int a)const{assert(a);return binary?inverses[a]:power(a,characteristic-2);}
  int integer(int64_t a)const{if(binary)return int(a&1);int r=int(a%characteristic);return r<0?r+characteristic:r;}
};

int64_t choose(int n,int k){if(k<0||k>n)return 0;k=min(k,n-k);int64_t r=1;for(int j=1;j<=k;++j)r=r*(n-k+j)/j;return r;}

vector<vector<int>> invert_matrix(vector<vector<int>> a,const Field&f) {
  int n=a.size(); vector<vector<int>> b(n,vector<int>(n));for(int i=0;i<n;++i)b[i][i]=1;
  for(int k=0;k<n;++k){int p=k;while(p<n&&!a[p][k])++p;assert(p<n);swap(a[k],a[p]);swap(b[k],b[p]);int iv=f.inv(a[k][k]);
    for(int j=0;j<n;++j){a[k][j]=f.mul(a[k][j],iv);b[k][j]=f.mul(b[k][j],iv);}
    for(int i=0;i<n;++i)if(i!=k&&a[i][k]){int z=a[i][k];for(int j=0;j<n;++j){a[i][j]=f.sub(a[i][j],f.mul(z,a[k][j]));b[i][j]=f.sub(b[i][j],f.mul(z,b[k][j]));}}
  }return b;
}

int determinant(vector<vector<int>> a,const Field&f) {
  int n=a.size(),det=1;
  for(int k=0;k<n;++k){int p=k;while(p<n&&!a[p][k])++p;if(p==n)return 0;if(p!=k){swap(a[p],a[k]);det=f.neg(det);}int pivot=a[k][k];det=f.mul(det,pivot);int iv=f.inv(pivot);
    for(int i=k+1;i<n;++i)if(a[i][k]){int z=f.mul(a[i][k],iv);for(int j=k+1;j<n;++j)a[i][j]=f.sub(a[i][j],f.mul(z,a[k][j]));}
  }return det;
}

int matrix_rank(vector<vector<int>> a,const Field&f) {
  int nr=a.size(),nc=nr?a[0].size():0,r=0;
  if(f.binary) {
    int blocks=(nc+63)/64;vector<vector<uint64_t>>bits(nr,vector<uint64_t>(blocks));
    for(int i=0;i<nr;++i)for(int j=0;j<nc;++j){assert(a[i][j]==0||a[i][j]==1);if(a[i][j])bits[i][j/64]|=uint64_t(1)<<(j%64);}
    for(int c=0;c<nc&&r<nr;++c){int p=r;while(p<nr&&!(bits[p][c/64]>>(c%64)&1))++p;if(p==nr)continue;swap(bits[p],bits[r]);for(int i=r+1;i<nr;++i)if(bits[i][c/64]>>(c%64)&1)for(int b=c/64;b<blocks;++b)bits[i][b]^=bits[r][b];++r;}
    return r;
  }
  for(int c=0;c<nc&&r<nr;++c){int p=r;while(p<nr&&!a[p][c])++p;if(p==nr)continue;swap(a[p],a[r]);int iv=f.inv(a[r][c]);
    for(int i=r+1;i<nr;++i)if(a[i][c]){int z=f.mul(a[i][c],iv);for(int j=c+1;j<nc;++j)a[i][j]=f.sub(a[i][j],f.mul(z,a[r][j]));}++r;
  }return r;
}

struct Symbol {vector<int>I,J;};
void enum_sets(int n,int next,int remaining,vector<int>&a,vector<vector<int>>&out){if(!n){if(!remaining)out.push_back(a);return;}for(int x=next;x<=remaining;++x){if(n*x+n*(n-1)/2>remaining)break;a.push_back(x);enum_sets(n-1,x+1,remaining-x,a,out);a.pop_back();}}
vector<Symbol> symbols(int n,int energy){int sum=energy/2-n;vector<Symbol>out;for(int s=0;s<=sum;++s){vector<vector<int>>a,b;vector<int>tmp;enum_sets(n,0,s,tmp,a);enum_sets(n,0,sum-s,tmp,b);for(auto&i:a)for(auto&j:b)out.push_back({i,j});}return out;}

struct Kernel {
  const Field&f; int x,y,ym1; vector<int>xp;vector<vector<int>>B,C;
  Kernel(const Field&f0,int x0,int mx):f(f0),x(x0),y(f.mul(x,x)),ym1(f.sub(y,1)),xp(2*mx+2,1),B(mx+1,vector<int>(mx+1)),C(B){
    for(int j=1;j<(int)xp.size();++j)xp[j]=f.mul(xp[j-1],x);
    for(int r=0;r<=mx;++r)for(int n=0;n<=mx;++n)for(int j=max(0,n-r);j<=n;++j){int z=f.integer(choose(r,n-j)*choose(r+j,j));if(j&1)z=f.neg(z);B[r][n]=f.add(B[r][n],f.mul(z,f.power(y,j)));C[r][n]=f.add(C[r][n],f.mul(z,f.power(y,n-j)));}
  }
  int entry(int rowparty,int colparty,int i,int j)const {
    // Party order is a,d,c,b, as in the manuscript's block matrix.
    if(rowparty==colparty)return 0;
    if(rowparty==0&&colparty==1)return C[i][j];
    if(rowparty==0&&colparty==2)return i==j?xp[2*i+1]:0;
    if(rowparty==0&&colparty==3)return f.mul(ym1,f.mul(xp[2*i+1],B[i][j]));
    if(rowparty==1&&colparty==0)return f.neg(C[j][i]);
    if(rowparty==1&&colparty==2)return f.mul(xp[2*j+1],B[j][i]);
    if(rowparty==1&&colparty==3)return i==j?f.neg(xp[2*i+1]):0;
    if(rowparty==2&&colparty==0)return i==j?f.neg(xp[2*i+1]):0;
    if(rowparty==2&&colparty==1)return f.neg(f.mul(xp[2*i+1],B[i][j]));
    if(rowparty==2&&colparty==3)return f.neg(f.mul(ym1,C[i][j]));
    if(rowparty==3&&colparty==0)return f.neg(f.mul(ym1,f.mul(xp[2*j+1],B[j][i])));
    if(rowparty==3&&colparty==1)return i==j?xp[2*i+1]:0;
    assert(rowparty==3&&colparty==2);return f.mul(ym1,C[j][i]);
  }
};

int tensor_eval(const array<const Symbol*,4>&s,const Kernel&k,int n){vector<vector<int>>M(4*n,vector<int>(4*n));for(int rp=0;rp<4;++rp)for(int cp=0;cp<4;++cp)for(int r=0;r<n;++r)for(int c=0;c<n;++c)M[rp*n+r][cp*n+c]=k.entry(rp,cp,s[rp]->I[r],s[cp]->J[c]);return determinant(M,k.f);}

int main(int argc,char**argv){
  if(argc!=4&&argc!=5){cerr<<"usage: sh_crossing_ranks SIZE ENERGY FIELD [cumulative|binary-coefficients]\n";return 2;}
  string mode=argc==5?argv[4]:"individual";
  int n=atoi(argv[1]),energy=atoi(argv[2]),p=atoi(argv[3]);assert(n>=1&&energy>0&&energy%2==0);
  Field f(p);auto syms=symbols(n,energy);int q=syms.size();assert(q>0);int mx=0;for(auto&s:syms){mx=max(mx,s.I.back());mx=max(mx,s.J.back());}
  int theta=4*energy,degree=theta+4*n,L=degree+1;assert((p==2&&L<256)||(p>degree));
  vector<Kernel>kernels;for(int x=0;x<L;++x)kernels.emplace_back(f,x,mx);
  vector<vector<int>>V(L,vector<int>(L));for(int i=0;i<L;++i){V[i][0]=1;for(int j=1;j<L;++j)V[i][j]=f.mul(V[i][j-1],i);}auto inverse=invert_matrix(V,f);
  int total=q*q*q*q;vector<vector<int>>coeff(theta+1,vector<int>(total));int tail_bad=0,nonbinary=0,identity_bad=0,extra_bad=0;
  auto index=[q](int a,int b,int c,int d){return ((a*q+b)*q+c)*q+d;};
  Kernel extra(f,L,mx);
  for(int a=0;a<q;++a)for(int b=0;b<q;++b)for(int c=0;c<q;++c)for(int d=0;d<q;++d){
    array<const Symbol*,4>s{&syms[a],&syms[d],&syms[c],&syms[b]};int id=index(a,b,c,d);vector<int>eval(L),co(L);
    for(int x=0;x<L;++x)eval[x]=tensor_eval(s,kernels[x],n);
    for(int k=0;k<L;++k)for(int x=0;x<L;++x)co[k]=f.add(co[k],f.mul(inverse[k][x],eval[x]));
    for(int k=0;k<L;++k){if(k>theta&&co[k])++tail_bad;if(p==2&&co[k]>1)++nonbinary;if(k<=theta)coeff[k][id]=co[k];}
    int at1=0;for(int v:co)at1=f.add(at1,v);
    int expected=(syms[c].J==syms[a].I&&syms[c].I==syms[a].J&&syms[b].J==syms[d].I&&syms[b].I==syms[d].J);
    if(at1!=expected)++identity_bad;
    int ate=0;for(int k=L-1;k>=0;--k)ate=f.add(f.mul(ate,L),co[k]);if(ate!=tensor_eval(s,extra,n))++extra_bad;
  }
  int reflection_bad=0;for(int a=0;a<q;++a)for(int b=0;b<q;++b)for(int c=0;c<q;++c)for(int d=0;d<q;++d)for(int k=0;k<=theta;++k)if(coeff[k][index(a,b,c,d)]!=coeff[theta-k][index(a,d,c,b)])++reflection_bad;
  cout<<"# size="<<n<<" energy="<<energy<<" q="<<q<<" characteristic="<<p<<" theta="<<theta<<" interpolation_degree="<<degree<<"\n";
  cout<<"# tail_bad="<<tail_bad<<" nonbinary="<<nonbinary<<" identity_bad="<<identity_bad<<" extra_bad="<<extra_bad<<" reflection_bad="<<reflection_bad<<"\n";
  if(mode=="binary-coefficients") {
    assert(p==2);cout<<"N\tpacked_hex\n";const char*hex="0123456789abcdef";
    for(int k=0;k<=theta;++k){cout<<k<<'\t';for(int i=0;i<total;i+=4){int v=0;for(int j=0;j<4&&i+j<total;++j)v|=coeff[k][i+j]<<j;cout<<hex[v];}cout<<'\n';}
    return tail_bad||nonbinary||identity_bad||extra_bad||reflection_bad?1:0;
  }
  if(mode=="cumulative") {
    cout<<"K\trank_prefix_ad_bc\trank_tail_ab_cd\trank_prefix_ab_cd\trank_tail_ad_bc\n";
    vector<int>prefix(total),target(total);
    for(int k=0;k<=theta;++k)for(int id=0;id<total;++id)target[id]=f.add(target[id],coeff[k][id]);
    for(int k=0;k<=theta;++k){
      for(int id=0;id<total;++id)prefix[id]=f.add(prefix[id],coeff[k][id]);
      vector<vector<int>>pa(q*q,vector<int>(q*q)),pb=pa,ta=pa,tb=pa;
      for(int a=0;a<q;++a)for(int b=0;b<q;++b)for(int c=0;c<q;++c)for(int d=0;d<q;++d){int id=index(a,b,c,d),v=prefix[id],u=f.sub(target[id],v);pa[a*q+d][b*q+c]=v;pb[a*q+b][c*q+d]=v;ta[a*q+d][b*q+c]=u;tb[a*q+b][c*q+d]=u;}
      cout<<k<<'\t'<<matrix_rank(pa,f)<<'\t'<<matrix_rank(tb,f)<<'\t'<<matrix_rank(pb,f)<<'\t'<<matrix_rank(ta,f)<<'\n';
    }
    return tail_bad||nonbinary||identity_bad||extra_bad||reflection_bad?1:0;
  }
  assert(mode=="individual");
  cout<<"N\trank_ad_bc\trank_ab_cd\trank_ac_bd\n";
  for(int k=0;k<=theta;++k){vector<vector<int>>m1(q*q,vector<int>(q*q)),m2=m1,m3=m1;
    for(int a=0;a<q;++a)for(int b=0;b<q;++b)for(int c=0;c<q;++c)for(int d=0;d<q;++d){int v=coeff[k][index(a,b,c,d)];m1[a*q+d][b*q+c]=v;m2[a*q+b][c*q+d]=v;m3[a*q+c][b*q+d]=v;}
    cout<<k<<'\t'<<matrix_rank(m1,f)<<'\t'<<matrix_rank(m2,f)<<'\t'<<matrix_rank(m3,f)<<'\n';
  }
  return tail_bad||nonbinary||identity_bad||extra_bad||reflection_bad?1:0;
}

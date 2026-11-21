// Exact enumeration from Davis2008 Theorem4.1 proof and Theorem4.16.
// Each matrix is encoded as twice its Gaussian-rational entries.
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <unordered_map>
#include <vector>
using M=std::array<int8_t,32>;
struct Hash { size_t operator()(M const& a) const {size_t h=1469598103934665603ULL;for(auto x:a){h^=uint8_t(x);h*=1099511628211ULL;}return h;} };
M ident(){M a{};for(int j=0;j<4;j++)a[2*(4*j+j)]=2;return a;}
M mul(M const&a,M const&b){M c{};for(int j=0;j<4;j++)for(int k=0;k<4;k++){
 int re=0,im=0;for(int l=0;l<4;l++){int u=2*(4*j+l),v=2*(4*l+k);re+=a[u]*b[v]-a[u+1]*b[v+1];im+=a[u]*b[v+1]+a[u+1]*b[v];}
 if(re%2||im%2||re/2>127||re/2< -128||im/2>127||im/2< -128)throw std::runtime_error("denominator/range assertion");
 c[2*(4*j+k)]=re/2;c[2*(4*j+k)+1]=im/2;
 }return c;}
M star(M a){M b{};for(int j=0;j<4;j++)for(int k=0;k<4;k++){b[2*(4*j+k)]=a[2*(4*k+j)];b[2*(4*j+k)+1]=-a[2*(4*k+j)+1];}return b;}
std::vector<M> seeds(){std::vector<M>s;M a{};for(int j=0;j<4;j++)for(int k=0;k<4;k++)a[2*(4*j+k)]=(j==k?1:-1);s.push_back(a);
 a=ident();a[0]=a[10]=0;a[3]=2;a[9]=-2;s.push_back(a);
 a=ident();a[0]=a[10]=0;a[2]=a[8]=2;s.push_back(a);
 a=ident();a[10]=a[20]=0;a[12]=a[18]=2;s.push_back(a);
 a=ident();a[20]=-2;s.push_back(a);
 for(auto const&g:s)assert(mul(g,g)==ident()&&star(g)==g);return s;}
void print_matrix(std::ostream&o,M const&a){o<<"[";for(int j=0;j<32;j++){if(j)o<<",";o<<int(a[j]);}o<<"]";}
void run(int nr,char const*path){auto ss=seeds();ss.resize(nr);std::vector<M>gs{ident()};std::unordered_map<M,int,Hash>index;index.emplace(gs[0],0);
 for(size_t p=0;p<gs.size();p++){M g=gs[p];for(auto const&s:ss){M b=mul(g,s);if(!index.count(b)){index.emplace(b,int(gs.size()));gs.push_back(b);}}}
 assert(gs.size()==(nr==4?7680:46080));for(auto const&g:gs)assert(mul(star(g),g)==ident());
 std::vector<char>seen(gs.size());int nc=0,covered=0;std::ofstream o(path);o<<"{\"matrix_encoding\":\"2g, real and imaginary entries interleaved row-major\",\"group_order\":"<<gs.size()<<",\"generator_count\":"<<nr<<",\"generators\":[";
 for(int j=0;j<nr;j++){if(j)o<<",";print_matrix(o,ss[j]);}o<<"],\"classes\":[";
 for(size_t p=0;p<gs.size();p++)if(!seen[p]){if(nc++)o<<",";seen[p]=1;std::queue<int>q;q.push(p);int count=0;
  while(!q.empty()){int j=q.front();q.pop();count++;for(auto const&s:ss){M b=mul(s,mul(gs[j],s));int v=index.at(b);if(!seen[v]){seen[v]=1;q.push(v);}}}
  M z=ident();int ord=0;do{z=mul(z,gs[p]);ord++;assert(ord<=192);}while(z!=ident());
  o<<"{\"index\":"<<nc<<",\"size\":"<<count<<",\"order\":"<<ord<<",\"representative\":";print_matrix(o,gs[p]);o<<"}";covered+=count;
 }
 assert(covered==int(gs.size()));o<<"],\"class_count\":"<<nc<<",\"all_exact_unitarity_checks_pass\":true}\n";
 std::cout<<"G"<<(nr==4?29:31)<<": order="<<gs.size()<<", classes="<<nc<<", all exact matrix checks PASS\n";
}
int main(int argc,char**argv){if(argc!=3){std::cerr<<"usage: enumerate_gaussian_groups G29.json G31.json\n";return 1;}run(4,argv[1]);run(5,argv[2]);}

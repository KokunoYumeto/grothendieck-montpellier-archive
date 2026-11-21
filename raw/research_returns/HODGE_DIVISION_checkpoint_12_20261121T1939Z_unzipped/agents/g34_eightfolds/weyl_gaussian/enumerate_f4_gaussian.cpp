// Exact enumeration of the Gaussian unitary normalizer of the F4 root lines.
// Stores twice every Gaussian matrix; no external group library is used.
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
struct Hash{size_t operator()(M const&a)const{size_t h=1469598103934665603ULL;for(auto x:a){h^=uint8_t(x);h*=1099511628211ULL;}return h;}};
M ident(){M a{};for(int j=0;j<4;j++)a[2*(4*j+j)]=2;return a;}
M mul(M const&a,M const&b){M c{};for(int j=0;j<4;j++)for(int k=0;k<4;k++){
 int re=0,im=0;for(int l=0;l<4;l++){int u=2*(4*j+l),v=2*(4*l+k);re+=a[u]*b[v]-a[u+1]*b[v+1];im+=a[u]*b[v+1]+a[u+1]*b[v];}
 if(re%2||im%2||re/2>127||re/2< -128||im/2>127||im/2< -128)throw std::runtime_error("denominator/range assertion");
 c[2*(4*j+k)]=re/2;c[2*(4*j+k)+1]=im/2;
 }return c;}
M star(M const&a){M b{};for(int j=0;j<4;j++)for(int k=0;k<4;k++){b[2*(4*j+k)]=a[2*(4*k+j)];b[2*(4*j+k)+1]=-a[2*(4*k+j)+1];}return b;}
std::vector<M>seeds(){std::vector<M>s;M a;
 for(int j=1;j<=2;j++){a=ident();a[2*(4*j+j)]=a[2*(4*(j+1)+j+1)]=0;a[2*(4*j+j+1)]=a[2*(4*(j+1)+j)]=2;s.push_back(a);}
 a=ident();a[30]=-2;s.push_back(a);
 int v[4]={1,-1,-1,-1};a={};for(int j=0;j<4;j++)for(int k=0;k<4;k++)a[2*(4*j+k)]=2*(j==k)-v[j]*v[k];s.push_back(a);
 int phi[16]={0,-1,-1,0,1,0,0,1,1,0,0,-1,0,-1,1,0};a={};for(int j=0;j<16;j++)a[2*j]=a[2*j+1]=phi[j];s.push_back(a);
 for(auto const&g:s)assert(mul(star(g),g)==ident());return s;
}
void print_matrix(std::ostream&o,M const&a){o<<'[';for(int j=0;j<32;j++){if(j)o<<',';o<<int(a[j]);}o<<']';}
int main(int argc,char**argv){if(argc!=2){std::cerr<<"usage: enumerate_f4_gaussian output.json\n";return 1;}
 auto ss=seeds();std::vector<M>gs{ident()};std::unordered_map<M,int,Hash>index;index.emplace(gs[0],0);
 for(size_t p=0;p<gs.size();p++){M a=gs[p];for(auto const&s:ss){M b=mul(a,s);if(!index.count(b)){index.emplace(b,int(gs.size()));gs.push_back(b);}}}
 assert(gs.size()==4608);for(auto const&a:gs)assert(mul(star(a),a)==ident());
 std::ofstream o(argv[1]);o<<"{\"group_order\":4608,\"matrix_encoding\":\"2g real/imag interleaved row-major\",\"generators\":[";
 for(size_t j=0;j<ss.size();j++){if(j)o<<',';print_matrix(o,ss[j]);}o<<"],\"classes\":[";
 std::vector<char>seen(gs.size());int nc=0,covered=0;
 for(size_t p=0;p<gs.size();p++)if(!seen[p]){if(nc++)o<<',';seen[p]=1;std::queue<int>q;q.push(p);int count=0;
  while(!q.empty()){int j=q.front();q.pop();count++;for(auto const&s:ss){M b=mul(s,mul(gs[j],star(s)));int v=index.at(b);if(!seen[v]){seen[v]=1;q.push(v);}}}
  M a=ident();int ord=0;do{a=mul(a,gs[p]);ord++;assert(ord<=192);}while(a!=ident());
  o<<"{\"index\":"<<nc<<",\"size\":"<<count<<",\"order\":"<<ord<<",\"representative\":";print_matrix(o,gs[p]);o<<'}';covered+=count;
 }
 assert(covered==4608);o<<"],\"class_count\":"<<nc<<",\"all_exact_checks\":true}\n";
 std::cout<<"F4 Gaussian normalizer: order4608, classes"<<nc<<", exact enumeration PASS\n";
}

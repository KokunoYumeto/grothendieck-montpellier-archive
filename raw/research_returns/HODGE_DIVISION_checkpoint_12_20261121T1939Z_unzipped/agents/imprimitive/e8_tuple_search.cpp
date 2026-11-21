// Exact search in the conjugacy orbit of a square root of -I in W(E8).
// Input: Cartan matrix, representative j, then labelled simple-root words.
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using Mat=std::array<int,64>;
struct Hash {size_t operator()(Mat const&a)const{size_t h=1469598103934665603ULL;for(int z:a){h^=uint32_t(z);h*=1099511628211ULL;}return h;}};
Mat eye(){Mat a{};for(int i=0;i<8;i++)a[8*i+i]=1;return a;}
Mat mul(Mat const&a,Mat const&b){Mat c{};for(int i=0;i<8;i++)for(int j=0;j<8;j++){long long t=0;for(int k=0;k<8;k++)t+=(long long)a[8*i+k]*b[8*k+j];assert(t<1000000&&t> -1000000);c[8*i+j]=int(t);}return c;}
Mat neg(Mat a){for(auto&z:a)z=-z;return a;}
int trace(Mat const&a){int t=0;for(int i=0;i<8;i++)t+=a[8*i+i];return t;}
void emit(std::ostream&o,Mat const&a){o<<'[';for(int i=0;i<64;i++){if(i)o<<',';o<<a[i];}o<<']';}
std::array<long long,9> elementary(Mat const&a){std::array<long long,9>e{},p{};e[0]=1;Mat b=eye();for(int k=1;k<=8;k++){b=mul(b,a);p[k]=trace(b);long long z=0;for(int i=1;i<=k;i++)z+=(i%2?1:-1)*e[k-i]*p[i];assert(z%k==0);e[k]=z/k;}return e;}
int target(Mat const&w){int t=trace(w);if(t!=1&&t!=-1)return 0;Mat w2=mul(w,w);if(trace(w2)!=3)return 0;auto e=elementary(w);std::array<long long,9>expected{1,t,-1,0,2,0,-1,t,1};if(e!=expected)return 0;Mat p=eye();for(int i=0;i<12;i++)p=mul(p,w);assert(p==eye());return t==1?57:58;}
int main(int argc,char**argv){assert(argc==3);std::ifstream f(argv[1]);Mat H,j0;for(auto&z:H)f>>z;for(auto&z:j0)f>>z;assert(mul(j0,j0)==neg(eye()));std::vector<Mat>ss;for(int i=0;i<8;i++){Mat s=eye();for(int k=0;k<8;k++)s[8*i+k]-=H[8*i+k];assert(mul(s,s)==eye());ss.push_back(s);}
 std::vector<Mat>orbit{j0};std::vector<int>parent{-1},edge{-1};std::unordered_map<Mat,int,Hash>seen;seen[j0]=0;
 for(size_t p=0;p<orbit.size();p++){Mat a=orbit[p];for(int i=0;i<8;i++){Mat b=mul(ss[i],mul(a,ss[i]));if(!seen.count(b)){seen[b]=orbit.size();orbit.push_back(b);parent.push_back(p);edge.push_back(i+1);}}}
 assert(orbit.size()==15120);for(auto const&j:orbit)assert(mul(j,j)==neg(eye()));std::cerr<<"j orbit exact size "<<orbit.size()<<'\n';
 int count;f>>count;std::ofstream out(argv[2]);out<<"{\"orbit_size\":"<<orbit.size()<<",\"searches\":[";
 for(int mode=0;mode<count;mode++){std::string label;int len;f>>label>>len;std::vector<int>word(len);for(auto&z:word)f>>z;Mat c=eye(),ci=eye();for(int z:word)c=mul(c,ss[z-1]);for(auto it=word.rbegin();it!=word.rend();++it)ci=mul(ci,ss[*it-1]);assert(mul(c,ci)==eye());if(mode)out<<',';out<<"{\"label\":\""<<label<<"\",\"word\":[";for(int i=0;i<len;i++){if(i)out<<',';out<<word[i];}out<<"],\"c\":";emit(out,c);out<<",\"matches\":[";int matches=0;
  for(size_t k=0;k<orbit.size();k++){Mat w=mul(orbit[k],ci);int cl=target(w);if(!cl)continue;if(matches++)out<<',';std::vector<int>path;for(int z=k;parent[z]>=0;z=parent[z])path.push_back(edge[z]);out<<"{\"orbit_index\":"<<k<<",\"spectral_class\":"<<cl<<",\"conjugations\":[";for(int a=path.size()-1;a>=0;a--){if(a!=int(path.size())-1)out<<',';out<<path[a];}out<<"],\"j\":";emit(out,orbit[k]);out<<",\"w\":";emit(out,w);out<<'}';}
  out<<"],\"match_count\":"<<matches<<'}';std::cerr<<label<<": "<<matches<<" matches\n";
 }
 out<<"],\"all_exact_checks_pass\":true}\n";
}

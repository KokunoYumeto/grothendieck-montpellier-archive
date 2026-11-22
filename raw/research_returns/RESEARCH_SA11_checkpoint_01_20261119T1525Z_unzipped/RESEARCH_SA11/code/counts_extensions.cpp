#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
using namespace std;
struct Term {int a,sa,b,sb,c;};
int main(){
 int m,nr,nz;cin>>m>>nr>>nz;
 vector<array<Term,3>> r(nr);
 for(auto &rel:r)for(auto &t:rel)cin>>t.a>>t.sa>>t.b>>t.sb>>t.c;
 vector<vector<int>> zsets(nz);
 for(auto &z:zsets){int k;cin>>k;z.resize(k);for(int &i:z)cin>>i;}
 vector<int>s(m),active;
 for(auto &z:zsets){
  fill(s.begin(),s.end(),1);for(int i:z)s[i]=0;
  active.clear();for(int i=0;i<m;++i)if(s[i])active.push_back(i);
  for(uint64_t mask=0;mask<(uint64_t(1)<<(active.size()-1));++mask){
   s[active[0]]=1;for(int j=1;j<(int)active.size();++j)s[active[j]]=(mask>>(j-1)&1)?1:-1;
   bool okay=true;
   for(auto &rel:r){
    int signs=0;
    for(auto &t:rel){int v=t.sa*t.sb*t.c*(t.a<0?1:s[t.a])*(t.b<0?1:s[t.b]);if(v>0)signs|=1;if(v<0)signs|=2;}
    if(signs==1||signs==2){okay=false;break;}
   }
   if(okay){for(int j=0;j<m;++j)cout<<s[j]<<(j+1==m?'\n':' ');}
  }
 }
}

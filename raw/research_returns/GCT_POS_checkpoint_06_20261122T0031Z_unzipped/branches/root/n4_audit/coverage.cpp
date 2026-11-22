// Independent coverage check: expand certificate orbits, then check every
// normalized raw spectral triple; no minimization/key algorithm is reused.
#include <array>
#include <vector>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
#include <stdexcept>
using Quad = std::array<int,4>;
using Triple = std::array<Quad,3>;
uint64_t key(Triple a) {
  for (auto& row:a) std::sort(row.begin(),row.end());
  std::sort(a.begin(),a.end());
  uint64_t k=0;
  for(int j=0;j<3;++j)for(int i=0;i<4;++i) k=(k<<4)|a[j][i];
  return k;
}
int main() {
  std::vector<Quad> spectra;
  for(int i=0;i<16;++i)for(int j=i;j<16;++j)for(int k=j;k<16;++k)
    spectra.push_back({0,i,j,k});
  for(int order: {8,16}) {
    std::set<uint64_t> expanded;
    std::ifstream in("deliverables/branches/kronecker/m16_chi"+std::to_string(order)+"_spectra.txt");
    Triple a; int records=0;
    while(in>>a[0][0]) {
      for(int j=0;j<3;++j)for(int i=0;i<4;++i)if(j||i)in>>a[j][i];
      ++records;
      for(int u=1;u<16;u+=2)if((u*(16/order))%16==16/order)
      for(int x:a[0])for(int y:a[1])for(int z:a[2])if((x+y+z)%16==0) {
        Triple b=a; int shift[3]={x,y,z};
        for(int j=0;j<3;++j)for(int i=0;i<4;++i)b[j][i]=(u*(b[j][i]-shift[j])+256)%16;
        expanded.insert(key(b));
      }
    }
    uint64_t checked=0;
    for(size_t i=0;i<spectra.size();++i)for(size_t j=i;j<spectra.size();++j)
    for(size_t k=j;k<spectra.size();++k) {
      Triple b={spectra[i],spectra[j],spectra[k]}; int total=0;
      for(auto& row:b)for(int x:row)total+=x;
      if(total%16 != 16/order)continue;
      bool cover[3][4]={};
      for(int p=0;p<4;++p)for(int q=0;q<4;++q)for(int r=0;r<4;++r)
        if((b[0][p]+b[1][q]+b[2][r])%16==0)cover[0][p]=cover[1][q]=cover[2][r]=true;
      bool all=true; for(auto& row:cover)for(bool v:row)all=all&&v;
      if(!all)continue;
      ++checked;
      if(!expanded.count(key(b)))throw std::runtime_error("Uncovered spectrum");
    }
    std::cout << "character_order=" << order << " records=" << records
              << " orbit_expansion=" << expanded.size() << " normalized_cases=" << checked << " PASS\n";
  }
}

// Complete refinement of feasible spectral multisets at a prescribed
// determinant exponent.  The target may be zero or nonprimitive.
// n <= 5; M a power of two <= 64.  No feasibility decisions occur here.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
using Factor = array<uint8_t,5>;
using Weights = array<Factor,3>;
struct Hash {
  size_t operator()(const Weights& x) const {
    uint64_t h=1469598103934665603ULL;
    for (auto a:x) for (auto v:a) {h^=v;h*=1099511628211ULL;}
    return h;
  }
};
int n,M,target;
vector<int> normalizers[64];
unordered_set<Weights,Hash> seen;
uint64_t raw=0,covered=0;

void consider(const Weights& W) {
  ++raw;
  int d=0;
  for(auto a:W)for(int i=0;i<n;++i)d+=a[i];
  d%=M;
  if(normalizers[d].empty())return;
  vector<int> values[3];
  for(int a=0;a<3;++a)for(int i=0;i<n;++i)
    if(i==0||W[a][i]!=W[a][i-1])values[a].push_back(W[a][i]);
  vector<array<int,3>> edges;
  int cover[3]={0,0,0};
  for(int i=0;i<(int)values[0].size();++i)
   for(int j=0;j<(int)values[1].size();++j)
    for(int k=0;k<(int)values[2].size();++k)
     if((values[0][i]+values[1][j]+values[2][k])%M==0) {
       edges.push_back({i,j,k});cover[0]|=1<<i;cover[1]|=1<<j;cover[2]|=1<<k;
     }
  for(int a=0;a<3;++a)if(cover[a]!=(1<<(int)values[a].size())-1)return;
  ++covered;
  Weights best;for(auto& a:best)a.fill(255);
  for(int u:normalizers[d]) {
    Factor shifted[3][5];
    for(int a=0;a<3;++a)for(int j=0;j<(int)values[a].size();++j) {
      shifted[a][j].fill(0);
      for(int i=0;i<n;++i)shifted[a][j][i]=((W[a][i]-values[a][j]+M)*u)%M;
      sort(shifted[a][j].begin(),shifted[a][j].begin()+n);
    }
    for(auto edge:edges) {
      Weights candidate={shifted[0][edge[0]],shifted[1][edge[1]],shifted[2][edge[2]]};
      sort(candidate.begin(),candidate.end());
      if(candidate<best)best=candidate;
    }
  }
  seen.insert(best);
}

vector<Factor> refinements(const Factor& old) {
  vector<pair<int,int>> mult;
  for(int i=0;i<n;++i) {
    if(mult.empty()||mult.back().first!=old[i])mult.push_back({old[i],1});
    else ++mult.back().second;
  }
  vector<Factor> out;
  Factor f;f.fill(0);
  function<void(int,int)> visit=[&](int j,int pos) {
    if(j==(int)mult.size()) {
      Factor sorted=f;sort(sorted.begin(),sorted.begin()+n);out.push_back(sorted);return;
    }
    auto [r,count]=mult[j];
    for(int high=0;high<=count;++high) {
      for(int k=0;k<count;++k)f[pos+k]=r+(k<high?M/2:0);
      visit(j+1,pos+count);
    }
  };
  visit(0,0);return out;
}

int main(int argc,char** argv) {
  if(argc!=7)return 2;
  n=stoi(argv[1]);M=stoi(argv[2]);target=stoi(argv[3])%M;
  if(n<2||n>5||M<2||M>64||(M&(M-1)))return 3;
  for(int d=0;d<M;++d)for(int u=1;u<M;u+=2)
    if(u*d%M==target)normalizers[d].push_back(u);
  string input=argv[4];
  if(input=="BASE") {
    vector<Factor> factors;
    for(int ones=0;ones<n;++ones) {
      Factor f;f.fill(0);for(int i=n-ones;i<n;++i)f[i]=1;factors.push_back(f);
    }
    for(int a=0;a<n;++a)for(int b=a;b<n;++b)for(int c=b;c<n;++c)
      consider({factors[a],factors[b],factors[c]});
  } else {
    ifstream file(input);int first;
    while(file>>first) {
      Weights W;for(auto& a:W)a.fill(0);W[0][0]=first;
      for(int a=0;a<3;++a)for(int i=0;i<n;++i)
        if(a||i){int v;if(!(file>>v))return 4;W[a][i]=v;}
      auto A=refinements(W[0]),B=refinements(W[1]),C=refinements(W[2]);
      for(auto a:A)for(auto b:B)for(auto c:C)consider({a,b,c});
    }
  }
  vector<Weights> sorted(seen.begin(),seen.end());sort(sorted.begin(),sorted.end());
  ofstream out(argv[5]);
  for(auto W:sorted){for(int a=0;a<3;++a)for(int i=0;i<n;++i)out<<int(W[a][i])<<' ';out<<'\n';}
  ofstream stats(argv[6]);
  stats<<"{\"raw_refinements\":"<<raw<<",\"covered_refinements\":"<<covered<<",\"orbits\":"<<seen.size()<<"}\n";
  cout<<"GENERATED "<<n<<' '<<M<<" target "<<target<<" raw "<<raw<<" covered "<<covered<<" orbits "<<seen.size()<<endl;
}

// Exact Weyl coefficient for det^6 in Lambda^14(Lambda^3 C^7).
// Equivalently f_9(7), by omega and exterior duality.
// Integer arithmetic only. Compile: g++ -O3 -std=c++17 exact_exterior_7.cpp -o exterior7
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <vector>

template<size_t N> uint64_t key(std::array<int,N> a) {
  std::sort(a.begin(),a.end());
  uint64_t z=0; for(int d:a) z=(z<<4)|d; return z;
}
long long fact(int n) {long long z=1; for(int i=2;i<=n;++i)z*=i; return z;}

int main() {
  // Every three-uniform simple hypergraph on six labeled vertices.
  std::vector<std::array<int,3>> triples;
  for(int i=0;i<6;++i)for(int j=i+1;j<6;++j)for(int k=j+1;k<6;++k)
    triples.push_back({i,j,k});
  assert(triples.size()==20);
  std::unordered_map<uint64_t,long long> orbit_counts;
  std::array<int,6> deg{};
  unsigned prev=0;
  for(unsigned i=0;i<(1u<<20);++i) {
    unsigned gray=i^(i>>1);
    if(i) {
      unsigned change=gray^prev; int edge=__builtin_ctz(change);
      int sign=(gray&change)?1:-1;
      for(int v:triples[edge])deg[v]+=sign;
    }
    ++orbit_counts[key(deg)]; prev=gray;
  }
  std::unordered_map<uint64_t,long long> labeled_counts;
  for(auto [k,count]:orbit_counts) {
    uint64_t tmp=k; std::array<int,11> freq{};
    for(int i=0;i<6;++i){++freq[tmp&15];tmp>>=4;}
    long long orbit=720;for(int x:freq)orbit/=fact(x);
    assert(count%orbit==0);labeled_counts[k]=count/orbit;
  }

  // For the triples containing vertex0, their other ends form a
  // simple graph on the six remaining vertices. Store every subset.
  std::vector<std::array<int,2>> pairs;
  for(int i=0;i<6;++i)for(int j=i+1;j<6;++j)pairs.push_back({i,j});
  std::array<std::vector<std::array<int,6>>,16> graph_degrees;
  deg.fill(0);prev=0;int edges=0;
  for(unsigned i=0;i<(1u<<15);++i) {
    unsigned gray=i^(i>>1);
    if(i) {
      unsigned change=gray^prev;int edge=__builtin_ctz(change);
      int sign=(gray&change)?1:-1;edges+=sign;
      for(int v:pairs[edge])deg[v]+=sign;
    }
    graph_degrees[edges].push_back(deg);prev=gray;
  }
  auto weight_multiplicity=[&](std::array<int,7> target) {
    std::sort(target.begin(),target.end());
    if(target[0]<0||target[6]>15)return 0LL;
    long long count=0;
    for(const auto &gd:graph_degrees[target[0]]) {
      std::array<int,6> rem{};bool valid=true;
      for(int i=0;i<6;++i){rem[i]=target[i+1]-gd[i];if(rem[i]<0||rem[i]>10){valid=false;break;}}
      if(valid){auto it=labeled_counts.find(key(rem));if(it!=labeled_counts.end())count+=it->second;}
    }
    return count;
  };

  // Coefficient of x^(lambda+rho) in ch(V) det(x_i^(rho_j)).
  std::array<int,7> perm{0,1,2,3,4,5,6};
  std::map<std::array<int,7>,long long> signed_orbits;
  do {
    int inv=0;for(int i=0;i<7;++i)for(int j=i+1;j<7;++j)inv+=(perm[i]>perm[j]);
    std::array<int,7> target{};
    for(int i=0;i<7;++i)target[i]=6+perm[i]-i;
    std::sort(target.begin(),target.end());
    signed_orbits[target]+=(inv%2?-1:1);
  }while(std::next_permutation(perm.begin(),perm.end()));
  long long answer=0,terms=0;
  std::cout<<"degree_sequence\tsigned_coefficient\tweight_multiplicity\tcontribution\n";
  for(auto [target,sign]:signed_orbits)if(sign) {
    long long count=weight_multiplicity(target);answer+=sign*count;++terms;
    for(int i=0;i<7;++i)std::cout<<(i?",":"")<<target[i];
    std::cout<<"\t"<<sign<<"\t"<<count<<"\t"<<sign*count<<"\n";
  }
  std::cerr<<"six_vertex_orbits="<<orbit_counts.size()<<" signed_orbits="<<terms
           <<" f_9(7)="<<answer<<"\n";
  assert(answer>=0);
}

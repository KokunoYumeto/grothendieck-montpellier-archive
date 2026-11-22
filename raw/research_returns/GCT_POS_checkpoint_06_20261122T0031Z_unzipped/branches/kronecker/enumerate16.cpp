#include <array>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <chrono>
using namespace std;
using A4=array<int,4>;
int main(){
 vector<A4> a;vector<uint16_t> masks;vector<int> sums;
 for(int b=0;b<16;b++)for(int c=b;c<16;c++)for(int d=c;d<16;d++){
  A4 x{0,b,c,d};a.push_back(x);uint16_t m=0;int s=0;for(int v:x){m|=1u<<v;s+=v;}masks.push_back(m);sums.push_back(s%16);
 }
 int N=a.size();vector<uint16_t> pairneg(N*N);
 for(int i=0;i<N;i++)for(int j=0;j<N;j++){uint16_t m=0;for(int u:a[i])for(int v:a[j])m|=1u<<((-u-v)&15);pairneg[i*N+j]=m;}
 vector<array<array<uint16_t,16>,8>> shifted(N);
 for(int i=0;i<N;i++)for(int k=0;k<8;k++)for(int b=0;b<16;b++){
  A4 x;for(int j=0;j<4;j++)x[j]=((2*k+1)*(a[i][j]-b))&15;sort(x.begin(),x.end());uint16_t p=0;for(int j=0;j<4;j++)p|=x[j]<<(4*j);shifted[i][k][b]=p;
 }
 unordered_set<uint64_t> keys8,keys16;keys8.reserve(100000);keys16.reserve(100000);
 uint64_t covered8=0,covered16=0;auto start=chrono::steady_clock::now();
 for(int i=0;i<N;i++){
  for(int j=i;j<N;j++){
   uint16_t nc=pairneg[i*N+j];
   for(int k=j;k<N;k++){
    int d=(sums[i]+sums[j]+sums[k])&15;if(!(d&1) && (d&3)!=2)continue;
    if(masks[k]&~nc)continue;
    if(masks[i]&~pairneg[j*N+k])continue;
    if(masks[j]&~pairneg[i*N+k])continue;
    int target=(d&1)?1:2;
    uint64_t best=UINT64_MAX;
    for(int u=1;u<16;u+=2){
     if((u*d&15)!=target)continue;int ui=(u-1)/2;
     for(int x:a[i])for(int y:a[j]){
      int z=(-x-y)&15;if(!(masks[k]&(1u<<z)))continue;
      array<uint16_t,3> v{shifted[i][ui][x],shifted[j][ui][y],shifted[k][ui][z]};sort(v.begin(),v.end());
      uint64_t key=uint64_t(v[0]) | (uint64_t(v[1])<<16) | (uint64_t(v[2])<<32);best=min(best,key);
     }
    }
    if(target==1){covered16++;keys16.insert(best);}else{covered8++;keys8.insert(best);}
   }
  }
  if(i%40==0)cerr<<"progress "<<i<<"/"<<N<<" orbits χ8="<<keys8.size()<<" χ16="<<keys16.size()<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
 }
 for(int target:{8,16}){
  auto& data=target==8?keys8:keys16;vector<uint64_t> sorted(data.begin(),data.end());sort(sorted.begin(),sorted.end());
  ofstream out("deliverables/branches/kronecker/m16_chi"+to_string(target)+"_spectra.txt");
  for(uint64_t key:sorted){for(int j=0;j<3;j++)for(int l=0;l<4;l++)out<<((key>>(16*j+4*l))&15)<<" ";out<<"\n";}
 }
 cout<<"spectra="<<N<<" covered χ8="<<covered8<<" χ16="<<covered16<<" orbits χ8="<<keys8.size()<<" χ16="<<keys16.size()<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}

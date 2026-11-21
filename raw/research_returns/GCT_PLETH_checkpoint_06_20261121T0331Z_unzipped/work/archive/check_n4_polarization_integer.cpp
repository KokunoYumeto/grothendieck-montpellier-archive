#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
#include <string>
using Exact=__int128_t;
std::string decimal(Exact value){
  if(!value)return "0";
  bool negative=value<0;if(negative)value=-value;
  std::string text;
  while(value){text.push_back('0'+value%10);value/=10;}
  if(negative)text.push_back('-');
  std::reverse(text.begin(),text.end());return text;
}
using Row=std::array<int64_t,4>;
int main(){
  std::array<Row,32> rows{};
  std::array<int,32> signs{};
  for(int mask=0;mask<32;++mask){
    int bits=0;
    for(int j=1;j<=5;++j)if(mask&(1<<(j-1))){
      ++bits;int64_t power=1;
      for(int col=0;col<4;++col){rows[mask][col]+=power;power*=j;}
    }
    signs[mask]=(bits%2?-1:1);
  }
  std::array<std::array<int64_t,32>,32> two{};
  for(int a=0;a<32;++a)for(int b=0;b<32;++b)
    two[a][b]=rows[a][0]*rows[b][1]-rows[a][1]*rows[b][0];
  std::vector<int64_t> three(4*32*32*32);
  auto at=[&](int omit,int a,int b,int c)->int64_t&{
    return three[((omit*32+a)*32+b)*32+c];
  };
  for(int omit=0;omit<4;++omit){
    std::array<int,3> cols{};int r=0;
    for(int col=0;col<4;++col)if(col!=omit)cols[r++]=col;
    for(int a=0;a<32;++a)for(int b=0;b<32;++b)for(int c=0;c<32;++c){
      std::array<int,3> p{0,1,2};int64_t value=0;
      do{
        int inversions=0;for(int i=0;i<3;++i)for(int j=i+1;j<3;++j)inversions+=p[i]>p[j];
        int64_t term=rows[a][cols[p[0]]]*rows[b][cols[p[1]]]*rows[c][cols[p[2]]];
        value+=(inversions%2?-term:term);
      }while(std::next_permutation(p.begin(),p.end()));
      at(omit,a,b,c)=value;
    }
  }
  Exact total=0;uint64_t visited=0,nonzero=0;int64_t maxdet=0;
  for(int a=0;a<32;++a)for(int b=0;b<32;++b)for(int c=0;c<32;++c)for(int d=0;d<32;++d){
    ++visited;
    if(!rows[a][0]||!rows[d][0]||!two[a][b]||!two[c][d]||!at(3,b,c,d)||!at(3,a,b,c))continue;
    int64_t determinant=0;
    for(int j=0;j<4;++j)determinant+=(j%2?-1:1)*rows[a][j]*at(j,b,c,d);
    if(!determinant)continue;
    ++nonzero;maxdet=std::max(maxdet,std::abs(determinant));
    Exact term=rows[a][0];
    term*=rows[d][0];term*=two[a][b];term*=two[c][d];
    term*=at(3,b,c,d);term*=at(3,a,b,c);
    term*=determinant;term*=determinant;
    total+=signs[a]*signs[b]*signs[c]*signs[d]*term;
  }
  Exact mod=total%1000003;if(mod<0)mod+=1000003;
  std::cout<<"boolean_points "<<visited<<"\nnonzero_integer_summands "<<nonzero
           <<"\nmax_abs_determinant "<<maxdet<<"\ncoefficient_integer "<<decimal(total)
           <<"\ncoefficient_mod_1000003 "<<decimal(mod)<<"\n";
}

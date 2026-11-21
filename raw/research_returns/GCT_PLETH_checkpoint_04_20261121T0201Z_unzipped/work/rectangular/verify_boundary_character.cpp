#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
    assert(argc==2);
    const int b=15,N=60,base=61,grid=base*base*base;
    vector<vector<long long>> h(5,vector<long long>(grid));h[0][0]=1;
    auto idx=[&](int x,int y,int z){return x+base*y+base*base*z;};
    // Multiply the 816 factors (1-t*x^w)^(-1), truncating t at degree4.
    // Ascending t-degree permits repeated use of the current monomial.
    for(int u=0;u<=b;u++)for(int v=0;v<=b-u;v++)for(int w=0;w<=b-u-v;w++){
        for(int j=1;j<=4;j++){
            int total=(j-1)*b;
            for(int x=0;x<=total;x++)for(int y=0;y<=total-x;y++)
                for(int z=0;z<=total-x-y;z++){
                    long long c=h[j-1][idx(x,y,z)];
                    if(c)h[j][idx(x+u,y+v,z+w)]+=c;
                }
        }
    }
    map<array<int,4>,long long> supplied;
    ifstream in(argv[1]);string line;getline(in,line);
    while(getline(in,line)){
        replace(line.begin(),line.end(),',',' ');stringstream s(line);
        array<int,4>lam;long long m;
        s>>lam[0]>>lam[1]>>lam[2]>>lam[3]>>m;
        supplied[lam]=m;
    }
    int blocks=0,maxmult=0;long long summult=0,dim=0;
    for(int a=N;a>=0;a--)for(int c=min(a,N-a);c>=0;c--)
    for(int d=min(c,N-a-c);d>=0;d--){
        int e=N-a-c-d;if(e<0||e>d)continue;
        array<int,4>lam{a,c,d,e},rho{3,2,1,0},p{0,1,2,3};
        long long m=0;
        do{
            int sg=1;array<int,4>w{};bool valid=true;
            for(int i=0;i<4;i++){
                w[i]=lam[i]+rho[i]-rho[p[i]];
                if(w[i]<0||w[i]>N)valid=false;
                for(int j=i+1;j<4;j++)if(p[i]>p[j])sg=-sg;
            }
            if(valid)m+=sg*h[4][idx(w[0],w[1],w[2])];
        }while(next_permutation(p.begin(),p.end()));
        assert(m>=0);
        if(m){
            assert(supplied.count(lam)&&supplied.at(lam)==m);
            supplied.erase(lam);blocks++;summult+=m;maxmult=max(maxmult,(int)m);
            long long numerator=1;
            for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)numerator*=lam[i]-lam[j]+j-i;
            assert(numerator%12==0);dim+=m*(numerator/12);
        }
    }
    assert(supplied.empty());
    long long fullweightdim=accumulate(h[4].begin(),h[4].end(),0LL);
    assert(dim==fullweightdim&&dim==18609648876LL);
    cout<<"PASS independent product-character DP: blocks="<<blocks
        <<" multiplicity_sum="<<summult<<" max_multiplicity="<<maxmult
        <<" source_dimension="<<dim<<"\n";
}

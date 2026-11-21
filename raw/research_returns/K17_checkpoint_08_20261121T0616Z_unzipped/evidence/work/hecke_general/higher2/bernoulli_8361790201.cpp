// Exact B_(p-19) mod p. Voronoi multiplier 2; primitive enumerator 19.
// The two roles are deliberately separate. No residue uses floating point.
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
using u64=std::uint64_t;
using u128=unsigned __int128;
constexpr u64 P=8361790201ULL, H=19, N=P-19, COUNT=(P-1)/2;
constexpr u64 inverse(u64 a) {
    u64 x=1;
    for(unsigned i=0;i<6;++i) x*=2-a*x;
    return x;
}
constexpr u64 NEG=0-inverse(P), R=(u128(1)<<64)%P;
inline u64 mont(u64 a,u64 b) {
    const u128 t=u128(a)*b;
    const u64 m=u64(t)*NEG;
    const u64 u=u64((t+u128(m)*P)>>64);
    return u-P*(u>=P);
}
u64 mul(u64 a,u64 b) {return u128(a)*b%P;}
u64 power(u64 a,u64 n) {
    u64 z=1;
    while(n) {
        if(n&1) z=mul(z,a);
        a=mul(a,a); n>>=1;
    }
    return z;
}
bool prime(u64 n) {
    if(n<2) return false;
    if(n%2==0) return n==2;
    for(u64 d=3;d<=n/d;d+=2) if(n%d==0) return false;
    return true;
}
int main() {
    assert(prime(P));
    assert(8ULL*9*25*167*27817==P-1);
    for(u64 q:{2ULL,3ULL,5ULL,167ULL,27817ULL}) {
        assert(prime(q));
        assert(power(H,(P-1)/q)!=1);
    }
    assert(power(H,P-1)==1);
    assert(P*NEG==u64(-1));
    assert(mont(R,1)==1);
    const u64 probes[]={0,1,2,P-1,P-2,P/2,123456789,987654321};
    for(u64 a:probes) for(u64 b:probes)
        assert(mont(mul(a,R),mul(b,R))==mul(mul(a,b),R));
    const u64 step=power(H,N-1), step_mont=mul(step,R);
    const u64 factor=mul(mul(N,power(2,N-1)),
                         power((power(2,N)+P-1)%P,P-2));
    assert(power(2,N)!=1);
    assert(factor==mul(19,power((1ULL<<19)-2,P-2)));
    u64 j=1,w=R,sum=0;
    const auto start=std::chrono::steady_clock::now();
    for(u64 i=0;i<COUNT;++i) {
        // Pair a,-a in the multiplier-2 Voronoi sum.
        const bool q=j>P/2;
        sum=q ? sum+w : sum+P-w;
        sum-=P*(sum>=P);
        j=(H*j)%P; // H*j < 19*p < 2^38.
        w=mont(w,step_mont);
        if((i+1)%1000000000ULL==0) {
            std::cout<<"terms="<<i+1<<" seconds="
                <<std::chrono::duration<double>(
                    std::chrono::steady_clock::now()-start).count()
                <<" j="<<j<<" sum="<<mont(sum,1)<<std::endl;
        }
    }
    assert(j==P-1 && w==P-R);
    const u64 S=mont(sum,1), B=mul(factor,S);
    const double seconds=std::chrono::duration<double>(
        std::chrono::steady_clock::now()-start).count();
    std::ofstream out("work/hecke_general/higher2/bernoulli_8361790201.json");
    out<<"{\n  \"status\": \"COMPLETE exact half-orbit\",\n"
       <<"  \"p\": "<<P<<",\n  \"n\": "<<N
       <<",\n  \"voronoi_multiplier\": 2,\n  \"primitive_enumerator\": "<<H
       <<",\n  \"iterations\": "<<COUNT<<",\n  \"sum\": "<<S
       <<",\n  \"factor\": "<<factor<<",\n  \"bernoulli_residue\": "<<B
       <<",\n  \"endpoint_j\": "<<j<<",\n  \"endpoint_weight\": "<<mont(w,1)
       <<",\n  \"weight_step\": "<<step<<",\n  \"seconds\": "<<seconds
       <<",\n  \"scope\": \"Single Bernoulli residue only.\"\n}\n";
    std::cout<<"COMPLETE S="<<S<<" factor="<<factor<<" B="<<B
             <<" seconds="<<seconds<<std::endl;
}

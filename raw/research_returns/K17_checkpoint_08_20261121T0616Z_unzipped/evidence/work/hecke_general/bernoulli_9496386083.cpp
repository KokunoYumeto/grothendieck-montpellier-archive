// Exact constant-memory Voronoi certificate for B_(p-11) modulo p.
// There is no floating-point arithmetic in any residue calculation.
// Compile: g++ -O3 -std=c++17 bernoulli_9496386083.cpp -o bernoulli_9496386083
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>

using u64 = std::uint64_t;
using u128 = unsigned __int128;
static constexpr u64 P = 9496386083ULL;
static constexpr u64 HALF = (P-1)/2;
static constexpr u64 N = P-11;

constexpr u64 inverse_odd(u64 a) {
    u64 x = 1;
    for (unsigned i=0; i<6; ++i) x *= 2-a*x;
    return x;
}
static constexpr u64 NEG_INV = 0-inverse_odd(P);
static constexpr u64 R = (u128(1)<<64)%P;

inline u64 montgomery(u64 a, u64 b) {
    const u128 t = u128(a)*b;
    const u64 m = u64(t)*NEG_INV;
    // t + m*P < P^2 + 2^64*P < 2^100, so no 128-bit overflow.
    const u64 u = u64((t+u128(m)*P)>>64);
    return u-P*(u>=P);
}

u64 multiply(u64 a, u64 b) { return u128(a)*b%P; }
u64 power(u64 a, u64 n) {
    u64 out=1;
    while(n) {
        if(n&1) out=multiply(out,a);
        a=multiply(a,a);
        n>>=1;
    }
    return out;
}
bool prime(u64 a) {
    if(a<2) return false;
    if(!(a&1)) return a==2;
    for(u64 d=3; d<=a/d; d+=2) if(a%d==0) return false;
    return true;
}

int main(int argc, char** argv) {
    const u64 steps = argc>1 ? std::stoull(argv[1]) : HALF;
    const std::string base = argc>2 ? argv[2] : "work/hecke_general/bernoulli_9496386083";
    assert(steps<=HALF);
    assert(prime(P));
    assert(2ULL*17*293*953261==P-1);
    for(const u64 q : {2ULL,17ULL,293ULL,953261ULL}) {
        assert(prime(q));
        assert(power(2,(P-1)/q)!=1);
    }
    assert(power(2,P-1)==1);
    assert(P*NEG_INV==u64(-1));
    assert(montgomery(R,1)==1);

    const u64 c=power(2,P-12); // 2^(n-1) = 2^(-11) modulo p.
    const u64 cm=multiply(c,R);
    assert(c==2916614671ULL);
    assert(multiply(2,c)==5833229342ULL);
    for(u64 a=0; a<101; ++a)
        for(u64 b=0; b<101; ++b)
            assert(montgomery(multiply(a,R),multiply(b,R))
                   ==multiply(multiply(a,b),R));
    const u64 probes[] = {P-1,P-2,P/2,P/3,123456789,987654321};
    for(u64 a : probes) for(u64 b : probes)
        assert(montgomery(multiply(a,R),multiply(b,R))
               ==multiply(multiply(a,b),R));

    u64 j=1, w=R, sum=0, done=0;
    const auto start=std::chrono::steady_clock::now();
    while(done<steps) {
        const u64 stop = steps-done<250000000ULL ? steps : done+250000000ULL;
        for(; done<stop; ++done) {
            const bool q=j>P/2;
            // For the pair j,-j, floor(2j/p)j^(n-1)
            // + floor(2(p-j)/p)(p-j)^(n-1) = (2q-1)j^(n-1).
            sum = q ? sum+w : sum+P-w;
            sum -= P*(sum>=P);
            j=2*j-P*q;
            w=montgomery(w,cm);
        }
        const double seconds=std::chrono::duration<double>(
            std::chrono::steady_clock::now()-start).count();
        const double eta=done ? seconds*double(steps-done)/double(done) : 0;
        std::ofstream checkpoint(base+".checkpoint.json");
        checkpoint << "{\"p\":" << P << ",\"n\":" << N
            << ",\"steps\":" << done << ",\"target\":" << steps
            << ",\"j\":" << j << ",\"weight_montgomery\":" << w
            << ",\"sum_montgomery\":" << sum
            << ",\"elapsed_seconds\":" << std::setprecision(12) << seconds
            << ",\"estimated_remaining_seconds\":" << eta << "}\n";
        std::cout << "steps=" << done << "/" << steps
            << " elapsed=" << std::fixed << std::setprecision(2) << seconds
            << "s eta=" << eta << "s\n" << std::flush;
    }
    const u64 S=montgomery(sum,1);
    const u64 gn=power(2,N);
    const u64 denominator=(gn+P-1)%P;
    assert(denominator!=0);
    const u64 factor=multiply(multiply(N,c),power(denominator,P-2));
    assert(factor==multiply(11,power(2046,P-2)));
    const u64 bernoulli=multiply(factor,S);
    if(steps==HALF) {
        assert(j==P-1);
        assert(w==P-R);
    }
    const double seconds=std::chrono::duration<double>(
        std::chrono::steady_clock::now()-start).count();
    std::ofstream output(base+".json");
    output << "{\n  \"status\": \"" << (steps==HALF ? "COMPLETE" : "BENCHMARK")
        << "\",\n  \"p\": " << P << ",\n  \"n\": " << N
        << ",\n  \"primitive_root\": 2,\n  \"half_orbit_terms\": " << steps
        << ",\n  \"endpoint_j\": " << j
        << ",\n  \"endpoint_weight\": " << montgomery(w,1)
        << ",\n  \"voronoi_sum\": " << S
        << ",\n  \"bernoulli_factor\": " << factor
        << ",\n  \"bernoulli_residue\": " << bernoulli
        << ",\n  \"elapsed_seconds\": " << std::setprecision(12) << seconds
        << ",\n  \"montgomery_radix_residue\": " << R
        << ",\n  \"montgomery_negative_inverse\": " << NEG_INV
        << ",\n  \"scope\": \"Exact Bernoulli residue only; reflection and K-group bridge are separate.\"\n}\n";
    std::cout << "status=" << (steps==HALF ? "COMPLETE" : "BENCHMARK")
        << " S=" << S << " B=" << bernoulli << " seconds=" << seconds << "\n";
}

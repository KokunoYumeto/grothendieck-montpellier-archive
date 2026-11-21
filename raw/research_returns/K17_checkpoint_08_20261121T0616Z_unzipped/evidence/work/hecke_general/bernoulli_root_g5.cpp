// Independent ordinary-modular-arithmetic replay of one Voronoi sum.
// Uses primitive root 5 and unsigned __int128 division, not Montgomery
// reduction or the other program's primitive-root-2 traversal.
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>

using u64 = std::uint64_t;
using u128 = unsigned __int128;
constexpr u64 P = 9496386083ULL;
constexpr u64 G = 5;

u64 mulmod(u64 a, u64 b) { return (u128(a) * b) % P; }
u64 power(u64 a, u64 n) {
    u64 result = 1;
    while (n) {
        if (n & 1) result = mulmod(result, a);
        a = mulmod(a, a);
        n >>= 1;
    }
    return result;
}
bool prime(u64 n) {
    if (n < 2) return false;
    if (n % 2 == 0) return n == 2;
    for (u64 d = 3; d <= n/d; d += 2)
        if (n % d == 0) return false;
    return true;
}

int main() {
    assert(prime(P));
    const u64 factors[] = {2, 17, 293, 953261};
    u64 product = 1;
    for (u64 q : factors) {
        assert(prime(q));
        product *= q;
        assert(power(G, (P-1)/q) != 1);
    }
    assert(product == P-1);
    const u64 n = P-11;
    const u64 count = (P-1)/2;
    const u64 weight_step = power(G, n-1);
    const u64 denominator = (power(G, n)+P-1) % P;
    assert(denominator != 0);
    const u64 factor = mulmod(mulmod(n % P, weight_step),
                              power(denominator, P-2));
    u64 j = 1, weight = 1, sum = 0;
    auto start = std::chrono::steady_clock::now();
    for (u64 i = 0; i < count; ++i) {
        const u64 raw = G*j;
        const u64 quotient = raw/P;
        const int coefficient = int(2*quotient) - int(G-1);
        const u64 absolute = coefficient < 0 ? -coefficient : coefficient;
        const u64 term = (absolute*weight) % P;
        if (coefficient >= 0) {
            sum += term;
            if (sum >= P) sum -= P;
        } else {
            sum += P-term;
            if (sum >= P) sum -= P;
        }
        j = raw-quotient*P;
        weight = mulmod(weight, weight_step);
        if ((i+1) % 1000000000ULL == 0) {
            auto elapsed = std::chrono::duration<double>(
                std::chrono::steady_clock::now()-start).count();
            std::cout << "completed=" << i+1 << " seconds=" << elapsed
                      << " j=" << j << " weight=" << weight
                      << " sum=" << sum << std::endl;
        }
    }
    assert(j == P-1 && weight == P-1);
    const u64 bernoulli = mulmod(factor, sum);
    const auto seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now()-start).count();
    std::ofstream report("work/hecke_general/bernoulli_root_g5.json");
    report << "{\n  \"status\": \"COMPLETE exact independent Voronoi sum\",\n"
           << "  \"p\": " << P << ",\n  \"n\": " << n
           << ",\n  \"primitive_root\": " << G
           << ",\n  \"iterations\": " << count
           << ",\n  \"half_orbit_sum\": " << sum
           << ",\n  \"conversion_factor\": " << factor
           << ",\n  \"bernoulli_mod_p\": " << bernoulli
           << ",\n  \"endpoint_j\": " << j
           << ",\n  \"endpoint_weight\": " << weight
           << ",\n  \"seconds\": " << seconds << "\n}\n";
    std::cout << "B_n_mod_p=" << bernoulli << " S=" << sum
              << " factor=" << factor << " seconds=" << seconds << std::endl;
}

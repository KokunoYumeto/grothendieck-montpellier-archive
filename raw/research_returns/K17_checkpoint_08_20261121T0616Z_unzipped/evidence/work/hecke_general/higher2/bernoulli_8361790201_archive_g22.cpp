// Independent full Voronoi calculation: both multiplier and enumerator are 22.
// Uses ordinary unsigned 128-bit modular division, not Montgomery arithmetic.
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>

using word = std::uint64_t;
using wide = unsigned __int128;
constexpr word modulus = 8361790201ULL;
constexpr word generator = 22;

word product_mod(word x, word y) {
    return (wide(x) * y) % modulus;
}

word exponentiate(word x, word exponent) {
    word value = 1;
    while (exponent != 0) {
        if (exponent & 1) value = product_mod(value, x);
        x = product_mod(x, x);
        exponent >>= 1;
    }
    return value;
}

bool is_prime(word n) {
    if (n < 2) return false;
    for (word divisor = 2; divisor <= n / divisor; ++divisor)
        if (n % divisor == 0) return false;
    return true;
}

int main() {
    assert(is_prime(modulus));
    assert(8ULL * 9 * 25 * 167 * 27817 == modulus - 1);
    for (word prime_factor : {2ULL, 3ULL, 5ULL, 167ULL, 27817ULL}) {
        assert(is_prime(prime_factor));
        assert(exponentiate(generator, (modulus-1)/prime_factor) != 1);
    }
    assert(exponentiate(generator, modulus-1) == 1);

    const word index = modulus - 19;
    const word total = (modulus - 1) / 2;
    const word weight_multiplier = exponentiate(generator, index-1);
    const word denominator = (exponentiate(generator, index) + modulus-1) % modulus;
    assert(denominator != 0);
    const word conversion = product_mod(
        product_mod(index, weight_multiplier),
        exponentiate(denominator, modulus-2));

    word residue = 1;
    word weight = 1;
    word accumulator = 0;
    const auto begin = std::chrono::steady_clock::now();
    for (word position = 0; position < total; ++position) {
        const word unreduced = generator * residue;
        const word quotient = unreduced / modulus;
        const int coefficient = 2 * int(quotient) - int(generator-1);
        const word magnitude = coefficient < 0 ? -coefficient : coefficient;
        const word term = (magnitude * weight) % modulus;
        if (coefficient > 0) {
            accumulator += term;
        } else {
            accumulator += modulus - term;
        }
        if (accumulator >= modulus) accumulator -= modulus;
        residue = unreduced - quotient * modulus;
        weight = product_mod(weight, weight_multiplier);

        if ((position+1) % 1000000000ULL == 0) {
            const double elapsed = std::chrono::duration<double>(
                std::chrono::steady_clock::now()-begin).count();
            std::cout << "terms=" << position+1 << " elapsed=" << elapsed
                      << " residue=" << residue << " weight=" << weight
                      << " sum=" << accumulator << std::endl;
        }
    }
    assert(residue == modulus-1);
    assert(weight == modulus-1);
    const word bernoulli = product_mod(conversion, accumulator);
    const double elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now()-begin).count();
    std::ofstream out("work/hecke_general/higher2/bernoulli_8361790201_archive_g22.json");
    out << "{\n  \"status\": \"COMPLETE independent exact half-orbit\",\n"
        << "  \"p\": " << modulus << ",\n  \"n\": " << index
        << ",\n  \"voronoi_multiplier\": " << generator
        << ",\n  \"primitive_enumerator\": " << generator
        << ",\n  \"iterations\": " << total
        << ",\n  \"sum\": " << accumulator
        << ",\n  \"conversion_factor\": " << conversion
        << ",\n  \"bernoulli_residue\": " << bernoulli
        << ",\n  \"endpoint_residue\": " << residue
        << ",\n  \"endpoint_weight\": " << weight
        << ",\n  \"weight_multiplier\": " << weight_multiplier
        << ",\n  \"elapsed_seconds\": " << elapsed
        << ",\n  \"scope\": \"Complete Bernoulli residue; reflection and K-group implications are separate.\"\n}\n";
    std::cout << "COMPLETE sum=" << accumulator << " factor=" << conversion
              << " B=" << bernoulli << " elapsed=" << elapsed << std::endl;
}

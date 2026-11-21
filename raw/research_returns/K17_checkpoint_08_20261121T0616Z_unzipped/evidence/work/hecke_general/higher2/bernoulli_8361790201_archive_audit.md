# Independent full Bernoulli certificate at 8361790201

Date: 2026-11-21. Reviewer and independent implementation author: GPT-6 Astra Pro, archive_kummer.

**PASS.** A second complete exact computation gives

    B_8361790182 = 1827838999 modulo 8361790201.

The residue is nonzero. This reviewer wrote, compiled, executed, and read back the complete second program and its complete output, rather than relying on another agent's run. It uses both a different primitive-root enumerator and a different arithmetic implementation from the original certificate.

## Exact independent run

The original computation in `bernoulli_8361790201.cpp` uses Voronoi multiplier 2, primitive enumerator 19, and Montgomery weight arithmetic. Its entire source and complete output were read before constructing the independent check.

The independent source is `bernoulli_8361790201_archive_g22.cpp`. Both its Voronoi multiplier and its primitive enumerator are 22, and every multiplication is reduced by ordinary unsigned 128-bit integer division. It has no Montgomery arithmetic and no input of a stored Bernoulli residue or sum.

It was compiled with `g++ -O3 -std=c++17` with assertions enabled and executed in full. Exactly 4,180,895,100 half-orbit terms were processed in 51.276 seconds. Progress was observed at each billion terms. The completed report is `bernoulli_8361790201_archive_g22.json`:

| Quantity | Exact value |
| --- | ---: |
| p | 8361790201 |
| n=p-19 | 8361790182 |
| multiplier and enumerator | 22 |
| half-orbit sum | 1660697019 |
| conversion factor | 7951289779 |
| Bernoulli residue | 1827838999 |
| final residue and final weight | 8361790200 |

The source SHA256 is `55dbb504d22d3d3ac9850b3eb67a9961522dfcfd225029cad9983d989de390b4`; the output SHA256 is `4ec434aade265f21885f2a2156f687c79794c5d3179e03d679820af12076b4dd`.

## Independent derivation of the formula

For an even n with 2 <= n <= p-3, the Bernoulli recurrence gives p-integrality of all B_j for j <= n. Faulhaber's formula then gives sum_(a=1)^(p-1) a^n = p B_n modulo p^2. Write ga=r_a+p q_a with 1 <= r_a <= p-1. Since r_a permutes the nonzero residues, binomial expansion modulo p^2 yields

    (g^n-1) p B_n = n p g^(n-1) sum q_a a^(n-1) modulo p^2.

When g^n != 1 modulo p this implies

    B_n = [n g^(n-1)/(g^n-1)] sum q_a a^(n-1) modulo p.

This derivation is valid whether the enumeration of a uses g or another primitive root. It confirms the original program's distinction between multiplier 2 and enumerator 19.

For the independent run, g=22 serves both roles. The program proves p prime by trial division, verifies the complete factorization

    p-1 = 2^3 * 3^2 * 5^2 * 167 * 27817,

proves every displayed factor prime, and checks 22^((p-1)/q) != 1 for each prime divisor q. Thus 22 has order p-1, and its first (p-1)/2 powers give one representative of each pair {a,-a}. Because n-1 is odd and q_(p-a)=g-1-q_a, each pair contributes

    [2 floor(ga/p) - (g-1)] a^(n-1).

The loop computes exactly these terms. At its start, the state is (a,w,S)=(1,1,0). At iteration i, a is the least positive residue of 22^i, w=a^(n-1)=a^(-19), and S is the sum of the preceding i paired terms. The update preserves that invariant. Both endpoint assertions equal -1, as required by the primitive-root order and odd exponent. The separately computed conversion factor is the unsimplified expression n*22^(n-1)/(22^n-1), not the multiplier-2 factor from the first run.

## Arithmetic safety and reproducibility

All residue values are below p. The unreduced orbit value is below 22p<2^38. The signed coefficient has absolute value at most 21, so its product with a weight is also below 2^38 and fits unsigned 64-bit arithmetic. The sum update is below 2p. The modular weight product is below p^2<2^67 and is evaluated in unsigned 128-bit arithmetic. Thus no unintended overflow occurs. Loop counts and exponents use unsigned 64-bit integers; no floating-point quantity controls arithmetic or termination. Floating-point values appear only in timing output.

The original run obtained S_2=7432636175 and factor 2677869827. The independent run obtains the different sum and factor in the table, but their products give the same Bernoulli residue. This checks the formula through different paired terms, a different orbit, a different conversion factor, and ordinary modular reduction.

## Arithmetic consequence and scope

The already proved and independently audited reflector lemma applies with e=18. The index is p-1-e=p-19 and the mirror character is 1+e=19. Therefore the nonzero residue gives A_p^[19]=0, then A_p^[-18]=0, and finally K_36(Z){p}=0 by the established K-group/class-component vanishing equivalence. This checks one specified component, not all of Vandiver at p. The separate global K_36 deduction still uses the stipulated source arithmetic theorem and its complete Hecke coverage for other primes.

The entire independent source, output, proof, and this audit were read back after execution. No correction is requested.

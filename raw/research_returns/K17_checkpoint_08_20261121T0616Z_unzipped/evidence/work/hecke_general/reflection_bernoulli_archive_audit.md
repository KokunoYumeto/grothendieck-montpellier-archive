# Isolated reflection and Bernoulli audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, archive_kummer.

## Verdict and exact scope

**PASS** for the complete arithmetic implication in `reflection_bernoulli_section.tex`. The exact specialization is

    B_9496386072 mod 9496386083 != 0
      => A_9496386083^[11] = 0
      => A_9496386083^[-10] = 0
      => K_20(Z){9496386083} = 0.

No all-component Vandiver assertion is needed. This review also checks the complete arithmetic logic and every line of the original C++ Bernoulli certificate, but does not claim to have independently executed its full 4,748,193,041-term loop. The root is performing the independent full numerical replay with a different implementation. The original completed JSON was read and gives the nonzero residue 3753150554.

## Primary sources actually read

1. Romyar Sharifi, *Iwasawa Theory*, complete author PDF, Theorem 4.4.2 and its entire proof, pp.111–113; Corollary 4.4.4 p.113; also Theorem 4.5.7 and its entire proof, pp.117–118. The first states the reflection inequality with the roots-of-unity exception; the cyclotomic corollary is exactly r_p(A^[i]) <= r_p(A^[1-i]) <= r_p(A^[i])+1 for even i. The Herbrand proof uses the Stickelberger annihilator and is compatible with the exponent conventions in the new section.

   Primary URL: https://www.math.ucla.edu/~sharifi/iwasawa.pdf

   Author-maintained chapter: https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch04.html

   Local PDF: `work/sharifi_full_iwasawa.pdf`, SHA256 `cf4aa93fb12933b806052173ee1091959700b3b181516214e3470bde73c732de`.

   The shorter author AWS notes were also read at Theorems 2.2.1 and 2.2.3, pp.13–14. The complete modern proof, rather than the exercise there, is the cited corroboration. The original Leopoldt 1958 article was bibliographically located but not read; no locator in that uninspected original is asserted.

2. Kenneth A. Ribet, *A modular construction of unramified p-extensions of Q(mu_p)*, Inventiones 34 (1976), Main Theorem (1.1), printed p.151. The entire displayed statement and its preceding definitions were freshly visually read from the original author-hosted scan. For even 2 <= n <= p-3, it says p divides B_n if and only if (A/pA)^[1-n] is nonzero. Only the direction historically due to Herbrand is used here.

   Primary URL: https://math.berkeley.edu/~ribet/Articles/invent_34.pdf

   Local PDF: `work/references/ribet1976.pdf`, SHA256 `6985813b4026bb0fd7098aed3f816262e0922f62a5d2dab22e29bcc2eb323471`.

   Fresh rendered source page: `work/hecke_general/ribet1976_p151.png`. The file's first PDF page is a digitization cover; the mathematical printed p.151 is PDF page 2. The image was rendered from that second page and visually checked.

## Complete weak-reflection reconstruction

The section includes the full argument needed in this application. For an even character i != 0 modulo p-1, let B=A^[i]/p and let L/F be the corresponding elementary unramified class-field extension. Because the eigenspace quotient is stable under Delta, the extension is Galois over Q and the class-field identification is equivariant. Its Kummer radical V is the dual of B with Tate twist one, so it has character j=1-i, not -i or i-1.

Unramifiedness at each finite prime, including the prime above p, implies that the valuation of every Kummer representative is divisible by p. Thus (a)=I^p and the ideal class map V -> A[p] is well-defined and equivariant. Its kernel consists of unit classes. An odd unit eigenspace is zero unless the character is omega: for any unit u, u/conj(u) is a root of unity, and u^2=(u/conj(u))*u*conj(u). Consequently units modulo roots of unity and real units have exponent dividing two. Because p is odd, only mu_p contributes to the odd unit quotient, and it has character omega. This proves injectivity for j != 1 and hence the required rank inequality. This argument handles the prime above p explicitly and does not assume that a general p-unit radical is unramified there.

For e even with 2 <= e <= p-3, i=-e is nonzero and j=1+e is odd and different from 1. Taking n=p-1-e gives 2 <= n <= p-3 and 1-n congruent to 1+e. The Herbrand statement therefore has exactly the required mirror exponent. Finite p-group Nakayama passes from the quotient modulo p to the group. Finally e=2k, so the established K2 vanishing equivalence identifies A^[-e]=0 with K_(2e)(Z){p}=0. It does not claim an equality of group orders.

## Independent derivation of the numerical congruence

Let n be even with 2 <= n <= p-3 and let g be a primitive root modulo p. For 1 <= j <= p-1, write r_j=gj-p*q_j in {1,...,p-1}. The r_j permute these residues. Expanding their n-th powers modulo p^2 gives

    (g^n-1) * sum(j^n) = n*p*g^(n-1) * sum(q_j*j^(n-1)) mod p^2.

The Bernoulli recurrence shows that B_0,...,B_n are p-integral, since all recurrence denominators are at most n+1<p. Faulhaber's formula then gives sum(j^n)=p*B_n modulo p^2. Division by p is legitimate in this congruence, and g^n-1 is nonzero modulo p. Thus

    B_n = n*g^(n-1)/(g^n-1) * sum(q_j*j^(n-1)) mod p.

For g=2, n=p-11, this multiplier simplifies to 11/2046. In a primitive-root orbit j=2^i, pairing j and p-j is valid because 2^((p-1)/2)=-1. The exponent n-1 is odd, and q_(p-j)=1-q_j, so the two summands become (2*q_j-1)*j^(n-1). This proves the half-orbit loop exactly, without an approximation or an assumption about the distribution of residues.

## Complete original C++ audit

The entire file `bernoulli_9496386083.cpp` was read. Its SHA256 is `42a54fe79cf5ad46fb8fca0fa95e8c9ba2e031d3c432483463ed097a8ac3a236`. The complete output JSON was read, SHA256 `6ce027eaa18c8cc0b9dd1d441a13662aab63e68bb5923f4084fba46d8335eb97`.

The program deterministically tests primality by trial division, verifies p-1=2*17*293*953261 with every factor prime, and tests every prime divisor of p-1 to prove that 2 has full order. Its pair update uses q=(j>floor(p/2)), j_next=2j-pq, exactly the least positive residue. It starts the weight at one and multiplies by 2^(p-12), so the ith weight is j_i^(n-1). The accumulator adds or subtracts that weight according to 2q-1. The completed orbit length is (p-1)/2=4,748,193,041 and both final residues are -1, as required.

The Montgomery implementation has radix R0=2^64 and negative inverse -p^(-1) modulo R0, computed by six unsigned Newton steps. For reduced inputs a,b<p, t=ab<p^2<R0*p. The integer m is chosen so t+mp is divisible by R0, and 0 <= t+mp < 2*R0*p; thus its quotient is less than 2p and one subtraction suffices. No 128-bit overflow occurs because the numerator is less than 2^100. Storing each residue multiplied by R0 modulo p makes the multiplication update correct. All j and accumulator sums are less than 2p<2^35 and fit uint64. The conversion back is multiplication by ordinary one. Floating-point quantities occur only in timing diagnostics, never in residue decisions.

The read completed output has S=4849818985, multiplier=5565086468, and B_n=3753150554 modulo p. The endpoint checks and complete status are present. These are the output of the author's full run, not a full execution performed by this reviewer. Their independent replay is a separate root-owned check.

## Final self-readback

The complete new TeX, bibliography addition, and this audit were read after writing. No source-index, parity, or exceptional-character issue remains. The arithmetic implication is ready for an independent whole-proof read. The numerical computation is explicitly kept separate from the proof of the reflection and K-group bridge.

# Primer: GRH_ALGORITHMS (prompt 67), what the proof of Dirichlet GRH makes unconditional in algorithms

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7). It is a recall of the run, nothing new.

**The run.** GPT-6 Astra (ChatGPT Pro mode), prompt 67, sent 22 Nov. Its last checkpoint is 08 (23 Nov 02:24 UTC).
The thread is beyond reach. Its finishing run is 67c (GRH_ALGORITHMS_FINISH).

**Read the FINISH primer for the mathematics as it stands now.** It covers everything below with full mechanisms:
`intakes/GRH_ALGORITHMS_FINISH/PRIMER_GRH_ALGORITHMS_FINISH_20261123.md`.

A is Alpöge's theorem: RH for every Dirichlet L-function, ζ included.

## What this run established, by checkpoint
- **cp04 (22 Nov):**
  - the classification of eighteen classical GRH-dependent algorithmic statements by their exact L-functions;
  - the pure-field equivalence RH(ζ_{Q(p^{1/r})}) ⇔ RH(ζ_{Q(ζ_r, p^{1/r})}) under A (P001);
  - Lenstra's Teichmüller equivalence (P004);
  - the first average theorem (P058: auxiliary primes ≤ C log P log log P for all but O(√P log log P) inputs);
  - many restrictions on single routes.
  - Checked by us: P056-P058, by targeted proof check, and all seven programs rerun.
- **cp05 (23 Nov 00:05):**
  - P074 halves the average's threshold to C_r > (r−1)/(2 log r), since only r^m ≥ √P is needed;
  - P092-P095 give the logarithmic cubic search: k ≤ C log P with C > 1/log 3. Its mechanism is the private prime
    divisors of k² + 3k + 9 (after Cilleruelo).
  - Checked by us: P074 and P092-P095.
- **cp08 (02:24):**
  - unconditional F_{p^r} in time poly(r, log p, M₂), M₂ = Φ_d(p)/(2^{v₂} r^a) (P128/P131, after Bach-von zur
    Gathen-Lenstra);
  - F_{p^r} under A in time C_{r,b}(log p)^{c_{r,b}} for each fixed (r, b) (P125/P126, after Pila; CM-theta);
  - cubic fields at v₃(p+1) = 2 (P119).
  - Checked by us: the root-extraction lemma behind P128/P131.
- **Paper reviews:** at cp05 the verdict was "postable after fixes" (ten fixes); at cp08 they became the twelve items of
  67c.

## Open rows at cp08
- Q01: uniform construction from A alone, partly proved.
- Q02: the classical auxiliary-prime bound from A alone; gate: the one-sided window for the induced order-r Hecke
  function.
- Q07 (density), Q08 (elliptic trace), Q09 (CM discriminant): open.

The FINISH run since reduced Q01's unconditional parameter to C_L (P144/P145) and closed Q05.

## Where the results went
- Hexagon board row H29.
- Seed `reports_20261122/paper_seeds/SEED_MAS_ARTIN.md`, Paper 2, with its status note of 23 Nov.
- Prompt 67c, the finishing run.
- The P vs NP fleet map ANT-07 (succinct finite planes).

# Higher2 — root complete proof and exact replay audit

Date: 2026-11-21 04:41 UTC. Reviewer: GPT-6 Astra Pro; effort not exposed; K17 root.

PASS for K17-HECKE-HIGHER2 and K17-BERNOULLI-8361790201. Read the whole final higher_harmonic_section.tex proof, the whole Bernoulli section, all96 new GL2 wrapper lines (using the previously wholly read generic arithmetic routines), the whole comparison/Lucas program, and both complete C++ programs and their completed reports. The generic harmonic verifier is unchanged and was read wholly in the preceding audit; its full new-data execution was actually performed by root, including all six complete operators, exact kernels and identifying equations, polynomial factors and extra evaluation checks. Root also actually reran the complete new GL2 reconstruction and all59 recursive Lucas nodes and combined product gcds. No probable-prime test is used in these certificate checks.

The larger harmonic spaces include every orbit with coordinate differences0,+/-6,+/-12. The source/target dimensions64/50,104/83,156/129 give complete kernels14,21,27. The swap signs agree with8+6,12+9,15+12. The exact identifying determinants are nonzero, so full equations AM=B identify each operator; the modular screening used only to discover points is not a proof premise. Every old source normalization and full-level argument is uniform in e and remains separately checked. The GL2 basis dimensions8,10,11 agree with floor((2e-5)/3)+1; precision260 covers every identifying coefficient and extra checks through37 and20. All p-divisible-index correction terms remain in the loop.

Lucas proof: for every prime r dividing n, the witness has order exactly n-1 modulo r, because every q-primary factor of n-1 is forced by the gcd condition. Hence n-1 divides r-1 and r>=n, proving n prime. The certificate orders nodes after their dependencies and verifies each full factorization; root reran it. The combined products, not separate branch gcds, have exactly the displayed factors. Only25078104767246023 for e16 and8361790201 for e18 exceed2^31.

The e18 Bernoulli formula uses multiplier2 but primitive enumerator19. Those roles are correctly separated. Pairing a with -a gives2floor(2a/p)-1, weight exponent-19, and n=-19 modulo p but n=-18 modulo p-1, giving factor19/(2^19-2). All signed Montgomery states remain belowp, intermediate products below2^100, and raw19a<2^38. The independent archive calculation instead uses multiplier and enumerator22 with ordinary128-bit modular division. Its coefficient is in[-21,21], and the full half-orbit invariant and endpoints hold. Both complete4,180,895,100-term reports give1827838999. Root read both programs and reports in full but did not relabel either loop as a root execution. The actual runs were author and independent archive, whose identities and timings are retained.

The arithmetic conclusion uses the separately proved reflection lemma with e18 and reflected character19, plus the generic unit-trace criterion. No all-character Vandiver claim at8361790201 or K32 vanishing follows from this audit.

## Reviewed hashes

- `higher_harmonic_section.tex`: `06f7c86c6e6887ecfc4a94d4fda26cd9e826cb0d904695c911b7320c97918026`
- `bernoulli_8361790201_section.tex`: `7c5ecd615f1e8bc53c463a2787ea43653a09379dadd0526a15265a87998773ab`
- `gl2_higher2_certificate.py`: `80424d6d8031b9b4538d05f18417600b13d6b90acc5fa00f915fd4b4b974ad81`
- `comparison_certificate.py`: `2018b69e756a5a7e641d5c20000c1ebc413f59688bb148d244cbf4db1d625614`
- `bernoulli_8361790201.cpp`: `df0aab416b2ec201cfa78f2c58d5a4074a376b7dff127e3a8b9a1e2c0fe10d49`
- `bernoulli_8361790201_archive_g22.cpp`: `55dbb504d22d3d3ac9850b3eb67a9961522dfcfd225029cad9983d989de390b4`
- `harmonic_hecke_exact_data.json`: `b362945a162a6e6355be470f753dd2281e6b2dd284b9af8cff1e2a4ef9b8ee6e`
- `harmonic_hecke_root_replay.json`: `f811e58393049e5149323d5c23063a006d12ae913c77a5d9355fed73a7ab23a1`

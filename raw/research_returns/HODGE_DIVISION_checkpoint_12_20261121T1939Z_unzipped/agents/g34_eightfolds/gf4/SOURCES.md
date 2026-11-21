# F4 extension over Q(sqrt−2): source and certificate record

## Published root data

Patricia Cahn, Ruth Haas, Aloysius G. Helminck, Juan Li, Jeremy Schwartz, **Permutation notations for the exceptional Weyl group F4**, *Involve* 5(1) (2012), 81–90.

Publisher PDF: <https://msp.org/involve/2012/5-1/involve-v5-n1-p09-s.pdf>. The exact 48-root system and four simple roots are stated in §3, printed p83 (PDF page4 including cover). They coincide with the seed in our code. PDF and layout text are saved as `CahnF4.pdf` and `.txt`.

For context, the author PDF of Chi-Kwong Li, Ilya Spitkovsky, Nahum Zobin, **Finite Reflection Groups and Linear Preserver Problems**, <https://nxzobi.people.wm.edu/lsz.pdf>, was also read at §5, manuscript p13: equations(8)–(9) give F4 and its real orthogonal normalizer. The PDF is saved as `LiSpitkovskyZobin.pdf`. Its normalizer classification is not a premise: our specific Φ matrix and its normalization property are proved directly from the root system. We do not conflate the real normalizer with the complex group defined using z=(sqrt−2/2)Φ.

## New construction and exact data

The group is rebuilt from the published F4 root reflections and

```
Phi = [[0,-1,-1,0],[1,0,0,1],[1,0,0,-1],[0,-1,1,0]],
t^2=-2, z=(t/2)Phi.
```

The proof shows Phi²=−2I, z²=1, and Φ exchanges short roots with long roots, the reverse direction having scale2. Thus z normalizes W(F4), and G_F=W⊔Wz has order2304. A separate elementary orbit/stabilizer proof gives |W|=24·48=1152. These facts are also checked by exact enumeration.

The exact search used seed20261121. Trial12 found the five displayed reflection roots and the tuple `(s1,s1,...,s5,s5,z,z)`. The standard F4 generators have short words

```
s2 s5 s2, s5, s3, s1 s2 s4 s2 s1.
```

The fixed default run of `gf4_reconstruct.py` uses the frozen witness and checks these words, group equality, the negative-eigenspace bases, the14-variable parabolic quotient, all nine twists, all63 PSD principal minors, and the determinant. Its `--search` mode preserves the reproducible discovery procedure but is not needed for verification.

Certificate values:

- group order2304; real reflection subgroup order1152;
- ten rank-one and two rank-two involutions;
- curve genus4609; Chevalley–Weil multiplicities3,3;
- relation rank4, coboundary rank4, coefficient count14, quotient dimension6;
- logarithm ranks1,1,1,1,1,2,2,2,3;
- common square-zero block form and pairwise vanishing products;
- negative-block sum leading principal minors18,379,1286;
- K-determinant `(256+640t)/27`, norm `2^15/3^3`;
- character trace witness `tr(s_e1 P12 z)=−t`;
- integral t-action `(1−s_e1)P12z` on the selected primitive factor;
- source projector bound `G e ∈ Z[G]`, yielding Δ_A|2304^6.

Actual period rank9 and splitness are proved separately in D-GF4-03 using the geometric twist comparison and limiting mixed Hodge structure. The matrix determinant is not mislabeled as a direct period computation.

## Shared cycle/analytic inputs and quantitative scope

Published analytic and cycle inputs are exactly those recorded in `../SOURCES.md` for G34 and `../g24/SOURCES.md`: Frediani–Ghigi–Penegini Theorem2.10; Dettweiler–Wewers Lemma2.2/Theorem2.5; Schmid4.12/6.16; Schoen2.0/Cor3.1 with the independently proved localization repair; Serre Brauer induction; Milne full Lefschetz invariants. The supplied SQ3–SQ7 proofs give the arithmetic mass/intersection estimates after the new geometric hypotheses are proved.

The effective degree bound is

```
G=2304, g=4609,
R=(2G+1)G!G^G, L=2gR,
S0=G^(2g)(g!)^2, SB=(L/2)!S0^R, k=L/2+3,
B02=(40G)^k binom(k,3) SB 6! G^6,
D_6,2(Delta)=[4G^6 Delta]^6 B02.
```

The maximal-order source lattice is proved stable by an actual integral group-algebra endomorphism, so no hidden source saturation factor is used. A fixed nonmaximal target order contributes f^12 inside Delta. The result covers split sixfolds, including the principal balanced E^6 datum overQsqrt−2. No assertion covering every nonsplit determinant is made.

rStation75 was a lead only. No unrefereed theorem, Severn theorem, Markman theorem, or032 premise is used. These are exact arithmetic and mathematical proof checks, not formal proof-assistant certification. No successful TeX compile is claimed in the present environment.

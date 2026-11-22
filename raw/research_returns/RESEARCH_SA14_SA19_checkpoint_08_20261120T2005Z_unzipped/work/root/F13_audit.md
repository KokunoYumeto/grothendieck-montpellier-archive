# Independent full proof audit: F13

20 November 2026, after formal review03. GPT-6 Astra (OpenAI, ChatGPT
Pro mode), root run; effort inherited and not exposed. No priority claim.

**PASS for the stated complete normal equal-characteristic surface pair.**
This is a bound on logarithmic ramification, not the unproved local
Betti estimate F13.5.

1. I re-proved F13a with the specified abelian normal subgroup N. Its
   normal ell-primary subgroup acts trivially on a simple module. The
   remaining character spaces form one orbit. On a chosen stabilizer I,
   the commutator pairing on I/N is well defined by invariance of chi.
   A maximal isotropic L contains the radical and equals its orthogonal:
   otherwise any element of L-perp outside L enlarges it. The preimage K
   has commuting matrices, hence a common eigenvector. Distinct conjugate
   K-characters split the induced module into character lines even when
   ell divides the group order. Every submodule is a sum of those lines,
   and transitivity proves simplicity. No erroneous Maschke assertion for
   the ambient group is needed. K contains N, so is normal in Gamma.
2. A connected finite etale cover of the fixed regular resolution is
   regular and integral. Its finite Stein normalization is complete and
   local: a finite algebra over the complete local base is a product of
   complete local factors, and connectedness leaves one. The residue
   field is the given algebraically closed k. The pulled-back exceptional
   divisor is SNC and is the proper closed fibre. Thus the F10 argument
   applies to that cover. Riemann--Hurwitz and the node count give
   k'_a=d_a*k_i; the intersection projection formula gives
   (B' f*t)_a=d_a*(Bt)_i. Negative definiteness therefore gives exactly
   t'_a=t_i, with no growth in the covering degree. BCE separately audited
   this geometric sublemma.
3. On the fixed F10b cover, all original abelian monodromy extends to the
   resolution. Its boundary inertia consequently lies in
   N=Gamma_0 intersect Gamma'. Every inducing subgroup from F13a contains
   N, so the inducing cover is unramified at all boundary DVRs. Purity on
   the regular resolution extends it to a finite etale cover. The p-part
   of its rank-one character obeys step2; the prime-to-p part is tame.
4. I independently opened Kato--Saito, Coincidence of two Swan conductors
   of abelian characters, arXiv1904.08604v3 / Epijournal3(2019), Th1.3
   printed p2, and Abbes--Saito, Ramification of local fields with
   imperfect residue fields, author PDF dated1 February2002, Prop3.15(3)
   printed p8. The first identifies Kato's rank-one Swan conductor and
   the logarithmic break, with no perfect-residue-field restriction. The
   second identifies positive logarithmic groups under unramified base
   change. Mackey decomposition at the completed DVR then shows that
   induction through this unramified cover preserves the cutoff t_i.
5. Positive logarithmic ramification has p-group image. Its finite
   representations over characteristic ell different from p are
   semisimple. Triviality on all composition factors therefore implies
   triviality on M, even when M is not semisimple under full monodromy.
6. I independently opened Hu--Teyssier, arXiv2502.11060, Th7.34 printed
   p41, and Def4.6/Th4.7 pp15--16. The first is rank-linear for finite
   coefficient fields but requires a proper smooth finite-type k-scheme.
   The second requires a geometric henselian trait, explicitly used in
   spreading out. Neither supplies the uniform complete-local estimate
   F13.5 without a further comparison argument. This limitation is
   accurately preserved in the statement and remaining gate.

Thus all finite metabelian-monodromy systems with coefficient prime
different from p obey one fixed conductor bound after one fixed cover.
The rank-linear local H1 estimate and the derived-length-three generator
bound remain unproved. This audit postdates review03 and cannot be
retroactively counted in that review.

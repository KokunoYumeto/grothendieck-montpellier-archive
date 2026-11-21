# Intake of RESEARCH_SA06 (final return of 19 Nov 2026): the mathematics

Claude Opus 5.5 at effort max, agent `c14_c15rest_part1` (the sweep-3 reader of SA06 cote 14, scans 2-58), resumed on
20 Nov 2026 for this intake by the main session (Claude Opus 5.5 at effort max). The run: GPT-6 Astra (ChatGPT Pro mode).

## 0. What I read, and my scope

- **Return read:** `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`
  (the final checkpoint, marked INCOMPLETE by the run; report updated 2026-11-19 20:52 UTC). Read: the status table of
  `RESEARCH_SA06_report.md` (lines 1-60); in full, `sections/E1_effectivity.tex`, `sections/E3_albanese.tex` (with the
  included `agents/cycles/morphic_counterexample.tex`), and `sections/C_cycles.tex` lines 33-160 (C.1a-e) and 1197-1360
  (C.5a-e). The rest through the sort (`field_experts/intake_20261120/SORTED/RESEARCH_SA06.md`, `.tsv`) and the packet
  statements. Archive side: my sweep-3 reading `readings/c14_c15rest_part1.md` and `STUDY.md`.
- **Rows:** all 246 RESEARCH_SA06 rows of packets 01-08 (A.1a-A.8c, B.1a-B.4g, C.1a-C.5e, D.0a-D.4g, E.1a-E.6b, F.2a-b).
- **Read in full, with the proof (24 rows):** E.1a-e, E.3a-f, E.3t, E.3u, C.1a-e, C.5a-e, and B.1a (statement plus my own
  proof). These are the rows on my archive stretch (14:9, 14:24-39, 14:30, 14:44-47, and 15:100-106 through STUDY.md).
- **At the level of the statement (222 rows):** all the others, marked "not read in full" in section 1. They include
  rows the programme rests on that I did not check: C.3e (used by 17), C.4j, C.4p, C.4n, A.1d, B.4a, the whole local
  restriction programme C.3 (75 rows), the Jacobian-summand programme C.4 (28 rows), Deuring A (23), real Weil and gerbes D (18),
  E.2 and E.4-E.6.
- Cited theorems that the proofs I read rely on, and that I did not open, are named in each verdict.

## 1. Verdicts, row by row

Counts over the 246 rows: read in full 24, of which targeted proof check confirmed 17 (five of them, E.3b, E.3e,
E.3t, E.3u, C.1a, confirmed as deductions from cited theorems I did not open, named in the row), refutation confirmed
by checking the counterexample 5 (E.1c, E.3f, C.1b, C.1e, C.5d), known result carried as background 1 (C.5b),
independent re-proof 1 (B.1a). No gap found and nothing refuted among the rows I read. Not read in full: 222.

| Row | Run status | Read | My verdict | Note |
|---|---|---|---|---|
| A.1a | Refuted | statement | not read in full | The unrestricted F_(p^2) determinant formulation is false |
| A.1b | Proved | statement | not read in full | Exact finite-field Tate determinant criterion; algebraic-closure existence |
| A.1c | Proved | statement | not read in full | Unique integral rank-two slope-half crystal and oriented O-actions |
| A.1d | Proved | statement | not read in full | Choice-independent Deuring rule from oriented reconstruction and cup trace |
| A.1e | Proved | statement | not read in full | Terminating geometric reconstruction and explicit intertwiner prescription |
| A.1f | Refuted | statement | not read in full | Maximal quadratic order is not equivalent to all trace-zero descents |
| A.1g | Proved | statement | not read in full | Corrected restriction equivalence of determinant rules on maximal-order descents |
| A.1h | Proved | statement | not read in full | Unique descent of the geometric rule on the exact finite-field Tate domain |
| A.2a | Proved | statement | not read in full | Integral adelic base, Kummer group, local Brandt image and splitting |
| A.2b | Proved under stated hypotheses | statement | not read in full | Canonical quotient comparison torsor and trivial profinite Frobenius action |
| A.2c | Proved | statement | not read in full | Neutral comparison gerbe and geometric section at every place |
| A.3a | Proved | statement | not read in full | Positivity fixes real comparison class, leaving two automorphisms |
| A.4a | Proved | statement | not read in full | Quaternionic Hermitian realization with exact sign ambiguity |
| A.5a | Proved under stated hypotheses | statement | not read in full | Rigidified Picard equivalence under symmetric condition C |
| A.5b | Proved | statement | not read in full | Base-change admissibility condition and maximal-order case |
| A.5c | Refuted | statement | not read in full | Arbitrary ramified base change preserves a Picard category of determinant-rigidified autoequivalences under Deuring axio |
| A.5d | Proved qualification | statement | not read in full | The counterexample is excluded by strict maximal-order or Azumaya hypotheses; condition (C) theorem retains its restrict |
| A.6a | Proved | statement | not read in full | Unique Phi-normalized norm-line trivializations and determinant transport |
| A.6b | Refuted | statement | not read in full | Bare uniqueness without the positive norm normalization is false |
| A.7a | Proved under stated hypotheses | statement | not read in full | Supersingular comparison determines the motivic mu2 pushout |
| A.8a | Known | statement | not read in full | All Fp supersingular class counts and correction of triple identification |
| A.8b | Proved | statement | not read in full | Unit groups in the exceptional j cases; original scan confirms unfinished question |
| A.8c | Known | statement | not read in full | Maximal-order trace-zero triples have class number h(R) |
| B.1a | Known | statement + my own proof | independent re-proof, confirmed (known: Milne 1994 Prop. 2.6, proof; locator not opened by me) | λ Weil q-integer of weight i: an i-th root μ is a Weil q-integer of weight 1 (all conjugates /μ'/=q^{1/2}); Honda-Tate gives A/F_q with eigenvalue μ on H^1; H^1(A)^{⊗i} ⊂ H^i(A^i) carries μ^i = λ. m=1. Settles the 'conjecture forte' of 15:100-106, recorded open in STUDY.md §1. |
| B.1b | Proved | statement | not read in full | Effective construction data and semisimple numerical motive with the required eigenvalue. |
| B.2a | Proved | statement | not read in full | Exact all-weight eigenvalue set is the Weil q-integers. |
| B.3a | Proved | statement | not read in full | Every weight-i Weil q-integer factors into i weight-one Weil q-integers in an allowed extension number field. |
| B.3b | Proved | statement | not read in full | Explicit F2 abelian threefold realizes (3+sqrt(-23))/2 on H3. |
| B.4a | Proved | statement | not read in full | Exact norm-one p-unit divisor cokernel with full unit norm correction. |
| B.4b | Proved | statement | not read in full | Finite lattice presentation including the complete 2-primary extension. |
| B.4c | Refuted | statement | not read in full | Inclusion-valued canonical point of D(M0/torsion) exists as stated in R7. |
| B.4d | Proved | statement | not read in full | Powered point g_k and exact rational lift criterion. |
| B.4e | Proved | statement | not read in full | Finite arithmetic lift algorithm and sufficient power 2h/D_p//mu(L)/. |
| B.4f | Proved | statement | not read in full | Correct normalization inside ker epsilon and direction of base change. |
| B.4g | Proved | statement | not read in full | Audit of R5 and R7 used steps. |
| C.1a | Proved under stated hypotheses | full | targeted proof check of the deduction, confirmed (Clemens 1983 Th. 0.2 not opened by me) | Very general quintic: A^1=Qh, A^2=Qh^2⊕G, dim G=∞, coker L = G. |
| C.1b | Refuted | full | refutation confirmed | Letter's A, A', A'' and τ=num fail mod algebraic equivalence; A' fails for ANY smooth hyperplane section (NS(Y) finite-dimensional vs G infinite) — simpler than the Moishezon step in my reading of 14:45. |
| C.1c | Proved | full | targeted proof check, confirmed | L^{n-2}: NS_Q -> A^{n-1}_alg injective, cokernel G^{n-1} (hard Lefschetz + Lefschetz (1,1)); V×P^{n-3} counterexamples. |
| C.1d | Proved | full | targeted proof check, confirmed | i=0 and 2i=n cases; n<=2; surface B = Hodge index. |
| C.1e | Refuted | full | refutation confirmed (counterexample checked) | X = V×P^1, L = h+t: L: A^2->A^3 iso, B(X) vacuous, G≠0 numerically trivial. |
| C.1f | Proved under stated hypotheses | statement | not read in full | Universal letter A over C holds exactly for i=0 or 2i=n; every 1<=i<n/2 has a finite-source/infinite-target counterexamp |
| C.1g | Proved | statement | not read in full | Specified universal quintic over Q(t_1,...,t_113) has an infinite-order homologically trivial difference of its two disp |
| C.1h | Proved | statement | not read in full | For a geometric generic hyperplane the rational Gysin image modulo algebraic equivalence equals the image of multiplicat |
| C.1i | Proved | statement | not read in full | Universal A-prime/A-double-prime over C holds in the range 2c>n exactly at top codimension c=n; explicit split-quadric c |
| C.1j | Proved | statement | not read in full | Complex middle letter B is equivalent to injectivity of L on the middle rational Griffiths group; semidefinite positivit |
| C.1k | Proved under stated hypotheses | statement | not read in full | Universal cycle-class injectivity, algebraic-up-to-torsion=numerical, finite rank and finite generation hold exactly in  |
| C.1l | Proved | statement | not read in full | Nonzero Griffiths class gives an explicit nonzero Jacobson-radical correspondence; nonsemisimple examples in every dimen |
| C.1m | Proved under stated hypotheses | statement | not read in full | Universal finite-dimensional semisimple correspondence algebra modulo algebraic equivalence holds exactly in dimensions0 |
| C.1n | Proved | statement | not read in full | The universal endpoint image criterion is equivalent to standard D; for a fixed target it is equivalent to D and vanishi |
| C.1o | Proved | statement | not read in full | Projective-space stabilization identifies the exact middle-positivity radical and universal shifted Griffiths injectivit |
| C.1p | Proved | statement | not read in full | Abelian projective stabilizations satisfy middle positivity exactly when all nonpositive Beauville pieces of the Griffit |
| C.1q | Proved | statement | not read in full | The exact exceptional normal-bundle polynomial controls a blow-up middle radical; ample pencil bases give a candidate cr |
| C.2b | Proved | statement | not read in full | Affine homological vanishing is true; it does not supply algebraic Gysin preimages |
| C.2c | Proved under stated hypotheses | statement | not read in full | Standard A and Hodge-type positivity yield D; D yields A; product hypotheses in standard B comparisons |
| C.2d | Known | statement | not read in full | Numerical motives semisimple; homological motives inherit this if D holds on all required products |
| C.2e | Proved under stated hypotheses | statement | not read in full | Universal A-prime implies A by a generic-pencil and codimension induction |
| C.2f | Proved | statement | not read in full | A implies A-prime; affine-vanishing implication has exactly the universal standard-A gate |
| C.2g | Proved under stated hypotheses | statement | not read in full | Critical-dimension A-prime implies every degree case by projective-bundle stabilization |
| C.2h | Proved under stated hypotheses | statement | not read in full | Universal middle positivity gives all primitive degrees; product standard hypotheses give positive trace form |
| C.2i | Proved under stated hypotheses | statement | not read in full | Semisimplicity and algebraic preimages for every algebraic cohomological map |
| C.2j | Proved under stated hypotheses | statement | not read in full | Conditional Weil integrality, functional equation, absolute values and Frobenius semisimplicity |
| C.2k | Known with derivation | statement | not read in full | Numerical equals homological in codimensions0/1/2/n−1/n over C and the degree-two homological Lefschetz cokernel is its  |
| C.3a | Proved | statement | not read in full | Exact obstruction sequence splits algebraic Lefschetz failure into Griffiths and homological gates |
| C.3b | Proved | statement | not read in full | J1 Lefschetz map injective over C, cokernel equals rational Albanese kernel |
| C.3c | Refuted | statement | not read in full | K3 J1 surjectivity and global punctured-cone finite Chow claim fail |
| C.3d | Proved under stated hypotheses | statement | not read in full | Universal J-Lefschetz surjectivity over C holds exactly for the identity exponent; all n>=2i>=2 have zero-source/nonzero |
| C.3e | Proved | statement | not read in full | Integral strict local cone injection for rational and algebraic equivalence |
| C.3f | Refuted | statement | not read in full | Explicit strictly local threefold counterexample to finiteness and Gysin vanishing |
| C.3g | Refuted | statement | not read in full | Universal strict local high-degree finiteness fails in every nonempty proposed range |
| C.3h | Proved | statement | not read in full | Exact Beauville-graded gates for both abelian Lefschetz injectivity assertions |
| C.3i | Refuted universal full-Picard injection/ | statement | not read in full | For every N>=4 a smooth strict-local hyperplane restriction has exact additive Picard kernel C^3 |
| C.3j | Proved in the stated scope | statement | not read in full | Ordinary algebraic-equivalence Picard restriction is injective for algebraizable characteristic-zero strict local germs  |
| C.3k | Proved in the separately stated scopes | statement | not read in full | Prime-to-residue torsion Picard injectivity for arbitrary excellent normal strict local germs of dimension at least thre |
| C.3l | Proved | statement | not read in full | Both universal abelian injectivity assertions together are equivalent to ordinary Beauville negative-index vanishing |
| C.3m | Refuted, with an explicit actual-line-bu | statement | not read in full | Ordinary algebraic-equivalence J1 restriction fails to be surjective for explicit excellent normal strictly henselian co |
| C.3n | Proved in the explicitly stated coeffici | statement | not read in full | Ordinary Picard restriction has zero kernel in characteristic zero and p-primary torsion kernel in characteristic p for  |
| C.3o | Proved/refuted with explicit strictly he | statement | not read in full | Sharp ordinary rational degree-one thresholds over C: injectivity fails in dimension two and holds from dimension three; |
| C.3p | Known with full hypothesis-checked deriv | statement | not read in full | Finite-etale restriction is fully faithful in dimension at least three and an equivalence in dimension at least four for |
| C.3q | Proved under explicitly stated geometric | statement | not read in full | Every target abelian subgroup of local Picard functors in the normal essentially-finite-type characteristic-p dimension- |
| C.3r | Refuted | statement | not read in full | Ordinary local higher-cycle restriction is non-surjective at every boundary dimension N=2r+1 |
| C.3s | Refuted | statement | not read in full | Exact universal local Chow and ordinary-J finiteness range over C |
| C.3t | Refuted | statement | not read in full | For every r>=2 and r+1<=N<=2r−1 there are explicit regular strict-local punctures with a non-torsion ordinary Gysin imag |
| C.3u | Proved under explicitly stated smooth-co | statement | not read in full | For a strict local smooth projective cone of dimension at least four with degree-one-generated full section ring, ordina |
| C.3v | Refuted | statement | not read in full | Exact ordinary divisor quotient on the strict local Segre-quartic cone in every dimension at least two |
| C.3w | Proved in the stated algebraizable coeff | statement | not read in full | Every k-point of a proper abelian subgroup of the local Picard scheme of an algebraizable normal strict local germ with  |
| C.3x | Proved/refuted with explicit examples in | statement | not read in full | Complete ordinary rational degree-one restriction table in positive characteristic for algebraizable normal strict local |
| C.3y | Proved/refuted with an explicit ring and | statement | not read in full | In every characteristic an explicit normal strict local surface has ordinary Pic_alg=0 and Pic=k* direct sum (Z/4)^2; in |
| C.3z | Proved | statement | not read in full | General excellent henselian coefficient-field germs admit a regular algebraic model map and ordinary Picard subgroup poi |
| C.3aa | Refuted, with a complete Segre-Nori coun | statement | not read in full | For every complex strict-local dimension N>=4 and codimension2<=r<=N-2 there is an explicit normal isolated cone germ wi |
| C.3ab | Proved under the stated explicit surface | statement | not read in full | For a strict henselian cone over a smooth projective surface in characteristic zero with all positive absolute-different |
| C.3ac | Known with derivation | statement | not read in full | Abelian rational Chow hard Lefschetz over Fpbar is classical; under the cited2026 CM-Hodge theorem rational and numerica |
| C.3ad | Proved in the stated rational smooth-con | statement | not read in full | For every strict henselian smooth-projective cone over Qbar of dimension d+1>=3 with normal degree-one full section ring |
| C.3ae | Refuted, with an explicit counterexample | statement | not read in full | For every complex local dimension N>=7 the ordinary codimension-two restriction cokernel can surject integrally onto the |
| C.3af | Refuted, with an explicit counterexample | statement | not read in full | For every r>=2 and N>=4^(r-1)+2r-1 an explicitly specified ordinary codimension-r local restriction cokernel surjects on |
| C.3ag | Refuted | statement | not read in full | Ordinary degree-two local restriction fails in dimension six; integral cokernel surjects onto Pic0 of a specified Fermat |
| C.3ah | Refuted, with an explicit counterexample | statement | not read in full | For every r>=1, a specified regular source of dimension N=r+2 has zero CH^r and a principal regular puncture with non-to |
| C.3ai | Refuted, with an explicit counterexample | statement | not read in full | For every r>=1 and r+2<=N<=2r+1, a specified regular ambient strict local source has zero CH^r while its regular princip |
| C.3aj | Refuted, with fully specified Hodge-gene | statement | not read in full | For every r>=2 and N>=2r+2 there is a specified excellent normal strict-local complex germ with regular puncture and reg |
| C.3ak | Proved | statement | not read in full | For every r>=1, ordinary local J^r restriction over C is universally surjective exactly in dimensions N<=r+1; the same u |
| C.3al | Proved/refuted in the stated ranges | statement | not read in full | Principal Gysin images lie in the ordinary closed-restriction kernel integrally; explicit infinite-order kernels for r>= |
| C.3am | Refuted, with explicit counterexamples | statement | not read in full | For every r>=2 a specified Fermat-cubic cone of local dimension2r has an infinite-order ordinary restriction kernel for  |
| C.3an | Refuted integral finiteness with an expl | statement | not read in full | For every algebraically closed field of characteristic five a specified normal excellent strict-local threefold has regu |
| C.3ao | Refuted, with specified counterexamples | statement | not read in full | For every r>=2,N>=2r+1 a specified strict cone and smooth principal puncture have an infinite-order ordinary CH^r restri |
| C.3ap | Proved, with counterexamples in every co | statement | not read in full | Complete ordinary complex local restriction table: r>=2 injection iffN<=r,surjection iffN<=r+1,isomorphism iffN<=r; r1 i |
| C.3aq | Refuted integral finiteness in every pos | statement | not read in full | For every algebraically closed field of every positive characteristic a specified normal excellent strict-local threefol |
| C.3ar | Proved in the stated restricted scope | statement | not read in full | For complex strict cones over products of Qbar-defined curves with external ample L and normal degree-one section ring,  |
| C.3as | Refuted integral top finiteness in every | statement | not read in full | For every algebraically closed field of characteristic p>0 and every N>=3 a specified excellent normal strict-local N-fo |
| C.3at | Refuted rational ordinary surjectivity a | statement | not read in full | For every prime p and r>=2 a specified regular strict-local ambient of dimension N=r+2 has zero source CH^r and a regula |
| C.3au | Proved in the stated restricted scope | statement | not read in full | For the specified complex Fermat quintic surface cone, B^2(Z)_Q=Q by exceptional degree and B^2(X)_Q=0 |
| C.3av | Refuted rational ordinary surjectivity i | statement | not read in full | For every prime p and r+2<=N<=2r+1 a specified regular strict-local ambient has zero CH^r while its regular principal pu |
| C.3aw | Refuted rational ordinary injectivity th | statement | not read in full | For every prime p and r+1<=N<=2r-1 with r>=2 a specified normal strict-local germ with both punctures regular has a non- |
| C.3ax | Proved | statement | not read in full | For every smooth connected projective cone in characteristic p with normal degree-one full section ring, restriction K0( |
| C.3ay | Refuted rational ordinary injectivity at | statement | not read in full | For every prime p and r>=2 a specified normal excellent strict-local germ of dimension2r with both punctures regular has |
| C.3az | Proved | statement | not read in full | For an algebraizable positive-characteristic strict-local germ with regular projective resolution and one smooth connect |
| C.3ba | Refuted integral finiteness in every hig | statement | not read in full | For every algebraically closed field of characteristic p>0 and every2<=r<=N-1 a specified excellent normal strict-local  |
| C.3bb | Refuted integral divisor finiteness in e | statement | not read in full | For every algebraically closed field of characteristic p>0 and N>=2 an explicitly specified excellent normal strict-loca |
| C.3bc | Proved | statement | not read in full | For an algebraizable strict-local germ over Fpbar admitting a regular projective SNC resolution with a positive exceptio |
| C.3bd | Proved | statement | not read in full | For a normal algebraizable strict-local surface or threefold germ over Fpbar with regular puncture, the rational top Cho |
| C.3be | Proved | statement | not read in full | For every excellent local domain R of dimension N>=2 with residue field Fpbar, CH_1(Spec R)_Q=CH^(N-1)(Spec R minus its  |
| C.3bf | Refuted universal integral ordinary degr | statement | not read in full | Over k=Fbar_5 and for every N>=4 an explicitly specified excellent normal strict-local N-fold with regular puncture and  |
| C.3bg | Proved | statement | not read in full | In every characteristic p>0 and every local dimension N>=3, algebraizable normal strict-local examples with regular punc |
| C.3bh | Proved/refuted in the stated dimensions | statement | not read in full | Complete universal integral ordinary Picard restriction table in positive characteristic: injective iff N=1; surjective  |
| C.3bi | Refuted universal integral ordinary codi | statement | not read in full | Over Fbar_5 an explicitly specified excellent normal strict-local fivefold with regular puncture and regular principal p |
| C.3bj | Refuted universal integral ordinary codi | statement | not read in full | For every algebraically closed field of characteristic p>0 and every N>=5 a specified excellent normal strict-local N-fo |
| C.3bk | Refuted universal integral ordinary inje | statement | not read in full | For every algebraically closed field of characteristic p>0 the stated excellent normal strict-local examples have an ord |
| C.3bl | Refuted universal integral ordinary rest | statement | not read in full | For every algebraically closed field of characteristic p>0, r>=2 and N>=2r, the specified strict-local regular-puncture  |
| C.3bm | Proved reduction | statement | not read in full | For every algebraically closed field of positive characteristic, the ordinary rational top quotient of every algebraizab |
| C.3bn | Proved under the stated resolution and a | statement | not read in full | For every algebraically closed characteristic-p field and every algebraizable excellent henselian coefficient-field loca |
| C.3bo | Proved reduction | statement | not read in full | For every exceptional SNC surface in C.3bm, the weighted Picard-to-component-Albanese intersection matrix is an isogeny, |
| C.3bp | Proved reduction | statement | not read in full | For every resolved SNC exceptional divisor of pure dimension d>=2 with a positive negative-ample exceptional combination |
| C.3bq | Proved in the stated scope | statement | not read in full | For exceptional SNC surfaces with a negative ample combination, the kernel of component CH0 restriction lies in the actu |
| C.3br | Proved under the stated triple-free and  | statement | not read in full | For a triple-free projective SNC surface over an algebraically closed characteristic-p field with surjective joint ratio |
| C.3bs | Proved under the stated dual-cohomology  | statement | not read in full | For a projective SNC surface in positive characteristic with H2 of its dual complex zero and surjective joint rational P |
| C.3bt | Proved in the stated scope | statement | not read in full | For a negative exceptional SNC surface in characteristic p>0 the component CH0 map from F_gamma^2 K0_Q is onto and its f |
| C.3bu | Proved (auxiliary strengthening) | statement | not read in full | Under the algebraizable positive-characteristic regular-modification and ample full exceptional Cartier-divisor hypothes |
| C.3bv | Proved (auxiliary strengthening) | statement | not read in full | For a noetherian local coefficient-k algebra with algebraically closed residue field k and a fixed smooth connected proj |
| C.3bw | Proved (auxiliary strengthening) | statement | not read in full | For any noetherian local coefficient-k algebra with algebraically closed residue field k and any fixed smooth connected  |
| C.4a | Proved | statement | not read in full | Degree-one mixed ample Lefschetz inverse is a unique normalized rational divisor correspondence independent of ell |
| C.4b | Proved | statement | not read in full | Inverse isogeny least denominator is kernel exponent; integral iff isomorphism; ell-integral iff degree prime to ell |
| C.4c | Proved | statement | not read in full | Question1 iff generic Albanese point lifts to degree-zero CH0; curves and all abelian varieties satisfy it |
| C.4d | Proved | statement | not read in full | Question2 for A iff A is an actual direct summand of a product of Jacobians |
| C.4e | Proved under stated hypotheses | statement | not read in full | For complex ppav Question2 iff integral minimal class algebraic; very general dimension>=4 fails |
| C.4f | Proved | statement | not read in full | Question2 holds for curves, Jacobians, their products, and ppav dimension<=3 |
| C.4g | Proved under stated hypotheses | statement | not read in full | Question1 for X and Question2 for AlbX imply Question2 for X integrally |
| C.4h | Proved | statement | not read in full | Scalar multiplication maps factoring through products of Jacobians form an ideal; generator one is equivalent to an actu |
| C.4i | Proved | statement | not read in full | For a g-dimensional abelian variety over any algebraically closed field the scalar obstruction divides (2g-1)!. |
| C.4j | Proved | statement | not read in full | For g<=3 the scalar obstruction divides gcd((2g-1)!,delta(A)) with delta(A)=gcd chi(L). |
| C.4k | Proved | statement | not read in full | Finite NS Euler-polynomial computation gives sufficient tests; same-dimensional prime-to-ell principalization is impossi |
| C.4l | Proved | statement | not read in full | For a complex NS-rank-one surface of type(1,d) with End=Z the divisor-product subring yields exactly gcd(6,d) multiples  |
| C.4m | Proved | statement | not read in full | For a principally polarized abelian variety of dimension at most five over any algebraically closed field, twice the ide |
| C.4n | Proved | statement | not read in full | For every abelian surface in every characteristic the scalar obstruction divides gcd(2,delta(A)); odd Euler characterist |
| C.4o | Proved | statement | not read in full | Every principally polarized sixfold over any algebraically closed field has an integral curve of class six times the min |
| C.4p | Proved | statement | not read in full | Every abelian threefold satisfies s_J(A)/gcd(6,delta(A)); separate polarization checks at2 and3 suffice for an actual di |
| C.4q | Proved | statement | not read in full | For simple complex A of dimension2 or3 with End(A)=Z and primitive rank-one NS type(1,d2,...,e), Fourier images of curve |
| C.4r | Proved | statement | not read in full | Over every algebraically closed field, for A of dimension2 or3 the actual Jacobian-summand property is equivalent to P^( |
| C.4s | Known | statement | not read in full | Every supersingular abelian surface over every algebraically closed field of positive characteristic is an actual direct |
| C.4t | Proved | statement | not read in full | For a complex type(1,2) surface the natural principal polarization on A x Adual is not a genus4 Jacobian; when End(A)=Z  |
| C.4u | Proved | statement | not read in full | Every supersingular abelian threefold over an algebraically closed field of characteristic at least five is an actual di |
| C.4v | Proved | statement | not read in full | Full Rosati-fixed degree-g real multiplication implies delta(A)=1 in characteristic zero; for any such order every prime |
| C.4w | Proved | statement | not read in full | Ordinary Rosati-fixed degree-g real multiplication has delta(A)=1 for the full integer ring; for any such order every pr |
| C.4x | Proved | statement | not read in full | Full Rosati-fixed real multiplication in characteristic p forces delta(A) to be a p-power; the Lie determinant condition |
| C.4y | Proved | statement | not read in full | Semihomogeneous Chern classes on A times its dual for End(A)=Z and primitive type(1,2) polarization cannot produce Poinc |
| C.4z | Proved | statement | not read in full | The explicit correlated rank-two forms admit no common Z_(2)-orthogonal graph splitting at any positive integer level |
| C.4aa | Proved | statement | not read in full | The rank-one forms x²,y²,(2x+y)² admit no common Z_(2)-orthogonal graph splitting at any positive level although they oc |
| C.4ab | Proved in the stated scope | statement | not read in full | For the stated complex type-(1,2) surface, actual Jacobian-product splitting, integral first-Kunneth-projector algebraic |
| C.5a | Proved | full | targeted proof check, confirmed | Over F̄_p, CH^r_alg is torsion and divisible, so αβ = (mα)γ = 0 integrally; answers the 14:30 margin over F̄_p (the rectangle ν is rationally 0). |
| C.5b | Known | full | known; deduction confirmed (Spiess-Szamuely 2003 Th. 1.2 not opened by me) | Integral Albanese isomorphism on CH_0^0 over F̄_p, p-part included. |
| C.5c | Proved | full | targeted proof check, confirmed | Explicit generic rectangle on E×E of infinite order: decomposition-of-diagonal argument on H^{2,0} (Bloch-Srinivas/Mumford method). Answers the 14:30 margin over C. |
| C.5d | Refuted | full | refutation confirmed | Every universal member of the 14:126 chain fails over C, integrally and rationally, from C.5c. |
| C.5e | Proved | full | targeted proof check, confirmed | Universal 4° => 3°bis via Jacobians and chains of curves. |
| D.0a | Proved under stated hypotheses | statement | not read in full | R3 band and used local assertions rechecked under the Tate identification |
| D.0b | Proved | statement | not read in full | R8 compact real torus cohomology and parity-torsor calculation |
| D.1a | Proved | statement | not read in full | Slope parity exists exactly for values in Z_(2), including subgroups with torsion |
| D.1b | Proved | statement | not read in full | Intersection of all odd-denominator domains is the largest Galois-stable slope-parity domain |
| D.1c | Refuted proposed remedy | statement | not read in full | D(Q) cannot supply a nontrivial mu_2 lift |
| D.1d | Proved | statement | not read in full | q=25 and lambda=15+20i have slopes 3/2 and 1/2; real fibres still exist |
| D.1e | Proved at character level | statement | not read in full | Full Weil-number group has no R8 real-point parity; full even-weight group has a unique parity |
| D.2a | Proved | statement | not read in full | Real finite-type torus orbits are one orbit in odd weight, and zero/nonzero complement orbits in even weight |
| D.2b | Refuted general transitivity | statement | not read in full | Rational automorphism transitivity fails, with exact finite character-lattice orbit invariant |
| D.3a | Proved in a compatible Galois-cocycle pr | statement | not read in full | Inversion of an abelian band lifts coherently with order two iff 2h=0 |
| D.3b | Proved under R3 band identification | statement | not read in full | The actual Artin/Tate-rigidified motivic gerbe has infinite-order class |
| D.4a | Proved under stated hypotheses | statement | not read in full | Coincidence of transported polarizations follows from specialization-compatible algebraic polarizations |
| D.4b | Proved equivalence | statement | not read in full | Recovery of effectivity cone is equivalent to spectral integrality implying effectivity |
| D.4c | Proved criterion | statement | not read in full | A quotient specialization preserves polarization when trace forms are positive on the new endomorphisms |
| D.4d | Known with derivation | statement | not read in full | CM reduction preserves geometric polarizations, with an unconditional Lefschetz-cycle version |
| D.4e | Proved under cited 2026 theorem | statement | not read in full | Integral Frobenius eigenvalues characterize effective finite-field motives of abelian type |
| D.4f | Proved under the stated numerical-motive | statement | not read in full | All-motives spectral effectivity, Frobenius-identity effectivity and the full Tate cycle conjecture are equivalent |
| D.4g | Proved under cited 2026 theorem and expl | statement | not read in full | All specializations of polarized abelian families preserve one common geometric polarization |
| E.1a | Proved | full | targeted proof check, confirmed | Galois connection E/I; Sat = I∘E a closure; saturated sets <-> intersections of P(ν). Answers 14:9's unspecified 'saturation'. |
| E.1b | Proved | full | targeted proof check, confirmed | Torus: Sat(C) = integral bipolar (Galois orbit of m in C^∨ is an effective rational rep.); reductive: V(m) weights in conv(Wm). Same argument as my 14:11 reading. |
| E.1c | Refuted | full | refutation confirmed (counterexample checked) | C = N(1,1)+N(1,-1) on G_m × R^1 G_m: Galois-stable, contains j=(2,0), ε interior to the real polar, Sat(C) = {a>=/b/} ∋ (1,0) ∉ C; root-saturated C_open also unsaturated. Answers 14:9 '(est-elle automatiquement satisfaite ?)': no, for additive cones. |
| E.1d | Proved under stated hypotheses | full | targeted proof check, confirmed | C = K∩N, K closed convex, ε interior to K^∨: separation, perturbation m+tε, rational approximation. Exactly his 14:9 margin condition. |
| E.1e | Proved | full | targeted proof check, confirmed | P(ν) closures; uniform twist by compactness of the section ⟨ε,·⟩=1. Matches my CE 14:9. |
| E.2a | Proved under stated hypotheses | statement | not read in full | Arithmetic effectivity is intersection of rational slope halfspaces; motivic effectivity under Tate. |
| E.2b | Refuted | statement | not read in full | Full M(q) admits normalized integral i1 with i1(q)=1. |
| E.2c | Proved | statement | not read in full | Integrality criterion for a specified slope on a finite character subgroup. |
| E.2d | Proved | statement | not read in full | Finite CM effective cone recovers rational slope orbit and decomposition field. |
| E.2e | Refuted | statement | not read in full | Finitely many simple effective types in each weight globally. |
| E.3a | Proved | full | targeted proof check, confirmed | N^i, P^i; P^1=Pic^0(k), P^n=Alb(k) (both directions of 14:29 Th. 1.4); product rectangle (14:30 Th. 1.6); abelian replacement up to m (14:32-34) as in my item 5. |
| E.3b | Proved | full | targeted proof check, confirmed (cited ACMV 2022 Ex. 1.14, Th. 9.1, 9.3 not opened by me) | Th. 3.1 of 14:38 in char 0 via the regular Abel-Jacobi map and the cylinder map; careful spreading-out transfer (better than my 'reduce to C'). |
| E.3c | Proved | full | targeted proof check, confirmed | Over C: rational converse <=> AJ⊗Q injective on P^i⊗Q (my hunch c14a-H5, now proved as a reduction). |
| E.3d | Proved | full | targeted proof check, confirmed | i=1, n: family maps are homomorphisms of abelian varieties; zero iff zero on rational Tate modules. |
| E.3e | Proved | full | targeted proof check, confirmed (Bloch 1979 Prop. 3.5, 3.8, 3.9, Th. 4.2 not opened by me) | Th. 3.1 in every char p, integral premise: torsion lemma by spreading the whole relation and specializing to F̄_p (prime-to-ℓ isogeny Alb(T_s)->B_s, Roitman-Bloch, C.5a), then Tate modules. Settles the char-p case I left open on 14:38. |
| E.3f | Refuted | full | refutation confirmed (counterexample checked) | y^2=x^3-x over F̄_5 (disc 64≡4), Z=Δ−X×{0}: u_Z⊗Q=0 (points torsion) but identity on H^1. The rational premise is vacuous over F̄_p. |
| E.3g | Proved | statement | not read in full | Every algebraically trivial cycle is integrally a point of an abelian family; all regular invariants kill N^i, which is  |
| E.3h | Refuted | statement | not read in full | Integral Albanese and ordinary Abel-Jacobi equivalence differ on algebraically trivial cycles from abelian families, in  |
| E.3i | Proved | statement | not read in full | A finite Walker isogeny obstruction cannot detect failure of the zero-cohomology family-map converse |
| E.3j | Proved | statement | not read in full | Integral family-map converse for one-cycles when CH0 is supported on a curve |
| E.3k | Refuted | statement | not read in full | Literal integral LeadE4 biconditional is false on the same Ottem-Suzuki fourfold; exact fixed-target Walker-kernel crite |
| E.3l | Proved | statement | not read in full | Canonical integral P^{n-1}(X) equals Walker Jacobian points if CH0(X) is supported on a surface |
| E.3m | Proved | statement | not read in full | Integral family converse is equivalent to the exact equality N^i=ker Walker and to P^i=Walker Jacobian points |
| E.3n | Proved | statement | not read in full | Over C a torsion-valued abelian-family map to P^i vanishes; rational and integral family converses are equivalent |
| E.3o | Known | statement | not read in full | Integral Walker kernel equals Saito's product A*H, while N is the zero-cycle-generated relation <H*2>_0; the general fam |
| E.3p | Proved | statement | not read in full | The manuscript's N is generated integrally by Albanese kernels of smooth projective surfaces |
| E.3q | Proved under stated hypotheses | statement | not read in full | For varieties with CH0 supported on a surface, P2 is integrally the Walker and ordinary algebraic intermediate Jacobian  |
| E.3r | Proved | statement | not read in full | The displayed 72-parameter geometric generic Enriques pencil times an independent Legendre elliptic curve has a nonzero  |
| E.3s | Proved | statement | not read in full | The integral generated Albanese quotient is the connected point group of the large one-motivic Chow Albanese sheaf |
| E.3t | Proved | full | targeted proof check of the deduction, confirmed; inputs Walker 2007 Ex. 5.5, Th. 5.7, Prop. 3.3, Cor. 5.9 not opened by me | Morphic AJ kills N^i; family zero in the morphic Jacobian iff Lawson cylinder zero; u_Z=0 => λ_Z=0 => a(^tZ)=0. |
| E.3u | Refuted | full | targeted proof check of the deduction, confirmed; inputs Friedlander 2000 Th. 3.4 with Nagel's bound and Walker 2007 Th. 6.2 product computation not opened by me | Converse of 14:38 false over C even rationally: X = Y×E, Y a geometric generic degree-14 section of the split 6-quadric, γ = difference of two 3-plane traces (cl=0, sγ≠0 in L_1H_4), Z = γ×(Δ_E−E×o). Checked: ζ^2=−2, hζ=0, H_4(Y)=Z by weak Lefschetz, cl(Z)=0, injectivity of the Lawson cylinder from the product formula, countability. |
| E.4a | Proved with explicit Geisser negative-tw | statement | not read in full | All Weil-etale Tate groups over Fq, all integer twists, with p-primary part |
| E.4b | Refuted | statement | not read in full | The exact integral Spec Z table equals standard compactified Weil-etale cohomology |
| E.4c | Proved in the bounded localization exten | statement | not read in full | Open-subset twist-one groups from purity and normalized trace |
| E.4d | Refuted under explicitly stated comparis | statement | not read in full | Literal twist-one table is incompatible with the usual coefficient triangle and degree-zero Kummer comparison |
| E.4e | Proved for the specified bounded derived | statement | not read in full | Canonical normalized Gysin and explicit coherent twist-one open complexes, with finite coefficients |
| E.4f | Proved at the complex level | statement | not read in full | A specified sign deletion realizes the literal tables and preserves stated localization and proper duality |
| E.4g | Proved | statement | not read in full | Every rational twist on compactified Spec Z and a coherent rational extension to all finite-prime opens |
| E.4h | Proved, with prime-to-p scope made expli | statement | not read in full | Continuous cohomology of the procyclic Galois group and the obstruction to a characteristic-prime cyclotomic lattice |
| E.4i | Proved with explicit descent | statement | not read in full | Brauer injectivity under strict-local factoriality and finite-etale descent criterion over a local ring |
| E.4j | Refuted with an explicit totally real qu | statement | not read in full | Integral all-twist purity with the finite-field values and ordinary finite-coefficient comparison on opens |
| E.4k | Refuted, even without integral purity | statement | not read in full | Finite generation on arithmetic opens with the desired rational restriction table and every finite-coefficient compariso |
| E.4l | Proved | statement | not read in full | Actual twist-zero local support and all groups of every finite-prime real-place-retaining open |
| E.4m | Proved with stipulated Flach--Morin nega | statement | not read in full | Every negative twist has an explicit wild local Galois-cohomology correction |
| E.4n | Proved | statement | not read in full | Full integral purity in all positive weights n>=2 on the specified number-ring opens |
| E.4o | Proved on the stated family of opens | statement | not read in full | The explicit twist-one open localization complex has the actual Artin--Verdier finite-coefficient comparison |
| E.4p | Proved with explicitly restricted scope | statement | not read in full | A coherent all-twist bounded integral extension with all finite-coefficient comparisons and explicit wild localization |
| E.5a | Known with derivation | statement | not read in full | Any two neutral fibre functors over an algebraically closed field are isomorphic, without cardinality restrictions |
| E.5b | Refuted as a universal affine-gerbe stat | statement | not read in full | Perfection alone makes all pro-fibre functors isomorphic |
| E.5c | Proved and computed | statement | not read in full | Crystalline fibres at two points may be nonisomorphic even after isogeny |
| E.5d | Proved for the specified structured modu | statement | not read in full | Frobenius structures use sigma-conjugacy and lattices use X_mu(b), not ordinary unstructured H1 |
| E.5e | Proved | statement | not read in full | Unstructured W(k)-valued fibre torsors vanish under smoothness, and under connectedness over perfect cd<=1 residue field |
| E.5f | Refuted with an explicit affine fpqc tor | statement | not read in full | Trivial finite-stage fibre torsors imply a trivial pro-torsor over a perfect field of cd<=1, or over its Witt vectors |
| E.5g | Proved | statement | not read in full | Connected transition kernels or compact point sets give coherent pro-level trivializations |
| E.6a | Proved | statement | not read in full | Artin--Tate local comparison class is [decomposition embedding,1] |
| E.6b | Proved | statement | not read in full | Over a number field the comparison class is the tuple over v/l |
| F.2a | Proved | statement | not read in full | Two normalization corrections in the supplied Tate survey |
| F.2b | Known | statement | not read in full | Published correction of the supplied numerical positivity-cone statements |

## 2. What is new (rows read in full)

- **E.3e (Theorem 3.1 of 14:38 in every positive characteristic, integral premise).** I find it stated in this form
  nowhere I know; its ingredients are classical (Bloch's torsion map, Bloch 1979; Roitman's theorem; specialization of
  Chow groups), and the new step is the torsion lemma that specializes the whole Albanese-kernel relation at once rather
  than its (possibly non-torsion) generators. E.3f shows the integral premise cannot be weakened. Modest novelty, correct.
- **E.3u (the converse of Theorem 3.1 fails over C even rationally).** In substance this is Walker's example of
  Abel-Jacobi-trivial, morphically nontrivial cycles (Walker, The morphic Abel-Jacobi map, 2007, Th. 6.1-6.2, as the run
  cites it: locator unverified by me), made explicit (a geometric generic degree-14 section of the split 6-quadric, with
  Nagel's effective bound in place of an unspecified large degree) and applied to Grothendieck's question. New: the
  application and the explicit specification, not the phenomenon. With E.3c it gives the exact statement: over C the
  converse is equivalent to rational Abel-Jacobi injectivity on P^i, and that injectivity fails.
- **E.1 (the saturation of 14:9).** Elementary convex geometry; new only as the answer to his question: saturation is
  C = I(E(C)); not automatic for additive Galois-stable cones (E.1c); automatic for closed convex lattice cones with ε
  interior to the polar (E.1d), which is his own margin condition.
- **C.1a-e, C.5a-e, B.1a.** Known in substance: Griffiths (1969) and Clemens (1983) for the quintic; Mumford (1969) and
  the Bloch-Srinivas method for rectangles; Spiess-Szamuely (2003) and Kato-Saito for F̄_p; Milne (1994, Prop. 2.6) for
  B.1a (all locators as the run gives them, unverified by me). The packaging is new and correct: C.1c (the divisor-to-curve
  cokernel is exactly G^{n-1}), C.1e (letter-B for a fixed variety does not give algebraic = numerical), C.5c (an explicit
  generic rectangle of infinite order on E × E).
- Against our own results: E.1 and E.3 answer open points of my sweep-3 reading (section 3); B.1a settles an item recorded
  open in STUDY.md §1. Michel Hua's project had already stated the refutation of the 1965 algebraic-equivalence
  conjectures and the publication of the letter (my reading, item 8); the run agrees.

## 3. Implications for the archive and the programme

Archive (cote 14 and 15, by scan):
- **14:9.** "une condition de saturation que nous ne précisons pas ici (est-elle automatiquement satisfaite ?)": the
  condition is C = I(E(C)) (E.1a); not automatic in the additive reading (E.1c); automatic when "cône" means K ∩ N with ε
  interior to K^∨ (E.1d), the condition of his margin. Close the open point in my item 1.
- **14:30, margin "On ignore si cet ν est lin. équiv. à 0".** Over F̄_p: yes, integrally (C.5a). Over C: no, explicit
  infinite-order rectangle on E × E (C.5c). My reading answered it over C via Mumford and over F̄_p via Kato-Saito; the run's
  C.5a gives the elementary F̄_p proof (torsion and divisibility).
- **14:38-39, Theorem 3.1.** True in characteristic 0 (E.3b) and in every characteristic p with the integral premise (E.3e),
  which settles the case my item 6 left open; "C(k) -> A(k) surjectif" is literally false for dim A >= 2 (the run's remark
  after E.3u: the curve generates A through its Jacobian), a slip of his that my reading did not flag; the degree
  H^{2(n-i)+1} is the right one (my correction C10). **"A-t-on une réciproque": no over C, even rationally (E.3u)**;
  equivalent to rational AJ injectivity on P^i (E.3c, my hunch c14a-H5, now proved as a reduction and refuted as a
  statement); true for i = 1, n (E.3d) and under surface support of CH_0 (E.3j, E.3l, E.3q: not read in full).
- **14:44-47, the letter.** C.1a-b confirm my item 8: A, A', A'' and "τ-équivalence = équivalence numérique" fail modulo
  algebraic equivalence. C.1b's refutation of A' (any smooth hyperplane section: NS(Y)_Q finite against G infinite) is
  simpler than mine, which used a very general Y and Moishezon's theorem; the Moishezon step is unnecessary.
- **14:126 (outside my stretch).** The chain 1°-6° holds over F̄_p and fails over C (C.5a-e).
- **15:100-106 (STUDY.md §1).** The "conjecture forte" (every Weil q-integer of weight i a Frobenius eigenvalue on H^i
  over F_q) is **true in every weight** by root extraction and Honda-Tate (B.1a; Milne 1994): STUDY.md's "I know no
  reference settling it" should be corrected.
- **15:70 (A.8).** The run reports that the official scan 70 ends after "égal", as STUDY.md records ("cut off").

Programme:
- My sweep-3 hunches: c14a-H5 is decided (E.3c, E.3u). c14a-H2 (Frobenius interpretation of effectivity) is taken up by
  E.2a ("arithmetic effectivity is the intersection of rational slope half-spaces") and D.4f (all-motives spectral
  effectivity equivalent to the full Tate conjecture, under the stated framework): the finite-field counterpart of my
  c14a-H1 (effectivity through the Hodge cocharacter and the generalized Hodge conjecture). Not read in full; worth a
  targeted check in the next intake round.
- The rows the programme rests on most (C.3e used by 17; C.4j, C.4p, C.4n; A.1d; B.4a) were not checked in this intake.
  They need their own targeted checks before anything is built on them.

## 4. Bridges (redone 20 Nov 2026 under the corrected criterion of the brief, step 4)

The earlier version of this section said that no row bears on Alpöge's result. That was wrong under the corrected criterion and is replaced here. The two principles used below:

- **GRH for Dirichlet L-functions** (L. Alpöge, *Remark*, https://alpo.ge/remark.pdf, with the Lean archive) is the Riemann hypothesis for the rank-one Artin-Tate motives χ ⊗ Q(n) over Q, since L(χ ⊗ Q(n), s) = L(χ, s+n): the zeros in the critical strip lie on Re s = 1/2 - n. By sums it holds for every Artin-Tate motive over Q with abelian Artin part, the Dedekind zeta functions of abelian fields included. The center 1/2 - n is never an integer: GRH says nothing about values or orders of vanishing at integers (Borel, Lichtenbaum, Beilinson, Bloch-Kato), which the Γ-factors and the K-groups fix.

- **Deligne's purity** (La conjecture de Weil I, Publ. IHÉS 43 (1974); II, 52 (1980): locators of the theorems as usually cited, not opened in this intake) is the Riemann hypothesis over finite fields: Frobenius weights of Tate twists (Q(n) has weight -2n) and of every pure motive.

Rows covered: the 98 flagged rows of BRIDGE_FLAGS.tsv, all assigned below (none missing), and 12 unflagged rows that treat positivity, class numbers as L-values, or the standard conjectures (A.8a, A.8c, B.3b, B.4a, B.4b, B.4c, B.4d, B.4e, C.1j, C.1o, C.1p, C.2k).

### 4.1 The links, family by family

- **Weil numbers realized over F_q** (B.1a, B.1b, B.2a, B.3a, B.3b). Purity (Deligne, Weil I, Th. 1.6) gives: the Frobenius eigenvalues on H^i of a smooth projective X/F_q are Weil q-integers of weight i. The rows give back the converse: every Weil q-integer of weight i occurs on H^i of an abelian-variety power over F_q (B.1a by root extraction and Honda-Tate), so the RH constraint over F_q is exactly sharp: the reciprocal zeros of P_i(X,t) range over all Weil q-integers of weight i (B.2a). Alpöge's RH/GRH: no link (these are finite-field zeta functions).

- **Weil conjectures from the standard conjectures** (C.2j). Purity (Deligne) now gives unconditionally the absolute values that C.2j derives from the standard conjectures; what C.2j derives beyond Deligne (Frobenius semisimplicity, the cycle-theoretic integrality route) stays conditional. Nothing goes back to RH.

- **positivity (the letter's B, the Hodge standard conjecture)** (C.1d, C.1e, C.2c, C.2d, C.2k, C.1j, C.1o, C.1p). Positivity is Grothendieck's road to RH over F_q: a positive involution on the algebra of correspondences forces |α| = q^{w/2} (the Kähler argument the letter announces: the absolute values 'justiciable de B'). For curves it is a theorem: the Hodge index theorem on C × C (C.1d: 'surface B by the Hodge index theorem') gives RH for the curve C over F_q (Weil; Grothendieck, Sur une note de Mattuck-Tate, 1958). Deligne proved purity without B; purity does not give B back (the Hodge standard conjecture in characteristic p remains open). Alpöge's RH concerns zeta of Spec Z, not these positivity statements: no link.

- **Griffiths groups and algebraic vs homological equivalence over C** (C.1a, C.1b, C.1c, C.1f, C.1l, C.1n, C.1q, C.2b, C.2e, C.2i, C.3a, C.3b, C.3c, C.3d). Frobenius eigenvalues and the zeros of zeta and L-functions see only cohomology; these rows concern the kernel of the cycle class map (Griffiths groups), which no zeta function sees. The would-be bridge is Beilinson-Bloch: for X over a number field, rank CH^i_hom(X) = ord_{s=i} L(H^{2i-1}(X), s), a central point. It carries nothing here: very general complex varieties have no L-function, and H^3 of a quintic is not an Artin-Tate motive, so Alpöge's Dirichlet GRH does not reach it.

- **Weil-number group, weights, real points, gerbes** (D.0b, D.1a, D.1b, D.1c, D.1d, D.1e, D.2a, D.2b, D.3a). Purity (Deligne) places the Frobenius of a pure motive of weight w in the weight-w part of the Weil-number group (|λ|^2 = q^w); the real-point parity, orbit and gerbe statements are statements about that group and its band. Nothing goes back to RH, and Alpöge's result has no finite-field content: no link beyond the weight grading purity supplies.

- **polarizations under specialization; effectivity from Frobenius** (D.4a, D.4b, D.4c, D.4d, D.4e, D.4f, D.4g, E.2a, E.2b, E.2c, E.2d, E.2e). Positivity of the Rosati involution is Weil's proof of RH for abelian varieties (|α|^2 = q). The polarization rows (D.4a, c, d, g) keep a positive involution through specialization, hence keep that proof available on the special fibre; no new RH content. For effectivity (D.4b, e, f; E.2a-e): purity gives the archimedean condition |λ| = q^{w/2} for every conjugate; effectivity also needs p-adic integrality, slopes >= 0 (Katz's conjecture, Mazur's theorem: Newton above Hodge). The rows give back the p-adic half: arithmetic effectivity is the intersection of rational slope half-spaces (E.2a). D.4f (all-motives spectral effectivity iff the Tate conjecture) uses purity to identify Tate classes with the weight-0 Frobenius-fixed part of H^{2i}(i).

- **cycles, Albanese and Abel-Jacobi over finite fields** (C.5a, C.5b, C.5c, C.3ac, E.3a, E.3b, E.3c, E.3d, E.3e, E.3f, E.3s, E.3u). Purity (Deligne) gives H^1(F_q, H^{2i-1}(X̄, Q_l(i))) = 0, since Frobenius has weight -1 on H^{2i-1}(i) and so no eigenvalue 1: the l-adic Abel-Jacobi image of homologically trivial cycles over a finite field is torsion. This is the cohomological reason for Beilinson's conjecture that CH^i_hom(X)_Q = 0 over finite fields. The rows give back unconditional parts of it: algebraically trivial cycles over F̄_p are torsion and their products vanish (C.5a); the Bloch map kills Albanese-trivial torsion (E.3e). With Kato-Saito at the finite level, #CH_0(X/F_q)^0 = #Alb_X(F_q) = |P_1(1)|, and Weil's RH for abelian varieties bounds it between (√q-1)^{2g} and (√q+1)^{2g} (C.5b). Over C (C.5c, E.3u, E.3b-d, E.3s) there is no Frobenius and no L-function: no link.

- **Weil-étale cohomology with Z(n), Artin-Verdier, special values** (E.4a, E.4b, E.4c, E.4d, E.4e, E.4f, E.4g, E.4h, E.4i, E.4j, E.4k, E.4l, E.4m, E.4n, E.4o, E.4p). This is the cohomology of the twisted Tate motives over F_q, Spec Z and number rings (Spec Z has étale cohomological dimension 3, Artin-Verdier duality). Over F_q: the weight of Q(n) is -2n, so Frobenius acts by q^n ≠ 1 for n ≠ 0 and the groups are finite; Lichtenbaum's formula reads |ζ(F_q, -n)| = 1/(q^n - 1) = 1/#K_{2n-1}(F_q) (Quillen). Over Spec Z the Euler characteristic of RΓ_W(Spec Z̄, Z(n)) is to give ζ*(n) (Lichtenbaum, Flach-Morin). RH (Alpöge) gives: all nontrivial zeros of ζ lie on Re s = 1/2, and GRH: those of L(χ ⊗ Q(n), s) = L(χ, s+n) on Re s = 1/2 - n. The center 1/2 - n is never an integer, so neither RH nor GRH changes a special value or an order of vanishing at an integer (those are fixed by the Γ-factors and Borel's ranks). The rows give back the integral cohomological side of the special-value formulas; no zero-location content. Note: the 'purity' of E.4c, E.4j, E.4n is cohomological (Gysin) purity, not Deligne's weights.

- **fibre functors, torsors, crystalline points** (E.5a, E.5b, E.5c, E.5d, E.5e, E.5f, E.5g). Purity with Katz-Messing (1974) makes the characteristic polynomial of crystalline Frobenius equal the l-adic one, so weights are constant in a family while the Newton slopes may jump: E.5c (crystalline fibres at two points nonisomorphic) is the slope side. The torsor rows (E.5a, b, d-g) have no weight or L-function content: no link.

- **effectivity cones in representation theory** (E.1a, E.1b, E.1c, E.1d, E.1e). Only the normalization ⟨ε, j⟩ = 2 (Q(1) of weight -2) that purity fixes; no Frobenius, no L-function: no link.

- **Artin-Tate motives and their gerbes** (E.6a, A.7a, D.0a, D.3b). GRH for Dirichlet L-functions (Alpöge) is RH for the rank-one Artin-Tate motives χ ⊗ Q(n), L(χ ⊗ Q(n), s) = L(χ, s+n), hence for every Artin-Tate motive over Q with abelian Artin part. E.6a's local class is the decomposition-group datum that gives the Euler factor (1 - χ(p) p^{-n-s})^{-1}: the row is local, GRH global; nothing goes back. A.7a, D.0a, D.3b concern the band and the class of the motivic gerbe (an H^2 class), which the zeros do not see: no link.

- **Jacobian summands, Lefschetz inverses, real multiplication** (C.4a, C.4b, C.4c, C.4d, C.4e, C.4f, C.4g, C.4i, C.4x). A polarization is the positivity behind Weil's RH for abelian varieties; these rows (summands of Jacobians, denominators of Lefschetz inverses, δ(A), real multiplication) do not touch Frobenius eigenvalues or zeros: no link.

- **notation** (F.2a). Normalizations of Tate twists in a survey: no link.

- **class numbers as L-values (unflagged, added)** (A.8a, A.8c, B.4a, B.4b, B.4c, B.4d, B.4e). Class numbers are L-values: h(-D) = (√D/π) L(1, χ_{-D}) for D > 4. GRH for the quadratic Dirichlet character (Alpöge) gives Littlewood's bounds L(1, χ_{-D}) between c/log log D and C log log D, hence h(-p) and h(-4p) between √p/log log p and √p log log p up to constants; by Deuring and Eichler the number of F_p-rational supersingular j-invariants is a combination of these (A.8a), so GRH bounds it the same way. The rows give back exact counts (Eichler's mass formula, h(R) of A.8c) that these bounds estimate. For B.4's CM fields L: when L is abelian, ζ_L is a product of Dirichlet L-functions, and GRH gives an effective upper bound for h(L)R(L) through ∏ L(1, χ), hence an a priori bound for the power 2h|D_p|/|μ(L)| of B.4e; for non-abelian L the input stays conditional.

### 4.2 Row by row

| Row | Family | Flagged | Link (see 4.1) |
|---|---|---|---|
| A.7a | Artin-Tate motives and their gerbes | yes | GRH = RH for χ⊗Q(n); row local or H^2 |
| A.8a | class numbers as L-values (unflagged, added) | added | GRH => Littlewood/effective class-number bounds |
| A.8c | class numbers as L-values (unflagged, added) | added | GRH => Littlewood/effective class-number bounds |
| B.1a | Weil numbers realized over F_q | yes | purity: constraint sharp |
| B.1b | Weil numbers realized over F_q | yes | purity: constraint sharp |
| B.2a | Weil numbers realized over F_q | yes | purity: constraint sharp |
| B.3a | Weil numbers realized over F_q | yes | purity: constraint sharp |
| B.3b | Weil numbers realized over F_q | added | purity: constraint sharp |
| B.4a | class numbers as L-values (unflagged, added) | added | GRH => Littlewood/effective class-number bounds |
| B.4b | class numbers as L-values (unflagged, added) | added | GRH => Littlewood/effective class-number bounds |
| B.4c | class numbers as L-values (unflagged, added) | added | GRH => Littlewood/effective class-number bounds |
| B.4d | class numbers as L-values (unflagged, added) | added | GRH => Littlewood/effective class-number bounds |
| B.4e | class numbers as L-values (unflagged, added) | added | GRH => Littlewood/effective class-number bounds |
| C.1a | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.1b | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.1c | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.1d | positivity (the letter's B, the Hodge standard conjecture) | yes | positivity => RH over F_q; not back |
| C.1e | positivity (the letter's B, the Hodge standard conjecture) | yes | positivity => RH over F_q; not back |
| C.1f | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.1j | positivity (the letter's B, the Hodge standard conjecture) | added | positivity => RH over F_q; not back |
| C.1l | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.1n | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.1o | positivity (the letter's B, the Hodge standard conjecture) | added | positivity => RH over F_q; not back |
| C.1p | positivity (the letter's B, the Hodge standard conjecture) | added | positivity => RH over F_q; not back |
| C.1q | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.2b | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.2c | positivity (the letter's B, the Hodge standard conjecture) | yes | positivity => RH over F_q; not back |
| C.2d | positivity (the letter's B, the Hodge standard conjecture) | yes | positivity => RH over F_q; not back |
| C.2e | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.2i | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.2j | Weil conjectures from the standard conjectures | yes | purity supersedes part |
| C.2k | positivity (the letter's B, the Hodge standard conjecture) | added | positivity => RH over F_q; not back |
| C.3a | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.3ac | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| C.3b | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.3c | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.3d | Griffiths groups and algebraic vs homological equivalence over C | yes | carries nothing (cohomology-blind) |
| C.4a | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4b | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4c | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4d | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4e | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4f | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4g | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4i | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.4x | Jacobian summands, Lefschetz inverses, real multiplication | yes | carries nothing |
| C.5a | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| C.5b | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| C.5c | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| D.0a | Artin-Tate motives and their gerbes | yes | GRH = RH for χ⊗Q(n); row local or H^2 |
| D.0b | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.1a | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.1b | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.1c | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.1d | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.1e | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.2a | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.2b | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.3a | Weil-number group, weights, real points, gerbes | yes | purity: weight grading only |
| D.3b | Artin-Tate motives and their gerbes | yes | GRH = RH for χ⊗Q(n); row local or H^2 |
| D.4a | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| D.4b | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| D.4c | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| D.4d | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| D.4e | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| D.4f | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| D.4g | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| E.1a | effectivity cones in representation theory | yes | normalization only |
| E.1b | effectivity cones in representation theory | yes | normalization only |
| E.1c | effectivity cones in representation theory | yes | normalization only |
| E.1d | effectivity cones in representation theory | yes | normalization only |
| E.1e | effectivity cones in representation theory | yes | normalization only |
| E.2a | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| E.2b | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| E.2c | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| E.2d | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| E.2e | polarizations under specialization; effectivity from Frobenius | yes | Rosati positivity / slopes complement purity |
| E.3a | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.3b | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.3c | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.3d | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.3e | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.3f | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.3s | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.3u | cycles, Albanese and Abel-Jacobi over finite fields | yes | purity => AJ torsion over F_q; rows give unconditional parts |
| E.4a | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4b | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4c | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4d | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4e | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4f | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4g | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4h | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4i | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4j | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4k | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4l | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4m | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4n | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4o | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.4p | Weil-étale cohomology with Z(n), Artin-Verdier, special values | yes | special values at integers; RH/GRH zeros off integers |
| E.5a | fibre functors, torsors, crystalline points | yes | weights constant, slopes vary |
| E.5b | fibre functors, torsors, crystalline points | yes | weights constant, slopes vary |
| E.5c | fibre functors, torsors, crystalline points | yes | weights constant, slopes vary |
| E.5d | fibre functors, torsors, crystalline points | yes | weights constant, slopes vary |
| E.5e | fibre functors, torsors, crystalline points | yes | weights constant, slopes vary |
| E.5f | fibre functors, torsors, crystalline points | yes | weights constant, slopes vary |
| E.5g | fibre functors, torsors, crystalline points | yes | weights constant, slopes vary |
| E.6a | Artin-Tate motives and their gerbes | yes | GRH = RH for χ⊗Q(n); row local or H^2 |
| F.2a | notation | yes | carries nothing |

The remaining unflagged rows (the local C.3 programme, the C.4 summand rows not listed, the Deuring rows A.1-A.6, the E.3 Walker and Saito rows) have no Tate-twist, weight, L-value or positivity content in their statements: no link.

## 5. Prompt updates (for a successor of this run)

- Do not redo: E.1a-e, E.3a-f, E.3t-u, C.1a-e, C.5a-e, B.1a (settled; checked here).
- Carry the archive corrections of the sweep-3 reading of cote 14 (`readings/c14_c15rest_part1.md`, CORRECTIONS C1-C10)
  into the package, so that the run works from the ink: in particular 14:3 ("engendré par les éléments de la base
  canonique"), 14:7 ("contenant j"), 14:9 ("la classe de i" read j), 14:15 ("relation de finitude"), 14:24 ("Consulter Weil,
  Critères d'Équivalence"), 14:38 (degree 2(n-i)+1); and the printed letter (Correspondance Grothendieck-Serre, SMF 2001,
  pp. 232-234) with the two differences of the archive copy ("A et B impliquent"; the N.B. on twists).
- Open work the successor should take, with the gate: D.4f (the one open row: prove or refute the equivalence of
  all-motives spectral effectivity with the Tate conjecture in the stated framework); rational AJ injectivity on P^i in
  the cases between surface support and E.3u (which X?); the C.3 "global and rational top gates" and C.4 nonprincipal cases
  named in the status table; A.8 is a historical-text item that cannot be completed (the page ends).
- Ask the run to open and quote, with page, every cited theorem it relies on for a refutation: Walker 2007 (Th. 5.7,
  Prop. 3.3, Ex. 5.5, Th. 6.2), Friedlander 2000 (Th. 3.4), Nagel's effective bound, Clemens 1983 (Th. 0.2), Bloch 1979
  (Prop. 3.5, 3.8, 3.9, Th. 4.2), Spiess-Szamuely 2003 (Th. 1.2), ACMV 2022 (Th. 9.1, 9.3), Milne 1994 (Prop. 2.6).
- The checks this intake did not make: targeted checks of C.3e, C.4j, C.4n, C.4p, A.1d, B.4a, E.2a, D.4a-g, and of the
  included E.3g-s files.

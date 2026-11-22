# F13.5/F13.6 research after checkpoint07

Status: **INCOMPLETE**. This note distinguishes the audited reductions from
the still missing complete-local cohomology estimate. It was written by
GPT-6 Astra (OpenAI, ChatGPT Pro mode); it makes no priority claim.

## Audited and integrated results

The authoritative complete proofs are F_bounded_cyclic_reduction.tex
(F13c/d), F_refined_swan_zeros.tex (F13e),
F_small_conductor_corollary.tex (F13f), and F_swan_residue_gap.tex
(F13g/h), all appended to owner F.tex after root audits. In particular:

- Unramified p-primary characters on each finite étale resolution cover
  form a divisible group. The proof uses proper henselian specialization
  and Artin–Schreier H²(D,Fp)=0, with F−1 surjective on finite-dimensional
  H¹(D,O_D).
- Every p-primary character is an unramified twist of a character of
  bounded p-power order, with one exponent independent of the degree of
  the resolution cover.
- The total zero length of the refined-Swan sections on those original
  exceptional components is bounded linearly in that degree. The exact
  component bound is d_a(−B_ii)(t_i−s_a).
- A negative Swan intersection forces the corresponding positive Swan
  coefficient to be divisible by p. Thus any nonzero Swan divisor has a
  coefficient at least p. The sufficient unramified exponent improves to
  p^(e+1)>T0, and the proved tame subclass requires t_i<p, instead of the
  initial t_i<1 condition.

None of these statements proves F13.5 or F13.6 in general. The latter asks
for a degree-linear tame fundamental-group generator bound on resolutions
of cyclic ramified covers of one fixed bounded p-power degree. The
reduction to that assertion, including unramified twists, cyclic
restriction, tame affine cocycles and Shapiro, is complete.

## Primary sources actually opened during this pass

1. Yuri Yatagawa, *Characteristic cycle of a rank one sheaf and ramification
   theory*, arXiv1712.09234v1, 26 December2017, 58 pages:
   https://arxiv.org/pdf/1712.09234 . Definition2.1 p8 and formula(2.5) p9
   give the weighted Witt filtration and explicit refined-Swan formula
   for complete DVRs. These are used in F13g. Proposition2.32 p28 gives
   vanishing of Rj_* on the ramified boundary for clean rank-one sheaves.
   Sections3–4 describe Kato's logarithmic characteristic cycle and its
   lifting. Those geometric statements are made for smooth finite-type
   surfaces; no complete-local extension of them has been assumed.
   Example3.3 p30 explicitly shows that zero logarithmic point
   multiplicity need not mean that ramification is clean.
2. Masao Oi, *On ramifications of Artin–Schreier extensions ... I*, JSIAM
   Letters6(2014),33–36:
   https://www.jstage.jst.go.jp/article/jsiaml/6/0/6_33/_pdf . The full
   primary PDF was downloaded and read. It explains the local Kato r_x
   algorithm and distinguishes r_x from a simpler r'_x. This does not
   itself supply a local Betti bound.
3. Masao Oi, *On ramifications ... III*, arXiv1507.00097v1,
   1 July2015,4 pages: https://arxiv.org/pdf/1507.00097 . Theorem5.1 p4
   bounds r_x in terms of the local Newton data of an order-p character.
   The printed setting is a smooth proper finite-type surface. No
   assertion about arbitrary p-power order or complete-local cohomology
   was inferred from it.
4. Yoshifumi Takeda, *Artin–Schreier coverings of algebraic surfaces*,
   J.Math.Soc.Japan41(1989),415–435, in the University of Osaka thesis
   scan: https://ir.library.osaka-u.ac.jp/repo/ouka/all/3328/09050_Dissertation.pdf .
   The introduction and Section1 distinguish covers of simple type;
   every degree-two cover in characteristic2 has that type, but covers
   of higher prime degree need not. Section2 begins with complete local
   calculations and treats characteristic2 with smooth reduced branch
   curve. It does not prove the general bounded-conductor estimate.
5. Kato1994, *Class field theory, D-modules, and ramification on
   higher-dimensional schemes I*, DOI10.2307/2375001: the full primary
   text was **not opened**. JSTOR returned empty metadata/HTML rather
   than the requested PDF. Its clean-resolution theorem is cited by
   Yatagawa, but that citation is not treated as having opened Kato's
   paper.

The exact local-file inventory, SHA256 digests and retrieval program are
code/fetch_cleanup_sources.py and output/cleanup_sources.json. Source PDFs
and their text extractions remain external-source working material and
are excluded from the deliverable ZIP by the main checkpoint policy.

## Routes still under investigation, not proofs

**Quantitative clean resolution.** F13e controls the zero divisor of the
initial refined-Swan sections. It does not control the number of later
blowups or the cohomology of exceptional curves created above those
zeros. The local Kato invariant r_x counts weighted conductor drops,
not simply the number of blowups. Some blowups have weight zero. Thus
a bound for r_x must not be silently substituted for a resolution-size
bound.

**Characteristic-cycle route.** For a finite-type smooth surface, the
point-supported perverse kernel of j!→Rj_* can be bounded by the point
multiplicity of the effective characteristic cycle. Yatagawa expresses
that cycle through ramification data. One would need a precise version
over the complete-local formal neighborhoods, or a comparison uniform in
the covers and their ranks. The present work has neither supplied that
comparison nor used the finite-type result outside its scope.

**Finite-jet route.** A bounded-order Artin–Schreier–Witt cover with
bounded poles has a derivative in its torsor coordinate supported on a
fixed boundary monomial. High normal-order coefficients should be
removable by a henselian argument; tangential formal coefficients and
the uniformity of the finite-jet bound are separate issues. Approximating
one cover by an algebraic cover does not establish a common geometric
bound for all covers. No such uniform finite-determinacy claim is made.

**Characteristic2 prototype.** A normal degree-two cover of a regular
surface is locally a hypersurface z²+a z+b=0. Its Jacobian contains a,
and a is supported on a bounded multiple of the boundary. This suggests
bounding the Jacobian scheme through boundary differential sections,
then bounding exceptional-curve cohomology by vanishing cycles. The
required global length estimate and the exact local comparison remain
unproved. For larger p, Takeda's Example1.5 shows why one cannot simply
assume all normalized cyclic covers have the same hypersurface form.

No excluded construction, source search, packaging work or new subclass
corollary is being counted separately as a formal-review movement.

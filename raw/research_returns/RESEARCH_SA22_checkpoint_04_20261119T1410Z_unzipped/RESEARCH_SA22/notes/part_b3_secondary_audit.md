# Independent B.3 audit

Date: 2026-11-19. Auditor: GPT-6 Astra, OpenAI, ChatGPT Pro mode, `part_c_algebra` agent.
The B researcher owns and edited `sections/part_b.tex`; this audit sent corrections before any change and did not make competing edits.

## Coverage and exact manuscript input

I read every B.3 theorem/proof block, from subject 21 through the final SGA2 block, and compared the numbered headings with `inputs/RESEARCH_SA22_transcriptions/transcriptions/H66-01_transcription.tex` (relative to the workspace root). The input has subjects 1–11 at lines 21–47, 12–19 at lines 52–76, 20–22 at lines 82–87, the Pour mémoire diagram at lines 90–116, subject 23 at line 120, subject 24 at lines 122–124, and subjects 25–28 at lines 137–145. No part of the unrelated cote-68 game transcription was used for this comparison.

The two errors found below were sent to the B researcher, who applied the corrections and updated the primary notes/results/events. Current theorem labels remain stable even if later assembly changes line numbers.

## Corrections found and checked after application

### Analytic duality: Hausdorffness has a one-degree shift

- Affected statement: `thm:B3-analytic-duality`; current `sections/part_b.tex` lines 930–940.
- Original incorrect sentence: either member of the displayed dual pair is Hausdorff if and only if the other is.
- Correct statement:
  \[
  H^q(X,F)\text{ Hausdorff}\iff \operatorname{Ext}^{1-q}_c(F,K_X)\text{ Hausdorff},
  \qquad
  H_c^q(X,F)\text{ Hausdorff}\iff \operatorname{Ext}^{1-q}(F,K_X)\text{ Hausdorff}.
  \]
  The perfect pairings on separated quotients still pair degree \(q\) with degree \(-q\).
- Primary verification: Ramis–Ruget, Theorem 1, printed p.81, and Theorem 2, printed pp.82–83. Both source pages were rendered and visually read; the superscripts are unambiguously \(1-p\), not \(-p\). Images: `qa/ramis_ruget_p81_review.png`, `qa/ramis_ruget_p83_review.png` (PDF pages 6 and 8, counting from one).
- Mathematical cross-check: closedness of the image of a differential is equivalent to closedness of the image of its transpose; that transposed differential controls the adjacent dual cohomology degree. This independently explains the source's shift.
- Resolution: corrected by the B researcher; re-read in the current fragment.

### Characteristic cycles: curve-fibre sign and exact sublemma

- Affected statement: `thm:B3-index`; current fragment starts at line 1245, source locator at line 1262.
- With the stated convention \(CC(F)=(-1)^d\operatorname{rank}(F)[T_X^*X]\) for a local system, the curve formula is
  \[
  CC(F)=-\left(\operatorname{rank}(F)[T_X^*X]+
  \sum_x a_x(F)[T_x^*X]\right).
  \]
  Thus the additional fibre coefficients are **negative** Artin conductors.
- Primary verification: `sources/saito_charcycle.txt`, Lemma 4.11(1),(3), equations (4.16),(4.18),(4.19), printed p.46. Part (2) is étale pullback, so the former locator “(1)–(2)” was also incorrect. The index formula itself is Theorem 6.13, equation (6.22), printed p.64.
- Resolution: sign and locator corrected by the B researcher; re-read in the current fragment.

## Direct independent source matches

| Statement(s) | Source text independently read | Finding |
|---|---|---|
| B.3.1, B.3.8 crystalline comparison | Stacks 07MW, 07JH; opened refs `turn358918442view0`, `turn358918442view2` | The smooth lift, divided powers and nilpotent prime hypotheses match. The value on the lift and de Rham comparison are typed correctly. The converse retains topological quasi-nilpotence. |
| B.3.2 finite flat local/global duality | Milne ADT III, Theorem 6.10, p.277, and Theorem 8.2, p.290, in `sources/milne_adt.txt` | Local degrees sum to 2 and global compact-support degrees sum to 3. Local topologies and the discrete global cohomology convention are necessary and retained. \(K/K^p\) verifies why finite-group language would be false for the local infinitesimal example. |
| B.3.2–3 abelian p-primary duality | Suzuki local paper Theorems A–C pp.3–4; global paper Theorem A p.3, in `sources/suzuki2014.txt`, `sources/suzuki2018.txt` | Local SD shift \([1]\) and the SDSD term match. The global triangle is unshifted in its middle arrow and retains \(V[-1]\to D^{SDSD}\to C^{SD}\to V\). The perfect-field and sheaf-valued-site hypotheses are retained. |
| B.3.7 arithmetic duality | Geisser Theorem 7.8 and its proof, pp.30–31, `sources/geisser_duality.txt` | \(\mathbb Z\)-dual shift \([-1]\), Ext degree \(2-i\), and modified real-place compact support match. The proof's \(\mathbb Q/\mathbb Z\)-dual shift is \([-2]\). |
| B.3.8 differential modules | Narváez Macarro Theorem 3.1.1, p.67, and the unshifted DR/Sol definitions, `sources/narvaez2004.txt` | \(DR(M)=RHom_D(O,M)\) and \(DR(M)[d]=D_X(Sol(M)[d])\) have the correct shifts. Holonomicity, not regular holonomicity, suffices for this local duality theorem. |
| B.3.11–12 Néron scope | BLR §1.3 Theorem 1 and Corollary 2, p.16, `sources/blr_neron1990.txt` | Arbitrary DVR, smooth finite-type generic group, and boundedness of strict-henselian points match. The finite-type convention is essential and is distinguished from the locally-finite-type multiplicative model. |
| B.3.18 Artinian quotient | Stacks Proposition 39.23.9, tag 03BM; opened ref `turn358918442view1` | Both projections must be finite locally free and the map into \(U\times U\) an equivalence relation. The affine invariant ring represents the fppf quotient; finite faithful flatness and \(R=U\times_MU\) match. Artinianity descends by faithful flatness of ideal chains. The nonfree-action caveat is correct. |
| B.3.23 Chow pullback | Weber Def.4.1.12, Lemma4.1.13, Thm4.2.1, Cor.4.2.3 pp.29–39, `sources/weber2015.txt` | The orientation is a **rational bivariant class**, uniquely specified by its value on the target's fundamental class. The relative grading is correct. Finite type and separatedness over \(\mathbb Z\) are retained; no integral generalization is asserted. |
| B.3.26 relative Rosenlicht | Contou-Carrère1979 §0 hypotheses and Theorem1.4 pp.203–204, `sources/contou_carrere1979.txt` | The relative-curve hypotheses, arbitrary base, all degree components and pro-smooth inverse limit match. The universal property does not require a chosen section of the open curve. |
| PM resolution | Temkin Theorem1.2.1; ILO introduction Theorem3(1) | Functorial characteristic-zero resolution is stated for generically reduced noetherian quasi-excellent schemes. Arbitrary-characteristic replacement is an alteration, not a birational resolution. |
| PM regular base change | ILO XIV Lemma2.5.3 pp.216–217 | qcqs \(f\), regular \(g\) between noetherian schemes, arbitrary étale \(\mathbb Z/n\)-sheaf and invertible \(n\) match exactly. No finite-type hypothesis on \(g\) is needed. |
| PM potential duality | ILO XVII Theorems5.1.1 and6.1.1 pp.287,293–294 | Even without finite Krull dimension, bounded constructibility and finite Tor dimension of the normalized potential complex are explicitly in the source. Finite quasi-injective dimension is equivalent to finite Krull dimension. No false global finite-dimensionality assumption is hidden. |
| PM finite-type finiteness | ILO XIII Theorem1.1.1 and1.1.2 p.195 | Constructibility **and** eventual vanishing hold for finite-type maps over noetherian quasi-excellent bases, with invertible torsion; properness and finite Krull dimension are not hypotheses. |
| PM affine dimension | ILO XV Theorem1.1.2 and Cor.1.2.2 p.219 | The support/dimension-function inequality matches, and specialization to a point gives the affine \(d\)-dimensional bound. It is not an arbitrary fibre-dimension bound. |
| PM rigid geometry | Bosch §8.4 Theorem3 p.204, `sources/bosch_rigid2014.txt` | Formal side is quasi-paracompact admissible formal schemes, localized at admissible blowups; rigid side also has quasi-separatedness. The source explicitly explains automatic quasi-separatedness on the formal side. |

## Proof and counterexample checks

- **Specialization, subject16:** the direction is geometric generic to geometric special, and the surjection becomes an isomorphism only on the maximal prime-to-\(p\) quotient in residue characteristic \(p\). For \(\lambda=2+t\) in characteristic3, the Legendre discriminant is a unit and the Cartier coefficient is \(-t\); the special and geometric generic p-ranks are 0 and1. The resulting \(H^1(-,\mathbf F_3)\) dimensions distinguish the full fundamental groups. This is a fully specified counterexample, correctly not identified with Artin's unnamed marginal example.
- **Subject3:** the characteristic7 cubics are smooth; \([x^6](x^3+ax+b)^3=3b\) gives the two Cartier ranks. The covers have the same local permutation-representation **types and multiplicities**, not the same labelled branch divisor. The text retains that distinction. The Artin–Schreier cokernels are zero over the algebraically closed field, so the Euler values 1 and0 follow.
- **Program:** `code/part_c_b3_audit.py` was actually executed successfully. Its independent exact output is `code/part_c_b3_audit_output.json`. It verifies the symbolic characteristic7 coefficient, the two nonzero discriminants, and the characteristic3 coefficient/discriminant. Its scope is the finite arithmetic hypotheses; it does not claim to compute étale cohomology.
- **PM SGA2 counterexample:** checked all four annihilator identities for \(e_n=x^n/(uv^{n+1})\), the toric embedding \((u,v,x,y)=(ac,ad,bd,bc)\), the Laurent exponent \((-n-2,n,-1,-1)\), and the exclusion from \(R_u+R_v\). The infinite independent socle proves the stated failure of finiteness. Complete-intersection parafactoriality is used only in its stated dimension and the factoriality deduction is compatible with localization.
- **Subject6 holomorphic Lefschetz:** checked the Dolbeault numerator \(\det(1-\overline{df})\) and the real denominator \(|\det(1-df)|^2\); cancellation gives the stated complex denominator. Isolatedness and compactness give a finite fixed-point sum.
- **Subject14 points:** the complete atomless Boolean algebra argument proves absence of any frame point, rather than only absence of a conservative family. Its sheaf topos is nondegenerate.
- **Subject15:** the internal Hurewicz statement, the object \(B\alpha_p\), and the external profinite-shape comparison are distinguished. The Artin–Schreier/Frobenius exact sequence gives the explicit nonzero infinitesimal torsor; reduced étale test schemes kill the restricted \(\alpha_p\) sheaf. The Postnikov comparison is a proof of the profinite statement, not an uncompleted comparison.
- **Subject20:** the positive-characteristic vanishing implies the characteristic-zero formulation by proper semicontinuity on the integral Schubert model after restricting to a flat open. No arbitrary-line-bundle or noncomplete-homogeneous-space vanishing is claimed.
- **Other blocks:** read for consistency of categories, coefficients and deductions, but this audit does not independently certify every page of every cited long source. In particular the primary B researcher remains responsible for the source verification of the Picard criterion, full six-functor motivic formalism, approximation, positivity cones, and representability criterion.

## Scope that must remain explicit in the final report

The prompt permits B.3 to identify the strongest proved statement with its locator. It does not license relabelling every broad 1964 programme as solved in all possible senses. The current fragment correctly retains the following limitations:

- “Schémas morcelés” is not defined in the four sheets; the Néron theorem addresses the named functor, not an invented identification of that category.
- The motive construction is rational and triangulated. It does not supply an abelian category of mixed motives or a motivic t-structure.
- The operator-valued Euler formula is prime-to-characteristic. The p-primary discussion includes the obstruction to a formula depending only on local types and the separate abelian duality theorem.
- The Artinian theorem concerns finite locally free equivalence relations, not nonfree groupoids with stabilizers.
- Subject23 retains rational coefficients and the arithmetic finite-type scope; no integral pullback for every regular base is inferred.
- The SGA2 heading receives a complete counterexample to one proposed finiteness statement and a precise positive local-Lefschetz theorem. It is not a declaration that all questions in SGA2 have been settled.
- Original Gabber1994/Fujiwara1995 text access remains distinct from the modern opened proofs; see the separate retrieval audit.

After the two applied corrections, this audit found no further definite mathematical error in the reviewed B.3 fragment.

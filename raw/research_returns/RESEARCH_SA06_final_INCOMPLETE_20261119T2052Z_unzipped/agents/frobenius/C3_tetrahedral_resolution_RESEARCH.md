# Explicit tetrahedral resolution: geometry certificate and remaining gate

Written 19 November 2026 by GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06, `/root/frobenius`; inherited effort setting not separately exposed. This is unregistered research geometry. It is not a claimed Chow counterexample, a negative-K nonvanishing result, or main-gate movement.

## Exact construction

The complete first-person proof is `C3_tetrahedral_resolution.tex`, equations TG.1–TG.5. We take the local hypersurface

$$x_0x_1x_2x_3-G_5(x)=0$$

at the origin. For p different from 5, the polynomial is the Fermat sum of fifth powers. At p=5 it is

$$G_5=\sum_i x_i^5+\sum_{i<j}x_i^4x_j.$$

All coordinate plane sections are smooth, all six coordinate edges have five distinct nonvertex zeros, and the four vertices have nonzero value. The characteristic-five assertions are proved directly from the derivatives, without a genericity hypothesis. The Euler identity then proves that the affine hypersurface is smooth off the origin. Its local hypersurface ring is a normal domain.

The first blowup has exactly thirty ordinary edge nodes. Blowing up the four exceptional components in the fixed order 0,1,2,3 resolves them projectively. The two actual Rees charts at a node uv=tw are t=ua,v=aw and u=tb,w=bv. These show regularity, smallness, the chosen plane's point blowup, the unchanged other plane, and the reduced SNC closed fibre. Later centres are Cartier at the already resolved points. The final components are plane blowups at 15,10,5,0 points; there are six projective-line double curves and four triple points. The dual complex is S2.

The full exceptional fibre E is Cartier and satisfies mO_Z=O_Z(−E). Its conormal restricts on each component to the pullback of O_P2(1). This is nef and is **not ample**: it has degree zero on all thirty small exceptional curves. A different positive integral combination D of the four components has −D relatively ample, by recursively combining the relatively ample tautological line at each blowup with a sufficiently high power from the previous stage. The proof does not substitute D's conormal for E's conormal.

The construction commutes with localization and strict henselization. It is unchanged over the puncture.

## Primary sources freshly opened and read

The Rees charts are calculated in full in the proof. We also freshly opened and read the following complete Stacks statements/proofs:

- Lemma31.33.2, Tag0804, affine blowup algebras: <https://stacks.math.columbia.edu/tag/0804>.
- Lemma31.33.3, Tag0805, flat base change: <https://stacks.math.columbia.edu/tag/0805>.
- Lemma31.33.4, Tag02OS, effective Cartier pullback and the tautological line: <https://stacks.math.columbia.edu/tag/02OS>.
- Lemma31.33.7, Tag0807, the identity for a Cartier centre: <https://stacks.math.columbia.edu/tag/0807>.
- Lemma31.33.13, Tag02NS, projectivity and relative ampleness for a finite-type blowup ideal: <https://stacks.math.columbia.edu/tag/02NS>.
- Lemma29.38.8, Tag0C4K, relative ampleness under composition, together with the complete proof of preceding Lemma29.38.7: <https://stacks.math.columbia.edu/tag/0C4K> and <https://stacks.math.columbia.edu/tag/01VG>.

Exact fresh retrievals: `turn751594657view0`–`view3`, `turn120411441view0`–`view1`, and `turn884870426view0`–`view3`. Existing canonical bibliography keys `rootStacksBlowup` and `frC3beStacksCompositeAmple` are reused, with the additional precise locators given explicitly in the proof and this ledger. No small-resolution classification theorem is needed.

## Finite certificate

Program: `code/check_tetrahedral_resolution.py`.

Output: `output/tetrahedral_resolution_certificate.json` and `.out`.

The completed run started at 16:04:19.720278 UTC and finished at 16:04:19.817451 UTC, taking 0.097176904 seconds. All 36 checks passed. They comprise twelve characteristic-five projective-face affine charts whose singularity ideals have Groebner basis [1], six edge squarefreeness checks, four vertex values, seven selected Fermat edge primes, the integer Euler identity, the two node-chart equations and overlap identities, and the ordered node-assignment/tetrahedral incidence counts. The all-prime assertion is proved algebraically in the text, not inferred from the seven primes. The program does not test a Chow or K-theory conclusion.

An initial invocation stopped before any calculation because of a Python `subs(w:b*v)` syntax typo. It was immediately corrected to `subs(w,b*v)`. The successful certificate above is the first executed mathematical calculation; no failed mathematical check was suppressed.

## Standalone build

Program: `code/build_tetrahedral_auxiliary.py`. It builds the geometry together with the separate exact fixed-family negative-K auxiliary, using only their five cited canonical bibliography entries. The final build completed at 16:05:20.670446 UTC, took 5.804138609 seconds, and produced a four-page PDF of 156,883 bytes. All five return codes are zero, with no warnings, undefined citations, overfull boxes, or underfull boxes in the final log.

Artifacts: `output/C3_tetrahedral_auxiliary_check.pdf`, `output/tetrahedral_auxiliary_build.json`, and `.out`. The preceding build's source-extraction regular expression omitted a multiline KST citation; its log/JSON are retained under `initial_tetrahedral_auxiliary_build.*`. The expression was corrected to allow whitespace before the citation key and the clean build rerun. This was a wrapper bibliography extraction issue, not a change in either proof.

## Unresolved mathematical step

The exact fixed-product cokernel lemma FF.1 identifies the obstruction after inverting p with K−1(SpecR×P). A prospective dual-complex coefficient kappa multiplied by a proper-curve K2 class xi has connecting image xi times the boundary of kappa. Neither product faithfulness nor product vanishing has been established. The existence of the regular projective resolution removes the geometry hypothesis from that investigation; it does not settle the actual coefficient or family lift. The rational ordinary top quotient remains a gate.

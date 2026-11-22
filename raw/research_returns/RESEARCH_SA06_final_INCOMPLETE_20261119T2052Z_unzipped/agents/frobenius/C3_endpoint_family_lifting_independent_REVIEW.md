# Independent audit of the fixed-curve endpoint lifting theorem

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro, run RESEARCH_SA06, agent `/root/frobenius`; inherited reasoning effort not separately exposed.

Date: 19 November 2026. Full typed proof read after the 16:47:19 UTC tool-clock reading; mathematical verdict sent before the 16:48:42 UTC tool-clock reading. The exact primary Weibel pages were freshly reopened and read immediately afterwards. Earlier message estimates “16:47–49” were approximate prose times, not independent clock measurements.

Reviewed file: `../real_weil/C3_endpoint_family_lifting_draft.tex`, all four proof steps, equations EL.1–EL.5, and the complete tetrahedral application. This is an independent proof audit, not a program rerun or an assertion that the combined draft has already been registered.

## Verdict and exact scope

**PASS on the complete mathematical argument.** The only clarification requested was to say explicitly that the class to which gamma squared is applied has rank zero: the negative-degree class kappa pulls back to zero at every field-valued point, and nilpotent invariance preserves rank. An integral representative of a rational rank-zero class has integer rank zero.

The theorem concerns two endpoint restrictions of an actual perfect family on a fixed product. It does **not** assert that the initially prescribed class on the whole exceptional product lifts. In particular it does not prove that the fixed-product negative-K obstruction FF.1 vanishes. This distinction is retained in the proof and is essential.

The conclusion is conditional on the stated geometry: a regular projective threefold over an excellent henselian algebraizable local ring in positive characteristic, a simple normal crossing exceptional divisor, and a positive exceptional Cartier divisor with ample conormal. It is not a theorem about every isolated threefold singularity or every formal perfect complex. The tetrahedral conclusion uses the separately audited FF, TG, TS and TC computations.

## 1. Perfect gamma classes and generation

The projective schemes D, E and D times P have the resolution property. Perfect K0 can therefore be represented by vector bundles. The gamma filtration, its special lambda-ring identities, and its pullback functoriality are used on these singular schemes, without replacing perfect K0 by coherent G0 or ordinary Chow groups.

For a vector bundle V and a high power L^m, a generating map to V dual tensor L^m dualizes and twists to

`0 -> V -> (L^m)^N -> Q tensor L^m -> 0`,

where Q is globally generated. Thus a rank-zero virtual bundle is a difference A minus B of bundles of equal rank with arbitrarily adequate global and first-jet generation. Tensoring a globally generated bundle with a first-jet-generated line bundle generates its first jets: use the values of generating bundle sections and the first jets of the line sections. Adding a common positive summand preserves the difference and permits rank at least two and positive determinants.

The gamma identity in the draft follows from gamma_t(x-y)=gamma_t(x)/gamma_t(y). Modulo filtration three, replace each rank-zero bundle class by its determinant difference. This gives exactly the displayed cross term with a minus sign and the square of the B determinant difference. General products in filtration two reduce to products of line differences; writing a line as the quotient of two sufficiently positive lines works modulo filtration two. These manipulations retain possible Cartan-kernel classes.

For a general matrix of n minus one sections of a rank-n bundle, the deeper rank-drop stratum has codimension six and misses the three-dimensional scheme. Near rank n minus two, an invertible minor reduces the residual matrix to one two-entry column. The two entries form a regular sequence under the stated transversality conditions. The exact determinantal/Koszul sequence gives

`[O_C] = 1 - [A tensor det(A)^(-1)] + (n-1)[det(A)^(-1)]`.

In line roots its quadratic term is gamma squared of A minus n. Thus the congruence is in perfect K0, not merely in the cycle group. Complete intersections similarly represent products of positive line differences. The finite rational combination therefore represents beta modulo filtration three.

## 2. Characteristic-free incidence and the actual regular hypersurface

On a smooth stratum of dimension d at least two, the first rank-drop condition has codimension two. Conditional on this, failure of surjectivity of the normal derivative has codimension d minus one. Hence the total bad-jet codimension is d plus one. On strata of dimension below two the rank-drop locus is simply avoided. First-jet generation makes this an ordinary finite-dimensional incidence calculation; no generic-smoothness theorem in inseparable characteristic is imported.

There are finitely many reduced SNC strata and two selected fibres. The choices can simultaneously yield a curve on each component, finitely many transverse intersections on double strata, avoidance of triple strata, and finite codimension-two lci schemes in the two endpoint surfaces. The curve remains an lci in the nonreduced Cartier divisor D: D is Cohen–Macaulay, and the two equations have the required height and are nonzerodivisors in succession. Endpoint choices in fact avoid the lower-dimensional intersection strata there.

For a sufficiently high ample twist, the ideal of C and its conormal quotient have the needed generated sections. A general section of the rank-two conormal bundle on the one-dimensional scheme C has no zero on its reduction. Thus the hypersurface H contains C as an effective Cartier divisor. At C the selected linear combination of the two local equations has nonzero ambient differential. Away from C, ordinary stratumwise first-jet Bertini supplies this differential. This covers the possible double and triple strata without assuming that D itself is regular.

The extra requirement that H contain no entire component surface in any parameter fibre is valid: for a high twist, vanishing identically on a specified surface imposes at least two independent linear conditions, whereas the parameter varies in dimension one. The fixed curve cannot contain a whole surface fibre. Thus the union of these bad conditions is proper. Fibrewise Cartier criteria give flatness over P and fibres of dimension one, allowing their given nilpotent multiplicities.

The high line bundle is chosen on the actual Z times P. Relative Serre vanishing lifts the equation on D times P to that actual product. Its zero divisor W is regular along the closed fibre by the ambient differential condition. Excellence makes the nonregular locus closed, and properness over the local base forces the image of any nonempty such closed locus to contain the closed point. Consequently W is regular everywhere. The same argument and fibrewise nonzerodivisor criterion justify W's flatness over P. This is an actual fixed hypersurface, not a varying etale neighbourhood depending on the curve parameter.

## 3. The whole line bundle lifts after one finite power

Let J be the Cartier ideal of H in W. Its restriction L to H is relatively ample over the proper curve P, because the exceptional conormal was ample on D. Relative Serre gives the eventual vanishing of positive direct images of L^n. Since the base is a curve, Leray gives H2(H,L^n)=0 for all sufficiently large n. No H1 vanishing is needed or asserted.

The line-bundle obstruction between successive Cartier thickenings lies in H2(H,L^n). Each such group is killed by p. At each of finitely many early stages, taking one pth power kills the obstruction and permits a lift, while replacing all earlier choices by the same power preserves compatibility. After the vanishing range begins, the exponent no longer increases. This is an actual compatible system of one line bundle; it is not an inference from stabilization of abstract K0 groups.

The exceptional ideal and the maximal-ideal extension have the same support and cofinal powers. Proper Grothendieck existence over the completed base produces an actual formal algebraization. Applying it also to the inverse and using full faithfulness proves the algebraized object is invertible. Popescu descends that bundle to one smooth algebra. Crucially the smooth algebra is then lifted from its specified R modulo m^M point, not just from a residue-field point. Taking m^M contained in J ensures that this preserves the entire bundle on H, with its whole proper curve parameter. The henselian smooth lifting statement applies to the pair (R,m^M).

## 4. Exact endpoints and the tetrahedral application

The negative Cartier line Q0=O_H(-C) is the correct choice. Its Cartier sequence gives i_*(1-Q0)=[O_C] exactly. After the finite p-power lift, regular Cartier pushforward gives an actual perfect family on Z times P.

At either selected endpoint all required intersections are Tor independent by the earlier flatness and regular-sequence conditions. The endpoint C_u is finite artinian. Every invertible sheaf on it is trivial. The geometric series therefore proves

`i_*(1-Q0,u^m) = sum_j [O_Cu tensor Q0,u^j] = m[O_Cu]`

exactly in perfect K0(D). This avoids any theorem asserting compatibility of singular pushforward with the gamma filtration. Dividing by the finite power and adding the finite list of generators gives the endpoint equality. The omitted filtration-three part vanishes on E by its dimension two and the singular quasi-projective gamma dimension theorem.

For the tetrahedral application, nilpotent invariance lifts the given exceptional-product coefficient to D times P rationally. Its two endpoint classes are square-zero and have Adams weight two. For an integral rank-zero multiple y, the universal identity `gamma2(y)=(y^2+2y-psi2(y))/2` implies gamma2(y_u)=-y_u. Applying the endpoint theorem to minus gamma2(y) divided by the clearing integer works without any global weight decomposition of K2(P).

FF.4 then identifies the endpoint lifts with the unique weight-two classes on Z. Taking the second Chern-character component on finite-type smooth models yields a cycle on the fixed product whose endpoint difference is ordinarily algebraically trivial. This is the required equivalence convention.

The retained proper-curve symbol lemma works in every positive characteristic. On the normalization of a component through (a,b) of `(f-1)^2(g-1)^2 = c f g`, no component is vertical or horizontal. A point over f=0 has g=1 and f=u(g-1)^2 for a unit u. The symbol satisfies `{f,g}={u,g}+2{g-1,g}={u,g}` because `{g-1,g}={-1,g}` and twice this is zero, including characteristic two. Its specialization is zero there and {a,b} at the chosen point. The unramified section lifts to global Quillen K2 on the smooth proper curve by the dimension-one descent edge. Symbols with an entry one vanish and cause no exceptional case. Thus the tetrahedral coefficient relations are supplied by actual proper parameters, and the stated B2 rational conclusion follows from TC.

## Fresh primary source audit and reused inputs

Freshly opened the complete 106-page author-hosted Chapter II of Charles Weibel's *The K-book*: https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf . Read Splitting Principle 8.8.1, Corollary 8.8.2, Proposition 8.8.4 and Remark 8.8.5 on chapter p.83, and Proposition 4.9 / Theorem 4.10 context on pp.32–33. Retrieval references: turn232827250view0, turn670715747view0–2. The noetherian quasi-projective dimension theorem in Remark 8.8.5 does not assume nonsingularity. The following paragraph introduces nonsingularity only for the separate Chow discussion. The draft's exact source scope is therefore correct.

The original SGA6 VI.6.6 was **not** opened in this audit; Weibel's explicit statement and citation are the source actually read. Use the owner's chapter-specific key `D_Weibel2013KbookII`, not the earlier Chapter III or IV keys.

The square-zero Picard obstruction, relative Serre, projective existence, regular completion, Popescu, finite-presentation bundle descent and henselian smooth lifting inputs are the exact Stacks statements already opened and fully audited in C.3az and the subsequent PB proof. This audit rechecked their hypotheses in the new geometry but does not claim a second fresh opening of all those pages. FF/TG/TS/TC had already received complete independent proof audits. No numerical computation, certificate rerun, or original-literature priority claim is made here.

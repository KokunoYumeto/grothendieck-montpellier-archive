# Independent full proof and final-text review — F59 all-rank scalar closure

Reviewer: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting not exposed. Date: 2026-11-21 UTC, completed shortly after 05:00 UTC.

Verdict: **PASS, with no mathematical correction required.**

## 1. Exact frozen scope

I read the entire report and the entire generated fragment directly from disk, and independently reconstructed every proof step. I also read the full all-variable module dependency and the complete new bibliography fragment.

- agent_soergel_allrank_scalar_closure.md: SHA256 475bd56d0486831328193453faec89612ea1c97a8bb81786d12970053eb34f27.
- finding_F59_allrank_scalar.tex: SHA256 956b51070bd4cfc30b208512912bf0501d2da8d38a43ec94c65bbd56bd763b77.
- finding_F59_allrank_bib.tex: SHA256 49f61afe0214ec14d4b7e666f943e04a6c64674373277aa6bf68a254ef416e17.
- Full module dependency agent_soergel_top_module_all_variables.md: SHA256 b5a655cbc1748433c10cb29912d07f4af929ed60c03b52314f97cec739925de1, as checked against the supplied report metadata and its full text.

This is an independent mathematical proof review and a direct report-to-fragment match. It is not a formal proof-assistant verification, a numerical experiment, or merely a review of the author's summary. I did not edit any target or master file.

## 2. Fresh primary-source verification

I independently reopened the original Lichtenbaum article's author-uploaded full text at https://www.researchgate.net/publication/247050802_On_the_vanishing_of_Tor_in_regular_local_rings. The fresh retrieval is turn988929871view0. I read Theorem2, all four clauses and the surrounding proof context, also using the locally saved original-text extraction. The statement requires a complete unramified regular local ring and finite modules. Its torsion-free chi-one equality clause and positive-Tor rigidity are exactly the ones used here. The extraction loses some subscripts, so I separately checked the precise field case in the following author notes. I do not claim an original-article visual PDF audit.

I independently reopened Hochster's original Math615 Winter2012 PDF at https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/10/615W12.pdf. Fresh references turn988929871view1 and turn853657893view0 contain the printed-p169 corollary, its hypotheses, and full proof reduction to Koszul homology. In the field case, the truncated Tor Euler characteristic is nonnegative and vanishes exactly with all subsequent Tor groups. This confirms the indices needed here; the argument uses no ramified variant or inaccessible later theorem. A screenshot was requested, but the source verification recorded here is the actually read PDF text and theorem/proof context, not a claim of a successful visual audit.

I independently reopened and read Stacks tags00MB and00MC at https://stacks.math.columbia.edu/tag/00MB and https://stacks.math.columbia.edu/tag/00MC, fresh references turn988929871view2 and turn988929871view3. The flatness and local faithful-flatness hypotheses match the application. Only the needed flatness is used to preserve the torsion-free embedding and the finite resolution.

I reread the original local Elias--Williamson Localized Calculus PDF text, Sections1.1--1.2, including the faithful-action qualification for actual graph bimodules, equations1.1--1.2, Theorem1.6 and Remark1.7. The ordinary characteristic-zero type-A realizations in the report are faithful, so the distinct graph labels and monoidal multiplication used in the proof are valid. No claim in the report relies on a degenerate nonfaithful realization.

The new bibliography accurately identifies these sources and does not claim a nonexistent local PDF or original-article visual check.

## 3. The all-variable tensor-dimension lemma

I reconstructed the complete argument rather than treating the known theorem as the whole proof.

For a torsion-free module, the minimal graded resolution is finite because the finite Koszul resolution of the residue field kills Tor above the number of variables; minimality then kills the corresponding free terms. Localization computes its alternating free rank. The finite grading of V makes the homogeneous maximal ideal nilpotent, so every tensor term and Tor group has finite dimension. The displayed chi-one formula has the correct alternating sign.

A finite torsion-free module embeds in a finite free module by clearing denominators after a fraction-field basis choice. Localizing and completing preserves that injection. The completed ring is the required equicharacteristic complete regular local domain, the completed quotient remains torsion-free, and all Tor lengths agree with k-dimensions because V is supported at the origin and the residue field is unchanged. The local theorem therefore applies with every hypothesis checked.

The equality argument uses more than Euler-zero: it first obtains vanishing of Tor1 and then of every positive Tor. If a minimal resolution had a final positive term, the nonzero socle of V in each final generator would survive as nonzero top Tor. This is a valid contradiction and proves graded freeness.

For an arbitrary module, the torsion-free quotient has the same rank. Nonfreeness of that quotient gives strictness through the tensor surjection. If the quotient is free, its homogeneous basis lifts to a one-sided graded splitting; nonzero torsion then survives after taking both origin quotients. This covers rank-zero and zero-quotient cases correctly. No projective-dimension-one claim is made in higher dimension.

## 4. Generic probability measure and the actual global top

I checked the passage from the actual ambient Euler class to F(-1)=2(e+tau): forgetting internal grading sends the ordinary simple generator to e+s, and its shifted complement to s-e. Their two-factor sum is 2(e+tau). The scalar Euler dimension is four.

Augmentation of F squared equals dF gives total dimension d because the Laurent ring is a domain and the nonzero character has positive coefficients. For each positive real parameter the normalized support is fixed, closed under multiplication and therefore a subgroup of the finite group. At a maximal coefficient the convolution equality is a weighted-average equality, forcing uniformity throughout the subgroup. The nonzero Euler value then identifies the subgroup exactly as {e,tau}. Thus every global cohomology rank equals the corresponding scalar cohomology dimension. This uses only the ungraded generic graph category; it does not retain an invalid internal grading through the fraction field.

The nonzero tensor-square assertion is also valid for a torsion bimodule: take the nonzero finite left-origin quotient, then quotient its positive-degree right action and the second factor's left action. Their tensor over k is nonzero. Hence the highest global cohomology cannot disappear from the top tensor square. Comparing the actual and generic top degrees correctly forces a=b=c and a positive top rank. The top-truncation identity is an ordinary derived-tensor top-degree identity; negative Tor terms cannot contribute above it. The module lemma then proves actual left freeness at the top.

## 5. Global graph splitting and AR9

For a left-free module with the two generic graph types, the polynomial matrix identities yU=xV and U squared=x squared extend globally by torsion-freeness. Coprimality gives U=xZ,V=yZ, and then Z squared=I. The spectator coordinates act by their left scalars. Characteristic zero permits the two idempotents, whose images are actual graded projective graph modules. The homogeneous residue-basis argument makes them graded free; it also makes the two graph summands right-free. This argument never specializes spectator coordinates.

I checked the potentially delicate canonical map AR9 in detail. Forgetting the left action allows higher projective cohomology to split from the bounded right-projective complex. Acyclic top tails can be cancelled because the terminal projective surjections split; the remaining projective cohomology likewise splits. Tensoring those one-sided summands with the second complex gives their exact cohomology tensors. The remainder lies in degrees at most s, so its degree a+s tensor cohomology is exactly M_s tensor M_a. These are all terms of the displayed cross-product map.

The choices used to show bijectivity are one-sided, but the map being tested is the intrinsic cycle cross-product, already bimodule-linear. Therefore bijectivity proves a bimodule isomorphism without asserting bimodule formality or choosing bimodule splittings. This distinction is correctly maintained in both report and fragment.

## 6. AR10 and the full descent

For s<a, the two exceptional summands on the left are M_a tensor M_s and M_s tensor M_a. Each has origin-fiber dimension r times phi(M_s): the higher module is an actual shifted graph sum and its graph automorphisms fix the homogeneous origin. Every other pair has both indices greater than s and is graph-free, giving precisely the stated S_s.

On the scalar side, the exceptional terms have dimensions r times phi(M_s) and r times c_s. The remainder is the same S_s by the already established rank identity. This gives phi(M_s)=c_s=rank(M_s), with no hidden flatness assumption on M_s.

If this rank is zero, graded Nakayama kills M_s. Otherwise its minimal graded free surjection has exactly that rank; its kernel is a rank-zero submodule of a free module over the polynomial domain and hence is zero. Graph splitting then provides right freeness. The descending induction therefore closes all global cohomology degrees in the actual ambient ring.

## 7. Restored full grading and exact final scope

Only after this descent does the proof recover the full internal grading. One-sided projective-cohomology splitting gives canonical Kunneth in every degree. Distinct graph types have no nonzero bimodule map, since such a coefficient would be killed by the nonzero divisor2x. Origin grading determines the shifts within each type. Therefore the genuine nonnegative bivariate characters satisfy the two displayed product identities.

The tau character b is nonzero by the original Euler support. Cancellation in the integral Laurent domain gives d=2a, and evaluation at the cohomological sign gives a contradiction with the two odd outer coefficients of delta squared. I checked this final parity step separately from the earlier ungraded generic argument.

The theorem is exactly an exclusion for a bounded ordinary Soergel object with the specified ambient Euler class and an actual scalar-complex derived quadratic. It does not exclude non-scalar central complexes, polynomial differentials in unit-bimodule complexes, changed embeddings, different categories, localization or unbounded constructions. It makes no new purity or canonical-basis claim. The Grothendieck dictionary correctly separates the known Tor theorem from the new application and descent.

## 8. Final-text match and verification type

The entire generated fragment retains the report's full module proof, all generic and global steps, the one-sided AR9 explanation, the complete AR10 count and the final graded contradiction. The separate dictionary and source-access limitations also match. No statement was strengthened silently during conversion to TeX.

No numerical test was needed for this general homological proof. This review consists of full manual reconstruction, independent primary-source/hypothesis checks, and a complete generated-text match. I did not run an additional syntax compile; the author/root handle compilation and integrated visual QA. No master status or check file was changed.

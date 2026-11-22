# Cusp tameness and punctured surface consequence

Status at 2026-11-20T04:49:00.950235+00:00: configuration lemma and cusp theorem proved, with independent actual-file audits by root and D. Mixed klt/Gorenstein-lc boundary corollary also passed D's actual-file audit and primary CRY source reopening; the entire fragment is checked.

## Deliverable and exact scope

`D_cusp_tameness_B.tex` contains labels D:Gorenstein-lc-configurations, D:cusp-tame and D:Gorenstein-lc-boundary. The cusp theorem concerns normal integral finite separable covers, componentwise, etale on the punctured germ. It includes a single irreducible nodal rational curve by one node blowup. It proves tame ramification including residue separability in every characteristic. It makes no originality claim.

The proof works after strict henselization and uses proper henselian comparison. It does not assert a punctured completion comparison. A previous possible route through klt local finiteness was eliminated from the cusp proof: the discrepancy-zero exceptional fibre is a rational tree, so its fundamental group is already trivial on a proper resolution. The CRY theorem is only needed for the global mixed-boundary corollary.

## Primary sources opened

- Stacks Project, Lemma 58.9.1, tag 0A48, full statement and proof: finite etale covers of a proper scheme over a henselian local ring equal those of its closed fibre. URL https://stacks.math.columbia.edu/tag/0A48; web ref turn183517360view0. Root independently reopened it.
- Stacks Project, Lemma 54.17.1, tag 0C5R, full statement: any proper birational map of regular integral Noetherian surfaces factors into point blowups. URL https://stacks.math.columbia.edu/tag/0C5R; web ref turn183517360view2. Existing surface-resolution sources 0BGP and 0C2M and Kollar2013D section10.1 Theorem10.1 were already opened in D and are precisely reused.
- Stacks Project, section15.53 tag07QS, Lemmas15.53.5 and15.53.6: quasi-excellence implies Nagata; normal quasi-excellent local completion is normal. URL https://stacks.math.columbia.edu/tag/07QS; web ref turn183517360view1. Normalization finiteness is used; the completion statement was investigated but is not used in the cusp proof.
- Carvajal-Rojas and Yasuda (2025), Documenta Mathematica30,709--751, DOI10.4171/DM/1012, Theorem5.3 printedp739: local etale fundamental group of a log-terminal surface germ finite in arbitrary characteristic. TheoremB printedp713 and Corollary6.4 printedp741 state the complete local version. Publisher PDF reopened; web refs turn456574781view0/view1. Local PDF and arXivv4 TeX are under sources/CRY2025.
- Schroer1999D, introduction printedp1: normal proper surface projectivity iff its non-Q-factorial locus has an affine neighborhood, hence every regular proper surface resolution is projective. Exact local text lines18--28 read.

## Dependencies and non-claims

The cusp differential/discrepancy comparison reuses D:lc-elliptic-tame, independently audited earlier by B. The mixed-boundary consequence uses D:finite-exceptional-wild, also independently audited by B. No finite generation for arbitrary surface singularities, arbitrary lc index, or general higher-dimensional D1/D2 is asserted. The all-klt proper case alone overlaps the pre-existing projective case; the new consequence permits nonprojective proper surfaces with arbitrary retained singularities and isolated omitted cusp/elliptic points together with klt points.

## Prime-to-characteristic index extension

D_prime_to_p_index_B.tex contains three further checked statements, labels D:Gorenstein-lc-valuative-tame, D:prime-to-p-index-tame and D:prime-to-p-index-boundary. D completed an actual-file audit and reopened the primary inputs. Primary SGA1 reedition TeX parts/D/sources/SGA1/smf_doc-math_3_01.tex lines25225--25405, XIII5.1--5.3 printedpp428--430, gives the local regular Kummer cover, absolute Abhyankar lemma and strict-local domination. Stacks0EXT section15.116 Lemmas5--9 gives tame tower/subextension/common-Galois/base-change statements; web ref turn695790625view0. The index cover is explicitly constructed from the torsor of trivializations of the canonical line bundle; its Gorenstein and non-klt properties are proved.

The p-divisible-index remark was deliberately narrowed: CRY's introduction and Remark5.5 document failure of preservation of LOG TERMINAL singularities by index-one covers. They are not cited as a counterexample to preservation of log canonicity, which our proof simply does not establish in the inseparable case.

Root is pursuing a separate all-lc strengthening through the elementary general cycle argument and rational-tree Q-factoriality in positive characteristic. The checked prime-to-p theorem remains intact as a fallback and no all-lc conclusion is asserted by these files yet.

## All-lc core extension: checked

D_all_lc_core_B.tex is now proved and passed independent actual-file audits by root, C and D. It contains D:lc-exceptional-configurations, D:lc-cusp-tame and D:lc-core-valuative-tame. The classification uses rational coefficients only. For a selected cycle, all extra internal edges and external incidences are retained in the summed equation; negative definiteness forces one self-intersection less than minus two, and zero propagation forces discrepancy minus one around the whole cycle. External zero-discrepancy neighbors and internal extra edges are excluded. The arithmetic-genus-one case is isolated and nodality follows by point blowups.

No Gorenstein descent is needed: a quasi-etale cover of a Q-Gorenstein lc surface is Q-Gorenstein lc by canonical pullback and the determinant inequality. The previous henselian cycle argument then extends verbatim in its group-theoretic steps. The all-lc tree alternative is not claimed to be klt or rational. C separately proved bounded-exponent class group for a rational SNC exceptional tree in characteristic p; B read that entire proof and recorded its independent audit. C is assembling the global partial-resolution corollary. The earlier Gorenstein and prime-to-p statements are retained as checked historical milestones, not silently replaced.

## Higher-genus three-point surface: horizontal-tame reduction

At 05:14 UTC, `D_Schroer_horizontal_reduction_B.tex` contains the checked proposition `D:Schroer-horizontal-tame`: any finite etale cover of the three-point open U which is tame at the horizontal divisor A is tame at every vertical Ri. Thus the quotient killing only wild inertia at A is the full tame quotient of the smooth projective blowup and is finitely generated. D read the complete actual file and independently reopened both Hoshi primary statements; its proof audit passed. Root's actual-file audit has been requested.

Primary Hoshi2006 RIMS1558 was opened in full, downloaded, hashed, and text-extracted under `sources/Hoshi2006/`. Proposition2.4 printedpp16--17 proves the log product formula with one proper log-smooth factor and any connected log-regular second factor. PropositionA.10 printedpp57--58 identifies finite Kummer-etale covers exactly with finite covers tame at codimension-one boundary points. This precisely allows unrestricted wild ramification in the B direction. The argument uses the arcs t=s,z=lambda*s through the retained exceptional curves E0/E1, then the constant-c2 arc through E2; it makes no wild-inertia specialization-surjectivity assumption.

This is a strict restriction on a possible residual cover, not a new solved geometric instance and not full finite generation for the higher-genus surface. The remaining possible covers must be wild both horizontally and at a vertical exceptional valuation with inseparable residue extension. No claim that the horizontal wild image is finite has been established. Ordinary Kunneth for two nonproper curves is not used.

At 05:15 UTC, we independently audited D's `D_klt_threefolds.tex` in full and read the primary published CSK2023 text: Setup1.1 p694, TheoremA p695, Theorem3.7 pp708--709, Corollary4.5 and proof p714. Both `D:finite-local-images-arbitrary` and `D:klt-threefold-boundary` pass. In particular finite local images need no uniform order bound and the omitted set can be any codimension-two closed set; klt is needed only near that set, with p>5 in dimension three.


## 2026-11-20 05:56:57 UTC: post-checkpoint-seven source and obstruction work

The main Part B statements remain closed. The full all-genus Schroer three-point test is now closed by the independently audited formal-cone argument; the horizontal-tame reduction is retained as an earlier, more limited result.

The negative-curve formal-linearization theorem and its tame consequence have full actual-file audits by root, C and D. Their exact obstruction groups distinguish first order from every later order. The sufficient numerical condition is d > max(0,4g-4); no low-degree formal-linearity claim is made.

The explicit characteristic-two example in D_wild_genus2_curve_B.tex has full actual-file passes from root, C and D. It is a genuine quasi-etale double cover with fierce exceptional residue, at a single smooth genus-two curve of square -1. It refutes automatic tameness for such a curve, but not finite generation. The original 26-assertion certificate remains unchanged; D independently copied and reran it.

The companion D_wild_genus2_source_B.tex is now checked by root, C and D. Its (1,3,1)-weighted charts give a single smooth genus-two exceptional curve of square -2, and a finite lift to the target resolution restricting to Frobenius. The source discrepancy is -2. The independent 22-assertion certificate is recorded in output/wild_genus2_source.json. The existing weighted different inequality excludes every further wild degree-two cover of this source, with no hypothesis on the number of components upstairs. Purity, proper henselian comparison, and the explicit nilpotent Frobenius h1->h2->0 yield strict-local maximal pro-two groups 1 for T and Z/2 for S.

The remaining gate is arbitrary nonabelian wild inertia after other finite covers. A trivial maximal pro-two quotient does not imply trivial two-subgroups in finite non-two-group quotients. In particular, passage first to a tame cover can multiply the discrepancy ratio (2g-2)/d, and can change the exceptional curve and its p-rank. We have not promoted a finite full wild-inertia claim.

A tempting additional shortcut is not justified: the source T is not visibly formally conical. Its weighted initial form is F0=d^2+t^3*d+t*c^5, and the first higher term c^4*d has weight7. It is not in the degree7 Jacobian span generated by F0_c=t*c^4, F0_d=t^3, F0_t=t^2*d+c^5 and degree1 multiples of F0. A full nonconicality proof would also need the invariant exceptional-filtration argument. This is recorded as a direction, not as a checked paper theorem.

Independent complementary audits completed: C's weighted graded Q-factorial extraction (including p-divisible weights and normalized-blowup completion descent) and D's uniform H1/nonabelian-crown criterion. Primary Stacks0EGH/02RS/0BG4 and published LMT2020 pp10-13 were reopened; the latter's s>=d(L) was verified from a screenshot because text extraction obscures the inequality glyph. These audits do not close the general D.1/D.2(ii) gate.

## 2026-11-20 06:24 UTC: fixed finite cone cover

The two new fragments D_finite_formal_cone_cover_B.tex and D_finite_cone_boundary_cases_B.tex contain six statements, all now passed by C and D in complete actual-file audits, awaiting root's final assembly review. They construct one finite locally free cone cover of the completed germ from a curve cover killing the first-neighborhood class and later tangent/normal obstructions. Actual finite GE algebraization and the Stein ring identify an extension of the radial DVR, so one fixed finite cover bounds the full wild image for every finite covering group. The numerical threshold is d>2g-2, with order bound q for the displayed Frobenius choice; the equality case d=2g-2 is covered when omega_C tensor N is torsion, including arbitrary-index Q-Gorenstein germs. The explicit genus-two source T has a degree4 cone cover and wild image at most4, and its target S has bound8. These do not yet claim the whole D finite-generation problem. D is writing the global mixed-boundary corollary.

The added exact finite check has16 assertions and runtime0.044191410s. It checks the new infinity differential/canonical divisor arithmetic and the numerical bounds; full formal algebraization and group arguments remain the written mathematical proofs. An initial Python symbolic remainder implementation was replaced by polynomial reduction mod2 before the successful recorded run.

## 2026-11-20 06:36:30 UTC: promotion and exact residual

All eight local statements in the three finite-cone files are promoted to proved under their displayed hypotheses after C/D complete actual-file audits; the finite-jet pair also passed root's actual-file audit. The latter assumes only a retraction of C_r with rd>2g-2, constructs the finite Frobenius-pulled truncated cone through order r, and begins ordinary smooth-target lifting at n=r. The split first-neighborhood case d>g-1 is a recognition corollary, not separate movement. New pure-root route notes contain an exact local obstruction to filling rational tails, with13 polynomial checks; this is explicitly not a global D counterexample.

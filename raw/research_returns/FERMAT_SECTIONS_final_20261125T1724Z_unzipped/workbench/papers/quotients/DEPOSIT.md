# Deposit sheet

Status: prepared for filing; not deposited and no permanent work number assigned.

## Title

Fermat’s theorem for Selmer sections in solvable quotients

Grothendieck’s programme, after Kummer, McCallum, Pál, Stoll, and Saïdi

## Abstract

Grothendieck asked whether sections of the arithmetic fundamental group
of a Fermat curve arise from its evident boundary points. We study the
point-or-cusp Selmer form of this question in geometric quotients.
For every odd exponent divisible by three, five, or a regular prime,
every Selmer section in every finite derived quotient and in the maximal
prosolvable quotient is cuspidal. The section set is exactly three
disjoint packets, each parametrized by the full completed Kummer group.
Kummer's cyclotomic unit argument excludes first-case local centres;
a primary refinement of McCallum's supported-class argument isolates
the cusps. A global unit then identifies all local centres, and
Saïdi's localization theorem gives the global section.
For every regular prime greater than five, the full geometric
pro-prime quotient and the stated central and derived quotients have
the same three-packet classification throughout the prime-power tower.
At irregular primes, a cyclotomic class-rank bound gives one fixed set
of at most the exponent prime containing every compact local centre;
this applies at thirty-seven, fifty-nine, and sixty-seven.
We also prove the full geometrically pro-three classification at
exponents \(3^r\), \(5\cdot3^r\), and \(7\cdot3^r\), for \(r\ge1\),
using explicit arithmetic sources. The remaining pro-three exponents
and the complete irregular-prime classification remain open.
Separate applications of Stoll's finite-descent criterion provide
proper-curve results at exponents five, eleven, thirteen, and nineteen,
with explicit Jacobian factors, analytic certificates, and the precise
published arithmetic inputs. Two families of noncuspidal pro-three
sections fail the local Selmer condition at three. Pál's finite-action
theorem also separates different coordinate-boundary components in
the proper pro-three point map of every Fermat curve over finite
fields of characteristic prime to three and the exponent. Boundary
fibres have a uniform cyclic-block description; they are singletons
whenever three divides the exponent.
The mathematics and text were produced by GPT-6 Astra Pro in ChatGPT
Pro mode, selected principal statements were separately re-proved by
the same model, and no human has checked this paper.

## Subject and keywords

Arithmetic geometry; anabelian geometry; Fermat curves; Selmer sections; fundamental groups; cyclotomic fields; finite descent; local duality; modularity.

## Scope

The finite-derived, metabelian and maximal geometrically prosolvable Selmer theorem holds for every odd exponent divisible by 3, 5, or any regular prime greater than 5. The first prime not classified by this range is 37. The three rational cusp packets are disjoint and each is parametrized by H1(Q,Zhat(1)); the proof permits infinitely supported completed Kummer parameters and does not assume a full global lift of an unknown quotient section.

For every regular prime p>5 and every n=p^r with r>=1, the full geometrically pro-p group, every finite-derived quotient, every stated ordinary lower-central quotient, and every stable quotient retaining abelianization with torsion-free ordinary lower-central factors have the corresponding three H1(Q,Zp(1)) cusp packets. The separate arithmetic-source theorem gives whole nonabelian localization and integral compact localization for every odd regular prime. The fixed pro-17 fibre inside the prosolvable section set is classified: its Selmer subset is exactly the torsor of cusp parameters at coefficient primes other than 17, not the entire relative nonabelian H1 set.

The pro-3 range is unchanged: n=3^r, 5*3^r, or 7*3^r with r>=1. The full group and the same finite-derived, ordinary-central and stated torsion-free-grade quotients are covered. Compact base-five/seven pro-3 images and compact localization at exponent eleven are additional proper-curve results, not new affine pro-3 classifications.

For p>=5 with cyclotomic class rank r<(p+3)/8, one fixed set of at most p local points contains every compact Tp datum with curve-valued witnesses at all finite places. At 37, 59 and 67 the set lies in the three cusp residue discs; equality with the three cusps is not proved. At odd n=pm, the fixed-set bound is (p-3)d^2+3d, where d=gcd(m,p-1). The first-case relative-rank and odd-character congruences are proved separately in the proper mod-p abelian quotient. The prescribed supported-tower condition needed for further irregular cusp-disc isolation is explicit and remains unproved in those cases.

The separate Jacobian arithmetic results remain part of the paper. They include the complete quintic, septic, eleven and nineteen analytic/arithmetic certificates, finite full Sha for the exponent-eleven Jacobian and the rank-zero nineteen complement, and the split-prime rational Selmer theorem for the classical thirteen Prym. No finite whole Sha theorem is asserted for that Prym. Their section consequences at regular exponents are subsumed by the cyclotomic argument, while their proper-curve and arithmetic conclusions remain independent.

## Eight opening requirements

| Requirement | Location and content |
| --- | --- |
| Title and intellectual origin | Title and subtitle identify Fermat Selmer sections, Grothendieck's programme, and the contributions of Kummer, McCallum, Pál, Stoll, and Saïdi. |
| Contextual abstract | The abstract starts with Grothendieck's question, distinguishes the quotient ranges and the remaining irregular/pro-three questions, and ends with the exact model and no-human-check declaration. |
| Main theorems in full and in words | Section 1.1, “Main results,” states all principal transfer, arithmetic, primary, finite-field and conditional results, with their local-witness and quotient hypotheses. |
| Mathematical significance | The opening of Section 1 explains the section-theoretic Fermat question and why the completed cusp-parameter packets and quotient distinctions matter. |
| Division of credit | The introductory source-role table and adjacent prose identify published theorem inputs, neighboring work, and the deductions proved here; the separate classical Jacobian results retain their attribution. |
| Context and neighboring results | Section 1 and the comparison section locate Stoll, Betts–Kumpitsch–Lüdtke, Porowski, Hoshi, Pál and the prior Fermat/CM work with exact scope. No priority claim is made. |
| Scope and limitations | Each principal statement specifies its assumptions; the unresolved-boundaries section and the thirty-seven discussion distinguish finite local sets, proper boundary fibres and structural arithmetic from global affine classification. |
| Proof overview | Section 1.2, “Proof overview,” appears before the proofs and explains the regular-prime, descent, arithmetic-source and finite-field arguments. |

## Finite-field coordinate-boundary fibres

For every n>=3 over k=F_Q of characteristic prime to 3n, the full proper geometrically pro-3 point-section map separates rational points on different coordinate-boundary components. The full arithmetic group G_k is retained and conjugacy is by the geometric kernel. If the rational boundary is nonempty and d=gcd(n,Q-1), each component has d points. There is one divisor h of d, with 3 not dividing h, such that every boundary fibre is a coset of mu_h(k) in the regular mu_d(k)-action. There are exactly 3d/h boundary section classes. If 3 divides n, h=1, so the boundary map is injective over every allowed finite field.

For every prime exponent a>=5, the nonsplit case Q not congruent to 1 modulo a has three distinct boundary classes. In the split case either all 3a classes are distinct or each whole coordinate component is one fibre. For odd n prime to 3, the specified sufficient injectivity primes q with gcd(n,q-1)=1 have natural density product over p dividing n of (p-2)/(p-1), including 3/4 at n=5 and 5/6 at n=7. For 3 dividing n, all good primes give injectivity. The density is that of a stated sufficient set, not a claim that it equals the density of every injectivity prime.

Every fibre in this assertion is intersected with the coordinate boundary. No claim excludes an ordinary proper point from the full fibre of a boundary point, and no new affine pro-3 exponent is classified. The exact coordinate-divisor order is proved in every characteristic not dividing n. Pál's theorem is used only for C3 with 3 retained, never for S3 with only 3 retained. Target26 independently checked the earlier a=5,7 theorem with its declared related-work exposure. The separate exact current-theorem Target27 froze on 25 November 2026 at 16:46:56 UTC; root completed the whole proof, source/exposure audit, 23-entry manifest and exact-code comparison at 16:50:12 UTC. It covers the full general theorem, including the 3-divisible clause and exact divisor order. Earlier exact A/B and SGA1 exposure, and the initial inventory following a disclosed short interval of internal reasoning, remain explicitly qualified.

## The remaining arithmetic question at thirty-seven

For the cyclic quotient C: y^37=x(1-x)^10, its Jacobian is rationally isogenous to a sixfold A and a twelvefold P. The factors are rationally simple, End_Q^0(A)=Q and End_Q^0(P)=Q(zeta_3); A has positive rational rank, the rank of P is even, and P(Q)_tors is cyclic of order 37. Their conductors are 37^12 and 37^24; the root numbers are -1 and +1. The complementary representation uses a Dirichlet character of order nine, whose relevant Hilbert twists have nontrivial cubic central characters over a real sextic field.

These are structural and applicability results. Neither L(P,1) nonvanishing, rank P(Q)=0, whole-Sha finiteness, nor the split-prime Tate-Sha hypothesis is proved. The sixfold's positive rank prevents it from being a rank-zero target. The twelvefold is the only possible positive-dimensional rational rank-zero factor within this cyclic quotient, but its required arithmetic remains open. The exact program verifies finite structural arithmetic only. The all-prime exponent-37 classification and all remaining affine pro-3 gates are unchanged.

## Quintic finite-depth limitation

At rational primes q different from 3 and 5, split in Q(zeta5), with Frobenius of order twenty on the three-torsion of A=Jac(v^2+v=u^5), the full arithmetic cohomology set H1(G_Fq,N/gamma4 N) is a singleton for the proper Fermat quintic. Thus the whole proper point map is constant through nilpotency class three. This prime set has natural density 1/10 and contains q=11. The full proper pro-three theorem still separates different coordinate components; no full-group collision within one component is proved. Tensor-degree four already has a Frobenius eigenvalue one, so the stated low-depth exclusion stops there. This auxiliary limitation does not enlarge the affine classification or reduce a main mathematical gate.

Two further geometric observations delimit diagonal-symmetry arguments for exponents5 and7. Over a finite field containing the relevant roots of unity, a nonidentity diagonal twist of Frobenius cannot have three-power order on the full Fermat residual homology; the three quotient maps force the diagonal weights to vanish. Separately, a geometric complement for the full diagonal group has centralizer contained in gamma2, with quotient modulo its intersection with gamma3 isomorphic to Z3^(g-1), of rank5 or14. The complement is not asserted to be Galois invariant. These statements do not decide the full same-component fibres or supply an affine boundary-support theorem.

## Intellectual sources

Grothendieck supplies the section-theoretic question; Kummer's cyclotomic method and McCallum's supported-class argument supply the regular-prime arithmetic mechanisms. Stoll supplies finite abelian descent and finite support, Saïdi the localization input for actual full comparison-section actions, and Pál the admissible prime-order finite-action theorem. The exact roles of Shafarevich, Darmon, Nekovář, Elkies, Gross, Rohrlich, Lim, Tzermias, Loeffler, Rockwood, Zerbes, Mazur, Rubin, Serre, Tate, Jacquet, Langlands, Wiles, Shmelkin, Labute, Lubotzky, Segal, Coleman, Brumer, Rousseau, Fontaine, Herbrand, Gras and the neighboring section literature are stated where used and in the source-role table. Published works retain their own rights. No priority claim or contact with the cited authors is asserted.

## Method and rights

Mathematics and text produced by GPT-6 Astra Pro (ChatGPT Pro mode); same-model independent reproofs and targeted checks are distinguished in CHECK_EVENTS.tsv. Runtime effort not exposed. Earlier Claude Opus5.5 checks are historical records, not checks performed in this run. No human has checked this work. Original text and code: CC0 1.0.

## Current verification and historical preservation

Producing proofs, exposed whole comparisons, and separate same-model statement-only reconstructions are recorded separately in CHECK_EVENTS.tsv and the principal-statement coverage matrix. Targets22,23,24,25 and the higher-exponent addendum have preserved completed proofs and source audits. Target21 is one continued recovery reconstruction with declared earlier proof memory; it is not a second independent worker and does not restore lost original bytes. Target19's continued reconstruction passed whole comparison for its original arithmetic, primary and whole-fibre claims. Its kernel claim proves the whole-fibre bijection; the later Target21/all-regular argument supplies the classified Selmer subset.

The complete current FQ.005 and FQ.009 statements were separately reconstructed by a fresh no-history worker and frozen before proposed-proof exposure. Root's whole proof, source and identity comparison passed on 25 November 2026 at 16:31:48 UTC. This covers every stated exponent, quotient, ramification set, and both noncuspidal families; the earlier partial-check qualifications remain in the historical records. Target26 checks the earlier quintic/septic finite-field theorem only. The separate exact Target27 reconstruction of the stronger general theorem, including the 3-divisible clause, is frozen and whole-compared: root receipt `root_finitefield_general_complete_comparison_pass.json`, 16:50:12 UTC. Its prior exact A/B and SGA1 exposure and initial-inventory timing are disclosed; no producing-proof exposure preceded its freeze. Recovery and further checking are not counted as mathematical movement. No human has checked this work.

The exact 14:30 editorial proposal was never inserted into the manuscript. Its canonical label map was recovered and hash-verified; the full proposal remains lost and is not reconstructed under its old identity. Current source integrations have their own dated manifests. Earlier statement versions and check events are retained without replacing their historical status descriptions. The general finite-field statement retains its stable local tag with explicit immutable earlier-scope snapshots; its older quintic/septic check is not silently promoted to the stronger theorem.

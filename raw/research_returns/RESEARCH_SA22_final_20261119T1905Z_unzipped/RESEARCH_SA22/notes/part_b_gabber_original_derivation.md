# Gabber1994: original main theorem, exact hypotheses, and subject21 deduction

## Status and exact source

The original publisher preview of Ofer Gabber, *Affine analog of the proper base change theorem*, Israel Journal of Mathematics87(1994),325–335, now supplies original printedpp325–326. Both pages were visually read. The complete main **Theorem1, p326**, together with the definition and equivalent criteria for a henselian pair onp325, gives exactly the input used in `thm:B3-21`. The original article's later §5Corollary1 and its complete proof have **not** been read. They must not be cited as if directly opened. The full modern proof in Stacks tag09ZI remains separately opened and cited.

The prompt requires a derivation from Gabber1994 and exact locators; it does not require the particular later locator §5Corollary1. The actual main Theorem1 is a sufficient, more transparent original locator for the affine assertion. Its hypotheses are read from the original pages, not inferred from the abstract or from a modern generalization.

Current source outcome: the named-original Gabber requirement is discharged by the relevant original main theorem and its checked deduction below. The parent independently visually read both original pages and checked the deduction before integration. No whole-article reading is claimed, and the distinct Fujiwara1995 original-source requirement is unaffected.

## Lawful public retrieval and actual records

The current publisher article landing is ordinary public metadata. Its actual HTML has no preview link, so no preview endpoint was initially inferred from it. A new exact public CDX query returned an actual2018publisher landing:

- https://web.archive.org/web/20180616002714id_/https://link.springer.com/article/10.1007%2FBF02773001

This page explicitly embeds and twice advertises a public “Download preview PDF” link:

- https://page-one.live.cf.public.springer.com/pdf/preview/10.1007/BF02773001

That old host returned ordinary404, not an authentication or subscription denial. A separately logged stale-host repair kept the advertised `/pdf/preview/10.1007/BF02773001` path unchanged and used the publisher's current public preview host, already actually opened for Raynaud:

- https://page-one.springer.com/pdf/preview/10.1007/BF02773001

This returned HTTP200, application/pdf,70,550bytes,2pages, SHA256
`400895d1ea24f5dee20df5e28e604b76468ab6d3c679c7fb20baa4523a94f519`.
No subscription PDF URL, page-range parameter, access token, header workaround, authentication, or preview-limit change was used. The current Gabber landing is not inaccurately described as advertising the repaired URL: the old public landing advertises the path, and the host migration is expressly recorded.

Files:

- `sources/part_b_gabber_current_preview.pdf`
- `sources/part_b_gabber_current_preview.txt`
- `qa/part_b_gabber_preview_325.png`
- `qa/part_b_gabber_preview_326.png`

Utilities and measured times:

- `code/part_b_gabber_advertised_preview.py`: one current metadata request26.959410457995546seconds, wholeutility26.983111624998855seconds.
- `code/part_b_gabber_historical_preview.py`: exact public metadata10.640037994999147seconds, actual2018HTML9.356374241004232seconds, wholeutility20.008519709997927seconds.
- `code/part_b_gabber_original_preview.py`: unchanged old preview URL404 in7.238426486001117seconds.
- `code/part_b_gabber_preview_migration.py`: exact old-URL capture query200/empty list6.734107314994617seconds; repaired current public preview9.213256465998711seconds; parallel wholeutility9.215714224999829seconds.
- A logged PyMuPDF command extracted and rendered both original pages in0.15393232899805298seconds. It is a source-inspection command, not a mathematical finite check, and is not falsely identified as a separately saved historical script.

The web-search service could not open the successful public PDF URL (`turn526094499view0`, internal-error result). This is not the evidence for reading it. The ordinary HTTP response, exact saved PDF, visual page reads, and hash are the evidence. The current publisher metadata was opened as `turn590378913view0`; unsuccessful preview-oriented search results are `turn585058224search0`–`search9`.

## Exact original hypotheses

On printedp325, a pair consists of **an arbitrary commutative ringA and an idealI**. The displayed equivalent conditions include:

1. I lies in the Jacobson radical, together with the stated lifting property for coprime monic polynomial factorizations;
2. for every finite A-algebraB, the map from idempotents ofB to idempotents ofB/IB is bijective;
3. every A-algebra map from an étale A-algebra toA/I lifts uniquely toA.

Theorem1 on printedp326 uses this definition. For X=SpecA, Z=Spec(A/I), and the morphism of étale sites induced by the closed immersion, it asserts that the canonical restriction

H^q(X_et,F) → H^q(Z_et,i_et^*F)

is an isomorphism for **every torsion abelian étale sheafF onX and every integerq≥0**. The original image saysq≥0; its OCR loses the lower stroke in places and must not be used to replace this byq>0.

There is no noetherian hypothesis, no finite-generation hypothesis onI, no requirement thatF be constructible or locally constant, and no invertibility restriction on its torsion primes in this stated theorem. These are absences in the complete original theorem and definition, not extrapolations from the bibliographic abstract. The source itself immediately warns that arbitrary nontorsion coefficients cannot be substituted. We do not use its briefly stated nontorsion example as a newly proved counterexample here.

## Full deduction of the manuscript's equivalence

Fix any commutativeA, idealI, X=SpecA, Z=Spec(A/I), and i:Z→X. Let(i)mean that(A,I)is henselian; let(ii)mean that restriction onH0 is an isomorphism for every torsion abelian étale sheaf onX; and let(iii)mean the same in every cohomological degreeq≥0.

**(i)⇒(iii).** This is precisely Gabber's original Theorem1,p326. The objects, category, sheaf type, restriction map, and quantifiers agree exactly. No reduction to noetherian rings, finite-type ideals, constructible sheaves, or invertible torsion is made.

**(iii)⇒(ii).** Setq=0.

**(ii)⇒(i).** LetB be an arbitrary finite A-algebra and f:Y=SpecB→X the corresponding finite morphism. The direct image F=f_*underline(Z/2Z) is a torsion abelian étale sheaf onX. Degree-zero proper base change for this finite morphism identifies i^*F with the direct image of the constant two-element sheaf on Y_Z=Spec(B/IB). Thus(ii) gives a bijection

H0(Y_et,underline(Z/2Z)) → H0((Y_Z)_et,underline(Z/2Z)).

A section of this constant sheaf is a locally constant function to a two-element set; its two inverse images are a clopen decomposition. Such decompositions are equivalent to idempotents in the coordinate ring, by assigning to an idempotente the two clopen sets defined bye=0 ande=1. The restriction map on sections corresponds exactly to reduction of the idempotent moduloIB. Consequently Idem(B)→Idem(B/IB) is bijective for every finite A-algebraB. This is original condition(b),p325, and hence(A,I)is henselian. The separately opened Stacks Lemma15.11.6/tag09XI gives the same criterion.

The Jacobson-radical condition has not been silently discarded. It even follows directly from this all-finite-algebras test: if some maximal idealm ofA did not containI, chooseB=A/m, finite as an A-module. ThenIB=B, soB/IB=0; the two distinct idempotents0 and1 of the nonzero fieldB would map to the same idempotent of the zero ring, contradicting injectivity.

This proves the exact universal degree-zero characterization in the manuscript. It does not replace the universal sheaf quantifier by a single sheaf: the existing explicit Kummer example onGm shows that the latter reading is false. Completeness implies the henselian-pair condition by the separately opened Stacks Lemma15.11.4/tag0ALJ; completeness is a sufficient corollary, not an extra assumption imported into Gabber's theorem.

## What is and is not claimed read

- Original definition and its three criteria onp325: opened.
- Original complete main Theorem1 statement and all its hypotheses onp326: opened.
- Original remarks on constant coefficients and the beginning of Lemma1.1 onp326: read, but the continuation of its essential-surjectivity proof is not available in the preview and is not asserted proved from that page alone.
- Original §5Corollary1 and original full proof: not opened.
- Full modern proof and degree-zero lemma in Stacks59.82/tag09ZI: independently opened earlier.
- Subject21's universal characterization: fully derived above from the opened original main theorem and idempotent criterion, with the stated proper-base-change input.
- Fujiwara1995 completion-complement theorem: remains a distinct source gate; its noetherian original scope is not changed by this retrieval.

No new mathematical finite program was needed or run. The previous finite counterexample certificates and the formal all-rings argument retain their existing scope.


## Integration completed

The existing `thm:B3-21` now cites original Theorem1,p326 and condition(b),p325 directly, with an explicit Jacobson-radical check. The source-status paragraph, bibliography entry BGabber1994, subject21 inventory and owned result/event exports are updated. No new numbered theorem or finite mathematical test is introduced. The parent owns the aggregate report and remaining-source ledger.

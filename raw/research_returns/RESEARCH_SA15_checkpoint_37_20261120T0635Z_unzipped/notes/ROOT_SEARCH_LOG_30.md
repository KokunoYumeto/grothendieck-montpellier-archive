# Root original-source and search log for checkpoint30

This records actual retrieval and reading scopes, not theorem importation. Earlier logs retain the earlier searches and any failed retrievals.

## Rains--Sam: genus-two trivectors and characteristic two

Searches after checkpoint29 used the exact queries `"Coble" "Cartier" characteristic 2`, `"trivectors" "characteristic 2" abelian surface`, and `"theta" "multiplication" "Frobenius" "level 3"`. The primary result was opened in the publisher's original PDF: https://content.algebraicgeometry.nl/2019-3/2019-3-016.pdf . Other results were metadata or excerpts only and supply no theorem here.

Rains, E. M., & Sam, S. V. (2019). Vector bundles on genus 2 curves and trivectors. *Algebraic Geometry, 6*(3), 328--345. https://doi.org/10.14231/AG-2019-016 . OPENED, partial precise proof scope below.

The root read the introduction onpp328--329; the complete proof of Proposition2.5 onp330; Lemma2.6, Proposition2.7 and Corollary2.8 onp331; Lemma2.9 and Proposition2.10 onp332; the complete Lemma5.7 and Remark5.8 onpp341--342; and the AppendixA setup, TheoremA.1 statement and full proof, and full LemmasA.3,A.5,A.6 onpp342--344. The short full proof of Theorem5.4 onp341 was read, but it explicitly assumes characteristic different from2 and its dependencies4.3/4.4 were not fully audited. The full paper and all external dependencies were not read.

The relevant geometry describes H0(A×A,O(3Theta_1+3Theta_2-Theta_difference)), a nine-dimensional space, through the isogeny(a,b)↦(2a+b,a+2b), whose kernel is diagonal A[3]. The characteristic-two appendix describes a branch cubic through the restricted-Lie square of a trivector and its Pfaffian description. None of these read passages identifies this paper's actual Cartier pairing on higher theta sections. A theta-triality identification and the required twisted cross determinant remain unproved. No theorem from this source has been imported into the monodromy proof.

Root web references for the opened original and subsequent within-PDF reads: turn143235750view0, turn140003950view0; find passages turn311471667view0, turn311471667view1, turn311471667view2. These are retrieval provenance identifiers, not substitutes for the bibliographic entry and exact printed locators above.

## Torsion avoidance and semihomogeneous theta bounds

Exact engine2 queries: `abelian surface theta divisor maximal isotropic subgroup disjoint odd torsion` and `theta divisor torsion points maximal isotropic subgroup nonvanishing theta constants`. The original author-site Torsion_again.pdf request returned TimeoutError. The EMS two-page erratum and the arXiv1512.09296 original were successfully opened. A subsequent engine1 verification used `"Theta nullvalues of supersingular Abelian varieties" Pieper arxiv` and `"Torsion points on theta divisors" 2n n general bound`, locating the original Pieper and Pareschi preprints. These originals were opened; other hits were metadata only and supply no theorem.

The exact scopes and bibliographic data are recorded in the four new late-source census rows. The Pareschi11-page original was read completely, including its TheoremA/B proofs and genus2 TheoremC argument; the external semihomogeneous-bundle and multiplication dependencies were not newly audited. The source's field is complex. The genus2 proof suggested a direct alternative using the normalization and local delta invariant of[ell]Theta; the root's separate candidate proves its own branch-count bound in the stated characteristic and claims no extension of Pareschi's bundle theory. Its link to the actual Cartier tensor is unproved.

Retrieval provenance: search turn317902890search20--23; timeout turn246763466view0; complete erratum turn246763466view1; arXiv metadata turn246763466view2; original torsion paper turn608871158view0; Pareschi original turn964236038view0 and subsequent complete text reads turn911512914view1--3, turn811879239view0, turn709303443view0; Pieper original introduction turn964236038view1. These identifiers record retrieval, not an assertion that every dependency was read.

## Post-freeze B86 original-source verification at 2026-11-20T01:16:53.905061+00:00

Root opened and read the complete displayed proof of Stacks Theorem10.160.8 (Tag032A), https://stacks.math.columbia.edu/tag/032A, and Colmez, Corps locaux, https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf, Proposition2.12 with full proof on printedp11 and Proposition3.7 with its full two-divisibility proof on printedpp14-15. The opening field definition and Section3 perfect-residue hypothesis were checked: finite residue is not required. These are freshly read original passages, not theorem statements inferred from snippets. Linked Stacks formal-smoothness proofs were not newly read. The actual quotient-average formula applies to the totally ramified degree-p subextension of the genuine point field. Exact root web references, all source scopes and the separate candidate audit are retained in outputs/root_B86_audit.json. No frozen paper or bibliography was changed.

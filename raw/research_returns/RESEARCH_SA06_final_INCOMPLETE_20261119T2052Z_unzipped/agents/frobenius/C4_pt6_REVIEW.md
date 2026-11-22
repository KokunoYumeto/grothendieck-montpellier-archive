# Threefold improvement via Prym–Tyurin sixfolds

## Result

`C4_pt6_addition.tex` proves C.4o and C.4p. Every principally
polarized sixfold over any algebraically closed field has an integral
curve of class six times the minimal class, so `[6]` factors through
a product of Jacobians. It follows that every abelian threefold
satisfies

\[
 s_J(A)\mid\gcd(6,\delta(A)).
\]

Together with C.4n, the strongest current bounds are two for surfaces
and six for threefolds. The residual primes in this contribution
are respectively `{2}` and `{2,3}`. Thus rank-one surface type
`(1,3)` and threefold type `(1,1,5)` are affirmative. No general
resolution or counterexample is claimed for the residual cases.

## Primary theorem and field-transfer check

The published ADFIO2020 PDF contains **Theorem 1** and **Corollary 2**
on p.165. The latter explicitly states the effective curve assertion
for every complex principally polarized sixfold. The older preprint
numbers the main theorem 0.1, so that number must not be attached to
the published pagination. The exponent-six theta-restriction
identity is on p.164.

To pass from C to an arbitrary algebraically closed field of
characteristic zero, one must preserve more than an arbitrary
factorization of `[6]`: the curve class is needed for the next
specialization. We therefore spread the curves, their pointed maps,
and the exact identity

\[
\sum_a m_a f_a\lambda_{J(C_a)}^{-1}\widehat f_a\lambda_B=[6].
\]

These data spread to a nonempty finite-type scheme over the finitely
generated field of definition of `(B,Xi)`. A closed point has a
finite residue extension and can be embedded into the target
algebraically closed field. The same adjoint identity then holds.
The pairing calculation identifies the resulting curve class with
`6 gamma_Xi`; no argument based only on the existence of an
unpolarized retraction is used.

In characteristic p we use the polarized Witt lift already audited
in C.4m. Fulton's geometric specialization and compatibility with
cycle classes yield an actual integral special cycle. Rational
ell-adic equality for one ell different from p suffices for the
numerical equality used by Matsusaka. Neither p=2 nor p=3 is
excluded: the scalar six is never inverted.

For a sixfold X, principalizing every ample L gives
`6 chi(L) in I_J(X)`, hence `s_J(X)|6 delta(X)`. The Poincaré
bundle on `A x Adual` has Euler characteristic minus one, so delta
is one. Restriction to A and the earlier `delta(A)` factorization
complete the proof. The fragment gives a seven-polarization
integer interpolation formula, so the gcd construction is finite.

## Integration

Input the new fragment after `C4_prym_addition.tex`. Add
`C4_pt6_references.bib`, `C4_pt6_results.csv`, and
`C4_pt6_CHECK_EVENTS.tsv` to the corresponding master aggregations.

The final unnumbered scope paragraph in `C4_pt6_addition.tex`
supersedes the two older remaining-work paragraphs in
`C4_additions.tex` and `C4_prym_addition.tex`. For a clean narrative,
retain only the latest one. The earlier bounds 6/120 and their
tables are valid intermediate results, but they are no longer the
strongest bounds in the report.

## Opened-source ledger

| Key | Primary URL and locator | Opened refs |
|---|---|---|
| frC4ADFIO2020 | https://www.mathematik.hu-berlin.de/~farkas/a6cr.pdf; published Theorem1 and Corollary2 p.165; theta restriction and exponent6 p.164 | turn998089042view0; turn453460396view0 |
| frC4EGFSOptimality2025 | https://arxiv.org/html/2512.04902v1; Theorem1.2, smallest multiple exactly6 for a very general complex ppav6 | turn998089042view1; turn453460396view2 |
| frC4Oort1971 | https://www.numdam.org/item/CM_1971__23_3_265_0.pdf; valid sufficient direction of Theorem2.4.1 p.286, Corollary2.4.2 and proof p.287 | turn988083530view0; turn337819996view3 |
| frC4Fulton1998 | https://djvu.online/file/Pl4avuZzLcI6I; Example20.3.5 p.400 | turn115304589view2 |

All URLs were opened; search-result snippets alone were not used
to establish any theorem. The ADFIO DOI is printed on the opened
published PDF first page: `10.1515/crelle-2018-0005`.

The existing 2026 EGFS paper supplied the lead in Remark8.12, but
the upper-bound proof is based on the opened ADFIO primary article.
The companion EGFS2025 paper is used only to explain the scope of
generic sharpness. No very-general ppav theorem is applied to the
special family `A x Adual`.

## Why the requested matroidal obstruction does not directly apply

This is a proved limitation of that direct approach, not a claimed
obstruction to solving the residual cases by other degenerations.

Suppose a complex family `X=A x Adual` has unipotent monodromy around
a loop, and let N be its logarithm on `H1(A,Q)`. On the dual family
the logarithm is minus the transpose. Consequently

\[
 N_X=N\oplus(-N^{\mathsf t}),\qquad
 \operatorname{rank}N_X=2\operatorname{rank}N.
\]

Thus every nonzero such monodromy operator has even rank. Passing
to an isogenous abelian scheme conjugates rational monodromy;
finite ramified base change replaces N by a positive integer
multiple, which also preserves its rank.

In EGFS2026, Definition4.1(3), the monodromy form for each coordinate
divisor is a positive multiple of `y_s^2`, of rank one for a nonloop
of the matroid. Definition2.12 identifies that form with N through
the principal polarization, so its rank is the rank of N.
Hence a nontrivial isotypic family obtained in this way cannot
directly satisfy the stated matroidal-family condition. This
explains a concrete missing hypothesis in the proposed application
to `A x Adual`; an adaptation to rank-two monodromies would need
new work.

Opened locators: https://arxiv.org/html/2507.15704v3,
Definition2.12 (`turn596713770view0`), Definition4.1 and Remark4.2
(`turn950968762view1`), and Theorem1.6
(`turn199065391view3`). This rank calculation does not exclude a
different family or a different geometric obstruction, and does
not by itself imply that the residual cases are known open.

## Remaining search status

The principalization method has reached its precise local limit:
if ell divides delta(A), every same-dimensional principalization
has degree divisible by ell. The new generalized-Prym and
Prym–Tyurin constructions overcome some of those denominators
using `A x Adual`, but leave the primes recorded above. Searches
and checks in this contribution have not found an exact all-case
theorem or counterexample for nonprincipal surfaces or threefolds.
No novelty or priority claim is attached to the new deductions.

## Independent verification and editorial cleanup

On 2026-11-19, `/root/cycles` independently opened the published ADFIO PDF, verified Corollary 2 on printed p.165, and checked the descent of curves, maps, and the polarized factorization identity over an algebraically closed field of definition. The same review confirmed polarized lifting and integral cycle specialization to every characteristic. `/root` independently checked both new proofs and preservation of integral coefficients.

The two superseded remaining-work paragraphs were removed from `C4_additions.tex` and `C4_prym_addition.tex`. Only the latest paragraph in `C4_pt6_addition.tex` is retained. The algebraic-equivalence macro in C.4m and the final table heading were corrected.

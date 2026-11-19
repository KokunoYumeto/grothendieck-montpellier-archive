# C.3at: positive-characteristic ordinary restriction boundary

Status at 2026-11-19 11:07 UTC: finalized after full independent root
and cycles proof/source audits. Cycles' completed receipt is
11:06:41.565319UTC. The final file is
`C3_positive_characteristic_cy_boundary.tex`; the former draft is a
comment-only supersession pointer. The canonical result and original
check events are registered.

## Exact scope

For every prime p and r>=2, the proposed construction gives a regular
strict local ambient ring of dimension N=r+2, a principal regular
puncture, zero source CH^r, and a non-torsion ordinarily algebraically
trivial target class. The coefficient field is explicitly
the algebraic closure of Fpbar(T), where T is the specified finite-field
Calabi--Yau hypersurface. This is not a claim over Fpbar. The latter
field has torsion ordinary algebraically trivial cycles.

## Primary sources actually opened

1. Berthelot, Bloch and Esnault, *On Witt vector cohomology for singular
   varieties*. Complete 42-page author manuscript, filename version051014,
   `sources/bbe2005_witt_author.pdf`.
   URL: https://page.mi.fu-berlin.de/esnault/preprints/helene/80WittCohomology051014.pdf
   arXiv primary metadata identifies v1 submission as17October2005.
   Exact inputs read: introduction (1.1), author p.1; Theorem1.1 p.2;
   the derived inverse-limit and proper cohomology limit statements in
   Section2 pp.6--7; p=FV=VF and coordinatewise Frobenius in Proposition2.1
   proof p.7; Lemma2.5 and (2.7) pp.9--10. The direct Witt-module induction
   in our proof is supplied explicitly, rather than attributed to an
   unstated unit-root theorem. Published metadata independently opened
   at Cambridge: Compositio Mathematica143(2)(2007),363--392,
   DOI10.1112/S0010437X06002533. Exact locators in the proof refer to the
   opened author pagination.

2. Esnault, *Varieties over a finite field with trivial Chow group of
   0-cycles have a rational point*. Complete published five-page PDF,
   Inventiones Mathematicae151(2003),187--191,
   DOI10.1007/s00222-002-0261-8,
   `sources/esnault2003_chow_rigid.pdf`.
   URL: https://page.mi.fu-berlin.de/esnault/preprints/helene/62-chowgroup.pdf
   Exact inputs read: norm/spread diagonal argument p.187; crystalline
   correspondences and rational-Chow factorization Section2 p.189;
   Lemma2.1 and proof pp.189--190: supported cohomology in positive
   codimension has slopes at least one. We do not misstate its Theorem1.1
   as a general divisor-support theorem. The source-support term in our
   diagonal decomposition is separately treated by alterations and
   cohomological dimension.

3. Huang, Lian, Yau and Yu, *Hasse--Witt matrices, unit roots and period
   integrals*, arXiv1801.01189v1, 3 January2018. Complete 26-page primary
   author PDF, `sources/huang_lian_yau_yu2018_hasse.pdf`.
   URL: https://archive.ymsc.tsinghua.edu.cn/pacm_download/311/8917-Hasse-Witt3.pdf
   Exact inputs read: Section2 diagram(2.1), Corollary2.3 pp.7--8;
   Corollary2.5 p.9; Corollary2.8 p.11. General projective hypersurface
   coefficient formula works even when p divides the degree. The
   introduction's special Dwork-family assumption is not imported.
   arXiv primary metadata opened and confirms v1/date/26 pages.
   A Brandeis published-metadata page returned403; no claim to have
   opened the journal version is made.

4. De Jong1996, Theorem4.1 and Remark4.2 printed p.66, full primary
   paper previously opened and retained for C.3w. Its use is a smooth
   projective alteration of each source-support image. Rational cycle
   lifting is proved explicitly by choosing a closed point of a proper
   generic fibre; inseparable degrees are allowed and inverted.

5. Kerz2009, Theorems7.1 and7.5, author pp.21--22, full primary PDF
   independently opened in the preceding C.3as work and reread locally
   here. Its exact scope is regular schemes containing a field with
   sufficiently large residue fields. Every residue field here contains
   the infinite coefficient field. No finite-type condition is silently
   imposed on the strict henselization.

6. Stacks Tag0FD4, Lemmas33.47.1 and33.47.3, opened full statements and
   proofs on19November2026. They give immersion away from a prescribed
   closed set and Bertini smoothness. First-jet separation at the two
   prescribed points and connectedness of sufficiently ample sections
   supply the actual curve family.

7. Internal C.3e, full proof reread: integral strict-cone injection over
   every algebraically closed field, not only characteristic zero. All
   base changes, refined pullbacks and finite-descent hypotheses match.

## Retained exact computations

`code/check_ordinary_cy_boundary.py` constructs the prescribed Fermat or
triangular base polynomial plus lambda times the coordinate product.
It computes the Hasse coefficient exactly and checks that the full
Jacobian ideal is the unit ideal in every projective chart by finite-field
Groebner bases. It tries prime-field parameters first and then quadratic
extensions. All seven sampled pairs pass:
(p,r)=(2,2),(3,2),(5,2),(7,2),(2,3),(3,3),(5,3).
The p=3,r=2; p=2,r=3; and p=5,r=3 cases use quadratic extensions,
which are recorded with their irreducible polynomial and exact equation.
Fresh runtime:0.625202717 seconds at10:57:07UTC.
The initial prime-field-only run had four verified cases and three
honestly exhausted searches; extending the declared parameter field
resolved those three. Universal termination is independently proved by
the nonempty-open argument, not inferred from these seven computations.

`code/fetch_ordinary_cy_sources.py` retained all three new primary PDFs
and text extractions. Runtime13.140003084 seconds; exact byte counts and
SHA256 hashes are in `sources/ordinary_cy_source_manifest.json`.

The complete draft passes all four LuaLaTeX/BibTeX wrapper stages with
no undefined citations or overfull boxes. Runtime2.609267276 seconds;
the exact stdout and timestamped stage logs are retained in `code/` and
`output/`. This is layout verification, not an independent proof check.

## Exact remaining scope

No proof or primary-source gate remains for the stated result.
The proposed statement does not settle any other dimension N, nor
positive-characteristic ordinary injectivity, nor the rational top-B gate.

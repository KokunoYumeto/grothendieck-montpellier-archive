# Original-source scope audit: recent four-dimensional pseudo-isotopy papers

Observed source retrieval: 2026-11-19, 20:24--20:31 UTC.
Author: singularities_duality. This is a source audit, not a new comparison theorem.

## Orson--Powell--Randal-Williams

Full current author PDF opened:
https://www.maths.gla.ac.uk/~mpowell/smoothing_pseudo_isotopies.pdf

Web references: `turn842618982view0`; exact Theorem 3.5 and proof
`turn911596248view0`; Lemmas 3.2--3.3 and the addition formula
`turn982794534view3`.

The complete original was downloaded legitimately from the author site:
`logs/orson_powell_randal_williams_current.pdf`, 645,923 bytes,
SHA256 `0000528ebceb135ad9b7300b126e42b78a700bc122dd25c13034dbe7229fd559`.
It has 40 pages. Extracted text is in the adjacent `.txt` file.
Printed pages 9 and 10 were rendered and visually inspected by the author
of this audit in `logs/OPR_printed9.png` and `logs/OPR_printed10.png`.
Pages 7 and 8 have also been rendered, but this audit does not claim they
were visually inspected; their original text was read through the full PDF.

Official Glasgow record independently opened:
https://eprints.gla.ac.uk/397578/ (`turn911596248view1`). It identifies the
paper as accepted by Journal fuer die Reine und Angewandte Mathematik
(Crelle), with acceptance date 31 October 2026. No final volume, pages,
or publication date is supplied. The repository's accepted version is
restricted; the publicly available author PDF above was used, without
attempting to retrieve the restricted copy. The arXiv identifier is
2507.16984. Bibliography should say accepted, not claim a published final
journal version.

Exact scope checked:

* Theorem B, printed p.2, and its full Theorem 3.5, printed p.10, concern
  a TOP pseudo-isotopy whose two endpoint maps are diffeomorphisms.
  Vanishing of its relative Kirby--Siebenmann class is equivalent to an
  isotopy **relative to the entire boundary** to a smooth pseudo-isotopy.
  The proof explicitly uses that the smooth structures agree on both
  four-dimensional boundary components before invoking five-dimensional
  concordance-implies-isotopy.
* Lemma 3.2, pp.7--9, proves additivity of the smoothing obstruction on
  the paper's quotient Q(X). Lemma 3.3, p.9, gives an explicit homotopy
  of pairs from a bottom-fixed cylinder map to the identity. This
  removes the potential cohomology action in the addition formula.
* Section 2, pp.4--6, uses block automorphism spaces and a further
  pseudo-isotopy equivalence in defining Q(X). Its exact sequence is
  not an ordinary-family calculation of pi0 P_TOP(X).
* Theorems A and D concern endpoint diffeomorphisms and whether a smooth
  pseudo-isotopy exists; they do not by themselves classify components
  of the free-top ordinary concordance group.

Small formula correction verified directly from the printed page:
in Theorem 3.5's final implication, p.10, the definition
F'=F composed with (f0 times id)^(-1) has top f1 composed with f0^(-1).
The following sentence prints f1 composed with f0 instead. This is a
missing inverse in that sentence, not a defect in the zero-obstruction
argument. The bottom-fixed case f0=id is unaffected.

Use in the present project: this original supports the importance of
holding the entire boundary fixed. A137 is proved directly for PL
structures using the already opened Kirby--Siebenmann inputs; it does
not extend the smooth statement to a free four-dimensional top or use
an unproved smooth--PL comparison there.

## Galvin--Nonino

Full author original reopened:
https://dapgalvin.github.io/PI_vs_I.pdf (`turn842618982view1`). The local
55-page copy and extraction are `logs/galvin_nonino2025.pdf` and `.txt`.

Theorem 1.1, pp.1--2, supplies necessary TOP Hatcher--Wagoner invariants.
Theorem 1.2, p.2, realizes their possible values for good fundamental
groups. Neither is a completeness theorem in dimension four.

Remark 1.7, printed p.4, explicitly says that the high-dimensional
exact sequence does not hold in TOP dimension four, even for
fundamental group Z. Remark 3.13, printed p.20, separately explains
that elements killed by double suspension have both invariants zero
without necessarily being isotopic to the identity, referring to
Budney--Gabai examples. The definitions in Definition 3.11 and
Lemma 3.12 on that page factor through the actual double-suspension
homomorphism.

Therefore this source does not evaluate the missing kernel in the
general four-dimensional concordance computation, and its necessary
invariants must not be inserted into the full high-dimensional
component exact sequence without a new proof.

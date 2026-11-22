# C.3av: the positive-characteristic low ordinary-restriction interval

Current status: finalized after full independent root and Frobenius
proof/source audits. Frobenius certified at11:12:38UTC; root also
inspected the complete certificate source and exact five matrices.
The final file is `C3_positive_characteristic_low_range.tex`; the
former draft is a comment-only pointer. Canonical statement and original
check events are registered.

## Exact scope and new steps

For every p and r+2<=N<=2r+1, r>=1, the construction gives rational
failure of ordinary J^r surjectivity. The coefficient field is
the algebraic closure of Fpbar(T), with T the specified finite-field
hypersurface. It does not assert rational ordinary nonvanishing over
Fpbar, or failure in N>=2r+2.

The proof adapts C.3ai but replaces its Hodge obstruction by a crystalline
slope-zero obstruction. The degree is d+2 unless p divides d+2, in
which case it is d+3, so the suspended hypersurface is smooth by Euler's
identity and its separated gradient blocks. A monic leading determinant
is proved directly: for degree d+3, the top coefficient of the Hasse
matrix is the identity, because every off-diagonal target monomial has
a negative exponent. Generic ordinarity of arbitrary hypersurfaces is
not assumed.

The curve endpoint d=1 is separately checked: global Witt-coordinate
sections are W_n(F_q), so the preceding connecting map in the Witt
sequence vanishes. Freeness of the full finite Witt modules then follows
from length and Nakayama, in exactly typed semilinear notation.

## Exact source use

All primary files and bibliography entries are those newly opened and
retained for C.3at; see C3at_SOURCE_AUDIT.md and C3at_references.bib.

- Huang--Lian--Yau--Yu2018v1, Section2, Corollary2.3 authorp8 supplies
  the coefficient-matrix convention. The leading identity determinant
  is independently derived, so Corollary2.8 generic invertibility is
  consulted but not required.
- Berthelot--Bloch--Esnault2005 author manuscript, Theorem1.1 and
  smooth proper comparison(1.1) authorpp1--2; exact proper inverse-limit
  clause at the beginning of Section2pp6--7; Witt exact sequence
  Lemma2.5/(2.7)pp9--10. The curve endpoint uses the actual constant
  global sections, not a falsely asserted H^0(O)=0.
- Newly applied exact locator: BBE proof of Corollary1.2, authorp4.
  It explicitly states that smooth affine rigid cohomology agrees with
  Monsky--Washnitzer cohomology and vanishes above dimension, and uses
  rigid Poincare duality to deduce compact-support vanishing below
  dimension. Applying the compact-support localization sequence to
  projective space minus the smooth hypersurface gives the precise
  rational weak-Lefschetz isomorphism used. No integral or small-prime
  weak-Lefschetz assertion is imported.
- Esnault2003 Section2 and deJong1996 Theorem4.1/Remark4.2 supply the
  rational correspondence and source-alteration framework already
  fully audited in C.3at. The lifted source dimension is less than d,
  so its H^d slope-below-one part is zero by Witt cohomological dimension.
- Stacks0FD4 and Kerz7.1/7.5 provide the actual ordinary curve family
  and ambient strict-local Chow vanishing with the exact scopes retained
  in C.3at. C.3e is explicitly all-characteristic and integral.

## Tate shifts and correspondence checks

The incidence correspondence has codimension r=d+s and maps H^d(T)
to H^(d+2s)(V)(s). Its integral transpose left inverse has multiplicity
one because the two root-defined joins meet transversely along T.
A hypothetical hyperplane antecedent has codimension r-1, hence target
H^(d+2s-2)(V)(s-1). For s>=1 the latter is ambient: it is zero in
odd degree, otherwise its sole slope is d/2 after the displayed twist.
For s=0 the twist(-1) makes every slope at least one. Thus it cannot
receive any nonzero slope-zero vector. The constant correspondence and
source-support correspondence are separately killed. No Hodge-type
argument in characteristic p is used.

## Retained computation and layout verification

`code/check_positive_characteristic_low_range.py` and its complete stdout
and JSON retain:

- five exact smooth/nondegenerate-Hasse examples for
  (p,d)=(2,1),(3,1),(2,2),(3,2),(2,3), including cubic finite-field
  extensions in the two characteristic-two cases requiring them;
- 35 exact leading-matrix cases for p=2,3,5,7,11 and d=1,...,7;
- 78 dimension, codimension, transpose and Tate-shift cases with r<=12.

All pass. Runtime15.200971763 seconds. The first exploratory run capped
the coefficient-field search at degree two and correctly exhausted the
characteristic-two Hesse cubic: all nonzero F4 parameters have cube one
and are singular. The successful retained program allows degrees2--4
for its finite sample, finding F8; the universal terminating enumeration
in the proof has no such artificial cap. No false geometric assertion
was inferred from that exploratory exhaustion.

The complete draft passed its four-stage LuaLaTeX/BibTeX wrapper with
zero undefined citations or overfull boxes, runtime2.372249965 seconds.
The exact logs and outputs are retained. This is layout verification,
not a substitute for the completed independent proof/source audits.

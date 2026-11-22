# Independent literal-text audit: Jelonek sign repair and infinite positive subfamily

Observed audit time: 2026-11-20 02:22:51 UTC.
Auditor: singularities_duality.

Candidate: `agents/maximal_locus/notes/jelonek_sign_and_infinite_family_0218.tex`.
SHA256: `0d22222c52ac998bdee2575dd2fcc1dd0c073c8852e717ec4bd0f9b1b2dbc20f`.
The entire actual file was read, including its separate Kwiecinski
paragraph and its explicit exclusion of an A5 counterexample.

**Verdict: full mathematical and stated-source-scope PASS.**
No correction is requested. No finite symbolic certificate is being
treated as the proof of the topological claims.

## Formula and topology audit

* The sign change has the indicated direction: A composed with phi is A,
  B_m composed with phi is B_{-m}, and the target reflection corrects the
  last coordinate. Thus f_m and f_{-m} really are right-left equivalent
  in the source's unrestricted convention. The fixed nonzero radius a
  can be normalized by simultaneous spatial scaling, with the induced
  nonzero diagonal target scaling.

* Properness of each map, and of the parameterized map retaining m,
  follows directly from its last two coordinates and the retained
  parameter. It needs no claim of finite fibres. The top polynomial
  degree is twelve.

* The angular formulas for A, B_m, and their product are correct.
  For m>0, d>1, so the squared continuous factor covers the complete
  interval from zero to (1+d)^2. The lower and upper image-boundary
  sheets have respectively four and two points in every nonzero fibre
  sufficiently near the distinguished value. These cardinalities are
  intrinsic under ambient target homeomorphisms. Interior critical
  values do not affect that characterization because the image boundary
  is required as well.

* The positive-dimensional fibre at the distinguished value is unique
  globally. The cases Y<-1, Y=-1, and Y>-1 with R>0 are separately
  covered. Thus a global equivalence must take that value and its circle
  fibre to their counterparts, and induces one circle homeomorphism on
  the entire limiting relation.

* The closure of pairs over the intrinsically distinguished lower
  sheet has exactly the six stated rotation graphs. Necessity follows
  from the four angular solutions at every nonzero radial parameter;
  sufficiency follows by fixing the direction and letting the radial
  parameter tend to zero. All six angles are distinct for
  0<alpha<pi/2, so these disjoint circles are exactly its connected
  components. The same circle homeomorphism conjugates a chosen
  rotation to one target rotation; it cannot use unrelated maps on the
  two factors.

* The lift proof of rotation-angle invariance is valid for rational as
  well as irrational angles, and for orientation reversal. The integer
  discrepancy is constant by continuity; iteration and boundedness of
  H(t)-epsilon*t give the exact signed angle equality. The interval
  restriction then rules out every target angle except plus or minus
  alpha', and forces m=m'. This repairs the all-real-parameter source
  sentence while retaining an infinite positive-parameter family.

* The Kwiecinski compact restriction is legitimate when the selected
  unit-parameter arc lies in the relative interior of a fixed compact
  semialgebraic neighborhood. It preserves the indicated pointed germs;
  compactness makes the restriction proper. Its infinitely many pointed
  germs have a fibre-dimension jump. Neither example provides the
  unproved assertion about a nondefinable maximal bundle locus or
  constant-fibre failures.

## Primary originals actually opened and read in this audit

1. Z. Jelonek, *The Thom conjecture for proper polynomial mappings*,
   <https://arxiv.org/pdf/1404.7463>.
   The displayed header identifies arXiv:1404.7463v4 (8 February 2015).
   The retrieved PDF also has a later internal date; the audit relies
   on the actual displayed mathematical text, not a publication-date
   inference. Printed page 2 contains the real formula and the literal
   all-distinct-real-parameters assertion. Theorem 3.5, printed page 5,
   and the abstract concern smooth irreducible complex affine varieties.
   They do not imply the corresponding real or definable germ finiteness.
   Retrieval refs: turn161870384view0, turn173806920view1.

2. M. Kwiecinski, *Remarks on the local geometry of analytic maps*,
   RIMS Kokyuroku 1033 (1998), 140--147,
   <https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1033-14.pdf>.
   Read Example 7.1, its precise irrational-angle/equal-or-inverse
   exclusions, Definition 7.2 and Proposition 7.4 on printed page 145,
   and the complete relation calculation and circle argument on page 146.
   These support the final source paragraph exactly.
   Retrieval refs: turn161870384view1, turn173806920view0,
   turn173806920view2.

These were original-text readings. No screenshot viewing or independent
execution of the author's separate symbolic checker is claimed here.

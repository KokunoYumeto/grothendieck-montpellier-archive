# Independent review of endpoint family lifting

**Reviewer:** `/root/cycles`.  **Full proof check completed:** 2026-11-19
16:49:33 UTC, using the tool clock returned immediately after the final
antecedent reads.  This receipt concerns the complete proposed EL.1–EL.5
argument and its stated ordered-tetrahedral application in
`agents/real_weil/C3_endpoint_family_lifting_draft.tex`, read in full.

**Conclusion: PASS in its stated scope.**  The conclusion is an endpoint
lifting theorem for an actual fixed smooth proper parameter curve.  It is
not a theorem algebraizing arbitrary formal vector bundles.  Its
tetrahedral consequence is a restricted example; this receipt does not
assert a universal local Chow theorem or any higher restriction
surjectivity result.

## 1. Exact primary source reread

I freshly opened the complete author PDF of Charles Weibel's *The K-book*,
Chapter II, at
<https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf>.

* Corollary 8.8.2, author p. 83, states the special lambda-ring structure
  and identifies the first two gamma quotients.
* Remark 8.8.5, author p. 83, explicitly states the dimension bound
  `F_gamma^(d+1) K_0(X)=0` for noetherian quasiprojective schemes of
  dimension `d`.  It does not impose regularity.  The remark cites SGA 6,
  VI.6.6, and Fulton–Lang, V.3.10.  I read the actual displayed scope;
  I did not independently open either cited original in this check.
* The flag-bundle splitting principle 8.8.1 on the same page is injective
  on K_0 and applies to the singular projective schemes in this proof.
* Proposition 4.9, author p. 32, gives the Adams action on the gamma
  graded quotients.  I read the statement and proof.

Retrieval references retained in the session are `turn101621020view0`,
`turn800934455view0`, and `turn800934455view1`.  The references are audit
identifiers, not substitutes for the bibliographic source.

I also reread the complete relevant TS.2–TS.4 calculation, all of the TC
raw-Chow draft, and the retained proper-curve field-symbol lemma.  Their
previously certified primary inputs are reused; this receipt does not
claim a fresh opening of Drinfeld, Geisser–Hesselholt, or Quillen.

## 2. Perfect gamma classes on the singular parameter product

The argument stays in vector-bundle/perfect K_0 throughout.  The ample
line bundle gives the resolution property.  The positive-bundle
replacement is valid: from a generating surjection for `V^dual L^m`,
dualization gives an embedding of `V` in a sum of positive lines, whose
quotient is a globally generated bundle tensored with `L^m`.  Products
with first-jet generating sections of `L^m` supply the required jets.

The lambda-ring identity for gamma-two of a difference has the stated
cross terms.  The Hilbert–Burch sequence is locally verified by the
invertible minor and a regular sequence `(a,b)`.  Its perfect class has
degree-two term `gamma^2([A]-rank A)`.  The flag splitting argument
therefore proves the congruence in the gamma filtration without passing
to G_0 or discarding a Cartan-kernel class.

The first-jet incidence argument has the correct dimensions.  On a
smooth stratum of dimension `d`, rank drop has codimension two, and
failure of transversality at this rank has total codimension at least
`d+1`.  Deeper rank drop has codimension six.  The component strata,
double strata, triple strata, and both chosen endpoint fibres give only
finitely many such conditions.  The endpoint curves are finite regular
immersions in `D`.  The full curve need not be flat over every point of
`P`; the proof only requires its two specified endpoint intersections.

## 3. An actual regular hypersurface containing the curve

For a sufficiently high relatively ample twist, the conormal rank-two
bundle on the curve has a section nowhere zero on its reduction.
The rank-two/one-dimensional incidence count is sufficient.  Locally
the resulting equation is a combination of `(a,b)` with a unit
coefficient, so the curve becomes Cartier in the hypersurface `H`.

At a double normal-crossing point, the two original equations have
independent differentials along the double stratum.  Consequently the
chosen nonzero conormal combination has nonzero ambient differential.
The same is true on a component stratum; the curve avoids triple
strata.  Away from the curve the chosen hypersurface is transverse to
all strata.  This proves regularity of its actual lifted ambient
hypersurface `W` along the entire closed fibre.  Excellence and
properness over the local base then give regularity everywhere.

The additional incidence condition excluding a whole component
`E_i x {v}` for every `v` makes the defining equation a fibrewise
nonzerodivisor.  Thus `H` and `W` are flat over `P`.  The argument uses
finite-type strata over `k`; relative Serre vanishing then lifts the
chosen section to the fixed projective scheme `Z x P`.  No moving
henselian parameter neighbourhood is substituted for that fixed product.

## 4. Line-bundle lifting and exact endpoints

The ideal of `H` in `W` is invertible and its restriction is relatively
ample for `H -> P`.  Relative Serre vanishing and the fact that `P` is a
curve give `H^2(H,L^n)=0` for all sufficiently large `n`.  Each of the
finitely many earlier square-zero obstruction groups is killed by `p`.
Raising the current compatible line bundle to the `p`th power before
each such step gives one finite total power and then an infinite
compatible system with no further increase in exponent.

Projective existence algebraizes that system over the completed base.
Algebraizing the inverse and using full faithfulness verifies that the
result is an invertible sheaf.  Popescu descent and henselian lifting
match a single finite quotient containing all of `H`; hence they retain
the entire proper parameter curve, not merely independent endpoint
classes.  Cofinality of the exceptional ideal and the maximal-ideal
adic systems is sufficient here.

All endpoint intersections used in the proof are Tor independent.
The finite endpoint scheme `C_u` is Artinian, so its line bundles are
trivial.  The Cartier geometric-series identity therefore gives the
exact equality

`j_*(1-[O(-p^e C_u)]) = p^e [O_{C_u}]`

in perfect K_0 of the singular divisor.  No pushforward
compatibility of gamma filtrations is needed.  The omitted gamma-three
class restricts to zero on the two-dimensional reduced exceptional
scheme by the exact Weibel dimension theorem.  This proves EL.1.

## 5. Tetrahedral consequence

The rational nilpotent lift from `E x P` to `D x P` has rank zero.
For its integral multiple at an endpoint, square-zero and weight-two
give the stated identity `gamma^2(Na_u)=-Na_u`.  Thus the endpoint theorem
applies without any weight decomposition of the whole group `K_2(P)`.
The already proved point-parameter K_0 isomorphism identifies the lifts
uniquely.  The second Chern-character component of the actual fixed
product family gives an ordinary algebraic-equivalence relation on `Z`.

I reread the proper-curve symbol construction, including characteristic
two, the tame residues, and the zero specialization at `(0,1)`.  Together
with the audited TC quotient by the four exceptional degree coordinates,
it gives the stated vanishing of the rational ordinary top quotient for
this ordered tetrahedral construction.  No extension to all isolated
threefold singularities has been inferred.

## 6. Verification limits

This was a complete mathematical reread and a targeted fresh primary
source audit.  No new finite program was run, and no numerical test is
being used to certify the geometric proof.  The broader main high-degree
restriction-surjectivity gate remains unchanged by this receipt.

# Independent whole-proof audit: nonsplit Gaussian lattice and detector degree

**Reader:** `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not externally exposed. **Run:** HODGE_DIVISION. **Date:** 2026-11-21. Mathematical reading and re-derivation completed by 13:56–14:00 UTC; earlier portions were checked before the final revised read.

**Outcome: PASS** for D-E8-LAT01–02 and HD-E8Q1–6, with the precise input and verification scope below. This is a mathematical whole-proof audit, not a proof-assistant verification. The final two degree-proof clarifications were reread after their insertion; they change no constants.

## Files and scope

- `../g34_eightfolds/e8_grr/nonsplit_lattice_section.tex`: the entire lattice proof, including both directions of denominator clearing and polarization transport.
- `../../research/e8_detector_degree.tex`: the entire numerical bridge, including all supplier cases, incidence components, rational Hodge preimages, correspondence-degree costs, the sixfold map, and fixed-target transport.
- `e8_transfer_diagrams.tex`: authored here and separately reviewed in full by `/root` and `/root/sixfolds`. Both reported PASS after the splitting-field, primitive-projector, and rational-image clarifications. This audit does not count the author's own reading as an independent check of that file.

The Fermat cycle bound, finite E8 group data, analytic/GRR dominance, universal division theorem, and bounded-cycle closedness are separately identified inputs. They are not re-proved by this audit. Their uses and normalization interfaces were checked.

## D-E8-LAT01: quantitative two-sided lattice isometry

The rational classification input is Landherr's published local-global theorem. I read the author's paper, printed pp.246–247: the determinant norm-residue and real-signature invariants, followed by the induction using a common represented nonzero value and orthogonal complements. This supplies rational isometry to two hyperbolic planes plus `diag(1,-3)`. It supplies no quantitative denominator estimate; that estimate is newly proved in the audited text.

Let the integral Gaussian Hermitian lattice have rank six, signature `(3,3)`, signed determinant class three, and determinant absolute value `Delta`. The maximal rational isotropic plane meets the lattice primitively. Since `Z[i]` is a PID, its basis extends to an integral basis. Smith reduction of the pairing block gives the stated matrix with diagonal block `B`, binary residual `A`, `n_B=Nm(det B)`, `d=|det A|`, and `Delta=n_B d`.

I multiplied out the hyperbolic completion and its inverse. Both are cleared by `2 n_B`; bounding heights of a basis change is unnecessary. On the residual anisotropic plane, a primitive vector of least nonzero absolute norm can be made positive by changing the sign of the form. The Gaussian nearest-integer shear gives `|z|^2<=a^2/2`. Minimality gives `|c|>=a`, and the negative determinant forces `c<0`. Hence `a<=sqrt(d)`, `|c|<=d`, and `|Re z|+|Im z|<=sqrt(d)`.

For the five-variable integral quadratic form `Q=A-t^2`, the sum of absolute matrix entries is at most `9d`. Its Witt index is exactly one: a two-dimensional rational isotropic plane would meet `t=0` and make `A` isotropic. It has a rational zero because the classified binary form represents one. The complete small-zero argument was checked rather than attributed to an uninspected bound:

1. Choose a primitive integral zero with least sup norm `M`.
2. With `Q_0=floor(sqrt(3S))+1`, pigeonhole the `Q_0^4+1` fractional multiples of its first four normalized coordinates.
3. If `M>Q_0^4`, obtain `y=(k/M)x+e`, with `0<k<M`, last error coordinate zero, and all other errors smaller than `1/Q_0`.
4. The integral vector `Q(y)x-2B(x,y)y` is isotropic and has sup norm less than `M`.
5. It is nonzero: otherwise proportionality or a rational isotropic plane of dimension two contradicts primitivity or Witt index one.

Therefore `|t|<=11664 d^2`; the original distinguished coordinate `t` is nonzero even if a different coordinate was chosen as the maximal one in the pigeonhole argument. The norm-one vector and its explicitly written orthogonal complement give a determinant-one basis with norms `1,-d`. Since `d/3` is a rational Gaussian norm, all inert-prime valuations of `3d` are even, and an integral Gaussian `beta` of norm `3d` exists. The explicit residual isometry and its inverse are both cleared by `3d|t|`. I checked the integral sign-repair matrix and its determinant one.

Multiplying the two clearing integers gives

`q <= (2 n_B)(3d |t|) <= 69984 Delta^3`.

No hidden coefficient-height bound is used.

## D-E8-LAT02: actual source and target lattices

For two lattices, the product of their clearing integers gives both inclusions with

`N <= 69984^2 (Delta_source Delta_target)^3`.

I checked the Hermitian form convention `h(x,y)=E(x,iy)+iE(x,y)`, conjugate-linearity in the first argument, integrality over `Z[i]`, and `det E=(det h)^2`. The central Gaussian scalar in the actual E8 group ensures that the primitive abelian source lattice is stable under the maximal order.

The self-adjoint primitive projector has denominator dividing `M=2|G|`. If `Lambda_S=pV intersect Lambda`, unimodularity of the original Jacobian lattice and extension of integral functionals show `Lambda_S^#=p Lambda`. Thus `M Lambda_S^#` is contained in `Lambda_S`. Each of the six Hermitian elementary divisors divides `M`, giving `Delta_source<=M^6`.

The rational isometry followed by multiplication by `N` is an actual isogeny on the marked abelian families and pulls the target polarization back to `N^2` times the source polarization. The three-cycle degree cost is exactly `N^6`, and a nonzero Weil component stays nonzero. For an order of conductor `f`, the stable lattice `f Z[i] Lambda` has index at most `f^12`; the final identity isogeny uses the exact pulled-back polarization, introducing no further cycle-degree cost. This verifies the factor `f^216` in the eventual detector bound.

## HD-E8Q1–3: constants, full Brauer identity, and return graphs

The constants were independently recomputed symbolically from their defining inequalities:

`G=1393459200`, `g=1+53G/24=3077222401`, `M=2G`,

`R=(2G+1)G!G^G`, `L=2gR`,

`A=(4L)! [1000g(G+1)(L+1)]^(4L)`,

`B=(4L+4) A^(2L+4)`,

`S=[26(L+1)]^L H_12(L)`.

The bounded Brauer module identity uses the integer column-lattice argument on *all irreducible representation multiplicity rows*. It does not infer a module identity from the determinant-character statement printed in SQ3. The complete minor/Cayley-graph/Cramer argument yields coefficient mass at most `(G+1)G!G^G`, safely bounded by `R`. Taking actual multiplicity spaces gives the even slot number `l=6+2 dim M_-<=L`.

For each nontrivial cyclic supplier, `v=2b-2+r`, the bundle supplier dimension is at most `v`, and all quotient inertia orders divide twelve. I checked separately `r>=3`, `r=2`, and `r=0`, with zero-dimensional multiplicity omitted. For the projective-bundle convention of lines, `H=xi+x` is very ample because its section bundle is `O(1)^b direct-sum O(13)`. Nonzero fibre coordinates permit separation of base tangent vectors; fibre sections separate fibre tangent vectors. Both `xi` and `x` are globally generated and nef.

The universal zero divisor on the smooth quotient curve is finite flat of constant degree. Its pullback to `C` and the independent coordinate fibre products are finite flat too. This remains true at repeated zeros. To identify the actual return correspondence with an incidence component, the revised proof uses basepoint-freeness of `K(D)` (degree at least `2b`) or of the canonical system for `b>=2`. General divisors are reduced and avoid the finite quotient branch locus. The supplier map is dominant. Over this dense open, distinct projected zeros and a fixed residual cyclic label select an open-and-closed subcover of a finite etale incidence cover. A closure of an appropriate component therefore has degree at most the complete incidence. This avoids assigning an unspecified resolution a degree.

I checked the pushforward identity `pi_* xi^(b+k)=12^k x^k`, the volume bound `12*13^d`, all product factorials, and the numerical majorization of incidence equations. All lie below `A`. Trivial-character determinants are correctly treated as external Tate cycles `(C x_{C/H} C)^b` of degree at most `b!(12gG)^b`, not as finite graphs over a point. Their input-degree and correspondence-dimension shifts agree with the return maps.

## HD-E8Q4: effective generators and rational Hodge preimages

The bundle basis `xi^j pi^*W`, `j<=b`, is realized by flat pullback followed by generic globally generated divisors. After expanding the total polarization and pushing to the Fermat base, every surviving excess `xi` power contributes a factor twelve; the sum of nonnegative coefficients is at most `(13k)^d`. Every remaining nef base monomial is bounded by the degree for the sum polarization. This proves the generous uniform bound `S` without an omitted weak-composition factor.

The revised descent argument correctly uses a finite Galois coefficient field containing *all* `G`-th roots of unity. It expands all coefficient-field maps into rational algebraic correspondence terms and takes the **sum of their rational images**, equivalently the image of their direct sum. It does not sum the maps in a way that could cancel. This rational Hodge substructure contains the natural determinant line after field extension, hence its conjugate and the rational Weil plane. Polarizable-Hodge semisimplicity then supplies a rational Hodge preimage. The effective generators span the complete source Hodge space, so some finite linear combination has nonzero final Weil component. No unbalanced individual cyclic determinant is declared rational Hodge.

## HD-E8Q5–6: correspondence operations, last map, and target bound

The published moving lemma is used with a deliberately enlarged bound `2(m+1) deg(V)^(m+1)`. Its hypotheses and dimension range were checked. I read the full used proof of Truong's Lemma 2.2 in the author text, p.13. Cross product, moving intersection, and projection give individual effective pieces of degree at most `2(2L+1) A^(2L+3) E<=B E`.

There are precisely four charged operations. The group-algebra module maps become products of `k+6` deck graphs with degree `(k+6)!(12g)^(k+6)`, where `k=(l-6)/2`. Character projectors, matrix units, permutations, and duality contractions are included in these graphs. No uncontrolled arbitrary endomorphism of a multiplicity Hodge structure is inserted. At each operation the individual positive and negative moving parts are retained. Taking their rational span preserves the needed final nonzero projection, regardless of whether an individual term lies in an intermediate projector image. Thus one integral effective component works, with degree at most `B^4 S<=B^(4L+21) S`.

For the final sixfold map, `f=Mp` is integral and `f^* theta_B<=M^2 Theta_J`. Cauchy's inequality for addition of six vectors, together with Abel theta degree `g` and `deg H_C=6g`, gives `a_6^*theta_B<=M^2 H_{C^6}`. The determinant pullback pairs nontrivially with the retained alternating tensor. Projection formula therefore proves nonzero final Weil projection; component selection is performed after this fixed last map. The three-cycle degree cost is `M^6`.

Actual rank-nine dominance comes from the separately proved analytic or GRR family, not merely from a branch-count dimension. The source volume bound and lattice isogeny give

`D_3(Delta)=69984^12 M^114 Delta^18 B^(4L+21) S`.

The accepted bounded-cycle closedness and fixed-data spreading input is used exactly at the final extension from an analytic open to the full connected target family. Conductors replace `Delta` by `f^12 Delta`. Applying the separately checked universal-division theorem with `a=f(2+i)` gives factor `(5f^2)^24`, total conductor exponent `480`, and polarization-volume exponent `36`. These exponents and the coefficient `5462` check.

## Primary-source log for this audit

- W. Landherr, “Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper,” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* 11 (1935), 245–248, doi:10.1007/BF02940728. Original PDF: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf . Full used classification argument, printed pp.246–247, read. Local source SHA-256: `ccfaea6449b2d70fd3093551694bc7062548e88bc330ec8ef476612fdb34050f`.
- T. T. Truong, “Relative dynamical degrees of correspondences over a field of arbitrary characteristic,” *Journal für die reine und angewandte Mathematik* 758 (2020), 139–182, doi:10.1515/crelle-2017-0052. Author PDF: https://arxiv.org/pdf/1605.05049 . Lemma 2.2 and its full used degree proof, author p.13, read.
- Supplied `RETURN_HECKE_DIV_final_20261121T0204Z/HECKE_DIV.tex`, SQ3 proof, especially the integer column-lattice lemma. Entire used proof was read; the extension from determinant-character rows to all irreducible multiplicity rows is explicitly reproved in D-E8-XFER01.

No fresh numerical certificate is asserted for these symbolic inequalities. File hashes and actual audit events are recorded separately.

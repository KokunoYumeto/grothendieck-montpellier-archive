# A092. Complete audit of the stable second-row-two formula

**Result: PASS.** The complete G038 proof, SR2.1–SR2.17 and
all eight sections, the whole positive evaluator, its check
program and saved check receipt were read. The actual
quadratic polarization map and both exceptional module
splittings prove the claimed positivity. A separate exact
polarization and numerator reconstruction was executed.

Reviewed files are work/root/stable_second_row_report.md,
work/root/stable_second_row_positive.py,
work/root/check_stable_second_row_positive.py, and
work/root/STABLE_SECOND_ROW_POSITIVE_RECEIPT.json.

## 1. Original partitions and the exact stable transport

For $m\ge3$, $a\ge2$, $t\ge0$, and $n\ge a+t$, the output
$$
\lambda=(mn-a-2-(m-1)t,a+t,t+2,t^{m-3})
$$
has size $mn$. Its first gap is
$m(n-t)-2a-2\ge(m-2)a-2\ge a-2$; its second gap is $a-2$.
Thus every declared tuple is a partition. The stable chart
condition is exactly $\lambda_2\le n$.

The T032/G015 chart sends the balanced module to the full
Schur module of tail $(a+t,t+2,t^{m-3})$ on
$W=\mathfrak h_m$. Removing $t$ full determinant columns
gives $S_{(a,2)}W$ and the actual character
$\operatorname{sgn}^t$. This proves the stated effective
outer label and uses the already specified chart inverse
and exterior-column pairing. The remaining calculation is
on this exact Schur module, not merely its dimension.

## 2. The complete polarization kernel and cokernel

With tensor degrees two and one respectively, the map
$$
\phi:P\otimes\operatorname{Sym}^2W\longrightarrow P\otimes W,
\qquad
f\otimes uv\longmapsto fu\otimes v+fv\otimes u
$$
is $P$-linear, homogeneous and $GL(W)$-equivariant.
Its factors of two at repeated vectors are retained.

For total degree $D\ge4$, Pieri gives exactly the three
domain summands $(D)$, $(D-1,1)$, $(D-2,2)$ and the first
two target summands. The three displayed highest vectors
were checked with the literal raising derivation $y\mapsto x$.
The first has nonzero image $2x^{D-1}\otimes x$.
The second has nonzero image
$x^{D-1}\otimes y-x^{D-2}y\otimes x$.
The three terms in the third image cancel exactly, with
the stated coefficient minus two. Its weight is $(D-2,2)$.
The Young inclusions and semisimplicity therefore identify
the actual kernel with $S_{(D-2,2)}W$.

At degree three, the first two summands are still present
once each and their same nonzero images prove surjectivity.
At degree two, the map is the symmetric inclusion into
$W\otimes W$, so its cokernel is $\Lambda^2W$.
At degree one its cokernel is $W$. No other degree occurs.
These arguments include $\dim W=2$; every displayed
highest vector exists, and irrelevant Schur summands
vanish through their column antisymmetrizers.

As $I=\mathbb Q[e_2,\ldots,e_m]$ has no positive element
below degree two, its positive ideal kills the whole
cokernel. Under the actual exterior-hook maps the two
cokernel representations are the distinct Specht labels
$(m-1,1)$ in degree one and $(m-2,1,1)$ in degree two.
For $m=3$ these are the standard and sign representations,
so the smallest outer degree has exactly the stated
exceptional labels.

## 3. Freeness outside the exceptional labels

The invariant averaged coinvariant section gives the
graded multiplication isomorphism $I\otimes H\to P$.
Consequently the covariants of both free $P$-modules are
finite graded free $I$-modules. Their homogeneous basis
polynomials are precisely
$A_\nu=q^2f_{[\nu]\otimes\operatorname{Sym}^2W}$ and
$B_\nu=qf_{[\nu]\otimes W}$. The rational invariant perfect
Specht forms justify the tensor multiplicity notation.

Away from the two cokernel labels, the covariant map is
surjective by the exact rational averaging functor.
Choosing a homogeneous lift of every free target basis
element gives an actual graded $I$-linear section.
The kernel is therefore graded projective.

The stated freeness proof is valid without an unstated
projective-module theorem. Lift a homogeneous basis modulo
$I_+$, map the corresponding graded free module onto the
kernel, and use graded Nakayama for surjectivity.
Graded projectivity splits this surjection. After reduction
modulo $I_+$ its kernel is zero; another graded Nakayama
application gives zero kernel. All modules are finite and
bounded below, so both applications have their required
hypotheses. This supplies the actual free basis and proves
coefficientwise nonnegativity of $A_\nu-B_\nu$.

## 4. The exceptional decomposition, checked as actual modules

Fix an exceptional label and its degree $d=1$ or $2$.
Its cokernel is the single graded residue field $(I/I_+)[d]$.
A homogeneous free basis of $\mathcal B_\nu$ can be adapted
to the quotient: one degree-$d$ vector $e_0$ maps to one and
the others map to zero. Reduction of basis vectors in that
degree is ordinary rational row reduction. The image is
therefore exactly
$$
I_+e_0\oplus\mathcal B'.
$$
Lift the free basis of $\mathcal B'$ through the actual
surjection onto this image and split it off. The remaining
graded projective domain is free by the preceding argument
and maps onto $I_+e_0$.

Choose $x_i$ mapping to $e_ie_0$, in degree $d+i$.
Their residue classes are linearly independent in
$\mathcal A_0/I_+\mathcal A_0$, because their images in
$I_+/I_+^2$ are its independent minimal generators.
The map on these quotients is onto. Choose a homogeneous
complementary residue basis in its kernel and lift it to
vectors $y_j$. The $x_i,y_j$ form a free homogeneous basis
by the same graded Nakayama and projective splitting argument.

Each image of $y_j$ is in $I_+^2e_0$ and can be written
$\sum_i g_{ji}e_ie_0$ with homogeneous $g_{ji}\in I_+$.
The basis change
$y_j\mapsto y_j-\sum_i g_{ji}x_i$ fixes all $x_i$ and is
invertible triangular over $I$. It makes those images
zero. The exact kernel thus becomes
$$
K_\nu\simeq\mathcal F_\nu\oplus Z_1(I)[d],
\qquad
Z_1(I)=\ker\left(\bigoplus_{i=2}^m I\xi_i
\xrightarrow{\xi_i\mapsto e_i}I\right).
$$
This decomposition is on the specified polarization kernel.

The intermediate free domain has basis polynomial
$A_\nu-B_\nu+q^d$. Removing the $x_i$ gives
$$
F_\nu=A_\nu-B_\nu+q^d\left(1-\sum_{i=2}^m q^i\right),
$$
exactly SR2.3. It is the basis polynomial of the remaining
free span, so its coefficients are nonnegative.
Their degrees are at most $N+2$ with $N=\binom m2$:
coinvariant degrees are at most $N$, and the correction
degrees $d+i$ also obey the bound because $m\le N$.

As a check on the signs, the Hilbert numerator of $Z_1(I)$
is $\sum_iq^i-1+\prod_i(1-q^i)$. Adding its shifted
numerator to $F_\nu$ gives
$A_\nu-B_\nu+q^d\prod_i(1-q^i)$, precisely the kernel
Hilbert series obtained from the actual residue-field
cokernel. This is a consequence of the decomposition,
not a substitute for its basis construction.

## 5. The actual weighted cycle basis and positive polytopes

For a fixed monomial multidegree $\beta$, let
$J=\{i:\beta_i>0\}$ and $i=\min J$.
The degree-$\beta$ domain basis is
$e^\beta\xi_j/e_j$ for $j\in J$, all mapping to
$e^\beta$. Its kernel basis consists exactly of the
differences with the distinguished index $i$:
$$
e^\beta(\xi_k/e_k-\xi_i/e_i),\qquad k\in J\setminus\{i\}.
$$
Both quotients are polynomial. This proves the claimed
series by an explicit basis, with no unproved cancellation:
$$
\sum_{2\le i<k\le m}
\frac{q^{i+k}}{\prod_{l=i}^m(1-q^l)}.
$$

Each positive coefficient $c_{\nu,j}$ of the free polynomial
is encoded by one bounded coordinate from zero to
$c_{\nu,j}-1$, together with the invariant monomial exponents
satisfying $\sum ib_i=D-j$. Fixing the homogeneous basis
described above makes this an actual indexing of its vectors.
The matrices need only the integer basis counts, not
construction of every vector.

The exceptional cycle uses G037's single trivial-hook
polytope at total degree $D-d$, with hook parameter
$D-d-1\ge1$. This includes $m=3$, where the cycle is a
free generator of degree five and degree six is absent.
For $m\ge4$, its support is every degree at least five.
The free coin support is exactly degree zero or degree at
least two, since sizes two and three are available.
These give the stated complete support test, including
small $a$ and all exceptional endpoints.

There are at most $N+3$ free-degree pieces and one cycle
piece. Each free piece has $m$ variables, and the cycle
piece has $3m-3$. All upper bounds and degree equations
are literal bounded integer constraints. The positive
coefficient and support formulas follow from the actual
free/cycle basis decomposition.

## 6. Corner paths, pair module, and polynomial bounds

The ordinary tensor-coset isomorphism
$v\otimes gH\mapsto g\otimes g^{-1}v$ and its displayed
inverse prove the remove-one/add-one rule for
$[\nu]\otimes(\mathbf1\oplus W)$. Subtracting its actual
trivial direct summand gives the standard tensor rule.

The unordered-pair map
$$
\{i,j\}\longmapsto(P_me_i)(P_me_j)
$$
is equivariant and bijective. Indeed a putative kernel
gives a quadratic $\sum_{i<j}a_{ij}x_ix_j$ vanishing on
$\sum x_i=0$. Divisibility by that defining linear
polynomial gives $(\sum x_i)(\sum b_ix_i)$; the absent
square coefficients force every $b_i=0$. The dimensions
on both sides are $\binom m2$, proving the actual
isomorphism over $\mathbb Q$.

The pair stabilizer is $S_{m-2}\times S_2$. Restriction
followed by induction and the two Pieri rules give exactly
the remove-two/add-two formula of SR2.15. Horizontal and
vertical branches are counted separately when both occur;
different corner orders leading to the same strip are not
double counted. The code's sets of intermediate and upper
shapes, followed by its two independent strip tests,
implement precisely this convention.

Only polynomially many candidate corner paths are used.
The already proved fake-degree formula is truncated through
degree $N$, giving its entire polynomial. Its coefficient
bound by $m!$, multiplied by the polynomial path counts,
has $O(m\log m)$ bit length. The resulting nonnegative
free numerator has degree at most $N+2$.

The coefficient evaluator applies the previously proved
binary-degree rational-series extraction to this numerator
over $\prod_{i=2}^m(1-q^i)$ and adds the shifted cycle.
Both degrees are $O(m^2)$ and the same established
root-of-unity denominator bit bound applies.
The code retains the full numerator, validates the
physical inputs, and uses the correct determinant parity.
The stated explicit-$m$ encoding convention is appropriate.

## 7. Independent executed checks

The fresh implementation
work/archive/check_stable_second_row_independent.py
and receipt
work/archive/STABLE_SECOND_ROW_INDEPENDENT_RECEIPT.json
record two distinct comparisons.

First, the actual polarization matrix was rebuilt in each
polynomial multidegree. For a multidegree $\beta$, its target
rows are the indices in the support of $\beta$. A mixed
pair contributes the literal column with two entries one;
a repeated index with exponent at least two contributes
the literal single entry two. Exact rational column
elimination checks the map, including its normalization.
All 45 cases $\dim W=2,\ldots,6$, $D=1,\ldots,9$ pass,
covering 7,992 such multidegree blocks. The kernel dimensions
match the hook-content dimensions of $S_{(D-2,2)}W$,
and the only cokernel dimensions are $\dim W$ in degree
one and $\binom{\dim W}2$ in degree two.

Second, all 41 free numerators for partitions of
$m=3,\ldots,7$ were rebuilt independently. Fake degrees
were obtained by removable-corner standard tableaux and
their literal comajor statistics, covering 348 tableaux.
Symmetric-group characters were constructed from
Jacobi–Trudi and fixed ordered set partitions: each
permutation cycle is assigned to one block of its required
size. This uses no Murnaghan–Nakayama implementation.
The standard trace is the number of fixed letters minus
one; the unordered-pair trace is the number of pairs of
fixed letters plus the number of two-cycles.
Literal rational tensor-character averages then give
the numerator. All coefficients and exceptional shifts
agree with the positive evaluator.
Character dimensions, norms and 194 cross-row
orthogonality checks also pass.

The comparison imports the positive evaluator only as
the target under verification. It imports neither the
root's cycle/MN checker nor its hook-quotient computation.
The author's separate 2,160 module/support checks,
90 original plethysms, 182 polytope cases and 1,636
witnesses were read as a saved receipt and were not
claimed as independently rerun here.

## 8. Geometry and final scope

The balanced flag comparison supplies the original
Schur representation. The polarization, its image,
its free summands and its weighted cycle define
actual equivariant modules and coherent sheaves on
$\operatorname{Spec}I$. Their displayed sections,
basis changes and presentations give the asserted
transport through the established SGA3, SGA6 and EGA
dictionary. All maps are rational and spread after
inverting their finite denominators; the multiplicity
theorem concerns the characteristic-zero fiber.

The entire G038 proof and implementation pass in their
stated varying-outer-degree stable range. No unresolved
kernel-rank or numerator-positivity assumption remains.

# A090. Complete review of the first unstable hook order

**Result: PASS.** The whole T061 report, UH.1–UH.10 and all six
sections, the positive evaluator, and the author's verification program
were read. The actual evaluation maps, their endpoint behavior, and
the explicitly deleted lattice point all give the asserted formula.
This review includes a fresh independent exact matrix and lattice
calculation; it does not claim execution of the author's cycle sweep.

Reviewed files are
work/theta/unstable_hook/first_unstable_hook_report.md,
work/theta/unstable_hook/first_unstable_hook_positive.py, and
work/theta/unstable_hook/check_first_unstable_hook.py.
The retained G015 full flag model was also reread at the comparison
used here. All statements are over the rational characteristic-zero
fiber, with the actual permutation actions retained.

## 1. The section model, line factors, and evaluation

Write $E=\mathfrak h_m$, $d=m-1$, and
$v_i=e_i-m^{-1}\mathbf 1$. The original partition and balanced degree are
$$
\lambda=((m-1)a+t-m-r,a+t,(t+1)^r,t^{m-2-r}),
\qquad n=a+t-1.
$$
Their sum is $mn$, their first gap is $(m-2)a-m-r$, and the ideal
order in G015 is exactly $\lambda_2-n=1$.
After removing the full determinant factor, the smaller flag weight is
$(a,1^r,0^{d-r-1})$. For $r>0$ its line is
$$
(\mathcal S_1^*)^{a-1}\otimes\det\mathcal S_{r+1}^*.
$$
On the flag fiber over a line, the factor
$\det\mathcal S_{r+1}^*$ splits into $\mathcal S_1^*$ and the
exterior Young line for the quotient. Its degree-zero pushforward
is therefore $\mathcal O(a)\Lambda^rQ^*$. For $r=0$ this is simply
$\mathcal O(a)$.

The determinant factor is $\det(E^*)^t=\operatorname{sgn}^t$.
It has not acquired an extra sign from the quotient exterior factor.
Locally trivializing the quotient bundle makes the remaining flag
calculation a product over the base. Its Čech vector-space complex
over $\mathbb Q$ stays exact after tensoring with the base ideal
module. This proves the stated degree-zero pushforward with
$\mathcal I_Z$, without asserting that this ideal is a flat module.
The comparisons glue through the actual Young/Plücker maps.

Since $Q^*=\Omega^1(1)$, the section module before imposing the
point ideal is the Koszul kernel
$$
H^0(\mathcal O(a)\Lambda^rQ^*)
=H^0(\Omega^r(a+r))
\simeq S_{(a,1^r)}E^*.
$$
Here the Euler contraction is the multiplication differential used
in G037. Its coefficient degree is $a$ and its total Koszul degree
is $a+r$. Evaluation at the specified affine representatives is
the actual map
$$
F\longmapsto (F(v_i))_i:
S_{(a,1^r)}E^*\longrightarrow
\bigoplus_i\Lambda^r\operatorname{ann}(v_i).
$$
The horizontal equation puts the values in the indicated
annihilators. The vectors $v_i$ are literally permuted, so these
fiber trivializations introduce no scalar character.

The sum of fibers is the induced representation
$\operatorname{Ind}_{S_{m-1}}^{S_m}\Lambda^r\mathfrak h_{m-1}$.
An explicit coset comparison sends $g\otimes\phi$ to $g\phi$ in
the component indexed by $g(m)$. The stabilizer identification is
the zero-sum subspace of the first $m-1$ coordinates in
$\operatorname{ann}(v_m)$, using the invariant dot form.
Choosing the transpositions $(i\,m)$ gives an inverse coset
description. Thus the kernel of the displayed map is precisely
the G015 vanishing section space, with its full outside sign
$\operatorname{sgn}^t$.

## 2. Both actual evaluation splittings

The degree-$a\ge3$ right inverse in UH.8 checks directly.
At every frame point,
$s_2(v_j)=(m-1)/m$,
$z_i(v_i)=(m-1)/m$, and
$z_i(v_j)=-1/m$ for $i\ne j$. Substitution in UH.7 gives
$p_i(v_j)=\delta_{ij}$ and $\ell_i(v_i)=1$.
For $\phi_i\in\Lambda^r\operatorname{ann}(v_i)$,
$$
p_i\ell_i^{a-3}\iota_z(\ell_i\wedge\phi_i)
$$
has coefficient degree $a$, is horizontal because
$\iota_z^2=0$, and takes the prescribed value $\phi_i$ only at
$v_i$. The identity at that point is
$$
\iota_{v_i}(\ell_i\wedge\phi_i)
=\ell_i(v_i)\phi_i-\ell_i\wedge\iota_{v_i}\phi_i
=\phi_i.
$$
Every factor is permuted by the group, so summing these maps gives
an equivariant rational right inverse.

At $a=2$, the adjoint of
$l\otimes\theta\mapsto(l(v_i)\iota_{v_i}\theta)_i$
is exactly
$$
(\psi_i)_i\longmapsto
\sum_i v_i\otimes(v_i\wedge\psi_i),
\qquad
\psi_i\in\Lambda^r(E/\mathbb Qv_i).
$$
The map from each quotient exterior power to
$v_i\wedge\Lambda^rE$ is well defined and injective.
The only relation among the $v_i$ is their constant relation.
Consequently a vector in the adjoint kernel has
$v_i\wedge\psi_i=\eta$ independent of $i$.
Choosing $d$ frame vectors as a basis shows that an element of
every corresponding principal exterior ideal must contain every
basis vector. The intersection is zero for $r+1<d$.

It follows that evaluation is surjective for $r\le m-3$.
Every declared degree-two input has $r\le m-4$ by the first-gap
inequality. At the excluded endpoint $r=m-2$, the common
intersection is exactly $\det E$, so the cokernel is the
one-dimensional sign representation. This endpoint statement
also retains the actual group action on the common wedge.

The invariant positive forms and the displayed adjoint give the
rational splitting $B^*(BB^*)^{-1}$ followed by
$l\otimes\theta\mapsto l\iota_z\theta$. Surjectivity makes this
inverse well defined. No numerical-rank hypothesis enters the proof.

## 3. The correction types and the degree-two kernel

The hook identification
$\Lambda^r\mathfrak h_{m-1}\simeq[(m-1-r,1^r)]$
agrees with the standard alternating difference-vector Young map.
Its characteristic can also be checked from the actual splitting
$\mathbb Q^{m-1}=\mathbb Q\oplus\mathfrak h_{m-1}$:
the exterior power of the permutation module is the induced
sign/trivial tensor, and the resulting recurrence is the hook
Jacobi–Trudi recurrence.

Inducing this hook one further letter adds a single box.
With $q=m-1-r$, its possible shapes are exactly
$$
(q+1,1^r),\qquad(q,1^{r+1}),\qquad
(q,2,1^{r-1})\quad(r\ge1,\ q\ge2).
$$
They are distinct, including $r=0$ and $q=1$.
The coset module followed by rational Young projections supplies
the actual summands. Since the evaluation map splits, the kernel
multiplicity is the stable-hook multiplicity minus one exactly
for these labels. The original outer label changes to its
transpose exactly when $t$ is odd.

For $a=2$, removing the same determinant columns changes the
inner degree from $t+1$ to one and the nonzero output shape to
$(m-r-2,2,1^r)$. Its first part is at least two precisely in the
valid range $r\le m-4$. The tensor-word and Young maps for
$S_\nu(\operatorname{Sym}^1V)=S_\nu V$ give the claimed
single Specht kernel, including its actual inclusion obtained
from the evaluation splitting. This also explains the
zero-dimensional positive polytope at that endpoint.

The primary Macdonald passages were read in the retained
Macdonald.pdf/Macdonald.txt: Chapter I §5 (5.12)–(5.17),
printed pp.73–74, including the complete displayed derivation
of Pieri and its direct alternating proof; and Chapter I §7
(7.1)–(7.5), printed pp.112–114, including the proof that the
characteristic map carries the induction product to symmetric
function multiplication. The public primary copy used in this
project is https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf.
The precise one-box use is (5.16) with strip size one.

## 4. The removed point, including all special cases

For every non-row correction shape, the row-superstandard
tableau has comajor degree $b(\nu)$. This follows by summing
$m-j$ over the successive row-ending labels. Choosing the
$r$ least retained weights $j-i+1$, after deleting cells
$(1,1)$ and $(2,1)$, gives minima $r+2,r+1,r+2$ for the
three correction shapes respectively. In the first case the
row shape at $r=0$ is handled by the separate invariant formula.

For $a\ge3$, the remainder $D-L$ is at least one. It equals
one only for $a=3$ and a correction shape with $L=r+2$.
Every other remainder is at least two and is represented by
one coin three when odd and otherwise by coins two.

Each of the four exceptional numerator modifications in §4
was checked:

- For $(q+1,1^r)$, swapping the last first-row entry with
  the second-row entry moves its descent from $q+1$ to $q$.
  All other descents stay in place, and the tableau is standard
  even when $q=1$.
- For $(q,2,1^{r-1})$ with $r\ge2$, swapping cells
  $(2,2)$ and $(3,1)$ moves the relevant descent from
  $q+2$ to $q+1$. The column and row inequalities remain strict.
- For $(q,2)$ with $q\ge3$, the specified two rows have their
  sole descent at $q-1$, replacing the row-superstandard
  descent at $q$. They contain each label once and are standard.
- For $(2,2)$, replacing the retained selected cell $(2,2)$
  by $(1,2)$ changes its weight from one to two.

Thus each special construction raises the numerator degree by
exactly one. This includes the full retained-subset endpoint
$r=m-2$ and the sign shape in the second correction family.

For the row shape, $r=0$ and $D=a\ge3$. The chosen two/three
coin exponents are nonzero somewhere. Marking their least
positive index gives the unique support bit required by
G037's invariant polytope; no subset bit is selected.
Every coordinate of the point is specified, and its encoding
requires only polynomially many bits.

## 5. Actual positive pieces, code, and bounds

The two pieces for coordinate $j$ impose equality with the
specified point on all earlier coordinates and strict integer
inequality on coordinate $j$, written as an offset of one.
Their tag is therefore exactly the first differing coordinate
and its direction. Every other integer point has one tag and
the removed point has none. All pieces are bounded because
they retain every inequality of the original bounded polytope.
This proves the positive count for the split evaluation kernel.

The code follows this construction literally. It validates
the partition gap, computes the parity label, treats every
valid degree-two case directly, and otherwise obtains the
stable polytope and appends the prefix and differing-coordinate
constraints. The canonical-point function fixes all assignment,
descent, subset and coin variables. Its special tableau branches
agree with the four cases checked above.

The stable polytope has at most $N=m^2+3m-4$ variables.
There are at most $2N$ pieces, all with the same variable list.
Adding the prefix rows increases the output by a polynomial
factor only. The coefficient uses G037's binary-degree evaluator
and removes a known zero or one. Positivity and exact support
follow from the split evaluation map and the specified deleted
point, so no input-sized matrix inverse is part of the evaluator.
The explicit/unary-$m$ convention at $t=0$ and the ordinary
binary-part bound at $t\ge1$ are stated correctly.

## 6. Fresh independent executions and exact scope

The program
work/archive/check_first_unstable_hook_independent.py
and receipt
work/archive/FIRST_UNSTABLE_HOOK_INDEPENDENT_RECEIPT.json
record the following completed checks.

The adjoint was rebuilt in the frame
$e_1,\ldots,e_{m-1},-\sum e_i$ and reduced by exact rational
column elimination. This checks the actual exterior map,
without invoking the correction-label formula.
All 25 pairs $m=4,\ldots,8$, $r=0,\ldots,m-2$ have the
proved rank. The five excluded top cases have cokernel dimension
one. All 15 valid degree-two kernel dimensions match the
hook-length dimension of $(m-r-2,2,1^r)$.

An independent removable-corner tableau recursion, direct
retained-cell subsets and complete coin enumeration checked
120 deleted-point cases at $m=4,5,6$, $a=3,4,5,6$.
The exported formula contained 8,832 piece matrices. There were
549 original lattice points, exactly 120 specified removed
points, and 429 retained points. Every retained point satisfies
its literal exported first-difference matrix; for the 46
nonremoved $m=4$ points, membership in every piece was checked
and was exactly one. Another 81 literal removed points covered
large binary degree $10^{40}+1$ and extreme hook legs.

The source implementation was imported only as the evaluator
and exporter under test. The adjoint matrices, rank elimination,
tableau recursion, coin enumeration, and inequality checker
were independently written. The author's original cycle and
plethysm comparison sweep was read but was not rerun here.

## 7. Geometric transport and final audit status

All section, restriction, Euler and quotient comparisons used
above are actual equivariant maps on the stated flag/projective
schemes. Their rational splittings give finite-group module
splittings and hence the same covariant classes in the
already verified Schur/K0 dictionary. A finite collection of
coefficients and minors has only finitely many denominators,
so those maps spread after inverting their denominators; the
claimed multiplicities remain characteristic-zero statements.

Every allowed parameter is covered: $a=1$ violates the first
gap, $a=2$ is exactly the range $r\le m-4$, and $a\ge3$ allows
all $0\le r\le m-2$. The evaluation-surjectivity proof, actual
kernel decomposition, point-removal construction and exported
positive formula have no remaining mathematical gate in T061.

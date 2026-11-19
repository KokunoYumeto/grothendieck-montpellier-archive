# Audit of the all-genus single-line invariant reduction

2026-11-19. Agent: period_generation. This note proves the reduction
maps below. It does **not** assert the still pending all-genus tangent
vanishing or certify the proposed finite matrix.

## IR-1. The actual invariant projection

Let k=Q_l, let V=ka+kb+W be an orthogonal symplectic decomposition,
with <a,b>=1, and let h_6(V) be the degree-six special derivations.
Retain the actual Sp(V)-stable universal arithmetic subspace U and
the actual one-dimensional quotient q:U->Q of Nakamura, as established
through the strict geometric/arithmetic maps in F.3.24 and F.3.26.
The restriction of Q to Sp(V) is trivial: its GSp character is the
cube of the similitude multiplier.

Put S=Sp(W) x G_m, with t acting by a->ta, b->t^-1 b and fixing W.
This is an actual subgroup of Sp(V). Let

    P_a={D in h_6(V): D(a) in [L_6(V),a]}.

The subspace P_a is S-stable. For s(a)=t a and D(a)=[A,a],

    (s D s^-1)(a)=t^-1 s[A,a]=[sA,a].

The actual U is S-stable as the restriction of its Sp action. Since
S is reductive in characteristic zero, its finite-dimensional
representation h_6(V) is completely reducible. The projection e
onto the trivial S-isotypic component preserves every S-stable
subspace. One can make this last assertion internal to the actual
representation: the finite-dimensional algebra spanned by the
matrices of S(k) is semisimple, and the central idempotent for its
trivial simple module is e. The density of S(k) identifies its
invariant subspaces with the algebraic S-invariant subspaces.
Thus e is a finite k-linear combination of actual S(k) operators.

It follows that

    e(U intersect P_a) subset U intersect P_a intersect h_6(V)^S,
    q(eD)=q(D).

The second equality follows because q is S-equivariant with trivial
target. This is a projection of an already constrained vector in
the actual arithmetic image. It is not an assertion that eD is
the image of an individual Galois element.

The full mixed normalizer maps are also S-equivariant. Explicitly,
for B_ES(D)(delta)=ES_7([D,delta]),

    B_ES(sD)(delta)=s B_ES(D)(s^-1 delta).

The same equation holds for the source's R contraction. Thus the
zero loci of the complete mixed equations are S-stable. Choosing
only a few coordinate rows is permitted for necessary equations,
but one must not silently treat that chosen row subset as an
S-stable system.

## IR-2. Exact cyclic reconstruction and the 215 parameters

Use the Sp-equivariant tensor map

    T_D=sum_i (x_i tensor D(y_i)-y_i tensor D(x_i)) in V tensor L_7(V).

The bracket map V tensor L_7(V)->L_8(V) is represented in the
tensor algebra by 1-rho, where rho moves the first tensor letter
to the end. Hence specialness is exactly cyclic invariance of T_D.

An S-invariant tensor of length eight has equal multiplicities m
of a and b and 8-2m W slots, with 0<=m<=4. This decomposes the
**ambient** invariant tangent space. It does not by itself
decompose U: every m has the same S-character. All mixed equations
must be imposed on the sum of these blocks.

In a block with m>=1, tangency gives D(a)=[A,a] with A in L_6(V).
The map A->[A,a] is injective. Its associative centralizer is k[a],
and the only positive-degree primitive elements of k[a] in
characteristic zero are multiples of a; degree six therefore
has zero intersection with that centralizer. The unique A is
S-invariant, has m-1 copies each of a,b, and 4-m W pairs.

Let pi_b project a tensor word onto those with first letter b,
and let S_8=sum_{j=0}^7 rho^j. For every cyclic tensor T in this
block,

    S_8 pi_b T = m T.

Indeed, for each fixed word its coefficient is contributed once
for each of the m positions occupied by b. The same count holds
for periodic words: positions, not distinct cyclic representatives,
are counted. As pi_b T_D=-b tensor [A,a], the reconstruction is

    T_D=-(1/m) S_8(b tensor [A,a]).

Conversely, start with A in the indicated invariant Lie subspace
and form this tensor. It is cyclic by construction. To obtain
precisely the required special derivation, impose both

    T in V tensor L_7(V),
    pi_b T = -b tensor [A,a].

These are actual linear tensor equations. With them, extracting
the first-letter components defines a special D with D(a)=[A,a].
Neither condition is omitted on the basis of the cyclic formula.

The symplectic first fundamental theorem spans the invariant W
slots by pairings. After applying the normalized degree-six
Dynkin projector, the following decorated tensors span all A:

* m=1: six W slots, 15 pairings;
* m=2: one a, one b, four W slots, 6*5*3=90 diagrams;
* m=3: two a, two b, two W slots, 6!/(2!2!2!)=90 diagrams;
* m=4: three a and three b, binomial(6,3)=20 diagrams.

The total is 215 spanning parameters, not a claim that all are
independent. The Dynkin map is S-equivariant and acts as identity
on L_6 after division by six, so its images span every invariant
Lie tensor. Relations at a small complement dimension do not
invalidate this spanning assertion.

For m=0 the tensor is in h_6(W)^Sp(W). The opened primary
Morita--Sakasai--Suzuki2015 v2, Table5 (printed p19), gives
dimension five for complement genus at least three. Its explicit
five chord-diagram vectors C_1,...,C_5 are printed pp25--26,
and Proposition7.2 (pp26--27) proves their five-contraction
detector is an isomorphism. Thus the proposed 215+5 construction
spans the ambient invariant tangent space for total genus>=4.
The separately certified genus-three calculation handles its
complement genus two. No finite-rank or all-genus vanishing
claim follows merely from this parameter count.

## IR-3. Safe genus-uniform mixed equations

For an invariant D, curry the actual mixed ES map:

    B_ES(D) in Hom(Lambda^3 V,(V^tensor7)_cyc).

Use the symplectic form to identify its source dual, and use the
normalized cyclic projector to realize the cyclic quotient as a
direct summand. This puts the map in an actual invariant subspace
of V^tensor10. Contracting it against any S-invariant dual tensor
gives a scalar equation that is necessary in **every** genus.
The R map similarly gives scalar contraction equations in its
actual target; no replacement by an unrelated exterior quotient
is made.

These scalar tests can also detect the complete invariant output.
The tensor pairing is nondegenerate. Its restriction to the
trivial S-isotypic component is nondegenerate: every nontrivial
simple S-module pairs trivially with a trivial module, so a
vector orthogonal to the invariant component is orthogonal to
the whole representation. The invariant dual tensors are spanned
by the same first-fundamental-theorem pairings and a,b labels.
The cyclic and alternating source projectors are actual maps,
so testing their ambient tensor images is legitimate.

Every fully contracted decorated diagram evaluates by summing
indices in W. Closing a W strand produces its signed dimension
factor, and the result is a polynomial in N=dim W with rational
coefficients. This must be calculated with one consistent
symplectic cup/cap sign convention. A symbolic polynomial
identity after clearing denominators is valid for every integer
complement genus for which those denominators are nonzero.
Any exceptional roots require separate actual checks.

By contrast, equating all coefficients of a *formal* Brauer
output before evaluation may impose extra equations at a small
dimension, because diagram relations can survive there. A stable
independence assertion must be proved at its exact tensor degree,
or one can use the universally necessary scalar contractions
just described. The proposed matrix is not yet certified in
either implementation.

## IR-4. Five final contractions suffice

The same primary Proposition7.2 supplies five functionals K_D
whose restriction h_6(V)^Sp(V)->k^5 is an isomorphism for every
total genus>=3. Their chord indices in its lexicographic order
are 1,2,3,8,14. For any special D, all five contractions commute
with the full Sp(V)-invariant projector R_full:

    K_D(D)=K_D(R_full D).

If an actual D in U has this five-vector in the span of the
five-vectors of the two actual geometric brackets Z_1,Z_2 used
in the genus-three proof, choose Z in their span with the same
five-vector. The actual J_6 is Sp-stable, hence R_full Z is in
J_6. Injectivity of K_D on the invariant space gives

    R_full D=R_full Z.

As q is Sp-invariant and kills J_6, q(D)=q(Z)=0. The Z_i can be
embedded on three fixed handles in any larger genus: extension
by zero is the actual geometric boundary-surface inclusion.
Their five contractions are unchanged, because no added letters
occur. This argument supplies the exact map from a five-row
contraction certificate to the arithmetic quotient. It does not
project D down to a genus-three derivation.

## Records and retained gate

Read directly: work/LM6_A22_genus_three_single_line.tex;
work/LM6_A22_all_genus_full_tangent.tex;
work/sources_audit_next/MoritaSakasaiSuzuki2015_v2.txt,
Table5 and Proposition7.2 with the displayed chord vectors.
The primary PDF is alongside that text. The actual U/q and
normalizer maps are the previously independently audited
F.3.24 and F.3.26 maps, not newly substituted formal spaces.

These four reduction claims were sent to period_triangle and
root before a universal matrix was supplied. The polynomial
mixed-equation calculation and its implication for the five
contractions remain to be constructed and independently checked.


## Independent read of the complete typed reduction

The complete work/LM6_A22_all_genus_single_line_invariant_reduction.tex
was read after it became available. LI.1--LI.6 pass at their stated
reduction-only scope. In particular, the positive-m input and LI.3
output tensors have at most six W slots. The pairing diagrams there
are independent for complement genus at least three, so this part
really is one fixed integer matrix; the distinguished a,b slot
assignments are separate direct summands. The coupled mixed output
retains scalar contractions and therefore does not impose unsupported
ten-slot independence. The five-contraction map to the actual q6
quotient is exact. No universal matrix or all-genus vanishing was
supplied at this audit stage. Both parent and triangle were notified.

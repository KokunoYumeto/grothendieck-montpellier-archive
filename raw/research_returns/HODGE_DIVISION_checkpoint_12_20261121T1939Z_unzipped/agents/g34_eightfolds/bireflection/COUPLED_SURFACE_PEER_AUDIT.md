# Whole-proof audit: SF-E822

**PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort
inherited/unexposed, HODGE_DIVISION, 2026-11-21, approximately
18:16–18:19 UTC. I read the complete frozen draft, all hypotheses,
the actual example, scope limitations, and the entire author's
symbolic certificate. Reviewed SHA-256:
`bf9dec6e831599b53db853306b2d0c44867175ed36620c75fd7bed25c0c1b95c`.

No mathematical patch was needed. The conclusion is a necessary
condition on weak semiregularity for the specified coherent action;
neither an action nor a semiregular object is constructed.

## 1. The local class and actual coupled module

The sheaf Ext sequence for the kernel of H→i_*Q, using local freeness
of H, identifies Ext¹(K,i_*T) with Ext²(i_*Q,i_*T). The latter top
Koszul Ext is Hom(Q,T)⊗det N. Thus the local extension matrix is an
intrinsic section, irrespective of additional global extension data.

After shrinking, the quotient onto Q can be reduced to its first m
coordinates: a minor invertible on S remains invertible on an open
neighborhood, so local row operations give the asserted presentation.
The extra free summand splits because its Ext¹ into T vanishes.

The displayed three-block presentation and two-step resolution have
the correct orientation and source/target ranks. If d₁(a,b,c)=0,
nonzerodivisibility of f gives a=0, and the two-element Koszul relation
then gives (b,c)=(-gh,fh). Conversely these vectors lie in the kernel,
and d₂ is injective. To check the torsion injection, a relation with
zero first two generator blocks likewise has a=0; its last block is
in (f,g)R^m, exactly the stated torsion relation. This proves the
extension, not merely equality in K-theory. No invertibility of the
extension matrix is used in this exactness argument.

## 2. The first-order obstruction and intrinsic equation

With right modules and column vectors, the displayed matrices do act
by left multiplication, and composition uses the stated star product.
Passing from left modules over the opposite algebra changes π to −π.
The characteristic obstruction is linear in π, so this sign change
preserves its vanishing and cannot affect the final proportionality.

The first-order star product is associative by the biderivation
identity. Vanishing of the characteristic Ext² class gives a flat
module deformation by the finite-resolution argument already checked
in SF-E819. The particular finite free resolution can be lifted
generator by generator: flatness passes to each kernel, and the last
kernel vanishes by nilpotent Nakayama after reduction. Hence the
corrected differentials used here really exist. This step does not
assume that the hull morphism deforms.

Only the bottom block contributes to d₁*d₂. It is the commutator
f*(-g)+g*f, giving −επ(df,dg)I. Derivatives of the extension matrix
never occur because the corresponding block of d₂ is zero. Modulo
(f,g), d₂ vanishes and only the −E block of d₁ remains, so the
correction equation gives E Aπ=Pπ I after the harmless sign change.

The intrinsic type is correct: the first relation block is
Q⊗L⁻¹ and the final syzygy block is T⊗L⁻¹. Their common normal
determinant twist cancels from Aπ, giving Hom(T,Q). Changing local
normal equations changes E and Pπ by the same determinant-frame
factor; the bundle bases give the ordinary source and target changes.
Thus there is no unproved global choice of a matrix correction.

The balanced cap-kernel and invariant-evaluation argument is precisely
the previously reviewed SF-E819 bridge: published Buchweitz–Flenner
supplies the ordinary trace/composition identity; supplied S21 supplies
the specified invariant compatibility. Their source status is retained.
No unrefereed032 theorem or extra CY4 surjectivity statement is used.
The bivector components survive on the local affine open, where the
higher Čech components disappear. This yields both local equations.

## 3. Uniqueness, globalization and the equal-degree step

If one normal section is nonzero, the square equal-rank matrix E is
invertible over the function field. Its sheaf kernel is zero because
Q is locally free on an integral surface. Two local solutions Aπ
therefore coincide on overlaps, so they glue without any deformation
descent assumption.

The nonzero determinant of A₊ is a section of det Q⊗(det T)⁻¹.
Its zero divisor has degree zero against the ample θ|S by the exact
equal-degree hypothesis. A nonempty effective divisor has positive
ample degree. Nor can a nonzero section of a line bundle on the smooth
integral surface have only an isolated zero: its zero scheme, if
nonempty, is an effective Cartier divisor. Hence A₊ is everywhere
invertible. This is the essential global step; generic invertibility
alone would not suffice.

It follows that E=P₊A₊⁻¹ and P₊A₊⁻¹A₋=P₋I. The trace of the
global endomorphism A₊⁻¹A₋ is constant on the integral projective
surface. Taking trace gives mP₋=cP₊, proving linear dependence.
The cases where both sections vanish or only one is nonzero are
handled by the stated initial interchange of signs.

## 4. Ample class, GRR and the actual example

Adjunction with the fixed holomorphic four-form identifies det N with
K_S. Normal projection of π corresponds to restriction of its
contraction with that form; the local coefficient is exactly
π(df,dg). The two RM contractions are the opposite-plane volume forms.
Their diagonal norm pairings against θ² are positive and the mixed
pairings vanish by separate bidegrees. Thus every nonzero linear
combination has positive norm on [S]=k²θ², so the sections are
independent and the theorem applies.

The embedding GRR expansion is correct: td(N)⁻¹ begins with
1−c₁(N)/2. Equality of the entire pushed-forward characters first
gives equal ranks by the leading [S] term, then equal θ-degrees by
the next term. This uses the already checked smooth-embedding GRR
input, with the precise Fulton Corollary18.3.1(c) locator retained;
I do not claim a new proof of GRR in this audit.

I freshly read Stacks Lemma33.47.3 and its complete proof at
<https://stacks.math.columbia.edu/tag/0FD4>, and the complete
smooth-irreducible hyperplane argument in Remark37.32.4 at
<https://stacks.math.columbia.edu/tag/0G4G>. Applied successively to
the very ample embedding, these give the asserted smooth integral
complete intersection. The very-ampleness theorem retains its earlier
published-source check.

The global Koszul resolution of I_S becomes a two-term Hom complex
with zero differential after mapping into O_S. Its degree-one summand
is O_S(D₀+D₁), so every chosen section gives an actual global Ext¹
class. There is no missing local-to-global obstruction. The chosen
P₊ is nonzero by the preceding norm argument. The extension M_e has
K-class O_X, and dualizing across its codimension-two torsion gives
M_e^{**}=O_X, with hull image I_S. Tensoring by the actual rank32
bundle therefore gives exactly the asserted hull, torsion, defect and
entire character. The earlier explicit rank32 character calculation
was independently reconstructed in my E820 audit and is unchanged.

On the dense open where e is nonzero, the extension matrix eI is
invertible. Its projection to any positive-rank torsion summand is
still nonzero. A local splitting would make that pushed-out extension
class zero, which is impossible. Thus this example is genuinely
coupled and does not invoke SF-E821's local direct-summand hypothesis.

## 5. Independent certificate and limitations

`audit_coupled_surface.py` uses my own first-jet matrix arithmetic with
independent derivative symbols and all six bivector coefficients. It
checks the exact ordinary square, star-square, absence of extension
derivatives, and reduced correction for m=1,2,3. A separate
tuple-permutation exterior algebra, not the author's bitmask code,
gives the normal-form Gram matrix 2I and top θ₊²θ₋² coefficient4.
The complete run passed in0.056seconds; input proof hash and output
are retained in `audit_coupled_surface.json`.

The universal rank-m proof was checked algebraically above; the finite
matrix sizes are not presented as an all-ranks proof. Global gluing,
perfectness, degree positivity and the all-action implication were
audited mathematically, not computationally. The stated limitations
for unequal degrees, nonreduced or singular supports and other derived
couplings are necessary and correctly retained. No TeX compilation
was performed.

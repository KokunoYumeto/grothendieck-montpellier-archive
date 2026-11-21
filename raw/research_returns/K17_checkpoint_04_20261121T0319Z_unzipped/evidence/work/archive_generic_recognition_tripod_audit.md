# Independent whole-proof audit: generic recognition

Agent: /root/tripod_integral. Model: GPT-6 Astra Pro. Reasoning effort not exposed.
Date: 2026-11-21 UTC. Verdict: PASS at the exact scope of
`work/archive_generic_recognition_section.tex`.

I read the entire TeX and its bibliography, independently reconstructed
all three proofs, and checked the source statements and specified source
proofs below. The already retained relative hypotheses include a smooth
normal integral base of finite type in characteristic zero and the exact
geometric-kernel sequence. The generic function field is finitely
generated over Q. This audit does not assert a theorem for arbitrary
profinite diagrams, nonnormal bases, or mixed-characteristic exponents.

## F149-GENERIC

The surjection G_K→G follows because finite étale connected covers of
a normal integral scheme are normal integral and remain connected at
the generic point. The natural map from the generic normal-line group
to the group fibre product is a map of exact extensions with identical
kernel and quotient, so is an isomorphism. The same applies to the
whole curve group under the retained geometric homotopy assumption.

On a trivializing affine open W, the pulled-back proposed splitting can
be compared with the actual basis splitting. Their difference is a
continuous cocycle with values in the abelian inertia module. Modulo n,
the class is an étale mu_n torsor on W: only the usual degree-one
fundamental-group/torsor comparison is used, not a K(pi,1) assertion.
All n are invertible because the scheme is over a characteristic-zero
field. If the generic class is the Kummer class of x, restriction to
the DVR at a height-one point and Pic(DVR)=0 force ord(x) to be
divisible by n. Doing this for every n forces the valuation to vanish.

The intersection property of normal noetherian domains applies to x
and x^(-1), so the rational vector and its inverse trivialization
extend over every W. Agreement on the generic point makes these local
extensions glue. This produces a nowhere-zero global vector, even
when Pic(S) is not finitely generated. Equality of the resulting
section class with the original class follows from inflation
injectivity: the same cobounding element in I works on G because
G_K→G is onto. Thus there is no residual invisible global cocycle.

The uniqueness assertion uses the separate arithmetic hypothesis that
K is finitely generated over Q. I reread the complete existing
F149-FULLINJ argument: divisors on a normal proper model reduce an
element divisible by all exponents to the constant number field, and
its integer unit group then has zero intersection of all n-multiple
subgroups. This would not give uniqueness over arbitrary large constant
fields, and the present theorem does not claim that extension.

I freshly read EGA IV2, Theorem 5.10.5 and its full printed proof,
pp.115–116, from `work/ega_iv2.pdf`/`.txt`. It is the depth-two
extension theorem; normality supplies the needed depth condition for
a codimension-at-least-two complement. The direct height-one
intersection argument in the TeX also proves the exact use made here.

## F149-MARKED-RECOGNITION

Fresh primary source:
S. Mochizuki, *The local pro-p anabelian geometry of curves*,
Invent. Math. 138 (1999), 319–423, author manuscript
https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf .
Retrieval ref: `turn490814783view0`; local files
`work/mochizuki_local_anabelian_1999.pdf` and `.txt`.
I read Theorem A (manuscript p.3), Theorem B (p.4), Theorem 16.5 and
the complete following full-profinite comparison (p.86), and Theorem
17.1 with its complete proof (p.87). The entire 103-page paper was
not independently re-proved. The cited anabelian theorems are accepted
primary inputs, with their exact field, morphism and conjugacy scope
checked here.

The isomorphism consequences are sufficient. Number fields and their
finitely generated extensions are sub-p-adic, and regularity of K/k
supplies exactly the relative algebraic-closure condition of Theorem B.
Applying the theorem in both directions to an isomorphism and its
inverse gives a unique field isomorphism; injectivity makes their
composites identities. With that marked field fixed, the full curve
fibre product over G_K determines the hyperbolic curve by Theorem A.
The group-theoretic cusp marking selects the geometric boundary point,
and a curve isomorphism induces the corresponding isomorphism of its
normal line and tangential specialization.

This is a functorial determination on the essential image of the
geometric construction, which is exactly the stated scope. It does not
need to provide a finite procedure for constructing a realization.
Within any realization, choosing a nonzero rational normal vector b
gives the criterion that the difference cocycle lie in the full Kummer
image of K^times. Changing b translates the difference by a member of
that same image. The criterion is therefore independent of b, and the
generic/global theorem proves the equivalence over S.

I also checked the realization and conjugacy issue. Representatives
of the field-group maps can be chosen compatibly with the supplied
marked diagram. After transporting by the corresponding field
isomorphism, the remaining curve-group ambiguity in Theorem A is
geometric conjugacy. Once the selected inertia representatives are
aligned, any remaining such conjugator normalizes geometric cusp
inertia, hence lies in I by the previously checked self-normalizer
theorem. Thus the result is genuinely a well-defined subset of
I-conjugacy classes, not just a subset after uncontrolled full-group
conjugation. It needs the additional G_K and identified arithmetic
base marking, as explicitly stated.

## F149-BARE-EXTENSION

For a split extension with abelian kernel, every continuous cocycle z
gives the extension automorphism (t,g)↦(t+z(g),g). The cocycle equation
is exactly the multiplicativity condition; −z gives its inverse.
It fixes the specified kernel and quotient and translates section
classes by [z], so these automorphisms are transitive on all classes.

For the example over Q, the full Kummer image of Q^times is proper.
The exponent alpha with 2-component −1/3 and all other prime
components zero is compatible in Z-hat. The class of 2^alpha cannot
come from a rational number because its 2-valuation would have to be
an integer equal to −1/3 in Z_2. I reread the full-completion portion
of F149-KUM, including its cofinal factorial system and degree-one
derived-limit check, so a continuous cocycle exists. Equivalently it
can be obtained directly by multiplying the usual full Kummer
cocycle of 2 by alpha. Translation by it sends the geometric reference
class to a nongeometric class. This does not produce an automorphism
of the full marked curve diagram and is consistent with the preceding
proposition.

## Corrections and conclusion

The initial read found only a bare `]` in one display; the root author
had independently caught it and repaired it to `\\]`. I reread that
part in the updated file. Theorem B's precise manuscript locator was
also narrowed to p.4. No mathematical correction or extra hypothesis
was needed. All three claimed results pass at their stated scope;
there is no effective finite-quotient recognition claim and no claim
that the additional generic marking can be reconstructed from G alone.

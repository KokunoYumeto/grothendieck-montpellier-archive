# Independent audit: the relative-curve surface gate

Date: 2026-11-19, 05:32–05:35 UTC.
Written statement audited: sections/b3_surface_gate.tex,
label thm:B-relative-surface-gate.
Status: the complete written proof passes in its stated scope.

Fix p≠ell. The statement compares Tate divisors for all smooth projective
surfaces over F_p, allowing finite constant fields, with finite cokernel
of Br(S){ell}→Br(X){ell} for every smooth projective family of geometrically
connected curves over every smooth separated finite-type finite-field
base. It suffices on the family side to use bases open in P¹ and a section.
Here Br means cohomological torsion H²_et(G_m).

## 1. Exact source input

Independently opened Kahn, *Sur la conjecture de Tate pour les diviseurs*,
Essential Number Theory 2(1) (2023), 83–92:
https://webusers.imj-prg.fr/~bruno.kahn/preprints/Tate-pour-les-diviseurs-ENT.pdf.
Read Lemma 2 and Proposition 3, p. 86; Proposition 5 with full proof,
pp. 87–88; Theorem 6 with proof, p. 88; Proposition 7, pp. 88–89;
Theorem 8 with proof, pp. 89–90; Remark 9, p. 90.
Refs turn902394190view0, turn919840917view3/4,
turn342841895view0/2.

Theorem 6 passes from smooth projective to all smooth separated
varieties using alteration, a finite flat trace on a dense open,
and the divisor-correspondence retraction. There is no unproved
general semisimplicity hypothesis. Theorem 8 reduces to surfaces.
Its published proof explicitly notes the positive-characteristic
Picard weak-Lefschetz issue in Morrow's initial higher-dimensional
reduction and replaces it by iteration of the crystalline diagram.

Independently opened Morrow, *A Variational Tate Conjecture in crystalline
cohomology*, original author version:
https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Morrow,%20M.,%20Variational%20Tate.pdf.
Read Proposition 4.1, Lemma 4.2 and the complete Theorem 4.3 proof,
author pp. 25–27. Refs turn902394190view1,
turn919840917view5, turn342841895view1. Its threefold-to-surface
step selects a smooth ample surface after a finite extension with
no larger generalized Frobenius-one eigenspace, then uses the
crystalline variational divisor theorem. Kahn's published correction
handles the higher-dimensional iteration in the audited proof.

## 2. Tate divisors imply relative Brauer finiteness

For every smooth Z/k, the preceding sources give surjectivity
Pic(Z)⊗Q_ell→H²(Z_kbar,Q_ell(1))^Gamma. Continuous Hochschild–Serre
has the natural degree-two short exact sequence

  0→H¹(Gamma,H¹(Z_kbar,Q_ell(1)))→H²(Z,Q_ell(1))
    →H²(Z_kbar,Q_ell(1))^Gamma→0.

Arithmetic divisor classes lift the geometric classes supplied by Tate.
Subtracting them and applying Kummer shows that the first term maps
surjectively to V_ell Br(Z). The first term is not discarded: for
Z=G_m over a finite field it is Q_ell.

The geometric low-degree Leray sequence for f gives

  0→H¹(S_kbar,Q_ell)→H¹(X_kbar,Q_ell)→C→0,
  C⊂H⁰(S_kbar,R¹f_*Q_ell).

The global section space is pure of weight one. After a finite
constant extension, evaluate on one finite-field point of each
geometric connected component. Evaluation of sections of a lisse
sheaf is injective, and the resulting fibres are smooth projective
curves, whose H¹ is pure of weight one. A positive Frobenius power
detects the same weight before extension. Thus C(1) has weight −1,
so its Gamma-invariants and coinvariants both vanish.

It follows that the two arithmetic H¹(Gamma,H¹(−)(1)) terms for S
and X are isomorphic. Their natural maps to rational Brauer Tate
modules imply V_ell Br(S)→V_ell Br(X) is surjective.

Finite-coefficient étale cohomology of these finite-type separated
finite-field schemes is finite. Kummer consequently makes Br(Z)[ell]
finite. An ell-primary torsion group with finite ell-torsion has
finite cotype: a finite group modulo its maximal divisible subgroup,
which is a finite sum of Q_ell/Z_ell. Rational Tate-module surjectivity
therefore makes the divisible part of the target lie in the image,
and the quotient of the original Brauer groups is finite.

There is no need to assume Pic(Z) finitely generated for the forward
surjection: Pic(Z)/ell^n has surjective transition maps, and the
inverse Kummer sequence maps H²(Z,Z_ell(1)) onto T_ell Br(Z).
Actual divisor classes already map to zero, which is enough.

## 3. The pencil implication

For a geometrically connected smooth projective surface Y/k, choose
over kbar a pencil of a sufficiently ample linear system whose
generic member is smooth and whose nonempty finite base locus is
transverse. These are open conditions defined using finitely many
coefficients, so the pencil descends to some finite k'/k. Enlarge
k' to make one base point rational. Blowing up gives a regular
projective surface Ytilde→P¹_k' with an exceptional-divisor section.
Over a nonempty open U the morphism is a smooth projective curve
family with geometrically connected fibres. No assertion of ordinary
quadratic singularities in the omitted fibres is used.

Restriction gives an injection

  Br(Ytilde){ell}→Br(Ytilde_U){ell}/Br(U){ell}.

Indeed, if beta|_U=f*alpha, the extending section gives
alpha=(section*beta)|_U=0 because Br(P¹_k')=Br(k')=0.
Then beta vanishes on a dense open, so regularity and injectivity
into the function-field Brauer group give beta=0. The written proof
uses Grothendieck Brauer II, Corollary 1.8, separately opened by
Part B and root; this audit does not pretend a new opening of that
scan. Pullback Br(Y_k')→Br(Ytilde) is injective for the same
function-field reason. Thus the relative assertion forces
Br(Y_k'){ell} to be finite.

## 4. Finite extension and the final Tate identification

No prime-to-ell degree restriction is needed. Restriction followed
by corestriction is multiplication by d=[k':k]. Hence the kernel
of restriction on Br(Y){ell} is contained in Br(Y)[ell^v],
v=v_ell(d), a finite group by Kummer. The image is finite because
the target is finite. This proves finite descent to k.

For proper Y, H¹(Y_kbar,Q_ell(1)) has weight −1, so the left
Hochschild–Serre term vanishes. Pic⁰(Y)(k) is finite and NS(Y)
is finitely generated, hence the rational Kummer kernel is exactly
Pic(Y)⊗Q_ell. Therefore V_ell Br(Y)=0 is precisely Tate
surjectivity for divisors. Since Br(Y){ell} has finite cotype,
this is equivalent to its finiteness.

## 5. Quantifier and Brauer scope

The written theorem explicitly quantifies all finite k/F_p and
allows larger fields of constants in its surface clause. Thus the
finite field extensions in the pencil proof remain inside its
hypotheses. Restricting both sides to geometrically connected
objects over one fixed finite field would require another argument;
that narrower formulation is not used.

The proof concerns cohomological Brauer groups. It does not use
an unproved Azumaya/cohomological identification on an arbitrary
nonquasiprojective higher-dimensional base. It also does not extend
the surface equivalence to singular or nonseparated bases, and it
does not touch the characteristic-primary counterexample.

Two minor exposition suggestions were sent root: make the words
“kernel of restriction” explicit in the res/cor paragraph, and
state the proper Picard finite-generation fact in the final
Kummer comparison. Neither alters the argument.

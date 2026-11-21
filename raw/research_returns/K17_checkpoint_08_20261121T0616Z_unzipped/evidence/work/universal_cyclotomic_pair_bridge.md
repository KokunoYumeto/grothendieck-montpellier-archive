# K17-NORM-TORSION / K17-UNIVERSAL-PAIR

Date: 2026-11-21 UTC. Author: `/root/archive_kummer`, GPT-6 Astra Pro.
Reasoning effort: not exposed. Status: complete candidate proof, awaiting
independent whole-proof review. This supplies a conditional arithmetic
Pair-NV implication outside the hypothesis of Greenberg; it does not supply
the cubic Triple-NV input or an unconditional new kernel case.

## 1. A norm-compatible family annihilates all Iwasawa torsion

Let `P=H semidirect Gamma`, `Gamma=<gamma>=Z_p`, and let the coefficient
character have `chi(gamma)=u in 1+p Z_p` and be trivial on `H`. Put
`P_n=H semidirect Gamma^{p^n}`, `Lambda=Z_p[[Gamma]]`, and `M=H^ab`.
No freeness of `H` or `M` is needed in this paragraph. Suppose we have
classes

\[
c_{n,r}\in H^1(P_n,\mathbb Z/p^r(1))\qquad(n\geq0, r\geq1)
\]

compatible both with coefficient reduction and with corestriction in `n`.
Write `a_{n,r}:M -> Z/p^r(1)` for their restrictions. Restriction is an
actual homomorphism, independent of the cocycle representative, because
`H` acts trivially on the coefficients. The cocycle identity also gives

\[
a_{n,r}(\gamma^{p^n}m)=u^{p^n}a_{n,r}(m).
\]

Choose a compatible basis for the Tate coefficient modules, solely to
write scalar formulas. Define

\[
\Phi_{n,r}(m)=
 \sum_{j=0}^{p^n-1}u^{-j}a_{n,r}(\gamma^j m)[\gamma^j]
 \in (\mathbb Z/p^r)[\Gamma/\Gamma^{p^n}].                 \tag{N.1}
\]

Give this group ring the `P`-action with `H` trivial and `gamma` acting
by multiplication by `u[gamma]^{-1}`. Shifting the sum and using the
preceding equivariance identity proves

\[
\Phi_{n,r}(\gamma m)=u[\gamma]^{-1}\Phi_{n,r}(m).             \tag{N.2}
\]

The restricted corestriction formula, using representatives
`gamma^{-k p^n}`, is

\[
a_{n,r}(m)=\sum_{k=0}^{p-1}u^{-kp^n}
                      a_{n+1,r}(\gamma^{kp^n}m).             \tag{N.3}
\]

Consequently the ordinary group-ring projection from level `n+1` to
level `n`, which sums coefficients over each fiber, carries
`Phi_{n+1,r}` to `Phi_{n,r}`. Coefficient reductions are also compatible.
Taking the inverse limit of these actual homomorphisms therefore gives

\[
\Phi:M\longrightarrow\Lambda^\#(1),                         \tag{N.4}
\]

a continuous `Gamma`-equivariant homomorphism. This is the restriction
form of integral Shapiro: at finite level the module in (N.1) is the
coinduced module from `P_n`, written after untwisting its function
coordinates. The convention agrees with Sharifi, *Reciprocity maps with
restricted ramification*, author version 30 June 2017, section 2.5,
printed pp.16--17: his `Lambda^iota` has the inverse group action, and
transition is corestriction. The displayed finite formulas prove the
part needed here directly. In particular no interchange of cohomology
with an inverse limit, no `lim^1` vanishing, and no compatible choice of
cocycle representatives is being assumed.

Let `T` denote the `Lambda`-torsion submodule of `M`. If `f(gamma)t=0`
with `f` nonzero, equivariance gives

\[
 f(u\gamma^{-1})\Phi(t)=0.
\]

The substitution `gamma -> u gamma^{-1}` is an involutive continuous
automorphism of `Lambda`: in the parameter `Z=gamma-1` it is
`Z -> u/(1+Z)-1`. The ring `Lambda=Z_p[[Z]]` is a domain. Thus
`Phi(t)=0`. At every finite level the coefficient of the identity basis
element in (N.1) is exactly `a_{n,r}(t)`. We have proved, integrally,

\[
                    a_{n,r}|_T=0\quad\hbox{for all }n,r.      \tag{N.5}
\]

The result applies to any linear combination or prime-to-`p` character
projection of such families.

## 2. Every finite cyclotomic symbol has these inputs

Now take `p` odd and the arithmetic cyclotomic tower. At level `n` put
`F^(n)=Q(mu_{p^{n+1}})`, with compatible roots of unity, and use the
maximal pro-`p` group unramified outside `p` over `F^(0)`. Its subgroups
are the preceding `P_n` and `H` is the kernel over the whole cyclotomic
tower. For every `a in Z_p^times`, set

\[
v_n(a)=1-\zeta_{p^{n+1}}^{\,a\bmod p^{n+1}}.
\]

These are `p`-units and

\[
 N_{F^{(n+1)}/F^{(n)}}v_{n+1}(a)=v_n(a).                     \tag{N.6}
\]

Kummer maps commute with norm and corestriction. Therefore their finite
Kummer classes form the families of section 1 and kill `T` on restriction
to `H`. The classes are classes of the maximal pro-`p` quotient: the
Tate action factors through it, and the previously proved degree-one
comparison with etale cohomology is an isomorphism. That comparison is
natural for the tower transfers. One can also see the factorization
directly from the `p`-power Galois closure of the Kummer extension, since
the fields contain `mu_p`.

There is no restriction to unit exponents in the final assertion.
At level `n`, write any nonzero exponent modulo `p^{n+1}` as `p^s b`,
where `0<=s<=n` and `b` is a unit. Then

\[
1-\zeta_{p^{n+1}}^{\,p^s b}
 =\prod_{j=0}^{p^s-1}
    \left(1-\zeta_{p^{n+1}}^{\,b+jp^{n+1-s}}\right).          \tag{N.7}
\]

Each exponent on the right is a unit. This is the polynomial identity
`product_j(1-X eta^j)=1-X^{p^s}` for a primitive `p^s`-th root `eta`.
Every factor is the level-`n` value of a norm-compatible family. Thus
the Kummer class of every cyclotomic input appearing in the finite
Fukaya--Kato symbol theorem restricts to zero on all of `T`, not merely
on its even part. Formula (N.7) is an equality in the same finite field;
no descent or division by its degree is involved.

Complex conjugation `c` commutes with these norms. Averaging a family
by `(1+c)/2` preserves the conclusion. For a cyclotomic unit `v`, its
negative conjugation component is in the cyclic root-of-unity subgroup,
since `v/c(v)` is a root of unity. Equivalently, for any `p`-unit this
quotient is a global unit of absolute value one at every embedding:
the unique prime over `p` is fixed, so its valuation cancels. Two such
negative Kummer classes have zero cup product, because they are
multiples of one class and the cup is alternating for odd `p`.
Mixed-parity cups contribute only to the odd target. It follows that
the even target spanned by cyclotomic symbols is spanned by cups of
`c`-even classes whose restrictions factor through `Q=M/T`.

## 3. The corrected class-two extension when odd torsion is present

Assume `Delta=F_p^times` acts on `H` and commutes with `Gamma`, the
coefficient character extends to `P semidirect Delta`, and its value
on the involution `c` is `-1`. Assume `H` is free pro-`p`,
`M` is finitely generated over `Lambda`,
`T` is finite free over `Z_p`, and `Q=M/T` is `Z_p`-torsion free,
has only odd conjugation parity, and becomes free of finite rank over
`R=Lambda[1/p]`. These are the module hypotheses in the cubic theorem.
Suppose each even character component `T_e^+[1/p]` is cyclic over `R`.

For odd `p`, the actual class-two quotient of `H` has its integral
Baker--Campbell--Hausdorff Lie structure. Its central commutator module
is the completed exterior square of `M`. Quotient that central module
by the closed subgroup generated by all brackets with a `T` input.
The remaining central module is

\[
                     N=\widehat\bigwedge{}^2_{\mathbb Z_p}Q.
\]

The equality of this kernel with the required exterior-square quotient
also follows by choosing a continuous `Z_p`-splitting of `M -> Q`;
such a splitting exists because compact torsion-free `Z_p`-modules are
products of copies of `Z_p`. It is not assumed `Gamma`-equivariant.

The central module `N` has positive conjugation parity. Hence the
negative part of the resulting Lie module maps isomorphically onto
`M^-`, giving a canonical `Gamma`-equivariant section there. Its lift
of `T^-` is central, since brackets with `T` were killed. Quotient this
central `Gamma`-stable lift as well. The resulting Lie module has its
canonical odd section from `Q`, and its even part is the actual
extension

\[
            0\longrightarrow N\longrightarrow E
                    \longrightarrow T^+\longrightarrow0.   \tag{N.8}
\]

This construction neither splits `M` as a `Gamma`-module nor discards
the extension in (N.8). For a rational cyclic generator `v_e` of
`T_e^+` and an even lift `y_e`,

\[
                    q_e(\gamma)y_e=C_e\in N[1/p].           \tag{N.9}
\]

This is exactly the free-`Q` quadratic companion of the cubic theorem:
brackets involving torsion lifts vanish in (N.8), the companion product
therefore becomes the additive characteristic-polynomial expression,
and the logarithm and Magnus quadratic part agree on a derived element.

## 4. Norm-family cup generation forces Pair-NV

Suppose, on a cofinal diagonal of group and coefficient levels, that
`H^2(P_n,Z/p^n(2))^+` is generated by cups of even classes with
restrictions killing `T`. We prove that for every root `alpha` of every
`q_e`, at least one free-`Q` coefficient of `C_e` is nonzero on

\[
                   (1+T_1)(1+T_2)=\alpha.                   \tag{N.10}
\]

Use a finite splitting field `L/Q_p`, with integers `O`. The coordinates
of `Q[1/p]` in an `R`-basis, and their inverse, have bounded denominators
because the modules are finitely generated over `Lambda`. Completed
tensor and exterior powers inherit this bound. Thus `N[1/p]` is the
alternating bounded-denominator series module in the two variables.
All roots `alpha` are congruent to one in the maximal ideal of `O`, by
continuity of the pro-`p` action on the finite-rank lattice `T`.

If all coefficients vanish on (N.10), the integral formal-coordinate
change

\[
 S=(1+T_1)(1+T_2)-\alpha,
 \qquad T_2=(\alpha+S)/(1+T_1)-1
\]

shows that `C_e=(gamma-alpha)A` in `N_L`. Division preserves a common
denominator bound; the quotient is alternating since the divisor is
symmetric. Let `r_e(z)=q_e(z)/(z-alpha)`. Cyclicity implies
`w=r_e(gamma)v_e` is a nonzero vector spanning the `alpha`-socle, even
when the root is repeated. Then

\[
        \widetilde w=r_e(\gamma)y_e-A
\]

is an equivariant lift of `w` in (N.8). Let `W=Lw` and
`W_O=W intersect T_O^+`. The latter is saturated and hence a direct
summand over `O`. Choose an `O`-linear section of (N.8), after inverting
`p`, extending this equivariant lift on `W_O`. A single power `p^b`
clears its denominators. With the canonical odd section, write the
class-two logarithm of `h` as

\[
             x(h)+s(t(h))+z(h),\qquad
 x(h)\in Q_O,\quad t(h)\in T_O^+,\quad z(h)\in N_L.
\]

The same `p^b` makes every `z(h)` integral. The section defect
`beta_delta(t)=delta s(t)-s(delta t)` vanishes on `W`.

Fix two even cocycles `f,g` at level `n`, averaged under `c`.
They vanish on the chosen `Gamma^{p^n}` section: conjugation fixes
its elements and acts by `-1` on the coefficient module. On `H` they
are additive maps factoring through `Q`, by hypothesis. Let
`psi=f wedge g:N_O -> O/p^n(2)`. The integral cochain

\[
 k(h)=-\frac{p^b}{2}f(h)g(h)-\psi(p^b z(h))                  \tag{N.11}
\]

has differential `dk(h_1,h_2)=p^b f(h_1)g(h_2)`. Indeed the central
coordinate of a product is `z_1+z_2+[x_1,x_2]/2`; its two contributions
are respectively `p^b(f_1g_2+f_2g_1)/2` and
`p^b(f_1g_2-f_2g_1)/2`. The Hochschild--Serre edge of this cup is
therefore, up to an irrelevant convention sign,

\[
                  \psi(p^b\beta_\delta(t)),                 \tag{N.12}
\]

which is zero on `W`. This computes the actual cup map, rather than
inferring it from characteristic ideals.

Both `H` and `Gamma^{p^n}` have `p`-cohomological dimension at most one. Odd
components of `M`, including its odd torsion, contribute only negative
parity to `Hom(M,O/p^n)(2)`. Thus

\[
 H^2(P_n,O/p^n(2))^+
 =H^1(\Gamma^{p^n},\operatorname{Hom}(T^+,O/p^n)(2)).         \tag{N.13}
\]

Put `V=Hom_Zp(T^+,O)(2)` and let `B` be its `gamma` operator.
The latter group is

\[
              V/(p^n V+(B^{p^n}-1)V).                       \tag{N.14}
\]

Corestriction sends a generator value to the same value in the larger
group's coinvariants, so its transition is the quotient map, not
multiplication by `p`. Continuity gives `B^{p^n}-1 -> 0`; the
denominators in (N.14) are cofinal with the `p`-adic neighborhoods.
The inverse limit is therefore `V`.

Restriction gives a nonzero torsion-free quotient of `V` onto
`Hom_O(W_O,O)(2)`, whose rational root is `u^2/alpha` and whose
character is `chi^2 e^{-1}`. This map is surjective because `W_O` is
saturated. Formula (N.12) and the cup-generation assumption imply that
`p^b` times every element of every finite target has zero image in the
corresponding quotient for this dual line. Taking the separated inverse
limit would make `p^b` annihilate a nonzero torsion-free quotient, a
contradiction. The power `b` was chosen once, before the finite cups;
no compatible choices of their expressions as sums are needed.
This proves Pair-NV for every root, with arbitrary multiplicity.

## 5. A precise arithmetic sufficient hypothesis

For `p>=5`, let `X` be the unramified Iwasawa module of the cyclotomic
tower. For each even `theta !=1,omega^2`, put `chi=omega^{-1}theta`
and let `xi_chi` be a characteristic series of `X_chi(1)`, in the
ring and twist convention of Wake--Wang-Erickson. Assume, for every
nonzero such component, the two conditions

\[
\begin{split}
 &X_\chi(1)[1/p]\text{ is cyclic over }(\Lambda/\xi_\chi)[1/p],\\
 &X_\theta\otimes_\Lambda(\Lambda/\xi_\chi)[1/p]=0.           \tag{N.15}
\end{split}
\]

These are exactly *Pseudo-modularity and Iwasawa theory*, author
version arXiv:1505.05128v3, Corollary 8.1.3(2), p.49. Its entire proof
has been read again: the conclusion is an integral isomorphism for
`varpi` after quotienting the modular-symbol source by its `p`-primary
torsion. Hence the original `varpi` is surjective. The argument allows
repeated roots. It does not require the derivative of `xi_chi` to be
invertible.

The tame-level-one hypotheses are `p>=5`, primitive `theta`, and
`theta != omega^2`; precisely `theta=1,omega^2` are omitted among even
characters. The source also assumes a nonunit characteristic series.
For unit series the target is zero: `X^-` is `p`-torsion free, and a
finite such module is zero. We do not apply that nonunit theorem to
a zero component.

Fukaya--Kato, author version 15 August 2012, sections 7.1.8--7.1.10,
printed p.86, turns this surjectivity into generation at every finite
cyclotomic level by symbols `{1-zeta^a,1-zeta^b}`. Their allowed
exponents are nonzero and at least one is prime to `p`; (N.7) handles
both factors whether or not either exponent is a unit. No restriction
on common higher powers is being added. Their section 7.1.9 identifies
the mod-`p^r` target with the corresponding class-group quotient.

The two omitted even target characters correspond to
`X_{omega^{-1}}` and `X_omega`, both zero by the Stickelberger exception
calculation already checked. Norm maps from the inverse minus class
module onto every finite minus class group are surjective; thus these
finite targets are zero too. The exact source is Sharifi's Iwasawa
notes, Proposition 3.4.1 and proof, pp.90--91. The exceptional
`omega^{-1}` zero is explicitly recorded in Wake--Wang-Erickson,
*Ordinary pseudorepresentations and modular forms*, proof of Lemma
5.2.7, p.13. At the field `F^(n)` the FK coefficient index is `n+1`;
reduction gives the needed `p^n` coefficients. The Brauer term is zero
because there is one omitted finite prime and no real place.

Use the previously proved degree-one isomorphism and degree-two
injection from maximal pro-`p` group cohomology to etale cohomology.
Lifting all the Kummer inputs and then their cup expressions makes
this injection surjective on the even target. Its naturality also
identifies the finite norm families used above. This argument does
not assume an arithmetic `K(pi,1)` theorem.

The unconditional module inputs already established in the Greenberg
and cubic sections give `Q[1/p]` rank one in every odd character and
zero in even characters. The first condition in (N.15), together with
the Kummer pseudoisomorphism
`M^+ ~ (X^-)^iota(1)`, makes each rational even component cyclic.
Its root `alpha` and character `e` correspond to the target root
`u^2/alpha` and character `omega^{2-e}`. Thus every assumption of
sections 3--4 is fulfilled. **Under (N.15), the actual free-`Q`
quadratic companions satisfy Pair-NV even when odd Iwasawa torsion
is nonzero.**

The second condition in (N.15) is a support condition, not a statement
that all of `X^+` is finite. No simpler untwisted shared-root condition
is substituted for it. Greenberg implies (N.15), but this proof uses
exactly the displayed hypotheses. It provides no example with
`X^+[1/p]` nonzero and does not prove (N.15) without them.

For the existing cubic kernel criterion one must additionally have
cyclicity of every odd rational torsion character and actual Triple-NV.
The first has the reflected even-class-module interpretation described
there; the second is not supplied by this proof. Combining those two
additional hypotheses with (N.15) gives a conditional kernel theorem
with Pair-NV removed from its separate assumptions. It does not yet
weaken the established arithmetic Greenberg gate without verifying
the remaining arithmetic cubic input.

## 6. Actual primary checks and files

* Full displayed proof reconstructed and read back; independent review
  is pending at this version.
* Sharifi, *Reciprocity maps with restricted ramification*, author PDF
  dated 30 June 2017, full opening of section 2.5, pp.16--17, freshly
  read; it is not Proposition 2.4.3 (that proposition concerns duality).
  Primary https://www.math.ucla.edu/~sharifi/selmer.pdf ; local
  `work/sharifi_reciprocity_2017.pdf` and `.txt`.
* Wake--Wang-Erickson, *Pseudo-modularity and Iwasawa theory*, full
  setup pp.2--3, section 2.1 pp.7--8, and full Corollaries 8.1.2--8.1.3
  and proofs pp.48--49 freshly read. Primary
  https://arxiv.org/pdf/1505.05128v3 ; local
  `work/wake_wang_erickson_pseudo.pdf` and `.txt`.
* Fukaya--Kato, *On conjectures of Sharifi*, inspected 15 August 2012
  author version, full sections 7.1.8--7.1.10 freshly read, along with
  adjoining 7.1.1--7.1.7. Primary
  https://www.math.ucla.edu/~sharifi/sharificonj.pdf ; local
  `work/fukaya_kato_sharificonj.pdf` and `.txt`.
* Existing entire cup/Ext TeX and the relevant complete arithmetic
  portion of `greenberg_kernel_section.tex` read again. Their earlier
  exact primary checks are retained, rather than falsely described as
  newly repeated here.

No formal proof execution, new class-group computation, or arithmetic
nonvanishing certificate is claimed.

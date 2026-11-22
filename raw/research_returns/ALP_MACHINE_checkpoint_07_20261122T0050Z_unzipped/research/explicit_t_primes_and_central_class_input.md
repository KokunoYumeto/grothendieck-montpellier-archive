# AM-R-017: explicit auxiliary T-primes and a first source class at maximal 29-level

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 22 November2026UTC.
Effort is not externally exposed.

This result makes two previously qualitative choices concrete. It supplies
one explicitly certified auxiliary T-prime for each of the K031 and K032
hosts. It also constructs a nonzero first automorphic input with the G
generic type and nontrivial T dilation characters, without imposing a
principal level at29 to remove rational stabilizers. Its exact class mass
is computed. The theta lift of this input with the complete prescribed raw
kernel is not proved nonzero here: averaging a translated29 kernel over
the maximal29 compact remains a separate issue. The unchanged source
`Fields.Kq` obstruction also remains.

## 1. Two explicit norm primes with the full source congruence

Use the already checked fields of K031 and K032, and write
\(\delta=\sqrt{-7}\) in their common external quadratic subfield.
The following data use the exact G-primes of those findings:

| Product host | f | k | Rational conductor c | g0 | g1 | n |
|---|---:|---:|---:|---:|---:|---:|
| J14 |42|42|812|4615409|5276377|3|
| J56 |168|168|52780|22285932761|64072175441|16|

In each row set
\[
 L=c(g_0g_1)^2,\qquad A=1+nL,\qquad
 \pi_T=A+L\delta,\qquad T=A^2+7L^2.
 \tag{R17.1}
\]
Thus every number in the construction is specified without a prime-search
oracle. The exact prime integers, also recorded in the certificate, are:

- J14: `3710360310942963702130514092646914581678165356491757211050633`.
- J56: `3045759889845354427724717877501093821489629367456155582288640401018208099619883018305672886530161`.

Both T are prime. Here is the complete certificate method, including the
factored divisors required to make the primality conclusion deterministic.
For J14 use \(F=586L\), and for J56 use \(F=44L\). Their factorizations are
\[
\begin{aligned}
 F_{14}&=2^3\cdot7\cdot29\cdot293\cdot g_0^2g_1^2,\\
 F_{56}&=2^4\cdot5\cdot7\cdot11\cdot13\cdot29\cdot g_0^2g_1^2.
\end{aligned}
\tag{R17.2}
\]
Each listed prime factor is verified by trial division through its integer
square root. The replay verifies \(F\mid T-1\), \(F^2>T\), and, for every
prime \(r\mid F\),
\[
 z_r^{T-1}\equiv1\pmod T,\qquad
 \gcd(z_r^{(T-1)/r}-1,T)=1,
 \quad z_2=3,\quad z_r=2\ (r\ne2).
 \tag{R17.3}
\]
These are precisely Pocklington's factored-divisor criterion. The exact
modular residues and gcds are in
`checks/explicit_t_prime_and_stabilizer_certificate.json`. Candidate
discovery used a separate primality screen, but that screen is not an
input to the saved replay or to this primality proof. The replay uses only
integer arithmetic, modular powers, gcds, and trial division on the small
factors in(R17.2).

The norms and congruences required in the source follow exactly:
\[
 \pi_T\bar\pi_T=T,\qquad \pi_T\equiv1\pmod{c(g_0g_1)^2},
 \qquad T\equiv1\pmod c.
 \tag{R17.4}
\]
The certificate checks \(\gcd(T,2A)=1\). A prime dividing both
\(\pi_T\) and its conjugate would divide T and their sum \(2A\), which
is impossible. The two ideals therefore are coprime, also after extending
to either host. Since the host is contained in the c-th cyclotomic field,
T splits completely. Exactly f primes divide \(\pi_T\), all to exponent
one and with residue field \(\mathbf F_T\): at each conjugate pair one
must divide the product T, and coprimality forces exactly one to divide
\(\pi_T\). This verifies the norm, congruence, coprimality, half-cardinality
and residue-norm clauses for this explicit choice.

The first T has61 digits and the second97. This supplies exact finite
values, not an asymptotic upper bound for a changing-weight family. For
example, retaining the K031/K032 constants C, define
\[
 A_{\rm size}=2(2k+1)C+2+2fN_2.
 \tag{R17.5}
\]
The two values are respectively `7676528679020` and `27317450103536`.
The replay verifies
\(2fN_2+1<4A_{\rm size}<T\). These are the `a_gt` and `T_gt` inequalities
of `Sizes` for this size parameter. The independently specified `spread_le`
inequality must still be verified for whichever full collection of source
words is used; it is not inferred merely from finding a large T. No
quantitative MainX window is claimed by(R17.5).

The field-membership clause `piT_Kq` is deliberately not asserted. K031
proved that the source's defined common field is Q for this induced
primitive type. The present \(\pi_T\) lies in the actual external
\(\mathbf Q(\sqrt{-7})\), as do the previously constructed G generators.

## 2. The exact rational stabilizer of a standard definite lattice

Let E be either host, let F be its maximal real subfield, and let
\(X=(E^a,I_a)\). Write
\[
 K_0=\prod_{v<\infty}U(I_a,\mathcal O_{F_v}),\qquad
 \Gamma=U(X)(F)\cap K_0.
 \tag{R17.6}
\]
At split places this notation means the standard \(\mathrm{GL}_a\)
compact; equivalently K0 stabilizes \(\mathcal O_E^a\) at every finite
place. Then
\[
                  \Gamma=\mu(E)^a\rtimes S_a.
 \tag{R17.7}
\]

Indeed every entry x of a matrix in Gamma is integral, and at every
complex embedding \(|\tau(x)|\le1\), by the unitary row norm. If x is
nonzero, its algebraic norm is a nonzero integer, so the product of these
absolute values is at least1. Every factor must therefore equal1. Such
an integral x is a root of unity: all powers of x lie in the bounded set
of the Minkowski lattice \(\mathcal O_E\) with these absolute-value bounds;
that set is finite, so two powers coincide. The row norm now forces
exactly one nonzero entry in each row. Orthogonality forces their column
positions to be distinct. This proves containment in the displayed
monomial group, and the reverse containment is immediate.

For both fields \(\mu(E)=\mu_{28}\). K031 has Galois group
\(C_2^2\times C_{21}\), and K032 has \(C_2^4\times C_{21}\), each of
exponent42. Their conductors are c from the table. A cyclotomic subfield
arising from an additional root of unity must have conductor dividing c.
The possible new factors29, and also5 or13 in the second case, would
require a quotient Galois group of exponent divisible by4, which these
groups do not possess. The2-part of c is4 and its7-part is7. Since i and
\(\zeta_7\) already belong to both fields, exactly \(\mu_{28}\) remains.

Choose one of the T places and identify its residue field with
\(\kappa=\mathbf F_T\). Reduction embeds \(\mu_{28}\) in \(\kappa^\times\),
since T is prime to28. Suppose \(b\in\kappa^\times\) has order greater
than a in the quotient \(\kappa^\times/\mu_{28}\), and take
\[
 u=(1,b,b^2,\ldots,b^{a-1}),\quad
 P_u=\{g\in\mathrm{GL}_a(\kappa):ug=s(g)u\},\quad
 H_u=\ker(s:P_u\to\kappa^\times).
 \tag{R17.8}
\]
Then the exact intersections with the rational group are
\[
 \boxed{\quad\Gamma\cap\widetilde P_u=\mu_{28}I_a,
               \qquad\Gamma\cap\widetilde H_u=\{1\}.\quad}
 \tag{R17.9}
\]
Tildes denote reduction preimages inside K0 at that place, with no
extra restriction at the other places.

To prove(R17.9), pass to \(\kappa^\times/\mu_{28}\). A monomial g in
\(P_u\) must carry the set of coordinate classes
\(\{1,[b],\ldots,[b]^{a-1}\}\) to itself by multiplication by \([s(g)]\).
The class \([s(g)]\) belongs to the cyclic subgroup generated by \([b]\),
because it carries one member of that set to another. A proper consecutive
interval of length a in a cyclic group of order greater than a has trivial
translation stabilizer: its cyclic consecutive gaps have a unique gap
greater than1, which any stabilizing translation must fix. The same
claim is immediate for a=1. Thus \([s(g)]=1\). All coordinate classes
are distinct, so the permutation of g is the identity. Every diagonal
entry equals s(g), and g is scalar. Fixing u then forces that scalar to
be1. Conversely every scalar root lies in \(P_u\), as required.

For both numerical rows we may take b=2. The certificate checks
\[
                     2^{28j}\not\equiv1\pmod T
                         \quad(1\le j\le a),
 \tag{R17.10}
\]
with a=42 or168. Thus no primitive-root search or complete factorization
of T-1 is required. Formula(R17.8) is an explicit residue functional.
The argument remains valid if the other chosen T places use the same
functional, and if the G places are kept at their full maximal compact.

## 3. A nonzero class-supported input and its exact mass

Let \(\rho_\infty\) be any of the specified irreducible compact types
on \(U(a)^f\), let \(d_\rho=\dim\rho_\infty\), and choose a unit vector
\(v_\rho\). At each G place use the finite Steinberg representation and
its unit generic vector from DO033/LIFT20. Denote their dimensions by
\(d_{G,P}\), and put \(d_G=\prod_{P\in G}d_{G,P}\). Their central
characters are trivial, because they occur in the finite flag module
\(\operatorname{Ind}_B^{\mathrm{GL}_a(\kappa)}1\).

Let H be K0 with its component at each of the f chosen T places replaced
by \(\widetilde P_u\); use(R17.8) at every such place. With each maximal
compact having volume1,
\[
 d_T=[\mathrm{GL}_a(\mathbf F_T):P_u]
       =\frac{T^a-1}{T-1},\quad
 \operatorname{vol}(H)=d_T^{-f},\quad
       \Gamma_H=U(X)(F)\cap H=\mu_{28}I_a.
 \tag{R17.11}
\]
The index is the number of projective nonzero row vectors: the full
general linear group is transitive on them and Pu is the stabilizer.
Equation(R17.9) gives the last assertion; no congruence at29 has entered.

Write \(\omega_\infty\) for the character of \(\mu_{28}\) on
\(\rho_\infty\). Choose multiplicative residue characters
\(\nu_P:\mathbf F_T^\times\to\mathbf C^\times\), all nontrivial, such that
\[
       \omega_\infty(\zeta)\prod_{P\mid\pi_T}\nu_P(\bar\zeta_P)=1
                       \qquad(\zeta\in\mu_{28}).
 \tag{R17.12}
\]
This choice always exists. Restriction from the character group of the
cyclic group \(\mathbf F_T^\times\) to that of its subgroup \(\mu_{28}\)
is surjective. Each restriction has \((T-1)/28>1\) extensions, so it
has a nontrivial extension even if the prescribed restriction is trivial.
Prescribe trivial restrictions at all but one place and the required
inverse character at the remaining place. This also explains the finite
coefficient extension needed for the \(\nu_P\): roots of order T-1 must
be included. Their coefficient-field cost is not discarded.

For \(h\in H\) and \(k\in U(a)^f\), define
\[
 m(k,h)=\langle v_\rho,\rho_\infty(k)v_\rho\rangle
   \prod_{P\in G}\langle v_P,\operatorname{St}_P(\bar h_P)v_P\rangle
   \prod_{P\mid\pi_T}\nu_P(s(\bar h_P)).
 \tag{R17.13}
\]
Use the conjugate-linear-first Hermitian convention in this display.
Define \(F\) on \([U(X)]\) to be \(\overline{m(k,h)}\) on
\(U(X)(F)U(a)^fH\), and zero off this class. This is well-defined: two
presentations differ by an element of \(\Gamma_H\), and(R17.12) says
exactly that the resulting product multiplier is1. F is smooth, has
the required dual real compact type and inverse G-generic character,
and is invariant under \(\widetilde H_u\) at T. At29 it is invariant
under the full maximal compact. It is nonzero, since F(1)=1. It is an
automorphic cusp form because U(X) is anisotropic over F.

The exact scalar-dilation augmentation at each T place is zero:
right multiplication by an element of Pu with s-coordinate t multiplies
F by \(\nu_P(t)^{-1}\), and
\(\sum_{t\in\mathbf F_T^\times}\nu_P(t)^{-1}=0\).
This is the local augmentation condition used for the initial ramified
column. Reading it as the full source `RamT` record additionally uses
its specified decoration/dilation dictionary; the scalar identity alone
does not instantiate that independent record.

Normalize Haar measure on the compact real group to1, as in DO033.
The quotient of the support class has measure \(d_T^{-f}/28\).
Schur orthogonality at the real group and the independent G compacts
therefore gives
\[
 \boxed{\quad \|F\|^2
       =\frac{1}{28\,d_T^f\,d_\rho\,d_G},
       \qquad F(1)=1,\qquad\|F\|_\infty\le1.\quad}
 \tag{R17.14}
\]
Every T character has modulus1 on its support. The factor28 comes from
the actual rational stabilizer and is not absorbed into Haar measure.
The finite G scalar denominators and the coefficient metric of
\(v_\rho\) remain those of DO033/R011; this statement does not replace
their primitive integral models by an arbitrarily rescaled unit vector.

For the explicit ranks the new projective-level index is an11-adic unit:
\[
                         v_{11}(d_T)=0.
 \tag{R17.15}
\]
For J14, T is2 modulo11 and a=42, so neither numerator nor denominator
of dT is divisible by11. For J56, T is1 modulo11 and a=168, so
\(v_{11}(T^a-1)-v_{11}(T-1)=v_{11}(168)=0\).
The certificate checks these exact valuations. The analytic norm cost
\(d_T^f\), despite its11-adic unit valuation, is still large and fully
retained in(R17.14).

## 4. What this removes, and what it leaves

The old first-input construction made the rational stabilizer trivial
by a principal level at29. Equations(R17.8)–(R17.14) supply a different
actual input with the required first G generic behavior and T
augmentation while keeping maximal level at29. Thus rational-stabilizer
compatibility, by itself, is no longer an obstruction to a source input
at that level. The two numerical T choices also replace the qualitative
prime choice for these fixed hosts by exact certified integers.

There is still no nonvanishing assertion for the raw kernel applied to
this F. If a previously chosen29 Weyl translate is inserted into the
theta kernel, the source integral at maximal29 level averages that
translate over the compact. Its resulting selected coefficient can
vanish. Neither the explicit T-prime nor(R17.14) proves that projection
nonzero. The previous-image integral lattice, the terminal row map, the
global MainX mass, and the changed-family DP44 cost remain separate.
Likewise(R17.4) does not repair `Fields.Kq`, and(R17.5) does not prove
the complete quantitative size window for an unbounded weight family.

## 5. Exact sources and checks

- K031, (HC3)–(HC16) and section5; K032, sections4–6: the two actual
  product hosts, G-primes, conductors, ranks and constants. These are
  used with their recorded whole-proof checks.
- Alpöge's stipulated pinned source at commit
  `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`:
  `Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`,
  `Primes.Ok`206–238 and `Sizes`486–494; these are the literal norm,
  residue, congruence, common-field and size conditions distinguished
  above. `LevChiEqOne.lean`, `RamT`85–87, is the separate global
  decoration/dilation condition.
- Pocklington, H. C. (1914–1916). The determination of the prime or
  composite nature of large numbers by Fermat's theorem. *Proceedings
  of the Cambridge Philosophical Society, 18*,29–30. The precise
  factored-divisor form used here is also stated as Theorem1 in the
  FLINT official documentation, *Primality proving: APRCL and ECPP*,
  https://flintlib.org/doc/algorithms/number-theory/primality-proving.html.
  The latter statement was consulted directly; this is not a claim
  that the inaccessible original PDF was read in full.
- DO033 sections1 and4, DO034 section6, R011: matrix-coefficient
  normalization, actual compact masses and the separate coefficient
  metric. The new class calculation retains their conventions.

The exact replay is `scripts/explicit_t_prime_and_stabilizer_certificate.py`.
Its finite checks certify(R17.1)–(R17.5),(R17.10),(R17.15). The proofs
of(R17.7)–(R17.14) are the mathematical arguments above, not consequences
of a numerical experiment. Whole-proof review is recorded separately.

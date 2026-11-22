# ALP-LIFT-18 — exact literal-G character compatibility and an explicit admissible family

Author: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE, 21 November2026UTC.

This result solves the even stage-character compatibility problem for the actual mixed host, with the source's specified G-residue characters. It gives a necessary and sufficient congruence, constructs the characters when it holds, and supplies numerical Harish--Chandra data satisfying that congruence and the displayed source gap conditions. The next local type and prescribed-kernel nonvanishing problems are not solved by the character construction.

The norm-one torus class-number statement of AM-R-009 is used as a checked input. The exact residue characters and conductor conventions are the ones audited in ALP-LIFT-17. The independently obstructed unramified odd character etaT is not supplied here.

## 1. Host, the actual G half, and the root norm

Put
\[
 E'=\mathbf Q(\zeta_{28}),\qquad F'=E'^+,\qquad
 K_q=\mathbf Q(\sqrt{-7}),\qquad
 \Phi'=\{1,3,9,15,17,23\}.
 \tag{G1}
\]
The actual primitive CM type on \(J^2\) is \(\Phi'\), with
\(\sigma_a(\zeta_{28})=\zeta_{28}^a\).
The G half in the source is defined instead by a prime generator
\(\pi_G\in K_q\), with
\(\pi_G\bar\pi_G=q\), where \(q\equiv1\pmod{28}\) is prime.
Its selected places are the six places of \(E'\) above the chosen
prime of \(K_q\), namely the support of \(\bar\pi_G\).
They give one member of every conjugate pair over \(q\).

The subgroup \(\operatorname{Gal}(E'/K_q)\) consists of those
units modulo28 whose reduction modulo7 is a quadratic residue:
\[
                    \Psi'=\{1,9,11,15,23,25\}.
\]
For an elementary check of this quadratic subfield, put
\(u=\zeta_7+\zeta_7^2+\zeta_7^4\) and
\(v=\zeta_7^3+\zeta_7^5+\zeta_7^6\).
Then \(u+v=-1\) and direct multiplication gives \(uv=2\),
so \((u-v)^2=-7\). A residue-class automorphism fixes \(u-v\)
exactly when it preserves \(\{1,2,4\}\), which gives the displayed
subgroup. Directly,
\[
                \sum_{a\in\Psi'}a=84,\qquad
       N_{E'/K_q}(\zeta_{28})=\zeta_{28}^{84}=1.
 \tag{G2}
\]
The other coset gives the same norm-one assertion. It is important
that this norm uses the induced G half, rather than the primitive
CM type \(\Phi'\), whose exponent sum is68.

At the selected degree-one G places, all residue fields are canonically
\(\mathbf F_q\) through their prime fields. For any global root
\(z\in\mu_{28}\), (G2) gives
\[
               \prod_{P\mid\bar\pi_G}(z\bmod P)=1
                                      \quad\hbox{in }\mathbf F_q^\times.
 \tag{G3}
\]
This is simply the reduction of its relative norm.

## 2. Prescribed compact characters and the exact congruence

Let \(g_0,g_1\) be two such G primes, with the source's selected
halves. For each choose a faithful residue character
\(\omega_\epsilon:\mathbf F_{g_\epsilon}^\times
 \to\mathbf C^\times\).
At stage \(i\), the literal source condition is
\[
        \chi_{i,P}=\omega_\epsilon^{\,2(i+1)}
                 \qquad(P\mid\bar\pi_{G,\epsilon}),
 \tag{G4}
\]
and the desired Hecke character \(\mu_i\) is required to be unitary,
trivial on \(\mathbb A_{F'}^\times\), tame, unramified outside
\(g_0g_1\), and to satisfy
\[
         \mu_{i,P}|_{\mathcal O_{E',P}^\times}=\chi_{i,P}^{-1}.
 \tag{G5}
\]
These are the IsMu0 conditions, before the independent odd-character
and arithmetic-kernel pins.

Let \(T'=\ker(N_{E'/F'}:\operatorname{Res}_{E'/F'}\mathbf G_m
\to\mathbf G_m)\), and \(K_0=(\widehat{\mathcal O}_{E'})^1\).
At a relative split finite place, projection to its selected E-prime
identifies the compact norm-one group with the local unit group.
Define a compact character \(\rho_i\) of \(K_0\) by
\[
       \rho_i(t)=
          \prod_{\epsilon=0}^1
          \prod_{P\mid\bar\pi_{G,\epsilon}}
                            \chi_{i,P}(t_P\bmod P)^{-1},
 \tag{G6}
\]
and take it to be one at every other finite place.
Equations(G3)–(G4) imply
\[
                         \rho_i|_{\mu_{28}}=1.
 \tag{G7}
\]

For any integer vector \(\mathbf e_i=(e_{i,a})_{a\in\Phi'}\),
let
\[
          \beta_i(t_\infty)=
                    \prod_{a\in\Phi'}\sigma_a(t_\infty)^{-e_{i,a}}.
 \tag{G8}
\]
This is a unitary character of \(T'_\infty\simeq U(1)^6\).
AM-R-009 proves
\[
 T'(\mathbb A_{F',f})=T'(F')K_0,\qquad
                          T'(F')\cap K_0=\mu_{28}.
 \tag{G9}
\]
Therefore \(\beta_i\rho_i\) descends to an automorphic character
of \(T'(\mathbb A_{F'})\) if and only if its restriction to
the diagonal roots is one. By(G7), the exact condition is
\[
 \boxed{\sum_{a\in\Phi'}a e_{i,a}\equiv0\pmod{28}.}
 \tag{G10}
\]
For a uniform vector \(e_{i,a}=e_i\), this is equivalent to
\[
                                7\mid e_i,
 \tag{G11}
\]
since \(\sum\Phi'=68\) and \(\gcd(68,28)=4\).

There is no further norm-one global-unit condition hidden here:
the full intersection in(G9) is precisely \(\mu_{28}\). This
uses the actual class-number-one torus decomposition, rather than
testing only one necessary root relation in an arbitrary CM field.

## 3. Explicit construction and necessity for the actual Hecke character

Assume(G10). Given a finite norm-one idele \(t_f\), write
\(t_f=\delta k\), with \(\delta\in T'(F')\), \(k\in K_0\),
using(G9), and set
\[
 \gamma_i(t_\infty,t_f)
       =\beta_i(\delta_\infty^{-1}t_\infty)\rho_i(k).
 \tag{G12}
\]
If another decomposition is used, the two rational factors differ
by an element of \(T'(F')\cap K_0=\mu_{28}\).
Equations(G7),(G10) make(G12) independent of that choice.
The formula is multiplicative, continuous, unitary, and trivial
on the diagonally embedded \(T'(F')\). It is therefore an actual
automorphic character.

Put \(j(x)=x/\bar x\) on ideles and define
\[
                              \mu_i(x)=\gamma_i(j(x)).
 \tag{G13}
\]
It is trivial on the base-field ideles. At infinity its restriction
is
\[
           \prod_{a\in\Phi'}
               \left(\frac{\sigma_a(x)}{|\sigma_a(x)|}\right)^{-2e_{i,a}},
 \tag{G14}
\]
which is exactly HasInfQ with exponent vector \(-\mathbf e_i\):
the source definition sets the integral angular exponent to twice
the HasInfQ entry. At a selected G-prime, an idele supported in
that E-component maps under \(j\) to the norm-one pair
\((x,x^{-1})\). Equations(G6),(G13) therefore give precisely(G5),
with its inverse sign. At other split places it is unramified.

At a nonsplit finite place the extension \(E'/F'\) is unramified,
and every norm-one element is a unit. Moreover every norm-one
unit is \(a/\bar a\) for a local unit \(a\): start with local
Hilbert90, then multiply its witness by a base-field uniformizer
power to make its valuation zero, using relative ramification
index one. Since \(\rho_i=1\) there, \(\gamma_i\) is the trivial
local torus character, and \(\mu_i\) is trivial on the entire
local multiplicative group. All required outside-G unramified
conditions follow. The G characters factor through residue units,
so tameness is exact. Their conductor is the one in LIFT17(F19).

Conversely, suppose a genuine \(\mu_i\) satisfies these exact
finite restrictions and HasInfQ\((-\mathbf e_i)\). The idele
map \(j:\mathbb A_{E'}^\times\to T'(\mathbb A_{F'})\) is
surjective by local Hilbert90, with kernel
\(\mathbb A_{F'}^\times\); the global rational version is also
surjective. Hence \(\mu_i\) descends to an automorphic \(\gamma_i\)
on \(T'\). At each relative split finite place its restriction
to \(K_0\) is forced by the unit character. At a nonsplit place
the preceding integral Hilbert90 argument shows that an unramified
\(\mu_i\) descends to a character trivial on the whole compact
torus. Thus \(\gamma_i|_{K_0}=\rho_i\), and its infinity character
is(G8). Rational triviality on \(\mu_{28}\) forces(G10).

This proves necessity as well as sufficiency. The conclusion is
about the exact IsMu0 finite and infinity conditions, with its
uniformizer values defined by the constructed character. It does
not allow independently prescribing incompatible muVal entries.

## 4. Concrete primes and a fixed coefficient field

For the actual minimal numerical choice \(k=6,m=2\), take
\[
 \begin{array}{c|c|c}
 q&\pi_G&\pi_G\bar\pi_G\\ \hline
 113&1+4\sqrt{-7}&113\\
 281&13+4\sqrt{-7}&281 .
 \end{array}
 \tag{G15}
\]
Both rational primes are \(1\bmod28\), so they split completely
in \(E'\). The elements are algebraic integers in \(K_q\).
Their conjugate ideals are coprime: a common prime would divide
both their norm \(q\) and their sum \(2\) or26, which is impossible.
Consequently they define the required six-element selected halves,
with residue fields \(\mathbf F_q\). Their lower size bound is
\[
            g_\epsilon-1>2\cdot6\cdot6=72.
\]
This verifies the displayed G-prime conditions used here. No
additional primitive-field D7 or etaT condition is inferred.

The faithful residue characters can take values in
\[
                              K=\mathbf Q(\zeta_{560}),
 \tag{G16}
\]
since \(560=\operatorname{lcm}(28,112,280)\).
This is a fixed degree192 cyclotomic field, independent of all
the stage weights. Formula(G12) also has algebraic finite values
in this field: the rational norm-one factor \(\delta\) belongs
to \(E'\), all its selected complex conjugates are Galois
conjugates in \(E'\), and its absolute values are one.
Thus the integer-power product \(\beta_i(\delta_\infty)\)
belongs to \(E'\); the remaining factor is a root of unity in
the displayed cyclotomic field.

This identifies actual finite character values, including values
on uniformizers, by a formula. It does not assert that all those
algebraic values are units at11. On compact units their values are
roots of unity and hence units at every finite place. Values on
noncompact determinant representatives require the separate
normalization in the class presentation.

For these two stages the exact conductor is
\[
       \mathfrak f(\mu_i)=31753\,\mathcal O_{E'},\qquad
                   N_{E'/\mathbf Q}\mathfrak f(\mu_i)=31753^{12}.
 \tag{G17}
\]
This conductor is independent of the size of \(\mathbf e_i\).
Its norm alone is not a complete H or a theta-row error term.

## 5. Nonempty source gap locus with the required character congruence

The compatibility condition does not force the numerical
Harish--Chandra gap locus to be empty. Here is a fully explicit
uniform example satisfying the numerical clauses of Hyp3.
Keep
\[
       k=6,\quad m=2,\quad r=7,\quad t=1795,\quad d=t+1=1796.
 \tag{G18}
\]
The source rank inequalities hold:
\(k,m\) are even, \(t\) is odd, \(m+3\le k\),
\(r+5\le t\), \(3m<t\), and
\(1801\le r+t=1802\). With the actual degree-six CM type count,
take its corresponding order parameter3, so \(m\le6\le k\).
The remaining displayed quadratic rank bound is immediate.

Choose any positive multiple \(C\) of7 satisfying
\[
                  C>(r+mt)^3+k+t+10.
 \tag{G19}
\]
At every one of the six embeddings define, with zero-based indices,
\[
 \begin{split}
 u_i&=(2(k-i)+1)C+\tfrac12
                                &&(0\le i<k),\\
 v_i&=2(k-i)C                    &&(0\le i<k-1),\\
 b_j&=(4j-2)C,\qquad e_j=4jC     &&(0\le j<m),\\
 \eta&=-\tfrac12 .
 \end{split}
 \tag{G20}
\]
The \(u_i\) are half-integral, the other parameters are integral,
and
\[
 u_i>v_i>u_{i+1},\qquad
 u_{k-1}=3C+\tfrac12>-b_0=2C,\qquad
 b_0<e_0<b_1<e_1.
\]
Every required centred distance is at least
\(\min(2C,4C-(t-1)/2)\), except for the positive \(u+e\) and
\(v+e\) distances, which are still larger. Thus each exceeds
\((t+3)/2\).

For NCGaps, the only false-sign element at stage0 is
\(-b_1=-2C\). The other \(b\)-element is \(2C\), and all
\(v_i\) are at least \(4C\), so every opposite-sign difference
is at least \(4C>(r+mt)^3\). At stages1 and2 every element
in the literal Dpar list has true sign, so the cross-sign
condition is empty. The common \(\eta\)-shift at odd stages
does not alter any difference. These statements directly check
the source definition in DataTheta.lean538–555 and
CayleySignature.lean106–118.

The splitting weights are \(e_0=0,e_1=4C\), both divisible by7.
Hence(G10) holds at both stages, and sections2–3 supply actual
global even characters with exactly the prescribed G residue
restrictions and no29 ramification. Their infinity exponents
are the required \(-e_j\). The selected first partition is
nonnegative: its smallest entry is \(3C-898>0\).
The degree and other selected real data are therefore genuine
finite quantities, although very large.

For a concrete integer, one may take
\[
 C=46539458987,\qquad
 (e_0,e_1)=(0,186157835948),\qquad
 (b_0,b_1)=(-93078917974,93078917974).
 \tag{G21}
\]
Here \((r+mt)^3=46539457173\), and(G19) holds.
The symbols \(e_j\) in(G20)–(G21) are the Harish--Chandra
splitting weights, not the DP44 error array.

The numerical \(\eta=-1/2\) matches an odd splitting character
with infinity exponent \(+1/2\). It does not supply the original
all-finite-unramified etaT pin, which AM-K028 separately
obstructs on this host. Thus this paragraph verifies the stated
numerical gap and character conditions, not a complete D7 instance.

## 6. What is now fixed and what remains

The even global characters are now explicit on a nonempty actual
parameter locus, with the literal G conductor, exact residue
characters, fixed coefficient field, and exact unit compatibility.
The conductor29 character choice of LIFT14 was convenient for its
spherical chain, but it is not needed for existence of these
different stage characters.

At a split G place, changing to these characters changes the local
theta parameters: the inserted rank-d block carries the stage
character with its nontrivial residue restriction. This is exactly
the kind of local change that the obstruction in LIFT17 requires.
It is not obtained by choosing another vector in the old spherical
constituent or by one uniform tame determinant twist.

To proceed to a chain with the prescribed column types, one must
identify the ramified local constituents and show that the
specified generic/determinant-block type and raw Xi map survive on
the previous image. Their levels, projection masses and integral
content remain to be calculated. Neither the existence of the
characters nor their fixed finite conductor proves that local
type occurrence, global prescribed-kernel nonvanishing, an
integral gain, or a shorter DP44 chain.

## Source and input locators

- AM-R-009, first_lift_unramified_host.md, equationR9.15 and its
  norm-one ideal proof: actual class-number-one torus
  decomposition and the complete root-unit intersection.
  Masley(1976) remains the checked class-number input.
- ALP-LIFT-17, sections4–7: exact source residue characters,
  G-prime conditions, size bounds, tameness and conductor.
- Formalism/LocalToGlobal/UnitaryNorms/IsUnitaryNormOf.lean,
  lines66–94: LevelLe, UnrAt, TameAt, HasInf and HasInfQ.
- Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean,
  lines205–224,273–306,315–323 and488: G halves, chi_om,
  IsMu0 and g_big.
- Formalism/LocalRingCardinality/DataTheta.lean, lines501–555,
  and Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean,
  lines106–125: the exact numerical parameter and gap conditions.
- AM-K028: the separate odd-character obstruction is carried,
  not used as a substitute for the even-character construction.

All recovered source paths are relative to
work/research/alpoge_source, pinned to commit
7cbf7a0c32fca1badf05931879a37c3f8a2b03b4.
No Lean build or complete source constructor is claimed.


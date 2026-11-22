# ALP-LIFT-19 — ramified theta constituents with the literal nonterminal column types

Author: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE. Written 21 November2026UTC.

This theorem repairs the local representation obstruction of ALP-LIFT-17. At a degree-one split G-place, start with an irreducible representation containing the finite Steinberg type, and use the distinct tame stage characters required by IsMu0. Every later local theta representation then contains the literal adelic column type, with the correct inverse character. An explicit finite induced vector is primitive in its natural coefficient lattice and has a computable positive Hermitian norm.

The theorem is local and independent of the degree of the global CM field. It therefore applies to the old degree12 host or to an enlarged host whenever the same degree-one G-place and stage-character hypotheses hold. The global character construction of LIFT18 is used only for its stated old host. No class-number-one assertion, G-prime example, or mass formula is silently transported to the degree84 repaired host.

The finite Steinberg representation, Casselman's Iwahori theorem, Zelevinsky's irreducibility criterion, and Mínguez's local theta theorem are literature inputs. The new work here is their exact assembly with the source columns, the explicit Mackey component and its primitive vector/norm, and the consequent removal of this specific local type obstruction. The literal raw PhiG/Xi kernel and the integral lattice of the iterated global image remain separate.

## 1. Local data and the source sign

Let F be a nonarchimedean local field of characteristic zero with residue field
\(\kappa=\mathbf F_q\). For the literal degree-one G places, q is the rational G prime. Put
\[
 K_n=\operatorname{GL}_n(\mathcal O_F),\qquad
 K_n^1=1+\varpi M_n(\mathcal O_F).
 \tag{T1}
\]
Fix integers \(k\ge1,t\ge1,m\ge2\), set \(d=t+1\), and write
\[
 n_j=k+jd=(k+j)+jt,\qquad r_j=k+j.
 \tag{T2}
\]
Let \(\eta_0,\ldots,\eta_{m-1}:F^\times\to\mathbf C^\times\)
be unitary tame characters whose residue characters
\(\bar\eta_i:\kappa^\times\to\mathbf C^\times\) are pairwise distinct and nontrivial.

At a selected source G-prime, IsMu0 and chi_om say exactly
\[
 \eta_i|_{\mathcal O_F^\times}
       =\chi_i^{-1},\qquad
 \chi_i=\omega^{\,2(i+1)},
 \tag{T3}
\]
where \(\omega\) is faithful. The source inequality \(q-1>2fk>2m\)
ensures the required nontriviality and distinctness. This is the
character condition already audited in LIFT17; LIFT18 constructs
actual global even characters with it on its specified weight locus
over the degree12 host.

The adelic column convention has an inverse. In the pinned source,
Columns/RecLevel.lean50–52 defines
\[
 \operatorname{levChr}(\lambda)=\lambda\circ\operatorname{levRed},
 \qquad
 \operatorname{levTyp}(\lambda)=\operatorname{levChr}(\lambda)^{-1}.
 \tag{T4}
\]
Consequently the desired adelic right-translation character at stage
\(j<m\) is \(\lambda_{X,j}^{-1}\), whose determinant-block factors
are the \(\bar\eta_i\) in(T3).

Choose a nontrivial additive character \(\psi:\kappa\to\mathbf C^\times\).
For \(0\le j<m\), define
\[
 \begin{split}
 H_j&=\bigl(U_{r_j}(\kappa)\times
                 \operatorname{GL}_t(\kappa)^j\bigr)N_{P_j},\\
 P_j&=P_{(r_j,t,\ldots,t)}\subseteq\operatorname{GL}_{n_j}(\kappa),\\
 \lambda_j(h_0,h_1,\ldots,h_j;n)
   &=\psi_{S_j}(h_0)^{-1}
                    \prod_{i=0}^{j-1}\bar\eta_i(\det h_{i+1}),\\
 S_j&=\{0\le a<k+j-1:\ a+1\ne k\text{ or }j+1=m\}.
 \end{split}
 \tag{T5}
\]
Here \(U_r\) is upper unitriangular, and \(\psi_S\) applies \(\psi\)
to the sum of the indicated simple-root entries. This is exactly
HX, SX and the inverse of lamX in
GenericUnipotentCharacter.lean437–452.
The character is trivial on \(N_{P_j}\).
For \(j=0\), it is the full generic character of \(U_k\).
For \(1\le j<m-1\), it omits only the root joining the first k
coordinates to the last j coordinates in \(U_{k+j}\).
For \(j=m-1\), it is fully generic in \(U_{k+j}\).
The terminal HXm case \(j=m\) is not included.

## 2. The exact local representation theorem

Let \(\pi_0\) be an irreducible admissible representation of
\(\operatorname{GL}_k(F)\) such that
\[
 \operatorname{St}_k(\kappa)\hookrightarrow\pi_0^{K_k^1}
 \quad\hbox{as }\operatorname{GL}_k(\kappa)\hbox{-modules}.
 \tag{T6}
\]
For \(j\ge0\), form normalized parabolic induction
\[
 \Pi_j=
 \pi_0\times(\eta_0\circ\det_{\operatorname{GL}_d})
       \times\cdots\times
                (\eta_{j-1}\circ\det_{\operatorname{GL}_d}).
 \tag{T7}
\]

**Theorem.** For every \(0\le j\le m\), the representation \(\Pi_j\)
is irreducible. For each \(0\le j<m\), \(\Pi_{j+1}\) is the actual
local theta descendant of \(\Pi_j\) under the literal bilinear Hom
convention with the same splitting character \(\eta_j\) on both
members of edge \(n_j\to n_{j+1}\).
For \(0\le j<m\), its finite column space is nonzero:
\[
                   \Pi_j^{\widetilde H_j,\lambda_j}\ne0,
 \tag{T8}
\]
where \(\widetilde H_j\) is the full inverse image of \(H_j\) in
\(K_{n_j}\). Thus the desired finite type occurs in the entire
actual ramified theta representation. This is the opposite local
conclusion from LIFT17's unramified chain.

### 2.1 Cuspidal support and irreducibility

The finite Steinberg representation has a one-dimensional
Borel-fixed subspace. For example, in its integral basis
\(\{u e:u\in U_k\}\), the vector \(\sum_u u e\) is fixed by
\(U_k\), and diagonal matrices permute its summands because they
fix e and normalize \(U_k\). Thus(T6) gives a nonzero Iwahori-fixed
vector in \(\pi_0\).

Casselman(1980), Proposition2.6, printed p.396, states that every
irreducible admissible representation with a nonzero Iwahori-fixed
vector embeds in an unramified principal series. Hence the cuspidal
support of \(\pi_0\) consists entirely of unramified characters of
\(F^\times\). This statement applies to \(\operatorname{GL}_k\),
including its center; Casselman's paper is formulated for connected
reductive groups.

The cuspidal support of the one-dimensional representation
\(\eta_i\circ\det_{\operatorname{GL}_d}\) is
\[
 \bigl\{\eta_i|\cdot|^{(1-d)/2},
             \eta_i|\cdot|^{(3-d)/2},\ldots,
                         \eta_i|\cdot|^{(d-1)/2}\bigr\}.
 \tag{T9}
\]
Its residue character is uniformly \(\bar\eta_i\).
The distinctness in(T3) therefore puts different factors of(T7)
on disjoint cuspidal lines; none meets the unramified support of
\(\pi_0\). No two segments from different factors can be linked,
since an unramified absolute-value twist does not change the residue
character.

Zelevinsky(1980), Proposition8.5, printed p.196, now says that the
product(T7) is irreducible. Its Proposition8.6, printed p.197,
records the equivalent factorization by distinct cuspidal lines.
This argument does not require \(\pi_0\) to be tempered or generic.
If \(\pi_0\) is unitary, so is(T7), because every inducing factor is
unitary and normalized parabolic induction preserves unitarity.

### 2.2 Identification with the actual theta descendant

At a relative split place, write the common unitary character as
\((\eta_j,\eta_j^{-1})\) on \(F^\times\times F^\times\).
The actual Hom oscillator carries the scalar
\[
             \eta_j(\det g)^{-1}\eta_j(\det h).
 \tag{T10}
\]
The source lift is bilinear, \(\int\theta(g,h)f(g)\,dg\), so the
untwisted type-II source representation is
\(\Pi_j^\vee\otimes\eta_j\).
Mínguez(2008), Theorem1(2), printed p.718, gives nonzero local theta
for every irreducible input in the smaller rank. Its target
Langlands quotient has the contragredient old parameters and the
parameters of the rank-d trivial representation. Restoring(T10)
therefore leaves the old \(\Pi_j\) block unchanged and inserts
\(\eta_j\circ\det_{\operatorname{GL}_d}\).

This identifies the target with(T7) for \(j+1\): the induced product
is irreducible by section2.1, and its Langlands quotient is precisely
the one in Mínguez's theorem. Equivalently its standard parameter is
the direct sum of the old parameter and(T9). This use of the
Langlands quotient is not an assertion that an arbitrary reducible
parabolic induction equals small theta.

The same convention was checked against the actual Hom action in
LIFT14(E10–E11) and AM-DO-028. The finite right-translation character
in(T4) is retained; no Hermitian-input convention is substituted.

It remains to prove(T8). We do so constructively.

## 3. A finite Mackey component adapted to the source columns

For this section write \(G=\operatorname{GL}_{n_j}(\kappa)\) and
\[
 Q=P_{(k,d,\ldots,d)},\qquad
 \mathcal M_j=
 \operatorname{Ind}_{Q}^{G}
       \left(\operatorname{St}_k\boxtimes
                  \bigboxtimes_{i=0}^{j-1}\bar\eta_i\circ\det_d\right).
 \tag{T11}
\]
Finite induction is unnormalized; its function model consists of
functions \(f:G\to V_{\operatorname{St}}\) with
\(f(qg)=\tau(q)f(g)\), acted on by right translation.

Give the Q blocks the coordinate order
\[
        A,\ L_0,T_0,\ L_1,T_1,\ \ldots,L_{j-1},T_{j-1},
 \qquad \dim A=k,\quad\dim L_i=1,\quad\dim T_i=t.
\]
Let w be the permutation sending the P-coordinate order
\[
            A,L_0,\ldots,L_{j-1},\ T_0,\ldots,T_{j-1}
\]
to this Q-coordinate order. Put \(H=w^{-1}Qw\cap P_j\).
The image of H in the Levi
\(L_{P_j}=\operatorname{GL}_{r_j}\times\operatorname{GL}_t^j\)
is exactly
\[
              R=P_{(k,1,\ldots,1)}
                       \times\operatorname{GL}_t^j.
 \tag{T12}
\]
This can be checked entry by entry. Within the first P-block,
the Q-upper-triangular conditions impose the parabolic blocks
\(k,1,\ldots,1\); every matrix with those conditions is allowed.
The T-block diagonal matrices are unrestricted.
Thus every element of R has a lift in H.

The representation \(\tau\) in(T11) is trivial on
\(w(H\cap N_{P_j})w^{-1}\). Indeed off-diagonal Q blocks act
trivially by inflation. Within \(L_i\oplus T_i\), the remaining
intersection has matrices
\(\left(\begin{smallmatrix}1&*\\0&I_t\end{smallmatrix}\right)\),
on which a determinant character is trivial. On the image R,
the action is
\[
 \operatorname{St}_k\boxtimes
     (\bar\eta_0,\ldots,\bar\eta_{j-1})
       \boxtimes
          \bigboxtimes_{i=0}^{j-1}\bar\eta_i\circ\det_t.
 \tag{T13}
\]

It follows that \(\mathcal M_j^{N_{P_j}}\) contains the component
\[
 \mathcal V_j\boxtimes
       \bigboxtimes_{i=0}^{j-1}\bar\eta_i\circ\det_t,\qquad
 \mathcal V_j=
 \operatorname{Ind}_{P_{(k,1,\ldots,1)}}^{\operatorname{GL}_{r_j}}
        (\operatorname{St}_k\boxtimes\bar\eta_0\boxtimes
                                  \cdots\boxtimes\bar\eta_{j-1}).
 \tag{T14}
\]
Here is an explicit proof, so a quotient in a Mackey filtration is
not mistaken for a submodule. Take functions in(T11) supported on
the finite double coset QwP_j and invariant under right
\(N_{P_j}\). Their restriction to wP_j is the induced-function
model from H to P_j. The trivial action of \(H\cap N_{P_j}\)
just proved makes such a function descend to \(L_{P_j}\).
Its left transformation law is exactly(T13) on R.
Conversely every induced function with that law inflates to P_j
and extends uniquely to QwP_j with the Q-equivariance of(T11),
and by zero elsewhere. These constructions are inverse and
\(L_{P_j}\)-equivariant. They give the actual subspace(T14).

This is the Mackey component whose intersection-size matrix has
entries k in the first-first position, one from each new Q block
in the first P block, t in its corresponding determinant block,
and zero elsewhere. No new free trailing block is used.

## 4. Generic and degenerate generic vectors in the first block

We use the following elementary finite induction observation.
Let \(R'=P_{(a_1,\ldots,a_s)}\subseteq\operatorname{GL}_r(\kappa)\),
and suppose each representation \(\sigma_i\) of
\(\operatorname{GL}_{a_i}(\kappa)\) has a vector for the chosen
generic upper-unitriangular character. Then
\(\operatorname{Ind}_{R'}^{\operatorname{GL}_r}
(\boxtimes_i\sigma_i)\) also has such a vector.

To prove it, take the permutation which reverses the order of
the blocks while preserving the internal order in each block.
Its conjugate parabolic meets \(U_r\) in the product of the
within-block upper-unitriangular groups, with the blocks in
reversed order. Choose the tensor of the given generic vectors.
Define an induced function on the corresponding \(R'wU_r\)
double coset by right multiplication with the desired generic
character, and zero elsewhere. The transformation law on the
stabilizer agrees with the tensor vector by construction, so the
function is well-defined and nonzero. It is a generic eigenvector
under right \(U_r\). This construction uses no averaging denominator.
It works with \(\psi^{-1}\) just as with \(\psi\).

The finite Steinberg representation is regular on \(U_k\)
(Steinberg1957, Theorem2(i), printed p.349), so it contains the
required \(\psi^{-1}\)-eigenvector. Applying the preceding observation
to(T14) proves the fully generic case \(j=m-1\).

For \(1\le j<m-1\), the source character omits the root at k.
Transitivity of finite induction rewrites \(\mathcal V_j\) as
\[
 \operatorname{Ind}_{P_{(k,j)}}^{\operatorname{GL}_{k+j}}
  \left(\operatorname{St}_k\boxtimes
      \operatorname{Ind}_{B_j}^{\operatorname{GL}_j}
                (\bar\eta_0\boxtimes\cdots\boxtimes\bar\eta_{j-1})\right).
 \tag{T15}
\]
The subspace supported on \(P_{(k,j)}\) and fixed by its radical
contains exactly the displayed Levi representation.
Its first factor has the generic \(\psi^{-1}\) vector; the second
has the generic \(\psi^{-1}\) vector by the preceding open-orbit
construction with all block sizes one.
Their tensor is therefore an eigenvector for the character of
\(U_{k+j}\) which is generic inside the k and j blocks and trivial
on the joining radical. That is precisely \(\psi_{S_j}^{-1}\).
Together with(T14), this proves
\[
                         \mathcal M_j^{H_j,\lambda_j}\ne0.
 \tag{T16}
\]
For \(j=0\), the same assertion is simply the generic Steinberg
vector. The proof treats both source branches exactly.

## 5. Passage to the actual p-adic representation

By Iwasawa decomposition, the compact function model of(T7)
restricts to induction from \(Q(F)\cap K_{n_j}\).
Taking \(K_{n_j}^1\)-invariants gives the exact finite induced model
\[
 \Pi_j^{K_{n_j}^1}\simeq
 \operatorname{Ind}_{Q(\kappa)}^{\operatorname{GL}_{n_j}(\kappa)}
       \left(\pi_0^{K_k^1}\boxtimes
                  \bigboxtimes_{i=0}^{j-1}\bar\eta_i\circ\det_d\right).
 \tag{T17}
\]
For clarity, right \(K_{n_j}^1\)-invariance means that a function on
K factors through its finite quotient. Its value is fixed by
\((Q\cap K_{n_j}^1)\), whose Levi projection is
\(K_k^1\times(K_d^1)^j\). These are exactly the coefficient invariants
in(T17). Conversely such a finite induced function inflates to K
and extends by Iwasawa; modulus characters are one on the compact
intersection. This proves the isomorphism rather than merely an
inclusion.

By(T6), the finite module(T11) embeds in(T17).
Equation(T16) proves(T8), completing the theorem.

## 6. A primitive finite vector and its exact norm

There is a useful quantitative statement before any global
automorphic integration. Let R be a ring of integers enlarged to
contain the values of \(\psi\) and the \(\bar\eta_i\).
Use the Steinberg lattice
\[
        \operatorname{St}_{k,R}
          =\bigoplus_{u\in U_k}R\,u e
          \ \subset R[\operatorname{GL}_k(\kappa)/B_k].
 \tag{T18}
\]
The basis and its integral realization are Steinberg's Theorem1;
the same statement over arbitrary coefficient rings is recorded
in Geck(2015), Theorem2.1. Give the flag permutation module its
Hermitian metric with flags orthonormal.

The generic vector
\(v_\psi=\sum_{u\in U_k}\psi_U(u)\,u e\), with the sign chosen
to give right type \(\psi_U^{-1}\), is primitive in(T18).
Its coefficients in that basis are roots of unity.
Moreover
\[
                     \|v_\psi\|^2=|U_k|=q^{k(k-1)/2}.
 \tag{T19}
\]
To see the norm directly, expand e as the alternating sum of
Weyl flags. For every Weyl element except the longest, its
\(U_k\)-stabilizer contains a simple-root subgroup on which
\(\psi_U\) is nontrivial, so the sum cancels.
Only the longest Bruhat cell remains; its \(|U_k|\) flags are
distinct and have coefficients of absolute value one.
This proves(T19). It does not assert that the whole basis
\(\{u e\}\) is orthonormal.

Give(T11) its normalized compact-induction metric
\[
                    \|f\|^2=\frac1{|G|}\sum_{g\in G}\|f(g)\|^2.
\]
The constructions in sections3–4 can be made over R with no
division. At one selected coset their value is \(v_\psi\);
at every nonzero coset it has the same norm, because the
Steinberg action is unitary and all character values have modulus1.
Hence they produce a primitive vector \(v_j\) in the natural
R-valued induced lattice with exact type \(\lambda_j\).

Its support size in \(Q\backslash G\) is
\[
 q^{\,d j(j-1)/2+\epsilon_j k j},\qquad
 \epsilon_j=
 \begin{cases}
  1,&j=m-1,\\
  0,&0\le j<m-1.
 \end{cases}
 \tag{T20}
\]
For \(j=0\) this means one coefficient. For \(j\ge1\), the fiber
of \(H\backslash P_j\to R\backslash L_{P_j}\) has
\[
        [N_{P_j}:H\cap N_{P_j}]=q^{t j(j-1)/2}.
\]
Indeed precisely the entries from \(L_\ell\) to \(T_i\) with
\(\ell>i\) are allowed in the P radical and forbidden by Q.
There are \(t\,j(j-1)/2\) such entries; all others are unrestricted.

In the fully generic first-block construction the open U orbit
has size
\[
 |U_{k+j}|/|U_k|=q^{kj+j(j-1)/2}.
\]
In the omitted-root construction(T15), the support lies in
\(P_{(k,j)}\) and its flag orbit is the longest cell for
\(\operatorname{GL}_j\), of size \(q^{j(j-1)/2}\).
Combining these counts proves(T20).

Write the Gaussian multinomial index as
\[
 \mathcal J_j(q)=[G:Q]
 =\frac{\prod_{s=1}^{k+jd}(q^s-1)}
        {\left(\prod_{s=1}^k(q^s-1)\right)
         \left(\prod_{s=1}^d(q^s-1)\right)^j}.
 \tag{T21}
\]
Every left Q coset has \(|Q|\) elements, so(T19)–(T21) give
\[
 \boxed{\|v_j\|^2=
       \frac{q^{\,k(k-1)/2+d j(j-1)/2+\epsilon_j k j}}
                       {\mathcal J_j(q)}.}
 \tag{T22}
\]
This is a norm of an explicit primitive finite vector, before
mapping into a chosen automorphic image lattice.
The embedding(T6) may be scaled to be an isometry on its finite
Steinberg copy, in which case the same norm holds in the compact
model(T17). Such an isometric scaling does not by itself identify
the arithmetic lattice inherited from a global coefficient row.

For \(11\nmid q\), let \(h=\operatorname{ord}_{11}(q)\) and
\(c=v_{11}(q^h-1)\). Put
\[
             D_q(n)=c\lfloor n/h\rfloor
                         +v_{11}(\lfloor n/h\rfloor!).
\]
The elementary lifting-the-exponent formula gives
\[
 v_{11}\mathcal J_j(q)
       =D_q(k+jd)-D_q(k)-jD_q(d),\qquad
 v_{11}(\|v_j\|^2)=-v_{11}\mathcal J_j(q).
 \tag{T23}
\]
Indeed only s divisible by h contribute to
\(\prod_{s=1}^n(q^s-1)\), and their valuations are
\(c+v_{11}(s/h)\). This displays an actual finite normalization
factor. It is not an assertion that the global theta row has that
content or that this factor is a DP44 gain.

## 7. Global use and remaining gates

For this section assume the rank gaps, selected real types and
angular weight inequalities of LIFT14, in addition to the local
hypotheses above. These global hypotheses are stronger than the
bare local inequalities \(k\ge1,t\ge1\).

The local theorem applies to any nonzero global first lift whose
initial local representations at all G places contain the finite
Steinberg type, and whose common stage characters have the literal
unit restrictions(T3). Such a first input is constructed on the
old degree12 host by the finite-type extension of AM-DO-030:
use a full-rank residue-matrix orbit to place the actual Steinberg
compact type in the auxiliary finite Schwartz vector, including
the determinant character in(T10); simultaneous multijet
interpolation supplies a permitted29 half-translate with nonzero
selected kernel coefficient; compact Schur orthogonality then
extracts an actual nonzero first lift. The exact extraction and
normalizations belong to AM-DO-033, rather than being inferred from
finite type occurrence alone.

For later edges the analytic induction of LIFT14 carries over
after enlarging its omitted finite set S to include the G primes.
All nonsplit local components and their fixed spherical tests are
unchanged. Every G place is split, so Mínguez supplies local
occurrence there. Outside S the same standard-parameter recurrence
holds, and the partial Rallis factor remains
\[
 L_{E}^{S}\!\left(\frac{d+1}{2},
             \operatorname{BC}(\pi_0)\mu_j^{-1}\right)
       \prod_{r<j}\prod_{\ell=1}^{d}L_E^{S}(\ell,\mu_r\mu_j^{-1}).
 \tag{T24}
\]
Here BC denotes the unramified standard parameters, as in LIFT14,
not a new global base-change theorem.
The initial factor converges absolutely by the same crude unitary
bound and source rank gap. Each ratio has nontrivial angular
infinity type, so the \(\ell=1\) factors are finite and nonzero
by the checked boundary argument in LIFT14; all other factors are
in their absolutely convergent range.

Thus the same Rallis proof gives nonzero later lifts with
unrestricted finite Schwartz vectors, with the selected real
Schur component retained. Its joint-kernel proof continues to
apply to each actual automorphic multiplicity copy. At the G
places every constituent has the local form(T7), for its own
initial ancestor, and hence contains(T8).

One can consequently choose nonzero stage vectors of the exact
nonterminal finite column type. To justify this selection, take
the product of the compact character projectors at the finitely
many G places. If it killed every finite translate of a nonzero
cyclic automorphic submodule, that submodule could have no
constituent containing the corresponding local types, contrary
to(T8). Therefore some finite translate followed by the projector
is nonzero. These operations commute with the selected real
type and are absorbed into the preceding finite Schwartz input
by Weil equivariance. The output remains in the actual generated
previous theta image.

This assertion does not impose a predetermined raw PhiG, PhiGS
or Xi vector. A local type can occur while a particular local
intertwiner vanishes on the previous image; an integral projector
can also change content. Nor does it establish the terminal HXm
condition, the odd etaT pin on the old host, the full arithmetic
D7 constructor, or the six comparison identities.
The degree84 host needs its own global even stage characters
and first finite-type extraction hypotheses before this
conditional transfer can be invoked there.

The new local primitive vector(T22) and the first extraction
normalizations do not compute the later global image lattice.
The missing quantitative object remains the class-integrated
selected theta matrix restricted to that prior image, with the
source's fixed row normalization. Its saturation, coefficient
denominators, levels and archimedean size determine the actual
\(g_j,e_j,H\) required by DP44.

## 8. Finite diagnostic and scope of verification

The exact certificate ramified_column_type_certificate.py checks
the first nonterminal model \(k=j=t=1\) over both
\(\mathbf F_3\) and \(\mathbf F_5\), with a nontrivial quadratic
determinant character. It verifies every matrix-line covariance
identity for the constructed vector, its support and the norm
in(T22), and the character-projector multiplicity. The generic
branch has multiplicity1; the omitted-root branch has multiplicity2.
The latter corrected an initial auxiliary test expectation of
multiplicity1. No uniqueness claim is used or made in the theorem.

The same certificate verifies the forbidden-entry root count in
100 small block configurations and(T23) against exact integer
Gaussian multinomials in1344 cases. These finite checks support
the sign and normalization; the general local and global proofs
are the arguments above. No Lean compilation, raw-Xi realization
or global integral saturation check is claimed.

## Primary sources and exact source locators

- Casselman, W. (1980). The unramified principal series of p-adic groups. I. The spherical function. Compositio Mathematica, 40(3), 387–406. Propositions2.4 and2.6, printed pp.395–396. https://numdam.org/item/CM_1980__40_3_387_0.pdf.
- Geck, M. (2015). On the l-modular composition factors of the Steinberg representation. arXiv:1504.04157v2. Theorem2.1, printed p.3, and Corollary2.3, printed pp.4–5. This records the integral Steinberg basis and proves the Borel-fixed line. https://arxiv.org/pdf/1504.04157.
- Mínguez, A. (2008). Correspondance de Howe explicite: paires duales de type II. Annales Scientifiques de l'École Normale Supérieure, 41(5), 717–741. Theorem1, printed p.718, and equation(1.4), pp.721–722. https://www.numdam.org/item/ASENS_2008_4_41_5_717_0.pdf.
- Steinberg, R. (1957). Prime power representations of finite linear groups II. Canadian Journal of Mathematics, 9, 347–351. Theorems1–2 and the integral-basis corollary, pp.348–350. https://doi.org/10.4153/CJM-1957-041-1. Original PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1A82E966D7A0832A4FD80689E5F67CAE/S0008414X00044709a.pdf/prime-power-representations-of-finite-linear-groups-ii.pdf.
- Zelevinsky, A. V. (1980). Induced representations of reductive p-adic groups. II. On irreducible representations of GL(n). Annales Scientifiques de l'École Normale Supérieure, 13(2), 165–210. Proposition8.5, p.196; Proposition8.6, p.197. https://www.numdam.org/article/ASENS_1980_4_13_2_165_0.pdf.

Pinned source root: work/research/alpoge_source, commit
7cbf7a0c32fca1badf05931879a37c3f8a2b03b4.

- Formalism/LocalToGlobal/Columns/RecLevel.lean50–52: exact inverse adelic type.
- Formalism/LocalToGlobal/Columns/GenericUnipotentCharacter.lean437–452: HX, SX, lamX, including omitted-root branch.
- Formalism/LocalToGlobal/Columns/ColForms.lean92–105: literal colLev and ColV.
- Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean273–306,315–323,488: chi_om, distinctness, IsMu0 and g_big.
- AM-DO-028: actual Hom/bilinear splitting dictionary.
- AM-DO-030/033: fixed auxiliary multijet and finite-type first extraction.
- ALP-LIFT-14: later selected global analytic induction, including its every-vector and multiplicity scope.


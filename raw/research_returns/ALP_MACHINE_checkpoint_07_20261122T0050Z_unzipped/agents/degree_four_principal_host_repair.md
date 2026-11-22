# AM-K032 — an actual product principal host with degree divisible by eight

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 22 November 2026 UTC; inherited reasoning effort not separately exposed.

The degree-seven construction of AM-K029/030 repairs the odd character but has real degree42. This finding supplies an explicit further real extension of degree4, together with an exact polarized product identification. The resulting host is the actual principally polarized variety \(J^{56}\), with full integral CM action, real degree168, and \(8\mid168\). Its odd character, all uniform even stage characters, and the permitted alpha half-orbit persist. The primitive-type common-field obstruction remains: the source's defined Fields.Kq is still \(\mathbb Q\). Consequently this is not a complete D7 constructor or a MainX estimate.

The new ingredient is elementary weighted trace linear algebra. No classification of positive unimodular lattices and no uncomputed class group is needed.

## 1. Two exact rank-two weighted trace forms

For \(a\in\{1,3\}\), put
\[
 d_a=a^2+4,\qquad R_a=\mathbb Q(\sqrt{d_a}),\qquad
 u_a=\frac{a+\sqrt{d_a}}2,
 \qquad \delta_a=\frac{u_a^{-1}}{\sqrt{d_a}}.
\tag{QH1}
\]
Thus \((d_1,d_3)=(5,13)\). Each \(d_a\) is a squarefree discriminant congruent to1 modulo4. The ring of integers is
\[
                 \mathcal O_{R_a}=\mathbb Z[u_a],
           \qquad u_a^2-au_a-1=0,
           \qquad u_a^{-1}=u_a-a.
\tag{QH2}
\]
For a=3, the generator differs by1 from the usual \((1+\sqrt{13})/2\), so it gives the same integral ring. The discriminant of the displayed basis is \(d_a\).

### Proposition QH3

The element \(\delta_a\) is totally positive, generates the inverse different of \(R_a/\mathbb Q\), and satisfies
\[
 \operatorname{Tr}_{R_a/\mathbb Q}(\delta_a)=1,\qquad
 \operatorname{Tr}_{R_a/\mathbb Q}(\delta_a u_a)=0,\qquad
 \operatorname{Tr}_{R_a/\mathbb Q}(\delta_a u_a^2)=1.
\tag{QH3}
\]
Thus the weighted trace form \((x,y)\mapsto\operatorname{Tr}(\delta_a xy)\) has matrix \(I_2\) in the **integral** basis \((1,u_a)\). Multiplication by \(u_a\) in that basis is the symmetric integral matrix
\[
                         M_a=\begin{pmatrix}0&1\\1&a\end{pmatrix}.
\tag{QH4}
\]

**Proof.** Write \(s=\sqrt{d_a}>a>0\) in the positive embedding. Then
\[
 \delta_{a,+}=\frac{s-a}{2s}>0,\qquad
 \delta_{a,-}=\frac{s+a}{2s}>0.
\tag{QH5}
\]
Their sum is1. Since \(\delta_a u_a=1/\sqrt{d_a}\), its trace is0. Since \(\delta_a u_a^2=u_a/\sqrt{d_a}\), its trace is1. This proves all three entries of the Gram matrix. In particular the integral lattice is selfdual for the weighted trace form, so
\(\delta_a\mathcal O_{R_a}=\mathfrak D_{R_a/\mathbb Q}^{-1}\) by the definition of the inverse different. This also follows from the derivative \(2u_a-a=\sqrt{d_a}\) and the unit \(u_a^{-1}\), but the Gram computation already proves it directly. The multiplication matrix follows from \(u_a^2=1+au_a\). Finally
\[
                    N_{R_a/\mathbb Q}(\delta_a)=1/d_a.
\tag{QH6}
\]
All statements are exact. ∎

Let \(R=\mathbb Q(\sqrt5,\sqrt{13})\). Coprimality of the two discriminants implies
\[
 \mathcal O_R=\mathcal O_{R_1}\otimes_{\mathbb Z}\mathcal O_{R_3},
 \qquad [R:\mathbb Q]=4,\qquad d_R=5^2 13^2.
\tag{QH7}
\]
In the basis
\[
                     1,\ u_1,\ u_3,\ u_1u_3,
\tag{QH8}
\]
the form \(\operatorname{Tr}_{R/\mathbb Q}(\delta_1\delta_3xy)\) is \(I_4\). The two generating actions are commuting symmetric integral Kronecker matrices. These facts follow by multiplying the two trace identities, and the certificate checks the four-by-four matrices explicitly.

## 2. Tensoring the actual CM lattice

Retain the notation and the **actual** polarized product construction of AM-K030:
\[
 \begin{split}
 E_0&=\mathbb Q(\zeta_{28}),\qquad
 B\subset\mathbb Q(\zeta_{29}),\quad[B:\mathbb Q]=7,\\
 K&=E_0B,\quad F=K^+,\quad [K:\mathbb Q]=84,\\
 \mathcal A_B&=\pi_B^{-3}\mathcal O_B,
 \qquad \pi_B=N_{\mathbb Q(\zeta_{29})/B}(1-\zeta_{29}),\\
 \Lambda&=\mathcal O_{E_0}\otimes\mathcal A_B
               =\pi_B^{-3}\mathcal O_K,\qquad
 \xi_0=\frac{\zeta_7-\zeta_7^{-1}}{14}.
 \end{split}
\tag{QH9}
\]
The carried lattice \((\Lambda,\operatorname{Tr}_{K/\mathbb Q}(\xi_0x\bar y))\) is exactly the product principal CM lattice of \(J^{14}\), by the explicit trace-orthonormal basis of \(\mathcal A_B\). Its type is induced from \(\Phi_0=\{1,3,9,15,17,23\}\) and contains every real B-lift.

Set
\[
                  K^*=KR,
              \qquad F^*=FR.
\tag{QH10}
\]
The discriminants of K and R are coprime, and K is unramified at5 and13. Thus the fields are linearly disjoint and
\[
 \begin{gathered}
 [K^*:\mathbb Q]=336,\qquad [F^*:\mathbb Q]=168,\\
 \mathcal O_{K^*}=\mathcal O_K\otimes\mathcal O_{R_1}
                               \otimes\mathcal O_{R_3}.
 \end{gathered}
\tag{QH11}
\]
For completeness, any nontrivial subfield of the biquadratic R contains one of \(\mathbb Q(\sqrt5),\mathbb Q(\sqrt{13}),\mathbb Q(\sqrt{65})\), all ramified at5 or13; hence K cannot intersect R nontrivially. The integral tensor assertion is the coprime-discriminant lemma, applied twice.

Define
\[
 \Lambda^*=\Lambda\otimes\mathcal O_{R_1}\otimes\mathcal O_{R_3}
                   =\pi_B^{-3}\mathcal O_{K^*},
 \qquad
 E^*(x,y)=\operatorname{Tr}_{K^*/\mathbb Q}
                       (\xi_0\delta_1\delta_3x\bar y).
\tag{QH12}
\]
Use every extension of each old CM embedding to K*, so the new type has four lifts of each of the42 old embeddings.

### Theorem QH13

The CM lattice (QH12) is an actual product principal polarization:
\[
                    (A^*,L^*)\simeq
                       (J,L_{2\infty})^{56}
\tag{QH13}
\]
as principally polarized abelian varieties. It has a full action of \(\mathcal O_{K^*}\), with Rosati involution equal to complex conjugation. The CM extension \(K^*/F^*\) is unramified at every finite prime. On the standard lattice \(\mathcal O_{K^*}\), the coefficient of its alternating trace form is
\[
                    \boxed{\xi^*=\xi_0\pi_B^{-6}\delta_1\delta_3.}
\tag{QH14}
\]

**Proof.** Decompose an element of \(\Lambda^*\) in the four-element real basis (QH8), with coefficients in \(\Lambda\). Taking the trace first over the two quadratic extensions and applying (QH3) kills the mixed terms and leaves the sum of four copies of the old alternating trace form. Consequently the lattice is the orthogonal direct sum of four old principal symplectic lattices. Since all four real lifts of each old holomorphic embedding are chosen, the corresponding complex structure is the product complex structure. This proves (QH13), not merely an isogeny statement. Positivity is also immediate either from this product identification or from the total positivity of both \(\delta_a\).

The two new integral actions are the matrices (QH4), tensored with identity matrices; they commute with each other and with the old \(\mathcal O_K\)-action. Their tensor ring is the full integer ring in (QH11). They are selfadjoint because their matrices are symmetric in the product principal lattice. The old Rosati involution is conjugation; together these facts give conjugation on the full K* action. The CM type is the asserted induced type.

The extension K/F is finite-unramified by AM-K029/030. Finite étale quadratic algebras remain étale under base change. Applying this to F*/F proves the finite-unramified assertion. The quadratic base change is still a field: F* is totally real, whereas a generator of the quadratic CM extension K/F cannot lie in a totally real field.

Finally, write \(x=\pi_B^{-3}x'\) and \(y=\pi_B^{-3}y'\) in (QH12). The element \(\pi_B\) is real, so the coefficient becomes (QH14). This multiplication transports the entire lattice and form; it is not an assertion that the coordinate factor is a unit at29. ∎

As an independent norm/discriminant check,
\[
 \begin{split}
 |d_{K^*}|&=|d_K|^4d_R^{84}
      =2^{336}7^{280}29^{288}5^{168}13^{168},\\
 N_{K^*/\mathbb Q}(\xi^*\mathcal O_{K^*})
      &=|d_{K^*}|^{-1}.
 \end{split}
\tag{QH15}
\]
The latter is the norm of the inverse different ideal. Equivalently, the principal trace-dual lattice calculation already shows that \(\xi^*\mathcal O_{K^*}=\mathfrak D_{K^*/\mathbb Q}^{-1}\).

## 3. Actual line, gauge, eigenbasis and finite coordinate costs

The trace-one element
\[
                 w_0=-(\zeta_7+\zeta_7^2+\zeta_7^4),
                      \qquad w_0+\bar w_0=1,
\tag{QH16}
\]
acts diagonally on all56 ordinary J factors. Under the polarized product identification, its symmetric trace-one line is the external product of \(L_{2\infty}\). One way to fix the symmetric representative is to use its invariance under \(\zeta_7\): the endomorphism \(\zeta_7-1\) is invertible on the two-torsion, so the principal polarization has a unique symmetric representative fixed by this action. This is the same argument used for the actual source line in ALP-LIFT-07/08 and K030.

Transport the already fixed product section, rather than introducing a new unconstrained section. With the notation of AM-R-006 and K030 its reduced germ is
\[
                    c^{56}\prod_{\ell=1}^{56}\sigma_q(u_\ell),
\tag{QH17}
\]
and its origin multiplicity is112. Here \(\sigma_q\) is the actual q-normalized principal germ and c is the fixed derivative-Thomae scalar. The transported principal section is primitive at11 by the carried finite normalization; no theta-null unit at the origin is claimed, since the section vanishes there.

To compare the new CM coordinates, first retain K030's trace-orthonormal B coordinates z, whose Hermitian form has coefficient \(1/(2G_i)\) on each old E₀ label \((i,\pm)\) and B embedding. For one new quadratic extension, the two ordinary product coordinates \((z_0,z_1)\) become
\[
 \begin{pmatrix}z_+\\z_-\end{pmatrix}
      =V_a\begin{pmatrix}z_0\\z_1\end{pmatrix},
 \quad
 V_a=\begin{pmatrix}1&u_{a,+}\\1&u_{a,-}\end{pmatrix},
 \quad \det V_a=-\sqrt{d_a}.
\tag{QH18}
\]
This is the embedding matrix of (1,u_a), and
\[
     V_a^{\mathsf t}
           \operatorname{diag}(\delta_{a,+},\delta_{a,-})V_a=I_2.
\tag{QH19}
\]
In particular it is a **weighted** identity. The unrescaled V_a is not asserted to be orthogonal. After both extensions the Hermitian form is exactly
\[
       H=\sum_{i,\pm,k,\epsilon,\epsilon'}
          \frac{\delta_{1,\epsilon}\delta_{3,\epsilon'}}{2G_i}
                      |z_{i,\pm,k,\epsilon,\epsilon'}|^2.
\tag{QH20}
\]
The positive square-root rescaling by
\(\sqrt{\delta_{1,\epsilon}\delta_{3,\epsilon'}}\)
is an archimedean isometry to the product metric. Formula (QH20), rather than an untracked scalar bound, is the appropriate input for the selected Fock norm.

Both V_a and V_a^{-1} are integral at11, since the u_a are algebraic units and their determinants are11-units. Combined with K030's B comparison and the old \(\pm i\) comparison, the full K* eigenbasis is therefore an integral invertible change of the primitive ordinary J tangent basis at11. The central \(\zeta_7\) still has holomorphic labels1,2,3. Their pairwise sums never vanish modulo7, including repeated factors. Thus AM-K018's uniqueness proof for the full-CM canonical/source gauge applies to this ordinary product. This supplies the same gauge comparison for (QH17); no extension to a product with conjugated J factors is asserted.

The additional finite coordinate costs are explicit:

| Prime | Additional effect from \(R/\mathbb Q\) |
|---|---|
| 11 | V_a and its inverse are integral invertible; all \(\delta_a\) are units |
| 29 | No new denominator from V_a; the B and standard-lattice \(\pi_B^{\pm3}\) factors of K030/DO034 remain |
| 5 | Entries of \(V_1^{-1}\) have valuation \(-1/2\), normalized by \(v_5(5)=1\); the other V is invertible integral |
| 13 | Entries of \(V_3^{-1}\) have valuation \(-1/2\); the other V is invertible integral |
| Other primes | Both new embedding matrices and their inverses are integral invertible |

Indeed
\[
 V_a^{-1}=\frac1{u_{a,-}-u_{a,+}}
              \begin{pmatrix}u_{a,-}&-u_{a,+}\\-1&1\end{pmatrix}.
\tag{QH21}
\]
At the discriminant prime every numerator entry is a unit and the denominator has valuation1/2. Thus transforming a homogeneous degree-D polynomial from new eigen-derivatives to the ordinary product derivatives has additional coefficient denominator at most D/2 at5 and at13. This is an upper bound for the coordinate change, not a claim that an actual selected theta value attains it. The old dyadic and29 costs are retained. The explicit metric (QH20) and these local changes must be included when extending DO034's selected polynomial calculation; they are not removed by the11-unit comparison.

## 4. Exact ranks, conductor and explicit full-congruence G primes

The smallest real extension degree h making \(8\mid42h\) is4. The present construction realizes it. The exact source f_le_k therefore requires
\[
       \boxed{f=168,\qquad \operatorname{ord}=84,\qquad k\ge168.}
\tag{QH22}
\]
The abstract Frame can again use its parameter e=0 and distinguished element0. Its group may be \(C_{21}\times C_2\times C_2\), of order84. Its quotient to HGrp(0) is trivial and satisfies the literal Frame clauses. In fact
\(\operatorname{Gal}(K^*/\mathbb Q)\simeq C_2^4\times C_{21}\), compatible with an abstract \(G_0\times A\) decomposition. This observation alone does not construct the source's full field/type record.

For m=2 and k=168, take
\[
 \begin{gathered}
 t=1633,\quad r=169,\quad d=1634,\quad r+t=1802,\\
                    (N_0,N_1,N_2)=(168,1802,3436).
 \end{gathered}
\tag{QH23}
\]
All source rank inequalities hold. Substituting these ranks in K031's same numerical parameter formula gives
\[
 \begin{gathered}
 S=3435,\quad S^3=40\,530\,337\,875,\quad
 C=S^3+k+t+11=40\,530\,339\,687,\\
 u_i=(337-2i)C+\tfrac12,\quad
 v_i=(336-2i)C,\quad
 (b_0,b_1)=(-2C,2C),\quad(e_0,e_1)=(0,4C).
 \end{gathered}
\tag{QH24}
\]
The identical proof verifies every numerical parity, interlace, centred and NCGaps clause of Hyp3 with \(\eta_{\rm num}=-1/2\). The certificate separately checks the actual new finite lists. The source selected recurrence yields
\[
 \begin{split}
 \nu_{0,i}&=(337-2i)C+i-984\quad(0\le i<168),\\
 \min_i\nu_{0,i}&=3C-817>0,\qquad
 \Delta=4C-1634,\qquad
 \nu_1=(\nu_0+\Delta,\Delta^{1634}).
 \end{split}
\tag{QH25}
\]
The actual new selected polynomial must use all168 CM blocks. The highest bideterminant construction in DO034 is defined separately at each CM place and therefore gives a polynomial in these168 blocks by the same formula; its diagonal coefficient remains one. DO034's saved first-extraction theorem is stated for42 places. Extending its global formula requires the present quadratic metric data and new local indices, rather than silently retaining its numerical exponents. Equations (QH20)–(QH21) supply those additional metric/coordinate data; the separate first-lift analysis retains responsibility for that extension.

The rational conductor is exactly
\[
                         N^*=812\cdot5\cdot13=52\,780.
\tag{QH26}
\]
Containment in \(\mathbb Q(\zeta_{52780})\) follows from the three cyclotomic containments. Conversely, containment in any cyclotomic field forces divisibility by812 by K031, and ramification of the two new quadratic subfields forces divisibility by5 and13. This is exactly the source's minimum-divisibility IsCond criterion.

The following explicit primes satisfy the full new congruence:
\[
 \begin{array}{c|r|l}
 i&g_i^*&\pi_i^*\\\hline
 0&22\,285\,932\,761&52\,781+52\,780\sqrt{-7}\\
 1&64\,072\,175\,441&211\,121+52\,780\sqrt{-7}.
 \end{array}
\tag{QH27}
\]
The finite certificate checks primality by direct trial division through the integer square roots149284 and253124, respectively. It also checks
\[
 \pi_i^*\bar\pi_i^*=g_i^*,\qquad
 \pi_i^*\equiv1\pmod{52780\mathcal O_{\mathbb Q(\sqrt{-7})}},\qquad
 g_i^*\equiv1\pmod{52780},\qquad
                 g_i^*-1>2\cdot168^2=56\,448.
\tag{QH28}
\]
The conjugate ideals are coprime because
\(\gcd(g_i^*,2\operatorname{Re}\pi_i^*)=1\).
The primes split completely in K*, and each chosen half contains168 degree-one primes. Thus the actual norm, full PiGCong, residue cardinality and G-size clauses are met in the same external quadratic subfield as K031. The literal piG_Kq clause is still not met.

For faithful residue characters one may use primitive roots3 and6 at the two primes. The certificate verifies their order from the complete factorizations of \(g_i^*-1\). The common residue-root field can be chosen using
\[
 L^*=\operatorname{lcm}(28,g_0^*-1,g_1^*-1)
                  =13\,526\,981\,751\,068\,240.
\tag{QH29}
\]
This explicit coefficient extension is large; no claim that its degree or arithmetic height is negligible is made.

## 5. Actual characters and the unchanged permitted family

Let \(\eta\) be K029's actual odd character on K. Define
\[
                    \eta^*=\eta\circ N_{K^*/K}.
\tag{QH30}
\]
By the norm-compatibility proof in K029, this character is unitary, finite-unramified, has angular exponent1 at each new CM embedding, and restricts to \(\eta_{K^*/F^*}\) on \(\mathbb A_{F^*}^\times\). Its normalized etaVal values lie in one finite coefficient field: at a prime P of residue degree f over p, the normalized value is the f-th power of the old normalized value. A norm of a local uniformizer has valuation f; its unit factor is killed by the unramified character, so no choice of uniformizer affects this assertion.

For any integers e_j choose the LIFT18 finite-order zero-infinity characters \(\nu_j\) of E₀ at the primes (QH27), and set
\[
         \boxed{\mu_j^*=(\nu_j\circ N_{K^*/E_0})(\eta^*)^{-2e_j}.}
\tag{QH31}
\]
The full proof is HC16–21 of K031 and applies verbatim: every new G completion is the same degree-one \(\mathbb Q_{g_i^*}\), so its local norm is the identity; the even eta power changes infinity weight while changing no compact unit character. Hence all exact uniform IsMu0 clauses hold, without a divisibility condition on e_j and without a large-field class-number assumption. A single finite field contains all muVal and etaVal values. For j=0,1 the exact conductor is
\[
     \mathfrak f(\mu_j^*)=g_0^*g_1^*\mathcal O_{K^*},
       \qquad N\mathfrak f(\mu_j^*)=(g_0^*g_1^*)^{336}.
\tag{QH32}
\]
Qualitative T-prime choices use K031's ray-class construction with modulus \(52780(g_0^*g_1^*)^2\); no quantitative upper window is inferred.

The same central element
\[
           \alpha=(1+2\sqrt{-7})^e,\qquad M=29^e,
                    \alpha\bar\alpha=M
\tag{QH33}
\]
acts diagonally on all56 J factors and is congruent to1 modulo2. Its conjugate ideal remains coprime. Therefore on an edge of ranks a,b the permitted product DP59 basis is exactly the h=4 instance of K031:
\[
 \begin{gathered}
 X=(A^*)^{ab}=J^{56ab},\quad \dim X=168ab,\\
 \mathcal W_M=[\alpha]^*H^0(X,\mathcal L^M),
       \quad\operatorname{rank}\mathcal W_M=M^{168ab},\\
 \mathcal L=(L^*)^{\boxtimes ab},\qquad
 t'\in X[\alpha^2]/X[\alpha],\qquad Mt'\in X[\alpha].
 \end{gathered}
\tag{QH34}
\]
The ordinary D-jet threshold remains \(M\ge3D+2\), and each individually selected finite translate has norm1. The auxiliary multijet threshold in DO030 is unchanged under its stated coprimality assumptions. The selected highest-symbol factorial bound is K022's bound in the new integral eigenbasis. It does not transfer an old six-place sharp directional witness to one new full-CM selected weight.

At29 both real quadratics split, as witnessed by
\[
                       11^2\equiv5\pmod{29},\qquad
                       10^2\equiv13\pmod{29}.
\tag{QH35}
\]
Thus F* has24 primes over29, each with ramification index7 and residue field \(\mathbb F_{29}\), and all are split in K*/F*. The rational principal-level index in a rank-a split unitary factor is consequently
\[
        \boxed{I^*(M,a)=M^{168a^2}
                       \prod_{i=1}^a(1-29^{-i})^{24}.}
\tag{QH36}
\]
This follows from
\(|\operatorname{GL}_a(\mathcal O_v/29^e)|
 =29^{7ea^2}\prod_{i=1}^a(1-29^{-i})\)
at each of24 places. It is the rational principal-level factor, not a substitution for every source level or the prescribed ramified G-column index. The latter uses the new primes,168 selected places at each G, and the separate LIFT19/DO034 formulas.

## 6. The remaining constructor obstruction

The source's eight_dvd condition is now fulfilled by the actual host. The source's common-field requirement is not. The induced type includes every R- and B-lift of each E₀ embedding. If every selected embedding agrees on x, agreement across all lifts first forces \(x\in E_0\); the automorphisms3 and17 in \(\Phi_0\) then force \(x\in\mathbb Q\), exactly as in K031(HC28). Hence
\[
                       \mathrm{Fields.Kq}=\mathbb Q.
\tag{QH37}
\]
This restates the already identified primitive-type obstruction on the new host. Neither the larger field nor the odd character changes it. In particular the external \(\mathbb Q(\sqrt{-7})\) containing the explicit prime generators cannot be relabeled as the source-defined common quadratic field.

The completed pieces are therefore an actual principal CM product host with8-divisible real degree, a literal odd Hecke character, all uniform even character conditions, explicit rank/prime/congruence data, and the unchanged permitted half-orbit. The source's full field/type record, exact later selected image, prescribed raw-Xi chain and quantitative MainX window remain separate. This finding makes no conclusion about GRH or a Kummer extension of the accepted theorem.

## 7. Primary and exact input locators

- Milne, J. S. (2020). *Algebraic number theory* (Version3.08), Example2.41, printed p.39, for quadratic integer rings and discriminants; Lemma6.5, printed p.100, and Remark6.6(c), printed p.101, for the coprime-discriminant integral tensor and discriminant formula. Primary author PDF: https://www.jmilne.org/math/CourseNotes/ANT.pdf. The weighted trace identity itself is proved in full in (QH3)–(QH6).
- AM-K029/030: the actual finite-unramified degree-seven CM host, odd character, trace-orthonormal inverse-different basis and full principal product identification. AM-K031 HC1–28: source numerical records, character norm pullback, permitted isogeny and exact common-field scope.
- Formalism/LocalRingCardinality/Params.lean:6–22; Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean:59–76,108–125,206–238,310–331,486–494,560–579; Formalism/LocalToGlobal/UnitaryNorms/IsUnitaryNormOf.lean:66–94: the exact unmodified field, character, degree and rank clauses. Paths are relative to work/research/alpoge_source.
- AM-K018 and ALP-LIFT-07/08: the actual principal line, finite normalization and full-CM reduced-gauge uniqueness for ordinary J powers. AM-R-006: fixed scalar c. Carried DP59, AM-K022 and AM-DO-030/034: actual allowed half-orbit, finite jets and new-block selected construction.

The exact certificate degree_four_principal_host_repair_certificate.py and its JSON output check both weighted trace matrices, integral symmetric actions and tensor commutation, new degree/discriminant arithmetic, the actual new rank/gap/partition lists, direct primality and full prime congruences, primitive-root witnesses and the29 splitting/index identities. They are finite arithmetic checks. The polarized variety, character and canonical-gauge proofs are the mathematical arguments above and their explicitly stated carried inputs; no Lean build or analytic window check is claimed.

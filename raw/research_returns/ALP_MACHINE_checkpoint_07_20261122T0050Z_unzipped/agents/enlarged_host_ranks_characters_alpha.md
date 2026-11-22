# AM-K031 — exact enlarged-host ranks, uniform stage characters, and the unchanged half-orbit isogeny

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC; inherited reasoning effort not separately exposed.

This finding supplies concrete numerical rank/gap data, compatible split primes and actual Hecke characters on the CM host of AM-K029/030. It also proves that the permitted DP59 half-orbit survives the real-field enlargement. It is deliberately not a `Dat.Ok` or D7 instance: the unmodified source still requires \(8\mid f\) and a common quadratic CM subfield for the selected type. The latter is the already audited primitive-type obstruction of AM-R-003, not a new general impossibility theorem.

Throughout the first three sections,
\[
 E_0=\mathbb Q(\zeta_{28}),\quad F_0=E_0^+,\quad
 K=E_0B,\quad F=F_0B,\quad [B:\mathbb Q]=7,
\]
where \(B\subset\mathbb Q(\zeta_{29})\), and the actual type contains every lift of \(\Phi_0=\{1,3,9,15,17,23\}\). Thus \([F:\mathbb Q]=f=42\), and the actual principal abelian variety is \(J^{14}\). Let \(\eta\) be the literal `IsEtaT` character constructed in AM-K029.

## 1. The source rank constraints and an explicit gap locus

The exact record `Formalism/LocalRingCardinality/Params.lean:6–22` imposes
\[
 \begin{gathered}
 k,m\text{ even},\qquad t\text{ odd},\qquad 2\le m,
 \qquad m+3\le k,\\
 k+m+4\le t,\qquad 3m<t,\qquad
 m\le f=2\operatorname{ord}\le k,\qquad
 m^2\le k+m(t+1).
 \end{gathered}
\tag{HC1}
\]
The real-place type count is tied to this f by
`AbelianHostFieldConditions.lean:567`. In particular the old \(k=6\) cannot remain the starting rank on the degree-84 host:
\[
                         \operatorname{ord}=21,\qquad k\ge42.
\tag{HC2}
\]
The inherited `Frame` record itself causes no numerical obstruction to order21. Take its additive group to be \(\mathbb Z/21\mathbb Z\), its cyclotomic parameter to be zero, its projection to the trivial group \(HGrp(0)=(\mathbb Z/4\mathbb Z)^\times/\langle-1\rangle\), and its distinguished element to be zero. The projection and cyclic-kernel clauses in `ZsmulGeneratorEqZeroOfProjection.lean:16–24` then hold. This is a mathematical record construction, not a claim of Lean compilation or of its compatibility with every later host record.

For the shortest allowed length \(m=2\) and smallest starting rank \(k=42\), the rank clauses alone give the least odd t as49. The numerical Hyp3 condition \(1801\le r+t\), where \(r=k+m-1\), is stronger. A convenient simultaneous choice is
\[
 \boxed{f=k=42,\quad m=2,\quad r=43,\quad t=1759,
         \quad d=t+1=1760.}
\tag{HC3}
\]
It gives
\[
       n_V=r+t=1802,
       \qquad (N_0,N_1,N_2)=(42,1802,3562).
\tag{HC4}
\]
The actual G-size clause is
`AbelianHostFieldConditions.lean:488`, namely
\[
                 2fk<g_i-1.
\tag{HC5}
\]
Here its right lower threshold is3528, not the value obtained by retaining \(k=6\).

The following uniform parameters verify all numerical parity, interlacing, centred-distance and opposite-sign gap inequalities occurring in Hyp3. Put
\[
 \begin{split}
 S&=r+mt=3561,\qquad S^3=45\,156\,047\,481,\\
 C&=S^3+k+t+11=45\,156\,049\,293.
 \end{split}
\tag{HC6}
\]
At every one of the 42 embeddings use zero-based indices and set
\[
 \begin{split}
 u_i&=(2(k-i)+1)C+\tfrac12 &&(0\le i<k),\\
 v_i&=2(k-i)C &&(0\le i<k-1),\\
 b_j&=(4j-2)C,\qquad e_j=4jC &&(j=0,1),\\
 \eta_{\mathrm{num}}&=-\tfrac12.
 \end{split}
\tag{HC7}
\]
In particular
\[
 (e_0,e_1)=(0,180\,624\,197\,172),\qquad
 (b_0,b_1)=(-90\,312\,098\,586,90\,312\,098\,586).
\tag{HC8}
\]

**Verification.** The u's are half-integral, the other displayed weights are integral, and
\(u_i>v_i>u_{i+1}\), while \(u_{k-1}=3C+1/2>-b_0=2C\). Both consecutive b/e gaps are \(2C\), exceeding \((t+3)/2=881\).

For the exact `Centred` predicate, \(u_i+e_j\ge3C+1/2\), \(v_i+e_j\ge4C\), and \(|e_j-b_i|\ge2C\). The only cross-block term has centre difference \(4C\) and a block half-width \((t-1)/2=879\), so its absolute value is at least \(4C-879>881\). These are all four kinds of quantifiers in `DataTheta.lean:550–555`.

For `NCGaps`, the literal boolean in `Dpar` is
\(i\le j\) or \(i-j\) even. At stage0 the only false-sign entry is \(-b_1=-2C\); the other b-entry is \(2C\), and all v-entries are at least \(4C\). Thus every opposite-sign distance is at least \(4C>S^3\). At stages1 and2 every entry has true sign, so no opposite-sign comparison remains. The common odd-stage shift by \(\eta_{\mathrm{num}}\) changes no distance. This is the full finite sign analysis for \(m=2\), not a gap check only for adjacent entries.

The source's extra `e_even` condition at line578 also holds: \(\sum_\tau e_j=42e_j\) is even. In the half-angular convention of `HasInfQ`, the constructed odd character has infinity type \(+1/2\), so the required numerical sign is precisely \(\eta_{\mathrm{num}}=-1/2\). This checks the numerical equality; an actual `ThetaX.infTy` realization remains part of the analytic adapter.

For comparison with AM-DO-025, the first selected partition at each place is
\[
           \nu_{0,i}=(85-2i)C+i-921\quad(0\le i<42),
\tag{HC9}
\]
whose smallest entry is \(3C-880>0\). The next partition is
\[
         \nu_1=(\nu_0+\Delta,\Delta^{1760}),
         \qquad \Delta=4C-1760>0.
\tag{HC10}
\]
These follow by substitution into the already checked selected-weight recurrence, not by asserting that an old six-place polynomial remains a single 42-place weight. A new selected polynomial is constructed in the new CM blocks separately.

## 2. Exact conductor and split G primes, including PiGCong

The abelian field K has rational conductor
\[
                              N=28\cdot29=812.
\tag{HC11}
\]
It lies in \(\mathbb Q(\zeta_{812})\). Conversely, a cyclotomic field containing K contains i and \(\zeta_7\), forcing respectively \(4\mid N'\) and \(7\mid N'\); ramification at29 forces \(29\mid N'\). Hence \(812\mid N'\). This verifies the minimum-divisibility formulation of `IsCond` in `RealCyclotomicTwoPower.lean:54`, including every conjugate embedding since K is normal over \(\mathbb Q\).

Write \(\delta=\sqrt{-7}\in E_0\), and use the following **explicit** primes and generators in the external quadratic subfield \(K_q=\mathbb Q(\delta)\):
\[
 \begin{array}{c|c|c}
 i&g_i&\pi_i\\\hline
 0&4\,615\,409&1+812\delta\\
 1&5\,276\,377&813+812\delta.
 \end{array}
\tag{HC12}
\]
Both rational integers are prime. The accompanying certificate checks primality by trial division through the integer square root, as well as
\[
 \pi_i\bar\pi_i=g_i,\qquad
 \pi_i\equiv1\pmod{812\mathcal O_{K_q}},\qquad
                   g_i\equiv1\pmod{812}.
\tag{HC13}
\]
Their conjugate ideals are coprime: a common prime would divide both the norm \(g_i\) and the sum \(2\operatorname{Re}\pi_i\), whereas the corresponding rational gcd is one. Coprimality persists after extension to K.

Thus both primes split completely in K. The support of \(\bar\pi_i\) consists of42 distinct primes, each with residue field canonically \(\mathbb F_{g_i}\) through its prime field. Equations (HC12)–(HC13) supply the norms, coprimality, cardinalities, residue norms, distinctness, full `PiGCong`, and strict G-size inequalities. The value \(812\) in `PiGCong` is not replaced by28. The explicitly retained exception is `piG_Kq`: the source's **defined** common field `Fields.Kq` is \(\mathbb Q\) for this type, rather than the external \(K_q=\mathbb Q(\sqrt{-7})\) used here. Section6 explains that literal failure.

At each i choose a faithful character
\(\omega_i:\mathbb F_{g_i}^{\times}\to\mu_{g_i-1}\).
For example 3 and5 are primitive roots for \(g_0\) and \(g_1\), respectively; the certificate checks their orders using the complete factorization of \(g_i-1\). Use the literal residue characters
\[
             \chi_{j,P}=\omega_i^{2(j+1)}
                       \qquad(P\mid\bar\pi_i).
\tag{HC14}
\]
They satisfy the equality-on-prime-field and `chi_om` clauses. For \(j=0,1\) they are nontrivial and distinct. Their values lie in
\[
        \mathbb Q(\zeta_L),\qquad
        L=\operatorname{lcm}(28,g_0-1,g_1-1)=14\,995\,460\,592.
\tag{HC15}
\]
This is a fixed coefficient extension; its large degree is not discarded in any later height budget.

## 3. Actual global stage characters for every uniform integral weight

### Theorem HC16

For any integers \(e_j\), there are continuous unitary Hecke characters \(\mu_j\) of K which are trivial on \(\mathbb A_F^\times\), tame at every finite place, unramified away from \(g_0g_1\), have infinity component
\[
       (\mu_j)_\infty(z)
             =\prod_{\tau\in\Psi}
                    \left(\frac{z_\tau}{|z_\tau|}\right)^{-2e_j},
\tag{HC16}
\]
and satisfy
\[
       \mu_{j,P}|_{\mathcal O_{K,P}^\times}=\chi_{j,P}^{-1}
                  \qquad(P\mid\bar\pi_i).
\tag{HC17}
\]
These are the exact `IsMu0` character conditions for a uniform splitting weight. The values required as `muVal` lie in a single finite coefficient field, after adjoining the host embeddings and normal closure if required. There is no new class-number-one assumption on K or F.

**Construction and proof.** Apply the checked ALP-LIFT-18 construction on E₀ to these new split primes, with **zero** infinity weight at every embedding. Its root compatibility is then automatic. Concretely, on the compact norm-one torus its character is the product of \(\omega_i^{-2(j+1)}\) at the six selected E₀-primes. The product on global roots is one because
\(N_{E_0/K_q}(\mu_{28})=1\), as proved in LIFT18(G2)–(G3). The checked class-one torus decomposition of AM-R-009 makes this an actual automorphic torus character. Composing with \(x\mapsto x/\bar x\) gives a finite-order Hecke character \(\nu_j\) of E₀, trivial on \(\mathbb A_{F_0}^\times\), with zero infinity type and the required inverse residue characters. Its values lie in the roots of unity in (HC15). This is an application of the existing character theorem; its class-number proof is not rederived here.

Pull this actual character back to K by the idele norm:
\[
              \widetilde\nu_j=\nu_j\circ N_{K/E_0}.
\tag{HC18}
\]
At every chosen G prime the extension is completely split, so the completion map is \(K_P=(E_0)_{P_0}=\mathbb Q_{g_i}\). On an idele supported in one such component, the local norm is the identity. Thus (HC18) has the required residue character at **each** of the seven lifts of every old selected prime; it does not raise a single local residue character to the seventh power. Norms take local units to units at every other place, so the pullback is unramified there, including the new ramification place29. The norm of an F-idele lies in \(\mathbb A_{F_0}^\times\), hence the pullback is trivial on \(\mathbb A_F^\times\).

Now use the actual odd character of AM-K029:
\[
                   \boxed{\mu_j=\widetilde\nu_j\,\eta^{-2e_j}.}
\tag{HC19}
\]
The restriction of η to \(\mathbb A_F^\times\) is the quadratic character \(\eta_{K/F}\). Its even power in (HC19) is therefore trivial on that group. Since η is everywhere finite-unramified, it changes no compact residue restriction or tame conductor. Its angular exponent is one, so its \(-2e_j\) power supplies exactly (HC16), which is the literal `HasInfQ(-e_j)` convention. All the claimed properties follow.

For the two stages in (HC3), the finite conductor is exactly
\[
          \mathfrak f(\mu_j)=g_0g_1\mathcal O_K,
          \qquad N_{K/\mathbb Q}\mathfrak f(\mu_j)=(g_0g_1)^{84}.
\tag{HC20}
\]
Both halves have conductor exponent one because the selected residue characters are nontrivial and base-field triviality forces the inverse character at the conjugate place. Unramified η cannot cancel a nontrivial residue character.

To check the common algebraic field, let
\(a_P=\eta(\varpi_P)(NP)^{-1/2}\), the `etaVal` supplied in AM-K029. At a finite uniformizer,
\[
        \mu_j(\varpi_P)
          =\widetilde\nu_j(\varpi_P)\,a_P^{-2e_j}(NP)^{-e_j}.
\tag{HC21}
\]
The first factor is in the fixed finite group of roots from (HC15), the second lies in the fixed `etaVal` field, and the last is rational. Thus one coefficient field works for every integer choice of the uniform weights. Taking its normal closure and adjoining K preserves finiteness. No effective small degree, discriminant or uniformizer-height bound is inferred. ∎

This is stronger than merely pulling back LIFT18's nonzero infinity weights, which would retain its sufficient \(7\mid e_j\) restriction. Here all integer uniform weights work. For example the explicit \(C\) in (HC6) is \(5\bmod7\), so \(e_1=4C\equiv6\bmod7\); it is covered by (HC19) and not by the old uniform congruence.

The construction is stable under further totally real extension: pull η back by norm, and pull \(\nu_j\) directly from E₀. At G-primes chosen completely split in the enlarged CM field, each local norm remains the identity. Every integer uniform infinity weight again works. This gives a parameterized character construction for later real-field repairs without reusing an unjustified large-field torus class-number-one assertion.

## 4. The fixed alpha and the actual permitted DP59 half-orbit

The alpha used in AM-K022/DO030 is in \(\mathbb Q(\sqrt{-7})\), not in \(\mathbb Q(i)\):
\[
       \alpha=(1+2\delta)^e,\quad M=29^e,\quad e\ge1,
                   \qquad \alpha\bar\alpha=M.
\tag{HC22}
\]
The alternative \((5+2i)^e\) has the same norm identity, but changing to it is unnecessary. We retain (HC22), which acts diagonally on every ordinary J factor.

The ideals of \(1+2\delta\) and its conjugate are coprime in every extension of E₀. A common prime would divide their sum2 and their product29, which is impossible. Thus the ideals of α and \(\bar\alpha\) remain coprime in K and in every further real extension. At rational29, their valuations in K are \(7e\) on the two disjoint six-prime halves, rather than e. This ramification does not change the element identity or the coprimality statement.

The element \(1+2\delta\) is congruent to one modulo2. It therefore acts trivially on the relevant two-torsion characteristic, and the exact odd symmetric pullback normalization carried in DP59 applies to the same invariant theta line. Under the K030 polarized product isomorphism, α is still the same diagonal endomorphism on all14 J factors: it lies in the central old E₀-action and commutes with the real trace-lattice transport.

More generally suppose a further real-field construction realizes the induced host as \(J^{14h}\) with its product line, h a positive integer. On an edge of ranks a,b put
\[
       X=J^{14hab},\quad g_X=42hab,\quad
       \mathcal L=L_{2\infty}^{\boxtimes14hab}.
\tag{HC23}
\]
Tensor the **carried** single-J DP59 basis, using precisely (HC22). It gives an integral basis of
\[
       \mathcal W_M=[\alpha]^*H^0(X,\mathcal L^M)
                         \subset H^0(X,\mathcal L^{M^2}),
       \qquad \operatorname{rank}\mathcal W_M=M^{42hab}.
\tag{HC24}
\]
Its parameters are the prescribed representatives of
\(X[\alpha^2]/X[\alpha]\), with actual rescaled translation
\[
                         x=Mt'\in X[\alpha].
\tag{HC25}
\]
Indeed \(\alpha Mt'=\alpha^2\bar\alpha t'=0\), and coprimality makes \(\bar\alpha\) invertible on α-primary torsion. This remains the permitted half-orbit, not the full level-\(M^2\) theta group.

At11, α is étale and all new CM-coordinate changes under consideration are integral invertible by K030 or by the corresponding later host proof. Consequently the K022 ordinary-jet surjectivity, equality of all determinantal image ideals, and one-translate norm-one conclusion apply with
\[
               M\ge3D+2,
       \qquad e(D)=\max\{1,\lceil\log_{29}(3D+2)\rceil\}.
\tag{HC26}
\]
The threshold is independent of h,a,b. Each individually selected finite Heisenberg translate has finite Schwartz norm one; its coefficient vector is one standard basis vector. No new coefficient-combination height or norm is introduced by the real extension. The Fock norm, source representation dimension, class mass, actual period and finite29 coordinate changes are separate and remain in the cost.

The auxiliary multijet statement of DO030 also persists with its same threshold \(3s(D+1)-1\), provided its auxiliary torsion/order and Schwartz support remain prime to29 and11. Its proof uses the same half-orbit, integral selfdual trace lattice, and the isogeny's invertibility on that auxiliary torsion. Rational29 now has the new local ramification depth, so its explicit class-index factor is PH26 of K030, not the old degree-six formula. None of this identifies the DP59 translate with the separate literal source raw-Xi input.

## 5. Auxiliary T-prime existence and size scope

For any finite collection of words and any specified finite lower size threshold, the norm/congruence part of the T-prime interface can be supplied in the same external quadratic subfield. Let
\[
                      L_T=812(g_0g_1)^2.
\tag{HC27}
\]
Take the ray class field of \(\mathbb Q(\sqrt{-7})\) for the ideal modulus \(L_T\mathcal O_{K_q}\), and its normal closure over \(\mathbb Q\). There are infinitely many rational primes splitting completely in this finite normal extension, by the unconditional Chebotarev theorem. At such a prime q, a chosen prime ideal of \(K_q\) lies in the trivial ray class, hence has a generator \(\pi_T\equiv1\pmod{L_T}\). Since the prime has degree one and \(K_q\) is imaginary quadratic,
\(\pi_T\bar\pi_T=q\). Its conjugate ideals are distinct and coprime. Moreover \(q\equiv1\pmod{812}\), so it splits completely in K and supplies the required42-element half with residue norm q. Choosing distinct such q outside a finite set gives the requested finite family.

For any fixed finite weight data one can choose a real size parameter a with
\(2fN_m+1<4a\) and every source spread at most \(2a\), then choose these T-primes larger than \(4a\). This proves qualitative nonemptiness of the corresponding norm, congruence and lower-size clauses. It supplies no effective upper bound for T and no assertion that this choice meets the quantitative MainX window. The same literal `piT_Kq` obstruction remains as for G, since the source's common field is not this external quadratic subfield.

## 6. Literal source failures and exact scope

The following distinctions are necessary.

| Interface | Result on this host |
|---|---|
| Actual principal CM variety and full integral action | K030 gives \(J^{14}\), degree84, induced type, exact coefficient and lattice |
| Literal `IsEtaT` and normalized `etaVal` | K029 proves all character clauses and a finite common coefficient field |
| Numerical `Ranks`, with f tied to degree | (HC1)–(HC4) supply \(f=k=42,m=2,t=1759\) |
| Numerical parity, interlace, centred and NCGaps inequalities | (HC6)–(HC10) verify them; this alone is not a `ThetaX` instance |
| Exact uniform even stage-character conditions | (HC16)–(HC21) prove them for every integer uniform weight |
| G norms, coprimality, residue cardinalities, full PiGCong and lower bound | (HC12)–(HC14) give explicit values in an external quadratic subfield |
| DP59 half-orbit and integral 11-jets | (HC22)–(HC26) retain the actual allowed family with parameterized dimensions |
| `eight_dvd : 8 ∣ f` | Fails for \(f=42\); a further real extension of degree divisible by4 is necessary numerically |
| `Fields.Ok.quad`, `Primes.Ok.piG_Kq`, `piT_Kq` | Fail for the unchanged primitive type: its defined common field is \(\mathbb Q\) |
| Full D7, prescribed raw Xi, later selected image and quantitative cost window | Not supplied by these constructions |

For the common-field assertion, the induced type contains all B-lifts of each E₀ embedding, so an element on which every selected embedding agrees must first lie in E₀. The selected E₀ embeddings contain the identity, 3 and17. The subgroup generated by3 is
\(\{1,3,9,27,25,19\}\), and17 is outside it; together they generate all12 automorphisms of E₀. The common element is consequently rational. Thus
\[
                  \mathrm{Fields.Kq}=\mathbb Q.
\tag{HC28}
\]
The source defines this field in `AbelianHostFieldConditions.lean:60–76`, requires degree2 at lines108 and157, and requires the prime generators to belong to it at lines210 and226. This is a precise restatement of the prior primitive-type obstruction. It cannot be repaired by relabeling the external \(\mathbb Q(\sqrt{-7})\) as `Fields.Kq`.

For an induced type under any further totally real extension, the same common-field obstruction persists. Agreement across all lifts first forces descent to E₀, and the preceding group argument still gives \(\mathbb Q\). In contrast, the numerical condition \(8\mid42h\) is equivalent to \(4\mid h\). At its first possible real extension degree4, f becomes168 and the rank constraint becomes \(k\ge168\), with G-size threshold at least \(2\cdot168^2=56\,448\). A construction of that larger polarized host must be supplied separately; the formal divisibility check alone would not construct it.

## 7. Sources and verification scope

- Exact source: `Formalism/LocalRingCardinality/Params.lean:6–22,28–40`; `Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean:60–76,108–125,206–238,293–331,486–494,560–579`; `Formalism/LocalToGlobal/UnitaryNorms/RealCyclotomicTwoPower.lean:54`; `Formalism/LocalRingCardinality/DataTheta.lean:501–555`; `Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean:106–125`.
- Inherited Frame: `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ZsmulGeneratorEqZeroOfProjection.lean:16–24` and `Formalism/FrobeniusOrbits/Statement.lean:27–29`. Additional recovered members are pinned to commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`; their retrieval manifests explicitly record when no intake-author hash exists. No original-byte match is inferred from that absence.
- AM-R-009 and ALP-LIFT-18(G2)–(G14): the checked E₀ norm-one torus and its actual character construction, used with zero infinity weight. AM-K029/030: the repaired odd character, full product host and exact finite comparisons. AM-DO-025: selected partition recurrence. Carried DP59 and AM-K022/DO030: the permitted basis and ordinary/multijet interfaces.
- Milne, J. S. (2020). *Class field theory* (Version4.03). Chapter V, Theorem3.6, printed p.158, and Theorem3.23, printed p.164, for ray class fields and unconditional Chebotarev. Primary author PDF: https://www.jmilne.org/math/CourseNotes/CFT.pdf. These are used only for the qualitative T-prime choice, not an effective size estimate.

The finite certificate checks every numerical rank clause, all displayed gap comparisons including every actual opposite-sign pair, the prime norms/congruences/primality and primitive-root orders, the common-field finite group computation, and the alpha norm/coprimality arithmetic. It does not infer analytic nonvanishing, a selected-image bound, a large-field class number, a character theorem, or a Lean instance from those finite checks.

The independently replayable files are `enlarged_host_ranks_characters_alpha_certificate.py` and its JSON output. The certificate uses integer/Fraction arithmetic and direct trial division, with no probable-prime substitution. In particular it checks the literal natural subtraction in the Dpar sign rule and reconstructs the selected partition from the source weight recurrence before comparing it with (HC9)–(HC10).

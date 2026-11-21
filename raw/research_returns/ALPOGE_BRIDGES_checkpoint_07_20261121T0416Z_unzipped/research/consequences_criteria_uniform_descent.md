# A uniform finite computation of each geometric descent monoid

## CC-AG16 — A conductor bound independent of the target multiplicity

Work in the established rational numerical abelian--Artin--Tate categories, with the exact simple-object and local-index formulas of CC-AG08--09. The theorem below computes the entire geometric multiplicity monoid over a specified finite source field. It retains the full positive multiplicity data; the noncyclic monoid of CC-AG14 and the stronger local obstruction of CC-AG15 are included.

Choose a stabilized representative at the least positive exponent:

\[
 \xi=[\gamma,h],\qquad
 K=\mathbf Q(\gamma^n)\quad(n\ge1),\qquad h=h_\xi.
 \tag{CC-AG.148}
\]

Let \(d_\xi\) be the geometric Schur index, and fix the source field \(\mathbf F_{p^a}\), with \(a\ge1\). Write \(H_a(\xi)\) for the additive monoid of multiplicities of the geometric simple \(S_\xi\) obtained by base extension from that source.

If \(K\) has a real embedding, then \(K=\mathbf Q\) and \(H_a(\xi)=\mathbf N\), as follows from the real-centre cases of CC-AG13 and subsequent base extension. Suppose henceforth that \(K\) has no real embeddings.

Let \(E/\mathbf Q\) be the splitting field of

\[
 \operatorname{Norm}_{K/\mathbf Q}(X^h-\gamma^a),
 \qquad M=[E:\mathbf Q],\qquad S=\{\ell:\ell\text{ prime},\ \ell\mid h\}.
 \tag{CC-AG.149}
\]

For \(\ell\in S\), put

\[
 \varepsilon_\ell=
 \begin{cases}1&\ell\ne2,\\2&\ell=2,\end{cases}
 \qquad
 b_\ell=\max\bigl(\{v_\ell(r-1):r\in S\setminus\{p,\ell\}\}\cup\{0\}\bigr),
 \tag{CC-AG.150}
\]

\[
 c_\ell=
 \begin{cases}
 \varepsilon_\ell,&\ell=p,\\
 v_\ell(p^{\ell-1}-1)+b_\ell,&\ell\ne p,\ \ell\ne2,\\
 v_2(p^2-1)+b_2,&\ell=2\ne p,
 \end{cases}
 \qquad
 B_\ell=c_\ell+v_\ell(M!)+v_\ell(h).
 \tag{CC-AG.151}
\]

Define

\[
 N=\prod_{\ell\in S}\ell^{B_\ell}.
 \tag{CC-AG.152}
\]

Empty products mean \(N=1\). Since \(B_\ell\ge v_\ell(h)\), we have \(h\mid N\). Form the finite rational polynomial

\[
 P_{\xi,a}(X)=
 \operatorname{Norm}_{K/\mathbf Q}
       \left(X^N-\gamma^{aN/h}\right).
 \tag{CC-AG.153}
\]

Factor it over \(\mathbf Q\), and let \(\alpha_1,\ldots,\alpha_t\) represent its distinct irreducible root orbits. Compute each source Schur index \(d_j\) from the specified local-invariant formula, and put

\[
 m_j=\frac{[\mathbf Q(\alpha_j):K]d_j}{d_\xi}
     =\frac{[\mathbf Q(\alpha_j):\mathbf Q]d_j}
            {[K:\mathbf Q]d_\xi}.
 \tag{CC-AG.154}
\]

Here an embedding of \(K\) into each source centre is chosen through its corresponding factor of the norm; the second formula is independent of that choice. All \(m_j\) are positive integers, and

\[
                         H_a(\xi)=
                  \langle m_1,\ldots,m_t\rangle_{\mathbf N}.
 \tag{CC-AG.155}
\]

Thus the finite polynomial cutoff depends on the germ and the source field, and **does not depend on a target multiplicity**. It computes the exact monoid, its minimal generators, its gcd, its gaps among multiples of that gcd, and a conductor relative to those multiples. The displayed bounds are deliberately coarse. No practical complexity estimate is asserted.

### 1. Elementary principal-unit facts

For a prime \(\ell\), write
\[
 U_\ell(s)=1+\ell^s\mathbf Z_\ell\qquad(s\ge\varepsilon_\ell).
\]
We shall use two explicit elementary facts:

\[
 \overline{\langle u\rangle}=U_\ell(s)
 \quad\text{if }v_\ell(u-1)=s\ge\varepsilon_\ell,
 \qquad
 U_\ell(s)^m=U_\ell(s+v_\ell(m)).
 \tag{CC-AG.156}
\]

Here the first closure is in the \(\ell\)-adic topology, and the second expression is the image of the \(m\)-th power map, for any positive integer \(m\).

For a proof, binomial expansion gives
\[
 v_\ell(u^n-1)=s+v_\ell(n)\qquad(n\ge1).
 \tag{CC-AG.157}
\]
When \(\ell\nmid n\), the linear term has valuation \(s\) and every higher term has larger valuation. For \(n=\ell\), the linear term has valuation \(s+1\), the intermediate terms have larger valuation, and the final term has larger valuation for \(s\ge1\) if \(\ell\) is odd and for \(s\ge2\) if \(\ell=2\). Iterating proves the general formula. Consequently the order of \(u\) modulo \(U_\ell(s+j)\) is exactly \(\ell^j\), which is the order of that whole quotient. The generated cyclic subgroup is therefore dense. The same argument applied to \(u^m\), together with compactness of \(U_\ell(s)\), proves the power-map formula in (CC-AG.156).

### 2. A computable cyclotomic subgroup that fixes the auxiliary field

Let \(\mu_{S^\infty}\) denote the roots of unity whose orders have all prime divisors in \(S\). The cyclotomic character identifies

\[
 \operatorname{Gal}\bigl(\mathbf Q(\mu_{S^\infty})/\mathbf Q\bigr)
       =\prod_{\ell\in S}\mathbf Z_\ell^\times.
 \tag{CC-AG.158}
\]

This is the inverse limit of the usual finite cyclotomic Galois groups: their orders and their faithful action on a primitive root give the full groups \((\mathbf Z/n\mathbf Z)^\times\), and the Chinese remainder theorem separates the prime factors. The finite degree input is Milne (2020), Theorem 6.4(a), p. 99.

Put
\[
                    C_\ell=c_\ell+v_\ell(M!).
 \tag{CC-AG.159}
\]

The following two assertions use the same constants:

* In \(E(\mu_{S^\infty})/E\), every cyclotomic action which is the identity at the primes other than \(\ell\), and is any specified element of \(U_\ell(C_\ell)\) at \(\ell\), is realized by an automorphism fixing \(E\).
* For every \(p\)-adic completion \(E_w\), the identical assertion holds in \(E_w(\mu_{S^\infty})/E_w\).

We prove both assertions, including the independence from the exponents in every other cyclotomic tower.

For the global assertion, the cyclotomic actions which fix \(E\) form a subgroup of (CC-AG.158) of index
\[
 [E\cap\mathbf Q(\mu_{S^\infty}):\mathbf Q]\le M.
\]
Its quotient is finite abelian of order at most \(M\), so it is killed by \(M!\). Thus the \(M!\)-th powers of all independently supported principal units occur. By (CC-AG.156), the subgroup contains the independently supported
\(U_\ell(\varepsilon_\ell+v_\ell(M!))\). Since \(c_\ell\ge\varepsilon_\ell\), this proves the stated global assertion.

For the local assertion, first work over \(\mathbf Q_p\). Roots of unity of order prime to \(p\) lie in the maximal unramified extension; Frobenius acts on them by \(\zeta\mapsto\zeta^p\). Hence the image of the local cyclotomic character on the factors indexed by \(S\setminus\{p\}\) is the closure of the cyclic subgroup generated by \(p\) in
\(\prod_{r\in S\setminus\{p\}}\mathbf Z_r^\times\). The \(p\)-power roots, when \(p\in S\), give the full independent factor \(\mathbf Z_p^\times\): their cyclotomic extensions are totally ramified, whereas the preceding extensions are unramified. The exact primary inputs are Milne (2020), Proposition 6.2(a),(c), pp. 96--97, Proposition 7.50 and Corollary 7.51, pp. 127--128, and Example 7.54, p. 129. Equivalently, the prime-to-\(p\) assertion follows by simple-root lifting from finite residue fields, and total ramification follows from the Eisenstein polynomial for \(\zeta_{p^k}-1\).

We now isolate one prime \(\ell\ne p\) in that procyclic Frobenius image. The continuous power map from the profinite integers sends
\[
 t\in\widehat{\mathbf Z}=\prod_q\mathbf Z_q
          \quad\text{to}\quad p^t.
\]
Take all coordinates \(t_q=0\) for \(q\ne\ell\). In a factor \(\mathbf Z_r^\times\) with \(r\ne\ell\), the pro-\(r\) part is thereby killed. Its remaining \(\ell\)-primary finite part has order dividing \(\ell^{v_\ell(r-1)}\). This statement also covers \(r=2\ne\ell\), when that \(\ell\)-primary part is trivial.

If \(\ell\) is odd, further take \(t_\ell\in\ell^{b_\ell}\mathbf Z_\ell\). This kills all the other factors. In its own \(\ell\)-factor, the pro-\(\ell\) component of \(p\) generates the same closed subgroup as \(p^{\ell-1}\), since \(\ell-1\) is an \(\ell\)-adic unit. By (CC-AG.156), its image after the additional power is exactly
\[
 U_\ell\bigl(v_\ell(p^{\ell-1}-1)+b_\ell\bigr)=U_\ell(c_\ell).
\]
If \(\ell=2\ne p\), use \(t_2\in2^{b_2+1}\mathbf Z_2\). The additional factor \(2\) kills the sign in \(\mathbf Z_2^\times\); the powers of \(p^2\) generate \(U_2(v_2(p^2-1))\). The resulting independently supported image is therefore \(U_2(c_2)\). Finally, for \(\ell=p\), the independent totally ramified factor already contains \(U_p(\varepsilon_p)=U_p(c_p)\).

Thus the local cyclotomic image over \(\mathbf Q_p\) contains each independently supported \(U_\ell(c_\ell)\). Passing to \(E_w\) imposes a subgroup of index
\[
 [E_w\cap\mathbf Q_p(\mu_{S^\infty}):\mathbf Q_p]
       \le [E_w:\mathbf Q_p]\le M.
\]
Again the quotient is finite abelian and is killed by \(M!\). Applying (CC-AG.156) gives every independently supported \(U_\ell(C_\ell)\), as claimed. This proof works at once for every \(w\) and for all heights in the other prime towers.

### 3. An orbit-degree lemma with a specified lower-conductor label

We isolate the exact group argument needed below. Let \(F\) be a characteristic-zero field, let \(E_0/F\) be finite Galois, and let \(x\in E_0^\times\) satisfy \(x^h\in F\). Suppose that in
\[
                         E_0(\mu_{S^\infty})/E_0
\]
every independently supported \(U_\ell(C)\) action occurs, for a fixed \(\ell\in S\). Put \(H=v_\ell(h)\). Fix roots of unity at the other primes in \(S\), with product \(\eta\) of order prime to \(\ell\). Choose compatible primitive roots
\(\zeta_{\ell^{k+1}}^\ell=\zeta_{\ell^k}\), and define

\[
 x_k=x\zeta_{\ell^k}\eta,\qquad
 F_k=E_0(\zeta_{\ell^k},\eta).
 \tag{CC-AG.160}
\]

Then for every \(k\ge C+H\),

\[
 [F(x_{k+1}):F]=\ell[F(x_k):F].
 \tag{CC-AG.161}
\]

To prove it, write \(\Gamma_k=\operatorname{Gal}(F_k/F)\). Projection to \(\operatorname{Gal}(E_0/F)\) is injective on the stabilizer of \(x_k\). Indeed an automorphism which fixes \(E_0\) and \(x_k\) fixes the product \(\zeta_{\ell^k}\eta\); its coprime primary components generate the cyclotomic part of \(F_k\), so it fixes \(F_k\).

For \(\sigma\in\operatorname{Gal}(E_0/F)\), set
\(\lambda_\sigma=\sigma(x)/x\in\mu_h\). Decompose it into its primary parts. A lift fixes \(x_k\) precisely when its action on each cyclotomic component compensates the corresponding component of \(\lambda_\sigma\). All conditions at primes other than \(\ell\) are independent of \(k\). At \(\ell\), write
\[
 (\lambda_\sigma)_\ell
        =\zeta_{\ell^k}^{\,j\ell^{k-H}}.
\]
The required exponent of the cyclotomic action is
\[
                       u_k=1-j\ell^{k-H}.
 \tag{CC-AG.162}
\]
For \(k\ge C+H\) this is an element of \(U_\ell(C)\).

More explicitly, a lift at level \(k\) extends to the infinite Galois extension. Its full \(\ell\)-adic cyclotomic action is congruent to \(u_k\) modulo \(\ell^k\), hence lies in \(U_\ell(C)\). Multiply that lift by the independently supported inverse action which fixes \(E_0\) and all the other cyclotomic towers. This produces a lift of the same \(\sigma\) whose action on the entire \(\ell\)-tower is the identity and whose other required actions are unchanged. Conversely, from any such lift with trivial \(\ell\)-action, multiplication by the independently supported action (CC-AG.162) produces a lift fixing \(x_k\). Thus the image of the stabilizer in \(\operatorname{Gal}(E_0/F)\), and consequently its cardinality, is independent of \(k\) throughout this range. This argument is uniform in \(\eta\) and works for every choice of the primitive root.

For \(k\ge C\), the extension \(F_{k+1}/F_k\) has degree exactly \(\ell\). Its degree is at most \(\ell\) by adjoining a root of \(T^\ell-\zeta_{\ell^k}\). The independently supported subgroup \(U_\ell(k)\subset U_\ell(C)\) acts trivially on \(F_k\) and has an image of order \(\ell\) on \(\zeta_{\ell^{k+1}}\), proving the reverse inequality. Therefore \(|\Gamma_{k+1}|=\ell|\Gamma_k|\). The orbit-stabilizer formula, with the constant stabilizer just proved, yields (CC-AG.161).

### 4. Simultaneous global and local recurrences

Fix a root \(x=\alpha_0\) of \(X^h-\gamma^a\) in \(E\). The field \(E\) in (CC-AG.149) contains \(\mu_h\), since quotients of the roots of one binomial factor give these roots of unity. Every positive power of \(\gamma\) generates \(K\), so \(K\subset\mathbf Q(\alpha_0)\).

Consider any label
\[
 \alpha_k=\alpha_0\zeta_{\ell^k}\eta,
\]
where \(\eta\) has order supported on \(S\setminus\{\ell\}\), and let
\[
 \alpha_{k+1}=\alpha_0\zeta_{\ell^{k+1}}\eta,
 \qquad \zeta_{\ell^{k+1}}^\ell=\zeta_{\ell^k}.
 \tag{CC-AG.163}
\]
Both labels are Weil \(p^a\)-numbers with germ \(\xi\), and their centres contain \(K\). In particular the lower label is specified explicitly; it is not an unspecified field of a related degree.

Apply Section 3 first with \(F=K\), \(E_0=E\), and \(C=C_\ell\) of (CC-AG.159). Since \(B_\ell=C_\ell+v_\ell(h)\), for \(k\ge B_\ell\) it gives
\[
 [\mathbf Q(\alpha_{k+1}):K]
            =\ell[\mathbf Q(\alpha_k):K].
 \tag{CC-AG.164}
\]

Now fix any embedding of the common Galois number field
\[
                 E(\zeta_{\ell^{k+1}},\eta)
\]
into \(\overline{\mathbf Q}_p\). Its restriction determines a place \(v\) of \(K\) and a completion \(E_w\). Use Section 3 with \(F=K_v\), \(E_0=E_w\), and the embedded conjugate of \(\alpha_0\). The completion \(E_w/K_v\) is Galois, because \(E/\mathbf Q\) is Galois. Section 2 supplies the same \(U_\ell(C_\ell)\) subgroup. We obtain, for this paired embedding,

\[
 [K_v(\alpha_{k+1}):K_v]
                =\ell[K_v(\alpha_k):K_v].
 \tag{CC-AG.165}
\]

The notation in (CC-AG.165) means the embedded elements. These fields are exactly the corresponding completions of the two source centres. Every embedding of either centre into \(\overline{\mathbf Q}_p\) extends to the displayed common Galois field. Thus every local place at the upper level and every local place at the lower level occurs in such a pair. No local place is discarded by the comparison.

The quotient of the two labels in a pair is a root of unity, so their normalized \(p\)-adic slopes are identical. Formula (CC-AG.165) therefore multiplies the source local invariant by \(\ell\). Since all centres contain the field \(K\) with no real embeddings, there are no real-place invariants. All finite invariants away from \(p\) vanish. Consequently, if \(d_k,d_{k+1}\) are the two source Schur indices, the *whole sets* of local invariants, with repetitions immaterial, give

\[
                  d_{k+1}=\frac{d_k}{\gcd(d_k,\ell)}.
 \tag{CC-AG.166}
\]

Indeed multiplying a finite set of rational classes of least common denominator \(d_k\) by \(\ell\) changes that denominator to \(d_k/\gcd(d_k,\ell)\). Combining (CC-AG.164)--(CC-AG.166) with the exact transition multiplicity formula gives

\[
 \frac{r_{\alpha_{k+1}}}{r_{\alpha_k}}
                =\frac{\ell}{\gcd(d_k,\ell)}
                    \ \in\ \{1,\ell\}.
 \tag{CC-AG.167}
\]

Thus every step above the cutoff replaces a generator by a positive integer multiple of the specified lower-conductor generator. There is no need to assume that the two source centres are nested, or to wait until an \(\ell\)-primary index has vanished.

### 5. Reduction to the finite norm polynomial

The already proved prime-support lemma BR-15-PRIME-SUPPORT says that every source label can be replaced by one whose
\[
                         \alpha^h/\gamma^a
\]
has order supported on \(S\), and whose positive transition multiplicity divides the original multiplicity. This is a reduction for a geometric target; it does not purport to preserve a prescribed finite-field target label.

For such a restricted label, \(\zeta=\alpha/\alpha_0\) is itself a root of unity supported on \(S\). Its \(h\)-th power is the indicated root of unity. A prime outside \(S\) dividing the order of \(\zeta\) would still divide the order of its \(h\)-th power, which is impossible. Thus all the restricted labels have the form used in (CC-AG.163).

If the \(\ell\)-primary component of \(\zeta\) has order \(\ell^k\) with \(k>B_\ell\), keep every other primary component fixed and replace that component by its \(\ell\)-th power. Equation (CC-AG.167), applied with lower level \(k-1\ge B_\ell\), shows that the old multiplicity is either the same as, or \(\ell\) times, the new one. Repeating finitely many times for each prime in \(S\) produces a label \(\alpha_0\zeta'\) with \((\zeta')^N=1\), whose multiplicity divides that of the original source label.

Because \(h\mid N\),
\[
       \alpha_0^N=(\alpha_0^h)^{N/h}=\gamma^{aN/h}.
 \tag{CC-AG.168}
\]
The reduced labels, with their conjugates, are exactly the roots of (CC-AG.153). Conversely every root of that polynomial is a valid source Weil number with the required germ orbit. If
\(\alpha^N=\sigma(\gamma)^{aN/h}\), taking complex absolute values gives weight \(w\) relative to \(p^a\), taking valuations away from \(p\) gives zero, and raising to \(h\) gives germ equality. Also \(\sigma(K)\subset\mathbf Q(\alpha)\), by stabilization.

The polynomial lies in \(\mathbf Q[X]\) by the norm construction. It is separable: each binomial has distinct roots, and the constants belonging to different embeddings of \(K\) are distinct because \(\gamma^{aN/h}\) generates \(K\). Its factors therefore give finitely many distinct source simple classes. Their multiplicities (CC-AG.154) are positive integers by the exact transition theorem.

We have proved that every unrestricted source generator is a positive integer multiple of one of these finitely many generators. Conversely each of the listed generators occurs as a source simple. Positivity and semisimple decomposition prove (CC-AG.155).

If \(h=1\), the same conclusion holds with \(S\) empty and \(N=1\): the prime-support step reduces every label to \(\gamma^a\). No tower argument is then needed. This completes the proof of the uniform finite cutoff for nonreal \(K\).

### 6. Real centres, arithmetic effectivity, and exact monoid output

For completeness, a stabilized centre with a real embedding is \(\mathbf Q\). If the weight \(w\) is even, the germ is the Tate germ represented by \(p^{w/2}\), and a single copy is defined over the prime field. If \(w\) is odd, the representative \(-p^w\) at exponent \(2\), followed by a square root, gives an imaginary quadratic Weil \(p\)-number of index one whose geometric image is one copy of the rank-two geometric simple. These are exactly the fully proved real-centre cases of CC-AG13. Base extension of this prime-field source to \(\mathbf F_{p^a}\) still realizes one copy. Hence \(H_a(\xi)=\mathbf N\) for every \(a\), as claimed.

All constants in the nonreal case are finite and effectively determined. The minimal exponent and a witness \(\gamma\) are obtained by the finite root equations of CC-AG13. A splitting field of the finite polynomial (CC-AG.149), and its degree \(M\), are found by finite number-field calculations. The valuations in (CC-AG.150)--(CC-AG.151) are valuations of explicit nonzero integers; \(v_\ell(M!)\) can be computed as
\(\sum_{j\ge1}\lfloor M/\ell^j\rfloor\). The norm polynomial (CC-AG.153), its rational factorization, and the local-index computations are therefore finite exact operations.

Here is also a direct finite procedure for the additional monoid data asserted after (CC-AG.155). Let \(g=\gcd(m_1,\ldots,m_t)\), put \(a_j=m_j/g\), and let \(m=\min_j a_j\). On the finite set \(\mathbf Z/m\mathbf Z\), give each directed edge
\[
                     x\longrightarrow x+a_j
\]
the positive integer cost \(a_j\). All vertices are reachable from \(0\): the nonnegative sums in a finite group form a subgroup, and the gcd of the \(a_j\) is one. Finite shortest-path calculation therefore gives a least cost \(A_x\) for every residue \(x\). A cost is the corresponding nonnegative integer sum, so \(A_x\) is precisely the least element of the divided monoid in that residue class.

An integer \(n\ge0\) is in the divided monoid if and only if
\[
                          n\ge A_{n\bmod m}.
 \tag{CC-AG.169}
\]
Necessity is minimality. For sufficiency, the difference is a nonnegative multiple of the generator \(m\). Hence the conductor is
\[
                         \max_x A_x-m+1,
 \tag{CC-AG.170}
\]
with value \(0\) when \(m=1\). Multiplication by \(g\) gives the conductor relative to \(g\mathbf N\) and all gaps among those multiples. Every indecomposable positive element of the original monoid belongs to the original finite generator list, because any expression using at least two positive summands decomposes it. First remove repeated integers from the list. Testing each remaining generator against the bounded positive combinations of the others then gives the minimal generator list. Thus the theorem computes all the claimed monoid data. \(\square\)

### Scope

The cutoff lists enough source classes to generate all possible multiplicities. It does **not** say that every source simple belongs to that finite list. The earlier rank-dependent procedure CC-AG12 remains the statement that enumerates every preimage class of a specified target object. For a geometric object with finitely many simple isotypic components, the present theorem gives one finite positive multiplicity system for each orbit, valid for all target multiplicities in that orbit.

The whole construction takes place in the established abelian--Artin--Tate sector and does not construct arbitrary-variety cross-correspondences. It therefore closes the uniform coefficient-descent calculation in that sector while leaving the stated arbitrary-motive/full-Tate gate explicit. No cyclicity or norm-only gcd formula is asserted; CC-AG14--15 show why those shortcuts are inadequate.

## Primary references and exact locators

- Milne, J. S. (1994). Motives over finite fields. In U. Jannsen, S. Kleiman, & J.-P. Serre (Eds.), *Motives* (Proceedings of Symposia in Pure Mathematics, Vol. 55, Part 1, pp. 401--459). American Mathematical Society. Version used: corrected author manuscript, November 2, 2019. https://www.jmilne.org/math/xnotes/Seattle1.pdf . Exact local-invariant and simple-object inputs: convention p. 17; Theorems 2.15--2.16, p. 18; Theorems 2.18--2.19, p. 20, applied only within the established abelian sector.
- Milne, J. S. (2020, July 19). *Algebraic number theory* (Version 3.08) [Author course notes]. https://www.jmilne.org/math/CourseNotes/ANT.pdf . Exact locators: prime-power cyclotomic degree and total ramification, Proposition 6.2(a),(c), pp. 96--97; cyclotomic degree, Theorem 6.4(a), p. 99; simple-root lifting, Proposition 7.31, p. 120; unramified extensions and roots of unity, Proposition 7.50 and Corollary 7.51, pp. 127--128; Frobenius description, Example 7.54, p. 129; completion decomposition, Propositions 8.1--8.2, p. 136. The principal-unit estimates, independently supported deep-subgroup bound, orbit-degree lemma, simultaneous local recurrence, conductor cutoff and exact positive-monoid deduction are proved in full above.

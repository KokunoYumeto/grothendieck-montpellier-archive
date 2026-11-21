# The complete finite-field profile of geometric rational descent

## CC-AG17 — Periodicity, divisor tables, and all source fields

Use the established rational abelian--Artin--Tate categories and the exact simple-object transition formulas of CC-AG08--09. Let

\[
 \xi=[\gamma,h],\qquad
 h=h_\xi,\qquad K=\mathbf Q(\gamma^n)\quad(n\ge1),
 \tag{CC-AG.171}
\]

be a stabilized geometric germ of weight \(w\), represented at its least positive exponent. Let \(H_a(\xi)\) be its geometric multiplicity monoid for source \(\mathbf F_{p^a}\), for \(a\ge1\).

Then

\[
 H_{a+h}(\xi)=H_a(\xi),\qquad
 H_a(\xi)=H_{\gcd(a,h)}(\xi),\qquad H_h(\xi)=\mathbf N.
 \tag{CC-AG.172}
\]

More generally,

\[
 \gcd(a,h)\mid\gcd(b,h)
          \quad\Longrightarrow\quad H_a(\xi)\subseteq H_b(\xi).
 \tag{CC-AG.173}
\]

The periodic equality has an explicit bijection on **all** source simple-label orbits, preserving the actual geometric multiplicity. After aligning a source label with the germ \(\xi\), that bijection is

\[
                 \alpha\longmapsto\alpha\gamma
       \quad\text{from source exponent }a\text{ to }a+h,
 \tag{CC-AG.174}
\]

with inverse \(\beta\mapsto\beta/\gamma\). These two labels have exactly the same centre and Schur index. The equality involving \(\gcd(a,h)\) is an equality of multiplicity monoids; it does not assert this particular bijection of simple orbits between arbitrary equal-gcd exponents.

Consequently the entire monoid profile over all finite source fields is determined by the finite table

\[
                         \{H_d(\xi):d\mid h\},
 \tag{CC-AG.175}
\]

which CC-AG16 computes by finite algebraic calculations. This uses the full positive monoids, including their gaps, rather than replacing them by gcd divisibility tests.

### Complete proof

We first make the orbit alignment in (CC-AG.174) precise. The stabilizer of the germ \(\xi\) in \(\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)\) is exactly \(\operatorname{Gal}(\overline{\mathbf Q}/K)\). One inclusion is immediate because \(\gamma\in K\). For the other, if \(\sigma\xi=\xi\), then some positive powers of the two stage-\(h\) representatives agree:
\[
                         \sigma(\gamma)^N=\gamma^N
\]
for a positive integer \(N\). Stabilization says that this power generates \(K\), so \(\sigma\) fixes \(K\) pointwise, and in particular fixes \(\gamma\).

Every source Galois orbit whose geometric germ orbit is \(O_\xi\) has a representative with germ exactly \(\xi\). Two such aligned representatives in the same full Galois orbit differ by an automorphism fixing \(K\), by the preceding stabilizer calculation. Thus these full source orbits correspond precisely to the \(\operatorname{Gal}(\overline{\mathbf Q}/K)\)-orbits of aligned labels.

Take an aligned source label \(\alpha\in W(p^a)\). For some \(N\ge1\),

\[
                         \alpha^{hN}=\gamma^{aN}.
 \tag{CC-AG.176}
\]

It follows that \(K\subset\mathbf Q(\alpha)\). Put \(\beta=\alpha\gamma\). At every complex embedding,
\[
 |\beta|=p^{aw/2}p^{hw/2}=p^{(a+h)w/2},
\]
and its valuations away from \(p\) vanish. Therefore \(\beta\) is a Weil \(p^{a+h}\)-number of weight \(w\). Equation (CC-AG.176) gives

\[
                        \beta^{hN}=\gamma^{(a+h)N},
 \tag{CC-AG.177}
\]

so its germ is again \(\xi\), and \(K\subset\mathbf Q(\beta)\). Since \(\gamma\in K\), the inclusions in both directions now give

\[
                       \mathbf Q(\alpha)=\mathbf Q(\beta)=L.
 \tag{CC-AG.178}
\]

Conversely, if \(\beta\) is an aligned label at source exponent \(a+h\), division by \(\gamma\) gives the correct Weil absolute values, the unit condition away from \(p\), and equation (CC-AG.176) at exponent \(a>0\). It is therefore the inverse operation. Multiplication and division are equivariant for automorphisms fixing \(K\), so the aligned-label bijection induces the claimed bijection on all source Galois orbits.

The source indices also agree. At a \(p\)-adic place \(z\) of the common centre \(L\), equation (CC-AG.176) implies
\[
 \frac{\operatorname{ord}_z(\alpha)}{a}
       =\frac{\operatorname{ord}_z(\gamma)}{h}.
\]
Hence

\[
 \frac{\operatorname{ord}_z(\beta)}{a+h}
       =\frac{\operatorname{ord}_z(\alpha)}{a}.
 \tag{CC-AG.179}
\]

The normalized slopes, local field degrees and therefore the \(p\)-adic Brauer invariants in the source-index formula are the same. At every real place the weight is the same, so the invariant \(w/2\) is unchanged; at the remaining places both invariants vanish. Their least common denominators are equal:

\[
                              d_\beta=d_\alpha.
 \tag{CC-AG.180}
\]

Using the exact transition formula,
\[
 r_\beta=[L:K]d_\beta/d_\xi
        =[L:K]d_\alpha/d_\xi=r_\alpha.
 \tag{CC-AG.181}
\]
The bijection of simple orbits therefore preserves every positive multiplicity sum, giving \(H_{a+h}(\xi)=H_a(\xi)\). It also gives a bijection of isomorphism classes of all source objects with geometric image \(S_\xi^{\oplus r}\), for every fixed \(r\), by transporting their simple summands and multiplicities.

For the divisor assertions, finite-field base extension supplies

\[
                         H_a(\xi)\subseteq H_{ua}(\xi)
                       \qquad(u\in\mathbf Z_{>0}),
 \tag{CC-AG.182}
\]

because the subsequent geometric base extension is the same. If \(\gcd(a,h)\mid\gcd(b,h)\), the congruence \(au\equiv b\pmod h\) has an integer solution. Adding a positive multiple of \(h/\gcd(a,h)\) makes \(u\) positive. Periodicity equates the monoids at the two positive congruent exponents \(au\) and \(b\). Combining with (CC-AG.182) proves (CC-AG.173). Taking \(b=\gcd(a,h)\), and then using the reverse inclusion since \(b\mid a\), gives \(H_a(\xi)=H_{\gcd(a,h)}(\xi)\).

Finally the finite label \(\gamma\) over \(\mathbf F_{p^h}\) has centre \(K\). Its local invariants are exactly the geometric invariants of the stabilized germ, including the real-place convention, so its finite index is \(d_\xi\). The transition multiplicity is \(1\). Direct sums give \(H_h(\xi)=\mathbf N\). This proves all assertions in (CC-AG.172)--(CC-AG.175). \(\square\)

### The field-of-definition profile of a specified geometric object

Let

\[
                  Z=\bigoplus_{j=1}^s S_{\xi_j}^{\oplus r_j}
 \tag{CC-AG.183}
\]

be a geometric rational object in the established sector, with distinct simple germ orbits and positive multiplicities. Put

\[
                              H=\operatorname{lcm}(h_{\xi_1},\ldots,h_{\xi_s}).
 \tag{CC-AG.184}
\]

There is an effectively computable finite antichain \(\mathcal D_Z\) of divisors of \(H\), with respect to divisibility, such that for every \(a\ge1\),

\[
 Z\text{ comes from }\mathcal A_{p^a}
       \quad\Longleftrightarrow\quad
                 d\mid a\text{ for some }d\in\mathcal D_Z.
 \tag{CC-AG.185}
\]

Here “comes from” means isomorphism after geometric base extension; it does not choose or preserve a finite target-field model.

**Proof and finite construction.** For every divisor \(e\mid H\), test the finite collection of conditions

\[
                r_j\in H_{\gcd(e,h_{\xi_j})}(\xi_j)
                         \qquad(1\le j\le s).
 \tag{CC-AG.186}
\]

These are decidable either from the whole-monoid tables of CC-AG16 or directly from the earlier specified-object procedure CC-AG12. By positivity and the one-orbit image of each source simple, their conjunction is exactly descent of \(Z\) from \(\mathbf F_{p^e}\).

The set of successful divisors is nonempty: \(e=H\) succeeds by \(H_{h_{\xi_j}}(\xi_j)=\mathbf N\). It is upward closed under divisibility, by finite-field base extension. Define \(\mathcal D_Z\) to be its minimal elements. This is a finite, effectively computable antichain.

For any \(a\ge1\), set \(e=\gcd(a,H)\). Then
\(\gcd(e,h_{\xi_j})=\gcd(a,h_{\xi_j})\) for every \(j\). The first part of the theorem shows that descent at \(a\) is equivalent to success of the divisor \(e\). Since the successful set is upward closed in the finite divisor poset, this is equivalent to \(d\mid e\) for some \(d\in\mathcal D_Z\). Because every such \(d\) divides \(H\), this is equivalent to \(d\mid a\), proving (CC-AG.185).

For the zero object use \(H=1\) and \(\mathcal D_Z=\{1\}\), giving descent from every source field. No assumption that the antichain has only one element is needed or made. \(\square\)

### The complete profiles of the two explicit threefold germs

For each of the examples CC-AG14 and CC-AG15, \(h=9\) and \(d_\xi=3\). Their entire source-field profiles are therefore:

| Condition on the source exponent \(a\) | CC-AG14, characteristic \(2\) | CC-AG15, characteristic \(163\) |
|---|---|---|
| \(3\nmid a\) | \(3\mathbf N\) | \(3\mathbf N\) |
| \(3\mid a,\ 9\nmid a\) | \(\langle2,3\rangle_{\mathbf N}\) | \(3\mathbf N\) |
| \(9\mid a\) | \(\mathbf N\) | \(\mathbf N\) |

Indeed the three divisors of \(h\) are \(1,3,9\). At \(1\), CC-AG13 gives \((h/d_\xi)\mathbf N=3\mathbf N\); at \(3\), CC-AG14 and CC-AG15 give the two different monoids displayed; at \(9\), (CC-AG.172) gives \(\mathbf N\). The gcd reduction proves every entry for all positive \(a\).

### Source scope and what has been computed

For a single germ, only the divisor table of its computable exponent \(h_\xi\) is needed to know its multiplicity monoid over every finite source field. For a specified geometric object, (CC-AG.185) computes its entire geometric field-of-definition profile as a finite union of divisibility conditions. A fixed source's actual preimage isomorphism classes remain those of CC-AG12; the periodic orbit bijection (CC-AG.174) transports them between source exponents differing by \(h_\xi\).

The proofs use the inspected Milne classification and transition theorem in the established abelian--Artin--Tate sector. They do not supply correspondences placing an arbitrary numerical motive in that sector, and do not make a finite-target descent statement by changing a Frobenius label.

## Primary reference

Milne, J. S. (1994). Motives over finite fields. In U. Jannsen, S. Kleiman, & J.-P. Serre (Eds.), *Motives* (Proceedings of Symposia in Pure Mathematics, Vol. 55, Part 1, pp. 401--459). American Mathematical Society. Version used: corrected author manuscript, November 2, 2019. https://www.jmilne.org/math/xnotes/Seattle1.pdf . Exact classification and local-invariant inputs: convention p. 17; Theorems 2.15--2.16, p. 18; Theorems 2.18--2.19, p. 20. The orbit alignment, periodic bijection, divisor-table reduction and finite field-of-definition profile are proved in full above.

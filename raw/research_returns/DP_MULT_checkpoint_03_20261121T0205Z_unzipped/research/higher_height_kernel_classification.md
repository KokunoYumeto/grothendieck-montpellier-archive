# Classification of the scalar higher-height kernel

Date: 2026-11-21 (UTC). Agent: /root/formal_bound, inherited GPT-6 Astra Pro; effort setting not exposed. This supplements higher_height_kernel_attempt.md. It uses a known primary-source biextension theorem; the coefficient arguments establishing the integral passage and normalization are written out to expose all hypotheses. No Lean execution or compilation is claimed.

## HK5 / proposed DP31: full scalar derivative slope after integral trivialization

Let \(p\) be odd, let \(h>2\), let \(q=p^h\), and let \(k\) be a perfect field containing \(\mathbf F_q\). Put
\[
 R=W(k),\qquad K=R[1/p],\qquad
 L(T)=\sum_{e\ge0}\frac{T^{q^e}}{p^e},\qquad E=L^{-1}.
\]
Let \(G\) be the integral one-dimensional height-\(h\) formal group with logarithm \(L\). Let \(\zeta\in R^\times\) be a primitive \((q-1)\)-st Teichmüller root.

Assume \(\beta\in K[[X,Y]]\) vanishes on both axes, is invariant under
\[
 (X,Y)\longmapsto(\zeta X,\zeta^{-p}Y),
\]
and the two series
\[
 C_X(S,S',T)
 =\exp\!\left(\beta(L(S)+L(S'),L(T))
             -\beta(L(S),L(T))-\beta(L(S'),L(T))\right),
\]
\[
 C_Y(S,T,T')
 =\exp\!\left(\beta(L(S),L(T)+L(T'))
             -\beta(L(S),L(T))-\beta(L(S),L(T'))\right)
\]
are integral units with constant coefficient \(1\).

Then
\[
 \boxed{\quad B(S,T):=\exp\beta(L(S),L(T))
                   \ \in\ 1+ST\,R[[S,T]].\quad}
 \tag{HK5.1}
\]

This is stronger than the general elementary estimate HK3 in the companion memo, but its base ring is now explicitly \(W(k)\), and it uses the formal biextension classification. It does not assume or assert a theta realization.

As a consequence, for a finite set \(J\), an integral series \(U\in R[[S_j:j\in J]]\), integral linear forms \(\ell_j(\mathbf t)\) in \(N\) variables, a unit \(\epsilon\in R^\times\), and \(\sigma\in\{1,-1\}\), the same scalar kernel as in HK3,
\[
 \Theta(\mathbf t)=
 U(E(\ell_j(\mathbf t)):j\in J)
 \exp\left(\frac{\sigma}{2}\sum_{j\in J}
       \beta(\ell_j(\mathbf t),\epsilon\ell_j(\mathbf t))\right),
\]
satisfies
\[
 \boxed{\quad
 v_p\!\left(\kappa!\,[\mathbf t^\kappa]\Theta\right)
 \ge c_h|\kappa|-\frac{\sum_i s_p(\kappa_i)}{p-1},
 \qquad
 c_h=\frac1{p-1}-\frac1{p^h-1}.
 \quad}
 \tag{HK5.2}
\]
The bound is a consequence of integrality (HK5.1), not of the false higher-height version of source LemmaS. The explicit nonzero integral-unit correction in HK4 shows that this slope is sharp within this scalar class.

## 1. The exact known classification input

Thomas Zink, “The display of a formal \(p\)-divisible group,” Astérisque **278** (2002), 127–248, §4.4:

- Proposition 121, beginning on p.241, identifies the dual formal group obtained from the dual display with the formal part of \(\underline{\mathrm{Ext}}^1(G,\widehat{\mathbf G}_m)\).
- Equation **(243)** and the paragraph immediately following it, p.246, give an **injective** homomorphism
  \[
   \mathrm{Biext}^1(G\times G',\widehat{\mathbf G}_m)
       \hookrightarrow \mathrm{Hom}(G,(G')^t)
   \tag{HK5.3}
  \]
  when \(G,G'\) are formal groups of displays. This is the part needed here.
- Diagram (244) and Theorem 122, p.247, identify the map with the bilinear-form/display description and give an isomorphism under the stated \(F\)-nilpotence condition.
- The existence of displays for the formal \(p\)-divisible groups under consideration is covered by the equivalence stated as Theorem 9 in the introduction: an excellent local ring on which \(p\) is nilpotent is allowed. Each \(R/p^nR\) is an Artinian local ring with nilpotent \(p\), so it lies in that scope.

The dual here agrees with the Cartier dual for a \(p\)-divisible group when that Cartier dual is connected. For the present one-dimensional height-\(h\) group, the special-fibre slopes of \(G\) and \(G^t\) are \(1/h\) and \((h-1)/h\); both groups are connected for \(h>1\). These are the standard Dieudonné slope and Cartier-duality facts already used in the main formal-group analysis. Disjoint slopes imply zero Hom over the residue field. The proof below does not infer integral triviality directly from that rational slope statement: it supplies reduction injectivity, a trivialization at every \(p^n\), uniqueness, and inverse-limit compatibility.

The exact known reference for this Hom vanishing was subsequently verified: N. M. Katz, “Slope filtration of F-crystals,” Astérisque 63 (1979), §1.3, pp.119–120, first paragraph of p.120. The unnumbered Dieudonné semisimplicity theorem there identifies the simple objects \(E(\lambda)\) by slope. Distinct slopes have disjoint simple constituents, so their Hom vanishes; faithful extension to an algebraic closure handles perfect \(k\). This is not the statement numbered 1.3.1. The primary PDF and visually inspected p.120 are recorded in paper_review_dp28_dp29.md.

Published primary source:
https://www.numdam.org/article/AST_2002__278__127_0.pdf

Author's public version:
https://www.math.uni-bielefeld.de/~zink/display.pdf

The author's version numbers the injection (244) on its printed p.118, and the diagram (245) on p.119. **Use the published equation number (243), p.246, when citing the Astérisque version.**

## 2. Integral coboundaries define the required biextension

Over \(K\), define \(B=\exp\beta(L(S),L(T))\). Because \(\beta\) vanishes on the axes, \(B(S,0)=B(0,T)=1\). Let \(F\) be the law of \(G\). The two assumed integral series are exactly
\[
 C_X(S,S',T)=\frac{B(F(S,S'),T)}{B(S,T)B(S',T)},\qquad
 C_Y(S,T,T')=\frac{B(S,F(T,T'))}{B(S,T)B(S,T')}.
 \tag{HK5.4}
\]
They satisfy the two symmetric associativity identities and the interchange identity: these follow by taking the corresponding two multiplicative coboundaries of \(B\). The identities hold integrally because all their terms are integral and \(R\hookrightarrow K\) is injective.

Thus, on the trivial \(\widehat{\mathbf G}_m\)-torsor over \(G\times G\), use the multiplication factors \(C_X\) and \(C_Y\) in the two group directions. These identities make it a commutative biextension. Concretely, the first partial multiplication of fibre coordinates is
\[
 (S,T,u)\star_X(S',T,u')
   =(F(S,S'),T,uu'C_X(S,S',T)),
\]
and likewise in the second direction. Its normalized splitting by a unit \(I\) is precisely the pair of equations
\[
 \frac{I(F(S,S'),T)}{I(S,T)I(S',T)}=C_X,\qquad
 \frac{I(S,F(T,T'))}{I(S,T)I(S,T')}=C_Y.
 \tag{HK5.5}
\]
The integral unit \(I\) is what must be established; using the nonintegral candidate \(B\) over \(K\) at this stage does not presume the conclusion.

## 3. Zero Hom over every \(R/p^nR\)

Write \(R_n=R/p^nR\), \(G_n=G\otimes R_n\), and \(G_n^t=G^t\otimes R_n\). On the special fibre, the distinct slopes \(1/h\) and \((h-1)/h\) give
\[
 \mathrm{Hom}(G_1,G_1^t)=0.
 \tag{HK5.6}
\]

Here is a direct injectivity argument for reduction in this particular setting. Let \(f:G_n\to G_n^t\) be a homomorphism whose reduction is zero. Choose formal coordinates on the connected target. Each coordinate of \(f\) lies in \(pR_n[[T]]\). Suppose inductively that all coordinates lie in \(p^jR_n[[T]]\), with \(1\le j<n\), and write \(f=p^jg\) coordinatewise.

The target multiplication-by-\(p\) series has linear term \(p\) times the identity and terms of order at least two thereafter. Consequently
\[
 [p]_{G_n^t}(f(T))\equiv0\pmod {p^{j+1}}
\]
because \(2j\ge j+1\). Since \(f\) is a homomorphism,
\[
 p^j\,\overline g([p]_{G_1}(T))=0\pmod {p^{j+1}},
\]
so \(\overline g([p]_{G_1}(T))=0\) over \(k\). The scalar series \([p]_{G_1}(T)\) has nonzero initial term of degree \(q\). Composition with it is injective on \(k[[T]]\): a nonzero series of initial degree \(d\) acquires initial degree \(qd\) with nonzero coefficient. Hence \(\overline g=0\) in each target coordinate. This raises the divisibility of \(f\) to \(p^{j+1}\). Induction proves \(f=0\).

Together with (HK5.6), this yields
\[
 \mathrm{Hom}(G_n,G_n^t)=0
 \quad\text{for every }n\ge1.
 \tag{HK5.7}
\]
No comparison of generic-fibre slopes is being used.

By Zink's injection (HK5.3), the reduction modulo \(p^n\) of the biextension in §2 has zero class. It therefore has an integral normalized splitting
\[
 I_n\in1+ST\,R_n[[S,T]]
\]
satisfying (HK5.5) modulo \(p^n\).

## 4. Uniqueness and the integral inverse limit

Two splittings differ by a normalized bihomomorphism \(J\in1+ST\,R_n[[S,T]]\) from \(G_n\times G_n\) to \(\widehat{\mathbf G}_m\). In particular
\[
 J([p]_{G_n}(S),T)=J(S,T)^p.
 \tag{HK5.8}
\]

First work modulo \(p\). If \(J\ne1\), take the least positive \(T\)-degree \(b\) occurring in \(J-1\), and write its nonzero coefficient as \(j_b(S)\in k[[S]]\). On the left of (HK5.8), the coefficient at \(T^b\) is \(j_b([p]_{G_1}(S))\ne0\). On the right, Frobenius makes all positive \(T\)-degrees at least \(pb>b\). This is a contradiction. Hence \(J=1\) modulo \(p\).

For the lift, suppose \(J-1=p^jV\) with \(j\ge1\). The right side of
\[
 (J-1)([p]S,T)=(1+(J-1)(S,T))^p-1
\]
is divisible by \(p^{j+1}\): its linear term is \(p(J-1)\), and every higher term has valuation at least \(2j\ge j+1\). Dividing by \(p^j\) and reducing gives
\[
 \overline V([p]_{G_1}(S),T)=0.
\]
Composition in \(S\) is injective on \(k[[S,T]]\) for the same initial-degree reason, now with coefficients in the domain \(k[[T]]\). Thus \(J-1\) is divisible by \(p^{j+1}\). This proves \(J=1\) over \(R_n\).

The splitting \(I_n\) is therefore unique. Reduction of \(I_{n+1}\) satisfies the same equations as \(I_n\), so uniqueness makes the family compatible. Since \(R\) is \(p\)-adically complete, the coefficientwise inverse limit gives
\[
 I\in1+ST\,R[[S,T]]
\]
with exactly the two integral coboundaries (HK5.5).

## 5. The torus removes the remaining generic bilinear term

In additive coordinates, put
\[
 A(X,Y)=\beta(X,Y)-\log I(E(X),E(Y)).
\]
Equations (HK5.4)–(HK5.5) show that \(A\) is additive separately in \(X\) and \(Y\). In characteristic zero, a formal series additive in one variable is linear in that variable, as one sees from the interior binomial coefficients of each monomial. Hence
\[
 A(X,Y)=aXY
 \quad\text{for some }a\in K.
 \tag{HK5.9}
\]

The logarithm and exponential are equivariant under \(\mu_{q-1}\). Therefore the assumed invariance of \(\beta\) makes \(B\), and then both of its coboundaries, invariant under simultaneous multiplication of the first-variable inputs by \(\zeta\) and the second-variable inputs by \(\zeta^{-p}\).

It follows that \(I_n(\zeta S,\zeta^{-p}T)\) is another integral normalized splitting of the same biextension. Uniqueness in §4 gives its equality with \(I_n\), and the inverse limit gives the same invariance for \(I\). Thus the difference \(aXY\) in (HK5.9) is invariant. But
\[
 aXY\longmapsto a\zeta^{1-p}XY,
\]
and \(\zeta^{1-p}\ne1\), since \(q-1>p-1>0\). Therefore \(a=0\). We have \(\beta(X,Y)=\log I(E(X),E(Y))\), or equivalently \(B=I\). This proves (HK5.1).

## 6. The final coefficient bound

The correction factor of the scalar kernel can now be written as
\[
 \prod_{j\in J}
 B(E(\ell_j),E(\epsilon\ell_j))^{\sigma/2}.
\]
Because \(p\) is odd, the exponent \(\sigma/2\) lies in \(\mathbf Z_p\), and every such binomial power of an integral unit with constant coefficient \(1\) is integral. Thus the whole kernel is an integral power series in the finitely many coordinates \(E(\ell_j)\) and \(E(\epsilon\ell_j)\).

The inverse-logarithm estimate gives weighted valuation at least \(\rho_h=1/(q-1)\) to each such coordinate when every \(\mathbf t\)-variable has weight \(\rho_h\). Integral linear substitutions preserve this bound. The entire kernel consequently has weighted valuation at least zero:
\[
 v_p([\mathbf t^\kappa]\Theta)\ge-\rho_h|\kappa|.
\]
Adding Legendre's exact factorial valuation proves (HK5.2).

The explicit kernel in HK4,
\[
 E(t)(1+E(t)^pE(\epsilon t))^{1/2},
\]
has nonzero correction and exact derivative valuations \(c_h(q^r-1)\) at \(n=q^r\). Thus the full slope \(c_h\) occurs in this class; the improved final bound is compatible with the failure of the intermediate LemmaS estimate in DP28.

## 7. What this resolves, and what it does not

This resolves the analytic scalar replacement question under the stated unramified hypotheses: the natural two-scalar generalized BHyp actually forces the correction to be an integral-unit gauge for \(h>2\), and the final derivative bound can use \(c_h\).

It also explains why this replacement is geometrically different from the original height-two self-dual situation. The proof uses
\[
 \mathrm{Hom}(G,G^t)=0.
\]
For the genuinely dual pair \(G\times G^t\), however, the corresponding classification target is
\[
 \mathrm{Hom}(G,(G^t)^t)=\mathrm{End}(G),
\]
which is nonzero. The second factor there has dimension \(h-1\). The scalar integrality theorem does not construct or estimate that multivariate dual kernel. It supplies neither the required normalized theta realization nor the prescribed Cartier minors/nonvanishing nor a comparison of lift multiplicity and cost.

The smaller remaining construction problem is therefore explicit: build and bound the one-dimensional-by-\((h-1)\)-dimensional dual kernel, with its actual CM signature and polarization, and supply the corresponding integral theta/jet and nonvanishing interfaces. It is no longer accurate to describe the scalar analytic \(q\)-logarithm substitution itself as unresolved.

## 8. Genuine check and source-recovery record

- 2026-11-21 00:50:09 UTC: primary-source search identified Zink's display duality and Mumford's formal biextension paper. The direct Mumford PDF fetch returned HTTP 503; this was not used to infer a mathematical limitation.
- 2026-11-21 00:54:52 UTC: opened the author's Zink PDF and read the exact introductory hypotheses and the formal duality section through the web tool.
- 2026-11-21 00:57:26.597668 UTC: downloaded the 11,718,483-byte published Numdam PDF. SHA-256: 2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69.
- 2026-11-21 00:58:12.392312 UTC: downloaded the 850,452-byte author PDF. SHA-256: ca30bdcc7c2b04ac54854e36e8090947a7ee79cf43d2dc6a794520cf590665e2.
- 2026-11-21 00:58:38 UTC observed clock, followed by direct page inspection: checked the published p.246 injection and p.247 Theorem 122 against rendered page images, finding and correcting the one-step equation-number difference from the author's version.
- The coefficientwise rigidity, normalized bihomomorphism uniqueness, inverse-limit passage, and torus elimination were developed and checked by this agent. A separate parent proof challenge has been requested. It is not claimed to have occurred until the parent records its own review.

Local primary-source files: Zink_2002_Display.pdf and Zink_2002_Display_author.pdf. Inspected images: zink_p246.png, zink_p247.png; the author's p.118 was also inspected as zink_author_p118.png.


## HK-C4: complete proof challenge

At 2026-11-21 01:02:29 UTC (observed clock), this agent completed a full self-challenge of the hypotheses and proof, including the formal torsor cocycle identities, the connectedness of the Cartier dual, reduction injectivity for a multidimensional target, normalized splitting uniqueness modulo every \(p^n\), the coefficientwise inverse limit, torus equivariance, and the final binomial-power substitution. All steps passed this self-review. Model: inherited GPT-6 Astra Pro; effort not exposed. This is not a separate-model review or a Lean check.

The same agent also challenged the sibling's DP30 argument at this stage: the Cartier-dual orientation, the quotient \(G[p]/G[F]=\ker V_G\), its identification with the relative \((h-1)\)-st Frobenius kernel by the defining ideal \((T^{p^{h-1}})\), the Teichmüller degree cutoff, the primitive elements of \(k[t]/t^{p^{h-1}}\), and the lifting of a primitive invariant derivation all passed. The quotient identification does not assert equality of Verschiebung with a Frobenius iterate as morphisms.

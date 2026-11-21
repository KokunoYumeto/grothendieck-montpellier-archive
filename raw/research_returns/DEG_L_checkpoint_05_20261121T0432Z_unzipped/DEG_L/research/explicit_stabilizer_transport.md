# DEG_L / explicit stabilizer and source-degree bounds

Run DEG_L_20261121; author /root/lvalue_bounds; GPT-6 Astra Pro; effort not exposed. This refines the existence constant in B21. The geometric input is the classical generalized Bézout inequality, imported with its exact source; the argument below tracks its constants in the present transport problem.

## B22. Explicit stabilizer bound and a necessary source-degree growth rate

Let $(A_0,L_0)$ be a polarized complex abelian variety, and fix an integer $k\ge1$ such that $L_0^{\otimes k}$ is very ample. Let $Z\subset A_0$ be an integral subvariety of dimension $n\ge1$ with finite translation stabilizer. Set
\[
 D=\deg_{L_0}Z=\int_Zc_1(L_0)^n.
\]
Then
\[
 |\operatorname{Stab}_{A_0}(Z)|
 \le (k^nD)^{n+1}
 =k^{n(n+1)}D^{n+1}.
\tag{B22.1}
\]
In particular, one may use $k=3$ for every ample line bundle on an abelian variety. If $L_0$ is already very ample, one may use $k=1$. Simplicity of $A_0$ is sufficient for the finite-stabilizer hypothesis whenever $0<n<\dim A_0$, but is not needed for (B22.1) itself.

Now retain the fixed simple CM reference and compatible generic Weil data of B19--B21, with $\dim A_0=2n$, target polarization volume $V=\chi(L)$, fixed integral-projector denominator $R$, and target maximal-order core index $J$. For every integral source witness $Z\subset A_0$ with $e_0[Z]\ne0$ and every nonzero integral $E$-linear homomorphism $h:A_0\to A$, write
\[
 D'=\deg_Lh(Z)_{\mathrm{red}}.
\]
There is the explicit inequality
\[
 D'D^{n+1}
 \ge
 \frac{\sqrt2\,n!\sqrt V}{R\,k^{n(n+1)}}\sqrt J.
\tag{B22.2}
\]
Consequently a transport construction satisfying $D'\le B$, with $B>0$ fixed, must use
\[
 D\ge k^{-n}
 \left(\frac{\sqrt2\,n!\sqrt V}{RB}\right)^{1/(n+1)}
 J^{1/(2(n+1))}.
\tag{B22.3}
\]
For surfaces in abelian fourfolds, the universal choice $k=3$ gives
\[
 D\ge\frac19
 \left(\frac{2\sqrt2\sqrt V}{RB}\right)^{1/3}J^{1/6}.
\tag{B22.4}
\]
No optimality of the exponent in (B22.1) or (B22.3) is asserted. These are necessary bounds for the specified transport mechanism, not lower bounds for the intrinsic least degree of a target Weil witness.

### Proof of (B22.1)

Write $H=\operatorname{Stab}_{A_0}(Z)$. As sets of complex points,
\[
 H=\bigcap_{z\in Z}(Z-z).
\tag{B22.5}
\]
Indeed, membership on the right says that $a+Z\subseteq Z$. Both sides of this inclusion are irreducible closed subvarieties of the same dimension, so the inclusion is equality. Conversely, a stabilizing translation belongs to every displayed translate.

We select at most $n+1$ of the translates in (B22.5) whose intersection is finite. Start with any $z_0\in Z$ and $X_0=Z-z_0$. Suppose that $X_j$ has a positive-dimensional irreducible component $C$. Since $H$ is finite, choose $c_C\in C\setminus H$. By (B22.5), there is a point of $Z$ whose translate does not contain $c_C$. Equivalently,
\[
 B_C=\{z\in Z:c_C\in Z-z\}=Z\cap(Z-c_C)
\]
is a proper closed subset of $Z$. There are only finitely many positive-dimensional components $C$ of $X_j$. Irreducibility of $Z$ allows a point $z_{j+1}$ outside their finitely many proper closed sets $B_C$. The translate $Z-z_{j+1}$ then contains none of those components in its entirety. Thus
\[
 X_{j+1}=X_j\cap(Z-z_{j+1})
\]
has strictly smaller dimension on every previously positive-dimensional component. Starting at dimension $n$, after at most $n$ further intersections all components have dimension zero. The resulting nonempty finite intersection contains $H$. If it becomes finite sooner, repeat any one of the already chosen translates to have exactly $n+1$ factors.

Translation on the connected complex torus $A_0$ acts trivially on integral cohomology, hence preserves numerical degree. In the fixed embedding defined by $L_0^{\otimes k}$, all of these $n+1$ translates have degree $k^nD$.

We now apply Fulton, *Intersection Theory*, second edition, Example 8.4.7, printed p.148: for subvarieties of a fixed projective scheme with finite intersection, the number of intersection points is at most the product of their projective degrees. Its input, Example 8.4.6 on the same page, bounds the sum of degrees of all irreducible components of an arbitrary intersection and imposes no proper-intersection hypothesis. Therefore
\[
 |H|\le\#\bigcap_{j=0}^{n}(Z-z_j)
 \le\prod_{j=0}^{n}(k^nD)=(k^nD)^{n+1}.
\]
This proves (B22.1). The classical fact that $L_0^{\otimes3}$ is very ample is stated, for example, in Milne, *Abelian Varieties*, version 2.00, Chapter I, section 6, printed p.30, in the paragraph immediately preceding Example 6.5. We import this fact; no new proof of very ampleness or of Bézout is intended here. QED.

### Proof of (B22.2)--(B22.4)

The generic degree of $h$ on $Z$ is, by the exact B20 finite-kernel count,
\[
 \delta_h=|\ker h\cap\operatorname{Stab}_{A_0}(Z)|
 \le k^{n(n+1)}D^{n+1}.
\tag{B22.6}
\]
The strengthened B18 even-square integrality gives
\[
 \|e_0[Z]\|_{q_0}\ge\frac{\sqrt2}{R}.
\]
Poincaré pairing under the finite isogeny and the comass bound B7 give
\[
 \begin{aligned}
 \delta_hD'
 &=\deg_Lh_*Z\\
 &\ge n!\sqrt V\,\|e_Ah_*[Z]\|_{q_A}\\
 &=n!\sqrt V\sqrt{\deg h}\,\|e_0[Z]\|_{q_0}\\
 &\ge\frac{\sqrt2\,n!\sqrt V}{R}\sqrt J.
 \end{aligned}
\tag{B22.7}
\]
The last inequality uses $\deg h\ge J$, the exact integral Hom lattice bound B19. No choice of a small homomorphism is needed for this lower bound. Combining (B22.6) and (B22.7) proves (B22.2); taking the $(n+1)$st root proves (B22.3). Substitution of $n=2$ and $k=3$ proves (B22.4). QED.

### Consequences and limits

One may replace the abstract constant of B21 by the explicit value
\[
 S_{A_0,L_0,n}(D_0)=k^{n(n+1)}D_0^{n+1}.
\]
Thus every target-dependent choice of source witnesses of degrees at most $D_0$ satisfies the fully explicit lower bound obtained by substituting this expression into B21.2. The Hilbert-scheme proof B21 remains useful for arbitrary boundary subschemes and for other bounded families; the present sharper constant applies to the reduced integral witnesses needed in the transport construction.

The result does not say that growing the source degree at the indicated rate is sufficient. It also does not exclude new target cycles, or a construction using a changing reference family. In particular, an obstruction to these reference-isogeny transports cannot be promoted to a lower bound for intrinsic bounded-division complexity. Dirichlet GRH and Hecke GRH do not enter the argument.

### Primary sources and actual reading scope

- William Fulton, *Intersection Theory*, second edition, Springer, 1998, Examples 8.4.5--8.4.7, printed pp.147--148. The original page images were visually read, including the full ruled-join reduction in Example 8.4.5, the complete short proof of the generalized Bézout inequality in Example 8.4.6, and the finite-intersection specialization in Example 8.4.7. The source scan is <https://djvu.online/file/Pl4avuZzLcI6I>; the exact original page images are <https://djvu.online/jpg2/P/l/4/Pl4avuZzLcI6I/161.webp> and <https://djvu.online/jpg2/P/l/4/Pl4avuZzLcI6I/162.webp>. Local checked images are `work/external/Fulton_page161.webp` and `work/external/Fulton_page162.webp`.
- J.S. Milne, *Abelian Varieties*, version 2.00, 16 March 2008, Chapter I, section 6, printed p.30, the paragraph immediately preceding Example 6.5: the cube of any ample line bundle on an abelian variety is very ample. Official source <https://www.jmilne.org/math/CourseNotes/AV.pdf>, PDF index 35. The exact assertion was read; this source states it without proof, and its upstream proof is imported.
- Marc Hindry, *Autour d'une conjecture de Serge Lang*, Invent. Math. 94 (1988), Lemmas 5--8, printed pp.579--581, gives the related degree-and-equation formulation for stabilizers. The original author-hosted scan <https://webusers.imj-prg.fr/~marc.hindry/Conj-Lang.pdf> was read on those pages, including the full proof of Lemma 8. Its extra equation-degree hypotheses are unnecessary in the direct numerical-degree application of Fulton above; no unverified conversion from defining-equation degree is used.
- B7, strengthened B18, B19.8, B20 and B21 supply the already checked polarization normalization, integral Weil lower bound, integral Hom index, and generic-degree identity. The whole argument above, including the finite intersection selection and exponents, has been read and checked. No proof-assistant verification is claimed.

## B22a. Two translates and an intrinsic quadratic stabilizer bound

Assume that $A_0$ is simple of complex dimension $2n$, and let $Z\subset A_0$ be an integral subvariety of dimension $n\ge1$. Write
\[
 D=\deg_{L_0}Z,\qquad V_0=\chi(L_0),\qquad H=\operatorname{Stab}_{A_0}(Z).
\]
Then the difference map $\Delta:Z\times Z\to A_0$, $(z_1,z_2)\mapsto z_1-z_2$, is dominant and generically finite. Its degree is the positive self-intersection of the middle-dimensional class. More precisely,
\[
 \begin{aligned}
 d_\Delta&=\int_{A_0}[Z]^2>0,\\
 d_\Delta/|H|&\in2\mathbf Z_{>0},\\
 |H|&\le\frac12\int_{A_0}[Z]^2
 \le\frac{D^2}{4(n!)^2V_0}.
 \end{aligned}
\tag{B22a.1}
\]
The last inequality uses the polarization metric directly; no projective-embedding power is needed.

In the fixed simple CM transport setting of B19--B23, for a source witness with nonzero generic Weil projection and target reduced-image degree $D'$, this improves (B22.2) to
\[
 D'D^2\ge
 \frac{4\sqrt2\,(n!)^3V_0\sqrt V}{R}\sqrt J.
\tag{B22a.2}
\]
Thus $D'\le B$ requires
\[
 D\ge
 \left(\frac{4\sqrt2\,(n!)^3V_0\sqrt V}{RB}\right)^{1/2}J^{1/4}.
\tag{B22a.3}
\]
For surfaces in abelian fourfolds the constant inside the square root is $32\sqrt2\,V_0\sqrt V/(RB)$. These bounds retain exactly the reference-transport scope of B22.

### Proof of dominance and the self-intersection formula

We use the characteristic-zero sum-dimension theorem in its standard geometric-nondegeneracy formulation. Debarre, *On the geometry of abelian varieties*, Chapter 1, Definition 2.1 and Examples 2.2(2), printed p.8, states that every irreducible subvariety of a simple complex abelian variety is geometrically nondegenerate. Corollary 2.5(a), printed pp.9--10, then gives
\[
 \dim(V+W)=\min(\dim V+\dim W,\dim A_0)
\]
when $V$ is geometrically nondegenerate. Smoothness of the subvarieties is not assumed. Apply this to $V=Z$ and $W=-Z$. It gives $Z-Z=A_0$ and hence dominance of $\Delta$. The dimensions of its domain and target are both $2n$, so it is generically finite. These classical results are imported, not reproved here.

We spell out the generic-fibre issue for possibly singular $Z$. The singular boundary
\[
 (Z_{\mathrm{sing}}\times Z)\cup(Z\times Z_{\mathrm{sing}})
\]
has dimension at most $2n-1$. Its image under the proper map $\Delta$ is a proper closed subset of $A_0$. Remove it. Also restrict to a nonempty open set where the proper generically finite map is finite. In characteristic zero, generic smoothness, followed by removing the image of the remaining ramification locus of this finite map, gives a further nonempty open set over which it is étale. Fibres there consist of exactly $d_\Delta$ reduced points, all lying in $Z_{\mathrm{reg}}\times Z_{\mathrm{reg}}$.

For such a point $u\in A_0$, the first projection identifies $\Delta^{-1}(u)$ with $Z\cap(Z+u)$. At a corresponding pair $(z_1,z_2)$ the kernel of the differential of $\Delta$ is the intersection of the translated tangent spaces $T_{z_1}Z\cap T_{z_2}Z$. Étaleness makes this zero; since both tangent spaces have dimension $n$, the intersection is transverse in the ambient $2n$-fold. Every local intersection multiplicity is therefore one. Translation acts trivially on cohomology, so
\[
 d_\Delta=\#\bigl(Z\cap(Z+u)\bigr)=\int_{A_0}[Z]^2>0.
\tag{B22a.4}
\]

This also gives the proposed two-translate argument explicitly. Choose $(z_1,z_2)\in\Delta^{-1}(u)$. The finite intersection $(Z-z_1)\cap(Z-z_2)$ is isomorphic to the same fibre and contains $H$. Equivalently, $H$ acts freely by simultaneous translation on every such difference fibre. In particular $|H|$ divides $d_\Delta$. Fulton Example 8.4.7 would already give the quadratic bound $|H|\le k^{2n}D^2$; the next two steps improve its constant.

### Proof of the factor two and the metric bound

Let $q:A_0\to A_0/H$ be the quotient isogeny, of degree $|H|$, and set $Z'=q(Z)_{\mathrm{red}}$. The full inverse image of $Z'$ is $Z$: set-theoretically it is the union of the translates $Z+h$, all equal to $Z$. The isogeny is étale, and the inverse image of a reduced complex subvariety under an étale map is reduced. Thus this is also the scheme-theoretic equality needed for flat pullback of fundamental cycles. Consequently
\[
 [Z]=q^*[Z'],\qquad
 \int_{A_0}[Z]^2=|H|\int_{A_0/H}[Z']^2.
\tag{B22a.5}
\]
The rightmost self-intersection is a positive integer by (B22a.4). It is even: integral cohomology of an abelian variety is an exterior algebra on its degree-one lattice; a positive even-degree class has zero squares on individual exterior monomials, while its distinct cross terms occur in pairs. This is the general even-square argument already checked in B18. Hence the quotient in (B22a.5) belongs to $2\mathbf Z_{>0}$, proving $|H|\le d_\Delta/2$.

Choose the invariant Kähler form $\omega_0$ representing $c_1(L_0)$ and its flat metric. The total metric volume is
\[
 \operatorname{Vol}(A_0)=\int_{A_0}\frac{\omega_0^{2n}}{(2n)!}=V_0.
\]
Let $\alpha$ be the invariant harmonic representative of $[Z]$, and write $\alpha_+=(\alpha+*\alpha)/2$ and $\alpha_-=(\alpha-*\alpha)/2$. On real middle-degree forms in real dimension $4n$, the Hodge star is an isometric involution. If $v$ is a unit decomposable real middle-degree covector, then $\langle v,*v\rangle=0$, because $v\wedge v=0$. Hence its self-dual projection has norm $1/\sqrt2$. For every self-dual form $\eta$ this proves the pointwise estimate
\[
 \operatorname{comass}(\eta)\le |\eta|/\sqrt2.
\]
All harmonic forms for this flat torus metric are invariant, so the pointwise norm of $\alpha_+$ is $\|\alpha_+\|_{L^2}/\sqrt{V_0}$. Poincaré duality, self-duality, orthogonality of the two star eigenspaces, and Wirtinger's formula give
\[
 \begin{aligned}
 \|\alpha_+\|_{L^2}^2
 &=\int_{A_0}\alpha\wedge\alpha_+
 =\int_Z\alpha_+\\
 &\le\operatorname{comass}(\alpha_+)\operatorname{Vol}(Z)
 \le\frac{\|\alpha_+\|_{L^2}}{\sqrt{2V_0}}\frac{D}{n!}.
 \end{aligned}
\tag{B22a.6}
\]
For singular $Z$, the integral is over its smooth locus, or equivalently its integration current; the singular locus has zero volume and Wirtinger's formula still gives $D/n!$. The self-dual part is nonzero because the self-intersection is positive. Cancelling its norm yields
\[
 \int_{A_0}[Z]^2
 =\|\alpha_+\|_{L^2}^2-\|\alpha_-\|_{L^2}^2
 \le\|\alpha_+\|_{L^2}^2
 \le\frac{D^2}{2(n!)^2V_0}.
\]
Together with the preceding factor two this proves (B22a.1).

Finally, the exact generic degree $\delta_h$ of the reference isogeny on $Z$ is no larger than $|H|$. Substitute (B22a.1) into the already proved inequality (B22.7). This gives (B22a.2), and taking a square root gives (B22a.3). QED.

### Improved integer constant for the bounded-family and ideal-content results

For a positive integer source-degree bound $D_0$, one may now use the explicit positive integer
\[
 S_2(D_0)=\max\left\{1,
 \left\lfloor\frac{D_0^2}{4(n!)^2V_0}\right\rfloor\right\}
\tag{B22a.7}
\]
in B21 and in B23.17--B23.18. The maximum with one covers the empty small-degree family and ensures that $\operatorname{lcm}(1,\ldots,S_2(D_0))$ is defined in the same convention. If there is any such source subvariety, (B22a.1) itself ensures that the displayed real upper bound is at least one. The proof of B23 uses only an integer upper bound on every generic mapping multiplicity, so its exact divisibility and fixed-order comparison remain valid with this improved choice.

### Exact source locators and check scope for B22a

- Olivier Debarre, *On the geometry of abelian varieties*, author-hosted lecture notes, <https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/Taiwan.pdf>, Chapter 1: Lemmas 1.1--1.2 p.8; Definition 2.1 and Examples 2.2(2) p.8; Theorem 2.3, Lemma 2.4, and Corollary 2.5(a) pp.9--10. The exact statements and all the adjoining short proofs were read. All varieties in this chapter are irreducible, reduced, and complex; no smoothness assumption is added to Corollary 2.5.
- The same simple-ambient nondegeneracy assertion appears in Debarre, *Fulton--Hansen and Barth--Lefschetz theorems for subvarieties of abelian varieties*, J. reine angew. Math. 467 (1995), section 1, Examples (1), pp.188--189; original author-hosted scan <https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/30.pdf>.
- A direct current statement is Olivier Debarre and Ben Moonen, *Bézout's theorem for abelian varieties*, Theorem 1.1 p.1, <https://www.math.ru.nl/~bmoonen/Papers/BezoutAV.pdf>; section 2.1 p.3 reviews the characteristic-zero argument. These statements and that complete short review were read. The stronger positive-characteristic and semismallness results are unnecessary here and are not independently audited.
- The middle-class estimate uses the invariant-metric/comass argument of B7, sharpened by the explicit self-dual projection calculation above. The full proof was checked, including singular-boundary removal, reduced generic fibres, the stabilizer quotient, even self-intersection, the extra factor two in the self-dual comass bound, and the improved integer constant. It supplies no assertion for a merely finite-stabilizer subvariety of a nonsimple ambient variety without the stated geometric nondegeneracy input.

# Mathematical checks for cotes 47, 54 and 44

**Audit date: 19 November 2026.** Claim numbers in this file abbreviate `CL-SA19-`. The diplomatic transcription remains unchanged. A proof supplied here is this run’s reconstruction unless explicitly identified as an argument present on the manuscript page. The executable checks are in `code/computations.py`; exact rational and symbolic output is in `outputs/computations.json` and `outputs/computations.txt`. Finite examples do not prove the unrestricted geometric statements.

## 1. Fourier kernels, inversion and the two products

Let $A/S$ be an abelian scheme of relative dimension $g$, let $B=A^\vee$, and let $P$ be the Poincaré bundle rigidified on both zero sections. For a perfect complex $F$, put

\[
\Phi_A(F)=R p_{B*}(p_A^*F\otimes^L P), \qquad
F*G=Rm_*(F\boxtimes^L G).
\]

The fibrewise degree-zero and rigidification assumptions on the manuscript’s more general $L$ identify it with a pullback of $P$ by a classifying map $X\to B$. They are essential to the displayed multiplicative-kernel identity. On $A\times A\times B$, that identity reads

\[
(m\times1)^*P\simeq p_{13}^*P\otimes p_{23}^*P.
\]

Projection formula and derived flat base change therefore identify the transform of $F*G$ with the pushforward of $F\boxtimes G\otimes p_{13}^*P\otimes p_{23}^*P$. Relative Künneth identifies the latter with $\Phi_A(F)\otimes^L\Phi_A(G)$. This is the argument actually written on cote47/4 through “cqfd”; the earlier note understates it. The margin on cote47/3 supplies only a binary kernel isomorphism for three more general kernels. Coherent associativity and units for a monoidal functor require additional compatibility; they are not manufactured from this binary datum (claims 401–402).

Proper smooth projections preserve the perfect complexes and satisfy the necessary derived base changes (Stacks Project, Tag 0DJT). Laumon’s relative formulation assumes a locally noetherian base. Descent of a finite diagram of perfect complexes and finitely presented abelian schemes gives the general-base perfect-complex extension used here; this extension is our argument, rather than a quotation of a hypothesis-free theorem from Laumon. For arbitrary unbounded quasi-coherent categories, the appropriate support, Tor-amplitude and projection-formula hypotheses must still be imposed (Laumon, 1996, §1; Stacks Project, Tag 0FYP).

The verified inversion formula is

\[
\Phi_B\Phi_A(F)\simeq(-1_A)^*F\otimes\pi_A^*\tau_A[-g],
\qquad \tau_A=\det(\operatorname{Lie}A).
\]

It is represented by the anti-diagonal kernel. Thus the later correction of the source’s initial identity to inversion is mathematically necessary. The retained earlier identity target does not become a second theorem. On $K_0$, the formula becomes

\[
\Phi_B^K\Phi_A^K(x)=(-1)^g[\pi_A^*\tau_A](-1_A)^*x.
\]

The line factor is not removed by knowing its rank is one. It disappears after trivializing it, as over a field. Laumon’s canonical identification of the determinant lines of $A$ and $B$ identifies two lines; it does not trivialize either (claims 403–405; Mukai, 1981, Theorem 2.2; Laumon, 1996, Lemma 1.1.3 and Theorem 1.2.4).

## 2. The missing unit-fibre check

The kernel theorem is

\[
Rq_*P\simeq e_*\tau[-g]
\]

on $B^\vee$, where $q:B\times B^\vee\to B^\vee$. Mumford’s vanishing of all cohomology of a nontrivial degree-zero line bundle shows vanishing off the zero section. That support calculation alone neither determines the infinitesimal support nor identifies the whole derived object. The manuscript constructs a comparison with the claimed zero-section complex and explicitly leaves its compatibility at the unit fibre unfinished (claims 406–408; Mumford, 1970, §8(vii), p. 76; Laumon, 1996, Lemma 1.2.5).

Write $T=e^*T_{B^\vee/S}$, of rank $g$. The zero section is a regular immersion with conormal bundle $T^\vee$. The Koszul resolution gives

\[
\mathcal H^{-j}(Le^*e_*\mathcal O_S)=\Lambda^jT^\vee.
\]

After tensoring by $\det T$ and shifting by $[-g]$, the group in cohomological degree $i$ is

\[
\Lambda^{g-i}T^\vee\otimes\det T\simeq\Lambda^iT,
\qquad 0\leq i\leq g.
\]

The isomorphism is the canonical contraction pairing of exterior powers. The program checks the binomial dimensions for $0\leq g\leq8$; that check is only a consistency test. A proof that the specific comparison map is an isomorphism must show that its induced maps equal the canonical identifications. Only then can one use perfect-cone fibre detection. This audit does not silently replace the unfinished map check by a dimension count (Stacks Project, Tags 0621 and0G99).

For a classifying homomorphism $\psi:C\to B^\vee$, the correct derived base-change expression is

\[
R\operatorname{pr}_{C*}N\simeq L\psi^*(e_*\tau[-g]).
\]

The missing $e_*$ in one manuscript line is a substantive typing alarm. If $\psi$ is flat, the inverse image $K=\ker\psi$ is the flat pullback of the regular zero section, giving $\mathcal O_K\otimes\tau[-g]$, a perfect complex. Without flatness, higher Tor terms need not disappear (claim 409).

## 3. Sections, translations, determinant and Chern coefficients

The transform of a section sheaf is its kernel restriction: $\Phi_A(\delta_s)=P_s$. Inversion then gives $\Phi_A(P_t)=\tau\otimes\delta_{-t}[-g]$. With $T_t(y)=y+t$, convolution by $\delta_u$ evaluates a sheaf at $y-u$, so it is $T_{-u}^*$. Tensoring by $P_t$ before the transform corresponds to $T_t^*$ afterward. Consequently the convolution factor in that identity is $\delta_{-t}$, under the explicit conventions just fixed. The source’s final $\delta_t$ is flagged for scan review; it is not corrected diplomatically (claims 410–411; Mukai, 1981, (3.1)).

For perfect $F$ over a field, the rank of the virtual transformed complex is the Euler characteristic of $F\otimes P_b$, which is constant in $b$ and equals $\chi(F)$. Applying inversion gives

\[
\operatorname{rank}\Phi(F)=\chi(F), \qquad
\chi(\Phi(F))=(-1)^g\operatorname{rank}F.
\]

These are virtual invariants, not assertions about the rank of each cohomology sheaf (claim 412).

For an ample line bundle $L$ on an abelian variety over an algebraically closed field, put $r=\chi(L)>0$ and $E=\Phi(L)$. Mukai’s pullback formula is

\[
\phi_L^*E\simeq H^0(A, L)\otimes L^{-1}.
\]

Here $\phi_L:A\to B$ is finite flat. Pullback is injective on rational Chow groups because pushforward after pullback is multiplication by its positive degree. Taking determinants gives $\phi_L^*c_1(E)=-r c_1(L)$. If $D'=-c_1(E)$, then

\[
\operatorname{ch}(E)=r\exp(-D'/r), \qquad
c_t(E)=(1-D't/r)^r.
\]

This proves the precise ample-field form of the manuscript’s heuristic. It is not the construction of a fractional line bundle. Mukai’s nondegenerate nonample version has an index and a cohomological shift; a family version also requires the relative base factors. The signed determinant/adjugate relation follows from the same pullback identity after specifying the source’s tilde identifications. We do not infer an arbitrary-base integral Picard-functor formula from this field calculation (claims 413–414; Mukai, 1981, Proposition 3.11; Beauville, 1983).

Expanding the generating series gives

\[
c_k(E)=\frac{(-1)^k(r-1)(r-2)\cdots(r-k+1)}{k!\, r^{k-1}}(D')^k.
\]

Equivalently, if the falling factorial begins with $r$, its denominator is $k!r^k$. The transcription’s expanded formulas have one fewer factor of $r$ in the denominator and therefore equal $r c_k(E)$. The generating series itself is correct. The program checks the general symbolic falling-factorial identity for $k=1, \ldots, 6$, with the algebraic derivation above proving it for every $k$ (claim 415).

The geometric counterexample meets all ample-field hypotheses. Take $A=E_1\times E_2$ over $\mathbb C$, with $L$ the external product of line bundles of degrees1 and2. On the dual product write $\theta_1^2=\theta_2^2=0$ and $\int\theta_1\theta_2=1$. Then

\[
\operatorname{ch}(E)=(1-\theta_1)(2-\theta_2)
=2-2\theta_1-\theta_2+\theta_1\theta_2.
\]

Thus $D'=2\theta_1+\theta_2$, $(D')^2=4\theta_1\theta_2$, and

\[
c_2(E)=\frac{c_1(E)^2}{2}-\operatorname{ch}_2(E)
=\theta_1\theta_2.
\]

Its degree is1, whereas the literal expanded coefficient gives2. The proposed counterexample in the earlier notes is thereby independently checked, not merely repeated.

The final integrality expression on the page has coefficient

\[
\frac{(r-1)\cdots(r-k+1)}{k!r^{k-2}}(D')^k=(-1)^k r c_k(E).
\]

It therefore still has an integral algebraic-cycle lift in this restricted setting. This is weaker than a torsion-sensitive integral equality or an integral Fourier operation on the whole Chow lattice (claims 416–417). Beckmann and de Gaay Fortman(2023, Theorem 3.8) and Hasan etal.(2025, §§3–5) address those stronger questions with explicitly different hypotheses and coefficient rings.

## 4. Todd factors, the converse product and duality

Let $T_A=\operatorname{Td}(\operatorname{Lie}A)$, and similarly $T_B$, in a rational intersection theory where the stated GRR formulas apply. Addition on $A$ has relative tangent pulled back from $\operatorname{Lie}A$; projection from $A\times B$ to $B$ has the same relative tangent. Hence

\[
\operatorname{ch}(x*y)=(\operatorname{ch}x*\operatorname{ch}y)T_A,
\qquad
\operatorname{ch}\Phi_A(x)=\Psi_A(\operatorname{ch}x)T_A.
\]

Applying the first derived product identity yields the common invertible factor $T_A^2$ on both sides, and therefore

\[
\Psi_A(a*b)=\Psi_A(a)\Psi_A(b).
\]

There is no parity sign in this direction. Kleiman’s printed Lemma 2A12 states precisely this identity. His adjacent Remark2A13 does not state the converse product identity. Thus the manuscript’s allegation of a missing sign in Kleiman is not verified by those passages (claims 418–422; Kleiman, 1968, pp. 377–378).

The reverse derived product identity carries $\omega_A[g]$, so passage through GRR retains both source and target Todd factors:

\[
\Psi_A(ab)=(-1)^g(\Psi_A(a)*_B\Psi_A(b))T_A T_B\operatorname{ch}(\omega_A).
\]

Since $\omega_A=\det(\operatorname{Lie}A)^\vee$, the one-root identity

\[
\frac{x}{1-e^{-x}}e^{-x}=\frac{-x}{1-e^x}
\]

gives $T_A\operatorname{ch}(\omega_A)=\operatorname{Td}((\operatorname{Lie}A)^\vee)$. The Hodge exact sequence then identifies the entire extra factor with $\operatorname{Td}(H^1_{\mathrm{dR}}(A/S))$. The program verifies the exact rational-function identity and its series expansion. It does not prove that the resulting characteristic class vanishes. That last statement is Moonen’s Corollary 2.7(1), for an abelian scheme over a connected smooth finite-type scheme over a Dedekind ring. The separable-polarization condition belongs to a stronger conclusion about all Chern classes, not to his Todd-class assertion (Moonen, 2026).

Derived duality has another convention-sensitive factor. For the ordinary dual $F^\vee=R\mathcal Hom(F, \mathcal O_A)$, relative duality gives

\[
\Phi_P(F)^\vee\simeq\Phi_{P^\vee}(F^\vee\otimes\omega_A[g])
\simeq(-1_B)^*\Phi_P(F^\vee\otimes\omega_A[g]).
\]

The same-kernel expression on the page is valid if its undefined $\check F$ includes $(-1_A)^*F^\vee$. No such local definition is silently assumed (claim 423; Mukai, 1981, (3.8); Laumon, 1996, Proposition 1.3.4). Poincaré functoriality likewise exchanges pushforward by a homomorphism with pullback by its dual. An automorphism action written only as $u.F$ does not decide which variance was intended (claim 424). The bounded quasi-coherent extension follows from the same kernel identity under the usual finite cohomological-dimension/Tor conditions; it is separate from the unrestricted marginal unbounded claim (claim 425).

## 5. De Rham, universal extensions and finite $p$-torsion

For dual abelian varieties $A, B$, let $U=\operatorname{Lie}A$ and $V=\operatorname{Lie}B$. Then $H^0(A, \Omega_A^1)=U^\vee$ and $H^1(A, \mathcal O_A)=V$. Translation-invariance of differentials and the exterior algebra structure give

\[
H^p(A, \Omega_A^q)=\Lambda^p V\otimes\Lambda^q U^\vee.
\]

The corresponding group $H^q(B, \Omega_B^p)=\Lambda^q U\otimes\Lambda^pV^\vee$ is its dual by evaluation, with the ordinary graded permutation convention. The manuscript’s $\Omega_A$ on the $B$-side is a subscript alarm. This exterior argument needs no splitting of the Hodge filtration (claims 426, 428).

The universal vector extension $E(A)$ has kernel with Lie algebra $V^\vee$, so its tangent sequence is

\[
0\to V^\vee\to\operatorname{Lie}E(A)\to U\to0.
\]

It identifies with the Hodge sequence of $B$, not of $A$: $\operatorname{Lie}E(A)\simeq H^1_{\mathrm{dR}}(B)$. Invariant differentials on $E(A)$ identify with $H^1_{\mathrm{dR}}(A)$. Coleman’s convention $V(M)=\operatorname{Spec}\operatorname{Sym}M$ is contravariant; ignoring it reverses the dual. The universal extension class, rather than equality of dimensions, produces the canonical identification (claim 427; Coleman, 1998, Theorem 2.2(i), §4; Laumon, 1996, §2.2).

In characteristic $p>0$, over a perfect field, the finite group scheme $A[p]$ has rank $p^{2g}$; its Frobenius kernel has rank $p^g$. Cartier duality identifies $A[p]^D=B[p]$. Transposing the Frobenius/Verschiebung factorization, with the Frobenius twists retained, identifies the annihilator of $\ker F_A$ with $\ker F_B$. Rank alone would not prove this identification (claim 429).

Oda’s contravariant module convention is explicit. If $M$ is a Dieudonné module and $D(M)=\operatorname{Hom}_W(M, \operatorname{Frac}(W)/W)$, then

\[
(Fa)(x)=\sigma(a(Vx)), \qquad (Va)(x)=\sigma^{-1}(a(Fx)).
\]

Thus the adjunction is semilinear and exchanges $F, V$. Proposition 3.13 identifies $M(G^{(p)})=(W, \sigma)\otimes_W M(G)$; Theorem 3.19 identifies Cartier duality with this module duality. Corollary 5.11 identifies $M(A[p])$ with $H^1_{\mathrm{dR}}(A)$, and $VM=\ker F$ with $H^0(A, \Omega^1)$. This is the precise filtered finite-group answer to cote54’s question (claims 429–431; Oda, 1969, pp. 82, 86, 89, 131). Oda’s footnote dates the Harvard dissertation to June1967; publication was1969. The finite group scheme, rather than just its geometric points, is indispensable.

Height-one finite group schemes are classified by restricted Lie algebras in the cited SGA3 framework. The additive kernel of the universal extension has zero restricted $p$-operation; the extension inherits the operation from its algebraic group. This explains the height-one part of the source. It does not identify every finite $p$-group scheme from its ordinary Lie algebra, nor does it bypass Oda’s extra $F, V$ data (Gabriel, 1970, ExposéVIIB, Corollary 4.4.1).

## 6. Reused flatness sheets: exact EGA counterpart and failed amendment

The retained Proposition A on cote54/6 is the universal generic closed flattening stratum. Its exact published counterpart is EGA IV₃ Proposition 11.4.5, pp. 146–147, including freeness on a specified finite affine cover. The missing “4.1bis” is Corollary 11.4.4, pp. 145–146. The canceled generic-freeness corollary on cote54/4 is Corollary 11.4.6, p. 147 (claims 432, 434, 458).

The published Proposition 11.4.5 assumes an irreducible base, while the supplied transcription says merely nonempty. The broader existence of some nonempty open follows by descending the finite data to an affine noetherian subring. A noetherian spectrum has finitely many irreducible components, so it has a nonempty open lying in one component. The map from the original affine base to this approximating spectrum is dominant because the subring map is injective; its inverse image is therefore nonempty. Apply the published irreducible theorem there and pull it back. This extension is this run’s proof of the source’s broader formulation; no stronger published hypothesis is concealed.

Here is the algebra behind the universal ideal. Suppose $I\subset A$ is nilpotent and $M/IM$ is free. Lift a basis to obtain $F\twoheadrightarrow M$; surjectivity follows by iterating $M=\operatorname{im}F+IM$ until $I^N=0$. Its kernel $K\subset IF$. For an $A$-algebra $A'$ over which $M'=M\otimes_AA'$ is flat, reduction modulo $I'=IA'$ makes $F'/I'F'\to M'/I'M'$ an isomorphism. Flatness makes its kernel reduce to zero, and nilpotence forces that kernel to be zero. Thus $M'$ is free on the chosen lifted basis.

Let $J\subset A$ be generated by every coefficient of every element of $K\subset F$. Then $M'$ is flat if and only if all those coefficients vanish in $A'$, equivalently $JA'=0$. Conversely that condition gives $M'\simeq F'$. In a noetherian approximation $J$ is finitely generated. For finitely many affine charts, sum the ideals $J_i$, and their common condition cuts out the finite-presentation closed subscheme. The final manuscript sentence means that **all** chart conditions hold, not that each single $J_i$ equals their sum.

The same basis argument proves the nilpotent descent version. If $A\to\prod A_i$ is injective and each $M\otimes A_i$ is flat, every coefficient of $K$ maps to zero in every $A_i$; it is therefore zero. Hence $M\simeq F$. EGA IV₃ Theorem 11.4.1 gives this exact theorem, and also the flat-reduction variant for a finite family. Its proof uses a finite associated-graded filtration, read and checked in this audit.

Deleting nilpotence without adding an appropriate topological condition is false. Let

\[
A=k[t], \quad I=(t), \quad A_1=k[t, t^{-1}], \quad M=A/(t).
\]

The map $A\to A_1$ is injective, $M/IM=k$ is free over $A/I=k$, and $M\otimes_AA_1=0$ is free of rank zero. But over $R=A/I^2=k[t]/(t^2)$, the module $M\otimes_AR=k$ is not flat. The injective map $(t)\hookrightarrow R$, after tensoring with $k$, becomes the zero map $k\to k$, which is not injective. This proves the failure of the amended assertion already for $n=1$. The ring is noetherian and $M$ is finite and $I$-adically ideally separated, so the literal extra branch at the bottom of the page does not repair it (claim 433).

The published nonnilpotent statement, EGA IV₃ Proposition 11.4.7, p. 147, requires finitely many primes containing $I$ and equivalence between the topology defined by the intersection of their symbolic powers and the $I$-adic topology. Those hypotheses supply exactly the missing control; joint injectivity alone does not. The whole amended Proposition 4.1 is canceled on the reused sheet. Its counterexample is not an accusation that the retained EGA theorem is false.

## 7. Other reused mathematics: completion, reflections and walls

For a noetherian nonnegatively graded ring whose degree filtration is equivalent to an adic filtration, noetherian completion is flat and exact on finitely generated modules. For a finitely generated graded module, completion is the product of its graded pieces. Exactness can also be checked degree by degree. Faithfulness within the graded category follows because any nonzero bounded-below graded module has a nonzero homogeneous component that remains visible in the product. The source’s “TF” category is not defined locally; no larger claim is inferred (claim 455; Stacks Project, Tags 00MB and00MC).

The ungraded module $k[x]/(x-1)$ is killed by completion at $(x)$, since $x-1$ is invertible in $k[[x]]$. The program checks the inverse $-\sum_{j=0}^{n-1}x^j$ modulo $x^n$. This warns against unqualified faithful flatness but does **not** refute the qualified graded assertion: $k[x]/(x-1)$ has no standard grading compatible with this quotient.

For the canceled root draft, a finite root set spanning $P_\mathbb Q$ gives a positive definite form on $P_\mathbb Q^\vee$ by summing products of evaluations over the roots. Every permutation of the roots preserves that form. A reflection preserving the root set is therefore orthogonal for the dual form and is the unique orthogonal reflection whose negative eigenspace is its root line. This proves the rational uniqueness argument (claim 456).

It does **not** prove the next claim that the coroot lies in $P^\vee$. Take

\[
P=\mathbb Z^2, \qquad
\Delta=\{\pm e_1, \pm e_2, \pm2(e_1+e_2), \pm2(e_1-e_2)\}.
\]

The set is finite, generates $P$, and has only a root and its negative on each rational line. The reflections in $e_1, e_2$ change the corresponding coordinate sign. The reflections for $2(e_1+e_2)$ and $2(e_1-e_2)$ are respectively

\[
\begin{pmatrix}0&-1\\-1&0\end{pmatrix}, \qquad
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

All preserve the displayed set and the lattice, and all send their root to its negative. Yet for $\alpha=2(e_1+e_2)$, the formula $s_\alpha(x)=x-\gamma_\alpha(x)\alpha$ gives $\gamma_\alpha=(1/2, 1/2)$, so $\gamma_\alpha(e_1)=1/2\notin\mathbb Z$. The claimed primitivity of every root also fails. The program verifies all eight roots, all matrices, involution, determinant, root-set permutation and reduced-line conditions (claim 464).

A sufficient repair is to **assume** each root primitive in $P$. Then

\[
(1-s_\alpha)P\subset P\cap\mathbb Q\alpha=\mathbb Z\alpha,
\]

which proves integral coroot values (claim 465). The manuscript presents primitivity as a consequence of its preceding axioms; this repair is not a transcription emendation. SGA3 ExposéXXI Definition 1.1.1 includes integral coroot data from the outset.

The second formulation on the sheet uses two lattices integrally paired with **rationally** perfect duality. It does not require a perfect integral pairing. Expanding

\[
\langle u-\langle u, \alpha\rangle\alpha', \ x-\langle\alpha', x\rangle\alpha\rangle
\]

and using $\langle\alpha', \alpha\rangle=2$ cancels the two negative cross terms against the positive double term, leaving $\langle u, x\rangle$. Thus the paired reflections are contragredient (claim 457). This matches the root/coroot lattice calculation in SGA3, while a full character/cocharacter root datum has stronger integral duality.

For a locally finite affine-hyperplane arrangement, a chamber is an open convex component of the complement. A compact segment meets only finitely many hyperplanes. If a point lies outside the intersection of the chamber’s wall half-spaces, follow a segment from an interior point to it: the first separating wall gives the contradiction. At a relative interior point of a wall, a sufficiently small ball avoids every other hyperplane, so precisely two local half-balls, and hence two chambers, meet there. A point of a chosen hyperplane avoiding the others exists because local finiteness leaves only finitely many proper subspaces in a small ball. The fragment’s final induction is cut off, so the complete proof just given is ours; the original Bourbaki provenance is not assigned (claim 435).

## 8. Incidence, full-kernel descent, factor two and positivity

Let $X$ be smooth projective of dimension $2m-1$, $T$ smooth connected and pointed by $a$, and $z\in CH^m(T\times X)$ with $z(a)=0$. On $T\times T\times X$, form

\[
D=r_*(p^*z\cdot q^*z).
\]

Its codimension is $m+m-(2m-1)=1$, so it is a divisor correspondence. Exchanging the two copies of $T$ exchanges the two cycle factors, whose product in Chow theory is commutative. Thus $D$ is symmetric. The zero normalization makes it a pointed correspondence and hence gives a homomorphism between the appropriate Albanese/Picard varieties. These formal facts do not prove positivity (claim 449).

The literal integral descent through the **full** kernel fails even in the elliptic case. Take a complex elliptic curve $E$ with $\operatorname{End}(E)=\mathbb Z$, set $X=T=E$, $m=1$, and $z=2c_1(P)$, with the normalized Poincaré bundle identified through a principal polarization. The restriction at zero is zero. In the exterior algebra on $a_i, b_i$, put $P_{ij}=a_i b_j-b_i a_j$. Direct wedge multiplication and integration on the third factor give

\[
r_*(P_{13}P_{23})=-P_{12}.
\]

The program verifies this exact sign with the ordered basis $a_1, b_1, a_2, b_2, a_3, b_3$. Hence $D$ corresponds to $-4\operatorname{id}_E$; its full kernel is $E[4]$. Identify the quotient by that kernel with $E$ via $q=[4]$. Any integral homomorphism $\mu:E\to E^\vee$ pulls back as $q^\vee\mu q=16\mu$. Equality with $-4\operatorname{id}$ would require $\mu=-\tfrac14\operatorname{id}$, which is not integral. Thus no integral divisor correspondence on the quotient pulls back to $D$ (claim 450).

This example extends to every $m\geq1$: take $X=E\times\mathbb P^{2m-2}$, let $h$ be its hyperplane class, and put $z=2c_1(P)h^{m-1}$. Pushing the product integrates $h^{2m-2}$ to1 and gives the same correspondence. All dimension, smoothness, projectivity, algebraic-variation and normalization hypotheses remain valid. This refutes only full-kernel **integral** descent; it does not decide a source convention that may have intended an abelian radical, rational coefficients or a normalization.

Over $\mathbb C$, or over a perfect field with the reduced neutral abelian subvariety of the kernel, quotient by the abelian radical gives an integral symmetric homomorphism with finite kernel: symmetry makes the original map land in the annihilator of that radical, and the universal property of the abelian quotient gives the factorization. Further finite quotients admit the factorization in the rational isogeny category, where denominators are allowed. In the example, the required rational map is exactly $-1/4$. “Connected kernel” here means the connected **abelian subvariety**; a finite connected nonreduced group scheme in characteristic $p$ must not be substituted without another descent check (claim 459).

The factor-two remark has a separate elementary proof. For a symmetric $f:A\to A^\vee$, the Poincaré line bundle on $A\times A^\vee$ has off-diagonal homomorphism matrix

\[
\lambda_P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Pulling back along the graph $(1, f)$ gives $\lambda_{(1, f)^*P}=f+f^\vee=2f$. This constructs the Néron–Severi class promised modulo factor2. It does not prove ampleness (claim 461; van der Geer and Moonen, undated, ChapterVII §7.18 and Exercise 7.5). Indeed for an ample symmetric $L$ on a positive-dimensional abelian variety, $L^{-1}$ has symmetric isogeny $-\lambda_L$ but negative degree on every curve. This refutes the shortcut “symmetric isogeny implies positive”; it is not by itself a counterexample to the specifically signed primitive incidence conjecture.

If $j:Y\hookrightarrow X$ is smooth projective of codimension $m-1$, the normalized Poincaré divisor on $\operatorname{Pic}^0(Y)\times Y$ pushes forward to a codimension-$m$ family on $\operatorname{Pic}^0(Y)\times X$, zero at the origin. This verifies the test-family construction in the letter. It does not prove that those families suffice for the entire positivity problem (claim 463). The source explicitly retains unspecified unproved assertions and a primitive-decomposition warning; conditional modern incidence comparisons preserve those issues (claim 462; Peters, 2026, Criterion7.3 and Corollaries 7.8–7.9).

## 9. Tate lattices, heights and equivalence relations

If the asserted subquotient statement is literally a surjection of $\mathbb Z_\ell$-modules $S\twoheadrightarrow T_\ell J$, with $S\subset H$, then it already yields an abstract embedding $T_\ell J\hookrightarrow H$. Choose a basis of the finite free module $T_\ell J$, lift its basis elements to $S$, and extend $\mathbb Z_\ell$-linearly. This is a section, so injective. The assertion is nontrivial only if additional naturality, correspondence, polarization or Galois compatibility is required. The letter does not specify which of these it intends (claim 446).

The modern geometric realization must retain its exclusions: Achter, Casalaina-Martin and Vial(2023, Proposition 8.2) treat $i=1, 2, \dim X$, with $\ell$ prime to the characteristic and to a miniversal-cycle multiplicity, and target cohomology modulo torsion. They obtain a correspondence-defined Galois-equivariant map. It does not establish an unrestricted all-codimension integral realization. Likewise, an incidence representative, a universal regular representative and the algebraic Abel–Jacobi image have different universal properties. Saito’s all-codimension existence and dimension bound concern the first of these (claims 440–447).

For the height/intersection programme, $i+j=n$ is the intersection-degree condition on $X$; complementary incidence duality instead has $i+j=n+1$. In the balanced pencil case $i=j=n/2=m$, $n$ is even and the generic fibre has dimension $2m-1$. Away from that case, one of $2i, 2j$ is less than $n$. If restriction to a smooth ample hyperplane is homologically trivial, weak Lefschetz injectivity in that lower degree forces the original lower-degree class to vanish; therefore its intersection with the complementary class is zero. This proves the intersection-side vanishing only. Height-side vanishing also needs the exact realization and fixed-part compatibility (claims 451–453).

For divisors on a regular fibred surface, canonical geometric height is the negative intersection of vertically orthogonal corrected lifts. Over a finite field the usual arithmetic normalization includes $\log q$. Those correction and normalization data are absent from the broad source formula. Ulmer’s author-posted errata restricts some general-ground-field claims, so this audit uses only the finite or algebraically closed settings supported by that correction. Künnemann’s higher-cycle height theorem is for an abelian variety over a number field; it is not the manuscript’s unrestricted pencil theorem (Ulmer, 2014, §4.3, with errata; Künnemann, 2001, Theorem 1.6 and Corollary 1.7).

Finally, if the undefined $\tau$ means algebraic equivalence after multiplication by a nonzero integer, the numerical=$\tau$ statement is valid for divisors by Matsusaka’s theorem as recorded in Grothendieck’s FGA VI §4, p. 242. It fails for arbitrary codimension: Clemens’s very general smooth complex quintic threefold has non-torsion codimension-two classes homologically trivial modulo algebraic equivalence. Homological triviality implies numerical triviality by cycle-class compatibility with intersection, while non-torsion in the Griffiths quotient rules out every nonzero algebraically trivial multiple. Thus all smoothness/projectivity hypotheses hold, but the conclusion fails. The counterexample is conditional on the symbol’s meaning and cannot decide the ink (claims 454, 460; Clemens, 1983, Theorem 0.2 and(0.1)).

## Scope of the computational certificates

The executable output proves the asserted rational polynomial, exterior-algebra and finite-matrix identities exactly. The geometric examples additionally require the hypotheses explained above. Bibliographic theorem verification consists of reading the exact statements and matching hypotheses; it is not labelled an independent proof of Mukai inversion, Oda’s theorem, Saito’s representability theorem or Clemens’s construction. Their cited primary results remain the mathematical inputs.

# Independent checks and reconstructions: cotes 22, 23, 26

Run SA23-20261119, owner ega; GPT-6 Astra Pro, effort not independently exposed. These arguments are this run's checks. They do not replace the supplied transcriptions. The finite symbolic certificates are in `computations.py` and `computation_outputs.json`; the arguments below explain the unrestricted mathematical assertions which those finite calculations alone cannot prove.

## 1. Adic and discrete formal smoothness (claims 020–023)

Let $A=K[[t_1,\ldots,t_n]]$, $n>0$. Its maximal-ideal formal smoothness is different from formal smoothness with the discrete topology. For the latter, projectivity of $\Omega_{A/k}$ is necessary (Stacks, tag 00TH). A projective module over a local ring is free, with no finite-generation assumption (tag 0593).

If $K=k$ has characteristic zero, then $\Omega_{A/K}\otimes_A K\simeq (t_1,\ldots,t_n)/(t_1,\ldots,t_n)^2$, of dimension $n$. If $\Omega_{A/K}$ were projective it would therefore be free of rank $n$. But its localization at the fraction field has dimension at least $n+1$: $t_1,\ldots,t_n,\exp(t_1)$ are algebraically independent over $K$. To check the extra transcendence, a polynomial relation in $t,\exp(t)$ would give a linear relation between distinct exponentials $\exp(jt)$ with coefficients in (K(t)). Choose a relation with the fewest nonzero terms, normalize one coefficient to 1, differentiate, and subtract the logarithmic derivative of that exponential times the original relation. Minimality would force a rational function $r$ to satisfy $r'/r=c\ne0$, impossible at infinity. Hence the differential module is not projective, and $K[[t_1,\ldots,t_n]]/K$ is not discretely formally smooth. The manuscript's examples $K=\mathbf Q,\mathbf C$ are thereby settled negatively. No finiteness of the original differential module was assumed.

For the manuscript's nonsplitting assertion, suppose $\dim_K\Omega_{K/k}=\infty$ and suppose the coefficient map $\Omega_{K/k}\otimes_K A\to\Omega_{A/k}$ had an $A$-linear retraction. Composing with the universal derivation gives a derivation $D:A\to\Omega_{K/k}\otimes_K A$ restricting to $d_{K/k}$. Each of the finitely many $D(t_i)$ has finite support. Quotient $\Omega_{K/k}$ by a finite-dimensional subspace containing all their coefficient directions. The resulting target still has infinite dimension and the induced derivation kills all the $t_i$. Choose $a_j\in K$ whose differential images are linearly independent and extend them to a basis of that quotient. Each coordinate derivation is continuous for the $t_1$-adic topology because it kills $t_1$. Applied to $f=\sum_{j\ge0}a_jt_1^j$, its $j$-th selected coordinate is $t_1^j$. Thus (D(f)) has infinitely many nonzero coordinates, contrary to the direct-sum target. This completes the argument left unfinished on cote22/025.

There is also a stronger, separately attributed earlier-run idea: $\Omega_{A/k}$ itself is not projective when $\Omega_{K/k}$ has infinite dimension. Here is a proof avoiding an infinite Nakayama argument. Were it free, let $e_s$ be a basis. Reduction modulo the maximal ideal gives $\Omega_{K/k}\oplus K^n$. Inductively choose $a_j$ and a coordinate $s_j$ outside the finite supports of $dt_1, da_0,\ldots,da_{j-1}$, such that the $s_j$-coordinate of $da_j$ is a unit. This is possible because the residue images of exact coefficient differentials span an infinite-dimensional space. For $f=\sum a_jt_1^j$, differentiating its finite truncation plus the remainder shows that the $s_j$-coordinate of $df$, modulo $t_1^{j+1}$, is $t_1^j$ times that unit. It is nonzero for every $j$, a contradiction to the finite support of an element of a free module. This strengthening is not silently attributed to the manuscript proposition.

## 2. A differential kernel which does not descend (claim 026)

In characteristic 2 take $K=\mathbf F_2(x,b,c)$, $y=b^2x+c^2$, and $k=\mathbf F_2(x,y)$. These are fields, and $x,y$ are algebraically independent. The map on absolute differentials sends $dx\mapsto dx$ and $dy\mapsto b^2dx$; its kernel is the line $K(dy-b^2dx)$. Since $b^2\notin k$, this line is not obtained by extending a line over $k$.

To check the extra hypothesis $k\cap K^2=k^2$, put $L=\mathbf F_2(x,b^2,c^2)=k(b^2)$. On $L/K^2$, the derivation with $Dx=1$, $D(b^2)=D(c^2)=0$ satisfies $Dy=b^2$. If $r\in k\cap K^2$, then $0=Dr=r_x+b^2r_y$. Because $b^2$ is transcendental over $k$, both partial derivatives vanish. Therefore $r\in\mathbf F_2(x^2,y^2)=k^2$. The finite variant replaces $b^2$ by $a\in\mathbf F_4\setminus\mathbf F_2$, takes $K=\mathbf F_4(x,c)$, $y=ax+c^2$, $k=\mathbf F_2(x,y)$, and has degree 4. Linear independence of (1,a) over the rational function field $k$ gives the same intersection calculation.

The printed EGA IV, 0.22.5.10$i$, p.204, was inspected independently. It really prints $k=k_0(X,Y)$ and $K=k(X^{1/p}+ZY^{1/p})$, with $Z$ independent, without adjoining $Z$. In that literal field, $T=X^{1/p}+ZY^{1/p}$ is transcendental over $k$; otherwise $Z$ would be algebraic over $k(X^{1/p},Y^{1/p})$. Thus $K=k(T)$, whose coefficient differential map is injective. Adjoining $Z$ as well repairs this example and gives $dX+Z^p dY=0$. The original printed error and the candidate repair are recorded separately. This is an external printed-source check, not an ink decision about the manuscript.

## 3. Elementary literal failures (claims 017, 030, 032–037)

For cote22 Theorem4.6$ii$, let $A=B=\mathbf Q[e]/(e^2)$, $C=\mathbf Q$, and $u$ the quotient. With $I=(e)$, $u_0$ is an isomorphism; the identity $B/A$ satisfies the smoothness and projectivity conditions printed for $B$. All the nilpotent topologies are complete and discrete. Nevertheless $u$ has nonzero kernel. The candidate comparison theorem must constrain $C$, not repeat the conditions on $B$.

The discriminant of degree $d$ forms in $r+1$ variables has coefficient degree $(r+1)(d-1)^r$, not the literal $(d-1)(r+1)$. A plane cubic distinguishes 12 from 6; binary forms and quadrics do not detect the mistake. Buse–Jouanolou, Proposition4.7, gives the first exponent, and Proposition4.13 gives the coordinate-change character $d(d-1)^r$. In the elliptic cubic calculation, the independent adjunction computation gives $M=L^6$ because $\det(E)=L^5$ and $L^{-1}=L^5M^{-1}$.

The logarithm product law must read $\log(gg')=\log g+\log g'$ for commuting elements. In $\mathbf Q[t]/t^2$, $g=g'=1+t$ gives (2t) on the left and 0 for the printed product of logarithms. In the Hopf algebra $\mathbf Q[x]$, with $x$ primitive, and coefficient ring $\Lambda=\mathbf Q[t]/t^3$, $\exp(tx)-1=tx+t^2x^2/2$ is not primitive: its reduced coproduct is $t^2x\otimes x$. Exponential maps primitives to group-like elements; it does not land in $1+\mathrm{Prim}$ in general.

The shortened Cartier hypotheses need a connectedness condition. Let $H=\mathbf R^{C_3}$, with coproduct induced by addition in the cyclic group. It is finite-dimensional and cocommutative. Its primitive elements are additive homomorphisms $C_3\to(\mathbf R,+)$, hence zero. Its real group-like elements are homomorphisms $C_3\to\mathbf R^*$, hence only 1. Yet $H$ is three-dimensional and not (U(0)). Cartier's actual HA3, inspected in Exp.2, requires an exhaustive connected filtration $H_0=\mathbf R$ compatible with coproduct; it excludes this example. Exp.3 Proposition8 proves injectivity of $U(\mathrm{Prim}H)\to H$, not the unrestricted surjectivity alleged by a shortened reading.

Likewise a finite augmented algebra with locally free associated graded need not be infinitesimal: $\Lambda=k\times k$, augmented by the first projection, has a nonzero idempotent augmentation ideal $I=I^2$. The trivial positive associated-graded pieces do not imply $I$ nilpotent.

## 4. Regular sequences and nonnoetherian separation (claims 049–053)

Let $R_0=k[x,y]_{(x,y)}$, let $M=k(x)$ be an $R_0$-module with $y$ acting as zero, and form the local square-zero idealization $R=R_0\ltimes M$. Multiplication by $x$ is injective on both summands. Since $xM=M$, $R/xR\simeq k[y]_{(y)}$, where $y$ is a nonzerodivisor. Thus ((x,y)) is an $R$-regular sequence. But $y$ kills $M\ne0$, so ((y,x)) is not regular. Koszul acyclicity is invariant under permutation, which explains why the nonnoetherian geometric definition must use it. SGA6 VII, printed pp.416–421, explicitly makes this replacement of EGA IV16.9.2.

The distinction between $A$- and $B$-subquotients is substantial. For a DVR $A$ with parameter $\pi$, $B=A[[T]]$ contains $A[T]\simeq A^{(\mathbf N)}$ as an $A$-submodule. It has an $A$-linear quotient $A[1/\pi]$, which is nonzero and satisfies $\pi M=M$. Hence arbitrary $A$-subquotients of a separated $B$ are not separated. Such a quotient is not being asserted to be a finite $B$-module. The graded analogue is $B_0[T]/(T-1)$, where the $T$-adic ideal becomes the unit ideal.

A finite-presentation algebra can have a non-finitely generated kernel from the base. Take $A=k[t]\ltimes\bigoplus_{n\ge1}k[t]/(t^n)$, and $B=A_t\simeq k[t,t^{-1}]$. The algebra $B=A[z]/(tz-1)$ is finitely presented. Its kernel is the entire square-zero summand, not finitely generated. This is a precise negative answer to the kernel question raised in the Deligne material; no noetherian hypothesis is imposed in this example.

In printed EGA IV, 0.19.3.12, pp.85–86, the sets of algebra-homomorphism lifts are called closed linear varieties. Deligne's objection is valid: multiplicativity imposes nonlinear equations. One cannot apply linear compactness to arbitrary polynomial solution sets. For example, over an infinite field, every finite subsystem of $(X-u)Y_u=1$, indexed by $u\in k$, has a solution, but the whole system has none. This refutes the proof step, not by itself the theorem under all its stated hypotheses.

## 5. Differential and inseparable-curve checks (claims 042–043)

For odd characteristic $p$ and $a\notin k^p$, the curve $y^2=x^p-a$ is regular over $k$: away from $y=0$ it is smooth; the remaining prime is generated by $y$, since $x^p-a=y^2$, and its one-dimensional local ring is a DVR. After adjoining $a^{1/p}$, the origin of $y^2=z^p$ has embedding dimension 2 and dimension 1, hence is singular. This checks example$ii$, without turning the overwritten example$i$ into a single settled formula.

Flatness alone does not make the usual equalizer of $B\rightrightarrows B\otimes_A B$ equal to $A$: take $\mathbf Z\to\mathbf Q$. Faithful flatness supplies the correct descent statement. Nor does vanishing on every infinitesimal diagonal force a function to descend for an arbitrary extension: for a nontrivial finite separable field extension the diagonal ideal is idempotent, and every infinitesimal diagonal is just the diagonal. These are distinct hypothesis failures.

## 6. One-equation dimension drop and normalization (claims 071–077)

At the origin of $\operatorname{Spec}k[x,y,z]/(xy)$, dimension is 2. For $f=x$, one irreducible component is not contained in (V(f)), but the quotient by $f$ is (k[y,z]), still of dimension 2. The equality criterion therefore cannot say merely that there exists a component not contained in (V(f)); one must avoid all relevant top-dimensional components at a point where the required local dimension is attained. In the following parameters statement, elements already in $\mathfrak p$ have zero images in $A/\mathfrak p$, so they cannot be a nonempty system of parameters there. The suggested $A$ in place of $A/\mathfrak p$ remains an ink alarm.

For the normalization $A=k[t^2,t^3]_{(t^2,t^3)}\subset B=k[t]_{(t)}$, the support of $B/A$ has codimension 1. Thus defining $Z$ to be that support and simultaneously claiming every point of $Z$ has codimension greater than 1 is false. A codimension-two extension argument must first assume equality in codimension one, not manufacture it from the definition of $Z$.

The fibre-product construction with $R=T\times_{T/I}T$ has exact sequence $0\to R\to T\oplus T\to T/I\to0$. If a diagonal element $g\in I$ is a nonzerodivisor on $T$, reduction modulo $g$ introduces the term $\operatorname{Tor}_1^T(T/I,T/gT)\simeq T/I$. This is the source of the intended depth effect. The preliminary geometric choice still needs the non-Cohen–Macaulay locus on the projective input to be suitably isolated; normal and non-Cohen–Macaulay alone do not guarantee that a single hypersurface cuts the cone's bad locus down to its vertex. The source's construction is therefore not certified in its unrestricted wording.

## 7. Graded algebra counterexamples and repairs (claims 078–082)

The relation $\varphi\psi(A_+)=0$ is necessary in the split graded algebra discussion. With $A=B=C=k[t]$ and both maps the identity, it fails and the proposed description of the kernel is false. Under that compatibility and nonnegative gradings, generation modulo $A_+B$ lifts by induction on total degree. A change of graded section changes the resulting map by an operator which lowers the $C$-degree; on each total degree its deviation from the identity is nilpotent. This proves section independence of the isomorphism condition in the corrected setting, without a global finite-generation assumption.

Without compatibility, section independence fails: let $A=k[x]$, $B=k[x,y]$, $C=k[t]$, $\psi$ the inclusion and $\varphi(x)=\varphi(y)=t$. The section $t\mapsto y$ gives $A\otimes_k C\simeq B$; the section $t\mapsto x$ does not. A rank or Poincaré-series criterion must also retain the preceding surjectivity condition. For example, with $A=k[x]\to B=k[u,v]$ sending $x$ to zero, and $C=k[v]$, the expected Hilbert-series equality holds but the map $A\otimes C\to B$ does not hit $u$.

The first proposed flatness implication is false: $A=B=k[t]$, $C=k$, and $\varphi$ the augmentation satisfy the split-module condition and $B$ is flat over $A$, but $C$ is not flat over $A$. The certificate computes $\operatorname{Tor}_1^{k[t]}(k,k)=k$. The other two implications are positive under the stated split identification $B\simeq A\otimes_K C$: flatness of $C/K$ implies flatness of $B/A$, and then flatness of $A/K$ implies flatness of $B/K$ by transitivity. If $C$ is polynomial, choose lifts of its variables to obtain an algebra section; an isomorphism of the associated $A$-module map is then an algebra isomorphism $B\simeq A[T_i]$.

## Limits of these checks

The computation file does not certify the full Tor criterion of the Jouanolou offprint, the broad nonlocal Cohen-lifting problem, the incompletely specified finite-epimorphism descent statement, the exact gap alleged in Lang's proof, or the initial geometric choice in the non-Cohen–Macaulay construction. Those have explicit searched limitations in the claims and problem registers. Reused-page attribution, cancellations, and all candidate manuscript readings remain for inspection of the actual scans.

## 8. The relative pro-Tor comparison (claim 055)

Here the claim concerns pro-objects, not merely their inverse limits. Let $A\to B$ be a local map of noetherian local rings, let $N$ be finite over $A$, let $M$ be finite over $B$, and let $I\subset A$ be an ideal. The natural morphism
\[
\{\operatorname{Tor}^A_q(N,M)/I^n\}_n
\longrightarrow
\{\operatorname{Tor}^A_q(N/I^nN,M)\}_n
\]
is an isomorphism of pro-modules.

First replace $B$ by its faithfully flat completion. Tor and the displayed comparison commute with this flat base change. Choose a flat noetherian local $A$-algebra $C$ surjecting onto $\widehat B$; the complete Cohen factorization supplies one. More explicitly, complete $A$, write $\widehat A=R/J$ with $R$ a complete regular local ring, choose a formally smooth complete noetherian $R$-algebra $S$ mapping onto $\widehat B$, and put $C=S/JS$. The quotient $C$, rather than $S$ itself, is the required $\widehat A$-algebra. It is flat over $\widehat A$, hence over $A$.

Both $N_C=N\otimes_A C$ and $\widehat M$ are finite $C$-modules. Choose a free resolution $P_\bullet\to\widehat M$ with finite free terms over $C$. The complex $X_\bullet=N_C\otimes_C P_\bullet$ has finite terms. The Artin–Rees lemma says that $E\mapsto\{E/I^nE\}_n$ is exact as a functor from finite $C$-modules to pro-modules: for a submodule $E'\subset E$, the filtrations $I^nE'$ and $E'\cap I^nE$ are cofinal. Apply this exactness to the kernels, images and homology of $X_\bullet$. It gives
\[
\{H_q(X_\bullet)/I^nH_q(X_\bullet)\}_n
\simeq
\{H_q(X_\bullet/I^nX_\bullet)\}_n.
\]
Only three adjacent degrees of the resolution enter each fixed $q$, so its possibly infinite length causes no additional completion issue. Flat base change identifies the left homology with $\operatorname{Tor}^A_q(N,\widehat M)$, and the right homology with $\operatorname{Tor}^A_q(N/I^nN,\widehat M)$. This proves the comparison after completion. Faithful flatness reflects a zero transition map on the kernels and cokernels; hence it reflects their being pro-zero and descends the comparison to $B$.

This proves the relative statement used in Deligne's letter from the flat-cover and Artin–Rees ingredients. Stacks tag0911, Lemma15.28.3, explicitly proves the finite-module pro-Tor vanishing mechanism and points back to Quillen's Lemma9.9; it is not cited as literally stating the relative two-module formula. The subsequent relative depth formula uses depth with respect to the maximal ideal of $A$. Replacing it silently by $\operatorname{depth}_B M$ would change the assertion.

## 9. Published withdrawal and the differential-sign errata (claims 053, 061)

The original EGA IV1 proof of 0.19.3.12 calls the algebra-lift sets closed linear varieties. EGA IV4, Liste3 de corrections, IV no.8, printed p.347, expressly withdraws the proposition for the same reason Deligne gives: those sets need not be linear varieties. Thus the correct bibliographic fate is a published withdrawal in1967. The nonlinear compactness counterexample in §4 diagnoses the proof mechanism and does not, by itself, falsify every hypothesis of the withdrawn theorem.

The same errata list contains the exact changes proposed in the letter: no.6 removes noetherianity in0.16.1.9; no.9 inserts locality in0.19.8.3–4; no.14 removes integral closure in0.20.4.13(iv). The dimension extension also follows from the faithful finite-module determinant trick and dimension invariance under an integral extension. The differential torsion assertion follows by localizing to the separable algebraic fraction-field extension.

Nos.12–13 reverse the universal-differential convention. There is a second, edition-level issue: the original p.125 has $d=p_1-p_2$ and $dx=x\otimes1-1\otimes x$, whereas the first sentence of erratum12 tells the reader to replace $p_2-p_1$ by $p_1-p_2$. Its next sentence instead correctly reverses the displayed tensor formula, and no.13 adjusts the identity between $p_1,p_2,d$. The first old/new pair in erratum12 is therefore transposed. We record the discrepancy; we do not silently rewrite either external printed text or the manuscript.

## 10. The reused Artin passages (claim070)

Both ExposéIX and ExposéXII of SGA4 tome3 are expressly attributed to Michael Artin on their title pages. The cote23/079 constructibility paragraph has the subject of IX2.14(i), printed p.23: a finite morphism of finite presentation carries a constructible sheaf to a constructible direct image. The final proof uses limit reduction to a field, rather than repeating this draft's radicial-piece argument. This establishes the theorem and its exact necessary context without supplying missing ink to the draft.

The cancelled Corollaire6.3 on cote23/081 is identifiable with XII6.3, printed pp.100–102. The final statement explicitly assumes that cohomological functors on $D^+(C)$ vanish in negative degrees on complexes with no negative cohomology. Its part(i) extends an isomorphism through degree$n$ and monomorphism in degree$n+1$ from objects to those complexes. The proof truncates by the first nonzero cohomology object and uses induction with the five lemma. The final part(ii) assumes both complexes have nonnegative cohomology and uses an injection on $H^0$; the cancelled draft has a different formulation involving negative degrees. These are comparisons, not readings substituted for the missing symbols. The handwritten $R^1$ expressions above the typescript remain separately unidentified (claim097).

## 11. The completion fraction field in EGA III4.3.6 (claim061)

Original EGA III1, printed p.133, really states $\operatorname{Frac}(\widehat A)=\operatorname{Frac}(A)\otimes_A\widehat A$ for an analytically integral noetherian local domain. The literal equality is false. Put $A=\mathbf Q[x,y]_{(x,y)}$, so $\widehat A=\mathbf Q[[x,y]]$, and let $h(x)=\exp(x)-1$. The prime ideal $P=(y-h(x))$ of $\widehat A$ is nonzero and contracts to zero in $A$: otherwise a nonzero polynomial in $x,y$ would make $h(x)$ algebraic over $\mathbf Q(x)$, contrary to the elementary exponential-transcendence argument in §1. Thus $P$ remains a nonzero proper prime after localizing $\widehat A$ by $A\setminus\{0\}$. That localization is $\operatorname{Frac}(A)\otimes_A\widehat A$ and is not a field, whereas $\operatorname{Frac}(\widehat A)$ is a field.

The intended unibranchness argument survives. The localization embeds naturally in $\operatorname{Frac}(\widehat A)$. For every finite $A$-subalgebra $A_\lambda\subset\operatorname{Frac}(A)$, flatness of completion therefore embeds $A_\lambda\otimes_A\widehat A$ in that field. This tensor product is the $\mathfrak m$-adic completion of the finite semilocal algebra $A_\lambda$, hence is a domain. If $A_\lambda$ had more than one maximal ideal, its completion would decompose as a nontrivial product. It follows that every $A_\lambda$ is local, and hence that the integral closure of $A$ is local. Consequently Deligne correctly rejects the displayed equality, but the stated implication “analytically integral implies unibranch” is not refuted.

## Recovered Deligne hard-Lefschetz request

K23-03:230–236 is Deligne’s letter of17October1966. The author defers a proof of the named theorem and hopes another person undertakes it; no proof, computation or detailed hypotheses occur there. The name is identified by SGA7IIXVIII5.2.2–5.2.2.1, printedpp281–282. The author page254 says N.Katz, based on succinct Grothendieck notes. The definition concerns powers of an ample hyperplane class on rational l-adic cohomology; the smooth case is still conjectural there.

Deligne’s1980WeilII4.1.1, printedp217, states the smooth projective pure-dimensional ample-class theorem over an algebraically closed field with l different from its characteristic. The text suppresses Tate twists after choosing a trivialization. Pages217–218 reduce to the nondegeneracy of the intersection pairing on the image of a smooth hyperplane section, identify that image with monodromy invariants, and invoke complete reducibility. The elementary4.1.4 step is checked as follows: split a semisimple representation V as V^pi plus a complement W with no trivial quotient. Invariance forces W to be orthogonal to V^pi, so nondegeneracy on V forces nondegeneracy on V^pi. This verifies that local linear-algebra step only; the global weights/semisimplicity and invariant-cycle inputs are published dependencies, not reproved here.

The exact source request and the modern theorem are different evidence layers. No integral-coefficient, nonprojective or standard-conjecture extension is inferred. There is no source calculation requiring numerical code, and no new finite certificate is fabricated. Primary locators: EGA_KatzSGA7XVIII1973; EGA_DeligneWeilII1980.

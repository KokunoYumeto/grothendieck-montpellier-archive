# ALP_MACHINE — question 3: the Kummer character and the precise transfer gate

Author/checker: GPT-6 Astra Pro, ALP_MACHINE child `/root/kummer_extension`; inherited reasoning effort is not separately exposed. Date: 21 November 2026. This is a mathematical contribution for integration into the main paper, not a claim that the requested RH extension has been completed.

## 0. Outcome and scope

The source has a field-independent analytic theorem that can be applied to the Kummer character. **AM-K005** below proves all of its pole-data hypotheses and identifies a single, explicit remaining arithmetic window estimate. For $r=3$, **AM-K004** also realizes the character as a rank-one summand in a tensor construction from two explicit CM elliptic curves. These are constructive reductions. They do not prove the missing window estimate.

The literal existing character host cannot receive the Kummer splitting field or its induced representation. This is stronger than a missing notation adapter: **AM-K002** proves three exact obstructions—non-CM splitting field, failure of norm pullback from a rational Dirichlet character, and failure of a finite Artin-formalism factorization into rational Dirichlet characters. Each obstruction is explicitly scoped; none asserts that a different CM-geometric construction is impossible.

Alpöge's theorem and archive are used as accepted theorems, as directed. CX-ALG-024, CX-R02, CX-G06, DP6, DP32, DP34, DP42 and the supplied source-interface results are carried with their existing status. No check of the validity of the accepted Dirichlet GRH theorem is undertaken. Masullo's consequences remain conditional. No Lean compilation was performed in this contribution; the archive checks below are checks of actual declarations and their types.

### 0.1 Source provenance and what was actually read

The primary note is Alpöge, *Remark*, pp. 3–4, numbered timeline steps 2–20, https://alpo.ge/remark.pdf. The note calls this a rough timeline. Its historical step numbering is not itself a one-to-one module index.

Actual Lean text was recovered at pinned mirror commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of `CocoSgt/riemann-hypothesis-lean`, under `src/`. The local copy is `work/agents/kummer_sources/`; `manifest.json` records each downloaded file, byte count and SHA-256. Two files checked against the supplied original-author source manifest already match: `Formalism/SizeWindowBrackets/GrowthBoundGivesRiemannHypothesis.lean` and `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean`. The remaining copies are pinned mirror text, corroborated where applicable by the supplied original-archive map; this contribution does not claim every mirror file has independently been compared with the original archive.

The supplied map is `RETURN_THETA3_checkpoint_07_20261121T0604Z/supplied_sources/ALPOGE_LEAN_MAP_20261120.md`, especially §§3–4. Its low-confidence keyword correspondences for steps 11, 14, 17 and 19 are not promoted to a complete dependency audit here.

## 1. Setup and the $p=r$ edge case

Let $r$ be an odd prime, $p$ a rational prime, $\alpha=p^{1/r}>0$, and

\[
K=\mathbf Q(\zeta_r),\qquad F=\mathbf Q(\alpha),\qquad E=K(\alpha).
\]

The user assumes $r\nmid(p-1)$. The algebraic results below do not need this restriction. It matters for the surrounding finite-field construction. Let $\chi=\chi_{p,r}:G_K\to\mu_r$ be $\sigma\mapsto\sigma(\alpha)/\alpha$, viewed by class field theory as the primitive finite-order Hecke character with its actual conductor. Write $L(s)=L_K(s,\chi)$, retaining all primitive local factors.

### AM-K000. The edge $p=r$ is permitted and is algebraically nondegenerate

**Statement.** The displayed condition permits $p=r$. For this case $[E:K]=r$, the same affine Galois group and character analysis used below apply, and the finite-field task of constructing $\mathbf F_{p^p}$ has the elementary irreducible polynomial $T^p-T-1\in\mathbf F_p[T]$. Its use requires no RH premise.

**Proof.** The polynomial $T^r-r$ is Eisenstein over $\mathbf Q$, so $[F:\mathbf Q]=r$. Because $[K:\mathbf Q]=r-1$, the intersection $F\cap K$ is $\mathbf Q$, and $[E:K]=r$. Equivalently, at the unique prime $\mathfrak r$ of $K$ above $r$, the normalized valuation satisfies $v_{\mathfrak r}(r)=r-1\not\equiv0\pmod r$, so $r$ is not an $r$-th power in $K$. The statement is not that $T^r-r$ is Eisenstein over $K$; its constant-term valuation there is $r-1$. The automorphisms $\alpha\mapsto\zeta_r^b\alpha$, $\zeta_r\mapsto\zeta_r^u$ give the full affine group of order $r(r-1)$.

For the finite-field assertion, let $a$ be a root of $T^p-T-1$ in an algebraic closure of $\mathbf F_p$. Then $a^p=a+1$, and induction gives $a^{p^m}=a+m$ for every nonnegative integer $m$. The least positive $m$ with $a^{p^m}=a$ is $p$. Its Frobenius orbit therefore has length $p$, so its minimal polynomial has degree $p$ and equals the given degree-$p$ polynomial. ∎

The previously accepted CX-ALG-024 was stated for $p\ne r$. The finite-field observation separates the omitted wild case from that statement without changing it.

## 2. The exact target representation and L-function

### AM-K001. A single real L-function for all nontrivial Kummer powers

**Statement.** Set $N=\operatorname{Gal}(E/K)\simeq C_r$, $G=\operatorname{Gal}(E/\mathbf Q)\simeq\operatorname{AGL}_1(\mathbf F_r)$, and let $P$ be the permutation representation of $G$ on the $r$ roots of $T^r-p$. For every nontrivial character $\vartheta$ of $N$,

\[
\rho:=\operatorname{Ind}_N^G\vartheta\simeq P-\mathbf 1.
\tag{K1}
\]

Consequently, for $a=1,\ldots,r-1$,

\[
L_K(s,\chi^a)=L_{\mathbf Q}(s,\rho)
=\frac{\zeta_F(s)}{\zeta_{\mathbf Q}(s)}=:L(s).
\tag{K2}
\]

The identities hold with ramified local factors as well. The resulting Dirichlet series has real coefficients, $L(\bar s)=\overline{L(s)}$, and its representation is self-dual. Under the accepted Dirichlet GRH theorem, RH for this $L$ is equivalent to RH for $\zeta_F$ and for $\zeta_E$.

**Proof of the additional representation statement.** Write an affine map as $x\mapsto ux+b$. The permutation character has values $r$, $0$, $1$, respectively, at the identity, a nonidentity translation, and an element with $u\ne1$. Its augmentation character therefore has values $r-1,-1,0$.

Since $N$ is normal, the induced character vanishes off $N$. On $N$, its restriction is the sum of the conjugates of $\vartheta$ under $\mathbf F_r^\times$. This group acts transitively and freely on all nontrivial characters of $N$. Their sum has value $r-1$ at the identity and $-1$ at every other translation. The two characters agree, proving (K1). This also proves that inducing any nontrivial power gives the same representation.

Artin induction compatibility for L-functions now gives (K2); the standard permutation representation identity gives $L(P)=\zeta_F$, while $L(\mathbf1)=\zeta_{\mathbf Q}$. These identities are local identities on inertia invariants, so they include ramified primes. Since $P-\mathbf1$ is defined over $\mathbf R$ and self-dual, the asserted reality and duality follow. Equivalently, conjugation of the Euler product sends $\chi$ to $\chi^{-1}$, which has the same L-function by (K1).

For the final equivalence, use the already checked CX-ALG-024 identity $\zeta_E=\zeta_K L^{r-1}$; it is not rederived here. Inside $0<\Re s<1$, both $\zeta_{\mathbf Q}L$ and $\zeta_K L^{r-1}$ are products of holomorphic functions, so their zero divisors add with nonnegative multiplicities. Dirichlet GRH puts every zero of $\zeta_{\mathbf Q}$ and $\zeta_K$ on the critical line. The equivalence follows. ∎

**Sources.** CX_GRH/GRH_NIGHT, CX-ALG-024, in `GRH_NIGHT.tex`, subsection containing lines 14723–14826 of the supplied checkpoint. For induction, Milne (2020a), VIII §10, pp. 261–262. Milne uses “Dirichlet” also for ray-class characters of general number fields in that discussion; this does not make those characters rational Dirichlet characters of $(\mathbf Z/N\mathbf Z)^\times$.

## 3. Three exact obstructions to literal reuse

### AM-K002. No cyclotomic host, norm pullback, or rank-one Dirichlet factorization

**Statement.** For odd $r$:

1. $E$ is not a CM field and cannot embed into a CM field. In particular it cannot be the field supplied to the literal `IsChiField` record.
2. $\chi$ is not the pullback of a rational Dirichlet character along the idelic norm $N_{K/\mathbf Q}$.
3. $\rho$ is not a virtual finite sum of one-dimensional rational Galois characters. Thus a finite factorization of its L-function into rational Dirichlet L-functions cannot be obtained by equality of Artin Euler factors, even after enlarging the common finite Galois extension.

These statements do not exclude CM abelian varieties defined over $K$, tensor constructions involving their twists, or a new Hecke-character version of Alpöge's arithmetic host.

**Proof.** Let $\sigma(\alpha)=\zeta_r\alpha$ and let $c$ be ordinary complex conjugation. Since $c(\alpha)=\alpha$ and $c(\zeta_r)=\zeta_r^{-1}$,

\[
c\sigma c^{-1}=\sigma^{-1}\ne\sigma.
\tag{K3}
\]

Complex conjugation is central in the Galois group of a normal CM field: its intrinsic involution commutes with every automorphism. Thus $E$, which is normal, is not CM. There is also a direct containment obstruction. In a CM field embedded in $\mathbf C$, the subfield of elements fixed by ordinary complex conjugation is totally real. The positive real number $\alpha$ cannot be in that subfield, because its minimal polynomial $T^r-p$ has nonreal conjugates. If an embedding of the normal field $E$ into a CM field existed, its image in $\mathbf C$ would again be $E$ and would contain $\alpha$, a contradiction. This proves (1). The central-involution characterization is Milne (2020b), Proposition 1.4 and Corollary 1.5, p. 10.

For (2), conjugation acts on the Kummer character by $\chi^c=\chi^{-1}$, from (K3). A character pulled back through $N_{K/\mathbf Q}$ is $c$-invariant, since $N(c x)=N(x)$. It would follow that $\chi=\chi^{-1}$. An order-$r$ character for odd $r>1$ cannot satisfy this equality.

For (3), the commutator of a multiplier $h_u:x\mapsto ux$ with a translation $\sigma_b:x\mapsto x+b$ is translation by $(u-1)b$. Choosing $u\ne1$ shows that every translation is a commutator. Since $G/N$ is abelian, $[G,G]=N$. Every one-dimensional character is trivial on $N$; every virtual sum of such characters therefore has the same trace at the identity and at any translation. But (K1) gives trace $r-1$ at the identity and $-1$ at a nonidentity translation. This proves the representation obstruction, extending the accepted cubic example CX-R02 to the displayed family.

For completeness, enlargement of the finite quotient cannot remove it. Suppose a finite collection of rational Dirichlet characters and integer exponents gave the same unramified Euler factors as $L(s,\rho)$. Form a finite Galois extension containing $E$ and all their cyclotomic fields. At every prime outside a finite set, equality of the coefficient of $T$ in the Euler factors gives equality of the corresponding virtual traces. Chebotarev gives this equality on every conjugacy class of the enlarged Galois group. The induced map on commutator subgroups surjects onto $[G,G]=N$, whereas each one-dimensional character is trivial on the enlarged commutator. Lifting a nonidentity translation contradicts its trace $-1\ne r-1$. The same argument applies to rational exponents after clearing a common denominator. ∎

**Exact source boundary.** `CharacterBoxes/ExistsPageN.lean`, definition `IsChiField`, line 19, explicitly requires a $\mathbf Q$-algebra embedding into `CyclotomicField N ℚ`. It also uses a fixed field determined by rational congruences modulo $2^{e+2}$, a primitive rational character $\psi$, and two Jacobi symbols. `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Analytic.lean`, `HostRaw.dir`, line 102, explicitly constructs a `DirichletCharacter ℂ H.condN` from the rational residue map `H.art`. This is the literal specialization excluded here.

**Scope.** The conclusion is not that RH for this L-function is logically independent of Dirichlet GRH. It rules out the stated finite rank-one Artin factorization and these literal host substitutions. In particular, Brauer induction permits characters over other base fields; it does not turn those bases into $\mathbf Q$.

## 4. The cubic case with its actual conductor and completed function

### AM-K003. Cubic arithmetic data and the target Euler coefficients

Let $r=3$, $K=\mathbf Q(\sqrt{-3})$, $\lambda=1-\zeta_3$, and assume $3\nmid p-1$. Thus $p=3$ or $p\equiv2\pmod3$. Let $\mathfrak f$ be the primitive conductor of $\chi_{p,3}$.

\[
\begin{array}{c|c|c|c}
\text{case}&D_F&\mathfrak f&N\mathfrak f\\ \hline
p\ne3,\ p\equiv8\pmod9&-3p^2&(p)&p^2\\
p\ne3,\ p\equiv2,5\pmod9&-27p^2&(p)\lambda^2&9p^2\\
p=3&-243&\lambda^4&81
\end{array}
\tag{K4}
\]

The analytic conductor factor is $|D_K|N\mathfrak f=|D_F|$. With $\Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s)$,

\[
\Lambda(s)=|D_F|^{s/2}\Gamma_{\mathbf C}(s)L(s),
\qquad \Lambda(s)=\Lambda(1-s).
\tag{K5}
\]

In particular the root number is $+1$; the functional equation does not force a central zero.

**Justification and specialization.** Harron (2016), §2.1, Lemma 2.1, p. 5, gives the integral bases and discriminants of pure cubic fields. Its Type II condition specializes to $p\equiv\pm1\pmod9$, and under $p\equiv2\pmod3$ this is $p\equiv8\pmod9$. Otherwise the discriminant is $-27p^2$, including $p=3$.

The Artin conductor of an induced character is the discriminant of the base times its relative conductor norm; in the present quadratic induction case see, for example, the formula in the proof of Hida (2025), Corollary 6.18, p. 45. One can verify the normalization directly here without any local convention ambiguity. The quotient of the standard completed Dedekind functions $\Lambda_F/\Lambda_{\mathbf Q}$ is $|D_F|^{s/2}\Gamma_{\mathbf C}(s)L(s)$, because $F$ has signature $(1,1)$. It satisfies the functional equation with sign $+1$. The standard primitive Hecke completion is $(3N\mathfrak f)^{s/2}\Gamma_{\mathbf C}(s)L(s)$. Its dual has the same L-function by AM-K001. Dividing its functional equation by that of the Dedekind quotient gives $C^{s/2}=W C^{(1-s)/2}$, where $C=3N\mathfrak f/|D_F|>0$. On an open set where the functions are nonzero this identity forces $C=1$ and $W=1$, and then holds by continuation. This proves the asserted conductor normalization.

Only primes above $3p$ can ramify, from the polynomial discriminant. If $p\ne3$, $p\equiv2\pmod3$ is inert in $K$, and $T^3-p$ is Eisenstein at $(p)$. The resulting local degree-three extension is tame, so every nontrivial local character has conductor exponent one. The remaining conductor exponent at $\lambda$, whose norm is $3$, is determined by the displayed norm identity. This gives (K4), including $\lambda^4$ when $p=3$. ∎

At a rational prime $\ell\nmid3p$, use the factorization of $T^3-p$ modulo $\ell$. With $T=\ell^{-s}$, the reciprocal Euler polynomials of $L(s)$ are

\[
\begin{array}{c|c|c}
\text{factorization}&\det(1-\rho(\mathrm{Frob}_\ell)T)&
\operatorname{tr}(\rho(\mathrm{Frob}_\ell)^m)\\ \hline
1+1+1&(1-T)^2&2\\
1+2&1-T^2&0\ (m\text{ odd}),\ 2\ (m\text{ even})\\
3&1+T+T^2&-1\ (3\nmid m),\ 2\ (3\mid m)
\end{array}
\tag{K6}
\]

These formulas follow directly from the eigenvalues $1,1$, $1,-1$, and $\zeta_3,\zeta_3^{-1}$ of the augmentation representation. Thus the rational prime-power coefficient in $-L'/L$ is the last column times $\log\ell$. This is the concrete coefficient system that a new geometric family must produce. It is not a periodic rational Dirichlet-character coefficient system.

The same completion argument in arbitrary odd prime degree gives

\[
\Lambda_{p,r}(s)=|D_F|^{s/2}\Gamma_{\mathbf C}(s)^{(r-1)/2}L(s),
\qquad\Lambda_{p,r}(s)=\Lambda_{p,r}(1-s),
\tag{K7}
\]

using the signature $(1,(r-1)/2)$ of $F$ and (K2). This statement needs no explicit general formula for $D_F$.

## 5. An explicit geometric realization in the cubic case

### AM-K004. The Kummer character is a Hom line between two CM elliptic motives

**Statement.** Over $K=\mathbf Q(\zeta_3)$, take

\[
A_0:y^2=x^3+1,\qquad A_p:y^2=x^3+p^2.
\]

For an auxiliary prime $\ell$, use a coefficient field $C_\ell\subset\overline{\mathbf Q}_\ell$ containing $\zeta_3$. Let $V_0,V_p$ be the $\zeta_3$-eigenlines of the endomorphism $[\zeta_3]:(x,y)\mapsto(\zeta_3x,y)$ acting on $H^1_{\mathrm{\acute et}}$. Then, with this eigenline convention,

\[
V_p\simeq V_0\otimes\chi_{p,3},\qquad
\operatorname{Hom}_{C_\ell}(V_0,V_p)\simeq\chi_{p,3}.
\tag{K8}
\]

This is realized by algebraic correspondences: the Artin line is a direct factor of $h^1(A_p)\otimes h^1(A_0)^\vee$, with coefficients containing $K$. It has weight zero. The realization does not provide Alpöge's required quantitative theta-lift family or the window estimate of §6.

**Proof.** Put $\alpha=p^{1/3}$. Over $E=K(\alpha)$ the map

\[
g:A_p\longrightarrow A_0,\qquad (x,y)\longmapsto(\alpha^{-2}x,p^{-1}y)
\tag{K9}
\]

is an isomorphism, since $\alpha^6=p^2$. For $\sigma\in G_K$, the ratio $\sigma(\alpha)/\alpha=\chi(\sigma)$ lies in $\mu_3$, and $\chi^{-2}=\chi$. Therefore

\[
\sigma(g)=[\chi(\sigma)]\circ g.
\tag{K10}
\]

On cohomology, functoriality gives

\[
\rho_p(\sigma)g^*\rho_0(\sigma)^{-1}
=(\sigma g)^*=g^*[\chi(\sigma)]^*.
\]

The two $[\zeta_3]^*$-eigenvalues on $H^1$ are $\zeta_3,\zeta_3^{-1}$. This can be seen on the differential $dx/y$, where the eigenvalue is $\zeta_3$, and its complex-conjugate Hodge summand; the characteristic polynomial is unchanged in étale realization. The projector

\[
e_{\zeta_3}=\frac13\sum_{j=0}^2\zeta_3^{-j}[\zeta_3]^{j*}
\tag{K11}
\]

is an algebraic-correspondence projector over the coefficient field. Restricting the displayed functoriality identity to its image yields

\[
\rho_p(\sigma)g^*=\chi(\sigma)g^*\rho_0(\sigma),
\]

which is precisely (K8). The line in the Hom motive becomes the trivial line over $E$ with descent cocycle $\chi$; this identifies it with the Artin motive defined by that character, not merely with an unrelated equal-dimensional representation. As a tensor of weight-one cohomology with its dual, it has weight zero. ∎

**What this does and does not change.** Both elliptic curves have CM by $K$, are isomorphic over $\overline{\mathbf Q}$, and have the same geometric CM type and stable Faltings height. At a good prime their formal groups become isomorphic after extension. At good rational primes inert in $K$, these formal groups have height two, so the existing height-two derivative mechanism applies after suitable base extension; DP6 supplies its known exponent. Split good primes have height one and give no extra height-two contribution. A finite-order descent twist is actual arithmetic information, but it is not a new geometric height budget.

The invariant differentials in these equations satisfy

\[
g^*(dx/y)_{A_0}=\alpha\,(dx/y)_{A_p}.
\tag{K12}
\]

Indeed $\alpha^{-2}/p^{-1}=p\alpha^{-2}=\alpha$. For transported complex cycles, $\Omega_0=\alpha\Omega_p$. These algebraic factors must be retained in the integral lattices and period normalization. Removing them by consistent normalization cannot itself supply a favorable extra lift cost. No equality of `MainX` kernel, covolume, mass, or terminal-period records has been inferred from this isomorphism.

This construction is also why the non-CM statement in AM-K002 must not be overstated as “the character cannot occur in CM motives.” It does occur in this explicit tensor category over $K$.

## 6. A completed analytic transfer and the surviving arithmetic gate

### AM-K005. Field-independent Landau reduction for the Kummer L-function

Define $\Lambda_K(\mathfrak a)=\log N\mathfrak q$ when $\mathfrak a=\mathfrak q^m$ for a prime ideal $\mathfrak q$ and $m\ge1$, and zero otherwise. Extend the primitive character by zero at ideals not coprime to its conductor. Put $c_1=L'(1)/L(1)$ and, for $x\ge1$,

\[
G_\chi(x)=\sum_{N\mathfrak a\le x}\Lambda_K(\mathfrak a)\chi(\mathfrak a)
\left(\frac{x}{N\mathfrak a}-1\right)+xc_1.
\tag{K13}
\]

**Theorem.** This is real-valued. Fix $0<\theta<1$ and $\delta>0$. Suppose the following single window condition holds:

> **$\mathcal W_\chi(\theta,\delta)$.** For every $\eta>0$ and every $Y_0\ge1$, there exist $Y\ge Y_0$ and a measurable $R:[Y,Y^{1+\delta}]\to\mathbf R$ such that $0\le R(x)$, $G_\chi(x)\le R(x)$, $R(x)x^{-\theta-1}$ is integrable, and
> \[
> \int_Y^{Y^{1+\delta}}R(x)x^{-\theta-1}\,dx\le Y^\eta.
> \tag{K14}
> \]

Then $L(s)$ has no zero with $\Re s>\theta$. Consequently it suffices to prove $\mathcal W_\chi(1/2+\epsilon,1/2)$ for every $0<\epsilon<1/2$ to prove RH for $L$, and hence the CX-ALG-024 consequences under accepted Dirichlet GRH.

**Proof.** We verify the actual `Deduction.PoleData` interface and invoke the accepted source theorem `Deduction.landau_window`. The analytic continuation, functional equation, Euler product for $\Re s>1$, and nonvanishing $L(1)\ne0$ of a nontrivial finite-order Hecke character are classical. In the Artin description (K2), the relevant holomorphy is the classical monomial case, obtained by its identification with this nontrivial Hecke L-function; it is not inferred from an unproved cancellation in a quotient of zeta functions. The standard nonvanishing at $1$ is Milne (2020a), V Theorem 2.4(b), p. 156; its Euler product and continuation conventions are V §2 and VIII §10.

By AM-K001, the coefficients of $L$, and therefore those of $-L'/L$, are real. In particular $c_1\in\mathbf R$. Grouping the ideal terms by rational norm writes

\[
-\frac{L'}L(s)=\sum_{n\ge1}\frac{b(n)}{n^s},\qquad
G_\chi(x)=\sum_{n\le x}b(n)(x/n-1)+xc_1,
\tag{K15}
\]

with $b(n)\in\mathbf R$. At a rational prime $\ell$, the local factor is the determinant of $1-\rho(\mathrm{Frob}_\ell)\ell^{-s}$ on inertia invariants. All its nonzero eigenvalues are roots of unity, and there are at most $d=r-1$ of them. Thus

\[
|b(\ell^m)|\le d\log\ell,
\qquad b(n)=0\quad\text{if }n\text{ is not a prime power}.
\tag{K16}
\]

This bound includes ramified primes and proves the absolute convergence needed below. It also gives the elementary growth estimate, for $x\ge1$,

\[
|G_\chi(x)|\le dx\sum_{2\le n\le x}\frac{\log n}{n}+|c_1|x
\ll x(1+\log x)^2\ll x^2.
\tag{K17}
\]

At a threshold $x=n$ the newly appearing term is zero. Hence $G_\chi$ is continuous and piecewise affine. Set $g(u)=G_\chi(e^u)$ for $u\ge0$, and $g(u)=0$ for $u<0$. It is measurable and $|g(u)|\le C e^{2u}$ for $u\ge0$.

For $\Re s>1$, direct integration gives

\[
\int_n^\infty (x/n-1)x^{-s-1}\,dx=\frac{n^{-s}}{s(s-1)}.
\]

The absolute integral of the summands is bounded by the corresponding expression with $|b(n)|$ and $\Re s>1$, which is finite by (K16). Termwise integration is therefore legitimate and yields

\[
\Phi(s):=\int_1^\infty G_\chi(x)x^{-s-1}\,dx
=-\frac{L'(s)}{s(s-1)L(s)}+\frac{c_1}{s-1}
=\frac{-L'/L(s)+s c_1}{s(s-1)}.
\tag{K18}
\]

At $s=1$ the numerator vanishes. Define $\Phi(1)$ by the removable continuation; it equals $c_1-(L'/L)'(1)$. At zeros of $L$, regard $\Phi$ as meromorphic and assign arbitrary values if a total function is required by the formal interface. At points with positive real part outside those zeros it is holomorphic, including $1$. Under $x=e^u$, (K18) is the Laplace identity

\[
\Phi(s)=\int_0^\infty g(u)e^{-su}\,du,
\]

in particular on the source's required half-plane $\Re s>2$.

Let $Z=\{\rho:\Re\rho>0,\ L(\rho)=0\}$. The function $L$ is entire, not identically zero, and $L(1)\ne0$. Its zeros are isolated. If $\rho\in Z$ has multiplicity $m$, write $L(s)=(s-\rho)^m a(s)$, with $a$ nonvanishing near $\rho$. Then

\[
\Phi(s)=\frac{m}{\rho(1-\rho)}\frac1{s-\rho}+h_\rho(s),
\tag{K19}
\]

where $h_\rho$ is holomorphic near $\rho$. The residue is nonzero since $\rho\ne0,1$. If $\rho$ is real, the Euler product excludes $\rho>1$, and $L(1)\ne0$, so $0<\rho<1$. The residue $m/[\rho(1-\rho)]$ is then strictly positive and real. These are exactly the positivity and simple-pole conditions of `PoleData`; the pole is simple even when the zero of $L$ has higher multiplicity.

All fields of the source record have now been supplied: measurability, exponential growth, Laplace representation, positive real parts of $Z$, holomorphy away from $Z$, isolation, and the required nonzero residues with positive sign at real zeros. No Hecke-family extension of its Dirichlet-specialized `CharFamily` is needed for this application.

It remains to translate (K14). Given the $U_0\in\mathbf R$ required by `WindowHypU`, choose $Y_0=\max(1,e^{U_0})$. Put $U=\log Y$ and $\widetilde R(u)=R(e^u)$. Then $U\ge U_0$, $\widetilde R\ge0$, $g\le\widetilde R$, and the change of variables $x=e^u$ gives

\[
\int_U^{(1+\delta)U}\widetilde R(u)e^{-\theta u}\,du
=\int_Y^{Y^{1+\delta}}R(x)x^{-\theta-1}\,dx
\le e^{\eta U}.
\]

This is precisely `WindowHypU g θ δ`. The accepted theorem `landau_window` gives $\Re\rho\le\theta$ for every $\rho\in Z$.

If the condition is known for every $\theta=1/2+\epsilon$, then no zero has real part $>1/2$. The self-dual functional equation (K7) maps a nontrivial zero of real part $<1/2$ to one of real part $>1/2$, while the gamma factor is nonzero and holomorphic in the critical strip. This proves RH under the asserted window conditions. ∎

**Actual Lean locators.** With common prefix `Development/AutomorphicArithmetic/DedekindLFunctions/`:

| Record/theorem | File and locator | Exact transfer use |
|---|---|---|
| `Deduction.PoleData` | `LandauZeroFreeCriterion.lean:15` | Arbitrary $g:\mathbf R\to\mathbf R$, $\Phi:\mathbf C\to\mathbf C$, $Z\subset\mathbf C$; no character or base-field parameter. |
| `Deduction.WindowHypU` | `LandauZeroFreeCriterion.lean:25` | Quantifiers and weighted window integral translated in (K14). |
| `Deduction.landau_window` | `LandauTheorems/landauWindow.lean:83` | The accepted analytic implication used above. |
| `poleData_abstract` | `LandauTheorems/poleData.lean:22` | Confirms a generic analytic layer precedes the Dirichlet-family specialization at line 248. The proof above directly verifies the record instead of claiming a new Lean instantiation. |
| ramp Mellin kernel | `LandauTheorems/MellinRamp.lean:10`; `mellinGchiOfNeOne.lean:65,116` | Generic scalar kernel and arithmetic-sequence integration before Dirichlet specialization. |

**A sufficient stronger estimate.** If, for every $\epsilon>0$, $G_\chi(x)\le x^{1/2+\epsilon}$ for all sufficiently large $x$, take $R(x)=x^{1/2+\epsilon}$. The integral in (K14) is $\delta\log Y$, which is at most $Y^\eta$ for all sufficiently large $Y$. Thus a one-sided pointwise bound suffices; absolute-value control is unnecessary for this deduction. No such bound is proved here.

**Current gate, Q3-KUMMER-WINDOW.** Construct a relative character host and an actual arithmetic theta-lift family whose period, divisibility, covolume, integral-structure, and cost equations prove (K14), for each $\epsilon>0$, with $\theta=1/2+\epsilon$, already for the explicit cubic data (K4), (K8), (K13). This is an explicit analytic obligation left by the arithmetic construction. The source's generic Landau theorem eliminates a separate analytic-generalization obligation.

## 7. Steps 2–20: actual interface audit and replacement obligations

The short titles in the following table identify the historical timeline. The right-hand column distinguishes a completed replacement from a required new instance. A source anchor is a declaration whose scope was actually checked, or a clearly labelled carried source interface. It is not a claim to have exhaustively inspected every proof body contributing to that step.

| Step | Q-sensitive interface and replacement over $K$ | State and exact anchor |
|---|---|---|
| 2: local derivations | The local divided-power/height statement is already local arithmetic geometry. For $r=3$, the CM elliptic curves of AM-K004 give explicit good-reduction inputs after extension. All conductor primes remain in the global bookkeeping. | DP6, DP32, DP34 and DP42 are carried; no new exponent is asserted. AM-K004 supplies the twist, not a better divisibility budget. The supplied map §4 labels its correspondence to `BlockTheory/HeightDefect` and CM-good-curve files as low confidence. |
| 3: quadric and biextension | Poincaré bundles and the relevant quadratic constructions can be formed over a number field. What must be newly proved is that the resulting character-weighted arithmetic functional equals the norm-indexed $G_\chi$ in (K13), with its actual integral lattices. | The generic geometry does not manufacture this equality. Carried source families: `Formalism/LocalToGlobal/GlobalTheory`; directly checked assembly record `ThetaIntegralsAgree` and `LocalMatching` in `SiegelEisensteinSecondTermHypotheses.lean:44,69`. |
| 4: determinant positivity | Positivity of a fixed Hermitian determinant is field-independent linear algebra. Identifying it with the target arithmetic sum is a separate global construction. | No new positivity theorem is needed at this level; no target determinant identity has been proved. The supplied map found no exact one-to-one source module for this historical step. |
| 5: smoothed explicit formula | Replace rational integer coefficients $\Lambda(n)\psi(n)$ by $\Lambda_K(\mathfrak a)\chi(\mathfrak a)$, and rational conductor normalization by (K4). | Completed analytic replacement in AM-K005. Literal definitions are `Analytic.lean:9,11,18,23` (`abelian₂`, `logDerivativeAtOne`, `sumLamChi`, `gChi`). |
| 6: zero-free deduction | Apply a base-field-free pole theorem to the real induced L-function; do not substitute a Hecke character into `PChar`. | Completed conditional deduction AM-K005. `LandauZeroFreeCriterion.lean:15,25`; `LandauTheorems/landauWindow.lean:83`. |
| 7: periods and weights | The underlying CM/unitary setting is not restricted to $\mathbf Q$. The new task is to choose the target ray-class character, test vectors and interlacing data so its period is exactly the coefficient functional needed in step 5. | Generic CM Galois row is visible in `WeightsConjBis.lean:69` (`Row0b`); it does not state a Hecke RH conclusion. Carried period anchor `Formalism/PeriodIntegrals/BesselPeriodGGP.lean`. Target period identity open. |
| 8: repeated definite lifts | Build an actual chain for the new ray-class family, with the six carried lift identities, controlled nonvanishing and correct rank costs. Keeping $K$ CM is possible; using non-CM $E$ as a CM base is excluded by AM-K002. | AM-K004 gives initial geometric descent data only. Direct assembly anchor `nonempty_hyps_definite_side_of_closed_bound`, `SiegelEisensteinSecondTermHypotheses.lean:44`, requires linked norm bounds and the other records. |
| 9: norms and masses | Replace level/discriminant and local indices by those of the relative conductor, and include the unit and archimedean normalizations over $K$. The cubic conductor is explicit in (K4). | Generic mass identities may be reused with hypotheses, but their evaluation for the new chain is open. Carried `Formalism/PeriodIntegrals/UnitaryGroupMassFormula`; `CovolumeBoundOfX` in the checked assembly theorem. |
| 10: global divisibility | Local DP bounds remain available; the global sum must be normalized by $\log N\mathfrak q$, residue degrees, bad-prime lattices and all embeddings. | No equality of the new global gain to the original gain is proved. Carried divisibility interfaces `Formalism/SharpRestriction/Divisibility` and `Formalism/LocalToGlobal/Divisibility`. |
| 11: auxiliary tower | A relative ray-class tower over $K$ must replace the rational cyclotomic fixed-field construction. The Kummer layer need not be CM as an absolute number field. | Literal substitution fails by AM-K002. `ExistsPageN.lean:19,27,39` (`IsChiField`, `WinPair`, `PageN`) explicitly require rational congruence and cyclotomic data. New tower with the necessary character separation and size bounds is open. |
| 12: seesaw and terminal period | Seesaw/Rallis formalism over CM $K$ is available at the generic level. The target family must satisfy the specified character independence and terminal-period normalization. | The explicit twist identity is not that terminal period identity. Actual checked bridge: `ThetaIntegralsAgree`, `LocalMatching`, `SiegelEisensteinSecondTermHypotheses.lean:44,69`. Carried `ThetaCorrespondence/RallisInnerProduct`. |
| 13: slope inequality | The Arakelov slope inequality is already a number-field statement. Supply the actual metrized lattices, normalize degrees by the field degree, and include residue degrees in finite contributions. | New lattice/cost instance open. Carried source `Formalism/LatticeSlopes/LatticeSlopesProofs/SlopeInequality.lean`; source assembly still needs `CovolumeBoundOfX`. |
| 14: cost evaluation | Compute every local and global term for the new lifts, using the actual conductor and period scaling (K12). The algebraic twist alone does not determine those terms or their cancellation. | No cost improvement or RH follows from the same geometric CM type. The supplied step-to-source map identifies `UnitaryGroupMassFormula/UnipotentCost` only with low confidence; it is not treated as a complete formula for the target. |
| 15: common integral structure | Replace rational primitive-character sets by finite-order ray-class characters over $K$, and prove common coefficient-ring, saturation and congruence properties for their sections. | New host adapter required. `Analytic.lean:102,106,145,149,154` (`HostRaw.dir`, `IsPrimOf` and analytic bounds) all quantify rational Dirichlet characters. AM-K002 excludes the naive norm-pullback route. |
| 16: trace/orthogonality bound | The relative trace identity needs an actual ideal/ray-class indexing, stabilizers, unit factors and quantitative orbital count for the new host. | A formal orthogonality equality alone does not supply the needed scale-uniform bound. Carried `Formalism/PeriodIntegrals/OrbitalBoundsConclusion`; no target version is proved. |
| 17: cohomology control | The weighted Galois-cohomology size predicate `VVle E t B` is generic in a number field $E$. Its available supply theorem is indexed by rational `PChar` and `IsChiField`. | `ExistsPageN.lean:12,41,44,49`; `SupplyChi.lean:8`. A relative version over the new tower, with the same quantitative allowance, remains open. It is not supplied just by Dirichlet GRH. |
| 18: covolumes and indices | Compute the actual determinant and finite-index lattice for the new global family; the conductor table fixes only part of its arithmetic input. | `CovolumeBoundOfX` is a required hypothesis at `SiegelEisensteinSecondTermHypotheses.lean:44,69`. No `MainX` instance or covolume equality for $\chi$ has been constructed. |
| 19: combinatorial tower choice | Any abstract finite-set combinatorics must be realized with the new ray-class/tower parameters and the necessary cost and independence properties. | The supplied map §4 explicitly marks the use of `Formalism/BehrendSets` in the final chain as uncertain. No extra Q-specific theorem is invented from that historical label. The precise checked tower restrictions remain `IsChiField` and `WinPair`. |
| 20: final theorem | The literal endpoint is `EveryCharacter`, a statement about `DirichletCharacter ℂ N`. The replacement endpoint is the conclusion of AM-K005 once the target window is proved. | `CharacterBoxes/EveryCharacter.lean:13`; `ThirdPlaceSeries/TopPlug.lean:12,16`. The new arithmetic window remains unproved, so the requested Hecke RH conclusion is not established. |

Two additional interface observations make the gate concrete. First, `CharacterBoxes/Supply.lean:10` defines a generic request type `FReq`, but its actual target request at line 42 is

\[
\texttt{GChi ψ}:
\quad\texttt{EAtH (Level.cyc ψ) H.toHostRaw TT s.x s.eps 4}
\ \land\ \texttt{VVle H.E t (sqrt s.b)}.
\]

The ambient request formalism is not the obstruction; the specific character/host supply is. Second, `CharacterBoxes/ZeroFreeAllOfTopG.lean:12,26` separates the generic design/top-level family machinery from its application to `PChar`. A relative version must produce a new target request and prove its supply, then connect it to (K13). Merely adding a new character type without those proofs would relocate the gap.

## 8. Grothendieck-language formulation

### AM-K006. The finite étale and motivic dictionaries preserve the gate

Let $U=\operatorname{Spec}\mathbf Z[1/(rp)]$, $U_K=\operatorname{Spec}\mathcal O_K[1/(rp)]$. The normalization $U_E\to U_K$ is a finite étale $\mu_r$-torsor. Indeed $p$ and $r$ are units there; the derivative $rT^{r-1}$ is invertible on $T^r=p$, and $K$ already contains $\mu_r$. The character $\chi$ is its Kummer local system. For coefficients containing $\mu_r$, the idempotent

\[
e_\chi=\frac1r\sum_{g\in C_r}\chi(g)^{-1}g
\]

in the finite-cover correspondence algebra projects its rank-one Artin summand (with the chosen action convention). Every geometric Frobenius eigenvalue on that summand is a root of unity. Thus it is pointwise pure of weight zero. This is a statement about each closed fibre, not about zeros of the global L-function.

For the finite étale cover $U_F\to U$, the permutation local system satisfies

\[
[\rho]=[h^0(U_F/U)]-[\mathbf1]
\]

in the Grothendieck group of finite-monodromy local systems, equivalently in the representation ring of $G$. Its characteristic-polynomial identity is

\[
\det(1-gT\mid\rho)=\frac{\det(1-gT\mid P)}{1-T}.
\]

Exterior-power operations $\lambda^j$ encode these determinants. AM-K001 and the carried CX-ALG-024 are therefore identities in the Artin-motivic $K_0$ / representation-ring setting. AM-K002 says that this particular class is outside the subring generated by rational abelian Artin lines: every virtual object in that subring has trivial commutator action, whereas $\rho$ does not. Adding tensor products, duals, exterior powers, symmetric powers or characteristic-zero direct summands of those abelian lines does not change that action. This is the elementary finite-group content of the carried GRH_NIGHT AG-LAMBDA discussion, not a new global purity theorem.

For $r=3$, AM-K004 gives the more useful relative realization over $K$: the finite-monodromy line is the Hom of two CM elliptic eigensummands. The elliptic curves and their Picard duals extend as abelian schemes after deleting their bad primes. Their Poincaré biextensions give the usual tensor/duality pairings. The finite descent cocycle changes the Artin factor while leaving the geometric CM type and local height-two formal-group isomorphism unchanged after extension. The arithmetic integral lattice and descent factors remain essential for the cost.

**Exact framework locators.**

| Language | Locator and status | Meaning here |
|---|---|---|
| Finite étale covers and finite G-sets | SGA 1, Exposé V, Théorème 4.1; primary reedition https://arxiv.org/pdf/math/0206203 | The covering/local-system/representation dictionary used above. |
| Kummer torsors | SGA 1, Exposé XI §6, Proposition 6.1, Définition 6.2, Corollaires 6.3 and 6.5; reedition PDF pp. 248–250, original marginal pp. 303–305 | $T^r=p$ on the base with $rp$ inverted and its $\mu_r$-character. |
| $\lambda$-rings and $K_0$ | SGA 6, Exposé V §§2 and 7, especially (7.1.1); carried GRH_NIGHT AG-LAMBDA | Exterior-power determinant operations on Artin classes; no analytic RH follows from the class identity. |
| CM motives | Milne (2020b), §5, p. 45, for the framework; explicit new construction (K8)–(K11) here | The Artin Hom line belongs to a relative CM tensor category despite the non-CM splitting field. |
| Formal groups and crystals | Carried DP_MULT DP10, DP6, DP32/DP34; Grothendieck cote 54 scans 5–7; cote 4 scans 5–6, 8.4.2 and Lemma 8.4.3, and scans 7–10 for torsion corrections | The local crystalline/Cartier-duality interpretation of the formal groups. No new monodromy result for cote 4 scan 12, §8.6, is asserted. The boxed zero restricted power in cote 54 concerns the vector kernel, as DP10 already established. |
| Picard schemes | FGA, Bourbaki exposé 232, Théorème 3.1; exposé 236, Corollaires 1.7 and 2.3, Proposition 2.10(ii), carried through DP_MULT | Picard/dual abelian schemes for the elliptic curves; this gives geometric objects, not a `MainX` arithmetic identity. |
| Biextensions | SGA 7 I, Exposés VII–VIII; carried DP_MULT/THETA3 framework | Poincaré biextension and Cartier duality organize the pairings; no finer unverified proposition number is fabricated. |
| Weights versus global zeros | Carried CX_GRH CX-G06 | Weight zero of a finite-monodromy sheaf does not imply RH over a number field. The missing input remains (K14). |

The archive cote locators above are carried from the supplied DP_MULT record, not newly reread scans in this child contribution. Their exact statements are not enlarged.

## 9. Tried approaches and the remaining work

| Approach | Result reached | Why it does not finish RH |
|---|---|---|
| Instantiate the final theorem with $\chi$ | Actual endpoint type read | `EveryCharacter` quantifies rational Dirichlet characters. |
| Pull back a Dirichlet character by the norm | Refuted, AM-K002(2) | The target is anti-invariant under complex conjugation and has odd order. |
| Express the Artin L-function by finitely many rational Dirichlet factors | Refuted in the Euler-factor/Artin sense, AM-K002(3) | Nontrivial commutator trace. This does not refute every conceivable deduction from A_D. |
| Insert $E$ as the existing cyclotomic/CM host | Refuted, AM-K002(1) | $E$ cannot embed in a CM field, whereas `IsChiField` requires a rational cyclotomic embedding. |
| Realize the cubic character geometrically | Completed explicit Hom-line realization, AM-K004 | The integral lattice, period functional, nonvanishing chain, and cost/window identities are not consequences of the geometric twist. |
| Generalize the analytic Landau stage | Completed reduction, AM-K005 | All source `PoleData` hypotheses verified; the arithmetic window (K14) remains. |
| Use known generic CM automorphic source rows | Type checked | `Row0b` is already CM-general, but the proved outer endpoint and host supply remain rational-character-specific. |
| Use a newer cubic-Hecke zero-free source | Consulted only | OpenAI (2026), Theorem 1.1, claims $\Re s>7/8$. Its long proof was not audited here and is not an accepted premise stipulated by the user. The downloaded `ComparatorChallenges/HeckeSevenEighths.lean` is a comparator statement containing `sorry`, not a proof certificate. Even the stated half-plane would not prove RH. |
| Use Masullo's claimed all-Hecke theorem | Conditional only | No Masullo premise is made unconditional. The carried GRH_NIGHT gate Q-MAS-GEOMETRIC-NARROW remains unchanged. |

**Masullo locators as supplied, without a new draft audit.** `INTAKE_CX_GRH.md` records the all-Hecke claim in §§1.2 and 1.2.3, PDF pp. 12–16; Theorem 13.3.1.2 on PDF p. 522 is blank in that draft. The same intake records the relevant gaps at §9.3.2, Lemmas 9.3.2.4–9.3.2.5 and Theorem 9.3.2.6, pp. 425–426; §11.3, p. 495; and §§12.3–12.4. `INTAKE_GRH_NIGHT_part3.md` carries the stronger narrowed gate. Those records are cited with their existing check status; no new proof of those draft claims is supplied here.

**Next concrete attack.** Build the relative host for the explicit cubic conductor in (K4), with $\chi$ represented by (K8), and prove that its arithmetic functional is exactly (K13). Then compute the actual lift costs and common integral structure. Success must yield (K14) for every $\theta>1/2$; an estimate at a fixed $\theta>1/2$ is a partial result only. The previously accepted DP64 leading budget and the twist's unchanged geometric height preclude treating a mere relabelling of the same CM data as a newly computed cost saving.

## 10. References and source records

- Alpöge, L. (2026). *Remark*. https://alpo.ge/remark.pdf. Timeline steps 2–20, pp. 3–4; Lean archive as specified in the prompt. Actual declarations and pinned copies listed above and in `kummer_sources/manifest.json`.
- Grothendieck, A., et al. (1971/2003). *Revêtements étales et groupe fondamental (SGA 1)*. Lecture Notes in Mathematics 224; recomposed edition. Exposé V, Théorème 4.1; Exposé XI §6, Proposition 6.1, Définition 6.2, Corollaires 6.3, 6.5. https://arxiv.org/pdf/math/0206203.
- Harron, R. (2016, May 24). *The shapes of pure cubic fields*. §2.1, Lemma 2.1, p. 5. https://math.hawaii.edu/~rharron/research/Harron-PureCubicShapes.pdf.
- Hida, H. (2025, March 27). *Non-vanishing of integrals of a mod p modular form*. Proof of Corollary 6.18, p. 45, induced-conductor formula only. https://www.math.ucla.edu/~hida/EllrevF.pdf. No use of its separate nonvanishing assertions is made.
- Milne, J. S. (2020a). *Class field theory* (v4.03). V §2 and Theorem 2.4(b), p. 156; V Theorem 3.27 and Remark 3.28, pp. 165–166; VIII §10, pp. 261–264. https://www.jmilne.org/math/CourseNotes/CFT.pdf.
- Milne, J. S. (2020b). *Complex multiplication* (v0.10). Proposition 1.4 and Corollary 1.5, p. 10; §5, p. 45. https://www.jmilne.org/math/CourseNotes/CM.pdf.
- OpenAI. (2026, September 30). *The quasi-Riemann hypothesis: A zero-free half-plane Re(s)>7/8*. Theorem 1.1, consulted but not used as an established premise in this report. https://github.com/openai/math/tree/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026. Saved TeX SHA-256: `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
- Supplied programme sources: `INTAKE_CX_GRH.md`; `INTAKE_GRH_NIGHT_part3.md`; `GRH_NIGHT.tex`, CX-ALG-024 and AG-LAMBDA; `DP_MULT.tex`, DP6/DP10/DP32/DP34/DP42/DP64; `ALPOGE_LEAN_MAP_20261120.md`, §§3–4. These are carried under the user's stated check status.

**Status for integration.** AM-K000–AM-K006 are proved in their stated scope, with whole-proof author readings recorded separately. The requested RH theorem remains open at Q3-KUMMER-WINDOW. No unconditional deterministic-factoring conclusion is asserted from this contribution. The $p=r$ finite-field construction in AM-K000 is independently unconditional.

**Subsequent concrete progress.** The companion kummer_cubic_host.md proves AM-K007–AM-K011: explicit cubic ray-class characters at every allowed prime; finite-Euler-factor invariance of the normalized window; source-compatible splitting transport and its telescoping limit; and the actual CM tower $\mathbf Q(\zeta_{3\cdot7^n})$ with an invariant coprime half-different, positive unimodular Hermitian lattice, principally polarized products of the CM elliptic twists, and the retained Artin Hom line. Adding the split prime $13$ supplies every mathematical field of the source's AbelianUnramifiedExtensionConditions, including $8\mid f$. The addendum proves why a relative tower ramified at inert $2$ cannot preserve that invariant-half-different condition, and identifies the target's nonsplit and wild ramification that its displayed IsMu0/QDat families do not directly allow. The complete HostRaw/MainX replacement and the arithmetic window remain open.

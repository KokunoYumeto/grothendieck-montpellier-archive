"""NN-C027: smooth integral cubic arithmetic schemes with hard Tate multiplicity."""

def append_c027(add,E,VV):
    A={'source':'A: Alpoge, Remark; designated RH and Dirichlet-GRH input theorems',
       'locator':'riemannHypothesis and riemannZeta_eq_zero_re, Main.lean lines4,6; LFunction_eq_zero_re_of_isPrimitive, Main.lean line12, as recorded in OURS_ALPOGE_LEAN_MAP_20261120.md Section3',
       'path':'sources/OURS_ALPOGE_LEAN_MAP_20261120.md',
       'url':'https://alpo.ge/remark.pdf',
       'access_note':'Designated input theorem; no new Lean replay or full input-proof verification claimed.'}
    sga1={'source':'SGA1, ExposeII, Section4',
          'locator':'Theorem4.10(iii) and Corollary4.12, relative Jacobian criterion over the integer base',
          'url':'https://grothendiecksga.com/read/sga1/fr/II-4.html'}
    basechange={'source':'SGA4, ExposeXVII',
                'locator':'Theorem5.2.6 and Proposition5.2.8 (!-base change and geometric stalks); Theorem5.4.3 (compact-support Kunneth); localization5.1.16.3',
                'url':'https://grothendiecksga.com/read/sga4/fr/XVII-5.html'}
    trace={'source':'SGA4, ExposeXVIII',
           'locator':'Equation2.8.1 (affine-space top trace), Theorem2.9 (relative trace, base change and normalization); Proposition1.1.6 and equation1.1.3.2 for the projective-line calculation',
           'url':'https://grothendiecksga.com/read/sga4/fr/XVIII-2.html',
           'additional_url':'https://grothendiecksga.com/read/sga4/fr/XVIII-1.html',
           'access_note':'Exact statements and local proof passages read in the text edition; no original archive cote claimed.'}
    zeta={'source':'NIST Digital Library of Mathematical Functions',
          'locator':'Equation25.4.2 (zeta functional equation); equation25.2.11 (Euler product on Re(s)>1)',
          'url':'https://dlmf.nist.gov/25.4',
          'additional_url':'https://dlmf.nist.gov/25.2'}
    add('NN-C027','NEG_NIGHT-10e',
        'Smooth integral cubic arithmetic schemes carry counting-hard pure Tate multiplicities',
r'''Let $N=\#\operatorname{SAT}(\Phi)$ for a fixed-width CNF with $n\geq1$ input variables and $m$ clauses. In polynomial time one can construct a smooth affine scheme $X_\Phi/\mathbb Z$, with every geometric fiber integral, given by one sparse cubic equation in $O(n+m)$ coordinates. There are explicit integers $v,h=O(n+m)$, with $v,h\geq1$, for which
\[
 [X_\Phi]=\mathbb L^{v+h}+N\mathbb L^h,
 \qquad
 \#X_\Phi(\mathbb F_q)=q^{v+h}+Nq^h
\]
for every prime power $q$, and
\[
         \zeta_{X_\Phi}(s)=\zeta(s-v-h)\zeta(s-h)^N.
\]
The Grothendieck-class identity is proved by an explicit stratification. Separately, over any field $K$ and any prime $\ell$ invertible in $K$, the actual geometric compactly supported l-adic groups are
\[
 H_c^{2h}=\mathbb Q_\ell(-h)^N,
 \qquad H_c^{2(v+h)}=\mathbb Q_\ell(-v-h),
\]
and all others vanish, as representations of the absolute Galois group of $K$. Over finite fields these particular groups are pure Tate; this is proved, not inferred from their point counts alone.

For every nonreal nontrivial zeta zero $\rho$ in $0<\Re\rho<1$, one has
\[
 \operatorname{ord}_{s=h+\rho}\zeta_{X_\Phi}(s)
              =N\operatorname{ord}_{s=\rho}\zeta(s).
\]
The shifted zero locations are therefore controlled by A, while their multiplicity contains the original exact Boolean count. No use of M is made. E computes the multiplicity in its original $n$-variable time bound. Polynomial-time extraction of that multiplicity from these cubic presentations would compute every $\#\mathrm P$ function in polynomial time.

There is also a literal quadratic-character variant over $B=\mathbb Z[1/2]$:
\[
 X^-_\Phi:\ t^2+1=\sum_i y_i f_i(x),\qquad
 \zeta_{X^-_\Phi}(s)=\zeta^{(2)}(s-v-h)L(s-h,\chi_{-4})^N,
\]
where $\zeta^{(2)}(s)=(1-2^{-s})\zeta(s)$. Its lower group is
$H_c^{2h}=(\chi_{-4}\otimes\mathbb Q_\ell(-h))^N$ and its top group is the same Tate line. At any nonreal nontrivial zero $\rho$ of this Dirichlet L-function, its shifted zeta has order $N\operatorname{ord}_\rho L$. Both variants are smooth with geometrically integral fibers; their fixed-$\mathbb F_3$ point-count parity is $1+N\bmod2$.''',
        [{'source':'Prior catalogue CX-E07','locator':'constant finite etale Boolean Z-scheme with degree equal to the satisfying-assignment count; background construction only'},
         dict(E,locator='Theorem1.1, original-variable counting bound'),A,sga1,basechange,trace,zeta,
         {'source':'NN-C006','locator':'exact-count and parity complexity implications, including Toda and Valiant--Vazirani locators'}],
r'''First recall the parameter content of the earlier finite Boolean construction, without counting it as a new finding. Compile the CNF into an AND/NOT verifier circuit with $O(n+km)$ gates. Let $x_1,\ldots,x_v$ be all input and gate coordinates. Impose their Boolean equations $x_j^2-x_j=0$, the quadratic gate equations $z-ab=0$ and $z+a-1=0$, and the acceptance equation $z_{\rm out}-1=0$. These are $h=O(v)$ polynomials $f_1,\ldots,f_h\in\mathbb Z[x]$ of degree at most two and constant monomial sparsity. The Boolean algebra splits as a product of copies of $\mathbb Z$ indexed by bit assignments. Each gate or acceptance equation evaluates to zero or to a unit $\pm1$ in each factor. Consequently
\[
        Y=V(f_1,\ldots,f_h)\subset\mathbb A^v_\mathbb Z
           \simeq\coprod_{N}\operatorname{Spec}\mathbb Z.
\]
There is one extension of each accepting input to the gate coordinates. Retain a Boolean polynomial, say $f_1=x_1^2-x_1$, which is nonzero over every field.

Now introduce $y_1,\ldots,y_h,t$ and define
\[
 X=X_\Phi=V\left(t^2-t-\sum_{i=1}^{h}y_i f_i(x)\right)
                  \subset\mathbb A^{v+h+1}_\mathbb Z.
\]
Its single equation has degree at most three, $O(v+h)$ monomials and constant-size integer coefficients. Denote its left side by $G$. In its coordinate ring,
\[
 1=(2t-1)^2-4\sum_i y_i f_i
   =(2t-1)\frac{\partial G}{\partial t}
       +4\sum_i y_i\frac{\partial G}{\partial y_i}.
\]
Thus the relative Jacobian ideal contains one over $\mathbb Z$ itself. The relative hypersurface criterion proves that the projection $\pi:X\to\mathbb A^v_\mathbb Z$ is smooth of relative dimension $h$, and hence $X\to\operatorname{Spec}\mathbb Z$ is smooth of relative dimension $v+h$. This argument treats characteristic two and odd characteristics uniformly.

To prove geometric integrality, work over an algebraically closed field $K$ of any characteristic and view $G$ as a polynomial in $y_1$ over
$R=K[x,t,y_2,\ldots,y_h]$. Its coefficient is $-f_1\ne0$. The other coefficient is $t^2-t-\sum_{i>1}y_i f_i$, a monic polynomial in $t$. It has no common irreducible factor with $f_1$: every such factor of $f_1$ depends only on $x$, whereas the leading coefficient in $t$ is one. Hence $G$ is primitive over the unique-factorization domain $R$. It is linear and irreducible over $\operatorname{Frac}(R)$, so Gauss's lemma makes it irreducible, and therefore prime, in $R[y_1]$. Every geometric fiber is a domain. The monic equation in $t$ also makes the original coordinate algebra free of rank two over $\mathbb Z[x,y]$.

The count and class have an elementary proof valid over every base. Let $U_i$ be the locally closed stratum where $f_1=\cdots=f_{i-1}=0$ and $f_i$ is invertible. On $U_i$, solve the equation for $y_i$. The other $h-1$ coordinates $y_j$ and $t$ are free, giving
\[
             \pi^{-1}(U_i)\simeq U_i\times\mathbb A^h.
\]
On $Y$, the equation is $t(t-1)=0$; the two factors are comaximal over every ring. Thus
\[
             \pi^{-1}(Y)\simeq
                   (Y\times\mathbb A^h)\coprod(Y\times\mathbb A^h).
\]
Here $[\ ]$ denotes the Grothendieck ring with the usual closed-open scissor relation and $\mathbb L=[\mathbb A^1_\mathbb Z]$. Summing the displayed strata gives
\[
 [X]=\mathbb L^h([\mathbb A^v]-[Y])+2\mathbb L^h[Y]
     =\mathbb L^{v+h}+\mathbb L^h[Y]
     =\mathbb L^{v+h}+N\mathbb L^h.
\]
The same stratification proves the point count, with $N$ rational points of $Y$ over every finite field. Equivalently, for a base point with some $f_i(x)\ne0$, every choice of $t$ and the other $h-1$ coordinates gives one point, so its fiber has $q^h$ points. At a point of $Y$, the fiber has $2q^h$ points. No cancellation estimate or character-sum bound is needed.

We next justify the stronger actual-cohomology assertion. This step is separate from the Grothendieck-class calculation. Fix any base field $K$ and a prime $\ell$ invertible in $K$, with rational coefficients $\mathbb Q_\ell$. Work on the geometric base for cohomology and retain the descent data from $K$. The trace, stalk and projector argument does not require a finite field; Frobenius will be used only for the subsequent finite-field interpretation. The standard affine-space calculation is
\[
 R\Gamma_c(\mathbb A^h_{\overline K},\mathbb Q_\ell)
                   =\mathbb Q_\ell(-h)[-2h].
\]
For $h=1$ this follows from Kummer theory and $\operatorname{Pic}(\mathbb P^1)=\mathbb Z$, the projective-line top trace, and the localization sequence at infinity; powers follow from compact-support Kunneth. Exact source interfaces are SGA4 XVIII1.1.3.2 and Proposition1.1.6, XVII5.1.16.3, XVII5.4.3, and XVIII2.8.1. The !-base-change theorem XVII5.2.6 and its geometric-stalk Proposition5.2.8 now show that $R\pi_!\mathbb Q_\ell$ is concentrated in degree $2h$. Write its sole sheaf as $\mathcal T$.

The involution $\iota:t\mapsto1-t$ acts on $\mathcal T$. Since two is invertible in $\mathbb Q_\ell$, the projectors $(1\pm\iota)/2$ split it into $\mathcal T^+\oplus\mathcal T^-$. Off $Y$ the fiber is affine $h$-space, and $\iota$ is an affine automorphism in the displayed coordinates; it acts trivially on its top compact cohomology. On $Y$ it exchanges the two affine-space components. The relative trace of SGA4 XVIII2.9 gives
\[
                  \mathcal T(h)\longrightarrow\mathbb Q_\ell.
\]
On the plus part it is an isomorphism on every geometric stalk: off $Y$ it is the affine-space trace, and on $Y$ it is the sum of the two component traces, restricted to the diagonal line. The latter sends $(a,a)$ to $2a$; its normalized basis is half the sum of the two component classes. This remains invertible for $\ell=2$ because the coefficient field is $\mathbb Q_2$, not $\mathbb Z_2$. A morphism of etale sheaves that is an isomorphism on every geometric stalk is an isomorphism, so this proves a global identification of the plus sheaf, not just equality of ranks.

The minus part vanishes off $Y$. Base change to $Y$ identifies it globally with the anti-diagonal in the two labeled components $t=0$ and $t=1$, namely $\mathbb Q_\ell(-h)$. If $i:Y\hookrightarrow\mathbb A^v$ is the immersion, the canonical localization map $\mathcal T^-\to i_*i^*\mathcal T^-$ is an isomorphism on every geometric stalk, and hence an isomorphism of sheaves. It follows that $\mathcal T^-=i_*\mathbb Q_\ell(-h)$. All maps are defined over $K$ and are Galois-equivariant; when $K$ is finite they commute with Frobenius. Since the original derived image has a single cohomology sheaf, it is canonically that sheaf shifted. We have proved
\[
 R\pi_!\mathbb Q_\ell
  \simeq\bigl(\mathbb Q_\ell\oplus i_*\mathbb Q_\ell\bigr)(-h)[-2h].
\]
Taking compactly supported cohomology on $\mathbb A^v$ gives exactly the two claimed groups, because $Y$ is $N$ split points. Their degrees are distinct because $v\geq1$. Involution acts as minus one on $H_c^{2h}$ and plus one on the top group. These are actual Tate representations, pure of the displayed distinct weights when the base field is finite; no inference from an arbitrary positive polynomial point count is used.

The local zeta function at a prime $p$ follows from the all-extension-field count:
\[
 Z(X_{\mathbb F_p},T)
       =\frac{1}{(1-p^{v+h}T)(1-p^hT)^N}.
\]
Taking the Euler product, initially for $\Re s>v+h+1$, gives the stated arithmetic zeta identity, and the right side gives its meromorphic continuation. A's RH theorem places the nontrivial zeros of the two Riemann-zeta factors on the shifted lines $\Re s=v+h+1/2$ and $\Re s=h+1/2$, with the second factor present only when $N>0$. For any fixed nonreal nontrivial zero $\rho$ of $\zeta$, use only $0<\Re\rho<1$ and $\Im\rho\ne0$. At $s=h+\rho$ the other factor is $\zeta(\rho-v)\ne0$: its argument has negative real part and nonzero imaginary part, and the functional equation together with the zero-free Euler product on $\Re s>1$ excludes a zero there. Hence the displayed order formula holds without A; A is needed here only to specify the shifted critical lines. No simplicity assumption is required, and no algorithm for measuring this analytic order from a cubic equation is supplied by RH.

The quadratic-character variant uses the same $f_i,v,h,N$, over $B=\mathbb Z[1/2]$, and has equation $t^2+1=\sum_i y_i f_i(x)$. Let $G^-=t^2+1-\sum_i y_i f_i$. In its coordinate ring over $B$,
\[
 1=-\frac t2\frac{\partial G^-}{\partial t}
                     -\sum_i y_i\frac{\partial G^-}{\partial y_i}.
\]
Thus the projection $\pi^-:X^-\to\mathbb A^v_B$ is smooth of relative dimension $h$, by the relative hypersurface criterion already sourced above. For geometric integrality, view $G^-$ as a polynomial linear in a coordinate $y_i$ whose coefficient $f_i$ is nonzero. That coefficient has no common irreducible factor with the remaining coefficient, which is monic in $t$. The primitive-linear-polynomial argument above applies in every residue characteristic of $B$.

Off $Y=V(f_1,\ldots,f_h)$, solving for a coordinate $y_i$ again gives affine $h$-space fibers and the same locally closed affine-bundle stratification. Over $Y$ the scheme is
\[
       Y\times_B\operatorname{Spec}B[i]\times_B\mathbb A^h_B.
\]
This is the actual quadratic etale cover with its two conjugate geometric points. For $p$ odd, the number of roots of $t^2+1$ in $\mathbb F_{p^a}$ is $1+\chi_{-4}(p)^a$: a square root of minus one is present precisely when $p^a\equiv1\pmod4$. Since $Y$ has $N$ rational points over every finite field, adding the rational fibers proves
\[
 \#X^-(\mathbb F_{p^a})=p^{a(v+h)}+N\chi_{-4}(p)^a p^{ah}.
\] The corresponding scissor identity is
\[
 [X^-]=\mathbb L^{v+h}
       +N\bigl([\operatorname{Spec}B[i]]-[\operatorname{Spec}B]\bigr)\mathbb L^h
\]
over $B$. Its difference of classes is the quadratic sign class; the entire scheme is nevertheless an honest smooth integral geometric object.

The full compact-support realization is not inferred solely from this class. Use the cohomological projector proof above for the involution $t\mapsto-t$. Over a geometric base point off $Y$, its action on the top compact cohomology of affine $h$-space is the identity. Over $Y$, it interchanges the two components indexed by $i$ and $-i$. Consequently the plus part of $R^{2h}\pi^-_!\mathbb Q_\ell$ is the constant Tate sheaf, by the global trace normalization. The minus part is supported on $Y$ and is the anti-invariant summand of the rank-two permutation sheaf of the quadratic cover, tensored with $\mathbb Q_\ell(-h)$. This is the sheaf of the character $\chi_{-4}$. Geometric-stalk base change, the global relative trace, and the canonical localization map identify these summands as sheaves, exactly as above; there is no unresolved extension between them because the idempotent projectors split it. All other direct-image sheaves vanish because the geometric fibers are unions of affine $h$-spaces.

Taking compact supports on $\mathbb A^v$ therefore gives
\[
 H_c^{2h}(X^-_{\overline{\mathbb F}_p},\mathbb Q_\ell)
       =\bigl(\chi_{-4}\otimes\mathbb Q_\ell(-h)\bigr)^N,
 \qquad
 H_c^{2(v+h)}=\mathbb Q_\ell(-v-h).
\]
Here the character notation denotes the unramified local Frobenius representation at $p$; its eigenvalue is $\chi_{-4}(p)$. Thus the lower group has Frobenius eigenvalues $\chi_{-4}(p)p^h$, of complex absolute value $p^h$, and is pure of weight $2h$. The upper group is pure of weight $2(v+h)$. The degrees differ because $v\geq1$. This explicit calculation uses only classical etale trace and base-change theorems; A is used afterward for the global analytic zero locations.

The local zeta factor is
\[
 \frac{1}{(1-p^{v+h}T)(1-\chi_{-4}(p)p^hT)^N}.
\]
Multiplication over odd primes gives the stated arithmetic zeta identity in its half-plane of absolute convergence and then meromorphically. The omitted prime-two factor of the Tate term is exactly the factor in $\zeta^{(2)}$. Its extra zeros are explicit Euler-factor zeros, not nontrivial zeros of a Dirichlet L-function.

For any nonreal nontrivial zero $\rho$ of $L(s,\chi_{-4})$, write $\sigma=\Re\rho$ and use only $0<\sigma<1$. The Tate factor at $s=h+\rho$ is $\zeta^{(2)}(\rho-v)\ne0$. Indeed $\zeta(\rho-v)\ne0$ by the functional-equation argument above, and the modulus of $2^{-(\rho-v)}$ is $2^{v-\sigma}>1$, so the removed Euler factor is also nonzero. Hence
\[
 \operatorname{ord}_{s=h+\rho}\zeta_{X^-_\Phi}(s)
              =N\operatorname{ord}_{s=\rho}L(s,\chi_{-4}).
\]
This order identity also needs no A; A identifies the shifted critical line. No assumption that the chosen zero is simple is made. Locating its line does not evaluate its multiplicity in this constructed zeta function.

At the fixed prime $p=3$, where $\chi_{-4}(3)=-1$, one obtains
\[
       N=\frac{3^{v+h}-\#X^-_\Phi(\mathbb F_3)}{3^h}.
\]
The point-count function is in $\#\mathrm P$: guess the finitely many ternary coordinates using binary codes, reject unused codes, and check the one cubic equation. It is counting-hard by the displayed numerical reduction. Its parity equals $1+N\bmod2$, so even parity counting over this fixed field is $\oplus\mathrm P$-complete on the promised class. Rational-point existence is always true, because $N\leq2^v<3^v$ gives $\#X^-(\mathbb F_3)>0$. The hard Boolean question is whether the sign-Tate summand has nonzero rank, not whether the entire smooth scheme has a rational point.

E evaluates $N$ from the original CNF with its original $n$-variable bound and polynomial bit overhead for the displayed arithmetic. A makes the nontrivial zero-location statements unconditional under the user's designated input convention; it does not compute $N$. M is unused because the only nontrivial arithmetic character is the primitive quadratic Dirichlet character modulo four.

Finally consider effectivity. A single point count at $q=2$ recovers
\[
          N=\frac{\#X(\mathbb F_2)-2^{v+h}}{2^h}.
\]
Counting those points is in $\#\mathrm P$ by guessing the $v+h+1$ bit coordinates, and is $\#\mathrm P$-hard by this numerical reduction. Since $v\geq1$, its residue modulo $2^{h+1}$ is $2^h(N\bmod2)$, whereas every lower binary digit vanishes. At any odd prime power $q$, instead, $\#X(\mathbb F_q)\equiv1+N\pmod2$. In particular parity of rational-point counting is $\oplus\mathrm P$-complete already for these smooth geometrically integral sparse cubic hypersurfaces over the fixed field $\mathbb F_3$. The multiplicity $N=\dim H_c^{2h}$ is a $\#\mathrm P$ function on the encoded class; its nonvanishing is NP-complete and its parity is $\oplus\mathrm P$-complete. Rational-point existence for $X$ itself is always true, because $\#X\geq2^{v+h}$.

There is also an exact fixed-modulus transfer. Fix an integer $m_0\geq2$ and a prime $p$ not dividing $m_0$. Since $p^h$ is a unit modulo $m_0$,
\[
 N\bmod m_0=(p^h)^{-1}\bigl(\#X(\mathbb F_p)-p^{v+h}\bigr)\bmod m_0.
\]
Conversely the same point-count identity computes the point count modulo $m_0$ from $N\bmod m_0$. Thus the two modular counting functions are polynomial-time equivalent on the encoded class. This is stated for the function returning the count residue; no convention-dependent identification with a class called $\operatorname{Mod}_{m_0}\mathrm P$ is needed. If instead $p$ divides the modulus, division by $p^h$ is not invertible at that precision. In particular modulo $p^r$ with $r\leq h$ the whole count vanishes, whereas knowing the count modulo $p^{h+r}$ and subtracting the top term recovers $N\bmod p^r$ after exact division by $p^h$. The support of the whole point count is always nonzero; it does not supply the separate hard test $N>0$ for the lower cohomological multiplicity.

E computes $N$ through the source formula in $\operatorname{poly}_k(n+m)2^{O_k(n\log\log n/\sqrt{\log n})}$ time, with the sharper exponent when $m=O(n)$. Once $N$ is known, every displayed count and compact zeta-factor description is obtained by polynomial-bit arithmetic; a count at $q$ has $O((v+h)\log q+n)$ bits. Substituting the geometric coordinate count into E would be a weaker parameter statement. The elementary smooth construction is a classical quadric/Artin--Schreier form of the Cayley counting mechanism; the new conclusion here is its explicit arithmetic, pure-sign, and original-witness effectiveness gate, not a claim to have discovered the underlying point-count identity.''',
        'Complete integral smoothness, stratification, global cohomological projector, quadratic-character and arithmetic-zeta proofs; complete deduction-level self-reading passed; independent review pending.',
r'''The exact obstruction is now a multiplicity in a genuine pure Tate cohomology group of a smooth geometrically integral arithmetic scheme. Its degree is at most three, its defining polynomial is sparse, and its two global zeta descriptions use Riemann-zeta shifts and the quadratic Dirichlet factor covered by A. This proves that those geometric and analytic structures can coexist with a counting-complete multiplicity-extraction problem. It does not prove that polynomial-time extraction is impossible: such an algorithm would give $\mathrm{FP}=\#\mathrm P$ and $\mathrm{PH}=\mathrm P$, while parity extraction would give $\mathrm P=\oplus\mathrm P$ and $\mathrm{NP}=\mathrm{RP}$. M is unnecessary for these objects, but that fact does not remove the general Dedekind witness-field gate in Burgisser or Koiran. No GCT canonical-basis identification, positive polytope formula, or VP/VNP separation follows without an additional effective representation-theoretic construction.''',
r'''Let $f_1,\ldots,f_h\in\mathbb Z[x_1,\ldots,x_v]$ be the sparse quadratic Boolean and verifier equations in the proof, so that $v,h\geq1$, $f_1=x_1^2-x_1$, and $Y=V(f_1,\ldots,f_h)\simeq\coprod_N\operatorname{Spec}\mathbb Z$. Then the sparse cubic arithmetic hypersurface
\[
 X=V\left(t^2-t-\sum_{i=1}^h y_i f_i(x)\right)
             \subset\mathbb A^{v+h+1}_\mathbb Z
\]
is smooth of relative dimension $v+h$ with geometrically integral fibers. Its class is $[X]=\mathbb L^{v+h}+N\mathbb L^h$. For every field $K$ and every invertible prime $\ell$, its actual geometric compact-support groups, with their Galois actions, are
\[
 H_c^{2h}(X_{\overline K},\mathbb Q_\ell)=\mathbb Q_\ell(-h)^N,
 \qquad
 H_c^{2(v+h)}(X_{\overline K},\mathbb Q_\ell)=\mathbb Q_\ell(-v-h),
\]
and all other groups vanish. When $K$ is finite the displayed identifications are Frobenius-equivariant; they do not require finite $K$ to hold as Galois representations. Its arithmetic zeta is
$\zeta_X(s)=\zeta(s-v-h)\zeta(s-h)^N$.
These are separate proved assertions: affine-bundle stratification proves the scissor identity, while !-base change, the global trace and the involution $t\mapsto1-t$ prove the actual sheaf decomposition. Their exact interfaces are SGA4 XVII5.2.6/5.2.8 and XVIII2.8.1/2.9. The relative Jacobian identity proves smoothness over the full integer base, using SGA1 II4.10(iii)/4.12.

Over $B=\mathbb Z[1/2]$, replace the equation by $t^2+1=\sum_i y_i f_i(x)$. The resulting $X^-$ is also smooth with geometrically integral fibers. Its lower compact-support group is $(\chi_{-4}\otimes\mathbb Q_\ell(-h))^N$, its upper group is the same Tate line, and
\[
 \zeta_{X^-}(s)=\zeta^{(2)}(s-v-h)L(s-h,\chi_{-4})^N.
\]
Here the sign is the actual anti-invariant summand of the regular permutation representation $1\oplus\chi_{-4}$ of $\operatorname{Spec}\mathbb Z[i,1/2]\to\operatorname{Spec}B$. The first construction has a separate algebraic involution; the second realizes a quadratic Galois sign. Neither asserts an injective realization of the full split-zero semiring.

The proof constructs these data from a Boolean formula with $N$ satisfying assignments, with $v,h$ and the cubic description polynomial in that formula's size. Consequently extracting the lower cohomology multiplicity $N$ from this succinct geometric input is counting-complete, its parity is parity-counting-complete, and its nonvanishing is NP-complete. The corresponding shifted nonreal nontrivial zeta-zero orders are $N$ times a fixed nonzero analytic multiplicity; this identity is unconditional, while A locates the shifted critical lines. E evaluates $N$ with its original-witness bound. Thus actual purity, a concrete sign representation, smooth integral geometry and A-controlled analytic zero locations all coexist with this precise multiplicity-extraction problem. No unconditional time lower bound or effective GCT canonical-object identification is inferred.''',
        [E,A,sga1,basechange,trace,zeta,VV])

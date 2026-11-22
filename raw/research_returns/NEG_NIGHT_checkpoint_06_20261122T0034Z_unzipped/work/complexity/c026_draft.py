"""NN-C026: deterministic smooth projective Artin--Schreier curve gate."""

def append_c026(add,E,SGATRACE,VV):
    sga1={'source':'SGA1, ExposeII, Section4',
          'locator':'Theorem4.10(iii) and Corollary4.12, used on the two explicit affine curve charts',
          'url':'https://grothendiecksga.com/read/sga1/fr/II-4.html'}
    weil={'source':'Deligne, La conjecture de Weil I, PMIHES43(1974),273--307',
          'locator':'Trace equation1.5.1 p275; Theorem1.6 p276; Poincare duality Theorem2.3 and discussion2.4--2.5 p281',
          'url':'https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf',
          'access_note':'Exact statements and local discussion read in original NUMDAM text; full Weil theorem imported.'}
    cech={'source':'The Stacks Project, Cohomology of Schemes',
          'locator':'Lemma30.2.2, tag01XB (affine acyclicity); Lemma30.2.6, tag01XD (affine-cover Cech comparison)',
          'url':'https://stacks.math.columbia.edu/tag/01X8'}
    add('NN-C026','NEG_NIGHT-03',
        'Deterministic pure projective curves encode counting in the next binary digit',
r'''From a $k$-CNF $\Phi$ with $n\geq1$ variables and $m$ clauses one can deterministically construct, in polynomial time, an explicitly presented field $\mathbb F_q$ with $\log_2q=O(n)$ and a smooth geometrically integral projective curve $C_\Phi/\mathbb F_q$ such that
\[
               \#C_\Phi(\mathbb F_q)=1+2\#\operatorname{SAT}(\Phi).
\]
The curve is given by a polynomial-size arithmetic circuit for a monic odd-degree Artin--Schreier equation, together with its explicit weighted-projective completion. Its degree and genus are exponentially large and are encoded in binary. There is no promise of a polynomial-degree dense equation or a polynomial-genus curve.

The integer count, and the integer trace of the pure weight-one l-adic Frobenius representation, are therefore $\#\mathrm P$-hard from these succinct descriptions. Reduction of the count modulo four is parity-counting complete after subtracting one and dividing by two. Nevertheless every curve in this class has
\[
 Z(C_\Phi/\mathbb F_q,t)\equiv(1-t)^{-1}\pmod2,
\]
and its entire coherent Frobenius matrix is determined by a simple entry formula from its genus and field, independently of the satisfying-assignment count. This entry formula does not require listing an exponentially large matrix. Thus a genuine pure finite Weil object can be constructed deterministically here, while the next integer counting digit remains a separate effective gate.''',
        [{'source':'NN-C024','locator':'deterministic quadratic-tower finite-field construction'},
         {'source':'NN-C025','locator':'Boolean indicator and odd-degree Artin--Schreier irreducibility arguments'},
         dict(E,locator='Theorem1.1, evaluation through the original formula'),sga1,cech,SGATRACE,weil,VV],
r'''Let $b$ be the least power of two with $b\geq n$, and put $q=2^b$. Then $n\leq b<2n$ unless $n=1$, when $b=1$. The field tower in NN-C024 constructs $K=\mathbb F_q$, its arithmetic, and a basis $e_1,\ldots,e_b$ deterministically in polynomial time. If needed it also supplies a monic irreducible defining polynomial of degree $b$. The absolute trace $\operatorname{Tr}:K\to\mathbb F_2$ is nonzero, by the polynomial-degree proof in NN-C024. Its pairing $(a,x)\mapsto\operatorname{Tr}(ax)$ is nondegenerate: multiplication by any nonzero $a$ is a bijection, so this pairing cannot vanish for every $x$. Linear algebra over $\mathbb F_2$ therefore constructs the dual basis $\beta_i$ with
\[
 \operatorname{Tr}(\beta_i e_j)=\delta_{ij}.
\]
Define the linearized coordinate polynomials
\[
 L_i(X)=\operatorname{Tr}(\beta_i X)
       =\sum_{j=0}^{b-1}(\beta_iX)^{2^j}.
\]
They have degree at most $q/2$, polynomial-size repeated-squaring circuits, and for $x=\sum_j a_j e_j\in K$ satisfy $L_i(x)=a_i\in\mathbb F_2$.

Let $S_\Phi$ be the Boolean satisfaction polynomial in NN-C025. Use all $b$ coordinates to define
\[
 P(X)=1+S_\Phi(L_1(X),\ldots,L_n(X))
                 \prod_{i=n+1}^{b}(1+L_i(X)).
\]
For every $x\in K$, $P(x)$ is zero or one; it is zero exactly when its first $n$ coordinates satisfy $\Phi$ and all remaining coordinates are zero. Hence exactly $\#\operatorname{SAT}(\Phi)$ field elements have $P(x)=0$, with no padding multiplicity. Its formal degree is at most $(km+b)q/2$ and its circuit size is polynomial in $n+m$ for fixed $k$.

Find $\lambda\in K$ with $\operatorname{Tr}(\lambda)=1$ by testing the basis vectors. Choose
\[
 d=(km+b+1)q+1,
 \qquad
 f(X)=\lambda P(X)+(X^q+X)X^{d-q}.
\]
The integer $d$ is odd, its binary length is $O(n+\log(m+2))$, and it exceeds the degree bound for $P$. The polynomial $f$ is monic of degree exactly $d$. All powers shown can be computed by binary powering, so its circuit and coefficient presentation have polynomial bit length. On $K$ the extra term vanishes, and
\[
           \operatorname{Tr}(f(x))=P(x).
\]
The linear map $y\mapsto y^2+y$ on $K$ has kernel $\{0,1\}$ and image equal to the trace-zero hyperplane. The image is contained in that hyperplane by telescoping the trace, and both have dimension $b-1$. Therefore the affine equation $y^2+y=f(x)$ has exactly two $K$-solutions in $y$ when $P(x)=0$, and none otherwise. Its number of affine points is exactly $2\#\operatorname{SAT}(\Phi)$.

Write $d=2g+1$ and set $w=g+1$. Let $f^h(X,Z)=Z^d f(X/Z)$ be its degree-$d$ homogenization. It has a polynomial-size homogeneous arithmetic circuit: at each addition gate multiply the lower formal-degree input by the appropriate power of $Z$, and homogenize multiplication gates multiplicatively. Every needed exponent has $O(\log d)$ bits, so binary powering keeps the overhead polynomial. Define
\[
 C_\Phi=V\bigl(Y^2+YZ^w-Z f^h(X,Z)\bigr)
              \subset\mathbb P_K(1,w,1).
\]
All terms have weighted degree $2w=d+1$. Weighted projectivity does not require constructing an exponentially large ordinary embedding. For existence of such an embedding, the $w$th Veronese ring of $K[X,Y,Z]$ with weights $(1,w,1)$ is generated in degree one by $Y$ and $X^aZ^{w-a}$ for $0\leq a\leq w$. Its Proj is the same weighted projective space and is a projective closed subscheme of ordinary projective space. The latter embedding has exponentially many coordinates and is not part of the polynomial-size output.

The curve is covered by the two weight-one charts $Z\ne0$ and $X\ne0$: a hypothetical point with $X=Z=0$ would have $Y^2=0$ and hence all homogeneous coordinates zero. On $Z=1$ its equation is $y^2+y=f(x)$, whose $y$ derivative is one. On $X=1$, put $z=Z/X$ and $v=Y/X^w$; the equation is
\[
       v^2+v z^w=z^{d+1}f(1/z).
\]
At $z=0$ this has the unique point $v=0$. Its derivative in $z$ is one at that point, because $f$ is monic of degree $d$ and the right side starts with $z$. Thus the curve is smooth everywhere, over an algebraic closure as well, by the local Jacobian criterion. There is exactly one $K$-rational point at infinity. The ambient possible singular point $[0:1:0]$ is off the curve, so it supplies no exception to this chart argument.

The affine polynomial $y^2+y+f(x)$ is geometrically irreducible by the odd-degree proof in NN-C025. The smooth point at infinity lies on the closure of that affine curve: on its smooth one-dimensional chart, $z$ is a nonzero regular function and its zero set is just that point. Thus the projective curve is geometrically integral. This proves
\[
              \#C_\Phi(K)=1+2\#\operatorname{SAT}(\Phi)
\]
with no smoothness promise and no randomized parameter selection.

We compute the genus and the coherent Frobenius directly, so no unverified genus formula is needed. On the intersection of the two affine charts, the coordinate ring has the free $K[x,x^{-1}]$-basis $1,y$. Sections from the $Z=1$ chart have coefficients in $K[x]$ for both basis elements. Sections from the $X=1$ chart have constant coefficients in $K[x^{-1}]$ and $y$-coefficients in $x^{-w}K[x^{-1}]$, since $v=x^{-w}y$. The Cech quotient has no constant part, and its $y$-part has the basis
\[
       e_j=[x^{-j}y],\qquad 1\leq j\leq g.
\]
The same intersection calculation gives $H^0(C_\Phi,\mathcal O)=K$. The two affine opens and their affine intersection compute coherent cohomology by affine acyclicity and the Cech comparison (Stacks, Lemmas30.2.2 and30.2.6); hence $H^1$ has dimension $g=(d-1)/2$. In particular the genus is exponential in the original witness parameter, despite the short equation.

Absolute two-power Frobenius sends
\[
 e_j\longmapsto[x^{-2j}y^2]
       =[x^{-2j}y]+[x^{-2j}f(x)].
\]
The second summand is a Laurent polynomial in $x$ with no $y$ term, and is a Cech coboundary. The first is $e_{2j}$ if $2j\leq g$ and is a coboundary otherwise. Thus its semilinear matrix is the coefficient-independent shift
\[
 e_j\longmapsto
 \begin{cases}e_{2j},&2j\leq g,\\0,&2j>g.\end{cases}
\]
Iterating $b$ times gives the $K$-linear $q$-Frobenius shift $e_j\mapsto e_{qj}$, with out-of-range terms zero. It is nilpotent, with known rank $\lfloor g/q\rfloor$, independently of $f$ and $\Phi$. Applying SGA7 XXII3.1 to this proper curve gives the asserted complete zeta congruence $(1-t)^{-1}$, not just equality of first point-count residues. At fixed $n,m,k$, both the field and this entire based coherent Frobenius description are fixed, although satisfying-assignment counts can differ.

Finally let $\ell$ be any odd prime. The geometric l-adic cohomology is a genuine finite Weil representation. Its $H^1$ is pure of weight one by Deligne1.6. The connected curve has trace one on $H^0$ and trace $q$ on $H^2$, by the duality and degree discussion2.3--2.5. Deligne's trace formula1.5.1 gives the integer identity
\[
 \operatorname{Tr}(\operatorname{Frob}_q\mid H^1_{\rm et})
           =q+1-\#C_\Phi(K)
           =q-2\#\operatorname{SAT}(\Phi).
\]
Purity controls the eigenvalue magnitudes, but computing this integer trace, or its residue modulo four, recovers the count or its parity respectively. This is reduction of an integer trace, not reduction of an odd-adic field modulo four.

The divided count belongs to $\#\mathrm P$ directly on the whole succinct Artin--Schreier class: guess the $b$ coordinate bits of $x\in K$, evaluate the circuit for $f(x)$, and test $\operatorname{Tr}(f(x))=0$. For every monic odd-degree member, it equals $(\#C(K)-1)/2$. Our reduction proves its $\#\mathrm P$-completeness, and its parity is $\oplus\mathrm P$-complete. A deterministic polynomial-time mod-four count procedure would therefore give P=$\oplus$P and NP=RP; exact polynomial-time counting gives the stronger counting and Toda consequences recorded in NN-C006. E instead evaluates the constructed instances from the source $k$-CNF in its original $n$-variable time bound, with polynomial construction overhead. No efficient method for arbitrary high-degree circuit-presented curves is inferred.''',
        'Complete deterministic field, curve, Cech and counting proofs; complete deduction-level self-reading passed; independent review pending.',
r'''This supplies a deterministic smooth projective finite-field counting object, strengthening the existence side of the geometric gate. It does not derandomize the low-degree rank-one-coherent construction of NN-C024: the curve degree and coherent rank are exponential, and the parity information now occurs modulo four rather than modulo two. The representation is an actual pure l-adic representation attached to a smooth curve, but obtaining its integer trace from the succinct input remains counting-hard. All characteristic-two coherent Frobenius data above are already coefficient-independent, showing by explicit construction why that residue-level realization cannot determine the next integer digit. These are valid reduction barriers, not unconditional complexity separations or a GCT canonical-basis realization.''',
r'''For each fixed-width CNF $\Phi$ on $n\geq1$ variables, the proof explicitly constructs a finite field $K=\mathbb F_q$, $q=2^b$ with $b$ polynomial in the input size, and a monic odd-degree circuit-presented polynomial $f_\Phi(X)\in K[X]$. Put $d=\deg f_\Phi=2g+1$ and $w=g+1$. Its weighted projective completion
\[
 C_\Phi:\quad Y^2+YZ^w=Z^{d+1}f_\Phi(X/Z)
       \subset\mathbb P(1,w,1)
\]
is a smooth geometrically integral projective curve of genus $g$, with one rational point at infinity and
\[
 \#C_\Phi(K)=1+2\#\operatorname{SAT}(\Phi).
\]
The polynomial and the integers $d,g$ have polynomial-size circuit/binary descriptions; $d$ and $g$ themselves may be exponential. The two affine charts in the proof establish smoothness, completion and the Cech basis $e_j=[x^{-j}y]$, $1\leq j\leq g$, for $H^1(C_\Phi,\mathcal O)$. Absolute Frobenius sends $e_j$ to $e_{2j}$, with out-of-range indices zero; $q$-Frobenius sends it to $e_{qj}$. These coherent operators are nilpotent, independently of the encoded satisfying count.

For every prime $\ell\ne2$, the actual $H^1_{\rm et}(C_{\overline K},\mathbb Q_\ell)$ is pure of weight one and has Frobenius trace $q-2\#\operatorname{SAT}(\Phi)$. SGA7 XXII3.1 explains the common full zeta reduction modulo two; Deligne Weil I1.5.1,1.6 and2.3--2.5 supply the integral trace and purity interfaces. This proves a precise contrast between the characteristic-two coherent realization and the next binary digit of the integer etale trace. The divided count $(\#C(K)-1)/2$ is a counting-complete function on the succinct class, and its parity is parity-counting-complete. E evaluates the constructed instances from their original Boolean witnesses; it does not give a polynomial algorithm on arbitrary high-degree circuit-presented curves. No plethysm/Kronecker multiplicity identification or canonical-basis construction is claimed.''',
        [E,sga1,cech,SGATRACE,weil,VV])

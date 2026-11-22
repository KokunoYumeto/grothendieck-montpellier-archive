"""NN-C025: smooth integral affine counting gadgets, fixed degree presentation."""

def append_c025(add,E,SGAFINITE,ALGTRACE,VV):
    sga1={'source':'SGA1, ExposeII, Section4',
          'locator':'Theorem4.10(iii) and Corollary4.12, Jacobian smoothness criterion',
          'url':'https://grothendiecksga.com/read/sga1/fr/II-4.html'}
    trace={'source':'Deligne, La conjecture de Weil I, PMIHES43(1974),273--307',
           'locator':'Section1.3--1.5, especially compact-support trace equation1.5.1, printedpp274--275; contrast projective smooth Theorem1.6 p276',
           'url':'https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf'}
    add('NN-C025','NEG_NIGHT-03',
        'Geometrically integral smooth quadratic affine schemes retain exact counts above parity',
r'''A $k$-CNF $\Phi$ with $n\geq1$ variables and $m$ clauses has a deterministic polynomial-time construction of a geometrically integral smooth affine scheme $Y_\Phi/\mathbb F_2$ of dimension exactly $n$, together with a finite etale degree-two map
\[
             Y_\Phi\longrightarrow\mathbb A^n_{\mathbb F_2},
\]
such that
\[
        \#Y_\Phi(\mathbb F_2)=2\#\operatorname{SAT}(\Phi).
\]
It has a presentation by $s+1$ equations of degree at most two in $n+s+1$ coordinates, with $s=O(n+km+\log(m+2))$, and an explicitly displayed Jacobian minor identically equal to one. Thus rational-point existence is NP-complete on this promised class, exact point counting is $\#\mathrm P$-hard by one division by two, and point counting modulo four encodes parity-SAT. Point counting modulo two is identically zero on the entire class. E evaluates these counts through the original $n$ witnesses, with its exact Theorem1.1 bound; geometric auxiliary coordinates do not become independent Boolean witnesses.''',
        [{'source':'NN-C006 and prior CX-E07','locator':'finite Boolean solution schemes and the correct affine trace boundary; used only for contrast, not repeated'},
         dict(E,locator='Theorem1.1, original-variable exact k-CNF counter'),sga1,trace,VV],
r'''For a clause $C$, let $v_C(x)$ be the product of its false-literal indicators: a positive literal contributes $1+x_i$, and a negative literal contributes $x_i$. Put
\[
 S_\Phi(x)=\prod_C(1+v_C(x)),\qquad P_\Phi(x)=1+S_\Phi(x).
\]
On $\mathbb F_2^n$, $P_\Phi(x)=0$ exactly for satisfying assignments. The polynomial has degree at most $km$ and has a fan-in-two arithmetic circuit of $O(n+km)$ gates over $\mathbb F_2$. Empty products and empty clauses have their usual values, so tautological and contradictory inputs are included.

Choose the odd integer $d=2km+3$ and form
\[
        f_\Phi(x)=P_\Phi(x)+x_1^d+x_1.
\]
The added two terms vanish on every bit assignment. They ensure that the total degree is exactly the odd integer $d$, with leading monomial $x_1^d$. Binary powering takes $O(\log(d+1))$ additional gates. Define
\[
 Y_\Phi=\operatorname{Spec}
 \mathbb F_2[x_1,\ldots,x_n,t]/(t^2+t+f_\Phi(x)).
\]
The coordinate algebra is free of rank two over $\mathbb F_2[x]$, with basis $1,t$, because the equation is monic in $t$. Its relative derivative in $t$ is one. The hypersurface Jacobian criterion therefore makes its projection smooth of relative dimension zero, hence etale; alternatively it is finite flat and its relative differentials vanish. Composition with the smooth affine-space projection makes $Y_\Phi$ smooth of dimension $n$.

Geometric integrality is also explicit. Over any algebraic closure $\overline k$ of $\mathbb F_2$, a factorization of $T^2+T+f_\Phi$ over $\overline k(x)$ would give a rational function $h$ with $h^2+h=f_\Phi$. Write $h=A/B$ in coprime polynomials. The relation $A^2+AB=f_\Phi B^2$ forces every irreducible factor of $B$ to divide $A$, so $B$ is constant. Thus $h$ is a polynomial. If nonconstant, $h^2+h$ has even total degree $2\deg h$; if constant, it has degree zero or is zero. Neither possibility equals the odd-degree polynomial $f_\Phi$. The quadratic is therefore irreducible over the fraction field. Its monic quotient embeds in that field extension, so is a domain. This proves geometric integrality, not merely connectedness or reducedness.

For an $\mathbb F_2$ point, $t^2+t=0$ for both possible values of $t$. Each satisfying input $x$ therefore has exactly two points above it, and every nonsatisfying input has none. This proves the exact factor-two identity. No equations $x_i^2-x_i=0$ were imposed on the scheme: its geometric dimension is $n$, and its projection has two geometric points over every geometric base point. The vanishing or splitting of the rational fiber over a bit assignment is the arithmetic distinction being used.

To obtain the quadratic complete-intersection presentation, order the gates of the circuit computing $f_\Phi$ topologically. Introduce one coordinate $y_j$ for each gate, with equation
\[
 y_j-a-b=0,\quad y_j-ab=0,\quad\hbox{or}\quad y_j-a-1=0
\]
as appropriate, where $a,b$ are inputs or earlier gates. In characteristic two subtraction equals addition. Add the final equation $t^2+t+y_{\rm out}=0$. In the columns $(y_1,\ldots,y_s,t)$ and this order of equations, the Jacobian submatrix is lower triangular with diagonal entries all one: each gate equation has derivative one in its new gate, and the final equation has derivative one in $t$. Its determinant is identically one over the whole coordinate ring. Eliminating the gates, in order, recovers precisely the displayed Artin--Schreier coordinate algebra. The gate equations are a regular sequence by successive elimination, and the final monic polynomial is a nonzerodivisor. Thus this is a complete intersection, with constant-degree sparse equations and a proved global smoothness certificate. All coordinates and equations are written in polynomial time.

The exact-count complexity claim concerns this presentation. Guessing its polynomially many bit coordinates and checking its equations is a $\#\mathrm P$ computation. From its integer count one recovers $\#\operatorname{SAT}(\Phi)$ by division by two, so hardness is under a polynomial-time numerical reduction, not a falsely claimed parsimonious reduction for an always-even output. The divided count is itself a $\#\mathrm P$ function: guess just $x$ and check $P_\Phi(x)=0$. Its parity is exactly half of the point count modulo four. Consequently a deterministic polynomial-time mod-four algorithm gives P=$\oplus$P and, by Valiant--Vazirani, NP=RP. A polynomial-time existence algorithm would directly give P=NP. All these are conditional gates, not conclusions from smoothness.

For the upper bound, the constructor retains the source $k$-CNF presentation. Each assignment to its $n$ input bits determines every gate coordinate, and the extra coordinate $t$ contributes the known multiplicity two. E Theorem1.1 therefore gives
\[
 \operatorname{poly}_{k}(n+m)\,
 2^{O_k(n\log\log n/\sqrt{\log n})}
\]
bit operations and polynomial space, with exponent $O_{k,D}(n/\sqrt{\log n})$ when $m\leq Dn$. Applying a sparse-equation counter blindly to all $n+s+1$ coordinates would instead use that larger variable parameter. The smaller bound follows from the explicit functional graph and the original clause structure; it is not claimed for arbitrary succinct arithmetic circuits. Inputs with no variables have their constant count evaluated separately.''',
        'Complete affine construction, geometric-integrality and parameter proofs; complete deduction-level self-reading passed; independent review pending.',
r'''This strengthens the affine boundary of NN-C006: even geometric integrality, smoothness, an everywhere invertible quadratic Jacobian minor, and a finite etale cover of affine space do not remove exact counting hardness. It is different from the earlier zero-dimensional Boolean solution scheme, whose number of components already equals the count. Here the geometric object is integral of the original witness dimension, and every rational count is even. The precise information lost by reduction to characteristic two is one binary digit: modulo four retains it. The construction does not supply a smooth projective compactification in polynomial-size ordinary coordinates, nor permit the pure smooth-projective conclusion of Deligne1.6. It does not resolve P versus NP or VP versus VNP; E changes the available running time while the reductions remain valid.''',
r'''For every fixed-width CNF $\Phi$ on $n\geq1$ Boolean variables there is an explicitly constructed polynomial $f_\Phi\in\mathbb F_2[x_1,\ldots,x_n]$, represented by a polynomial-size arithmetic circuit and having odd degree, such that
\[
 U_\Phi=\operatorname{Spec}\mathbb F_2[x,t]/(t^2+t-f_\Phi(x))
\]
is smooth and geometrically integral of dimension $n$, finite etale of degree two over $\mathbb A^n$, and satisfies $\#U_\Phi(\mathbb F_2)=2\#\operatorname{SAT}(\Phi)$. Its graph presentation is a polynomial-size complete intersection of quadratic equations with a displayed triangular Jacobian minor equal to one. In particular its count is always zero modulo two, whereas its count modulo four is twice the Boolean parity. The proof above constructs $f_\Phi=1+S_\Phi+x_1^d+x_1$ with $d$ odd and larger than the verifier degree; the odd pole at infinity proves that $f_\Phi$ is not $h^2+h$ over the algebraic closure. Thus this geometric integrality claim has an explicit certificate argument.

The map is an Artin--Schreier torsor under the constant group $\mathbb Z/2\mathbb Z$. Over a satisfying rational input its fiber is $\operatorname{Spec}(\mathbb F_2\times\mathbb F_2)$; over a nonsatisfying one it is $\operatorname{Spec}\mathbb F_4$. These fibers have the same geometric degree, but respectively two and zero rational points. The multiplication trace of the unit in either rank-two algebra is zero in characteristic two; its algebraic trace locator is EGA IV4,18.2.1--18.2.2, printedp111. SGA4 XVII6.2.3 is the corresponding sheaf-theoretic finite trace, a distinct formalism. The whole affine point count is the alternating compact-support etale trace, by Deligne Weil I(1.5.1); it is not the trace on infinite-dimensional ordinary affine coherent $H^0$. Its integer residue modulo four is a separate operation, not a map from an odd-adic coefficient field to $\mathbb Z/4\mathbb Z$. Exact point counting on these circuit-presented smooth objects is counting-complete by division by two, while E evaluates the constructed objects through the original $n$-variable formula. No canonical GCT multiplicity or positive polytope formula is identified.''',
        [E,sga1,trace,SGAFINITE,ALGTRACE,VV])

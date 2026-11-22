"""NN-C033: the integral swap matrix and arbitrary-characteristic symbolic transfer."""

def append_c033(add,E,ALGTRACE):
    inputs=[
        dict(E,locator='Lemma3.2 complete integer-measurement-fiber proof; Lemma3.3 ring-valued Boolean differences; Proposition3.4 Taylor routine; Lemmas4.1--4.3 swap matrix and row support; equation swap-matrix-definition; Lemmas4.5--4.8 layout, height and parameters'),
        {'source':'NN-C016','locator':'bounded-arity universal partition polynomial, high-incidence branching and coefficient-independent circuit unrolling'},
        {'source':'NN-C029','locator':'ordinary integral ideal-multiplier correction, sparse-CNF first-violation identity, homogeneous components and affine coordinate maps'},
        ALGTRACE,
        {'source':'Elementary finite-field construction and Chinese remainder theorem','locator':'Complete existence, deterministic bounded-size construction and Hasse-jet argument proved below; no fast irreducible-polynomial oracle is assumed'}]
    add('NN-C033','NEG_NIGHT-04;NEG_NIGHT-06;NEG_NIGHT-10e',
        'Integral swap matrices remove the fixed-characteristic symbolic-circuit gate',
r'''Fix arity $w$ and factor density $C$. For every prime $p$ and every factor hypergraph on $n$ Boolean variables with $m\leq Cn$ factors of scope at most $w$, its universal partition polynomial
\[
 Z_H(y)=\sum_{x\in\{0,1\}^n}\prod_f y_{f,x|I_f}
                      \in\mathbb F_p[y]
\]
has a deterministically constructible, division-free arithmetic circuit over $\mathbb F_p$ of size
\[
 S(n)=\operatorname{poly}(n)\,
       2^{O_{w,C}(n(\log\log n)^2/\sqrt{\log n})}.
\]
Construction bit time is $S(n)\operatorname{poly}(\log p)$. The equality is equality of formal polynomials, with arbitrary independent weights, in every characteristic including two. The output circuit uses only prime-field constants. A small auxiliary field is used during construction and eliminated by explicit coordinate simulation.

Consequently all ordinary ideal-multiplier and affine-trivialization constructions of NN-C029 hold over every field of characteristic $p$, with the same variable parameter and subexponential bound. In particular, an unsatisfiable bounded-density local Boolean verifier has a Hilbert-like IPS certificate over $\mathbb F_2$ of that size, with ordinary polynomial identity $\sum_i a_i f_i=1$ and multiplier degrees at most $v$. For a fixed-width $O(n)$-clause CNF the original-$n$ specialization still needs no Boolean axioms. The output multipliers are exactly reductions of the explicitly specified integral first-violation and local-correction polynomials.

After polynomial overhead, the prime-field circuits can be made constant-free with syntactic formal degree at most $\max(m,1)$ for $Z_H$, at most $\max(v,1)$ for the multipliers, and at most $v+1$ for the IPS certificate. Here constant-free means that the only constant leaves are $0,1,-1$, and formal degree gives each constant or variable leaf degree one, addition the maximum, and multiplication the sum. This is a positive-characteristic statement. This prime-field argument itself does not construct integral-gate circuits over $\mathbb Z$; that remaining step is subsequently proved in NN-C034.''',
        inputs,
r'''We modify the actual common routine of E, rather than reducing its rational circuit modulo $p$. The key is an integral strengthening of its auxiliary swap matrix.

Use E's notation: commuting integral permutation involutions $\Pi_1,\ldots,\Pi_Q$, their product $V_0$, and
\[
 W_0=\frac12\sum_{s=1}^Q(I-\Pi_s),\qquad
 \mathcal I=\{A_0,\ldots,A_0+R-1\},\qquad
 M_0=(-1)^{A_0}V_0\sum_{j=0}^{R-1}
                      (-2)^j\binom{W_0-A_0I}{j}.
\]
Although this displayed construction uses rational matrices, $M_0$ is in fact integral. In the formal matrix power-series ring over $\mathbb Q$, one has
\begin{equation}\label{eq:C033-integral-generating}
 \sum_{j\geq0}(-2)^j\binom{W_0-A_0I}{j}U^j
       =(1-2U)^{-A_0}\prod_{s=1}^Q\bigl(I+U(\Pi_s-I)\bigr).
\end{equation}
To prove the identity, use the common rational eigenbasis in E Lemma4.1. If exactly $a$ involutions act by minus one, the right side acts by
$(1-2U)^{-A_0}(1-2U)^a=(1-2U)^{a-A_0}$, whose generalized binomial expansion is exactly the left side. Equality on this basis proves the matrix identity coefficient by coefficient. The scalar series $(1-2U)^{-A_0}$ has integral coefficients: for $A_0>0$ its coefficient of $U^j$ is $2^j\binom{A_0+j-1}{j}$; for $A_0=0$ the entire series is $1$. Every factor on the right is an integral matrix polynomial. Therefore each coefficient on the left is integral, and so is $M_0$.

This proof also gives a direct integral construction by truncating the product at degree $R-1$. It takes polynomially many operations in the auxiliary dimension $D$, $Q$ and $R$. Since $A_0,R\leq Q$, the coefficients have polynomial bit length, for example the norm bounds of E Lemma4.6 imply $O(Q\log(Q+2))$ bits for entries of $M_0$. The stronger conclusion is integrality, not a new asymptotic height assumption. The generating identity is proved over $\mathbb Q$ only to identify this particular integral matrix; after the integer coefficients have been formed, reduction or scalar extension is an ordinary ring homomorphism. No occurrence of $1/2$ or $1/j!$ is evaluated in characteristic two.

Keep the integer measurement matrix $C^{\mathcal B}$ of E Lemma4.1, the same incidence labels and copies, and the same integral matrices $C_{t,g}$. Two facts of E's construction remain available. First, $M_0[u,y]\ne0$ implies at most $R-1$ mismatches between $a_y(s)$ and $d_u(s)$, by Lemma4.2. Second,
\[
   C^{\mathcal B}\xi=0,\quad \xi\in\mathbb Z^{\mathcal B}
                  \quad\Longrightarrow\quad M_0\xi=\xi
                       \quad\hbox{in }\mathbb Z^{\mathcal B}.
\]
Indeed the hypothesis also holds over $\mathbb Q$, where Lemma4.1 proves the conclusion; integrality then makes it an exact integer equality. We do not claim that the reduction of $M_0$ fixes the entire kernel of the reduced matrix over $\mathbb F_p$. That stronger assertion is unnecessary and is not obtained by reducing a rational kernel calculation.

Choose an explicit extension field $L/\mathbb F_p$ containing at least $Q$ distinct nonzero elements, denoted $\alpha_1,\ldots,\alpha_Q$. If $p>Q$, take $L=\mathbb F_p$ and $\alpha_t=t$. If $p\leq Q$, let $e$ be least with $p^e>Q$. Then
\[
                 p^e\leq pQ\leq Q^2,\qquad e=O(\log(Q+1)).
\]
An explicit monic irreducible polynomial of degree $e$ can be found deterministically by enumerating the $p^e$ candidates and testing division by every monic polynomial of positive degree at most $\lfloor e/2\rfloor$. A reducible polynomial has a proper factor of degree at most half its degree, so this test is exact, and the total enumeration has cost polynomial in $Q$ and $\log p$.

For completeness, existence does not require a randomized construction theorem. In an algebraic closure the roots of $T^{p^e}-T$ are distinct and closed under the field operations, so they form a field with $p^e$ elements. Every element of smaller degree has degree a proper divisor of $e$, by the period of Frobenius, and hence belongs to the union of the root sets of $T^{p^d}-T$ for proper divisors $d$ of $e$. For $e\geq2$, the size of that union is at most
$\sum_{d=1}^{\lfloor e/2\rfloor}p^d<p^e$. Some element therefore has degree $e$, and its minimal polynomial is an irreducible candidate. The case $e=1$ is immediate. Represent $L$ by the resulting quotient with basis $1,\theta,\ldots,\theta^{e-1}$, and take any $Q$ distinct nonzero coordinate vectors. All arithmetic in this field has bit cost polynomial in $Q$ and $\log p$.

For a pair $(u,y)$ with $M_0[u,y]\ne0$, write
$E_{u,y}=\{s:a_y(s)\ne d_u(s)\}$ and replace E's scalar polynomial by
\[
       \varphi_{u,y}(T)=\prod_{s\in E_{u,y}}(1-T/\alpha_s).
\]
Form the new rows over $L$ by
\[
 \vec P_u(T)=\delta_u(I-M_0)
          +\sum_yM_0[u,y]\varphi_{u,y}(T)\delta_y.
\]
Integer matrix entries in this formula are reduced into $L$. The rows have degree at most $R-1$ and satisfy $\vec P_u(0)=\delta_u$. At $T=\alpha_t$, every term with $a_y(t)\ne d_u(t)$ vanishes. All denominators here are nonzero field elements chosen explicitly.

The separation property needed by the routine still holds on its actual enumeration domain. Suppose two Boolean assignments differ only inside an off-target group and have equal \emph{integer} measurements $C_{t,g}x_g$. Their difference, copied into each auxiliary array, is an integer vector in the kernel of $C^{\mathcal B}$ and supported in that off-target group. The term $I-M_0$ annihilates this integer vector by the exact integer equality above. Every surviving $\varphi$ term uses the target group and hence also annihilates the difference. Reducing these equalities into $L$ proves that $\langle\vec P_{f,v}(\alpha_t),x\rangle$ is constant on each such integer measurement fiber. The same reasoning applies over every commutative $L$-algebra. It uses an equality of integer vectors before scalar extension, not an assumed saturation of a reduced kernel.

We spell out why this weaker fiber statement suffices for the entire symbolic routine. E Lemma3.2 enumerates tuples of integer measurement values in $[-D,D]$, scans Boolean assignments to find one representative in each nonempty local fiber, and then scans the same fibers again. To evaluate a factor assigned to group $g$, it combines the actual group assignment with fixed representatives in all other groups. Every intermediate assembled vector is Boolean. Successively replacing an off-target group's representative by another assignment in the same integer fiber leaves that factor unchanged by the property just proved. Distributivity then gives the exact product of group sums and sum over measurement tuples. The proof never needs invariance on arbitrary vectors over $L$, and it never replaces integer measurement equality by equality modulo $p$. Thus its vector count, storage bound and coefficient-independent control remain exactly those in Lemma3.2.

Let $\mathcal A=L[y]$, with the factor weights retained as formal independent indeterminates, and use the standard multilinear factor interpolation
\[
 \Phi_f(z)=\sum_{a\in\{0,1\}^{I_f}}y_{f,a}
            \prod_{i:a_i=1}z_i\prod_{i:a_i=0}(1-z_i).
\]
Its value at a Boolean local input is the corresponding indeterminate as a formal polynomial, in every characteristic. Define the polynomial $H(T)$ using the new replacement rows as in E Section3.1. Then $H(0)=Z_H(y)$ exactly in $\mathcal A$, and $\deg_T H\leq dR$ with $d\leq wm=O(n)$.

Set $q=\lfloor dR/Q\rfloor$ and $J=q+1$. At node $\alpha_t$ write
$\Delta P(z)=P(\alpha_t+z)-P(\alpha_t)$. Its entries are divisible by $z$. Introduce the independent Boolean-substitution indeterminates $X_i$ used in E's auxiliary polynomial $\mathcal G_x(X,z)$. Every occurrence of $X_i$ carries a factor $z$, so $\deg_X[z^j]\mathcal G_x\leq j$. This is a polynomial degree statement over $\mathcal A$ and has no characteristic restriction.

E Lemma3.3 is explicitly an identity over every commutative ring. Its proof replaces positive powers of each $X_i$ by $X_i$ and performs subset Mobius inversion with coefficients $1,-1$. Apply it coefficientwise to $[z^j]\mathcal G_x$, for $j<J$. For each fixed substitution $X=\mathbf1_U$, the corrections involving $\Delta P$ are independent of the enumerated Boolean assignment $x$. Hence the integer-fiber separation just proved computes the corresponding restricted sum with $x_i=1$ for $i\in E$. The resulting identity is the exact Hasse jet
\[
                      H(\alpha_t+z)\bmod z^J
                         \quad\hbox{in }\mathcal A[z]/(z^J).
\]
All equalities are formal polynomial identities in the weight indeterminates $y$. We have not compared numerical evaluations at finitely many $y$ values.

Finally the ideals $(T-\alpha_t)^J$ are pairwise comaximal in $L[T]$. Their differences are nonzero units. The Chinese remainder theorem gives an isomorphism
\[
 L[T]\big/\!\prod_{t=1}^Q(T-\alpha_t)^J
              \longrightarrow\prod_{t=1}^Q L[z]/(z^J),
       \qquad H\longmapsto(H(\alpha_t+z))_t.
\]
Both sides have dimension $QJ$, with the monomial and jet bases. Its invertible matrix has entries
$\binom uj\alpha_t^{u-j}$, using integer binomial coefficients reduced into $L$. This is Hasse interpolation: it divides by no $j!$ and requires no inequality $J<p$. Compute its inverse over the explicit finite field and use only its final entries as scalar constants. Tensoring this matrix identity with the coefficient algebra $\mathcal A$ recovers $H$ and $H(0)$ formally. Any internal field inversions used to find the constants disappear from the resulting arithmetic circuit. Since $QJ>dR$, the recovered polynomial is the original $H$.

The number of enumerated vectors is the same as E Proposition3.4:
\[
 2Qr\left(\sum_{s=0}^{\min(q,n)}2^s\binom ns\right)
                       (2D+1)^{2\tau n}2^{2n/r}.
\]
The combinatorial layouts and their integer measurements are unchanged. For bounded arity and linear total incidence, branch on at most $n/\sqrt{\log_2n}$ variables of incidence above
$\max(1,\lceil M_{\rm inc}/n\rceil)\lceil\sqrt{\log_2n}\rceil$, retaining declared scopes. On each branch E Lemmas4.7--4.8 apply with the same $Q,R,r,D,\tau$ and the same three exponential costs. The field and matrix computations introduce polynomial overhead only. Bounded exceptional input sizes are handled by direct expansion. Summing all branches yields $S(n)$ operations in the coefficient algebra, with construction bit cost $S(n)\operatorname{poly}(\log p)$.

Unroll these operations into a shared division-free circuit over $L$. Every branch, representative and layout choice depends only on discrete scopes, Boolean bits and integer measurement data. No test of whether a symbolic polynomial is zero occurs. Replace each $L$-valued gate by its $e$ coordinates over $\mathbb F_p$. Addition is componentwise and multiplication uses the explicit structure constants for the quotient basis, at polynomial overhead in $e$. A weight input $y$ is represented by $(y,0,\ldots,0)$. The final computed element is precisely the universal partition polynomial, whose coefficients already lie in $\mathbb F_p$. Its coordinate of one is therefore exactly $Z_H(y)$ and every other coordinate is the zero formal polynomial. Taking that coordinate supplies the required prime-field circuit; no identity test is needed to know the other coordinates vanish. This also proves agreement with the reduction of the original integral universal partition polynomial, not merely agreement as a function on a finite field.

NN-C029's preliminary first-violation multipliers are constant-size substitutions into these universal partition polynomials. Its at-most-eight local specializations and integral monomial division establish the ordinary identity over $\mathbb Z$; performing those same constructions over $\mathbb F_p$ reduces each polynomial identity coefficientwise. Consequently the final circuits compute the reductions of the specified integral multipliers and satisfy $\sum_i a_if_i=1$ as a formal identity. The stronger sparse-CNF identity and affine coordinate formulas transfer for the same reason. For example the mutually inverse maps remain
\[
 z_i=y_i+a_i(x)(2t-t^2),\qquad
 t=\sum_i f_i(x)z_i,\qquad
 y_i=z_i+a_i(x)(t^2-2t),
\]
with coefficients reduced in the field. In characteristic two the terms containing $2t$ vanish, and the directly verified identities still hold. Original-$n$ versus $n+s$ verifier parameters are exactly those already proved in NN-C029.

To obtain the constant-free formal-degree claim, apply homogeneous-component truncation through the known output degree $D_0$ in the polynomial indeterminates. It has polynomial overhead and computes the same output because no division by an indeterminate is present. Every degree-zero component is a prime-field constant and can be evaluated explicitly. A multiplication with such a scalar can be implemented by binary doubling and addition of its other input, using $O(\log p)$ addition gates; this does not increase formal degree. Each nonconstant multiplication combines positive-degree components, so induction bounds its formal degree by the sum of their variable degrees. Constant outputs themselves can be built from one by additions, with formal degree one. Replacing all scalar multiplications in this manner, and using constant leaves only $0,1,-1$, gives formal degree at most $\max(D_0,1)$ and polynomial overhead in $\log p$. Take $D_0=m$ for the universal partition polynomial, $D_0=v$ for multipliers, and $D_0=v+1$ for the Hilbert-like IPS polynomial. This argument uses reduction in the prime field; it does not convert the original rational circuits into integral-gate circuits over $\mathbb Z$.''',
        'Complete integral-matrix, modified finite-characteristic routine, formal-output descent and ideal-certificate proofs; independent review pending.',
r'''This closes the fixed-small-characteristic gap left by NN-C016 and the large-characteristic-only addendum of NN-C029. It gives formal symbolic partition circuits, ordinary ideal certificates and empty-case affine trivializations over fixed F2 at E's subexponential source-parameter bound. The proof does not merely reduce rational interpolation constants modulo two: it changes the nodes and uses integral Boolean measurement fibers. Constant-free prime-field circuits of polynomial formal degree follow after homogeneous-component processing. NN-C034 subsequently supplies integral-gate circuits over Z as well. Polynomial-size IPS certificates, efficient PIT verification and a VP/VNP collapse remain unproved. Exponential monomial-PC lower bounds are still compatible with the resulting shared circuits.''',
r'''For every prime $p$, let $B=\mathbb F_p[y]$ and let
\[
 \mathscr A=B[x_1,\ldots,x_n]/(x_i^2-x_i),\qquad
       a=\prod_f\Phi_f(x).
\]
This is a finite free split algebra of rank $2^n$, with the Boolean orthogonal idempotents as a basis. Its multiplication trace $\operatorname{Tr}_{\mathscr A/B}(a)$ is the universal partition polynomial, because multiplication is diagonal in that basis. The theorem constructs a prime-field arithmetic circuit for this relative trace in size $S(n)$, naturally under arbitrary substitutions of the parameters. The auxiliary scalar extension is finite separable and free; the proof computes the trace after that extension and recovers its original scalar coordinate by an explicit basis. This descent is an identity of regular functions on the full parameter scheme, not pointwise interpolation on its rational points.

For an unsatisfiable local verifier, the same construction supplies an ordinary ideal identity in $\mathbb F_p[x]$ and polynomial maps identifying its associated smooth cubic with affine space over every extension field of characteristic $p$. The maps and inverses are explicitly represented by subexponential circuits and have the degree bounds from NN-C029. Thus the characteristic-two geometric trivialization gate is also closed for this family. The exact classical finite-locally-free trace locator is EGA IV4,18.2.1--18.2.2, printed p111, especially base-change equation18.2.1.2. The integral-matrix identity, change of interpolation nodes, integer-fiber separation and coordinate descent are proved here; no additional Grothendieck archive locator is asserted. This family-level effective trace theorem supplies neither a canonical GCT multiplicity realization nor general polynomial-time geometric recognition.''',
        inputs)

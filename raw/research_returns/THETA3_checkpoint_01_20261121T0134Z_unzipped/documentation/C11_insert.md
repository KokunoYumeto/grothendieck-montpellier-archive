## 4A. A precise local bridge to the exponent in Alpöge step2

### THETA3-C11. Height-two formal derivatives: the exact slope and infinitely many sharp values

**Statement.** Let p be an odd prime, Q=p², and let pi be an element of C_p with normalized valuation v_p(pi)=1. Put

    ell(T) = sum_{r>=0} T^{Q^r}/pi^r,
    E(Z) = ell^{-1}(Z),
    D = ell'(T)^{-1} d/dT.

For every f(T) in O_{C_p}[[T]] and every integer a>=1,

    v_p(D^a f(0)) >= v_p(a!) − (a−1)/(p²−1)
                  = ap/(p²−1) + 1/(p²−1) − s_p(a)/(p−1),

where s_p(a) is the sum of the base-p digits of a, and v_p(0)=+infinity. Moreover, D^p is zero after reduction modulo p. The bound is sharp infinitely often: for f(T)=T and a=Q^r (r>=0), equality holds and

    v_p(D^{Q^r} T(0)) = (Q^r−1)p/(p²−1).

In particular the coefficient p/(p²−1)=1/p+1/p³+... in Alpöge step2 arises from a precise local formal-group estimate with an explicit logarithmic digit-sum error. This statement does not assert that an arbitrary analytic theta section, in its stated analytic normalization, has an integral coefficient function in this formal frame.

**Proof of the lower bound.** Choose beta in C_p with beta^{Q−1}=pi. Then v_p(beta)=1/(Q−1). The scaled logarithm

    L(T)=ell(beta T)/beta
        =sum_{r>=0} pi^{(Q^r−1)/(Q−1)−r} T^{Q^r}

has integral coefficients and linear coefficient1: its r-th exponent is

    (Q^r−1)/(Q−1)−r = 1+Q+...+Q^{r−1}−r >=0

for r>=1. Recursive inversion of a formal power series whose linear coefficient is1 works over any commutative ring. Its inverse U(T)=E(beta T)/beta therefore belongs to T O_{C_p}[[T]] and has linear coefficient1. Since f is integral,

    f(E(beta T))−f(0)=f(beta U(T))−f(0) belongs to beta T O_{C_p}[[T]].

The logarithmic coordinate Z=ell(T) rectifies the derivation: the formal chain rule gives d(f(E(Z)))/dZ=(Df)(E(Z)). Hence

    f(E(Z))=sum_{a>=0} D^a f(0) Z^a/a!.

The coefficient of T^a in f(E(beta T)) has valuation at least v_p(beta). It is beta^a D^a f(0)/a!, so

    v_p(D^a f(0)) >= v_p(a!)−(a−1)/(Q−1).

Legendre's formula v_p(a!)=(a−s_p(a))/(p−1) gives the displayed expression. Since s_p(a)<=(p−1)(1+floor(log_p a)), the error is explicitly O(log a), with no unspecified theta- or curve-dependent constant in this formal calculation.

**Proof of nilpotence modulo p.** Since Q=p² and v_p(pi)=1,

    ell'(T)=sum_{r>=0} (Q/pi)^r T^{Q^r−1}

is an integral unit congruent to1 modulo p. Thus D reduces to d/dT on (O_{C_p}/p)[[T]]. The p-th iterate of d/dT is zero: on every monomial, the product of p consecutive integer factors is divisible by p. This remains true when the coefficient ring is nonreduced. Hence D^p is zero modulo p.

**Proof of sharpness.** For r=1 the exponent in L is0; for every r>=2 it is positive. Modulo the maximal ideal of O_{C_p}, therefore, L(T) reduces to T+T^Q. In characteristic p the formal series

    V(T)=sum_{j>=0} (−1)^j T^{Q^j}

satisfies V(T)+V(T)^Q=T, so it is the inverse of T+T^Q. Formal inversion commutes with reduction because it uses only integral coefficient recursion. Thus the coefficient of T^{Q^r} in U(T) is a unit. Since E(Z)=beta U(Z/beta), its Z^{Q^r}-coefficient has valuation exactly −(Q^r−1)/(Q−1). Apply D^a T(0)=a![Z^a]E(Z). For a=Q^r, s_p(a)=1, yielding

    v_p(D^a T(0))=(a−1)/(p−1)−(a−1)/(p²−1)
                  =(a−1)p/(p²−1).

This proves both sharpness and the equality claimed. ∎

**Coordinates and the CM elliptic application.** The displayed logarithm is a permitted coordinate for a height-two Lubin–Tate formal group with uniformizer pi. Bannai–Kobayashi, *Integral structures on p-adic Fourier theory*, Ann. Inst. Fourier66(2016), pp531–532, Proposition3.5 and its proof, first use exactly sum T^{q^r}/pi^r and then pass to general integral parameters. An integral change of parameter with unit linear coefficient preserves integrality of f; the corresponding normalized invariant derivations differ by a constant unit under the formal-group isomorphism, so valuations of iterates agree. In their CM elliptic application, §5 pp543–544, p is odd inert and the elliptic curve has good supersingular reduction, and its formal group is the height-two Lubin–Tate group attached to pi=−epsilon p. The proof just given works with that pi, without assuming epsilon=−1.

There are actual nontrivial functions satisfying the integrality hypothesis in this primary source. On p546, with b prime to p, they set

    wp_b(z)=wp(z)−b²wp(bz),
    phi(t)=wp_b(lambda(t)) in O_K[[t]],

and similarly an integral modified zeta function. Their Proposition5.5, pp546–547, identifies the invariant derivatives and Fourier moments with the modified Bernoulli–Hurwitz values; Theorem5.1 on p544 (Katz's theorem, re-proved in their §5) gives the stronger floor(np/(p²−1)) divisibility after the stated modification. These are existing CM elliptic applications of the same local slope, not a claim that C11 newly proves Katz's theorem or all raw theta-section integrality.

The coefficient also equals the normalized valuation of a Lubin–Tate period: Schneider–Teitelbaum, *p-adic Fourier theory*, Lemma3.4(b), states v_p(Omega_LT)=1/(p−1)−1/(e(q−1)); putting e=1 and q=p² gives p/(p²−1). Their Appendix supplies its period calculation. This p-adic Omega_LT must not be confused with the complex period Omega_C in Alpöge's normalization.

**Exact remaining frame gate.** A theta function is a section of a line bundle. Extending that line bundle as an invertible sheaf over the formal integral neighborhood gives some integral frame, but the invariant derivative of a section depends on the chosen frame or connection. The required comparison is an equality between the analytically normalized derivatives D^a theta(0)/Omega_C^a and the iterates D_G^a f(0) of an integral coefficient function in a specified compatible frame. Existence of an arbitrary integral trivialization does not establish this equality. A horizontal or cubical analytic frame need not be integral.

Here is an explicit jet obstruction. In the formal characteristic-zero germ C_p[[T]], take the trivial line bundle with section1 and frame e. For fixed a>=1 and any integer M>0, replace the frame by e'=(1+p^{−M}T^a)e. Both frames agree at the origin; the section has the same empty divisor, but its new coefficient is f'=(1+p^{−M}T^a)^{−1}, for which D^a f'(0)=−a!p^{−M}. Its valuation can be arbitrarily negative. The new frame is a generic formal frame, not an integral frame; precisely that distinction defeats an inference from divisor data or the value at the origin alone. This is a formal-germ example and makes no assertion that the frame is invertible on the whole rigid open unit disc.

Even an integral Cartier divisor does not determine exact derivative values. Fix2<=a<Q. The integral functions f_N(T)=T(1+p^N T^{a−1}) all define the same Cartier divisor(T), have the same first derivative at0, but D^a f_N(0)=a!p^N, because E(Z)=Z+O(Z^Q). Their a-th derivative valuations vary with N. The universal lower bound C11 still applies; the example rules out recovering precise higher jets from the divisor alone.

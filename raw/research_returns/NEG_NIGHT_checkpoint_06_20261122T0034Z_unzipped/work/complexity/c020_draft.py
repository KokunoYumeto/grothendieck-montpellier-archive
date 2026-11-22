"""NN-C020: explicit coefficient algebras remove the GRH gate for bounded outputs."""

def append_c020(add,ALGTRACE,BUR):
    add('NN-C020','NEG_NIGHT-09',
        'Unconditional Boolean simulation from a small explicit coefficient algebra',
r'''Let $C_n$ be a division-free arithmetic circuit of polynomial size over $B_n\otimes_{\mathbb Z}\mathbb Q$, where $B_n$ is a commutative finite free $\mathbb Z$-algebra supplied by a basis $e_0=1,e_1,\ldots,e_{r(n)-1}$ of polynomial rank and polynomial-bit integer multiplication constants. Suppose every circuit constant is supplied by polynomial-bit rational coordinates in this basis, and the total circuit and algebra description has polynomial size. Assume that on every Boolean input the output is $g_n(x)e_0$, where $g_n(x)$ is an integer in $[0,2^{w(n)})$ for a polynomial $w$. Then $g\in\mathrm{FP}/\mathrm{poly}$, without GRH and without a formal-degree bound. If these descriptions and the output bound are constructible in polynomial time, then $g\in\mathrm{FP}$.

In particular, the conclusion applies when constants lie in a number field of polynomial degree supplied by an integral primitive element with polynomial-bit monic minimal polynomial and polynomial-bit rational power-basis coordinates. A collapse giving such circuits for all $\#\mathrm P$ counting families implies $\#\mathrm P\subseteq\mathrm{FP}/\mathrm{poly}$ unconditionally.''',
        [{'source':'Elementary quotient-algebra simulation','locator':'complete proof below'},
         {'source':'NN-C015','locator':'constant-free counting-family construction; coefficient-height proof refined here'},
         BUR,ALGTRACE],
r'''Write each constant as $d_g^{-1}\sum_j a_{g,j}e_j$, with $d_g$ a positive integer. Put $D=\prod_g d_g$. This product has polynomial bit length, because the total constant description does. Every circuit value lies in the localization $B_n[D^{-1}]$. Choose the integer modulus
\[
 M=D\,2^{w(n)+1}+1.
\]
Its bit length is polynomial, it exceeds $2^{w(n)}$, and it is coprime to every $d_g$. In fact, an explicit inverse of $d_g$ modulo $M$ is
\[
 -\frac{D}{d_g}\,2^{w(n)+1}\pmod M,
\]
because multiplying this expression by $d_g$ gives $1-M$.

Therefore the canonical map $B_n\to B_n\otimes_{\mathbb Z}\mathbb Z/M\mathbb Z$ extends to a ring homomorphism
\[
 B_n[D^{-1}]\longrightarrow
 B_n\otimes_{\mathbb Z}\mathbb Z/M\mathbb Z.
\]
Evaluate the full circuit in this quotient algebra. Each stored value has $r(n)$ coordinates modulo $M$. Addition is coordinatewise and multiplication uses the supplied table; a naive multiplication needs only $O(r(n)^3)$ modular scalar operations. All integers have $O(\log M)$ bits. Consequently the whole evaluation uses polynomially many bit operations and polynomial space, independent of the magnitude of unreduced intermediate characteristic-zero values. Exponentially large formal degrees cause no difficulty: repeated squaring remains a sequence of the originally supplied polynomially many modular gates.

By the homomorphism property, the final vector is $(g_n(x)\bmod M,0,\ldots,0)$. The algebra remains free with the supplied basis after base change, so this coordinate statement is literal, not merely equality in an unspecified residue field. Since $0\leq g_n(x)<2^{w(n)}<M$, the least nonnegative representative of the first coordinate is the exact desired integer. This proves the simulation. Polynomial descriptions serve as advice in the nonuniform case; in the uniform case they are constructed before evaluation in polynomial time.

For the number-field specialization, let $f_n\in\mathbb Z[T]$ be the supplied monic minimal polynomial of the integral primitive element $\alpha_n$. Then $B_n=\mathbb Z[\alpha_n]\cong\mathbb Z[T]/(f_n)$ is free in the power basis of size $\deg f_n$. Reducing products of two basis powers by the monic relation constructs an integral multiplication table of polynomial bit length: at most $O(\deg f_n)$ successive reductions are needed, and each can increase the coefficient bit bound by at most a polynomial in the degree and the bit height of $f_n$. The given rational constant coordinates lie in $B_n[D^{-1}]$. The general argument applies even if $f_n$ becomes reducible or inseparable modulo $M$; neither a field quotient nor a root modulo $M$ is required.

Applying the simulation to the VNP counting polynomials constructed in NN-C015 proves its $\#\mathrm P$ consequence directly for this larger effective coefficient model. In particular, constant-free circuits use $B_n=\mathbb Z$ and $D=1$. Their formal-degree restriction is part of the definition of the usual constant-free Valiant classes and was needed for NN-C015's characteristic-zero height proof, but it is not needed for this modular Boolean simulation of promised bounded integer outputs. The proof also applies to explicitly supplied rational constants of polynomial total bit height.

This does not replace Burgisser's general complex-constant theorem. An arbitrary polynomial-size circuit over $\mathbb C$ need not come with a polynomial-rank finite algebra, polynomial-bit constants, or an effectively small algebraic replacement. Burgisser's constant-replacement system constructs bounded algebraic witness fields of possibly much larger degree, and its small residue-degree-one prime argument addresses that different presentation problem. The present proof uses the entire quotient algebra in polynomial rank and thus has no corresponding prime-splitting requirement.''',
        'Complete model refinement proved; complete self proof-check passed; independent review pending.',
r'''The analytic transfer gate is now more precisely located: polynomial rank and an explicit polynomial-bit coefficient presentation suffice, with composite-modulus arithmetic and no RH input. The contrapositive transfers Boolean counting lower bounds to this restricted but broad arithmetic model unconditionally. It does not transfer ordinary $\mathrm P\ne\mathrm{NP}$ to $\mathrm{VP}_{\mathbb C}\ne\mathrm{VNP}_{\mathbb C}$, and does not give a converse to Burgisser. Arbitrary complex constants, large algebraic degree, absent presentations, and unrestricted division gates remain outside the theorem.''',
r'''The coefficient object is a finite locally free affine scheme $\operatorname{Spec}B_n\to\operatorname{Spec}\mathbb Z$ with an explicit polynomial-rank trivialization of its pushforward algebra. The algorithm performs base change to $\operatorname{Spec}(\mathbb Z/M\mathbb Z)$ and evaluates in the full fiber algebra, including all of its components and nilpotents. It does not seek a rational point of that fiber. The scalar-output condition makes the resulting section descend to the base ring, where the magnitude bound identifies its unique integer lift. EGA IV4, printed p.111,18.2.1--18.2.2 gives the finite-algebra trace dictionary and base-change formula; the computational proof itself is the explicit multiplication table above. A weight or purity assertion without this small presentation does not supply the simulation, and no GCT orbit-closure obstruction is constructed.''',
        [ALGTRACE,BUR])

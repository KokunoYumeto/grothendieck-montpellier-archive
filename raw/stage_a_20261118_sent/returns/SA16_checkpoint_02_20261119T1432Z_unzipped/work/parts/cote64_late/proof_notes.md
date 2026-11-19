# Independent checks for cote 64, scans 78–157

Run: SA16-2026-11-19-cote64-late. Actor: GPT-6 Astra Pro; effort inherited/unspecified. Date: 2026-11-19. These are this run’s reconstructions. They are neither changes to the diplomatic transcription nor claims that the author supplied the missing arguments. Source statements used are identified by bibliography keys. Exact executable calculations and their output are in `code/recompute.py`, `outputs/recompute.txt`, and `outputs/computation_records.json`.

## 1. Torsors, twists, and pinning scope

**C-SA16-502–515; SA16-502–516.** If a μ4-torsor has associated scalar line N, its square has the associated μ2-line N². Thus `(M⊗N)²=M²⊗N²`. This proves `(M^sharp)²=(M²)^b`, rather than the literal `(M^sharp)²=M^b`. Taking the torsor trivial and M=O(1) on P1 over C satisfies every module/base hypothesis and gives degrees two and one in the latter identity. The specialization to O(2) on scan 81 already uses the correct rule.

Let L have a chosen square root `(T0,β0)`. For another root `(T,β)`, the sheaf of square-compatible isomorphisms T0→T is a μ2-torsor. Locally trivialize both lines; its equation is z²=u for a unit u. With 2 invertible it is étale and locally nonempty. Conversely a μ2-torsor twists T0, and the square descends because the character squares to one. Evaluation identifies the two composites with the identity. This proves the root/torsor equivalence; it does not by itself identify Grothendieck’s specific tangent-square line with an elliptic moduli functor.

A further team proof now closes the geometric elliptic/root-line equivalence (C-SA16-512), separately from the symmetric pinning normalization. It was read and checked in early64 `proof_supplement.md`, §9. Send a four-branch elliptic double cover to its tangent at the distinguished ramification section, with the norm-induced square isomorphism and the explicitly fixed norm/jet sign. Étale locally order J and choose a Legendre model. The double covers with fixed branch data are then its μ2 twists; the tangent-square roots are twists by the same μ2. The nontrivial deck transformation acts as −1 on the tangent, so the induced map on automorphism sheaves is an isomorphism. Hence the functor is locally essentially surjective and fully faithful. Both sides satisfy descent, so it is an equivalence over arbitrary S and cubic étale J. This does not choose or compare the distinguished symmetric μ4 pinning scale of equations73 and83c.

The example Q0 with s⁴=−4 is an earlier-run model, not manuscript ink. Its derivative is 4s³ and s is a unit over Z[1/2], so it is a μ4-torsor. The quotient coordinate i=−s²/2 has i²=−1. Over this quotient, s=1−i is a section because `(1−i)²=−2i`. This also checks its normalization under the order-four action. The fixed-orientation pinning torsor is elementary; the full symmetric μ4-equivariant identification is a distinct comparison problem.

The pages themselves distinguish a pinning from a pinning with an ordering of the three nonzero two-torsion points. For the latter, an automorphism preserving the order lies in ±1 (Conrad, Proposition 2.1); −1 acts as −1 on a tangent line, so fixing a nonzero pinning kills it. Without the order, even cyclic permutations remain possible at the equianharmonic parameter. The polynomial λ²−λ+1 has two distinct roots away from characteristics 2 and 3, but becomes `(λ+1)²` in characteristic 3. This warns against transporting the characteristic-zero fixed-scheme description unchanged. It does not refute rigidity with both structures imposed.

The two linear conditions on the three coordinates of a proposed pinning determine only a one-dimensional kernel. A character law and weight −1 under rescaling a tangent basis likewise leave a scalar. The tensor-square condition on scans 100 and 121 is therefore a separate obligation. Conrad, Proposition 3.2, proves a canonical ordered level-four-to-Legendre construction. This is genuine progress on the existence issue, but the exact identification of its square normalization and μ4 action with equations 73 and 83c has not been supplied by the manuscript or the opened references. This audit does not label that comparison an established open conjecture in current mathematics.

## 2. The order-twelve group and its characters

**C-SA16-507–510.** Write μ4 additively as Z/4 and let parity be its map to C2. The fibre product consists of pairs `(g,a)` with `sign(g)=a mod 2`. There are twelve. The pair with a transposition and a=1 has order four, its square is the central pair `(1,2)`, and no element above a transposition has order two. Thus the central extension of S3 by C2 is nonsplit. A three-cycle generates a normal C3 and conjugation by the order-four element inverts it. This gives `C3⋊C4`, usually Dic3. The commutators generate C3, so the abelianization is C4 and the centre is C2. The program enumerates the complete finite group, not a random sample.

On the orientation factor, `(g,λ)` has character `sgn(g)λ²`; its stabilizer is exactly that fibre product. On the claimed tangent line the character is λ, and on its square it is λ². Multiplying the square character by the sign character gives one on the stabilizer. These are exact character checks. They do not establish every functorial geometric identification asserted with these characters.

## 3. A caution concerning a modern quotient statement

**R-SA16-L64-Hain315; literature result Hain2008:Proposition 3.15.** The displayed strict quotient in Proposition 3.15 of the opened Hain preprint, and in the author’s 2021 revision, uses C2×S3 with C2 trivial on the Legendre parameter line. At λ=−1 the S3 stabilizer has order two. The resulting strict quotient has stabilizer C2×C2. The curve `y²=x³−x` instead has origin-preserving automorphism group C4: `(x,y)↦(−x,iy)` has square −1 and order four. The two stabilizer groups are not isomorphic, so this literal strict quotient cannot be the elliptic moduli stack. Antieau–Meier, Proposition 4.5 and Lemma 4.7, provide the root atlas with twisted S3 descent and avoid this mismatch. This is a bounded refutation of that proposition’s strict quotient reading; it does not discredit Hain’s period-family or framed-moduli arguments used elsewhere.

## 4. Pole filtration and the invariant derivation

**C-SA16-516–523.** Let E/k be a smooth geometrically connected projective genus-one curve with k-rational origin O. Riemann–Roch gives `dim F_n=n` for n≥1 and `F0=F1=k` (MilneEC2021, I.4.13 and II.1). The absence of a simple-pole nonconstant function makes the n=1 associated graded piece exceptional. For n≥2, the quotient is the ordinary principal-part line.

Choose a local parameter t at O and a nonzero tangent vector δ. Write `Dδ(t)=a+O(t)` with a≠0. If `f=b t^(−n)+...`, then `Dδ(f)=−nab t^(−n−1)+...`. Hence `gr_n(Dδ)=−n μδ`. If the principal-part identifications are changed multiplicatively by `ε_n=c^n pp_n`, the coefficient becomes −nc. It cannot be one for every n, since multiplicativity and the Leibniz rule require the coefficient in degree m+n to be the sum of those in degrees m and n. The small missing indices in the degree-one diagram must not be used to hide this obstruction.

For nonzero δ in characteristic zero, `ker(Dδ:k(E)→k(E))=k`; the field of constants is k because E is geometrically connected with a rational point. In characteristic p over perfect k, the differential-kernel theorem (Stacks031W, Lemma 10.158.2) gives `ker Dδ=k(E)^p`: a nonzero derivation on the one-dimensional differential space has the same kernel as the universal differential. If `f=g^p` lies in F_n, valuations show that g has no poles away from O and pole order at most floor(n/p) there. Therefore

`ker(Dδ|F_n)={g^p:g∈F_floor(n/p)}`, with dimension `max(1,floor(n/p))` over perfect k.

A nonconstant x with pole order two gives the first such element x^p at order 2p. Taking n=2p+1 also shows why merely imposing p∤n does not repair the filtered statement. The program checks the basis calculation in several odd characteristics; the valuation argument establishes the general result.

For the section/Rees ring `R=⊕ F_n T^n`, define `D(fT^n)=Dδ(f)T^(n+1)` and S=1T. Then `ker D=k[S]` in characteristic zero. Over perfect k of characteristic p, it is `R^p[S]`: every homogeneous kernel element has the form `g^pT^n=(gT^m)^p S^(n−pm)` with m=floor(n/p). This differs from the filtered union F∞, whose kernel is k or F∞^p. The literal graded statement “kernel k” is already false in characteristic zero because S is killed.

Negation sends the invariant tangent vector to its negative, so D switches parity. An even x of pole order two and odd y of pole order three give bases by distinct pole orders: even functions are polynomials in x and odd functions are y times polynomials in x. The zero tangent vector is excluded. At δ=0, the prescribed principal part for x vanishes, x lies in F1, and y=Dδx=0. Scan 115 explicitly says that δ is a basis; scan 105’s local display does not.

The monic coefficient requires care. With ordinary principal parts and δ normalized by D(t)=1+..., choosing x with leading coefficient one yields y=Dx with leading coefficient −2, so y² has leading coefficient four relative to x³. With `ε_n=(−1/2)^n pp_n`, the corresponding x starts with `4t^(−2)` and y with `−8t^(−3)`, giving a monic equation. This convention makes the degree-two derivation coefficient one, but not the coefficient in every degree. No source in scans 2–157 specifies ε_n sufficiently to choose an ink correction solely from this calculation.

## 5. Cubic construction, signs, and group law

**C-SA16-524–533.** For `f(X)=∏(X−ζ_i)=X³+a1X²+a2X+a3`, the signs are `a1=−Σζ_i`, `a2=Σζ_iζ_j`, `a3=−ζ1ζ2ζ3`. Restriction of the even subspace spanned by 1,x,x² to the three distinct roots is a Vandermonde isomorphism. The odd function y vanishes there, so the kernel of restriction F3→k^J is ky. The program checks the author’s specific determinant after substitution. Scan 106 completes this local argument and is not an outstanding open step.

For `A=k[x,y]/(y²−f(x))` in characteristic different from two, set Dx=y and Dy=f′(x)/2. Applying D to the relation gives zero. The alternative `a2x²` with the displayed derivative leaves residual `a2(1−2x)y`, and a single-prime expression in place of D²x fails degree and parity. Replacing x by x+b gives coefficients

`a1−3b`, `a2−2a1b+3b²`, `a3−a2b+a1b²−b³`.

Thus the trace-zero translation uses 3 invertible, exactly as the author says. A squarefree cubic gives a smooth affine curve; its ordinary projective cubic completion has a single smooth point at infinity and genus one. Its section ring is generated in weights 1,2,3, whereas the ungraded union is the affine coordinate ring. These are distinct constructions (MilneEC2021, II.1; Stacks0BYA).

For three **distinct finite points**, vanishing of the determinant with rows `(1,x_i,y_i)` means they lie on a line. Its divisor is `P1+P2+P3−3O`, so their group sum is zero. If two rows repeat, the determinant vanishes without implying that sum. On `y²=x³−x`, the points `(0,0),(1,0),(0,0)` have determinant zero and sum `(1,0)≠O`; all are points on a smooth curve over Q. The author corrects the missing distinctness on scans 110–111.

For distinct x-coordinates, write the secant as y=mx+b. The third root w satisfies `u+u′+w=m²−a1`, and the third point `(w,mw+b)` is the negative of the sum. Tangent substitution gives the usual doubling formula when 2y≠0; if y=0 the point is two-torsion. The program checks the cubic factorization, not only a numerical example.

## 6. Möbius involutions and fourth division

**C-SA16-532–535.** For a root r and the other roots u,v, put A=(r−u)(r−v). Translation by `(r,0)` descends under x to

`σ_r(z)=r+A/(z−r)`.

Its representing matrix squares to A times the identity, and direct substitution gives `f(σ_r(z))=A² f(z)/(z−r)^4`. The fixed x-values solve `(z−r)²=A`. Because the roots are distinct and 2 is invertible, these are two distinct values, neither a branch root; each has two nonzero y-values. They give the four halves of `(r,0)`. The three nonzero two-torsion points give twelve points of exact order four. The r=0 case is `uv/z`; formulas dividing a3 by r must be interpreted by this polynomial continuation or restricted to r≠0.

Expanding A gives `A=−(a1r+2a2−3uv)`. The scan-118 bracket with +3uv is wrong relative to the scan-116 equation. With `(r,u,v)=(1,2,3)`, the valid A is 2 and the written expression is −34. The marginal constant similarly requires `a2−2uv`. These are separate reading alarms, not replacements of the transcript. The fourth-division computation does not finish the pinning scale deferred on scans 100/121.

## 7. The tautological sequence and cyclic differences

**C-SA16-514,536–538.** Let F_t be the line of sections of O(1) vanishing at t. Tensoring `0→F_t→V→O_t(1)→0` by F_t dual gives the exact sequence in scan 119. Its middle map is `v⊗f^∨↦v/f`; rescaling f changes its dual inversely, so the ratio is canonical. The quotient is the tangent line at t. This argument uses the lines’ actual variance and does not guess the ambiguous dual glyph.

The equations `Σψ_i=Σζ_iψ_i=0` have rank two for three distinct ζ_i. Their kernel is generated by `(ζ2−ζ3,ζ3−ζ1,ζ1−ζ2)`. Solving the author’s equations for f1,f2 gives

`Δ0 f1=Σ(ζ_j−ζ_k)e_i`, and `−Δ0 f2=Σζ_i(ζ_j−ζ_k)e_i`,

where `Δ0=(ζ1−ζ2)(ζ2−ζ3)(ζ3−ζ1)` and the indices cycle. The code verifies both equations symbolically. The mark before Δ0 f1 on scan 126 cannot be decided as a dot or minus by transcription alone; the equations demand the positive sign in this convention. Weight −1 gives `φ_i(λδ)λδ=φ_i(δ)δ`, which proves independence of basis but supplies no differential connection on a base.

## 8. Complex structures, orientations, and holomorphic families

**C-SA16-539–544.** For a complex subspace L of V_C with real-part map φ:L→V invertible, the manuscript uses conjugate transport `J=−φ i φ^(−1)`. Conversely `L={x+iJx}` is stable under i and real part is its inverse. The second expression in scan 132 must therefore contain φ^(−1), a type check independent of convention.

For `L_z=C(z,1)`, z=x+iy and y>0, this convention gives

`J_z=(1/y)[[−x,x²+y²],[−1,x]]`.

Consequently `det(e1,J_ze1)=−1/y`, so it induces the opposite orientation. The author withdraws the positive-orientation statement and later changes the line convention. This is an authorial correction, not an unresolved mathematical claim.

A faithful circle representation with only two conjugate weights has weights ±m; faithfulness gives |m|=1. Choosing an order-four element therefore gives J or −J. In real dimension 2n their orientations differ by (−1)^n. Orientation selects one only for odd n. In real dimension two a circle-invariant positive definite form is unique up to scale: in a rotation basis, a commuting symmetric matrix is scalar. In higher dimension this uniqueness would be false, and is not claimed here.

The first-draft period −bar(z) depends antiholomorphically on z. A framed holomorphic family has holomorphic period ratio, so it cannot be the claimed universal holomorphic family in that coordinate. The second draft uses a holomorphic τ. For an oriented lattice basis, Eτ=C/(Z+Zτ), Im τ>0; the quotient family over H is holomorphic. Period integration gives the inverse map for framed families, and an automorphism fixing both periods is the identity. The opened precise comparison is Hain, Sections 2.3–2.4; Grothendieck’s Cartan X introduction supplies the earlier lattice-family context.

## 9. Actions, outer automorphisms, and freeness

**C-SA16-545–553.** The right framing convention produces `(dτ+b)/(cτ+a)`. The map `σ(g)=Jg^(−1)J`, J=diag(−1,1), is an anti-automorphism converting conventions. It is not a cusp inertia element. The usual left action on `(τ,z)` has multiplier `(cτ+d)^(−1)`; multiplying matrices proves the cocycle identity. With the order of translations written on scan 149, conjugation gives `ρ(g)=[[a,−b],[−c,d]]`, hence `(g,v)(h,w)=(gh,v+ρ(g)w)`. These identities are checked symbolically with determinant-one relations.

The universal framed **base** H covers the moduli stack `[H/SL2(Z)]`. Its total elliptic family has fundamental group Z² because it is a fibre bundle over contractible H with torus fibre. It is not that universal cover. The coarse j-line also has different covering theory because it discards the elliptic stabilizers.

A once-punctured torus retracts onto a wedge of two circles. Thus Π=F2 and Π_ab=Z², contradicting the first draft’s rank-one parenthesis. The classical identification Out(F2)=GL2(Z) is recalled in Bux–Ershov–Rapinchuk, Section 3. Orientation/peripheral conjugacy gives the determinant-one subgroup. For explicit lifts `S(x)=y,S(y)=x^(−1)`, `T(x)=x,T(y)=xy`, free reduction checks `S⁴=1` and `(ST)³=Inn(yx^(−1))S²`. Thus the modular relations hold in Out(F2). This computes the requested discrete outer action, but not an arithmetic Galois image or the kernel of a profinite comparison.

On double-frame space `P=C*×H`, each separate action of C* or SL2(Z) is free. The pair `(−1,−I)` fixes the base and acts on each elliptic fibre by z↦−z. Its four fixed points are E[2]; three remain after deleting O. This verifies the author’s withdrawal of product freeness. For a split extension N⋊U, changing between left and right normal forms gives y=uxu^(−1) and the usual semidirect multiplication. The cancelled diagram around it does not specify the group or augmentation module enough for a further theorem.

## 10. Quadratic orders over a DVR

**C-SA16-554–559.** Unique factorization in Z[T] and Q(T) gives the square-class representative εqQ described in the item. The uncertain “anneau jauge” is not silently decoded as DVR. The following proof is conditional on A being a DVR, with uniformizer π and a≠0.

If v(a)=1, the maximal ideal of B=A[S]/(S²−a) is generated by S and B is a one-dimensional regular local ring, hence a DVR. If v(a)≥2, S/π is integral over B and not in B, so B is not normal. If v(a)=0 and 2 is a unit, B is finite étale over A and normal. This proves the odd-residue-characteristic criterion v(a)≤1.

In residue characteristic two with a a unit, nonsquare residue makes B/πB a field. Its maximal ideal is πB; B is a DVR. Its residue extension is purely inseparable of degree two, so normality here is not étaleness. If the residue is a square, choose α lifting its square root, put t=S−α and b=α²−a. Then `B=A[t]/(t²+2αt+b)` and its maximal ideal is (π,t). Replacing α by α+πc changes b by `2απc+π²c²∈π²A`, so b mod π² is intrinsic. If v(b)=1, the relation makes π a multiple of t, and B is a DVR. If b∈π²A, the relation has no nonzero linear term in `(π,t)/(π,t)²`, so B has embedding dimension two and is not a DVR. Equivalently t/π is an integral element outside B, satisfying `U²+(2α/π)U+b/π²=0`.

The hypothesis cannot be enlarged to an arbitrary regular local ring. Over `A=Q[[x,y]]`, the ring `A[S]/(S²−xy)` is a hypersurface and is regular at every height-one point: its only singular point is the maximal ideal (x,y,S), of codimension two. It is therefore normal by R1+S2, although a=xy belongs to m². This checks every assumption of the competing higher-dimensional interpretation.

Exactness of completion (Stacks0BNH) identifies `A[[t]]/(t²+2αt+b)` with the t-adic completion. If b≠0, B/(t)=A/(b) is Artinian, so (t) is maximal-ideal-primary and the t-adic and local topologies agree. If b=0 they need not agree. For `A=Z_(2),a=α=1`, quotienting by t leaves noncomplete A, whereas the local completion would leave its completion. This split example is excluded when a is required to define a genuine quadratic field, but refutes an unrestricted completion assertion.

When b∈π²A, the tangent quadratic is `X²+cXY+dY²`, with c the residue of 2α/π and d that of b/π². Over an algebraic closure of the residue field it has distinct lines exactly when c≠0, equivalently v(2)=1. In equal characteristic two, `a=1+π³` gives the cusp relation `t²+π³`, with doubled tangent. In `A=Z2[sqrt(2)]`, π=sqrt(2), a=5 and α=1 give b=−4, again a doubled tangent because v(2)=2. Thus the unrestricted “ordinary double point” assertion is false if that term means distinct geometric tangents. The manuscript’s terminology and its uncertain ring hypothesis remain reading issues.

## 11. Global normality and generic étaleness

**C-SA16-560–564.** The ring `Z[T,S]/(S²−P)` is a hypersurface in a regular ring, so it is Cohen–Macaulay and satisfies S2 (Stacks02JN). If the local quadratic orders at all height-one points are normal, they satisfy R1. Serre’s criterion then gives global normality: there is no residual finite exceptional set. EGA IV2, Theorem 5.8.6, printed page 108, and its proof were opened; Stacks031O gives the modern exact statement. The conclusion is an application of that theorem, not a newly attributed result of these notes.

Now let `P=εqQ` be a nonzero squarefree element of Z[T], with ε a sign, q its positive squarefree content, and Q primitive with positive leading coefficient. Assume it defines a genuine quadratic field over Q(T). Let N be its normalization over Z[T]. At the generic point of an integer fibre p, any p dividing q gives valuation one and a ramified quadratic extension. Thus generic étaleness for every p forces q=1. At every odd p not dividing q the unit radicand gives an étale order. At p=2 write `A=Z[T]_(2)`, whose residue field is F2(T). A unit radicand gives an unramified quadratic normalization exactly when P is a square modulo 4A. Here is the needed algebraic justification rather than an appeal to an integer-only discriminant rule.

If the normalization is finite étale over this DVR, it is free of rank two with a basis containing 1. Its other generator u satisfies `u²−ru−h=0` with unit discriminant `d=r²+4h`; necessarily r is a unit. Since its fraction field is K(sqrt(P)), d and P differ by a square c² in K. Both are units, so c is a unit of A. Therefore P is a square modulo 4A. Conversely such a congruence gives this standard étale quadratic presentation. Finite normalization exists here because the base is excellent; alternatively the explicit presentation proves sufficiency without that general existence input.

The local square congruence globalizes. If P is a square in F2(T), its polynomial factor valuations show that its square root lies in F2[T]. Choose a lift r0∈Z[T]. Any local square root modulo two differs from r0 by 2A, so its square has the same residue modulo 4A. Thus `P−r0²∈4A∩Z[T]=4Z[T]`. The latter equality follows because the denominators inverted in A are not divisible by two. Hence P=r²+4h with integer polynomials r,h.

Set `u=(S+r)/2`. Then `u²−ru−h=0`, so `N0=Z[T,u]/(u²−ru−h)` is a finite free quadratic order. Its discriminant is P and `(2u−r)²=P`, so it is étale on D(P). It is normal: at horizontal height-one primes squarefreeness gives valuation at most one; at vertical odd primes it is generically étale; at the vertical prime two, r is nonzero in F2(T), so the derivative is a unit. Thus R1 holds, and the hypersurface gives S2. Consequently N0 is the full normalization. This proves the exact sufficiency left without proof on scan 156 and its converse.

The dyadic test must use P including its sign. For example P=3 and P=−1 both have unsigned Q=1, yet their original quadratic orders over Z_(2) are normal: b is respectively −2 and 2. If the handwritten Q is shorthand for P, no correction is needed; the table preserves this ambiguity.

For nonzero integer λ, suppose `εT(T−λ)` is a polynomial square modulo four. Reduction modulo two forces λ even and the square root congruent to T. Every lift has square congruent to T² modulo four, so the T² coefficient forces ε=+1 and the T coefficient forces 4|λ. These conditions suffice. The value λ=2 satisfies the weaker congruence modulo two but not modulo four.

With λ=4m and x=1/T, dividing S by T gives `(S/T)²=1−λx`, not λx−1. The normalized chart is `u²−u+mx=0`; its discriminant is `1−4mx` and is a unit on the claimed open. At infinity x=0 its fibre is split, `u(u−1)=0`. Reducing modulo two gives an Artin–Schreier equation. With the written opposite sign and λ=4,x=0 one instead obtains Q(i), ramified at two. This point lies in the stated open, so it is a valid counterexample to the literal claim.

## 12. Earlier-run differential and congruence leads

**SA16-539–546,575–579,589.** These are not claims made on the pages. They are kept in their own project-lead table. For the standard Legendre family, direct rational differentiation checks that the Picard–Fuchs operator `L=λ(1−λ)∂²+(1−2λ)∂−1/4` applied to dx/y is the x-derivative of `x(x−1)/(2(x−λ)y)`. The usual elimination of the first-derivative term gives Schwarzian `(λ²−λ+1)/(2λ²(λ−1)²)` for a locally univalent period ratio.

For odd p and m=(p−1)/2, put `H=Σ binom(m,k)²λ^k`. The coefficient equation for LH is `(k+1)² c_(k+1)=(k+1/2)² c_k`. Since m≡−1/2 mod p, the binomial ratio satisfies it; the terminal coefficient vanishes because m+1/2=0 mod p. Expanding `(x(x−1)(x−λ))^m` gives coefficient `(−1)^m H` at x^(p−1). This is the elementary coefficient calculation behind the Cartier formula, not an identification with a base connection. The polynomial checks for p=3,5,7,11,13 support but do not replace that universal argument.

For the companion solution connection ∇=∂−A used in the earlier note, the program iterates the connection on a basis in F3(λ). It obtains

`ψ3 = [[−(λ+1),(λ+1)²],[−1,λ+1]] / [λ²(λ−1)²]`.

This is nonzero and square-zero, including at λ=−1. The dual coefficient connection has the negative transpose. Katz1970, Theorem 5.1, concerns descent for **zero** p-curvature; Theorem 5.10 supplies nilpotence bounds for Gauss–Manin. Those are different assertions. No such operator is written in the cote 64 passages cited by the notes.

The q-loop τ↦τ+1 gives the usual T matrix; reduction of a Torelli frame modulo N gives Γ(N). Neither identifies an arithmetic outer image. Bux–Ershov–Rapinchuk’s main theorem concerns the nonabelian profinite congruence action on the profinite free group, not injectivity of the classical abelian congruence map to SL2(Zhat). Hain, Proposition 8.2 and Corollary 8.3, identify the differential-frame fundamental group with B3; the central full twist maps to −I and its square generates the kernel to SL2(Z). These are opened comparison results, not computations secretly present in the manuscript.

## Verification boundaries

The finite group, polynomial, free-word and finite-characteristic calculations are exact and reproducible. General claims above use the stated arguments and opened primary results. No Lean library was run or audited, and no earlier-run script was inherited as a proof. The only first execution failure was a Sympy matrix expression requiring entrywise simplification before comparison with zero; after that implementation change all 31 recorded check groups passed. Reading questions remain undecided because this run has no scans.

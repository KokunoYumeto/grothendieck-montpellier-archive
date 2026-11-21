# Whole-proof audit of A24

**PASS.** The complete authored proof `A24_FROBENIUS_SIDON.tex`, final SHA256 `075d9fe80de01483666517d0c9fea7e35c19f77b9f69693dd79cdb2e4f46f250`, was reread. Root and effective_galois independently read the entire same source and reported PASS. Both also reopened Lenstra's primary scope. These are mathematical reviews, not proof-assistant verification.

## Development and exact scope

The parent proposed the Frobenius-orbit pair bound. I proved the counting inequality, obtained the direct quadratic Cayley–Hamilton relation, first checked the large-prime bound and the small inert primes7,11,13, and then extended the mechanism to actual eligible prime powers. Effective_galois supplied the stronger signed norm-kernel argument. I checked and incorporated it: the final uniform proof needs no cutoff or exceptional computation. The small calculations remain explicitly nonessential consistency checks.

The final restriction concerns this particular A13 curve and actual n=ell^r with <2,-1>=U_n. A theta point of that exact order requires ell=3,5 or ell=1,2,4,8 modulo15. It is necessary, not sufficient; the conditional residual-density claims are separated from it.

## Finite geometry and local module

The genus-two theta-translate bound gives at most two representations of each nonzero difference. Counting ordered pairs proves |A|(|A|-1)<=2(|H|-1) for any A contained in theta and a finite subgroup H, including groups of prime-power exponent. The particular Raynaud theta is symmetric because B^2=omega and degree-one Riemann–Roch equates h0(BL) and h0(BL^-1). No invariance under multiplication by2 is asserted.

The original F2 characteristic polynomial gives psi^4-psi^2+4=0 integrally. Thus Phi=psi^2 satisfies the quadratic relation directly; no inference from a squared polynomial without semisimplicity is needed. At an inert prime the quadratic ring is unramified, beta has norm4, and the residue signed group <beta,-1> has norm image of order h=(ell-1)/2. Its kernel is even. Kernel order2 would identify that group with F_ell^times, contradicting irreducibility. Therefore its size is at least2(ell-1).

The unramified quadratic integer ring O acts on the Tate lattice. A nonzero O-element acts invertibly after tensoring with Qell, so the lattice is torsion free over O and free of rank2. Moduloell^r, an exact-order point in R^2 has a unit coordinate, proving R to Rz injective and |Rz|=ell^(2r). This is the full annihilator argument.

Reduction of beta's order gives s_r=s1*ell^b, b<=r-1. The actual finite-level signed-unit hypothesis gives ord_(ell^r)(4)=h*ell^(r-1). Norm divisibility forces b=r-1. This is a finite-level implication, not a blanket non-Wieferich assumption. The local unit group has the unique order2 element-1, so adjoining-1 doubles both residue and lifted orders, or neither. Hence the signed orbit has at least2(ell-1)*ell^(r-1) points. The displayed strict inequality violates the pair bound for everyell>=5; inert primes here start at7. All exponents are covered.

## Conditional densities

I reopened Lenstra1977 Sections2-3, including Theorem3.1 and its entire Section3.2 argument. W may contain torsion, so W=<2,-1> is permitted. The sufficient family is exactly zeta of Q(zeta_n,2^(1/n),(-1)^(1/n)), squarefree n; the fixed split condition in Q(sqrt(-15)) does not require adding separately the compositum zetas. Premise M contains this family. The analytic infinite-limit theorem is cited, not proved by the finite sums.

For odd squarefree m, Eisenstein at2 and the affine Galois group give degree m*phi(m) and maximal abelian subfield Q(zeta_m). The even field is Q(zeta8)K_m of degree4m*phi(m). Its maximal abelian subfield is Q(zeta_(8m)). The quadratic field of discriminant-15 is contained exactly when15 dividesm: containment then is cyclotomic, and otherwise missing ramification at3 or5 excludes it. The total signed-eligible density is3A/2. Forcing15 dividesn changes the Euler product by(-1/5)(-1/19)=1/95. Thus split density is(3A/4)(1+1/95)=72A/95. With W=<2>, the even degree factor is2 instead of4; total densityA gives split48A/95. Both hypotheses and conditional status are explicit.

## Arithmetic and remaining obstruction

`check_A24_orbits.py` ran successfully. Quadratic-ring pairs and separately implemented2x2 matrix multiplication verify orders24,60,84 at7,11,13, including all prime-divisor witnesses. Split classes and rational Euler-factor algebra also pass. The latter is not a computational proof of natural density.

The known4159 witness is split and already prevents an all-eligible-prime nonexistence interpretation. At split primes a point with both eigencomponents can have generated dimension2 and orbit size at mostell-1, which this numerical bound permits. An eigenline point can have short orbit, as the F128 witnesses do. This quadratic-algebra orbit test therefore does not automatically extend to exclude the surviving split candidates or settle the variable-prime incidence gate.

An audit-writing command first stopped at a source-hash assertion because the concurrently maintained A23 file had changed from its earlier checked hash. I reread that entire current file and recorded its new hash above; no mathematical claim was affected.

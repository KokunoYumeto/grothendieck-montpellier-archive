# DET-11: independent determinant, resolvent, and prime-sum transform check

Run **TRACE_DET_20261121**, 21 November 2026. Checker `/root/step1_history_route`, GPT-6 Astra Pro (inherited developer label); effort setting not exposed.

## Verdict

**PASS.** I read all of `paper_resolvent_bridge.tex`, including its final inverse-transform and scope paragraph. I then recomputed the determinant normalization, the resolvent sign, the actual ramp transform, and the zero multiplicities independently. The result is unconditional relative to the already proved zero-based construction B-01 and the classical completion/Euler-product facts. RH is not used. No change to the mathematical statement is required.

Small locator precision in the initial draft: `poleData_change` begins at line114, not112; the initial112–135 range nevertheless contained its whole declaration/proof. Root updated it to114–135, which was confirmed on the final complete reread. The modulus-one Mellin theorem really is stated for Re(s)>1. The adjacent `poleData_integrable` uses Re(s)>2 for a different coarse bound, and should not be confused with the sharper modulus-one calculation. The proof's Re(s)>1 conclusion is correct.

## Independent calculation

Let J index one zero from each pair {γ,−γ} of Ξ, with multiplicity, as in B-01. Write

\[
b_j=\gamma_j^{-2},\qquad
\rho_j=\tfrac12+i\gamma_j,\qquad
c_j=\frac{b_j}{1+b_j/4}=\frac1{\gamma_j^2+1/4}
=\frac1{\rho_j(1-\rho_j)}.
\]

The input facts are γ_j≠0, |γ_j|→∞, Σ|b_j|<∞, ξ(0)=ξ(1)=1/2, and

\[
\det(I-wB)=G(w)=\Xi(\sqrt w)/\Xi(0)
\]

in the even-power-series meaning of G. These are the proved/cited facts of B-01, not RH assumptions.

### A. Both rational operator transforms exist

If 1+b_j/4=0, then γ_j²=−1/4, so γ_j=±i/2. Then one of ρ_j=0 or1 would be a zero of ξ, contradicting ξ(0)=ξ(1)=1/2. Thus every diagonal entry of I+B/4 is nonzero. Because these entries tend to1, they have a positive infimum in modulus: beyond a finite index they have modulus at least1/2, and the remaining finite nonzero set has a positive minimum. Consequently I+B/4 has a bounded diagonal inverse. Its product with trace-class B is trace class; equivalently Σ|c_j|<∞.

Similarly,

\[
1-c_j/4=\frac{\gamma_j^2}{\gamma_j^2+1/4}\ne0,
\qquad 1-c_j/4\longrightarrow1.
\]

Hence I−C/4 has a bounded inverse, and diagonal multiplication gives

\[
C(I-C/4)^{-1}=B.
\]

This proves the inverse claimed at the end of the paper subsection, including boundedness and without a selfadjointness assumption. The exclusion c_j=4 uses Ξ(0)≠0, already part of B-01.

### B. Normalization of the entire determinant

For each diagonal entry and every v,

\[
1-vc_j=\frac{1-(v-1/4)b_j}{1+b_j/4}.
\]

Products of these factors converge absolutely and locally uniformly because Σ|b_j| and Σ|c_j| converge. The denominator product is nonzero: it is G(−1/4)=ξ(0)/ξ(1/2), so no nonzero limiting factor is lost. Therefore

\[
D_C(v)=\det(I-vC)=\frac{G(v-1/4)}{G(-1/4)}.
\]

Put v=s(1−s). The identity v−1/4=−(s−1/2)² permits the *explicit* choice z=−i(s−1/2), so z²=v−1/4 and

\[
G(v-1/4)=\frac{\Xi(z)}{\Xi(0)}
=\frac{\xi(s)}{\xi(1/2)}.
\]

This is an identity of entire functions obtained from G(z²)=Ξ(z)/Ξ(0); no analytic square-root branch is chosen. Also G(−1/4)=ξ(0)/ξ(1/2). Hence

\[
\boxed{D_C(s(1-s))=2\xi(s).}
\]

As a quick normalization check, s=0 or1 gives D_C(0)=1 on the left and2ξ(0)=2ξ(1)=1 on the right. No extra exponential factor survives: the ratio was obtained from the actual absolutely convergent products of B-01, not merely from equality of zero sets.

### C. Resolvent trace and its sign

If ξ(s)≠0, the determinant identity gives D_C(v)≠0. Equivalently, 1−vc_j≠0 for every j. Since c_j→0, these denominators are bounded away from zero; the diagonal inverse of I−vC is bounded, and

\[
R(v):=C(I-vC)^{-1}
\]

is trace class, with

\[
\operatorname{Tr}R(v)=\sum_j\frac{c_j}{1-vc_j}.
\]

On a compact v-set avoiding determinant zeros, choose a tail for which |vc_j|≤1/2 uniformly. Its terms are bounded by2|c_j|; the finitely many other terms are bounded because their denominators do not vanish. Thus the sum is absolutely locally uniformly convergent. Termwise differentiation of local logarithms gives

\[
\frac{D_C'(v)}{D_C(v)}=-\operatorname{Tr}R(v).
\]

Differentiating D_C(s(1−s))=2ξ(s) then yields

\[
\frac{\xi'(s)}{\xi(s)}
=(1-2s)\frac{D_C'(v)}{D_C(v)}
=(2s-1)\operatorname{Tr}R(v).
\]

The sign is positive in front of2s−1 because both the determinant logarithmic derivative and v'(s)=1−2s supply a minus sign.

At s=1/2, ξ(1/2)≠0, the resolvent exists because no c_j=4, and the factor2s−1 is zero. The left side is zero by ξ(s)=ξ(1−s). Thus the formula holds there without division by2s−1 or a limiting singularity.

### D. Multiplicity and residues

A pair {ρ,1−ρ} of zeros of ξ of multiplicity m produces the eigenvalue

\[
c=1/[\rho(1-\rho)]
\]

of C with multiplicity m, not2m. The corresponding factor of D_C(v) is (1−vc)^m. Substitution v=s(1−s) gives roots at both ρ and1−ρ, each of multiplicity m because ρ≠1/2. Equality of the products is therefore consistent with all zero multiplicities.

More explicitly, for that pair,

\[
\frac{c}{1-s(1-s)c}
=\frac1{\rho(1-\rho)-s(1-s)}
=\frac1{(s-\rho)(s-(1-\rho))}.
\]

Multiplying by2s−1 gives

\[
\frac{2s-1}{(s-\rho)(s-(1-\rho))}
=\frac1{s-\rho}+\frac1{s-(1-\rho)}.
\]

Thus ξ'/ξ has residue m atρ, and the nontrivial-zero residue of the displayed prime-sum transform is

\[
-\frac{m}{\rho(\rho-1)}=\frac{m}{\rho(1-\rho)}.
\]

This agrees with the source `poleData_char` at `LandauTheorems/poleData.lean:137–143`. Under no RH assumption is this complex number asserted to be a positive real number. For a realρ in(0,1), the denominator would be positive; general complex zeros require the stated qualification.

### E. Independent integral computation on Re(s)>1

Let σ=Re(s)>1 and use the exact scalar endpoint

\[
G_\zeta(y)=\sum_{n\ge2}\Lambda(n)(y/n-1)_+
-y\log y+(1+\gamma_E)y,\qquad y\ge1.
\]

For fixed y the sum is finite. Substitution y=e^u, du=dy/y, gives

\[
\Phi_\zeta(s)=\int_1^\infty G_\zeta(y)y^{-s-1}\,dy.
\]

For n≥2, direct integration gives

\[
\int_1^\infty(y/n-1)_+y^{-s-1}\,dy
=\frac1n\int_n^\infty y^{-s}\,dy-
\int_n^\infty y^{-s-1}\,dy
=\frac{n^{-s}}{s(s-1)}.
\]

Interchange with the sum is justified absolutely, not just formally. Since Λ(n)≥0,

\[
\sum_{n\ge2}\int_1^\infty
\left|\Lambda(n)(y/n-1)_+y^{-s-1}\right|dy
=\frac1{\sigma(\sigma-1)}\sum_{n\ge2}\Lambda(n)n^{-\sigma}<\infty.
\]

The last sum converges because Λ(n)≤log n. The two elementary completion terms are also integrable forσ>1, and

\[
\int_1^\infty y^{-s}\log y\,dy=\frac1{(s-1)^2},\qquad
\int_1^\infty y^{-s}\,dy=\frac1{s-1}.
\]

The classical absolutely convergent Euler-product logarithmic derivative is

\[
\sum_{n\ge2}\Lambda(n)n^{-s}=-\frac{\zeta'(s)}{\zeta(s)},\qquad\Re s>1.
\]

Consequently

\[
\boxed{\Phi_\zeta(s)=-\frac{\zeta'(s)/\zeta(s)}{s(s-1)}
-\frac1{(s-1)^2}+\frac{1+\gamma_E}{s-1}.}
\]

The exact source expression at `mellinGchiModOne.lean:115–118` is

\[
-\frac{\zeta'/\zeta+1/(s-1)+1-(1+\gamma_E)s}{s(s-1)}.
\]

The two expressions agree because

\[
\frac{-1/(s-1)-1}{s(s-1)}=-\frac1{(s-1)^2},
\qquad
\frac{(1+\gamma_E)s}{s(s-1)}=\frac{1+\gamma_E}{s-1}.
\]

Finally, logarithmic differentiation of

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

on Re(s)>1 gives

\[
\xi'/\xi=A_\infty+\zeta'/\zeta,
\quad A_\infty=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2).
\]

Therefore −ζ'/ζ=A∞−(2s−1)TrR(v), proving exactly the paper's final formula, with every sign and constant accounted for.

## Source checks and scope

The following source statements were read directly:

- `Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean:10–22`: finite ramp, Gχ and scalar G; modulus-one character has values1.
- `Formalism/StatementOC.lean:11–13`: Sz and Gz. For y≥1, the finite ranges and positive-part conventions agree because terms with n>floor(y) vanish and Λ(0)=Λ(1)=0.
- `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean:27–55,85–118`: individual ramp transform, elementary logarithm integral, exact modulus-one Mellin theorem and its Re(s)>1 hypothesis.
- `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/poleData.lean:114–135`: exact change of variables; at137–143, the scalar zero residue.

These source readings identify the scalar function to which the independent calculation applies; they do not claim a complete Lean replay. The result constructs a zero-dependent Fredholm representation of the scalar endpoint. It does not identify any upstream finite period/Gram/Capelli determinant with B or C, and does not produce arithmetic cohomology or an independently constructed positive operator.

Whole-proof check after this independent derivation: reread the original complete DET-11 proof and the derivation above, checking compact-set convergence, both bounded inverses, normalization at0/1, central value, multiplicity, complex residue sign, absolute Fubini, the source's exact numerator, and all hypotheses. No gap found.

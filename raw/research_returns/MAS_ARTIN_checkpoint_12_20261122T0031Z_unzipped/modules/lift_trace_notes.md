# Actual convolution-after-projection repair

## New proved results

`lift_trace.tex` proves MA-LIFT-001--003. It is an actual weighted-operator theorem, rather than an abstract quotient implication or a scalar use of the explicit formula.

1. MT-M26 polynomial block lifts imply a sufficiently high resolvent power of the quotient translation generator is trace class.
2. For the precise weight w=exp(2alpha|x|)(1+x²)^(s/2), the adjoint translation generator is L=w^(-1)∂w. Its high resolvent power on Z=J-perp is trace class by adjunction. Splitting integration by parts at0 writes C_g P_Z as a bounded operator times this power plus finitely many cusp-jet terms. The latter are bounded rank-one terms after the resolvent, by elementary local Sobolev estimates.
3. Actual cutoff spectral operators converge in S1, and for g(0)=0 the actual geometric-order trace tends minus the spectral trace, because M_rho C_g itself has trace g(0) integral(rho)=0.

## Exact hypothesis and limits

The uniform interior containing-strip hypothesis from MT-M26 is essential to the supplied block-resolvent proof. This gives alpha>1/2 unconditionally. All alpha>0 for rational/Dirichlet sectors uses A explicitly; for general Hecke sectors it uses conditional M. No unconditional partial-strip theorem or boundary assertion is inferred.

This repairs the actual-order premise behind F-SM18/F-SM21 at that scope and source Theorem10.4.2.8 (pp463-464), whose printed proof explicitly ends with an unfinished-proof footnote. It does not provide an independent local geometric arithmetic transport or an independent proof of zero location.

## Verification

Authoring agent GPT-6 Astra Pro, effort inherited/not externally exposed, read the complete MT-M26 proof and the source target proof, then reread the complete newly written proof. All derivative signs, domains, boundary terms, norm estimates and trace cyclicity were checked. Parent/root subsequently reported a complete independent proof reading with no fault found in the block resolvent, adjoint domain, half-line boundary/Sobolev, bounded coefficient, or trace-cyclicity steps; root records that event separately. The integrated MAS_ARTIN report subsequently compiled successfully; its build and rendering checks are recorded separately.

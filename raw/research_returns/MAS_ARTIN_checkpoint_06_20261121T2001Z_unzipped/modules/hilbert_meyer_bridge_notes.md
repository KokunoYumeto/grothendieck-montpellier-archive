# Hilbert–Meyer bridge and partial-strip obstruction

## New results

MA-HM-001 constructs an order-zero nuclear smoothing lift from the actual Hilbert quotient Z into the exponential Schwartz test space E:

    S̃_g = Σ_n T_n M_{g,n} r_n.

Its quotient S_g:Z→Q satisfies both actual operator identities

    S_g i_a = C_{exp(−a x)g} on Q,
    i_a S_g = C_g on Z.

The full proof uses MT-M18's polynomial bounds for each Schwartz seminorm and MT-M26's uniformly bounded Hilbert block restrictions. Per-seminorm convergence is strengthened to a genuine nuclear tensor representation by an Auerbach expansion and square-root normalization of the rapidly decaying Mellin bound b_n(g). The coefficient sequence lies in every ℓ^p, and the target vectors form one bounded set for all Schwartz seminorms. Bounded test families admit a common bounded disk. The quotient-valued S_g is independent of the interpolation section and intertwines translations with the explicit exp(−a y) factor. Its representative lift into E may depend on the section.

MA-HM-002 proves trace cyclicity from the same rank-one expansion. The exact MT-M22/M24 map transports smooth convolution to Meyer's actual negative quotient. Source trace additivity gives

    Tr_Z C_g = χπ+(f) − A_S(f) + D_S(f).

For rational zeta at a=1/2, the actual defect computed in MA-MEY-003 is D_S=−B_out, giving P−W_S−B_out. This proof does not use equality of scalar zero sums.

MA-HM-003 removes the uniform-interior assumption to investigate the genuinely partial-strip case. The completion map i_a still exists continuously with dense image, but it kills the entire local jet block at every completed zero ρ for which Re(ρ−a) lies strictly outside the closed strip [u,v]. Any nonzero image would contain an eigenvector growing faster under translation than the weighted Hilbert norm permits. Therefore even an arbitrary linear return map satisfying S_g i_a=C_{exp(−a x)g} is impossible unless every Mellin derivative through the full multiplicity vanishes at every such exterior zero. An allowed compact test can make its value1 at any one exterior zero. The obstruction is lost representation data, independent of scalar trace comparisons. Boundary jets are expressly outside this assertion.

The property that all allowed compact tests admit these full smoothing factorizations on every positive centered strip is consequently equivalent to RH for the one function. Necessity already holds for arbitrary linear return maps; sufficiency follows from MA-HM-001 under RH. This locates why the containing-strip premise cannot be silently bypassed by the same construction.

MA-HM-004 combines the actual ambient operator estimates in MA-LIFT-001–003 with the bridge and the actual Meyer commutator:

    lim Tr(Mρ C_g P_G) = A_S − D_S − polar = A0 + B − P,

for compact g with g(0)=0, under the explicit MT-M26 containing-strip premise. Every step is an operator trace or trace-norm limit. It does not identify individual finite orthogonal cutoffs with local Fourier cutoffs.

## Scope and checks

The only zero-location premise for MA-HM-001,002,004 is MT-M26's uniform interior: one closed strip containing **every** completed nontrivial zero must have positive distance from both Hilbert-strip endpoints. It holds unconditionally on a wide strip and on every positive Dirichlet strip using A. For the cubic imaginary quadratic character, its narrow instantiation needs that character's RH, sufficiently M.

The complete proofs of MA-HM-001 and002 were independently read by the S5 agent and by root. The author checked all four proofs in full; independent checks of003/004 are recorded separately as they complete. A subsequent short clause proved canonical independence and translation equivariance by density. The author also read and independently checked every written proof of MA-MEY-001–003 and MA-LIFT-001–003; the exact scope is recorded in s5_meyer_input_review_events.tsv and root_lift_input_review_events.tsv. Neither reviewer record claims a fresh proof of every upstream published Meyer result.

The current paper has replaced the earlier ambient-transport gap wording: LIFT plus HM plus MEY completes that operator trace-limit comparison under the same stated premise. The surviving independent-method gate is the location of the full zero divisor needed to instantiate the premise on arbitrarily narrow strips. MA-HM-003 gives a structural obstruction to recovering the missing full quotient after genuinely exterior blocks have been annihilated.

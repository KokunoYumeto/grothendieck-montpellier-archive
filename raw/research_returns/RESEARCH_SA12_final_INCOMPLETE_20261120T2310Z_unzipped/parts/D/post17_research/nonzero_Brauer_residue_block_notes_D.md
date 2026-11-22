# Nonzero local Brauer residues and rank-efficient blocks

Status: research notes only. No new theorem, quantitative atlas, or main-gate movement is claimed. The local Brauer-zero packet and its surface-transfer closure are separately checked.

## Exact residue calculation to source-check

Let Y resolve a complete normal local surface R with algebraically closed residue field, let E be its reduced SNC exceptional curve, and U=Y-E. For n prime to p, the already checked Picard argument gives Pic(Y)/n = Pic(E)/n = (Z/n)^v. Proper base change identifies H^2(Y,mu_n) with H^2(E,mu_n); the degree classes identify the latter with (Z/n)^v. Thus Br(Y)[n]=0. Also H^3(Y,mu_n)=H^3(E,mu_n)=0, and Pic(Y)->Pic(U) is onto by closing divisors on regular Y.

The localization sequence should therefore identify Br(U)[n] with H^3_E(Y,mu_n). Absolute purity and support Mayer--Vietoris, with no triple intersections, give the exact sequence

0 -> direct_sum_i H^1(E_i,Z/n) -> Br(U)[n] -> H_1(dual_graph(E),Z/n) -> 0.

The final map is the kernel of the signed node-to-component incidence map. Component classes are unramified characters of E_i. Graph-cycle terms instead encode possible ramification at nodes; they must not be silently treated as unramified component characters. Tate twists can be identified over the algebraically closed coefficient field, but a written proof should fix those identifications.

## Fixed symbols for the unramified component summand

The normalization constant-sheaf sequence on E makes H^1(E,Z/n)->direct_sum H^1(E_i,Z/n) surjective. Proper henselian finite-etale equivalence lifts every whole-E character to Y. Thus a character on one component can be lifted with zero characters on the other components.

For each i, weak approximation for the finitely many exceptional DVRs gives one rational function t_i in Frac(R) with v_{E_j}(t_i)=delta_ij. These functions may be fixed independently of n. A lifted character chi_i then gives the cyclic symbol (chi_i,t_i), whose exceptional residues are the desired character on E_i and zero on the other components.

The horizontal residue issue has a useful exact check. The normalization of the strict transform of any height-one prime of R is proper and quasi-finite over the complete one-dimensional local domain R/p, hence finite. It is a complete normal local curve with residue k, hence strictly henselian. Every finite-etale character of Y restricts trivially to it. Therefore the symbol has no horizontal ramification. Extending the resulting unramified class to Br(U) needs the exact regular-curve Brauer localization/purity input; this source has not been newly opened in this note. Weak approximation and the component/graph support calculation also need explicit primary locators before promotion.

This describes only the unramified component summand. It does not represent the graph-cycle part by the same symbols.

## Quantitative weight-block route

Root proposes the following potential rank-efficient replacement for a growing-rank Morita anchor. On the n-th root stack along an exceptional component, a residue character of order m permutes m inertia-weight blocks of a rank-r twisted object. Such an orbit forces divisibility by m; on the degree-m character cover of the component the corresponding block has rank s=r/m. If its object and formal-neighborhood presentation costs O(m s^2), the contribution is at most O(r^2), while a rank-m anchor followed by an ordinary rank-rm atlas loses this scale.

The component cover is finite etale, so its genus and fixed divisor degrees grow linearly with m. This is narrower than an arbitrary quasi-etale covering surface. C has been asked whether its hereditary object-atlas work provides an effective linear-index presentation in this narrower curve setting. Dimension estimates or tangent-space counts alone do not supply the required bound on variables and equation degrees.

Remaining points: make the root-stack inertia/permutation statement precise for actual Frobenius-unit twisted bundles; extend the block description across the formal neighborhood; prove the all-Artinian object and specified-map presentation with O(m s^2) variables; handle graph-cycle/node residues and their projective-Heisenberg analogue. No one of these is assumed merely from the cyclic-symbol description.

## Literature scope retained

Root freshly read Lieblich, Moduli of twisted sheaves, arXiv math/0411337v2: Proposition 2.3.2.9 and the stated later boundedness passages. Their fixed twisted anchor and splitting-cover constants do not give a uniform bound as the gerbe/index varies. The retained source tar is sources/Lieblich2007_moduli/source.tar. This is a limitation of the cited input, not a counterexample to the desired bound.

Recorded UTC: 2026-11-20T12:54:26.997462+00:00

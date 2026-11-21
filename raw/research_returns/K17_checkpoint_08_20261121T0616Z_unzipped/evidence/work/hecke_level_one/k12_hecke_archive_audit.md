# K17-K12-VANISH — independent complete-chain audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, archive_kummer.

**Verdict: PASS under the stipulated arithmetic theorems of Alpöge's source.**
The final theorem preserves this hypothesis explicitly. The review supplies an independent mathematical reconstruction of the new deduction, primary-source checks described below, source-content checks, and exact arithmetic replay. It is not a claim that the recovered Lean project was executed or that its stipulated arithmetic contracts were independently formalized in this session.

## 1. Documents actually reviewed

The complete final files were read:

| File | Reviewed SHA256 |
| --- | --- |
| `gl2_conductor_section.tex` | `6419cf200c28a8ffff42aaf7778049c86a60e3f265a67767db1947632c1671c3` |
| `gl2_conductor_bibitems.tex` | `90ff482fb0cf3cc206814ecb2e7912d06fb22a62f63a09df2f1112fe796b5eda` |
| `k12_hecke_vanishing_section.tex` | `98eaa9733c5ac311b988ed491fb19a179cba9f5d27d46a93cccc2594bb28fa9c` |
| `u3_hecke_section.tex` | `454170ba09eefab28c1a717e28559e5050de7c738df8acb30a654178444b6087` |
| `gl2_weight13_section.tex` | `8465519484928cd1ddf09f9532cc139a6accc5fd5a19afb6440fa336960b7188` |
| `../hecke_coverage/step17_unit_interface_section.tex` | `71366fb5a11ca4607978470b98a266f1e1b2e8c15c80f22cebc9d67d63dac628` |
| `../hecke_coverage/u3_coverage_section.tex` | `4b3f91bab7b67b6408dd5facd06b69313be16d7ad2029b42ce427dc5805f0790` |

The U3 coverage and GL2 modular-form sections had already received this reviewer's complete independent proof/source audits. They are retained, not represented as freshly proved external theorems. The final conductor argument and all its source locators were independently checked in `gl2_conductor_archive_audit.md`; the present review also read its final TeX and bibliography in full.

The following complete recovered source files were read for the exact interface: `NumberU3US.lean`, `KeepLevel.lean`, `FOneCharU.lean`, and `SmallClassNumbers/CorGKOf.lean`. The entire `SmallClassNumbers/ClassNumberThree.lean` datum construction was also read. Previous complete definition reads of `AutNewformW.lean`, `Newform.lean`, `AdmissibleRankTwoSelf.lean`, and `BlochKatoSelmerVanishes.lean` supply the rank-two interpretation. This checks source contents and quantifiers, not proof execution.

## 2. The source inequality really permits a pointwise unit argument

`OneCharU_s` first requires that every actual representation in the disjunction
`Adm3U_s(iota,e,N) or Adm2A(iota,e,N*abs(discr K))`
have trace distinct from the comparison value. It then concludes both finiteness of `Vlen` and existence of a finite set of these same representations whose sum of valuations, multiplied by 2, bounds `Vn`. The finite set is pairwise representation-isomorphism distinct, but its multiplicities and cardinality are unnecessary once each summand is zero.

The full `FOneCharU.oneChar_unramU` and `oneCharU_of_katoTwoW_rig_admI_automorphy` proofs were read. The closed inputs in `SmallClassNumbers.corGK_of` instantiate the latter theorem before supplying it to `propGK_of_numberU3U_of_oneCharU`. Therefore retaining this intermediate assertion uses the stipulated source assembly; it does not replace an old integer product by an unjustified divisor.

If every trace difference is an ell-adic unit, each valuation is zero. The inequality gives `Vn=0`. Its positive coefficient normalization and the separately supplied `Vlen != top` imply `Vlen=0`. The proof does not infer zero length from an `ENat.toNat` value without excluding infinity.

## 3. Datum and local level hypotheses

For ell greater than 2^31, choose the same field and character used in `ClassNumberThree.gd`: E=Q(sqrt(-3)), N=2, e=6, and trivial psi. Its complete proof supplies class number one, absolute discriminant 3, parity, coprimality, and the noncontainment condition. In particular the eta condition is proved using ramification at 3, whereas the relevant ell-cyclotomic extension is unramified there. The exceptional divisibility condition fails because ell-1 is greater than 12. Thus no datum hypothesis is lost in the numerical specialization.

For the rank-three branch, `Adm3U_s` retains `Th.Unl`, as well as the actual `Adm3Alt` condition. `KillsMu 2` is trivial, so the source level becomes one. Twisting rho by the inverse cyclotomic character gives weights (5,-1,-7). The full `Keep.levelCore_alt` and `levelKA_alt` proofs show that the supplied ordinary flag and witness hypotheses give fixed vectors at every finite place, including the coefficient prime, and infinitesimal character (6,0,-6). No conclusion of being spherical at the coefficient prime is inferred merely from an away-prime comparison.

The source's geometric-Frobenius convention and its algebraic Satake normalization yield the compact U3 trace with scale p^6. Thus the compact coefficient representation has highest weight (5,0,-5), and the proved scaled eigenvalue 157899 gives trace 157899/7^6.

The full U3 coverage audit checked the proved generic/pure-inner scope of KMSW Theorem 5.0.5, the archimedean sign and component group, the ramified-prime principal-series case, and the full lattice fixed vector. It did not apply a conjectural unrestricted packet theorem. Relevant primary locators and source PDFs are recorded in `../hecke_coverage/u3_coverage_archive_audit.md`.

## 4. The rank-two conductor reduction is complete

The actual source flag and diagonal inertia are retained. At primes different from ell, the characters factor through Gal(Q(mu_3)/Q), so actual inertia is finite; monodromy is zero. At ell the two flag characters after twisting are unramified characters times 1 and chi_ell^(-2e). Their unramified factors have unit Frobenius values. Exactness of D_st after a common finite semistable extension gives slopes differing by 2e. The relation N phi = ell phi N forces a nonzero N in dimension two to connect slopes differing by one, so N=0. The finite descent inertia is an extension of two trivial characters and is semisimple in characteristic zero; it is trivial.

The precise primary coefficient-prime source is Saito, *Galois representations in arithmetic geometry*, author PDF `suams.pdf`, section 2c, Theorem 3, p.9. It identifies the full Frobenius-semisimplified Weil–Deligne representations and retains N. The whole section 2 and rendered pp.8–9 were read. This is an exact classical Q statement, not an invalid specialization of a Hilbert theorem with degree greater than one. The original 1997 journal PDF was not recovered, and no original theorem number is claimed. Colmez–Fontaine section 3.3 p.21 and section 4.1 Proposition 4.2 p.23 supply the slope relation and exactness; section 4.2 Proposition 4.4 p.24 supplies the rank-one calculation. Carayol section 0.7 Theorem A pp.410–411 supplies the away-prime comparison, with its even-degree-field exception inapplicable to Q.

The nebentypus is consequently unramified outside 3 and has conductor dividing 3. Its odd parity forces chi_-3. At 3 exactly one of the two tame inertia characters is nontrivial, and N=0, so the primitive conductor is exactly 3. At a split p, R(sigma^-1)=p^e W(sigma^-1), hence the source rank-three trace is 1+a_p/p^e. For e=6 every such form lies in the complete computed S_13(Gamma_0(3),chi_-3), with no assumption about multiplicity one in the source finite set.

## 5. Exact Hecke and product checks

The complete `u3_hecke_section.tex` was reread. Its class-number-one argument, harmonic kernel and invariant line, seven explicit neighbor representatives, complete unit orbits, and positive/negative Hecke comparison were independently reconstructed. The complete standalone `u3_orbit_certificate.py` was read and executed afresh. It checks all seven Gram identities, line reductions, exhaustive orbits, the harmonic polynomial, and all integer evaluations. It returns 57 cosets at 7, weighted sum 315798, and scaled eigenvalue 157899. It also verifies the auxiliary 13 calculation. The current script SHA256 is `f448ae20e54a7d5346907f128e40401c3d3777f93f4280836ae3609c5ea3feec`.

The complete weight-13 basis and integer certificate had been independently constructed and executed earlier by this reviewer and subsequently audited by another agent. The monic polynomial is

P_7(X) = (X-40250)^2 (X+153502)
       = X^3 + 73002 X^2 - 10736848500 X + 248682833875000.

The new independent standard-library check `k12_product_archive_certificate.py` evaluates both the expanded polynomial and its factorization and checks the exact prime-power product and primality of each listed factor. It obtains

* E_7 = 13841404851;
* E_7-157899 = 13841246952;
* P_7(1+7^12) = 2651744832098840875904898134016;
* their product is 36703455074769833036351681539319447519232;
* the product factors as 2^15 * 3^19 * 7 * 13^5 * 37 * 43^3 * 47^3 * 61 * 271^3.

At every ell greater than 2^31, the numerator of the rank-three trace difference is a unit. In the rank-two branch all roots of the monic integral polynomial are algebraic integers. In any splitting field at ell, each difference (1+7^12)-a_7 has nonnegative valuation, and their product has valuation zero. Each difference therefore has valuation zero, including repeated roots. Division by 7^6 preserves this. This is a pointwise assertion for every actual admissible representation; no unsupported replacement of a trace product is used.

## 6. Strict duality and the coverage of all primes

The exact duality (K5) was reread and reconstructed for e=6. Finite Poitou–Tate gives the dual of H^2(S_ell,Z/ell^n(e+1)) as the kernel of localization of H^1(S_ell,Z/ell^n(-e)): the global and local H^0 groups agree because both cyclotomic images are Z_ell^times. This remains true when those invariant groups are nonzero. The finite-level systems satisfy the needed Mittag–Leffler condition; Pontryagin duality and filtered continuous cohomology then give the strict Selmer kernel with Q_ell/Z_ell(-e). There is no omitted local H^2 term.

The source's additional prime 2 condition is automatic: the unramified local H^1 group is D/(2^(-e)-1)D=0 by divisibility of D and the nonzero scalar. The bottom coefficient field has coefficient ramification index one. Hence zero source length implies zero K_12(Z){ell} by the étale K-theory comparison and exact strict duality.

All odd primes below 2^31 are covered by the published Vandiver verification, combined with the already proved vanishing equivalence (K2). The numerical verification itself was cited, not rerun. The prime 2 is covered by Rognes–Weibel as already established in (K4). There is no boundary prime ell=2^31, since that number is composite. Finite generation and the known zero rational even K-group make K_12 finite; vanishing of all primary parts therefore proves K_12(Z)=0 under the stated source contract.

## 7. Class-group, periodicity, and Soulé consequences

The class-group assertion uses only the established vanishing equivalence K_4k(Z){ell}=0 if and only if A_ell^[-2k]=0. Setting k=3 gives the component [-6]; it asserts no equality of full orders and no all-component Vandiver statement.

For positive k congruent to 3 modulo (ell-1)/2, the residual character -2k equals -6. The same vanishing equivalence gives the stated periodic vanishing. This periodicity is an equivalence of vanishing, not an asserted periodicity of K-group orders.

The full-domain Soulé theorem (K18) was reread in full. Its chosen Kummer normalization has image index equal to |K_(2m-2)(Z){ell}|, and the primitive rank-one H^1 generator restricts primitively to the full cyclotomic-kernel domain. For odd m=7 and every odd ell, the residual cyclotomic character has nontrivial Delta action, including ell=3; no exceptional-prime restriction is needed. Thus K_12=0 makes the full-domain kappa_7 image all of Z_ell. This does not imply primitivity on a deeper weight subgroup, which carries the separate factorial issue.

## 8. Editorial readback points

No mathematical correction is requested. Two integration points were sent to the root: consistency of the `VK-SOULE-INDEX` finding name and the earlier paragraph describing an exact trace calculation as a future target. A subsequent readback at 04:27 UTC verified both corrections in `k_groups_section.tex`: the theorem now explicitly includes `VK-SOULE-INDEX`, and the trace paragraph says the direct unit criterion and complete level-one calculation close e=6. No editorial point remains open from this audit.

The theorem is ready for integration with its explicit stipulated-source qualification and the described scope of the full-domain Soulé corollary retained.

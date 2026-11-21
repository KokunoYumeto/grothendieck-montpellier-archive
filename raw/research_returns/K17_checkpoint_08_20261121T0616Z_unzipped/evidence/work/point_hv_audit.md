# Host-family and PointHV source closure

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; effort setting not exposed.

## Final status

The initially cautious definition-only description can now be upgraded. `CountI` and `PointHV` both have closed forward compositions of inspected source theorem declarations under the main paper's stipulated source contract. No Lean execution was performed, and no numerical bound for the layer input was obtained.

`work/host_refinement.tex` supplies the complete mathematical statements, proofs of the orbit-counting and final arithmetic aggregation steps, and exact declaration locators. It has been read back in full. `work/point_hv_composition.lean` supplies an explicitly labeled uncompiled composition; it has also been read in full.

## CountI

`UpperTheory.V.U3.countI UpperTheory.V.SmallClassNumbers.corGK` is a closed term of type `HV.CountI`. The full 8,154-byte `UnitaryThreeGroups/CountI.lean` proof was read. It applies the field-dependent `CorGK` to K_chi = Q(sqrt(-p_K(chi))), rather than relying on the more strongly quantified `HV.CorG` definition.

For each source PChar chi, constants C,r_1,r_2 precede every host, twist, coefficient family, and finite prime set. A host consists of a >= 2 and primes q = 3 mod 8 and d = 7 mod 16, coprime to the modulus m. Its N is lcm(2^(a+2),m) qd. The Big(t) conditions and r_i < q,d are stated exactly in the fragment. CaseI is precisely ell outside B_chi and (ell-1) not dividing 2e, with ell odd separately required.

Finiteness accompanies the normalized-length estimate. The character set consists of characters factoring through the host field and having parity (-1)^e. Both positive even and odd e are allowed; no unqualified even-twist restriction was inserted.

`GdOfHost` and `Cases` were read in full. The prime p_K detects the field exclusion by ramification. The finite set B_chi removes prime divisors of the character order and the auxiliary quadratic class number. Grouping by character kernels and counting faithful characters of cyclic quotients gives sum_H phi(index H) <= phi(N) <= N. A fixed k absorbs 2 c5(log r_1+log r_2) into 16^k, and e+1 <= t yields C = k+1+A. This proves the ordinary statement in the fragment.

## Closed PointHV composition

Let hN be the closed `SmallClassNumbers.litN`; let hH be `published_hypotheses_from_patching_alt hN descWeak`. The exact closing sequence is:

1. `HVFinalU.pt_s hN` supplies Poitou--Tate; hN.coh supplies the two compact local inputs.
2. `KFinal.lemmaK_litN_alt hN` supplies an existential LemmaK witness, via the inspected `LemmaKOfLitN` and closed `BOdd.bOdd` calls.
3. The closed CountI composition above supplies the first count.
4. `AdjointLiftingOfCohomology.countII_and_countIII_of_printsH_of_sp4In hH hK (Sp4In0.sp4In0_alt hH)` supplies II and III.
5. `DnEndsTop.ends0_alt hH` supplies the reduced unitary lifting endpoint. `LinkedUnlE.count_v_of_printed_bound_k_reduced_unitary_lift hH hK (...) .2` supplies V. The exact source theorem and its calls to the full CountV theorem were read, including the local cohomology and HostVanE inputs.
6. `countZ X.propZ` supplies Z; `LevelCohomology/PropZ.lean` has a closed proof.
7. `JointWinOfCounts.pointHV_of_counts` applied to these arguments proves PointHV.

The assembly theorem `HVCore.of_four_alt` and the full caller `WindowBoundOfLiteratureLevel.vwin_of_hypotheses_H_E_alt` corroborate exactly this input package, but no reverse implication from VWin is used. The new composition stops at PointHV itself.

Every assembly file named above was fully read. Some additionally downloaded files were searched or partially read while locating the chain; no claim that every downloaded source file was fully read is made. The imported automorphy and arithmetic theorems remain the same source-contract inputs used elsewhere in the main paper.

## Exact remaining premise and output

For chi and an arbitrary function j:N->N, PointHV gives C and auxiliary primes. At every ell in the fixed finite bad set B_chi, its LayerLe premise concerns all cyclotomic ell-power layers F of degree ell^j(ell) over Q(mu_(ell*m)). The groups S_ell(F,e) for 1 <= e < t must have finite length and their unweighted length sum must be at most a common real B >= 0.

The conclusion is finite length of the source plus eigenspace over the host field at every odd ell and every 1 <= e < t, together with the weighted sum bound (N t)^C + C B over every finite odd-prime set. The eigenspace is the eigenvalue (-1)^e space for complex conjugation acting on cohomology including Tate coefficients. It is not always the literal +1 eigenspace.

The definitions `LayerLe`, `Lchi`, `IsLayer`, `VVat`, `VVplusLe`, and the earlier plus-action source definitions were checked. The source field descriptors are invariant under number-field presentations; they give exactly the cyclotomic base and layer stated in the fragment.

## Final combination proof

The full proofs of `FinalLe.sumIn` (263-line file), `SumOut.sumOut` (231-line file), `CountIV.countIV`, `CountVs.countVs`, `PointArith.point`, and `JointWinOfCounts` were read. They partition primes inside/outside B_chi, retain the cohomological finiteness assertions, and incorporate the actual layer bound through CaseIV. They do not discard the layer assumption.

Writing x=N t >= 2, let C_0 be the outside exponent, C_ell the inside exponents, D=sum C_ell and b=|B_chi|. Then C=C_0+D+b+bD suffices, since

    x^C_0 + b*x^D + b*D*B
      <= (b+1)*x^(C_0+D) + C*B
      <= x^(C_0+D+b) + C*B
      <= x^C + C*B.

Here b+1 <= 2^b <= x^b. This complete elementary argument was rechecked independently of the source tactics.

## Retrieval record

All new URLs use pinned revision `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`. Initial retrieval results are in `point_hv_retrieval_results.json`. Ten of those downloads were subsequently compared with the commit-pinned GitHub directory's independent blob identifiers, and their status was updated to verified. Further exact downloads used the parent's existing blob-verifying fetch script and are recorded in `point_hv_more_manifest_results.json`, `point_hv_final_manifest_results.json`, and `point_hv_link_manifest_results.json`. The directory metadata is saved in `point_hv_directory.json`. Two guessed names returned 404 and are retained as failed retrieval events; they are not used as evidence.

The distinction between retrieved-and-hashed and independently blob-verified records is preserved. No assertion that the public mirror is authenticated as a whole, or that this review rebuilt it, follows from these checks.

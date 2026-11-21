# DP57: independent complete CM repair and actual adelic endpoint review

**Verdict: PASS.** The complete original version was read at03:47:57 UTC; after the author's finite-étale Host strengthening, the entire final eight-section version was actually reread at03:50:10. Every claimed new explicit construction and every exact source-application hypothesis was checked. No mathematical correction is required. Main paper was not edited.

Checker: `/root/archive_binomial`, GPT-6 Astra Pro; runtime effort not exposed. Date:2026-11-21 UTC. Final whole SHA256: `94cbd0918b4cda91325d5715f1155f525de4ca304adaaad2643b0bd47bec849b`. The full checked snapshot, prior version identity, twelve-file exact source-range manifest and source-reading metadata are in `late_proof_snapshots/DP57_complete_archive_checked.md` and `DP57_archive_review_metadata.json`. This is a complete mathematical/source-interface review, not Lean execution or an audit of accepted global theorems.

## Field condition and literal unramifiedness

The source's `CMData` and `IsCMUnram` declarations were directly read. The latter really requires an integral theta whose difference from its conjugate is outside each maximal ideal. In Q(zeta7), every such difference vanishes modulo the unique prime(1−zeta7), because all integral elements are polynomials in zeta7 and both it and its conjugate reduce to1. Thus the original failure is exact and is limited to this interface.

For E'=Q(zeta7,i), the norm of zeta7−zeta7^(-1) is7, so that difference is a unit away7; at primes over7 the alternative difference2i is a unit. These choices also work at2. The elementary z+bar(z)=−1 and z*bar(z)=2 calculation gives delta²=−7 and identifies the real fixed field with F(sqrt7), of degree6. Cyclotomic degree12 and canonical conjugation give all the remaining CMData fields.

The added stronger statement is correct. At each local ring R=O_F',v, the chosen theta is nonreal and hence generates the quadratic field E'/F'. Its trace and norm lie in R, and its discriminant is a unit simultaneously at every prime above v. The quadratic order R[theta] is finite étale. Stacks Lemma10.163.9 (Tag033C), independently opened and read, makes it normal. Since its fraction field is E', it contains every element integral over R and is exactly the integral closure. This supplies actual everywhere finite unramifiedness; localization also proves the global finite-étale assertion. The explicit Host fields d=7, rt=−delta, w0=−z, conjugation, and the chosen complex root satisfy the literal source record, including d mod16=7 and 2w0=1+rt. `Datum.dom` is not included in that construction.

## Integral principally polarized J²

The diagonal E-action commutes with I=[[0,−1],[1,0]], I²=−1. E has unique quadratic subfield Q(sqrt−7), so E and Q(i) are disjoint; the unital field map E(i) into M2(E) is faithful. With compatible roots, zeta28=zeta7²*i^(-1), and the cyclotomic integer-ring theorem identifies Z[zeta7,i] with the full integer ring of E'. Thus the action is genuinely integral, with no isogeny or index left unresolved.

Product Rosati is matrix transpose followed by the original Rosati. It sends I to−I and E to canonical conjugation, hence does so on E'. The original principal polarizations therefore give a product principal polarization; an artificial factor7^6 is not needed. The six tangent characters are exactly both i-extensions of each old character1,2,3, giving the stated explicit type. This is a full degree12 CM action on a dimension6 abelian variety, even though the variety is a product.

Both displayed Frobenius orbits at11 and their indicator sequences were independently recomputed. Their sizes are6 and their Hodge dimensions4 and2. Their slopes agree with the two copies of the already established original factors. The local E'-field acts with six cyclic rational eigenspaces; Frobenius forces equal ranks, so a nonzero E'-stable local factor has height divisible by6. The memo correctly distinguishes those factors from the old height3 product summands and does not infer one-dimensional E'-stable formal groups from tangent diagonalization.

## Concrete source application at29

The residue2 has order28 modulo29: its14th power is−1 and its4th power is not1. Thus P=(29,zeta28−2) has residue F29 and is distinct from its conjugate, where the root becomes15. Cyclotomic monogenicity and simple roots make29 completely split; the selected completion is Q29. The singleton support with empty T-support satisfies the literal IsSplitSet and disjointness definitions.

The exact declarations were read: `InputsGenus.unimodGenus_holds` takes CMData and positive rank, `reduction_surjective_bis` proves the defined RedSurj proposition, and `AdelicLemmas.decoPtSurj_of` takes those two inputs plus precisely splitness and disjointness. Their hypotheses are all supplied. This is a valid application of named accepted results, not a re-proof or assumed substitute for their conclusion.

The complete generic `stepOf` constructor was read. With T=pi=1, empty T-support and f=6, the divisibility, norm, membership, cardinality, excluded-prime and standard-lattice index conditions all hold. Its U and chi fields are exactly the two IsLevOf requirements. No specialized X.Ok wrapper is needed. The generic `tieLevP` shows the same unit construction; its use of a support named Pr.vGs does not restrict the underlying generic constructor. Trivial residual character removes any additional extension choice.

## Actual Fi/adelic identification and period

The `fi_iff_FiC` statement and both directions were read, with its full surrounding variables. It requires CM datum, weak point-goodness, DecoPtSurj and IsLevOf, all now constructed. The source therefore identifies the exact finite coefficient-value space with actual adelic finite-weight values at the chosen representatives. It does not identify an arbitrary theta germ with such a vector.

The fresh principal29 level is free by the already checked DP55 argument: a finite lattice isometry trivial modulo P belongs to the torsion-free group1+29 M_n(Z29). Nonempty decorated classes and the nonzero extremal coefficient vector give a nonzero finite function and hence a nonzero adelic form. The actual perfect partner pairing gives a period-one witness. The result applies at the newly constructed level, not an unchanged previously prescribed level; that scope is explicit.

## Exact residual type and quantitative gates

The automorphisms3 and15 modulo28 belong to the selected type, generate all twelve automorphisms, and force the common restriction field to be Q. Thus this type is not induced from any imaginary quadratic field. The exact source HasType, CMObj and Datum.dom declarations impose the missing uniform two-fibre multiplicities/trace identity. Constructing Host does not supply Datum.dom or CMObj. Separately f=6 fails the old wrapper's8-divisibility condition, which is absent from the generic endpoint constructor.

The field degree and geometric dimension have doubled, and the endpoint level has changed. The principal polarization still has degree1. No coefficient-height, mass, norm or total-cost bounds are supplied. The construction proves actual endpoint interfaces and nonzero periods, without showing that a prescribed theta lift reaches those vectors or that the surviving height3 product directions can replace the E'-eigenbasis for free. It proves no shorter-chain or no-shortening theorem.

## Known primary facts

Milne's official *Algebraic Number Theory*, version3.08, was directly opened. The readable PDF text of Proposition6.2(b),(c) and its residue statement, and Theorem6.4(a),(b), was examined at the exact printed pages cited by the memo. These give precisely the cyclotomic ring and prime facts used. The screenshot tool supplied placeholders in this pass; the present check does not claim a separate visual reading of those pixels. The Stacks normality statement was independently read at its exact tag. Known theorems are cited/applied, not re-proved in the mathematical review.

## Intended integrated version — whole reading

At2026-11-21 03:55:21 UTC I read the entire intended LaTeX proposition, proof and scope paragraph. **PASS**: complete final memo content retained, including literal finite-etale Host, integral principal J² and local heights, all generic adelic constructor hypotheses, fresh-level period1, and residual two-type obstruction. FragmentSHA `1726637d4732a912abee1585d9e71670543d5057ec241a7d61819cbc846d02a1`; complete proposition/proofSHA `4d7e76bca7412f3850a2ba7a6f237e9d9e7a22365cda3daaffd4c33d3964d886`. Current exact main fragment count=1; complete proposition/proof count=1. Actual whole integrated reading, not just a hash comparison. Snapshot and metadata are under `late_proof_snapshots/DP57_integrated_archive_*`.

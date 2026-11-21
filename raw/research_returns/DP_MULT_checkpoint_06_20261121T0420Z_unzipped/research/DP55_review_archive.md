# DP55: independent complete endpoint-detection proof review

**Verdict: PASS.** The complete eight-section memo was actually read, and all substantive steps were challenged against the exact source interfaces. No mathematical correction was required. The main paper was not edited.

## Provenance and scope

Checker: `/root/archive_binomial`, GPT-6 Astra Pro; effort not exposed by runtime. Date: 2026-11-21 UTC. Complete memo read observed at03:35:03; exact source/dependency challenge through03:36:08. Whole SHA256: `501e96954b863d39e7c8eea9f25777d8997dfe48ccee5aafcba8e2cab01e21c2`.

The complete checked memo and twelve-file source-range manifest are preserved in `late_proof_snapshots/DP55_complete_archive_checked.md` and `DP55_archive_review_metadata.json`. This is a mathematical and declaration-level check, not Lean execution. No accepted RH proof or unrelated formal theorem was audited. A guessed missing `GSet.lean` path was not read; the actual needed `GSetLemmas.lean` and `Record.lean` declarations were read instead.

## Exact source space and row surjectivity

The codomain is precisely `Ev.Fi`, the complex span of evaluated K-valued equivariant functions (Record.lean224), not the whole ambient function space. `TiedValFi.lean16–133` gives exactly the classwise coefficient-span and stabilizer-invariance characterization. The averaging proof is valid over K because each finite stabilizer has nonzero order in characteristic zero. Complex coefficients are retained outside those averages, so no unwarranted K-valuedness of an arbitrary element of Fi is used.

The round/square pairing is the actual normalized bilinear Fock pairing `pairBK`, not a hermitian pairing substituted for it. Its invariant and nondegenerate theorems are actual proved declarations (`CoefModB.lean188–203`), and the finite-dimensional representability step is proved in `TiedPer.lean204–219`. The inverse finite characters cancel in the exact `perDua` constructor232–239. No common quadratic field is an input there.

The partner equation is linear in its tested coefficient x. The hermitian form is conjugate-linear in the first slot, so `H(phi(d),x)` is a K-linear functional in x and can be represented by the bilinear pairing. The displayed equivariance calculation has the correct inverse and representation orientation. `partner`, `jOf_partner`, `jOf_smul`, and `jOf_onto` were all directly read. The representing vector uses conjugated complex row coordinates; passing from generators to their complex span requires precisely `sum conjugate(t_i) z_i`. Thus J is conjugate-linear and onto exactly Fi.

The abstract source theorems require point-goodness, invertible coefficient Gram, and a row basis. Their later endpoint wrappers use `X.Ok` only through `ptOk`. DP52 supplies the weakened point/row goodness; the same `perDua`, basis and Gram declarations apply. This checks that the failed quadratic-field wrapper is not reintroduced indirectly.

## Positive detection and exact period identity

`RecordInst.lean48–58` identifies the evaluated coefficient Gram with `roundPk_gram_pos`. The latter declaration and proof at `NonDeg.lean407–412` were read: it assumes the coefficient record and an embedding, with no `X.Ok` or quad hypothesis, and is genuinely positive definite. Therefore the coefficient hermitian form is positive on the evaluated coefficient span, not merely nonsingular.

The exact period formula in `Record.lean315–337,1568–1589` and the conjugate-linear representing map give `per(F,z)=ipCl(Jz,F)` with the stated slot order. Reciprocal stabilizer orders are strictly positive. Every nonzero Fi vector has a nonzero class value, so selecting Jz=F gives a strictly positive period. This argument needs no free action. No estimate for the row coordinates follows.

## Auxiliary principal level and freeness

The new auxiliary level is a trivial subgroup of the actual finite residual general linear group (`ColForms.lean16–37`), not a claim that the entire adelic compact group is trivial. The source permits an arbitrary finite support; no conjugate-pair closure is required at this endpoint interface. One auxiliary place is enough.

The torsion-free congruence lemma is correct for odd unramified residue characteristic. A nonidentity finite-order element has a power of prime order; writing its first nonzero depth as `ell^a C` with a unit entry gives the displayed nonzero first terms. In the order-ell case, every intermediate binomial term has valuation at least a+2, and the last term satisfies a*ell >= a+2, including the limiting case ell=3, a=1. Matrix binomial expansion is valid because the identity commutes with C.

A lattice isometry preserving the positive definite trace form belongs to a finite group, so its order is finite. Stabilization and the exact decoration action (`StdLatUnimodular.lean108–111`) imply equality of residue-coordinate maps after the inverse isometry. Additivity and the kernel field89–94 then give `(g^{-1}-1)N subset P N`. Completion makes the lattice free and P generated by ell, so the local matrix lies in the torsion-free principal congruence subgroup. The embedding of E into its completion is injective, hence local identity implies global identity. Surjectivity of every remaining residue decoration then forces every finite h-component to be identity. This proves freeness of the entire source action, with no omitted finite-character or quad condition.

The weakened goodness proof still applies to the refined level: the relevant source proof `ColFormsLemmas.lean83–119` uses conjugation on E and K, coefficient equivariance, and finite characters, all retained. Finite class number and finite stabilizers are not being inferred from freeness alone.

## The normalized period-one witness

The source decorated set has its explicit base object (`StdLatUnimodular.lean650`) for positive endpoint rank. The coefficient module contains the nonzero highest-weight extremal tensor (`CoefColLemmas.lean320–342`). At a free action, `resFree` identifies equivariant functions with arbitrary coefficient values on class representatives. Thus the point and row functions supported on one class with values x,y and B(x,y)=1 exist. Choosing the embedded K-coordinates of the row function makes `perCl_emb` collapse to one term with stabilizer weight one. Its value is exactly sigma(1)=1; no untracked complex conjugation or normalization remains.

This works for the actual mixed type123 after the weak DP52 construction and at every admissible rebuilt even lift count. It changes an auxiliary level and supplies no level-cost bound.

## Adelic and global scope

The complete `fi_iff_FiC` statement and both proof directions in `TiedValFi.lean239–255` were read. It uses CM datum, point-goodness, DecoPtSurj and IsLevOf; it has no Fields.Ok argument. The memo correctly keeps the decorated/adelic identification hypotheses explicit and does not infer them from local formal-group information. Later source wrappers can still use Fields.Ok; the abstract theorem itself does not.

The result establishes detection of every nonzero vector in the exact endpoint space, and nontriviality plus a period-one example after a principal auxiliary level. It does not place the prescribed iterated theta image in that space, prove it nonzero, identify the finite global theta-jet realization with the required kernel family, or control the detecting row vector, level, norms or heights. It therefore proves neither an actual shorter global chain nor impossibility of shortening.

## Main-paper editorial recommendation

The research memo usefully retains the full arguments. In the paper, known abstract facts may be cited exactly: `TiedPer.jOf_onto`, `jOf_mem_Fi`, the positive Gram theorem, and `TiedValFi.mem_Fi_iff`. The new proof should emphasize substitution of DP52's weaker goodness, the principal-level torsion/freeness argument, and the exact period-one construction. No full reproving of those unchanged background theorems is necessary.

## Complete intended integrated version

At03:37:20 UTC, the complete proposition, all proof paragraphs, and the final scope paragraph of `DP55_integrated_fragment.tex` were actually read against the checked original memo. **PASS**: all three claims, conjugate-linear partner/surjectivity, positivity, exact Fi characterization and adelic hypotheses, complete principal-level argument and period-one normalization are preserved. Fragment SHA256: `4b35c270efb26002060248e9e0b606f416a8fbf24d5785dd9cd4213dd6ec5adc`; complete proposition/proof SHA256: `7edda95a3ba291383c54f7590d0e73a0f8c30398ac287ec2748644db5094614d`. Exact current main-fragment count at capture: 1. This is an intended-fragment reading and preservation event, not a second independent proof of the unchanged memo. Metadata is saved separately.

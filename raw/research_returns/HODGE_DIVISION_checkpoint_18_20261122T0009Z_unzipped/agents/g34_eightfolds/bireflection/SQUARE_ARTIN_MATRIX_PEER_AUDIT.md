# SF-E837 — independent whole-proof audit

**Result: PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, run HODGE_DIVISION. Report written at the actual UTC time recorded in `CHECK_EVENTS.tsv`. The complete mathematical proof, complete author program, and complete author output were read. No mathematical repair was requested.

Reviewed frozen manuscript:

`agents/sixfolds/rm_square_artin_matrix_obstruction_draft.md`

SHA-256 `f076fc5a22600fc88b0811b6550951b2c47a42b9e1eef7cf25bbbe5b889a4972` (196 lines).

The author's `rm_square_artin_matrix_certificate.py` and `_output.json` were read in full. The independent supplement is `audit_square_artin_matrix.py` / `.json` in this directory. It first completed successfully at **2026-11-21 21:55:17.283081 UTC**, in **0.137928210 seconds**. The final tool output was truncated by the context boundary; the retained complete JSON was subsequently opened and its successful status and frozen proof hash verified. This was an output-size issue, not a failed mathematical test.

## 1. Universal filtered matrix lemma

I independently checked the proof for every matrix size, without assuming diagonalizability, commutation of matrix entries beyond the coefficient ring, or an equivariant presentation.

Let `A = C[t1,t2,t3,t4]/(t1²,t2²,t3²,t4²)`. If four distinct quadratic edge monomials annihilate the cokernel of a square matrix `C`, the conclusion that `C` is invertible is valid. Elementary invertible row and column operations split all unit pivots and preserve the cokernel. A remaining nonempty `k × k` block has every entry in the maximal ideal. Modulo its cube, write this block as `C1+C2`, where `C1` is linear and `C2` quadratic.

For the linear map `L: C^k → V ⊗ C^k` given by `C1`, put `a=rank L`. The pure degree-two part of the image is exactly

`C2(ker L) + V · im L`.

Indeed, a constant input contributes no degree-one term precisely when it belongs to `ker L`; degree-one inputs contribute through `C1`; higher inputs have no degree-two contribution. Its dimension is at most `(k−a)+4a ≤ 4k`. The four independent edge annihilators force the `4k`-dimensional subspace `J ⊗ C^k` into that image. Equality therefore forces `a=k`, eliminates the `C2(ker L)` contribution, and gives `V · im L=J ⊗ C^k`.

Write `C1=Σ ti Ai`. For an omitted edge `ij`, multiplication by `ti` forces `Aj=0`, and multiplication by `tj` forces `Ai=0`. The two distinct omitted edges together contain at least three vertices. Consequently at most one coefficient matrix survives, and then `V · im L` has dimension at most `3k`, contradicting `4k`. This proves the lemma for arbitrary `k`; the finite graph supplement does not substitute for this proof.

## 2. Actual companion equations and equality of lengths

I reread the complete preceding E836 draft, with particular scrutiny of its actual companion construction in §§2–3, and compared it with E837's use. Both matrix orders

`Cπ Bij = Bij Cπ = Pπ,ij I`

are justified. The extension matrices `Bij` are the same for both bivectors; only `Cπ` depends on the deformation. The first order follows from the lifted presentation relation and the map to the free hull. The opposite order follows from the commutator on lifted torsion. Terms passing through the ordinary free splitting cancel. The required lift exists because finite-length modules over the four-dimensional regular local ring have no Ext in degrees below four, giving the stated `Ext¹(M,R^r)=0`.

The equality of multiplicities follows from the previously reviewed E819 finite-perfect-cone supertrace argument: the two defects have lengths `16n` and `16m`, so a nontrivial proposed simultaneous deformation forces `n=m>0`. E837 does not infer equal matrix sizes from a numerical Chern-character identity alone.

This audit reuses the previously whole-reviewed E819 published-source bridge in its exact stated scope. The complete E836 mathematical text was reread, but I did not freshly audit its upstream Eisenbud–Ulrich theorem. E837 does not need that general complete-intersection Jacobian-socle theorem: the square algebra and its socle are explicit.

## 3. Nonlinear regular parameters and constant bivectors

For arbitrary formal regular parameters `ui`, the coefficients `aπ,ij(t)=π(dui,duj)` need not be constant. The presentation nevertheless gives

`Pπ,ij = 4 ti tj aπ,ij(t)`.

Associativity of the two companion systems gives the scalar cross-minor relations. For complementary edges, the product is a multiple of the nonzero socle `t1t2t3t4`; every positive-degree contribution to either coefficient vanishes. Thus the constant bivector coefficients satisfy exactly

`pij qkl = qij pkl`.

The constant Jacobian is invertible. Hence the two constant skew forms `p,q` remain decomposable rank-two forms with nonzero mixed wedge. No claim that all formal parameter changes preserve constant bivector coefficients is used. No reducedness assumption on the Artin ring is used in the scalar argument; the scalar coefficients at this stage lie in `C`.

If the union of the two edge supports has at most three elements, it has at most one complementary pair. With none, the mixed wedge is zero immediately. With one, write the relevant coefficients as `a,b,c,d`. Decomposability gives `ab=cd=0`, while the cross relation gives `ad=cb`. The common number has square `abcd=0`, so it is zero, and the mixed wedge again vanishes. Thus at least four edge coefficients occur.

## 4. Matrix pencil and final contradiction

Choose a nonzero scalar `λ` avoiding the finite set of cancellations, so that every coefficient in the union support is nonzero in `p+λq`. The actual matrix `Cλ=C+ + λC−` satisfies

`Cλ Bij = Pλ,ij I`.

This is an algebraic matrix pencil; the proof does not assume that it is supplied by a third quantization or third Hochschild deformation. Each selected coefficient is a unit of the Artin ring, so its associated quadratic monomial annihilates `coker Cλ`. The universal lemma makes `Cλ` invertible.

Substitution into the plus equation gives, for `D=C+ Cλ⁻¹`,

`D Pλ,ij = P+,ij I`.

Taking degree two yields `(pij+λqij)D0=pij I`. One nonzero pencil coefficient forces `D0` to be scalar; the collection then makes `p` and `q` proportional. The nonzero mixed wedge rules this out. This step does not commute `C+` with `C−` or interchange inverse factors unjustifiably.

## 5. Global interpretation and examples

The globalization uses only the actual E819 interface: balanced weak semiregularity for a finite coherent action forces the two invariant Hochschild evaluations to vanish, and forgetting the action and completing yields the two flat first-order module deformations. The fixed `B`-field shear leaves the relevant bivector pieces unchanged. There is no assumed action on the chosen local presentation.

The examples are actual coherent sheaves. A formal finite-colength ideal contains a power of the maximal ideal, so its quotient is an algebraic finite quotient. A surjection from the stated rank-32 bundle exists for the permitted multiplicity. The extension is a coherent extension of its kernel by the finite-length torsion, and its hull and defect are the claimed ones. The dimension `96m²` is the Koszul `Ext²` dimension `6 · 16 · m²`. The torsion and quotient cancel in the full Chern character. Neither a group action nor indecomposability is asserted merely from these calculations.

The theorem concerns a common formal-square quotient. It does not claim every Artin algebra, every complete intersection, arbitrary distinct defect algebras, or arbitrary derived objects.

## 6. Independent exact supplement

The independent program imports no author code or selected output. The author program had been read before this separate program was written. The illustrative rational boundary data come from the manuscript; their identities are independently reconstructed rather than presented as newly discovered data.

The program performs:

1. All 15 four-edge subsets of the six-edge complete graph. For each, it constructs the omitted-edge coefficient constraints as an exact matrix, computes its nullspace, and computes the multiplication-image dimension. Twelve have constraint rank three and possible degree-two image dimension three; three have rank four and possible image dimension zero. All are strictly below four.
2. All 42 subsets having at most three edges, checking the complementary-pair statement.
3. An independent rational decomposable-column construction of the two constant forms, with orientation determinant `−4/5`.
4. A generic four-parameter nonlinear shear

   `u1 = l1 + αl2l3 + βl2l4 + γl3l4 + ηl2l3l4`,

   with the remaining coordinates unchanged. Quotient arithmetic uses exact polynomial monomials and discards any exponent at least two; it does not reuse the author's bitmask implementation.
5. All 36 ordered scalar cross minors, both self-Pfaffians, the mixed socle coefficient `−64/5`, and the incompatible constant ratios `1/2, 1/3, 1/4` (each occurring twice).

The certificate binds the exact reviewed manuscript hash. It is supplementary finite and symbolic evidence. The all-size matrix lemma, actual deformation/Ext interface, and global argument were checked as proofs, not claimed to be certified by finite sampling.

## 7. Source and review classification

The new filtered-matrix and support arguments are elementary and were checked in full. E819's published Buchweitz–Flenner compatibility and local quantization bridge are carried in their previously reviewed exact scope; supplied S20/S21 retain their recorded status. No Markman/032 theorem has been promoted to an unconditional premise. No new external classification, unrefereed theorem, or undocumented computer table is used by E837.

The review comprises a **targeted proof check of the whole proof**, a separate **computation or formal certificate**, and a **used and rechecked in this run** event for the actual companion/deformation interfaces. It does not claim a new independent derivation of the entire manuscript or a fresh reconstruction of every earlier published input.

# P-F17: fixed semisimple branching and fixed inner plethysm

Author/checker: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Date: 2026-11-21 UTC.

## What is now proved

`positivity_fixed_plethysm.tex` applies P-F16 to one fixed semisimple homomorphism `rho:H->G`. It verifies the previously abstract algebraic gate using the actual universal branching algebra

`R_rho=(C[G]^(U_G) tensor C[H]^(U_H))^H`.

There are finite constants `L_rho` and `C_rho`, independent of the stretched highest weights, such that every nonzero ray has a positive rational form with all denominator weights `L_rho`, positivity and saturation indices at most `C_rho`, and the source's **canonical modular index**, defined using a lexicographically minimal h.s.o.p., at most `L_rho`.

The fixed-inner plethysm conclusion is for **fixed n and fixed mu**. Restricting the fixed representation to `SL_n->SL_m`, with `m=dim S^mu C^n`, gives the same graded canonical multiplicity algebra on centrally balanced rays. Therefore the bounds also hold uniformly in the outer/output weights for this fixed pair `(n,mu)`. The constants are not shown to grow polynomially as `(n,mu)` varies. Fixing only `mu` while allowing `n` to grow is not claimed.

## Exact source passages inspected

Primary source: the supplied GCT VI LaTeX at `sources/LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex` and the corresponding PDF text at `work/positivity_sources/GCTVI.txt`, arXiv **0704.0229v4**, <https://arxiv.org/abs/0704.0229>.

- **Proof of Theorem 4.4.1**, printed pp. **75--76**, equations **(4.7)--(4.8)**: finite generation of the two right-unipotent invariant algebras, their left-group/right-torus decomposition, and Hilbert finite generation of the diagonal reductive invariant algebra. This supports the fixed ambient multigraded algebra, not only finite generation of its support semigroup.
- **Section 3.5.1**, printed p. **59**: reduction to the highest-weight projective orbit and rational singularities of its affine cone.
- **Theorem 3.4.1(b)--(c)**, printed p. **57**: quasi-polynomiality and normal rational canonical rings for subgroup restriction.
- **Proof of Theorem 4.1.1**, equations **(4.2)--(4.3)** and **Lemma 4.1.3**, printed p. **67**: the opposite-degree torus invariant construction followed by reductive invariants, rational singularities, and global quasi-polynomiality. The paper uses Boutot's theorem here. The proof under review identifies its actual ray algebra with this construction and uses this verified source statement; it does not claim a new independent proof of Boutot's theorem.
- **Section 4.1.2**, equation **(4.5)**, printed p. **69**: the explicit canonical algebras `R=direct sum V_(n lambda)`, `S=direct sum V_(n lambda) tensor V_(n pi)^*`, and `T=S^H`. This is the clearest exact locator for the canonical ray, with its multiplication supplied by the preceding construction.
- **Section 4.1.1**, printed p. **68**: the canonical modular index uses the largest entry of a lexicographically minimal parameter-degree sequence. The proof includes the extra extension argument needed for this definition; it does not substitute minimum possible maximum degree.

These are direct source-text inspections. No new scan-image inspection of those pages is claimed. The invalid numerator index in display (4.4) is not used; the earlier P-F12 diagnosis remains in force. The isolated degree-zero value on empty rays is excluded from global quasi-polynomiality rather than silently using the source's overbroad wording there.

## Actual whole-proof check performed

I read the entire written proof after drafting, including the later canonical-index and GL-to-SL algebra paragraphs. This is a **same-agent targeted whole-proof check**, not a formal certificate or an independent re-proof. The audit included:

1. Correct right-weight labels: `(lambda*,pi)` in the universal algebra gives `(V_lambda tensor V_(pi*))^H=Hom_H(V_pi,V_lambda)`. The duality involution is linear and preserves dominance.
2. Domain and finite generation: the tensor algebra embeds in the coordinate ring of the irreducible product group, and taking invariants preserves the domain property. The source's finite-generation proof works for homomorphisms with kernel as well as embeddings.
3. Strict positivity of the multigrading: the sum of simple-coroot pairings is positive on every nonzero dominant weight for semisimple groups. This is exactly why determinant-unit problems of the full general linear universal algebra are avoided.
4. **Actual multiplication**: matrix coefficients of a highest vector give the degree-one section module. Products land in the specified irreducible right-weight component and are nonzero in the domain, hence span that component. This identifies the inherited multiplication with the Cartan section-ring product. The opposite-degree tensor diagonal is therefore the source's actual canonical invariant algebra, not an unrelated ring with the same dimensions.
5. Weight-zero conventions: when one highest weight is zero, the external section-ring grading gives `C[t]`; a nonzero joint weight still distinguishes ray degrees. The pair `(0,0)` is handled separately. A ray with no positive-degree invariant has algebra `C` and is assigned zero constituent indices without calling its isolated `f(0)=1` a global quasi-polynomial.
6. Known rational-singularity and quasi-polynomial inputs: they are applied to the same canonical ring after the multiplication identification. No purity argument or unproved generality about arbitrary branching rings is inserted.
7. Canonical modular index: powers of homogeneous generators lie in degree `L`, so the degree-`L` ideal has radical the irrelevant maximal ideal. After a partial parameter sequence, generic degree-`L` elements avoid the positive-dimensional minimal components and reduce dimension one at a time. Thus every partial parameter sequence extends using only degree `L`. Induction on a lexicographically minimal nondecreasing degree sequence bounds every entry by `L`. This closes the distinction between an all-`L` parameter system and the lexicographically defined source index.
8. GL-to-SL reduction: the restriction lands in `SL_m` because connected semisimple groups have no nontrivial algebraic characters. Central balance is precisely `|pi|=|mu||lambda|`. A balanced `SL_n`-equivariant map is `GL_n`-equivariant because the center acts identically and generates `GL_n` together with `SL_n`.
9. **Canonical ring compatibility under GL-to-SL**: restrictions of matrix coefficients are degreewise nonzero maps between the same irreducible `SL_j` representations and preserve products. External grading prevents collapse when the restricted highest weight is zero. Central balance makes the two invariant subalgebras equal. Hence parameter degrees and their lexicographic minimum genuinely transfer; this step uses more than coefficient equality.
10. Trivial groups, one-dimensional inner representations, empty partitions, and determinant-only weights reduce to the separately treated constant/zero cases. The chosen homomorphism need not be faithful.

I corrected two accidental literal plus signs and the phrasing about choosing Borels with unipotent radicals and maximal tori. Independent reviewers also suggested replacing “nonconstant ray” by the algebra condition and explicitly sorting parameter degrees. Those clarifications are applied.

## Independent review status

Both `/root/plethysm` and `/root/complexity` read the whole proof and exact GCT VI source passages. Both separately checked the subsequent canonical-index and GL-to-SL algebra additions and reported **PASS**. Their actual check events belong in their reviewer-owned ledgers; this author note does not duplicate or pre-count them.

## Remaining mathematical and algorithmic question

The qualitative fixed-embedding gate is closed in this semisimple setting. P-F18 subsequently proves a qualitative finite envelope depending only on the inner dimension for ordinary general-linear plethysm. P-F19 then refutes **polynomial growth of the canonical modular index** in that family: a single cubic inner representation in a varying number of variables has canonical index at least `2^(n-1)` while the source parameter is `O(n^6)`. Thus a polynomial bound for canonical parameter degrees as the embedding varies is no longer an open target of this argument.

The later P-F30--P-F31 close the weaker positive-form gate: the complete cubic-support classification makes the chain curve the unique fixed support, and the generically smooth fixed-component argument gives an actual primitive-`2^(n-1)` pole. Every rational denominator presentation therefore contains a weight divisible by that number. Thus polynomial growth fails even for the existence clause of ordinary PH3. This is not inferred from P-F19's parameter-degree lower bound alone. I independently checked P-F30 and P-F31 in full, with events in `cross_full_cubic_support_checks.tsv` and `cross_actual_cubic_pole_checks.tsv`.

PH2 and SH(a) remain open. P-F32 supplies a polynomial lower bound of order the square root of the number of variables, not a refutation. P-F12's implication from suitably bounded positive-form weights to PH2 remains valid even though its premise now fails in general. The earlier warning that an affine covariant-slice period cannot be transferred to simultaneous rays using quasi-polynomiality alone remains valid.

The P-F17 theorem itself is unchanged and remains valid for each fixed homomorphism. Its proof gives no polynomial-time procedure for producing the positive forms and does not reinstate the broad rank-only hypotheses refuted by the torus examples. No historical-priority claim is made.

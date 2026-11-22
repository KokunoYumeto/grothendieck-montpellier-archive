# Independent whole-proof audit: cyclic normalizers of projective PSL3(4) modules

**Outcome: PASS.** Reviewer `/root/imprimitive`, GPT-6 Astra Pro,
reasoning effort inherited/not exposed, run `HODGE_DIVISION`, 2026-11-21,
approximately 18:31–18:35 UTC.

## Material read and frozen identity

I read the entire proof `agents/g34_eightfolds/bireflection/l34_normalizers/normalizer_coverage.tex`,
its adjacent `normalizer_bibitems.tex`, and every line of `check_multiplier.py`.
The proof SHA-256 is
`b6a53359d99547f2ed8f302f168771e37a30055a79f6d4d89378c07b646cd2c8`.

I freshly read the complete invoked primary-source passage, Breuer–Malle–O'Brien,
*Reliability and reproducibility of Atlas information*, §3.3 introduction and
§3.3.1 through Lemma3.1, author pp5–6. This is the published research article
in Contemporary Mathematics694 (2017),21–31, DOI10.1090/conm/694/13960.
The retained author PDF has SHA-256
`0f619a98eb52cdb2622b6c4fa6a71d1c454442c1d141ab77d18f28bdf4d3512f`.
The public author URL is
https://agag-malle.math.rptu.de/~malle/download/atlas.pdf .
My new web attempt timed out; I read the complete passage in the already
retrieved original author PDF/text, not a secondary review. The complete
classification is cited as a published input, not newly proved here.

## Mathematical review

1. **Cyclic extension of a representation.** If `bP` generates a cyclic
   quotient of order `d`, an intertwiner `T` has
   `T^d rho(b^d)^(-1)` scalar. Rescaling solves the actual `d`th-power
   relation, and the usual normal forms `p b^j` give a genuine
   representation. This is valid for a nonsplit extension. Its restriction
   is irreducible, so the extension is irreducible. No false identification
   of different central power relations is made.

2. **Isoclinism and conjugation.** The induced isomorphism of central
   quotients agrees with the commutator-group isomorphism on every
   commutator, hence on the whole derived subgroup. Faithfulness of each
   cyclic outer quotient puts the full center inside the derived subgroup
   and identifies the cyclic quotients. The commutator identity then
   transports the actual conjugation of a chosen coset generator. Thus the
   old intertwiner extends to the new cyclic group after a scalar change.
   This proves the needed projective-spectrum statement; it does not
   assert equality of character tables or element orders under isoclinism.

3. **Reduction of a normalizing matrix.** A nontrivial projective
   representation of the simple group has a central kernel on its
   universal perfect cover. The faithful matrix image has cyclic center
   by Schur's lemma. If the normalizing matrix induces an outer class of
   order `d`, its `d`th power induces an inner automorphism. An
   automorphism of a perfect group inducing the identity modulo its
   center is identity, because its central discrepancy is a homomorphism
   to an abelian group. Therefore the `d`th matrix power is scalar times
   a core element. Rescaling produces a finite group with precisely `d`
   cosets, perfect derived group equal to the core, and faithful cyclic
   outer quotient. All hypotheses of the cited bicyclic classification
   and the isoclinism lemma are met.

4. **Completeness of the list.** The paper expressly classifies all36
   bicyclic extensions up to isoclinism. The eight core types and outer
   profiles in the new proof match the full displayed published list.
   Arbitrary kernels of the multiplier character are allowed; they are
   not assumed characteristic. Both order-four central-cover types and
   all their three involution extensions are retained, as are the
   order-three and order-six outer extensions of the appropriate cores.

5. **Scope of character selection.** Every constructed extension has
   irreducible core restriction, so checking all such rows in the36
   tables is sufficient. Adding rows nonfaithful on the core center can
   only enlarge the tested set. The proof correctly separates this
   coverage theorem from the numerical character-spectrum checks.

6. **Source-label discrepancy.** The displayed action sends the named
   `2_2` to inversion on `C4^2/<a>` and identity on `C4^2/<ab^2>`.
   The following source prose reverses these two centralization labels.
   I independently confirmed the discrepancy. Neither the complete list
   nor the argument depends on those two labels, and both cover orbits
   are included. No unnoticed omission results.

## Independent finite reconstruction

I authored and executed `independent_check.py` in this audit directory.
It imports no author program, selected kernel list or character-table
data. It uses abstract pairs `(i,epsilon)` for the dihedral group of
order12, matrices over `Z/4` for the two multiplier coordinates, and a
sign action on `Z/3`. It independently reconstructs all48 multiplier
characters and their20 distinct kernels, the8 kernel orbits, and all36
simultaneous orbits of `(kernel, cyclic outer subgroup)`.

**Actual result: PASS**, retained in `independent_check.json`. The complete
center-order/outer-order profile agrees with the published list and author
check. The source-label discrepancy is independently verified. This is a
new finite structural reconstruction; I did **not** rerun or independently
reconstruct the separate36-table character-spectrum calculation.

No mathematical gap was found in the reviewed proof.

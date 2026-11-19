# Geometrically simply connected surface gate: audited proof note

**Integration update, 2026-11-19 07:44 UTC:** the full proof is now the
numbered theorem `thm:B-simply-connected-surface-gate` in
`sections/b3_simply_connected_surface_gate.tex`, included from Part B.
Its exact fixed-field statement incorporates the inherited numerical
conditions. The typeset discussion adds an explicit cyclic Fermat-quotient
family proving strictness of the intrinsic class after finite extension,
with complete finite exponent certificates. The earlier pending wording
below describes the checkpoint-06 state and is retained as audit history.

Written 2026-11-19 after the checkpoint-06 main-file freeze. The argument
below is a proposed strengthening of the already proved irregularity-zero
surface gate. Root, C and D have independently read this entire written
proof and passed it. B has also read the exact SGA passages listed below,
Yuan Theorem 4.5 and its proof, and the exact Néron-isogeny passages.
The final numbered theorem is pending after checkpoint 06. No assertion
of the restricted Tate conjecture is made.

## Statement

For each fixed finite field k, divisor Tate for all smooth projective
geometrically integral surfaces over k is equivalent to its restriction to
surfaces Y satisfying all of:

- geometric étale fundamental group trivial;
- H¹(Y,O_Y)=0;
- canonical bundle very ample.

The already proved arbitrarily large K² and p_g and slope-near-one
conditions can be imposed at the same final cut. They are inherited
numerical consequences, not separate additional gate movements.

## Proof construction

Start with Yuan's proof of Theorem 1.6, Sections 4.1–4.2. A smooth
surface X is reduced, over the same k, to BSD for a semistable abelian
variety A over K=k(t) whose Hodge bundle on P¹ is ample. If A=0 the
original Tate statement is already known, so assume dim A>0. Yuan
Theorem 4.5 gives a smooth projective total space P over k, a proper
flat map P→P¹, generic fibre A∨, and

    R¹ψ_*O_P = Lie(𝒜/P¹).

Thus H¹(P,O_P)=0. The generic zero section extends to all P¹ by the
valuative criterion of properness. This provides a section and a
k-rational point.

### 1. The geometric fundamental group is finite abelian, of order prime to p

Choose a nonempty open U⊂P¹ where P_U is the abelian scheme extending
A∨. On geometric base change, the proper smooth homotopy sequence is
exact:

    π₁(A∨_{Kbar}) → π₁(P_Ubar) → π₁(Ubar) → 1.

The section splits the last map. The dense-open map
π₁(P_Ubar)→π₁(Pbar) is surjective because P is normal. The section's
π₁(Ubar) image is killed in π₁(Pbar), since it factors through
π₁(P¹_bar)=1. Consequently π₁(Pbar) is a quotient of the abelian group
π₁(A∨_{Kbar}). This argument only uses the smooth open; it does not
apply a smooth homotopy sequence across singular fibres.

Put N=π₁(Pbar), now known abelian. Since H¹(Pbar,O)=0, the Picard-zero
scheme has zero tangent space and is trivial. For every n prime to p,
Kummer identifies H¹(Pbar,μ_n) with Pic(Pbar)[n]=NS(Pbar)[n]. The
torsion subgroup of NS is one finite group, so the entire prime-to-p
character group of N is finite. Artin–Schreier gives
H¹(Pbar,Z/p)=0, since F−1 is onto on kbar and H¹(Pbar,O)=0. An
abelian profinite group with nontrivial pro-p part has a Z/p quotient,
so the pro-p part is zero. Hence N is finite of order prime to p.

### 2. Kill N over the original finite field, preserving the section

The rational point supplied by the section splits the arithmetic sequence

    1 → N → π₁(P) → Gal(kbar/k) → 1.

Its splitting image is a closed open subgroup of index |N|. Let
P'→P be the corresponding connected finite étale cover. Its geometric
fundamental group is trivial and its degree is |N|, prime to p. The
chosen point lifts rationally. More strongly, the section P¹→P lifts:
the image of π₁(P¹)=Gal(kbar/k), for these compatible basepoints, is
exactly the chosen splitting subgroup. Thus there is no forced finite
constant extension.

The generic fibre B=P'_K is a connected finite étale cover of A∨ with
a K-point over zero. It is geometrically connected: its finite field of
global functions embeds in K through that point, so equals K, and
proper smooth base change gives geometric connectedness. The pointed
cover has a unique abelian-variety group structure for which B→A∨ is
an isogeny. This follows geometrically from SGA1 XI §2 and descends by
the uniqueness of the pointed group law. Its degree n=|N| is prime to p.

### 3. Rebuild the regular model to restore coherent H¹ vanishing

Do not assume that the finite cover P' retains H¹(O)=0. Instead use
the prime-to-p isogeny. Its dual isogeny A→B∨ has a quasi-inverse
whose two composites are [n]. Both extend to the Néron models over
P¹. On invariant differentials, their composites are multiplication
by the invertible scalar n. Therefore the Hodge bundles of A and B∨
are isomorphic, and the latter is ample. Semistable reduction is
isogeny invariant.

Set A_new=B∨ and repeat Yuan's Step3, applying Theorem 4.5 to
A_new∨=B, without changing K or making a new isogeny. The theorem
thus models the identical generic abelian variety B. It gives a smooth
projective model P''→P¹ with

    R¹ψ''_*O_{P''} = Lie(𝓑∨/P¹).

The dual Hodge bundle is ample, so H¹(P'',O)=0 as before. The smooth
proper varieties P' and P'' are birational, because both have generic
fibre B over the same K. Birational invariance of étale π₁ therefore
gives π₁(P''_bar)=1.

### 4. Cut to a surface and retain the original isogeny factor

Apply the already audited high-degree-cut proof to P''. If dimP''=2,
first replace it by P''×P¹; its geometric π₁ and coherent H¹ are
unchanged, and the generic Picard-zero variety remains B∨. Each smooth
ample hypersurface cut from an ambient smooth variety of dimension at
least three induces an isomorphism on geometric π₁ (SGA2 XII Cor3.5).
The same Serre-vanishing and finite-field Bertini conditions preserve
H¹(O)=0 and injectivity of H¹ of the generic fibre, and make that fibre
smooth. At the final cut on a threefold choose the degree large enough
that adjunction makes the canonical bundle very ample and supplies all
previously stated numerical tails.

The resulting smooth surface Y has π₁(Ybar)=1 and H¹(O_Y)=0.
Its generic Jacobian J receives B∨ with finite kernel by the tangent
injection, so B∨ is an isogeny factor of J. Since B∨ is isogenous to
A, Tate(Y) implies BSD(J), then BSD(A), then Tate(X), by the exact
Yuan/Artin–Tate chain. The reverse universal implication is immediate.

## Exact primary sources read

- Yuan, author version, Theorem 4.5 and full proof, pp.33–34, and
  Section4.2, pp.34–36 (printed and one-based PDF page numbers):
  https://faculty.bicmr.pku.edu.cn/~yxy/preprints/positivity_hodge_bundle.pdf .
  B re-opened these passages after07:15. The theorem constructs a model
  of the same generic abelian variety. Its underlying degeneration-theory
  references remain used through Yuan, not claimed independently reproved.
- SGA1, corrected SMF edition, https://arxiv.org/pdf/math/0206203 :
  X Theorem1.3 and Corollary1.4, pp.202–203, full proofs;
  X Corollaries3.3–3.4, pp.213–214, full proofs;
  XI §2, pp.221–222, abelian π₁ and pointed-isogeny argument;
  XI Proposition6.4, Corollary6.6 and following discussion, pp.234–235;
  XI Propositions6.7–6.8 and Corollary6.10, pp.236–237.
  C opened the primary PDF; B independently read these full passages in
  the extracted primary text `part_c/sources/sga1_2004.txt`.
- SGA2, corrected edition, https://arxiv.org/pdf/math/0511279 :
  XII Corollary3.5, p.120 (original p.152), statement and full proof.
  C opened the primary PDF and preceding proof; B independently read
  Corollary3.5 in the extracted primary text.
- Stacks Lemma58.10.7, tag0BQI,
  https://stacks.math.columbia.edu/tag/0BQI : B and C each opened the
  complete proof of dense-open surjectivity for geometrically unibranch
  schemes. Normal smooth P satisfies the hypotheses.
- Bosch–Lütkebohmert–Raynaud, *Néron Models* (1990), Section1.2
  Definition1, pp.12–13, and Section7.3 Lemma5, Proposition6 and
  Corollary7 with their complete proofs, pp.180–181. B opened these
  passages directly in the university primary scan:
  https://www.math.stonybrook.edu/~kamenova/homepage_files/Bosch_Raynaud_Neron_Model_tc.pdf .
  The degree-n quasi-inverse and its Néron extension are explicit in
  Lemma5/Proposition6; Corollary7 gives isogeny invariance of semi-abelian
  reduction. The differential isomorphism in step3 is then immediate
  because n is prime to p.

## Scope warning

This is an equivalence with a smaller intrinsic test class, not a proof of
Tate for that class. Étale simple connectedness is not used to infer
algebraicity of degree-two cohomology. The p-primary step uses the full
abelianity established in step1; H¹(O)=0 by itself would not make an
arbitrary geometric fundamental group finite or trivial.

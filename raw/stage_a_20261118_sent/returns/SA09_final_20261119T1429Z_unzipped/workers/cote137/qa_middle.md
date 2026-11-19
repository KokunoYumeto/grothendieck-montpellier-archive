# Independent mathematical QA of cote138 middle

**Reviewer:** GPT-6 Astra Pro; reasoning-effort setting not exposed to worker; SA09/cote137 independent middle review, 19 November 2026.

## Scope and conclusion

The review read `workers/cote138_middle/proof_audit.md`, the targeted `claims.json` records, `programs/compute_middle.py`, its saved JSON key inventory, the relevant original transcription passages, and the explicit M027/L011 merger in `programs/consolidate.py`. It independently checked the odd-power conic construction, marked homeomorphism-group interpretation, reversal formulas, joint permutation/multiplier surjectivity, the rank-two GT0 comparison, and the finite-p-subgroup statement. Primary reference passages were reopened where their exact scope mattered. No scans exist here, so this review makes no new ink decision.

The targeted mathematical arguments pass within their stated scopes. Two corrections were identified and applied in the authorized builder patch: M030 needed to repeat the rank restriction before asserting exact order2, and several claims pointed to nonexistent keys in the saved computation JSON. The historical class E of M022 is supportable after adding the exact pre1978 Quintas source found during this review. The modern Yagasaki theorem is additional confirmation, not a reason to date the finite-type homotopy-group result to2000.

## 1. Odd-power conic maps: passed

**Claims:** CL-SA09-138M-003,004,005. **Source:** `MPL_138_046-089_transcription.tex:158–184;311–381;522–561`, scans49,51,55.

For (C:x^2+y^2+z^2=0) over ℚ, the coordinate (u=(y-ix)/z) over ℚ(i) satisfies σ(u)=-u^{-1}. Compatibility of the power map with this datum is exactly the odd-exponent condition. If (m>0) is odd and ((y-ix)^m=B_m-iA_m), the norm gives (A_m^2+B_m^2=(x^2+y^2)^m), so ((A_m:B_m:z^m)) maps the conic to itself.

There is no basepoint: for (z≠0) the third coordinate is nonzero, and for (z=0) one of (y-ix,y+ix) is nonzero, preventing simultaneous vanishing of (A_m,B_m). Over the splitting field the map is (u↦ u^m), of degree (m). The cubic has (A_3=-x(x^2-3y^2)) and (B_3=y(y^2-3x^2)), agreeing with the displayed source signs. The split parametrization on scan51 belongs to (x^2+y^2-z^2=0); the review confirms the existing decision to preserve the model conflict as a reading question.

This is a targeted proof check of the exact family, not a classification of all self-maps of nonsplit conics or a historical priority claim.

## 2. M022: mathematical scope and historical class

**Source:** `MPL_138_046-089_transcription.tex:1210–1236`, scans74–75. The statement concerns finite-type oriented surfaces, finite pointwise markings and identity components. It correctly excludes the sphere/plane exceptions and does not assert that the entire marked homeomorphism group is trivial. Nor does it assert contractibility of an operator centralizer or cover infinite discrete markings.

The evaluation argument is mathematically sound. For the torus, translations give a section of evaluation and induce its isomorphism on the exceptional ℤ² fundamental group. For the open annulus, rotations do the same for the ℤ factor. Vanishing in the point-fixing identity component then follows from the evaluation fibration; further finite markings preserve vanishing using the corresponding aspherical surface fibers. The distinctions between components and the full marked group are essential.

The original citation to Hamstrom(1974), Theorem1.5.2, has **compact** manifold scope; it is not by itself the exact reference for the open annulus. The following primary source supplies the needed pre1978 range:

**Quintas(1965), pp.721–725**, opened in full at the URL in `references_addendum.bib`. Page721 defines compact-open topology. Theorem(c) gives vanishing of all homotopy groups of identity components for punctured tori; Theorem(h) gives it for spheres with at least three punctures. Equation(2.2), p.722, compares positive-degree homotopy groups of the point-fixing component to those of the surface with one additional puncture, citing McCarty1963, Theorem4.4. Page723 explicitly explains the torus point-fixing case. Thus the marked open annulus reduces to the three-punctured sphere before1978. **Retain class E for the present homotopy-group interpretation**, and add this exact source to its fate and bibliography.

**Yagasaki(2000)** gives a convenient stronger modern statement. Theorem1.1, PDFp1, treats compact-open homeomorphisms fixing a compact subpolyhedron; the open annulus is exceptional only when that fixed set is empty. Lemma2.1(i), PDFp2, covers a torus with a nonempty finite fixed set. The end-compactification discussion at PDFp12 relates the exceptional cases to older compact results. This source was opened as arXiv:math/0010223v1, submitted24October2000. Its publisher page returned403. No full independent reproof of the general noncompact theorem was attempted.

The attempted original McCarty1963 AMS PDF also returned403. Its result may be cited as the dependency explicitly used by the opened Quintas paper; it must not be described as a newly opened original in this review.

## 3. Reversal: passed after explicit rank qualification

**Claims:** CL-SA09-138M-029,030. **Source:** `MPL_138_046-089_transcription.tex:1571–1590`, scan85.

Let (a=λ_0), (P_j=λ_1⋯λ_j), and (P_ν=a^{-1}). The lower1 interpretation gives

\[
t(λ_i)=P_{ν-i}λ_{ν-i+1}P_{ν-i}^{-1},\qquad t(a)=a.
\]

Reversing and cancelling the consecutive factors gives (t(P_k)=a^{-1}P_{ν-k}^{-1}), hence (t^2(P_k)=a^{-1}P_ka). This proves relation preservation and the exact square formula. The square being an automorphism also proves that the original endomorphism is an automorphism. For ν≥2, the reversal induces a nonidentity permutation of the abelianized generators, so its outer class has exactly order2. For ν=1 the displayed map is the identity. The corrected statement now explicitly repeats this boundary.

The lower0 interpretation, retaining the final unconjugated λ_1 actually displayed in the tuple, leaves the relator (aλ_1^{-1}a^{-1}λ_1), nontrivial for ν≥2. This confirms the reading alarm without selecting the ink. It concerns this lift only, not the existence of a different strict involutive lift.

**Applied authorized patch:** state M030 for ν≥2 and add the ν=1 identity boundary. The scan85 text precedes scan89's explicit rank restriction, so the qualification must not be suppressed merely because the later source fixes the range.

## 4. Joint multiplier/permutation map: passed

**Claim:** CL-SA09-138M-025. **Source:** `MPL_138_046-089_transcription.tex:1390–1455;1703–1709`, scans80–81,89.

The source object is Σ=(T,π,I,(Φ_i)); the Tate line and peripheral embeddings are part of its data. Orientation-preserving puncture permutations provide ((s,1)). The arithmetic outer action on a line with rational punctures provides ((1,u)) for every unit through cyclotomic surjectivity. Products therefore provide every pair. Choosing based representatives suffices for surjectivity; the argument does not need a canonical based lift of the full Galois action or a splitting homomorphism. At rank1 it is particularly important not to discard the separate Tate-line datum and silently replace this system's group by an unadorned subgroup of Aut(ℤ̂).

The local Kummer calculation is uniform in the puncture index. The argument makes no claim that arithmetic transport surjects onto the entire peripheral automorphism group.

## 5. Rank-two S3 centralizer: passed

**Claim:** CL-SA09-138M-033. **Source:** `MPL_138_046-089_transcription.tex:1628–1653`, scans86–87.

The rational Möbius transformations permuting (0,1,∞) give an outer S3-action whose puncture permutation is the identity section of the permutation quotient. Arithmetic transport commutes with that action and fixes the puncture labels. This proves the claimed splitting and containment in the centralizer inside the **pure peripheral outer group**, where pure means label-fixing and does not force multiplier1.

Guillot(2014), full publisher PDF, §5.6, printedpp371–373, was reopened. The power/normalization condition and commutation with the two specified outer generators are precisely the gentle GT0 conditions; Lemma5.19 and Proposition5.20 identify the two formulations, and Theorem5.21 gives the arithmetic embedding and cyclotomic projection. No equality with the absolute Galois group follows. The pentagon remains additional. Commutativity is at outer level; no simultaneous canonical based lift was supplied.

## 6. Finite p-subgroup assertion: passed

**Claim:** CL-SA09-138M-016. **Source:** `MPL_138_046-089_transcription.tex:1049–1065`, scan68, entirely cancelled draft.

Faber Lemma4.3 was reopened with its algebraically closed field convention. A nontrivial finite p-subgroup in characteristic p is conjugate to translations by a finite 𝔽_p-subspace and has a unique common fixed point. One can also see this by choosing a nontrivial central order-p element: its unique fixed point is preserved by the whole p-group, and the multiplicative diagonal character is trivial because (k^\times) has no p-torsion. The result does not put an arbitrary finite wild group in a Borel. The original audit correctly keeps that stronger cancelled assertion separate and preserves the source cancellation.

## 7. M027/L011 merge: passed

The explicit merge in `programs/consolidate.py` retains **at least two geometric punctures on P1** before asserting inclusion of the full local inertia ℤ̂(1). It keeps rational-puncture scope, the common character, and the outer/based distinction. The later occurrence adds the puncture-index independence and does not erase the degeneracy warning.

For complete standalone notation, the merged statement can say that k is an algebraic closure of k0 and that the removed finite set defines a divisor over k0. These are already implicit in the stated complement over k0 and the source setup; their omission was not counted as a mathematical failure.

## 8. Computation-pointer repair

The saved calculations and formulas agree, but the following keys named in the claim text were nonexistent. The authorized builder-only patch changes the pointers, not the computations or verdicts:

| Old key | Existing saved key |
|---|---|
| dihedral_maps | dihedral |
| cubic_identity; cubic_basepoint_check | cubic; basepoint subfield no_basepoint_check_z0_and_y2_minus_x2 |
| odd_power_conic_maps | odd_power |
| conic_parametrisation | conic_models |
| target_category_counterexample | groupoid_corollary_counterexample |
| bipyramid_cancellation | bipyramid_product |
| spherical_signatures | tame_spherical_signatures |
| kummer_factorisation | kummer_basechange |
| mu5_action | unit_vs_cyclic_action_n5 |
| reversal_words | reversal |

The orientation_ranks key was already correct. No new finite computation or formal certificate is claimed by this review. The general arguments, code and output-key inventory were inspected; the existing middle computation was not rerun as part of QA.

## References and audit records

New sources are in `references_addendum.bib`; opened historical and modern statements are separately scoped there. Previously included sources reopened for this review are Faber, `https://arxiv.org/html/1112.1999v4`, Lemma4.3; Guillot, `https://ems.press/content/serial-article-files/44274`, §5.6; Hamstrom, `https://www.maths.gla.ac.uk/~mpowell/Hamstrom%20homotopy%20in%20homeomorphism%20spaces.pdf`, Theorem1.5.2 and reference48; and Farb–Margalit version5.0 at the URL already in the middle bibliography. `qa_middle_search_log.tsv` records the chronology searches and access failures without retaining full third-party papers. `qa_middle_events.tsv` records the exact level of each independent check.

# P-F52: actual nonstandard multiplication, not an assigned spectrum

## Result

The central word

`Z=(Q1-Q2)^2+S-f^2`

in the actual cubic nonstandard algebra acts on its conjugate blocks by `-c,-c'`, where `c` is the source coefficient used in P36/P39. The initial leading-coefficient argument was strengthened at root's request: the complete source relation and all coefficients of the source cell element factor as `r(t)=prod(t-g_i)` and `p1(t)=prod_(i!=1)(t-g_i)`. Therefore `(G-g1)u=r(G)Q1=0` directly, independently of the split-block assertion. The split decomposition now only labels the full simple-algebra summands. This does not use an arbitrary assignment to central idempotents.

The explicit descended map `a -> a u1 + tau(a) u2` sends `(1,x)` to `(u1+u2, x(u1-u2))`. The resulting multiplication matrix is exactly P39's `M0`, including sign, orientation and normalization. Four copies act on the eight-dimensional descended two-sided ideal. The two-dimensional subspace is only asserted to be stable under the central operator; it is not silently called a left ideal or simple module.

The actual tensor action is positive for every real `q>0`. An explicit positive product Gram form makes the source's sixteen-dimensional rescaled projection matrix self-adjoint, and `Z` is a square of a self-adjoint difference plus the strictly positive scalar

`3v^4+23v^3+57v^2+48v+16`, `v=q^2+q^-2-2>=0`.

The generic rational intertwiners need not remain injective at exceptional specialization. This is stated explicitly. The positivity of the unscaled actual operator still does not imply Laurent-coefficient positivity: its two-dimensional determinant has P39's negative coefficients. The source's normalization, other coefficients, full canonical-basis category and any theta/cohomological comparison remain further inputs.

## Source audit and quarantined discrepancy

Freshly read GCT VII printed pp. 6–10, 14–22 and 29–36, plus Figure 11 p.40. Visually inspected original printed pp.20,30,31,36,40. Source URL: https://arxiv.org/pdf/0709.0749 ; fresh full web ref `turn332053315view0`. The exact theorem inputs are Section7.1.1–2 pp18–20, Figure2 p31 and Figure7 p36; tensor positivity is checked directly from Figure1 p30. Local renders are `work/nonstandard_sources/gct_vii_20.png`, `gct_vii_30.png`, `gct_vii_31.png`, `gct_vii_36.png`, `gct_vii_40.png`.

The two-by-two generator matrices printed on p.20 are both upper triangular. Taken literally, they have a common invariant line and cannot be the asserted generic irreducible modules. This was confirmed in the actual page image, not inferred from a text-extraction error. The display is quarantined. No correction is silently made, and the proof never uses it. The central eigenvalue instead follows from the independent original relation and word coefficients; it agrees with the displayed `g1` scalar in Figure11.

## Actual checks

At approximately 03:03–03:04 UTC, read the entire written proof in two output chunks and reconstructed every step. Centrality follows directly from `Qi^2=fQi`; comparison of the `w4` coefficient gives the exact scalar. The descent and eight-dimensional ideal arguments were reconstructed independently, including the distinction between four-dimensional simple algebra summands and two-dimensional simple left modules. Every Gram block and the positive scalar expansion were rechecked.

Ran `work/verify_nonstandard_central_word.py` successfully. It transcribes the actual Figure1 matrix and checks, over the rational-function field, `Gram*P=P^t*Gram`, `P^2=fP`, the same properties for its complement, the scalar positivity identity, and the exact change of basis producing `M0`. This is a finite exact verification of a concrete remaining normalization risk, not a numerical sample.

At 03:07 UTC, read the complete factor-certificate addition P-F52f1–f3 and reran the extended exact verifier. Every one of the six relation coefficients and five cell coefficients was transcribed independently from the original source, then compared with the compact factor table. All pass, as does the complete six-coefficient identity `(t-g1)p1(t)=r(t)` modulo `x^2=D`. This closes the robustness issue raised by the quarantined p20 display; the eigenvector calculation is independent of that display and of the simple-block assertion.

Plethysm subsequently reported a completed independent entire-proof and exact-primary review: PASS, no correction. Its review independently reconstructed the central word, leading coefficient, descent, four-copy ideal, every Gram block and scalar positivity, and visually inspected the relevant original figures. The separate event is recorded by plethysm; this sentence reports that received result.

Plethysm also independently rechecked the complete factor-certificate extension against every original coefficient, ran the extended verifier, and reported PASS. Root reports a whole-proof/source read and successful independent execution of that verifier.

## Normalization corollary and final whole-proof reread

At root's request, appended a precise within-example normalization comparison. The alternative `H=(q+1+q^-1)^4` gives positive actual action and two positive symmetric nonincreasing determinant coefficient vectors, printed in full. It has Laurent width8, while the source's `F` has width32, so `F` cannot divide `H`. Thus those strengthened finite properties do not characterize the prescribed source normalization. No claim is made that `H` satisfies the source's additional lattice/canonical-basis conditions or normalizes other coefficients.

At03:10:32 UTC read the **entire revised file**, including both extensions, and reconstructed all proof steps. Ran the complete verifier again: source matrix, full relation and cell coefficients, all intertwiner identities, and the alternative full coefficient certificates PASS. Plethysm has been asked to independently check the short final corollary.

## Exact spectral-denominator provenance

At root's request appended P52q–s, identifying the actual additional source rule. Freshly read original VII p27 equations32–35 and p28; visually inspected the p27 render and the previously audited p28 normalization. The source chooses the product of the two Lagrange denominators for the positive R-eigenspaces, not the smallest matrix denominator. Multiplying the actual four eigenvalue differences gives

`f_p=-q^-33(q10-1)^2(q6+1)(q12+1)(q4+1)(q²+1)`.

Dividing by the convenient `f`, removing the source's explicit `-(q-1)^2/q` factor and centering by `q11` gives exactly

`F=q^-16(1+q+...+q9)^2(1+q²)(1+q12)`.

The proof accounts for every sign and exponent and treats q1 by the canceled Laurent identity. It proves coefficient positivity of this actual source factor directly. The exact verifier independently multiplies the six eigenvalue differences after q=r² and compares the full33-term F vector; PASS. This fixes provenance once the specified interpolation rule is supplied, while the H corollary shows positive action and Lefschetz determinant coefficients do not impose that rule. It does not supply a categorical integral form or all-coefficient multiplication compatibility.

## Latest peer and obstruction checks

Plethysm independently checked both final m-s normalization/provenance corollaries, freshly read originalVIIpp27-28, and executed the complete verifier PASS. Root also whole-read and visually checked those source pages and executed the verifier PASS. The root-authored t-x ordinary/virtual lambda and fixed-operator all-extension obstruction was independently whole-read and reconstructed by bridges at03:21:32 UTC; separate event recorded in this file family’s checks. No purity/semisimplicity assumption is needed for that obstruction.

## Positive multiplication in the actual restricted central algebra

After checkpoint06 freeze was released, appended P52y–ah at root's request. The source normalization is unchanged. With t=T1,n=N1,e=q^±4+q^±8+q^±12+q^±24, the explicit polynomials a=(t−e)/2,d=(t+e)/2,b=ad−n have complete positive symmetric nonincreasing coefficient vectors printed in the proof. The full verifier checks all their coefficients exactly, including vanishing beyond the displayed ranges.

The actual restricted central operator z=FZ generates a quadratic Q(q)-field; its C(q)-extension is the already identified actual central endomorphism algebra. The R0=Z[q±1] order R0[z]=R0[u], u=z−a, has the positive multiplication table u²=e*u+b. This is an endomorphism algebra construction. The original iota(K) is only an intertwining subspace of B0 and is never called a subalgebra. Its explicit new basis (v0,e*v0/2+F*v1/(2q20)) gives z the positive integral Laurent matrix [[a,b],[1,d]]. All positive power traces therefore count finite weighted closed walks. Generic scalar-extension assertions are separated from exceptional specializations.

The exact q1 value b(1)=5,759,984 excludes an interpretation of this specialized basis as the two simple classes of a complex-linear semisimple rigid tensor category with simple unit and finite Hom spaces, by unit multiplicity at most1. This does not exclude nonsimple-object or additive models. Indeed the proof explicitly gives an additive exact functor on two copies of finite graded vector spaces, using the a,b,d Tate–Lefschetz coefficient models, whose Grothendieck matrix is the actual operator matrix. The source-basis map intertwines it after C(q) scalar extension. No monoidal coherence, canonical source integral form, full B0 action or uniform tensor-degree theorem is supplied.

At03:37:54 UTC I completed the whole new-block reconstruction and exact verifier. Plethysm independently read y-ag and executed the verifier PASS; the short subsequent ah functor paragraph is separately awaiting its check. All previous source/check histories are preserved.

## Actual source word form, internal bar, and two failed stronger comparisons

At03:54–03:56 UTC I completed the final entire ai-as reread. The convenient Q/P-generator word form is free on the21 source alternating words by monic integral reductions. Full reciprocal relation coefficients give the actual generator-fixing internal bar; the source intertwining lattice R0v0+R0w is integral and bar-fixed. This does not reconstruct the external Hecke embedding or minimum-degree criterion.

The centered global element uhat has Q12 coefficient−F. Every element of the explicitly F-rescaled generator form has that coefficient divisible by F², so uhat is not in it, even over the source integral closure. The literal denominator-rescaled form lies inside it and is excluded too. This statement concerns those exact forms. The generic expansion of w in the actual displayed source candidate basis has one strictly negative coefficient on every positive real branch. Figure6 of VIII was visually read and compared with Figure7 of VII; no unproved canonicity claim was added.

The full exact verifier was executed at03:49:03 and all new and previous checks passed. Plethysm has now independently whole-read ai-as, checked the original pages and run the verifier: PASS. Its separate ah additive-functor review also passed. These received events and the author/source/computation checks are logged separately.

Root proposed the short structural sign refinement at-au. I proved and checked it: in any unit-containing positive Laurent basis of a quadratic field, alpha cannot vanish and is positive on q>0; the two values of the second basis element therefore have opposite signs. This excludes simultaneous PSD basis elements in a representation containing both real characters. It imposes no PSD requirement on a source canonical basis. Peer review of this short addition has been requested.

The existing P39Q4 and P52Q4/Q6/Q8 rows were updated in place, closing the convenient-word/internal-bar subquestions and recording the two precise negative comparisons. The still-open parts are ambient external-degree/full canonical products, coherent monoidal or supplied theta-projector comparisons, and uniform families.

## Both actual rescaled generators on a rank-four source lattice

At04:02:00 UTC completed the full author reread and executed the entire extended verifier for P52av-bc: PASS. The positive generator v=e-u gives h=FS-d=(FL-e)/2 with a complete49-term symmetric-unimodal coefficient certificate and h1=3996. The four actual vectors (v0,vhat*v0,Q2*v0,vhat*Q2*v0) are independent, integral in the convenient word form and fixed by its internal bar. The independence proof uses the original cell relation and g1 notinF0; no quarantined source matrix is used.

The actual FQ1,FQ2 matrices in this basis have positive Laurent entries, as do all their ordered words. Their generic field span is an actual left ideal, unlike the earlier2D central intertwining space. Additive graded-vector-space endofunctors reproduce all ordered-word matrices on K0; no coherent natural isomorphisms for the defining relations or monoidal categorification is asserted. A common nonnegative basis for both Q/P complementary pairs would force diagonal commuting matrices and is impossible generically.

This extension is author-checked and sent for root/plethysm independent review. It was not promoted at the04:02 review cutoff before those reviews. Existing question rows will be reconciled after peer confirmation.

Plethysm final whole-proof at-bc review and complete extended verifier execution passed at04:04:22, received and separately logged. The original P39Q4 and P52Q4/Q8 rows have now been updated in place: the actual full rescaled-Q-generator module/all-word/additive comparison is closed, while canonical-basis products, coherent natural relation data, ambient external-degree, supplied theta and uniform families remain open.

## Quadratic functor relations and actual Gram compatibility

The complete P52bd-bl extension was author-whole-read and the exact verifier passed at04:10:24. The actual matrix functors have specified natural quadratic isomorphisms E_i²=H tensor E_i, coherent for repeated equal-generator runs. Their ordinary Vect4 adjoints fail to implement source self-adjointness, but this is a narrow model limitation: an explicit symmetric reciprocal nonnegative Laurent Gram does symmetrize both actual matrices. Exact source factorization proves this Gram positive definite at positive q except1, and positive semidefinite of rank3 at1. Pairwise coefficient spaces and matrix identities still do not give Hom composition, natural adjunction, mixed nonstandard relation or canonical coherence.

Root reports whole-proof bd-bl PASS at04:11:34; its verifier run was ongoing at receipt. Root directed that this author-plus-parent review suffices before checkpoint, without diverting plethysm from P57. P52 source is frozen for checkpoint07.

## Intrinsic ordinary graded-semisimple adjoint obstruction

After checkpoint07 release, wrote and whole-checked P52bm-br. It excludes a faithful realization of the actual rank4 source module inside localized splitK0 of an ordinary graded semisimple category with both rescaled-generator functors self-adjoint. The intertwiner may use arbitrary rational/virtual classes, and finite power regrading is allowed. Finite support in simple-shift orbits yields a rational matrix Z, and the Hom pairing is genuinely Hermitian under coefficient conjugation plus q inversion. On unit-circle arcs outside finitely many poles/rank drops, Z*Z is positive definite.

The exact primitive12 source specialization has f0,L1,N00,Fnonzero. Nearby, one G eigenvalue stays above1/2 while f² is below1/4. Self-adjoint generators would force G=f²−(Q1−Q2)²<=f²I, a contradiction. This does not assume faithfulness at the root itself and is not limited to the earlier four-simple-object basis.

At04:21:18 the full exact verifier completed successfully, including arithmetic in Q[q]/Phi12. Original VIII Conj3.5p24 and3.6p25, plus supplied Remark item8p4, were freshly read. None imposes the additional categorical dictionary. Positive real-parameter theta/Hilbert-space adjoints alone do not give unit-circle Hom positivity, so the no-go is not asserted against those source statements. Nonsemisimple/derived Hom geometry or a different duality remains possible. Complexity has been asked for independent whole review.

## 2026-11-21 04:34 UTC — actual completed projector comparison

P52bs–bz is in `positivity_nonstandard_projector_lift.tex`. The comparison uses CK’s explicitly completed Euler group over Z[[q]][q^-1], followed by C((q)) scalar extension, and its rational four-dimensional fusion subspace. It is an isomorphism there, not an unproved ordinary K0 assertion. CH higher projectors on six cables in channels0 and4 preserve the P3 boundary corner, and finite Ff shifts produce the actual full source generators. The intertwiner is evaluation on the channel-zero fusion vector; it is nonzero in both conjugate blocks. An independent exact tensor certificate reconstructs this from original Figure1 and records a nonzero rational determinant atq2. The length11 relation is still only an Euler-class relation; no mixed natural homotopy/coherence is inferred. One-sided completion and reversal of both gradings make the distinction from the preceding semisimple ordinary-adjoint no-go concrete. Author whole check PASS; sibling/root reviews requested and pending.

## 2026-11-21 04:50 UTC — full tensor-image Euler lift and integral-object gate

The bs–bz module construction has passed plethysm’s full independent proof/source review and complete original-tensor verifier. The ca–ce extension has passed root and complexity entire-proof/source reviews. It identifies the entire21-dimensional concrete source algebra with a preserved rational Euler subspace of the TL9 boundary corner, with exact regular left/right action and unit/multiplication. The same construction works uniformly for the actual sl2 tensor-image algebra, with the abstract Hecke-algebra faithfulness question explicitly separated. Existing P39Q4 and P52Q4/Q8 rows were reconciled in place; their previously open derived construction is now closed in this precise completed-Euler sense.

The new cf–ci arithmetic refinement is author-whole-checked and awaiting independent review. Actual admissible diagram complexes have integer Laurent-series Euler coordinates, while G is a rational diagram operator. The source discriminant begins5q24, so neither split eigenvalue belongs to Q((q)); any nonzero rational-coordinate eigenvector would contradict this through a nonzero coordinate quotient. Thus no actual integral Euler object lies wholly in either conjugate block, including arbitrary scalar multiples of the source cell vectors or their4D images and every finite power regrading. Rational conjugate sums and the scalar-extended Euler realization are unaffected. No general obstruction to different geometric categories is asserted.

P52cf–ci is now independently passed: plethysm whole-proof review at04:50:20. Root also whole-read and approved, requesting only a corrected TeX escape/spacing and explicit scalar-extended Phi for the individual split vectors; these are applied. The existing P39Q4/P52Q4/Q8 states now record the actual integral-object exclusion, while preserving scalar-extended full algebra, rational conjugate sums and all precise open coherence/theta/product conditions.

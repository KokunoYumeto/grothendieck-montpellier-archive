# Endpoint perfect-family lifting: exact source and proof scope

19 November 2026. Owner `/root/real_weil`, GPT-6 Astra (OpenAI),
ChatGPT Pro, run RESEARCH_SA06; inherited effort is not separately exposed.

## Final theorem and independent checks

The final unnumbered theorem is `C3_endpoint_family_lifting.tex`.
The former draft is a comment-only pointer; the entire audited draft is
preserved at `output/C3_endpoint_family_lifting_audited_draft.tex`.
The final proof retains the general regular-threefold/SNC/positive
exceptional-divisor hypothesis separately from the specific ordered
tetrahedral application. It proves endpoint equality on an actual fixed
proper-curve product. It does not claim surjectivity of the full family
restriction map or vanishing of the fixed-product negative-K obstruction.

The complete four-step theorem and application were independently read
by root, Frobenius, and Cycles. Both peer written receipts were read by
the owner after their completion. Frobenius's mathematical verdict was
between his actual 16:47:19 and 16:48:42 clock readings; Cycles completed
at 16:49:33. Root's final refinements and full pass were communicated at
16:52. No different underlying model or original-literature priority is
claimed by these separate-agent audits.

Proof refinements retained in the final text:

* Incidence bad sets from locally closed strata have images with proper
  closures by the dimension bound; the images need not themselves be closed.
* D is projective over k because a power of the maximal ideal kills its
  structure sheaf and the resulting Artinian local ring is finite over k.
* Uniform restriction spaces on each component surface fibre have at least
  two independent sections by ideal generation followed by multiplication
  with a very ample factor.
* W is a regular actual scheme, not a claimed regular morphism; properness
  over the local base removes a possible nonregular locus away from the
  closed fibre. Its parameter flatness is checked fibrewise.
* C is only required to have finite regular fibres at the two selected
  endpoints; no unnecessary assertion of global flatness of C is made.
* The Picard bundle is O_H(-C), and the finite endpoint identity is exact in
  perfect K0. This avoids a singular gamma-filtration pushforward theorem.
* Popescu descent matches the prescribed map modulo a sufficiently large
  power of the maximal ideal, preserving the entire thickened proper family.
* The tetrahedral class has rank zero, and gamma squared is applied after
  clearing denominators. No global Adams projection on K2(P) is used.

## Freshly opened primary sources

1. **Weibel, The K-book, Chapter II**, full 106-page author PDF:
   <https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf>.
   Directly read Splitting Principle 8.8.1, Corollary 8.8.2,
   Proposition 8.8.4, and Remark 8.8.5, chapter p.83. The last explicitly
   gives `F_gamma^(d+1)K0=0` for noetherian quasiprojective schemes without
   a regularity assumption. Also read Proposition4.9's Adams action,
   chapter p.32, and Corollary8.9.1 with its proof, p.84, for the subsequent
   comparison. Exact owner retrievals: `turn725244446view7`,
   `turn548119078view0–1`, `turn275999804view1`. Bibliography key
   `D_Weibel2013KbookII` is chapter-specific in `SEMIPURITY_references.bib`.
   **SGA6 VI.6.6 itself was not freshly opened**; the explicit Weibel
   statement is the source used, and the attribution to SGA6 remains his.
2. **Stacks Lemma30.17.1**, <https://stacks.math.columbia.edu/tag/01XO>:
   proper-over-affine Serre vanishing, full statement/proof directly read.
   For relative vanishing over P, apply it on a finite affine cover and
   take the largest bound; positive higher direct images vanish thereafter.
3. **Stacks Lemma37.4.1**, <https://stacks.math.columbia.edu/tag/0C6R>:
   exact first-order unit/Picard obstruction sequence, complete proof read.
   Applied separately to each square-zero step, not to an arbitrary thickening.
4. **Stacks Lemma30.24.3**, <https://stacks.math.columbia.edu/tag/0885>:
   projective Grothendieck existence, equivalence and complete proof read;
   full faithfulness from Lemma30.24.1 is part of that proof.
5. **Stacks Theorem16.12.1**, <https://stacks.math.columbia.edu/tag/07GC>:
   Popescu theorem and displayed proof read. The deeper lemmas invoked by
   that proof are accepted primary inputs, not independently re-proved here.
6. **Stacks Lemma32.10.3(2)**, <https://stacks.math.columbia.edu/tag/0B8W>:
   finite-presentation descent of invertible bundles, full proof read,
   including simultaneous descent of the inverse and its evaluation.
7. **Stacks Lemma15.13.3**, <https://stacks.math.columbia.edu/tag/0H74>:
   lifting a specified point of a smooth algebra over a henselian pair,
   complete proof read. The pair used is `(R,m^M)`, not merely `(R,m)`.
8. **Stacks Lemma15.51.14**, <https://stacks.math.columbia.edu/tag/0AH2>:
   regularity of completion of a G-ring, full statement/proof read.

The seven Stacks entries reuse exact bibliography keys from
`../frobenius/C3_smooth_exceptional_references.bib`; no duplicate source
entries were introduced. Owner fresh retrievals are
`turn725244446view0–6` and `turn275999804view0`.

## Prior directly checked inputs reused

The general point K0 isomorphism FF.4, TG geometric resolution,
TS whole-diagram spectrum calculation, and TC raw Chow calculation have
separate complete audits. Their Drinfeld, KST, Geisser–Hesselholt,
Thomason–Trobaugh, Khan, and WeibelIV sources are reused with their
existing version-specific locators. The field-symbol proper-curve lemma
is fully written in `TOP_QUOTIENT_RESEARCH.md` Section2; its primary
Quillen1973 Section7 Proposition3.2/equation3.3 p127 and Theorem5.11
pp133–134 were opened earlier in the same run. This new audit does not
pretend those literature proofs were freshly re-proved.

## Computations and formatting

`code/check_endpoint_family_algebra.py` completed at
2026-11-19T16:50:58.740215 UTC in **0.10592786000052001 seconds**:
23 exact finite checks passed, zero failed. It checks Hilbert–Burch
quadratic terms at ranks2–10, the virtual gamma expansion, eight Cartier
power identities, the four stratum dimension inequalities, and the
endpoint square-zero/weight-two identity. The universal proofs are in
the text; finite samples do not certify the geometric theorems.

`code/compile_endpoint_family.py` produced a four-pass clean standalone
draft build at 2026-11-19T16:51:01.177477 UTC in
**2.8254054410062963 seconds**, all exit codes zero and no retained
overfull/undefined diagnostics. Timestamped per-pass outputs and JSON
remain under `output/`. A later promoted-file build, if performed, is
recorded separately rather than overwriting this historical timing.

## Subsequent comparison scope

`C3_exceptional_ordinary_presentation_draft.tex` is a separate proposed
consequence, pending its own full audits at the time this record was
written. It identifies ordinary cycle relations on Z with actual
proper-product gamma-two endpoint relations on E. It explicitly retains
the problem of gluing independently moving edge/vertex classes into a
global class on E times the parameter curve. It makes no universal
finiteness conclusion from the tetrahedral example.

### Final comparison supersession, 2026-11-19T16:59:39.474217+00:00

The separate EP comparison is now fully audited by root and both peers and promoted to `C3_exceptional_ordinary_presentation.tex`; the preceding pending designation is retained only as history. Owner read both written receipts. Exact relation-group equality removes the ambient endpoint-lifting obstruction, but global perfect-family gluing on E remains explicit. The audited draft is preserved in output and the old path is a pointer. The complete FF/TG/TS/TC/EL/EP chain is included through `C3_tetrahedral_endpoint_bundle.tex`, with the parent-authorized single input after C3bl in cycles.tex. Final combined formatting metadata is in output/compile_endpoint_family.json.

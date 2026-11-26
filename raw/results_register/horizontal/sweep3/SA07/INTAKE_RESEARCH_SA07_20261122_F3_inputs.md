# The open inputs of the CM case of LM6 A.22 (board row S07c): F.3.24, F.3.29, F.3.30, Nakamura 1994, F.3.33

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 22 Nov 2026, at the main session's request. The run is
RESEARCH_SA07 checkpoint 12, GPT-6 Astra (ChatGPT Pro mode). This continues `INTAKE_RESEARCH_SA07_20261121_F332.md`.
Check events: `INTAKE_RESEARCH_SA07_20261122_F3_inputs_CHECK_EVENTS.tsv`, beside this file.

## Verdict

**The CM case of LM6 A.22 now stands on checked inputs.** No gap was found. What is left open is listed below.

| Input | Check | Result |
|---|---|---|
| Nakamura 1994, Lemma (2.1.4), p. 96 (open PDF, J. Math. Sci. Univ. Tokyo 1 (1994) 71-136) | targeted proof check against the source | as F.3.31 uses it. A non-cuspidal z has a prime ℓ and an open H ∋ z with z ∉ [H,H]Hˡ⟨Z∩H⟩, for C = all finite groups and (g,n) = (1,1) |
| F.3.24 (genus three, six basis lines) | targeted proof check, read in full | confirmed as a derivation. Graded geometric image = rational Johnson image (Hain 1997 Thm 3.4, Lemma 4.5, Cor 4.8, checked as statements); [U₆, J₁] ⊂ J₇ by the normalizer action; ES₇(J₇) = 0 moved to genus 3 by adding handles; then Sp(V)-invariance. The finite ranks (G3.7) and kernel (G3.10) are in-run certificates, not rerun; the displayed 4×4 minor (det 1) I checked by hand |
| F.3.29 (genus three, one line) | certificate rerun from my folder (SHA = the run's record): PASS in 15 s; trace matrix 7977×180 of rank 48; minor −10752 | confirmed computationally. The proof logic was followed in part; its R-map input is the one reconstructed in F.3.34 (rerun PASSED) |
| F.3.30 (higher-genus invariant reduction) | both certificates rerun (SHA = records): input dimension 12 for every s ≥ 3; detector J and quotient L as in F.3.32 | confirmed. The logic of (LI.1) and (LI.6) is sound as read |
| F.3.33 (every affine hyperbolic curve over a number field) | targeted proof check, in part | the proof follows F.3.31/F.3.32 for a general curve: rational cusp after base change; full-class detector; an explicit regular cover of degree 5^{2g+n−1}, or of degree eight, giving genus ≥ 3; Nakamura 1996 over the same field; then UC.1. I did not redo the Riemann-Hurwitz computations. **The printed statement is garbled:** a clause is missing between "open image in G_k exactly" and the display of R_X. It should read, roughly, "exactly when it is cuspidal; in particular R_X has no …". The run should repair it |

**Left open:**
- Enomoto-Satoh 2014 (Thm 3.5, Prop 3.6; ES₇ on the Johnson image), not opened.
- Hain's Theorem 4.10 and Remark 4.11, not opened.
- The in-run integer certificates of F.3.24 (G3.7) and (G3.10), not rerun.
- The arithmetic corollary paragraphs of F.3.29, read at statement level.
- The covers of F.3.33, not re-derived.

None of these is a gap. They are inputs I did not re-derive.

## What the chain settles, in plain words

For the CM curve E₀ ∖ {O}, with E₀: y² = x³ − x, and every finite base change, no nontrivial closed procyclic subgroup of
the common kernel R has an arithmetic normalizer with open image. This is A.22's open case.
- It is proved in the run by F.3.31-F.3.32 on the inputs above.
- With this pass, every input on that path has an outside check (rerun, source or argument), except the in-run
  certificates of F.3.24 and the unopened sources listed above.
- A.22 can be recorded as "proved; checked outside the run at the levels listed in the two SA07 F.3 files".

## Literature: is the cuspidality statement known?

**The known theorem has an extra hypothesis.** Nakamura characterized cusp inertia under a *cyclotomic* normalizer:
- Nakamura 1994, Theorem (2.1.1), p. 97: its proof concludes from the weight filtration that z lies in W₋₂, and needs
  the normalizer to act through the cyclotomic character.
- The general form, as cited in [arXiv 0809.0017](https://arxiv.org/pdf/0809.0017) ("On cuspidal sections of algebraic
  fundamental groups"): a procyclic subgroup is in an inertia subgroup if and only if it is *cyclotomically*, or
  *essentially cyclotomically*, normalized.

**What F.3.20, F.3.29 and F.3.33 claim is stronger.** Their hypothesis is only that the normalizer has open image in
G_k, with no condition on its character. F.3.20 is the pro-ℓ form for once-punctured elliptic curves; F.3.33 is the full
profinite form for every affine hyperbolic curve.
- Exactly that difference is LM6 A.22's recorded obstacle: "its line can have weight one" (CM Jacobian factors carry
  Galois-stable lines of weight −1).
- The run removes it with Nakamura 1996's degree-six class.

**Gates before any Hexagon post:**
- Check whether the open-normalizer form is already in the literature. Look first at:
  - Mochizuki, *Absolute anabelian geometry* and *Topics in absolute anabelian geometry I*
    ([author PDFs](https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20I.pdf));
  - Tamagawa 1997 (Compositio 109);
  - Nakamura-Tamagawa-Mochizuki's survey
    ([author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Grothendieck%20Conjecture%20on%20the%20Fundamental%20Groups%20of%20Algebraic%20Curves.pdf));
  - Hexagon.
- I did not settle this tonight.
- F.3.33's statement needs its missing clause restored.

## Consequences

- **LM6 A.22:** proved in RESEARCH_SA07 F.3.31-F.3.32, with every input on its path checked outside the run at the
  levels above. LM6 A.52 takes the same status.
- **S07c on the board:** the proof inputs are checked. The literature gate is open.
- **EXIT_TOWER and GT_TOWER_CHECK:** no change.

## Sources used

- [Nakamura 1994](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf).
- [Nakamura 1995](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms020107.pdf).
- Hain 1997, arXiv alg-geom/9512001.
- Nakamura 1996, through a922466087ec53798's check against the GDZ scan.
- [arXiv 0809.0017](https://arxiv.org/pdf/0809.0017).

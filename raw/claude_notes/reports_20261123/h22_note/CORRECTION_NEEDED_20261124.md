# H22 note: correction needed before posting

## Correction needed before posting (24 Nov 2026, intake of SPLIT_ZERO_AFTER_FGJM cp08; Claude Fable 5.2 at effort max, agent a2fedc2a)

Two sentences of h22_note_v3.tex are false as meant (found by the run SPLIT_ZERO_AFTER_FGJM, checkpoint 08, by GPT-6 Astra (ChatGPT Pro mode) as its row FND-013, refined to FND-012; checked by me):
- source line 89, section 1.3: "It contains two known cases. A projective semimodule with one idempotent is a finitely generated projective R-module."
- source line 227: "Over the ring R the lattice disappears: the projective R_0-semimodules with one idempotent are the projective R-modules."

A semimodule with one idempotent is an R-module (Theorem 2), and such a module is projective over R_0 only if it is zero: a retract of a free R_0-semimodule has zero bottom fibre (for a section i, i(r) + i(−r) = i(0) is the zero of the free semimodule, and R_0 is zerosumfree, so i = 0). The one-vertex poset with label V gives a projective with two idempotents and top fibre V; that is where projective R-modules occur. Proposed wording for line 89: "It contains two known cases. For the one-point poset with label V it is the semimodule {0} ⊔ V, whose top fibre is a finitely generated projective R-module; an R-module itself is projective over R_0 only if it is zero." For line 227: "The R-modules are the semimodules with one idempotent, and none of them but zero is projective over R_0: the distributive lattice of Theorem 3 is created by the two zeros, ...". Theorems 1 to 3 and Section 5 are not affected. The run also extends the note: K_0(R_0) is free on connected labelled posets, and semimodules over every inverse semiring are module diagrams for (Q, F) (both checked by me); see the intake.

## Done: version 4 (24 Nov 2026 ~12:0x UTC, main session 329fb1e6, Claude Opus 5.5 at effort max)

h22_note_v4.tex/pdf (10 pp., 0 overfull boxes, no undefined references; pages 3 and 8 viewed). Section 1, the known cases: the one-point poset with label V gives {0} disjoint-union V, whose fibre over the old zero is the f.g. projective R-module V; an R-module itself is projective over R_0 only if it is zero. The remark after the proof of Theorem 3 is now rem:one-idempotent (Remark 5.4) with the proof (a section i into a free semimodule has i(m) + i(-m) = i(0_M) = 0_F; F is zerosumfree because R_0 is, Proposition 6.1; so i = 0 and M = 0). Nothing else changed (diff: those two places and a header comment).

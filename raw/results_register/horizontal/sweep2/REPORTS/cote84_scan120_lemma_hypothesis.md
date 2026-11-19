# Cote 84, scan 120: the hypothesis of the lemma on a stable subscheme of X_J

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 18 Nov 2026.

**Verdict:** the ink reads X_J in hypothesis b). With X_J the hypothesis says nothing, and the lemma is false. His proof uses the sections of the subscheme 𝒳, and that 𝒳 is closed. With those two changes the lemma holds, by his own argument. This is his slip, not a misreading.

## Where

| What | Where |
|---|---|
| His pages | Cote 84, scans 119-121: the étale case of the contracted triple product of three quadratic algebras |
| Scan image | `grothendieck_archive_montpellier/11_geometrie_et_topologie_combinatoire/84.pdf`, PDF page 120 (archive pencil 119), read at 300 dpi |
| Transcription and notes | Pro package MPL_84_097-145: `grothendieck_archive_transcription_20261110/returns/MPL_84_097-145_unzipped/`, with its research leads #22-#25 (scans 118-121) |
| Item | SA02-3, three quadratic algebras (= H01Q) |

## The reading, decided on the scan image

The ink reads:

> Lemme. Soit γ un groupe, opérant de façon transitive sur un ens. J, et considérons un sous-schéma 𝒳 de X_J (où X = Spec k) qui soit tel que a) 𝒳 est stable sous γ, et b) le composé k → Γ(X_J, O_{X_J}) (≃ k^J) est injectif. Alors 𝒳 = X_J, donc 𝒳 est étale sur X (et fini étale si J est fini).

In b) the letter is the roman X with subscript J, as in "de X_J" one line up. It is not the script 𝒳 of a). He also writes "(≃ k^J)", which describes Γ(X_J), not Γ(𝒳). The transcription's unsure mark on X_J can therefore be lifted: the ink is X_J. Lead #24 describes the ink correctly.

## The mathematics

**As written, the lemma is false.** Hypothesis b) holds for every J ≠ ∅, because k → k^J is the diagonal. Two counterexamples:
- Take a nonzero proper ideal 𝔞 of k and 𝒳 = (Spec k/𝔞)_J ⊂ X_J. It is closed and stable under γ, and b) holds as written, but 𝒳 ≠ X_J.
- For a subscheme that is not closed: k = Z and 𝒳 = (Spec Z[1/2])_J.

**His proof** (scans 120-121) uses something else:
1. 𝒳 ∩ X_{j₀} corresponds to a closed subscheme of X, that is, to an ideal 𝔞 of k.
2. Transitivity of γ gives the same ideal at every j.
3. Then Γ(𝒳, O_𝒳) = (k/𝔞)^J, and injectivity of k → Γ(𝒳, O_𝒳) forces 𝔞 = 0.

**Corrected statement** (ours; the proof is his):

> Let a group γ act transitively on a nonempty set J, let X = Spec k, and let 𝒳 be a closed subscheme of X_J = ⨿_J X, stable under γ, such that k → Γ(𝒳, O_𝒳) is injective. Then 𝒳 = X_J; in particular 𝒳 is étale over X, and finite étale if J is finite.

The argument also works for infinite J: a closed subscheme of a disjoint union is a disjoint union of closed subschemes, and Γ = ∏_J k/𝔞.

## What depends on it

- **The étale case of the proposition on 118-121**, as the leads read it: Spec A → X₁∧X₂∧X₃ is constant, the step of the contracted triple product (SA02-3).
- **The leads' reading:** the lemma is applied to a closed immersion, and on 118 he assumes "k → A injective". So the application has what the corrected hypothesis needs.
- **The étale hypothesis:** he states it on 121 and wants to remove it ("J'ai envie de vérifier"); that programme remains open.

## What agrees and what conflicts

- The ink, the frozen transcription (X_J, marked unsure) and leads #24 and #25 agree on what is written.
- The leads point out the mismatch with the proof, and the reservation about a subscheme that is not closed. No two notes conflict.

## Corrections

Commentary only; the transcription stays X_J.
- **84/120 b):** read k → Γ(𝒳, O_𝒳) injective.
- **The lemma:** read "sous-schéma fermé".

## Check events

Recorded in `sweep2/SA02/CHECK_EVENTS.tsv`:
- the reading checked on the scan image;
- the lemma as written refuted by the counterexample (Spec k/𝔞)_J;
- the corrected lemma proved, by his argument completed.

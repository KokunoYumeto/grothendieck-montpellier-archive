# Root source review, 19 November 2026

## Complete read coverage

Read all 107 indexed notes from MPL_11_043-058+56, including the appended standing-question tables, bibliography and reproducibility paragraph. Read the complete 1,958-line Pro transcription and all three independent K56 Codex transcriptions. Read all K55-01 transcription pages and the four corresponding Codex notes files. Source-line read outputs are under `outputs/root_*`; quotations there reproduce user-provided material, not downloaded literature.

## Material distinctions

Cote11: correspondence formalism (44,46,48), tautological rings (51,53,55,57), and reused configuration quotient typescript (43,45,47,49,52,54,56,58). Cote56: quadric degeneration (3,5,7); cone/quadric calculations (11,13,15,17,20,22,24,26,28,30,32,35); SGA3 XII draft sheets on tori/ranks/centres; signed Delzant1962 offprint (36–39). Cote55: Stein-compact/coherence notes (2,4,6,8,10,12,14), dimension/associated-point typescripts (3,5,7,9,11,13,15), torus example (17,18).

## Checks requiring explicit treatment

1. Cote11:51 `base` is not universal linear independence. On P1, diagonal = h1+h2. Its top-degree two-factor entry has an extraneous third index. At55 the partition includes the empty block, but57 counts all blocks as geometric factors; distinguish nonempty-block count. The set-theoretic statement at55 is not an excess-intersection proof. The transverse case has an authorial OK; the excess χ coefficient still has a question mark. Cancellation of extraordinary pullback is not evidence the operation never works.
2. Cote56:15 has TWO degree alarms. For Q^(2ν−1), the punctured cone's integral Z/2 lies in degree2ν, not2ν−2. For Q^(2ν), Gysin gives free middle cohomology in degrees2ν and2ν+1, not2ν−1 and2ν+1. Both independent transcriptions retain the second discrepancy. Earlier indexed notes emphasize only the first. The ν=1 surface cone is a useful check.
3. Cote56:26 λ_ν² is written positive; with λ=α−β from30 its sign is (−1)^ν relative to ξ^(2ν). Q²=P1×P1 gives −2[point], not+2[point]. No ink correction authorized. Cote56:20's pairing sign cannot be settled merely by replacing a generator by its negative (a quadratic self-pairing is unchanged by that operation).
4. Cote56:16's unrestricted nested-subtorus Weyl-subquotient claim admits the explicit SL4 counterexample in noteN100. Both Codex and Pro agree on the wording. Opened SGA3 XII re-edition also states unrestricted wording and uses maximality in its proof (pp128–129). Need recompute all lattice stabilizers and distinguish corrected maximal-T statement from the printed false literal assertion.
5. Cote55:17 literal lattice <e1,ie1,e2,e1+ik e2> splits integrally by replacing fourth generator with fourth−first; resulting complex torus is a product of elliptic curves. At18 the inference c',c''∈Q from first-coordinate integrality fails when that coordinate is zero, e.g. x=e2. An alternative extension lattice may illustrate the intended true existential claim, but is a separate reconstruction.
6. Cote55:6 LemmaA for arbitrary ringed spaces is refuted by RP² with constant sheaf C. Quasi-compactness, coherence, noetherian stalks and H1 vanishing for every finite local system were checked, while the sign local system has no global sections. The separate global-generation condition β repairs the categorical argument. Agent16 independently checked this proof; the neighborhood-basis variant is not refuted by this example. The later abstract LemmaB remains class C: its uniform-neighborhood argument is not established by the analytic Siu comparator.
7. Delzant c56:37's u(q)=w2(q) needs the precise descent normalization from Springer1959, not an assumed raw Clifford-Brauer difference. In rank4 over R, <-1,1,1,1> gives zero Hasse-Witt w2 but raw Clifford difference relative to<1,1,1,1> is nonzero. Investigate before verdict; keep normalization conditional.

No source transcription has been edited. All modern reconstructions and counterexample checks are separate from the proposed ink checks.

## Completed source concordance and remaining limits

The reused GIT leaves match Mumford–Fogarty Chapter3 Proposition3.1, Corollary3.2 and Theorem3.8 in the opened second-edition text; their original typescript date and first-edition glyphs were not established. SGA7 XII3.3/3.7 and XV2.1/2.2 give the exact quadric and cone comparisons. SGA3 XII Remark1.6 states the Gm/Ga family, and XIV1.4,3.20,3.21(c) settle the revised torus-containment alternatives.

Original EGA IV.1 and IV.2 were downloaded and read at the cited paragraphs. IV.1 contains the topological-dimension and parameter-ideal arguments; IV.2 contains associated points, reduced modules, field dimension and the flat dimension formula. In particular, IV.2 3.1.7(ii) identifies the missing antecedent of the isolated associated-union formula, and3.2.2 identifies the unfinished reduced-module definition. The missing manuscript clauses are still not filled into the transcription.

The coherent-elimination question has an exact negative answer in the opened LSY2012 theorem, supplemented by a fully checked coherent-product example. The literal complex-torus lattice splits; the alternate nonprojective extension is both independently proved and matched to Oort–Zarhin1996 Lemma3.2 and Rosen–Shnidman2017 Proposition2.3. Their earlier references were followed bibliographically without claiming that every cited book passage was opened.

The root package has115 individually formulated claims,39 problem records and57 reading alarms. Its source/query mapping and certificate integrity are checked in parts/root/audit.json. Those are pre-integration owner counts; the final dossier counts canonical merged records.

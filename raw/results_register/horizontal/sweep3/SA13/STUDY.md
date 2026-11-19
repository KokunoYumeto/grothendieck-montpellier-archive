# SA13 (Séminaire de Géométrie Algébrique, SGA), sweep 3: what the pages contain and establish

This study was led by Claude Opus 5.5 at effort max (agent a84c887cf408574ed, the SA13 lead) on 19 Nov 2026.

**Who read what.** All transcribed pages were read in full, in four stretches:
- `readings/c34.md`: cote 34, scans 3-210, 203 pages, by the c34 reader (agent a8fa5978a09e88ff4, Claude Opus 5.5 at effort max).
- `readings/c33_c36_c39.md`: cotes 33, 36 and 39, 181 pages, by the second reader (agent ac599a5fb99cb85fd, Claude Opus 5.5 at effort max).
- `readings/c32_c35_c37_c40.md`: cotes 32, 35, 37 and 40, 103 pages, by the same second reader.
- `readings/c27_c28_c41_c42.md`: cotes 27, 28, 41 and 42, 63 pages, by the lead.

**Counts.** 550 pages; 184 check events (`CHECK_EVENTS.tsv`); 57 corrections (`CORRECTIONS.tsv`); 24 hunches (`HUNCHES.md`).

**Sources.** Item ids SA13-nn are those of `sweep2/SA13/OBJECTS.tsv`. Print was compared in the French LaTeX of SGA 5 and SGA 7 (`sga7_readers_publish_20261112/sga-fr/volumes/`). Michel Hua's project served as a credited witness only.

**Unread, because untranscribed** (identified on thumbnails only):
- cote 32, scans 7-10 and 12-15 (typescripts);
- cote 37, about 50 typescript scans;
- cote 27, scan 8.

Cotes 29 and 31 belong to SA12.

## The topic in one paragraph

SA13 is the working material of the SGA seminars from about 1965 to 1971:
- **Cote 33:** the 1965 manuscript draft of SGA 5 (the six operations, Künneth, Lefschetz-Verdier, traces, biduality, injective dimension).
- **Cote 34:** Grothendieck's own manuscript of the first SGA 7 exposés (1967-68). Print has only Deligne's summary of it (SGA 7 I, Exp. I).
- **Cote 36:** his part of SGA 7: the draft of Exp. IX with Deligne's written remarks on it, biextensions, Picard duality, invariant cycles, the arithmetic proof of the orthogonality theorem, and the typed draft "Le théorème de Griffiths par voie algébrique" behind SGA 7 XVIII, XX and XXI.
- **Cote 39:** an axiomatics of "elementary" function rings with a formal preparation theorem.
- **Cotes 27-28:** SGA 3 complements, including a "théorème de 1/2 continuité" and notes of Demazure's 1970 talks on the Cremona group.
- **Cotes 32, 35 and 37:** corrections and re-edition planning for SGA 4-7 and EGA. These include a letter from Deligne, with his old version of SGA 4 XVIII 3.1, and a cancelled section "Faux schémas abéliens (ou Motifs mixtes effectifs de poids 1)".
- **Cote 40:** α_p-torsors.
- **Cotes 41-42:** drafts on étale schemes of irreducible components and on networks of local rings.

The mathematics checks out almost everywhere. The corrections are listed below and in `CORRECTIONS.tsv`.

## Cote 33: the SGA 5 draft of 1965 (SA13-1 to SA13-20)

Reading: `readings/c33_c36_c39.md`, first part.

**What the draft contains.**
- The exchange formulas and the "Formulaire" for ⊗^L and D^-.
- The projection formula and Künneth (SA13-3, SA13-4). His "peut-être vrai dès que Y est noethérien" (33/110) fails for coefficients divisible by a residue characteristic; this is hunch H2 of that reading.
- The programme turn and traces over Z/ℓ^ν (SA13-5, SA13-7). His conjecture on 33/118 is SGA 4½, Th. finitude 1.9.
- Tor-dimension (SA13-2).
- The Lefschetz-Verdier formula with K_X ⊠ K_Y = K_{X×Y} and the local Künneth formula (SA13-6, SA13-15, SA13-16).
- "Compléments dualité": a research list (SA13-20) that maps onto the next decade.
- The plausible anti-equivalences and the injective-dimension theorem (SA13-17 to SA13-19).

**Established.**
- **The constructible half of the injective-dimension theorem.** Decided on the scan: on 33/172 (i) the Ext is the sheaf ℰxt, which makes the Pro note's counterexample inapplicable. The 2n bound holds there, via the codimension ≥ j/2 support bound for ℰxt^j.
- **The reduction for the global half.** His Theorem (ii), Ext^i(F, C) = 0 for i > 2n and C with injective stalks, reduces to his question on 33/174. That question is a Lazard theorem for étale sheaves of Z/N-modules. Print (SGA 5 I 1.5) has only ≤ 4n.

**Corrections.** In `CORRECTIONS.tsv`. Among them, the typescript's Lemme 4(c) at 33/145 (an étale criterion, from a reused source) was decided on the scan.

**Reused typescripts, not his.** Topological vector spaces, an analytic operator sheet, a ramification typescript, and an axiomatic étale-topos typescript.

## Cote 34: Grothendieck's manuscript of the first SGA 7 exposés (SA13-21 to SA13-33)

Reading: `readings/c34.md`.

**What the manuscript contains.**
- Exposé I (34/3-51): the ℓ-adic representations of inertia; tame inertia and its cyclotomic twist; integral representations; the local monodromy theorem by the arithmetic route (I §5-6, proved on the pages); the conjectural general statement I 7.1 ("(Serre-Tate)" inserted); its arithmetic proof (I §8); and the reductions of §9, conditional on resolution.
- Exposé II (34/53-82), not printed: Theorem 1.1 on the image of the arithmetic fundamental group, proved on 34/70-78. Also abelian schemes over separably closed fields, change of ℓ, good reduction and CM, almost all ℓ, and H¹.
- Exposé III (34/84-128): the geometric proof. Vanishing cycles, the localization principle, the sheaves Ψ, normal crossings, purity, and the tame vanishing-cycle sheaves (Theorem 6.2; question 6.4, since answered).
- A chapter "IV/V" (34/130-162): affine and global Lefschetz bounds, the five schemes, the local Lefschetz theorem, and a maximal non-smooth point (Theorem 5.6).
- Exposé VI (34/164-181): monodromy and the fundamental group.
- §6 of Exposé II (34/183-199): analytic and algebraic envelopes of profinite groups, a 1968 Tannakian construction of π^alg with Mod(π^alg) ≃ Mod_{Q_ℓ}(π), and Tate's conjecture.
- An appendix on the standard conjectures and weight spectral sequences (34/200-209).

**Established.** The mathematics holds except at eight places:
- **Refuted.** Four overstatements:
  - Serre's lemma "et alors seulement" at ℓ = p (34:67);
  - the ℓ-adic realization over Q (34:36);
  - pure weights on inertia invariants (34:209; refined to weights ≤ i on invariants and ≥ i on coinvariants);
  - "dimensions toujours infinies" (34:195).
- **A false step.** The isogeny step of I 6.1 b) (34:32, counterexample V ⋊ SL₂). The statement survives with the [M,M]-coinvariants.
- **Missing hypotheses.** Three statements of print-level results: 34:5-6 (genericity in Pic = Z), 34:138 and 34:147.
- **Transcription.** One correction: 34:155, where the ink has "de X₀", decided at 400 dpi. With "points de X", Theorem 5.6 would be false.

**Open on the pages.**
- Remark 5.7 b) (local acyclicity by geometric depth), status not determined.
- Lemma 5.3.3, "Donner démonstrations !".
- I 7.3-7.4: ℓ-independence in mixed characteristic.
- The appendix's induction.

## Cote 36: "SGA 7 (ma part)" (SA13-34 to SA13-50, SA13-69)

Reading: `readings/c33_c36_c39.md`, second part.

**36/3-8, the "Remarques. SGA 7 IX".** They are in Deligne's hand on every sheet, compared with his signed letter at 32/31. They are addressed "tu" to the draft's author, and the pencil replies are probably Grothendieck's ("non, mon argument marche").
- The Pro notes' "self-flagged" classification is corrected.
- Decided in sweep 2: "63 est faux" (no point).

**36/10-27, "Le théorème de Griffiths par voie algébrique".** This is the typed draft behind SGA 7 XX, XVIII 5.8 and XXI.
- Théorème 7.1 proves only traces on stable subspaces. That gives non-nilpotence of Frobenius on E₀(Y), the weak form printed as XXI 1.4.
- It does not give Cor. 7.2 or "G₀ n'est pas un p-groupe". The margins say so: "pas prouvé sous cette forme forte".
- Cor. 7.3 survives on the weak form.
- Errors in the draft:
  - the algebraicity of Λ "lorsque X se remonte en car. zéro" is overstated;
  - Lemma 7.6 needs N ≤ r d₁^n;
  - the injectivity of n°4 is not "essentiellement trivial" (print needs (LV) and (A)).
- **Open.** The strong 7.1, and the conjecture of n°6 ("le niveau d'un motif ne peut que diminuer par spécialisation").

**The other sheets of cote 36.**
- **36/28-34:** biextensions of two-term complexes [M → G], a draft of SGA 7 VIII §2. In hunch H1 these are Deligne's 1-motives, drafted for SGA 7.
- **36/35-46:** "Picard et dualité".
- **36/47-52:** biextensions of sheaves of groups.
- **36/53-59:** rigidity, with his questions on a GIT typescript.
- **36/60-72:** "Th. des cycles invariants: Cas du H¹", after Raynaud. It asks "demander Raynaud si Ker est donc Z/dZ" (36/71).
- **36/73-84:** the arithmetic proof of the orthogonality theorem by Frobenius weights, and the Jacobian in relative dimension 1 (the discriminant pairing).
- 36/56: φ(u+v) − φ(u−v) = 2(φ(u)+φ(v)), with a minus; his slip, decided in sweep 2.

## Cote 39: "Fonctions et structures élémentaires" (SA13-51 to SA13-55)

Axioms a)-h) for systems of power-series rings: units, composition, inverse functions, henselianity, flows, Pfaff closure. They also cover differential operators, formal structures and quotients, and a formal preparation and division theorem over complete linearly topologized A (39/19-20, proved; the α index is his slip). Hunch H8: these are close to the Weierstrass systems of Denef-Lipshitz.

**Open.** "f′) implique-t-il f ? il ne semble pas" (39/4), and the faithful-flatness question (39/13).

## Cotes 32, 35, 37: corrections and re-editions (SA13-60 to SA13-65)

Reading: `readings/c32_c35_c37_c40.md`.

**Cote 32.**
- 32/3-25 are correction lists and notes on SGA 4 X, XVII and XVIII, with derived non-additive functors.
- 32/26-48 are in Deligne's hand: XVIII Lemme 1.2.9; his letter and its "Liste de compatibilités manquantes" (32/31-32); and his old version of XVIII 3.1 (32/37-48), with marginal remarks very probably Grothendieck's.
- The Codex inventory's attribution of 37-48 to Grothendieck is corrected.

**Cote 35.** The plan of SGA 7, as a diagram (35/6).

**Cote 37.**
- The SGA 4 re-edition (37/8-38).
- Finite topoi, and biextensions as SGA 7 VIII §4 (37/47-63).
- The SGA 7 and EGA re-edition (37/64-100).
- At 37/79, a cancelled section "Faux schémas abéliens (ou Motifs mixtes effectifs de poids 1)". It plans the local invariant cycle problem for H¹, which 36/60-71 proves.

## Cote 40: torsors under α_p (SA13-66)

Affine group schemes and torsors in Hopf-algebra language (40/2-16), and α_p-torsors (40/17-28).
- **His open step at 40/23 is proved by the reader:** the natural group law on α_p-torsors corresponds to that of A/A^p.
- Hunch H4 of that reading: this is Hopf-Galois theory by hand, possibly before Chase-Sweedler (1969).

## Cotes 27-28: SGA 3 complements; Demazure's Cremona group (SA13-56 to SA13-59)

Reading: `readings/c27_c28_c41_c42.md`.

**27/2-14: typed "Divers pour XII à XIV".**
- Prop. 1.3-1.7 are proved.
- Rosenlicht's Th. 6.4, with Cor. 1 re-derived.
- Torus extensions that split as torsors split; re-proved by the cocycle argument.
- Pic(G) = Pic(G/B)/Im D(T), checked.

**27/15-26.**
- Statement 2° on 27:15, "Pic(G) ≃ Pic(G_k̃)", is refuted as an isomorphism by PU₃. The correct statement is Pic(G) ≅ Pic(G_{k_s})^Γ.
- The nilpotent Lie algebra lemma is checked.
- The characteristic-2 counterexamples (SL₂, PGL₂) are checked.
- A solvable F_p-group with no regular element, checked.
- A non-representable centre, checked.

**27/27-37: the "Théorème de 1/2 continuité".** Semicontinuity of ρ_ab, ρ_aff, ρ_r, ρ_u, ρ_n and ρ_ss for smooth group schemes.
- The proof is partly given. The affineness step (generic affine ⇒ special affine) goes by Frobenius weights, checked.
- Left open: the "lemme à rapporter" (27:34) and ③④ (27:37).
- 27:31 is a reused page of his own, with a self-flagged open claim on Ω̂¹_{A/K_α}.

**Cote 28: Grothendieck's notes of Demazure's talks (5 Jan and 12 Feb 1970).** Published by Demazure, Ann. ENS 1970 (locator unverified).
- Subgroups of maximal rank of Cr_n.
- Root data (x_α, ρ_α), checked on explicit models.
- The commutator formula, checked on de Jonquières maps.
- The "systèmes d'Enriques".
- The equivalence on 28:5 has an index slip. Corrected, and combined with Beauville-Colliot-Thélène-Sansuc-Swinnerton-Dyer (1985), it gives tori of Cr₆ that lie in no maximal split torus (hunch).

## Cotes 41-42: étale schemes of components; networks of local rings (SA13-67, SA13-68)

**Cote 41.** The functor of geometrically irreducible fibre components ("sections monisantes").
- A Lemma building an étale modular M is proved on the page.
- A valuative criterion for M étale separated, and for M finite étale, is stated with a proof through the Lemma.
- **Open:** "La condition (i) est peut-être nécessaire et suffisante" for a non-separated M; "Est-il représentable ???".

**Cote 42.** Networks of local rings.
- The Proposition (Γ = lim of coherent germs) is checked.
- Lemma 3 holds for Y separated, the 1960 "schéma"; it is false for a doubled origin.
- The Remark at 42:7 is decided on the scan as "finie", which is his slip for "infinie".
- **Open:** full faithfulness for non-separated préschémas, and his finiteness question (42:3).

## Where the topic stands

- **Every transcribed page is read.**
- **Missing transcriptions:** about 58 typescript scans in cotes 32 and 37, and scan 27:8.
- **Single witness.** The Codex-web cotes (27, 28, 32, 34/18-210, 35, 36/10-27, 37, 40-42) have one transcription each. The doubtful places need a second witness before an edition.
- **Readings still open:** listed in each reading's "Deliverable state".
- The research questions are in `RESEARCH_PACKAGES.md`.

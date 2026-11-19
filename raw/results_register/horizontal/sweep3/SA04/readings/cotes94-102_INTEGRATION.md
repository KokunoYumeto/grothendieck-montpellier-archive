## STUDY

Read in full by reader R1 (Claude Opus 5.5 at effort max), 19 Nov 2026: Pro text (GPT-6 Astra, ChatGPT Pro mode) for 98 and 100, Codex-web otherwise; one scan viewed (97/005). Full reading: `cotes94-102.md`.

**Cote 94 (SA04-36): representing functors on modules.** Criteria for a functor Mod(A) → Ens to be representable by a module of finite type:
- faithfully flat descent (Lemma 1);
- f-adic gluing (Lemma 2);
- noetherian induction (Prop. 3), the local case through injective hulls (Prop. 4), constructibility of ranks (Remark 5 bis);
- generic base change along regular sequences (Lemma 6, Cor. 7), dualizing modules on a dense open, Theorem 12.

Two theorems follow. Theorem 14 is EGA III 7.7.6 (the module H(F, G) for G flat and f proper), here with a new proof. Theorem 19: Weil restriction of affine schemes along proper flat morphisms is affine. Checked: Lemmas 1-2, Prop. 3, and Lemma 6 b), whose "trivial" step needs the remark that a regular sequence stays regular modulo the nilradical when gr_J is free. Cor. 7 and Lemma 16 have slips.

**Cote 97 (SA04-37): Chern classes and Fuchsian groups.**
- The Chern classes of the regular representation of Z/p: the ink has c_{p−1}(r_G) = ξ₀^{p−1}. Wilson's theorem gives −ξ₀^{p−1}, so c(r_G) = 1 − ξ₀^{p−1}. His conclusion H^{Nk}(G)(p) ≠ 0 stands.
- A cocompact torsion-free Fuchsian group always lifts to SL₂(R): the obstruction is the Euler number 2 − 2g mod 2. This is a spin structure, with E₀ ⊗ E₀ = T_X ⊕ 2.
- The cohomology of B_G, and torsion primes of reductive groups (the matter of his Séminaire Chevalley exposé of 1958).

**Cote 98 (SA04-17): norms and bounded families.**
- An axiomatic theory of norms Y → Σ^r(X/Y) for "normed" morphisms (cf. SGA 4 XVII). Its degree axiom (v bis) holds for finite locally free morphisms, since invariants of a permutation basis are free on the orbit sums.
- Hypersheaves on G-sets and Leray-Čech spectral sequences.
- "Familles limitées" (cf. SGA 6 XIII): a refined Chow lemma; stability of bounded families under ⊗, Hom, Tor and Ext; base-change lemmas for Tor and Ext under flatness of the Tor and Ext sheaves. Both lemmas were checked.
- Reused leaves: Bourbaki *Topologie générale*, and a typescript on abelian varieties carrying his margins.

**Cote 100 (SA04-38): good reduction via p-divisible groups.**
- The theorem: abelian schemes over S are the same as pairs of an abelian scheme over U and a p-divisible group over S. The functor is fully faithful when U meets every component, and an equivalence when the étale depth along T is at least 2 and S has a geometrically unibranch finite cover.
- The proof: Grothendieck's Inventiones 1966 rigidity theorem, Serre-Tate, level structures and Mumford's moduli (the GIT sheets are in the folder), descent along proper epimorphisms, and algebraization of formal abelian schemes.
- The algebraization rests on a Baire-category argument over complete local rings. It was checked, with one qualification: V must be a complete discrete valuation ring.
- The reused EGA IV₄ proofs (14 March 1967) date the folder to after March 1967.
- Pro and K100 diverge strongly on six pages.

**Cote 101 (SA04-39): local cohomology, "Notes antiques 1958".**
- Cones and Proj; local duality for non-quasi-coherent modules, worked out with adèles for n = 2.
- The 1958 notes: the canonical module as "module fondamental", local duality in degrees ≥ k iff H^i(A) = 0 for k ≤ i < n, deficiency modules Ω^{(i)}, and characterizations of Gorenstein rings by Ext^{n−1}, Ext^n and Ext^{n+1}(k, ·). They come before Bass (1963) and the 1961 Harvard seminar.
- His question "Ext^i(K, A) = 0 for all i?" has a positive answer for every complete local noetherian domain: A is pure-injective, hence cotorsion.

**Cote 102 (SA04-40): "Pour EGA VI".** As in the sweep-2 report: gluing of objects of a site along a class M, the "Questions pour Artin", and a plan for properties of morphisms of functors.

**Deliverables.** Nothing is ready for an edition: one transcription pass per cote (two for 100), 8 to 14 unsure marks per scan. Cote 100's divergent pages and the 1958 notes come first.

## HUNCHES

- **H94-1 (one programme for EGA V-VI).** Cotes 94, 98 and 102 are three drafts of one book plan: representability of linear functors (94), finiteness and bounded families (98), gluing and properties of morphisms of functors (102). Grounds: the cross-references to EGA III 7.7, SGA 4 XVII and SGA 6 XIII, the shared methods (generic flatness, noetherian induction), and the EGA VI plan of cote 26 (SA23-28).
- **H100-1 (the source of a known extension theorem).** The theorem of 100/003 is likely the unpublished source of the extension results for abelian schemes via p-divisible groups later cited in the literature (Faltings-Chai, ch. V). Grounds: the hypotheses (étale depth ≥ 2, geometric unibranchness) and the method (moduli with level structure, descent). This is a historical question, to be checked against Faltings-Chai's attributions.
- **H101-1 (priority of the canonical module).** The 1958 notes define the canonical module and characterize Gorenstein rings by Ext(k, A) five years before Bass. Grounds: the dated title "Notes antiques 1958" and the content of 101/017-043. It would be worth a historical note, with care about what Serre and others had at the time.
- **H101-2 (his Problem C and the margins on 101/041-042).** His claim that no two of the three conditions on Ext^{n−1}, Ext^n and Ext^{n+1}(k, M) suffice is a precise statement about modules. Roberts' theorem (rings of type 1 are Gorenstein) bears on a neighbouring statement for rings (P. Roberts, "Rings of type 1 are Gorenstein", Bull. London Math. Soc. 15 (1983), locator to be checked).

## PACKAGES

- **P101-1: his 1958 Gorenstein and canonical-module characterizations, set against the literature.**
  - *Question:* state each characterization of 101/031-043 precisely (Propositions 13-16, the closing theorem, Problem C, and the margin that two of the three Ext conditions do not suffice). Prove or refute each, and give counterexamples for the pairs.
  - *Why:* it is the earliest dated form of this theory in the archive, and his own questions there remain open.
  - *Rests on:* Bass (1963); Roberts (1983); Bruns-Herzog, ch. 3.
  - *Strongest reduction:* SA04-R101-01 to -03.
  - *Material:* 101/017-043 after a reading on the scans.
- **P100-1: the good-reduction theorem of 100/003 in full.**
  - *Question:* prove the theorem as stated (full faithfulness, and the equivalence under étale depth ≥ 2 with a geometrically unibranch finite cover, or his simplicial condition), or find the hypothesis it needs. Compare it with the published extension theorems.
  - *Why:* it is the arithmetic outcome of the Barsotti-Tate programme of cote 93.
  - *Rests on:* Grothendieck (Invent. Math. 1966); Serre-Tate; Raynaud's descent for abelian schemes; Faltings-Chai ch. V; the Baire argument checked here.
  - *Material:* 100/002-045 after the divergent pages are decided on the scans.

## Cote 122 against the research runs (SA20-19); cote 122's open readings; cote 125, local and projective duality (SA20-W2)

By Claude Opus 5.5 at effort max, reader `122_125`, horizontal sweep 3, wave 2, 19 Nov 2026, for ae4ae3dc. The full
working is `readings/122_125.md`; the cote 68 image decisions are in `../SA22/readings/68_images.md`.

**What was read:**
- **Cote 122:**
  - 013–035 of the Pro transcription MPL_122 (GPT-6 Astra, ChatGPT Pro mode);
  - its notes RN001–RN069 and §7, and the doubt rows of 017–035.
- **Cote 125:**
  - all of K125-01, a Work reading by GPT-6.2 Astra at reasoning effort max (ChatGPT Work, batch K);
  - its notes, mathnotes, doubts and check events.
- **The register:**
  - the REGISTER.tsv, EDGES.tsv and CHECK_REGISTER.tsv rows of the seven runs named in SA20-19;
  - the sweep-1 merges;
  - WG H2 in the war-game hunches file.
- **Witness H:** Michel Hua's project, the modern readings of 122 and 125.
- **Scan images:** 122/017, 020, 022, 028, 032; 125/003, 006, 008.

### 1. Cote 122: the open readings, decided on the ink

- **028, local Lefschetz, "un isom pour i ≤ n−2".**
  - The 2 is bold and traced over a 1. The next line, "un mono pour i = n−1", has a cancelled "−2" under a blot.
  - The dual lines read "isom si i ≥ n+1" and "épim si i = n" (the "=" over a "≥", a "+1" struck). They are the
    transposes by Poincaré duality on W and W₀.
- **032, "H^i(W₀) ≅ H^{2n−i−1}(M)^∨ si i ≥ n+1".**
  - The final numeral is a heavy 1 over an earlier 2.
  - The bound is sharp: the map is an isomorphism exactly when H^i(M) = H^{i+1}(M) = 0.
  - His parenthesis "(donc 2n−i−1 ≤ n−3)" belongs to the superseded n+2. With n+1 it reads ≤ n−2, which is the range of
    the next line, "H^i(M) ≅ H^i(W₀) si i ≤ n−2". The two lines are transposes of each other.
  - Michel Hua's project gives the reason. n+2, "épim si i = n+1" and n−3 are what the first vanishing bound of 030
    gives (H^i(M) = 0 for i > n+1, before he struck the "+1"). When he improved that bound he retraced this one to n+1
    and left the rest. Witness H's footnote still reads the bound as n+2.
- **020, "la suite exacte de dévolution qui relie H^i(W−W₀) et H^{i−1}(W₀)".**
  - The word reads "dévolution" letter by letter. It is his word, not a standard term.
  - The sequence is the Gysin (residue) sequence, which 026 writes out. The edition should keep the word, with a note.
- **022, "(signe ?)".**
  - Clear, and in a blacker ink than the line, so it was probably added in the same pass as the bold numerals.
  - The sign of the self-transposition of (a′) is (−1)^n on the middle degree (the intersection form of a 2n-manifold
    is (−1)^n-symmetric), times the sign conventions for shifting and rotating triangles, which the page does not fix.
- **017, the dictionary.** The letter read "[η|γ]" is η, and the row under M reads X′_{η̄}.
  - So the Milnor fibre M is the geometric generic fibre, and the circle S is η: the dictionary of SGA 7 (from memory).

### 2. Cote 122 against the register rows (SA20-19)

The Pro run on MPL_122 compared the pages with seven rows of a register digest it was given, and with one remark of
Michel Hua's project (notes RN062–RN069). None of the rows was written about 122: their places are LM §51.16, 149/35–36,
LM1, LM4 §25 bis and §30, 146 and STRATA, and 149/99–103.

| Row (status) | What the run states | What 122 shows | Verdict |
|---|---|---|---|
| LM7 E.23 (Open) | The section classes of the metabelian and depth-two quotients of π₁(U₃/ℚ) are not determined; the image of the pro-3 map Sect(N/γ₄N ⋊ G_ℚ)/N → Sect(N/γ₃N ⋊ G_ℚ)/N is open | The π of "catégorie dérivée de Λ[π]" (020, 022) is the local monodromy group; RΓ^π is its derived invariants | No shared object |
| FLAGGED_149 B9 (Open in the register) | Prime-to-p injectivity of points into section classes for curves over fields finitely generated over 𝔽_p | "À prouver dans le cas algébrique" (022) and "coefficients généraux" (026) concern the duality triangles | No shared object. B9 has been answered since by ANABELIAN_A1_SUCCESSOR A.1 and ANABELIAN_A1 A.33, merged as stronger in sweep 1 |
| LM1 D.11, LM4 D.12, LM4 F.7 (Open) | The integral μ₂-extensions at 2; torsion in profinite GT₀; the A₅ centralizer comparison | The cited faces (021, 025, 029, 031) are pages 4.11–4.15 of an English typescript by another author (Nagata's quintics, Hironaka's example) | Void comparisons |
| WG H2 (hunch, unchecked) | A limit action carries the cyclotomic action on each vanishing cycle; a smooth proper curve never does | The n = 1 case of 030 is a node: W₀ the Hopf link, M an annulus, the monodromy a Dehn twist about the vanishing cycle. In the étale reading the residue part is L(−1)[−1] | Compatible in cohomology; the nonabelian content of H2 is not on the pages |
| EXIT_TOWER B.27 (Proved, the run's claim) | A finite colimit of finite groupoids built from surfaces with boundary, with boundary-twist lattice A = ℤ^I | 013's gluing data, the boundary trivialisations σ, τ. For n = 1, the choice of σ is a ℤ^{π₀(∂M)}-torsor that moves the monodromy in Γ(M, ∂M) by boundary Dehn twists | Shared group and lattice for n = 1; no shared statement |
| Hua's étale twist | "Dans le cadre étale s'ajoute une torsion (n)"; L(−1)[−1]; Thom isomorphism L(−1)[−2] | No twist on the page. The brackets on 020 were corrected toward shifts ("(−1]" with the ] over the ), and "[−2]") | The tame and Thom twists agree. The (n) is right only on RΓ_c: RΓ_c(M°) ≅ K^∨(−n)[−2n] |

**Check events of the rows** (CHECK_REGISTER, 18 Nov):
- E.23: 15 (intakes and an expert note by Claude Fable 5.2 at effort high; in-run reviews by GPT-6 Astra, ChatGPT Pro
  mode).
- B9: 4.
- D.11: 0.
- D.12: 9.
- F.7: 16, including the 14 Nov intake's "they cannot prove the equality of F.7; they can only fail to refute it".
- B.27: 0.
- WG H2: none (a hunch).

**Which Pro dispositions stand:** all of them. Three are sharpened to "void". Two get a named shared object (WG H2, B.27).
- **Correction to sweep 2:** CLAIM_LINKS.tsv files the typescript's claims (RN055–RN059) under SA20-18 as "his claim".
  They are another author's.

### 3. Cote 125: "Dualité locale et dualité projective" (SA20-W2)

**The folder:**
- 002: a cover title, with a struck "affine".
- 003, 005, 006, 008, 009: his notes.
- 004, 007: two pages of a French typescript with handwritten symbols, numbered III-18 and III-5.
  - It uses internal references of the form "I,1,4,th.2", an early EGA-type draft, not identified here.
  - III-5 is Čech cohomology of an affine covering by Koszul complexes.
- There is no date. The paper and the title point to the SGA 2 period, about 1961–62 (my inference).

**What he does, in order.**
1. **The chain of equivalences (003).** X projective of dimension r, Y closed, 0 < m < r, X̂ the completion along Y.
   - (A) H^p(X−Y, F) = 0 for p ≥ m.
   - (B) The same for O(−n), n large.
   - (C) H^p_Y(X, F) → H^p(X, F) is bijective for p > m and surjective for p = m.
   - (E) By the arrow marked "dualité": Ext^q(X; F, Ω^r) → Ext^q(X̂; F̂, Ω̂^r) is bijective for q < r−m and injective
     for q = r−m.
   - (F) For n large, H^0(X, O(n)) ≅ H^0(X̂, Ô(n)) and H^i(X̂, Ô(n)) = 0 for 0 < i < r−m.
   - (G) H^q(X, F) → H^q(X̂, F̂) is bijective for q < r−m and injective for q = r−m, for F locally free.
   - Two NBs: "le cas p = m peut être omis, car H^m(X, O(−n)) = 0 pour n grand"; and, for Y of dimension n,
     H^p(X−Y, O(∗)) = 0 for 0 < p < r−n−1, with H^0 an isomorphism if n < r−1.
   - "Cas important": n = dim Y, m = r−n.
2. **The duality (005).**
   - H^p_Y(P, F) = lim→ Ext^p(O_{Y_n}, F) and H^p(P−Y, F) = lim→ Ext^p(J^n, F).
   - "Son dual est" lim← Ext^{r−p}(F, O_{Y_n} ⊗ Ω^r) = Ext^{r−p}(Ŷ; F̂, Ω̂^r).
   - The two long exact sequences are written one above the other.
3. **Hypersurface sections (006).**
   - The same pairing for a divisor X′ of dimension r−1: the pairing degrees are r, r−1 and r. "Plus général" adds the
     supports Y and Y′.
   - A "?" asks whether the completed duality holds on X′.
4. **The criterion and a programme (008–009).**
   - For P ⊃ X: H^i(P̂, Ω^r(m)) = 0 for 0 < i < n and H^0 an isomorphism, "pour m grand, ou tt m", stand beside "P − X
     est de dim coh. r−n [et non plus grand]".
   - Then six places where formal schemes enter algebraic geometry: proper morphisms, Lefschetz theory, the formal
     theory of moduli, duality, formal groups and π₁, Greenberg–Néron.

**Checked (re-derived):**
- Every equivalence of 003 holds for X projective and Cohen–Macaulay. The page does not state that hypothesis.
  - (A)⟺(C) is the local cohomology sequence.
  - (A)⟺(B) is a resolution by sums of O(−n) and descending induction.
  - (C)⟺(E) is Serre duality together with the formal duality of 005: the dual of a colimit is a limit, and the dual of
    a surjection is an injection.
  - (E)⟺(G) holds for locally free F, and the chain closes through (B).
  - (F) is (G) for O(n) by Serre vanishing.
- The NB on p = m needs exactly m < r. This supports reading "r > m > 0" in the header (three arches in the ink; the
  Work pass read n).
- The oblique NB holds for X = P^r: local cohomology vanishes below the codimension.
- The typescript's Prop. 2 (007), H^p(U, F) ≅ H^{p+1}((f), M), is the affine case of 003's sequence.
- His "?" on 006 holds for X′ proper: lim← H^j(X′, E_n) = H^j(X̂′, Ê) (EGA 0_III 13.3; from memory).

**Wrong or refined:**
- 008's "de dim coh. r−n" is the vanishing threshold, not the cohomological dimension. The box is equivalent to
  cd(P−X) ≤ r−n−1. When n = dim X that is the least possible value, codim − 1, reached by set-theoretic complete
  intersections.
- Readings decided on the ink and by the mathematics: box B is O(−n); the NB twist is O(∗); "[n = dim Y]"; the
  connecting term on 005 is H^{p+1}_Y.
- Witness H differs from the ink on 008 (H^r, (−n), r−m) and calls r−m "la codimension". On the page r−m = n = dim Y.

**Open:**
- the header bound on 003 (r−n is expected; the ink is overwritten);
- the subscripts "−" and "a" on 006;
- the word after "Lefschetz –" on 008 ("Courant" or "Ce sont" in the Work pass, "Grauert" for witness H);
- the induction that the 006 frame prepares.

**How it connects:**
- 003 and 008 are the duality criterion for the cohomological dimension of a complement. It is in SGA 2 XII §1 and XIII,
  and later in Hartshorne (1968; Ample subvarieties III.3.4; Compositio 1971, Prop. 2.9, cited by Michel Hua's
  project), Ogus and Speiser (all from memory).
- 125 states it for any projective Cohen–Macaulay X, in both directions, with the injectivity clause (H20-122_125-2,
  R20-122_125-2).
- 006 and 008's item 2 are the formal Lefschetz programme of SGA 2. 122/028's "Lefschetz local" is its local side.
- **Deliverables:** 125's handwritten faces are ready after one ink pass on the header bound and the 008–009 list.
  - translate_to "en; vi; fa": the local-cohomology schools of Hanoi and Tehran, weighed against SGA 2 in those
    languages.
  - The typescript pages 004 and 007 are for the user's decision.
- **Hunches:** H20-122_125-1, the variation forced by the trivial action on L; -2; -3.
- **Packages:** R20-122_125-1 (to merge into R20-3) and -2.

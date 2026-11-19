# One-off update of sweep3/SA21/STUDY.md after readers A, B, C (agent a6d42bf6, 19 Nov 2026). Asserts every anchor.
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
P = sys.argv[1]
t = io.open(P, encoding='utf-8').read()

READ = '''## What was read, and how

- **156-4, scans 2-89:** read in full by this agent (a6d42bf6fe2b0d8a8, Claude Opus 5.5 at effort max).
  - The source is the Codex web transcription J156-4-01 to J156-4-11, cleaned by `_tools_a6d42bf6/clean_tex.py`.
  - One scan image was viewed (scan 45).
- **156-3 and 156-5 to 156-9:** read by three readers, each Claude Opus 5.5 at effort max, briefed with `_tools_a6d42bf6/READER_BRIEF.md`:
  - **reader A (a4e5251e8164eb831):**
    - 156-6 in full, with scans 5, 14, 19 and 22 viewed;
    - 156-5 in full, with no scan viewed.
  - **reader B (ae747b2de9d398034):**
    - 156-7: scans 2-60 line by line, scans 61-114 for statements and proofs, five scans viewed;
    - 156-3 in full, with no scan viewed.
  - **reader C (a770b79a, launched by the main session):**
    - 156-8 in full, with scans 4, 6, 31, 32 and 86 viewed;
    - 156-9 in part: scans 2-9, 46-50, 78-80, 109-111 and 115-118 in full, the rest by statement lines.
  - **Where their work is:**
    - their full readings are in `readings/<part>.md`;
    - their study, hunches and packages are merged at the end of this file and of HUNCHES.md and RESEARCH_PACKAGES.md;
    - their check events and corrections are in the tables.
- **156-1 and 156-2:** studied in sweeps 1-2 through the Pro notes. The three readings left open there were decided on the scans in this run (§3).
- **Still read only by statement lines:** 156-7 scans 61-114 (the proofs), and 156-9 scans 10-45, 51-77, 81-108 and 119-140.
- **Michel Hua's project:** the readers used his modernised readings as a credited witness. The ink decided every reading.

**The checks** are in CHECK_EVENTS.tsv. Each re-derivation is one row.

## 0. Cote 156 after the readings (19 Nov 2026)

**What the series is.**
- Between 8 June and 15 July 1986, in nine parts, he axiomatizes tame geometric forms without points:
  - first the contrées (156-4);
  - then the ateliers (156-6, 156-7);
  - then the magasins (156-8);
  - after the word swap of 9 July, ateliers again, with the supports as ortholattices (156-9). The swap is on 156-9/41: "je dirai 'atelier' là où je disais 'magasin', et inversement".
- 156-3 and 156-5 are the one-dimensional and the set-theoretic models. 156-1/2 is the first one-dimensional theory.

**The main results of the readings, in mathematical order.**

1. **The line (156-3).**
   - For a totally ordered tronçon, the tame parts Mod(L) are exactly the finite unions of points and open intervals. These are the definable sets of the o-minimal structure (L, <).
   - So "modéré" on the line is the o-minimal condition, written down in June 1986, at the same time as Pillay and Steinhorn's 1986 paper (reader B; also in Michel Hua's project).
   - A tronçon is known up to reversal from its strict betweenness, and the betweenness is read off the cuts (re-proved).
   - For non-total tronçons this is not in Hilbert 1899 or Huntington-Kline 1917.
2. **The set-theoretic model (156-5).**
   - Admissible families of subsets are preorders on parts of L.
   - The set-theoretic figures, with their refinement and subdivision, satisfy C1-C3, C5-C7 and C8₀ of 156-4 (computed).
   - **His claim that C4 "est automatique" is false.** The multistrates of Fig(L) have 3 components on 2 points and 5 on 3 (SA21-K5-01).
   - The supports are P(L). From the figures one recovers P(L), not L.
3. **The atelier (156-6, 156-7).**
   - 156-6 makes refinement ≪ primitive, where 156-4 had subdivision, with At 1-At 14.
   - At 13, "l'axiome du support", is the axiom 156-4/42 asked for, and subdivision becomes maximal refinement.
   - The Théorème-Scholie of 156-7 is re-derived both ways. It represents spacious ateliers by (M, ≤, ≪) with a disjointness graph on the minimal elements.
   - His characterization of simplices (156-7/14-15) is false: the face poset of a square satisfies "polyédral + At simp 1". Simplices need distributivity.
   - "Axiome des Cat PL VI p.52" (156-7/13) is 156-6/53, the axiom At ens 1. H11 is refuted.
4. **The magasin (156-8).**
   - Mag 1-4 take "intérieurement disjoints" (|∘|) as primitive. From them alone, the compatibility-disjunction axioms of 156-6 and 156-7 and the gluing of refinements follow (re-derived). This is what he means by "l'innovation d'avant-hier faisant tomber tout le fouillis des axiomes de compatibilité-disjonction".
   - The weakened Mag 4′ of 28 June is too weak, by a maquette countermodel.
   - The Proposition-Scholie of 156-8/16-17 lacks the transitivity of ≪°. There is a five-element countermodel, and the ≪°-form repairs it.
   - Oriented maquettes of dimension ≤ 1 are Serre's graphs; Michel Hua's project gives the identification first.
   - His "Sauf erreur" for dimension 2 is not right as stated. The axioms admit 2-cells bounded by several disjoint cycles and exclude the one-vertex torus. With "∂X connected" added, they are the 2-complexes whose cells are attached along simple closed paths.
5. **The supports.**
   - The lattice Σ of supports (156-4/66-69) is not distributive in general. His own counterexample is the "ficelle à deux brins" (156-7/82-84).
   - **In faithful magasins Σ_M is the complete Boolean algebra of regular open sets of the Alexandrov topology of (M, ≪°)** (156-8, SA21-R8-25).
   - Under divisibility and Mag L2: faithful ⇔ Σ is Boolean with the lieux as distinct atoms (156-9 reading).
   - The plain "distributive ⇔ faithful" is refuted, by two non-disjoint lieux.
   - His "spatios" (156-9/78-80) are complete ortholattices.
   - Three of his statements are the **orthomodular law**: Lemma 1 and Cor 1 (156-9/109-111), the formal lemma of 156-7/97-99, and the "axiome des supports" (156-9/117).
   - The orthomodular law **fails on the hexagon O₆**, which arises from the fence a′ < a > b < b′.
   - **MO₂ is orthomodular but not Boolean.**
   - His own diagnosis (156-9/128): "Ce sont mes 'cordes' ... qui causent tous les ennuis".
6. **The July restart (156-9/5-16).**
   - The setting is the magasin of an ordered set: points and intervals with the positional order a < I_{a,b} < b (156-8/90-127).
   - |∘| is comparability, and the figures are the flags of the positional order, not of the incidence order.
   - It is faithful exactly when L is total.
7. **Documentary.**
   - The sheet "Table des Matières T 1 : T 10 … fascicule 4" on 156-9/3 is a reprography order for Récoltes et Semailles ("Fascicule 0"), not a table of the 1986 notes. H12 is refuted (SA21-K9-01).
   - Scans 5 and 7 of 156-8 and scan 114 of 156-9 are Récoltes et Semailles leaves.

**What stays open, in the order of the packages:**
- the support lattice of the non-faithful magasins (cords and strands), and the cograph hunch for comparability magasins (P8-1, P9-1);
- oriented maquettes against regular CW complexes in every dimension (P6, P8-2);
- the o-minimal contrée and its faithfulness (P2, H9-3);
- open on the pages:
  - the converse of the Théorème-Scholie of 156-6;
  - At 9_Σ + At 10 ⇒ At 12;
  - the uniqueness in At 14 bis;
  - the saturation (156-6, 156-9/3);
- what replaces C4 in the axioms.

'''
m = re.search(r'(?ms)^## What was read, and how\n.*?(?=^## 1\. What cote 156 is)', t); assert m
t = t[:m.start()] + READ + t[m.end():]

m = re.search(r'(?ms)^## 4\. 156-3 and 156-5 to 156-9: what was read tonight, and what was not\n.*?(?=^## 5\. )', t); assert m
t = t[:m.start()] + '''## 4. 156-3 and 156-5 to 156-9: this agent's first account, and the readings

- Section 5 is this agent's first account, from the axiom, definition and dated lines (18 Nov).
- The readers' full readings supersede it where they differ. See §0, the merged blocks at the end of this file, and `readings/`.
- The corrections to section 5 are marked in place.

''' + t[m.end():]

a = 'The 1986 notes were organized in fascicules.'
assert a in t; t = t.replace(a, 'Reader C read the sheet as a reprography order for Récoltes et Semailles ("Fascicule 0"), not a table of the 1986 notes (H12 refuted, SA21-K9-01).', 1)
a = 'and those of dimension 2 are presumably the combinatorial cell complexes of dimension ≤ 2 (156-8/6).'
assert a in t; t = t.replace(a, 'and they are Serre\'s graphs. His "Sauf erreur" for dimension 2 needs "∂X connected" (reader C; §0, item 4).', 1)
io.open(P, 'w', encoding='utf-8', newline='\n').write(t)
print('ok', len(t))

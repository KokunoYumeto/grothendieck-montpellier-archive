## STUDY

**156-3, "Réseaux … via découpages", CF III, 8-9 June 1986, scans 2-41.**
- Read in full by Claude Opus 5.5 at effort max (reader B, sub-agent of a6d42bf6fe2b0d8a8) in the transcription, with no scan image viewed (readings/156-3.md).
- Michel Hua's project was used as a credited witness of remarks.

**What the part does.** A second axiomatics of the one-dimensional networks of 156-1/2: tame pairs of lieux (the 0-spheres S₀), and the connected components of the "tame complement" C(T) of a finite tame set (scans 2-6). In order:
1. **The ordered line (scan 7), and the definition of the "tronçon ordonné" (scan 9).** An ordered set that is divisible, directed both ways, with directed cones. It need not be totally ordered; ℝ² with the product order and the doubled line are tronçons.
2. **A tronçon is known up to reversal from strict betweenness** (Lemme, scans 12-14). Betweenness is in turn read off the cuts: for a < b < c only b has its two components disjoint (scans 15-16). Both re-proved; they use divisibility.
3. **The tronçons form the largest class closed under cones** (scan 17).
4. **Closed tame parts** (scans 18-22). Finite unions of mutually tame, disjoint wide closed sub-tronçons. Their decomposition is unique, and intersections and tame sups exist (Prop scan 20). His own counterexample: no tame closure of {0} ∪ {1/n}.
5. **9 June, topologies** (scans 22-25).
   - The interval topology is T₀ for ficelle lieux.
   - His question whether every tronçon is T₀: answered no, by the doubled line. Michel Hua's project gave the answer first, with "ℝ with a doubled origin".
   - Sobriety stays open.
6. **Pseudo-tronçons, the interstitial tronçon, Mod(L)** (scans 26-34).
   - Mod(L) is the poset of tame parts, with a tame complement X′ and a closure.
   - Properties 1)-8) make the mutually tame families Boolean.
   - His margin asks whether tameness is "X ∧ Y exists": refuted in ℝ².
7. **Relativization, components, and the Boolean algebra of a subdivision** (scans 35-40).
8. **His ending** (scan 41). "Ça doit avoir été fait depuis longtemps (Hilbert ?)". He is right for total orders: Hilbert 1899 §3; Huntington-Kline 1917. The recovery of betweenness from cuts in non-total tronçons is not covered there.

**The main connection.**
- For a totally ordered tronçon, Mod(L) is exactly the family of finite unions of points and open intervals: the definable sets of the o-minimal structure (L, <) (also in Michel Hua's project). So "modéré" on the line is the o-minimal condition, written down in June 1986. It is contemporary with Pillay-Steinhorn 1986.
- 156-7/71 corrects the terms of this part: the tame parts should be "constructibles", and the closed ones "modérées". It reuses the tronçon of 156-3/9 for the Stratos of an ordered set.

**Checked:** 13 check events. **Corrected:** 8 (four slips, one refinement, his own renaming, one refuted conjecture, one answered question).

**Open:**
- the axioms on betweenness or on the cut data characterizing a tronçon (scans 17, 41), in the non-total case;
- sobriety;
- properties 1)-8) for non-total tronçons;
- the axioms of scan 4, announced but never written.

## HUNCHES

**H3-1. Grothendieck's tame parts of a line are the o-minimal sets, and 156-3 is the one-dimensional case of H2** (sharpens H2).
- For totally ordered L, Mod(L) is the definable sets of (L, <). The facts he lists, X finite ⇔ X° = ∅ and the uniqueness of the decomposition, are the o-minimal monotonicity facts on the line. His "constructibles" (156-7/71) is the right word for that Boolean algebra.
- Grounds: 156-3/30-34, 40; 156-7/71; Michel Hua's project makes the same link.
- Literature: L. van den Dries, *Tame topology and o-minimal structures*, LMS LN 248, CUP 1998, ch. 1 (locator to be checked); A. Pillay and C. Steinhorn, "Definable sets in ordered structures I", Trans. AMS 295 (1986) 565-592 (locator to be checked).

**H3-2. The cut data (S₀, R_ε) of 156-3 determine the biorder for non-total tronçons too, and their axiomatization is a new, finite-type question.**
- For total orders betweenness is classical (Huntington-Kline 1917), and for partial orders the order from betweenness and comparability is in the literature (Michel Hua's project cites Altwegg 1950 and Courcelle 2020).
- The recovery from cuts (scans 15-16), and the axioms on (S₀, R_ε) that he left as an exercise (scans 17, 41), are not, per the same project's note on Courcelle.
- Grounds: 156-3/12-17, 41, re-proved here.

**H3-3. The Boolean algebra of a subdivision (156-3/40) is the germ of the supports of 156-4/66-69 and 156-7/62-68.** In dimension one, mutually tame parts generate a Boolean algebra whose atoms are the points and open intervals of the subdivision. The failure of distributivity found on 156-7/84 (two strands) is exactly where mutual tameness fails. This confirms his "Conclusion-Scholie" of 156-7/84 and sharpens H3: Boolean on mutually tame families, not beyond.

## PACKAGES

**P3-1. Tronçons from their cuts.**
- **The question:**
  - Give axioms on (S₀ ⊂ P₂(L), R_ε for ε ∈ S₀) that characterize the biordered tronçons, total and non-total, and more generally the networks of 156-1/2 (his scans 4, 17 (2), 41).
  - Decide the sobriety of T₀ tronçons (scan 23).
  - Do properties 1)-8) of Mod(L) (scans 32-34) hold for non-total tronçons?
- **Why it matters:**
  - It is the one-dimensional base of the axiomatics of cote 156, and the question he left as "classical" without checking.
  - The non-total case is not classical.
- **What it rests on:** 156-3/2-41 (read here); 156-1/2 (SA21-2 to SA21-6); 156-7/70-73.
- **Strongest known reduction:**
  - The biorder is determined by betweenness, and betweenness by the cuts (scans 12-16, re-proved).
  - T₀ fails in general (the doubled line). The total case is classical (Huntington-Kline 1917).
- **Material:**
  - the 156-3 .tex and scans;
  - the 156-1/2 package;
  - Huntington-Kline 1917; the references Michel Hua's project gives (Altwegg 1950, Courcelle 2020; locators to be checked);
  - van den Dries 1998, ch. 1.

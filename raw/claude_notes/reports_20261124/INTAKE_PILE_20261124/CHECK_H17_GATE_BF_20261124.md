# H17 note v2, Corollary 22(b): does the Boggi–Funar gap reach it?

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 25 Nov 2026, for the main session 329fb1e6. Check events:
`CHECK_H17_GATE_BF_20261124_CHECK_EVENTS.tsv`.

## Verdict

**Corollary 22(b) is unaffected.**
- The lemma that EXIT_TOWER E.14 disputes is in a later Boggi–Funar preprint. Lochak's Theorem 5.10 does not cite that
  preprint.
- The Boggi–Funar paper Lochak does use, his [3], is the earlier J. Topology paper. From it he takes only the
  type-preservation theorem. He cites it next to his own independent source, and that theorem is proved in [3] without
  the disputed lemma.

## 1. What Lochak's proof of Theorem 5.10 uses from [3]

Lochak, Algebra i Analiz 37:2 (2025), author version (`sources_checked/lochak2025.txt`).
- His reference [3] is Boggi–Funar, *Automorphisms of procongruence curve and pants complexes*, J. Topology 16 (2023),
  no. 3, 936-989 (lines 3194-3195). This is arXiv:2004.04135v4.
- His reference [16] is Lochak, *On procongruence curve complexes and their automorphisms*, Algebra i Analiz 35 (2023),
  no. 3, 57-137.

**The proof of Theorem 5.10** (lines 2918-2983) "gathers information from above".
- **i):** Aut*(Γ̌(S)) = Aut(Č(S)).
- **ii):**
  1. Take F ∈ Aut(Č(S)).
  2. Twist F so that it fixes a (1,3)-piece T. This works "because F is type preserving".
  3. Apply Proposition 4.1 or Theorem 4.2 to the (0,5)- and (1,2)-pieces. This gives a compatible pair.
  4. Proposition 5.7 (from Hatcher–Lochak–Schneps [8] and Nakamura–Schneps [30]) gives an element of Out*(Γ̌(S)).
  5. Injectivity (his Theorem 1.5) closes the circle.

**The uses of [3] on this path:**
- **Type preservation of automorphisms of Č(S):** "it is known ([16], Theorem 6.4 or [3]) that automorphisms of Č(S)
  preserve the topological type of curves" (line 530); "([16], Theorem 6.4 or [3], Theorem 5.3)" (line 1379). In both
  places [3] is an alternative to his own [16].
- **The facts on type preservation** (separating curves; the case (1,2)), "proved in [16] and [3]" (line 2243).
- **The identification Aut(Č(S)) = Aut(prograph Č(S)):** "nontrivial facts from above and [16] (see also [3])" (line 2390).

**What the path does not use:**
- His §5 and the proof of 5.10 do not cite [2], Boggi's *Automorphisms of profinite mapping class groups*
  (arXiv:2011.15075). In §5, "[2]" appears only in Γ_{1,[2]}.
- Theorem 1.5 rests on [16] §7.5.
- Theorem 4.2 rests on [8], [30], [9] and [13].

## 2. Which paper E.14 disputes, and whether [3] depends on it

EXIT_TOWER checkpoint 28, `sections/E.tex` lines 1197-1240 and 2405-2420, read. E.14 says three proof assertions are
false as printed:
1. Boggi2026 (arXiv:2011.15075), Proposition 6.9, p. 36: the closed hyperelliptic group identified with B_{2g+1}/⟨z²⟩.
2. Boggi2026, Lemma 6.16, pp. 42-44: uniqueness of an inertia-preserving extension.
3. **BF2026**, Lemma 2.23, p. 22: P̂Γ_{1,2,γ⃗} ∩ P̂Γ_{0,5} = P̂Γ_{0,5,q(γ)}.

E.14 adds that these "do not refute the main automorphism-group theorems". The later lines (2405-2420) say the error in
Lemma 2.23 "lies upstream of the gluing criterion", so that source's procongruence argument is "not certified by this
audit".

**BF2026 is a different paper from [3].** Its bibliography entry names Boggi–Funar, *Automorphisms of procongruence
pants complexes*, arXiv:2311.17025v3. The arXiv listing (queried on 25 Nov) gives "Automorphisms of the procongruence
pants complex", 2311.17025v3. [3] is 2004.04135v4, published in J. Topology 2023.

**BF2026 builds on [3], not the reverse.** I opened its LaTeX source (`AutPantsv19.tex`).
- It says: "we will make use of several results established in our former paper [BF]" (line 430), where [BF] is the
  J. Topology paper (line 2175).
- It says: "The following two sections will be devoted to improving one of the main results of [BF] (cf.
  [BF, Theorem 8.1])" (line 565). That theorem is on the pants complex.
- Lemma 2.23 sits in those sections, in the S_{1,2} case of the pants-complex rigidity.

**[3] Theorem 5.3 does not depend on it.** I opened its LaTeX source (`main.tex`, lines 1435-1450).
- The theorem: every automorphism of Č(S) is type preserving if S is not of type (1,2); for S_{1,2}, if and only if it
  preserves the separating curves.
- It is proved in [3] §5 through its Lemma "separatingpreserved", from the material of [3] §4 on profinite simple closed
  curves, Dehn twists and centralizers.
- The pants complex is [3] §8. BF2026 is a later preprint that improves [3]'s Theorem 8.1, so it cannot enter [3]'s proof
  of Theorem 5.3.
- Lochak also gives his own [16], Theorem 6.4, for the same fact.

## 3. What is not checked here

- I read the proof of Lochak's Theorem 5.10 in outline. I did not referee [3] Theorem 5.3 or [16] Theorem 6.4 line by
  line.
- I did not check E.14's three counterexamples. They are a claim of an unrefereed run.

None of this touches the dependency question, which is settled by the citations and by the direction of dependence
between the papers.

## The sentence for the note (optional; no v3 is needed)

> Corollary 22(b) rests on Lochak's Theorem 5.10 ii); from Boggi–Funar it uses only the type-preservation theorem of
> *Automorphisms of procongruence curve and pants complexes*, J. Topology 16 (2023), Theorem 5.3, for which Lochak also
> cites his own *On procongruence curve complexes and their automorphisms*, Algebra i Analiz 35 (2023), Theorem 6.4; it
> does not use the later preprint arXiv:2311.17025.

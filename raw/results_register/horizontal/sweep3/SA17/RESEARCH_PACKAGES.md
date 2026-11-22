# SA17 research packages, in concept (sweep 3)

Written by Claude Opus 5.5 at effort max (a34c04448e8299803), 18 Nov 2026. No prompt is written here: the user and the
main session conceptualize the prompts. Literature locators are from memory and marked "to verify". The zips carry
LaTeX where it exists (arXiv e-prints), and PDFs only where no source exists.

Following the rule on Pro slots (one prompt per cluster of related questions), cote 129 gives two clusters.

## SA17-RP1 · Nice IV-V: the Hodge-filtration classification beyond nilpotent divided powers

**Question.**
- **(a) His V.** Let A be p-adically separated and complete, with A_o = A/pA. Decide whether the functor
  G ↦ (G_o, filtration on D(G_o)_A) is fully faithful on BT groups up to isogeny, for every p including p = 2.
  - Decide also whether it is fully faithful integrally.
  - Prove it, or give a counterexample with the exact hypothesis that fails.
- **(b) His IV.** Take a PD thickening S_o ⊂ S whose divided powers are not nilpotent. Decide whether "deforming G_o =
  lifting the Hodge filtration of D(G_o)_{S_o} to D(G_o)_S" holds under each of his two alternative hypotheses: the
  fibres of G_o have no toroidal component, or the fibres of G_o are connected.
  - Prove each, or refute it with the corrected hypothesis.

**Why it matters.**
- V is his own integral form of the "mysterious functor" programme, written at Nice in 1970.
- IV's alternative hypotheses look like the conditions of display theory (HUNCHES H2). If they hold as written, the
  page anticipates them. If not, the exact correction is a new statement about his programme.
- No research run rests on cote 129 so far.

**What it rests on.**
- Cote 129, scans 113-115, with the decided readings:
> [19 Nov 2026, sweep 3.5] Bears on line 28: B:NiceV (129 scan 115) (SA17 intake, confirmed; PROPAGATION.tsv n=500); B:crystal-counterexamples (129 scan 114) (SA17 intake, confirmed; PROPAGATION.tsv n=501). See results_register/horizontal/sweep3_5/SUMMARY.md.
  - 0 → ω_G → D(G)_S → ω̌_{G*} → 0;
  - the negation "n'aient pas de comp. toroïdale".
- Scan 90 ("d + d* = h").
- Items SA17-5, SA17-6, SA17-11 and SA17-13 (STUDY.md).

**Strongest known reduction (from STUDY.md, my derivation, to be checked by the run).**
- For p ≥ 3, the divided powers on pA are nilpotent modulo p^N, so Grothendieck-Messing (Messing LNM 264, V 1.6, to
  verify) along A/p^N → A/p, with the algebraization of BT groups over p-adically complete A (de Jong 1995, 2.4.4,
  to verify), gives V integrally.
- For p = 2, 4A is PD-nilpotent modulo 2^N (v_2(4^m/m!) ≥ m + 1). So the integral statement holds relative to A/4,
  and V reduces to the step A/4 → A/2.
- For A a complete discrete valuation ring of mixed characteristic with perfect residue field, V is known (to verify):
  - Fontaine;
  - Breuil for p > 2;
  - Kisin;
  - W. Kim, Lau and Liu for p = 2.

**Material a run needs.**
- Messing, LNM 264, chapters IV-V.
- Berthelot-Breen-Messing, LNM 930.
- Zink, "The display of a formal p-divisible group", Astérisque 278.
- Lau, "Displays and formal p-divisible groups" (Invent. Math. 2008) and "Frames and finite group schemes over complete
  regular local rings" (2010).
- Kisin, "Crystalline representations and F-crystals" (2006).
- The p = 2 papers of W. Kim, Lau and Liu.
- Scholze-Weinstein, "Moduli of p-divisible groups" (2013).
- Anschütz-Le Bras, "Prismatic Dieudonné theory".
- Grothendieck, SMS 45 (1974) and the Nice talk.
- Our 129 package (MPL_129_077-115 transcription, notes and doubts) and this STUDY.md.

## SA17-RP2 · Dieudonné crystals over general bases: the scan-114 conjecture and the scan-94 complex

**Question.**
- **(a)** Where does the full faithfulness of BT(S)° → Cris Dieud(S) stand?
  - Give the largest classes of bases for which it is proved.
  - Say whether some base is known where it fails, and construct one if none is known and one exists.
  - Say what the essential image is ("Dieudonné crystals": locally free, with F and V, FV = VF = p), and for which
    bases the functor is an equivalence.
- **(b)** Take G finite locally free over a base on which p is locally nilpotent.
  - Construct a Dieudonné complex Δ*(G) of perfect amplitude in [0,1], reducing to the classical module over a perfect
    field.
  - Prove ℓ^G ≃ (D/DF) ⊗^L Δ*(G), his formula of scan 94, or show where it fails.

**Why it matters.**
- (a) is his conjecture as he wrote it.
- (b) is his own statement. It would tie the deformation theory of scan 93 (co-Lie complex) to the Dieudonné theory.

**What it rests on.**
- Cote 129, scans 93-94 and 114-115.
> [19 Nov 2026, sweep 3.5] Bears on line 77: B:L6-refutation (129 scan 94) (SA17 intake, confirmed; PROPAGATION.tsv n=499). See results_register/horizontal/sweep3_5/SUMMARY.md.
- Items SA17-3, SA17-6 and SA17-13.
- HUNCHES H1 and H4.

**Strongest known reduction.**
- Over a perfect field, ℓ^G ≃ D/DF ⊗^L M. Its consistency was checked on μ_p, Z/p and α_p (CHECK_EVENTS).
- BBM's Dieudonné theory of finite locally free groups (to verify).
- Prismatic Dieudonné theory over quasisyntomic rings (Anschütz-Le Bras, to verify).
- Full faithfulness for the classes of bases covered by Berthelot-Messing III, de Jong 1995, de Jong-Messing 1999 and
  Anschütz-Le Bras (which classes, to verify).
- My first candidate counterexample over k[ε]/(ε²) fails (HUNCHES H4), so none is recorded.

**Material a run needs.**
- BBM, LNM 930.
- Berthelot-Messing III (Grothendieck Festschrift I, 1990).
- de Jong, Publ. Math. IHÉS 82 (1995).
- de Jong-Messing, Bull. SMF 127 (1999).
- Lau (JAMS 2013; Compositio 2018).
- Anschütz-Le Bras.
- Mondal (Dieudonné theory via classifying stacks).
- Illusie, LNM 283, ch. VII.
- Mazur-Roberts (1970).
- Grothendieck, SMS 45.
- Our 129 package.

## SA17-RP3 · Cote 131: his representability theorem for locally quasi-finite separated functors, as he states it

**Question.** Prove or refute his Théorème of cote 131, scan 14, as stated: F is representable by an X that is
> [19 Nov 2026, sweep 3.5] Bears on line 104: A:8-literal (131 scan 14) (SA17 intake, counterexample; PROPAGATION.tsv n=302); A:ind-thickening (131 scan 14 margin) (SA17 intake, confirmed; PROPAGATION.tsv n=497). See results_register/horizontal/sweep3_5/SUMMARY.md.
locally quasi-finite and separated over a locally noetherian S iff conditions 1°-8° hold. The conditions are, in
brief:
- fpqc sheaf;
- limits;
- adic limits of artinian rings;
- a Schlessinger-type exactness on artinian arguments;
- finite prorepresenting rings;
- separation;
- local modularity;
- generic modularity.

Settle his two questions from the margin of scan 14:
- **(i)** Give an example over a base of dimension 1 showing that 8° is not superfluous.
- **(ii)** Decide whether 7° follows from the others once 4° is strengthened to noetherian adic rings.

Complete his proof where the sheets stop:
- the constructibility of the modularity locus from 1°-8°;
- the definition of "quasi-modulaire";
- the gluing proposition.

Do the same for the étale and unramified corollaries.

**Why it matters.**
- The sheets are a complete programme with proofs of the formal steps.
- The modern route (Artin's criterion, then "separated, locally quasi-finite algebraic spaces are schemes") uses
  deformation and obstruction theory. His conditions avoid it.
- If his theorem holds as stated, it is a self-contained criterion with weaker-looking hypotheses in the quasi-finite
  case. If it fails, the missing hypothesis is the finding.
- His redundancy questions are precise and have not been answered on the sheets.

**What it rests on.** Cote 131, scans 2-7, 9, 12, 14-17, 20, 23-41, and STUDY.md (SA17-14 to SA17-18). In this sweep
the formal steps were checked:
- Prop. 1;
- Cor. 1, with the gap at T' ×_T T' filled;
- the openness and neighbourhood steps of Prop. 3;
- the diagonal argument of scan 20, with its implicit steps supplied.

**Strongest known reduction.**
- His own: the theorem reduces to the constructibility of the modularity locus (Prop. 3 with Cor. 1 and Prop. 2,
  scans 4-6, 33).
- Necessity is checked.
- From the literature (to verify): Artin's criterion gives an algebraic space when an obstruction theory is
  available, and Knutson's theorem then gives a scheme.

**Material a run needs.**
- Artin, "Algebraization of formal moduli I" (1969) and "Versal deformations and algebraic stacks" (Invent. Math.
  1974).
- Knutson, *Algebraic Spaces* (LNM 203).
- The Stacks Project chapters on Artin's axioms and on locally quasi-finite separated spaces. These are in LaTeX on
  GitHub.
- Schlessinger (1968).
- EGA IV_3 §8 (limits) and EGA IV_4 §17-18 (étale and unramified).
- Raynaud-Gruson (1971), for the flattening functor.
- Raynaud, LNM 119, for the projectivity application.
- Our MPL_131 package and this STUDY.md.

## SA17-RP4 · Cote 133: the finite-set operations and his functor calculus on finite sets and injections

**Question.**
- Determine the Grothendieck ring of his "distinguished" functors on finite sets and injections, modulo his
  "equivalences", with the operations ⊔, × and ∘.
- Decide whether it carries the λ-ring structure he asks about on scan 19 ("λ^i(xy) = ?"), and whether it is special.
- Relate it to the Burnside-ring operations τ^n, T^n and q_H^n of scans 20-23. The corrected formula for T^n in
  terms of τ^n is to be written with φ_α.
- Settle his question of scan 29: classify the rings k for which ⊕ R_k(S_n) is the polynomial ring on the ρ_i. It is
  false for F_p and true over fields of characteristic 0; the open cases include Z_p and other local rings of
  characteristic 0.

**Why it matters.**
- The sheets anticipate FI-sets and species (HUNCHES H10).
- His question of scan 29 is precise, and half-answered.
- Nothing in the research runs rests on cote 133.

**What it rests on.**
- Cote 133, scans 19-29, and STUDY.md.
> [19 Nov 2026, sweep 3.5] Bears on line 179: C:local_charzero_counterexample (133 scan 29) (SA17 intake, confirmed; PROPAGATION.tsv n=503). See results_register/horizontal/sweep3_5/SUMMARY.md.
- The Pro notes F01-F12 (credited).
- The quadratic Witt-group sheets W01-W16 (scans 3-9), not studied in sweep 3.

**Strongest known reduction.**
- Characteristic 0: the Frobenius characteristic and Λ = Z[h_1, h_2, …].
- Characteristic p: the rank of R_{F_p}(S_p) is p(p) − 1.
- His own corrected type decomposition of Hom(I_n, E).

**Material a run needs.**
- Macdonald, *Symmetric Functions and Hall Polynomials* (ch. I).
- Knutson, *λ-rings and the representation theory of the symmetric group* (LNM 308).
- tom Dieck, *Transformation Groups and Representation Theory* (LNM 766), on Burnside-ring power operations.
- Joyal (1986), on species.
- Church-Ellenberg-Farb (2015), on FI-modules.
- Curtis-Reiner, for Grothendieck groups of lattices.
- Our MPL_133 package, its notes and this STUDY.md.
- Pursuing Stacks §§120-122: the notes connect the sheets to it.

## SA17-RP5 · The split Grothendieck-Witt ring WG(S) of a locally ringed topos (cote 133, scans 3-9)
> [19 Nov 2026, sweep 3.5] Bears on line 198: SA17 intake 3. His text (claims about the pages, l.211 (SA17 intake, reading; PROPAGATION.tsv n=387). See results_register/horizontal/sweep3_5/SUMMARY.md.

From the reader a598c2dff473d448c (Claude Opus 5.5 at effort max). It belongs with SA17-RP4 in one cluster, the
λ-operations.

**Question.**
- Is his WG(S) a λ-ring when 2 is invertible (scan 6)?
- Determine WG(B_{O(m)}) ("d'où la tâche").
- Describe the image of the hyperbolic map in the Stiefel-Whitney target.

**Why it matters.** It is his explicit question, and his WG differs from the modern GW for non-affine S.

**What it rests on.**
- Scans 3-9 and their corrections: no pre-λ-structure without 2 invertible; P_i up to λ^i; "Lazard dixit".
- The new formula w(H(E)) = Σ(1+α)^{r−k} c̄_k(E).
- The Pro notes W01-W16 and Michel Hua's project (credited).

**Strongest known reduction.**
- His reduction to B_{O(m)×O(n)}.
- Characteristic 0 by complete reducibility (H-133-1; to verify).
- **21 Nov 2026** (corrected 21 Nov 2026 after the intakes of GCT_PLETH and ALPOGE_GCT, Claude Opus 5.5 at effort
  high): the first question has the answer no in general for specialness: with 2 invertible, GW^⊕ over BC₃ in
  characteristic 3 is not special (ψ³ not multiplicative; GCT_PLETH A-003, re-proved in its intake). Exterior powers do
  not descend to the Witt group (ALPOGE_GCT PL-08, confirmed). Characteristic 0 (H-133-1) and the other
  characteristics p > 3 are not decided by this counterexample.

**Material a run needs.**
- Zibrowius 2015 and 2018.
- McGarraghy.
- Fasel-Haution.
- Laborde 1976 (Mém. SMF 48).
- Delzant 1962.
- Milnor 1970.
- Knebusch.
- Atiyah-Tall 1969.
- SGA 6 V.
- MPL_133.

## SA17-RP6 · A group through its centre and its derived group; formal and algebraic versions (cote 133, scans 36-54)

From the same reader.

**Question.**
1. Which central extensions E give a G with N' = Z(G) and N = DG?
2. Transpose this to formal groups over a perfect field of characteristic p, with (I) and (II) up to isogeny.
3. Relate the algebraic analogue (scans 42-44) to Rosenlicht-Brion.

**Why it matters.** Michel Hua's project registers the centre and derived-group criteria as a finding ("new to us",
unsearched), with a Lean check of the ordinary-group part, credited. The ordinary-group part is now re-derived. The
formal part is new and unproved.

**Strongest known reduction.**
- For discrete abelian π₀ and π₁ the question is linear algebra.
- In the formal case (I) fails exactly through the universal vector extension.

**Material a run needs.**
- Hall 1940.
- Beyl-Tappe, LNM 958.
- Aldrovandi-Noohi 2009.
- Mazur-Messing, LNM 370.
- Demazure-Gabriel.
- Fontaine, Astérisque 47-48.
- Brion 2009 and 2016.
- Rosenlicht 1956.
- MPL_133 notes G01-G21.

## SA17-RP7 · Effective descent along Spec Ô → Spec O for locally quasi-finite separated schemes (step 3 of cote 131)

From the reader ac8bd2a26d00b4f37 (Claude Opus 5.5 at effort max), its package PK-A. It joins SA17-RP3 in one cluster,
the representability programme.

**Question.** For S local noetherian and F satisfying 1°b, does F_Ŝ representable by a locally quasi-finite separated
X imply F_S representable?

**Strongest known reduction.**
- Quasi-compact pieces work, by ZMT and SGA 1 VIII 7.9.
- The rest is a gluing question for algebraic spaces (H-K-1, H-K-2).

**Material a run needs.**
- Cote 131.
- K126-02 (scans 32-35).
- SGA 1 VIII §7.
- EGA IV §18.12.
- The Stacks Project chapters on algebraic spaces and fpqc descent.
- Artin 1969.

## SA17-RP8 · Lemma 1 of cote 128 in characteristic 2 (non-flat descent through the conductor)

From the same reader, its package PK-B. It goes in the same cluster as RP3 and RP7.

**Question.** Is Ker(H^1(A'/A, G_m) → ·) ≅ Ker(H^1(A'/A, G_a) → ·) under C_0 = C_0^* + Im B, or is there a
characteristic-2 counterexample (H-K-4)? The Théorème of cote 128 (GL_m-torsors against H^1) rests on it.

**Material a run needs.**
- K128-01 and K128-02.
- References on Amitsur cohomology.
- Raynaud-Gruson, part II.

## SA17-RP9 · Shioda's height formula in cote 130, made exact

From the same reader, its package PK-C.

**Question.** Write the scans 4-6 correction terms v and the scan 15 formula as the Shioda height formula for the mobile
part J' of a Lefschetz pencil Jacobian, with the corrected Picard count ρ(J') = ρ(X) + deg X − 2.

**Why it matters.** It is a dated anticipation of the Mordell-Weil lattice formula, and it can be checked.

**Material a run needs.**
- K130-01 and K130-02.
- SGA 7 IX.
- Shioda 1990 and 1999.
- Néron 1965.

## Clusters, for the Pro prompts

- **Representability and descent:** RP3, RP7, RP8 (cotes 131, 126-128).
- **λ-operations and finite-set operations:** RP4, RP5 (cote 133).
- **Groups through centre and derived group:** RP6 (cote 133).
- **BT groups and Dieudonné crystals:** RP1, RP2 (cote 129).
- **Heights:** RP9 (cote 130).

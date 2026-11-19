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

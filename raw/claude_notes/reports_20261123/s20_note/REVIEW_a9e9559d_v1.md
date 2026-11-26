# Review before writing: S20 note, Int(R) free for finite-conductor rings (23 Nov 2026)

These comments are by the editor, Claude Opus 5.5 at effort high (agent a9e9559d), the same agent that wrote the checkpoint-12 intake of POLISH_TOPOLOGY_PERIODS.

The source is Paper 2 of that run (GPT-6 Astra, ChatGPT Pro mode):
- Theorem 12.1, the patching lemma;
- Theorem 12.2, the finite-conductor theorem;
- Corollary 15.5.

## 0. Is it useful, and why: yes

The note settles four published conjectures and gives the first positive answer to CFFG Problem 19 for a class of non-Krull domains.

**The conjectures.** Elliott, Comm. Algebra 39 (2011), conjectured three things:
- **Conjecture 2.10:** there is a local, Noetherian, one-dimensional, analytically irreducible domain D with Int(D) not flat.
- **Conjecture 2.15:** Int(D) is not flat for D = F_2 + T F_4[[T]].
- **Conjecture 2.17:** the same for D = F_2[[T^2,T^3]].

He repeated in 2011 (arXiv:1109.3921v1, p. 2) that these were open. In 2016 (arXiv:1608.00171v1, p. 2) he still conjectured that domains with non-free Int(D) exist.

**What the note proves.**
- Int(D) is **free** for every one-dimensional, analytically irreducible, Noetherian local domain D. So all three conjectures are false.
- The note writes the obstruction polynomials explicitly. For D = F_2[[t^2,t^3]], X^2 + X = t^2 h_1 + t^3 h_2 with h_1, h_2 in Int(D). This is exactly the negation of Elliott's statement (1) in Propositions 2.14 and 2.16.

**Why now.** This spring the open-problem list of Cahen-Fontana-Frisch-Glaz (2014) was answered negatively:
- Problem 19 (is Int(D) always flat? always free?) by H. Ma with the reasoning system Rethlas (arXiv:2604.05922, April/May 2026);
- Problem 21 (the biring) by Jiang-Li-Sun-Wang-Xiao-Yu (arXiv:2605.25259, Theorem 3.4).

Both counterexamples use the same **two-branch** domain, F_2 + t(t+1)F_2[t]_S. The note shows that the **one-branch** side behaves the other way. For every such domain:
- Int(D) is free;
- the tensor maps Int(D)^{⊗n} → Int(D^n) are isomorphisms;
- the biring and plethory structure exists and is unique.

So, after Ma and Jiang et al., the dividing line runs between one branch and two, at least where the normalization is finite. A reader who saw the Rethlas results this spring would want to know this. Nobody has posted anything on Hexagon about Int(D) as a module: the search "integer-valued" on 23 Nov returned five unrelated posts.

**Kind: needs a pass.** Ma (2026) and Jiang et al. (2026) are neighbouring work posted elsewhere in recent months. I have done the pass:
- I read both papers at the source (§3 of RECORDS.md).
- War-game: their example and ours do not overlap. Theirs has a two-branch normalization; ours covers every one-branch domain with finite normalization. Nothing of theirs supersedes ours, and ours corrects nothing of theirs. Together they show that the number of branches decides these questions.
- The note says this fairly in Section 1 and in the context section.

Once the pass is written in, the note can go out with the clear ones.

## 1. What we want to say, and what the run's material does not serve

**The run's paper.** In the run the statement sits as Theorem 12.2 of an 85-page paper titled "Grothendieck's collars, cones, and polynomial operations", between concordance theory and PL topology. An algebraist interested in Int(D) would never find it there, and the paper states only "projective".

- **The commutative algebraist** needs the statement in the field's terms: "Int(D) is free; Elliott's Conjectures 2.10, 2.15 and 2.17 are false". The finite-conductor hypothesis should be translated into "one-dimensional, analytically irreducible". The run's paper does neither, and does not give Elliott's own conjecture numbers or the published version (it cites only the 2011 arXiv preprint 1109.3921, where the conjecture is only recalled).
- **Elliott** is served by a short note that names his conjectures at their pages, keeps his flatness criterion (Proposition 2.13) as his, and shows the explicit polynomials his Propositions 2.14 and 2.16 asked about.
- **Ma and the Rethlas team** are served by a note that presents their counterexample as the other half of the picture, and does not place ours "after" or "against" it.
- **The newcomer** is served by a worked example of the smallest case, done by hand.

The run's paper has no example.

## 2. What I add as editor, to be checked by someone other than me

Each item below is reported here and recorded in RECORDS.md as a check event.

1. **"Projective" becomes "free".** Int(R) is countably generated and projective over the local ring R, so it is free by Kaplansky's theorem. This is a strengthening, not a fault: the run's statement is true and weaker.
2. **Corollary for analytically irreducible domains.** It needs three steps:
   - analytically irreducible implies analytically unramified, so the normalization is finite (Stacks, Tag 032Y);
   - the normalization is local, by a completion argument written in full in the note;
   - in the infinite-residue-field case, Int(D) = D[X], by Lagrange interpolation, also written in full.
3. **The two hand examples.** I derived the explicit polynomials h_1, h_2 myself. They are checked by exact series arithmetic: `check_examples.py`, with its output in `check_examples.out`.
4. **Problems 20 and 21 for this class.** These follow from freeness through Elliott's published theorems (Elliott 2007, Propositions 6.8(a) and 6.10(d), as quoted in CFFG p. 9 and Elliott 2011b p. 16). I have not opened Elliott 2007; the note says so.

## 3. Checkpoint 13 against checkpoint 12

Checkpoint 13 (saved 10:48 UTC) has a different Paper 2 main.tex:
- checkpoint 12: SHA-256 c90f7393…;
- checkpoint 13: SHA-256 8162c1af….

The diff has 61 lines. All of them are in the cone convention: base-fixed parametrizations in §1.1, Theorems 1.1 and 1.5, and a new paragraph "Parametrizations of one cone". One locator was corrected to Igusa, dimension ≥ 6.

The text blocks of Theorems 12.1-12.2 with their proofs, of the branch criterion (Theorem 12.3) and of Corollary 15.5 are **byte-identical** in the two checkpoints. I hashed each block separately. **Nothing in S20's statements or proofs changed.** The note is written from checkpoint 13; the theorem numbering is unchanged.

## 4. Faults found

None in the run's statements or proofs that the note uses. I checked Theorems 12.1 and 12.2 line by line in the intake.

Two points of presentation, both fixed in the note:
- the run's paper attributes the conjecture to the 2011 arXiv paper 1109.3921, p. 2, which only recalls it; the conjectures are in Comm. Algebra 39 (2011), pp. 11-12 of arXiv:1105.0142v1;
- the run's paper calls the two rings "flat examples" without saying that they were Elliott's conjectured non-flat ones.

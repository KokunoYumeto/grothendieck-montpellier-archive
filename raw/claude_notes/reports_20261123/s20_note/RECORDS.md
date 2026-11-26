# S20 note: records (23 Nov 2026)

These records are kept by the editor, Claude Opus 5.5 at effort high (agent a9e9559d).

**Files:**

| File | What it is |
|---|---|
| `s20_note.tex` | source; SHA-256 8f9c0462… |
| `s20_note.pdf` | 9 pages; SHA-256 abd76421… |
| `REVIEW_a9e9559d_v1.md` | the editor's review |
| `check_examples.py`, `check_examples.out` | program and its output for the hand examples; script SHA-256 265bcfe1… |
| `build.log` | the build log |

**Build:** three pdflatex passes, 0 overfull boxes, no undefined references. I rendered all 9 pages at 70 dpi and read them. Page 3 was re-read after the last edit, which touched only that page.

**Source of the mathematics:** run POLISH_TOPOLOGY_PERIODS (GPT-6 Astra, ChatGPT Pro mode), Paper 2: Theorem 12.1 (`result-28`), Theorem 12.2 (`result-29`) and Corollary 15.5 (`result-51`).
- Taken from checkpoint 13 (`…_checkpoint_13_20261123T1048Z_unzipped/workbench/homotopy-and-categories-workbench/work/PAPER-02/v1/main.tex`, SHA-256 8162c1af…).
- The blocks from `result-28` to `result-30`, the branch-criterion block, and the `result-51` block are byte-identical to checkpoint 12 (block hashes f972a056…, ace42eb4…, d622450b…).
- The 61 changed lines of checkpoint 13 concern only the cone convention and an Igusa locator.

## 1. Literature, with exact locators

Every source below was fetched on 23 Nov 2026 and read at the locator given, unless the row says otherwise.

| Source | Locator read | What it says / how it bears |
|---|---|---|
| Cahen, Fontana, Frisch, Glaz, *Open problems in commutative ring theory*, in *Commutative Algebra* (Springer 2014) 353-375. Authors' version dated 23 Dec 2013, https://www2.math.uconn.edu/~glaz/Publications_Selected%20Articles/OpenProblemsInCommutativeRingTheory.Springer14.pdf (SHA-256 54236d04…) | pp. 9-10, Problems 19-21; the attribution of Problems 19-23 to J. Elliott | 19a: is Int(D) flat for every domain? 19b: is it free? Free for Dedekind D; locally free for Krull and TV PvMD [37 = Elliott 2011a]. 20: θ_n is an isomorphism if Int(D) is free [35 = Elliott 2007]; is it always injective or surjective? 21: a unique compatible biring; this holds if θ_n is an isomorphism for all n [36 = Elliott CIRM 2010]. |
| J. Elliott, *Integer-valued polynomial rings, t-closure, and associated primes*, Comm. Algebra 39 (2011) 4128-4147; arXiv:1105.0142v1 (SHA-256 1e69da40…) | p. 3 (intro: "evidence ... not flat"); p. 4 (k[[T^2,T^3]] is outside Theorem 1.2); p. 11 (Conjecture 2.10); p. 12 (Lemma 2.11, Lemma 2.12, Proposition 2.13, Proposition 2.14, Conjecture 2.15, Proposition 2.16, Conjecture 2.17, Proposition 2.18) | The conjectures that the note refutes, and the flatness criterion (Proposition 2.13). Statement (1) of Propositions 2.14 and 2.16 is X^2+X ∉ M Int(D); the note proves its negation. |
| J. Elliott, *Presentations and module bases of integer-valued polynomial rings*, arXiv:1109.3921v1, only version, no journal reference (SHA-256 c144fb04…) | p. 2 (Int(D) free for Dedekind D, [CC Remark II.3.7(iii)]; "no confirmed examples" of non-free; the conjecture "is still open"); p. 16 (θ_X is an isomorphism if Int(D) is free, citing Elliott 2007 Propositions 6.8(a) and 6.10(d); Proposition 5.4 with F_q = (X^q - X)/π) | Status in 2011; the route to Corollary 3. |
| J. Elliott, *Integer-valued polynomials on commutative rings and modules*, arXiv:1608.00171v1 (dated 10 July 2018 inside; SHA-256 278ad48b…) | pp. 1-2 | (1) free ⇒ (3)-(5): unique R-plethory and the universal properties [Elliott, Idempotent plethories, J. Algebra 463 (2016), Theorems 2.9 and 7.11; not opened]. The author "has conjectured that there exist integral domains D such that Int(D) is not free". Nothing on these rings. |
| H. Ma, *A counterexample to Problem 19 on integer-valued polynomial rings*, arXiv:2604.05922v2 (27 May 2026; SHA-256 0685fe69…) | p. 1 (Problem 19 quoted; Theorem 1.1); §2 Proposition 2.1 (= Elliott's Proposition 2.13); §3 Lemma 3.1, pp. 2-4 (D = F_2 + t(t+1)T, T semilocal with two maximal ideals); §4 Proposition 4.1, pp. 4-5; §5 Corollary 5.1 (19a and 19b negative); §6 (found by Rethlas, checked by Ma) | A two-branch non-flat example. It does not touch analytically irreducible domains, and so not Conjecture 2.10. No overlap with our theorem. |
| J. Jiang, Y. Li, Z. Sun, Y. Wang, L. Xiao, J. Yu, *On some open problems in commutative algebra resolved by Rethlas*, arXiv:2605.25259v2 (28 May 2026) | pp. 1-2 (overview); Problem 2.4 (= CFFG Problem 21); Theorem 3.4 with its full proof, §3.4 | The same two-branch domain has no compatible biring. Our Corollary 3 gives the opposite for one-branch domains with finite normalization. The text contains no mention of F_2[[T^2,T^3]] or F_2 + T F_4[[T]] (checked by a text search). |
| H. Ju et al., *Automated conjecture resolution with formal verification*, arXiv:2604.03789 | abstract and listing only | The Rethlas/Archon system cited by Ma; its own case study is Anderson's quasi-completeness problem. Not about Int(D). |
| Stacks Project, Tag 032Y (Lemma 10.162.10) | the tag page, opened 23 Nov; item (5) | An analytically unramified Noetherian local domain is N-1: its normalization is finite. Used in Corollary 2. |
| Hexagon (hexagonmath.org) | search "integer-valued", 23 Nov | Five unrelated hits: 2611.00793 (Graham), 2611.00411, 2611.00210, 2611.00205 (Tang), 2610.00591 (Grinberg). None concerns Int(D) as a module. |
| Hexagon | search "commutative algebra flat module" | 0 hits. |
| Web searches (extended) for Elliott's conjecture, F_2[[T^2,T^3]], flatness of Int(D) | 23 Nov | Only Elliott's papers and Ma's preprint. No proof of flatness or freeness for these rings was found. |
| P.-J. Cahen, J.-L. Chabert, *Integer-Valued Polynomials*, AMS Math. Surveys Monogr. 48 (1997) | **not consulted: no free copy** | What this leaves open: whether the book proves freeness for some class containing these rings. This is very unlikely: Elliott, who cites it, called the question open in 2011 and conjectured non-flatness for exactly these rings. The note says the book was not consulted. |

**Cited from memory, not opened:**
- Atiyah-Macdonald: Theorem 8.7, Propositions 10.13 and 10.14.
- Kaplansky, Ann. of Math. 68 (1958), Theorem 2.
- Milnor, *Introduction to Algebraic K-Theory* (1971), §2, and Whitehead's lemma.
- Bhargava, J. reine angew. Math. 490 (1997).
- Elliott 2007, Propositions 6.8(a) and 6.10(d), and Elliott CIRM 2010, as quoted in CFFG and Elliott 2011b.

The note's method section says this.

## 2. Checks, by model and effort

Types follow HOW.md.

| Statement | Date | Who | Type | Outcome |
|---|---|---|---|---|
| Thm 1 (run's Theorem 12.2) and its Lemma 8 (run's 12.1) | 23 Nov | GPT-6 Astra (ChatGPT Pro mode), run's own event P02-C039 | targeted proof check | no fault found ("greedy Newton basis, congruence indicators, free refinement module, conductor pullback" checked) |
| Thm 1 / Lemma 8, as run statements | 23 Nov | GPT-6 Astra (ChatGPT Pro mode), run's own scope review P02-ROOT-SCOPE081 | targeted proof check | B.021-B.025 accepted at exact scope |
| Thm 1, Lemmas 4-8 | 23 Nov | Claude Opus 5.5 at effort high (POLISH_TOPOLOGY_PERIODS cp12 intake) | targeted proof check | confirmed, every step |
| Thm 1, "projective" strengthened to "free" | 23 Nov | Claude Opus 5.5 at effort high (cp12 intake, and this editing) | targeted proof check | Kaplansky applies: countably generated projective over local R |
| Lemma 4, Noetherian step | 23 Nov | Claude Opus 5.5 at effort high (editor) | targeted proof check | The run's wording ("JhV is finite because V is") is completed in the note: hJ = hπ^mV ≅ V. Not a fault, a precision. |
| Corollary 2 (analytically irreducible case) | 23 Nov | Claude Opus 5.5 at effort high (editor) | targeted proof check | proof written by the editor. Gate: **check by someone other than the editor** |
| Corollary 3 | 23 Nov | Claude Opus 5.5 at effort high (editor) | carried as background without fault found | rests on Elliott 2007 and CIRM 2010 as quoted by CFFG pp. 9-10 and Elliott 2011b p. 16; those papers not opened |
| Example 9 (F_2 + tF_4[[t]]) and Example 10 (F_2[[t^2,t^3]]) | 23 Nov | Claude Opus 5.5 at effort high (editor) | computation or formal certificate | `check_examples.py`: 400 random x each; values of h_1, h_2 lie in D up to precision t^52 and t^56 |
| Examples 9 and 10 by hand | 23 Nov | Claude Opus 5.5 at effort high (editor) | targeted proof check | derivation in the note; the program confirms it |
| Thm 1 | — | — | independent re-proof | **none yet** (see §4) |

No fault was found in any statement or proof that the note uses. No statement was changed.

## 3. Pass for neighbouring work

The kind is **needs a pass**: Ma (April/May 2026) and Jiang et al. (May 2026) are neighbouring work. I did the pass:
- I read both papers at the locators above.
- War-game: their domain is two-branch, and our theorem needs a local finite normalization. Their example and ours are disjoint, neither supersedes the other, and ours corrects nothing of theirs. Together they show that the branch count decides flatness, freeness and the biring, at least with finite normalization.
- The note's Section 1 ("Why this matters", "The credit") and Section 2 say this.

## 4. Five Hexagon tests

| Test | State |
|---|---|
| 1. Complete | Every step is proved in the note. |
| 2. Self-contained | Inputs are standard textbook results (Atiyah-Macdonald, Kaplansky, Stacks 032Y), cited. |
| 3. Stable | The run's checkpoint 13 is probably its last, and S20's text is unchanged in it. The literature search found no prior proof. The Cahen-Chabert book was not consulted (see §1). |
| 4. Checked | Two targeted checks (the run's and my intake's) and a computation for the examples. **Missing:** an independent re-proof of Theorem 1, and a check of Corollary 2 by someone other than its author (me). |
| 5. Of interest now | Strong: Problems 19 and 21 were answered this spring, by the same two-branch example. |

**Left before posting:**
1. An independent re-proof of Theorem 1 and a check of Corollary 2 by another agent: a fresh Claude, given only the statement and the commutative-algebra facts used.
2. The user's word.
3. Optional: the e-mail to Elliott sent first.

## 5. Whom to write to when it is posted

All drafts unsent.
- **Jesse Elliott** (CSU Channel Islands): his Conjectures 2.10, 2.15 and 2.17 are refuted, and his flatness criterion is used. The draft is updated in `field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/EMAIL_DRAFTS_POLISH_TOPOLOGY_PERIODS.md` (Draft 2, version of 23 Nov 2026 ~14:xx UTC).
- **Haotian Ma** (Zhejiang University): our note is the one-branch complement to his counterexample. A short courtesy note with the link, no draft yet.
- **Sophie Frisch and Paul-Jean Cahen**, as keepers of the problem list: Problems 19-21 on this class. Optional.

## Main-session reading, 23 Nov 2026 13:54 UTC

Read in full by the main session 329fb1e6 (Claude Opus 5.5 at effort max), every step followed: Lemma (ring) including the inverse of an element of 1+J and the Noetherian and dimension arguments; Lemma (Newton basis); Lemma (indicators): the identity for delta(x)-delta(y), the induction on valuations, H_c and the Q^m-th power; Lemma (free functions); Lemma (patching): the Whitehead factorization multiplied out, the lift and the map (b,c) -> (Gamma^-1 b, c); the proof of Theorem 1 (A = M_alpha); Corollary 2 (Lagrange for infinite residue field; Stacks Tag 032Y = Lemma 10.162.10(4), checked at the source on 23 Nov; r = 1 through D' (x) D-hat inside Frac(D-hat); the conductor); both examples recomputed by hand. Type: targeted proof check. Outcome: confirmed; no gap.

Before posting: the note on method should name this check; Corollary 3 rests on Elliott 2007 (Props 6.8(a), 6.10(d)) and Elliott 2010 as recalled by CFFG pp. 9-10 (open them at the source, or say so as now); the other locators given from memory; the workbench address; view every rendered page; the user's word.


## 6. After posting (added 23 Nov 2026, evening intake, Claude Opus 5.5 at effort high)

- Posted as hexagon:2611.00937 (board WB-0004), committed 14:24 UTC by the main session.
- Checkpoint 13 is probably the run's last. Its Paper 2 blocks for Theorems 12.1-12.2, the branch criterion and Corollary 15.5 are byte-identical to checkpoint 12, so nothing in the note needs changing. The continuation prompt 91b carries the note's literature (Elliott's conjectures at their pages, Ma, Jiang et al.) into Paper 2.
- Still open from section 4: an independent re-proof of Theorem 1 and a check of Corollary 2 by an agent other than the editor.


## 7. Prior announcement found by the run's continuation (added 23 Nov 2026 ~23:4x UTC, cp19 intake, Claude Opus 5.5 at effort high)

- **Source.** J. Elliott, MathOverflow question 75202, "Polynomials mapping the twisted cubic power series ring to itself": https://mathoverflow.net/q/75202. Asked 12 Sep 2011; edited 26 Dec 2013.
- **Read at the source** by me on 23 Nov 2026 (HTML fetched with curl; SHA-256 2963f1f2...). The edit reads: "ADDED TWO YEARS LATER: It turns out that Int(D) is free over D for D = F_2[[T^2,T^3]]. I will be writing up the proof in a paper at some point."
- **Also on the page:**
  - user2035's 2011 answer refutes the derivative bound Elliott asked about.
  - Elliott's 2011 comment: "I was really hoping I could show that X^2+X is not of the form T^2 f(X) + T^3 g(X)".
- **What it means for the posted note** (hexagon:2611.00937, version 1). Freeness for the cusp F_2[[T^2,T^3]] was announced by Elliott himself in 2013, without a proof that we could find in print. Version 1 says "We know of no earlier proof that Int(D) is flat for either of Elliott's two rings". That is true of proofs, but it omits the announcement, so the credit is incomplete.
- **The repair.** `s20_note_v2.tex` / `s20_note_v2.pdf` (9 pp.; 3 passes, 0 overfull; pages 1-3, 8 and 9 viewed, pages 4-7 have unchanged text):
  - it credits the announcement in the abstract, in Section 1 and in "The credit";
  - it adds the MathOverflow reference [10];
  - the mathematics is unchanged.
- **For the main session:** whether to post version 2 on Hexagon. Draft 2 of the Elliott e-mail is revised to acknowledge his announcement.
- **Cross-check.** The run's continuation (checkpoint 19, Paper 2) found the same item and credits it: notes/continuation_integer_root_literature.md; its HTML SHA-256 0f0159b6... comes from a different fetch.

## Version 2 committed (24 Nov 2026, 00:03 UTC)
Main session 329fb1e6 (Claude Opus 5.5 at effort max), under the standing rule hexagon-post-when-sure. Version 1
(published 23 Nov 21:40 UTC) lacked the credit to J. Elliott's announcement on MathOverflow 75202 (addition of
26 December 2013) that Int(F_2[[T^2,T^3]]) is free; found by the POLISH_TOPOLOGY_PERIODS cp19 intake (a9e9559d,
Claude Opus 5.5 at effort high), who read the MathOverflow page at the source and built v2 (s20_note_v2.tex/pdf;
mathematics unchanged; abstract, introduction, credit paragraph, note on method and references changed).
- Every page of s20_note_v2.pdf read by the main session (23 Nov ~22:50 UTC); 0 overfull boxes in the build log.
- Hexagon: revise -> draft b54e4f65; v1's staged source removed; v2 source uploaded as int_free_analytically_irreducible.tex
  (28,945 bytes, SHA-256 cef7f513f219e448...); metadata HEXAGON_METADATA_WB0004_v2.json (the v2 abstract; the change
  note at the head of `comments`; author fields kept as stored); verify-meta: every field as ours (formalizations [] by
  the server); compile preview HEXAGON_PREVIEW_WB0004_v2.pdf word-for-word identical to the local build (4,409 words,
  9 pp., 0 differing tokens).
- Committed 24 Nov 00:03:25 UTC: hexagon:2611.00937v2, sourceTreeSha256 91b70865dd601de8...; status compiling at 00:03:36.

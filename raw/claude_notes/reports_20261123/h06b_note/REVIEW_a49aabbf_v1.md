# H06b, editor's comments before writing (v1)

Claude Fable 5.2 at effort max (agent a49aabbf5ed57bb8e), 23 Nov 2026. The mathematics and the current text (19 pages,
`papers/ihara/main.tex` of the run's checkpoint 11; identical in checkpoint 13) are by GPT-6 Astra (ChatGPT Pro mode).

## The reading gate: is "Vandiver implies Ihara", or the range p < 2^31, already known?

**As far as this pass can tell, no. What is known is the regular case.**

- **Known.** Sharifi, Proc. Sympos. Pure Math. 70 (2002) 275–284, Theorem 1.1 (p. 2 of the author's version): at an
  odd regular prime, the Deligne–Ihara conjecture implies Ω_p* = Ω_p. Brown, Ann. of Math. 175 (2012), Theorem 1.1,
  proves that conjecture. So the question of Anderson–Ihara (Ann. of Math. 128 (1988), p. 272, question (a)) has a
  positive answer at odd regular primes. Ishii, arXiv:2312.04196v3 (6 Jan 2026), Theorem 1.1 and Remark 1.1.1, p. 2,
  recalls exactly this and proves the analogue for once-punctured CM elliptic curves under an analogue of
  Deligne–Ihara. Hart–Harvey–Ong, Math. Comp. 86 (2017), §1 item (2): Vandiver's conjecture for every odd prime below 2^31.
- **Not found.** Any statement of the field equality at an irregular prime, under Vandiver's or Greenberg's
  conjecture or otherwise. Two web searches of 23 Nov returned only the regular case; one result (Rasmussen–Tamagawa,
  arXiv:1803.08524) is on a related rationality question, not on this one. Hexagon: "Ihara" gives one unrelated
  work, "Vandiver" none.
- **How far I read.** Abstracts only: Sharifi 2002 (arXiv math/0104116), Ishii 2312.04196 and 2602.00615,
  Rasmussen–Tamagawa. The locators above are the run's (its SOURCE_AUDIT.md lists each source it opened, with page
  and SHA-256). I did not open Sharifi's Annals paper of 2011, Fukaya–Kato or Wake–Wang-Erickson. My context was
  past 70 %, and our rule then is to read no more literature.
- **What that leaves open.** One outside reading before posting: Sharifi 2002, §§1 and 4 (what he proves at irregular
  primes concerns integral generation by Soulé elements, a different question; this should be confirmed at the
  source), and the introduction of Sharifi, Ann. of Math. 173 (2011), for any remark on the kernel field.

## What we want to say

1. The question is Anderson and Ihara's, the inclusion is Ihara's, the regular case is Sharifi's with Brown. The
   theorem: the answer is yes at every odd prime with X_p^+ finite, in particular at every prime satisfying
   Vandiver's conjecture, so at every odd prime below 2^31.
2. The mechanism in one paragraph: at an irregular prime the abelianization of H = Gal(Ω_p/Q(μ_{p^∞})) has an even
   part; its generators enter the free Lie algebra in length two with denominators q_e, and the integral symbol
   theorems of Fukaya–Kato and Wake–Wang-Erickson force the numerators not to vanish on the poles.
3. The Vandiver form first, as the board asks. The proof in the current text is the same for finite X_p^+, so the
   theorem states both and the title names Vandiver.

## Whom the current text would not serve

- **The newcomer.** Its abstract opens well, but Section 1 goes from the definitions to the theorem in half a page;
  the answer to "what was known at irregular primes" is one clause. There is no section headed "Proof overview";
  the paragraph "Why poles enter" is one, compressed.
- **The expert.** The text is checkable. It carries p = 2 with a separate analytic argument, which lengthens a
  first note and has its own conventions at the real place.
- **The people whose work it is.** The credit is exact in the body. The abstract's last sentence names the checks
  without effort settings and says "reread by GPT-6 Astra", which is process.

## Decisions

1. **The note is the run's text with a new opening.** Sections 1–2 are mine: the question, the theorem in words,
   why it matters, credit, context, scope, proof overview. Sections 3–8 are the run's Sections 2–6 and 8, unchanged
   except for five places listed in RECORDS.md. This follows the brief for long rigorous texts: the editor writes
   the opening, the body stays Astra's.
2. **p = 2 is left out** of this note (the run's Section 7), and the numerical corollary is stated for odd primes.
3. **No mathematics is changed.** I read Sections 2–6 of the run's text once, as an editor. I did not referee them.

## Kind of note

**Needs a pass, and the pass is not complete.** Nobody has posted on it at Hexagon, and I found nothing at irregular
primes elsewhere. But the neighbouring work (Sharifi 2002 and 2011, Fukaya–Kato, Wake–Wang-Erickson, Ishii 2026) is
exactly what the proof and its context rest on, and of those I read abstracts only. It goes out after the clear ones.

## Before posting

1. The outside reading named above (Sharifi 2002 §§1, 4; Sharifi 2011, introduction).
2. A check of Sections 4–6 of the note (the run's §§3–5) in their present text. The Opus intake of 23 Nov checked
   the Vandiver lemma in this text, and the pole-separation argument and the Vandiver deduction in earlier versions
   (21–22 Nov); it did not compare the new text with those line by line, and it did not check the use of
   Fukaya–Kato and Wake–Wang-Erickson.
3. The user's word and the line of authors.

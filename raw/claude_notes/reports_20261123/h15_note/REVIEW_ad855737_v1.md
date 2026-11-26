# H15 note: comments before writing (v1)

By the field expert and editor of this note, Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by
the main session (Claude Opus 5.5 at effort max), 23 Nov 2026.

**Sources.**
- The run's paper: Part A of the CM-orbits paper of the night run, `main.tex`, read whole and checked step by step on
  23 Nov.
- My intake of it.
- The main session's gate, `GATE_JASWAL_GR23_20261123.md`.

**Read at the source today:**
- Gaudron-Rémond, *Nouveaux théorèmes d'isogénie*, authors' preprint (Sept. 2022): Notations 1.1-1.2, Theorems
  1.5(2), 1.8 and 1.9, Proposition 13.7. Page 15 was rendered and read.
- Tsimerman, arXiv:1506.01466v5: Theorems 1.1, 4.1, 5.1, 5.2 and §3.
- The abstracts of:
  - Banks arXiv:2610.15483 and arXiv:2610.31402;
  - Liu hexagon:2611.00080v2;
  - Binyamini-Schmidt-Yafaev arXiv:2104.05842;
  - Pila-Shankar-Tsimerman arXiv:2109.08788;
  - Tsimerman arXiv:1103.5619.
- The Hexagon listings for October and November 2026 (all four November pages).

## Is the result useful, and why

**Yes.** It is the first lower bound for the Galois orbits of all CM points of A_g with an explicit exponent and
explicit constants: |Gal·x| ≥ c_g |disc Z(End A_x)|^{1/(4g)}, logarithmically D^{1/(2g)}. It covers every centre
order and every product, so it is exactly the input that the Pila-Zannier strategy for André-Oort on A_g consumes.

- Tsimerman's bound (Ann. Math. 2018, Thm 5.1 in arXiv v5) has an unspecified exponent, less than 1/(4c_g) with c_g the
  Masser-Wüstholz isogeny exponent, and an ineffective constant through Brauer-Siegel.
- Jaswal's effective orbit bound (hexagon:2611.00339v3, Prop. 3.3) holds for all Shimura varieties. Its exponent,
  1/(16 t s n_T(n_T−1)), is measured in the discriminant of the Galois closure.
- For A_g, ours is much stronger in the exponent, and it is measured in the discriminant of the centre itself.

The proof is short and transparent. Two published theorems carry it:
- Gaudron-Rémond's 2023 isogeny theorem (Theorems 1.5(2) and 1.8): the discriminant of the Galois image bounds the
  centre discriminant;
- the averaged Colmez formula: the height of a CM abelian variety.

Alpöge's theorem enters at one place: it excludes a possible exceptional zero of L(s, χ_{E/F}) near 1, which is what
made the earlier height bounds ineffective.

## What we want to say, and what the draft material would not serve

1. **The run's abstract says "make the estimates explicit using Alpöge's theorem" as if effectivity were the news.**
   It is not, since October 2026.
   - W. Banks (arXiv:2610.15483), writing up an OpenAI manuscript, proves (1 − β) log q ≥ 3.0·10⁻³ for every real
     zero of every real primitive L(s, χ) with q ≥ 3 (abstract read).
   - Cureton-Thorner (hexagon:2610.00200) prove a zero-free half-plane for every Dedekind zeta function.
   - Liu (hexagon:2611.00080) bounds every real zero of every Dedekind zeta function.

   Any of these, refereed or not, makes the same proof effective with other constants. **The news is the exponent
   1/(4g) with explicit constants, for every centre order.** The note says this plainly, and its Remark 5 gives the
   constants under Banks's bound: a_r becomes 2^{r−1}(75/2 + max(16 r!, 1/δ)).
2. **The expert** wants to see at once that the exponent comes from Gaudron-Rémond's d ≤ Υ^{2n} and Υ ≪ [K:Q]·h.
   - The newcomer wants the mechanism in one paragraph: Galois commutes with the endomorphisms, so it lies in the centre
     and its discriminant bounds the centre discriminant; Gaudron-Rémond bound that discriminant by (degree × height)^{2n};
     averaged Colmez bounds the height by log D.
   - Both are served by a "Proof overview" section before the lemmas. The run's paper had no such section.
3. **Gaudron and Rémond** carry the proof and should be credited first after Tsimerman. Their own Theorem 1.9(5),
   combined with our centre lemma and height bound, already gives an explicit orbit bound, with exponent 1/(4g²).
   The note says so; the finer Theorem 1.8 gives 1/(2g).
4. **Jaswal** should find his Proposition 3.3 stated beside ours with the exact difference (invariant, exponent, input,
   generality), and his effective André-Oort credited as his, with Cureton-Thorner's half-plane.
5. **Out of the note:** the run's André-Oort specialization section, the surface enumeration algorithm, the
   120-class list and the elliptic class-number lists. They are other material, and either cited work or long. The
   note keeps:
   - the orbit theorem and its four lemmas;
   - the explicit corollary for rational CM points of A_2 (D < 10^80);
   - one elliptic sanity check (D = 163, 427).

**Kind of note: needs a pass, now done.** The neighbouring works were posted or appeared within the last weeks:
- Jaswal (Hexagon, 18 Nov);
- Cureton-Thorner (Hexagon, Oct.);
- Liu (Hexagon, Nov.);
- Banks (arXiv, Oct.).

The note integrates them in its context and credit sections. With this pass done it can go out.

## Faults found in the source material (no mathematical fault)

| Place | Fault | Repair |
|---|---|---|
| Run's §1 | Cites Tsimerman "Theorem 5.2, p. 385" for the orbit bound. In arXiv v5 the orbit bound is Theorem 5.1 (§5) and Theorem 5.2 is André-Oort. | The note cites Theorem 5.1 and Theorem 4.1 of arXiv v5. The published page numbering was not seen. |
| Run's abstract and §1 | Presents effectivity as the contribution. | The note presents the exponent and the explicit constants as the contribution, and the zero-free inputs as interchangeable (Remark 5). |
| Run's §5 | Uses Theorem 1.8 without noting Theorem 1.9(5). | The note states both and why 1.8 gives the better exponent. |

All the run's statements and proofs enter unchanged in substance. Proofs were rewritten in my words, with the steps I
checked made explicit: the sign of the archimedean terms, the −L'/L(0) formula, the descent of endomorphisms.

# SA28: Autour de La Longue Marche, part 1 (cotes 142, 143, 141): topic notes, horizontal sweep 1

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026.
- **Inputs:** `horizontal/inputs/SA28/`.
- **The notes:** Pro's, by GPT-6 Astra (ChatGPT Pro mode), first pass.
- **The second pass:** by Claude Opus 5.5 at effort max (13 Nov for cote 142; 17 Nov for 143 and 141). It checked
  every first-pass note against the scans and the corrected transcription.
- **There are no Work math notes for this topic.**

## What the notes cover

Three packages, 481 entries:

| Package | Entries | Pages |
|---|---:|---|
| MPL_142_001-093 | 310 | 142/003–093 |
| MPL_142_094-122 | 96 | 142/094–122 |
| MPL_143+141 | 75 | 143/001–034, then 141/001–016 |

They fall into 30 items and 2 singletons.

**Cote 142, "Action de Galois sur Teichmüller", in order:**

| Scans | What the pages do | Item |
|---|---|---|
| 003–008 | finite étale maps of surfaces, and finite-order mapping classes | SA28-1 |
| 009–014 | the profinitely completed isotopy category | SA28-2 |
| 015–021 | the base field, and filling and forgetting | SA28-3, SA28-4 |
| 024–042 | the four-point groupoid with poles: presentations, and the equations on (λ, β) that reduce to one equation | SA28-5, SA28-6 |
| 044–064 | the real blow-up of a marked triple, PGL₂(Z), pinnings, boundary pinnings | SA28-7, SA28-8 |
| 067–093 | the arithmetic groupoid with rational base points: path torsors, cocycles f and g, Kummer coordinates, faithfulness, Belyi maps, liftability | SA28-9 to SA28-12 |
| 094–107 | the recognition problem, his "conditions draconiennes" | SA28-13 |
| 102–107 | horizontal paths | SA28-14 |
| 108–114 | the Klein-four and tetrahedral configurations | SA28-15 |
| 115–122 | presentations by boundary arcs | SA28-16 |

**Cote 143, "Paradigmes des courbes algébriques":**
- the anabelian programme over a base (SA28-17);
- the structured object (X, D, J), with filling and drilling (SA28-18);
- the moduli of curves with few points and the Galois action on Teichmüller groups (SA28-19).

**Cote 141, "Théorie de Kummer" and the note:**
- Kummer theory (SA28-21);
- classifying spaces (SA28-22);
- modular groups (SA28-23);
- bitorsors (SA28-24);
- the polygon group (SA28-25).

**Heavy and light:**
- The heaviest items are SA28-9 (68 entries), SA28-6 (40), SA28-13 (36), SA28-7 (32) and SA28-12 (32).
- The light ones are the cote-141 algebra (3–5 entries each) and the dating apparatus (SA28-26).

## Counts

| | |
|---|---|
| Entries | 481 (Pro); no Work units |
| Items | 32: 30 clustered, 2 singletons |
| Basis | 475 index-row, 1 entry-read, 5 passage-read |
| Fidelity of my passage reads | 5 agree |
| Second pass | about 360 first-pass notes verdicted. In 142/001–093: ~16 corrected, 3 kept with a qualification, the rest kept. In 142/094–122: 13 corrected. In 143+141: ~16 corrected. None dropped. Recorded in `CHECK_EVENTS.tsv` under the second pass's name |
| Flags | 12: 5 the note overstates or misreads, 3 links across folders, 2 suspected misreadings, 2 lens |
| Check events | 364: 6 mine, the rest the second pass's verdicts |

## The flags that matter

1. **142/008, his NB.** "Tout sous-groupe fini de T_X peut s'obtenir de cette façon comme stabilisateur !! (th. profond et
   récent…)".
   - The stabilizer of f is the deck group of the étale cover f defines.
   - In genus 2 a finite étale map to a hyperbolic surface has degree 1 (Riemann–Hurwitz), so as written the NB is
     false for étale arrows (note N008.3; I checked it).
   - It is true for stabilizers of complex structures: the realization theorem it cites, presumably Kerckhoff's (1983).
     That also dates the sheet to the early 1980s; this is my inference.
2. **142/113.** P_i^{ω,ζ} = −P_{ω²i}^{ω,ζ} cannot hold with nonzero values around a three-cycle: iterating gives
   P_i = c³P_i. The minus sign is very likely a cube root of unity misread or miswritten (note B16; computation
   checked). For the scans.
3. **142/025–027 against 037.** σ_∞(λ) appears as l₁^{−γ} under the brace, but with a positive exponent later (N025.4).
   The page agrees with the note; the convention σ_∞(l₀) = l₁ was not located. For the scans.
4. **First-pass notes that rested on a misreading, now corrected by the second pass:**
   - N024.2: the conflict came from reading l₀l₁l_∞ for l_∞l₁l₀.
   - N051.2: a misread (24).
   - 141 N61: only λ₀λ₁λ₂λ₃ = 1 is struck.
   - 143 N25, N27: "car grps connexes" is a misreading.
   Sweep 2 should use the second-pass readings.
5. **The five-point question.** 143/028–033 has the configuration-space description of T_{0,ν} and the braid group, but
   no pentagon or order-five equation (N28; agrees). The notes point to cotes 146, 147 and 148 for it.
6. **The LM lens.**
   - 449 of 481 notes compare with La Longue Marche (the LM_140 files).
   - In 143+141, 50 notes also cite research-run ids, and N40–N42 are about LM §32 rather than 143's page.
   - The comparisons sit in separate "Context" paragraphs, so the page readings mostly stand on their own.

## Objects that cross into other topics

- the four-point groupoid equations, the GT-type equations (SA28-6): to SA31 (149) and SA29 (148);
- tangential base points and boundary pinnings (SA28-7, SA28-8): to SA30 (147, structure at infinity);
- the recognition conjecture (SA28-13): to SA31 (149) and to LM_140-2 scans 23–24;
- the five-point question: to SA29 and SA30 (146–148);
- the platonic configurations (SA28-15): to SA30 (146, 147);
- Kummer theory and inertia (SA28-21): to SA31 (149).

## What sweep 2 should look at first

1. The genus-2 objection to the NB on 142/008, and which reading of "de cette façon" his text intends.
2. The two sign questions, 142/113 and 142/025–037, on the scans.
3. SA28-6, the one-equation locus, against the GT-type equations of SA31 (cote 149). It is the same object, reached
   earlier.
4. SA28-13, his recognition conjecture, in its own terms: its precise hypotheses (condition a) without b), the
   peripheral condition, G_m as the counterexample), before any comparison.

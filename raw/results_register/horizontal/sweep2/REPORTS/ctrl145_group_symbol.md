# CTRL-145 and CTRL-145_2: the group on 145/023–033 is a script E

Piece of horizontal sweep 2, part 2. Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. Topic SA29, item
SA29-20 ("Printemps 81, second part"); the control-run rows are filed in `SA28/PLACEMENT.tsv`.

## Where it is

| What | Location |
|---|---|
| His pages | Cote 145, scans 020–034, in `grothendieck_archive_montpellier/18_autour_de_la_longue_marche_a_travers_la_theorie_de/145.pdf`. |
| Pro's notes | Package MPL_145, notes #25–#56 (item SA29-20), by GPT-6 Astra in ChatGPT Pro mode. |
| Control run CTRL-145 | `grothendieck_archive_transcription_20261110/codex_web_20261113/returns_control/CTRL-145/out/`: mathnotes `work:CTRL-145#1-6`, sheet notes `codex:CTRL-145#1-2`. |
| Control run CTRL-145_2 | `…/returns_control/CTRL-145_2/out/`: `work:CTRL-145_2#1-6`, `codex:CTRL-145_2#1-2`. |

The pages develop the cartographic group and its completion: the generators σ_i, ρ, the loops l_i, the square roots
ε_i, and the involutions τ_i. They go on to Malgoire's "triangulé pondéré" cartographic group, the multiplier p and the
conjugators g_i, partial splittings from fixed points, a presentation by ρ, σ₀, τ₀, and the five-entry tuples
(p, σ, g₀, g₁, g_∞) of the enlarged group.

## The difference

- **CTRL-145 and Pro** read a script E:
  - "Le sous-groupe ℰ_τ de ℰ image inverse de Z/2 engendré par τ, est le groupe cartographique 'triangulé pondéré' de
    Malgoire" (023; Pro's transcription line 920);
  - "description de ℰ tt entier" (029);
  - "② Le groupe Sℰ̂̂" (033).
- **CTRL-145_2** reads Σ throughout: Σ_τ, "description de Σ tt entier", SΣ̂̂.

## Decided on the scan images

The images are `img/145_023_sym3.png` (145.pdf p. 23, first line) and `img/145_033_top.png` (p. 33, the heading).
- The symbol is a rounded capital shaped like an epsilon: a script E.
- A Σ would have a straight top bar, a straight bottom bar and a sharp vertex.

So CTRL-145_2 misreads. CTRL-145 and Pro agree with the page.

## What the two runs agree on

- **His slips, proposed by both runs:**
  - Γ₂ for Γ_{1/2} after the fixed point 1/2 (028);
  - the right tuple of (9′) beginning (p, σ, …) for (p, 1, …) (034).
- **The open question** "j'ignore si cette inclusion est une égalité" (024).
- **The negative answer** "on trouve comme tantôt que non" (022).
- **The pointer** to Malgoire.
- **The computational objection** on 033–034: u(g′_i) needs word descriptions of the inputs.

## What depends on it

- The group ℰ and its completions ℰ̂̂ and Sℰ̂̂ carry all of SA29-20.
  - ℰ_τ is Malgoire's cartographic group.
  - The tuples of 033–034 are elements of Sℰ̂̂.
- The prompted question SA29-Q2 (what each Γ or 𝒯 on these pages denotes) concerns the same family of symbols.
  - On 148/020 the second pass found 𝒯 where Pro had Γ (sweep 1).

## Correction

| Correction | Recorded in |
|---|---|
| CTRL-145_2's Σ is corrected to ℰ | `SA28/CORRECTIONS.tsv` |
| The slips proposed by both runs, listed as proposals | `SA28/CORRECTIONS.tsv` |
| The readings decided on the images | `SA28/CHECK_EVENTS.tsv` and `SA29/CHECK_EVENTS.tsv` |

**For part 3:** Work's ink check of SA29-20 uses ℰ.

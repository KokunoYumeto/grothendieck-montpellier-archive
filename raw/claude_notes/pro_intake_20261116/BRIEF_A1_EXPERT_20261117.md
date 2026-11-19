# Brief: first check of ANABELIAN_SUCCESSOR's A1 (17 Nov 2026, ~00:1x UTC)

To: ab3f12f24d7009736, Claude Fable 5.2 at effort max: a copy of the Longue Marche field expert a125034f, rolled back to
the end of its turn of 14 Nov 04:16 UTC (834k context). The original is untouched. Since then, the main session's
records exist as files (you need none of them for this task).

## Why you, and the user's words

The user, 16 Nov 23:56-23:57 UTC: [the user's words, omitted]; [the user's words, omitted] It has not been asked: the claim was filed and noted (my NOTES section 39; queued as F18 in
claude_math_notes/FOR_FABLE.md), and nobody has checked it. The user's standing rule (16 Nov 23:40 UTC): no separate
referee decision; whoever uses an important result double-checks it while using it, and the check goes into the next
prompt that uses it.

## The claim

The return ANABELIAN_SUCCESSOR (GPT-6 Astra, ChatGPT Pro mode; final of 16 Nov 12:43 UTC), folder
`<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_SUCCESSOR_final_20261116T1243Z_unzipped\`:

- **A.3 = AR.3 (Proved, per the run):** every smooth proper geometrically connected curve of genus >= 2 over every finite
  field has an injective geometrically prime-to-p point-section map. Conjugation is by the whole geometric prime-to-p
  group, and the arithmetic quotient is the whole G_k. The claim covers characteristics 2 and 3 and every finite constant
  extension.
- **A.98 = AR.9:** universal A1 is equivalent to the emptiness of every Saidi-Tamagawa exceptional set E_C for
  Sigma = {l != p}; A.97 = AR.8 is their statement (2009 Def. 1.10 and Cor. 1.11; 2017 Props. 2.11-2.12).
- **The question it answers:** cote 149, scans 35-36: "Il se pourrait qu'on puisse en deduire P = Q".

## What to read (only these; about 60-70k tokens)

1. `sections/A_foundations.tex` lines 1-186 (AR.1-AR.3; the AR.3 proof is lines 140-186).
2. `sections/A_structure.tex` lines 1-140 (AR.8, AR.9).
3. `agent_geometric/geometric_section.tex`:
   - lines 3280-3900: AG.39, "the full prime-to-p configuration fiber does not inject", even for complex curves;
   - lines 3901-4203: AG.40, the conditional cuspidal separation criterion; lines 4180-4197 are the run's paragraph on
     the literature (Saidi-Tamagawa Cor. 2.3 / Thm 2.7; the "full configuration-fiber assertion in the cited Mochizuki
     author versions": Absolute Anabelian Cuspidalizations of Proper Hyperbolic Curves, 2007, and its 2014 Comments);
   - lines 4204-4494: AG.41, fixed-prime cuspidal configuration exactness;
   - lines 4495-4687: AG.42, diagonal boundary and cuspidal transport.
4. The run's own audits in `agent_criteria/`: `fixed_prime_cuspidal_independent_audit.md`, `FF49_independent_audit.md`
   and `A1_downstream_scope_assessment.md`.

## The task: a first check, the whole of it

1. **Is the chain sound as read?** Follow AR.3 through AG.40-AG.42 and name the decisive step of each. Points to check:
   - **AG.41.** Keep the whole proper geometric prime-to-p quotient and replace only the cuspidal kernel by its maximal
     pro-r quotient. Is the pro-r cuspidal kernel then really injected, i.e. exact on the left?
     - The relevant action: the proper prime-to-p group acting on that kernel's pro-r quotients. Its finite images need
       not be r-groups.
     - So what does the argument use in place of unipotence? The run cites Kochloukova-Zalesskii 2011.
     - Does the arithmetic comparison (retaining G_k, and identifying each punctured-curve group with the inverse image
       of its point section) hold as stated?
   - **AG.42.** Does a geometric conjugator between s_P(G_k) and s_Q(G_k) lift to the diagonal boundary group, as needed?
     Is the puncture decomposition group exactly the intersection with that group?
   - **AG.40.** An isomorphism of the maximal cuspidally pro-r groups of C-P and C-Q satisfies two conditions: it lies
     over the identity of the full proper arithmetic quotient, and it carries the cusp decomposition group to a
     conjugate. Does such an isomorphism force P = Q?
     - The route: the zeta functions of the finite covers seen in the quotient, then a Kummer evaluation of a function
       with divisor p^e(P - Q).
     - Is the inverse-limit recognition of non-cuspidal point sections complete? Or is a finite-level test silently
       substituted for whole-group conjugacy?
2. **AG.39 and the literature, from what you know (read no literature):**
   - Is AG.39 plausible, and by what mechanism? My guess for you to confirm or correct: the point-pushing action on
     non-nilpotent prime-to-p quotients of the fiber group has images whose orders involve other primes, so the
     prime-to-p completion of the fiber does not inject.
   - Which published statement asserts full pro-Sigma configuration exactness for this Sigma, and does any published
     proof rest on it?
   - What would that mean for the papers that use it?

   I search the literature myself (E_C after 2017; the Mochizuki statement and its 2014 comments) and add what I find to
   your file as a separate section.
3. **If A1 holds, what follows** for the Longue Marche programme, the companion's wording on points as sections over
   finite fields, the SECTIONS_OVER_Q / LM6 line, and the ANABELIAN successor's open items (A3, A10(c); scope in
   `A1_downstream_scope_assessment.md`)?
4. **The check that goes into the next prompt.** Write the items a Pro run should check while it uses A1: each doubtful
   step, with file and line, stated as a task to prove or refute. Also name which unsent prompt it belongs in. If none
   fits, say that, and the items go into the next consolidated successor (one prompt per cluster: the user,
   16 Nov 23:34 UTC).
5. **Outreach.** If you find a gap in a published proof (as on 16 Nov with Boggi and Boggi-Zalesskii), say so with the
   exact place, so that I can draft a note to the authors. No one is written to before the step is checked in the
   source.

## Bounds and rules

- Stop by about 930k of context. Read only the files above. No sub-agents. No Grep or Glob over Documents or any other
  big tree: name the exact files.
- Do not stop for context; if your context starts with a summary you were compacted: reread this brief and your file,
  then go on.
- Record the check with who, how, model, effort and date: "Claude Fable 5.2 at effort max (copy ab3f12f2 of the
  Longue Marche expert), reading the proofs, 17 Nov 2026".

## Output

Write `<local>/Documents\pro_intake_20261116\EXPERT_A1_ANABELIAN_20261117.md`, in this order:

1. the verdict (sound as read / gap at step X / wrong at step X);
2. the steps checked, with lines;
3. the doubtful steps;
4. AG.39 and the literature, from your knowledge;
5. the implications;
6. the items for the next prompt;
7. any outreach point.

Then reply to me in at most ten lines.

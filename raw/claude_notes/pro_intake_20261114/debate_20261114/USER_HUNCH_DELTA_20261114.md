# The user's hunch on Delta (14 Nov 2026), for the consolidation

**The user (P5051), verbatim:** [the user's words, omitted]

**In precise form (main session, Claude Opus 5.5 at effort max; my reading of our files, checked by no one):** Delta, the extra CM bit of LM7_PUSH E.3, lives in the frame group (Z/12)^x / {+-1} = {1,5,7,11} / {+-1} (the dictionary's M1; the Longue Marche expert's 'sign of an idempotent of Z/12 = Z/3 x Z/4'). By the Chinese remainder theorem (Z/12)^x = (Z/3)^x x (Z/4)^x: a sign at 3 (the CM point j = 0, automorphisms mu_6) and a sign at 4 (the CM point j = 1728, automorphisms mu_4); modulo the overall sign only their ratio remains. Frames 1, 11: the two signs agree, Delta = 0; frames 5, 7: they differ, Delta = 1. So Delta = 0 exactly when the two CM signs cancel. E.2: the gentle part of GT-hat_0 reaches the frame 5 (no cancellation there). E.3 asks whether the full GT-hat (with the pentagon) forces the cancellation.

**Item for GPT-6 Astra (ChatGPT Pro mode), to be placed by the intake:** prove or refute that for every element of GT-hat the signs of its frame at the two CM points agree (Delta = 0 on GT-hat); in either case find the mechanism: which relation (pentagon, hexagons, the 2-cycle and 3-cycle relations) makes the two signs cancel, or the element of GT-hat for which they do not.

## The user's sharpening (verbatim)

- **P5052:** "You might, so notice how there is a local to global obstruction that is assigned. My hunch is that delta is literally the canceling of that sign. So there's a local to global obstruction, that's a plus minus or something. That thing is just the thing that cancels it. That's it. That's all it is."

- **P5053:** "Now, note that I'm sort of like distinguishing that from it can be zero, but it can be plus minus zero, and it is whichever one of those two is needed to cancel. So it has more information but it isn't non-zero, if that makes sense. It's like it's a sign idempotent or a directionality. I'm sure there's a precise term there. Actually, I'm pretty sure in the sign idempotent might be a precise term."

- **P5054:** "The concept I'm articulating is it's not a number. It's not -1 or -2. It's minus. It's whatever the sign is that cancels the other sign. And it's literally just the sign. That's why it's weird."

## Precise candidates for the user's notion (main session, Claude Opus 5.5 at effort max; to be worked out, not results)

- Not a number but a choice of sign: an element of a mu_2-torsor (an orientation). 'Zero, but +0 or -0' is a trivialization: the data of why an obstruction vanishes (a cochain whose coboundary is the obstruction cocycle, a null-homotopy) carries more information than the bare fact, and the choices form a torsor.
- Oriented points: the boundary of an interval is +b and -a, two signs that cancel; the total is zero, the signs are information.
- Sign idempotents: e_+ = (1 + s)/2 and e_- = (1 - s)/2 in Z[1/2][C_2] are the standard projections onto the sign eigenspaces; the idempotents 4 and 9 of Z/12 split Z/12 = Z/3 x Z/4 (the Longue Marche expert's 'sign of an idempotent').
- Reciprocity: in Hilbert's product formula the local signs (a,b)_v multiply to 1 over all places, so the sign at the last place is the one that cancels the others. On the tripod the three special points are j = 0 (sign at 3), j = 1728 (sign at 4) and the cusp: the user's hunch would make Delta the cancelling sign at the cusp, a reciprocity law on the tripod. Item: prove or refute such a product formula for the frame's local signs and identify Delta with the cusp term (compare the reciprocity condition of ANABELIAN D.27/D.28 and the dictionary's M4).

- The user, later: the sign anomaly 'could equally be phase anomaly. It's just whatever thing fixes.' So the cancelling object may be a phase (mu_n or U(1)), not only a sign; for the item: allow the frame's obstruction to take values in a phase group, the sign being its case n = 2.
- The user, then: 'Or a stack of phases.' One degree up: a gerbe (Giraud), obstruction in H² or H³(-, U(1)); for the item: allow Delta to be the shadow of a gerbe obstruction whose trivializations are the cancelling data.

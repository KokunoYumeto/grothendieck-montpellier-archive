# For the next version of hexagon:2611.00940 (H17, WB-0007): small accessibility edits, prepared 25 Nov 2026

Main session 329fb1e6 (Claude Opus 5.5 at effort max). Not applied: version 2 (API versionId 2611.00940v2, committed
24 Nov 23:27 UTC) is in screening, and the API refuses a pause for a version of an already published record (HTTP
409, 25 Nov 01:19 UTC: "Only the latest never-published submission can be corrected"). The user, 25 Nov ~01:2x UTC:
"no rush either way ... for something this benign, it's not necessary to change it at all if that would be pedantic."
So these go into the next version made for a substantive reason (for instance with the optional Boggi-Funar sentence),
and do not justify a version of their own.

## Abstract, first sentence (name the relations once; the title keeps the numbers)

Now: "Nakamura and Schneps (2000) defined a subgroup $\mathrm{I}\Gamma$ of the profinite Grothendieck--Teichm\"uller
group $\GT$ by two relations, $(\mathrm{III}')$ and $(\mathrm{IV})$, that hold for Galois elements; they proved that it
acts on the profinite mapping class groups of all surfaces, and left open whether it is all of $\GT$."

Proposed: "Nakamura and Schneps (2000) defined a subgroup $\mathrm{I}\Gamma$ of the profinite Grothendieck--Teichm\"uller
group $\GT$ by two further relations that hold for Galois elements, the images of the absolute Galois group of
$\mathbf Q$: $(\mathrm{III}')$, a relation in the profinite braid group on five strands that implies the pentagon
relation, and $(\mathrm{IV})$, a relation of Nakamura in the profinite braid group on three strands. They come from
asking that an element act, as Galois elements do, on the profinite mapping class groups of all surfaces in a
consistent way; Nakamura and Schneps proved that $\mathrm{I}\Gamma$ acts so, and left open whether it is all of $\GT$."

Source of the descriptions: Furusho, RIMS Kokyuroku 1267 (2002), pp. 191-192 (Definition 2.1: (III') in B-hat_5, (IV)
in B-hat_3; "Note that (III') implies (III). These two relations, (III') and (IV), describe the condition for elements
of GT to act (as G_Q does) on all types of pro-finite Teichmüller modular groups in a certain consistent way"), read on
the page image by the main session on 25 Nov; and the note's own statements (section 1 and the proof overview).
Nakamura-Schneps 2000 itself was opened by the second reader of version 2 at Theorem 1.1, Definition 1.1 and Theorems
1.3-1.4; check the wording against it once more before use.

## Abstract, two glosses

- "the normalized elements of $\GT$" -> "the normalized elements of $\GT$ (those with $\lambda=1$ and $\rho_2=0$, where
  $\rho_2$ extends to $\GT$ the Kummer cocycle of the roots of $2$)".
- "Galois elements" is glossed by the first sentence above.

Apply the same change to ABSTRACT (make_abstract.py) and to the metadata; rebuild; read page 1.

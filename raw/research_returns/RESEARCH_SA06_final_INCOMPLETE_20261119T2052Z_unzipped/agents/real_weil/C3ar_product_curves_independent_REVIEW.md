# Independent review of C.3ar

Reviewer: /root/real_weil, 19 November 2026.
Full typed source read: ../cycles/product_curve_top_quotient.tex.
Outcome: **PASS in the stated product-of-curves, rational-coefficient scope**.

The proof does not assert algebraization of arbitrary formal K0 classes.
Its actual line bundles are constructed by formal existence for Pic,
the exact Elkik puncture comparison, Cartier extension to the regular
resolution, and an exceptional-divisor twist. The single exceptional
divisor is precisely what makes the last adjustment sufficient. This
argument applies to each chosen logarithmic parameter.

The relative weight-d calculation has only the cohomological diagonal
H^d(K_d^(d)); lower sheaf degrees vanish and cohomological degrees above
d vanish. The positive internal-degree horizontal representatives glue
as the asserted twisted differential sheaves. The Qbar model gives the
absolute differential splitting. KAN removes every term with a positive
relative differential degree, leaving H^d(L^j) tensor the constant
absolute (d-1)-forms. No complex-vector-space structure on Chow is inferred.

The leading cup product is correctly normalized by the actual Milnor
symbol with first entry 1+t^j a. The cyclic logarithmic representative
has differential equal to its dlog class; the Euler contraction in
positive degree gives uniqueness. BEK's comparison is only pro-level.
A clarifying sentence was suggested: one may check each leading degree
after restriction from a higher compatible Pic-product stage. The separate
fixed-level weight-d calculation is the Loday/CHW input, not a strengthened
version of BEK. This is a clarification, not a newly found gap.

For each transcendental b, a reduced fibre of a Qbar-defined map of degree
greater than 2g-2 gives enough evaluations of holomorphic forms. A form
annihilated at all these points would have too many zeros. The finite
complex coefficients in this spanning argument are absorbed into the
actual parameter a of the Picard deformation. The argument never multiplies
a Chow class by an arbitrary complex scalar. Multiplication by the chosen
nonzero section surjects on H^1 by the dual injectivity on H^0. Kunneth then
gives every required tensor coefficient.

Each resulting product is an actual ordinary algebraically trivial cycle:
hold its constructed line bundle and the other factors fixed, and vary
one point divisor on its proper curve. Earlier internal degrees stay zero.
The finite detecting thickening therefore allows finitely many eliminations.
The final use of K0 injectivity is on an actual class, not a formal object.
Restriction and pullback identify the remaining ordinary quotient with
the degree quotient of CH0(V), and an ample-degree exceptional curve kills
that one-dimensional rational quotient on the puncture.

## Primary-source inspection

Reused the fully audited C.3ad inputs, including Loday's exact highest
Hodge summand and the CHW relative Adams/Chern comparison; no claim of
a new independent opening of their entire sources in this particular check.

Freshly opened both complete primary versions of Bloch--Esnault--Kerz:

- Author PDF: https://page.mi.fu-berlin.de/esnault/preprints/helene/112-bek.pdf
- Published PDF: https://content.algebraicgeometry.nl/2014-3/2014-3-015.pdf

Read Lemma 2.2 and Proposition 2.3, author pages3–4, and the full
Proposition 6.1 proof, author pages12–13. The latter explicitly retains
the pro-system and states the dlog normalization. It does not supply
an arbitrary finite-thickening algebraization theorem. The restricted
conclusion in C.3ar correctly leaves the unrestricted complex top quotient
and integral finiteness unresolved.

# Independent audit of finite duality on a nonseparated arithmetic scheme

19 November 2026. We read the integrated
`prop:B-finite-duality-nonsep` in `sections/part_b.tex`. The proof
passes for the explicitly declared compact-support convention.

Let X be regular, finite type over Z, of pure absolute dimension d,
and F a bounded constructible Z/m complex. A finite affine open
cover has quasicompact separated finite-type intersections U_I:
each is an open in an affine member and X is noetherian. Thus
ordinary compact support and Geisser--Schmidt finite duality apply
to every nonempty U_I.

The alternating chain complex of j_{I!}(F|U_I), in degree
-(|I|-1), augments quasi-isomorphically to F. At each geometric
point this is the augmented simplex complex on the finite nonempty
set of covering members containing that point. The argument
applies termwise to a bounded complex. Since the cycle complex
restricts to the cycle complex on an open, derived adjunction
identifies its dual complex with the finite Čech cochain complex
of RHom_{U_I,Z/m}(F,D_{U_I}). The chain/cochain signs and degrees
therefore have the required reversal.

Geisser--Schmidt's Theorem3.5 is a natural derived duality, not
merely an equality of group orders. Its Corollary3.6 gives the
real Tate version. Lemma3.7 supplies the coefficient shift, and
Theorem4.6 is proved by this natural identification and the
arithmetic base trace. We read all these statements and the
complete proof of Theorem4.6 in the opened author PDF. Their
naturality is exactly what permits termwise duality to commute
with open extension by zero in the finite total complex.

For cover independence, apply ordinary compact-support
Mayer--Vietoris on every separated intersection to its finite
intersection refinement. The resulting finite double Čech
complex identifies the two totalizations. No nonseparated
compactification is involved. One may use arbitrary finite
separated-open covers during this proof, since the same formula
and Mayer--Vietoris argument apply to them; affine covers form
a sufficient initial class. Refining three covers at once gives
the cocycle compatibility of the identifications.

Use functorial complex models or a derived enhancement to make
these totalizations and comparison maps canonical. This point
was explicitly sent to the author of Part B: GS Section2 itself
uses Godement models to avoid choosing nonfunctorial cones in
the bare derived category. It is a formulation refinement, not
a gap in the intended derived construction.

Finite horizontal totalizations commute with the real-place
modification, including its unbounded Tate directions. Every
cohomological degree remains an extension of finitely many
finite groups. Since Hom(-,Q/Z) is exact, termwise derived
duality yields the perfect pairing with total shift 2d+1.

The conclusion is limited to the specified descent definition
of compact support. It does not assert the existence of a
proper compactification of X or identify an unspecified other
nonseparated support functor. No requirement that m be prime
to all residue characteristics has been introduced: the
geometric special-fibre primary coefficient terms are handled
by the étale motivic cycle complex as in the preceding theorem.

Primary source: Geisser--Schmidt, Poitou--Tate duality for
arithmetic schemes, author PDF
https://www.mathi.uni-heidelberg.de/~schmidt/papers/poitou-highdim.pdf,
Theorem3.5 pp7--8, Corollary3.6 p7, Lemma3.7 p8 and Theorem4.6
p11; Section2 pp3--5. Browser ref turn211116192view0; local
opened text `primary_sources/part_b/geisser_schmidt2018.txt`.

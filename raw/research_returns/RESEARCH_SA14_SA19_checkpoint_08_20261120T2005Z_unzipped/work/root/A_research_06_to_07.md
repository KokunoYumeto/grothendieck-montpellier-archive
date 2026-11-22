# Main-question work after checkpoint 06

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited and not exposed. These are research notes, not unqualified theorem claims.

## Searches and scope checks, 20 November 2026, 18:38–18:48 UTC

We searched primary-source-oriented combinations of Picard/Lefschetz/p-torsion/smooth hyperplane, logarithmic differential/ample zero divisor, nonnormal mu-p/Godeaux, Albanese/hyperplane/inseparability, smooth extension/Veronese/positive characteristic, and geometrically nonnormal regular surfaces/conductor/ampleness. Sources that repeated known vanishing hypotheses or only treated rational Neron–Severi groups did not settle A1 or A2. Unverified AI-generated search results were not used as mathematical sources.

Opened Fanelli–Schroer, *The maximal unipotent finite quotient, unusual torsion in Fano threefolds, and exceptional Enriques surfaces*, published PDF https://epiga.episciences.org/6718/pdf, introduction pp.2–4 and Theorem7.3 p.25. Its torsion examples are integral denormalized Fano threefolds; the construction is not smooth and can fail Cohen–Macaulayness. Thus they do not meet Part A's smoothness hypothesis. Their normalization/conductor construction remains a possible source of ideas, not a counterexample here.

Opened Bernasconi–Martin, *Bounding geometrically integral del Pezzo surfaces*, arXiv:2306.07000v2 (7 October 2024), introduction and Proposition4.11 pp.17–18. The irregular regular examples in that proposition require imperfection degree at least2; a function field of a curve over the algebraically closed ground field has imperfection degree1. Therefore that particular irregular-del-Pezzo route cannot supply the generic fibre of the desired smooth threefold over a curve. This does not exclude all non-smooth generic fibres or all other constructions.

## A proposed obstruction to complete-intersection quotient constructions

Let P be a smooth scheme with a free mu-p action and smooth quotient Q, and suppose a smooth projective D in Q has a section of P over D. Its lift Dtilde embeds in P. The tangent sequence for a smooth mu-p torsor has trivial one-dimensional kernel and cokernel. If its induced normal sequence is exact as expected, it reads

0 -> O_D -> N_(Dtilde/P) -> N_(D/Q) -> O_D -> 0.

If D were an ample Cartier divisor in smooth X contained in Q, the final quotient would vanish on the ample line N_(D/X), so it would factor through N_(X/Q)|D. This is impossible when the latter is a sum of ample line bundles. This argument was sent to DGJ for an independent exact-sequence and global-trivialization check. It only excludes the indicated complete-intersection construction, not arbitrary smooth X.

## Further construction analysis (not promoted)

A purely inseparable smooth multisection D of a smooth ruled surface over a curve C has T_D equal to the relative tangent line; its normal line is the pullback of T_C. If C has positive genus, this prevents ampleness. In higher dimensions a divisor annihilating a base differential requires either a geometrically non-smooth generic fibre or a more complicated Albanese image; products do not repair ampleness.

For a hypersurface family over a curve defined by pth-power fibre coordinates, the base derivative must be nowhere zero along the geometric singular divisor to keep the total space smooth. In a positive projective hypersurface model of relative dimension at least2, that derivative is a section of a positive line bundle on a positive-dimensional proper locus and has zeros. This is a failure of that specific model, not a theorem excluding all fibrations. Regular non-smooth generic fibres must not be silently treated as smooth.

## A separate observation passed to the fundamental-group work

Under a finite etale cover X_d -> X of the fixed SNC resolution, let C'_a -> C_i have degree d_a. The intersection matrix B' applied to the pulled-back vector t gives d_a(Bt)_i. Also 2g(C'_a)-2+nu'_a=d_a(2g(C_i)-2+nu_i), so the same componentwise vector t solves the refined-Swan inequalities of F10. The p-power exponent bound is therefore unchanged by these unramified covers. The total number of components, genera and crossings grows at most linearly with d. This does not by itself bound the resolution complexity after a further wild cyclic cover, and does not yet settle the remaining coefficient-prime-not-p case of derived length3.

## Veronese cone smoothing, 18:54–18:56 UTC

We tested whether a smooth deformation of a projective cone over (P3,O(p)) could retain that divisor at infinity, thereby producing the p-divisibility needed for an A1 cokernel. The vertex is the scalar mu-p quotient of affine4. Opened Liedtke–Martin–Matsumoto, *Linearly Reductive Quotient Singularities*, arXiv2102.01067v3 (17 September2025), Convention9.1 and Proposition9.2 pp.37–38, Theorem10.8 and Corollary10.9 p.43. Their dimension-at-least4 infinitesimal rigidity applies to this isolated quotient; the scalar action is free away from the origin and mu-p is linearly reductive. Thus this equicharacteristic smoothing route fails. The three-dimensional infinitesimal exceptions are also rigid over reduced DVRs; a nonzero tangent deformation is not a smoothing. A possible cone route would have to start outside the linearly reductive quotient class.

We also examined a characteristic-two Frobenius incidence model over P1 x P1. Its contraction is the smooth quadric z^2+u0*u1+v0*v1=0 in P4. The resolved model is obtained by the corresponding incidence blowups; its evident Picard generators do not produce an index-two cokernel. This was a geometric exploratory calculation, not a promoted counterexample.

## Exact-scope checks after review03

Opened Li--Shentu, Strong stability of cotangent bundles of cyclic covers,
C.R. Acad. Sci. Paris352(2014), 639--644, Lemma2.1 p640. Its recalled
Grothendieck--Lefschetz theorem explicitly assumes negative H1 and H2
vanishing. The introductory phrase arbitrary characteristic does not
remove those hypotheses.

Downloaded and read Fujita, On the hyperplane section principle of
Lefschetz, J. Math. Soc. Japan32(1980), beginning pp153--157. Its notation
'/C' explicitly means the complex field. Corollary2.6 p156 is labelled
'/C'; its injectivity conclusion is therefore not a characteristic-p
theorem. The arbitrary-characteristic Corollary2.5 immediately above it
retains all negative-H1 vanishings. The source's introductory paragraph
also emphasizes the positive-characteristic limitation. The tempting
search snippet omitted '/C'.

Opened Brevik--Nollet, Noether--Lefschetz theory and surfaces containing
a multiple curve, Cambridge journal HTML published19 October2026,
Theorem1.1 and the surrounding introduction. The ambient threefold is
over C. Its general statement about restriction injectivity in that
discussion is in this fixed characteristic-zero scope, not a solution
to A2.

The proposed codimension-purity argument for the vanishing locus of a
torsion section fails even for abelian-scheme Picard targets. The full
explicit finite-flat and elliptic-family counterexamples and finite
checks are in work/bce/A2_group_purity_counterexample.md/.tex and
work/bce/code/check_group_purity.py. They do not realize the hyperplane family of
one fixed smooth ambient variety, so main A2 remains undecided.

# P-F45: range of the full cyclic-cubic-cover eigenspace domain

Author/checker: `/root/bridges`, GPT-6 Astra Pro, inherited/undisclosed effort.

The full proof is in `positivity_cyclic_cover_range.tex`. This is a narrowly scoped range result for the actual family underlying the cubic-surface and cubic-threefold ball constructions. For n>=4, the full deck-character Hodge classifying domain is a ball exactly at n=4,5. The eigenspace formula is `h^(n-1-p,p)_zeta=binom(n,3p+2-n)`. At n6 the signature is (15,6), with matrix domain of dimension90. For n>=7 three consecutive Hodge pieces produce an explicit compact holomorphic P1 in the full flag domain.

This does not rule out horizontal period images in smaller domains, special subfamilies, sub-Hodge structures, half twists, different covers, or alternative theta constructions. The fixed n5 theta/discriminant identification P-F41 is unaffected. The point is to delimit the exact full-eigenspace construction already used, not to create a general no-go assertion.

## Primary premises actually read

- Van Geemen–Izadi, *Half twists and the cohomology of hypersurfaces*, Math.Z.242 (2002), pp279–301, Section2.1 pp283–284 and Lemma2.4 p285. Primary author PDF: https://mathweb.ucsd.edu/~eizadi/papers/MathZ2002.pdf. Refs `turn539017407view0`, earlier `turn409544334view1/2/3`, `turn980060013view0`. The actual formula and proof on p285 were visually read at `theta_sources/van_geemen_izadi_7.png`. Its k=n-1,d=3,i=1 substitution gives exactly the degree3p+2-n; i2 gives3p+1-n. The residue volume's deck character is included.
- Griffiths, *Periods of integrals on algebraic manifolds: Summary of main results and discussion of open problems*, Bull.AMS76 (1970), pp228–296. Section2 pp234–235 describes the full domain and compact flag fibers; equation9.9 p254 gives `(-i)^d(-1)^r Q(v,conj(v))>0` for Hodge type(r,d-r). Primary IAS PDF: https://publications.ias.edu/sites/default/files/periodsofintegral.pdf. Refs `turn539017407view1`, earlier `turn829673669view2`, `turn991756948view2`. The sign equation was visually read in `theta_sources/griffiths_summary_27.png`; extracted text alone had garbled the exponent.

## Whole-proof self-check

I read the entire written proof and reconstructed the Jacobian coefficient formula, eigenspace convention, Hermitian polarization normalization h=i^d Q, all five displayed signatures, and the domain argument. The n6 nonball assertion has a direct proof using the intrinsic infinitesimal Carathéodory norm: at zero the matrix domain has operator norm, while a ball has a Hermitian norm; the matrix norm violates the parallelogram identity on E11,E22. No classification theorem is silently imported.

For n>=7, the first three available residue degrees give adjacent Hodge pieces. A line varying in the same-sign two-plane formed from the first and third pieces gives a holomorphic P1 of filtrations. Although the lower Hodge summand is an orthogonal complement, the filtration is holomorphic; on the conjugate eigenspace it is the Q-annihilator filtration. This distinction was explicitly checked.

One precision was corrected on self-read before completion: when the higher of two Hodge pieces is positive, graph coordinates use P→N, followed by transpose, rather than the antiholomorphic operation of taking its negative orthogonal complement. The final text includes the correct holomorphic graph-coordinate convention.

Independent review requested from `/root/plethysm`; root notified of complete draft. `/root/complexity` subsequently read the complete proof and exact primary sources and reported PASS, with its own event in `cross_positivity_checks.tsv`. External Hodge theorems are cited known premises, not claimed independently reproved here.

# D-OL25–26: the sharper Spin dimension cutoff

Recorded at **2026-11-21 23:21:41 UTC**, from the clock tool.
Author `/root/imprimitive`, GPT-6 Astra Pro, reasoning effort inherited/not
separately exposed; run HODGE_DIVISION.

## Frozen proof and author check

`spin_sharpened_section.tex`, SHA-256
`64b96290e2813c533cbe2817b789006e15359a2634946c1d035447aa00b61d78`.

The author has read the entire written proof twice and the complete
certificate program. PASS. This is a new author derivation, not an
independent-origin re-proof. Root and G34 whole-proof reviews have been
requested; they are pending as of this record. The previously frozen
D-OL22–24 proof is unchanged.

The new statement excludes actual rank-nine six-dimensional multiplicity
sources with nonempty mixed Spin cores whenever every odd natural
dimension is at least751 and every even natural dimension at least752.
It allows all nontrivial irreducible modules, represented central
kernels, scalars, compatible outer normalizers and factor permutations.
There is no ordinary-character, selfduality or transitivity premise.
For the transitive-core problem, the surviving necessary natural bounds
are therefore odd dimension at most749 and even dimension at most750.
No existence result inside that remaining range is inferred.

## Exact new constants

The published **second** line of LST(4.3.2), printed p.1918, has exponent
`sqrt(N/6)` and hypothesis `N>=144`. It is distinct from the first line
`sqrt(N/7)`, whose displayed hypothesis is `N>=567`.
Both lines were freshly checked visually on the complete published page,
not inferred from OCR. The full theorem/proof pp.1917–1923 was read
earlier in this run; the exact support convention, constants, sequence,
and restricted-scalar remark were freshly rechecked for the Spin work.

At N=375 the rational exponent419/53 works because
`2*419^2=351122 < 351125=125*53^2`, and
`19^419*150000^53 < 20^419*99997^53`.
The latter is a comparison of2692-bit positive integers. Taking positive
53rd roots proves the required bound without floating-point powers.
The resulting good threshold is `delta0=1/6+1/100000`.

The same quadratic Gauss argument gives the sharper rank-one fixed
fraction `(q^-1+q^-20)/(1-q^-20-q^-40)` in complement dimension at
least43. Its exact q3 endpoint yields `beta0=1/6-1/10000000`.
The proof explicitly derives the error bound, the all-q monotonicity,
and the all-dimension hypotheses. The source margin is exactly
`11*beta0+delta0-2=89/10000000`. The lifted-radical degree floor is
greater than one million, so even one good mark among twelve violates
the actual Euler budget. Twelve bad projective reflections are excluded
by the complete generation argument in either parity.

## Computation and exploration record

`check_spin_sharpened.py` and `spin_sharpened_checked.json` are the
standalone exact certificate. The first complete execution passed in
**0.000847442 seconds**, before the clock record23:21:08UTC.
It checks the positive-integer comparison, both exact rational Gauss
endpoints, all source margins, the minimal odd/even support thresholds,
the all-Spin degree floor at those minima, and TeX source integrity.
No floating-point comparison or imported checker is used.

An initial exploratory exponent15811/2000 also passed its exact integer
comparison. A search through denominators1 through53 found the shorter
successful fraction419/53, which is the only exponent used in the final
proof. This was a simplification of a valid certificate, not a failed
estimate. No failed assertion, mathematical counterexample or repaired
execution occurred in the sharpened certificate.

## Dependencies and primary source

The complete universal Clifford/radical/normalizer/all-orders/source
proofs D-OL19–24 are retained. Their source and peer-review records are
separate. In particular sixfolds explicitly reread D-OL20 and confirmed
that no independent dimension1136 assumption remains beyond the old
support/Gauss/degree constants; the lift needs22, and the elementary
radical cases work uniformly at the new larger-than-43 complements.
That interface confirmation did not claim an independent audit of
the new constants.

**M. Larsen, A. Shalev, P. H. Tiep**, The Waring problem for finite simple
groups, Annals of Mathematics174(2011),1885–1950,
DOI10.4007/annals.2011.174.3.10.
Published primary PDF:
<https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf>.
Exact locators: gamma_q and natural support p.1907; theorem and
formula(4.3.2) pp.1917–1918; complete proof pp.1918–1923;
Remark4.3.7 p.1923 for restricted scalar set mu2 in genuine Spin.
Existing bibliography key `HOS:LST2011`; no duplicate bibitem is needed.
The local published PDF hash remains
`dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e`.

The Gauss estimate and the new numerical/source implications are proved
in full in this section. The finite certificate checks their constants
and minimal endpoints, rather than claiming to establish their
universal hypotheses by finite sampling.

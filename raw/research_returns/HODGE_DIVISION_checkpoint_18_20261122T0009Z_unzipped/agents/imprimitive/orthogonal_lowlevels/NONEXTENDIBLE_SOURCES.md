# Sources and input boundary for D-OL-09–11

Author: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed, run `HODGE_DIVISION`. Author proof and certificate freeze: **2026-11-21 21:34:48 UTC**.

The new section is `orthogonal_nonextendible_section.tex`, SHA-256 `5f7e898c37be40cb4a17cd8ccbfdce9fa48b90d3c3beb40d0637fed620ae5bd4`. It does not modify the reviewed D-OL-06–08 section.

## New published numerical input

M. Larsen, A. Shalev and P. H. Tiep, *The Waring problem for finite simple groups*, Annals of Mathematics **174** (2011), 1885–1950, DOI `10.4007/annals.2011.174.3.10`.

Official published full text: <https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf>.

Local primary copy is retained only in the sibling source cache, `agents/g34_eightfolds/bireflection/sources/LST2011_Waring_published.pdf`; SHA-256 `dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e`. The third-party PDF is not a newly authored deliverable.

Exact invoked passages: Definition4.1.1 and equation(4.1.1), printed p.1907; Theorem4.3.6, pp.1917–1918, first line of(4.3.2); entire proof, pp.1918–1923, particularly part4 on p.1922; Remark4.3.7, p.1923. All these passages and the complete proof were freshly read in this run for the immediately preceding independent HOS16 audit. The original displayed exponent and the allowed scalar set were also checked visually from the rendered published pages.

The first exponent is `sqrt(N/7)`, valid for `N>=567`. The constant is `gamma_q=19/20` for `2<=q<43`, and `1/(sqrt(q)-1)` for larger q. The remark permits support restricted to `mu_2` for the spin group. In characteristic two that set has the single element1, so the relevant support is the natural moving rank. The theorem concerns all nontrivial ordinary irreducible characters of the finite simply connected classical group; inflation from the natural orthogonal quotient is legitimate and needs no faithfulness assumption.

The main paper's already supplied bibliography key `HOS:LST2011` is reused. No duplicate bibitem is required.

## Previously checked inputs reused with their hypotheses

- D-OL-06: exact line-radical group law, generation by two opposite radicals, equality and half-dimension bound of their fixed spaces, norm-level weight orbits, and the quadratic Gauss estimate. These arguments preceding the `R(g)` application do not assume an O-extension.
- D-OL-07: complete natural semilinear-normalizer coverage, including represented central quotients, arbitrary-field outer order and scalar centralizer; norm and form rescaling; finite-field vector descent. The new argument takes a projective-prime-order power, so its nontrivial field component has prime order even when the original field degree is composite.
- Li–Xia, Section2.2.2, Table2.1, author p.14, for the complete outer orders. This is the exact input already read in full for D-OL-07. The new result does not add an unexamined automorphism classification.
- Taylor, *The Geometry of the Classical Groups*, exact reflection, Witt, finite quadratic decomposition and perfectness passages recorded in `SUPPORT_SOURCES.md`. The rank-one exclusion is the same determinant/Dickson statement already checked there.
- Hiss–Husen–Magaard, ordinary-cover discussion p.4 and Chapter5 Table1 p.35, for the nonexceptional orthogonal covers at these large dimensions, already read in the preceding whole audits. The LST input is applied by inflation along the standard cover, rather than by asserting a character theorem for a different quotient.
- Guralnick–Larsen–Tiep, Inventiones **235** (2024), Theorem3.7, pp.165–167, for the ordinary degree lower bound. Full statement/proof previously checked in this run; exact source hash and full locators remain in `../orthogonal_levels/SOURCES.md`.
- D-OL-04–05 and D-OL-08: reality of full orthogonal characters, the invariant-form/nonreal inducing-field interface, and the actual pointed-intermediate-cover factorization. No source dimension inequality is treated as sufficient for dominance.

## New arguments

The new commutator uses an element of a line radical inside Ω, instead of a reflection outside Ω. Its natural moving rank can be four. The Gauss error for moving ranks2–4 remains at most `q^(N/2)`, giving the support bound with no O-extension.

The new uniform semilinear count uses the identity

`-18-[ell-N(ell-1)] = (N-20)(ell-1)+19(ell-2) >= 0`.

For even characteristic, the no-fixed-hyperbolic-pair case has either a semisimple fixed space of dimension at most2 or an involution moving rank at least `d/2-1`. Thus `d>=1136` gives the published support threshold567. A character of Ω invariant under the nontrivial `O/Ω=C2` coset extends by rescaling one involution intertwiner; consequently a nonextendible character has only inner compatible linear normalizers. These are new proved arguments, not cited as external facts.

## Exact certificate boundary

`check_orthogonal_nonextendible.py` and `orthogonal_nonextendible_checked.json` are authored here. First execution passed in0.058891208 seconds; the final frozen-proof execution passed in0.057138158 seconds. There was no failed certificate attempt. The checker independently clears all rational constants, checks the universal exponent identity symbolically, and supplies actual rank-four commutator witnesses in characteristics2,3,5 on a24-dimensional split space. It also checks the fixed hyperbolic pair in each example and basic TeX delimiter/control-character integrity.

These finite examples do not prove the universal character-support statements. The complete written argument supplies those statements; the supplement confirms the critical arithmetic and that rank four really occurs.

# P-F25: binary determinant rays, source specialization and remaining gate

Author/checker: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Theorem discussion: `work/positivity_binary_holes.tex`. Root assigned the new deductions the identifier P-F25; the BDP classification remains cited background. Existing B-H check rows below refer to the displayed subclaims within P-F25.

## Verified result and scope

Brouwer–Draisma–Popoviciu Proposition 4.2 is a complete known zero classification for invariants of a single binary form. With `q=2/gcd(d,2)`, ordinary degree `D=q*s` is the genuine ordinary-plethysm stretching grading for outer partition `(q)` and target `(d/g,d/g)`. Evaluation against compatible powers of a volume vector identifies the whole invariant ring, not just its dimensions, with this canonical multiplicity algebra.

The derived table has maximum finite realized hole thirteen, attained at binary sextics. Quadratics and cubics have even stretch support; their odd constituents vanish identically. This is a specialization of a published classification, not a new classification or historical-priority claim.

**No strict saturation-index bound of thirteen is inferred.** The supplied GCT VI Definition 1.2.4 requires positivity of every nonzero constituent polynomial at every positive integer, including values outside the constituent's residue class. Actual coefficient nonvanishing alone is insufficient for that requirement.

## Exact sources actually read

- BDP, *The degrees of a system of parameters of the ring of invariants of a binary form*, Transformation Groups 20 (2015), 953–967, Proposition 4.2, printed p.957. URL <https://pure.tue.nl/ws/files/17749340/Degrees2015.pdf>. Direct retrieval and exact statement/proof: `turn255124643view0`, earlier `turn438638339view0`. Section 1, p.953 and Proposition 2.1, p.954 give the invariant dimension and the `d>=3` parameter scope. The source's proof of Proposition 4.2 is independent of the problematic necessity argument in its Theorem 3.4 discussed in the separate audit.
- Derksen, *Polynomial bounds for rings of invariants*, Proc. AMS 129 (2001), 955–963: Theorem 1.1, Proposition 1.2 and Example 2.1, p.956, give `sigma<=2d^3` and `beta<=(3/2)(d+1)d^6`. Exact direct retrieval `turn426275223view1`. URL <https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.7.pdf>.
- Same source, Section 3, Lemma 3.2 and equation (3.1), p.957, give the genuine all-lcm-degree system of parameters; Section 4, Proposition 4.2, pp.960–961, improves the generator bound through module generation and a polynomial extension, not a parameter system of the original ring. Direct exact read `turn255124643view1`, with the full Section 4 read earlier at `turn321633106view0`.
- Supplied GCT VI transcription `sources/LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex`, Definition 1.2.4, label `dintrosat`, was freshly reread for the strict off-residue requirement. P-F17 already supplies the precise canonical Cartan-ring and global-quasipolynomial references.

## Quantitative consequence and limit

The finite collection of null-cone equations has stretch degrees at most `B_d=floor(2d^3/q)`. Raising each to degree `L_d=lcm(1,...,B_d)` preserves its common zero set. Homogeneous normalization gives an all-`L_d` h.s.o.p.; the already-proved prime-avoidance extension argument bounds the lexicographically canonical largest degree by `L_d` too. For dimension `r=d-2`, P-F9 and the canonical global-quasipolynomial property give `s<=p<=(d-3)L_d` for `d>=3`. The quadratic case is explicit.

This proves a computable envelope. It does not prove a polynomial canonical PH3 bound. A polynomial upper bound on algebra generator degrees does not automatically supply a polynomial upper bound on homogeneous parameter degrees. No stronger implication is being silently used.

## Actual verification

I reread the entire draft and independently substituted every case of the source classification into `D=q*s`, checked the determinant weight and Cartan multiplication, the parity exceptional cases, all bounds and source hypotheses, and the lcm normalization/lexicographic/positivity inference. `/root/complexity` independently reviewed the entire draft and exact primary passages and reported PASS on 2026-11-21; its separate ledger preserves that event. No calculation is being called an independent proof of the known classification.

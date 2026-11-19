# Current source investigation: restricting the surface-Tate gate

Status at 06:31 UTC,19 November2026: exact theorem statements and source metadata opened; full reduction proof audit still in progress. No new proved gate is asserted at this timestamp.

Ertl–Keller–Qin, Comparison of different Tate conjectures, arXiv2012.01337v4 dated4August2025, Remark4.13 authorp56 points to deJong unpublished note, Morrow Theorem4.3 and Yuan Theorem1.6. Primary open turn152399652view0 and exactremark turn693883516view0.

Yuan, Positivity of Hodge bundles of abelian varieties over some function fields, Compositio Mathematica157(9)(2021),1964–2000, DOI10.1112/S0010437X21007430. PublishedPDF obtained from https://par.nsf.gov/servlets/purl/10327977 via direct download, SHA256fbcb452f4d61444d8dbb89eff3b4a9665b5be7bae95b6c461360fd13c882e2ef. Theorem1.6 on publishedp1968 states that for a FIXED finite field k, divisor Tate for every smooth projective surface with H1(O)=0 implies divisor Tate for every smooth projective surface over that same k. Its full proof is in section4; audit is now reading it. Authorcurrentversion also opened at https://faculty.bicmr.pku.edu.cn/~yxy/preprints/positivity_hodge_bundle.pdf (turn271543023view0), and firstarXivversion1808.03960v1 opened (turn267791171view1); do not mix pagination.

The proposed change would be a proper subclass restriction of the existing surface gate. The reverse universal implication is immediate; the difficult direction is exactly Yuan1.6. It does not assert Tate for the restricted surfaces. The already-audited Kahn/Morrow all-dimensional reduction remains the source for higherdimensional consequences; deJong unpublished note has not been obtained and is not silently cited as read.

## Completed proof check, 06:39 UTC

The full published Section 4.1--4.2, pp. 1994--1997, has now been read by Part D and independently by root. The source audit passes. The exact written proof is `part_d/b3_irregularity_zero_surface_gate.tex`, awaiting a separate written-draft audit when this addendum is entered. Labels are `lem:B-surface-Tate-prime`, `thm:B-irregularity-zero-surface-gate`, and `rem:B-irregularity-zero-source-scope`.

The source theorem is over a fixed finite field in every characteristic. Its terminology in Section 1.6 requires geometrically integral varieties. Consequently the universal statement in our paper is obtained by applying the theorem separately over all finite extensions of the prime field, then accounting for larger constant fields by induction of Galois representations. There is no descent assumption omitted.

The proof proceeds over k. A finite-field Lefschetz pencil yields a semistable Jacobian over k(t). Yuan Theorem 1.1 splits that Jacobian up to isogeny into a constant part and an abelian variety A with ample Hodge bundle. The constant factor has analytic and Mordell--Weil ranks zero. If A=0 the original surface already satisfies Tate. Otherwise Theorem 4.5 gives a regular projective model of A-dual whose first coherent cohomology vanishes. Sufficiently ample Poonen sections retain that vanishing and inject the generic H1(O), producing a surface Y with H1(OY)=0 and A as an isogeny factor of its generic Jacobian. Rank-form Artin--Tate then gives Tate(Y) implies Tate(original surface).

The fixed-ell bridge is supplied explicitly in our lemma. Hodge index and finite averaging give a nondegenerate intersection form on NS^Gamma. If this equals the Frobenius invariant space for one ell, its orthogonal complement has no eigenvalue 1. Thus the algebraic rank equals the multiplicity of 1 in the Frobenius polynomial. That polynomial is independent of ell, while the algebraic invariant lattice injects for every ell. Therefore surjectivity holds for every ell. No general semisimplicity conjecture enters.

This is a proper geometric subclass: E times P1 for an elliptic curve has coherent irregularity one and is excluded. The restricted hypothesis contains no arbitrary original surface, correspondence, family, or alteration among its inputs.

## Additional source scope checks

- Poonen, *Bertini theorems over finite fields*, Annals 160 (2004), 1099--1127: author PDF https://math.mit.edu/~poonen/papers/bertini.pdf independently opened, Theorem 1.1 author p. 2 and Section 2.4 author p. 7 read. The supporting complete low/medium/high degree sieve proof is not claimed independently re-proved here.
- Original Tate, Bourbaki Expose 306 (1966), Section 4(d), printed pp. 427--430: https://www.numdam.org/item/SB_1964-1966__9__415_0.pdf opened. That historical text explicitly labels the refined comparison conjectural in full generality. We use the modern rank-form statement of Yuan Theorem 4.3, not an invented completed theorem in the original paragraph.
- Nguyen's 2005 Berkeley thesis metadata page was opened; its full text has not been obtained. The pencil theorem is used as an explicit input of Yuan's published reduction.
- Kun̈nemann and Faltings--Chai are used through Yuan Theorem 4.5. Their full primary texts have not been separately obtained in this check.
- The Q_p in the displayed recollection preceding Yuan Theorem 4.3 is an apparent typographical error; the definition in Conjecture 1.5 and our statement use Q_ell.

## Canonical and numerical refinement: complete written audit, 06:50 UTC

Part D read the entire added `cor:B-canonical-surface-gate` in `sections/b3_irregularity_zero_surface_gate.tex`. The proof passes. This is an inference from the freedom in Yuan's last cut, not an extra conclusion claimed to be stated in Yuan.

When the original regular model P has dimension two, replacing it by P times P1 preserves its H1(O) and the Pic0 of its smooth generic fibre. Thus the construction always reaches a smooth projective threefold W with H1(O)=0, smooth generic fibre and an injection of the original generic H1(O). The final hypersurface Y in |L^d| can be chosen for arbitrarily large d while meeting both Poonen smoothness conditions. All relevant vanishings and very-ampleness conditions have one finite threshold for d, so they are compatible.

Adjunction gives omega_Y=(omega_W tensor L^d)|Y, which is very ample for large d. With H=c1(L) and K=c1(omega_W), direct expansion of the normal-bundle sequence gives

K_Y^2=d^3 H^3+2d^2 K H^2+d K^2 H,

c2(Y)=d^3 H^3+d^2 K H^2+d c2(W)H.

Both have positive leading coefficient H^3, so their ratio tends to one, while K_Y^2 tends to infinity. The divisor exact sequence and the Hilbert polynomial give chi(O_Y)=H^3 d^3/6+O(d^2). Since H1(OY)=0, pg(Y)=chi(OY)-1 also tends to infinity. Hence any fixed lower bounds and any fixed positive neighbourhood of Chern slope one are simultaneously available over the original k.

These are intrinsic conditions on the tested surface. Projective planes and K3 surfaces already show that the canonical condition is a proper further restriction of the H1(O)=0 class. The numerical tail conditions are recorded as consequences of this one high-degree-cut mechanism, not counted as successive movements of the unresolved gate. Part B independently opened the exact Stacks very-ampleness and conormal-sequence inputs; this Part D audit verifies the written mathematical deduction and does not claim another opening of those sources.

# Source metadata for recovered higher-comparison proofs

Prepared 2026-11-20 after checkpoint19. This is an integration note; no shared bibliography was modified.

## Existing bibliography keys suffice

| Existing key | Primary source | Exact use and locator |
|---|---|---|
| Mnev2007 | Nikolai Mnëv, *Combinatorial fiber bundles and fragmentation of a fiberwise PL-homeomorphism*, arXiv:0708.4039v3 (16 September2007), https://arxiv.org/pdf/0708.4039 | A147/A148/A156/A159: literal product prisms, Proposition4 p.21, equation(11), Proposition5 pp.22–23; full-product endpoint coning, Lemma3 proof Steps2–3 pp.24–25; conic enlargement and incidence, Propositions35–36 pp.61–63; finite rank coarsening, Lemma6 pp.63–65; common coloring procedure, Lemma8 pp.67–68; functorial separation, Proposition57 pp.89–90. |
| Shiota2010 | Masahiro Shiota, *PL and differential topology in o-minimal structure*, arXiv:1002.1508v3 (17 February2010), https://arxiv.org/pdf/1002.1508 | Theorem2.1 p.5 supplies finite marked compact-polyhedron Hauptvermutung. Theorem2.2(1) p.6 supplies exact single-scalar triangulation in the separately audited A5.019. Field conventions are on pp.1,5. |
| Coste1999 | Michel Coste, *An Introduction to O-minimal Geometry*, November1999, author notes, https://perso.univ-rennes1.fr/michel.coste/polyens/OMIN.pdf | A155 and the coefficient-cell arguments use Hardt's theorem for definable families, Theorem5.22 pp.62–63. The notes explicitly work over arbitrary o-minimal real closed fields in §1.3 pp.9–10. |
| RourkeSanderson1972 | Colin P. Rourke and Brian J. Sanderson, *Introduction to Piecewise-Linear Topology*, Springer,1972 | A160 uses the recovered, independently audited A115 parameter-preserving PL field-invariance proof. Its simultaneous subdivision input is Theorems2.14–2.15 pp.17–19. The actual archived A115 proof, rather than an unproved interpretation of Shiota's homotopy notation, is the dependency. |

These keys already occur in RESEARCH_SA20_references.bib and/or notes/root_references.bib. Mnev2007 is also in agents/singularities_duality/references.bib. No duplicate entry is necessary.

## Source/proof distinction that must remain explicit

Mnëv's input category is PL. A147 supplies the new definable fixed-point deformation and then verifies that the finite support constancies suffice for the original finite coloring procedure. The marked ball/equatorial-disk property follows from Proposition36's conic-star and incidence properties together with the fixed locally flat seam subcomplex. It is our inference, not a separately stated source theorem. The split marked coarsening is likewise a checked modification of Lemma6, not its unchanged inscribed-ball conclusion.

The constant initial coloring Q is fixed before the fine K, the Hudson level number M, and the configuration presheaf. At the Proposition36 input, every Q(lambda) is this Q. Later rank subdivisions do not require choosing K again.

Shiota's finite marked Hauptvermutung is used after a finite spatial-cell system exists. It is not cited as a theorem preserving arbitrary parameter projections. Coste's graph trivialization is combined with our compact graph-projection argument to obtain joint evaluation on coefficient cells.

## Independently reopened originals during reconstruction

- Mnëv: readable full PDF turn528581511view0; Proposition57 turn812523702view0; complete Lemma8 proof and rank interface turn142030840view0.
- Shiota: readable full PDF turn552853085view0; exact Theorems2.1/2.2 and field conventions turn655906728view0.
- Coste author original: turn976103696view0; exact Theorem5.22 turn817415628view0.

The A157 and A158 external inputs are owned by singularities_duality. Their recent exact texts and source entries are in that agent's recovered sources and recovery_references_pending.bib. Our independent complete audits are A157_independent_audit.md and A158_independent_audit.md. A154's variation clocks and A156's PL normalizer are proved explicitly in the recovered source; they are not attributed to an external parametric theorem.

## Integration dependency order

A147 finite regularity criterion; A148 common-data pair criterion; A152 exact relative graph regularization; A154 spatial factorization and real surjectivity; A155 real-range/real-model consequences; A156 relative PL filling and real injectivity; A157 finite all-field join resolution; A158 all-field compact metric resolution; A159 standard-bound all-field higher surjectivity; A160 exact-relative all-field injectivity using recovered A115.

All these comparison statements retain the separate original A1(b) whole-TOP computation gate in base dimensions3 and4.

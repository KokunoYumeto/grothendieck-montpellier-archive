# Full nonabelian finite generation: source assessment

Checked on 2026-11-20, 06:30--06:42 UTC. This is a research note, not a new theorem resolving D.1 or D.2(ii). We introduce no finite numerical example here.

## Exact remaining group-theoretic datum

We opened Pagano and Shusterman, *High Rank and Multiplicity in Random and Perfect Profinite Groups*, arXiv:2609.30200v1, submitted 24 September 2026, Sections 3.1--3.2 and Theorem 3.5 with its proof. For a monolithic primitive finite group L with socle A, let L_t be the t-fold fibre product over L/A, and let f_L(m) be the first t for which d(L_t)>m. The theorem says that a finite group H requiring more than m generators, with m at least two, has a quotient L_{f_L(m)} for some L with d(L)<=m. Thus excluding arbitrarily large such crowns is a precise target; individual finiteness of the set of L-torsors is not a uniform exclusion.

When A=V is abelian, the theorem expresses f_L(m) using the dimension of V over its endomorphism field and the first cohomology of the complement. When A is nonabelian it gives f_L(m)>|A|^(m-8/5). For a nonabelian simple L, the threshold is one plus the number of generating m-tuples modulo automorphisms. These are finite group results. We have not obtained the required geometric bound on crown multiplicities for the residual punctured proper schemes.

We also opened Lucchini, Marion, and Tracey (2020), *Generating maximal subgroups of finite almost simple groups*, Forum of Mathematics, Sigma, 8, e32, author repository PDF, printed pp.10--12. Lemma 2.5 and Proposition 2.6 make the same distinction between abelian and nonabelian chief factors. A bound on cohomology with irreducible finite modules does not by itself bound the multiplicity of a nonabelian simple crown. The already checked alternating-product obstruction in Part D remains applicable.

Detomi and Lucchini, *Crowns in profinite groups and applications*, author PDF, Theorem 12 and Section 4, requires finite generation in its finiteness assertions for crown multiplicities and in the stated probabilistic-generation criteria. We do not reverse those hypotheses. No passage from smallness to finite generation is asserted.

Primary URLs:

- https://arxiv.org/html/2609.30200v1
- https://pure-oai.bham.ac.uk/ws/portalfiles/portal/147250970/LUCCHINI_et_al_2020_Forum_of_Mathematics_Sigma.pdf
- https://www.math.unipd.it/~detomi/docs/pubblicazioni/corone-profinite.pdf

The first and third sources are preserved under `sources/nonabelian_gate_2026/`. The second PDF was opened successfully by the web reader, but the separate local download returned HTTP403; the retrieval log records that failure rather than claiming a saved copy.

## Exact post-Suzuki literature scope

We reopened Suzuki (2023), *Finite generation of nilpotent quotients of fundamental groups of punctured spectra*, Journal of Algebra, 633, 489--509, arXiv:2207.01563v4. Conjecture 1.1 concerns the full punctured fundamental group. Theorem 1.2 proves finite generation of its maximal pronilpotent quotient. The proof's reduction to finite H1 with constant coefficients does not give a bound on the multiplicities above. Fresh searches of 2024--2026 primary sources did not find a full general theorem. This negative search result is not a claim that the entire literature as of November 2026 has been exhaustively classified.

The 2 April 2025 University of Michigan Srinivas seminar describes tame finite presentation and lifting obstructions; it is not an announcement of full local finite generation. Esnault--Shusterman--Srinivas, *Finite presentation of the tame fundamental group*, author PDF `141_ess.pdf`, uses the established finite generation hypothesis when applying the profinite finite-presentation criterion. Its rank-linear cohomology estimates in the tame setting do not remove the wild exceptional valuations in our residual case.

Primary URLs:

- https://arxiv.org/html/2207.01563v4
- https://events.umich.edu/event/132377
- https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf

## Langer's new rank-linear correction theorem

We opened the actual primary record and full HTML of Langer (2026), *Intersection theory and Chern classes on normal varieties II*, arXiv:2611.21118v1. The primary record dates this version to 16 November 2026. We read Theorem 0.1, Section 1.1, the entire Lemma 1.8 proof, the positive-characteristic proof in Section 1.6, and Section 5.2 through Corollary 5.9. The full HTML is preserved with a SHA256 retrieval record.

Theorem 0.1 genuinely applies to a **normal proper** algebraic surface over an algebraically closed field: its Riemann--Roch error is bounded by C times the rank, with C depending only on the surface. Theorem 1.1 is the corresponding local correction estimate. Lemma 1.8 bounds the finite-length difference between Frobenius pullback and its reflexive hull by c_R r p^(2e) on an excellent normal two-dimensional local ring.

These statements concern numerical or finite-length correction terms. They do not state a bound on all finite simple monodromy representations, do not construct a finite-dimensional tensor generator, and do not identify a fixed curve detecting all residual covers. The boundedness result, Corollary 5.9, works with ample polarizations on a normal projective variety and fixes the rank, first Chern number, a lower second-Chern-character bound, and a maximal-slope bound. It is not uniform in rank and is not a boundedness theorem for the nonprojective proper surface without that polarization.

Even a further deduction of rank-linear H1 estimates for Frobenius-periodic reflexive extensions would still leave the nonabelian crown multiplicity condition. We have not made that further deduction here: passing from coherent cohomology on the proper surface to etale cohomology on its puncture requires a separate analysis of local Frobenius terms. Consequently this source supplies a potentially useful numerical input, but closes no residual D gate by itself.

Primary URL: https://arxiv.org/html/2611.21118v1

## Audited obstruction to filling rational tails

We independently read B's full `D_pure_root_tail_obstruction_B.tex`, its exact program `code/check_pure_root_tail.py`, and output `output/pure_root_tail.json`. All thirteen recorded assertions passed in 0.044605832 seconds. We checked the valuation argument separately: after the pure normalization z^2=t+x^3 and the blowup x=s,z=sy, an Artin--Schreier change gives a nonzero simple pole along the rational exceptional divisor. The pullback cover therefore has ramification index two there. Smoothness or local factoriality of the normalized pure source and rationality of the tail do not justify filling that tail etale. The example is local and explicitly does not refute D.1 or D.2(ii).

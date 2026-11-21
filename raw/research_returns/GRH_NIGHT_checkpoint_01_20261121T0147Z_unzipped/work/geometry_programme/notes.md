# Geometry and Grothendieck programme — working notes

Last substantive source/read checkpoint: 2026-11-21T01:41:57Z, from the clock tool. Model GPT-6 Astra Pro; effort is not exposed. Filesystem mtimes are not used as check-event dates.

## Scope and durable handoff

Own deliverables are section.tex, rows.json, sources.json, events.tsv, questions.tsv and this notes.md. The parent owns the assembled paper, registers, checkpoint ZIPs and persistence. Original archives were already extracted and were not extracted again. Evidence PDFs/page renders under evidence/ are reference material for the source checks, not new deliverables or revised source documents.

The full uploaded prompt was read. A is the user-adopted Alpöge Dirichlet GRH theorem; M is conditional universal unitary Hecke GRH. Neither is presented as certifying every step of the proposed proofs. Source rows explicitly distinguish classical results, new formulations, conditional transfers, inherited conclusions, and unresolved comparison gates.

## Current movement

1. **BRIDGES Q03 is no longer merely restated.** The official cote34 PDF was downloaded in full. Thm1.1 is PDF53/footer52; the crossed-out Rem1.17 is PDF64/footer63. Exact groups are recovered: pi is an open arithmetic fundamental subgroup, I its geometric kernel, pi0 its image in Gk, I(ell) maximal abelian pro-ell quotient. H is a pi-stable pro-ell solvable quotient; earlier Lie-group language was struck out. The literal phrase puts closure[pi0,H] open in pi-prime, impossible with infinite arithmetic quotient. AG-C34-TYPE supplies Gm/Fq as a full example. AG-C34-REPAIR proves the intrinsic correction closure[P,H] open in H, for every pro-ell quotient, from the earlier theorem's finite abelian coinvariants. AG-C34-INDEX adds the torsion/Frobenius determinant index and exact Jacobian rational-torsion quotient. Alternative section-dependent intended meanings are kept separate.
2. **The original proof route was read, not inferred.** Cote34 §§2–3 occur later, PDF70–78. §2.4 dualizes coinvariants to H1 invariants, §2.5 handles compactification and finite-field curves, and §3 reduces normal X to a generic hyperplane curve. Thus the corrected statement uses an already available curve theorem, not new higher-dimensional purity. The literal Q04 equation at PDF74/footer73 was checked: multiplicative1 means trivial invariants. Standard SGA inputs are cited and not claimed re-proved from scratch.
3. **CM source gate closed.** Recovered G.W.Anderson, Cyclotomy and an extension of the Taniyama group, Compositio57(1986),153–217, originalNumdam PDF. Images27–31 were read. §5.3 defines PCM; Theorem6 §5.6 supplies Hecke/inertia/Frobenius comparison; Cor5.7.2/Rmk5.7.3 gives signed same-weight Hecke factorization. The print's internal Cor5.8.2 reference is a numbering error. Prop5.7.5 gives unconditional recognition from whole L-functions, with proof read in full (AG-CM-REC); §5.8 Theorem7 gives the exactly scoped tractible-critical period theorem (AG-CM-PERIOD). None implies arbitrary Chow projectors.
4. **Integral cote149 gate sharpened.** OriginalPDF79–86 were image-read. AG-KUMMER proves finite-level/completed Pic and Brauer exact sequences, carefully using inverse limits rather than silently continuous cohomology. AG-KUMMER-2 constructs the normal bundle from the order-two ideal class over Z[(1+sqrt(-35))/2,1/2]: rational Chern vanishing does not kill its integral2-adic class. This does not claim the separate LM6 group/cohomology comparison.
5. **Trace/determinant gate sharpened.** AG-DET extends the squared-zero trace-class determinant to specified entire selfdual order≤1 completions; AG-MOMENT gives monotone lowest-zero bounds and multiplicity; AG-HANKEL gives every finite positive Hankel minor. AG-SIGNED now characterizes the extra positivity needed in specified meromorphic quotients: a negative isolated divisor multiplicity gives an explicit polynomial witness in a finite Hankel matrix. A/M divisor location alone does not supply this positivity or Artin holomorphy.

## Independent checks and coordination

- Root independently whole-proof checked AG-FROB, COVER, LAMBDA, SIGN, HEIGHT, SIGN-NORM, CRITICAL, DET, MOMENT, HANKEL, KUMMER and KUMMER-2, without a substantive gap. Requested explicit ordering of gamma_j before use of gamma1; fixed.
- number_theory independently whole-proof checked AG-DET/MOMENT/HANKEL/CRITICAL, without a substantive gap; same gamma ordering fixed.
- I independently read and checked root MT-M01–03 whole proofs against original MasulloPDF425,426,804 and normPDF11. The complex-Gaussian zero-density and decreasing fixed-kernel counterexamples pass; the Hilbert projection repair passes. These auxiliary failures do not refute the endpoint M. Events already logged.
- I independently read root MT-Q01/Q02 path-quadric stratification and zeta proofs; both pass, including all characteristics and exact shifted signs. Events logged.
- I independently read NT-F01–04 whole proofs. A harmless Frobenius exponent typo and F03 canonical-model/boundary ambiguity were reported and fixed, then rechecked. NT-F02's sharper finite-etale error is rE_L+d|S|logx, r the number of geometricG-orbits/connected generic components; no square-root replacement needed.
- Complexity owns CX-GEO-004/005/008 finite-prime detection, forbidden-prime bounds, transitive G-set diagnostic and finite Galois-image generation. My AG-COVER is the complementary actual V4/Q disconnected arithmetic-scheme example. Complexity is now adding exact Jao–Miller–Venkatesan class/genus/isogeny graph applications; no duplication planned.
- RV1999 boundary locator supplied by number_theory and directly checked in its downloaded primary text: Theorem7-28 printed289, entire proof289–292; Theorem7-19 printed279 completed continuation/FE. This closes AG-CRITICAL's boundary-source locator.

## Honest residual gates

- General non-CM motivic/GL2 higher-rank RH is not covered by a mere weight normalization. A covers abelian Artin factors; M covers finite Artin divisor support and exact potentiallyCM factors. Higher-rank automorphy/RH and actual exceptional fibres remain separate.
- Artin holomorphy is not proved by universal Hecke GRH plus Brauer. AG-SIGNED and root MT-ART02 identify concrete additional positivity tests, rather than claiming their inequalities.
- The determinant operators here are defined from zeros, not constructed independently from primes or geometric cohomology. The arithmetic realization gate remains.
- Cote16 integral Lefschetz/algebraicity and cote44 arbitrary-cycle arithmetic Hodge index require their specified correspondences, denominators and height identities. AG-SIGN/HEIGHT corrects only the normalized analytic deduction.
- Cote149/LM6 integral comparison and specified class-group components remain; inherited2026 K8(Z)=0 is not certified and is not attributed to A/M. Alpöge step17 does not itself export an indexed K-group theorem.
- Finite Frobenius tests do not recover multiplicative scheme structure, mixed extensions, inertia maximality or a full profinite GT kernel. Rational Deligne–Drinfeld freeness in the intake remains a separate inherited2026 dependency.
- Original Q03 is resolved only as the literal obstruction plus the proved intrinsic repair; a different intended raw section-dependent group requires a fresh precise formulation.

## Evidence retrieval notes

Official cote34 full download:84,513,436bytes,210PDFpages including cover. Webopen refused the large file; a full local download succeeded. A range-download fallback was started but became unnecessary; it must not be mistaken for a different source. SHA256 is in sources.json. Source149:36,211,408bytes,136PDFpages, original equations13–22 at recorded locations, hash in sources.json. Anderson1986 NumdamPDF:66pages. The bibliography and exact locations are in sources.json, preserving web reference IDs and URLs. Local RV1999 PDF belongs to number_theory evidence and is referenced by its exact path.

## Next useful expansion

First finish parent peer checks of AG-SIGNED and AG-C34-REPAIR/INDEX, and fold any corrections into all registers. Then use the recovered Tate/CM source to connect actual theta/Shimura facts with the two-method comparison without promoting the endpoint theorem into a validation of intermediate claims. Continue gate reduction rather than merely adding unchanged archive labels.

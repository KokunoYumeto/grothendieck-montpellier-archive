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

## Update 2026-11-21T02:06:25Z

Root full-proof review of AG-SIGNED and AG-C34-TYPE/REPAIR/INDEX passed. I completed independent whole-proof checks of MT-ART05/06, the exact A5 cone and pole multiplicity thresholds; no gap found, events recorded. AG-C34-SECTION now settles the chosen-section solvable interpretation using every relevant finite arithmetic cover. AG-C34-NONSOLV gives an explicit compact analytic pro-ell counterexample to removing finite derived length in the abstract group argument; all matrix and approximation details are included. This is a group-theoretic scope counterexample, not an arithmetic realization. Registers now have44rows. Next: peer-check NT-H07/H08 tower results, then actual cote149 K(pi,1)/normal-bundle comparison.

NT-H07/H08 entire proofs independently checked at02:11:07UTC; both pass, with only optional strictly-increasing-degree subsequence clarification for family conventions. Primary Borne–Emsalem–Stix2015 Prop3.1/4.4 and surrounding continuous-cohomology arguments PDF5–9 recovered and fully read for the next cote149 comparison.

## Update 2026-11-21T02:17:25Z

AG-C149-COMP/LIFT/ELLIPTIC now give the exact group/cohomology comparison and a concrete nonsplit order2 normal-bundle extension over E/Q:y²=x³−x through which every Galois section lifts. Continuous H² is justified via vanishing lim¹H¹, not silently equated with the inverse limit. The original cote149 K(pi,1) condition is honored; the LM6 global tripod-kernel question remains distinct. Primary BES2015 whole relevant proofs and source images checked. Registers now have 47 rows. Next primary route: verify the exact Brown–Sharifi regular-prime/Ihara theorem and determine the residual ell2/irregular integral gate; continue peer review of number-theory zero bounds.

## Update 2026-11-21T02:21:24Z

Parent independently checked AG-C149-LIFT/ELLIPTIC whole proofs and passed. New exact LM6 rows recover Brown–Sharifi regular-prime kernel equality, the conditional Greenberg obstruction to canonical generators at irregular primes, and the explicit filtered-Soulé factorial test (p3,m5). This sharpens the Fable integral bridge without refuting LM6A45. Three primary bibliography records added with honest proof-reading scopes. Registers now 50 rows and 20 sources.

At 2026-11-21T02:22:06Z I independently checked NT-Z14 whole multiplicity/gap proof and NT-Z13 hypotheses; all pass. Event scope excludes an independent re-referee claim for the original CCM theorem. JSON/TSV schemas and catalogue ID uniqueness also checked after the 50-row update.

## Update 2026-11-21T02:27:02Z

Added five formal-height method rows. Exact unramified exponential and derivative bounds proved without the inherited Lubin–Tate normal-form claim; exact restricted derivation and integral-product extension also proved. This moves Fable§2 to concrete theta integrality/normalization inputs. All whole author proof checks recorded and root peer review requested. Registers now 55 rows, 21 sources.

At 2026-11-21T02:27:39Z the whole NT-H09/H10 relative closed-point tower/Frobenius-power proofs were independently checked and passed; exact collision-sum and finite quotient issues checked.

## Update 2026-11-21T02:40:03Z

The number_theory independent whole-proof review of AG-FG-EXP/DER/PPOWER/PRODUCT passed; two exponent-comma typography artifacts were fixed. Added five Arthur/Lefschetz rows, with exact Arthur1989 Prop9.1 rather than a blanket principle. The r_mu step changes strings in an explicit exterior-square example; Arthur and Deligne factors have different local L-functions despite the same Weil eigenvalues. Rational data do not fix integral indices. A positive exact binomial cokernel criterion now identifies sufficient divided-power and integral-splitting data for the theta-lattice gate. Full author checks recorded; peer review requested. Registers now 60 rows, 25 sources, 36 questions.

At 2026-11-21T02:41:08Z, independently whole-proof checked NT-Z17/Z18 and relevant primary hypothesis statements. Both pass. The shifted conjugate product closes the arbitrary unitary infinity-type zero-bound gate with pure norm exceptions handled separately. The sinc-square half-nonvanishing transfer uses the exact closed-support HR theorem.

## Update 2026-11-21T02:51:22Z

Parent and number_theory independently checked all four new Arthur/Lefschetz proofs and passed. The requested isotypic-lattice wording was corrected. Added AG-C149-NORMAL/FULLLIFT/CUSP: an explicit finite cyclic cover gives the actual cusp normalizer in a hyperbolic family, every Galois section lifts through full profinite inertia, yet the E/Q order2 class gives a globally nonsplit normalizer. The proof retains proper Künneth, crossed-cocycle stabilizers and the distinction from arbitrary families and LM6A45. Entire Stix local-theory and SGA1 product proofs read with exact primary locators. Registers now63rows,27sources,38questions,84events. Parent peer review requested.

At2026-11-21T02:56:01Z independently read all of the OpenAI4Oct2026 factoring preprint§4pp13–19, including geometry/module setup and every proof4.1–4.6. Re-derived the Frobenius filtration, Hilbert90 label sign, descent and final lattice obstruction; no gap found. Source local file work/literature/OpenAI_factoring_20261004_mirror.pdf/.txt, supplied by the complexity/root research. Scope explicitly excludes the norm solver and full factoring theorem. Six exact-source proof events recorded and both agents informed.

## Update 2026-11-21T03:01:00Z

Root independently passed the entire new cusp-normalizer trio; source Lemma14 scope chi≤0 including Gm was checked and clarified. Added AG-LEFSCH-INDEX/DEFECT, removing integral weight and isotypic splitting from the total-index gate, and giving exact finite Smith defects with possible ambiguity only at common-factor primes. Added the precise PF26 cyclic-cover geometric crosswalk and mapped geometric-only reviews to CX-ALG-027/028. Independently checked NT-L13 conductor-uniform Lindelof specialization against the complete cited corollary proof; passes with exact scope. Registers now66rows,28sources,40questions,96events.

## Update 2026-11-21T03:13:41Z

INDEX/DEFECT/C8 independent whole-proof review by complexity passed at03:10:53. Added three actual elliptic-function special-value rows, closing integrality rather than postulating it: REG uses pole-cancelled x−b²x∘[b], TORS uses prime-to-p torsion translations, HECKE fixes an exact class-number-one factorial/period normalization. All whole author proofs checked. The beta52 rational recurrence example has exact v7=7 and meets the formal bound. The cited stronger Katz/Fourier theory is located with honest limited source-check scope. All66 earlier catalogue IDs now explicitly appear in section.tex. Registers now69rows,29sources,42questions,102events.

Exact reproducible beta52 certificate: set c2=1/5,c4=0 and for even n=6,...,50 set c_n=6*sum(c_i*c_(n−2−i), even i≥2)/(n(n−1)−12); beta52=50!*c50. Rational arithmetic gives279611773860172254850760921879997834507061297152/265.

At2026-11-21T03:17:16Z added retrospective exact-S-AG-source-ID events for all26 bibliography records previously documented only through consequence events and source verification scopes. The records explicitly distinguish carried text, statement/location checks, and whole relevant proof readings; they do not claim a fresh full reread at this recording time. All29 source IDs now have check events.

Root whole-proof review of AG-THETA-REG/TORS/HECKE passed at03:14:54UTC; no gap found. Root independently checked the numeric lower bound; the exact rational recurrence was my separate computation.

Reproducible exact arithmetic certificate (Python standard library):

```python
from fractions import Fraction
from math import factorial
c = {2: Fraction(1, 5), 4: Fraction(0)}
for n in range(6, 51, 2):
    c[n] = 6 * sum((c[i] * c.get(n - 2 - i, Fraction(0))
                    for i in range(2, n - 3, 2)), Fraction(0)) / (n * (n - 1) - 12)
beta52 = factorial(50) * c[50]
def valuation(n, p):
    count = 0
    while n and n % p == 0:
        n //= p
        count += 1
    return count
assert beta52 == Fraction(279611773860172254850760921879997834507061297152, 265)
assert valuation(beta52.numerator, 7) - valuation(beta52.denominator, 7) == 7
```

## Update 2026-11-21T03:23:19Z

AG-THETA-CLASS/RAY remove the class-number-one and prime-to-p conductor restrictions in the actual elliptic-function special-value sector. Normalized prime-to-p ideal quotients retain the same global period scale and integral unramified formal group; finite-character coefficients may be ramified but remain units. Proper conductor eliminates the origin regularization and gives the full d_h(m−2) valuation without the weight congruence exception. Entire new proofs and relevant Vélu source derivation read; parent peer review requested. Registers now71rows,30sources,44questions,131events.

## Update 2026-11-21T03:28:23Z

AG-FG-POLE/THETA-PCOND close the remaining inert-p conductor gate with an honest exact denominator. The original unramified formal exponential controls integral functions even after ramified coefficient extension; formal torsion has exact parameter valuation and an explicit pole loss. The normalized ray lattice contributes exactly p^(−rm), including the x-coordinate scale. Mixed conductor points reduce away from zero; pure p-conductor points use height2 connectedness and the formal bound. Entire new proofs author-checked; parent peer requested. Registers now73rows,30sources,46questions,133events. NT-H12/H13 whole new proofs were also read with no gap before learning root had already completed the primary-source peer check; no additional source reread was done.

## Update 2026-11-21T03:33:14Z

AG-THETA-NONINT now gives a small exact normalization counterexample: the canonical reduced theta for the square CM lattice has first nonintegral formal coefficient1411/2016 at t8 over Z7[i]. Integral units and parameter changes cannot repair it. This scopes the remaining theta comparison and does not challenge adopted A or any separately normalized derivative statement. Primary BK reduced-theta convention and ordinary hypothesis checked. Complete independent reviews NT-L14/H11 pass, including all conductor/local/residue factors; classical Lumley numerical theorem remains cited. Registers now74rows,31sources,47questions,138events.

Exact reproducible reduced-theta coefficient certificate (Python standard library):

```python
from fractions import Fraction
l5, l9 = Fraction(-2, 5), Fraction(2, 3)
s5, s9 = Fraction(-1, 60), Fraction(-1, 10080)
c4 = l5 + s5
c8 = l9 + 5*l5*s5 + s9
assert c4 == Fraction(-5, 12)
assert c8 == Fraction(1411, 2016)
assert c8.numerator % 7 == 4
assert c8.denominator == 7*288
```

## Update 2026-11-21T03:38:32Z

AG-CM-INTEGRAL-MODEL closes the existential unramified model gate for every imaginary quadratic K: full level3 on the classical finite-etale CM stack gives a universal curve over O_F[1/3], relative degree≤48h/w and ramification only above3. One differential can be chosen integral at any finite prescribed set of inert primes, without enlarging F. AG-CM-MODEL-DEGREE combines this with adopted A and exact LLS/NT-H02 to give the explicit degree bound48e^gamma/pi times√D times the LLS logarithmic bracket, forD≥10^10. Entire new proofs and full relevant KRY source proof read; parent peer requested. Registers now76rows,32sources,48questions,143events.

## Update 2026-11-21T03:49:10Z

AG-FG-FOURIER/THETA-FOURIER now replace the logarithmic-size loss of the elementary formal-height bound by the exact floor(pn/(p²−1)) in the integral trace-compatible CM sector. The proof keeps the ramified coefficient value group explicit and improves the mixed conductor branch without applying integral functions at a pole. Whole author checks and exact source-proof checks recorded; root peer requested. Registers now 78 rows and 32 sources. BKY2017 sigma-radius source currently available only as publisher preview; no theorem from it is imported.

## Update 2026-11-21T03:57:54Z

Added AG-SHIMURA-PERIOD/SLOPE from the fully accessible published Andreatta–Iovita2024 result. Exact period valuation, classical-versus-varying-weight conductor thresholds, all Heegner/parity/cuspidal epsilon hypotheses and the correct depletion/class-sum normalizations are recorded. New full proof gives uniform divisibility on a closed weight disk and explicit Eisenstein character sequences obstructing naive interpolation at a nonzero value. The source uses positive adelic infinity type, so the auxiliary ideal character is alpha^(-w), not alpha^w; this sign was checked against §2.1 before registration. Registers now 80 rows, 33 sources. Parent peer requested. Root independent FOURIER pair/source review passed03:53:37; root owns those peer events.

Root whole-read AI2024 normalization and new slope/eta proof passed, with the precision correction applied at2026-11-21T03:58:10Z: unchanged local-unit character data, not an unchanged full finite adelic component. Root owns the peer event.

# What the two inputs change

This is a living account of the catalogue, not a claim that every consequence of an open-ended mathematical hypothesis has been exhausted. The exact statements and hypotheses are in `CONSEQUENCES.tsv`; the proofs and classical locators are in `GRH_NIGHT.tex`. Every identifier below refers to that record. A check of a classical theorem's statement is distinguished in `CHECK_EVENTS.tsv` from reading its entire proof.

## 1. The dependency map

**A_D** denotes the RH and Dirichlet-GRH theorem designated by the task, with the statements in `ALPOGE_Main.lean` and `ALPOGE_Statements.lean`. It is used as a cited theorem. The imported Lean development was not rebuilt here. **M_H** denotes the universal unitary-Hecke GRH claim of Masullo §1.2, conditional throughout. Its rank-one scope includes number fields other than Q and infinite-order unitary characters.

M_H contains A_D at the level of endpoint zero-location statements. Consequently the conjunction of the two endpoints has no larger L-function domain than M_H. The genuine additional results come from combining these endpoints with independent theorems, exact geometric factorizations, or new arguments about the proposed methods. An endpoint theorem also does not certify every auxiliary lemma in a proposed proof.

Three distinctions organize the record. A divisor-support theorem locates both zeros and poles; holomorphy additionally requires nonnegative local orders. A generic-fibre motivic factorization must be supplemented by the actual exceptional Euler factors before it describes a scheme over Z. An analytic zero statement does not determine integral torsion, extension classes, or algebraic correspondences.

## 2. Primes, fields and finite arithmetic geometry

NT-P01–P12 turn the adopted Dirichlet input into explicit estimates for primes and prime powers, primes in progressions, the least prime in a reduced class, subgroup witnesses and primitive roots. The constants come from the precise classical versions cited in the catalogue. The corrected v3 of Lamzouri–Li–Soundararajan is used. The least primitive root for a fixed prime and Artin's conjecture for a fixed integer at varying primes remain different statements with different field hypotheses.

The explicit progression estimates NT-P11/P12 are obtained from cyclotomic Chebotarev. A small model issue matters: if q is 2 modulo 4, the prime 2 is unramified in Q(ζ_q) but is omitted from reduced progressions modulo q. The formula retains an extra log x term for prime powers and an extra 1 for primes. This is an instance of the exceptional-fibre bookkeeping in ZETA_TWO ZT04, not a new analytic error term.

Under M_H, NT-C01–C04 give effective Chebotarev and prime-ideal intervals for arbitrary number fields. These concern closed points of Spec O_K and Frobenius in finite étale covers. Their exact input is RH for the named Dedekind zeta functions; the whole universal assertion is more than a given application needs. A_D suffices for the relevant abelian extensions over Q.

NT-F01–F04 transfer the class-by-class estimates to arbitrary class functions and finite étale point counts. The main term for a permutation character is the number of geometric orbits, so the error depends on the number of generic components rather than automatically on the full cover degree. Boundary primes have their own explicit contribution. This strengthens the finite-Galois and closed-point rows in RETURN_ZETA_TWO IAQ039/IAQ040–071 and the SA07 D.3.2, E.2/E.3 programme, with the Galois-category interpretation in SGA 1, Exposé V, §7.

AG-FROB and CX-GEO-004/008 make finite recognition effective. For actual Artin–Tate objects split by a specified Galois extension L/Q, equality of the Euler polynomials up to the Bach–Sorenson bound identifies every weight component. A finite set of Frobenius classes also certifies that an image is the whole finite Galois group, and at most floor(log_2 |G|) selected representatives generate it. The auxiliary quadratic extension in CX-GEO-004 permits prescribed excluded primes with an explicit discriminant cost. These close the finite-recognition formulation of ALPOGE_BRIDGES AQ-FINITE and sharpen ORDER item 30. They do not present an arbitrary entire profinite fundamental group by bounded data.

Recognition of a representation does not reconstruct the multiplication of a finite scheme. AG-COVER gives actual biquadratic Q-schemes with identical Artin realizations and Euler factors but different component degrees. CX-GEO-005 gives a transitive finite-G-set example using the natural and dual seven-point actions of GL_3(F_2). Thus the distinction is present both for disconnected and transitive finite covers. In the archive this belongs beside cote 98 scans 11–12 and the finite-G-set language, rather than being obscured by a claim that all Frobenius data reconstruct every geometric structure.

## 3. Class groups, primitive-root densities and cancellation

The class-number and regulator bounds in NT-H01–H04 are consequences of the Dirichlet or Hecke functions actually identified by the class-number formula. Bach's class-group generator theorem needs class-group Hecke characters over K. An abelian K/Q does not by itself reduce those characters to Dirichlet characters over Q. CX-ALG-011/012 separates a bounded factor base from the remaining work of finding a complete relation lattice.

NT-A01 and its extensions use the fields in Hooley's or Lenstra's theorems. These generally go beyond A_D. Under M_H the necessary Dedekind-zeta hypotheses are supplied and the corresponding Artin primitive-root densities become conditional only on M_H among the named unproved inputs. The entanglement and positivity conditions in the precise classical statements are retained. The Euclidean conclusion in the catalogue likewise retains the number of inverted places and the relevant principal-ideal assumption.

NT-L02/L03 supply fixed-function Lindelöf and reciprocal bounds. NT-L09/L10 give full Perron proofs of square-root-plus-epsilon cancellation for twisted Möbius sums and fixed residue or ray classes, including the ideal coefficient majorant and the truncation error. Their constants are not advertised as uniform in a varying modulus, number field or infinity type. These are trace-cancellation consequences on arithmetic covers; they do not produce missing algebraic cycles or a geometric cohomology theory over Spec Z.

## 4. Zero statistics: the part actually supplied

NT-Z11/12 add a precise central-nonvanishing conclusion: under A_D, at least 15/16 of the primitive quadratic family chi_(8d), with nonzero odd squarefree d of both signs, have nonzero central value, in the ordinary lower-density sense as well as the stated smooth weighted sense. The full proof approximates an endpoint test by admissible Schwartz functions, uses even central multiplicity, and separately removes the weight. It does not relabel this family as all fundamental discriminants.

The catalogue records Montgomery's restricted pair-correlation result, the specified family/support theorems for low-lying zeros, the conditional moment bounds, and the appropriate Lindelöf consequences. The support restriction, normalization and averaging family are part of each theorem. Full GUE, simplicity of every zero and universal central nonvanishing are not substituted for those statements. In particular the Iwaniec–Luo–Sarnak result cited there has a separate GL_2-RH hypothesis for the non-CM family; A_D supplies only its Dirichlet part.

Two exact classical equivalents are also useful: NT-Z08 combines A_D with Rodgers–Tao's lower bound to give the classical de Bruijn–Newman constant equal to zero; NT-Z09 gives Lagarias's precise divisor-sum inequality. Neither is a new proof of the adopted endpoint.

## 5. Arithmetic schemes, Artin–Tate objects and CM objects

AG-AT, AG-DED and AG-LOCAL retain the exact results ZETA_TWO ZT01–ZT05. An all-prime point-count identity determines the Euler product. Tate twists move the global divisor lines; signed virtual contributions permit poles. Omitting a prime introduces a separate local factor: the example Spec Z[1/p] already has extra zeros on an unshifted imaginary lattice. A geometric model is therefore part of the arithmetic statement.

AG-CM applies M_H to the identified potentially CM absolute-Hodge category in ZETA_TWO CM01. The original Anderson reference has been recovered: *Cyclotomy and an extension of the Taniyama group*, Compositio 57 (1986), §5.3, Theorem 6 in §5.6, Corollary 5.7.2 and Remark 5.7.3. These locate the signed Hecke factorization and common weight. They do not make absolute-Hodge projectors algebraic. The additional classical recognition and tractible critical-period results in that same source have their own hypotheses, recorded separately in the geometry section.

AG-LAMBDA explains exactly which tensor, dual, exterior, symmetric-power and direct-summand constructions remain in the covered categories. The SGA 6, Exposé V, §§2 and 7 lambda-ring framework is compatible with these operations. A construction leaves the domain when its factors no longer have the asserted Artin or Hecke description. Positive weight is not itself the obstruction: ZETA_TWO's weight-zero non-CM example remains non-CM, while potentially CM objects of positive weight are covered.

For general schemes the reduction in ZETA_TWO ZT06 remains useful: isolate finitely many smooth-projective geometric factors and the actual exceptional fibres. M_H removes identified potentially CM factors. The residual non-CM factors still require their own analytic continuation, functional equation and RH. ZT07's elliptic example shows this gate explicitly rather than hiding it in a formal quotient.

## 6. The path quadric: a complete geometric computation

MT-Q01 gives the exact unweighted path-quadric count over every finite field, including characteristic two. If Q_k = Σ x_i x_(i+1), d = ceil(k/2), then

    #V(Q_k)(F_q) = q^(k−1) + (q−1)q^(d−1),
    [V(Q_k)] = L^(k−1) + L^d − L^(d−1) in K_0(Var_Z).

The proof uses an integral full-rank bipartite matrix and a vector-bundle stratification; there is no characteristic-dependent diagonalization. MT-Q02 supplies the exact local and global zeta functions, with the numerator and denominator signs preserved. A_D then locates the nontrivial global divisor on the three indicated shifted lines. This builds on Alpöge steps 3 and 5, Fable EXPLAINED §3 and ZETA_TWO ZT01. It is an exact result for this family, not an extrapolation of a weighted finite-character identity to arbitrary varieties.

## 7. Cote 1 and the analytic trace programme

The relevant archival companions are cote 1 scans 79–80 and 111–112 as reconstructed in SA23 geo-H-lidskii/geo-H-genus, and ALPOGE_BRIDGES BR-TR-01/02. AG-DET extends the squared-variable positive trace-class determinant to the specified entire selfdual order-at-most-one completions in the Hecke/CM domain. Central multiplicity is removed explicitly. AG-MOMENT supplies monotone bounds recovering the first positive zero and its multiplicity; AG-HANKEL supplies positivity of all finite shifted moment matrices.

These are spectral realizations built from an already located divisor. The remaining arithmetic trace gate is a prime-defined or cohomologically constructed operator with the required trace identity. The diagonal operator from the zeros does not solve that inverse problem. The meromorphic signed-Hankel refinement in the geometry section makes this especially precise: under its stated hypotheses, positivity of all the finite shifted moment matrices is the extra condition that excludes noncentral poles. Zero location does not establish those inequalities.

## 7A. Cote 34: the previously open commutator question closes in a corrected form

The official cote 34 PDF was recovered and read directly. Theorem 1.1 is at PDF page 53/footer 52; its proof is in §§2–3, PDF pages 70–78. It concerns a normal geometrically connected scheme locally of finite type over a field finitely generated over its prime field, an open arithmetic fundamental subgroup, and a prime l different from the characteristic. Its maximal abelian geometric pro-l quotient is finitely generated and has finite arithmetic coinvariants.

The crossed-out Remark 1.17 at PDF page 64/footer 63 places the commutator closure in an impossible ambient group whenever the arithmetic quotient is infinite. AG-C34-TYPE gives the literal counterexample G_m/F_q. AG-C34-REPAIR proves the intrinsic correction: for any stable geometric pro-l quotient H and extension P, the closed subgroup generated by [P,H] is open in H. The quotient is exactly (H^ab)_(pi_0), a quotient of the finite group in Theorem 1.1. Solvability and an l-adic Lie hypothesis are unnecessary for this corrected statement.

AG-C34-INDEX adds the torsion-sensitive determinant bound. For a smooth proper geometrically connected curve over F_q, the quotient is the l-primary rational-point group of its Jacobian, so its index is exactly l^(v_l #J(F_q)). Theorem 1.1's proof uses curve compactification, a cyclotomic boundary, spreading out, and the classical finite-field curve theorem. Neither A_D nor M_H is required. This changes the inherited BRIDGES Q03 gate into a proved corrected statement and an explicit refutation of its literal ambient-group wording; section-dependent interpretations remain separately identified. The original (2.5.5), PDF page 74/footer 73, was also checked, confirming Q04's classical finite-field input.

## 8. Cotes 16 and 44: correspondences, signs and heights

Cote 16 scans 14–18, no. 7, and the Coates-letter material at scans 44–50 concern integral correspondences, Lefschetz operators and index positivity. The Hodge sketch's scan offset relative to the GCT_NSRH intake is retained. The remaining gate is the stated rank/cycle comparison on X×X together with denominator control. A_D and M_H do not supply that construction in the arguments in these materials.

Cote 44 Theorems 4–5 at scans 2, 4 and 6, and the Serre letter at scans 8–9, sit beside the central-sign question in the Hodge sketch §3.5. AG-SIGN proves the correct analytic implication: a real holomorphic function, positively normalized to the right and nonvanishing there, has positive first nonzero central Taylor coefficient. Multiplicity parity follows from its selfdual functional equation. AG-SIGN-NORM gives the exact counterexample if normalization is omitted.

AG-HEIGHT then requires a separately established identity H(Z)=C F′(c), C>0. It gives nonnegativity in that precise setting; strict positivity also needs a simple central zero. Neither a general cycle-height formula nor simplicity follows from GRH. AG-CRITICAL additionally separates off-centre critical values, where classical Hecke boundary nonvanishing often already suffices, from central values where the zero theorem allows vanishing.

## 9. Cote 149, integral inertia and mixed extensions

The original cote 149 PDF was read at PDF pages 80–85, repository footers 79–84. Equations (13)–(17) discuss the inertia-normalizer extension and its H²/Kummer class; (18)–(19) identify the line bundle as the normal bundle; (20)–(22) describe the H¹/completed-unit ambiguity. ORDER item 31 supplies the comparison with LM6 A.44–A.45 and bridge B3. These sheets themselves do not assert an irregular-prime or K_8(Z) theorem.

AG-KUMMER proves exact inverse-limit Kummer sequences and, for finitely generated Picard group, the criterion that a line bundle has zero compatible integral l-adic Chern class exactly when its class has order prime to l. Identifying this inverse-limit cohomology with a chosen continuous-cohomology theory retains its own lim¹ condition.

AG-KUMMER-2 makes the rational/integral distinction explicit. On Spec O_(Q(sqrt(−35)))[1/2], the ideal (3,(1+sqrt(−35))/2) has order two in the Picard group. Its compatible integral 2-adic Chern class is nonzero and becomes zero over Q_2. The zero section of its total line bundle has that normal bundle. This refutes the shortcut from rational vanishing to integral splitting; it does not identify an uncomputed group-extension comparison in LM6.

AG-EXT retains BR-MIX-01 and ZETA_TWO SV01–SV02: the nonsplit Kummer extension of 2 and the split Tate object have the same good Euler factors. Deligne–Goncharov's exact rational Ext and free graded Lie-algebra statements are separately located. Their rationality does not compute integral torsion or an entire profinite kernel. Alpöge step 17 is therefore kept distinct from what its endpoint declarations actually export.

## 10. Finite and profinite anabelian/GT questions

In SA22 run 1, A6-node-character is a finite quadratic character times the cyclotomic character. A_D gives effective detection of the finite sign; M_H allows arbitrary finite nonabelian splitting fields in the corresponding Frobenius tests. The finite-image recognition and generation results are meaningful improvements for the corresponding finite quotients.

They do not reverse SA22 run 2's recorded refutation of inertia maximality: finite-index inertia subgroups have the same weight. The profinite Ihara/GT kernel remains distinct from a cyclotomic quotient and from rational graded freeness. The supplied external 2026 freeness premise in CC-GT03 is not silently attributed to A_D or M_H. Its full profinite companion R-GTHAT remains separately recorded.

## 11. Complexity and the smaller gates now available

CX-ALG-001/002 keep the historical distinction between Miller's conditional algorithm and the unconditional theorem PRIMES in P. A_D supplies deterministic small nonresidues, square-root extraction and the specifically stated finite-field constructions. It does not by itself produce an arbitrary integer factorization algorithm.

Two refinements make the factoring discussion concrete. CX-ALG-014 refutes the immediate Miller-witness-to-three-gcd shortcut with N=35 and a=2. CX-ALG-015 proves deterministic polynomial-time factorization under A_D when a positive multiple of lcm_(p|N)(p−1) is supplied, with runtime polynomial in both input lengths. Producing that multiple for an arbitrary integer is not part of the promise.

CX-ALG-016 finds a zero fixed-generator resolvent in the literal BIMS17 auxiliary formula, checked against the original page. CX-ALG-017 repairs it by searching a power basis for a nonzero Frobenius eigenprojection. CX-ALG-018 gives a full unconditional even-degree quadratic-nonresidue construction. Thus the nonvanishing defect does not discard the intended finite-field conclusion.

Koiran's HN-in-AM theorem requires number-field zeta inputs, supplied by M_H. The field and input-size bookkeeping is explicit in CX-HN-001/002. A universal replacement by abelian witness fields is refuted by x³−2; the bounded abelian-witness promise remains a valid A_D specialization. CX-GEO-001–003 extend the method to Boolean constructible feasibility, radical membership and reduced-set inclusion/equality. The latter are not claims about scheme-theoretic ideal equality.

CX-GEO-006 handles orbit membership for explicitly given actions. CX-GEO-007 supplies an unconditional PSPACE route for the stated polynomial GL/SL orbit parameterizations, without first constructing orbit-closure equations. CX-GEO-009 isolates a smaller conditional-AM promise: a Laurent degeneration with polynomially bounded pole/precision and syntactic degree. Its coefficient-system reduction charges these bounds in unary. General exponential precision does not satisfy this promise.

The remaining GCT gates are uniform explicit constructions, hitting sets, actual quotient-rank inequalities and the independent hardness hypotheses in their cited theorems. Pure geometry and nonnegative Hilbert data do not replace those inputs. The previous counting theorem E and its ETH consequences remain a separate premise, not a consequence of the two L-function hypotheses.

## 12. The proofs against each other; GL_2 and Artin holomorphy

MT-M01 and MT-M02 are counterexamples to two auxiliary statements in the original Masullo PDF, pages 425 and 426, not merely to the model transcription. An exponential-Schwartz function can have Mellin transform exp(s²)sin(s²), with order-T many zeros in a unit-height window. A nonzero continuous Mellin evaluation also forces its kernel projector to remain a proper projector, so the displayed family of kernel projections cannot tend to the identity in the asserted generality.

The next routes were taken rather than leaving those faults as terminal objections. MT-M03 proves the exact strong limit: the projector onto the common kernel, with complementary projectors tending to the span of the Riesz vectors. NT-Z10/MT-M04 prove the needed O(log(|T|+3)) local zero count for every fixed unitary Hecke character, using polynomial vertical growth and a nonzero Euler-product centre in Jensen's formula. This repairs the arithmetic-divisor count unconditionally. It does not certify the later arbitrary-Schwartz ideal, Schauder-basis, nuclearity or geometric-kernel assertions.

The nonmonomial GL_2 advance is MT-ART01. Conditional on M_H, all odd irreducible two-dimensional finite-image complex Artin representations over Q satisfy GRH, including projective A_5 image. Khare–Wintenberger Corollary 10.2(ii) supplies the already established weight-one modularity and holomorphy; signed Brauer factorization supplies the divisor location. General non-CM positive-weight GL_2 forms are not rank-one Hecke functions over a number field and remain a different gate.

For general Artin functions, MT-ART02 gives an exact finite-dimensional positivity criterion at each divisor point: the local Heilbronn matrix must be positive semidefinite. Stark's multiplicity-at-most-one theorem narrows possible poles, under M_H, to multiple critical zeros. MT-ART04 proves that even all tests from induced one-dimensional characters do not force the needed positivity: an explicit virtual A_5 character passes those tests and has a negative constituent. The supplied exact finite computation verifies the group character calculation; it is not an example of actual Artin L-function orders.

MT-L01/L02 give another exact gate. For the damped Euler products of a nontrivial finite-image Artin representation, one single irrational damping parameter has single-valued meromorphic continuation to Re(s)>1/2 exactly when the original function is holomorphic and zero-free there. The proof uses a normally convergent higher-power correction and the integrality of divisor orders. Rational damping only imposes a divisibility condition. The trivial zeta factor is kept separate. This supplies a sharper continuation formulation; it does not prove the missing continuation or the critical-line positivity.

## 13. Continuing the research

The authoritative current gates are the individual rows of `QUESTIONS.tsv`, mirrored with dated movement in `LEDGER.md`. New archive readings, proof repairs and narrower promises update those rows rather than erasing their provenance. Full GUE, general Artin holomorphy, non-CM GL_2 RH, arbitrary integral inertia splitting and general derandomization remain problems unless the displayed extra inputs are supplied. The record makes no logical-independence claim about them.

# K17-U3-GENERAL — independent whole-proof and certificate audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, archive_kummer.

**Verdict: PASS for the stated complete compact-unitary coefficient spaces and exact Hecke polynomials.** The theorem correctly leaves global arithmetic coverage and any K-group conclusion to separate arguments.

## Reviewed frozen objects and execution scope

The entire 308-line `harmonic_hecke_section.tex` and all 329 lines of `harmonic_hecke_certificate.py` were read. The complete three-prime comparison certificate and its report were also read. The frozen degree records, every polynomial factor, identifying determinants, swap signs, and operator/evaluation shapes were inspected by a separate short standard-library command. That command checked that every identifying evaluation matrix has exactly d rows and d columns, that there are exactly d points, and that all three saved operator matrices have d-by-d shape, including the p=19 record. This is an additional concrete check of the hypotheses needed for the injective-evaluation argument.

The author and root had already executed the complete standalone reconstruction successfully, and the root explicitly requested a proof/code audit without another identical full rerun. This reviewer did not rerun the full generic neighbor-evaluation loop. The reports were read and their input hashes compared to the actual frozen data. The earlier seven-matrix e=6 certificate was independently rerun by this reviewer in the immediately preceding K12 audit.

Reviewed hashes:

| File | SHA256 |
| --- | --- |
| `harmonic_hecke_section.tex` | `897382bfbae06fcfe489d36ba0303b641c2e883610c2ae02fbae070b03d0932d` |
| `harmonic_hecke_certificate.py` | `04caddfd74a771da0d743981b8374cf0affd8f0d405a43d7e1e0675cc2584dee` |
| `harmonic_hecke_exact_data.json` | `30fe1d28f8aa4f1d08da2643cfd7b0429d14ff5d46e4e6e9853262a6ca2cc0b0` |
| `harmonic_hecke_certificate.json` | `d68117a7e47bf4503187535d9b32222ac5c8757981652c75bf012f452466efce` |
| `p19/harmonic_hecke_exact_data.json` | `d22844d0bf56d9c458c33b0d3daa9e44c4662ac8b380c7581f0c1cdef3c8aac7` |
| `p19/harmonic_hecke_certificate.json` | `62628feee65a1185dc812f759c9a7bbe9a0bb828c54f72f59bcfa68bc47cb8ce` |

## 1. Completeness of the coefficient representation

The contraction identity in UG.4 was independently derived from the product rule. For G of bidegree (k-1-j,k-1-j), contraction of R^(j+1)G gives the coefficient (j+1)(2k+1-j), exactly as stated. The displayed recursion cancels consecutive terms and proves surjectivity. The difference of the two polynomial-space dimensions is (k+1)^3. The vector w_1^k z_3^k lies in the kernel and has highest weight (k,0,-k), whose Weyl dimension is also (k+1)^3. Complete reducibility proves that the whole harmonic kernel is the desired irreducible representation.

The class-number-one Hermitian reduction and full stabilizer Gamma=mu_6^3 semidirect S_3 do not depend on k. Their previously checked argument therefore identifies the entire level-K algebraic modular-form space with this harmonic kernel's Gamma-invariants in every stated degree.

## 2. Exhaustive invariants and kernel bases

The action of each diagonal sixth root gives the exact congruence alpha_i-beta_i=0 modulo 6. The independent coordinate compositions enumerate every monomial satisfying both bidegrees, and sorting the three exponent pairs gives precisely simultaneous S_3 orbits. Orbit sums have disjoint supports and form the whole invariant space. In particular the calculation includes exponent differences ±6 in degrees 7, 9, and 11; it does not extend the e=6 equality alpha=beta incorrectly.

The certificate independently expands each orbit's contraction. Every possible resulting monomial is in the enumerated target list because contraction preserves each exponent difference modulo 6. It reads a canonical coefficient and verifies that it is constant throughout the target orbit. Its exact integer elimination computes rank over Q without floating-point arithmetic; row gcd removal changes only a nonzero rational scalar. The saved integral columns have full column rank and are annihilated by the whole contraction matrix. Their counts equal source minus target rank. This proves that they span the complete characteristic-zero harmonic kernel. A saturated integral basis is neither claimed nor required.

The resulting dimensions 3,6,8 and C-swap decompositions (2,1), (4,2), (5,3) are represented in the inspected frozen data and checked by the full certificate. The e=6 one-dimensional control is present as well.

## 3. Actual correspondence and scaling

For every neighbor U, the certificate checks U*U=pI and nonzero rank-one reduction at pi. Integrality of pU^(-1)=U* bounds all elementary-divisor valuations at pi by one; rank one therefore forces (0,1,1). After division by pi, the lattice type is (-1,0,0). Hermitian duality determines the conjugate-prime lattice, and the determinant identity excludes changes at other primes. Thus the complete set of reduced lines is exactly the negative-minuscule right-coset set, not merely a collection of matrices with plausible norms.

The verifier independently checks the whole projective plane: 57 lines at 7, 183 at 13, and 381 at 19. Distinct lines give distinct lattice cosets. It checks every Gram identity and each column's reduction to the claimed line.

For g=U/pi, g^(-1)=U*/bar(pi) and bar(g)^(-1)=U^t/pi. The bidegree (k,k) homogeneity therefore gives p^k rho(g)f=f(U*z,U^tw), precisely UG.7. The sum is the Hecke action on the full invariant space. There is no averaging by Gamma: these are right cosets, each included once. The minuscule Satake scale p in rank three then gives p^(k+1)=p^e times the normalized trace, with the same normalization already checked in the e=6 source and Hecke audits.

## 4. Positive direction, rationality, and integrality

The swap C(z,w)=(w,z) satisfies C rho(g) C=rho(bar(g)). Conjugation exchanges the complete positive and negative coset sets. Hence the characteristic polynomials agree on the entire space, even when the operators are not scalar. Since the chosen harmonic basis has rational coefficients, coefficientwise conjugation gives the same positive operator. In a C-eigenbasis, writing M=M0+omega M1 therefore gives C M0 C=M0-M1 and C M1 C=-M1.

For a same-sign entry, M1=0. For opposite signs, M1=2M0 and the entry is M0*(1+2omega). Multiplying each minus basis vector by delta=1+2omega, with delta^2=-3, transforms the matrix to the recorded rational one: -3M0 in a plus row/minus column and M0 in a minus row/plus column. The certificate checks both identities for every entry.

Formula UG.7 preserves the lattice of invariant harmonic polynomials over the Eisenstein integers. This is a full finite free lattice because it is a finitely generated torsion-free submodule over that PID and contains a characteristic-zero basis after clearing denominators. The scaled operator consequently has characteristic polynomial over the Eisenstein integers. Rationality puts it in Q[X]; the intersection is Z[X]. No integrality assertion is deduced merely from a possibly nonsaturated saved basis.

## 5. Injective evaluation really determines every matrix entry

The identifying points are pairs of independent integer triples, appropriate for the complexified polynomial model. There are exactly d of them for each d-dimensional harmonic space, and each saved d-by-d evaluation determinant is nonzero. The separately executed shape check verified these dimensions for every fixed record.

The scaled Hecke correspondence is already proved to preserve the full harmonic invariant space. Thus the identifying equations A M0=B0 and A M1=B1 uniquely determine its full matrix. The certificate computes each B entry from all actual cosets using exact Eisenstein integer pairs and verifies both matrix equations over exact rational numbers. This is not inference from a few unmotivated test vectors. The two additional points are redundant implementation checks, as the text correctly states.

The standard-library Faddeev–LeVerrier routine computes all characteristic coefficients over exact fractions and checks the terminal Cayley–Hamilton zero matrix. It verifies integrality and multiplies the listed factors back to the complete polynomial. Every factor in UG.10–UG.13 was compared with the frozen records; the signs and long coefficients match. No irreducibility of the factors is used.

## 6. Evaluations and residual-prime scope

The certificate uses exact Horner evaluation at E_(e,p)=1+p^e+p^(2e), then the integer Euclidean algorithm. It checks each claimed gcd against the product of its displayed prime powers and tests every prime by trial division through its integer square root. The inspected data and report give precisely the three factorizations in UG.2.

The complete p19 comparison certificate independently evaluates the three frozen e=10 polynomials and checks their gcd. It has prime factors 2,3,241,1847,9496386083 with exponents 28,26,1,1,1. This removes 43 from the U3-only gcd but preserves the large residual prime. The text correctly draws neither a K-group vanishing conclusion from this U3-only comparison nor a claim of new Vandiver verification. A final arithmetic application must combine the rank-two branch and retain ell different from the chosen auxiliary prime.

## Conclusion of the review

The complete mathematical proof and standalone certificate pass. The complete-space claims, extra invariant monomials, non-scalar direction comparison, integral characteristic-polynomial argument, and exact evaluation identification were all checked independently. The actual full numerical replays by the author and root are recorded separately; this audit does not relabel them as an execution by this reviewer. No mathematical correction is requested.

# Complete source and modular-form check for the alternate field −7

**Date:** 21 November 2026. **Agent/model:** /root/vandiver_k, GPT-6 Astra Pro.
**Effort:** not exposed. **Run:** K17.

## Status and exact scope

The complete texts minus7_source_coverage_section.tex and
gl2_minus7_section.tex have been read back in their entirety and their
arguments independently reconstructed from the stated inputs. The first
text gives the exact GD/source predicates, the U3 local/global transfer,
the necessary rank-two twisting argument, and the pointwise unit criterion.
The second proves the complete 61-dimensional modular-form space, its
integral lattice, and the finite determinant interface.

Self-check verdict: PASS. Independent reviews by root and archive are
separate events and must be recorded from their actual reports. This event
does not itself claim a complete review of the new two-class U3 computation
or a final K32 theorem. The numerical GL2 output was executed by root and
archive; I read both entire programs, the complete archive audit, and the
relevant generated output fields, but did not perform a redundant third run.

## Exact source interface

Fresh full reads:

- HeightAndVanishing/Counts.lean, the entire GD definition and adjacent
  CorG statement. Even N and discriminant coprimality exclude Q(i) from
  this source datum. For E=Q(sqrt−7), N=2, e=16, the source conditions hold.
- SmallClassNumbers/ClassNumberThree.lean, full gd proof: the existing
  source uses Kstar3. The new proof copies the ramification argument with
  prime7; it does not claim that an already-written Kstar7 specialization
  was found in that file.
- NumberU3US.lean, complete actual Adm3U_s, NumberU3U_s, and OneCharU_s
  definitions. The p>=7 and p∤N restrictions belong to the counting
  statement only. The direct OneCharU_s permits geometric Frobenius at2.
- AutNewformW.lean, entire Adm2A definition; Newform.lean, entire
  primitive-newform and attachment definitions; and
  BlochKatoSelmerVanishes.lean, full KillsMu, LevelAway, LevelAt and Level.

The previous complete KeepLevel/Unl/twist and global-packet proof checks are
retained as named dependencies. They were read back together with the new
specialization. The actual weight vector is (15,−1,−17), infinitesimal
character (16,0,−16), and compact highest weight (15,0,−15).

The new local lattice computation at7 was reconstructed explicitly:
choose a²=−5 in Z7, v=(1,2,a), split a hyperbolic plane using 1/2,
and use −d=Norm(det B) to normalize the last line to −1. Thus the full
standard lattice stabilizer is the exact Adler–Lansky one already used
in the previous source audit. Only the principal-series cases are used;
the unrelated q≠7 supercuspidal restriction is not imported.

## Rank-two coverage

KillsMu14 gives arbitrary global mod7 characters. In particular, the
untwisted primitive form is not automatically of conductor7: both inertia
characters can be nontrivial. Tensoring by inverse of one of them gives
inertia 1 plus their ratio. The determinant remains odd, so that ratio
is a nontrivial odd mod7 character. It has tame conductor exponent1.
The coefficient-prime argument uses the already checked full classical
Saito statement and slope gap32, so there is no hidden coefficient-prime
conductor. The twist has primitive conductor7. At2, all six possible
Dirichlet twists take the three values in μ3. This is exactly why the
root program evaluates det(t³−T2³), with t=1+2^32.

The unit criterion is formulated over a common coefficient DVR. It does
not assume that the residual prime splits in E. In fact its residue mod7
is3, so E is inert there.

## Primary modular-form statements and printed proofs actually read

1. Meier–Ozornova, *Rings of modular forms and a splitting of TMF0(7)*,
   Selecta Math.26(2020),article7, published institution copy:
   meier_ozornova_2020.pdf/.txt.
   Full §2 pp7–11 was read: Lemma2.1 and proof (flat base change),
   Lemma2.2 and proof (M1(7)=P1, ω=O2), weight-one E1 formula p8,
   Lemma2.3 complete proof and integral basis pp9–10,
   Proposition2.4 complete conic-ring proof pp10–11,
   Lemma2.6 complete diamond-action proof p11.
   The earlier preliminary version tmf07.pdf was also fully read
   through its Lemma2.5; it has different lemma numbers and is not
   silently cited with published page numbers.
2. Savitt, *An elementary proof of Newman's eta-quotient theorem*,
   author savitt_newman.pdf/.txt: Theorem1.1 and Remark1.2 p2,
   classical transformations §2, the complete §3 proof pp4–7 including
   Proposition3.1 and Theorem3.5, and the complete multiplier-identity
   proof §4 pp7–10 with its Jacobi-symbol appendix pp11–12.
   The application has both congruence sums24, weight3, characterχ−7.
   Determinant-normalized Fricke acts by i. Equal cusp widths1 and7
   in Γ1(7) and Γ0(7) give six simple zeros, with no upper-half-plane
   zeros. Therefore S33=D*M30.
3. The two-page Buzzard weight-one note was read as corroboration.
   Chan–Cooper–Liaw2008 was retrieved as a further primary cross-check
   but its complete paper is not counted as read in this check.

## Integral and computational proof

The exact E1-to-z basis determinant is (28/9)(2ξ−1), a unit away2,3,7.
The invariant quadratic relation is ac=(4/7)b²; it is monic in ac.
Hence the 61 standard monomials give the full weight30 lattice.
D/Q and its inverse are integral formal series, so division by D
preserves the integral Fourier lattice as well as holomorphy.
No rational-only basis is being substituted for an integral lattice.

I read every line of the original
gl2/gl2_minus7_residue_certificate.py as it stood before the announced
extra primality-replay edit. It reconstructs the three blocks and all
Fourier series, solves with unit identifying minors, verifies all
coefficients through80, and compares both cubic and three-twist
determinants. Its result is15133664954664570 modulo25078104767246023.
The actual exact Lucas certification of that prime is a prior check.

I then read every line of the independent 154-line
gl2/gl2_minus7_integral_archive_certificate.py.
It uses integral z-divisor-sum tables, the full cyclic diamond action,
a distinct eta-series multiplication, and Bareiss elimination. The
first61 coefficient matrix has determinant−1; the same full61-space
determinant is obtained. I checked its diamond exponent permutation,
coefficient2^32, precision160→80, and the fraction-free determinant.
The entire accompanying archive audit was read. The full large output
matrix was not printed; it is regenerated by the separately reported
actual archive execution.

Both source and finite-model TeX proofs were then read in full, including
the pointwise unit factors and the two embeddings of Q(ζ6). Their
conclusions do not rely on comparing the source's TrData multiplicities
or on dividing an older oversized characteristic polynomial.

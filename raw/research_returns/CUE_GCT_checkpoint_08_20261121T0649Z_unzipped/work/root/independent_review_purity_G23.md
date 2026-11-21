# Independent whole-proof review of G-23, with its G-22 stability dependency

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run CUE_GCT-20261121-purity.

Actual review completed: 2026-11-21 05:35:25 UTC. Result: **PASS** for the complete mathematical proof. A presentation typo in the no-scaling display (`quad` without a backslash) was reported to the author and corrected before the hash below was captured; it does not affect the argument. The repaired display was inspected.

Files read completely:

- `g23_fragment.tex`, observed SHA256 `4a5790841fd87e4e24d4cca8fc8dab4106dc24b1d9156880aba2792be14c80bd`.
- `g22_fragment.tex`, SHA256 `6b95183839d25a3dc2937478519fa3bbb8451c4a7234f562a15631575f3e8cb2`.
- `work/rectangular/r28_fragment.tex`, SHA256 `36b154bb06c3b0e2ff685d50ba762089ba14c3e30f4ccdca776ecd85df02c8d5`, separately reported in that module.

## G-23 checks

1. The determinant and padded-permanent affine dimensions give exactly `u=(r-2)n^2+r_eta-r^2+3` and `v=r m^2-2m+r+r_eta-r^2+2` after adding the flag dimension and subtracting `r^2-1`. The stated lower bounds ensure both dimensions exceed one. The padding increment is `r-1`, using generic recovery of the irreducible nonlinear factor and the padding line.
2. The ambient dimension is the stated symmetric-power dimension times the Weyl Schur dimension. The action degree is `L=ns+(r-1)e`, because inverse-transpose entries on SL_r have polynomial degree r-1. The independent homogeneous parametrization degree is `p=ns+e`; these two degrees are correctly distinguished.
3. With the stated Derksen inputs, degree(SL_r)=r and dimension=r^2-1 give sigma at most `r L^(r^2-1)`, and the displayed beta is the resulting integer generator bound. It exceeds the auxiliary constant 2 in the usual generator estimate in the stated range. Exactness of invariants transfers the ambient generators to the two quotient domains.
4. The common projectively free stable point and the trivial center exponent `ns-e=r nu_r` rule out scalar orbit periods. Closed-orbit separation then forces gcd one among generator degrees nonzero at this point. The shortest-path residue proof gives a nonzero common invariant in every degree at least beta^2.
5. The bound on the number of generators and the pure-block grouping argument give a standard E-Veronese for `E=r T beta!`; E is at least beta^2. The homogeneous image-degree estimate applies to independent parameter variables at degree pE and the actual projective quotient dimensions u-1 and v-1.
6. The two injections use degrees E+t and 2E-t exactly, giving the displayed all-residue sandwich. I rederived the binomial ratio `k(k+1)(k+2)/(u(k+u)(k+u+1))` and its lower bound k/(4u) for k at least u+1. The proposed threshold gives a strict comparison and the reverse threshold correctly uses the actual dimension v.
7. Standard-Veronese Hilbert asymptotics and the bounded-residue sandwich give an all-integer asymptotic with a positive leading constant and the stated O(j^-1) ratio error. This is not merely an assertion on one arithmetic progression.
8. The no-zero argument is valid: even r makes Delta odd; odd r forces equal parity of m,n and then r=1 mod4; reduction modulo r-2 would make -1 a quadratic residue modulo an integer congruent3 mod4, contradicted by one prime divisor congruent3 mod4. The exact floor/square-root boundary follows since equality is excluded.
9. Substitution of the strict rectangular condition `n<r m/(r-1)` and completion of the square produce a strictly positive lower bound for Delta. The choice `s=r/gcd(n,r)` enumerates precisely the admissible rectangular coordinate degrees. The final scope excludes nonstrict faces, r>m, arbitrary early finite degrees, and an efficient location rule.

## G-22 complete dependency check

I checked all of its Fourier-frame proof: positivity and sum of the mu_i; Fourier orthogonality and full-spark Vandermonde property; the ordered tensor's moment and projective stabilizer, including m=r and padding exponent at least one; and equality of every one-parameter minimum weight before and after multiplication in an integral domain. Thus stability survives symmetrization by the cited Hilbert--Mumford criterion. The Cartan-cone coordinate ring, Segre--Veronese grading, dual-sensitive extraction of j nu, and quotient dimensions agree with the already reviewed G-17 argument.

## Dependency and certification scope

G-21, R-17, R-23, and the previously reviewed G-10/G-11/G-17/G-18 estimates were used as stated inputs. This event does not claim a fresh complete proof audit of Derksen, Mukai, or the Hilbert-function sources, nor a recheck of the earlier large computational certificates. The mathematical arguments written in G-22, G-23, and R-28 were read in full and the new formulas were independently rederived. This is an independent-agent mathematical review, not a formal proof-assistant certificate.

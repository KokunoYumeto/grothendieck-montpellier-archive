# S5 audit and central gate closure

Date: 21 November 2026. Agent: `/root/s5_audit`, GPT-6 Astra Pro. Effort is inherited and not externally exposed. These are working handoff notes; the parent owns the final package.

## State reached

**MA-FQ-004 closes the central gate under the exact hypothesis `(R_B)`: `β=b+n`, hence `k=0`.** Its complete proof is in `modules/s5_crystal_rigidity.tex`, using MA-FQ-001 in `s5_crystal.tex` and MA-FQ-002 in `s5_coset.tex`. All four proofs have passed independent whole-proof readings in this run. The hypothesis `(R_B)` itself is not proved for every extension in the family. The conditional input M supplies it and supplies the additional Hecke zero-location input for all-factor GRH; A alone does not supply those general Hecke premises.

Before the Fourier argument, the successive necessary conditions for a hypothetical positive excess were:

\[
k=\beta-b-n>0,\quad (R_B)
\quad\Longrightarrow\quad
2\le k\le d+e,\qquad k,d,e\in 2\mathbb Z_{\ge0},
\]

where `d = ord L(V⊗η,1/2)` and `e = ord L(X,1/2)` are central orders of two already automorphic and entire Artin factors. Hence nonvanishing of their product at the center closes the comparison. No nonvanishing theorem for that product is claimed.

The earlier positive-excess deduction also gives the following signature for a hypothetical infinite exceptional set:

\[
\sum_{p\le X,p\in\Omega}\frac{\log p}{\sqrt p}\sim \frac{k}{4}\log X,
\qquad \frac{\log\pi_\Omega(X)}{\log X}\to\frac12.
\]

A fixed upper exponent below one-half would also close the gate, but is not needed by MA-FQ-004. The displayed conditional signature is not the unweighted asymptotic `c sqrt(X)/log(X)`.

## Findings and full-proof locations

- **MA-S5-001:** Complete audit of GRH_NIGHT MT-S504, MT-S505, MT-S507 and MT-S508 as used. S508's central equivalence is correct. Two scope corrections matter: Calegari initially compares a density-one set of places, not a cofinite set; equality plus `(R_B)` gives automorphy/holomorphy, while all-factor GRH needs M or further Hecke zero-location inputs. A one-B GRH hypothesis does not give GRH for all other irreducible factors.
- **MA-S5-002:** The automorphic comparison is self-dual by ordinary strong multiplicity one, applied to the two genuinely automorphic representations ϖ and ϖ∨. Its odd degree makes it orthogonal, so Arthur's root-number theorem gives sign +1. Consequently β, b and n are all even, and positive k is at least two and even.
- **MA-S5-003:** Exact character identities `End ξ=1+Vη+W+X` and `W⊗W=1+V+Vη+W+Wη+X`. At the exceptional primes the Rankin trace difference is 8 on odd powers and zero on even powers. Thus the two central Rankin orders satisfy `r4=n+d+e−k` and `r5=r4+c+f`, with bad factors nonzero at the center by finite-image local parameters. This first gives `k≤n+d+e`.
- **MA-S5-006:** The next route improves this to `k≤d+e`. Calegari's symplectic construction gives `Λ²Π⊗ν⁻¹=1⊞ϖ`; therefore the twisted symmetric-square order is `q=r4−n=d+e−k`. Takeda's published Theorem 7.1 makes q nonnegative. The full new deduction is proved and checked; Takeda's terminal proof was read, with the upstream integral/metaplectic theorems retained as classical input, not claimed independently re-proved.
- **MA-S5-004:** Logarithmic differentiation plus a fully written positive-measure Tauberian argument gives the weighted asymptotic and the exact counting exponent one-half.
- **MA-S5-005:** The even integer-order point `(a,b,c,d,x,y,e)=(0,0,0,2,2,0,0)`, `n=0`, `nη=2`, `β=2`, `f=0`, `k=2` satisfies all 43 monomial-cone inequalities and all the new Rankin/symmetric-square constraints. Even meromorphic germs realize the displayed central relations. This is explicitly a formal compatibility witness, not an arithmetic counterexample and not proof that any actual positive k exists.

The complete MA-S5 proofs are in `modules/s5.tex`. They were reread in full after writing on 21 November 2026 and independently reviewed by the parent. The closing argument has three further modules: `s5_crystal.tex` proves the exact gamma equality and atomic positivity after continuous correction; `s5_coset.tex` proves the locally finite coset classification; `s5_crystal_rigidity.tex` proves prime-frequency finiteness and central equality. Root, input_audit and pf26_audit independently read MA-FQ-001 in full. This agent independently read MA-FQ-002--004 in full. The events distinguish these readings from author self-checks.

## Corrections in Calegari's displayed formulas

The theorem conclusions used survive the corrections.

1. Lemma 4.8, publisher-PDF p.13, defines the finite comparison ratio in the inverse polynomial order. For `L_p=P_p(p^-s)^-1`, the ratio `A/L_W` has bad finite factor `P_W/P_ϖ`, as already corrected in GRH_NIGHT S508. The precise ratio is used in the new computations.
2. Lemma 4.6, publisher-PDF p.12, has the sign of the logarithmic asymptotic reversed: the density coefficient is −1/3 multiplying `log(1/(s−1))`. The comparison quotient is nonzero at 1, because the four factors each have exact simple poles; its logarithm is bounded, so the corrected expression still contradicts it.
3. Theorem 4.7's proof, publisher-PDF p.12, has a leading minus sign in front of the logarithm inconsistent with its local Euler coefficients. The correct formula is `log |L(Π×Π∨)/L(End ξ)| = 8 ΣΩ p^-s + O(1)`. The quotient has a nonzero finite limit at 1; this yields convergence of `ΣΩ1/p` by monotone convergence. The printed claim `o(|log(s−1)|^-1)` does not follow from boundedness. The valid density deduction uses `O(1)=o(log(1/(s−1)))`.

These are documented normalization/asymptotic repairs, not a claim that Calegari's comparison theorem is false. No defect in the central S508 equivalence was found.

## Exact finite checks run

The parent-extracted sources were reused, not unpacked again.

- `checks/s5/s5_hecke_cone_recheck.py` re-enumerates the finite subgroup/linear-character data from the prior exact algorithm after removing its exploratory numerical optimizer. It found 156 subgroups, 19 subgroup conjugacy classes and 43 induced-linear vectors.
- `checks/s5/s5_cone_decomposition_verification.py` checked all 43 decompositions in 12 displayed cone generators, plus the four sharpness witnesses, in integer arithmetic. The witnesses have minima `(relative,total)=(4,5)` and `(6,8)` in the two branches.
- `checks/s5/s5_new_certificates.py` checked three representation identities, three exact rational Euler ratios over Q(i), 16 power-trace comparisons, and all 43 tests on the new positive-k witness. The exact symmetric/exterior-square factors were included after the Takeda improvement. All assertions passed.

These are finite exact computations supplementing the proofs. No proof-assistant formalization, arithmetic S5 construction or L-value numerical certification is claimed.

## Primary locators and source-check boundaries

- Calegari (2013), *The Artin conjecture for some S5-extensions*, Math. Ann. 356, 191–207, DOI `10.1007/s00208-012-0839-4`; [author publisher PDF](https://www.math.uchicago.edu/~fcale/papers/S5.pdf). PDF page numbers: Theorem 1.1 p.2; root-number discussion p.3; character table p.4; projective ξ matrix table p.6; Lemma 2.5 pp.6–7; Lemma 4.2 pp.9–10; symplectic exterior-square decomposition p.10; exceptional 4A table p.11; Lemma 4.6 and Theorem 4.7 p.12; Lemma 4.8 pp.13–14; Landau Lemma 4.9 p.14; Lemma 4.10 pp.14–15; final proof of Theorem 1.2 p.15. The attached LaTeX was also read. The required comparison deductions were audited; the deep modularity and functoriality inputs remain cited classical theorems.
- Arthur (2013), *The Endoscopic Classification of Representations*, AMS Colloquium Publications 61, Theorems 1.4.1 and 1.5.3(a),(b). The exact root-number theorem is also stated in the author's [overview](https://www.claymath.org/library/cw/arthur/pdf/arthur-endoscopic-tifr.pdf), Theorem 3(b), p.8. Dalal–Gerbelli-Gauthier, [arXiv:2410.01976v2](https://arxiv.org/html/2410.01976v2), Theorem 3.3.6, explicitly records the trivial-GL1 specialization. The published Arthur theorem is the input; the more recent preprint contributes no new hypothesis. Only the applicable theorem statement was crosschecked here, not Arthur's full monograph proof.
- Cogdell (2004), [author notes](https://people.math.osu.edu/cogdell.1/fields-www.pdf), Theorem 9.2(i), printed p.74/PDF p.78, and Theorem 9.3, printed pp.74–75: Rankin–Selberg holomorphy at the center and ordinary strong multiplicity one. Classical upstream analytic proofs are carried; the exact statements and their scope were read.
- Takeda (2015), *On a certain metaplectic Eisenstein series and the twisted symmetric square L-function*, Math. Z. 281,103–157, DOI `10.1007/s00209-015-1476-x`; [primary preprint](https://arxiv.org/pdf/1506.04791), Theorem 7.1 and entire terminal proof pp.49–50. The terminal proof reduces to Theorem 6.2 plus earlier integral representations. Those earlier classical proofs were not re-refereed. Publication metadata was independently confirmed on [the author's publication list](https://sites.google.com/view/stakeda/publications).
- SGA1, Exposé V, §7, [primary recomposition](https://grothendiecksga.com/read/sga1/fr/V-7.html): finite étale covers versus finite continuous π1-sets. Exact statement read.
- Deligne (1979), *Valeurs de fonctions L et périodes d'intégrales*, Definition 6.1 and §§6.2–6.3; (0.5.3). [Translation](https://mathweb.tifr.res.in/~eghate/Deligne.pdf), PDF pp.20 and4: Artin motives, finite-image rational Galois representations, Hodge type (0,0), induction under restriction of scalars. Exact relevant passages read.
- SGA6 V §§2,7, especially (7.1.1), and the cote1 sheets79–80,111–112 links are carried from GRH_NIGHT MT-ART11/AG-LAMBDA and ALPOGE_BRIDGES BR-TR-01/02. This agent did not reread the scans and does not claim otherwise.

## Approaches tried and their precise limits

1. Root numbers remove odd excess; signs do not exclude even central zeros.
2. The two all-prime factorizations identify k exactly; they do not give the missing central nonvanishing.
3. Ordinary strong multiplicity one is valid for ϖ versus ϖ∨. It cannot compare a merely density-one automorphic/Artin pair as though they agreed cofinitely.
4. The complete monomial cone is insufficient; the k=2 integer-order witness survives it.
5. Rankin–Selberg comparison gives a new upper bound. The next symmetric-square route strictly strengthens that upper bound to d+e but does not prove d=e=0.
6. Exceptional-prime positivity yields a precise square-root exponent. No independent estimate below that exponent was obtained.
7. A degree-zero Selberg-class shortcut would need holomorphy or a finite-pole axiom absent for the actual quotient. No such axiom was assumed.
8. Finite-image local parameters of this nonregular automorphic representation do not, in this argument, construct a compatible global finite-image Galois representation. That would be an additional realization theorem, not a consequence of local boundedness.
9. **MA-S5-007:** An additional isobaric unitary GL10 automorphic realization of the twisted symmetric-square Euler data would close the comparison. The complete proof compares it with `π(Vη) ⊞ π(X)` and uses the exact Rankin–Selberg pole-order square `Σ(m1−m2)²`. Convergence of `ΣΩ1/p` makes the comparison quotient a unit at 1, so that square is zero. This is explicitly a sufficient extra hypothesis, not an asserted functoriality theorem and not an input to MA-S5-001 through006.
10. Farmer–Pitale–Ryan–Schmidt's 2026 analytic multiplicity-one theorem was checked as a possible replacement for this extra automorphy. Its coefficient-distance condition does not apply: the symmetric-square prime coefficients differ by4 on Ω, and its required series `Σ p|Δa_p|²(log p)/p^σ` diverges for `1<σ≤3/2` on the positive-k branch by MA-S5-004. The exact primary locators are arXiv:1305.3972v2, condition(2.20) p.11 and Theorem2.3 p.12. The paper's complete proof was not audited because its hypothesis already fails. Publisher metadata confirms publication27March2026, Math. Proc. Cambridge Philos. Soc.181(1),885–911, DOI10.1017/S0305004126102011. This is a failed particular application, not an impossibility theorem for analytic methods.

11. **MA-FQ-001--004 closes the branch.** The exact real-place descent gives equal gamma kernels. Booker supplies an integer signed divisor supported on the critical line. The finitely many bad-prime progressions have finite total variation by A1 and can be removed from the Fourier side by adding a bounded continuous density on the divisor side. Shrinking convolution squares isolate the atoms, giving `a(t)=-m_R(t)` as an integer positive-definite function on `R_discrete`, with `|a(t)|≤k`. Cohen's theorem and the fully proved dense-coset exclusion make its locally finite support a finite combination of ordinary lattice cosets and singletons. Ordinary Poisson summation then puts all nonzero prime-frequency atoms on finitely many unshifted lattices. Each such lattice contains `log p` for at most one rational prime. Thus Ω is finite and the fully audited S508 criterion gives `k=0`.

The previously proposed central nonvanishing, small central order, and sub-square-root estimate are no longer required. The equality is proved under `(R_B)`, while `(R_B)` itself and the further all-factor GRH premises remain explicitly separate.

## Input classes

The new parity, Rankin, symmetric-square, Tauberian, formal-compatibility and Fourier-rigidity arguments use classical results and their explicit `(R_B)` hypothesis; they use neither A nor M to establish their conditional conclusions. Their four-way input class is `none`, with the ordinary hypotheses retained. Applying MA-FQ-004 by invoking M to supply `(R_B)` has class M. MA-S5-007 remains a conditional implication with an additional, unproved functoriality hypothesis, but that route is no longer needed. The audit of MT-S504/505 records their original M dependence rather than erasing it. An asserted all-factor-GRH conclusion still has class M unless alternative Hecke inputs are supplied.

## Independent trace review follow-up

The entire root-authored `modules/trace_global.tex` was read, with the complete MT-M24, MT-M26 and MT-M30 interfaces used. MA-TR-101's full smooth theta–Möbius isomorphism and finite-Euler norm obstruction pass. MA-TR-102's full triangular representation counterexample passes. The original setup needed a distinction between an open-strip zero distribution and the actual Hilbert quotient trace, especially at boundary zeros; the Mellin paragraph also needed the logarithmic derivative and its convolution orientation stated exactly. These were communicated without editing root's file. The entire revised module was then reread: all corrections are present, and the new MA-TR-103 endpoint-jet proof passes with `2j<s−1`. Six actual review events are in `modules/s5_trace_review_events.tsv`.

For MA-S5-007's pole-order argument, the primary extra nonvanishing locator is Shahidi(1980), *On nonvanishing of L-functions*, Bull. AMS2(3),462–464, theoremp.462, DOI10.1090/S0273-0979-1980-14769-2. The full printed proof outline pp.462–463 was read; its earlier Eisenstein-series/Whittaker theorems remain classical inputs. Cogdell's Theorem9.2 and the partial-factor argument on printedpp.74–75 supply the exact simple poles and unchanged partial pole orders.

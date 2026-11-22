# Effective fixed-tail obstruction: D-AFT01–03 / Q2ct

## Frozen author result

The complete proof is `fixed_tail_section.tex`, SHA-256 **f8440af142bc40afe66df823a0d569f942f782b8acc2eed8d64459347134b817**. The author has read the entire proof and every line of `check_fixed_tail.py`. Mathematical author check: **PASS**. Independent whole-proof review is pending. No compilation is claimed; source delimiter, tag and inner-display checks pass.

For every fixed partition `mu` of size `k >= 3`, the published character polynomial supplies finite rational constants `C,M` and integer `F`. The theorem gives the explicit threshold

`N_mu = ceil max{2k+2, 200, 100/C, 100kM, [100(1+M)]^5, [100(1+M)F^k]^2}`.

For every `n >= N_mu`, the all-target eigenspace estimate `nu >= A I+B` has the full positive constant needed by the actual source argument. A single factor is excluded over every original imaginary quadratic field. All transitive tensor counts at least two are excluded whenever the inducing character field contains a non-Eisenstein imaginary quadratic field. No field-equality assumption is made.

In the main nonsplit problem this forces the tail size of a remaining ordinary alternating family with unbounded `n` to grow. It does not bound `n` for growing tails. The separate standard one-factor case still uses its previously proved split-polarization gate; no broader standard exclusion is inserted into the corollary.

## Proof mechanisms actually established

1. The published umbral polynomial has weighted degree at most `k` and unique ordinary-degree-`k` term `C f^k`, with `C=f^mu/k! > 0`.
2. The explicit `n^(3/5)` split gives a global negative-character bound `b=C n^(k-1)/100`.
3. A moved-letter coefficient estimate, treating zero fixed letters, bounded positive integer fixed letters, and fixed-letter count at least `F` separately, gives `c=a/n-C n^(k-2)/100`. The integrality of the positive fixed-letter count is used explicitly.
4. A sharper monotone defect when many letters remain fixed combines with cyclic averaging and exact Fourier multiplicities to give `A=a/n-101C n^(k-2)/100` and `B=2C n^(k-1)/5`.
5. The actual degree-`n` quotient produces a one-factor excess at least `19C n^(k-1)/25 >= 76`. The marked-scalar/weighted-cycle argument gives the all-count contradiction with explicit margin `79C n^(k-1)/25-2 > 0`.

The cyclic-average method is credited to root HD-AT301. The all-tensor framework is the accepted D-ATT07–09 argument. The new content is the effective universal coefficient estimate and its fixed-tail consequence, not an assertion of independent origin for the shared method.

## Exact supplement and honest chronology

`check_fixed_tail.py`, frozen SHA-256 **fb71d0037906b834c034ae2595929dbdded7fea50bdd247401673c6c4cb479c1**, constructs the polynomials from the published recursive umbral formula for all 63 partitions of sizes three through eight. It checks all 2,048 coefficient monomials, weighted-degree/leading-term assertions, exact threshold arithmetic, 189 independent hook-formula degree matches, the three known tail-three polynomials, and the universal rational margins.

First run passed at **2026-11-22 00:05:21.890435 UTC**, taking **2.687017904 s**. Full author rereading then found only three TeX layout placements: a multi-alignment row needed `aligned` rather than `split`, and two display tags were moved outside their inner environments. These were not mathematical changes or failed mathematical assertions. The initial successful output is retained in `fixed_tail_checked_initial.json`.

The final bound run passed at **2026-11-22 00:05:56.621771 UTC**, taking **2.520020243 s**, and is retained in `fixed_tail_checked.json`. There was no failed computational run. The checker does not enumerate permutations of the enormous threshold degree, certify period rank, or replace the written universal inequalities.

For example, `mu=(4)` has `C=1/24`, `M=192`, `F=769` and

`N_(4)=45553876119348246435500302090000`.

The threshold is intentionally coarse. The finite coefficient sample reaches 135-digit thresholds for some size-eight tails. Effectiveness, rather than numerical optimization, is the new assertion.

## Primary source and access scope

Garsia–Goupil, *Character Polynomials, their q-Analogs and the Kronecker Product*, Electronic Journal of Combinatorics **16**(2) (2009), R19, DOI `10.37236/85`:

<https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i2r19/pdf>

Proposition I.1 and formula (I.5), printed p. 2; recursive Corollary I.1, p. 3; complete invoked proof equations (2.1)–(2.6), pp. 9–11, were read in full during this run and rechecked for this construction. Local source: `sources/GarsiaGoupil2009.pdf`, SHA-256 `f3f9de4eb2d202bb355aa64a479818329f09a5daddbf2fd321915dd2e8f2f0b8`. Extracted text was read; no new visual-rendering claim. The shared bibliography key is `HD:GarsiaGoupil2009`; `fixed_tail_bibitems.tex` deliberately adds no duplicate item.

Ordinary alternating restriction/normalizer and actual Hurwitz quotient interfaces are the previously checked published inputs and accepted project proofs, applied with their hypotheses. No Severn theorem, Markman theorem, 032 proposition, or dimension-only sufficiency premise enters.

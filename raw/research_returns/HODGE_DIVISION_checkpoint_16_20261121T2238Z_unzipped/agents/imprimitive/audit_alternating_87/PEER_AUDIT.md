# Independent whole-proof audit: HD-ALT-06a/b

**Result: PASS.** Actual final audit time: 2026-11-21 20:37:32 UTC. Checker: /root/imprimitive, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION.

## Frozen proof and reviewed dependencies

Complete proof: research/ordinary_alternating_87_section.tex, SHA-256 **5ab4d6447f1b04c0d5c3b52afc5dbaf1a5450cd1d388034d51e3cd68f251cd79**. The complete root checker check_alternating_87.py was also read. The reported earlier display/control-character repairs are already incorporated in this hash; this audit concerns the repaired version.

I reread the full relevant HD-ALT-03a normalizer proof, the content formulas in HD-ALT-03b/04a, the transitive/selfduality and actual-family hypotheses of HD-ALT-04b, and HD-ALT-05a/b's tail estimates. These prior reviewed lemmas are used with their stated boundaries; no hidden extension to spin representations, nontransitive uncovered cores, or arbitrary scalar character fields is made.

## Independent mathematical checks

1. The first row contributes exactly S0 and the remaining contents have nonnegative squares. Since the prior long-row argument gives 0<t≤T, both replacements in t²−3S are in the correct direction.

2. Differentiating N=T²+n(n−1)−3S0 gives the displayed derivative. The estimate T≥n(n−2k−1)/2 follows from the exact difference k(k−1)≥0 for real k≥1. For k<n/4 this is at least n(n−2)/4. The derivative upper bound −n²(n−14)/4+1/2 is strictly negative for n≥15. The first support entry is increasing because n−1−2k>0. Thus the minimum is nondecreasing throughout the required real interval.

3. The long first row prevents a self-conjugate partition. Hence the alternating restriction is irreducible, retains the full Specht degree, and is real with symmetric invariant form. The full normalizer bound transfers to tensor products, while every nontrivial tensor cycle satisfies the included quarter bound.

4. The nontrivial multiplier follows from the actual imaginary character-field inclusion. Two such genuine inertias cost at least e/2 each. The actual intermediate period factorization supplies genus0, at least12 branches, and total moving rank2e+6. This yields exactly δ≤1/10+3/(5e).

5. For c=13/100 the exact limiting constant is δ*=10030839/100000000, strictly above1/10. Both rational comparison identities and the positive expansion at n=15+x check. Since c(1−c)>δ*, all three entries of the minimum are strictly above δ* when k≥cn. The large-n conclusion is the strict ceiling e<60000000/30839<2000.

6. At n≥30 the tail is at least4, so none of the three published small-degree exceptional shapes occurs. The lower bound a≥2n³/27≥2000 contradicts that ceiling. At15≤n≤29 every endpoint exceeds1/9, yielding e<54. The n15,k2 possibilities have degrees90 and91; every other relevant case uses the stated cubic floor≥250. There is no factor-of-two loss at any of these steps.

7. The label(19,3), n22, is a strict witness that this improves the previous six-sevenths region. The theorem correctly leaves longer labels open and does not treat the necessary inequality as sufficient.

## Independent exact reconstruction

Program: independent_check.py. Result: independent_checked.json. Actual **PASS in0.034737581seconds**.

This uses a separately authored sparse Fraction polynomial implementation, not SymPy or the root checker. It reconstructs the derivative, both rational numerator identities, positivity expansion and all constant ceilings. It parses the15 fractions from the frozen TeX and recomputes them from the literal sum of first-row squares.

As a further independent finite check, it enumerates877 Young diagrams in the claimed tail region for15≤n≤40, computes their individual contents and hook products, and checks the exact content inequalities and degree lower bounds. The minimum actual degree in this finite range is90. This finite enumeration is supplemental; the all-n theorem is the written universal proof and its cited precise degree-classification input.

No root arithmetic or selected finite output is imported. The root checker had been read before authoring this independent program, so a blind reconstruction is not claimed.

## Primary source and bibliographic precision

Freshly opened and read the complete invoked passage in the original published MSP PDF:

https://msp.org/tunis/2019/1-3/tunis-v1-n3-p01-p.pdf

Guralnick–Katz–Tiep, *Rigid local systems and alternating groups*, proof of Theorem9.7, printedp312. The proof explicitly invokes Rasala Result3 to deduce that a nonlinear Specht degree below2n³/27 has, up to transpose, one of (n−1,1), (n−2,2), (n−2,1,1). This is a general degree-classification consequence inside the proof; the theorem's separate semisimple-regular element hypothesis is not attached to that consequence.

**Bibliographic correction sent to parent:** the publisher PDF and landing metadata https://msp.org/tunis/2019/1-3/p01.xhtml give article pages **295–320**, not295–323. The landing XML explicitly has citation_firstpage295 and citation_lastpage320. The precise p312 input is unchanged. This is a bibliography correction, not a mathematical repair.

The content-eigenvalue and Specht restriction inputs retain their prior reviewed source status. No new proof of Rasala's classification is claimed. No mathematical defect or required change to the frozen theorem was found.


# Whole-proof review of NX01–NX04

Date: 2026-11-21T04:16:41+01:00 (Europe/Berlin). Reviewer: GPT-6 Astra Pro, inherited reasoning effort (runtime level not exposed), ZETA_NEXT `/root/cm_effectivity`.

**Type:** targeted proof check by complete reading of `normal/findings.tex`, source-locator verification, and explicit checking of the inequalities. This is not claimed as an independent re-proof of Stark or Louboutin, and is not a formal certificate.

**Outcome:** no mathematical gap found in NX01–NX04. Two citation/packaging details below should be corrected when merging.

## NX01

Read the entire proof and its constant setup. Original Stark p141 explicitly ends Lemma4 with c4=2c3. Garcia–Lee, arXiv2007.10313v4 §3 pp16–17, gives c4=2 exp(21/8+c1/2−c2 ψ(1/2)/8), with c1=0 and c2=2/log3. Since ψ(1/2)=−γ−2log2, the draft's C4 is exactly this constant. Its stated rounding C4<43.2 and 4C4<173 is valid. No use of the uncertain c8=π/6 appears. Stark's original Lemma8 p145 was visually read: normal fields use 4 and arbitrary fields 4n!, with descent to a quadratic subfield. The zero-exclusion interval for D≥3 is to the right of 1/2, so the supplied Dirichlet nonvanishing suffices. The class-number-formula normalization is consistent with the CM quotient in NC01.

## NX02: closure exponent and zero persistence

Visually read Stark's original Lemma7 p143: for M=K1⋯Ka it states D_M divides product_i D_Ki^(m/n_i), m=[M:Q]. For conjugates of K all n_i=n and D_Ki=D_K. The Galois closure is the compositum of at most n distinct conjugate fields, so D_L divides D_K^(a m/n) and a m/n≤m≤n!. The exponent m/n is an integer because K embeds into L. The logarithmic discriminant bound and the direction of interval inclusion in NX02 are correct: logD_L≤n!logD_K makes L's zero-exclusion interval at least as wide. Aramata–Brauer zero persistence is applicable because L/K is a finite Galois extension. The proof uses that persistence, and does not improperly compare two residues. If K's wider Lemma4 interval contains a real zero, the narrower exclusion gives exactly the lower bound for its distance from1 used in the proof. If there is no exceptional zero, the artificial β1 gives a still stronger distance. The final CM substitution is correct.

## NX03

Read the complete proof. Louboutin2001 Theorem1(1), printed p1195, supplies the general-degree residue upper bound used, without GRH. The lower signature inequality follows from 2≤sqrt(2π); the upper w_K≤2n² follows from φ(w_K)≤n and φ(t)²≥t/2. The last inequality is immediate prime-power by prime-power: only the 2-adic factor with valuation1 can contribute less than1, and it contributes1/2. Both logarithmic error bounds retain their correct signs. If n/logD→0, the upper term is L*x*log(e/(2x)) with x=(n−1)/L→0; hence dividing by L sends the error to0. The fixed-degree nonnormal correction −log(n!) is correct. This does not assert an arbitrary growing-degree Brauer–Siegel theorem.

**Merge detail:** the bibliography key `Louboutin2001` is not defined in this branch; the same exact source is supplied as `NC-Louboutin2001` in `cm/bibliography.tex`. Replace/alias the key when merging.

## NX04

Read the complete proof. The elementary inequality n!/n^n≤2^(1−n) follows by induction because (n/(n+1))^n≤1/2, and gives the claimed Minkowski factor≤1 for n≥2. Coefficientwise domination ζ_K≤ζ^n is valid at each Euler factor (there are at most n factors and every residue degree is≥1). The divisor-sum induction uses only the harmonic bound and holds for real X≥1. Counting all ideals of norm≤sqrtD therefore bounds the class number as stated. No regulator assumption and no RH enters.

**Locator addition:** cite J. S. Milne, *Algebraic Number Theory*, v3.08 (19 July2020), Theorem4.3, printed p70/PDFp72, for precisely the displayed ideal-class representative bound. Official primary: https://www.jmilne.org/math/CourseNotes/ANT.pdf . Opened and located the theorem in this run. The elementary counting argument is fully supplied in NX04 itself.

## Scope

The arithmetic-to-geometric distinctions in the final paragraph are correct. In particular, no lower bound on h alone is inferred from a lower bound on hR without regulator control; NC01 instead cancels regulators in the relative class formula. Full effective André–Oort algorithms are a separate conclusion from explicit CM orbit lower bounds. The exact 2018 proof's remaining counting/family steps and the known modular-powers replacement are recorded in the added scope paragraph in `cm/findings.tex`.

# MA-MO-020: exact rank-two outgoing polar defect

The complete proof is in `polar_quotient_rank.tex`, equations MA-MO.400–415. Its half-plane premise is exactly MA-MO.320; all polynomial weights s≥0 are allowed. No new zero-location statement is asserted.

## Exact source residues

The actual source functions are r0=Theta(f0)+phi exp(x/2) and r1=Theta(f1)−phi exp(−x/2). Their Mellin transforms are Z MF0−P(z+1/2)/(z+1/2) and Z MF1+P(z−1/2)/(z−1/2), respectively, where P is the transform of phi′ and P(0)=−1. The Gaussian transforms are MF0=(1/2−z)Gamma_R(1/2+z) and MF1=(1/2+z)Gamma_R(1/2+z). The residue at+1/2 in the second formula cancels as+1−1; at−1/2 in the first it cancels as−1+1, using Gamma_R(w)=2/w+O(1) and zeta(0)=−1/2. These are exact source Poisson/Mellin formulas, not informal polar assignments.

For a polar combination c, the entire cleared numerator is E_c(z)=−c0(z−1/2)P(z+1/2)+c1(z+1/2)P(z−1/2). Its values at+1/2 and−1/2 are−c1 and−c0. Thus it cannot vanish identically unless c=0.

## Multiplicities and counting

The stated half-plane premise and the zeta reflection symmetry place every nontrivial zero strictly inside the actual Hilbert strip. MA-WP-001 therefore retains every multiplicity in full, for every s. Membership of Cg(c0r0+c1r1) in J would force Mg·E_c to vanish to each full multiplicity.

For nonzero compact g and nonzero c, that product is a nonzero entire function bounded by C(1+|z|)exp(R|z|). The proof explicitly applies Jensen at a nonzero center and obtains O(T) zeros, counted with multiplicity. It does not replace the divisor by its distinct support.

The incompatibility with the full zeta divisor is proved directly. If that divisor had O(T) zeros, the completed-zeta Hadamard real logarithmic derivative would be O(1) as sigma→infinity: the low-height part is O(1), and dyadic height shells are O(2^(−k)). The explicit gamma logarithmic derivative instead tends to infinity. Its necessary lower bound psi(x)≥log(x−1) follows from the gamma integral and Jensen, so no sharp zero-count estimate or Stirling asymptotic is needed for this last contradiction. The standard order-one growth/Hadamard step is the already checked analytic argument of MA-RB.8–10, specialized to Q and restated with its constant normalization.

Consequently the outgoing C²→H/J map is injective. The raw positive source column has exact quotient rank2 for every nonzero compact smooth g, including tests with g(0)=0 and both polar Mellin values zero. Any correction making its target W+ has rank at least2; orthogonal output correction has exactly that rank. This does not obstruct all possible return maps or relative traces, and it does not undo the full W endomorphism constructed in MO018.

## Source check and proof status

The classical stronger count was checked for corroboration in the author-hosted primary paper: Hasanalizade, E., Shen, Q., & Wong, P.-J. (2022), *Counting zeros of the Riemann zeta function*, Journal of Number Theory235,219–241, DOI10.1016/j.jnt.2021.06.032. Exact locators: Corollary1.2, Eq1.5 p221; completed normalization and argument-principle setup §2, Eqs2.1–2.3 pp222–223. The paper’s numerical theorem is not used by the proof, and no complete reading of its23-page numerical-estimate proof is claimed. The primary PDF is https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf. The completed normalization and reflection were also checked at https://dlmf.nist.gov/25.4, Eqs25.4.3–25.4.4. No copyrighted source copy is included in the deliverable.

The author independently derived the whole argument, read the complete written proof, corrected a stray typographic character before the final version, and then reread the explicit endpoint-residue and counting clarifications. The author whole-proof check passed. Independent root and S5 complete readings have been requested separately; no outside author was contacted.

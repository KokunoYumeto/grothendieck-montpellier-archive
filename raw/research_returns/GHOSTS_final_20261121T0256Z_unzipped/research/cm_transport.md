# CM transport and quantitative specialization audit

Run: GHOSTS, 2026-11-21. Agent: `/root/cm_transport`, inherited GPT-6 Astra Pro model/effort (the API does not expose a more precise effort label). This is a mathematical proof check, not a Lean certificate.

## Sources actually read

* Attached OpenAI 032, *The rational Hodge conjecture for CM abelian varieties*, printed pp. 49–51, Corollaries 8.3–8.4 and Remark 8.5; reference [32], printed p. 52.
* Attached Milne, *On the Hodge, Tate, and standard conjectures for abelian varieties*, §§1.1–1.12, especially §§1.7–1.9; it discusses lifting and cites Kisin–Zhou, Theorem 2.2.7. It does not reproduce the general CM-transport corollary.
* OpenAI [32], *Milne’s rationality conjecture for abelian varieties*, 7 October 2026. The paper is not in the attached ZIP. The official PDF was subsequently downloaded to `work/primary/OpenAI_Milne_rationality_20261007.pdf`; this agent directly extracted and read its printed/PDF pp. 16–17 and 33. Exact locators: common similitude equations (3.15)–(3.16), p. 16; Corollary 3.4 and complete proof, p. 17; the same-dimensional caution, Corollary 6.4 and its complete proof, p. 33. Official URL: <https://github.com/openai/math/blob/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf>. The earlier audit also read the author-source HTML conversion and the official September source `build/sections/02_transport.tex`, labels `prop:transport`, `cor:cm-transport`, `eq:transport-rational-similitude`, and `eq:transport-eta-scaling`. The final locators and numbering here are checked against the October PDF itself.
* Milne, *Abelian Varieties*, corrected 2 January 2022 author version <https://www.jmilne.org/math/xnotes/AVs.pdf>, Corollaries 6.4–6.6 (cube identities and multiplication), Theorem 6.7 (square), Proposition 8.1 (isogenies finite flat), Theorem 8.2 (multiplication degree), §§12 and 15 (endomorphisms and cohomology).
* Deligne, *Variétés abéliennes ordinaires sur un corps fini*, Invent. Math. 8 (1969), 238–243, §§3, 7, 8, read in the translated primary article at <https://translations.thosgood.net/IM-8-1969-238.html>. In particular §3 gives functorial canonical lifts and lifting all endomorphisms, §7 gives the equivalence, and §8 identifies the Hodge decomposition by the positive versus zero p-adic valuations of Frobenius eigenvalues. The translation's terminology “covering” refers to lifting.

## C01. What Remark 8.5 actually uses

This is a source check, not a newly proved CM-transport theorem. OpenAI [32], Corollary 3.4 gives a CM abelian variety B, a positive integer n, a quasi-isogeny a:A_0^n -> B_0 and a rational Hodge class kappa of codimension r such that

    gamma_0 = (a j)^* kappa_0,

where j is the first-factor inclusion. The same equality holds in all prime-to-p realizations and in crystalline cohomology extended to the completed algebraic closure. OpenAI 032 Theorem 1.1 supplies an algebraic representative of kappa. OpenAI [32], Corollary 6.4 then gives the same rational cycle in all realizations. For b=a j, choose m>0 with h=m b an actual homomorphism. If Z represents kappa on B and Z_0 is its specialization, the cycle is

    z_gamma = m^(-2r) h^* Z_0.

The pullback is the refined Chow pullback between smooth varieties. It is not assumed flat or separable. A denominator divisible by p causes no problem with rational Chow groups or rational crystalline cohomology. These are precisely the steps used in Remark 8.5; the independent rationality theorem [32], Theorem 1.1 is not needed for this deduction.

The numerical-equivalence standard conjecture is not what supplies the rational coefficients in this argument. They come from the single rational class and the single rational homomorphism supplied by CM transport. Mere surjectivity of the Q_l-linear Tate cycle map would not by itself supply a rational cycle simultaneously in all realizations.

## C02. Correction of the same-family assertion

The general source does not say that the auxiliary is a same-dimensional CM point of the original special subvariety. In fact dim B=n dim A. Its proof, Proposition 3.1 and Lemma 3.2, enlarges the Hodge datum using a totally real splitting field P and takes W=(V tensor P)^{oplus m}, with n=m[P:Q]. The paragraph after Corollary 6.3 expressly excludes an assertion of a same-dimensional CM lift or a generic-fiber map. Thus the last sentence of sketch 2.6 cannot be quoted as a consequence of Remark 8.5 as written. T9 must either allow these auxiliaries or add a theorem giving transport in the chosen fixed integral Shimura model.

This is a correction of the purported deduction, not a counterexample to the possible existence of a same-family CM lift in a particular good PEL situation. At primes where the original Hodge datum itself satisfies the integral-model and special-point hypotheses, one may run its special-point theorem without the auxiliary enlargement. That extra application and its hypotheses must be checked for the actual family; it is not a consequence of good reduction alone as formulated in the sketch.

## C03. A quantitative pullback bound for actual homomorphisms

### Statement

Let A and B be abelian varieties over an algebraically closed field, of dimensions g and d. Let h:A -> B be a homomorphism, H an ample integral divisor on A, and L a symmetric ample integral divisor on B. Let 0 <= r <= min(g,d), and let Z be an effective codimension-r cycle on B. Write

    deg_H(Y) = H^(g-r) . Y,
    deg_L(Z) = L^(d-r) . Z,
    J_r(h;H,L) = H^(g-r) . (h^*L)^r.

For a translation parameter in a nonempty open subset of B, the refined pullback of the translate of Z is represented by an effective codimension-r cycle Y (possibly zero). Its degree is the exact integer

    deg_H(Y) = deg( Z . h_*(H^(g-r)) ).                    (C03.1)

It satisfies

    deg_H(Y) <= 2^d binom(d,r) J_r(h;H,L) deg_L(Z)/(L^d).  (C03.2)

For 0<r<d, the factor 2^d may be replaced by

    beta(d,r) = d^d/(r^r (d-r)^(d-r)).                    (C03.3)

For r=0 or r=d, the optimal limit of that factor in the argument is 1. These bounds are not asserted to be the optimal geometric pullback bound.

If H and L are very ample and Gamma_h is the graph in the product with its Segre polarization, put

    Delta_h = deg_{H boxplus L}(Gamma_h) = (H+h^*L)^g.

Then

    deg_H(Y) <= beta(d,r) binom(d,r)/binom(g,r)
                 * Delta_h/(L^d) * deg_L(Z),             (C03.4)

using beta=2^d if one wants a single formula without endpoint conventions.

### Full proof

First take an integral component V of Z. Consider

    F:A x V -> B,       F(x,z)=h(x)-z.

If F is not dominant, a general fiber is empty. If it is dominant, generic flatness gives a nonempty open U in B over which it is flat. The fibers then have pure expected dimension g-r; after shrinking U further to remove any unwanted non-flat loci in the finite cycle decomposition, their fundamental cycles are effective. The fiber over y is the scheme-theoretic inverse image h^{-1}(V+y). The Cartesian graph description of refined pullback identifies its fundamental cycle with h^*[V+y] on this open: the flatness over U makes the intersection with the regular embedding of the point y Tor-independent. This construction avoids a false assertion that arbitrary nonflat pullback preserves effectiveness. Apply it to the finitely many components of Z and intersect the open sets. Translation on an abelian variety acts trivially on cycle classes and on numerical classes. Therefore projection formula gives (C03.1).

To estimate its degree, replace H temporarily by a very ample positive multiple H'=eH. Intersect A with g-r sufficiently general members of |H'| and let S be the resulting effective complete intersection cycle, of dimension r. Projection formula, or intersecting the flat family above with these general divisors, shows that the generic length of

    F_S:S x V -> B,       (x,z) -> h(x)-z

is e^(g-r) deg_H(h^*[V+y]). If F_S is not dominant, this number is zero. If dominant, F_S is generically finite because its source and target both have dimension d. Counting scheme-theoretic generic lengths includes inseparable multiplicities. In either case the proper pushforward identity yields

    (L^d) e^(g-r) deg_H(h^*[V+y]) = integral_{S x V}(F_S^*L)^d.  (C03.5)

Set P=pr_S^*(h^*L|S) and Q=pr_V^*(L|V), both nef. On A x B, hence on S x V, the cube identity for the symmetric line bundle L gives

    (h(x)-z)^*L + (h(x)+z)^*L = 2P+2Q

in the numerical divisor group. The second pullback is nef. Thus 2(P+Q)-F_S^*L is nef. The difference of dth powers is a sum of intersections of nef divisors, all nonnegative on the effective projective cycle S x V. Consequently

    integral(F_S^*L)^d <= 2^d integral(P+Q)^d
      = 2^d binom(d,r) (integral_S(h^*L)^r) (integral_V L^(d-r))
      = 2^d binom(d,r) e^(g-r) J_r(h;H,L) deg_L(V).

Combine with (C03.5), divide by e^(g-r)(L^d), and sum with the coefficients of Z. This proves (C03.2) without a smoothness or separability hypothesis on V or h.

For the refinement take positive integers a,b. The same quadratic cube identity gives

    (1+a/b)P + (1+b/a)Q - F_S^*L
       = (ab)^(-1)([a]h(x)+[b]z)^*L,

which is nef. The previous argument replaces 2^d by

    (1+s)^r (1+1/s)^(d-r),       s=a/b>0.

If 0<r<d, its minimum occurs at s=(d-r)/r and is (C03.3). For the endpoints take the limit s->infinity or s->0. Each inequality holds for a positive rational s, so its limit also holds for the fixed intersection number. Finally

    Delta_h = sum_{i=0}^g binom(g,i) H^(g-i)(h^*L)^i
            >= binom(g,r) J_r(h;H,L),

since every mixed intersection is nonnegative. Substitution proves (C03.4). QED.

### Check notes

The strongest delicate point is effectivity for a nonflat h. The proof obtains it from generic flatness of the translation incidence morphism, not from flatness of h. The second delicate point is counting multiplicities; (C03.5) is a proper-pushforward degree identity for a generically finite morphism, and does not discard inseparable degree. The graph bound follows from a nef mixed-intersection expansion, so it does not misuse a reduced-component Bézout inequality for refined intersection multiplicities.

## C04. Quantitative CM-transport certificate

### Statement

Use the notation of C01, and fix a polarization H on A_0 and a symmetric ample L on B_0. Suppose that on B one has

    q kappa = [Z^+] - [Z^-],       q>=1,

with Z^+, Z^- effective of codimension r and L-degree at most D on specialization. Let m>=1 clear b=a j and h=m b. Define

    K_h = beta(d,r) binom(d,r) J_r(h;H,L)/(L^d).

Then t=gamma_0 has an effective difference representative with

    N = q m^(2r),
    deg_H(Y^+), deg_H(Y^-) <= K_h D,

and hence

    c_H(gamma_0) <= max(q m^(2r), ceil(K_h D)).            (C04.1)

The exact pulled-back degrees, rather than their upper bound, are

    D_h^+ = deg(Z_0^+ . h_*H^(g-r)),
    D_h^- = deg(Z_0^- . h_*H^(g-r)).                     (C04.2)

### Proof

Take closures of the finitely many cycles in a projective good model of B after descent to a number field and finite extension at the chosen place. Cycle specialization is effective and preserves the intersection degree with the extending polarization. Apply C03 to the specialized cycles, choosing a translation good for all components. Translation preserves every relevant cohomology class, so

    [Y^+]-[Y^-] = h^*([Z_0^+]-[Z_0^-])
                = q h^* kappa_0
                = q m^(2r) b^*kappa_0
                = q m^(2r) gamma_0.

The cohomological equality [m]^*=m^(2r) follows from H^*(A)=exterior^*H^1(A) and multiplication by m on H^1. C03 provides the degree bounds. This proves (C04.1) and (C04.2). The chosen translated Chow cycles may differ modulo rational equivalence from the untransformed refined pullback; their homological class, which is the invariant under study, is exactly the required one. QED.

This is a concrete sufficient gate for T9: bound q m^(2r) and K_h D simultaneously on infinitely many primes. Controlling the number or density of those primes supplies neither of these two bounds.

## C05. The source's normalization contributes a further visible denominator

In [32], Proposition 3.1, equation (3.15), printed/PDF p. 16, the common rational similitude is

    lambda = (a^*theta_B . theta_*^(d-1))/(theta_*^d).

Equation (3.16) and the following display set kappa=lambda^(-r) eta_B/e, where e=[P:Q]. Suppose lambda=u/v in lowest terms, u,v positive. If q eta_B=[Z^+]-[Z^-], then

    q e u^r kappa = v^r([Z^+]-[Z^-]).

Consequently the certificate in C04 can be taken with

    N = q e u^r m^(2r),
    degrees <= v^r K_h D.                               (C05.1)

This is an algebraic calculation, not an assertion of minimality. Positivity of lambda follows because both theta_* and the rational-isogeny pullback of theta_B are ample rational divisor classes. Denominators can cancel; (C05.1) is an explicit sufficient certificate before cancellation. It displays the four quantitative inputs that must actually be estimated: the cycle on the CM lift, the integral homomorphism denominator, the polarization/similitude normalization, and the geometric size of the homomorphism.

## C06. Transport cost is not an invariant of the prime

### Statement and proof

Assume r>0 and gamma_0 is nonzero. For a fixed prime and a fixed valid pair (b,kappa) with gamma_0=b^*kappa_0, every positive integer M gives another valid pair

    b_M=b/M,       kappa_M=M^(2r) kappa.

Indeed, b_M^*kappa_M=M^(-2r)b^*(M^(2r)kappa)=gamma_0. If Hom(A_0,B_0) is viewed as a lattice in its rationalization, choose an integral coordinate of b that is nonzero. Along primes M avoiding its numerator and the original denominator, the least integral denominator of b/M is divisible by M. Thus even the least denominator of the chosen transport homomorphism is unbounded at this one fixed reduction place, while the intrinsic class and its least cycle complexity are unchanged. Choosing M^(2r)Z as the new CM representative also makes the displayed degrees arbitrarily large.

Even with (b,kappa) fixed, a nonminimal denominator-clearing integer m can be replaced by M m. Then h is replaced by [M]h; both q m^(2r) and the exact degree of each generic translated pullback are multiplied by M^(2r). In the latter assertion use h_M^*=[M]^*h^* on cohomology and the numerical degree formula (C03.1). All formulas remain true if the characteristic divides M.

Therefore the phrase “the degree and the denominator of the transport at p” has no unique numerical value until one fixes a construction and normalization, or takes an explicitly specified minimum over admissible constructions. The intrinsic minimum c_H(gamma_0) is well defined once (A_0,H,gamma_0) are fixed; the cost of a chosen 032/transport construction is only an upper bound. An infimum over CM transport certificates is likewise an upper bound, with no assertion here that all minimal cycle representatives arise by that construction. QED.

### Chow warning

The rule m^(-2r)(mb)^* is independent of m on degree-2r cohomology and on cycles modulo homological equivalence. It need not define an independent-of-m operation on the entire group CH^r: multiplication has different eigenvalues on the nonzero Beauville gradings. The argument needs only a cycle representative with the correct homological class. It must not promote the cohomological scaling identity to all Chow cycles.

## C07. Ordinary reduction permits an identity marking, after algebraicity

### Statement

Let A_0 over an algebraic closure of a finite field be ordinary. Let B be its canonical Serre–Tate lift, viewed over Qbar at the selected place. Assume the rational Hodge conjecture for CM abelian varieties. Every class of a rational algebraic cycle on A_0 is the specialization of a rational Hodge class on B, and of a rational algebraic cycle on B. The same representative works in all prime-to-p and crystalline realizations. Thus, for the class gamma_0 of C01, one may choose the canonical CM lift with the special-fiber homomorphism b=id and m=1. This does not bound the denominator or degree of its characteristic-zero algebraic representative.

### Full proof

Descend A_0 to F_q and enlarge F_q when needed. The canonical lift is functorial and all its endomorphisms lift (Deligne 1969, §3). A maximal commutative semisimple algebra of dimension 2 dim A_0 in the endomorphism algebra therefore lifts, so B is CM. The lift descends to Qbar, as in Deligne's W_0 description. Fix an abstract complex embedding compatible with the chosen p-adic place.

Let pi be the q-power Frobenius endomorphism of A_0 and also its lifted endomorphism of B. It acts rationally on the Betti cohomology of B. Choose M divisible by the orders of all roots of unity among eigenvalues of pi^*/q^r on H^{2r} and of pi^*/q^(g-r) on H^{2g-2r}. These are finite sets. Put

    V_r = ker((pi^*)^M-q^(Mr)) in H^{2r}(B(C),Q),
    V_{g-r} = ker((pi^*)^M-q^(M(g-r))) in H^{2g-2r}(B(C),Q).

After scalar extension these are precisely the geometric Tate subspaces on the special fiber. Frobenius is semisimple on H^1 and hence on its exterior powers, so the pairing between these two spaces is perfect: Poincare duality pairs an eigenvalue alpha in degree 2r with q^g/alpha in degree 2g-2r, and the chosen union of root-of-unity eigenspaces is closed under this pairing.

Every element of V_r is a Hodge class with its twist. To see this explicitly, diagonalize pi on H^1 over a splitting field and then over C. Deligne's §8 says that the H^{1,0} summands are exactly those on which the eigenvalue has positive p-adic valuation; ordinary reduction makes these valuations v(q), while the H^{0,1} summands have valuation zero. An eigenmonomial of degree 2r occurring in V_r has eigenvalue q^r times a root of unity. Its p-adic valuation is r v(q); it therefore contains exactly r factors of each Hodge type. It is of type (r,r). The same proof applies to V_{g-r}. This argument also covers repeated eigenvalues, because the entire eigenspace of a given Frobenius eigenvalue has the same ordinary slope and hence the same indicated Hodge type.

Choose rational bases alpha_i of V_r and beta_j of V_{g-r}. Their pairing matrix G_ij is rational and invertible. By the CM Hodge theorem, all alpha_i and beta_j have rational algebraic representatives on B. Descend those representatives to Qbar by a connected Hilbert parameter space and specialize them to A_0. Their pairings on A_0 remain the entries of G.

Now let z be a rational algebraic cycle on A_0 of codimension r. Its class is Tate, so in every realization it is a linear combination of the specialized alpha_i. The pairing with the specialized algebraic representatives of beta_j is the rational number deg(z . sp(beta_j)). The same rational invertible matrix G determines the coefficients in every realization. Hence the coefficients are one rational vector c_i, independently of the realization. Set kappa=sum c_i alpha_i. A rational algebraic representative of kappa on B specializes to the class of z simultaneously in all the realizations. This proves the statement.

For gamma_0, C01 supplies z. Taking B_0=A_0 with the identity marking removes the homomorphism denominator m. Nevertheless B, its CM type, kappa, and an algebraic representative can all change with the reduction place. No bound on their degrees follows from m=1. QED.

### Checks and limitations

This does not assume that an arbitrary Q_l-linear Tate class is rational in canonical-lift Betti cohomology. Rationality was deduced from rational intersection numbers with a perfect algebraic dual basis. It uses algebraicity of the given local class, already provided by C01. Thus it is a quantitative reformulation of ordinary transport, not an independent proof of Remark 8.5 without CM transport.

## Approaches tried and exact remaining gate

1. Read Remark 8.5 alone: insufficient to audit its missing cited source. Located [32], read Proposition 3.1 and Corollaries 3.4/6.4, and checked the connecting algebra. The Kisin–Zhou special-point theorem is cited background, not re-proved in this agent run.
2. Treat all pullbacks as effective: rejected because h=a j may be nonflat. Repaired by the translation incidence morphism and generic flatness (C03).
3. Apply ordinary reduced-component projective Bézout directly to Gamma_h: rejected as insufficiently sensitive to refined intersection multiplicities and inseparability. Repaired by a group-law degree identity and nef comparison (C03), which then implies a graph-degree estimate.
4. Read T9's raw transport degree/denominator as an invariant of p: refuted by rescaling (C06). The meaningful quantity is a specified construction cost or a constrained minimum.
5. Use canonical ordinary lifts to eliminate transport: succeeds for the rational homomorphism denominator (C07), leaves CM cycle degree and cycle denominator.
6. Expect a large finite-field Tate span to control an integral degree minimum: no such implication. A rational realization span is not a bound on effective representatives or their denominators.

The explicit remaining gate is to obtain, on infinitely many primes, a uniform bound for the pair of quantities on the right side of (C04.1), allowing cancellation or a different better representative. For ordinary primes C07 makes m=1 possible, but leaves q and the representative degree varying. Prime-distribution theorems only select or count primes; a geometric estimate connecting those primes to these quantities is still required. This agent has not proved such an estimate and has not computed the intrinsic minimum for an unspecified polarized Weil fourfold/class.

## Check events (agent-local; merge into main CHECK_EVENTS.tsv)

statement_id	date	who	type	outcome
C01	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	targeted proof check	Read 032 Remark 8.5 and cited transport argument; deduction valid given cited CM transport and CM-Hodge inputs; no Lean verification
OAI001-Cor3.4	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	used and rechecked in this run	Read transport at the connecting-argument level in author-source reproduction and official earlier source; subsequently directly read October PDF p. 17 with the full corollary proof and p. 16 normalization; Kisin-Zhou theorem retained as cited background
OAI001-Cor6.4	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	targeted proof check	Complete proof directly reread in October PDF p. 33; exponent 2r, Chow pullback, descent and realization conventions checked; no flaw found in deduction from stated inputs
OAI032-Thm1.1	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	carried as background without fault found	Used as requested theorem; not independently re-proved
SKETCH-2.6-SAME-FAMILY	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	targeted proof check	The same-family existence statement is not refuted; the claimed inference from the cited corollary is unsupported. Precise replacement C02 allows B of dimension n dim A and records extra same-family hypotheses
C03	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	targeted proof check	Read entire newly written proof; checked flat incidence effectivity, inseparable multiplicities, projection formula, nef expansion, optimization and graph comparison
C04	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	targeted proof check	Read entire proof; specialization degrees and cohomological multiplication exponent checked; explicit bound is sufficient, not minimal
C05	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	computation or formal certificate	Rational scalar calculation checked by substitution; computation only, no formal certificate
C06	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	targeted proof check	Read entire proof; Hom lattice denominator argument and distinction from Chow-level independence checked
DELIGNE1969-SECTIONS3-7-8	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	used and rechecked in this run	Read canonical-lift and slope/Hodge characterizations in translated primary article
MILNE-AV-COR6.4-6.6	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	used and rechecked in this run	Read cube identities and multiplication formula in corrected author version
C07	2026-11-21	GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport	targeted proof check	Read full proof; perfect Frobenius-invariant pairing, slope count, rational coordinates and all-realization compatibility checked

At the original transport checkpoint no archive scan had been supplied to this agent or newly inspected. That initial limitation was later removed by direct reading of cote14 and cote16; see research/archive_reading.md and sections/source_audit.tex for exact scans, folios and the corrected two-letter grouping. No correction of a user-provided Grothendieck transcription is claimed. The initial warning remains valid: exact archive cotes must not be manufactured from thematic proximity.

# Independent audit of the generalized Kummer incidence exclusion

**Mathematical PASS for the stated K2(A) incidence construction, with the source-read scope below.** This is an auxiliary construction exclusion. It neither settles C.4 nor proves that every correspondence factors through K2(A).

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, `/root/cycles_continuation`; effort setting not separately exposed.

Read the entire `../real_weil/C4_KUMMER_INCIDENCE_RESEARCH.md`, SHA256 `c6143e3390a02db1cd1264cb50846519df8640c70bc49e8594d97c596e3c7ae9`, including §§1–8, and the complete successful `kummer_incidence_parity.json`. No program was rerun. The initial failed-coordinate assertion is expressly retained by the owner and is not counted as a successful run.

## Independent reconstruction

The universal incidence U has codimension two in A×K, so its map H2(A)→H2(K) has degree zero. Composition with an integral surface cut and the transpose therefore gives an integral degree-zero correspondence on A. The H1 action factors through H1(K)=0.

The normalized second-cohomology lattice is U³⊕〈−6〉. Its determinant is 6 and its rank is seven. For the symmetric-square pairing with polarized Fujiki factor c=3, diagonalizing the original form gives determinant c^(n(n+1)/2)·2^(n−1)·(n+2)·det(q)^(n+1). Substitution gives 2^14·3^38, independently of the numerical certificate.

Replacing the six pure y-squares by (y²−ey/3)/2 and u1u2 by Q/2 gives a basis change of absolute determinant 2^(−7). The other terms in those replacements only add columns, so they do not alter this determinant. The integral geometric inputs make these actual integral cohomology classes. Their Gram determinant is 3^38, hence the lattice becomes self-dual over Z_(2). For any integral h in H4, its rational orthogonal projection to Sym²H2 pairs integrally with this lattice and therefore belongs to it over Z_(2). This does not require a direct integral orthogonal decomposition of H4, its full saturation, or torsion-freeness of the ambient group.

The Hodge assumptions give precisely the four rational invariant directions ell², ell e, e², Q. To see this, split H2(K)_Q=Q ell⊕Q e⊕T(A)_Q. No T cross term has the required Hodge type, because NS(A)_Q=Q ell. The inverse polarization identifies the invariant line in Sym²T with the scalar endomorphisms of T; End_HS(T_Q)=Q makes this line one-dimensional. The Q direction differs from that inverse-form line only by an ell² term.

I independently expanded ell=u1+2u2 in the enlarged basis. The coefficients are exactly 2a, 8a, a/3+b, 4a/3+2b, −4a, −4a, c, and **8a+2d** in the order printed by the owner. Thus 2a,c,2d lie in Z_(2). In particular the correction of the initial mistaken Q/2 coefficient does not affect the deduction: 8a=4(2a) is already integral at two.

The four Fujiki pairings on T(A) are 12,0,−18,12 times its intersection form. For Q, the three internal hyperbolic contractions give 3q(alpha,beta), and the cross contractions together give q(alpha,beta), before multiplying by three. Therefore the induced scalar is

    s=12a−18c+12d=6(2a)−18c+6(2d)∈2Z_(2).

The correspondence preserves integral H2. A nonzero primitive integral vector of T is also primitive in H2, since T is the integral kernel of pairing with ell; applying scalar s to that vector shows s∈Z. Hence s∈2Z. The algebraic surface Y_p=Q/6 gives s=2, so integer sums and differences realize exactly 2Z. This proves the whole stated incidence exclusion for arbitrary integral Hodge cuts, and therefore for every integral algebraic surface cut.

## Primary-source checks actually made

Freshly read in the retained Kapfer–Menet author v2, *Integral cohomology of the generalized Kummer fourfold*, dated9May2018 on its title page: Corollary4.3 and complete displayed proof; Theorem5.11/formula(24), Proposition5.12 and complete displayed proof, and Notation5.13; all of §§6.4–6.5 through Proposition6.30, including the complete displayed proofs of Propositions6.23–6.25 and6.30 and the intervening corollaries. The retained primary is `sources/kapfer_menet2018_kummer_integral_v2.pdf`, obtained from https://arxiv.org/pdf/1607.03431 , SHA256 `dd2edd1fd2cd425d7d98ea6cc1fec8db68e61fdeb287affcaf8fb6d07f49191f`.

These passages support the exact integral classes used in the argument, the Q/6=Y_p identity, and the 1/2 Nakajima normalization for the incidence map. I did not independently reread the full original Qin–Wang, Beauville or Fujiki proofs in this continuation. They remain the explicitly cited foundational dependencies of those source results; the owner's final published-layout/erratum check is a separate receipt.

The extracted author proof of Proposition6.30 writes a displayed y without the 1/2 present in Notation5.13. This is a source-normalization typography issue to check against the published version, not a change to the owner's formula: the owner correctly uses the normalized incidence map and the stated divisibility proposition. This observation was sent to the owner before this receipt.

Also freshly read in the retained Hassett–Tschinkel author version, *Hodge theory and Lagrangian planes on generalized Kummer fourfolds*, https://www.math.brown.edu/bhassett/papers/hodge/hodge13.pdf : §3 equation(1) with its incidence description, and the explicit §4 W_tau/Y_p calculations from the proof of their three intersection assertions through Theorem4.4 and its displayed proof. These independently cross-check the actual surface Y_p and the pairing scalar two. I did not read all of §4's preceding introduction in this block, and do not claim a fresh complete proof audit of its externally cited excess-intersection or Nakajima foundations.

The Floccari–Varesco paper, the published Kapfer–Menet layout and its erratum were not independently opened by cycles during this receipt. No conclusion about their complete source audit is attributed to this review.

## Scope

The proof controls all integral Hodge surface cuts in the specified incidence factorization on K2(A). It does not classify arbitrary sheaf-moduli constructions, twisted universal kernels, different Kummer dimensions, or arbitrary integral correspondences on A×A. Its parity conclusion is not an algebraicity counterexample or a strictly smaller main existence gate. No main movement is certified.

Completed: 2026-11-19T19:42:41.539287+00:00

## Complete normalization-repair continuation

2026-11-19T19:44:05.804979+00:00: Read the entire revised owner manuscript through its new Section9, SHA256 `10230f84d4277655914cfe2373171f506aae82e7340380f57607c391f4245348`. PASS on the newly added Section3.1, independently reconstructed as follows. Since d is an even multiplication operator, it graded-commutes with G0(gamma). Applying graded Jacobi to q2(eta)=−[[d,q1(1)],q1(eta)] gives two identical q2(gamma eta) terms and hence [G0(gamma),q2(eta)]=2q2(gamma eta). For a=alpha beta with alpha,beta in H1, the two displayed applications have respectively the signs −2q2(a)q1(1)−q2(alpha)q1(beta) and +2q2(alpha)q1(beta)+q2(1)q1(a). Their zero restrictions on K give the factor four identity exactly. Using the correct halves for e and y then gives ey=3rho(q2(a)q1(1)) and y²=rho(q1(a)²q1(1)); the latter uses a²=0 for each displayed decomposable hyperbolic basis vector. Thus B_y is precisely the integral half-difference operator applied to q1(1)|0> and pulled back. There is no remaining normalization or graded-sign gap in this derivation.

In this continuation I freshly read the complete Qin–Wang author-v2 Sections3.1–3.2 and4.1–4.2, printed pp.5–11, including all displayed proofs of Lemmas3.2–3.4, Proposition3.5, Lemma3.6, Lemmas4.1,4.3,4.4 and Theorem4.5. I also read the preceding Stability Theorem2.1 statement, whose original Li–Qin–Wang proof is an explicit external dependency. Primary retained file: sources/qin_wang2005_integral_operators_v2.pdf; https://arxiv.org/pdf/math/0405600 ; SHA256 aa0d713c0e382cdb7a738421066aa20495bdbc33d5677b93cc44bc7b33a12dd1. Its m_(1,1)=(p1²−p2)/2 convention supplies exactly the needed operator. The prior complete Kapfer–Menet Corollary4.3 read supplies extension to non-Hodge integral classes on a torus.

I also freshly read the published Kapfer–Menet Section3 operator definitions and graded commutator equations(3.1)–(3.4), pp.530–531; Lemma4.1 and Corollary4.3 with full displayed proof, pp.532–533; the statement and delta normalization of Proposition4.4, p.533; and the complete statement/proof of Proposition5.3, p.535. The latter identifies the degree-one multiplication classes with summation pullbacks, so their restrictions on the fixed zero-sum fibre are literally zero. I did not reread all of Proposition4.4's duality proof or the complete published article. No new claim about the erratum, external monodromy foundations, original Beauville/Fujiki theory, Lehn's formula, Nakajima's symmetric-function geometry, or the original stability theorem is implied. The exact owner/source scopes remain explicit.

The geometric normalization condition of the initial receipt is now resolved at this source-chain scope. The entire new argument remains an auxiliary construction exclusion and supplies no main-gate movement. No certificate was rerun.

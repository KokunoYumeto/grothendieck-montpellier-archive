# Bounded primary-source audit: the selected quadratic Eisenstein symbol

Reviewer: /root/lean_chain, GPT-6 Astra Pro; effort not exposed.

**Outcome:** this bounded search located no theorem that supplies a unit
for the selected quadratic-twist coefficient in the present setting.
This is a scoped search result, not a claim that no such theorem exists.
No new arithmetic exclusion or auxiliary-field existence is inferred.

## Exact target

Fix p≥31, p≡3 mod 4, b=(p+3)/2, and k=b+3=(p+9)/2. At a prime
q≡1 mod p, take the already checked stabilization
E=G_k−q^(k−1)G_k(qz). For an odd negative fundamental D, prime to pq
and with χ_D(q)=−1, the selected X²Y^(k−4) coefficient is, in the
fixed normalization,

−15/8 · β_3(χ_D)β_b(χ_D) modulo p.

Thus the missing assertion concerns a single D for which both factors
are units. The relevant L-value is L(E,χ_D,3). Since k≥20, its argument
3 is not the central point k/2. A theorem about the nonzero full symbol,
an unspecified critical value, or one half-integral coefficient does not
by itself supply this assertion.

## Exact source boundaries

### Heumann–Vatsal

Theorem 5.1, printed pp. 747–748, applies to our integral Eisenstein
symbol: the cusp constants are divisible by p and p>k. Its complete
proof was read. It chooses characters of growing odd prime-power
conductor whose wild part has growing prime-power order, and concludes
nonvanishing using j=0. These characters are not quadratic.

Corollary 4.7 supplies the already verified coefficient formula for
quadratic characters, but does not assert that a selected quadratic
coefficient is a unit. Theorem 5.2 transfers congruences; it does not
supply the missing quadratic unit.

Primary: Journal de Théorie des Nombres de Bordeaux 26 (2014),
709–756, DOI 10.5802/jtnb.886, author/journal PDF already retained at
main_gate/literature/jacobi_simultaneous/Heumann_Vatsal_2014.pdf.

### Bruinier and the BJKOSV survey

The BJKOSV survey's Theorem 4′, p. 14, is Bruinier's Theorem 1.
The primary author paper requires the residue prime to be prime to
the auxiliary Legendre prime times one less than that prime. Thus one
cannot impose its Legendre condition at our auxiliary q≡1 mod p.
This is a failure of that application, not an obstruction to choosing
another auxiliary prime.

More fundamentally, Bruinier's Theorems 2–4 concern one half-integral
weight Hecke eigenform and its coefficients, with an explicit
eigenvalue exceptional set. They do not concern the same-D product
above. Corollary 7 of the survey / Theorem 6 of the primary paper gives
individual Dirichlet values, stated for even index and positive D.
The primary's ensuing odd-index remark still concerns one value.

No half-integral weight eigenform with fundamental coefficients equal
to the required product has been established here. The genus-six trace
does give that product, but is not the half-integral eigenform required
by these theorems.

Primary: Bruinier, Duke Mathematical Journal 98 (1999), 595–611,
author PDF https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/bruinier/publikationen/fcmodl.pdf .
Exact statements read: author pp. 6, 10–13; survey pp. 6–7, 13–14.
No whole-proof audit of Bruinier's foundational paper is claimed.

### Ahlgren–Boylan

Theorem 1.1 in the author version dated 29 June 2005 concerns central
quadratic values of a cuspidal newform of even weight and odd squarefree
level. It propagates a minimum valuation when that minimum is attained
for two distinct discriminants satisfying its local conditions. It
does not prove that the minimum is zero in our prescribed
normalization, and does not concern the noncentral Eisenstein value.

The full theorem statement and its hypotheses were read in the primary
web retrieval, author p. 2. A subsequent direct PDF download returned
503, and subsequent web opens returned 502; no local PDF or whole-paper
proof review is claimed.

Primary: https://people.math.sc.edu/boylan/reprints/THETAFINALNEW.pdf .

### A recent spanning theorem

Kayath–Lane–Neifeld–Ni–Xue, Theorem 1.2, gives spanning sets of complex
level-one cusp spaces defined using already nonzero central twisted
values. Its Proposition 2.4 proof, read completely on pp. 7–8, uses
the invertibility over C of the selected central L-values to recover
coefficients from period relations. It does not assert saturation of
an integral lattice at p. It also varies a range of periods, rather
than selecting our j=2 coefficient.

A nonzero complex multiplier can be divisible by p. Therefore this
proof cannot be reduced modulo p to obtain the required detection
without an additional integral result.

Primary: Canadian Journal of Mathematics, published online 3 October
2025, DOI 10.4153/S0008414X25101697. Exact Definition 1.2, Theorem
1.2, Proposition 2.2 and Proposition 2.4 with full latter proofs were
read. The remaining foundational results were not audited.

### Vatsal's earlier quadratic application

The precise quadratic nonvanishing application in Theorem 0.3 of
Canonical Periods and Congruence Formulae is for elliptic curves with
rational three-torsion, ordinary reduction at 3, and squarefree
conductor. Its modular-symbol congruences and its use of Washington
also do not provide the present arbitrary fixed p, higher weight,
selected noncentral coefficient. Exact Theorem 0.3 and the relevant
Eisenstein nondivisibility discussion on author pp. 3 and 14 were read.
No whole-paper reproof is claimed.

Primary: https://personal.math.ubc.ca/~vatsal/research/bah.PDF .

## Remaining precise requirement

One would need a theorem proving that the selected quadratic
evaluation functionals, with their stated parity and local conditions,
detect this particular nonzero integral Eisenstein-symbol class modulo
p. Equivalently for this fixed class, one must prove a unit value of
the same-D Bernoulli product above. Nonzero complex spanning, the
unrestricted-character nonvanishing theorem, and separate
indivisibility statements for each factor leave that requirement open.

The bounded search used both web search systems and the primary
papers listed above. It did not inspect or duplicate the parallel
Byeon/Kimura or explicit D± field-construction work. No new finite
degree job, O(p) scan, or numerical verifier was started.

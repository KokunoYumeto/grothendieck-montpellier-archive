# Independent review of the root GRH transfer lemmas

Reviewer: GPT-6 Astra Pro, agent /root/eth_consequences; effort inherited and not exposed. Run CX_GRH-20261121. Date: 2026-11-21 Europe/Berlin / 2026-11-20 UTC.

## Material read in full

The entire file work/root_premises.md was read, including its scope caveats. The two supplied Lean interface files were independently reread. Relevant Masullo text was checked directly in the extracted PDF text at Chapter 1 §1.2, Chapter 3 §3.2.1, and Chapter 13 §13.3.1. The final numbered GRH theorem heading in Chapter 13 is indeed unfilled; the root correctly invokes the introductory draft claim M rather than representing that heading as a proved, stated theorem.

These are **independent re-proofs of the elementary transfer lemmas**, not independent proofs of Alpöge, Masullo, global class field theory, or analytic continuation.

## CX-R01: independent derivation

### Abelian fields

Let \(K/\mathbb Q\) be finite abelian of degree \(d\), with group \(G\). Invoke the standard abelian reciprocity identification of the complex characters of \(G\) with primitive Dirichlet characters of conductors dividing a cyclotomic conductor for \(K\).

For a rational prime \(p\), let \(I_p\subseteq G\) be inertia, of order \(e\), and let \(F_p\) be Frobenius in \(G/I_p\), of order \(f\). There are \(g=d/(ef)\) primes of \(K\) above \(p\), each with norm \(p^f\). Characters not trivial on \(I_p\) have local factor 1. The remaining characters are the character group of \(G/I_p\). Their values on \(F_p\) run through the \(f\)-th roots of unity, each \(g\) times. Hence the product of their inverse local Euler factors is

\[
\prod_{\chi\in \widehat{G/I_p}}(1-\chi(F_p)p^{-s})
=\prod_{\omega^f=1}(1-\omega p^{-s})^g
=(1-p^{-fs})^g.
\]

Its reciprocal is exactly the local Euler factor of \(\zeta_K\). Primitive associated Dirichlet characters are essential here: merely using imprimitive characters at one common modulus would delete valid factors at primes dividing that modulus.

Taking products in \(\Re(s)>1\), where they converge absolutely, and then meromorphically continuing, yields

\[
\zeta_K(s)=\prod_{\chi\in\widehat G}L(s,\chi).
\]

At any \(s\) in the open strip \(0<\Re(s)<1\) off the central line, all the factors are finite and nonzero by \(A_D\). The one trivial factor has its sole pole at 1, outside that strip. The product is therefore nonzero. This independently proves the claimed Dedekind RH transfer. The proof is valid for every abelian field, including every subfield of a cyclotomic field.

Supporting source checked in this review: Andrew V. Sutherland, MIT 18.785, Lecture 19 (15 November 2021), Theorem 19.15, printed p.11, gives the exact primitive-character factorization; §19.3 specifies the character convention. URL:

https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec19.pdf

Web refs: turn715340481view0, turn703041392view0, turn703041392view1. The new transfer proof does not require reproducing this established factorization in the final paper.

### The Masullo conditional transfer

For an arbitrary number field \(K\), take the trivial idele class character. It is continuous, unitary, finite order, and unramified at every finite place. Its finite Hecke Euler product is exactly
\[
L_f(s,1)=\prod_{\mathfrak p}(1-N\mathfrak p^{-s})^{-1}
=\zeta_K(s).
\]
The completed function differs by a nonvanishing exponential factor and products of \(\Gamma(s/2)\) and \(\Gamma(s)\). These gamma functions have no poles or zeros in the open strip. Thus zeros of the finite and completed functions coincide there, with multiplicity. The draft claim M forces those zeros onto the central line.

For a finite-order ray-class character, the associated idele class character is unitary. Primitive Hecke L-functions therefore fall directly within M. If the algorithm uses an imprimitive ray-class Euler product, its ratio to the primitive L-function is a finite product of factors \(1-\alpha N\mathfrak p^{-s}\), with \(|\alpha|=1\). Their zeros have real part zero, so the open-strip conclusion is unchanged.

This proves the root's assertions. The finite-Hecke definition has the particularly useful exact locator **Masullo Definition 3.2.1.4, pp.123–124**, complementing Definition 3.2.1.2 and Proposition 3.2.1.3. The root's qualified comment on Brauer induction is correct: meromorphic expressions in Hecke L-functions do not prove Artin holomorphy on the critical line. No such extension is needed for these transfers.

**Verdict CX-R01:** passed independent re-proof. No gap found in the stated elementary deductions. The conditional status of M must remain visible.

## CX-R02: independent derivation and a recommended strengthening

The cubic \(x^3-2\) is Eisenstein at 2. Its discriminant is \(-108\), not a rational square. Its splitting field consequently has Galois group \(S_3\), and the representation on the three embeddings of \(K=\mathbb Q(\sqrt[3]2)\) is the standard permutation representation \(\rho\).

For a direct character check, the representation has trace 3 at the identity, trace 1 at a transposition, and trace 0 at a three-cycle. Every rank-one representation of \(S_3\) kills \(A_3=[S_3,S_3]\), so a virtual integral sum of rank-one representations has equal trace at the identity and a three-cycle. This contradicts the traces of \(\rho\). Thus \([\rho]\) is not in the subgroup of \(K_0(\operatorname{Rep}_{\mathbb Q_\ell}S_3)\) generated by rank-one objects.

The root's stated “equivalently” sentence is true, but its current proof only explicitly discusses rank-one representations that factor through this same \(S_3\) quotient. To exclude arbitrary Dirichlet/cyclotomic rank-one \(G_\mathbb Q\)-representations, add the following one-paragraph argument.

Choose \(u,v\in G_\mathbb Q\) mapping to the transpositions \((12),(23)\) in \(S_3\). Their commutator \(c=[u,v]\) maps to a three-cycle. Every rank-one character \(\chi\) of \(G_\mathbb Q\), whether or not it factors through \(S_3\), satisfies \(\chi(c)=1=\chi(1)\). The character of any virtual integral sum of rank-one representations therefore has equal values at \(c\) and 1. The permutation representation has values 0 and 3 there, respectively. Equality in the Grothendieck group would force equality of these traces, an impossibility. This proves the stronger assertion for arbitrary rank-one local systems.

This argument uses only additivity of trace in exact sequences; it does not need semisimplicity of an infinite-image category. It also avoids any issue about \(\mathbb Q_\ell\) containing all finite character values.

**Verdict CX-R02:** the finite-\(S_3\) statement passed independent re-proof as written. The broader local-system formulation passes after the displayed commutator justification; recommend incorporating it. The conclusion refutes a proposed representation-theoretic factorization route. It does not establish logical independence of \(A_D\) and the RH of this cubic field, nor rule out analytic reductions.

## Event entries for the root ledger

| statement_id | type | outcome |
|---|---|---|
| CX-R01 | independent re-proof | Full root proof read; factorization independently checked prime by prime, including inertia and primitive characters; strip-zero transfer and trivial-Hecke specialization re-proved; passed. |
| CX-R02 | independent re-proof | Full root proof read; traces re-computed; finite-quotient obstruction passed. Supplied independent commutator proof covering all rank-one \(G_\mathbb Q\) characters and recommended adding it to justify the broader formulation. |
| E-REVIEW-SUTHERLAND-19.15 | used and rechecked in this run | Located exact primitive-character factorization and convention; source used as established background. |

No computation or formal certificate event is claimed. Date/model/run attribution is as at the head of this file.

## Full review of the Koiran/GCT component

The complete file work/koiran_gct.md was subsequently read, including all eight new proofs and its source/scope tables. The corresponding attached GCT V source was reread at Theorems 2.8, 2.10, 3.4, 4.10, Definition 5.1, and Theorem 5.5. Koiran's DIMACS §2 and author erratum were inspected. This is a targeted full-proof check; no independent reproof of the height estimates or the analytic prime-ideal theorem is claimed.

### CX-K01

The root-field specialization is valid. Applying the effective Chebotarev theorem to E/E requires only RH for \(\zeta_E\), even if E/Q is nonnormal. The integral-element replacement formula is correct: if the leading coefficient of R is c and its degree is d, then \(c^{d-1}R(T/c)\) is monic and annihilates cθ. Its height remains at the singly exponential logarithmic scale required.

The subtraction of residue-degree-at-least-two primes is bounded by \(d\pi_{\mathbb Q}(\sqrt x)\); no hypothesis on RH over Q is needed for this elementary bound. Dividing the remaining prime-ideal count by d safely bounds the number of underlying rational primes. Removing primes dividing denominators and the index costs at most the stated degree times their number. Choosing a sufficiently large polynomial exponent in \(x=2^{P(N)}\) overcomes every singly exponential error parameter, so the polynomial bit-length of the random primes is preserved. The final arbitrary-field example establishes the range of fields in the proof, without pretending to establish logical necessity of H_D.

**Verdict:** passed targeted full-proof check.

### CX-K02 and CX-K03

The gate-variable encoding is parsimonious and has polynomially many degree-at-most-two equations; rational constants are handled correctly by nonzero integer denominators. The equation \(\sum_i u_i x_i=1\) is equivalent to the nonzero-point condition. AM is preserved by the deterministic reduction. The containment direction is **AM⊆Π₂**, and its complement is in Σ₂; there is no mistaken AM⊆Σ₂ assertion.

The abelian-witness promise in CX-K03 has the needed quantitative bounds explicitly built into the yes-side. Its protocol does not need to recognize or certify the witness field: the analytic promise is used in the completeness proof only. Its no-side uses Koiran's unconditional bad-prime bound. This is a legitimate promise-AM consequence and avoids an otherwise unwarranted claim that some abelian solution automatically enjoys Koiran's quantitative height bounds.

**Verdict:** both passed targeted full-proof check.

### CX-K04

The Eisenstein/nonnormality argument is valid for each of the three conjugate root fields. Every subfield of an abelian Galois extension is Galois. Therefore no such root can lie in an abelian extension. This counterexample addresses exactly the proposed abelian-solution replacement.

**Verdict:** passed targeted full-proof check.

### CX-K05

The source supplies a polynomial bit bound for the coefficients of successful linear forms. Once that bound is fixed, Good belongs to Σ₂ by CX-K02. Existentially guessing a candidate extending a prefix merges with the first Σ₂ block. Thus both minimization over cardinalities and bitwise recovery use polynomially many queries to a single Σ₂ predicate, proving FP^{Σ₂}, without an extra alternation.

The minimum successful cardinality equals the Krull dimension. Homogeneity places the proposed parameters in the vertex maximal ideal, including on each component of maximal dimension; the usual principal-ideal dimension bound therefore applies. For d=0 the empty set is correct. The finite-module proof by graded induction is sound, including nilpotents. Finiteness gives equality of dimensions, which forces algebraic independence for d generators. Field extension is faithfully flat and preserves the required statements. Enumeration in polynomial space also gives the asserted unconditional functional PSPACE bound.

**Verdict:** passed targeted full-proof check. As customary, the input size must count the declared ambient variables; if an encoding were allowed to declare exponentially many unused variables using only a binary count, the polynomial output statement would require an additional succinct-output convention. The cited standard specification does not introduce that unusual convention.

### CX-K06

The exponential-length oracle conversion preserves a fixed number of alternations. The s.s.o.p. proof correctly uses the exponential-size existential system from GCT V Theorem 2.8 and does not assume access to a small defining ideal. The h.s.o.p. statement correctly retains the independent exponential-time-equations premise from Theorem 5.5.

One wording repair was recommended: Definition 5.1 permits mixed positive weights, whereas CX-K05 is a standard-graded linear-form refinement. Therefore do not simply apply CX-K05 to a mixed-weight presentation. The safe existing-result transfer is to cite GCT V Theorem 5.5 itself and substitute H_M⇒H_D into its Koiran calls. Alternatively, add an explicit weighted reduction using common-degree powers and the same bounded-coefficient resultant argument. The author was notified; the mathematical statement is not invalidated.

**Verdict:** statement and main transfer pass; the cited standard-grading shortcut should be clarified as above before final integration.

### CX-K07

The existing unconditional border-hitting-set theorem composes with the deterministic transformation to succinct separating systems using polynomial space. The result is a small system with permitted cardinality slack. The proof does not inadvertently assert optimal cardinality or verification of every candidate. The historical comparison therefore follows from the exact cited results.

**Verdict:** passed targeted full-proof check, with FS18/GSS19 treated as cited theorems rather than independently re-proved.

### CX-K08

The affine-scheme, closed-point, localization, Frobenius-permutation, and finite-morphism dictionaries preserve the earlier proofs. The incidence projection is closed because Proj R is proper, and so successful matrices form an open parameter locus. The spread-out argument clears a finite set of coefficients in integral-dependence relations and works after one localization; it does not claim flatness.

Two precision edits were recommended. First, choose B to absorb the primitive-element index and use \(U=\operatorname{Spec}\mathbb Z[1/(B D_E\ell)]\), or explicitly restrict the Frobenius/weight statement to p≠ℓ and separately exclude index primes for the polynomial-root identification. Second, write the map to \(\mathbb P^{d-1}\) only for d≥1; for d=0, Proj R is empty. These are straightforward repairs, sent to the author and coordinator.

**Verdict:** passed targeted full-proof check after those explicit domain qualifiers.

### Event entries

All events below have reviewer/model/run attribution as at the beginning of this report and date 2026-11-21 Europe/Berlin (2026-11-20 UTC).

| statement_id | type | outcome |
|---|---|---|
| CX-K01 | targeted proof check | Complete proof read; root-field specialization, height scale, prime-ideal subtraction, bad primes and polynomial bit-length checked; passed. |
| CX-K02 | targeted proof check | Complete proof read; gate encoding and nonzero-point equivalence checked; AM/Π₂/complement directions correct. |
| CX-K03 | targeted proof check | Complete proof read; bounded abelian-witness promise and completeness/soundness roles correct. |
| CX-K04 | targeted proof check | Complete proof read; nonnormal cubic cannot be a subfield of an abelian extension; passed. |
| CX-K05 | targeted proof check | Complete proof read; FP^{Σ₂} prefix search, dimension minimization and graded finite-module criterion checked; passed. |
| CX-K06 | targeted proof check | Complete proof read; exp-equations gate retained; recommended direct use of cited weighted Theorem5.5 instead of unproved application of standard-graded K05. |
| CX-K07 | targeted proof check | Complete composition proof read; correct existing unconditional PSPACE scope; passed. |
| CX-K08 | targeted proof check | Complete dictionary proof read; recommended invert ℓ, absorb primitive-element index, and restrict projective map to d≥1. |

### Confirmation of revised Koiran/GCT component

At 2026-11-20 23:13 UTC, the revised CX-K05, CX-K06 and CX-K08 passages were reread. They now explicitly encode t≤N, cite GCT V Theorem5.5 directly in the varying-weight case, absorb the primitive-element index in B, invert ℓ, and treat d=0 separately in Proj. All recommended precision changes are present and pass the check.

Reviewed file SHA-256: 4e445ba51acab46be0af294485dc079a663c3123bcaf51cef92b675104a55459 (work/koiran_gct.md).

The revised CX-R02 paragraph was also reread at this time. It now contains the absolute-Galois commutator argument; the stronger assertion about arbitrary cyclotomic rank-one local systems therefore passes as written. Reviewed root-premises SHA-256: 4c3aa180cc4b213d472506a02e6d2fc0502be760d952254e0f9b28910976efa5.


## Full review of the separate geometric part

All six complete proofs in work/root_geometry.md were read, and their elementary algebraic, representation-theoretic, and geometric steps were reconstructed. This event is an independent-agent targeted proof check, not a reproof of FGA representability, class field theory, or the foundational étale equivalence. Primary historical locator verification belongs to the root agent; it was not independently repeated during this mathematical review.

- **CX-G01:** The geometric generic fiber is the embedding set, and its permutation matrices split into Frobenius cycles. For each f-cycle, det(1−tF)=1−t^f, so the reciprocal factors are exactly the unramified Dedekind factors. Fixed points count residue-degree-one primes. Character decomposition is available in the abelian case. The absolute-Galois commutator argument in CX-R02 survives passage to K_0 because trace is additive. No missing nonabelian analytic premise is erased. Passed.
- **CX-G02:** The derivative r t^(r−1) is a unit since r and t are units. The algebra of roots of t^r−a is finite étale, with μ_r acting simply transitively after an étale extension. The absence of a section is precisely the power-nonresidue assertion. For a squarefree algebra, CRT idempotents select factors and inverse images of component ideals recover their monic polynomials. These constructions do not supply the cost of finding idempotents. Passed.
- **CX-G03:** Fractional ideals and rank-one locally free modules correspond by a generic-fiber basis; isomorphisms are scalar multiplication. Tensor products, factor-base relations, and unit kernels agree. The original notation Spec H_K would have been incorrect for a finite cover; the corrected Spec O_(H_K) is finite étale over Spec O_K. Passed after that correction.
- **CX-G04:** Contraction makes the integral coordinate algebra a torsion-free subgroup of the rational one. Every finitely generated torsion-free abelian subgroup is free, so the filtered-union argument establishes flatness. The cone ideal is homogeneous; every graded piece is finite free. On each Proj chart, homogeneous localization is flat over Z and its degree-zero summand is a direct summand, hence flat. Graded fiber dimensions, and therefore the eventual Hilbert polynomial, are constant. The coaction vanishes on the contracted ideal because the target is torsion free and vanishes after tensoring with Q. Thus the integral group action and projective flat family exist. None of this identifies every special fiber with the orbit closure formed anew in that characteristic or computes equations efficiently. Passed.
- **CX-G05:** Exterior powers of a trivial rank-N bundle give the binomial polynomial, and its reduced class is literally zero. Young-idempotent images are projective summands only when the denominators defining those idempotents are invertible. I corrected the base condition to a Q-scheme or inversion of d!, rather than the potentially misleading phrase characteristic-zero ring. Integral Jacobi–Trudi operations on K_0 remain well-defined as formal λ-ring operations. The trivial and sign characters of C_2 have equal rank but unequal trace, proving the claimed rank-map failure. Passed after the base-condition clarification.
- **CX-G06:** Finite monodromy makes Frobenius eigenvalues roots of unity; tensor, exterior-power, and stable-summand operations preserve this. It supplies pointwise weights, without an analytic continuation or critical-strip argument. For Boolean fibers I corrected the cohomology statement to geometric étale cohomology over Fbar_q; arithmetic cohomology of Spec F_q need not be concentrated in degree zero. With that qualifier, the stated H^0, zeta function, and unit Artin motive follow component by component. Passed.

All three fixes were read in their final context. No unresolved mathematical gap was found in these six stated proofs. No formal certificate is claimed.

## Final ETH TeX check

The complete CX-E01–CX-E06 proofs in eth_consequences.tex and CX-E07–CX-E08 proofs in eth_geometry.tex were read after conversion. The TeX preserves the fixed-width quantifiers, polynomial input-size factor, fixed-density speedup, direction of reductions, numerical-versus-symbolic distinction, and exact Boolean circuit lower-bound quantifiers. The E01–E06 geometric restatement table is now included. For general parsimonious reductions it asserts equal ranks/isomorphism classes, while a specified witness bijection gives an actual component identification; for gate encodings the polynomial evaluation inverse proves the canonical projection is an isomorphism. The variable-count polynomial bound in E02 is explicitly part of its standard encoding hypothesis. The final E06 comparison includes the required determinant/border model qualifier suggested by the independent reviewer. All proofs passed this targeted author check.

Check timestamp: 2026-11-21 00:23:08 Europe/Berlin (2026-11-20 23:23:08 UTC).

- eth_consequences.tex: SHA-256 5fe8e9bafe7ed1d5ac437c0209562ea5241584dad287e4eae364a3a0e8cd1914
- eth_geometry.tex: SHA-256 f05fa2de13ce3da9b59409eba6e7d4f825cfe84a0e90f883997b99b9b0db6e62
- eth_bibliography.tex: SHA-256 4e7dfee4e4fc8009f50f83c1521009a43ba0ceb74e1f68106b40248c7ffc6c84
- root_geometry.md: SHA-256 de893efae6320ad21d16b79d18506c48341ed58805ecff9c7f035189fab3493d


## Additional CX-N09 prime-field automorphism result

At 2026-11-21 00:29:25 Europe/Berlin (2026-11-20 23:29:25 UTC), the complete proof in number_automorphism_gate.tex was read after drafting. SHA-256: 138a3d9495932b2247c631eff172b76919d05e136d4b4ce884792173c4dc9df5.

The proof passes: the order is recovered from lcm(1,...,d) with polynomial bit complexity; a prime-order permutation has an r-cycle and hence a nonzero primitive-root eigenspace over F_p; a singular eigenvector is already a zero divisor. Otherwise c=z^r is an r-th power in the fixed split algebra because its coordinate value is an r-th power separately on every orbit. The root algorithm stays in that split F_p algebra. Its primitive r^e-th root constant is obtained from the same prime-field nonresidue, without factoring the complement of the r-part of p−1. The product of the r nonzero factors z−zeta^j y vanishes, so at least one is a nonunit, detectable by multiplication-matrix singularity. The gcd then produces a proper polynomial factor. This author check is not a formal certificate. The number_algorithms agent was asked to perform an independent full read.

Primary source reads: Gao author PDF, https://www.math.clemson.edu/~sgao/papers/FacPoly.pdf, Section2.4 and Lemma2.6 pp7–9 (entire construction and proof), and Lemma3.6 p16 (statement only, cited Ronyai proof not supplied there). Web refs turn357429503view1, turn981272148view1, turn633382592view0. IKRS ECCC TR08-099, https://eccc.weizmann.ac.il/report/2008/099/download/, Section4.1 cyclotomic algebra definition, Lemma4.5 p16 full proof, Proposition4.6 pp16–17 statement; web refs turn514789830view4 and turn561015599view1.

The broader D-only gate remains unresolved in this audit. A further source chain was traced: BIMS2017 Corollary5.7 invokes BGL2001 Theorem2 and Adleman–Lenstra1986. The latter author PDF https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1986a/art.pdf, AlgorithmA Step2 and Proposition3, printedp351, demands a small q congruent to1 mod n with p inert in the degree-n cyclotomic subfield. Its proof invokes a variant of Bach–Shallit FOCS1985 Theorem2. This is an exact unresolved dependency, not a claim that D alone cannot suffice. The AMS full Bach–Shallit1989 PDF returned403, so its proof was not read.


Final E01/E02 clarification check at 2026-11-21 00:32:02 Europe/Berlin (2026-11-20 23:32:02 UTC): sparsification branch overhead, forced-zero padding, counting partition requirement, fixed-epsilon uniformity, polynomial-exponent overhead, and sufficient FPT parameter bound were read after insertion and passed. These are conditional reduction calculations, not a new sparsification theorem. Revised eth_consequences.tex SHA-256 24cf6f1bc65a3c66d7feeb526ebbaf5a446f4bfbb3aa8a67acf54bca858bb61f.

Williams exact-premise check at 2026-11-21 00:32:49 Europe/Berlin (2026-11-20 23:32:49 UTC): E03 now displays 2^n poly(n^a)/q(n) with q superpolynomial, every fixed a, and deterministic or co-nondeterministic algorithms, matching the author Theorem1.1 printedp2. The existing substitution proof remains unchanged. Revised eth_consequences.tex SHA-256 cc591bd403b99ae870d9e82e5948d52ed7478d96d03133bc0f16daae50f8cf77.


## Final expanded CX-N14 proof review (2026-11-21 00:43:01 Europe/Berlin (2026-11-20 23:43:01 UTC))

Read the complete final assembled `number_automorphism_gate.tex` end to end and reconstructed all newly derived cases. Passed: (i) characteristic-order enumeration; (ii) Dirichlet-only prime-field nonresidue, eigenvector and invariant radical; (iii) unconditional valuation-one cyclotomic/Teichmueller argument; explicit moved-ideal semiregularity; and the sufficient extra coefficient-Teichmueller unit input for the remaining branch. Full polynomial gcd recovery is included. Read all of IKRS Lemma 4.2 and Proposition 4.6 proofs: the descended zero divisor lies in A itself. This is an author targeted proof check, not an independent-agent review or formal certificate. Model GPT-6 Astra Pro; inherited effort not exposed. Final SHA-256 d5a59eab2facbb85a52d588416aad4aa7e5088e5ffc13472a8a463e70cee67d8.

Final refinement 2026-11-21 00:44:45 Europe/Berlin (2026-11-20 23:44:45 UTC): case (i) broadened to p<=d, independently noticed by root, with no automorphism needed. Read complete proof again; all steps pass. Final SHA-256 33cfd978e655cad476cbe10ae07c2b7d5aa165ea13ed67959ed9c19446ad2ff6. Number-algorithms agent independently read the whole final proof and original IKRS Lemma 4.2 and Proposition 4.6, reporting pass; their actual event is in number_check_events.tsv.

N14 shortcut counterexample 2026-11-21 00:45:48 Europe/Berlin (2026-11-20 23:45:48 UTC): added complete checked p=17,r=3,d=3 proof, as requested by root after independent check. It invalidates only the deduction that the guaranteed eigenunit and zeta must generate a noncyclic group when valuation exceeds one; not an impossibility result. Latest SHA-256 e01b02a84156fed3b02044a49af17ca6f44ad877c1c1931648d5daf7b44ecb4b.


## CX-N15 final full composition proof (2026-11-21 00:53:41 Europe/Berlin (2026-11-20 23:53:41 UTC))

Read the complete final proof end to end and reconstructed every original composition step. The primary interfaces are AL86 Algorithm A with N11 auxiliary-prime bound, BGL Theorem 2 with every auxiliary irreducible supplied, Lenstra explicit basis/structure-constant input, and IKRS Main Theorem plus Lemma 4.2/Proposition 4.6. The final proof uses Frobenius-equivariant interpolation, not the longer CRT/projector development draft. Generic maximum-order coefficient units handle all r, including s=1 and r=2, so its stated sufficient zeta family does not conceal a separate Dirichlet-character assumption. The direct prime-field Frobenius-fixed algebra reduces arbitrary Fq input, and recursion preserves the quasipolynomial degree bound. Passed; no formal certificate. Final SHA-256 5d433a8c0319e8a06c591f10d0ba52740e6bbb8564fd0646f078a1ef06cef247.
Also independently read and reconstructed the complete N11 algebraic/discriminant/Frobenius argument now used as a premise. Passed; its cited analytic bound remains a checked source theorem rather than a new reproof.

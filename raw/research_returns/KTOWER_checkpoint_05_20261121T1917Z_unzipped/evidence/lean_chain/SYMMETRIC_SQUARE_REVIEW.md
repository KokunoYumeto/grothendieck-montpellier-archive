# Independent symmetric-square, dual-Hecke, and Bernoulli review

Date: 2026-11-21 UTC. Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.

## Verdict

**PASS for the constructed symmetric-square subspace and its exact polynomial factor.** I read all of `unitary_audit/symmetric_square_results.tex`, its entire `symmetric_square_check.py`, the entire imported `gl2_uniform.py`, and the original complete `gl2_uniform_section.tex`. The earlier independent review of `check_spectral_split.py` supplies its small polynomial helpers. I also read the complete new `dual_hecke_results.tex` and `check_dual_hecke.py`, and root's entire `main_gate/lower_bernoulli_certificate.py`.

Fresh executions reproduce all 30 symmetric-square decompositions, every saved lower classical matrix and coefficient array, and every residual gcd. The dual calculation reproduces all nine parity-rank checks and the primitive common kernels. The standard-library Bernoulli replay is byte-identical to root's report. These are separately recorded computational events, rather than consequences inferred from the theorem's status.

## 1. Lower weights and the exact number of lines

The graded-ring basis argument uses only the integer parameter n and does not require n even. The generators have weights1,3,6, the cusp generator begins with q, and the second generator begins with q; consequently the basis remains integral and unitriangular. For n=1,2 its index set is empty. The CM condition is divisibility of the infinity exponent2n by6, and is likewise independent of the parity of n.

Setting n=e/2 gives lower weight e+1, dimension floor((e−2)/3), and one CM line precisely when6 divides e. Twisting by the primitive quadratic character preserves conductor one at3: the inertia characters1 and epsilon are interchanged and monodromy is zero. Away from3 the twist is unramified. A fixed point is CM, so the remaining forms have two-element twist orbits. Their number is exactly floor((e−2)/6).

## 2. Published lifting and fiber scope

I checked Gelbart–Jacquet Theorem9.3, printed p.534, with its no-nontrivial-self-twist hypothesis. Definition3.1.3 and the complete local arguments of Propositions3.2–3.3, pp.485–489, identify the determinant-one, self-dual adjoint lift; (3.3.6) is the principal-series formula used here. Section3.7 treats self-twists. I have not reconstructed the paper's full global converse-theorem proof.

For Arthur–Clozel I read Chapter3, Theorem3.1 and its entire proof at p.201, Theorem4.2(a),(d) at p.202, Definition1.2 at p.199, and the complete Theorem5.1 proof at pp.212–213. These give the required prime-cyclic cusp lifting, twist fibers, and all-place compatibility. The p.202 symbols were confirmed in the rendered primary PDF.

I read Ramakrishnan Theorem4.1.2 and its entire printed proof, including Lemma4.1.4, pp.90–93. Equal adjoints of unitary cuspidal GL2 representations force a character twist; equal central characters make the twist quadratic. The theorem's general Rankin–Selberg input remains imported background.

Primary sources and local copies:

- Gelbart–Jacquet: <https://www.math.columbia.edu/~hj/Forms%20on%20GL%282%29%20and%20GL%283%29.pdf>, `primary/gelbart_jacquet_1978.pdf/.txt`.
- Arthur–Clozel: <https://www.math.toronto.edu/arthur/pdf/30.pdf>, `primary/arthur_clozel_base_change.pdf/.txt`; printed p.202 is PDF page218.
- Ramakrishnan: the primary manuscript `unitary_audit/primary/ramakrishnan_2000.pdf/.txt`, corresponding to arXiv:math/0007203 and the published Annals152 (2000),45–111 article.

## 3. Application to the proposed subspace

For a non-CM lower form, a nontrivial self-twist would be quadratic by its central character and would make it dihedral, contradicting non-CM. Its adjoint is therefore cuspidal, self-dual and has central character one. A quadratic self-twist of this GL3 representation is impossible: it would multiply that central character by epsilon cubed, which is nontrivial. Its quadratic base change is consequently cuspidal. The same central-character calculation removes the nontrivial twist from the base-change fiber comparison of two such adjoints.

At3 the original two-dimensional inertia is1 plus epsilon with zero monodromy. Its adjoint inertia is1 plus two copies of epsilon, so restriction to E3 is trivial and monodromy remains zero. All other finite places were already unramified. The complex adjoint characters have exponents(e,0,−e), hence the required compact coefficient weight(e−1,0,1−e). The positive conjugate-dual parity and simple-generic packet multiplicity checks are the same already audited ones in the compact coverage theorem. No extension beyond their pure-inner generic scope occurs.

If the resulting two base changes coincide, the preceding fiber comparison makes the rational adjoints coincide. The corresponding lower forms then differ by a quadratic character unramified outside3. Only1 and epsilon are available. This proves exactly the two-element fibers used in the dimension formula, including possible Galois-conjugate eigenforms. The unique finite fixed lines and global multiplicity one give exactly one compact line per orbit.

This proves a constructed subspace of the stable spectrum. It does not classify every adjoint origin over E. Its members cannot be removed from the rank-three source comparison merely because their construction uses classical forms.

## 4. Eigenvalues and exact code semantics

At a split p, write the lower roots as alpha,beta with alpha*beta=p^e. The adjoint roots are alpha/beta,1,beta/alpha. Multiplication by p^e gives the scaled eigenvalue a_p^2−p^e. Inverting the multiset does not change it, so the opposite minuscule direction has the same value. This verifies the weight shift and both directions.

After removing the CM factor, the lower polynomial is the square of the twist-orbit polynomial. The already reviewed exact integer square-root routine reconstructs every coefficient and verifies the complete product. The new companion matrix has subdiagonal ones and final column −h_n,...,−h_1, so its characteristic polynomial is exactly h. The characteristic polynomial of C_h squared minus p^e times the identity is therefore the displayed resultant. Exact monic division into the stable polynomial and exact comparison-value multiplication check every coefficient of the claimed remainder.

The fresh replay covers every e=2,4,...,30 and p=7,13. At e=26,28,30 the constructed dimensions are4 and the remaining stable dimensions are72,92,112. All lower matrices and result objects agree with the author's report; only runtime fields and the hash of my relocated prior spectral report differ. Hashes and the full equality result are saved in `symmetric_square_reconciliation.json`.

For each of these three e, the smaller residual modulus divides the symmetric-square comparison at both primes and is coprime to both remaining stable comparisons. Each larger residual modulus is coprime to both stable factors at both primes. These are exact gcd statements over the displayed integers, independent of their primality.

## 5. The opposite minuscule matrices

The complete dual-Hecke proof passes. Swapping the polynomial variable sets is a linear involution C with C rho(g) C=rho(bar(g)). Its action interchanges the two coset sets. In the rational harmonic basis, the opposite matrix is also the coefficient conjugate, yielding M1=0 on equal parities and M1=2M0 on unequal parities. The diagonal change of basis with entries1 and delta=1+2omega gives precisely the saved rational matrix R. Since this change commutes with C, the opposite matrix in that same basis is CRC.

The identities hold before reduction. Delta is a unit away from3; no identification of a residue prime with its conjugate is required. The common kernel of both directions is C-invariant. When2 is a unit it splits into plus and minus parts, and the opposite equation on a parity vector follows from the first equation. Stacking only the first-direction matrices within each parity is therefore the exact simultaneous test.

The elimination program uses only unit row operations. A zero residual tail after its unit pivots gives a genuine identity block and free kernel over the composite residue ring; nonzero tails are labeled inconclusive. Every produced free vector is checked directly in each required matrix. The fresh replay gives plus ranks44/44,55/55,65/65 and minus ranks39/40,49/50,59/60 for e=26,28,30, at7 alone,13 alone, and jointly. Each joint minus vector has a coordinate1 and survives all four matrices, hence remains nonzero at every prime divisor of the modulus.

## 6. Independent exact Bernoulli check

Root's complete standard-library script uses the defining ordinary Bernoulli recurrence and the full conductor-three polynomial sum. I independently executed a byte-identical copy. Its report is byte-identical, SHA256 `73264db20a2fdf589ba306e9a0f11da138bd57960a33a23e0752f777f35b280f`. It proves:

| e | B_(e+1,chi_-3)/(e+1) | smaller modulus |
|---:|---:|---:|
|26|80907883885186609178/81|697446897311|
|28|−516454004244279410402/3|323026426255399|
|30|102431533589014497766094/3|236017358500033404991|

Each modulus divides the numerator and is coprime to6, the denominator, and1−2^e. The already reviewed Fretwell–Roberts sufficient theorem therefore applies at every prime divisor; it has no ell>weight requirement. The inert-prime residue excludes CM. This supplies the arithmetic conditions needed for an all-prime stable-congruence corollary via the proved adjoint injection, without factoring a modulus. The script's additional e=32,34,36 special values are exact discovery targets only; they do not certify full compact residual support or new K-group vanishing.

The new arithmetic corollary should be distinguished from the finite two-prime kernel test: the latter alone does not imply a global residual eigensystem. All actual source predicates remain separate in either case. No Lean kernel run, full new harmonic-operator reconstruction, or general functoriality proof is claimed.

## Final Eisenstein corollary and refreshed certificate

Whole-read the appended KT-U3-SYM2-EISENSTEIN corollary and its consequence paragraph. PASS: FR Theorem 3.6 applies with N=3, M=1, k=e+1, psi=1, phi=epsilon, and only ell>3; the inert-prime-two exclusion (or absence of CM when 6 does not divide e) ensures non-CM. The residual adjoint filtration gives the same three Eisenstein characters over the entire absolute Galois group of E, and the already checked symmetric-square construction supplies an actual stable compact system. The three exact normalized Bernoulli values, modulus divisibility, and combined denominator/6/inert-residue gcds were independently recomputed with Fraction arithmetic. This is an ambient stable conclusion; the new ordinary admissibility question is reviewed separately.

The author added only denominator/6/combined exception-gcd fields and assertions to the final polynomial certificate. Its entire change was read and a new complete 30-pair replay passed at 2026-11-21T16:49:54Z. Final script SHA256: `8f5842654d0f363aa1ddf0c2bc42c525b77b1ac0bf9b341280b37f5c042f40a0`; author report SHA256: `1cbe9d27760cb8030bac929e0385983b9892a4265de62154a87fc16234f1557d`. Exact reconciliation is in `symmetric_square_reconciliation.json`.

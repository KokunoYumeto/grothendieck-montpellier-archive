# Ordinary Milnor elements, completion, and the remaining B.1 gate

Status: the source statements below are opened and checked in the indicated scope. The extension in Section 3 has a complete proof independently read and passed by root and agent D; both also independently checked the exact primary weight and torsion-freeness statements. It is integrated as `prop:B-Milnor-divisible-kernel`. It is not a proof of the B.1 invariant-colimit vanishing and is not counted as qualifying movement.

## 1. Exactly what the current sources give

Schreieder, *Remarks on Milnor K-theory and Tate's conjecture for divisors*, author version dated 23 November 2024, published online in *Commentarii Mathematici Helvetici* on 9 March 2026, DOI 10.4171/CMH/615, proves the following.

- Theorem 2.2 and Corollary 2.3, pp. 6–7, distinguish ordinary generic continuous cohomology, defined as the filtered colimit over finite-type opens, from its adic completion. The integral generic continuous groups over a field containing all prime-power roots of unity are torsion-free.
- Lemma 4.1, pp. 11–12, says that an ordinary Milnor element whose every codimension-one residue is infinitely ell-divisible is itself infinitely ell-divisible when its degree is one or two, or when the corresponding finite-coefficient unramified group vanishes.
- Theorem 4.2 and Lemma 4.3, pp. 12–15, construct a countable free permutation-submodule model for the completion in degree two, and in degree three with the specified unramified vanishing hypothesis.

Primary URL: <https://www.iag.uni-hannover.de/fileadmin/iag/homepages/schreieder/publications/Milnor_K-theory_and_Tate.pdf>. The complete degree-two comparison chain in Lemmas 3.1–3.2, Proposition 3.3 and Theorems 3.4–3.5 has also been read. The paper does not assert the analogous ordinary invariant-to-completion injectivity in the degree required for B.1.

Colliot-Thélène and Schreieder, *Divisibility phenomena in motivic Bloch–Ogus theory*, arXiv:2605.22494v1, title-page date 22 May 2026, supply two different kinds of input.

- Proposition 3.7, p. 16, proves that for a smooth projective variety over a finite field, the refined unramified group
  \[
  H^i_{j,\mathrm{nr}}(\overline X,\mathbf Q_\ell(n))
  \]
  has weights in
  \[
  [i-2n,\max(i-2n,2i-2n-2j-2)].
  \]
  Its definition in (2.7)–(2.8), p. 11, is an image between ordinary filtered colimits over opens, not a completed generic-field group. The full definition and proof were read.
- Theorem 6.1 and its proof, pp. 27–29, concern the image of an integral Bloch–Ogus group in an inverse limit of finite-coefficient groups. In the proper case, the image for degree-zero and degree-one Zariski cohomology of the Milnor sheaf is torsion. Lemma 6.2 and (6.2)–(6.4) construct the compatible continuous cycle maps. These complete passages were read.
- Appendix B, Theorem B.1 and Lemma B.2, pp. 32–33, prove ell-divisibility of the ell-primary torsion subgroup of field Milnor K-theory when all ell-power roots of unity are present. The complete proof and the following alternative proof of Theorem 1.1 were read.

Primary URL: <https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/CTSchreieder21May26.pdf>. The main theorem's entire external dependency chain has not been independently reproved.

## 2. Why the inverse-limit statements alone do not correct residues

There is a genuine distinction between an ordinary integral Milnor element with zero residues and one whose residues are merely infinitely ell-divisible. The former is covered by the new unramified divisibility theorem. Passing from the latter to the former would require correcting the residues by an ordinary Milnor element; this is a Gersten cohomology issue.

Agent D independently supplied the following exact abstract-complex check. Let
\[
C^0=\mathbf Z,\qquad C^1=\mathbf Z[1/\ell],\qquad d:C^0\hookrightarrow C^1,
\qquad C^2=0.
\]
Then \(H^0(C)=0\), \(H^1(C)=\mathbf Z[1/\ell]/\mathbf Z\) is divisible, both terms have zero ell-primary torsion, and \(H^1(C/\ell^r)=0\) for every \(r\). Thus the degree-one map to the inverse limit of reductions is zero. Nevertheless, \(1\in C^0\) is not infinitely ell-divisible, although its residue \(1\in C^1\) is. The undetected obstruction is a Tate module of \(H^1(C)\), rather than its adic completion.

This is a formal counterexample to an inference from those statements alone. It is not a geometric counterexample and does not preclude using the additional weight theorem.

## 3. Proposed additional geometric argument

Let \(k=\overline{\mathbf F}_p\), let \(K/k\) be a finitely generated field extension, and let \(\ell\ne p\). For any model \(X\) of \(K\), write
\[
H^n_\eta(K,\mathbf Z_\ell(n))
=\varinjlim_{\varnothing\ne U\subset X}H^n_{\mathrm{cont}}(U,\mathbf Z_\ell(n)).
\]
The ordinary integral regulator
\[
\rho_n:K_n^M(K)\longrightarrow H^n_\eta(K,\mathbf Z_\ell(n))
\]
is obtained from the usual compatible cycle map, or from products of Kummer classes after restricting symbols to a common finite-type open. It commutes with residues, finite-extension restriction and transfer, and reduction modulo \(\ell^r\). Its reduction is the norm-residue isomorphism on the field. All these constructions are made before taking the filtered colimit; no exchange of completion and colimit is used.

### Proved intermediate lemma

For every \(n\ge0\),
\[
\ker\rho_n=\bigcap_{r\ge1}\ell^rK_n^M(K).
\tag{M1}
\]
Moreover, for \(n\ge1\), if \(X\) is smooth projective and \(\alpha\in K_n^M(k(X))\) has infinitely ell-divisible residue at every prime divisor, then \(\alpha\) is infinitely ell-divisible. The restriction \(n\ge1\) is essential in this second assertion: \(K_0^M=\mathbf Z\) has no nonzero residues and is not divisible.

### Proof

The inclusion from left to right in (M1) follows from reduction modulo every \(\ell^r\) and the norm-residue isomorphism. We prove the other inclusion by induction on \(n\). For \(n=0\), the source is \(\mathbf Z\) and the assertion is immediate.

First suppose that \(K\) has a smooth projective model \(X/k\), defined over a finite subfield. Let \(\alpha\) be infinitely ell-divisible. Its residue at each prime divisor is infinitely ell-divisible in \(K_{n-1}^M\) of the residue field. The induction hypothesis, applied to those residue fields, shows that every residue of \(\rho_n(\alpha)\) in ordinary generic continuous cohomology is zero.

Localization and codimension-one purity now place the rationalized regulator in
\[
H^n_{0,\mathrm{nr}}(X,\mathbf Q_\ell(n)).
\]
Concretely, a representative is defined on one open with finitely many missing prime divisors. For each such divisor its zero generic residue is already zero after removing a proper closed subset of that divisor. After deleting these finitely many subsets of codimension at least two, the localization sequence lifts the class across all prime divisors. This is an ordinary filtered-colimit argument, with no uniform inverse-limit claim.

By Proposition 3.7, every weight of this unramified group belongs to
\[
[-n,\max(-n,-2)],
\]
which is strictly negative for \(n\ge1\). The Milnor element \(\alpha\) is defined over a finite subfield and hence has a finite Frobenius orbit. Its regulator has the same property. Its finite-dimensional Galois-stable span therefore has only roots of unity as Frobenius eigenvalues, whereas every nonzero subquotient of the displayed unramified group has strictly negative weights. Consequently \(\rho_n(\alpha)\) vanishes rationally. Torsion-freeness of the ordinary integral generic continuous group, from Schreieder Theorem 2.2 and Corollary 2.3, implies integral vanishing.

For a general \(K\), take a projective finite-field model and a smooth projective alteration. After choosing a geometric component and, if needed, enlarging the finite field of definition, its function field \(L\) is finite over \(K\). The pullback of \(\alpha\) is infinitely ell-divisible and its regulator vanishes by the smooth-projective case. Restriction followed by corestriction on ordinary generic continuous cohomology is multiplication by \([L:K]\), including the inseparable factor. Thus \([L:K]\rho_n(\alpha)=0\); torsion-freeness gives \(\rho_n(\alpha)=0\). This closes the induction for all finitely generated residue fields as well.

Finally, let \(\alpha\) only satisfy the stated residue condition on a smooth projective model. The just-proved degree-\((n-1)\) assertion makes every residue of \(\rho_n(\alpha)\) zero. The same refined-weight and finite-orbit argument gives \(\rho_n(\alpha)=0\), and (M1) then gives infinite ell-divisibility. This extends the conclusion of Schreieder Lemma 4.1 to every degree using the additional 2026 refined-weight theorem; no novelty claim is made.

The induction is by Milnor degree, not by dimension. Alterations in the argument only establish the induction statement for arbitrary residue fields; no resolution of singularities is assumed. A finite extension of constants is harmless because the finite-orbit and strictly-negative-weight properties survive it.

## 4. Why this lemma does not settle B.1

The proof controls an **ordinary Milnor element**, whose Frobenius orbit is finite. It does not control an arbitrary vector in its adic completion. It also does not prove that every invariant vector in ordinary generic continuous cohomology is an ordinary Milnor element or a finite linear combination of such elements with compatible support.

The B.1 degree-four gate involves
\[
H^4(F_0\mathbf P^4_{\overline{\mathbf F}_p},\mathbf Q_\ell(3))^\Gamma,
\]
and its threefold residues have twist two. The regulator in (M1) has the diagonal twist \(n\), for which the relevant unramified weights are negative. For a threefold residue in degree three and twist two, Proposition 3.7 gives weights in \([-1,0]\); weight zero is precisely not excluded. The proof therefore cannot be applied after silently changing the twist. Completion of a locally finite Frobenius module can acquire non-root-of-unity eigenvectors, as the already-integrated formal limit diagnostic demonstrates. That diagnostic is not identified with a Milnor K-module; it shows why local finiteness alone cannot exclude such eigenvectors in a Milnor completion.

No universal Beilinson/Parshin conclusion, no shrinking-survival assertion, and no qualifying review movement is claimed.

## 5. Current integral-cycle source cross-check

Scavia and Suzuki, *Vanishing of degree 3 unramified cohomology over finite fields*, arXiv:2609.36188v1, 28 September 2026, was opened at <https://arxiv.org/pdf/2609.36188> and downloaded with the exact retrieval log in `output/post08_primary_capture.json`.

Theorem 1.2, pp. 2–3, assumes surface Tate, characteristic greater than two and Witt liftability. It proves integral one-cycle surjectivity for almost every prime, uniformly over finite extensions; in dimension three it concludes divisibility, not vanishing, of degree-three unramified \(\mathbf Q_\ell/\mathbf Z_\ell(2)\)-cohomology. Conjecture 4.4 is universal Tate plus Frobenius semisimplicity. Under that package, Theorem 4.7, pp. 30–31, removes liftability and gives both codimension-two and one-cycle surjectivity, together with the same divisibility conclusion, for almost all primes. The complete proofs of Lemma 4.5, Proposition 4.6 and Theorem 4.7 were read, as was the final proof of Theorem 1.2 and Corollary 6.5. The earlier full connecting-map/monodromy argument in Theorem 4.2 and all its dependencies have not been independently audited.

Corollary 6.5 obtains actual vanishing for the specified supersingular abelian threefolds by adding the abelian-type finiteness theorem of Colliot-Thélène–Kahn. None of these integral surjectivity or torsion/divisibility statements proves injectivity of the arbitrary rational codimension-two cycle map. A uniquely divisible rational kernel is invisible to these finite-coefficient conclusions.

## 6. Audit record

The owner checked all displayed arguments while writing this note. Agent D independently checked the exact abstract-complex certificate and the stated scope of Theorem 6.1 and Appendix B. D then independently read Proposition 3.7 with its complete proof, Schreieder Theorem 2.2 and Corollary 2.3, and the complete actual note, and passed the geometric extension. Root independently read every line of Section 3 and passed its degree induction, finite-orbit argument, ordinary localization, weight calculation, torsion-freeness and trace descent. Root then independently read definitions (2.7)–(2.8), the complete Proposition 3.7 proof, the complete Schreieder Theorem 2.2 and Corollary 2.3 proofs, and Remark 2.4, confirming their ordinary-colimit scope. Neither root nor D claims a new audit of the full foundational norm-residue theorem. No script execution is claimed for these mathematical proof checks.

## 7. A stronger formal completion diagnostic

Agent D supplied the following refinement of the earlier abstract function-module diagnostic; the owner independently checked every map and congruence. It shows that even being a free submodule of a countable direct sum of finite permutation modules does not rule out new eigenvalues after completion. This is not an identification with geometric Milnor K-theory.

Put \(D=\mathbf Z[1/3]/\mathbf Z\), with \(F\) acting by multiplication by four, and let
\[
N=\bigoplus_{r\ge1}\mathbf Z[C_{3^{r-1}}].
\]
Write \(e_{r,j}\) for the standard basis of the summand indexed by \(r\), with \(j\) taken modulo \(3^{r-1}\). Let \(F e_{r,j}=e_{r,j+1}\), and define
\[
\pi(e_{r,j})=\frac{4^j}{3^r}\pmod{\mathbf Z}\in D.
\]
The congruence \(4^{3^{r-1}}\equiv1\pmod{3^r}\) makes the wraparound compatible with \(F\). The map is surjective because \(e_{r,0}\) maps to \(1/3^r\). Therefore
\[
0\longrightarrow M\longrightarrow N\xrightarrow{\pi}D\longrightarrow0,
\qquad M=\ker\pi,
\]
is an exact sequence of locally finite Frobenius modules, and \(M\) is a free abelian group of countable rank because it is a subgroup of the free group \(N\).

Reduction modulo \(3^r\) gives the exact sequence
\[
0\longrightarrow D[3^r]\longrightarrow M/3^rM
\longrightarrow N/3^rN\longrightarrow0.
\]
Here the left map is the Tor boundary, and the right surjectivity uses divisibility of \(D\). The transition on \(D[3^r]\) is multiplication by three, and is surjective. Thus the inverse limit is exact:
\[
0\longrightarrow T_3D\longrightarrow\widehat M_3
\longrightarrow\widehat N_3\longrightarrow0.
\]
The subgroup \(T_3D\simeq\mathbf Z_3\) has \(F\)-action by four. In particular, \(\widehat M_3\otimes\mathbf Q_3\) has a nonzero four-eigenvector, although \(\widehat N_3\otimes\mathbf Q_3\) has none by the fixed-orbit argument already proved in the report.

An explicit compatible representative is
\[
\lambda_r=3^r e_{r,0}\in M,
\qquad [\lambda_r]\in M/3^rM.
\]
Compatibility follows from
\[
\lambda_{r+1}-\lambda_r
=3^r(3e_{r+1,0}-e_{r,0}),
\]
whose parenthesized term belongs to \(M\). Also
\(F\lambda_r-4\lambda_r\in3^rM\), including \(r=1\), where the sole basis vector is fixed. The class of \(\lambda_r\) has exact order \(3^r\): by torsion-freeness of \(N\), divisibility of \(3^s\lambda_r\) by \(3^r\) inside \(M\) would force \(3^s e_{r,0}\in M\), which occurs exactly when \(r\le s\). This proves nonvanishing and survival after rationalization, independently of any finite numerical check.

The finite congruence certificate in `code/permutation_submodule_completion.py`, with output in `output/permutation_submodule_completion.json`, checks levels one through eight only. It is supplementary to, and not a replacement for, the infinite argument above.

## 8. Free separated quotient and limited literature check

The integrated `cor:B-Milnor-free-quotient` adds the following consequence. Put \(D_\ell=\ker\rho_n\) and \(M_n=K_n^M(K)/D_\ell\). Then \(D_\ell\) is ell-divisible, \(M_n\) is free of at most countable rank, and the quotient induces a canonical Frobenius-equivariant isomorphism on ell-adic completions. Indeed, if \(a\in D_\ell\) and \(\ell b=a\), then \(\ell\rho_n(b)=0\), so \(b\in D_\ell\). For arbitrary \(K\), restriction to a smooth projective alteration injects \(M_n(K)\) into \(M_n(L)\), by trace and torsion-freeness. On the smooth projective model, the proved residue assertion injects \(M_n\) into the direct sum of the \(M_{n-1}\) of its prime divisors. Induction from \(M_0=\mathbf Z\), together with the subgroup theorem for free abelian groups, proves freeness. Every set and field in question is countable. Divisibility of \(D_\ell\) gives the canonical quotient isomorphisms modulo every ell-power and hence on completions.

This supplies neither a saturated residue embedding nor a Frobenius-stable permutation basis. Section 7 directly explains why even a permutation-submodule construction would not, by itself, exclude new completed eigenvectors.

Root performed a limited novelty search for the exact strings “Milnor K free abelian finite field”, “Milnor K-theory divisible free Schreieder”, and “Divisibility phenomena free”. The primary results returned the already-opened Schreieder Theorem 4.2/Proposition 5.1 and the Colliot-Thélène–Schreieder 2026 paper. No separate all-degree freeness theorem was verified in that search. Secondary hits were not used. This limited search is not a claim of priority, and the report explicitly makes no novelty claim.

## 9. One common quotient for all primes different from the characteristic

For primes \(\ell,\ell'\ne p\), consider the image of \(D_\ell\) in the proved free abelian group \(M_{n,\ell'}=K_n^M(K)/D_{\ell'}\). That image is ell-divisible, because \(D_\ell\) is ell-divisible. A free abelian group has no nonzero infinitely ell-divisible element: every element has finitely many integer coordinates, and divisibility by all ell-powers forces every coordinate to vanish. Hence \(D_\ell\subset D_{\ell'}\). Interchanging the primes gives equality.

Thus there is one canonical subgroup \(D^{(p')}\subset K_n^M(K)\), divisible by every prime different from \(p\), and one canonical countable free quotient
\[
M_n(K)=K_n^M(K)/D^{(p')}
\]
which induces the Frobenius-equivariant isomorphisms of completions for **every** \(\ell\ne p\). This is incorporated into the existing corollary, with its label retained. It is a consequence of the same intermediate proof, not a separate change in the universal B.1 gate.

The common integral quotient does not imply prime independence of completed eigenvalues. The formal \(M\) from Section 7 supplies an explicit counterexample to that inference. For any prime \(s\ne3\), multiplication by \(s\) is an automorphism of \(D=\mathbf Z[1/3]/\mathbf Z\), so
\[
D[s^r]=0,\qquad D/s^rD=0.
\]
Tensoring its exact presentation therefore gives canonical equivariant isomorphisms
\[
M/s^rM\simeq N/s^rN,
\qquad\widehat M_s\simeq\widehat N_s.
\]
The completed permutation module \(\widehat N_s\otimes\mathbf Q_s\) has no nonzero four-eigenvector. Indeed, projection to each fixed finite orbit of length \(d\) would give \((4^d-1)v=0\) in a torsion-free characteristic-zero module, hence \(v=0\); the completion embeds into the product of those orbit modules. In contrast, \(\widehat M_3\otimes\mathbf Q_3\) contains the four-eigenline of Section 7. A single free, locally finite integral Frobenius module can therefore have prime-specific completed eigenvalues. This is a formal module example, not a geometric realization or a counterexample to the conjectural arithmetic comparisons.

Root, D and the owner independently checked the common-kernel argument and the prime-specific completion argument. These conceptual checks preceded this post-checkpoint written addition; the subsequent actual-text checks are recorded separately. No finite numerical test is needed for the statement about every other prime; it follows from the exact quotient sequence just displayed.

The twist convention can also be matched precisely at the formal-module level. Regard \(F\) as arithmetic Frobenius for a formal base \(\mathbf F_4\); geometric Frobenius is \(F^{-1}\), with eigenvalue \(1/4\) on the three-adic line. Tensoring by \(\mathbf Q_\ell(-1)\) multiplies geometric Frobenius by four. The resulting completed representation therefore has a nonzero invariant at \(\ell=3\) and none at any other \(\ell\ne2\). This is the same numerical shift from diagonal twist three to twist two that admits weight zero in the B.1 residue problem. It remains a formal representation example; no geometric realization is asserted.

C subsequently read the complete revised corollary and Sections 7 and 9 and passed both the common-kernel proof and the prime-specific completion argument. Root reread the revised TeX and Section 9 at the measured time 09:37:34 UTC and passed them. The owner separately checked the final arithmetic/geometric twist convention above.

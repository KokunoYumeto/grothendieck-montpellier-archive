# Root whole-proof audit: Greenberg kernel reduction

Date: 21 November 2026 UTC. Reviewer: GPT-6 Astra Pro, `/root`; effort setting not exposed.

**PASS for the conditional theorem with the stated one-variable hypothesis that X+ is finite.** I read every paragraph of `greenberg_magnus_adaptation.md` §§1–10 and then every line of `greenberg_kernel_section.tex`, as well as the entire separate `cup_ext_pole_section.tex`. This is a mathematical whole-proof reading and independent reconstruction of the key deductions, not a formal proof execution.

## Whole-H and coefficient audit

The actual compact free basis is obtained from a convergent Zp-product basis of the entire abelianization; surjectivity follows from the closed-subgroup Frattini argument and injectivity from projectivity plus the same argument applied to a section. This avoids an invalid inference from finite index on abelianizations. The inverse limit over finite tails really recovers H: every finite quotient kills a tail, and compactness gives the converse surjectivity. Thus a nontrivial element has a first finite weighted Magnus degree.

I independently checked that a rational Lambda isomorphism and its inverse have fixed p-denominators because the modules are finitely generated. Completed tensor powers have the induced finite denominator at every fixed degree; the product Zp bases make them torsionfree. The even-letter change is homogeneous triangular, Y -> bY + A(X), and the inverse is valid degree by degree. It retains an actual first nonzero coefficient and makes no claim that rational companions are an integral group basis.

The target coefficient of each odd type is a nonzero evaluation functional by equivariance and actual-image density. Actual conjugates of a companion have quadratic coefficients z^j B, so the companion relation gives q(z)B=C. Partial fractions are a finite constant invertible transformation even with repeated roots. Finite target weight quotients justify the completed substitution and degree isolation through continuity on the compact actual group.

The Laurent separation was checked independently. For a maximal pair pattern, the selected disjoint divisors are formal coordinates; other pair positions cross distinct blocks, so their denominator has a nonzero constant over the fraction field of the surviving variables. Choosing a componentwise maximal pole vector leaves exactly its coefficient at the selected negative monomial. The surviving product has nonzero factors in a field. Bounds are needed only at that one degree, never uniformly over the whole Magnus series.

## Cup, transfer, and comparison audit

The separate cup lemma was read in full. I recomputed its BCH cochain: the symmetric quadratic and alternating central terms add to p^b f(h1)g(h2). The mixed-section defect is the pairing with p^b beta_delta(t), zero on the split eigenline. Corestriction of H1 for an index-p procyclic subgroup sends the normalized generator value to the same coinvariant value; it does not multiply by p. The finite targets have inverse limit Hom(T,O)(2), and restriction to the saturated eigenline is onto. The fixed denominator therefore yields the contradiction at every root, including multiple roots.

I independently verified the maximal-pro-p comparison. A nonzero P-invariant Hom(N,A) would give a larger pro-p quotient of the full etale group, impossible by maximality. The five-term sequence gives H1 isomorphism and H2 injection. The full universal etale tower kills each finite H1 torsor, and Cartan–Leray gives the further H2 injection into etale cohomology. Cup generation and the H1 isomorphism then give the exact even H2 surjectivity required. No arithmetic K(pi,1) theorem or vanishing of all higher universal-cover rows is assumed.

## Fresh source checks

I freshly read WWE, *Pseudo-modularity and Iwasawa theory*, §2.1 including the complete Corollary2.1.3 proof and the explanation following Conjecture2.1.5, p8; Corollary8.1.3 and its complete proof, pp48–49. The latter really concludes integral isomorphisms after quotienting the source by p-primary torsion, under rational cyclicity and the localized vanishing of X_theta. Its repeated-root proof uses nilpotence, not a simple-zero assumption.

I freshly read WWE, *Ordinary pseudorepresentations and modular forms*, Proposition2.2.6 and its complete proof, pp3–4, plus the exceptional-character paragraph in Lemma5.2.7, p13. The ramified/unramified modules and the inversion/twist were distinguished explicitly. Localizing the displayed Ext identity over the PID Lambda[1/p] gives rational rank-one freeness. I freshly read Sharifi, *Iwasawa Theory*, Theorem5.5.31 and its entire proof, p148, and Proposition6.1.1, pp151–152; the Coleman kernel/cokernel exactly give the two exceptional characters. Earlier actual checks of §3.4 supply the even module and norm projection inputs.

I freshly read FK's full §§7.1.8–7.1.10, p86, including its coefficient-reduction identifications and the proof that varpi-surjectivity implies finite symbol generation. The omitted characters have zero target by the checked Stickelberger and norm statements. The cyclic negative p-unit part makes all even symbols sums of even-even cups, without assuming that all H1 classes arise from units.

I freshly opened Milne, *Lectures on Etale Cohomology* v2.21, and read Theorem14.9 and its full proof, Remark14.10, Example14.11, pp96–97, and Proposition14.13 and proof, p98. The low-degree comparison in the new lemma is consistent with these primary statements. The application treats F_(n+1) with coefficients p^n explicitly, and the normal-closure argument correctly identifies its maximal pro-p group with the subgroup of the one fixed Omega.

The combined conclusion is **conditional on Greenberg only**. It does not prove Greenberg, give its converse, or supply a new numerical K-group vanishing. The independent full theorem is ready for integration after the author's and the second reviewer's final TeX readback.

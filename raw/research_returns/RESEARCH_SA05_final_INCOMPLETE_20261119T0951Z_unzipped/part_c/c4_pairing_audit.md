# Exact threefold pairing obstruction and scope

Recorded on 19 November 2026; owner /root/part_c.
The written fragment is c4_pairing_reduction.tex.

## What is proved

For a projective strictly semistable threefold, the two relevant Rapoport–Zink rows have the common middle term $U\oplus Z$, where $U=H^2(Y^{(2)})$ and $Z=H^0(Y^{(4)})(-1)$. The monodromy map is induced by the identity. A class in its kernel has a representative $(\rho a+\gamma b,\rho b)$. Subtracting the common domain boundary leaves $(r,0)$ with $r\in\operatorname{im}\rho$, and the only new cocycle condition is $\gamma r=0$. The relation $\rho^2=0$ removes the other condition. Duality identifies $\ker\gamma$ with the orthogonal complement of $\operatorname{im}\rho$.

Consequently the kernel is exactly

$$
\frac{\operatorname{rad}(b|_{\operatorname{im}\rho})}
{\operatorname{im}\rho\cap\gamma\ker\rho}.
$$

This is an exact kernel identification, not a proof of its vanishing. Morihiko Saito's dimension-three converse removes the nonprimitive Lefschetz pieces and the additional primitive Gysin-image condition: that latter condition is already equivalent to the known degree-two monodromy isomorphism. The remaining condition is nondegeneracy of the primitive restriction image in the degree-two cohomology of the double-intersection surfaces.

The new divisor-splitting corollary removes the primitive image that actually comes from the rational Néron–Severi group of the threefold components. The surface Hodge index theorem is applicable to this rational subspace, whose Gram determinant is nonzero in $\mathbb Q$; this determinant stays nonzero in $\mathbb Q_\ell$. It does not remove an arbitrary $\mathbb Q_\ell$-subspace merely contained in the divisor span.

Under the separate hypothesis of divisor Tate for all finite-field surfaces of the residue characteristic, Kahn's reduction gives divisor Tate for every stratum and every finite constant extension. An orthogonal Néron–Severi splitting and Tate surjectivity then separate the eigenvalues $q$ times roots of unity from all remaining eigenvalues. Restriction preserves the two spectral blocks. Its non-Tate image is primitive and orthogonal to every target divisor. This identifies the remaining pairing with the form on $\rho(T_1)\subset T_2$, without assuming full Frobenius semisimplicity.

## Sources actually opened and checked

1. Morihiko Saito, *Monodromy filtration and positivity*, arXiv:math/0006162v11, revised 25 September 2003. Owner read the complete proofs in §§1.1–2.7, author pp. 3–9; Theorem 0.2 is on p. 2 and the exact threefold converse is §2.7, p. 9. Part D read the complete §§4.1–4.3, pp. 14–16, and §§5.1–5.5, pp. 16–18. Root independently read §§2.1–2.7. Primary URL: https://arxiv.org/pdf/math/0006162 . Key c_msaito2003positivity.
2. Tetsushi Ito, *Weight-monodromy conjecture for certain threefolds in mixed characteristic*, IMRN 2004(2), 69–87. Owner read the complete Claims 4.4–4.7 and the concluding proof of Lemma 4.3 in the author version, pp. 11–14. The rational divisor-image step is Claim 4.6, pp. 12–13. Primary author URL: https://arxiv.org/pdf/math/0212109 . Publisher metadata confirms DOI 10.1155/S1073792804130250. Key c_ito2004threefolds.
3. Bruno Kahn, *Sur la conjecture de Tate pour les diviseurs*, Theorem 8, pp. 89–90. Owner opened and read the complete theorem proof; B, D and root had independently checked the underlying Morrow reduction and its implementation in sections/b3_surface_gate.tex. The proof retains the positive-characteristic Picard weak-Lefschetz correction; no naive restriction-only argument is substituted. Primary URL: https://webusers.imj-prg.fr/~bruno.kahn/preprints/Tate-pour-les-diviseurs-ENT.pdf . Existing key BKahn2023Divisors.
4. James S. Milne, *Polarizations and Grothendieck's standard conjectures*. Owner opened the complete submitted author version and read Remark 4.10 and footnote 3, p. 14; D checked both submitted and published versions. The submitted warning explicitly withdraws the inference from equality of motive categories to positivity of arbitrary geometric forms. The published Theorem 3.3 and Corollary 3.4, pp. 8–9, concern actual abelian varieties. URLs: https://www.jmilne.org/math/articles/2002aS.pdf and https://www.jmilne.org/math/articles/2002aP.pdf . Existing key DMilne2002Polarizations.

## Independent checks and finite certificate

Root and D independently passed the complete written kernel computation and Saito primitive-image reduction before the divisor-splitting addition. The shared restriction/Gysin sign convention is essential; it is fixed by commutation with monodromy. The twists in $A\times C$ and $U\times U$ both have target $\mathbb Q_\ell(-2)$.

The script code/part_c/check_c4_isotropic_ladic_line.py and its JSON output check the formal counterexample to an invalid scalar-extension positivity argument. The rational form $-x^2-y^2$ is negative definite, while the line $\mathbb Q_5(1,\iota)$ with $\iota^2=-1$ is isotropic. Exact Hensel lifts and the scalar Frobenius calculation are recorded. This is a formal linear-algebra counterexample only.

## Remaining gate and stopping-rule scope

The actual primitive image is still not proved nondegenerate. The conditional spectral identification depends on the separate surface-Tate hypothesis and does not solve unconditional C.4. No general positivity theorem is inferred from the October 2026 CM Hodge theorem or from an abstract abelian-motive isomorphism. This refinement isolates the first unresolved threefold block, but is not automatically counted as movement on the universal higher-degree C.4 task.

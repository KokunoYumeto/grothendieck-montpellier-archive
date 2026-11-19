# Focused review of the root Codex proofs

Reviewed November 19, 2026, by GPT-6 Astra Pro, with the inherited reasoning effort not exposed. This is a bounded cross-check requested by the parent, after the assigned Pro43 proofs and ledgers were written. No root-owned files were edited.

## C16: Frobenius shifts and the two mixed additive cells

The Witt Frobenius diagram gives \(F^*e=F_*e\). For the free left \(k[F]\)-module \(\operatorname{Ext}^1(\mathbf G_a,\mathbf G_a)\), pullback shifts \(a_iF^ie\) to \(a_iF^{i+1}e\), while pushout shifts it to \(a_i^pF^{i+1}e\). Both are injective over the stated perfect field. The covariant long exact sequence therefore proves \(\operatorname{Ext}^1(\mathbf G_a,\alpha_p)\cong k\).

The original contravariant deduction omitted the following term:
\[
\operatorname{Ext}^1(\mathbf G_a,\mathbf G_a)\xrightarrow{F^*}
\operatorname{Ext}^1(\mathbf G_a,\mathbf G_a)\to
\operatorname{Ext}^1(\alpha_p,\mathbf G_a)\to
\operatorname{Ext}^2(\mathbf G_a,\mathbf G_a)\xrightarrow{F^*}
\operatorname{Ext}^2(\mathbf G_a,\mathbf G_a).
\]
Without additional input it proves only the injection of the cokernel \(k\), not surjectivity. This was reported immediately. The parent corrected C16 to use its independently opened Fanelli–Schröer one-dimensionality result as additional input. This child did not claim to have opened that separate primary paper.

The finite-kernel reduction \(\operatorname{Ext}^1(\mathbf G_a,A[p])\cong\operatorname{Ext}^1(\mathbf G_a,A)\) is valid in the stated geometric extension category: \(\operatorname{Hom}(\mathbf G_a,A)=0\) and multiplication by \(p\) on the Ext group is zero because \(p\mathbf G_a=0\). This does not settle the separate \(\alpha_p\)-source or \(\mu_p\)-source cells.

## C8: labelled \(\alpha_p\) self-extensions

No hidden middle \(p\)-torsion obstruction survives. Start with the exact Dieudonné-module extension \(0\to k\to M\to k\to0\), before calling \(M\) a \(k\)-vector space. Both \(F(M)\) and \(V(M)\) lie in the submodule, and both operators vanish on that submodule. Thus \(FV=VF=0\), so \(pM=0\). It follows that \(M\) is a two-dimensional \(k\)-vector space.

With kernel and quotient bases fixed, \(Fe_2=ae_1\), \(Ve_2=be_1\), with the indicated semilinearity. Changing the lift by \(ce_1\) changes neither parameter. Baer addition gives the additive-group \(k\oplus k\) statement. This is a classification of **labelled extensions**, not isomorphism classes of their middle groups. The parent was advised to place the \(pM=0\) deduction before the vector-space assertion to avoid circular wording.

The internal Hom table's nilpotent-base warning is necessary: \(1+\varepsilon t\) is a nonconstant group-like unit on \(k[\varepsilon]/\varepsilon^2\). The finite restricted-Lie expressions and the qualified formal-category treatment of \(V\) are compatible with the distinctions used in this workstream. This review did not independently certify every unprinted or unresolved table cell.

## C9 and C12: bounded logical review

C9 explicitly assumes the normalized rigidity needed to kill associators; under that hypothesis the construction of a unique commutative extension from a primitive torsor is valid. A blanket assertion for every coefficient without rigidity would not follow. The perfect-field Artin–Schreier polynomial reduction is separate from arbitrary-base representability.

C12's finite-set counterexample to an unqualified fully faithful pro-object limit functor is valid: a singleton indicator on \(\{0,1\}^{\mathbf N}\) cannot factor through a finite prefix, though all finite sets are artinian. Its field coalgebra argument and finite-presentation qualifications do not claim the same approximation theorem over arbitrary rings. No additional clear category error was found in these bounded proof paragraphs; this is not a broad re-review of all root claims.

## Dossier §§1.3–1.5 and principal references

The local/coherent support distinctions, the relative infinitesimal-curve caution, the degree shifts and the difference between geometric Yoneda extensions and internal fppf Ext are retained correctly. Three wording changes were reported to the parent: the characteristic-p group \(\mathbf Z/p\) itself is étale, whereas the full collection including \(\mu_p\) and \(\alpha_p\) needs flat coefficients; the stable integral lattice assertion needs a continuous Galois representation or compact image; and the EGA universal-openness multiplicity question retains the full-support hypothesis. The parent had already planned the APA ordering of the two 2020 Suzuki publications: curves is 2020a and Néron models is 2020b. These bounded checks do not certify the other dossier sections.

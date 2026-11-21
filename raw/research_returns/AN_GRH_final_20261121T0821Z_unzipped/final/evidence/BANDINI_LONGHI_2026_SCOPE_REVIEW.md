# Bandini--Longhi 2026: targeted primary-scope check

Recorded 2026-11-21T08:02:54.133844+00:00. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Outcome

**No applicable bound on the actual characteristic-primary exponent in the nonconstant geometric cyclic tower was obtained from the checked statements.** This is a bounded source-scope check, not a proof that no such theorem exists. It adds no universal witness-supply theorem and does not count as main-gate movement.

The 2026 publication is the published work associated with arXiv2312.04666, already present in the earlier fixed-field-tower report. The arXiv record explicitly lists J. London Math. Soc. (2)113(2026), no6, e70601, DOI10.1112/jlms.70601. I checked both its v3 text and the later manuscript currently linked on the author's research page. The latter is a 34-page PDF with creation metadata10November2025; this metadata is not treated as a declared submission/version date. The publisher PDF returned403, so I do not assert a whole reading of the 46-page version of record or give its page numbers.

## Exact primary statements inspected

In the author's 34-page manuscript, Theorem1.2 pp3--4 and the setup of Section6 pp20--21 require an arithmetic abelian Galois extension of one global field. Theorem4.7 and its complete proof pp13--14 express ranks and valuations via component lengths; Theorem4.11 and its complete proof p16 give convergence in the tower-prime topology. These statements do not bound the component lengths.

Section7 p25 sets the field characteristic equal to the tower prime and assumes an abelian extension. Theorem7.12 pp31--32 identifies characteristic ideals with special-value ideals under its splitting hypotheses and the condition [Q_ell(mu_(p^n)):Q_ell]=phi(p^n) for all n. Its complete displayed proof was read. Corollary7.14 and Remark7.15 p32 treat the arithmetic constant extension and permit that construction in any positive characteristic. Their boundedness statement is for the constant tower.

The author manuscript ends its introduction by proposing nonabelian extensions as possible future applications; it does not state a semidirect-tower exponent theorem there.

## Why this does not apply directly to the present tower

To avoid notation reversal, write c for the curve characteristic and l for the odd tower prime. The article's coefficient prime ell would be c, and its tower prime p would be l.

Our required sequence consists of degree-l^r geometrically cyclic covers D_r over the same finite field k, with a rational lift of a prescribed point. Frobenius acts on the geometric deck group through a fixed a in Z_l^times of infinite order. The target invariant is exp(P_(l^r)(k)[c^infinity]) for the actual primitive Jacobian factor.

The geometric deck generator need not preserve the rational points of that factor. Therefore the rational groups are not automatically modules for the full Z_c[C_(l^r)] action required in the paper's arithmetic Galois setup. The actual invariant ring action and semilinear descent in A45/A51 are the appropriate weaker structure.

More concretely, after the constants needed to define the deck transformations are adjoined, the arithmetic normal closure retains Frobenius conjugation sigma -> sigma^a. The resulting arithmetic group is nonabelian whenever that action is nontrivial. Passing to a finite constant extension of degree m replaces a by a^m. Since a is not a root of unity, no such finite extension makes the entire infinite tower have constant deck group. Level-by-level constantization instead uses the growing fields of degree ord_(l^r)(a), so it does not produce one abelian Galois tower over the same global base to which Theorem1.2 applies. Passing to the full algebraic closure of the constants removes the finite-constant global-field hypothesis.

Even if an appropriate abelian module identification were separately supplied, Theorem4.7 contains unspecified nonnegative elementary-divisor lengths. Tower-prime-adic convergence of the cardinalities is not a real upper bound on the coefficient-prime exponent. Theorem7.12's equality of ideals would still require estimates or unit information on its special values. It does not itself give the sub-square-root bound needed by A47, or the annihilator-index bound needed by A52.

The constant-field corollary controls new constants for a fixed function field. It cannot be silently substituted for new geometric covers with changing Jacobians and a prescribed rational lift. The new publication citation thus does not repair the previously identified scope mismatch.

## Read and retrieval scope

Read in the later author-linked manuscript: introduction1.3--1.4; complete Theorem1.2 statement; Definition4.6; Theorem4.7 and complete proof plus Remarks4.8--4.9; Theorems4.10--4.11 and their displayed proofs; complete Section6 setup and6.1 through its module conclusions; Section7 setup; Lemma7.11 and Theorem7.12 with complete displayed proofs; Corollaries7.13--7.14 and Remark7.15. The external inputs to those proofs were not independently reproved, and the entire34-page paper was not audited. The v3 web text was used to cross-check the same hypotheses and locate the author version, not to claim identical pagination or an exact match to the published file.

This is a primary-scope audit and an explicit applicability argument. It contains no new arithmetic execution, geometric construction, or whole-paper correctness verdict.

## Primary URLs and retrieval references

- Publication record: https://iris.unito.it/handle/2318/2147010 ; initial direct open403, indexed primary record available as turn188949761search1.
- Publisher DOI: https://doi.org/10.1112/jlms.70601 ; primary metadata turn188949761search2. Direct publisher PDF403.
- Author research page: https://sites.google.com/site/banand207/home/research ; turn655094299view1, link8.
- Author-linked PDF: https://drive.google.com/file/d/1dSGB50B6Y2tWup4RttnJ5Wfrcc-FUyyz/view ; turn412478294view0. Public download retrieved from https://drive.usercontent.google.com/download?id=1dSGB50B6Y2tWup4RttnJ5Wfrcc-FUyyz&export=download . Retained PDF SHA3276bc3c8100102a0742d598c06d89290f93a467d7f530fef46688279afbccab.
- arXiv record: https://arxiv.org/abs/2312.04666 ; turn655094299view2.
- v3 primary PDF/HTML: https://arxiv.org/pdf/2312.04666 and https://arxiv.org/html/2312.04666v3 ; turn412478294view1/view2. Exact setup and statements: turn978965873view2/view3/view4/view5, turn166988213view0/view1/view2. These locators are for v3, not the version of record.

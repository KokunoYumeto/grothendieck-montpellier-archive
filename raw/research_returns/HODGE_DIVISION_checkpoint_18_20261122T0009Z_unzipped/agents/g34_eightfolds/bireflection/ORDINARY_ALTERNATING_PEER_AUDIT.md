# Independent whole-proof audit: HD-ALT-01a–c

**Result: PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited/unexposed effort, run HODGE_DIVISION, 21 November2026, approximately16:52–16:58UTC. The entire final proof was read, including the revised direct GKT degree threshold. Reviewed SHA256: `663a4d17bcd564ee438d70193dca444ba068740563e0346cc69b7899d34e269c`.

## Exact scope

The result excludes the specified ordinary alternating tensor-core shapes for primitive essentially self-dual inducing blocks of dominant nonsplit Weil sixfold sources, with alternating degree n≥15. It permits a larger inducing character field and all compatible outer automorphisms and factor permutations. It does not exclude every ordinary alternating representation. In particular the proof leaves long first-row/column shapes and nonselfdual split characters open, as stated.

## HD-ALT-01a

I independently reconstructed all66 spectra of all six nontrivial center-positive rows of the complete2.A6 table. My implementation uses rational Ramanujan Fourier, not the root's cyclotomic-polynomial arithmetic. All66 complete multiplicity vectors agree with the root's output. The six row degrees are5,5,8,8,9,10 and the exact minima of nu/degree are2/5,2/5,1/2,1/2,4/9,2/5. The certificate does not reconstruct or identify the finite group; the ATLAS table and its group identity remain the published input.

For any nonscalar normalizer, its induced nontrivial permutation fails to centralize some three-cycle, because the three-cycles generate A_n and the centralizer of the faithful irreducible core is scalar. The commutator is nonidentity and has support at most six, so it lies in a natural A6. Natural six-letter subgroups are conjugate in A_n for n≥8 by correcting an odd conjugator with a transposition on two exterior letters. The restricted trivial multiplicity d0 is therefore uniform. The fixed-eigenvalue estimate adds over nontrivial constituents, while the trivial part contributes at most d0; no false assertion about absence of trivial restriction is made. Scalar-adjusted rank subadditivity gives nu([g,c])≤2nu(g). A three-cycle and its inverse are conjugate in A_n, making its two nontrivial eigenvalue multiplicities equal. Consequently d0≤(a+2chi(c))/3, and the displayed coefficient2/15 follows exactly. Faithfulness and nonnegativity establish the stated interval for u.

## HD-ALT-01b

The Jucys–Murphy identity has the correct normalization: the equal terms contribute binomial(n,2) identities and each oriented three-cycle occurs exactly once, indexed by its largest letter. The three-cycle class size is n(n−1)(n−2)/3. Thus the character ratio is exactly ALT.6. For a split Specht restriction, the two constituents have equal degree and equal three-cycle value because the class has an odd centralizer, so the same normalized ratio applies to each half.

The diagonal Frobenius hooks partition all boxes, with arm and leg contents1 through their respective lengths. Under the stated shape hypothesis each length is at most k−1 and their total is n−d≤n−1. Bounding s(s+1)(2s+1)/6 by s k(2k−1)/6 gives the written total and precisely the two parity-dependent numerators n−7 and n−5. This is a universal combinatorial argument, not a finite partition experiment.

## HD-ALT-01c

The factorwise eigenspace bound extends to a tensor product by fixing all other eigenvalues; the tensor-cycle bound is the already independently checked weighted-word argument. Its quarter fraction is stronger than the new (n−1)/(10(n−2)) fraction. Scalar inertia has full actual moving rank. The actual intermediate Hurwitz factorization and nontrivial similitude argument supply twelve genuine inertias and two half-moving entries under exactly the primitive/essentially-self-dual/nonreal-field hypotheses retained in the statement. There is no assumption that the inducing field equals the original quadratic field.

The remaining ten terms give e+(n−1)e/(n−2)≤2e+6 and hence e≤6(n−2). The published nontrivial alternating degree minimum n−1 ensures that the earlier argument's degree hypothesis holds. An S_n Specht module containing a factor has degree at most twice that factor degree, hence at most12(n−2). The final proof uses the exact published GKT consequence for degrees below2n³/27, rather than extracting partition uniqueness only from a degree-value table. The strict inequality is valid at15 and increases:27 times its difference is2n³−324n+648, equal2538 at15, with forward difference6n²+6n−322 positive thereafter. The three possible Specht labels all violate the shape hypothesis. The self-conjugate implication follows from the first diagonal hook length2lambda1−1≤n; outer automorphisms and transpose preserve the condition. No issue found.

## Primary sources freshly read

- Collins–Matsumoto–Novak, *The Weingarten Calculus*, author arXiv2109.14890v1, Theorem4.2 and its preceding Jucys–Murphy definitions, numberedp9. The unversioned primary URL https://arxiv.org/pdf/2109.14890 resolved to v1. Published metadata: Notices AMS69(2022),734–745, DOI10.1090/noti2474. The exact content-eigenvalue theorem has no moment or stable-range hypothesis relevant to this application. Direct AMS access returned403; author and published page numbers were not conflated.
- Bessenrodt–Nguyen–Olsson–Tong-Viet, *Complex group algebras of the double covers of the symmetric and alternating groups*, Algebra & Number Theory9(2015),601–628, DOI10.2140/ant.2015.9.601. Actual published PDF https://msp.org/ant/2015/9-3/ant-v9-n3-p04-s.pdf: §2A p604 for the complete restriction rule; Lemmas3.1–3.2 p607 for the exact nontrivial degree minimum. The author PDF was also opened, but the cited locators refer to the journal.
- Guralnick–Katz–Tiep, *Rigid local systems and alternating groups*, Tunisian Journal of Mathematics1(2019),295–323, DOI10.2140/tunis.2019.1.295. Actual published PDF https://msp.org/tunis/2019/1-3/tunis-v1-n3-p01-p.pdf: entire Theorem9.7 proof pp312–313, especially the explicit Rasala shape consequence onp312. Only that unrestricted degree-classification consequence is used. The surrounding semisimple-regular hypothesis is not imported or claimed for the present source.
- The complete local ATLAS input has SHA256 d41d9bcb33344ce8d655dd83aa90f4a58ffc4f00a5cd22271c72895c22e7d26c. The independent program is `audit_ordinary_alternating.py`, output `audit_ordinary_alternating.json`.

The original Rasala1977 proof is not claimed freshly reconstructed or read in this event; the exact published GKT restatement was read. No unrelated low-degree classification or unrefereed theorem is assumed. TeX compilation is unavailable in this run and is not claimed.

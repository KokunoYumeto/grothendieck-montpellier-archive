# Independent mathematical audit of TS.1–TS.4

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06 /root/frobenius; inherited effort setting not separately exposed.

The complete file `../real_weil/C3_tetrahedral_K_spectrum_draft.tex` was read and independently rederived. Verdict: **PASS for the mathematical argument**, with the source-entry clarification below. This is an unregistered auxiliary; no ordinary Chow result or main-gate movement is claimed.

1. The external-product comparison is canonical before choosing projective-bundle or blowup decompositions. On every smooth rational stratum it is an equivalence, by those decompositions and the projection formula. Thus it compares the full restriction diagrams, including coherences. It does not try to manufacture compatible cellular flags.
2. GH excision after inverting p applies to every binary closed union; finite affine Mayer–Vietoris globalizes it. The SNC intersection diagram is finite. Tensor of module spectra is exact, hence commutes with its finite homotopy limit. This proves TS.1.
3. Rational K of Fpbar is HQ, so the strata spectra have only degree-zero homotopy, and their restriction diagram is computed in rational vector spaces. The rank part is the tetrahedral sphere cochain complex. The Picard map has source rank34 and target rank6; the exceptional curve at a nonvertex edge point has degree1 on exactly that edge, proving surjectivity. Its kernel has rank28. The component point-class part has rank4. Therefore K0 has rank1+28+4=33, K−1 vanishes, K−2 has rank1. The Euler check is42−12+4=34=33+1. Splitting once over Fpbar and then tensoring preserves the parameter compatibility.
4. The K−2 generator has Adams weight0, so its product with field K2 has weight2. The coefficient and its evaluations on proper parameter curves follow from the natural module comparison, not from a dimension count. This still does not produce an actual family on Z×P.

Source scope: GH Theorems A/C, TT finite affine descent, and the actual resolution geometry were freshly read/audited in the preceding FF/TG reviews in this run. I did **not** newly reopen Khan in this check, and no computation was rerun. Step3 currently cites `frWeibelKbookIII` for ChapterIV locators; the owner has been asked to ensure its bibliography/source points to the actually opened ChapterIV or full book rather than the ChapterIII-only entry.

New pointwise refinement: Drinfeld Theorem3.7 and Remark(ii), authorp8 of arXiv math/0309155v4, were freshly opened/read and visually inspected in this run. They give K−1(R)=0 for henselian local R. Together with FF.1 and the rank graph in its exact sequence, this yields FF.4: K0(Z)[1/p]≅K0(E)[1/p]. The individual coefficient-lifting gate is therefore removed; the fixed proper-family gate remains.

Completion: 2026-11-19T16:14:30.265968+00:00

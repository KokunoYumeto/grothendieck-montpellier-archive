# A.162: full promoted proof and split-kernel supplement

We read the complete 375-line promoted proof on 20 November 2026, including the added natural bridge and algebraic corollary. The subsequent insertion of a heading-keep command is purely typographical; the stable 376-line source is `agents/higher_comparison/part_RP3_equivariant_germs.tex`, SHA256 `2b56142c11d6d967f0d056c6a8f67e4205260204521129577d7c59efd369cbb9`.

The full local extension, horn lifting, strict-fibre and projective Smale arguments retain the earlier complete root audit in `notes/root_RP3_equivariant_germ_candidate_audit.md`. The typo identified there is corrected, and the full Cerf1961 proof locator is now included.

We also checked the following added steps against the actual A.132 proof in `parts/parametric_concordance.tex`:

1. The nonequivariant simplicial joint-germ group is literally the same model, with equality on a neighborhood of the entire compact parameter zero section.
2. Equation A.132.11 and the extension map immediately following A.132.12 preserve the actual linear O(4) inclusion. Thus the comparison on fundamental groups is the relevant natural map.
3. The established vanishing of pi1 and pi2 of TOP(4)/O(4) makes pi1(O(4)) to pi1 of the nonequivariant germ group an isomorphism. Since pi1(O(4)) is Z/2, the odd-germ group splits on pi1 as that linear summand plus the forgetting kernel.
4. The explicit map in A.162.10 is independent of the chosen representative modulo the linear summand, lands in the forgetting kernel, and is inverse to inclusion followed by quotient.
5. The component group agrees with the quotient group from the simplicial group fibre sequence and is abelian. Consequently the PL component image is a normal subgroup.
6. The previously proved Casson–Sullivan homomorphism is onto F2 on RP3 and vanishes on the PL image. The short exact sequence A.162.11 therefore follows, with kernel precisely ker(chi)/I. This does not evaluate that kernel or establish PL-to-TOP injectivity.

**PASS.** The independent literal supplement is `agents/singularities_duality/logs/A162_split_kernel_supplement_audit.md`. We give this structural model no qualifying movement credit: no original row closes and the named comparison gate has not been evaluated or proved strictly smaller.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We claim no priority.

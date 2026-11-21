# F39 complete generated-fragment review

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

Reviewed file: `finding_F39.tex`.

Reviewed SHA256: `f1dc5eccaa3cb5e3bb8ba262e0f40ee6876f45a2f2594186d9be63311fd0e2c4`.

**Result: PASS for the complete mathematical argument.** Two editorial source/format amendments have been requested: extend the point-comparison locator from equations (7.1)–(7.2) to (7.1)–(7.4), because the last two formulas specify normalized Frobenius; place the dictionary paragraph's ordinary `\ell` in math mode. Neither amendment changes the proof. This review is of the complete fragment, not of the eventual whole integrated manuscript.

## Direct proof checks

The resolution has rightmost positive differential multiplication by \(u=x-y\), with the next differential multiplication by \(w=x+y\). In \(S=k[x,y]/(x^2,y^2)\), multiplication by \(u\) has image spanned by (x-y,xy) and kernel spanned by \(x+y,xy\). Multiplication by \(w\) interchanges those subspaces. The augmentation kernel is the first image, and \(uw=0\). These computations prove every stage of the infinite free resolution, including the augmentation.

On the diagonal \(x=y=\epsilon\), the differentials become zero in odd homological degrees and \(2\epsilon\) in even homological degrees. Because the stated characteristic is greater than three, the displayed odd and even Hochschild groups follow exactly. In particular they are nonzero in every positive degree. A bounded perfect diagonal would have bounded derived tensor with the ordinary module \(B\), contradicting those Tor groups.

The transfer from the dual-number block to the actual algebra is valid. Restriction along a central product-block idempotent takes finitely generated projectives to finitely generated projectives. Matrix Morita equivalence on the two sides then carries the diagonal of \(M_2(B)\) to the diagonal of \(B\) and preserves perfectness. The actual algebra is finite dimensional, so it is proper. Its perfect dg category has the same smoothness defect. This step concerns the abstract collision algebra from F19, rather than a different faithful matrix image.

At split good fibers, the stated Chinese-remainder decomposition from F19 gives two scalar blocks and two matrix blocks. Matrix Morita equivalence gives four rational points; the semisimple quotient at collision gives only three. For a rational point the only crystalline cohomology is degree zero with Frobenius one, so the normalized even spectrum and empty odd spectrum follow. The square-zero matrix ideal is exactly the radical. No nilpotent information is retained by the three-point quotient.

## Primary source verification

I reopened Tabuada's primary arXiv PDF through the search tool. The inspected document identifies itself as arXiv:1808.00950v7, 6 December 2019, with a first-page manuscript date of 9 December 2019. Exact inspected locators are §1 pp.2–3 (domain and conjecture, Theorem1.5), §5.1 pp.13–14 (proper and smooth definitions), §6.1 pp.15–16 (cyclotomic construction), and §7 equations (7.1)–(7.4), p.17 (cohomology and normalized action). The general source theory is invoked, not claimed independently reproved.

Primary URL: https://arxiv.org/pdf/1808.00950

Retrieved source references: `turn608497332view0`, `turn698137661view0`, `turn698137661view2`, `turn698137661view3`.

## Scope check

The fragment correctly excludes this particular nonsmooth perfect dg category from a conjecture whose domain already requires smoothness. It does not refute the conjecture, preclude smooth replacements, or assert compatibility of a replacement with nonstandard based operations. Cyclotomic Frobenius is explicitly distinguished from matrix \(p\)-th powers and from the quantum parameter. The Grothendieck paragraph distinguishes classical affine/perfect-complex language from the modern noncommutative theory and does not assign this argument to the unpublished archive.


## Requested edits verified

The current fragment has SHA256 e67bdffef7b54e109217490bc8518807d4bcdfd595cd3b7018c0d4e504e21da7. Direct inspection confirms equations (7.1)–(7.4) and math-mode ell are now present. Both requested editorial amendments are resolved. The complete mathematical PASS above remains unchanged; this additional event does not claim a whole-main-paper review.

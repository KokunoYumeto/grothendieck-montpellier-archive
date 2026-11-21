# DP62 source assistance — relative multiplication and canonical metrics

Checker: `/root/archive_binomial`, GPT-6 Astra Pro; effort not exposed. Date2026-11-21 UTC. This is a targeted source reading and elementary relative-corollary check, **not** a whole-proof review of DP62.

## Relative multiplication, with exact primary locators

The following statements were directly opened and read at04:00:45 UTC:

1. Stacks Project, Lemma39.9.8, Tag0BFG, https://stacks.math.columbia.edu/tag/0BFG : multiplication by a nonzero integer on an abelian variety over a field is finite locally free of the indicated degree. Retrieval `turn107888672view1`.
2. Stacks Project, Lemma37.16.4, Tag039E, https://stacks.math.columbia.edu/tag/039E : an S-morphism X→Y is flat if X is flat and locally of finite presentation overS, Y is locally of finite type overS, and every fibre morphism is flat. Retrieval `turn107888672view2`.
3. Stacks Project, Lemma37.44.1, Tag02LS, https://stacks.math.columbia.edu/tag/02LS : finite is equivalent to proper with finite fibres. Retrieval `turn107888672view0`.

**Exact relative corollary.** Let A/S be an abelian scheme of relative dimensiong and N>0. The morphism [N]:A→A is proper because A is proper overS and its target is separated overS. Its fibres overS are multiplication byN on abelian varieties, hence finite locally free of degreeN^(2g) by0BFG, including at residue characteristics dividingN. Its fibres over points of the target are therefore finite, so02LS makes the whole morphism finite. The smooth source is flat and locally of finite presentation overS, and the smooth target is locally of finite type. Tag039E now makes [N] flat. Over the noetherian bases used here, finite flat implies finite locally free; its rank is read on the fibres and equalsN^(2g). It is surjective because every field fibre has positive finite locally free rank. Pullback along the identity gives finite locally free A[N]/S. This proves precisely the relative input needed for extending torsion points, without an invertibility assumption onN.

## Canonical metric statement actually read

At04:01 UTC I independently opened and read de Jong–Shokrieh, *Faltings height and Neron–Tate height of a theta divisor*, Compositio Mathematica158(2022), §12.2, from the published primary article:

https://www.cambridge.org/core/journals/compositio-mathematica/article/faltings-height-and-nerontate-height-of-a-theta-divisor/EEEA4CD22A6248EAC82F11C339C6F6F1

Retrieval `turn628240879view1`, lines1174–1182 in that rendering. It explicitly states uniqueness of the smooth Hermitian metric characterized by an isometric rigidification and translation-invariant curvature, and locates the original statement at Moret-Bailly, *Pinceaux de varietes abeliennes*, PropositionII.2.1. It also states the canonical [2]-pullback isometry. **I did not read the original Moret-Bailly page in this check.** Recovering its catalogue or PDF URL is not counted as reading its theorem.

## Algebraic normalization identity independently verified

If N is odd, U is a local theta lift, c=iota(U)U and d=U^N are central units, then c^N=d². Set a=c^((N−1)/2)/d. Direct multiplication gives a²c=1 and a^N d=1. Replacing U byuU changes a tou^−1a, so aU is independent of the local lift and glues. This uses only units and integer powers, not extraction of roots or division byN. It remains valid at primes dividingN. It does not independently establish the representability or torsor hypothesis of the theta group; those are separate exact inputs in DP62.

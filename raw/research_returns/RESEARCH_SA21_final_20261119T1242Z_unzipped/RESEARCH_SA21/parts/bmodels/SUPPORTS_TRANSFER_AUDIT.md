# Independent audit of the support-transfer proof

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. Auditor: /root/bmodels. Target: parts/supports/supports_transfer.tex. No edits were made to the target.

## SA21-A26: all-poset comparison — pass

The split-poset map sends point symbols to the vertical intervals and interval symbols to upper-to-lower intervals. Its endpoint inequalities give exactly the original disjunction relation, including endpoint touching. Every strict quotient is the concatenation of at most three image symbols. A quotient is orthogonal to another precisely when all of its concatenated pieces are: a change of side between adjacent pieces would force the quotient's upper endpoint below its lower endpoint. Thus E(B), defined by containment of all pieces in B, commutes with polar. The trace and E maps are inverse on closed sets. Empty orders and infinite orders are covered without a finiteness premise.

## SA21-A27a: finite conditionally complete sufficiency — pass

Adjoining a new strict bottom and top to a finite conditional lattice gives a finite bounded lattice. For a closed subset of the induced quotient orthoset, closure in the larger quotient space has the original set as its trace. The proof uses the bounded chain-type description only in the larger space and explicitly analyzes each trace block; it does not assume orthomodularity is inherited by arbitrary induced subspaces.

The four trace types are bounded intervals, lower rays, upper rays and the whole quotient space. A maximal orthogonal family restricts to a maximal family in each nonempty block, since all different blocks are orthogonal. Within a finite block no gap between successive quotients can remain: its quotient could otherwise be added. In a lower ray the terminal endpoint is the ray bound and the first endpoint is minimal in the whole original poset, since a predecessor would yield an addable quotient still in the ray. Hence its polar consists exactly of quotients above the bound. The upper-ray argument is dual. A maximal family in a whole block has empty polar. Intersecting the block polars gives the original closed set's polar. Dacey's criterion therefore applies. Empty blocks and disconnected original posets cause no missing case.

## SA21-A27: exact finite necessity and cut formulas — pass

The split poset is conditionally a lattice precisely when the original poset is: for incomparable base elements the meet carries the plus copy and the join the minus copy; comparable copies are handled directly. If a bounded pair has no join, its common-upper cut U and lower closure I satisfy I-up=U and I intersect U is empty. The latter would otherwise give the least upper bound. Finiteness supplies two incomparable maximal elements a,b of I and a global minimal element m below a.

The quotient sets supported in the split copies of I and U are mutual polars. Orthogonality to each vertical quotient over I cannot place a tested quotient below one of them, since that would put it in the same internally nonorthogonal set. It must therefore be above all of them, placing its lower base in U; the converse and dual are direct. The single quotient from m-minus to a-plus is maximal orthogonal in the I-side because m is globally minimal and a maximal in I. For any u in U, the quotient from a-plus to u-minus is orthogonal to this singleton but not to the vertical quotient over b: either direction would contradict I intersect U empty or maximal incomparability of a,b. Thus the singleton does not generate the closed set, disproving Dacey. Missing meets are dual.

## SA21-A28: the opened2022 arXiv version’s unbounded criterion — pass

Two disjoint two-element chains have two strict quotient symbols, with no orthogonal pair. Every nonempty singleton therefore closes to the whole orthoset although a singleton is downward closed in the quotient order. This directly refutes the unrestricted Corollary4.5 in the opened2022 arXiv:2206.08113v1 text. It does not assert that an uninspected later journal version has identical wording. The supplied bounded replacement has the requisite quotient witnesses from the global bottom or to the global top; failure of the tested inequality makes those quotients proper.

No substantive gap was found. These are independent targeted proof checks, not a claim that the argument was externally peer reviewed.



# Independent audit of part (d) of the support theorem

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. Auditor /root/bmodels. Target: the final addition to SA21-A16 in parts/supports/supports.tex. No target edits made.

## Source and type

The supplied J156-7-12_transcription.tex, lines17–20 (scan94), explicitly states part(d): for an incidence-closed A=deployment(G), S_A=Supp(G). Lines28–37 (scan95) reduce it to equality of the whole-figure disjointness tests. J156-7-11_transcription.tex, lines108–127 (scan90), defines the operative open set X-circle as those Y refining X and disjoint from its boundary. Its earlier polar-intersection definition is at lines10–18 (scan87); At supp1 and the following corollary compare those definitions. J156-7-12_transcription.tex, lines204–214, explains the small-lieu support version.

Use E=M with the OLD whole-figure disjunction ∥ on elementary figures, and write N∥ for that polarity. It is not the modern internal disjunction. For any figure G, set A=deployment(G)⊂M and Supp(G)=N∥²(A). Whole-figure disjointness satisfies Z∥G iff Z∥X for every X∈A, by compatibility-by-strata and the zero-intersection condition.

## Exact general criterion

If V_X⊂M is the actual open-stratum set used in defining S_A, then

S_A = Supp(G)

is equivalent to

N∥(⋃_{X∈A} V_X) = N∥(A).

This equivalence follows by taking N∥ and using N∥³=N∥, in both directions. Pointwise, the exact extra condition is

for every Z∈M,
[for every X∈A, Z∥X]
iff
[for every X∈A and v∈V_X, Z∥v].

This is the proposed incidence-coverage condition, correctly typed. It is independent of the two-neighbourhood condition for the lattice clauses(a)–(c). For a completely general atelier, the V_X here must remain the actual open-stratum sets; replacing them by open-lieu sets requires a separate polar-equivalence proof. Empty G gives equality of the two empty unions and is automatic.

## Automatic part(d) under the old hypotheses

Let L be the lieux, ell(Y) their full refinement shadow, and U_X={p∈L:p rho X} the open-lieu set. Carrier decomposition gives the disjoint union

ell(G) = ⋃_{X∈deployment(G)} U_X.

The old L2 tests whole-figure disjunction on FULL lieu shadows. It gives

Z∥G
iff every p∈ell(Z), q∈ell(G) has p∥q
iff for every X∈deployment(G), q∈U_X, Z∥q.

In the last step L2 is applied to the elementary point q, whose full shadow is {q}. Hence the two required polars agree. No orthomodular or Boolean hypothesis is used, and no finiteness is required.

## Comparing the literal open sets and open-lieu sets

For the scan90 definition V_X={Y≪X:Y∥boundary(X)}, one has U_X⊂V_X: a point with carrier X is orthogonal to every boundary carrier by L3 and hence to the boundary by L2.

Conversely every Y∈V_X has ell(Y)⊂ell(X) by refinement, and no point of ell(Y) lies in ell(boundary(X)), since Y is disjoint from the boundary and L2 is irreflexive on points. Thus ell(Y)⊂U_X. If Z is orthogonal to every point of U_X, old L2 makes Z orthogonal to Y. Together with U_X⊂V_X, this proves

N∥(V_X)=N∥(U_X).

Taking unions over any A proves that the original S_A is exactly its open-lieu version. If the earlier polar-intersection definition of X-circle is used, the old At supp1/corollary identifies it with this operative definition. The stated older hypothesis package includes those assumptions.

## Integration wording

A16's abstract orthoset statement characterizes lattice clauses(a)–(c); part(d) is the additional exact incidence-coverage criterion above and is automatic under the old hypotheses. The unrestricted orthogonal-family statement in A17 likewise concerns the lattice clauses: a bare orthomodular lattice and orthogonal family have no figure G or incidence deployment from which part(d) could be stated.

Verdict: the root's proposed repair is correct with these explicit type and scope qualifications.


## Actual integrated paragraph reread

The final A16/A17 text was reread after integration. Its definitions U_X for actual open subsets, V_X for open lieux, E=M with old whole-figure disjunction, the equality of their polars, the absorption/D0 comparison of scans87 and90, and the independent exact coverage criterion all pass. A17 now explicitly restricts the abstract orthomodular argument to lattice clauses(a)–(c), as required. A minor explicit indexing addition was recommended: set I=deployment(F) for an admitted figure F and quantify G≤F, so S_deployment(G) has its index subset stated in the theorem itself. No substantive mathematical gap remains.

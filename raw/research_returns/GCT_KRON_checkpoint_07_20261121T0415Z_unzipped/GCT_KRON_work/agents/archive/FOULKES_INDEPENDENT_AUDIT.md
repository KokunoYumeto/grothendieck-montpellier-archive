# Independent proof audit: quadratic Foulkes–Howe stabilization

Run GCT_KRON_20261120. Agent /root/archive_audit. Checker GPT-6 Astra Pro; effort not exposed. Completed 2026-11-20T23:58:04.483707+00:00.

## Source and scope

OpenAI, *Quadratic stabilization of the canonical Foulkes–Howe map*, dated September 25, 2026. Primary source: https://github.com/openai/math/blob/main/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/build/paper.tex . Local source: external_sources/Foulkes_quadratic_20260925.tex (474 lines). SHA-256: 6b4eb1977533b9b1503927a55687c72afd9dc68b05b27b94cf404413195dd2c2.

Status: independent-agent full reading of the written mathematical proof, not formal verification and not a claim about any Lean implementation. Theorem 1 is at source lines 99–103; Lemma 2 at 260–291; Proposition 3 at 304–430; theorem conclusion at 432–436. The proposition asserts that a symmetric a-linear form on Sym^b V vanishing diagonally on all products of b vectors is zero for b >= a(a−1), over a finite-dimensional complex vector space.

## Critical checks

| Location | Independent check | Result |
|---|---|---|
| 185–222 | Polarization has coefficient k!; averaging followed by the symmetric quotient is identity. Products of degree-one generators give precisely the stated diagonal product tensors, so the annihilator criterion is for the canonical image. | PASS |
| 267–290 | Direct calculation with D=Y·∂U and E=U·∂Y gives ED−DE=NU−NY. Under monomial norm squared alpha!, D*=E, hence norm(Dh)^2−norm(Eh)^2=(p−q)norm(h)^2. This sign gives injectivity when p>q. Spectator variables do not affect the commutator. | PASS |
| 328–348 | Substitution into the binary factorization is valid even when x and t are dependent; coefficient of c is a times the required mixed evaluation. | PASS |
| 350–378 | At derivative i, only t is differentiated. Earlier multipliers y_j do not change the new y_i degree, which remains r. The source degree is b−i+1, ending at r+1, so every derivative is injective. | PASS |
| 380–393 | For fixed x,t, the auxiliary form is symmetric r-linear on Sym^m V; m=b−r>=r^2>=r(r−1) and m>=1, exactly satisfying induction. | PASS |
| 395–424 | Each derivative has source v_i; previously inserted x factors are untouched. Across all r^2 derivatives the common x degree is at most r^2−1, while every source degree is at least b−r+1>=r^2+1. The entire composition is therefore injective. | PASS |
| 425–435 | Vanishing on tuples of pure powers implies complete vanishing by independent spanning in every slot; zero-dimensional and a=1 cases are covered. | PASS |

No gap was found in the stated complex characteristic-zero range. This check does not assess the historical priority discussion or external results cited only for context; the core proof is self-contained.

## Independent consequence for the determinant closure (root M-010)

Let V be the vector space of linear forms in n^2 variables, X the closure of the GL(V)-orbit of det_n in Sym^n V, and C the cone of products L_1⋯L_n. Every such product is a substitution into det_n by a diagonal matrix of the L_i. Any linear substitution is a limit of invertible substitutions: GL(V) is Zariski dense in End(V), and polynomial evaluation is continuous. Thus C is contained in X.

A degree-d homogeneous equation F on Sym^n V has a unique symmetric d-linear polarization T in characteristic zero. If it vanishes on C, the diagonal of T vanishes on every product of n vectors. Proposition 3, with a=d and b=n, implies T=0 and hence F=0 whenever d>=2 and n>=d(d−1). The case d=1 follows because products, including pure powers, span Sym^n V; degree zero is immediate.

It follows that I(X)_d is a subspace of I(C)_d=0. Therefore C[X]_d equals the complete ambient module Sym^d((Sym^n V)^*), with every irreducible multiplicity retained. Under the root notation this is K_{n,d}(lambda)=a_{n,d}(lambda) for every partition lambda in that degree. Any competing orbit closure Y in the same affine representation has coordinate module a quotient of the ambient one, so q_{n,d}(lambda)<=K_{n,d}(lambda). Thus an actual multiplicity obstruction requires d(d−1)>n.

The deduction uses Proposition 3 directly and therefore does not require identifying a transpose convention for the canonical Foulkes–Howe map. It does not claim saturation of Kronecker support, and it does not equate orbit-coordinate multiplicity bounds with actual closure multiplicities outside the proved range.

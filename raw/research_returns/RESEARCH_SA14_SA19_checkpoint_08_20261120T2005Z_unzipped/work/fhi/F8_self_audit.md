# F8: targeted self-audit of the Frobenius and nearby-cycle steps

Status: the candidate proof is complete; this note records the particular stress test requested by root. Independent promotion remains with root. BCE separately passed steps 1, 2, and 5.

## Finite monodromy with a p-part

The integer N is divisible only by the orders of boundary tame inertia. It is not assumed to divide or annihilate the full monodromy group. Start with the finite Galois torsor corresponding to the actual monodromy representation. On a root chart, Abhyankar's lemma makes its normalized pullback unramified at every codimension-one point lying over the boundary. All other codimension-one points are already in the étale locus. The chart is excellent and regular, so its finite normalization is étale everywhere by purity. The G-action and descent data extend uniquely from the dense open subset. The resulting sheaf on the root stack is locally constant even when p divides |G|.

Its associated vector bundle V has a unit Frobenius structure F*V ≅ V because its transition matrices lie in GL_r(F_p). A finite étale trivializing cover may still be a stack and may have degree divisible by p. This causes no problem: normalized determinant degrees multiply by a positive rational factor on each connected covering component, so triviality upstairs forces degree zero and forces every subbundle downstairs to have nonpositive degree. No semisimplicity of G-representations is used.

## Step 3: the Frobenius cokernel

On each regular root chart, after completion at a closed point,

R = k[[u,v]],
R ⊗_{R^p} R = R[α,β]/(α^p,β^p).

The pullback of the unit O → F_*O is the section a ↦ a⊗1 of multiplication. Hence F*((F_*O)/O) is canonically isomorphic as an R-module to the augmentation ideal I=(α,β). Its I-adic filtration has degree-a graded piece T^a Ω, with 1≤a≤2(p−1). The ideal and filtration are canonical and therefore commute with chart changes and the tame group action. Sun, Theorem 3.7, pp.12–13, and the local proof pp.6–8 explicitly supply this coordinate calculation; no projectivity assumption is imported into the local calculation.

On a root component, the conormal sequence is a two-line flag with degrees −C_i²/N and 2g_i−2+ν_i(1−1/N), both at most the fixed K_i. The truncated-symmetric representation restricts to an upper-triangular representation on that flag, with one-dimensional weights L_1^u L_2^v, 0≤u,v≤p−1, u+v=a. Thus every line layer has degree at most 2(p−1)K_i. Tensoring by the semistable degree-zero V preserves this upper slope bound for every graded layer. Intersecting an arbitrary subbundle with the filtration, and saturating its graded images if necessary, bounds its degree by the sum of rank times that bound. Frobenius multiplies normalized determinant degree by p. Consequently every subbundle of V⊗B_N has slope at most 2(p−1)K_i/p, uniformly in N and r.

Absolute Frobenius on the tame root stack is representable: on every μ_N stabilizer it induces the automorphism ζ↦ζ^p. It is finite flat on the regular root charts. These facts ensure the module calculations and subbundle pullbacks are typed correctly.

## Step 4: twisted nearby-cycle formulas

Étale locally, V has an F_p basis, so all the Artin–Schreier calculations reduce to Suzuki's scalar calculation (version 4, pp.5–7). The exact pole-lattice sequence is

0 → J^{-m}V/V →^{F−1} J^{-pm}V/V → U_m R^1ΨM → 0.

One can check the kernel directly: in each DVR normal to a boundary component, Frobenius multiplies a pole order by p. A vector with pole order larger than that permitted by J^{-m} cannot have F(v)−v in J^{-pm}. Integrality of a vector whose Artin–Schreier image is regular also follows from normality after choosing the étale F_p basis.

For m≥2, J^{-m}⊂J^{-p(m−1)}, so the linear term vanishes in the associated graded. With Z_N defined by J, Frobenius sends pZ_N to Z_N, and projection formula, using F*V≅V, gives

gr_m R^1ΨM ≅ B_N|_{Z_N} ⊗ V|_{Z_N} ⊗ J^{-m}|_{Z_N}.

The unit map becomes v↦v⊗1 under this formula, so its cokernel really is B_N⊗V, with no extra representation twist. The Frobenius permutation of the μ_N characters is already absorbed in the unit-Frobenius identification of V.

The filtration of O_{Z_N} may have N times as many layers, but the degree of each layer is at most the fixed L_i because the normal/crossing degrees are B_ij/N. The upper slope of each associated-graded layer is therefore at most b_i+L_i−m d_i. The chosen m_0 makes these all negative. No dependence on a hidden trivializing-cover degree occurs.

## Source URLs

- Suzuki: https://arxiv.org/pdf/2207.01563 , §§2–3, pp.4–7.
- Sun: https://arxiv.org/pdf/math/0611360 , Theorem 3.7 pp.12–13 and local proof pp.6–8.
- Abhyankar: https://stacks.math.columbia.edu/tag/0BRM .
- Purity: https://stacks.math.columbia.edu/tag/0BMB .
- Root-stack charts: https://www.charlescadman.com/raw/pdf/stacks.pdf , §§2.3–2.4, pp.7–10.
- Root-curve degrees: https://arxiv.org/pdf/math/0604458 , Theorems 4–5 pp.12,17 and Lemma 15/Proposition 6 p.22.

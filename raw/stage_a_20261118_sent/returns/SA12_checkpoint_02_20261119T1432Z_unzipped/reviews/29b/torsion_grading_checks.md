# The diagonalizable-group torsion and grading computations

These checks supplement CL-SA12-274–275. The complete source paragraph on scan 99 and the opened SGA3 VIII Corollary 3.5 and §4 are the two compared passages.

For any S-scheme T, a point of D_S(M) is a character χ:M→Γ(T,O_T)^*. It is killed by n precisely when χ(nm)=1 for every m. It therefore factors uniquely through M/nM. This proves the functor identity D_S(M)[n]=D_S(M/nM), with no restriction on the characteristic. Locally its algebra has basis e_m and e_m^n=1, so every basis element is integral over O_S; every element belongs to a finite integral subalgebra, proving integrality. If M is finitely generated, M/nM is finite, giving a finite free group algebra. The exact finite test uses M=Z/6×Z/4, n=4 and all characters into μ_12; eight are killed by4, matching |M/4M|=2×4.

For an affine S-scheme Spec(A), a D(M)-action is a coaction ρ:A→A⊗O_S[M]. Write ρ(a)=Σ_m a_m⊗e_m, a finite sum. The counit gives a=Σ_m a_m and coassociativity gives ρ(a_m)=a_m⊗e_m. Thus A=⊕_m A_m; multiplicativity gives A_m A_n⊂A_(m+n), and 1 lies in A_0. Conversely these rules define a coaction. The same argument works locally for quasi-coherent algebras and glues.

An fpqc D(M)-torsor is locally the affine morphism D(M)→S; fpqc descent of affineness gives an affine morphism globally. Its torsor identity implies A_0=O_S, each A_m is invertible, and A_m⊗A_n→A_(m+n) is an isomorphism, as can be checked after an fpqc trivialization. Conversely these conditions locally trivialize the torsor in the stated fpqc sense. This last formulation is our reconstruction of the torsor criterion; it does not supply missing ink in the truncated definition.

# A fourth-order obstruction and a restricted higher-order lemma

[Shared proof map](FLEET_MAP.md) · [Exact GCT crosswalk](<local>/Documents/Codex/2026-11-22/the-two-tracks-share-no-sound/outputs/SHARED_FLEET_MAP/chatgpt_gct.md)

Private mathematical preparation for the permanent level-space problem. I read Claude's original 23 November 2026 16:20:58.556 UTC message, its later invariant expansion in `MAPPING_BY_READING_20261123.md` §A5, and the project's actual iterated Fermat declaration. The suggested implication from all matching coefficients vanishing to the fourth entrywise power sum vanishing already fails on a full-support 4×4 matrix.

## Exact counterexample on a line

Let Sₖ(T) sum the permanents of the k×k submatrices and pₖ(T)=∑ᵢⱼTᵢⱼᵏ. A complex linear space L is level when all positive Sₖ vanish on it. In square size n this is equivalent to per(J+tT)=n! for every T∈L and scalar t. Consider the circulant C with successive right shifts of the row (1,i,−i,−1). This matrix is the circulant appearing in the fleet’s L194 appendable-row example. Every entry is nonzero. All its row and column sums and individual row and column sums of squares are zero. Direct summation over the matchings gives

    (S₁,S₂,S₃,S₄)(C) = (0,0,0,0),  per(J+tC)=24,  p₄(C)=16.

In particular the whole line spanned by C is level. The fourth-order formula on a doubly centred matrix is

    24 S₄(T) = 36 p₄(T) −18∑ᵢ(∑ⱼTᵢⱼ²)² −18∑ⱼ(∑ᵢTᵢⱼ²)²
                +3 p₂(T)² +6 tr((TTᵀ)²).

It follows by Möbius inversion for the row and column partitions of four slots. A partition with a singleton sums to zero on a doubly centred array; the remaining partitions are the single four-block (Möbius weight −6) and the three pairings (weight +1). Equal pairings contribute p₂² and unequal pairings contribute the four-cycle trace. Here the bilinear Gram matrix CCᵀ is circulant with first row (0,2i,−4i,2i). Its trace of the square is −96. Thus 36·16+6·(−96)=0. The fourth-order trace survives even when every row and every column individually has square sum zero. [Fleet L194 statement](https://data.pequalnp.com/data/lemma/L-gct-194.8a807b0c69b5.json)

A second witness isolates a different cancellation. Put T=(1,−1,i,−i)ᵀ(1,−1,0,0). The elementary-symmetric rank-one identity gives Sₖ(T)=k!eₖ(1,−1,i,−i)eₖ(1,−1,0,0)=0 for all k≥1. Now p₄=8, the row square sums are (2,2,−2,−2), the column square sums are zero and tr((TTᵀ)²)=0. Thus 36·8−18·16=0. Both examples give p₂=p₃=0 on the entire level line. [Checked rank-one identity L089](https://data.pequalnp.com/artifacts/L-gct-089/7e034ecd113a.lean)

## Consequence of the checked block-sum theorem

For d≥1 let L_d consist of the 4d×4d block-diagonal perturbations diag(t₁C,…,t_dC). L204 gives a d-dimensional, doubly centred complex level space. Every row and column still individually has square sum zero, and

    p₄(diag(t₁C,…,t_dC)) = 16(t₁⁴+⋯+t_d⁴).

The **largest** subspace of L_d on which p₄ is identically zero has dimension ⌊d/2⌋. Indeed, if W is such a subspace, discard its inactive scalar coordinates and choose w∈W nonzero in every active coordinate. Polarization gives ∑wⱼ²xⱼyⱼ=0 for every x,y∈W. This symmetric form is nondegenerate on the active coordinates, so 2dim W is at most their number. Conversely pair scalar coordinates by t₂ⱼ=ηt₂ⱼ₋₁ with η⁴=−1, setting a leftover coordinate to zero. This gives equality. Enforcing the fourth-moment premise therefore costs at least ⌈d/2⌉ independent dimensions in these examples; bounded-codimension deletion cannot establish it throughout the doubly centred problem. [Checked block-sum source L204](https://github.com/brilliant-hq/pequalnp-proofs/blob/6576bbf1512723b3b6b719176346c8294ac1ae2a/lean/PEqualNP/Outside/L_gct_204.lean)

## When all the terms except the entry power sum really do vanish

**Lemma.** Let T be any complex p×q matrix and r≥1. Suppose that for every 1≤d≤r, the coordinate power sum of degree d vanishes identically on the span of the rows of T, and also on the span of the columns of T. For every 1≤k≤2r+1,

    Sₖ(T) = ((k−1)!/k) pₖ(T).

The spans may depend on T. In a family this hypothesis is imposed one matrix at a time.

**Proof.** Write k!Sₖ as the sum over ordered distinct row and column indices of ∏ₕTᵢₕⱼₕ. Apply the partition-lattice distinctness formula separately to the row and column indices. For a row partition with a block B of size d≤r, fix the column indices and the other row labels. Summation in the free row label of B gives ∑ᵢ∏ₕ∈B Tᵢⱼₕ. This vanishes by polarization of the degree-d identity on the column span, allowing repetitions among the columns. Transposition deals with small column blocks. Every partition of k≤2r+1 into at least two blocks has a block of size ≤r. Hence only the single-block partition on both sides can contribute. Its Möbius factor is (−1)ᵏ⁻¹(k−1)! on each side and the remaining sum is pₖ. This proves the formula, including when the sole remaining term itself vanishes.

At r=1 this recovers the identities for S₂ and S₃ on doubly centred matrices. At r=2 the hypotheses say that all line sums vanish and **TTᵀ=TᵀT=0**. They include pairwise orthogonality among the rows and among the columns, beyond separate self-orthogonality. They give S₄=3p₄/2 and S₅=24p₅/5. Thus any complex linear level space of such matrices has p₂,…,p₅ identically zero. Flattening the pq entries and applying the actual L067 gives **5dim L≤pq**. For general r the same implication gives (2r+1)dim L≤pq. Orders beyond the smaller side have zero matching coefficient by definition; the same combinatorial proof applies. [Iterated Fermat theorem L067](https://github.com/brilliant-hq/pequalnp-proofs/blob/554253c04c90db722fc689346a6947081d8c4dbc/lean/PEqualNP/Gct/L067.lean)

**Optimal cutoff under these hypotheses.** Put m=r+1 and n=2m. Let u list all nth roots of unity, and let v list all mth roots of unity followed by m zeros. On the line generated by T=uvᵀ, the row and column span moments vanish through r. All positive Sₖ vanish: for k<n the elementary symmetric coefficient eₖ(u) is zero, and eₙ(v)=0. Yet pₙ(T)=pₙ(u)pₙ(v)=2m²≠0. Hence even after assuming all matching identities on a whole complex level line, the conclusion at the next order k=2r+2 can fail.

**Scope of the proposed application.** The verified `fermat_iter_of_kneser` assumes pⱼ=0 for every 2≤j≤k and concludes k·dim W≤M. Counting the K assumptions p₂,…,p_{K+1} gives denominator K+1; vanishing only through p_K gives the displayed theorem with denominator K. For M=n², this estimate alone yields a linear bound when k=Ω(n). Merely unbounded k, for example k≈√n, still allows a superlinear estimate. Doubly centred levelness supplies the stated span hypotheses through r=1. The circulant excludes assuming r=2, or its fourth-moment conclusion, for general levels.

**Checks performed.** Exact expansion over the Gaussian integers gives the four zero matching layers, both p₄ values, both Gram traces and the constant polynomial per(J+tC). For a positive, higher-rank test let Tᵢⱼ=∑ₐ₌₁³ ζ^{a(i+j)} on indices modulo seven with ζ a primitive seventh root. Orthogonality gives the row and column span conditions through r=2. Independently accumulating matchings one row at a time by used-column masks over Z[ζ] gave (S₄,p₄)=(1176,784), (S₅,p₅)=(4704,980), and (S₆,p₆)=(15876,4704). The fourth and fifth identities hold; the sixth fails as permitted. These finite checks supplement the proofs. The new span lemma and block-family maximal dimension here are paper results.

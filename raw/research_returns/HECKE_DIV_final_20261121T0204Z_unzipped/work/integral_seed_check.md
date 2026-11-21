# P2b / R27: independent check of the integral Weil seeds

Date: 2026-11-21 UTC. Checker: GPT-6 Astra Pro; reasoning effort not exposed; agent /root/reductions. This is an independent mathematical derivation from coordinates, followed by comparison with the root's proposed formulas and `work/integral_seeds.py`/`.json`. No rerun of the same exterior-algebra implementation is counted as an independent proof.

## Verdict and conventions

All proposed identities and numerical upper bounds are correct with the following explicit convention. Choose ω=(−1+√−3)/2 with positive imaginary part; write a point on E=C/(Z+Zω) as z=s+ωt. Let e=ds and f=dt denote the integral cohomology classes dual to the lattice basis (1,ω), so ∫_E e∧f=1. The degree of an r-dimensional cycle is ∫θ^r[Z], without division by r!.

Set A_0=E_x^n×E_y^n with the balanced action a·(x,y)=(ax,bar(a)y), and take the product principal polarization. The result supplies explicit integral representatives for a full integral basis of the Weil plane at A_0. It does not produce a uniform representative on its Hecke orbit; raw pullback still has a factor m^{2n} in degree and multiplier.

## 1. Direct computation on one pair E_x×E_y

Suppress the pair index. The holomorphic and antiholomorphic forms are

    dz_x=e_x+ωf_x,       dbar z_y=e_y+ω²f_y.

Expanding, and using ω²=−1−ω and ω³=1, gives

    ζ=dz_x∧dbar z_y=U+ωV,
    U=e_x∧e_y−e_x∧f_y+f_x∧f_y,
    V=f_x∧e_y−e_x∧f_y.

Both U and V are integral. They are of type(1,1), since ζ and its complex conjugate are of type(1,1) and ω≠barω.

Let F_x={0}×E_y and F_y=E_x×{0}; their sum has class

    θ=e_x∧f_x+e_y∧f_y.

Interchanging the names F_x,F_y has no effect on any formula below. For b∈O_K let Γ_b be the graph y=bx. Its cohomology class is the pullback of the point class on E by the homomorphism (x,y)↦y−bx.

For b=1, direct exterior multiplication gives

    [Γ_1]=(e_y−e_x)∧(f_y−f_x)=θ+V.

For b=ω, multiplication by ω acts on real coordinates as

    (s,t)↦(−t,s−t),

hence m_ω^*e=−f and m_ω^*f=e−f. Therefore

    [Γ_ω]=(e_y+f_x)∧(f_y−e_x+f_x)
          =θ+e_x∧e_y−f_x∧e_y+f_x∧f_y
          =θ+U−V.

Solving proves the proposed divisor formulas:

    V=[Γ_1]−[F_x]−[F_y],
    U=[Γ_ω]+[Γ_1]−2[F_x]−2[F_y].

This computes the actual classes of the specified graphs. Their self-intersections and pairwise intersection numbers alone would not uniquely certify these identities.

Each fibre divisor F_x,F_y has θ-degree1. Both graph divisors have θ-degree2, because their projections to each factor have degree1 (ω is a unit). Thus the displayed representatives have equal positive and negative degrees:

    deg(U^+)=deg(U^-)=4,
    deg(V^+)=deg(V^-)=2.

The identities are identities of cohomology classes represented by the displayed integral signed divisors. They need not be recast as claims about equality of particular Chow classes if only cohomology is intended.

## 2. Pairing and orientation on the pair

Put vol=e_x∧f_x∧e_y∧f_y. We have

    dz∧dbar z=(ω²−ω)e∧f=−i√3 e∧f.

To put ζ∧barζ in the order dz_x,dbar z_x,dz_y,dbar z_y requires two exchanges of one-forms. Consequently

    ∫ζ∧barζ=(−i√3)²=−3.

Also ζ²=0 because dz_x appears twice. Since U,V have even cohomological degree,

    0=(U+ωV)²=(U²−V²)+ω(2UV−V²),

so U²=V²=2UV. On the other hand,

    ζbarζ=U²−UV+V²=3UV.

Integrating gives

    ∫U²=−2,  ∫UV=−1,  ∫V²=−2.

In particular [Γ_1]²=[Γ_ω]²=0 and [Γ_1]·[Γ_ω]=3, consistently with the degree of the isogeny 1−ω. These are consequences and useful checks of the directly derived graph formulas.

## 3. The global Weil forms and their full integral lattice

Index the pairs by j=1,…,n and put ζ_j=U_j+ωV_j. Define

    Ω=dz_{x_1}∧…∧dz_{x_n}∧dbar z_{y_1}∧…∧dbar z_{y_n}.

Moving the j-th y-form in the product ∏ζ_j past the n−j later x-forms yields

    Ω=(−1)^{n(n−1)/2} ∏_{j=1}^n(U_j+ωV_j)=u+ωv.

Here u and v are integral because the entire expansion takes place in Z[ω] tensored with integral cohomology. For n=2 the prefactor is−1; for n=4 it is+1. This sign must be retained in actual cycle formulas, although it does not affect the pairing or the symmetric upper bounds for positive and negative degrees.

For the balanced K-action, dz_{x_j} and dbar z_{y_j} all lie in the same K-embedding eigenspace of H^1. They form a basis of that 2n-dimensional eigenspace. Thus Ω is its top exterior form, barΩ is the other extreme form, and their rational plane is exactly the Weil plane W_Q. Since ω∉Q and Ω,barΩ are independent, u,v form a rational basis of W_Q.

To check saturation, use the integral exterior basis obtained by ordering the elliptic factors x_1,…,x_n,y_1,…,y_n, with e,f in each factor. In Ω's expansion the coefficient of the all-e exterior monomial is1. The coefficient of the monomial obtained by replacing e_{x_1} with f_{x_1} isω. Hence the corresponding two coordinate functionals take values

    u ↦ (1,0),          v ↦ (0,1).

If au+bv, with a,b rational, is an integral cohomology class, these two exterior coordinates force a,b∈Z. Therefore

    W_Q ∩ H^{2n}(A_0,Z)=Zu⊕Zv.

This establishes the **full integral Weil lattice**, not just a finite-index integral sublattice. It uses the coefficient expansion of Ω in the specified global order, so it is unaffected by the separate sign in the product-of-pairs expression.

## 4. Gram matrix

Reordering the degree-two forms ζ_j and barζ_j incurs no signs. Reordering the real four-dimensional pair factors into the global order likewise incurs no signs, since each interchange moves two one-forms past two one-forms. Hence

    ∫_{A_0}Ω∧barΩ=∏_j∫_{E²}ζ_j∧barζ_j=(−3)^n.

The identity Ω²=0 gives u²=v²=2uv. It follows that

    ∫uv=(−1)^n3^{n−1},
    ∫u²=∫v²=2(−1)^n3^{n−1}.

For Q_W(a,b)=(−1)^n∫ab, the Gram matrix in the saturated basis u,v is

    G_n=3^{n−1} [[2,1],[1,2]],       det G_n=3^{2n−1}.

It is positive definite. In the requested cases:

| n | Dimension of A_0 | G_n | det G_n |
|---:|---:|---|---:|
| 2 | 4 | [[6,3],[3,6]] | 27 |
| 4 | 8 | [[54,27],[27,54]] | 2187 |

## 5. Explicit signed cycles and degree bounds

For I⊂{1,…,n}, define the signed cycle M_I by taking the external product of V_j's displayed signed-divisor representative for j∈I and U_j's representative for j∉I. Let k=|I|. Each sign choice in the expanded product is an effective n-cycle. Its degree for the product polarization is

    n! ·4^{n−k}·2^k = n!2^{2n−k}.

The factor n! comes from the coefficient of θ_1⋯θ_n in (θ_1+⋯+θ_n)^n. All other monomials restrict to zero on the product of n curves: a factor is either missing or repeated. Among the 2^n sign choices, exactly2^{n−1} are positive and2^{n−1} negative. Therefore M_I has effective positive and negative parts each of degree

    b_{n,k}=n!2^{3n−k−1}.

For ω^k=α_k+ωβ_k, the pairs (α_k,β_k) repeat with period3:

    (1,0), (0,1), (−1,−1).

The global signed cycles

    C_u=(−1)^{n(n−1)/2} Σ_I α_|I| M_I,
    C_v=(−1)^{n(n−1)/2} Σ_I β_|I| M_I

have classes u and v, respectively. Splitting these displayed signed sums into effective positive and negative parts gives the upper bounds

    D_u=Σ_{k=0}^n binom(n,k)|α_k| b_{n,k},
    D_v=Σ_{k=0}^n binom(n,k)|β_k| b_{n,k}.

No moving lemma is needed for these products: the factors lie on disjoint pair factors, so they are external products of effective divisors, including their multiplicities. We do not need to intersect arbitrary effective divisors on one variety.

For n=2, b_{2,0}=64, b_{2,1}=32, b_{2,2}=16, hence

    D_u=64+16=80,
    D_v=2·32+16=80.

For n=4, the b-values for k=0,…,4 are49152,24576,12288,6144,3072. Thus

    D_u=49152+6·12288+4·6144=147456,
    D_v=4·24576+6·12288+3072=175104.

Each number bounds **each effective sign**, not merely a signed numerical degree. The clearing multiplier is N=1 because the signed cycles are integral. No minimality is asserted; cancellation and alternative signed decompositions may improve these bounds.

## 6. Raw Hecke pullback and a fixed arbitrary target

Let h be a rational special-unitary isometry carrying the marked point A_x to A_0, and let m clear its integral lattice denominator. For the corresponding isogeny f:A_x→A_0, the established conventions give

    f^*θ_0=m²θ_x,         deg f=m^{4n},
    f^*u_0=m^{2n}u_x,     f^*v_0=m^{2n}v_x.

The action on W is trivial for h because det_K h=1. Flat pullback preserves effectivity. The projection formula gives, for every effective n-cycle Z,

    deg_{θ_x}f^*Z=m^{−2n}deg(f)deg_{θ_0}Z
                    =m^{2n}deg_{θ_0}Z.

Therefore the integral basis has raw chosen representatives

| Dimension | Multiplier | Bound for each sign for u_x | Bound for each sign for v_x |
|---:|---:|---:|---:|
| 4 | m^4 | 80m^4 | 80m^4 |
| 8 | m^8 | 147456m^8 | 175104m^8 |

For a fixed rational class t=au+bv choose q≥1 with qa,qb∈Z. Then

    N_x=q m^{2n},
    D_x≤m^{2n} (|qa|D_u+|qb|D_v)

is a correct upper bound for these chosen representatives. These formulas substantially improve the old projected-graph seed bounds but do not eliminate the growing m^{2n}. They neither prove nor refute uniform bounded division, which concerns the existence of other representatives.

For an arbitrary rational unitary similitude the action on W can rotate this two-dimensional plane by its K-determinant; retaining the special-unitary convention or explicitly inserting the resulting2×2 rational matrix remains necessary.

## Checks actually completed

1. Independent coordinate derivation of Γ_1 and Γ_ω; identification of U,V as divisor classes; verification of the sign and degree conventions.
2. Independent wedge-product derivation of the pair and global Gram matrices, without relying on the root's integer-mask computation.
3. Saturation proof using two integral exterior coordinates.
4. Independent signed external-product degree count and arithmetic evaluation of the four bounds80,80,147456,175104.
5. Re-derivation of the Hecke pullback factors using the projection formula.
6. Comparison with root's `integral_seeds.py` and its JSON output: agreement. This is recorded as a proof check and arithmetic comparison, not as a second independent computational implementation.

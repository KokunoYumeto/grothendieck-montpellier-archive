# An actual one-cover proper-integral shear with nonintegral affine block

19 November 2026. Work only. This is the reverse of the E.2.29 boundary-moving construction on its same actual A5 cover. It supplies an actual continuous IA automorphism of the free profinite group, with the specified action at this cover. It does not assert preservation of all peripheral subgroups, all other cover lattices, or membership in the Galois image.

## 1. Frozen actual modules and explicit integral maps

Retain exactly the Cayley-graph basis, 44 cusp columns B, 61-dimensional affine lattice L, and rank18 proper quotient W=L/B from E.2.29. The boundary lattice is saturated of rank43. The frozen JSON work/build_A5_boundary_nilpotent.json has SHA256 ba0e10ed1fc1eb306fafdfbb2e77fe3ed38f17f5ba0f5593188f59203872b111. The new program reads that exact file and reconstructs the actual H=A5 action rho from its cycle chains. The standard four-dimensional representation is V, with matrices v(h).

The previous maps S:V->L and T:L->V, averaging projector E with E^2=60E and image B_Q, first actual cusp b, and integer proper functional q:L->Z with qB=0 are retained. Choose ell=e_0^* in V^* and v0=e_0 in V. The literal maps

    R = sum_(h in H) rho(h) b ell v(h)^(-1) : V -> B,
    U = sum_(h in H) v(h) v0 q rho(h)^(-1) : L -> V

are integral and H-equivariant. Each term in R lies in the actual integral boundary lattice. Every term in U kills B, so U factors through the actual proper quotient. Exact computation gives

    T R = 900 I_4,       U S = -25200 I_4.

Thus R is injective over Q and U is surjective over Q. The primitive matrix

    N_rev = R U / 14

has integer entries, rank4, maximum absolute entry11 and gcd of entries1. The program checks all61x61 entries, H-equivariance on x,y, and

    N_rev^2=0,   N_rev B=0,   E N_rev=60N_rev,
    N_rev E=0,   A N_rev=0,

where A:L->Z^2 is the actual base exponent map. It also computes integer coordinates for every column of N_rev in the previously specified unimodular 43-column boundary basis. Therefore its image lies in B integrally, not merely in B_Q. The square-zero assertion follows already from U(B)=0.

## 2. Actual profinite shear and an explicit failure of affine integrality

Let a in Zhat have 2-adic coordinate0 and coordinate1 at every odd prime. Define on the actual completed relation module

    gamma = I + 60 a N_rev : Lhat -> Lhat.

The matrix is continuous, H-equivariant and has inverse I-60aN_rev. It fixes Bhat pointwise and acts identically on What. Hence it preserves the actual proper lattice W, and also the boundary lattice B, at this cover.

Nevertheless it does not preserve L. With zero-based indexing the exact entry N_rev[0,1] is -1. Therefore the first coordinate of gamma(e_1) is -60a. This cannot be an integer: its 2-adic coordinate is zero, forcing any such integer to be zero by the injective map Z->Z_2, while its 3-adic coordinate is the nonzero element -60. This gives a literal nonzero off-diagonal obstruction in Hom(W,Bhat)/Hom(W,B). It is not merely an abstract allowed block shape.

## 3. Extension correction and specified free-profinite lift

Use the same BFS section of Fhat_2->H as E.2.29. Its actual factor set c(h,k) has values in L, and b0(h)=sum_k c(h,k) satisfies delta b0=60c. Put

    eta(h)=a N_rev b0(h).

Then delta eta=60aN_rev c=(gamma-I)c. For the actual profinite extension with multiplication (m,h)(n,k)=(m+rho(h)n+c(h,k),hk), the formula

    (m,h) -> (gamma m+eta(h),h)

defines a continuous extension automorphism fixing H. Since N_rev^2=0, its inverse is (m,h)->((I-60aN_rev)m-eta(h),h). The program verifies the integer coefficient identity delta(N_rev b0)=60N_rev c for all3600 pairs and N_rev(N_rev b0)=0.

Bleher--Chinburg--Lubotzky original v3, Theorem2.1 and especially Corollary2.4, printedpp4--5, lift this specified extension automorphism to an actual continuous alpha in Aut(Fhat_2), fixing the finite quotient H. The source applies to continuous module automorphisms; integrality over Z is not one of its hypotheses.

Every such lift is IA. Naturality of the actual map K_ab=L->F_ab=Z^2 gives alpha_ab A=A gamma=A, since A N_rev=0. The previously checked columns1,6 of A give the minor [[2,1],[-1,-1]] of determinant-1. Thus Ahat is onto Zhat^2 and alpha_ab=I. This conclusion does not depend on the chosen free-profinite lift.

## 4. Exact scope and retained obligation

This is an actual one-cover realization of the nonintegral boundary-extension block in E.2.28: both diagonal homology maps are identity, but the affine integral lattice is not preserved. The constructed lift fixes H and is IA. No claim has been proved that it preserves the conjugacy classes of individual peripheral procyclic subgroups; equality on their abelian classes does not supply that map. No condition at every finite cover is proved. Thus it is not a counterexample inside the actual Galois image, or to the all-cover implication retained after E.2.30.

## 5. Certificate

Program: work/build_A5_reverse_boundary_nilpotent.py. Exact matrices and boundary coordinates: adjacent .json. Output: adjacent .output.txt. Internal runtime0.180026064seconds, exit0. The finite computation verifies integral matrices, all3600 extension identities and the precise witness entry. The nonintegrality of -60a and the continuous extension lifting are the written proofs above; no explicit profinite generator words are claimed.

## 6. The three actual peripheral elements are conjugated in this extension quotient

The following strengthening is at the same finite-cover extension quotient P_N; it does not supply peripheral-preserving lifts in the full free profinite group. It uses the already verified N=N_rev and factor set, with no new matrix identity assumed.

First take the integral extension automorphism alpha_0 with linear part I+60N and correction N b0. For each actual element t=x,y,z=(xy)^(-1), let its quotient in A5 be h, of order d=3,5,5 respectively, and write t=(m_t,h) in the fixed section coordinates. Its displacement is the literal integral vector

    w_t = 60 N m_t + N b0(h),       alpha_0(t)=w_t t.

The actual boundary element t^d belongs to B and is fixed by alpha_0. Since conjugation by t acts on L through h, expanding (w_t t)^d gives

    (I+h+...+h^(d-1)) w_t = 0.

Put S_t=sum_(j=0)^(d-1) j h^j w_t. The preceding equality and h^d=I imply the exact integral identity

    (h-I) S_t = d w_t.

Now rescale the construction to the actual extension automorphism alpha_a with linear part I+3600 a N and correction 60 a N b0. Then alpha_a(t)=60 a w_t t. The element

    v_t = -(60/d) a S_t in Lhat

is defined because d divides60, and conjugation in the extension gives

    v_t t v_t^(-1) = ((I-h)v_t)t = 60 a w_t t = alpha_a(t).

Thus all three specified peripheral elements are individually conjugated by this extension automorphism, using the displayed actual conjugators. The same automorphism fixes completed boundary and proper homology pointwise and has a BCL lift which is IA. Its affine matrix still fails to preserve L: the earlier witness coordinate becomes -3600a and the identical 2-adic/3-adic argument proves nonintegrality.

The three conjugators live in P_N. The BCL lift theorem supplies a lift of the extension automorphism; it does not assert that a chosen lift carries all three full free-profinite peripheral elements to conjugates there. No such simultaneous full-group lift or all-cover/Galois assertion is made.

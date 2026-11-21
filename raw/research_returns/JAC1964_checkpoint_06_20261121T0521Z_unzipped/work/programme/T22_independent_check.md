# Independent check of the positive-genus Artin–Schreier extension

Run JAC1964-20261121. Checker /root/programme_audit, GPT-6 Astra Pro; effort setting not exposed. This note records an independent reconstruction of the geometric and representation-theoretic deductions. The precise Fourier-transform theorems of Katz are carried from root's directly recorded primary-source check; no fresh primary inspection or formal verification is claimed here.

## 1. The simple-pole family and its actual smooth normalization

Let k be algebraically closed of characteristic p>0, fix R≥2 distinct points b_0,...,b_(R−1) of P1 away from the critical set of the old pencil, and choose a coordinate with b_0=0 and all these points finite. Take nonzero constants c_i for i≥1 and let s be the coordinate of Gm. Consider

w^p−w = s/t + Σ_(i=1)^(R−1) c_i/(t−b_i).

The right side has exactly R simple poles. At any such pole use a local target parameter z and write the function c/z+a_reg(z), where c is a unit on the parameter base. Set v=1/w. The equation becomes

(c+z a_reg(z))v^p + z v^(p−1) − z = 0.

At z=v=0 its derivative with respect to z is −1. Thus the normalized branch chart is smooth over the parameter base, with v a relative parameter; solving the equation gives z=c v^p/(1−v^(p−1)−a_reg(z)v^p). This is a genuine normalization chart, not merely a numerical branch calculation. Over the punctured target it has the original Artin–Schreier function field; the chart is normal because it is smooth over a regular base. Away from the poles the original cover is étale. These charts establish a smooth proper family after normalization. The finite map to P1 times the base is flat of degree p: locally it is finite between regular schemes of the same dimension with zero-dimensional fibres, or use the displayed monic equation after dividing by its unit leading coefficient.

For a fixed fibre, that monic equation is Eisenstein at z, so it also proves that the covering field has degree p and the cover is connected. Its derivative with respect to v has valuation p+(p−2)=2p−2, since the coefficient c+z a_reg(z) is fixed over the target local field and p=0. Hence the local different exponent is 2(p−1). Riemann–Hurwitz gives

2g−2 = −2p + 2R(p−1), hence g=(p−1)(R−1).

Every branch value avoids the old critical set. Consequently the pulled-back pencil total space is smooth and proper over the parameter base: near old critical values the covering map is étale; away from them the old pencil morphism is smooth. This verifies the actual model needed for the height argument, including p=2.

## 2. Both nontrivial deck cohomology pieces have infinite parameter monodromy

Put x=1/t. The fixed rational function

a(x)=Σ_(i=1)^(R−1)c_i x/(1−b_i x)

has R−1 simple finite poles and is regular at x=∞. The variable term is s x. For any nontrivial additive deck character indexed by a scalar c∈F_p^*, set M_c=L_psi(c a(x)). It is a nonconstant irreducible rank-one middle extension with finite wild poles, so it is not an additive character sheaf L_psi(d x). Its local representation at infinity is trivial.

Let V be the original variable pencil local system after the reciprocal coordinate change; arrange t=0 to be a smooth pencil value, as above. Then V is also unramified at x=∞. The sheaf V tensor M_c remains irreducible, has rank r≥2, and cannot be an additive rank-one character. It has a rank-one transvection at each of the q old critical points. At each fixed pole of M_c it has Swan conductor r and invariant drop r.

The actual nontrivial deck middle cohomology of the incidence model is

H^(n−1)(A) tensor NFT(M_c)  plus  NFT(V tensor M_c),

with the Fourier parameter scaled by c. This keeps the fixed ambient cross term. Condition A removes punctual old-fibre terms. The outer Leray terms are deck invariant because the relevant sheaves are constant and a curve automorphism acts trivially on H0 and H2. The middle Leray term is permanent, as the base is a curve. The character-piece cohomology is compactly supported on A1 because the varying exponential is wild at infinity for s≠0, so the Fourier identification uses the actual family.

The Euler-characteristic calculation gives

rank NFT(M_c)=2(R−1),
rank NFT(V tensor M_c)=q+2r(R−1).

Indeed each simple finite wild pole contributes invariant drop plus Swan equal to2 in rank1 or2r in rankr; each old critical point contributes1. The new wild character at infinity contributes its rank. H0 and H2 vanish, giving the displayed ranks.

Katz's local formula at Fourier parameter0 identifies W/W^I with the local transform of the input representation at infinity. The latter is trivial of rank1 orr. Therefore the two local representations are respectively

J(1,2) plus J(1,1)^(2R−4),
J(1,2)^r plus J(1,1)^(q+2r(R−2)).

The calculation only uses the exact cited local Fourier rule and Jordan form. A nontrivial-character or wild summand would survive in the quotient by invariants and contradict the trivial quotient; a unipotent block of size greater than2 would do likewise. Both Fourier sheaves are irreducible by the cited Fourier-equivalence theorem and have infinite image because of these nonzero unipotent blocks. An irreducible infinite-image representation has no finite-orbit vector: take the normal core of a hypothetical finite-index stabilizer, whose nonzero invariant subspace would be the whole irreducible representation.

Thus neither the fixed ambient cross term nor the variable piece contains a nonzero finite-orbit vector. Finite algebraic definition of a geometric-generic cycle then annihilates its nontrivial deck cohomology. The usual actual Chow average Z−p^−1 Q^*Q_*Z is globally homologically trivial. On the already admissible domain this gives the exact p^−1 height-norm formula and radical, without asserting that the Chow norm kernel vanishes.

## 3. Every genus-g double cover in characteristic two has the claimed presentation

Let π:C→P1 be a finite degree-two map from a smooth projective geometrically connected curve of genus g≥1 over an algebraically closed field of characteristic2. The finite map is flat, since the target is a smooth curve and π_*O_C is torsion free. Its rank-two algebra A=π_*O_C contains O as a subbundle: the unity vector is nonzero in every fibre algebra and is therefore part of a local basis. Its quotient is a line bundle L^−1, yielding

0 → O → A → L^−1 → 0.

Euler characteristics give deg L=g+1. On P1, Ext1(L^−1,O)=H1(O(g+1))=0, so this sequence splits as a vector bundle. Multiplication on the chosen L^−1 summand is a pair of maps L^−2→O and L^−2→L^−1. They are exactly sections f of L² and h of L. After L≅O(g+1), the algebra is the cover

y²+h y=f,
h∈H0(P1,O(g+1)), f∈H0(P1,O(2g+2)).

The splitting is not canonical; it is only a presentation, which is all the argument needs. A purely inseparable degree-two map of smooth curves to P1 would force C to be a Frobenius twist of P1 and have genus0. Thus the positive-genus covers here are separable. In any case the open condition of being unramified over the nonempty old critical set rules out inseparable maps.

Let T be the smooth-cover, unramified-above-critical open subset of the affine vector space of all pairs (h,f). This ambient parameter space is irreducible. The covers are universally finite flat of degree2 by construction from O plus O(−g−1), and are projective because they are finite over P1. Smoothness is open in this proper flat family. For a smooth fibre, connectedness follows from the Euler characteristic: a disconnected degree-two cover would be two degree-one copies of P1, inconsistent with genus g≥1. Hence T gives the required smooth proper curve family.

It is nonempty and contains the simple-pole family explicitly. Take R=g+1, H(t)=∏_(i=0)^g(t−b_i), and

h=H, f=H²(s/t + Σ_(i=1)^g c_i/(t−b_i)).

This f is a polynomial of degree at most2g+1 and thus is a section of O(2g+2). Setting y=H w identifies the function fields. At a branch point b_i, f'(b_i)=c_i∏_(j≠i)(b_i−b_j)², with c_0=s, so it is nonzero. At infinity h has nonzero leading coefficient, hence the cover is étale. The presentation therefore gives the same smooth normalized curve, not a singular model masquerading as the normalization.

The pulled-back pencil over T is smooth and proper and has the actual lisse kernel projector 1−Q^*Q_*/2. Restriction to the embedded simple-pole family has no finite-orbit vectors by Section2, so neither does the full T representation. No surjectivity from the subfamily's fundamental group is required. The geometric-generic algebraic-cycle argument proves the exact height-norm formula for the full presentation space.

Finally, this is the correct meaning of the geometric generic genus-g double cover: every such cover admits a presentation, and changes of splitting or generator are gauge transformations, not an additional component. If one wants a moduli-stack formulation, the line bundle and splitting can be chosen locally in a base family because relative H1(O(g+1)) vanishes. Thus the irreducible presentation space dominates the corresponding cover moduli. No separate Hurwitz-space irreducibility theorem or conclusion for every specialized cover is needed.

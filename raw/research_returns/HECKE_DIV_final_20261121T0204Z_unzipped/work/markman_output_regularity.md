# Explicit regularity of Markman's genus-three output

Run HECKE_DIV_20261121. Written and checked on 2026-11-21 by `/root/arithmetic`, GPT-6 Astra Pro; effort setting not exposed. This is a new targeted derivation, not a theorem quoted from Markman and not a formal proof-assistant verification. The final independent review by another agent is recorded separately when received.

## M7. Statement and exact hypotheses

Let C be a smooth nonhyperelliptic curve of genus 3, X its principally polarized Jacobian, and identify Xhat with X using the principal polarization. Let Z1 be a disjoint union of thirteen translates of the Abel–Jacobi curve and Z2 a disjoint union of thirteen translates of its reflection. Assume

    H^0(X,I_Z1(2Θ)⊗P)=0 for every P∈Pic^0(X).

Choose the translates to satisfy Markman's other general-position assumptions, so that his reflexive sheaf E below has singular locus of codimension 4. On

    A=X_x×Xhat_α,   Y=X_y×A,
    π:Y→A,         a(y,x)=y+x,

write

    ℒ=O(Θ_y)⊗a*O(Θ)⊗P_(y,α)^(-1),
    D1={y∈Z1},     D2={y+x∈Z2},
    M=ℒ⊗I_D1 I_D2, G=Rπ_*M, E=G^∨[-1].

Let H be the very ample line bundle of numerical class 3(Θ_x+Θ_α). A sheaf F on A is m-regular here if H^i(A,F((m−i)H))=0 for i>0; this equals the regularity of its direct image in the projective embedding by H.

**Claim.** The sheaf E has rank 96 and is 112-regular with respect to H. In particular E(112H) is globally generated.

The source identifications are Markman, supplied `source/LIT_Markman_Hodge_abelian_fourfolds_2502.03415/250531.tex`: Assumption `assumption-on-C-i-s`, lines 5124–5135; input sheaves `eq-F-1-and-F-2`, lines 5403–5410; Proposition `prop-local-freeness`, lines 5450–5465; its proof, lines 5846–5950. These intervals were read. Rank, reflexivity, and the codimension-4 singular locus are taken from that proposition. The regularity proof below constructs additional finite complexes explicitly.

### M7.1. Inclusion–exclusion on the total space

Use the global coordinate change (y,x)↦(y,z=y+x). Then D1 and D2 are the inverse images of Z1 and Z2 under the two independent projections X_y×X_z→X. Consequently their defining ideals are Tor independent, and

    I_D1 I_D2=I_D1∩I_D2.

In particular there is an exact sequence

    0→M→ℒ→ℒ|D1 ⊕ ℒ|D2→ℒ|T→0,   T=D1∩D2.

The total space T is the disjoint union of 169 smooth components C_i×Σ_j×Xhat, each of dimension 5. Its map f:T→A is finite: on its first two factors it is the difference map (c,z)↦z−c. Since Σ_j is a translate of −C, this is, up to translations and a sign, C×C→C^(2)→Θ⊂X. Nonhyperellipticity implies that C^(2)→Θ is an isomorphism and Θ is smooth; C×C→C^(2) is finite flat of degree 2.

Let

    W=π_*ℒ, U=π_*(ℒ|D1⊕ℒ|D2), Tcal=f_*(ℒ|T).

The higher direct images defining W vanish because the fibre line bundle is 2Θ⊗P, which is ample; W is a vector bundle of rank 8. The restriction of ℒ to each curve in each fibre of D1 or D2 has degree 6. Genus 3 and Serre duality give H^1=0, so U is a vector bundle of rank 26·4=104. Finiteness gives no higher direct images for T. Thus G is represented by

    [ W→U→Tcal ]

in cohomological degrees 0,1,2. This assertion concerns the global total-space inclusion–exclusion sequence; it does not assert that every specialization of that sequence remains exact on its left.

The map W→U is fibrewise injective. A section in its kernel vanishes on Z1, and is therefore zero by the displayed H^0 assumption. Hence Q=U/W is locally free of rank 96, and G is represented by [Q→Tcal] in degrees 1,2.

Each component of Tcal is the direct image of a line bundle under a finite flat double cover of a smooth divisor in A. It has projective dimension 1, has no Hom to O_A, and has no higher Ext above degree 1. Finite duality, with ω_A=O_A, gives

    Tcal^D := Ext^1_A(Tcal,O_A)
            = ⊕_(i,j) f_(i,j),*( (ℒ|T_(i,j))^(-1) ⊗ ω_T_(i,j) ).

Dualizing the two-term description of G and shifting by −1 yields the exact sequence

    0→Q*→E→Tcal^D→0.                                      (M7.1)

This can also be read from the long exact cohomology sequence of the dual triangle: RHom(Tcal,O_A)=Tcal^D[−1], and Q is locally free. There is no unproved exactness assertion at a singular point of E in (M7.1).

### M7.2. The dual bundles W* and U* are 7-regular

In fact, for every integer q≥1,

    H^p(A,W*(qH))=H^p(A,U*(qH))=0   for every p>0.           (M7.2)

For W, relative Serre duality along π gives W*=R^3π_*(ℒ^(-1)), with all other direct images of ℒ^(-1) zero. Leray followed by Serre duality on the ninefold Y gives

    H^p(A,W*(qH))* = H^(6−p)(Y,ℒ⊗π*O_A(−qH)).

Project Y instead onto X_y. On each A-fibre, the class of the line bundle on the right is represented, relative to the product principal polarization, by

    [[1−3q,0],[0,−3q]].

It is antiample for q≥1. Serre duality and Kodaira vanishing on the abelian sixfold A show that only the sixth direct image for this projection can be nonzero. Hence all total cohomology in degrees below 6 vanishes, proving the W assertion.

For a curve summand of U, relative Serre duality along C×A→A gives the dual bundle as R^1 of ℒ_C^(-1)⊗ω_C. Serre duality on C×A, of dimension 7, again transforms its p-th cohomology with qH into

    H^(6−p)(C×A,ℒ_C⊗O_A(−qH))*.

Project onto C. For a D1 component the numerical A-fibre matrix is again diag(1−3q,−3q). For a D2 component write z=y+x and hold z fixed. Then θ_y contributes θ_x, and P_(y,α)^(-1) contributes +P_(x,α) up to a topologically trivial factor. The matrix is

    [[1−3q,1],[1,−3q]].

Before subtracting 3q times the identity its largest eigenvalue is (1+√5)/2<3. Thus it too is antiample for q≥1, and the same Leray argument applies. Translations change only numerically trivial factors and do not change this argument.

Because dim A=6, equation (M7.2) implies 7-regularity. The standard regularity theorem applied to the closed embedding by H then gives global generation of U*(7H), and the usual multiplication surjectivity for subsequent twists.

### M7.3. A kernel with regularity 112

Put N=h^0(A,U*(7H)). Its exact value is not required. Evaluation gives

    0→K_U→O_A(−7H)^N→U*→0.

The kernel K_U is locally free and is 14-regular. For 2≤i≤6, at twist (14−i)H the relevant cohomology groups of O_A(−7H)^N and U* vanish: the line bundle exponent is 7−i≥1, while (M7.2) applies to the U* term. For i=1, at twist 13H, the map on H^0 is surjective by the multiplication theorem for the 7-regular sheaf U*. More explicitly,

    H^0(U*(7H))⊗Sym^6H^0(P^M,O(1))→H^0(U*(13H))

is surjective and factors through the evaluation map with H^0(A,6H). This checks the low-degree condition that does not follow from higher cohomology vanishing alone.

Dualize 0→W→U→Q→0, and compose evaluation with its surjection U*→W*. Let

    0→J→O_A(−7H)^N→W*→0.

Then the two kernels fit into an exact sequence

    0→K_U→J→Q*→0.                                          (M7.3)

The Buchsbaum–Rim complex of the surjection to the rank-8 bundle W* resolves J, with terms

    C_k = ∧^(8+k)(O_A(−7H)^N) ⊗ Sym^(k−1)W ⊗ det W,
    k=1,2,…,N−8,

and C_1→J surjective. Divided powers and symmetric powers agree over C. The formula, including the indispensable determinant factor, is checked against Raicu and Sam (2022), pp.41–42, immediately before the proof of Theorem 3.2; primary PDF https://doi.org/10.1112/S0010437X21007703. Only this elementary complex is used from that source.

Exactness in this application can also be checked directly. Locally split the surjection as K⊕V→V, where dim V=8. Decompose each exterior power by the number a of factors from K. After the identification ∧^(8+k−a)V⊗det V*≅∧^(a−k)V*, the a-summand becomes the homogeneous strand of the polynomial de Rham complex

    ∧^(a−k)V* ⊗ Sym^(k−1)V*,   (a−k)+(k−1)=a−1.

For a≥2 it is exact by the Euler contracting homotopy, since the total degree a−1 is a nonzero integer in C. The a=1 strand maps isomorphically onto K, and the V summand of the original map maps isomorphically onto the target. Thus this entire augmented complex is locally split exact. This proves its required exactness without appealing to an unchecked depth condition.

We next bound its terms. Write b(x,α)=x−α under the principal-polarization identification. The theorem of the square gives

    W=O_A(Θ_x)⊗b* FM(O_X(2Θ)),

where FM denotes the degree-zero Fourier–Mukai bundle, with the consistent Poincaré sign. The elementary pullback formula along the polarization isogeny of 2Θ gives

    [2]_A*W ≅ Q0^⊕8,
    c1(Q0)=4Θ_x−2Θ_(x−α).                                  (M7.4)

For completeness, the pullback formula follows by changing the integration variable by translation: for L=O(2Θ), pull the Poincaré family back along φ_L=[2]; the theorem of the square identifies p_1*L⊗(1×φ_L)*P with a*L⊗p_2*L^(-1). Its direct image is H^0(L)⊗L^(-1). Using P^(-1) replaces φ_L by −φ_L and leaves the numerical line bundle class unchanged. Thus (M7.4) holds up to a harmless numerically trivial factor if the chosen symmetric normalizations differ.

The matrix of c1(Q0) is [[2,2],[2,−2]], with eigenvalues ±2√2. The matrix of [2]*H is 12 times the identity. Therefore for q≥k+7 the line bundle

    Q0^(k+7)⊗[2]*O_A(qH)

is ample. Formula (M7.4) shows that [2]*(Sym^(k−1)W⊗det W) is a direct sum of copies of Q0^(k+7). Kodaira vanishing upstairs and the trace splitting for the finite étale map [2] imply

    reg_H(Sym^(k−1)W⊗det W)≤k+13.

The exterior-power factor in C_k is a direct sum of O_A(−7(8+k)H), so

    reg_H C_k ≤ 7(8+k)+k+13 = 69+8k.                       (M7.5)

Only six terms of the Buchsbaum–Rim resolution are needed. Indeed for any R, the vanishings

    H^(i+k−1)(A,C_k((R−i)H))=0, 1≤k≤7−i,

imply H^i(A,J((R−i)H))=0 by the successive long exact sequences. The terminal group after these six steps has degree at least 7 and vanishes by dim A=6, regardless of the regularity of the remaining kernel. It suffices that

    R ≥ max_(1≤k≤6)(reg C_k−k+1).

Using (M7.5) gives max_(1≤k≤6)(70+7k)=112. Thus J is 112-regular. Sequence (M7.3), together with the 14-regularity of K_U, gives 112-regularity of Q*: at twist (112−i)H its H^i is between H^i(J)=0 and H^(i+1)(K_U)=0. No numerical value of N is involved in this estimate.

### M7.4. The torsion dual is 8-regular

Identify a component of T with C×C×Xhat, so that its map to X is, up to translation, −(c1+c2). On C×C let F1={p}×C, F2=C×{p}, S=F1+F2, and let Δ be the diagonal. The pullback A_C of the theta class under addition is

    A_C=4S−Δ.                                               (M7.6)

Here θ|C has degree 3. The mixed Poincaré class on C×C is S−Δ: its restrictions to both fibres vanish, and its H^1⊗H^1 component is the negative of that of the diagonal with the standard polarization identification. This gives (M7.6) by the theorem of the square. As a check, its intersection with Δ is 12, the degree of [2]*Θ on the Abel–Jacobi curve.

The divisor R=3S−Δ is nef. To prove this, choose a degree-3 morphism g:C→P^1, which exists by projecting the plane quartic from a point of C. The residual divisor to Δ in C×_(P^1)C is an effective divisor of class R. The transitive monodromy group is either S3 or A3. In the S3 case its action on ordered pairs of distinct sheets is transitive, so R is irreducible. One computes

    S^2=2, S·Δ=2, Δ^2=−4, R^2=2.

An effective irreducible divisor with nonnegative self-intersection on a smooth surface is nef, since all its intersections with other irreducible curves are nonnegative. In the A3 case the cover is cyclic and the residual divisor is Γ_σ+Γ_(σ²). Each graph has self-intersection −4. Riemann–Hurwitz gives five fixed points of σ; the two graphs intersect transversely at them, because the nontrivial third-root tangent eigenvalues differ. Thus R·Γ_σ=R·Γ_(σ²)=1, and its intersections with every other irreducible curve are nonnegative. It is nef in this case as well. This proof avoids any unstated general-branching assumption on the selected quartic.

Now A_C=R+S. Numerically, the restricted line bundle is

    c1(ℒ_T)=3F1+3F2−P_(c1,α),
    f*H=3A_C+3Θ_α.

For q≥3 decompose

    q f*H−c1(ℒ_T)
      = [3q A_C−6F1−3F2]
        +(3q−1)Θ_α
        +[3F1+Θ_α+P_(c1,α)].                               (M7.7)

The last bracket is the pullback of the theta class under (c1,α)↦AJ(c1)+α and is nef. The first bracket is

    3q R+(3q−6)F1+(3q−3)F2,

which is ample for q≥3: the last two terms form an ample product class on C×C and R is nef. Adding the positive theta class on Xhat makes the first two brackets ample on the whole product. The sum in (M7.7) is therefore ample. Translations and normalization choices contribute numerically trivial factors, so they do not affect ampleness.

Kodaira vanishing on the smooth fivefold T gives

    H^i(T,ω_T⊗ℒ_T^(-1)⊗f*O_A(qH))=0 for i>0,q≥3.

Finiteness and the formula for Tcal^D transfer this to A. The support of Tcal^D has dimension 5; hence q=8−i≥3 for 1≤i≤5 proves that Tcal^D is 8-regular. Finally (M7.1) and the 112-regularity of Q* prove the claim for E.

### M7.5. A stronger estimate stable under isogeny and positive twists

The same explicit complexes give the following useful variant. For any positive integer m and any line bundle L on A such that

    c1(L)−112 m² H is nef,

one has

    H^i(A,[m]*E⊗L)=0 for every i>0.                         (M7.8)

Any additional Pic^0 factor is allowed, since the hypothesis and the following ampleness tests are numerical. Here are all the required checks; (M7.8) is not inferred from global generation.

Pull back (M7.1), (M7.3), and the evaluation and Buchsbaum–Rim complexes by the finite étale map [m], so exactness is preserved. For [m]*W* and [m]*U*, the proof of M7.2 still applies after base change: the relevant spaces are X_y×A and C×A, now with x and α replaced by mx and mα in ℒ. The A-fibre matrices before twisting by L^(-1) are m² times the two matrices used there. Subtracting c1(L) makes them negative definite, because 112H minus either of those fixed matrices is positive definite, and adding a nef form preserves positivity. Thus [m]*W*⊗L and [m]*U*⊗L have no positive-degree cohomology.

In the evaluation sequence for [m]*K_U⊗L, the middle line bundle is L(−7m²H), which is ample. The preceding vanishings give

    H^j(A,[m]*K_U⊗L)=0 for j≥2.

No assertion about H^1 of this kernel, or a multiplication map with a varying Pic^0 factor, is needed.

For k≤6, pull [m]*C_k⊗L back further by [2]. Each summand then has numerical class

    [2]*c1(L)−7m²(8+k)[2]*H+m²(k+7)c1(Q0).

It is ample. Indeed write [2]*c1(L)=112m²[2]*H plus a nef form; the remainder is m² times the matrix

    12[112−7(8+k)]I_2+(k+7)[[2,2],[2,−2]],

which is positive definite for 1≤k≤6 (the worst safe estimate is 168−26√2>0 at k=6). Kodaira vanishing and the trace splitting give complete higher-cohomology vanishing for these first six pulled-back C_k terms. The same dimension-six truncation as before proves higher-cohomology vanishing for [m]*J⊗L, and (M7.3) then gives it for [m]*Q*⊗L.

Finally let T'=T×_(A,[m])A, with finite étale map g:T'→T and finite map f':T'→A. Finite flat base change identifies [m]*Tcal^D with

    f'_*(ω_T'⊗g*ℒ_T^(-1)).

The line bundle f'*L⊗g*ℒ_T^(-1) is ample: it is the sum of the pullback of the ample class 3f*H−c1(ℒ_T) from M7.4 and the nef class f'*(c1(L)−3m²H), using g*f*H=m²f'*H. Kodaira vanishing on each smooth component of T' proves the assertion for [m]*Tcal^D⊗L. The extension (M7.1) completes the proof of (M7.8).

## M8. From global generation to effective third-Chern cycles

This section is a separate elementary bridge. Let B be a rank-r ordinary coherent sheaf, with r≥3, on a smooth projective sixfold A, locally free away from a closed subset S of codimension at least 4, and suppose c1(B)=0 in CH^1(A) (or use the cohomological versions of every equality below if only cohomological triviality is given). Let h be a very ample divisor, R a nonnegative integer, and suppose F=B(Rh) is globally generated.

For p=2,3 choose r−p+1 general global sections of F. On A\S these define a map from a trivial bundle to the rank-r vector bundle F. Because the full evaluation map is surjective, the universal map of this fixed number of sections is transverse to each matrix-rank stratum. Generic smoothness in characteristic zero gives the expected codimension-p degeneracy locus, or the empty locus. Its fundamental cycle has class c_p(F) on A\S, by the special rank-drop case of the Thom–Porteous formula (equivalently the standard definition of Chern classes by dependence loci of general sections). Its closure C_p in A is an effective codimension-p cycle.

Localization for Chow groups gives an isomorphism CH^p(A)→CH^p(A\S) for p≤3, since no cycle of dimension 6−p can be supported on S, whose dimension is at most 2. Therefore [C_p]=c_p(F) in CH^p(A). This argument does not require F to be locally free at S and does not retain unwanted high-codimension degeneracy components there.

The twist identities are

    c2(F)=c2(B)+binom(r,2)R²h²,
    c3(F)=c3(B)+(r−2)R h c2(B)+binom(r,3)R³h³.

Eliminating c2(B) yields

    c3(B)=C3−(r−2)R h·C2+[r(r−1)(r−2)/3]R³h³.              (M8.1)

The last coefficient is an integer. General divisors in |h| intersect C2 properly, so h·C2 has an effective representative; h³ has one as well. Thus (M8.1) is represented by Z+−Z− with

    Z+=C3+[r(r−1)(r−2)/3]R³h³,
    Z−=(r−2)R h·C2.

For the degree convention deg_h Z=∫_A h³[Z] on codimension-3 cycles,

    D+=∫_A h³c3(F)+[r(r−1)(r−2)/3]R³∫_A h⁶,
    D−=(r−2)R∫_A h⁴c2(F).                                 (M8.2)

These are explicit fixed integer intersection formulas. They are nonnegative because the cycles just constructed are effective. The displayed pair has degrees at most max(D+,D−). Expanding the Chern classes makes the equivalent expressions

    D+=∫h³c3(B)+(r−2)R∫h⁴c2(B)
        +[r(r−1)(r−2)/2]R³∫h⁶,
    D−=(r−2)R∫h⁴c2(B)
        +[r(r−1)(r−2)/2]R³∫h⁶.

In particular, if the Weil projection of c3(B) is nonzero, at least one of these two effective cycles has nonzero Weil projection. No estimate for its direction relative to a preselected rational Weil vector is needed to supply the effective-cycle input to the separate finite-lattice/projector argument P3.

### M8.1. Normalizing the seed and comparing polarizations

Let E be the rank-r output above, r=96. Let h be a symmetric very ample line bundle which extends as the chosen polarization in the relevant Weil deformation family. Choose positive integers c,C such that

    c h−H is ample,        C h−c1(det E) is ample.            (M8.3)

These are explicit finite-dimensional positive-definiteness inequalities in the integral Riemann-form matrices at the seed. For example one may test successive integers by the exact principal-minor criterion, or use c>λ_max(h^(-1)H) and C>λ_max(h^(-1)c1(det E)). No existence bound for an unspecified sheaf is being invoked here: H is the displayed product polarization and det E is computed from [W]−[U]+[Tcal].

Because the 112th power of an ample line bundle on an abelian variety is globally generated, E(112 c h) is globally generated. Set D=det E and

    B0=[r]*E⊗D^(−r).

Its first Chern class vanishes: [r]*c1(E)=r²c1(E), while tensoring rank r by D^(−r) subtracts r²c1(E). Its normalized character satisfies

    ch_p(B0)=r^(2p)κ_p(E),    κ(E)=ch(E)exp(−c1(E)/r).

Pullback preserves global generation, and [r]*h≅h^(r²) for symmetric h. The line bundle (h^C⊗D^(-1))^r is globally generated, since r≥2. Therefore

    B0(R h) is globally generated for
    R = 112 r² c+r C.                                      (M8.4)

The determinant of B0 is cohomologically trivial, although it may have a Pic^0 factor if D is not chosen symmetric. A compatible flat-line normalization changes neither κ nor numerical intersections. If the normalized sheaf supplied by the local untwisting differs from B0 by an arbitrary Pic^0 line bundle, use the same argument with that factor absorbed into the final ample power; every Pic^0 twist of the rth power of an ample line bundle is globally generated for r≥2. Thus the same numerical R remains valid for seed global generation. For persistence in families we use the slightly larger, explicitly certified regularity bound below.

For c1(B0)=0 in rational cohomology, ch_3(B0)=c3(B0)/2, and hence

    c3(B0)=2 r⁶κ3(E).

If only cohomological determinant normalization is used, M8.1 and M8.2 are asserted as cycle-class equalities, which is exactly the required conclusion for bounded division. A literal Chow equality with the c1 terms omitted requires trivial determinant in CH^1, as stated at the start of M8.

### M8.2. Persistence on an analytic neighbourhood

Suppose the twisted deformation furnished by Markman's argument is flat over a sufficiently small contractible analytic base, with a fixed rank-r μ_r twisting class and determinant normalization. On a torus family, multiplication [r] acts by r² on the local system H²(−,μ_r), hence kills this twisting class. After shrinking, the μ_r Čech trivialization can be made on the family; it gives an ordinary flat coherent family. Its seed differs from the displayed normalized B0 only by a flat line bundle, which is already covered above.

For a relatively very ample h, global generation of a fibre alone does not automatically prove openness without a cohomological argument. Estimate (M7.8) supplies that argument with the explicit bound

    R_safe=112 r² c+r C+6.                                 (M8.5)

For each 1≤i≤6 set L_i=D^(−r)⊗h^(R_safe−i), with the harmless Pic^0 normalization factor included if needed. Then

    c1(L_i)−112r²H
      =112r²(c h−H)+r(C h−c1(D))+(6−i)h

is ample by (M8.3). Taking m=r in (M7.8) gives

    H^i(A,B0((R_safe−i)h))=0, 1≤i≤6.

Thus B0 is R_safe-regular with respect to h. These explicit six vanishings, rather than seed global generation alone, prove the required openness.

Upper semicontinuity makes the same regularity bound hold on a neighbourhood. The precise analytic source is Grauert (1960), §7, Satz 3, printed pp.62–63: a coherent analytic sheaf flat over the reduced base of a proper holomorphic map has upper-semicontinuous fibre-cohomology dimensions. The locus where the flat family is locally free is open in the total space; properness makes the dimension of its closed nonfree fibres upper semicontinuous. Since the seed singular locus has codimension at least 4, the same is true on a smaller neighbourhood. Applying M8 fibrewise with R=R_safe supplies the explicit degree bounds (M8.2) on that neighbourhood. The separate bounded-Chow/Baire lemma globalizes these effective-cycle data. This last globalization uses the explicit vanishing argument, not fixed Chern character alone.

## M9. Completely numerical seed degree

Use x=Θ_x, y=Θ_α, and p=c1(P_(x,α)); in the matrix convention used above a class bx+cy+ep has matrix [[b,e],[e,c]]. Since X is a principally polarized threefold,

    ∫_(X×Xhat) exp(bx+cy+ep)=(bc−e²)³.                      (M9.1)

The input character is ch(F)=1+θ−6θ²−2θ³. This follows either from the input Hilbert polynomial and the Abel–Jacobi curve character, or directly from Markman's displayed secant character at source lines3743–3776. Put c_0=1,c_1=1,c_2=−6,c_3=−2 and use the operator

    D_(u,v)=Σ_(0≤i,j≤3) c_i c_j ∂_u^i ∂_v^j |_(u=v=0).

Fibre integration of the exponential line bundle on X_y×A gives the Gaussian identity

    π_* exp(uθ_y+vθ_(y+x)−P_(y,α))
      =(u+v)³ exp((uvx+vp−y)/(u+v)).

This identity follows by factoring into the three symplectic coordinate pairs, or by completing the square in the exterior algebra. In degrees k≤3, its degree-2k part is the polynomial

    (u+v)^(3−k)(uvx+vp−y)^k/k!,

so evaluating D_(u,v) requires no limiting division by u+v. Because E=G^∨[−1], its character in degree k is (−1)^(k+1) times this polynomial's D_(u,v) value. The result is

    ch0(E)=96,
    ch1(E)=264x+22y−48p,
    ch2(E)=12p²−132px−11py−144x²−24xy−y²,
    ch3(E)=−2p³−6p²x+6p²y+72px²+12pxy+(1/2)py²
             +24x³−72x²y+(1/2)xy²−(1/6)y³.

Normalize by κ(E)=ch(E)exp(−ch1(E)/96). Exact simplification gives

    κ2(E)=−(169/48)(12x+y)²,
    κ3(E)=(13/3456)[−10368p²x+864p²y+288576x³
                         +51408x²y+6012xy²+119y³].          (M9.2)

In particular the invariant polarization line is spanned by h0=12x+y. To see this without guessing a convention for the dual torus, use Markman's established Spin(V)_P-invariance of κ(E) (main theorem item3, source lines510–513, and the construction at lines2406–2468). The derivative of invariance of the nonzero multiple h0² gives h0∧(a·h0)=0 for every Lie-algebra element a. Since h0 is ample, Lefschetz injectivity H²→H⁴ implies a·h0=0. The connected group therefore fixes h0. Its invariant line in H² is one-dimensional, as stated in the source at lines3966–3968. Thus h0 is the desired integral ample invariant class. We take

    h=3h0=36x+3y.

The triple of an ample line bundle on an abelian variety is very ample; Bauer–Szemberg (1996), Theorem1.1(b), supplies a primary-source statement and proof of the stronger three-ample-factor version. Since h0 is an integral invariant class, it remains of type (1,1) throughout the polarized period component; after choosing the local relative symmetric line bundle, h is relatively very ample. This is the h used in M8. Its type at the seed is (3,3,3,36,36,36), so

    Δ_h=h⁶/6!=108³=1,259,712,
    ∫h⁶=906,992,640.

For D=det E, the matrix of c1(D) is [[264,−48],[−48,22]]. Choose c=2 and C=12 in (M8.3). Then

    2h−H has matrix [[69,0],[0,3]],
    12h−c1(D) has matrix [[168,48],[48,14]];

their leading principal minors are respectively (69,207) and (168,48). Both are ample. Consequently the normalized seed and its nearby ordinary deformations have the certified regularity bound

    R=112·96²·2+96·12+6=2,065,542.                          (M9.3)

Let B0=[96]*E⊗D^(−96), up to the flat normalization already covered. Formula (M9.1) and (M9.2) give

    ∫h⁴c2(B0)=30,136,419,515,105,280,
    ∫h³c3(B0)=28,288,052,451,512,156,160.

For clarity, c2(B0)=33,226,752 h² in rational cohomology, and the coefficient of h³ in the orthogonal h³ component of c3(B0) is 31,188,844,544. The latter does not assert that the Weil component is zero; it is nonzero by Markman's independent-from-h³ statement, also visible in the p² terms of (M9.2).

Apply M8 with r=96 and R from (M9.3). Then

    D−=(94 R)∫h⁴c2(B0)+428640 R³∫h⁶
       =3,426,088,289,770,686,418,974,855,223,050,240,
    D+=D−+∫h³c3(B0)
       =3,426,088,289,770,714,707,027,306,735,206,400.

Thus the explicit source bound

    D6_source=3,426,088,289,770,714,707,027,306,735,206,400   (M9.4)

bounds both effective signs representing c3(B0), and at least one of these cycles has nonzero Weil projection. The same bound holds over a nonempty analytic open subset of the nine-dimensional source Weil period family. This uses the actual deformed sheaf and the regularity argument of M7–M8, not just the seed algebraicity of its Chern character.

The arithmetic is recorded in `work/markman_output_numbers.py` and its executed output `work/markman_output_numbers.json`. As a separate calculation, the script applies D_(u,v) to the cube of the determinant of

    [[u+v,v,−1],[v,v+b,e],[−1,e,c]],

which is absolute GRR on X³. Its top four homogeneous components agree exactly with the characters above paired against exp(bx+cy+ep). This checks signs, factorials, the rank, and the three numerical intersections by a different integration order. The script verifies polynomial and integer identities only; it does not formally verify the geometric derivation.

## M10. Maximal-order lattice and transfer to a principal sixfold family

This check concerns the parent's proposed subsequent isogeny transfer. At the pure-spinor seed with d=12, f=√−12 acts integrally. Indeed its action on H¹(X)⊕H¹(Xhat), using the principal-polarization contraction θ, has block form

    [[0,12θ],[−θ^(-1),0]],

as follows directly from its two eigenspaces in source `eq-W-1-and-2`, lines1353–1364. Both θ and θ^(-1) are integral. Its dual action on the integral homology lattice Λ is consequently integral as well. With

    ω=(f−2)/4,     O_K=Z[ω],
    Λ_O=Λ+ωΛ,

one has ω²+ω+1=0, so Λ_O is O_K-stable and is contained in (1/4)Λ. The quotient index I=[Λ_O:Λ] divides 4¹². This gives the degree-I quotient isogeny q_O:A→A_O.

The Riemann form 16h is integral on Λ_O: denominators of each of its two arguments divide4. It thus defines an ample polarization h_O with q_O*h_O=16h as classes. The line-bundle equality can also be arranged, because pullback on Pic^0 under an isogeny is surjective. Its polarization product satisfies

    Δ_O=16⁶Δ_h/I ∈ Z,

and is therefore an integer divisor of 16⁶Δ_h. This quotient construction commutes with the local period deformation, since its lattice data are fixed.

The denominator proof in SQ7 of `work/severn_quantitative.md` works in any split even K-rank. In rank6, its block Hermitian determinant is −Norm(det B), so throughout one must use the absolute determinant Δ. Over the PID O_K, choose a primitive rank3 isotropic submodule and extend its basis. In the resulting block matrix [[0,B],[B*,D]], the operations

    X=(B*)^(-1)D/2,  w'=w−vX,  u=w'B^(-1)

give a hyperbolic basis. In both directions all denominators divide2Δ. Applying this to A_O and to a fixed principal split target lattice gives a rational K-isometry with denominator dividing4Δ_O. Hence the uniform integer

    M=4·16⁶·Δ_h

clears the denominator, yielding a K-linear isogeny φ:A_O→A_pr with

    φ*θ_pr=M²h_O.

The transported target complex structure lies in the principal split period component. The induced rational period-domain map is an isomorphism, so the source analytic open set maps to an analytic open set. For an effective three-dimensional source cycle Z,

    deg_(θ_pr)((φ∘q_O)_*Z)=16³ M⁶ deg_h Z.

The Weil projection remains nonzero under isogeny pushforward. Therefore an effective integral seed with nonzero Weil projection on an analytic open subset of the principal split sixfold family has the explicit degree bound

    D6_pr=16³(4·16⁶·108³)⁶ D6_source.                      (M10.1)

The intermediate h_O needs only to be ample. For projective parameter spaces on the principal target one may embed with 3θ_pr and translate degree bounds by the fixed factor3³; intrinsic degree in (M10.1) remains measured by θ_pr. The later projector, Cramer, and fourfold contraction steps are separate and are not included in D6_pr.

### M10.1. Explicit principal-sixfold lattice conversion

Write D6=D6_pr. For the n=3 projector of P1, independent integer-pair Horner evaluation verifies

    δ3=1,701,760,099,946,011,389,900,
    B3=6,493,952,361,560,098,735,300,
    (3+ω)^6=37+360ω.

Here B3 is the sum of absolute numerator coefficients weighted by7^(3j). The saturated principal Weil lattice has a basis u3,v3 with positive Gram matrix9[[2,1],[1,2]]. For an effective cycle Z of degree≤D6 and nonzero Weil projection let z=δ3 P[Z]=xu3+yv3. The principal polarization has volume1, so the comass/Wirtinger argument of P3 gives

    ||z||≤δ3D6/6,
    18(x²+xy+y²)=||z||².

Thus with

    H3=max(1,floor(δ3²D6²/648)),

the integer h_z=x²+xy+y² lies in[1,H3]. Pullback by a=3+ω acts in this basis as

    T=[[37,360],[−360,−323]],
    det(z,Tz)=−360h_z.

Cramer's rule represents N_z u3, N_z=360h_z, by the integral classes z,Tz. Its two coefficients have absolute values |360x+323y| and |y|. Representatives of z have each sign of degree≤B3D6; those of Tz have each sign of degree≤343B3D6. Since |x|,|y|≤h_z for integer x,y with h_z>0,

    |360x+323y|+343|y|≤1026h_z<3N_z.

Therefore N_z u3 has each sign of degree≤3N_z B3D6. The bound N_z≤360H3 and these simultaneous degree bounds hold on the analytic open subset above. R21 globalizes the finite union of the corresponding closed loci to the whole principal split sixfold component. For a completely explicit single multiplier, set

    L3=lcm(1,…,H3),   N3=360L3.

Since N_z divides N3, scale the open-set cycles first and apply R21 to fixed N3. Every fibre then has representatives of N3u3 with each sign of degree≤3N3B3D6. The finite formula for the lcm is not expanded into a numeral.

### M10.2. Compensation and contraction to fourfolds

Let A4 range over the principal split fourfold component and let B=E_x×E_y have balanced K-action and product principal polarization θ_B. Put A6=A4×B and θ_6=θ_4+θ_B. On B let U,V be the integral Weil divisors satisfying

    U=Γ_ω+Γ_1−2F_x−2F_y,  V=Γ_1−F_x−F_y,
    ∫U²=∫V²=−2,  ∫UV=−1.

The integral marked exterior forms satisfy Ω3=Ω2Ω1, hence u3=u2U−v2V. Therefore

    pr_(A4),*(u3·(−2U+V))=3u2,
    pr_(A4),*(u3·(−U+2V))=3v2.

The two signed divisors admit the explicit decompositions

    −2U+V=3F_x+3F_y−2Γ_ω−Γ_1,
    −U+2V=Γ_1−Γ_ω.

Each graph Γ_1,Γ_ω is nef and is bounded above by2θ_B in the nef cone. The first divisor's positive and negative parts are bounded by3θ_B and6θ_B respectively; the second's two parts are each bounded by2θ_B. Translate these finitely many effective divisors generically on B before intersecting. Their cohomology classes and nef comparisons remain unchanged, and they meet every component of any given cycle properly.

For an effective three-cycle Z on A4×B,

    θ_6³≥3θ_4²θ_B

after integration on Z, since all remaining mixed intersections are nonnegative. Thus if each sign of a signed three-cycle has θ_6-degree≤D3, either of the two signed divisor intersections and pushforwards has each sign of θ_4-degree≤3D3. For the first divisor this is (3+6)D3/3; for the second it is4D3/3, bounded by3D3. It is the individual bounds on the two signs, not cancellation of their signed degrees, that prove this assertion.

Applying the sixfold representation of N_z u3 gives representatives of both3N_z u2 and3N_z v2 with each sign of degree≤9N_z B3D6. For a fixed rational class t=(a u2+b v2)/q, a,b integers and q≥1, it follows that there are integral effective cycles with

    N t=[Z+]−[Z−],
    N≤1080qH3,
    deg_(θ4) Z±≤3240H3 B3D6(|a|+|b|).                     (M10.2)

The same N_z is used for the two contractions. Consequently the multiplier does not grow by taking their sum. With the explicit single N3=360L3, one may instead take

    N=3qN3=1080qL3,
    deg_(θ4) Z±≤9N3 B3D6(|a|+|b|).                        (M10.3)

These formulas close the quantitative fourfold template for the principal split datum. A comparison to another fixed integral polarized K-datum introduces the corresponding fixed Hermitian-lattice and target-coordinate factors; those are not silently absorbed into (M10.2).

## Check events and exact scope

- M7.1: direct proof check of total-space Tor independence, the three direct images, fibrewise subbundle injection, and finite-duality extension. Passed; independently rechecked by `/root/reductions`.
- M7.2: direct proof check of relative and absolute duality indices, both A-fibre matrices, and all regularity cohomology groups. Passed; independently rechecked by `/root/reductions`.
- M7.3: source check of the complete Buchsbaum–Rim formula at Raicu–Sam pp.41–42; direct split-case exactness proof, [2] splitting calculation, and six-term cohomological truncation. Passed; independently rechecked by `/root/reductions`.
- M7.4: direct surface-intersection and nefness proof, including both possible degree-3 monodromy groups; matrix/class expansion of (M7.7) and every Kodaira twist. Passed; independently rechecked by `/root/reductions`.
- M7.5: direct recheck of every complex after finite étale base change, both duality arguments with a general positive line bundle, the six Buchsbaum–Rim summand matrices, and the finite-cover Kodaira argument. Passed; independently rechecked by `/root/reductions`.
- M8: direct general-section/localization proof, symbolic expansion of twist identities, and six explicit normalized-seed cohomology vanishings proving family openness. Passed; independently rechecked by `/root/reductions`. Its full review is in `work/markman_regularity_independent_check.md`, events R28.1–R28.6.
- M9: full relative-GRR derivation through ch3, polarization identification from invariant κ2 and Lefschetz injectivity, positivity of both numerical comparison matrices, and exact source-degree calculation. Arithmetic script executed and JSON read; separate absolute-GRR calculation agrees. The reductions agent independently reconstructed the proof and every number using a fresh Fraction/multinomial implementation without SymPy, `work/check_markman_numbers_independent.py`. All outputs agree; events R30.1–R30.3 in `work/reductions_check_events.tsv`.
- M10: independent check of the proposed maximal-order enlargement, integrality and polarization divisibility, the general-rank SQ7 denominator formulas including the odd-half-rank sign, and cycle-degree pushforward; independent n3 polynomial Horner check; complete proof check of the lattice norm cap, integer Cramer coefficients, both compensation contractions, proper moving and separate-sign degree estimates. Passed in this targeted audit and the reductions agent's complete independent second proof check, events R31.1–R31.4 and R32.3. New arithmetic fields are recorded in `markman_output_numbers.json`; no huge lcm is expanded.
- SOURCE-BS96: read Bauer–Szemberg Theorem1.1(a),(b) and its complete proof, primary author PDF pp.1–3, printed pp.79–81. It supplies the ample-product global-generation and very-ampleness statements used above, including Pic^0 twists.
- SOURCE-G60: read Grauert §7, Satz3 and its proof, primary PDF printed pp.62–63, including the properness, reduced-base and sheaf-flatness hypotheses immediately preceding it. This is the analytic semicontinuity input. The whole paper has not been audited.
- TEX-M7–M10: complete mathematical read of `deliverables/markman_quantitative.tex`, including all M7–M10 proofs and constants. Corrected the general M8 statement to r≥3; the application r=96 is unchanged. The reductions agent read the complete final M10 text and reported no outstanding mathematical correction. Root performs the compilation and rendered-layout checks.
- These are explicit finite formulas for any prescribed rational Weil vector in the principal split fourfold datum. No optimality of the regularity, source degrees, or final caps is claimed.

## References

Bauer, T., & Szemberg, T. (1996). On tensor products of ample line bundles on abelian varieties. *Mathematische Zeitschrift, 223*, 79–85. https://doi.org/10.1007/BF02621589. Primary author PDF https://www.informatik.uni-marburg.de/~tbauer/1996-On-tensor-products.pdf, Theorem1.1, PDF pp.1–3 (printed pp.79–81), web locator `turn771655727view0`. The theorem and complete proof were read; used for squares being globally generated and cubes being very ample, including arbitrary numerically trivial twists.

Grauert, H. (1960). Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen. *Publications Mathématiques de l’IHÉS, 5*, 5–64. https://doi.org/10.1007/BF02684746. Primary PDF https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf, §7, Satz3 and proof, printed pp.62–63; web locators `turn575073948view2`, `turn245465386view0`. This is the analytic semicontinuity source; EGA is not substituted for the analytic statement.

Markman, E. (2025). *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*. arXiv:2502.03415v2, supplied source dated250531. https://arxiv.org/abs/2502.03415. Exact supplied-source locators appear above.

Raicu, C., & Sam, S. V. (2022). Bi-graded Koszul modules, K3 carpets, and Green's conjecture. *Compositio Mathematica, 158*, 33–56. https://doi.org/10.1112/S0010437X21007703. The complex and exactness criterion are on pp.41–42; primary-source web locators `turn596298041view0`, `turn460055375view0`.

Charalambous, H., & Tchernev, A. (2003). Free resolutions for multigraded modules: A generalization of Taylor's construction. *Mathematical Research Letters, 10*, 535–550. https://doi.org/10.4310/MRL.2003.v10.n4.a12. Primary preprint https://arxiv.org/pdf/math/0207040, §3 and Proposition3.3, PDF pp.3–5; web locators `turn596298041view1`, `turn460055375view1`. Used as a second check of the split linear-algebra complex, not as a source for the numerical bound.

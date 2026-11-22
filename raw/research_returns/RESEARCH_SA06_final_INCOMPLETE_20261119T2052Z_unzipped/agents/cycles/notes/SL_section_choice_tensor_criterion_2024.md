# Exact section-choice criterion for the displayed SL coefficients

**Proved linear and geometric choice criterion. The identification with every actual supported HK node class remains unfinished. No main-gate movement.**

Author: GPT-6 Astra Pro (OpenAI), `/root/cycles_continuation`, RESEARCH_SA06; reasoning effort not separately exposed.

## SC.1. Types and fixed data

Work over an algebraically closed field k. Let A be the fixed smooth connected proper parameter curve in the marked VE/HK construction, with distinct points a0,a1. Write U=A minus {a0,a1}. Let I be the finite set of marked incidences. At an incidence q, let N_q be the evaluation line bundle on A, with its given trivialization at a0. In the intended Poincare construction N_q is algebraically trivial, but the criterion below works for arbitrary line bundles.

Fix a rational vector space V and vectors w_q in V. For the displayed exceptional calculation, V is the relevant weight-one subgroup of K_(-1)(E)_Q and w_q is the signed closed-union boundary of the edge point class [O_q]. The sign is the sign of that component in the oriented edge restriction. Every HK support curve meets edges away from triple points. Thus the point-supported class has a canonical coherent lift through the edge/vertex fibre: its restriction to every vertex has empty support. The boundary defining w_q uses that lift, rather than an arbitrary lift of an unsupported edge K0 class. Put W=span_Q{w_q:q in I}, a finite-dimensional subspace of V.

Choose an actual rational section r_q of N_q, regular and nonzero at a0 and a1, with r_q(a0)=1 in the given trivialization. Write

    B_q=div(r_q)=sum_(x in U) n_qx [x].

Such sections exist by the high-twist two-point evaluation argument already proved in VE. Only finitely many n_qx are nonzero. Define the displayed leading coefficient and its invariant tensor by

    v_x = sum_q n_qx w_q in W,
    Omega = sum_q w_q tensor [N_q] in W tensor_Q Pic(A)_Q.       (SC.1)

These are precisely the types of SL.3 and its associated Picard tensor. The inclusion W→V stays injective after tensoring over Q, so vanishing can equally be tested in V tensor_Q Pic(A)_Q. No injectivity of an exterior-product map to an ordinary Chow or K-group is asserted.

## SC.2. What changing h0 can and cannot do

The coefficients n_qx are determined before choosing the covering function h0. VE chooses h0 with zeros at the union of their supports, a prescribed nonzero value at a1, and its only pole at a0. Changing h0 while keeping these sections cannot change any v_x. It may add further zero points, but every coefficient at such a new point is zero. In the simple-zero semistable model these choices give the same labelled leading coefficient at the corresponding bridge.

No claim about an arbitrary multiple-zero model or about all possible actual K1 descent lifts is needed for this observation. The simple-zero choice is available: prescribe nonzero first derivative at the finitely many support points and use a sufficiently positive linear series separating the relevant jets. The usual one-dimensional incidence argument also avoids unwanted multiple zeros away from this finite set, in every characteristic.

## SC.3. Exact equivalence, allowing rational denominators

The following conditions are equivalent:

1. Omega=0.
2. There is one positive integer m and, for every q, a rational section r'_q of N_q^(tensor m), normalized to value1 at a0 and nonzero at a1, such that, on writing div(r'_q)=sum_x n'_qx[x], one has sum_q n'_qx w_q=0 for every x.

The multiplier is essential: all coefficient groups in the exceptional argument are rational, while the eventual VE construction must use actual integral line bundles and rational sections.

**Proof.** Let Div_U(A) be the free abelian group on closed points of U. Let Prin_U(A) be the subgroup of divisors of nonzero rational functions whose zeros and poles avoid a0,a1. The sequence

    Prin_U(A)_Q → Div_U(A)_Q → Pic(A)_Q → 0             (SC.2)

is exact. Surjectivity follows by representing any line bundle by a divisor avoiding the two points, as in VE. Integrally, the kernel of Div_U(A)→Pic(A) is exactly Prin_U(A); tensoring with Q retains exactness. In particular, a divisor trivial only in Pic(A)_Q becomes principal after a further integer multiplier, which must not be omitted.

Form d=sum_q w_q tensor B_q in W tensor Div_U(A)_Q. Its image under (SC.2) is Omega. If W=0 there is nothing to prove. Otherwise select a basis w_(q1),...,w_(qr) from the given finite list. Write

    d=sum_(j=1)^r w_(qj) tensor D_j.

If Omega=0, basis independence gives [D_j]=0 in Pic(A)_Q for every j. First clear all coefficients of the rational divisors D_j. Their integral divisor classes are then torsion. Choose one further common multiplier killing these finitely many torsion classes. Thus there is a single m>0 and rational functions f_j with

    div(f_j)=m D_j.

The divisors on the right are supported in U, so f_j is regular and nonzero at both marked endpoints. Rescale each f_j by its nonzero value at a0, making f_j(a0)=1. Replace

    r'_(qj)=r_(qj)^(tensor m)/f_j,
    r'_q=r_q^(tensor m) for q outside the selected basis indices.

These are actual rational sections of the required tensor powers. They preserve both endpoint conditions. Their weighted divisor sum is

    sum_q w_q tensor div(r'_q)
       =m d−sum_j w_(qj) tensor div(f_j)=0.

Independence of the point basis of Div_U(A)_Q gives every displayed coefficient zero. Conversely, passing the zero divisor sum in condition2 to Pic(A)_Q gives m Omega=0, hence Omega=0. This proves the equivalence.

After this single denominator-clearing step, choose h0 anew for the finite union of the new supports. VE is applied to the actual tensor-powered data; division by m takes place only after passing to the rational K-group. Thus the criterion does not replace actual proper families by fractional line bundles or formal sections.

## SC.4. Fixed finite covers do not annihilate Omega

Let f:A'→A be a finite surjective morphism of smooth proper curves of degree d, and keep the coefficient space W fixed. The pulled-back evaluation bundles have tensor

    Omega'=(id_W tensor f*)Omega.

On divisor classes, the norm identity Nm_f(f*N)=N^(tensor d) follows by pushing the pullback divisor, including its ramification multiplicities. Hence (id_W tensor Nm_f)(Omega')=d Omega. Rationally, f* is injective on these tensors. Therefore Omega' vanishes if and only if Omega vanishes. This includes inseparable finite morphisms; the smooth curves make the finite map flat and the divisor norm formula remains valid.

This statement concerns the same presentation after pullback. Choosing a different supporting curve or a different Poincare family is a different problem and may change Omega.

## SC.5. Standard normalization twists

For one supporting curve A_i in a component E_i, transversality and avoidance of triple points make the alternating edge restriction of [O_(A_i)] exactly the sum of its signed point-supported classes. Its closed-union boundary is zero, because it is the coherent restriction of an actual component class. Thus the corresponding incidence vectors satisfy sum_(q on A_i) w_q=0.

Tensoring that Poincare family by the pullback of a single line bundle M on the parameter changes every N_q in this group by M. The tensor changes by (sum_(q on A_i)w_q) tensor [M]=0. Such a normalization twist therefore does not provide an additional way to change Omega. The same conclusion holds for the corresponding component-divisor times parameter-line correction. It is a statement about these explicit corrections, not about every conceivable endpoint-zero K0 family.

## SC.6. Precise remaining limitations

The complete identification of the displayed v_x with the support-Mayer–Vietoris node class of every selected actual HK K1 lift has not been completed. The sheaf-to-K1 and coherent-totalization choices can contribute additional terms and must be tracked. Accordingly SC.3 is an equivalence for the displayed leading formula, not a certification that Omega=0 alone eliminates every actual supported obstruction.

Conversely, Omega nonzero prevents this fixed-data section/function maneuver from killing all displayed coefficients. It does not prove that an actual supported node class is nonzero, and it does not establish a nonzero class in UK.7. The existing elliptic calculation proves that actual exterior-product vanishing need not imply vanishing of the abstract tensor; no converse is inserted here.

Component Albanese-kernel membership does not by itself supply the tensor identity. At the correspondence level, the unresolved composite has the form h1(parameter)→t2(component)→h1(edge)(1). The Tate twist prevents the previously considered surface-motive orthogonality statement from applying. No weight-vanishing claim is made. A successful construction must supply a new presentation with the required compatibility or remove the actual supported boundary by another argument.

## Inputs and reading scope

This note gives the entire linear-algebra, divisor and normalization proof. Its geometric inputs are the previously completely audited VE construction and the HK supported point maps. The exact regular semistable model and the explicit caveat about SL.3 were reread in `../../frobenius/C3_SNC_semistable_specialization_limit.md` during this continuation. The elementary norm identity is derived above from divisor push-pull; no additional external theorem or unproved tensor-to-cycle injectivity is imported. No claim of priority or absence from the literature is made.

Saved: 2026-11-19T20:24:37.625951+00:00

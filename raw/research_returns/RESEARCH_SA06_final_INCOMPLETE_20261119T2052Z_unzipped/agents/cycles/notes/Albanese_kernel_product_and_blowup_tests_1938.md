# Albanese-kernel tests: vertical products and point blow-ups

**Status:** proved auxiliary calculations with exact scopes below; no new main-gate movement and no claim that the remaining UK.7 quotient vanishes or is nonzero. The crossed-boundary product problem remains unfinished.

Credit: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, /root/cycles_continuation; effort setting not separately exposed. No priority claim.

## VP.1. A vertical-product relative model kills the entire Albanese kernel (Proved)

Let A and B be smooth connected projective curves over an algebraically closed field k, and let D be a finite reduced subscheme of A. Put S=A×B and define the actual relative perfect K-spectrum

    F_S(P)=fib(K(S×P) → K(D×B×P))_Q.

Let J_0^prop(F_S) denote endpoint differences of actual relative K0 classes over fixed smooth connected proper curves. Write T(S)_Q for the kernel of the Albanese map on degree-zero CH0(S)_Q. Then every element of T(S)_Q is the component image of an element of J_0^prop(F_S).

### Proof

Choose a0∈A(k), b0∈B(k). For a point (a,b), the elementary cycle identity is

    [(a,b)] = ([a]−[a0])⊠([b]−[b0])
              +[(a,b0)]+[(a0,b)]−[(a0,b0)].             (VP.1)

Let z be any rational zero-cycle of degree zero and zero Albanese class. Its proper projections to A and B have zero degree and zero Albanese class by functoriality. The Abel map identifies CH0 of degree zero on a smooth proper curve with its Jacobian, so both projected Chow classes vanish. Summing (VP.1) therefore expresses z as a finite rational sum of the cross differences

    ([a]−[a0])⊠([b]−[b0]).                              (VP.2)

This argument only needs functoriality to the two curve Albanese varieties; it does not assume a further decomposition of the full Chow group of S.

The class x=[O_a]−[O_a0] in K0(A) has rank zero. Its restriction to every point of D is zero in K0(k), including when a or a0 belongs to D, since restriction is derived and rank is the K0 class over a field. The long exact sequence of the relative fibre consequently supplies an actual class

    x_tilde∈π0 fib(K(A)→K(D))

mapping to x. No uniqueness of this lift is asserted.

On B×B take the actual perfect class

    beta=[O_Delta]−[O_({b0}×B)]∈K0(B×B).

The second B is the parameter. Its fibre at b0 is zero, and its fibre at b is [O_b]−[O_b0]. These are actual equalities in perfect K0 by the regular, Tor-independent graph intersections. Exterior product of the fixed relative class x_tilde with beta is an actual class in F_S(B). Its endpoint difference has component image exactly (VP.2). Finite sums prove the assertion. This proof works integrally for individual cross differences; rational coefficients are used only to match the main project's conventions.

### Exact implication for the present specialization test

Taking a product of the marked-elliptic RC countermodel with an unrestricted proper curve does not produce an Albanese-kernel counterexample. Every cross-difference candidate is already an actual proper relative K0 relation. In particular, nonzero Pic0(A) in RC cannot simply be multiplied by Pic0(B) and declared to survive.

## VP.2. A restricted SNC component consequence (Proved)

Assume char(k)>0 and let E be a projective SNC surface. Suppose a component E_i is isomorphic to A×B and its entire reduced double-curve boundary is D×B for a finite reduced D⊂A. Then every class in T(E_i)_Q, with zero entries on the other components, lies in the image of actual proper K0 endpoint relations on E.

Indeed, set E_rest=∪_{j≠i} E_j. The actual binary closed-union descent square for E_i∪E_rest, after rationalization, identifies the relative fibre K(E_i,D×B)_Q with the fibre of K(E)_Q→K(E_rest)_Q. It therefore carries each relative family of VP.1 to an actual class on E×B with zero restriction to E_rest×B. The rational weight-two K0 projector preserves the desired endpoint component tuple. This uses exactly the positive-characteristic closed-union excision and finite gamma-filtration inputs already fully audited in C.3br/bt; it is not a new assertion of singular integral excision. Other components may have triple points, but none involving E_i occurs under the stated disjoint-fibre boundary hypothesis.

This is a restricted sufficient condition, not an automatic main-gate improvement. It does not apply to an arbitrary surface or an arbitrary boundary divisor.

## BP.1. Point blow-ups preserve a necessary marked-Picard correction condition (Proved)

Let two smooth surface components S and T of an SNC divisor in a regular threefold meet transversely along a smooth curve C. Blow up finitely many distinct points Σ⊂C away from all other strata. The strict transforms S' and T' are the point blow-ups, and over each x∈Σ there is a plane F_x. Its intersections with S' and T' are lines, identified with the exceptional curves e_{S,x} and e_{T,x}. The strict transform C' identifies with C and meets both lines at the triple vertex.

Consider arbitrary rational component divisor corrections M_S', M_T', and O_{F_x}(c_x). Every divisor class on a point blow-up uniquely has the form

    M_S'=π_S^*M_S + Σ_x a_x e_{S,x},
    M_T'=π_T^*M_T + Σ_x b_x e_{T,x}.                    (BP.1)

Here and below line-bundle classes are written additively. To see the decomposition directly, take a divisor representative and push its nonexceptional prime divisors to the smooth original surface; the difference is supported on the exceptional curves. Independence follows by restricting to the individual exceptional curves, where e_x has degree −1 and all pullbacks and other exceptional curves have degree zero.

Suppose the correction does not introduce a difference on the old positive-genus edge C', namely

    M_S'|C' − M_T'|C' = 0 in Pic(C)_Q.

It is enough to impose this equality; individual triviality of the two restrictions is unnecessary. Since e_{S,x}|C'=e_{T,x}|C'=[x], this condition gives

    (M_S−M_T)|C + Σ_x(a_x−b_x)[x]=0.                  (BP.2)

Orient both new edges from the old component toward F_x. Their degree differences are

    r_{S,x}=−a_x−c_x,      r_{T,x}=−b_x−c_x.           (BP.3)

Subtracting and using (BP.2) proves the necessary identity

    Σ_x(r_{S,x}−r_{T,x})[x] = (M_S−M_T)|C.             (BP.4)

Consequently, a defect of degree one on only the S'–F_x edge and zero on the T'–F_x edge can be corrected by such component divisor classes, while retaining equality on C', only if

    [x] ∈ im(Pic(S)_Q⊕Pic(T)_Q → Pic(C)_Q).            (BP.5)

Plane corrections affect both new edges equally and cancel out of (BP.4). Thus they do not remove this condition. The argument is necessary before any triple-point coherence question arises.

### Application to the proposed high-section construction

Let H be a global very ample line bundle and s a section whose zero set on C is the reduced divisor Σ. The bundle π^*H−Σe on each old component has trivial restriction to C', using s. High linear systems may indeed produce smooth proper curves disjoint from C'. However, the section gives the relation

    Σ_x[x]=H|C

in the old component restriction image; it does not supply each individual [x]. A graph of one of the new moving curves meets the new rational exceptional edges at parameter values. Correcting these one parameter value at a time by divisor-times-parameter-point classes requires the relevant individual versions of (BP.4), or a further proved relation among those parameter divisors. Numerical rational-edge surjectivity without the simultaneous C' condition does not suffice.

This calculation does not rule out corrections by arbitrary component K0 families, combinations across parameter values, or an additional argument using the Albanese-kernel condition. It identifies the gap in the proposed immediate reduction to rational edges. It is not a counterexample to UK.7.

## Unfinished crossed-boundary product test

For S=A×B and boundary (D_A×B)∪(A×D_B), both factors have markings. The family used in VP.1 need not vanish on A×D_B×P: its restriction can be a nonzero codimension-two class of A×P. Thus VP.1 does not settle this model. Conversely the RC proper-family calculation on each separate curve does not prove that every actual relative K0 family on the product factors into the two relative-curve groups. No such factorization, tensor exactness, Somekawa comparison, or surviving Albanese-kernel class is asserted. This remains a method test, not an E-specific theorem or counterexample.

## Proof and primary-source audit

The product calculation is the explicit cycle identity and actual relative exterior product above. Curve rank/determinant and Abel–Jacobi identification, graph perfection, Tor-independent restriction, K0 projectors and rational closed-union descent use the exact already-audited C.3br/bt and HK inputs. No fresh complete rereading of those external papers is claimed in this note.

For BP.1, the local blow-up geometry was freshly checked against the complete statements and proofs of The Stacks Project Authors, *Quadratic transformations*, Lemmas54.3.1–54.3.3, https://stacks.math.columbia.edu/tag/0AGP . These prove the exceptional curve, its O(−1) normal bundle, regularity, and the local Picard generator. Also freshly read the complete statements and proofs of *Blowing up*, Lemmas31.33.2–31.33.5, https://stacks.math.columbia.edu/tag/01OF . The global divisor decomposition and the correction identity are rederived above. Retrieval references: turn754758974view0 and turn754758974view1. No numerical program is needed or claimed, and no main result has been registered.

Written and full derivation checked: 2026-11-19T19:33:27.968631+00:00

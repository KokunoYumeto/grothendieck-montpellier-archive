# Independent checks: IX, scans 66–104

These are this run’s proofs and countermodels, not silent additions to the transcription. Finite enumeration is recorded in `code/finite_checks.py` and `outputs/finite_checks.json`; a symbolic proof is given whenever the conclusion ranges over infinite structures. No Lean verification is claimed.

## Notation and hypotheses

A **disjoncteur** is a set E with a symmetric relation ⊥ such that x⊥x implies x⊥y for every y. Put E₀={x:x⊥x}, A⊥={x:∀a∈A,x⊥a}, c(A)=A⊥⊥, ΣE={A:c(A)=A}, σE(x)=c({x}). A **spatios** is a complete ortholattice: a complete lattice L with an order reversing involution C and a∧Ca=0. Its orthogonality is a⊥b iff a≤Cb. These are the hypotheses actually given on scans 76–79. No distributivity, atomicity or orthomodularity is imposed.

For a set-valued correspondence α:E→P(F), write ᾱ(A)=⋃x∈A α(x) and fα(S)=cF(ᾱ(S)) for S∈ΣE. The latter formula always defines an isotone function. It need not preserve joins, and need not satisfy fα(σE(x))=cF(α(x)).

## P1. Inclusion in scan 66 does not justify the displayed equivalence

Take one-point irreflexive disjoncteurs E={p}, F={q}, α(p)={q}, β(q)=∅. The required inclusion ᾱβ(q)⊆cF({q}) holds and α even preserves and reflects orthogonality. But q⊥ᾱ({p}) is false while ᾱβ(q)⊥ᾱ({p}) is true. Thus the reverse implication in scan66:23 is unjustified. Scan67:49–76 explicitly replaces the inclusion by equality of closures; that replacement fixes this step.

## P2. The first arbitrary-generator lemma is false

Let E={0,1,2}, with the only orthogonal ordered pairs (0,1),(1,0). It is symmetric and irreflexive, hence satisfies both disjoncteur axioms. Its closed subsets are ∅,{0},{1},E. Let F={a}, with no orthogonal pairs, and set α(0)=α(1)=∅, α(2)={a}; all values are closed. Then fα({0})=fα({1})=∅, but {0}∨{1}=E and fα(E)={a}. Consequently arbitrary assignments E→ΣF do not extend to join-preserving maps by the displayed formula. This refutes scan72 Lemma1 literally. It does not refute the later corrected correspondence theorem.

## P3. Join preservation alone does not repair the earlier Lemma2

Take E={p,q} with no orthogonal pairs, so ΣE={∅,E}; take F={a,b} with a⊥b and b⊥a, so ΣF=P(F). Set α(p)={a}, α(q)={b}. The formula fα gives fα(∅)=∅ and fα(E)=F, a map preserving every join. The map g:P(F)→ΣE with g(∅)=∅ and g(B)=E for B≠∅ preserves all joins and satisfies fα(S)⊥B iff S⊥g(B). Thus scan73 condition(i) holds. But γ(a)={x:α(x)⊥a}={q} is not closed in E, so no raw pretranspose β of α exists. Condition(ii)/(iii) fails. Also fα(σE(p))=F≠{a}=cFα(p).

The missing equality is inserted on scan95:255–257 and acknowledged on scan97:351–355. These are an actual authorial correction, not an editorial conjecture. The strengthened theorem is P4.

## P4. Correct criterion for a pretranspose

For arbitrary α:E→P(F), the following are equivalent:

1. There is β:F→P(E) with α(x)⊥y iff x⊥β(y) for all x,y.
2. cF ᾱ cE(A)=cF ᾱ(A) for every subset A⊆E.
3. For every closed T∈ΣF, the set {x:α(x)⊆T} is closed in E.
4. Every γ(y)={x:α(x)⊥y} is closed in E.
5. fα preserves arbitrary joins, including the empty join, **and** fα(σE(x))=cFα(x) for every x.

(1) implies the subset adjunction ᾱ(A)⊥B iff A⊥β̄(B) by expanding both universal quantifiers. Replacing A by cE(A) does not change the right side. Testing all singleton y∈F proves (2). For (2)⇒(3), put U={x:α(x)⊆T}; ᾱ(U)⊆T implies ᾱ(cE(U))⊆T, hence cE(U)⊆U. Take T={y}⊥ to obtain (4). Under (4), set β(y)=γ(y)⊥. Then β(y)⊥=γ(y), giving (1). This β is the unique closed-valued pretranspose and is the largest raw pretranspose pointwise; any other has the same closure.

For (2)⇒(5), the join of closed Sᵢ is cE(⋃Sᵢ), and ᾱ preserves unions. For the converse, cE(A)=⋁x∈AσE(x), so (5) gives fα(cE(A))=⋁x∈A cFα(x)=cFᾱ(A). This also works for A=∅. It is exactly the argument completed on scan97 after the missing pointwise assumption is added.

For a pair α,β, the raw point adjunction is equivalent to the adjunction of the induced support maps **together with** the two closure-commutation identities. This is the repaired Proposition3 on scans90–93. Condition(iii)a alone is insufficient by P3. Normalizing each value by c leaves all orthogonality tests unchanged, but replacing a raw relation by another with the same induced support map is safe only after generator compatibility has been established.

## P5. Representation by a faithful join-dense family

Let σ:E→L, where L is a complete ortholattice, satisfy x⊥y iff σx⊥σy, and assume each a∈L is the join of {σx:σx≤a}. Define F(S)=⋁x∈Sσx and G(a)={x:σx≤a}. Then

G(Ca)=G(a)⊥.

Indeed, x∈G(Ca) iff σx⊥a iff σx⊥σy for every y with σy≤a, iff x⊥G(a). Therefore G(a) is closed, G preserves C, and FG=id. For closed S, the subsets S⊆GF(S) and S⊥⊆GF(S⊥) are orthogonal by faithfulness. If A≤B and CA≤D with B⊥D in an ortholattice, then A≤B≤CD≤A, hence B=A and D=CA. Applying this observation gives GF=id. The formulas yield order and complement preserving inverse bijections. Uniqueness follows from S=⋁x∈SσE(x).

The strong conditions on scans67–68 imply this theorem: apply σ(x)=cFα(x). The pointwise closure-density condition generates every σF(y); those elements already join-generate ΣF. Thus the question whether the resulting map is an isomorphism has an affirmative answer, subsequently proved in the general presentation on scans81–84. No global cardinality restriction is needed.

For a spatios L viewed as a disjoncteur, A⊥=↓C(⋁A) and c(A)=↓⋁A. Its closed subsets are exactly the principal lower ideals; a↦↓a is the claimed isomorphism. The orthogonality relation recovers a≤b by ∀z(z⊥b⇒z⊥a), and recovers Ca as ⋁{b:b⊥a}. On an arbitrary disjoncteur this recovered relation is a preorder, not necessarily antisymmetric.

## P6. Dense subdisjoncteurs and the scope of “order dense”

For D⊆E with induced orthogonality, the precise support-density condition is

S=cE(S∩D) for all S∈ΣE.

It is equivalent to join-density of σE(D), injectivity of S↦S∩D into P(D), and surjectivity of T↦cE(T) from ΣD to ΣE. For injectivity⇒density, put T=cE(S∩D); then T⊆S and T∩D=S∩D, so injectivity gives T=S. Under density, restriction and cE are mutually inverse ortholattice maps by P5. Surjectivity of cE likewise implies density because every S=cE(T) is generated by elements of S∩D.

The test using pairs is also equivalent, provided the quantified lower elements really belong to D: for x,y∈E, if D≤x⊥D≤y then x⊥y. The reverse implication to density follows by testing x against every y orthogonal to D≤x and applying the pair test. The source scan85:131 omits an explicit D-membership in its displayed quantifier; without it the condition is tautological and cannot characterize D.

The manuscript’s condition(iv), “dense for the canonical preorder”, must mean joins computed in the **support lattice**. It is not automatically the same as taking suprema only inside E. For E={e} with no self-orthogonality and D=∅, the empty set has supremum e in the one-element preorder E, whereas σE(D) does not join-generate the two-element lattice ΣE. Thus the ordinary intrinsic-poset interpretation makes the claimed equivalence false, absent a further convention. This is a semantic qualification, not a proposed ink correction.

For a given compatible preorder ≤ on E, it is contained in the canonical preorder. Therefore the stronger condition using the smaller lower sections D≤x suffices. This verifies scan88 Corollary3. The auxiliary scan86 lemma is immediate: if u=⋁S′≤ξ and every element η in a join-dense family with η≤Cu also satisfies η≤Cξ, density gives Cu≤Cξ, hence ξ≤u.

## P7. Normalized correspondences and their category

Every join-preserving f:ΣE→ΣF defines a normalized correspondence α(x)=f(σE(x)). Its reconstruction is f because the σE(x) generate. Isotonicity gives fα(σE(x))=α(x); P4 then applies. Thus normalized admissible correspondences and complete join maps are in bijection. The relation Rα={(x,y):α(x)⊥y} has closed rows and columns. Conversely such R defines α(x)=R(x)⊥ and a pretranspose using the closed columns. Note the orthogonal complement in this dictionary: Rα is generally not the graph of α.

Composition is (β∘disα)(x)=cG(⋃y∈α(x)β(y)). Under the above bijection it is ordinary composition of join maps, proving closure, associativity and identity σE. Every complete ortholattice L is a canonical support lattice by P5, so this gives the claimed categorical equivalence.

For f:L→M preserving arbitrary joins, let r(b)=⋁{a:f(a)≤b}; then f⊣r. Its orthogonal transpose is f†=CL r CM. Direct substitution gives f(a)⊥b iff a⊥f†(b). The transpose is unique, preserves arbitrary joins, satisfies (f†)†=f and (gf)†=f†g†. This is the canonical-category autoduality, and is not a claim that arbitrary point maps between disjoncteurs have an adjoint.

## P8. The OR product is smaller than the closed-fiber correspondence lattice

Read the ill-typed scan101 formula as (x,x′)⊥(y,y′) iff x⊥y or x′⊥y′; the reading alarm preserves the transcription unchanged. A product orthogonal complement is an intersection of sets whose each row/column is either the full factor or the perpendicular of one point. Hence every product-closed relation has closed rows and columns.

For a strict counterexample, take E=F={0,1,2,3} with only 0⊥1 and 2⊥3 (and their symmetric partners). Both support lattices consist of ∅, all singletons, and E. The diagonal R={(0,0),(1,1),(2,2)} has closed rows and columns. Any product point can be orthogonal to at most two of these three diagonal points: one through its first coordinate and one through its second. Thus R⊥=∅ and c(R)=E×E≠R. The program enumerates all 65,536 subsets of the 16-point product and finds 114 product-closed relations and 234 closed-fiber relations.

If E is trivial (x⊥y iff x≠y), then (R⊥)x=(Rx)⊥ and (cR)x=cF(Rx). Consequently closed rows are sufficient, and columns impose no condition. This proves the asserted positive special case without an atomicity assumption on F.

## P9. The complete lattice of correspondences need not be a spatios

For any complete lattices L,M, pointwise joins of join-preserving maps are join-preserving by exchanging the two joins. Thus Hom∨(L,M) is complete. Its infima generally are not pointwise infima.

Let L be the six-element lattice {0,a,b,c,d,1} with four incomparable atoms, any two distinct atoms joining to1 and meeting at0; pair a↔b and c↔d as orthocomplements. It is a complete ortholattice. A join map is specified by four values vi and t=f(1), with vi∨vj=t for every i≠j. Exhaustive enumeration finds 234 maps.

There are 40 atoms of Hom∨(L,L): sixteen maps with t a chosen target atom, exactly one source atom sent to0, and the other three to t; and twenty-four maps permuting the four atoms and taking1 to1. The latter are minimal nonzero because a smaller map with atomic top would need its nonzero value below three different atoms, while a smaller map with top1 must agree at all four atoms. Every nonzero map dominates one of these: if an atom has image0, the others equal t; otherwise either t is atomic or the non-1 atomic images can be extended to a permutation.

There are sixteen coatoms: choose one source atom and give it one target atom, send the other three atoms and1 to1. Every proper map lies below one of these. An order reversing bijection would induce a bijection between the atoms and coatoms. Since40≠16, this lattice has no order reversing bijection and in particular no orthocomplement. This refutes the universal hope on scans101–103 with its specified order, even for finite orthomodular factors.

The externally checked tensor results are recorded in `source_checks.md`. The count and the foregoing proof are this run’s independent certificate; no claim of novelty is made.

## P10. A general span factorization is impossible with the stated morphisms

Retain the six-element L of P9. Define f:L→L by f(0)=f(a)=0 and f(b)=f(c)=f(d)=f(1)=a. This preserves all joins: every pair of distinct source atoms has image join a, and empty joins are preserved.

The proposed decomposition in scan104 translates to f=h†g, where g:L→K and h:L→K preserve all joins and commute with the orthocomplements; K may be any complete ortholattice. Such maps also preserve all meets,0,1. If K is nontrivial, h has zero kernel. Indeed, if h sends some atom u to0, every other atom must go to1; two distinct other atoms then have images with meet1 although their meet is0. This is impossible. Thus the right adjoint r of h has r(0)=0, and h†(1)=C r(0)=1. Since g(1)=1, any such decomposition forces f(1)=1, contradicting f(1)=a. If K is the one-element lattice, its unique join map to L is zero, so the composite is zero and again cannot equal f.

This checks **all** possible intermediate K symbolically; enumeration merely verifies that the displayed f is a join map. The negative result applies to precisely the scan104 definition of morphism/comorphism. Factorizations using a weaker notion of map are a different question.

## P11. The set case

For sets E,F, a relation R corresponds to the union-preserving map A↦R[A]. Transposition satisfies R[A]∩B=∅ iff A∩Rt[B]=∅. With Γ=R and projections p:Γ→E,q:Γ→F, R=q∘pt, since a pair (e,f) lies in the composite exactly when it is represented by a point of Γ.

A union-preserving map P(E)→P(F) commutes with complements iff its singleton images form a disjoint partition of F. In that event there is exactly one function u:F→E whose inverse-image map it is. This includes empty-set edge cases. Transposition supplies the dual characterization of direct images.

For a trivial source E and any spatios M, Hom∨(P(E),M)≅M^E by values on singletons; its complement is therefore pointwise on those values. It is not pointwise on all subsets of E. For E={p,q}, M=P({a,b}), take f(p)={a},f(q)={b},g(p)={b},g(q)={a}. The generator values are orthogonal pairwise at each source point, but f(E)=g(E)={a,b}. Also a complement in the Hom lattice sends the empty source subset to0, whereas complementing f(∅)=0 in M gives1.

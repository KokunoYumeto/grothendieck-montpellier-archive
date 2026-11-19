# Targeted mathematical checks for VIII and IX01–08

These arguments are reconstructions made in this run on 19 November 2026. They do not emend the supplied transcription or decide its ink. Full reading is separately recorded in `coverage.tsv`. Finite computations are in `computations.py` and `computations_output.txt`.

## A. Double polarity and the complete ortholattice

**Claims:** C-SA21-8-034, C-SA21-9-022, C-SA21-9-025.

Let E have a symmetric relation ⟂ and define A⊥={x:∀a∈A, x⟂a}. Inclusion reverses under ⊥, and symmetry gives A⊆A⊥⊥. Applying these twice gives A⊥⊥⊥=A⊥. Thus cl(A)=A⊥⊥ is extensive, monotone and idempotent. Closed sets form a complete lattice: meet is intersection and join is closure of union. On closed sets ⊥ is an order-reversing involution. Under strict irreflexivity, S∩S⊥=∅, and De Morgan then gives S∨S⊥=E. If instead every self-orthogonal element is orthogonal to all of E, bottom is N=E⊥ and S∩S⊥=N. These are complete ortholattices, without a distributivity conclusion.

For an abstract complete ortholattice L, put E=L∖{0} and x⟂y iff x≤Cy. For any A⊆E, A⊥={x≠0:x≤C∨A}. Its second polar is {x≠0:x≤∨A}. Every such principal lower set corresponds to a unique element of L, including the empty lower set for 0. This verifies the converse representation used on IX52. Birkhoff1948, Chapter IV §§5–6, already proves the general polarity mechanism, including the weaker null-element meaning of antireflexivity.

## B. Spatial representation without the failed general sorite

**Claim:** C-SA21-9-028; cross-reference C-SA21-9-030.

Assume Σ is a complete ortholattice and A is the stated face-closed collection of elementary spatial figures. Let α(X) be the greatest support of X and assume α(A) is join-dense. Define β(S)={X∈A:α(X)≤S}. On A, X⟂Y iff α(X)≤Cα(Y).

For any S∈Σ,

\[
Y\in\beta(S)^\perp
\iff \forall X\,[\alpha(X)\le S\Rightarrow\alpha(Y)\le C\alpha(X)]
\iff \alpha(Y)\le C\bigvee_{\alpha(X)\le S}\alpha(X)
\iff \alpha(Y)\le CS.
\]

The last equivalence uses precisely join-density. Hence β(S)⊥=β(CS), and every β(S) is closed. Conversely for U⊆A, let s=∨α(U); direct calculation gives U⊥=β(Cs), hence U⊥⊥=β(s). Thus β maps Σ bijectively to the closed-set lattice; injectivity follows again from join-density. It preserves order and complement. In particular supp°A(X)=β(α(X)).

For X=(Φ,ρ), face closure says its principal subfigures all belong to A, and their greatest supports are exactly the elements of Φ. Transporting supports by β⁻¹ recovers Φ, and transporting incidence recovers ρ. The canonical deployment therefore becomes the original inclusion A⊆AtSpat(Σ). This is a direct proof of the representation under its actual hypotheses. It does not require the false assertion that every orthogonality-preserving correspondence induces the proposed support functor.

## C. Two separate failures in the functoriality attempt

**Claim:** C-SA21-9-030. The statements below are not interchangeable.

1. **Author’s complement example.** Let E={a}, E′={u,v}, with inequality as disjointness, and f(a)=u. This injective map preserves disjointness. For B={a}, f(B⊥)=∅ whereas f(B)⊥={v}. The closure operators are both identity, so this example does **not** refute the weaker formula cl′(f(cl A))=cl′(f(A)).
2. **Our counterexample to the weaker formula.** Let E={a,b} have no disjoint pairs; let E′={u,v} have u⟂v; set f(a)=u,f(b)=v. Disjointness preservation is vacuous but valid. In E, cl({a})=E; in E′, every subset is closed. Thus cl′(f(cl{a}))={u,v}, whereas cl′(f({a}))={u}. Every relation and closure is enumerated in the computation certificate.
3. **Valid remaining inclusion.** If α is a disjointness-preserving correspondence, α[B⊥] is orthogonal to α[B]. Since α[B]⊥ is closed, cl′(α[B⊥])⊆α[B]⊥. Equality needs an additional hypothesis; mere preservation proves only this inclusion.

The later Paseka–Vetterlein2025 Lemma3.5 proves the weaker equality for **adjointable single-valued maps**. Lemma3.7 and Theorem6.7 give corresponding functorial results with those hypotheses. They do not assert orthocomplement preservation for every such map, and they do not settle arbitrary atelier correspondences.

## D. The weakened face-disjointness axiom

**Claims:** C-SA21-8-018, C-SA21-9-024.

Take E={a,b,c,d,e}, incidence a<b,c<b and no other nontrivial incidences, open refinement equality, and symmetric orthogonality edges {a,b},{c,b},{a,d},{c,e}. Open-order, unique-carrier and face-lifting axioms hold; orthogonality heredity is trivial because open refinement is identity. Every pair of distinct comparable elements is orthogonal. But a,c are different faces of b and are not orthogonal, so the original common-face axiom fails.

The point supports are a°={a},b°={b},c°={c},d°={b,d},e°={b,e}. The five deployments are distinct; thus merely adding deployment injectivity does not repair the weakened comparable-pair axiom. If a purported axiom already requires the deployment to land in *spatial* figures, pairwise orthogonality is then implicitly restored by that well-typedness condition. The printed summary should be checked with this distinction in mind. The exact finite model is saved in the computation certificate.

## E. Five-element V-poset support calculation

**Claims:** C-SA21-8-045 and C-SA21-8-045R.

For a<b,c<b, the model has Pa,Pb,Pc,Sab,Scb. By the source formulas, Pa⊥Pb and Pa⊥Sab (equality at the left endpoint is allowed). Hence Pa⊥={Pb,Sab}; taking the intersection of their perpendicular sets gives Pa⊥⊥={Pa}. The source’s asserted cosupport {Pb} omits Sab, so its purported nonsingleton support does not follow.

The entire elementary figure {Pa,Pb,Sab} has empty perpendicular: no one of the five strata is orthogonal to all three. Its double polar is therefore all five elements. Its refinement shadow has only Pa,Pb,Sab, so the independent counterexample to whole-support=shadow remains valid without H. The computation verifies all original magasin axioms; this is a legitimate counterexample calculation, not a finite approximation.

## F. Infinite indexed-family counterexamples

**Claim:** C-SA21-8-026.

In N⊔{ω,q}, let An={ω}∪{k:k≥n} and A∞={ω,q}; index by inclusion. Then ⋂An={ω}, An°={n}, and A∞°={ω,q}. These interiors partition the total support. Every An meets the block A∞° only in {ω}, so saturation fails. No An can be recovered by the union of interior blocks whose indices are below it.

Add A={q}. Now A∞°={ω}, A°={q}; all interior blocks are singletons, so every set is saturated. Nevertheless A∞°⊆An while A∞⊄An. Thus saturation plus partition does not imply the order-detection condition γ. The formulas hold for every n and are an exact infinite example. The manuscript’s An∖A(n−1) in its second calculation is incompatible with its decreasing convention and is listed as a reading alarm, not silently corrected.

## G. Monotonicity alone does not extend to a figure map

**Claim:** C-SA21-8-030.

Source: the discrete two-stratum trivial maquette, with its full set as a figure. Target: two strata with incidence and open refinement equality and no disjoint pair. Both satisfy the original magasin axioms. Target figures are only ∅ and singletons, so the two nonempty elementary figures have no compatible join. The elementary-value assignment taking the two source strata to different target singletons is monotone. Source is finite and target uses its full figure collection. Nevertheless no join-preserving extension exists, since the image of the source’s two-element figure would have to be the nonexistent join. The extension assertion therefore needs compatibility of the assigned images.

## H. Triangle cosupport fails carrier closure

**Claim:** C-SA21-9-018.

Use the polyhedral magasin in the plane, a=(0,1), b=(0,0), c=(2,0), d=(1,0). Let Y=abc, X=abd, X′=bd, and Y′=bc. The relative interiors of Y,X,X′ avoid d, but the relative interior of Y′ contains d. X openly refines Y; X′ is a face of X and its carrier in Y is Y′. Thus Y,X,X′ belong to {d}⊥ while Y′ does not. All geometry is exact rational-coordinate incidence. This validates the negative answer on IX32–33. The large residual adds compatibility and its carrier argument works as given: a carrier in Φ would make an open-refining stratum orthogonal to itself.

## I. Finite counts and their scope

**Claims:** C-SA21-8-043, C-SA21-8-051, C-SA21-9-012.

For a fixed n-vertex flag, all vertices must occur and each of the n−1 consecutive interval strata may be independently included, giving 2^(n−1) figures. The empty flag gives the empty figure separately. Enumeration for n=1,…,6 confirms the count; the independent-choice argument proves it in general.

The five-type example has edges ab,bc,cd and included vertices a,c,e. Degrees are 1,2,2,1,0; therefore a is proper boundary, b lacunary, c redundant, d improper boundary, e isolated. The final degree-one boundary is {a,d}; earlier componentwise boundary language differs.

For a bounded flag with n intervals, its full figure has 2n+1 strata, so its power set has 2^(2n+1) elements. The claim that their supports remain distinct uses the support axiom, not cardinal arithmetic alone. The exact certificate computes closure for total-chain models n=1,2,3 and obtains 8,32,128 supports. This is a finite check of those models, not a proof of the entire arbitrary-poset support theorem. The source’s extension from a finite family to an arbitrary family of commensurable polygons requires a common finite flag; infinitely many different vertices do not have one.

## J. External support and faithfulness

**Claims:** C-SA21-8-033, C-SA21-8-038.

The 2 July marginal correction withdrawing natural-support faithfulness for topological pseudosegments is an authorial retraction. No independent topological model of that particular failure is supplied here, so it is recorded as a source correction, not independently refuted by us.

Full faithfulness is used for subsets Φ of one admissible figure F. In that restricted setting the source separates the represented complement by interiors of orthogonal strata; double polarity then gives supp-realization(Φ)=union of the selected interiors. Boolean operations within that figure follow from the resulting disjoint decomposition. This argument does not make the *global* support ortholattice Boolean, and it cannot be extended to incompatible figures without additional hypotheses.

## K. Checks deliberately not claimed

No unrestricted two-dimensional maquette/CW equivalence has been proved; no metric-space or topological-corde example has been independently formalized; no complete check of every alternate local axiom package has been performed; no handwritten sign was decided; no proof of the full polygon-complement theorem for every allowed poset was manufactured from finite enumeration. Those statements retain their exact on-page status and bounded literature assessment.

## L. L1 does not imply L2 in the abstract axioms

**Claim:** C-SA21-8-009; **problem:** MP-SA21-8-02.

Let M={x,y,X,Y}, incidence equality, and open-refinement order generated by x≪°X and y≪°Y. Declare only x⊥y and y⊥x. The open order is a partial order; general refinement is the same because incidence is equality. Each refinement has a unique carrier, and face lifting is automatic. Disjointness is hereditary under open refinement because its only disjoint elements x,y are already minimal. The common-face axiom is vacuous. Lieux are x,y and all four strata have a nonempty interior shadow, so L1 holds. However every lieu below X is disjoint from every lieu below Y while X is not disjoint from Y, so L2 fails. This refutes an *unrestricted* implication. It does not refute Grothendieck’s qualified expectation about unspecified practical examples. No external explanation for that expectation was found.

## M. Targeted independent check requested by root: side-contained contraction

**Root claim:** C-SA21-2-017. **Refinement:** R-SA21-side-contraction. This is outside the owned corpus and is recorded as a supplemental check, not silently added to the VIII/IX claim count.

The source passage was read in full context in the Pro transcription: IIscan2 definition of regularly immersed closed subset, IIscan4 Fic a–d, IIscan5 definition of the two sides of a lieu, IIscan7 lines1333–1338 replacement of the deleted avoidance condition by side containment. Li a explicitly places A inside its A-side even though the letter U/X is overwritten ambiguously. Thus the literal side-containment premise does not imply D∩A=∅. That textual uncertainty is retained.

Let X be a closed tripod with central vertex o and leaves a,b,e. Set A={a}, B={b}, and choose C={c} with c strictly inside the b-arm. X is compact Hausdorff; A,B are closed, nonisolated and disjoint, and removing either leaf leaves a connected graph. Each leaf has a closed interval neighborhood conical over one point. Hence (X,{A,B}) satisfies all four ficelle conditions. Removing c gives two components, the A-side containing o,a,e and the proximal part of the b-arm, and the B-side containing b. The point c has a conical interval neighborhood, so it is a lieu.

Take D to be the entire closed a-arm [a,o]. It is closed, connected and contractible, is wholly contained in the A-side of c, and contains A. It is even regularly immersed: the quotient X/D is a two-arm interval with the collapsed image d as its internal point, so d has a conical neighborhood over two points. The image of B is the b endpoint, and c is untouched. However (X/D)∖{d} has two nonempty components. Since the image of A is d, Fic c fails. This disproves the literal side-contained contraction assertion even with D connected and regularly immersed. Root owns the saved finite graph quotient computation; this check verifies its geometric hypotheses and the manuscript's allowed side condition independently.

The originally proposed Cantor-set version also works under the same reading: for X=[0,1], A={0},B={1},C={3/4} and D a scaled middle-thirds Cantor subset of[0,1/2], removing the collapsed A-image gives X∖D, which is disconnected. The finite tripod is the clearer main counterexample. The Cantor example additionally loses local conical regularity, since every neighborhood of the collapsed set contains a whole complementary-gap circle and that circle is a retract of the quotient. No Cantor computation is needed for the finite refutation.
## N. A faithful external support that is not fully faithful

This is a cross-cote check of the finite model supplied by the IX14–18 reader,
with stable identifier **R-SA21-9E-005** (source claim C-SA21-9-106).
The source question is VIII88–89, J156-8-11:309–344, repeated at IX124,
J156-9-16:105–115. The full-faithfulness definition is VIII86,
J156-8-11:188–209. Its ambient symbol is corrected by the author’s margin
from X to P; the mathematical interpretation uses that explicit correction.

Let the strata be 0,1,2,3, with equality as both incidence and open refinement.
Declare orthogonality exactly along the path 0–1–2–3. All least-carrier clauses
are identities, open-refinement heredity is automatic, and distinct common
faces do not occur. Thus even the stronger distinct-common-face axiom holds.
Take seven external points: private points p_i for each i and pair points
p_02,p_03,p_13 for the three nonorthogonal distinct pairs. Set S_i to consist
of p_i and the pair points carrying i. Every S_i is nonempty, the sets cover
and separate the external points, and S_i∩S_j is empty exactly when i⊥j.
With equality incidence, closed and open stratum supports agree. These facts
verify the external-support conditions and faithfulness of VIII68–71.

Full faithfulness nevertheless fails. For the allowed singleton figure
F={1}, the private point p_3 lies in P∖S_1. The strata orthogonal to 1 are
exactly 0 and 2, and p_3 belongs to neither S_0 nor S_2. Therefore the union
of supports orthogonal to F does not cover P∖|F|, contrary to VIII86’s
full-faithfulness condition. This direct verification needs no numerical
search and independently checks the separation asked for in VIII88.

The IX reader’s saved finite certificate additionally calculates the six-element
ortholattice generated by the virtual supports of the compatible middle pair
{1,2}; it is O6 and is not Boolean. That stronger calculation belongs to the
reader’s program and was read here, not rerun or represented as this agent’s
independent computation. The conclusion separates the exact two definitions;
it does not refute the valid theorem assuming full faithfulness.


The current outcome table precedes the dated checkpoint history. The report remains **INCOMPLETE**: the arbitrary-ambient structural questions A.3/A.4, sharp higher-dimensional B.3, and exact general B.4 index remain open. The narrower Noetherian-and-coherent refinement of E.2 is separately retained. All results described as proved below passed complete independent proof audits; each finite certificate has its precise scope recorded.

### A.4: eventual geometric and arithmetic groups for every ordinary elliptic pair

Let E1 and E2 be any ordinary elliptic curves over a perfect field of characteristic two, let X=E1×E2, and use the product of their cubic polarizations. There is a terminating procedure producing an integer d1 such that, in every odd degree d>=d1, both monodromy groups are GL_(9d²-1)(F2). In every even degree d>=d1, both are the full pointwise stabilizer of the three independent invariant covectors. Writing r=9d²-1, this consists of all matrices [A B;0 I3], with A in GL_(r-3)(F2) and arbitrary B. The representation is irreducible exactly in odd degree. The determinant character is trivial because the coefficient field is F2. This extends the previously completed fixed-product theorem to every ordinary elliptic pair.

The threshold is explicit through a finite terminating search. Enumerate chains of 3-isogenies E_i'→E_i until the product of the source curves has full degree-one GL8 monodromy, as decided by the already proved exact finite frame-cover algorithm. If the resulting odd degrees are m1,m2, take d1=max(m1,m2)+1. This is a terminating algorithm on an effective field of definition, and an existence construction over an arbitrary perfect field; no closed numerical bound uniform in the two elliptic curves is asserted. Chai(1995), Theorem2, printedp477, proves density of the fixed-prime ordinary Hecke orbit over every algebraically closed field. The checked geometric-integrality spreading lemma, Stacks Tag0559, Lemma37.27.5, supplies the nonempty open set of full-GL8 pairs that this search must meet.

There are two geometric steps. First, a universal one-factor Cartier calculation on y²+xy=x³+A x²+B, B nonzero, gives a constant invertible symmetrizer. Tensoring it gives a symmetric nine-dimensional pencil whose diagonal entries are independent coordinates. Its determinant contains the full squarefree diagonal monomial with coefficient one; every nonidentity matching term has a squared factor. This proves that the degree-one Hasse divisor is geometrically reduced. Uniform two-point jet bounds and a mixed-tacnode argument then show that the Hasse divisor is geometrically irreducible and reduced in every degree d>=2, with generic stable-rank drop exactly one. The common kernel of all invariant covectors is irreducible in every such degree. These assertions do not require finding the isogeny threshold.

Second, a generic degree-one curve on E1'×E2' has an ordinary nodal image under the odd product isogeny. The proof verifies double-point transversality and excludes triple points, including the loci where one translation coordinate is zero. The image has the exact divisor class O(3m2O) external tensor O(3m1O); the norm calculation controls the Picard-zero part as well. Adding a fixed grid realizes a degeneration in every degree d>=d1. The degree-one GL8 quotient can be isolated as an actual block acting trivially on a complement: the remaining node covers have symmetric-group factors of degree at most18, and their groups have no prime31, whereas GL8 has such a factor. The previously checked Goursat and first-cohomology arguments split the block. Transvection-group classification and the full translation-subgroup calculation then give the stated groups. All three invariant covectors in even degree are defined over the original perfect field, so the arithmetic group is the same pointwise stabilizer.

The root and reduction-descent agent each read and checked both complete proofs. The primary sources above were opened at the actual statements. The exact symmetrizer and product-isogeny incidence programs were independently executed; their finite calculations certify the algebraic identities and listed configurations, while the nodal and group arguments are proved in the paper.

### A.3: an exact all-degree parity formula on a supersingular product

For E0:y²+y=x³ over F2, X=E0×E0 and the same cubic product polarization, the generic relative stable rank is

    9d²-1 if d is odd; 9d²-3 if d is even.

The coherent relative dimension is 9d²-1, so generic relative Frobenius is bijective exactly in odd degree. Every even degree gives a defect of two. The ambient Picard scheme is smooth and crystalline cohomology is torsion-free. Thus this persistent defect has a different source from the earlier torsion counterexample. The full generic curve has genus9d²+1 and p-rank defect two or four according to parity. Its generic relative stable rank is positive in every positive degree.

For the upper bounds, restriction embeds Pic0(X) as an actual abelian subvariety of the curve Jacobian. The proof uses negative-twist Kunneth vanishing both to exclude a nontrivial geometric kernel and to show that the tangent kernel is zero. The dual norm map q has smooth connected kernel P, and its composite with the ambient inclusion is multiplication by m=3d. Thus f_Y=f_P and dimP=g(Y)-2. If m is even, X[2] embeds into P[2]. Functorial Verschiebung on these finite group schemes embeds the connected order-four kernel of V_X into the connected part of kerV_P. This forces dimP-f_P>=2 and the stronger even-degree upper bound. The argument concerns finite group schemes, not just their geometric points.

For the lower bounds, explicit Q8 automorphisms of E0 realize every positive integer as the degree of an endomorphism. The paper includes a complete four-square descent, including its equality case, and verifies the quaternion identities directly. For odd m, choose b with b†b=bb†=[m-1]. The isogeny [1 b;-b† 1] pulls back the product principal divisor to two supersingular elliptic graphs meeting transversely in m² points. The resulting nodal divisor has precisely the required line bundle N_m: equality of polarization homomorphisms gives a Pic0 difference, symmetry makes it 2-torsion, and the supersingular product has no nontrivial geometric 2-torsion points. Its stable rank is m²-1. Constant cohomology dimensions over the complete linear system, the finite-iterate rank condition and Bertini transfer that lower bound to generic smooth members. For even m=3d, a transverse union of sharp odd members in degrees3 andm-3 has stable rankm²-3. The same deformation argument gives equality. Projective normality identifies these complete linear systems with the actual ambient hypersurface systems.

The root and monodromy agent independently audited the complete proof. A separate exact certificate verifies the explicit automorphisms, both symbolic quaternion norm identities,4096 four-square witnesses, the degeneration arithmetic through10000 degrees, and all six retained Cartier matrix witnesses. The uniform theorem is proved geometrically and does not rely on extrapolating the finite checks.

### A.4: full degree-one monodromy despite a double Hasse component

The same supersingular product has geometric and arithmetic degree-one image GL8(F2) over every perfect characteristic-two base. In tensor coefficient coordinates s with3×3 matrixS, its relative Hasse polynomial is

    h(s)=det(S)²·(s^[2]t (J3 tensor J3) s),

where J3 reverses the three basis coordinates. The determinantal cubic and the second, smooth cubic are geometrically irreducible and distinct. Thus a double Hasse component is compatible with full geometric monodromy.

The proof derives the Cartier pencil from C(1)=0, C(x)=1, C(y)=x, C(xy)=y and the zero values on squares. After reversing the tensor basis it is the Hessian of detS. Its nine maximal Pfaffians are det(S) times the coefficient vector. The adjugate formula gives the determinant on the relative Euler-sequence hyperplane exactly, including both factors and their multiplicities.

Two explicit F8 points complete the group argument. The first has relative Frobenius polynomial T8+T7+T5+T+1, irreducible and nonreciprocal; an independent restriction-of-scalars27×27 characteristic-polynomial calculation confirms it. The second lies on the simple cubic component and has relative stable rank seven. Along an explicit tangent direction the determinant has a simple zero, and the first derivative on the one-dimensional Frobenius kernel has a nonzero component in the seven-dimensional stable subspace. A complete local lemma turns this into a wild transvection: lift the seven unit directions over a strict trait, write the last Frobenius column as (b(t),a(t)) with a of order one, and solve the Lang lift by Artin–Schreier equations with right side b/a². A nonzero simple pole forces ramification and hence a rank-one unipotent inertia element. Its normal closure, together with the irreducible nonreciprocal Frobenius element, is GL8 by the already checked transvection classification. The dense smooth-open restriction preserves the image; the two coefficient certificates do not require an additional claim that those particular curves are smooth.

The root and reduction-descent agent independently checked the complete proof and reran both the symbolic and extension-field certificates. The proof explicitly handles the Frobenius convention and the normal-closure step; it does not infer geometric monodromy solely from arithmetic Frobenius data.

### B.4: stronger wild lower bounds and an explicit 9-torsion ambiguity

The every-level wild elliptic construction now gives the character lower bound

    ν_min(3,2u,h) >= 1+min(s, floor((L+1)/2), floor((L+s+1)/4)),
    s=v3(u), L=floor(log3(u)), h>=2.

The two groups have identical full truncation at the indicated power of3, while the finite inertia action on one contains the order-four automorphism whose square is[-1]. This improves the earlier general lower bounds. It does not determine the least index.

A different explicit construction improves the smallest odd-ramification case further. Over K=Q3(zeta3), take

    B: y²-xy+y=x³-x²-28x-53,
    N=T_q[3∞], q=23328,
    M=B[3∞].

Then B[9] is isomorphic to T_q[9], whereas the manuscript characters have values-2 and2 on an inertia element of order two in the finite inertia image. Consequently ν_min(3,2,h)>=2 for every h>=2. The same construction proves the lower bound for every e congruent2 modulo4. The index convention is M(ν)=ker3^(ν+1); equality at9 is equality of M(1).

All data are explicit. The source curve y²-3xy-12y=x³-12x² has the rational point P=(0,0) of exact order nine. The paper displays all its multiples and an exact degree-nine rational isogeny with kernel generated byP, followed by the rational change of variables giving B. The descent function

    f=(x²-y)³(y-3x+4)/(x-4)³

has divisor9[P]-9[O]. Evaluating at5P and4P gives the connecting class-32/27; multiplying by(-3)^9 gives q=23328. The dual-isogeny sequence is the extension of Z/9 by μ9 classified by that Kummer class, and Tate's explicit finite group scheme identifies it with T_q[9]. The exact invariants c4=17·3^4 andΔ=-2·3^9 give integralj and potential good reduction forB. Its raw discriminant valuation overK is18, so every good-reduction ramification degreem satisfies12 dividing18m and hence is even. The faithful special-fibre inertia image therefore contains[-1], whose Dieudonne trace is-2. The Tate group satisfies the full manuscript filtration condition with good graded pieces μ_(3∞) andQ3/Z3, giving character2. It need not itself acquire good reduction, and the proof uses precisely the broader condition in B.4.

The root independently audited the whole construction and read Antieau–Auel(2021), AppendixA.1, LemmasA.1–A.2, printedp22, including the normalization discussion, and Tate(1995), “Points of finite order,” pp18–19. The retained certificate checks all81 subgroup additions, the degree-nine rational identity, the target change, both sets of invariants, the divisor identities and the Kummer adjustment. Whether index2 already suffices for every height-two group at(p,e)=(3,2) remains open.

### Executed root certificates and access record

| Program | Exact scope | Root runtime | Retained root output |
|---|---|---|---|
| ordinary_product_universal_symmetrizer.py | Universal polynomial symmetrizer, determinant and diagonal; tensor coefficients; matching tests through dimension7 |0.48850249600218376s |outputs/root_ordinary_product_universal_symmetrizer.json |
| ordinary_product_isogeny_incidence_checks.py |49 rank-one matrices,18424 triples,98 collinear triples, three derivative-relation models, prime31 |0.0528557190009451s |outputs/root_ordinary_product_isogeny_incidence_checks.json |
| A3_supersingular_product_checks.py |Q8, two symbolic norms,4096 four-square witnesses,10000 degeneration degrees, six exact Cartier witnesses |0.024118601999362s |outputs/root_A3_supersingular_product_checks.json |
| supersingular_product_degree_one.py |Nine symbolic Pfaffian identities, Hessian/gradient identities, all511 nonzero F2 sections |0.9957228610001039s |outputs/root_supersingular_product_degree_one.json |
| verify_supersingular_degree_one_group.py |Independent27×27 characteristic polynomial; irreducibility and nonreciprocity; local kernel, stable rank and derivative |0.04989594699873123s |outputs/root_verify_supersingular_degree_one_group.json |
| verify_p3_character_level2.py |All81 subgroup sums; exact degree-nine isogeny and changes; invariants, descent and Kummer identities |4.293367760001274s |outputs/root_verify_p3_character_level2.json |

Each listed program was read in full before its root execution, and author outputs were restored afterward. The archive also retains the author discovery programs and their outputs. Source checks for the supersingular rank proof include the original abelian-variety draft's Theorem4.38, Example4.40, Propositions5.19–5.22, Theorem7.5, Proposition7.6 and Corollary7.22. The norm existence argument is proved in the paper by explicit four-square descent; an unverified secondary pointer to a four-square theorem was not used. No priority claim is made.

The A.1 outcome-table wording has been tightened: the cup-product version of the transpose requires the stated torsion identification and includes the factor d. The paper already gave those qualifications. This is a reporting clarification, not mathematical movement. No proved passage from the preceding checkpoint has been withdrawn.

### Typesetting and completeness checks

The final paper has231 pages and265 numbered statements. The full LuaLaTeX/BibTeX build passed in24.248 seconds: zero overfull boxes before visual inspection and zero afterward; zero boxes over2pt; no undefined references or citations. The PDF size is1791586 bytes. We rendered31 pages, including every new section and a spread through the document, and actually inspected all eight montages. The root viewed montages1–6 and the obstruction/crystal agent viewed7–8. No clipping, overlap, missing glyphs or equation-number collision was observed. The retained inspection record is outputs/visual_qa_checkpoint09.json. The merged check register has300 events, the bibliography130 entries, and the source census131 rows including the unused Hua witness. Eighty-two agent program/output files were copied verbatim into code/, with their export manifest; the original agent files remain.

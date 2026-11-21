# Bounded specialization: checked research memo

Run: GHOSTS, 2026-11-21. Agent: /root/bounded_specialization. Model: GPT-6 Astra Pro (inherited); effort inherited, not separately observable. This is a mathematical proof review, not a Lean or other formal verification.

## Scope and conventions

Let K be a number field embedded in C, U a nonempty open of Spec O_K, and f:X -> U a smooth projective morphism of pure relative dimension g with a relatively ample line bundle L. Choose one relatively very ample power L^m only to construct Hilbert schemes; a bound D for the original L-degree corresponds to m^d D in that embedding, and all stated complexities retain their original L-degree. Fix r between 0 and g and write d=g-r. All cycle supports at a special fiber are over its algebraic closure. The degree of a d-cycle Z is deg_L Z=(c_1(L)^d . Z). Effective cycles have nonnegative INTEGER coefficients.

Let t be a rational absolute Hodge class on X_K. Deligne, *Hodge cycles on abelian varieties*, Proposition 2.9(b), says that the Galois action on the finite-dimensional Q-space of absolute Hodge classes factors through a finite quotient. We may therefore replace K by a finite extension so that t is fixed. After removing primes above a fixed auxiliary prime ell, its ell-adic component is a global section t_ell of R^{2r} f_* Q_ell(r). This replacement does not change geometric cycle complexities. The ordinary and supersingular labels, when used for abelian schemes, concern geometric Newton polygons and likewise survive residue-field extension.

For a geometric fiber s, define

c_ell(s)=min max(N,deg Z^+,deg Z^-),

where N is a positive integer, Z^+, Z^- are effective codimension-r cycles, and cl_ell(Z^+-Z^-)=N t_{ell,s}; set the minimum to infinity if there is no such triple. On the geometric characteristic-zero fiber, the same minimum in Betti cohomology is c_eta. Because the compared classes are rational, equality in one Q_ell realization is equivalent to Betti equality in characteristic zero. A compatible-all-realizations version c_all(s) satisfies c_ell(s)<=c_all(s).

No claim is made that such a class has a well-defined numerical complexity until X, L, r, t, and the coefficient convention have been fixed.

## B01. Proper bounded parameter spaces, including mixed characteristic

**Statement.** For every integer D>=0 there is a projective U-scheme H_D of finite type, with a finite collection of flat universal subschemes and fixed positive integer multiplicities, whose geometric points parameterize pairs of effective codimension-r cycles of degrees at most D. Every such pair occurs. The parameterization need not be injective. For every fixed positive integer N, the locus H_{N,D}(t_ell) where the represented difference has class N t_ell is an open-and-closed subscheme of H_D. In particular it is projective over U.

**Proof.** For an integral d-dimensional subscheme Y of a geometric fiber with degree at most D, its Hilbert polynomial belongs to a finite set P_D. This follows from the boundedness of reduced equidimensional subschemes of bounded degree: Grothendieck, FGA, Bourbaki Expose 221, Lemma 2.4. For every polynomial P in P_D, Hilb^P(X/U) is projective over U by Expose 221, Theorem 3.2. Write delta(P) for the L-degree, i.e. d! times the leading coefficient of P divided by m^d when the embedding uses L^m. The finite list comes from supports with original L-degree at most D.

An effective d-cycle of degree at most D is a sum sum_i m_i[Y_i] with at most D distinct integral supports, each m_i between 1 and D, and sum_i m_i deg(Y_i)<=D. Take the finite disjoint union Q_D of products

product_i Hilb^{P_i}(X/U)

indexed by the finite lists (P_i,m_i) satisfying sum_i m_i delta(P_i)<=D. Include the empty list, represented by U, for the zero cycle. Set H_D=Q_D x_U Q_D. It is projective and of finite type. On each factor the universal subscheme is flat over its Hilbert scheme. Every fiber has Hilbert polynomial P_i, hence top dimension d and top-dimensional fundamental cycle of degree delta(P_i). Nilpotents, embedded components, or lower-dimensional components at boundary points cause no problem: take the effective top-dimensional fundamental cycle, with its scheme-theoretic multiplicities. Thus every geometric point still supplies a valid effective cycle of the prescribed degree, and every desired effective cycle occurs by its integral supports.

The relative cycle-class construction gives a section of the pulled-back lisse sheaf R^{2r} f_* Q_ell(r) for each weighted flat universal cycle. The source permits fiber dimension at most d, without requiring pure-dimensional fibers. In Section 2.3.3 the more general weight has finite Tor dimension over the base, equivalently over the smooth ambient scheme; for a flat universal subscheme the weight is its structure sheaf. Thus it directly includes the lower-dimensional and embedded Hilbert-boundary phenomena. Its construction works over a singular parameter scheme: smoothness is required of X over the parameter scheme, and flatness of the universal subscheme supplies the relative fundamental class. Exact source: SGA 4 1/2, *Cycle*, Sections 2.3.1--2.3.3, with arbitrary base-change compatibility in Lemma 2.3.7 and Theorem 2.3.8. Smooth proper base change is SGA 4, XVI, Corollary 2.2 (with the locally-constant coefficient hypothesis from the published erratum, automatic here).

Subtract the negative universal class and N times the pullback of t_ell. The resulting global section Delta of a lisse Q_ell-sheaf is zero at one geometric point of a connected component if and only if it is zero at every geometric point of that component. One can see this from the fundamental-group description, or after multiplying by a power of ell and reducing modulo every ell^a. A noetherian scheme has finitely many connected components, each open and closed. Consequently the zero locus is an open-and-closed union of components. This is H_{N,D}(t_ell), proving the claim. QED.

**Why this repairs the sketch.** Smooth proper base change alone does not construct a class condition on an unspecified Chow scheme. The finite Hilbert parameterization and the relative cycle-class theorem provide the missing objects. Neither regularity nor flatness of the parameter scheme over U is required for B01.

## B02. Fixed-multiplier arithmetic criterion (precise form of sketch 2.5)

**Statement.** Fix positive integer N and nonnegative integer D. The following are equivalent:

1. There are effective integral cycles Z^+,Z^- on X_{bar K} of degrees at most D with cl_B(Z^+-Z^-)=N t.
2. At infinitely many good finite places v in U, there are such cycles on X_{bar k(v)} with ell-adic class N t_{ell,v}.
3. At every finite place v in U there are such cycles in the ell-adic realization.

Here primes above ell have been removed from U. For a compatible family of realizations the same equivalence holds if the local requirement asks for one pair of cycles realizing the class in all those realizations.

**Proof.** By B01, the condition at s is exactly nonemptiness of the geometric fiber of the proper map H_{N,D}(t_ell)->U. Its image is closed. A proper closed subset of U has only finitely many closed points: U is a noetherian integral scheme of dimension one, and every proper closed subset is a finite union of dimension-zero irreducible components. Thus (2) forces the generic point into the image. The generic fiber is a nonempty finite-type K-scheme and has a closed point over a finite extension K'/K. The corresponding cycles have the same degrees and their ell-adic difference equals N t_ell. Embed K' into C compatibly with the initial embedding. Comparison with Betti cohomology and injectivity of H^{2r}(X(C),Q(r))->H^{2r}(X(C),Q(r)) tensor Q_ell show that their rational Betti difference is N t. This proves (2)=>(1).

If (1) holds, the generic fiber of H_{N,D}(t_ell) is nonempty; its closed image must be all U. Hence (1)=>(3), while (3)=>(2) is immediate because U has infinitely many closed points.

For the simultaneous version, the reverse implication needs only one fixed ell and has just been proved. Conversely, take the actual characteristic-zero cycles from (1), define them over a finite extension, and specialize them along each good trait using properness of their Hilbert schemes. Degree and effectiveness are preserved. Compatibility of cycle class maps with specialization gives the target equality in every chosen realization. This is a statement about one specialized pair of cycles, not a separate choice for each ell. QED.

**Coefficient warning, B02a (refuted literal reading).** If the words “N t is algebraic” mean membership in CH^r tensor Q and N is prescribed, the sketch's wording is false. On P^g, take t=(1/2)h^r and N=1. It is rationally algebraic, but every integral cycle has integer coefficient of h^r in rational cohomology, in every characteristic. No difference of effective integral cycles has class (1/2)h^r. The corrected alternatives are: specify that N t is the class of an integral cycle; or quantify existentially over N. This issue disappears for the intended c(s) criterion, which quantifies over N.

**Existing literature.** Brünjes--Serpé, *Uniform bounds and ultraproducts of cycles*, arXiv:0901.4853, Definition 2.3(ii) and Theorem 3.4 already establish the bounded-rational-complexity principle for infinitely many closed points; the extension to number fields is discussed immediately before Section 2. The proof here supplies the geometric-fiber, fixed-(N,D), proper-parameter form and avoids presenting the principle itself as a new discovery.

## B03. Eventual exact constancy or cofinite divergence of the least complexity

**Statement.** In the setup above:

(a) If c_eta=C_0<infinity, then c_ell(v)<=C_0 for every v in U, and c_ell(v)=C_0 outside a finite subset of U.

(b) The same eventual equality holds for c_all(v), provided the class realizations and specialization are compatible as in B02.

(c) If c_eta=infinity, then for every finite C the set {v:c_ell(v)<=C} is finite. Therefore c_ell(v) tends to infinity in the cofinite filter on the good primes; so does c_all(v). If local algebraicity is known at every good prime, this means finite values escaping every fixed bound, not failure of local algebraicity.

**Proof.** The finite bound C amounts to the union over 1<=N<=C of H_{N,C}(t_ell). By B01 this is a finite union of projective schemes. Its image F_C in U is closed, and its generic fiber is nonempty exactly when c_eta<=C.

If c_eta=C_0, then F_{C_0}=U. If C_0>1, the generic fiber for C=C_0-1 is empty, so F_{C_0-1} is finite. Outside it, c_ell(v)>=C_0, establishing (a). For C_0=1 the minimum is already the smallest allowed value, so there are no smaller values. For (b), specialization of a triple realizing C_0 gives c_all(v)<=C_0 and c_ell(v)<=c_all(v); combine with (a). If c_eta=infinity, every F_C is a proper closed subset, hence finite, proving (c). QED.

**Meaning for ordinary and supersingular primes.** Fix A,L,t once. If its Weil class is known to be algebraic (for example in an applicable case of Markman's theorem), the least local complexity is the SAME unknown integer C_0 at all sufficiently large good ordinary primes and all sufficiently large good supersingular primes. This statement holds along either set if it is infinite. Constructed theta-cycle degrees or a chosen CM-transport denominator may still grow with p. Their growth is not growth of the least complexity.

B03 computes the shape of the function, not the value C_0 or its finite exceptional values. It must not be described as a numerical solution of the prompt's main problem.

## B04. A single-prime criterion and a class-independent exceptional integer

**Statement.** For each D, there is a nonzero integer b_D depending only on the polarized model X/U, the codimension, and the chosen finite Hilbert parameterization H_D, such that H_D is flat over U[1/b_D]. If v does not divide b_D and a pair of effective cycles of degrees <=D represents N t_{ell,v}, then a pair of the SAME degrees bounds represents N t over bar K. There is no bound required on N in this statement. In particular, if c_eta>C, then every v with c_ell(v)<=C divides b_C.

**Proof.** Generic flatness, EGA IV_2, Theorem 6.9.1, applied to the finite-type morphism H_D->U and O_{H_D}, gives a nonempty open V over which H_D is flat. Its finite complement can be removed by inverting one nonzero rational integer b_D.

Take a point z in H_{N,D}(t_ell) over v not dividing b_D. Flatness of H_D->U implies going-down for prime ideals, so z has a generization z_eta lying over the generic point of U. More explicitly, in affine neighborhoods a prime q of a flat O_{K,v}-algebra lying over the maximal ideal contains a prime q_eta over (0). Since H_{N,D}(t_ell) is open and closed in H_D, it contains every generization of z, including z_eta. Its generic fiber is nonempty. Choose a closed point of that generic fiber and apply the comparison argument of B02. This gives the requested characteristic-zero cycles with the unchanged N,D. The last assertion follows with D=C. QED.

**How b_D can be made concrete, without deciding a Hodge-class equality.** Once explicit equations of the finite Hilbert parameterization H_D are supplied, cover it by finitely many affine schemes Spec A_i over R=O_K[S^{-1}]. Let T_i=ker(A_i->A_i tensor_R K), the R-torsion ideal. It is finitely generated as an A_i-ideal. Choose nonzero a_i in R annihilating its finitely many generators. After inverting product a_i, each A_i is R-torsion-free; over the Dedekind domain R this means R-flat. Replacing product a_i by a nonzero rational integer divisible by its norm gives b_D. This eliminates all vertical embedded torsion as well as vertical irreducible components. It is deliberately a potentially nonminimal exceptional integer.

The construction uses the full H_D and is independent of t and N; one need not identify class-correct connected components computationally. Standard effective ideal arithmetic can produce the torsion annihilator when an explicit finite presentation and the finite Hilbert list are provided. No such presentation or b_D has been computed for the unspecified T5 family in this run. A general bound for its size is not being asserted.

**Concrete gate for a growing construction.** Suppose a CM construction at v produces a representative of degree D(v) and denominator N(v). A sufficient condition for global algebraicity is ONE place v with v not dividing b_{D(v)}. If a fixed C works for infinitely many places, this condition is automatic. If D(v) grows, neither infinitude nor effective distribution of the places establishes this condition: the exceptional integer also depends on D(v). This is the exact extra arithmetic-geometric comparison a GRH-assisted strategy would need.

## B05. Descending complex representatives without increasing complexity

**Statement.** Suppose X,L are defined over an algebraically closed subfield k of C, and a rational Betti class t on X(C) has a compatible ell-adic class on X/k. A pair of complex effective cycles of degrees <=D whose difference has class N t can be replaced by such a pair defined over k. In particular, the geometric characteristic-zero minimum over bar K equals the complex Betti minimum.

**Proof.** Use the fixed finite product of Hilbert schemes attached to the given supports and multiplicities. A C-point lies on a connected component after base change to C. Over the algebraically closed field k the connected components of this projective finite-type scheme are geometrically connected, so that component is the base change of a component over k. It contains a k-point. The two points give the same ell-adic class, because the family class is a global section of the constant cohomology sheaf for X times the parameter scheme. Degree and multiplicity data are unchanged. Comparison with rational Betti cohomology gives the desired equality. QED.

## Proof review and remaining limits

Full proof reread on 2026-11-21 by this agent, checking each implication, finite-extension step, geometric versus rational residue fields, finite Hilbert support list, flat universal families, relative class construction, zero-locus condition, and the rational/integral multiplier distinction. No fault found in B01--B06 in the stated setup. The main remaining limitation is quantitative: C_0, b_D, and the exceptional local minima are not numerical data supplied by these theorems. The theorem gives no new global algebraicity outside cases where bounded local data or known characteristic-zero cycles are available.

No original Grothendieck archive cote scans were provided to this agent. The exact FGA/EGA/SGA locators below are verified or source-checked at the indicated level; no archival transcription correction is inferred.

## Source locator register

- FGA: A. Grothendieck, *Techniques de construction et theoremes d'existence en geometrie algebrique IV: les schemas de Hilbert*, Seminaire Bourbaki, Expose 221 (1961), Lemma 2.4 (printed p.255; PDF scan index 7 when cover is index 0), Theorems 3.1--3.2 (printed pp.259--260; PDF indices 11--12). Original: https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf . Text of both statements read.
- EGA: Grothendieck--Dieudonne, EGA IV_2, Section 6.9, Theorem 6.9.1 and Lemma 6.9.2 (generic flatness/freeness), Publ. Math. IHES 24 (1965), p.154. Metadata at https://www.numdam.org/articles/10.1007/BF02684322/ . Full original PDF too large for web retrieval in this run; exact theorem text independently returned by indexed retrieval. This is not a new proof-check of EGA.
- SGA 4: Expose XVI, Corollary 2.2, original p.214 (smooth proper specialization); corrected hypothesis requires locally constant F. Re-edition https://www.normalesup.org/~forgogozo/SGA4/16/16.pdf , PDF pp.4--5. Statement and its derivation from 2.1 read. SGA 4 1/2 erratum p.312 supplies the omitted hypothesis in the original statement.
- SGA 4 1/2: A. Grothendieck, redige par P. Deligne, *La classe de cohomologie associee a un cycle*, LNM 569 (1977), pp.129--153; Sections 2.3.1--2.3.3, Lemma 2.3.7, Theorem 2.3.8, Remark 2.3.10. Original chapter metadata: https://link.springer.com/chapter/10.1007/BFb0091521 . Retypeset source linked by Milne: https://github.com/NomiL/sga4.5/blob/master/sga4.5-4.tex . Exact 2.3.7 and 2.3.8 statements also indexed at https://math.bu.edu/people/yangzhe/Cohomologie_Etale.pdf (retypeset p.70). IAS original https://publications.ias.edu/sites/default/files/Number32.pdf exceeded web size limit and direct download was denied (403). Distinguish a source-locator check from verification of the entire cycle-class theory.
- P. Deligne (notes by J.S. Milne), *Hodge cycles on abelian varieties*, LNM 900 (1982), Proposition 2.9(b); revised author-hosted text https://www.jmilne.org/math/Documents/Deligne82.pdf , pp.18--19. Statement and proof (three alternatives) read. Proposition 2.9(a) also records invariance of absolute Hodge cycles under extension of algebraically closed fields.
- L. Brünjes and C. Serpé, *Uniform bounds and ultraproducts of cycles*, arXiv:0901.4853, Definition 2.3(i)--(ii), Theorem 3.4; number-field extension described at the end of the introduction. https://arxiv.org/pdf/0901.4853 . Statement and proof of 3.4 read; its entire nonstandard foundational dependency chain was not re-proved.

## Check events (tab-separated)

statement_id	date	who	type	outcome
B01	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Full proof reread; finite Hilbert parameterization and relative cycle classes address singular parameter and mixed-characteristic concerns; no fault found under stated assumptions
B02	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Full proof reread; fixed N,D preserved; geometric fibers and finite extensions checked; no fault found
SKETCH-2.5-fixed-N-rational-reading	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	refuted, with the refined statement's id	B02a counterexample P^g and t=h^r/2,N=1; refine to B02 integral-cycle reading or existential N
B03	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Full proof reread; finite closed threshold loci yield exact eventual constancy; all-realizations squeeze verified
B04	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Full proof reread; flat going-down supplies horizontal generization; open-and-closed class locus contains it; b_D independent of t,N
B05	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Full proof reread; projective connected components over algebraically closed field are geometrically connected; degree and class unchanged
FGA-221-L2.4	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	used and rechecked in this run	Original statement read; bounded degree reduced equidimensional subschemes verified; proof not fully re-proved
FGA-221-T3.2	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	used and rechecked in this run	Original statement read; projectivity for fixed polynomial verified
EGA-IV2-T6.9.1	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	carried as background without fault found	Exact indexed statement and canonical metadata checked; original full PDF retrieval exceeded size limit
SGA4-XVI-C2.2	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	used and rechecked in this run	Statement read in re-edition with original-locator markers; locally-constant coefficient erratum explicitly imposed
SGA4half-Cycle-L2.3.7-T2.3.8	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	used and rechecked in this run	Relative construction and exact arbitrary-base-change statements read via retypeset source; foundational proof not fully re-proved
DELIGNE-1982-P2.9b	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Statement and three proof alternatives read in author-hosted corrected text; finite Galois orbit supplies class spread
BRUNJES-SERPE-T3.4	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	used and rechecked in this run	Statement and proof read; analogous known bounded-complexity criterion identified; nonstandard foundations carried as background

## B06. Denominator boundedness is automatic once total numerator degrees are bounded

**Statement.** In the setup of B01 with t_ell nonzero, fix D. There is a finite set M_D of positive integers such that whenever any geometric fiber s admits effective integral cycles Z^+,Z^- of degrees <=D satisfying cl_ell(Z^+-Z^-)=N t_{ell,s}, one has N in M_D. In particular, uniform boundedness of the two numerator degrees along infinitely many primes is equivalent to rational algebraicity of t; one need not assume a separate bound on their positive integer multipliers. The same assertion holds for a connected noetherian characteristic-zero parameter base carrying a nonzero flat rational section t and a smooth projective family: bounded total numerator degrees on a dense set imply bounded c and hence algebraicity everywhere.

**Proof.** H_D has finitely many connected components C_1,...,C_m. Write alpha for its universal difference class and beta for the pullback of t_ell. Every stalk of beta is nonzero, because the original section is nonzero and the base U is connected. For each component C_i, there is at most one integer N for which alpha=N beta holds on C_i: two such integers would give (N-N')beta=0 in a Q_ell-vector space and hence N=N'. If alpha=N beta at a geometric point, the lisse-section argument in B01 makes this equality hold throughout its connected component. Let M_D contain the positive integers arising in this way. This set has at most m elements and contains every multiplier that can occur.

If bounded degree D works at infinitely many primes, either take the finite upper bound max M_D and apply B02 with a repeated multiplier, or choose just one of those primes not dividing b_D and apply B04. Conversely, a rational algebraic cycle can be written (Z^+-Z^-)/N, so specialization gives a uniform numerator degree bound. If t=0, take N=1 and both cycles zero, so the conclusion about algebraicity and complexity is trivial even though the unrestricted set of possible multipliers is infinite.

For a connected noetherian characteristic-zero base, use the analogous finite Hilbert parameter scheme and its finitely many connected components. Each component again admits at most one multiplier. The union of the relevant components is therefore projective, and its image is closed. A dense set of represented fibers forces its image to be the whole base. QED.

**Scope.** The degrees here COUNT integer multiplicities in Z^+ and Z^-. This does not assert that a bound on reduced supports, a rationally normalized degree, or a denominator alone controls complexity. It also does not numerically evaluate max M_D. The reduction is nevertheless strict: an attempted uniform construction can focus on the degrees of the integral numerators; independent denominator estimates are not logically required once those degrees are bounded.

**Check event.** B06\t2026-11-21\tGPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization\ttargeted proof check\tWhole proof reread; at-most-one-N per component uses nonzero flat t and Q_ell coefficients; zero-class and multiplicity conventions separated; no fault found

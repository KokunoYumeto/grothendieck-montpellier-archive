# Bounded search: noncyclic odd covers and the missing rational-unit input

Date: 2026-11-21. GPT-6 Astra Pro, effort not exposed, AN_GRH `/root/row_audit`.

## Outcome

The bounded primary-source search did **not identify a theorem** giving, for every prescribed finite-field pair (C,P), an allowed odd prime-to-p pointed cover and a useful nontrivial actual factor with zero rational p-primary group, or zero geometric stable part. This is a report about the inspected sources, not a claim that no such theorem exists anywhere.

There is already a genuinely small integral operator for a noncyclic cover: `1-z`, for a nonidentity odd-order deck transformation z. The exact missing input is the vanishing of the entire actual image of that operator on rational p-primary torsion. Raynaud's Heisenberg construction does not provide that input. Its no-theta conclusion gives singular coherent Frobenius maps of large dimension, not their nilpotence or the absence of the arithmetic eigenvalue1.

No new finding ID or main-gate progress is claimed.

## Primary sources inspected and exact limitations

### Raynaud (already retained and checked)

M. Raynaud, *Revêtements des courbes en caractéristique p > 0 et ordinarité*, Compositio Mathematica123 (2000),73–88, DOI10.1023/A:1001840726893.

Primary PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16AB72912D3CE32BFC5D012B1025A8E4/S0010437X00000440a.pdf/revetements-des-courbes-en-caracteristique-pandgt0-et-ordinarite.pdf

Exact inputs: Proposition1(4)–(6), printedp75; Theorem2, p76; Heisenberg construction, p84; Theorem17 and Corollary18, p85; genus2,p2 choice m5,n3, p86. These passages and their displayed proofs were already read completely and were rechecked during the preceding A48 corollary.

The theorem works over an algebraically closed field and gives a representation with no theta divisor. It does not state a finite-field prescribed-point splitting condition or a rational p-torsion assertion. Proposition1(6) in fact permits tensoring a finite representation with another one to make it ordinary; the theorem is about ordinarity, not vanishing stable cohomology. Tensoring does not preserve a prescribed-point Frobenius condition for free.

For the explicit genus-six Heisenberg stage, its nontrivial central irreducible representations have rank3^6=729. The associated nontrivial degree-zero bundle has H0=0 and Euler characteristic729(1−6), hence coherent H1 dimension3645. A singular map on this multiplicity space need not have zero stable part. The A48 geometric corollary now makes this distinction on actual curves as well; no new matrix illustration is needed.

### Pacheco–Stevenson: exact embedding problems, but with a p-kernel

A. Pacheco and K.F. Stevenson, *Finite quotients of the algebraic fundamental group of projective curves in positive characteristic*, Pacific Journal of Mathematics192(1) (2000),143–158.

Primary PDF: https://msp.org/pjm/2000/192-1/pjm-v192-n1-p08-s.pdf

Read §1 (including definitions and Theorem1.3/Corollary1.4), the relevant representation bounds §2, and the complete statements and displayed proofs of Theorems7.1 and7.4. This is not a whole-publication proof audit.

Theorem1.3, printedp145, solves an embedding problem G→H when G has a normal p-Sylow subgroup P, with H=G/P. Its condition is m_chi·dim(chi)≤gamma_(cover,chi). These are lower bounds on existing geometric generalized Hasse–Witt multiplicities. Theorem7.1, pp154–155, specializes this when the given H-cover is ordinary. Theorem7.4, p155, is an existence criterion for some genus-g curve (equivalently the generic locus) when H is abelian; it does not prescribe an arbitrary finite-field source or point.

The mismatch is exact: a nontrivial new stage supplied by this embedding theorem has p-group kernel, so its degree is divisible by p and is outside the allowed prime-to-p cover class. If one insists that G have order prime to p, P=1 and the displayed embedding problem supplies no new extension. Even apart from this degree issue, no arithmetic Frobenius fixed-space or rational-unit assertion is present.

### Yu Yang: generic new-ordinary covers and geometric marked points

Y. Yang, *Raynaud–Tamagawa theta divisors and new-ordinariness of ramified coverings of curves*, retained primary author PDF:

https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/RTOC.pdf

Read introduction §§1.1–1.3, the exact statements of Theorem3.5 and Corollary3.6, and the complete Proposition4.2 statement and its short displayed proof. Printed manuscript locators: Theorem3.5 pp20–21, Corollary3.6 p22, Proposition4.2 pp24–25. No full proof audit of Theorem3.5 or its preceding degeneration results is claimed.

Theorem3.5 and Corollary3.6 concern generic curves or generic points of p-rank strata and give new-ordinariness under their ramification hypotheses. Their conclusion is maximal stable rank, not zero stable rank or arithmetic eigenvalue1 avoidance. The word “pointed” denotes the marked geometric curve over an algebraically closed field. It does not assert a split fibre over a prescribed finite-field rational point.

Proposition4.2 again concerns a cyclic prime-to-p quotient extended by a p-group, using positive Hasse–Witt multiplicity bounds. It has the same p-kernel obstruction as Pacheco–Stevenson for this task.

### Tamagawa: generalized Hasse–Witt interpretation

A. Tamagawa, *On the Tame Fundamental Groups of Curves over Algebraically Closed Fields of Characteristic >0*, MSRI Publications41 (2003),47–105.

Primary PDF: https://library.slmath.org/books/Book41/files/tamagawa.pdf

Read introduction items(i)–(v), printedpp48–49, describing generalized Hasse–Witt invariants as stable images of the character Frobenius map, and the theta-based maximal-rank estimates. These are geometric maximal-rank statements. No theorem here was used as a rational-pointed vanishing result, and no whole-paper review is claimed.

## The exact small-support criterion is already available

Let D→C be a constant odd Galois étale cover over k, with g(C)≥2 and a chosen rational point P′ over P. Let z be a nonidentity deck transformation (therefore of odd order), and define the actual k-abelian subvariety

    B_z = im(1-z : J_D → J_D).

If B_z(k)[p]=0, then B_z(k)[p^infinity]=0. Under a hypothetical point-section collision, the retained lifting argument supplies a rational p-primary class δ=[Q′−P′], with Q′ over a distinct base point Q. Thus (1−z)δ lies in B_z(k)[p^infinity] and is zero. Hence

    zQ′ + P′ ~ Q′ + zP′.

The two effective degree-two divisors are distinct because the P′ and Q′ deck orbits lie over distinct points. They determine the unique hyperelliptic pencil of D. Its involution commutes with z, so the two pairings imply z²P′=P′, contradicting the free odd-order deck action. This is precisely the already-retained B.1 stabilizer argument, applied to the actual image of 1−z; it is not a new separation theorem.

For the Heisenberg group one may take z in its central order-three subgroup. Then 1−z selects the whole nontrivial central-character packet. The operator really has support two, so a support-size failure is not the obstacle in this natural case. The missing assertion is

    B_z(k)[p]=0,

or, more strongly, f(B_z)=0, for an actual cover split at the prescribed P. Raynaud proves neither.

More general primitive rational projectors can isolate other noncyclic packets, but an arbitrary simple Fp[G] component is not by itself an actual rational abelian factor. A noncyclic extension of the A46 argument must separately control a Galois-stable actual projector, its integral coefficients/support, and the field generated by translates of the resulting rational function. None of the inspected existence theorems supplies these together with the required Frobenius vanishing. This caution does not claim a noncyclic extension is impossible.

## Why descent and twisting do not fill the arithmetic input

For any actual factor B over a finite field, B(k)[p]=0 means that arithmetic Frobenius has no eigenvalue1 on its geometric étale p-torsion. Geometric nonordinarity only bounds the dimension of that torsion space. If the space is nonzero, some finite extension rationalizes it; extending constants to obtain a prescribed lift therefore cannot be assumed to preserve a rational-unit condition. Existing rational torsion is never removed by such an extension.

The same distinction prevents using an unpointed good twist without a separate compatibility proof. A rational point in the prescribed fibre fixes its Frobenius torsor class. The known geometric results neither choose that arithmetic class nor prove the needed eigenvalue avoidance for it. A48 already records the precise cyclic pointing obstruction; this search does not replace it with a noncyclic supply theorem.

## Search boundary

The search was limited to primary-source leads for solvable/odd étale covers, generalized Hasse–Witt representations, relative class-number conditions and rational p-torsion. Both web search systems were used; exact primary papers above were opened. Results about Artin–Schreier covers, relative class number exactly1, generic ordinary Pryms, or unrelated characteristic-zero Pryms were not treated as a solution. No search-hit snippet was promoted to a theorem, no unsupported global nonexistence assertion was made, and no stopped historical/GT/Galois workstream was reopened.

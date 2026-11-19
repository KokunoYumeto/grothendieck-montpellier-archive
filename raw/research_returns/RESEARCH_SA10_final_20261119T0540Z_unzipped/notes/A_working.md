# Part A working notes

## Gates

A.1: A pro-topos is not an object of the 2-category Topos. Formulate pro-bicategorical gluing and distinguish from shape gluing. Investigate all-pair counterexample on 0⊂R⊂C. Need iterated intersection stones.

A.2: Pullback neighborhood systems cofinal for closed continuous maps: for W open containing f^-1(Y), take X minus f(Xprime minus W). Open immersion counterexample Xprime=X minus Y. This matches the manuscript correction: 151/071 says proper local immersion but explicitly NOT open immersion.

A.3: The remaining stratum centers agree, but pro-neighborhoods of their closures can retain ghost ends from deleted lower strata. Controlled tubes germed along open strata versus closed-stratum germs must be distinguished.

A.4: 151/053 premise does not actually force relation on I antisymmetric: object-level partial order may cycle indices using non-surjective embeddings. Need counterexample and correct diagram embedding condition, then meet condition fails absent cartesian squares.

## Confirmed finite certificates

check_A_finite.py checked all 14 canonical nonidentity inclusions among 9 distinct all-pair/triple germs; all compatible, overlap p→u disagrees. Successor witness 32 assignments, zero extensions. Finite-meet corollary: 7 indices, 12 points, colimit singleton.

stable_graph_meets.py complete inverse-edge-expansion enumeration: genus1 n1,n2,n3 counts2,5,23 and genus2 n0 count7 satisfy conditional meets. Failures at (1,4),(2,1),(3,0), explicit witnesses in output. Families: g>=3 use separating (1,g-1) vs nonseparating loop on g-1, with loop moved to either side in two-edge refinements; g2 n>=1 same with markings on different sides of loop; g1 n>=4 use 2-cycles separating leg1 and leg2, common refinements triangle [1],[2],[rest] and square [1],[3],[2],[rest].

## A3 explicit obstruction

X=C, closure strata0,R,C; delete0. Original V12=germ_R(C)\{0} has constant homotopy type S1, whereas induced germ_{R*}(C*) retracts onto R*, two points. Deleted stones have two versus four components. Cofinal variable-width tubular strips give the calculation.

## Correct 151/071 reading

The text explicitly inserts 'mais PAS (ou une imm. ouverte!)'. Study line221 and prompt A.2 misreport it as asserting open-immersion compatibility. The nearby identity R'_ij=f^-1R_ij is nevertheless false if recomputed by support containment after strata coincide: f:{0}→R with X0={0},X1=R. Use order-defined R_i^ord=union_{k:not i<=k}Xk for stable pullback.

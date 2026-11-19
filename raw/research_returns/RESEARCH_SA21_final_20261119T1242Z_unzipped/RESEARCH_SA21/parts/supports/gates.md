# Support gates — closed

Final mathematical status,19November2026: all gates listed in the historical notes below are closed. A03/A04 give the arbitrary-poset exact tests; A06 gives the Boolean interval class; A26/A27 give the complete split transfer and finite conditional-lattice classification. A09 and A10 separate finite and infinite figures; A14/A14a settle the atom class; A16 includes all four support-theorem clauses; A20 verifies the faithful external-support counterexample. Every finite model is certified, with independent audit records. The initial notes below are retained as work history, not current open claims.

# Support gates (active)

## 19 November 2026, initial deductions and computations

- A.1 whole M(L) is not invariably orthomodular: for L={a,b<c,d}, M(L) has eight strata and twenty supports; {Pa}<{Pa,Pb} is closed and the relative orthogonal difference is empty. Every figure satisfies supp 1. Code: supports_core.py and explore_supports.py; output magasins_initial.jsonl. Full formal verification pending.
- Sumner normality does not imply double-polar orthomodularity even for comparability graphs: the positional order of that eight-stratum M(L) is a witness. Need full normality proof and all-dimensional replacement criterion.
- M(L) finite: enumeration through n=5 exactly agrees with conditional lattice criterion (every bounded pair has meet/join). Need proof, likely reduction to Jenca 2022 proper-quotient orthoset of doubled L; infinite case requires separate cut criterion.
- M(L) Boolean conjecture now precise: non-isolated elements of L form a single chain. Counts through n=6 agree (2^n-n naturally labelled orders). Need proof via point-closedness and faithful-chain decomposition.
- A.5 candidate complete finite example: M={a,b}, incidence identity, a <<° b; |o| empty; P={a,b}; |a|={a}, |b|={a,b}. Faithful normalized support, not full for F={a}. Need typed verification of support-function conditions.
- A.3 arbitrary orthoset atom condition: N(x) subset N(y) implies N(x)=N(y), for every tested x and all y. Strong separation is N(x) subset N(y) implies x=y; manuscript conflates atom with this stronger condition. Need exact scope of lieux and all-stratum tests.
- A.4 finite-figure theorem criterion is admissibility of orthogonal family of open supports. Distinguish finite joins/complements from arbitrary subset complete embedding.

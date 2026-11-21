# Root final proof and computation audit

Run GHOSTS-20261121, /root, GPT-6 Astra Pro; runtime-default effort is not separately exposed.

## W01–W03

The entire written proofs were read. The binary a=2 parity argument uses O_K/(2)=F4; the ternary z=1 residue formulas reproduce both lower diagonal entries and the off-diagonal entries exactly. The z=0 exceptions have the asserted norm pairs and zero mutual inner product. The curve moment matrix retains actual pushforward multiplicity. For W02, all positive pair degrees without a degree-one pair are at least two; the rank-one 2-by-2 degree array forces all four entries to equal two. The n=2,b=1 case has a geometrically integral generic fiber because the conjugate component degrees must divide one, and the fixed unit-graph quotient gives exactly the asserted curve degrees. W03's saturated lattice makes the minors primitive; the only nonunit budget is norms3 and4. No gap found.

## W04 complete scope and code audit

The entire theorem and self-contained Python file were read. Each numerator has at most two nonzero-Weil components; two components must both be automorphism graphs. The complete period list has exactly four pairs. Coordinate inversion plus numerator exchange replaces the omitted plus-period1 pair by plus-period2 and sends the full target q to its negative. Both fixed-factor graph orientations occur. Zero-Weil extras include all six coordinate graphs and the degree14 primitive two-minor exceptions. The dynamic program admits every multiplicity. The bound156<1001 makes encoded equality an exact equality in all70 exterior coordinates, including subtraction of q. The matched numerator degrees follow from theta^2 q=0. No floating-point or probabilistic equality is used.

The original full catalog and comparison were copied into an isolated directory and independently executed. The output agrees at every degree, including 79,234,032 tested negative candidates at degree22. The portable self-contained certificate was then executed separately to completion and printed PASS W04. The later additional explicit sign-involution assertion was executed by importing the current module and running the target/upper checks; it passed. No search logic changed. These are executed integer computations, not formal proof-assistant certificates.

## R42–R45 and V07

All complete written proofs were read. Source theorem statements for Hoa, Haiman–Sturmfels, Poonen–Testa–van Luijk and Basu were inspected at the exact cited locators. R43's carrier map is simplicial and homotopic to the supplied marking inside common old simplices; orientation decisions are effective semialgebraic tests. R44 was independently derived using tracked monic bases and coefficient clearing; standard monomials are free by independence after embedding in the fraction field. The full R45 composition retains the marked geometric-place and good-model hypotheses. V07's two integral exterior coefficients give the stated unimodular minor, and the revised V04 denominator proof was reread.

The final framework map is contextual: it does not attribute the new bounds or algorithms to a conjectural archive passage. The archive, equivalence-relation, and source-scope distinctions match the separate source audit.

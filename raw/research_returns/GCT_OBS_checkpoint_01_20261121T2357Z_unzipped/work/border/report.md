# Border-rank work: provisional report

## Results reached

- **BR-001:** independent standard-library reconstruction verifies every one of the 25 previously non-independently recomputed seventh-minimum prolongation cases. There are 12 determinant cases covered by six two-dimensional-extension representatives and their transposes; 8 permanent cases of this type; two determinant P-15 transposes and two permanent P-15 cases; and P-19. The new arithmetic is sparse exact Gaussian elimination, independent of the inherited certificates and generators.
- **BR-002 (whole-proof review pending):** the integral divided-power coefficient tensors of `det_4` and `per_4` have CP border rank at least 43 over every algebraically closed field. The proof replaces the inherited modular certificate collection with full exact rank computations and arithmetic localization. All denominator/branch primes occurring in the computations divide 6; the necessary exceptions in characteristics 2 and 3 are separately recomputed. Characteristic 2 uses equality of determinant and permanent tensors. Literal unit replacements for all 9038 inherited minors are not claimed.

## Independent computations

`check_twodim_extensions.py`: 14 representatives, covering 20 cases. Q results reproduce all saturation/increment/conditional counts. Additional P-19 is included and correctly returns exactly eight remaining pairs.

`check_higher_prolongation.py`: independently enumerates all P-19 exact zero-pattern strata and obtains eight fixed spaces. For each, first prolongation rank 130, first kernel dimension 13, second prolongation rank 79, hence `P22` dimension 12. This works over Q and F2. The determinant P09_A type in F2 has eight analogous spaces and is also excluded; transposition handles its partner.

`check_support9.py`: recomputes all P-15 support and parameter strata without input certificates. It matches 46119, 46119, 51985 eligible supports and all published residual counts. It is an independent implementation of the exhaustive arrangement method, not a rerun or NumPy wrapper.

`check_koszul.py`: recomputes full Koszul ranks by torus weight blocks, ignoring every inherited selected minor. The 11 determinant support/Koszul cases and 1506 permanent Koszul cases all give at least 14 over Q. Determinant cases also all give at least 14 in F2 and F3. Rational pivot prime divisors are 2 and 3 for det; 2 for per.

`check_cover.py`: independently recomputes the 25 determinant Borel ideals and 1152-element permanent symmetry group; validates 1517 disjoint orbits and exhausts all 8347680 seven-subsets, with exactly 1543608 low-support subsets covered. This retains only original representative lists and orbit-size claims as input and checks those claims.

## Technical caveats addressed

1. A raw rational elimination can hide positive-characteristic failures. The new code records every nonunit pivot. In support9 compatibility tests it also records nonzero scalar numerators/denominators used by a direct zero test. This adds prime 3 for determinant support9; that case is rerun in F3.
2. In positive characteristic, symmetric squares in prolongations mean invariant tensors in a tensor square, not division by two. All wedge-kernel calculations retain diagonal tensor entries and impose transposition symmetry directly.
3. A finite-field rank result applies over its algebraic closure because the same finite matrix has the same rank after scalar extension. Linear-arrangement strata are interpreted over the infinite algebraic closure.
4. The `Space` RREF and nullspace implementation was compared with independent SymPy RREF on 196 seeded integer matrices, all passed. This is arithmetic validation, not a mathematical proof by sampling.

## Still open

The 44 target has not been settled. The inherited exploratory substitution files already try deleting low variable coordinates in used-variable factors and often yield only lower bounds 14--16. New work should avoid relabeling those attempts as new progress. The main remaining possibilities are exact treatment of Borel parameter families, stronger multigraded conditions, or an explicit rank-17 degeneration for a ten-plane.

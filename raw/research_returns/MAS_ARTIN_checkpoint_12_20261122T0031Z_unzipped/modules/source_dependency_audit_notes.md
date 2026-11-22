# Documentary audit of the global-to-local dependency chain

**Scope.** This audit freshly reads Masullo (2026), §§12.3–12.5, printed pp.514–520, in full. It compares the exact assertions with the checked results already in this project. It does not supply a new mathematical theorem, count a new movement, or claim that every possible global-to-local factorization fails. The accompanying TSV gives one row per dependency. Source PDF and extracted pages remain private working material.

## The decisive distinction

Section12.3 contains a heading and the footnote “Include section.” Thus the intended global-to-local deconstruction has no argument in that section. On p.516, StepIII explicitly requires identifying the kernel of the local truncated operator with the kernel denoted by kPW. On p.517, the draft computes the kernel of a local physical Fourier-cutoff composition and assigns it that notation. Computing and naming this kernel does not identify it with the kernel obtained from the weighted global orthogonal Paley–Wiener projection.

MA-PI-001–003 refute the canonical theta intertwining between these two constructions on actual source vectors. MA-PI-002 works in the literal printed realization, including the exact norm-half twist used on p.515; MA-PI-003 also gives principal-sector witnesses satisfying both polar conditions. The draft does not print the exact canonical intertwining equation tested by these theorems. The correct documentary conclusion is therefore: the required identification is not supplied, and a specific natural candidate is false. It is not a source claim that every other factorization is impossible, nor do these counterexamples prove that every scalar trace identity is false.

The separately author/root/PF-reviewed MA-PI-004 extends this canonical obstruction to the actual non-induced cubic character over Q(zeta3), retaining the different prime3 and conductor prime269, both physical Fourier shells, and genuine flat source data. This audit read its statement and exact arithmetic/source scope; it does not claim a new complete proof reading of PI004.

## Page-by-page dependency map

### 1. The local theorem and its actual hypotheses: p.514

Theorem12.4.1.1 assumes a structural finite set containing all archimedean places, class-group triviality after localization, all field-ramified places, and the indicated outside-S unit invariance of the test. These hypotheses must remain in applications. The field-ramification condition is additional to character ramification; it cannot be dropped when specializing to a nontrivial imaginary-quadratic character.

Footnote2 itself flags unfinished cutoff work: a one-sided support convention and then an independently moving lower endpoint, followed by a corresponding convergence analysis. This is an acknowledged source-scope gap. MA-LA-014–015, MA-CQ-003–004 and MA-GA-001 provide actual repaired local quotient operators in their stated scopes. The StepII frequency cutoff is a norm ball; the symmetric-annular frequency alternative belongs to MA-LA-016 and is a different operator.

### 2. The claimed source factorization: p.515

The proof fixes the norm-half twisted Sobolev realization, asserts nuclearity of the truncated quotient-Paley–Wiener operator, and invokes a factorization through a local theta image followed by cyclic trace transfer. Its claimed topological identification cites Proposition5.3.4.4 and has the footnote “Return here after the Proposition is updated.” That proposition's stated transform/image criterion does not itself specify the continuous inverse, actual nuclear lift, or commuting operator diagram needed for the cyclic transfer. Range inclusion alone is insufficient.

This is a missing map/topology justification, not a claim that a local quotient or a continuous section cannot exist. MA-LA-011, MA-CQ and MA-GA construct actual local quotient maps and sections; MA-MO-017/028 prove actual local-source returns on their stated completed-ideal domains. Those results keep their own metrics and domains and do not identify the global weighted orthogonal projection with the physical cutoff.

### 3. Literal operator assertions: pp.515–516

The operator displayed on p.515 contains an output factor |x|^(1/2). The raw K displayed in (12.4.1.7) on p.516 does not. MA-LA-008 proves the exact relation A=UK with U equal to multiplication by that factor. This is a repairable coordinate omission; moving to K coordinates also requires conjugating the other operators consistently.

The raw tensor containment following (12.4.1.7) would make the raw output constant on input S-unit coinvariant classes. MA-LA-009 gives a compact flat source counterexample: K is equivariant, but does not annihilate the input relations. Taking the output quotient or choosing an actual section is the valid repair.

StepII on p.516 claims that the product-norm position cutoff maps additive Schwartz data into the flat source. MA-LA-010 refutes this domain/codomain assertion in the mixed-place case, for both ball and annular product-norm multipliers: the required uniform finite-place local-constancy level is lost. Such multipliers remain bounded on additive L2; that weaker fact does not give the printed Schwartz mapping.

### 4. What is actually computed on pp.516–518

StepII explicitly specifies a Fourier norm ball, then convolution, then the physical position multiplier. Equations(12.4.1.8)–(12.4.1.10) compute the associated local physical-composition kernel. The p.517 notation kPW is assigned to that kernel. This supplies the local calculation, subject to the corrected quotient/source domains, but not the missing comparison with the global orthogonal projection.

The subsequent invocation of nuclearity is ambiguous if interpreted upstairs. MA-LA-012 proves that a nonzero unit-equivariant operator of this form cannot be compact on the full additive L2 cover. The p.515 nuclearity assertion concerns a quotient PW level, and p.517 subsequently uses a fundamental domain and unit sum. Accordingly, the audit does not attribute an explicit full-cover trace-class theorem to the draft. It rules out that interpretation and requires a genuine quotient/nuclear factorization. Actual quotient traces do exist.

The p.518 substitution and logarithmic-volume calculation are local orbital calculations. They neither construct a global intertwiner nor remove the independent lower-cutoff/rate issue flagged in footnote2. MA-LA-014–015 and the character/general-field extensions establish the corrected local limits with the operator order, conductor/different factors, compact sector, and thin-profile comparison retained.

### 5. The limiting theorem and the global reuse: pp.519–520

Page519 requires both printed smoothing products to tend to zero. It does not impose the additional slow-band relation between the two large radii. MA-LA-015 extends the actual repaired local theorem to all bounded smooth source profiles with vanishing logarithmic transition width. Its paired full-test comparison uses the explicitly stated slow-band relation; this additional relation must not be silently attributed to p.519.

Theorem12.5.1.1 assumes vanishing on the entire norm-one subgroup, not merely one point in a general character decomposition. Page520 chooses S with field and character ramification, structural/class-group conditions, test invariance, and all relevant small primes. These choices explain why the outside-S prime contributions vanish for the chosen compact support; they do not identify the remaining S-kernel.

The p.520 dependency chain is: decompose the global kernel into its S-part and outside-S parts; remove the latter using the cited shell theorem; invoke Theorem12.4.1.1 to identify the S-part with the local distributions minus the two polar terms; and then identify the global trace with the relative-strip zero sum by the spectral construction. The third step is the unsupported global-to-local kernel comparison. The absent §12.3 is precisely where such a comparison would have to be supplied. The local theorem alone does not prove the equality of the global S-kernel and the local physical quotient kernel, the compatibility of the exact Hilbert metrics, the cutoff limiting remainder, or the polar subtraction.

MA-FT-001/002 and the actual Gram/resolvent constructions distinguish these issues. They provide proved operator limits and an exact arithmetic deficiency criterion in their stated regimes. The canonical-map obstruction is an independent domain/comparison result, not an unconditional elimination of that arithmetic criterion.

## Verification scope and records

The present pass read every line of the extracted pp.514–520, then reread the relevant completed assertions and scope paragraphs of MA-LA-008–012 and the existing global-bridge discussion, the MA-LA-015 source-profile passage, MA-GA's original flat-source/quotient definitions, and MA-PI-002's exact printed-realization statement. It uses the separately recorded full proof reviews for the existing theorems; it does not relabel this documentary pass as a fresh complete proof check of all cited modules. In particular, PI003 is used with its root/S5 whole-proof records, not a new whole-proof claim by this auditor.

The immutable Review05 snapshot remains unchanged. Its CQ003 canonical-map component is the single previously unresolved component addressed by PI001–003. RF003 overlaps it; neither is a second independent movement, and neither broad all-factorization question is declared closed.

## Reference

Masullo, A. M. (2026). *The music of the primes* [Unrefereed draft]. https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf. Exact source scope: §§12.3–12.5, pp.514–520; inherited interface locators include Proposition5.3.4.4, Definition11.2.1.3, Proposition12.2.2.2, and LemmaC.3.2.2. This audit does not claim a new full proof review of those inherited results.

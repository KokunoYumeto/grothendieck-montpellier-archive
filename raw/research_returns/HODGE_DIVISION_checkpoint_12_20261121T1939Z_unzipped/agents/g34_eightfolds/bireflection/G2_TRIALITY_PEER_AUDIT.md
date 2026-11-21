# Whole-proof audit: D-G2T01–03

**PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro,
effort inherited/unexposed, HODGE_DIVISION, 2026-11-21,
approximately17:44–17:48 UTC.

I read the entire proof and bibliography, the source extractor,
the complete original-expression parser, the rational-polynomial
checker and the small-table checker. The reviewed proof SHA-256 is
`a10858e963218bbe96a32f0db909245c87554a3cf9c8660117a15b964f8b366c`.
I also wrote and executed a separate independent reconstruction of
every new generic inequality and every small-group spectrum.

## Published table input and exact scope

I freshly opened the official GenericCharacterTables introduction,
complete inventory for G2 and triality, and the complete generic
cyclotomic definition at:

- <https://oscar-system.github.io/GenericCharacterTables.jl/stable/>
- <https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/>
- <https://oscar-system.github.io/GenericCharacterTables.jl/stable/cyclo/>

The eight G2 conditions partition every characteristic and relevant
congruence class. The three triality conditions partition the even
and the two odd residue cases. These are full ordinary character
tables, unlike the separately labelled unipotent-only entries for
other families on the same inventory. The official inventory credits
the exact published Enomoto–Yamada, Enomoto, Chang–Ree and
Deriziotis–Michler sources stated in the proof.

The cyclotomic documentation defines each entry as rational polynomial
coefficients times exponentials of real rational expressions in the
integer parameters. At every admissible specialization those phases
have absolute value one. Thus the new proof can ignore all additional
phase relations and parameter restrictions while retaining an upper
bound. No hidden positivity or reality of the character values is
assumed.

The original published table classifications are inputs, not new
results proved by this audit. The exceptional multiplier list and
the small ATLAS normalizer conventions retain the independently
read primary-source checks recorded earlier for D-BI21/22. Fresh
web attempts to open the two J-STAGE PDFs timed out, although their
downloaded copies and source hashes are retained by the author.
I do not claim to have reconstructed those original classification
proofs or freshly read the inaccessible Chang–Ree/Deriziotis–Michler
full proofs in this event. The official complete mathematical table
inputs and their source boundary are explicitly preserved.

## Generic all-field proof

The formal unit products may be collected only when equal; treating
all others as independent can enlarge the triangle bound but cannot
decrease it. After translating q to q0+x, taking absolute values of
each coefficient before summing is valid for every real x≥0. The
coefficientwise comparison with one quarter of the degree polynomial
therefore proves the inequality simultaneously for all admissible
field sizes and all character/class parameter values. A finite range
of numerical q is not being extrapolated.

The trivial row, identity column, declared degree polynomials and
class lengths are all checked against the original inputs. Every
other class length is greater than one on the claimed range. Every
nontrivial degree polynomial has nonnegative translated coefficients
and the stated positive constant lower bound. This establishes both
the trace bound and the minimum degree without leaving a small-q
parameter exception inside the generic range.

## Small covers, outer operators and tensor factors

The universal covers include all exceptional central characters,
including representations factoring through a proper central
quotient. Exact pointwise or inner-product restriction selection
retains precisely the extension rows irreducible on the core.
The universal-cover lifting and scalar power rescaling prove that
every compatible outer operator occurs, up to scalar and an inner
factor, in one of the checked cyclic extensions. The argument does
not assume every outer automorphism stabilizes every central kernel.

For the generic field sizes, the commutator inequality uses actual
rank of the commutator minus identity and minimum eigenspace support
of the original operator. The scalar-commutator case is treated
separately and is stronger. This correctly includes outer inertia
without a character-table classification of all outer extensions.

The intrinsic simple-factor and derived-preimage argument forces
every normalizer to permute factor matrix algebras. The factorwise
maximum-eigenspace bound passes to tensor products. For a nontrivial
permutation cycle, finite order up to scalar makes the product twist
diagonalizable; a weighted basis-word orbit contributes at most one
vector to a prescribed eigenspace. Constant words and all other
orbits give the stated quarter bound. Mixed factor types are allowed
because only isomorphic represented factors can be permuted.

The actual intermediate-cover argument rules out positive base genus
and forces at least twelve genuine branch points in a rank-nine
source. Combining this with total moving rank2e+6 gives e≤24.
All tensor products have degree at least144. Every generic single
factor exceeds24, and every small single factor has the stronger
quarter bound forcing e≤6 against minimum degree at least12.
The conclusion and the explicit exclusion of nonsimple G2(2) are
therefore correct. No determinant or inducing-field-equality
assumption has entered the proof.

## Independent reconstruction and exact results

`audit_g2_triality.py` imports no author parser or checker. It reads
the immutable original-entry JSON, independently checks its extraction
against all eleven cached source files and their exact hashes, then
uses a new sparse rational AST interpreter. Its monomials record the
q-power and a formal multiset of phase atoms. It checks every
translated coefficient inequality directly from the original table
expressions, rather than accepting the author's coefficient list.

The first run correctly rejected an unrecognized `R(...)` ring
coercion occurring inside an exponent. After inspecting the original
source declaration `R=base_ring(S)`, I added the explicit identity
coercion rule and reran the complete calculation. No inequality,
phase value or published data was changed. The final run passes
all318 nontrivial row types and9,242 entries.

For the six small groups I reused my own previously reviewed
Ramanujan Fourier implementation, not the author's polynomial
Fourier helper. Rows are independently selected by rational-trace
restriction norms. All three normal fusions and their power maps
are checked. The result passes239 selected rows and11,502 complete
nonscalar spectra, with precisely the printed minimum degrees and
ratios. The complete combined run took1.355seconds. Its full output,
input hashes, final proof hash and source boundary are retained in
`audit_g2_triality.json`.

This is a whole-proof mathematical audit, fresh official-source
verification and independent complete arithmetic reconstruction.
It is not a new proof of the published finite-group classifications.
No TeX compilation was performed.

# Post-checkpoint15 root audits

INCOMPLETE. General D.1, general D.2(ii), and the corresponding part of L8 remain undecided. This record describes actual reads and proof checks after the immutable checkpoint15. None of the auxiliary work recorded here is, by itself, formal-review movement.

## Canonical defect and weighted genus

Root read both complete C proof files and all used Stacks passages: 0BVT; 49.15.1–2 in0DWM; the complete0E9Z proof; and the full54.7.1–8 chain in0AX7/0AXD. Root also freshly read the preserved Iyengar–Takahashi2016 paper at printedpp6–7, §3(3.1), Lemma3.1, and Examples3.2–3.3. The first-power Noether-different factorization is over the fixed Artinian coefficient base, not a deformation of the cover algebra. Root and D corrected the lifting sentence: the second map out of the free module is lifted through the target surjection. All four units passed after that correction.

## Local Eisenstein presentation

Root read B's entire pointed all-ring construction, derivative-weight calculation, Newton iteration, truncated Isom witness, and local branch-list count. Root required the explicit condition that each counted branch fibre contains a nontrivial branch. Arbitrarily many separately marked unramified fibres are not silently included in the count. The corrected file passed. Root freshly read Yasuda2025, §2, equation(4.1), Proposition4.4, Corollary4.6, and Lemma4.7 in full. Contextual Lemma4.9–Corollary4.12 were not fully reread by root and are not claimed as such. C's and D's central source events retain their narrower exact §4 scopes. The separate unpointed refinement subsequently passed all four complete actual-file checks and was promoted. Nilpotent translations are included by an explicit formal-coordinate inversion and Newton argument. The proof still does not claim that every Laurent-series family has this algebraization.

## RDP full sheaves

At11:38–11:40UTC root read the complete C file and independently checked the finite-support Ext spectral sequence, the fundamental-cycle addition algorithm, the inclusion of the maximal ideal in the fundamental-cycle ideal, the multiplicity-two generator estimate, and the final degree inequality. The extension to complete local rings is proved internally using proper duality. Root then freshly read Gustavsen–Ile's author version, §2.1 printedp4 and Proposition2.7 with its entire proof onpp7–8, including both directions. The result passed and was promoted before integration. No compatibility on adjacent core curves follows from this block estimate.

## Original de Jong–Katz note and fixed formal curve fibres

The original author-hosted note was found through de Jong's homepage, which links to https://www.math.columbia.edu/~dejong/papers/curves.dvi . Root downloaded the55,584-byte DVI and converted it with dvipdfmx. The first conversion lacked a font search path; the explicit existing SA12 TEXMF path gave a successful conversion. DVI, PDF and extracted text are preserved under sources/DeJongKatzCurves. Root read all12 pages, not only the abstract or a secondary quotation.

Proposition4.2, pp4–6, is the relevant primary statement: fixed discriminant and formally isomorphic wild ramification give a Hurwitz-number fibre bound for maps to P1 under the note's genus and high-degree hypotheses. Its formal-patching and deformation-complex alternatives leave details to the reader. Sections4.6–4.8 give the finite-field local count and the curve-count bound. Ellenberg–Venkatesh's later chapter §4.1 printedp162 reports the unpublished result but does not supply this proof; moreover its earlier Hurwitz discussion imposes characteristic prime to the group order. It cannot be used for the residual wild nonabelian gate.

Root read B's complete fixed-full-local-data fibre proof. It supplies the nilpotent-level finite-algebra patching, a common global discriminant, and injectivity of geometric generic isomorphism classes by uniqueness of normalization. The statement initially omitted the explicit degree condition when B is empty. Root and D independently identified this and B added degree n; root observed the correction. The resulting bound is(n!)^(2h)n^(2D), with no high-degree or Galois hypothesis. It remains a fibre-cardinality estimate, not an effective presentation of the locus of curve covers extending to a surface.

At11:47–11:49UTC root freshly read the complete used statements and proofs of Stacks0BP2;0BNI, Lemmas15.92.18–19;0BQB;09ZT;0DZQ; and0DZT, Lemmas109.15.1–2. Root also freshly read the primary SGA1 TeX for XIII2.12, complete statement and proof, printedpp392–394. These reads support the corrected B file. The remaining independent audits subsequently passed; the corrected statement was promoted with all four actual-file checks recorded in B's manifest.

## Renewed literature check

Root searched finite generation of punctured-spectrum and proper nonprojective fundamental groups, the citing literature of Suzuki2207.01563, and recent tame fundamental-group results. Suzuki's nilpotent theorem and Achinger–Hübner–Lara–Stix2608.12601 were already incorporated with their exact limitations. The latter's introductory definitions were opened again: they test valuation tameness, including valuations not represented by an original boundary divisor. Its theorem therefore does not identify the larger quotient asked for in D.1 without a separately proved comparison. No new general finite-generation theorem was found in these searches. A repeated search is not movement.

## Canonical energy and fixed-order generator obstruction

Root subsequently read both complete canonical-energy proofs, supplied the missing zero-rounded-cycle case, and checked the effective Schur-complement inequalities. The corrected hypotheses explicitly include a dualizing complex and a projective regular resolution. Root freshly read the complete Stacks0C2M proof. All four actual-file audits passed before promotion; the resulting energy budget is auxiliary and does not provide an object atlas.

Root read the complete elliptic-cone order example, its graded Hom identification, completion, Frobenius periodicity and semisimple lower bound. Root added the sharp upper bound using a basepoint-free pencil, then observed the independent B/C/D checks of that paragraph and the final scope clarification. The exact module-generator number is3r. Root freshly read the full used Stacks0EBJ,03RP,0E39 Lemma53.22.1 and0AYQ degree definition. Root actually reran the438486-assertion finite arithmetic certificate in0.08516565100217122seconds; the author's separately reported runtime is only known to nine decimal places,0.072169335seconds. The certificate checks the Jacobian, index sets, dimensions and congruences; it does not certify the geometric proof. The example refutes arbitrary-anchor uniformity, not the existence of a better anchor or the desired projective count.

## Integrated status at the source freeze

All twelve post-checkpoint15 units across eight proof files have completed the recorded root/B/C/D actual-file audits and are assembled. There are313 statement records,936 central check events and57 requested-outcome rows before the later build/QA bookkeeping. No requested row has changed and no strongest main gate has shrunk after review09. A missing display-math closing delimiter in the first Eisenstein formula caused build97 to stop; root restored the delimiter without changing the mathematics and began the next build. Final image QA is recorded separately only after actual inspection.

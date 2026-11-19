# After-checkpoint 09 addendum: actual CM orbits and the universal normalizer quotient

All three results below are integrated in the live `sections/F_audit.tex`. The included TeX is frozen until checkpoint 08 completes. Parent compilation, combined report, and combined check-event ledger are not edited by this agent.

## F.3.25 — exact rational CM model and genus-three application

For an absolutely simple CM abelian variety over Q with full CM endomorphism field E, the proof constructs the actual semilinear action on the rational Hodge filtration. In normal-closure notation, the equation is `sigma S = S n_sigma`. Its right stabilizer equals H: a larger stabilizer supplies an induced CM type and an explicit F-linear rational Hodge projector. Clearing lattice denominators gives an analytic homomorphism; Chow algebraizes its graph, and the original Milne 1986 Corollary 20.4(b), pp. 146–147, descends it from C to Qbar. Absolute simplicity then excludes it.

The kernel of the actual endomorphism action is the left stabilizer, hence normal. Normality turns it into a subgroup of the right stabilizer. The exact index chain forces E/Q to be Galois and the actual action onto Aut(E), with kernel G_E. The Tate action sends the embedding line indexed by phi to the line indexed by `phi composed with a_sigma inverse`. It supplies the whole actual orbit, and the rational polarization supplies its nondegenerate conjugate pairs.

For a once-punctured genus-three Q-curve with a whole absolutely simple Jacobian, Faltings and F.3.18 turn a candidate degree-one normalizer line into full CM. The rank-one module over E tensor Q_l has an idempotent of rational rank one only at a completely split prime, including the ramified-prime case in this argument. At a split prime, six actual conjugations of one normalizer supply six constraints for one common arithmetic element. The rational inner corrections are written with the full subgroup logarithms. The full diagonal-torus projector is applied afterward to the established linear constraint space; it needs no separate arithmetic lift. F.3.24 and the exact boundary-character transfer give cusp inertia.

Root audited the full proof and application. Generation separately audited the CM/Q lemma. Both requested the explicit descent step, which is included.

## F.3.26 — full-basis tangency in every genus at least three

The balanced degree-six specialness equations have support on at most four handles. The existing one-, two-, and three-handle blocks plus one new block therefore describe the complete space in all genera. The new block has 5040 rows and 960 columns, exact rational rank 958, and two independent integer kernel vectors. A nonzero ordered 958-minor has determinant 1 modulo 101. Both formal-z kernel generators have zero S4 average.

The actual geometric-normalizer equation holds in every genus at least three by the opened Hain scope, strict weight maps, and the actual boundary-fixed action. Enomoto–Satoh's stable trace vanishing is transferred to smaller genera through the explicit surface inclusion into genus nine and a cyclic-tensor projection left inverse.

For a three-handle symplectic span W, the exact cyclic trace projection has outside contribution `cyc(p delta A_i + p delta B_i)`. Each summand is a degree-seven Lie polynomial and vanishes in cyclic coinvariants. The genus-three trace kernel then kills every pair coefficient and forces the sum of the three coefficients on each triple to be zero. Handle permutations kill the triple differences under every invariant functional. The quadruple averages vanish also by a direct independent proof: at a fixed output handle, the S3 average of each degree-three multilinear Lie word cancels by exchanging the arguments of its inner bracket. Extending the actual quotient equivariantly and applying the later torus projector proves its vanishing on all full-basis tangencies.

Root and generation independently audited the complete source maps and proof. The exact certificate is:

- `output/RESEARCH_SA07/code/check_genus_four_tangent_block.py`
- `output/RESEARCH_SA07/code/check_genus_four_tangent_block.output.txt`
- `output/RESEARCH_SA07/code/check_genus_four_tangent_block.witness.json`

Initial actual runtime: 1.314309978 seconds. Root independent rerun: 1.597119087 seconds, exit 0. The canonical 37th computation record was then run through the registry in 1.348439 seconds, exit 0, preserving all 36 prior records. NumPy is explicitly listed as a runtime dependency; the elimination uses exact bounded integer operations modulo 101. The witness SHA256 is `127b51abbbdcbb44bae724088005a55ae58be45b692a260a3ec51333b9e197b9`.

## F.3.27 — all-genus whole absolutely simple Jacobian application

Root and generation freshly read the original Nakamura pages 115–117, including the rank table, Lemma 4.5, Corollary 4.6, and (4.7.1)–(4.7.2). The actual quotient has nonzero dimension-one degree-six part for every hyperbolic (g,n), n at least one, with the required finite-base fibre surjection and multiplier-cubed character. This supplies the exact all-genus source map.

For a once-punctured Q-curve whose whole Jacobian is absolutely simple, F.3.25 supplies all 2g paired actual orbit lines. The same finite intersection of normalizer images and full-log corrections gives all simultaneous constraints on one degree-six arithmetic class. F.3.26 excludes it. The original-curve first Magnus comparison and actual finite-cover boundary kernel then give the full normalizer's cyclotomic character and actual inertia containment. This proves the assertion at every prime, after every finite arithmetic base change, for every genus at least three.

Root read and approved the complete final proof. No new mathematical program was needed for this consequence.

## Exact remaining gate and records

A general rational normal-core detecting cover has its particular, possibly reducible Jacobian. A proper CM quotient supplies only the actual conjugate lines inside that larger homology. The equality relating the universal quotient to restriction onto that proper symplectic summand has not been proved. Mixed Johnson equations and actual punctured target maps remain the next concrete routes. The full LM6 A.22 subgroup assertion remains open.

The 307-assertion inventory still covers all 154 source entries. Dependencies were strengthened only for `I.B05.01`, `I.B05.02`, and `II.MB15.02`; all statuses are unchanged: 195 PROVED, 44 REFUTED, 28 OPEN, 30 READING, 9 DOCUMENTARY-GAP, and 1 NAMED-CONJECTURE-IMPLICATION.

The canonical after09 addendum contains 23 check events and 9 source-check rows, with three new bibliography entries. The Shimura 1998 original-book passage is explicitly an identified but unobtained lead; it is not a proof input. Goodman 2026 Lemma 2.5 is an opened literature comparison under its stated Galois-field premise. No novelty claim is made.

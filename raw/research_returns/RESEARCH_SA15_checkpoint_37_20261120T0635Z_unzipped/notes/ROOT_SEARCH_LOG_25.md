# Root source and approach log, checkpoint 25 interval

All dates below are UTC on 19 November 2026. The original manuscript scans remain unavailable; the supplied AI transcriptions are the manuscript witnesses. No remark from Michel Hua's project was used.

## Primary-source reads for the arbitrary-index inertia proof

At about 20:59--21:00 the root freshly opened The Stacks Project, Theorem 10.160.8, Tag 032A, at https://stacks.math.columbia.edu/tag/032A (retrieval `turn268057077view0`) and read its full coefficient-ring proof, including the mixed-characteristic inductive construction. The coefficient representatives in the new inertia argument are chosen in the base ring, so the wild group fixes them.

The root also freshly opened Tate's original *p-divisible groups* at https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf and read printed pp. 181--182, Theorem 4, Corollaries 1--2, the complete proof and the complete proof of Proposition 12 (`turn268057077view1`, `turn138414309view0`). These are indexed original pages; no page-image inspection is claimed. The theorem is applied to the actual generic descent map and its inverse, preserving the actual Tate lattice.

The retained original Serre (1961) text, *Sur les corps locaux a corps de restes algebriquement clos*, was freshly read on printed pp. 127--128: Section 3.1, the Herbrand functions and Proposition 3. Its original proof is a reference to Herbrand/Artin. The root therefore also read the full proofs in the retained author notes *Corps locaux* by Colmez, pp. 14--16: Proposition 3.7 (norm polynomial), Lemma 3.8, Corollary 3.9, Theorem 3.10 and Proposition 3.13. Upper-numbering quotient compatibility is used only after calculating the actual primitive point fields and cyclotomic quotient; it is never replaced by an equality of lower and upper breaks without proof.

Full root audits and author-preserving exact reruns are recorded in `outputs/root_B67_audit.json` and `outputs/root_B68_audit.json`. The latter identified and repaired two precision defects before promotion: the wild point-field torsor is under the **R-rational**, not L-rational, first-level module; the disjoint eigenvalue orbits in the square-determinant argument are **finite special inertia** orbits, not the isomorphic generic residual modules. The exact previous candidate and diff are retained by the reduction/descent agent. Neither correction changes an inequality or a program.

## Odd theta norms and the degree-seven construction

The root freshly opened Brock and Howe, *Purely inseparable Richelot isogenies*, arXiv:2002.02122v2, 26 March 2025, at https://arxiv.org/pdf/2002.02122. It read Lemma 2.1 and its complete printed proof on pp. 4--8, followed by Lemma 2.3 and Remark 2.4 (`turn268057077view2`, `turn138414309view1`, `turn712711785view0`, `turn712711785view1`). The proof text includes computer-assisted assertions; the root did **not** rerun that paper's Magma supplement and does not claim to have independently verified its automorphism census.

The source's order-four automorphism argument supplies a noncommuting order-four partner: there are twenty elements of order four and twelve elements of order at most two. With the central hyperelliptic involution, this produces a quaternion subgroup. The monodromy agent independently derives explicit universal quaternion identities and a norm-seven interpolation polynomial, with retained exact code and output. This source does **not** prove nodality of an odd theta image. Purely inseparable Richelot isogenies cannot be substituted for the etale isogeny required by the norm-transfer theorem.

The root separately proved a short candidate reduction for any odd finite kernel on a two-rank-zero or two-rank-one genus-two Jacobian: a tangency identifies a hyperelliptic pair and gives a geometric two-torsion image. Odd isogenies identify the geometric two-torsion groups, and every geometric two-torsion point of the source is represented by a Weierstrass point. Thus a tangency forces a third point in that same fibre. The candidate is `notes/root_odd_theta_nodality_reduction_candidate.tex`; it asserts no existence of a suitable isogeny. An initial phrase saying 'immersion at each point' was replaced before audit by the precise statement 'unramified, with injective tangent map at every point'; the initial text is retained as `notes/root_odd_theta_nodality_before_immersion_wording.tex`. A normalization of a nodal image is not claimed to be a global immersion.

## Search for a suitable five-neighbour at each fixed two-rank-one surface

Queries executed in both available search indexes included:

- `"genus 2" isogeny theta nodal image`
- `"abelian surface" "isogeny" "nodes" curve`
- `"5-torsion" "genus 2" characteristic 2`
- `genus two curves abelian surfaces nodal isogeny theta positive characteristic`
- `genus 2 torsion packets arbitrary base point 5 torsion characteristic 2`
- `"On isogenous principally polarized abelian surfaces" arxiv`

Knutsen and Lelli-Chiesa, *Genus two curves on abelian surfaces*, was obtained in the original arXiv v3 of 6 July 2020, https://arxiv.org/pdf/1901.07603 (`turn724174441view0`, `turn171978216view1`). Theorems 1.1--1.4, their stated scope, and the Section 2 reduction were read. The article works with **general complex** polarized abelian surfaces; its nodal existence theorem does not establish the fixed characteristic-two neighbour required here. The root did not use its unverified Section 3 theorem as a characteristic-two result. The initial institutional PDF request failed with 403 (`turn301112655view0`); the subsequent arXiv original succeeded.

Dolgachev and Lehavi, *On isogenous principally polarized abelian surfaces*, was obtained in original arXiv v3, 8 March 2008, https://arxiv.org/pdf/0710.1298 (`turn171978216view0`). The introduction and Theorem 1.1 were read to check applicability. The paper explicitly assumes ground characteristic different from two, so this theorem is not applied to the present gate. The first author-site URL redirected to an inaccessible endpoint (500, `turn301112655view1`); a direct redirected URL returned 404 (`turn724174441view1`); the arXiv original then succeeded.

Boxall--Grant--Leprevost's Weierstrass-relative five-torsion classification remains relevant only to its stated base-point problem. Additional text around Lemmas 3.7--3.8 was inspected, but the combined extraction was truncated and has mathematical OCR defects; **no complete new root proof-read of those lemmas is claimed**, and no new theorem is inferred from it. Bounds on five-torsion relative to a Weierstrass point do not control all translated three-point packets.

Two directions are explicitly kept separate. A suitable incoming isogeny B->A proves a monodromy assertion for the fixed target A. The existence of a good outgoing quotient A->B does not supply that assertion without a further argument. Also, three equivalences 5P~5Q~5R place three sections in a space of dimension four; they do not put the sections in a pencil. The earlier invalid Riemann--Hurwitz shortcut remains withdrawn and is retained in the preceding search log.

No new claim of priority is made. These literature checks have not closed the fixed two-rank-one degree-five gate.

## Late searches and a counterexample to an overstrong shortcut

At21:20--21:27, additional queries were executed:

- `genus two characteristic 2 (5,5) isogenies nodal theta divisor`
- `monodromy p rank curves linear system abelian surface characteristic 2 Hasse Witt divisor`
- `"Cartier" "abelian surface" "linear system" monodromy`
- `"Coble" "Pfaffian" "odd" polarization abelian`
- `"Hasse" "irreducible" "linear system" abelian surface`
- `"Cartier operator" "linear systems" "abelian"`
- `"p-rank" "linear system" "abelian surface"`
- `"unit-root" "monodromy" "hypersurfaces"`
- `"genus 2" "torsion packets" "5"`
- `"genus two" "torsion packets" "characteristic"`
- `"five" "torsion" "p-rank" genus two`

One initial three-query dispatch was aborted before execution and was then reissued successfully. The result sets were `turn527454258`, `turn979274304`, `turn343923782`, and `turn358639204`. They returned the previously inspected genus-two isogeny papers, general moduli monodromy, Coble cubic/quadric literature, and characteristic-zero torsion-packet papers. No additional theorem applicable to every fixed characteristic-two target was obtained or used. Search snippets are not recorded as full proof reads. In particular no conclusion is imported from a characteristic-zero torsion-packet theorem, and no arbitrary-polarization irreducibility statement is attributed to the degree-three Coble construction.

The odd-plus-even boundary shortcut was also reconsidered. Its exact previously identified obstruction is now written in `agents/monodromy/post_CP24_odd_even_boundary_obstruction.tex`: the boundary loses4-2f stable directions, and the currently forced blocks and heart span onlyR-6. A proper parabolic with an irreducible six-dimensional quotient has no invariant vector or covector and contains these forced subgroups. Thus those group inputs alone cannot prove the desired full odd image. This is a limitation of the approach, not a counterexample to the geometric assertion.

The root then performed a bounded, exact Cantor-arithmetic search on all rational points of24 specified two-rank-one curve/field pairs overF4,F16,F64,F256. The retained program `code/root_f1_five_packets.py` and its JSON/stdout/stderr completed successfully21:27:11.708746UTC in1.321733534001396 seconds. It checks finite-field inverses, every reduced divisor equation, inverses, repeated-multiple agreement and sampled associativity. Absence of packets in any finite row is not treated as geometric absence.

The search found an explicit bad five-kernel already on C:y²+xy=x5+x3+x overF4. WithQ=(0,0),P=(1,omega),omega²+omega+1=0, the changez=1/x,v=y/x³ gives the exact functionf=v+omega*z²+z+1 with norm(z+1)^5 and divisor5P-5Q. The hyperelliptic partnerPprime gives[Pprime-Q]=-[P-Q]. Every maximal isotropic five-plane through this nonzero order-five class therefore identifiesQ,P,Pprime; there are six such planes. The candidate `notes/root_f1_bad_five_kernel_candidate.tex` proves smoothness, genus, Cartier stable rankone, the complete divisor identity and the six-plane count. This refutes only the overstrong shortcut that every five-quotient is nodal; it does not refute existence of a good incoming neighbour and does not by itself count as main-gate movement.

A separate root norm-function certificate passed21:29:36.695811UTC in0.00020161300199106336 seconds (`code/root_f1_five_packet_function_certificate.py` with JSON/stdout/stderr). The monodromy agent independently derived the identity in0.001622812997084111 seconds, audited the communicated complete proof21:29:25.145155, then read the complete formal candidate and confirmed its exact SHA21:29:59.784836. Its audit and code/output are retained. The paper was already frozen for checkpoint25, so this candidate is included as a separately identified late research file, without silently changing the audited PDF or its numbered-statement table.

The root freshly reread the retained Boxall--Grant--Leprevost original text, printedpp30--31, Proposition1.1, Example1.2(i)--(ii), and the genus-two model conventions. The norm criterion is compatible with the explicit function above; Example1.2(ii)'s no-five-torsion observation concerns its stated one-Weierstrass-point family and is not applied to all two-rank-one curves. The specific counterexample is proved directly, without a claim of novelty or a claim that the source contains this exact equation.

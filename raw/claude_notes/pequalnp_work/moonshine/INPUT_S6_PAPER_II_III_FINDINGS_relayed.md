# Input for the lambency-6 / 3-2 pass: S6 Papers II and III, findings as relayed (23 Nov 2026 ~20:5x UTC)

Relayed by the user from the S6 intake session's report (which itself relays part of it from the S6 run's records;
"checked" below means checked by that intake, "relayed" means taken from the run's records). Statement tags are the S6
series' own.

- **P4R.13 (tag 02Y6), Paper II, "Elliptic components of the conductor"** said: when a singular fibre support has an
  elliptic conductor component, its image is a single smooth elliptic curve. The run built a compact example with THREE
  DOUBLE FIBRES whose support has TWO DISJOINT ELLIPTIC IMAGE CURVES, each the image of its own section under an
  unramified double cover, under the paper's standing hypotheses (a smooth compact threefold with b1 = b2 = 0, fibred by
  two-tori). Corrected statement: "one or two"; its proof lists three configurations (the original missed the third:
  two sections with different images). Relayed.
- **P4.40 (02XE)** falls with it: the same example has ordinary double curves on a support of Euler number 0, so the
  exclusion needs e(S) > 0. The faulty step assumed a section of multiplicity two before ruling out the reduced case.
- **E.2.15 (Paper II)**: stated for threefolds without smoothness; a projective cone over a pencil with K_X = f*O(-1)
  breaks it (A = 1, D = -1: the claimed D < -A fails); smoothness is now a hypothesis. Relayed.
- **02L5 (Paper III)**: the last step relied on program-saved "executed examples"; replaced by explicit holomorphic
  gluings. The run's first check glued in the wrong direction (groups of orders 1 and 13 instead of 1 and 11). Checked.
- **02K2 (Paper III)**: multiplication by N was treated as a map of degree N^2, but its kernel has order N^6. Checked.
- **02K4**: two lattice intersections claimed equal are related by an involution. Checked.
- **02KE**: the proof used H^4(X_p; Z) = Z/d without proof; the new proof does not need it. Checked.
- Paper II: 252 changes of type D25 (incorrect proof step) over 127 statements; examples: any quadratic lift works,
  refuted by f = y^2 + x^3; "integral, effective and numerically trivial implies nonempty elliptic roots", refuted by
  D = 0 on a Hopf surface; cap formulas off by a factor of |c|; "nh log s holomorphic at s = 0" (UN63, repair checked).

The user's ansatz (23 Nov): the 3-2 shape here (two elliptic curves over three double fibres; double covers; orders 11
and 13; kernel N^6 vs degree N^2) is the same 3-2 pattern as in "GL32" in the GRH work and as lambency 6 = 2 x 3 in the
moonshine: "on its face it's numerology ... but the numerology keeps lining up here, so we should check real seriously."

**Clarification (the user, 23 Nov ~20:5x UTC):** [the user's words, omitted] meant PG(2,3) (the projective plane of order 3): "I literally
meant PG 2.3". So the 3-2 objects to line up include PG(2,3) (13 points, 13 lines, 4 per line; Singer form {0,1,3,9}
mod 13; the plane of L-meta-650; full collineation group PGL(3,3) of order 5616, the Singer normalizer of order 39 and,
with the polarity, 78), AG(2,3) (the tetracode configuration, 9 points, 12 lines in 4 parallel classes), the Pappus
configuration (AG(2,3) minus one parallel class: 9 points, 9 lines, 27 incidences; Codex), lambency 6 (umbral moonshine,
Niemeier root system A5^4 D4), the (2,3,6) triangle group and Z[omega], Codex's j = 2304 point with its three quadratic
signs, the S6 example above (two elliptic curves, three double fibres, double covers; the orders 11 and 13 in 02L5), and
the 2-versus-3 thresholds on the fleet's side (two stacks versus three for the alternation speedup, Theorem B; two
alternations versus three for FP3; 2-SAT versus 3-SAT).

**Further ansatz (the user, same minute):** [the user's words, omitted] So also line up: GRH for GL(2) and GL(3) automorphic L-functions (Alpöge's theorem covers GL(1),
all Dirichlet characters), the symmetric-square lift GL(2) -> GL(3) (Gelbart-Jacquet), Rankin-Selberg GL(2) x GL(3), the
user's split-zero programme (a phase mechanism of order 3: cubic characters of Q(omega) as the first case beyond
Alpöge's theorem; the ladder of SU(n) centres mu_n; a paramodular rung GSp4).

**Concrete checks proposed by Claude (from memory, to be verified against the sources, not asserted):** (i) the
automorphism group of the ternary tetracode has order 48 and is GL(2,3) (a double cover 2.S4); (ii) the linear part of
the collineation group AGL(2,3) of AG(2,3) is GL(2,3) (order 432 = 9 x 48); (iii) in umbral moonshine (Cheng-Duncan-
Harvey), the umbral group at lambency 6 (Niemeier root system A5^4 D4) is listed as 2.S4: is it GL(2,3)? If (i)-(iii)
hold, "GL(2,3), lambency 6, the tetracode, AG(2,3) inside PG(2,3)" is one group acting on one structure. (iv) PG(2,3)
has 13 points and 13 lines; the S6 repair 02L5 has groups of orders 1 and 13 (wrong gluing) versus 1 and 11 (right):
test whether 13 and 11 there come from a plane or a tetracode structure. (v) PGL(3,3) has order 5616 = 2^4 3^3 13.

**The user's GL(2)/GL(3) ansatz, made precise (the user, ~20:5x UTC):** [the user's words, omitted] In standard terms:
the Rankin-Selberg L-function L(s, pi_2 x pi_3) of cuspidal representations of GL(2) and GL(3) has degree 6, and Kim and
Shahidi proved the functorial product GL(2) x GL(3) -> GL(6) (Ann. of Math. 155 (2002); with it the symmetric cube
GL(2) -> GL(4)); the symmetric square GL(2) -> GL(3) is Gelbart-Jacquet. Ansatz to check seriously: where does this
degree-6 product meet lambency 6 (umbral moonshine, A5^4 D4), the 3-2 structures above (PG(2,3), AG(2,3), the tetracode,
GL(2,3)), and the (2,3,6) triangle group; and what GRH for the GL(6) product would give in any of them.

**The sign ansatz (the user, ~21:0x UTC):** [the user's words, omitted] Concrete places where a sign (an involution, a quadratic character, a root number) sits next to
the 2 and the 3, to line up and check as one object:
- umbral moonshine writes lambency 6 for A5^4 D4 as "6+3": the "+3" is an Atkin-Lehner involution (a sign) on the 6;
- PG(2,3): the symmetry group of order 78 of the Singer form is the Singer normalizer of order 39 extended by the
  polarity (the point-line swap, an involution);
- the S6 example: each elliptic curve is the image of a section under an unramified double cover (a deck involution),
  with three double fibres;
- GRH: the GL(1) layer as quadratic characters twisting GL(2) x GL(3) (L(s, chi x pi_2 x pi_3), degree 6), and the root
  number (the sign of the functional equation) of the degree-6 product; Alpöge's purity by signs (the sign-only route of
  his footnote 3; our H01) as the GL(1) mechanism;
- Codex's j = 2304 family: three quadratic signs entering the four points Q with 2Q = (0, -1).
Question to check, not to presuppose: is it the same sign (one involution or character) across these, and how does it
change the 2 x 3 (or 1 x 2 x 3) count in each?

**How to check (the user, ~21:0x UTC):** not by looking up or remembering whether a relation is known: [the user's words, omitted]. For each ansatz: assume the relation; derive its
consequences (numbers, group orders, characters, counts, functional equations); try to reach a contradiction; if none,
test the consequences against everything else we know; report the surprisingly consistent ones first. The user adds:
assume the sign ansatz touches lambency (the "+3" of lambency 6+3).

**Correction (the user, ~21:1x UTC):** [the user's words, omitted]; [the user's words, omitted]; [the user's words, omitted]; [the user's words, omitted]. So THE SIGN FIELD IS THE OBJECT NAMED IN ALPÖGE'S
PROOF: read its definition there and use it exactly (Alpöge, "Remark", https://alpo.ge/remark.pdf, 4 pp., 20 Nov 2026;
find the local copy with claude_tools/find_paper.py; the Lean archive is in
Papors/Chatnotes/Zeta-Function-Foundation/literature/alpoge_rh_20261120 (modules GlobalSignature, SignDefiniteness,
PositiveSignKForm among others; lean_tar_listing.txt lists them); the main session's reading of the remark: task_notes/
catchup_20261123_329fb1e6.md around line 236, and the bridges in reports_20261120/alpoge_rh/). The list of sign-like
places above (the "+3" of lambency 6+3, the polarity of PG(2,3), the deck involutions of the S6 example, root numbers,
Codex's three quadratic signs) is only where Alpöge's sign field is to be tested, not a reinterpretation of it.
Note from the record: step 3 of Alpöge's note runs through C/Z[omega], the hexagonal lattice and the (2,3,6) triangle
group (1/2 + 1/3 + 1/6 = 1): a 2-3-6 structure inside the GRH proof itself.

**A test result, relayed by the user (~21:2x UTC, from another session's check):** [the user's words, omitted] (Classical identity behind
the level-2 match: the six points of a genus-2 picture and the 2-torsion of the Jacobian carry one S6 action through
S6 = Sp(4, F2); the symmetry stops at level 4.)

**The user's reframing (same time):** [the user's words, omitted]
So the task of the pass: for each appearance, state the identity behind it (exceptional isomorphisms such as
S6 = Sp(4,2), S4 = PGL(2,3), GL(2,3) a double cover of S4, PSL(2,7) = GL(3,2); the tetracode = AG(2,3) inside PG(2,3);
the A5^4 D4 glue and the umbral group at lambency 6+3; the hexagonal lattice and the (2,3,6) triangle group in Alpöge's
step 3; 2 x 2 = 3 + 1 and 2 x 3 = 4 + 2 in GL(2) x GL(3) -> GL(6) with the central-character twist; the level-2 match
and level-4 break above), then carry each identity into the other places and derive what it implies there; report the
implications that are new or interesting first.

**Codex's report (relayed by the user ~22:3x UTC; Codex = GPT-6.2 Astra at reasoning effort ultra; proofs in the public
mirror, structural_lemmas/conductor_symmetries.md and shadow_point_counts.md at commit a6bf6ce):**
- The S6 Paper II construction is printed as Example P205 (two distinct elliptic conductor images in each of three
  exceptional fibres); the two images within one fibre are isomorphic. Across fibres, for one admissible normalization the
  elliptic periods at infinity, 0, 1 are 2i, i eps^2/2, i eps; rectangular curves with periods iu, iv are isogenous iff
  u/v or uv is rational; so the pairs (infinity, 0), (infinity, 1), (0, 1) are isogenous exactly when eps^2, eps, eps^3
  is rational, and all these examples have the same integral monodromy. NOTE: the exponents are 1, 2, 3 (eps for
  (infinity, 1), eps^2 for (infinity, 0), eps^3 for (0, 1)): the user's [the user's words, omitted] as three isogeny conditions.
- For every admissible frame the conductor sections over infinity tend to the square curve j = 1728 (CM by Z[i], the
  mu4 / square lattice / (2,4,4) of the layer-4 metaplectic candidate), and their degree-two images to j = 287496 =
  j(2i) (CM by Z[2i]).
- The seven-point/seven-line (Fano, GL(3,2)) theorem from the GRH work restricts to exactly the two six-element actions of
  the example: permutable on 2-torsion, distinguished on 4-torsion.
- Lambency 6: two leading coefficients of a twined shadow recover the number of rational 3-torsion points of an elliptic
  curve and of its quadratic twist (the sign as the twist); on the auxiliary family the first coefficient determines a
  K3 point count mod 3 (checked on 252 finite-field fibres). Codex: the connection to the P vs NP work is through the
  explicit Fano actions and their circuit examples.

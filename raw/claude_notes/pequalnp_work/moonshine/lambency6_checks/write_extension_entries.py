"""Writes the extension entries X-gen-010 .. X-gen-022 of the lambency-6 pass into pequalnp_work/mirror/extension/entries.
Run: python -I -B write_extension_entries.py"""
import pathlib
D = pathlib.Path(__file__).resolve().parents[2] / "mirror" / "extension" / "entries"
assert D.is_dir(), D
BY = "Claude Opus 5.5 at effort max, 24 Nov 2026"
SRC_PASS = "computations of the lambency-6 pass (24 Nov 2026), kept with the project's moonshine notes"
CDH = "Cheng-Duncan-Harvey, Umbral moonshine and the Niemeier lattices (arXiv:1307.5793), section 5.1 and the tables of umbral groups"
E = {}
E["X-gen-010"] = dict(
    title="The lambency-6 twined shadow is the symmetric-power tower of the faithful two-dimensional representation of the umbral group GL2(F3)",
    attaches_to="none (moonshine side; no fleet node)", uses="", kind="identity",
    status="second-read (exhaustive computation over the 48 elements of GL2(F3))",
    sources=f"{CDH}; the tetracode marking of the twined shadow in the public structural-lemma note on shadow point counts; {SRC_PASS}",
    statement="""For X = A5^4 D4 with umbral group G = GL2(F3), let V be the faithful two-dimensional complex representation of G
(character field Q(sqrt(-2)), det V = the sign character). Write the twined shadow of g in G as the matrix
diag(a+1, b, a+c, b, a+1) on the unary theta functions S_{6,1}, ..., S_{6,5}, plus s in the (1,5) and (5,1) entries
(a = fixed lines of F3^2, b = their signed count, c = fixed pair partitions minus one, s = sign of the induced permutation
of the pair partitions). Then, as class functions on G: s = det V, a - 1 = Sym^2 V, b = Sym^3 V, a + c = 1 + Sym^4 V.
So component r carries Sym^{r+1} V for r = 1, 2, 3 (mirrored under r -> 6 - r), the W_3 cross term carries det V, and the
centre -I acts on component r by (-1)^{r+1}, the parity of Sym^{r+1} V. Moreover V (x) Sym^2 V = Sym^3 V (+) V (x) det,
with V (x) det the complex conjugate of V (the degree-six decomposition 2 x 3 = 4 + 2 with the '+2' twisted by the sign),
and det (x) V (x) Sym^2 V = Sym^3 V (+) V.""",
    where="""Not a fleet node: it organizes the umbral side of the moonshine atlas (the lambency-6 shadow) by the symmetric powers
of one representation, so that GL(1), GL(3), GL(4), GL(5) questions about it become questions about one Galois
representation (see X-gen-011).""",
    argument="""The eight class functions 1, s, c, a - 1, (a - 1)s, chi_V, conj(chi_V), b are orthonormal, so they are the
irreducible characters of G; Sym^k chi_V is computed from the eigenvalues of V. The identities are equalities of class
functions checked on all 48 elements; Sym^0..Sym^3 of V are the irreducibles 1, V, 3, 4 and Sym^4 V = 2 + 3 (the 2 of the
S3 quotient). The Clebsch-Gordan identity is V (x) Sym^2 V = Sym^3 V (+) V (x) det for any two-dimensional V; V (x) det is
the conjugate of V because V is two-dimensional with det of order two.""",
    missing="""Whether the mock modular forms H^X_g themselves (not only their shadows) decompose by Sym^k V with nonnegative
multiplicities; and the analogue at the other lambencies whose umbral group lies in GL2(C).""")
E["X-gen-011"] = dict(
    title="At Frobenius the lambency-6 shadow coefficients are the traces of det, Sym^2, Sym^3, Sym^4 of the Langlands-Tunnell weight-one form of E[3]",
    attaches_to="none (GRH side of the moonshine atlas; no fleet node)", uses="X-gen-010", kind="bridge",
    status="second-read (identity on GL2(F3) by computation; checked on y^2 = x^3 - 3x + 1 at all 428 primes 5 <= p < 3000; the automorphy is cited)",
    sources=f"Langlands-Tunnell theorem (octahedral case); the public structural-lemma notes on shadow point counts and on the j = 2304 curve; {SRC_PASS}",
    statement="""Let E/Q have mod-3 Galois representation onto GL2(F3) and let f be the weight-one newform with Galois
representation V(rho_{E,3}) (odd, det = chi_{-3}, projective image S4). At a prime p > 3 of good reduction, with t = a_p(f):
the twined-shadow coefficients at Frob_p are s = chi_{-3}(p), U - 2 = t^2 - chi_{-3}(p) = a_p(Sym^2 f),
V = t^3 - 2 chi_{-3}(p) t = a_p(Sym^3 f), (r = 3 coefficient) - 1 = a_p(Sym^4 f), and c(p) = (number of cube roots of the
discriminant of E in F_p) - 1, the trace of the dihedral representation of Q(zeta_3, Disc^{1/3}). Hence #E(F_p)[3] = U + V
and, for a quadratic twist by a nonsquare, U - V; L(f x Sym^2 f) = L(Sym^3 f) L(f (x) chi_{-3}) is a degree-six Artin
L-function read off the shadow components r = 1, 2.""",
    where="""The GRH ladder of the moonshine atlas: GL1 over Q (chi_{-3}, covered by the GRH for Dirichlet L-functions), the cubic
Kummer character of Q(omega) (c), then the octahedral Artin L-functions Sym^2, Sym^3, Sym^4 of a weight-one form (beyond it).""",
    argument="""By X-gen-010 the shadow coefficients are Sym^k chi_V at the Frobenius class; det of the mod-3 representation is the
cyclotomic character mod 3, so det V(Frob_p) = chi_{-3}(p). The S3 quotient of GL2(F3) cuts out Q(zeta_3, Disc^{1/3}) for
this curve (checked prime by prime against the cube roots of 6^4). Automorphy of V(rho) is the Langlands-Tunnell theorem;
Sym^2, Sym^3, Sym^4 of a weight-one form are Artin L-functions of the same field.""",
    missing="""A proof that the S3 layer is Q(zeta_3, Disc^{1/3}) for every such E (checked for one curve here); the use of GRH for
these Artin L-functions (effective Chebotarev in Q(E[3])) as an input anywhere in the programme.""")
E["X-gen-012"] = dict(
    title="The sign of the quadratic Gauss-sum mechanism lives on the chi_{-4} bits, and the order-2 x order-3 Gauss-sum defect is the Frobenius of eta(6t)^4",
    attaches_to="none (GRH side of the moonshine atlas)", uses="", kind="identity",
    status="second-read (computation: 161 moduli, 1029 pairs, 553 products, 37 primes)",
    sources=f"Alpoge, Remark (alpo.ge/remark.pdf, Nov 2026), footnote 3 and step 3; {SRC_PASS}",
    statement="""For odd squarefree c > 0 let eps_c = g(c)/sqrt(c) (Gauss sum of the Jacobi symbol mod c). Then eps_c^2 = chi_{-4}(c),
and eps_{cc'} = eps_c eps_{c'} (-1)^{x x'} with x = (1 - chi_{-4}(c))/2 in F2; for k pairwise coprime factors the defect is
(-1)^{e_2(x_1, ..., x_k)}, the complete-graph quadratic form over F2, which depends only on the number of factors that are
3 mod 4. The theta Gauss sum of lambency 6, sum_{r mod 12} e(r^2/24) = sqrt(12) e(1/8), is (2 e(3/8)) times (-i sqrt 3), its
2-part times its 3-part. For p = 1 mod 6, g(chi_2) g(chi_3) = J(chi_2, chi_3) g(chi_2 chi_3) and
a_p(y^2 = x^3 + 1) = -2 Re J(chi_2, chi_3): the defect between the order-2 and order-3 Gauss sums is the Frobenius of the
curve 36a1, whose newform eta(6t)^4 is the Mason form of the A5 Coxeter element on N(A5^4 D4).""",
    where="""Ties the sign mechanism of the Dirichlet-GRH proof (normalized Gauss sums on the double cover) to the characters of the
lambency-6 shadow (chi_{-4}) and to the first Hecke rung beyond it (the CM character of 36a1 over Q(omega)).""",
    argument="""Gauss's evaluation eps_c in {1, i} and g(cc') = (c/c')(c'/c) g(c) g(c') with quadratic reciprocity give the cocycle;
the k-fold formula follows by induction. The theta Gauss sum factors by the Chinese remainder theorem (1/24 = 3/8 - 1/3).
The Jacobi-sum identity is g(chi)g(psi) = J(chi, psi) g(chi psi), and counting y^2 = x^3 + 1 by characters gives
N = p + J + conj(J). All checked numerically.""",
    missing="""The order-6 (Q(omega)) version of the cocycle and its relation to the sixfold cover of the remark's step 3.""")
E["X-gen-013"] = dict(
    title="PG(2,3) with its polarity is P(sl2(F3)) with the determinant form; its conic is P^1(F3); the (2,3,6) triangle group maps onto the Singer normalizer with polarity for q = 2, 3",
    attaches_to="L-meta-650, L-meta-972, L-meta-956, L-meta-957", uses="", kind="identity",
    status="second-read (computation)", sources=f"{SRC_PASS}",
    statement="""(1) The absolute points of the polarity x -> -x of the Singer plane {0,1,3,9} mod 13 are {0,7,8,11}, a conic (no three
collinear); for q = 2, 4 they form a line. (2) On P(sl2(F3)) the adjoint action of GL2(F3) has kernel {+-I} and image
PGO3(3) (order 24), preserves the conic det = 0, and X -> ker X is a GL2(F3)-equivariant bijection from the conic onto
P^1(F3); so the conic is the set of four tetracode coordinates (the four A5 summands of N(A5^4 D4)) and the polarity's
centralizer S4 permutes it with character 1 + Sym^2 V. (3) The ring map Z[omega] -> Z/(q^2+q+1), omega -> q, maps the
triangle group Z[omega] x| mu6 onto the group of all affine maps x -> u x + t that preserve the Singer plane PG(2,q) as
collineations (u a power of q) or correlations (u = -q^k): of order 42 for q = 2 and 78 for q = 3; for q = 4 the image has
index 2 in the group of order 252 (the semilinear multiplier 2).""",
    where="""Symmetry for the PG(2,3) circuit searches: the order-78 group acts on the point-line incidence function of 650/972 (the
polarity swaps the point inputs and the line inputs); the order-39 part acts on the line-OR systems of 956/957.""",
    argument="""Direct computation on the 13 points and lines. q^3 = 1 mod q^2+q+1, so a + b omega -> a + b q is a ring map with kernel
(q - omega); mu6 maps to {+-1, +-q, +-q^2}; q is a multiplier of the Singer set (Singer) and -1 the standard polarity.
Every polarity of PG(2,3) is orthogonal and conjugate to the determinant form's, since 3 is not a square.""",
    missing="""Use of the order-78 group (with the point-line swap) for symmetry breaking in the 650 and 972 searches.""")
E["X-gen-014"] = dict(
    title="The umbral groups at Coxeter number 6 from the glue codes: GL2(F3) for A5^4 D4 (and E6^4), 3.S6 for D4^6 with a normal non-central mu3",
    attaches_to="L-meta-1303, L-meta-907, L-meta-911, L-meta-458", uses="", kind="identity",
    status="second-read (computation of the stabilizers of the glue codes)", sources=f"{CDH}; {SRC_PASS}",
    statement="""The glue code of N(A5^4 D4) (order 72: the tetracode in the 3-parts of the A5 classes and a binary part) has stabilizer
in Out(A5^4 D4) = ({+-1}^4 x| S4) x S3 (order 2304) of order 48 with 13 involutions, 12 elements of order 8 and derived
subgroup of order 24: GL2(F3). Its centre is the diagram flip of all four A5 (-1 on the tetracode, trivial on the binary
glue). The same holds for E6^4 (glue = tetracode). The hexacode's stabilizer in S3 wr S6 (the glue of D4^6) has order 2160,
maps onto S6 with kernel the scalars of F4 (simultaneous triality), has derived subgroup 3.A6 (order 1080) containing that
kernel, and its odd elements invert the kernel: it is 3.S6 with trivial centre.""",
    where="""Symmetry of the ternary incidence instances (AG(2,3) = the tetracode plane): GL2(F3) and its Borel subgroup act on the
Pappus and affine-plane instances of 1303, 907, 911, 458.""",
    argument="""Exhaustive computation: glue codes built from generators, checked isotropic with all nonzero glue words of norm at least
4 (so the root systems are exactly A5^4 D4, E6^4, D4^6); stabilizers enumerated; group structure from element orders,
centre and derived subgroup.""",
    missing="""Nothing for the identification; the statement corrects the description of the lambency-(6+3) group's mu3 as central.""")
E["X-gen-015"] = dict(
    title="The six ramification points of the S6 Paper II example P205 are the Weierstrass points of the Bolza curve, whose automorphism group is GL2(F3); P205's own level-4 lift differs",
    attaches_to="none (moonshine side)", uses="X-gen-014", kind="identity", status="second-read (computation)",
    sources=f"S6 series Paper II, Example P205, as presented in the public structural-lemma note on conductor symmetries (monodromy matrices and the base cover); {SRC_PASS}",
    statement="""The ramification points {0, oo, 1, -1, i, -i} of the base cover t = (z + 1/z)^2/4 of P205 are the octahedron's vertices
and the Weierstrass points of w^2 = z^5 - z (the Bolza curve). Its automorphism group has order 48 with 13 involutions and
12 elements of order 8: GL2(F3), the umbral group of lambency 6. Each deck involution z -> -z, -1/z, 1/z lifts to two
elements of order 4 whose square is the hyperelliptic involution, so the deck group lifts to Q8. P205's own monodromy
modulo 4 is a group of order 16 isomorphic to C4 x| C4 (square multiplicities 4, 4, 8): two of the three meridians have the
same divided square and the third a different one, where Q8 would have one common square. PSL2(Z/4) = S4 = PGL2(F3), but
SL2(Z/4) has 7 involutions and a normal (Z/2)^3, unlike GL2(F3).""",
    where="""Locates the level-2 match and the level-4 break of the S6 example inside the lambency-6 group: the level-2 data agree with
the octahedral S4 = PGL2(F3); at level 4 the example's squares are not those of Q8.""",
    argument="""Moebius stabilizer of the six points computed (24 maps), lifted to the curve through the sextic form; orders counted.
The mod-4 group generated by the integral meridians and its squares enumerated.""",
    missing="""Whether any natural genus-two curve in the construction carries this structure (P205's fibres are complex 2-tori; see
X-gen-016).""")
E["X-gen-016"] = dict(
    title="Refuted: the level-2 symmetry of P205 is the Sp4(F2) = S6 of a principally polarized genus-two structure",
    attaches_to="none (moonshine side)", uses="X-gen-015", kind="counterexample", status="refuted",
    sources=f"S6 series Paper II, Example P205 (integral monodromy as in the public structural-lemma note on conductor symmetries); {SRC_PASS}",
    statement="""The three integral meridians A1, A2, A3 of P205 (A1 A2 A3 = I) preserve no nonzero alternating form over Q, and none of
the eight alternating forms over F2 that they preserve is nondegenerate; their invariant symmetric forms are spanned by
x1^2 and alpha^2 (alpha the invariant covector), hence degenerate. So the level-2 action lies in GL4(F2) (with the Fano
plane of the invariant hyperplane), not in a symplectic Sp4(F2). Its F2[D]-module is also not the 2-torsion of the Bolza
Jacobian: the fixed-space dimensions of the three involutions are 3, 3, 3 against 2, 2, 2.""",
    where="""Removes the genus-two Sp4(F2) = S6 explanation of the six-point match of the S6 example; the match of the six-element
permutation actions stands.""",
    argument="""Solve A_i^T W A_i = W for alternating W over Q (only W = 0) and enumerate the 64 alternating forms over F2. A map
I + e4 phi with phi(e4) = 0 preserves a symplectic form omega only if phi = omega(e4, .); the three meridians have three
different phi, so at most one of them could be symplectic.""",
    missing="""Nothing; the six-point match is a statement about permutation actions only.""")
E["X-gen-017"] = dict(
    title="The isogeny exponents 1, 2, 3 of the exact P205 family are Kummer degrees of the deformation parameter",
    attaches_to="none (moonshine side)", uses="", kind="identity",
    status="paper-proof (criterion re-derived; patterns checked by computation)",
    sources=f"the exact normalized family of the public structural-lemma note on conductor symmetries (periods 2i, i eps^2/2, i eps); {SRC_PASS}",
    statement="""For the exact family with conductor-image periods 2i, i eps^2/2, i eps over oo, 0, 1, let d be the least k >= 1 with eps^k
rational (d = oo if none). The images over (oo,1), (oo,0), (0,1) are isogenous exactly as follows: d = 1: all three pairs;
d = 2: only (oo,0); d = 3: only (0,1); otherwise none. For eps^6 = r rational, (0,1) is decided by the square class of r,
(oo,0) by its cube class, (oo,1) by both (Q^x/Q^x6 = Q^x/Q^x2 x Q^x/Q^x3); transitivity is eps = eps^3/eps^2. The images are
CM exactly when the squares of their periods' imaginary parts are rational; for d = 2 all three are CM, the one over 1 by
Q(sqrt(-r)).""",
    where="""Explains the 1, 2, 3 of the isogeny table as the sign (square class) and phase (cube class) of one Kummer datum.""",
    argument="""Rectangular periods iu, iv are isogenous iff u/v or uv is rational: a rational matrix with iv (c iu + d) = a iu + b forces
b = -c uv and dv = au. The three periods carry eps-weights 0, 2, 1, so the pair conditions are eps^{|e_a - e_b|} or
eps^{e_a + e_b} rational.""",
    missing="""Whether the weights (0, 2, 1) of the deformation frame are forced by the construction or a choice.""")
E["X-gen-018"] = dict(
    title="Refuted: the isogeny exponents of P205 are the orders of elliptic points and the cusp",
    attaches_to="none (moonshine side)", uses="X-gen-017", kind="counterexample", status="refuted",
    sources=f"P205's integral monodromy (public structural-lemma note on conductor symmetries); {SRC_PASS}",
    statement="""All three local monodromies of P205 have characteristic polynomial (x - 1)^2 (x + 1)^2 with nontrivial unipotent square:
three double fibres, a (2,2,2) base orbifold. No fibre carries a local monodromy of order 3 or 6, so the exponents cannot be
read as elliptic orders (an order-3 point would need such an eigenvalue); and the integral monodromy is the same for every
eps, so no topological datum carries the exponents.""",
    where="""Closes one reading of the 1 x 2 x 3 pattern in the S6 example.""",
    argument="""Characteristic polynomials and squares of the integral meridians computed.""",
    missing="""Nothing.""")
E["X-gen-019"] = dict(
    title="The orders 11 and 13 of the S6 Paper III repair 02L5 against the ternary Golay code and PG(2,3): residue -1 mod 12 both ways; no lasting alignment",
    attaches_to="none (moonshine side)", uses="", kind="counterexample",
    status="refuted (the structural pairing); the residue statement holds",
    sources=f"S6 series Paper III, statement D.2.3 (02L5) and its checked repair; {SRC_PASS}",
    statement="""The peripheral integers of the right and wrong cusp gluings are 12 l0 - 1 and -12 l0 - 1 (with l1 = 1, l2 = -1 in
12 l0 - 4 l1 - 3 l2): both are -1 mod 12 for every l0, and the gluing direction changes |lambda| from 12 l0 - 1 to 12 l0 + 1,
which fixes chi_12 and flips chi_{-4}, chi_{-3}. At l0 = 1 the orders 11 and 13 are the lengths of the ternary Golay and
ternary Hamming codes (the latter with check columns the 13 points of PG(2,3)). The pairing does not persist: 12 l0 + 1 is a
plane size q^2+q+1 only at l0 = 1, 6, 11, and 12 l0 - 1 a perfect-code length only at l0 = 1, 2. The PG(2,3) line code over F3
is the cyclic [13,7,4] code with zero set {1,3,9} u {7,8,11}; it is not a quadratic-residue code (both ternary QR codes of
length 13 are [13,7,5]).""",
    where="""Settles the 11/13 lead of the 3-2 comparison as arithmetic (residues mod 12) plus a coincidence at l0 = 1.""",
    argument="""Tabulation of 12 l0 -+ 1 for l0 <= 12; zeros of 1 + x + x^3 + x^9 in F27; weight distributions of the three cyclic codes.""",
    missing="""What the groups Z/|12 l0 - 1| of 02L5 are (H1-torsion with a linking form?), which would decide whether chi_12 has a
geometric meaning there.""")
E["X-gen-020"] = dict(
    title="At the lambency-6 CM point the GL2 x GL3 product splits into GL1 over Q(omega); across the two elliptic points the twist is the other point's sign",
    attaches_to="none (GRH side of the moonshine atlas)", uses="X-gen-012", kind="identity",
    status="second-read (Euler factors at 194 primes 5 <= p <= 1200; the standard CM decomposition)", sources=f"{SRC_PASS}",
    statement="""For f = eta(6t)^4 (36a1, CM by Q(omega)): Sym^2 f = eta(2t)^3 eta(6t)^3 (+) chi_{-3}|.| and Sym^3 f = eta(3t)^8 (+) f(1), so
L(f x Sym^2 f) = L(eta(3t)^8) L(f, s-1)^2 (degree 6 = 2 + 2 + 2, all GL1 over Q(omega)). For g = eta(4t)^2 eta(8t)^2 (CM by
Q(i)): Sym^2 g = eta(4t)^6 (+) chi_{-4}|.|, and f x Sym^2 g = [degree 4, a Hecke character of Q(zeta12)] (+) f (x) chi_{-4}(1);
symmetrically g x Sym^2 f = [degree 4 over Q(zeta12)] (+) g (x) chi_{-3}(1). eta(2t)^3 eta(6t)^3 is the Mason form of a
Weyl-group element of A5^4 D4.""",
    where="""GRH for the degree-six products at the CM points reduces to GRH for Hecke L-functions of Q(omega), Q(i) and Q(zeta12) (the
first rung beyond Dirichlet); the Dirichlet pieces chi_{-3}, chi_{-4} are covered.""",
    argument="""CM decomposition Sym^2 Ind psi = Ind psi^2 (+) chi_K |.|; identification of the eta products by comparing Euler factors
at every prime in range (far beyond the Sturm bounds of these levels).""",
    missing="""Nothing for the identities.""")
E["X-gen-021"] = dict(
    title="Open: GRH for L(h x Sym^2 h) with h the newform of S4(Gamma0(6)), the first cuspidal GL2 x GL3 object of lambency 6",
    attaches_to="none (GRH side of the moonshine atlas)", uses="X-gen-020", kind="conjecture", status="sketch",
    sources=f"{SRC_PASS}; Gelbart-Jacquet and Kim-Shahidi functoriality for non-CM forms",
    statement="""h = eta(t)^2 eta(2t)^2 eta(3t)^2 eta(6t)^2 (the Mason form of the M24 class 1^2 2^2 3^2 6^2) has no CM, Atkin-Lehner signs
W2 = W3 = +1 and root number +1. L(h x Sym^2 h) = L(Sym^3 h) L(h, s - 3) has degree 6 with Sym^2 h cuspidal on GL3 and
Sym^3 h cuspidal on GL4. Conjecture (GRH): its nontrivial zeros lie on the critical line.""",
    where="""The lambency-6 degree-six L-function that no known rung covers.""",
    argument="""No CM: a_p(h) is nonzero in every class of p mod 3 and mod 4; the signs from a_2 = -2, a_3 = -3.""",
    missing="""Everything beyond the statement.""")
E["X-gen-022"] = dict(
    title="The spin L-function of the Bolza curve is a mu4-twisted Hecke L-function of Q(sqrt(-2))",
    attaches_to="none (GRH side of the moonshine atlas)", uses="X-gen-015", kind="identity",
    status="sketch (pattern checked at all 45 odd primes below 200; proof to write)", sources=f"{SRC_PASS}",
    statement="""For C: w^2 = z^5 - z and p odd, write p = a^2 + 2b^2 when p = 1, 3 mod 8. The L-polynomial of C at p is
(1 -+ 2a T + p T^2)^2 for p = 1 mod 8, 1 + 2(a^2 - 2b^2) T^2 + p^2 T^4 for p = 3 mod 8, (1 - p T^2)^2 for p = 5 mod 8 and
(1 + p T^2)^2 for p = 7 mod 8. So the Frobenius eigenvalues are +-pi (each twice) at p = 1 mod 8 and +-i pi, +-i conj(pi) at
p = 3 mod 8, pi = a + b sqrt(-2): the GSp4 L-function of the genus-two curve whose automorphism group is GL2(F3) is a quartic
twist of a Hecke L-function of Q(sqrt(-2)). Over Q the Jacobian is not isogenous to a product of elliptic curves (the
L-polynomial at 3 is 1 - 2T^2 + 9T^4).""",
    where="""Layer four of the GRH ladder at the point where it meets lambency 6: the paramodular rung collapses to GL1 over Q(sqrt(-2)),
with the phase i at p = 3 mod 8.""",
    argument="""Point counts over F_p and F_{p^2} give the L-polynomial; compared with the representation p = a^2 + 2b^2.""",
    missing="""The proof from the automorphism (z, w) -> (iz, zeta8 w) of order 8 and the CM type of the Jacobian.""")
for k, e in E.items():
    txt = (f"---\nid: {k}\ntitle: {e['title']}\nattaches_to: {e['attaches_to']}\nuses: {e['uses']}\nkind: {e['kind']}\n"
           f"status: {e['status']}\nby: {BY}\nsources: {e['sources']}\n---\n## Statement\n{e['statement']}\n\n"
           f"## Where it goes in the fleet's graph\n{e['where']}\n\n## Argument\n{e['argument']}\n\n## What is missing\n{e['missing']}\n")
    (D / f"{k}.md").write_text(txt, encoding="utf-8", newline="\n")
print("written", len(E), "entries into", D.name)

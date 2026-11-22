# Independent full audit of regular-target specialization RS.1–RS.11

**PASS under the supplied regular semistable-model hypotheses.** This is an auxiliary theorem. It does not construct the constant-target K1 lift or identify its endpoint class, and it gives no new main-gate movement.

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, `/root/cycles_continuation`; effort setting not separately exposed.

Read the entire `../frobenius/C3_regular_target_specialization_RESEARCH.md` during the checkpoint23 source freeze, after20:00:43UTC. Exact reviewed SHA256: `f95b8a3644945eaba62825f2e4fa7167df4c3212db346a3b0b00a1f7aac82356`. This receipt was saved only after root's20:05:40UTC thaw. No numerical program was run.

## Independent reconstruction of the entire proof

The supplied algebraic DVR A and its regular semistable parameter model are essentially of finite type over the perfect field k. Consequently their products with smooth Y are regular and noetherian. The generic endpoints extend by properness. At a node with local equation xy=pi up to a unit, a section cannot have both x and y in the maximal ideal of A because their valuations would sum to at least two. Thus each section meets one smooth component of the reduced special fibre with multiplicity one.

The localization boundary b is supported on Y×T and becomes zero after forgetting supports. Its decomposition as a sum of the regular-component Gysin images is valid: support-union Mayer–Vietoris has only regular node intersections Y, whose supported negative K group is K_(-1)(Y)=0 by regular purity. Iterating the finite union therefore gives the required surjection on supported K0. Equivalently, coherent dévissage inside the regular ambient product gives the same surjection. Neither argument invokes perfect purity for the singular union Y×T. The tuple beta_j is not unique, and uniqueness is not used.

The normal line of P_j is O_Pj(−sum of its nodes), because the whole reduced special fibre is the principal divisor of pi. Self-intersection is consequently multiplication by

    1−[N_j^vee]=1−[O_Pj(sum nodes)]=−sum_b[O_b].

The last equality follows by successive Cartier sequences and triviality of the twists on each rational point. This checks the minus sign in RS.7. Pullback of another component's Gysin class is the positive transverse point Gysin class at each shared node. Projection formula then gives exactly the difference beta_other,b−beta_j,b in RS.8. Pushing under the proper smooth projection Y×P_j→Y gives RS.9, since a point section composed with that projection is the identity. All these maps are perfect proper pushforwards or regular Tor-independent restrictions.

Modulo J_0^prop(Y), every point evaluation of one beta_j is equal because P_j itself is an allowed fixed smooth proper parameter. Thus the pushed restriction equations become the usual graph Laplacian with multiplicities. The finite connected graph has one-dimensional rational kernel, the constants. Tensoring that finite rational linear-algebra statement with the arbitrary rational vector space K0(Y)_Q/J_0^prop(Y) is exact. Therefore all component values agree. This does not require a tree, a chosen leaf ordering, or injectivity of an exterior-product tensor map.

Naturality of localization along either section, followed by Tor-independent base change at its smooth special point, identifies its residue with precisely the evaluation of beta_j on the component met by that section. All other component terms pull back to zero. These two evaluations agree modulo J_0^prop(Y), proving RS.2. For an actual constant-target equality of endpoint differences with {u}z_F, the product boundary is ord_pi(u)z=e z, and division by the positive integer e is allowed rationally. Thus the stated consequence of RS.3 follows.

The extension to regular algebraizable targets retains all the displayed regularity and proper-pushforward hypotheses; the finite geometric and perfect-complex data can be checked on the supplied regular finite-type models. This does not turn a henselization of a scalar-extended local ring into a constant product.

## Source scope

The full proof is reconstructed from the supplied model, the displayed Cartier identities and the elementary rational graph argument. The exact perfect-pushforward, projection, base-change, localization and supported-union inputs are the already fully read Thomason–Trobaugh §§3.14–3.18, Theorem7.4, Theorem8.1 and Corollary8.1.4 recorded in the cycles HK audit. Their supported analogue and regular purity/negative-K inputs are used at the same scopes here. No new full reading of all of Thomason–Trobaugh, or of an uninvoked semistable-reduction theorem, is claimed in this receipt.

The model is a hypothesis. The proof needs the actual equality in K1 of the constant regular target; equality only after projection to exceptional components is insufficient. A lift over a henselization of R⊗k k(u) does not supply it. The marked-curve RC countermodel and the singular-node K_(-1)(E) issue are therefore unaffected.

The separately discussed rank-and-determinant theorem for K0(R×P) was not present in this frozen RS manuscript. Its audit will receive a distinct receipt after the owner saves the full text; it is not silently included in this PASS.

Saved after thaw: 2026-11-19T20:06:59.815054+00:00

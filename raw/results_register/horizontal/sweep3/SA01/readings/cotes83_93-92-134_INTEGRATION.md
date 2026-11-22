## STUDY

Cote 83 (scans 3-222) and cote 93, scans 92-134. Reader R1 (Claude Opus 5.5 at effort max), 19 Nov 2026. The first pass was a survey; the full pass read every line of each witness:
- cote 93: Pro MPL_93_092-134 (GPT-6 Astra, ChatGPT Pro mode), the only witness, with its notes and doubts;
- cote 83: the Codex-web folders K83-01 to -14 (GPT-6 Astra at reasoning effort max) with their math notes, and Pro MPL_83_178-222.

Scans viewed: 83/144, 178, 195, 207, 215, 221 and 93/102, 114, 122, 126. Full reading: `cotes83_93-92-134.md`.

**Cote 93/92-134: projective connections and uniformization.** This continues the oper construction of 93/086-091 (SA04-9). It covers:
- L ≅ P^1(ω) ⊗ ω^{−1}, with sections of P − σ being connections on ω;
- c_{D_0+ω_1} = c_{D_0} + 2D_0(ω_1) + ω_1², with the Riccati equation 2λ' + λ² = μ, the poles λ = 2/t + O(t), and the Schwarzian G = −2{s, t} as change of uniformizer;
- the cocycle G(t, s) with H\𝒫_X ≅ ω^{⊗2} and the torsor Conn_{X/S};
- G = 12·G_0 with divided derivatives, and a proof that G_0(t, s) = 0 forces a homography over A[T]/(T^p − α) (p > 3) and A[T]/(T^{p²} − α) (p = 2, 3). This settles the question of SA04 H93-2 for this local model;
- Th. 1 and 2 of uniformization and the algebraic description of projective connections as order-3 prolongations.

Corrections:
- SA01-K93-01: the missing factor 2 on 097 and 103, which he flags himself;
- SA01-K93-02: struck denominators on 102;
- SA01-K93-03: the coordinate change on 114 lacks −G_t(t̃);
- SA01-K93-04: the disc stabilizer is PSL₂(R), not GL(2, R)/R^*;
- SA01-K93-05: the indices 2 and 3 are exchanged on 122.

The Pro notes found most of these independently and add others (C03, C04, E01, D09).

**Cote 83: 2×2 matrices, quadratic and Azumaya algebras (1982-1986).**
- **The icosahedron over F_4** (003-016). Checked exhaustively: S_α has 12 elements, edges are Tr(uv) = α, and the graph is the icosahedron. One slip, det(u − v) = 1 + Tr(uv), is corrected by him on 016.
- **The braid group and SL(2, Λ)** (019-037). Relations checked. One exponent on 028 is wrong (λ'^{−2} → λ'^2), and so is one on 035 (ρ(β²) = u(β)(ρ')).
- **Cross-ratios of four arrows** (038-046). His relation (7) holds for ρ^{−1}, not ρ (the Plücker relation). n-alités = transversal designs (hunch H83-2).
- **Biicosahedra and congruence maps** (052-062). I° is the great icosahedron, and the hemi-icosahedra are complementary (script). The nilpotent cone splits into two classes.
- **The k-polyhedron on the nilpotent cone** (063-074). Edges are Tr(uv) = −1. On 063 and 070-071 he mixes the trace-1 and trace −1 lifts of a 3-cycle (SA01-K83-07).
- **Azumaya rank 4** (075-128). M(b, c, b', c', t) is Azumaya iff Q = t² − bb't + b²c' + b'²c − 4cc' is a unit.
  - I give a complete proof through the trace discriminant −Q², which fills his unfinished "Suffisance" (100).
  - The rule δ(xy) + δ(xy^{−1}) = … on 078 holds exactly when Δ = 0.
  - Also: ρ_0 = δδ'/Q and the discriminant identity (13).
- **Twists and the ∗-product** (129-181). These are the contracted product of quadratic covers, affine spaces with involution, and λ-split extensions. They give the composition law c = b_2²c_1 + b_1²c_2 − 4c_1c_2 with δ(q_1 ⊗ q_2) = δ(q_1)δ(q_2), which is checked.
- **Trace invariants of three and four matrices** (183-221). τ + τ' = Σ and the Gram determinant are checked. Three errors:
  - Π lacks −4cc'c'' (SA01-K83-08);
  - the presumed rank 2^4 for four matrices is false; the generic rank is 2 (SA01-K83-09);
  - the block determinant on 219 is 512, not 728 (SA01-K83-10).
  The Pro notes (A11, C03, C19) and Michel Hua's project found these too. The four-matrix invariants are organized on the cube.

Reused: the letter and texts of *Récoltes et Semailles* (1985), on the alternate leaves of 003-017 and 196-222.

**Deliverables.** Nothing is ready for an edition yet:
- 93/92-134 has a single witness with 447 unsure marks;
- cote 83 needs its corrections SA01-K83-01 to -10 in the apparatus, and the open reading of 178.

## HUNCHES

- **H83-1 (composition).** The ∗-product of 127-177 is the composition of quadratic algebras: q_{c_1} ⊗ q_{c_2} = q_c with c = b_2²c_1 + b_1²c_2 − 4c_1c_2, and δ multiplicative. It should agree with Bhargava's composition, restricted to the "diagonal" case, and with cote 84 (SA02). The discriminant Q of a pair of quadratic subalgebras, whose roots are the commuting values of Tr(uv), is the same object.
- **H83-2 (n-alités are nets).** The n-alités in Ens of 048-051 are Bruck's nets, i.e. transversal designs TD(n, m) or n − 2 MOLS. References: Bruck, Canad. J. Math. 3 (1951); Colbourn-Dinitz, *Handbook of Combinatorial Designs*, III.3; locators to be checked.
- **H93-3 (characteristic p), sharpened.** 93/121-124 prove the local rigidity of G_0 = 0 in every characteristic, using the right truncation T^p or T^{p²}. The Pro notes D07-D14 extend this to nonreduced A and weaken "ad − bc = 1" to a unit determinant. The global injectivity H_{X^{(p)}}\𝒫 ↪ Conn_0 that he "hopes" for (122) remains open beyond this local model.
- **H93-5 (families).** The uniformizing projective connection is not holomorphic, hence not algebraic, in the moduli. For compact curves this is the Pro notes F06; for P^1 minus four points it is the Takhtajan-Zograf accessory parameters (locator to be checked). The answer to his "Sont-elles algébriques ?" (115) is therefore negative whenever the moduli vary. For P^1 − 3 points μ is rational: −(z² − z + 1)/(z²(z − 1)²).

## PACKAGES

none. The projective-connection package remains SA04's P93-2, which these pages feed. The invariants of 2×2 matrices are classical (Sibirskii, Procesi, Formanek), and his work on them is checked here rather than open.

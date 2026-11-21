# The two GRH results and the Hodge conjecture: routes, gates, and where the programme touches them

By the war-game agent (Claude Fable 5.2 at effort max), 21 November 2026, for the main session (Claude Opus 5.5 at
effort max). Work file with the list of what was read: `C:\Users\user\Documents\agent_notes\a3ccbc11011bcdf3a_NOTES.md`.

**Status words.** *Read*: I checked it in the source text in this session. *Proved*: an argument given here, checked
by me only. *Sketched*: a mechanism with its steps, not all verified. *Proposed*: a statement to test. *From memory*:
literature I did not reopen; section 8 lists it for verification. (mine) marks statements of this pass.

**The inputs, as cited.** L. Alpöge, *Remark* (alpo.ge/remark.pdf, 20 Nov 2026) with its Lean archive: RH and GRH for
Dirichlet L-functions, cited as a theorem. Masullo, *The Music of the Primes* (draft): GRH for Hecke L-functions of
every number field; every consequence below is marked **conditional (Masullo)**; one of our Pro runs reports its last
numbered divisor theorem unfinished (the main session's information). OpenAI family 032, *The rational Hodge
conjecture for CM abelian varieties* (6 Oct 2026; human proof by van Hoften and Sempliner, Hexagon 2610.00259);
Milne's report (Hexagon 2611.00244); Markman, arXiv 2502.03415. Of these I read: Alpöge's note (4 pages), the Lean
map of the main session's reader (Claude Opus 5.5 at effort medium, as its header says), and pages 1–4 and 47–51
of the 032 paper (introduction, contents, section 8). I did not read Masullo, the van Hoften–Sempliner paper,
Milne's report, Markman's paper, or sections 2–7 of 032.

---

## 0. The answer in brief

1. **Neither GRH result implies anything about the Hodge conjecture, and nothing goes back.** An L-function counts
   Tate classes by a pole at the edge of its strip and homologically trivial cycles by a zero at its central point;
   GRH is about all the other zeros (section 1).
2. **The bridge is in the proofs: one machine at two signatures, with a third setting in the literature.** The proof of the Hodge conjecture for CM
   abelian varieties (032) and Alpöge's proof both run on theta lifts of Hecke characters of a CM field to unitary
   groups. 032 uses a group of signature (2,1) at one real place and definite at the others: it gets holomorphic
   one-forms on a ball quotient, a surface, and a cycle. Alpöge uses totally definite groups: he gets periods, a
   positive determinant, and zeros on the line. I read this in both texts (Route 1).
3. **From CM to every abelian variety the missing statement is a bound**, which I put in three equivalent forms
   (families, Hecke orbits, primes) and prove equivalent. 032 gives the rational statement on every isogeny class;
   the open part is a division with bounded denominators. GRH does not supply it: heights of CM points grow
   (Route 2).
4. **Positivity.** 032's non-vanishing step is itself a positivity argument. Cote 44 is Grothendieck's reduction
   of Hodge positivity to the polarization of an intermediate Jacobian; cote 16 no 7 defines his universal Lefschetz
   ring on the cohomology of a principally polarized abelian variety; both now have unconditional cases in
   characteristic p through Milne's report (Route 3).

The top three routes are 1, 2, 3 in that order. Routes 4–6 are support: integral structures, the CM test bed, and
what GRH itself supplies.

---

## 1. The shape, corrected (point 0 of the starting sketch)

For X smooth projective over a number field and M = H^w(X):

| place on the s-line | what it counts | conjecture | where the archive is |
|---|---|---|---|
| pole at the edge (w = 2p: s = p + 1) | cycles of codimension p modulo homological equivalence | Tate 1965; with Mumford–Tate it is Hodge | 14, 16 |
| value at the central point (w = 2p − 1: s = p) | periods on definite groups; Selmer groups | Bloch–Kato; Gan–Gross–Prasad | (Alpöge steps 7, 12) |
| order of zero at the central point | rank of CH^p(X) homologically trivial | Beilinson–Bloch; heights | 44 |
| every other zero | nothing geometric known | GRH | — |

- The pole order at the edge equals the dimension of the Galois invariants as soon as the other constituents have
  L-functions holomorphic and non-zero at the edge. That is a statement of prime-number-theorem type (known for
  automorphic L-functions, from memory), not RH. Whether the invariants are classes of cycles is not visible to the
  L-function at all.
- So the sketch's "GRH is a statement about the centre" should read: GRH is about the central *line*; the central
  *point* is Beilinson–Bloch, which is where cote 44 lives. The SA06 intake, §4.1, reaches the same verdict for
  Griffiths groups ("cohomology-blind").
- One place where the edge does speak to the standard conjectures, in Grothendieck's own form (letter to Coates,
  4.1.67, cote 16 scans 44–46, read): his condition A "can also be expressed in terms of an equality of dimensions
  of C^i and C^{n−i}" (ranks of algebraic classes), and C(X) (Λ algebraic) is equivalent to C(Y) and A(X × X) in the
  critical degree. Hard Lefschetz is Galois-equivariant, so the L-functions of H^{2i}(i) and H^{2n−2i}(n − i) are the
  same and Tate's pole orders are equal: A is the statement that the cycles realize a symmetry the L-function already
  has. This is the only thing the L-function "knows" about Λ.

## 2. What now holds, and what follows formally

| statement | source | status |
|---|---|---|
| Hodge for every complex CM abelian variety; generalized Hodge for them | 032, Th. 1.1, Lemma 8.1, Cor. 8.2 (read) | claimed; Lean for the Hodge statement; human proof 2610.00259 |
| Tate for abelian varieties over finite fields, with numerical = homological equivalence; Hodge standard conjecture for abelian varieties in every characteristic | 032, Cor. 8.3 and 8.4, from Milne's Theorems 7.1 and 3.3 with corrections it cites (read); Milne's report (not read) | follows from the line above |
| every Hodge class on an abelian variety over the algebraic closure of Q is algebraic on each good special fibre | 032, Remark 8.5 (read) | follows, with CM transport |
| Tate for CM abelian varieties over number fields | Pohlmann 1968: Hodge and Tate equivalent for CM type (from memory) | follows |
| Milne's rationality conjecture | family 001; Madapusi, Hexagon 2610.00226; Milne's report (scoreboard row, read) | claimed |
| Weil classes algebraic on abelian fourfolds of Weil type; Hodge for abelian fourfolds | Markman (scoreboard row, read) | arXiv |
| RH for the L-functions of Artin–Tate motives over Q with abelian Artin part | Alpöge | theorem as cited |
| RH for the L-functions of all CM motives (products of Hecke L-functions, Shimura–Taniyama–Weil, Deligne) and for Dedekind zeta functions of all number fields | Masullo | **conditional (Masullo)** |

Two corrections to point 1 of the sketch. A CM elliptic curve over Q has L(E, s) = L(ψ, s) for a Hecke character ψ
of its CM field, which is not a Dirichlet L-function: Alpöge's theorem covers only the Artin–Tate part of the CM
world. And on CM motives "Hodge, Tate and RH hold together" holds with Tate through Pohlmann and RH conditional on
Masullo. Beilinson–Bloch at the central point stays open there.

---

## 3. The routes, ranked

### Route 1. One machine in three settings: definite, signature (n,1), integral models (theta lifts of Hecke characters to unitary groups)

**Statements.**

- **1.1 (read: 032, §§1.2–1.3 and contents).** 032 reduces every CM Hodge class to four-factor relations
  v₁ + v₂ = v₃ + v₄ among CM types (Pohlmann's balance criterion, Deligne, André, Hazama, Gao–Ullmo). A four-factor
  class is made algebraic by a surface criterion: rational Hodge maps hᵢ : U(vᵢ) → H¹(S, Q) with
  ∫_S h₁(α₁) ∪ h₂(α₂) ∪ h₃(α₃) ∪ h₄(α₄) ≠ 0; the cycle is the image of S in ∏ B(vᵢ). The surface is a compact
  arithmetic quotient of the complex two-ball, for a unitary group of signature (2,1) at one chosen real embedding
  and definite at all the others. The one-forms are holomorphic theta forms (Weil's theta covariance, the unitary
  splittings of the Weil representation, the Kudla–Millson kernels, and a product calculation of
  Bergeron–Millson–Moeglin, Lemmas 5.7 and 5.11). Their CM sources are identified through Hecke endomorphisms of
  Albanese varieties, a polynomial relation between Hecke operators and Frobenius, the Weil weight in degree one,
  which forces slope zero or one, and weak admissibility.
- **1.2 (read: Alpöge's note, steps 7–9, 12, 15, 18; the Lean map, §3 and the step table).** Alpöge chains theta
  lifts U(X₀) → U(X₁) → … → U(X_m) between totally definite unitary groups, π ↦ π ⊞ μ_j[t] (step 8), with
  Gan–Gross–Prasad periods (step 7), a seesaw after Rallis by which the period of the iterated lift is a Bessel
  period that does not depend on the Hecke characters (step 12), norms of lifts through Chowla–Selberg, Weyl and the
  Siegel mass formula (step 9), and an integral structure glued across Hecke characters (step 15). The Lean map records, in the chain to `Main`: `DefiniteSideCondition`, theta
  integrals, Siegel–Weil and a covolume bound; `Formalism/PeriodIntegrals/BesselPeriodGGP.lean`;
  `ThetaCorrespondence/RallisInnerProduct`; `UnitaryGroupMassFormula`; and, as theorems proved inside the archive,
  the Galois representations of regular algebraic polarized cuspidal representations of GL_a over CM fields
  (`galoisRepresentations_of_thetaLift`, with Hodge–Tate and crystalline properties) and temperedness
  (`CaraianiTempered`, `ClozelPurity`), with libraries `GroundTheory/PAdicHodge` and `Development/WeilBound`. So
  Alpöge's archive contains the indefinite side too, and it uses the same two ingredients as 032's sections 5–6: the
  Weil bound and p-adic Hodge theory applied to theta lifts.
- **1.3 (from memory).** The third signature is the integral model at an inert prime. There the special cycles of
  the Kudla programme have arithmetic intersection numbers equal to *derivatives* of local densities
  (Kudla–Rapoport; Li–Zhang), heights of arithmetic theta lifts are central derivatives (Li–Liu), the basic locus is
  uniformized by the Shimura set of the totally definite group (Vollaard–Wedhorn), and its components give Tate
  classes modulo p (Xiao–Zhu).
- **1.4 (mine, sketched).** The Arthur parameters are the same. The holomorphic one-forms on a quotient of the
  n-ball have parameters μ[n] ⊞ χ (for n = 2, Rogawski's packets, from memory); Alpöge's lifts add blocks μ_j[t]. The
  SL₂ of a block is the Lefschetz sl₂ on the cohomology of the Shimura variety (Arthur's conjecture, from memory),
  so a block of size t is a Lefschetz string of length t: this upgrades suggestion 6 of 20 November from "proposed"
  to a known principle. Cup products of theta classes are theta classes (the product lemma 032 takes from
  Bergeron–Millson–Moeglin), so 032's wedge of two one-forms is a two-step lift and Alpöge's m-fold lift is the
  same product structure iterated m times at definite signature.
- **1.5 (mine, elementary; the tensor construction from memory).** Alpöge's definite side is function theory on
  finite sets of CM abelian varieties. For B with CM by O_E and a positive definite Hermitian O_E-lattice X, the
  abelian variety B ⊗ X is isogenous to a power of B and carries the polarization of X; the unitary group of X is
  its group of polarized automorphisms, and the classes in the genus of X give the finitely many polarized varieties
  of this local type. Inside a unitary Shimura variety these are special points with CM by E itself: for a
  Hermitian space of signature (n,n), the points (B ⊗ X₁) × (B ⊗ X₂) with X₁, X₂ definite. For the hexagonal curve
  C/Z[ω] of step 3 they are the polarized abelian varieties isomorphic to powers of that curve. So the points where
  Alpöge's forms live are points of the families of Route 2.
- **1.6 (mine; the identity is proved, the reading is proposed).** "Multiplicity over the integers" exists natively
  at the third signature: an arithmetic intersection number is a length, and it equals a derivative. The exponent of
  step 2 fits: a·p/(p² − 1) = a·Σ_{s≥1} 1/e_s with e_s = p^{s−1}(p + 1), the ramification index of Gross's
  quasi-canonical lifting of level s at an inert prime (from memory), so the divisibility of D^a θ(0)/Ω^a is the sum
  over all levels of the valuation of the Lubin–Tate coordinate of that lifting. This carries suggestion 2 of
  20 November to the Gross–Zagier, Gross–Keating and Kudla–Rapoport multiplicities.
- **1.7 (mine, proposed).** The mixed period of 032 §4 and the Bessel period of Alpöge's step 12 are two values of
  one seesaw pairing, at signature (2,1) and at definite signature. 032 gets its non-vanishing by moving the data at
  the compact places only, with the finite theta input and the quotient fixed (§1.3); the compact places are where
  Alpöge's groups live.

**Mechanism.** For a Hermitian space over a CM field and a family of Hecke characters, the theta correspondence
gives: at definite signature, numbers (periods, central values); at signature (n,1), cohomology classes and special
cycles (classes at the edge); on integral models, heights (central derivatives). A change of signature at one place
is governed by local root numbers (theta dichotomy, from memory).

**Gate.** 032 reaches CM abelian varieties because the first cohomology of a ball quotient has only CM sources
(lifts of characters; from memory, Rogawski and Murty–Ramakrishnan). A non-CM abelian variety needs classes with
non-CM sources: lifts from U(1,1) and quaternionic forms (abelian varieties of GL₂-type), or the orthogonal groups
O(2,n) of Kuga–Satake type. Alpöge's note (p. 3) says that the first gain, multiplicity 2, was seen on O(2,n).

**First tests.**
- T1. Set 032 §§4–6 beside the Lean statements named in 1.2 (the map gives paths) and decide 1.7; decide whether
  032's non-vanishing admits an explicit lower bound.
- T2. Prove or refute the reading in 1.6: locate step 2 in the Lean and compare with Gross's liftings. The Lean
  map's candidates for step 2 (its confidence: low): `Development/AbelianVarietyTheory/BlockTheory/HeightDefect`,
  `Proofs/HomogeneousIdeals`, `Proofs/CubicalLineBundles`, and the literature props `IsGoodCMCurve`.
- T3. Can a 2n-factor balanced relation be realized directly by the cup product of 2n theta one-forms on a quotient
  of the n-ball, without Hazama's reduction to four factors? This matters for degrees (Route 2).
- T4 (the sketch's test b). Step 14's a priori stop at 2/3 against the range of
  Bergeron–Millson–Moeglin (Hodge classes on n-ball quotients in degrees outside ]n/3, 2n/3[ are spanned by special
  cycles; from memory). The note alone does not decide it. The Lean map places step 14 in
  `UnitaryGroupMassFormula/UnipotentCost` (its confidence: low); in Bergeron–Millson–Moeglin the third comes from
  the size of the unipotent block against the rest of the parameter. Same trade-off, unverified.

### Route 2. From CM to every abelian variety: the gate is bounded division

**Setting.** S a special subvariety of a moduli space of polarized abelian varieties with level structure, A → S
the family, t a flat section of R^{2p}f_*Q(p) of Hodge type at every point (S lies in the Hodge locus of t; such
loci are algebraic by Cattani–Deligne–Kaplan and special). For s in S let c(s) be the least max(N, D) such that
N·t_s = [Z⁺] − [Z⁻] with Z⁺, Z⁻ effective of degree at most D.

**Statements.**

- **2.1 Lemma (proved; standard).** {s : c(s) ≤ C} is a Zariski-closed subset S_C of S. *Proof.* Relative Chow
  varieties of bounded degree are projective over S with finitely many components; on a connected component of the
  pairs (Z⁺, Z⁻) the class [Z⁺] − [Z⁻] − N·t is a flat section, so its vanishing is open and closed; S_C is the
  image of finitely many components under a proper map. ∎ Hence: **t_s is algebraic for every s in S if and only if
  c is bounded on some Zariski-dense subset of S.** (If t_s is algebraic for very general s, Baire gives S_C = S for
  some C.) CM points are countable, so algebraicity at every CM point, which 032 gives, does not suffice; this is
  the exact reason Deligne's argument yields absolute Hodge classes and not cycles.
- **2.2 Proposition (proved; Hecke form).** Let x₀ be any point of S. The points x whose rational Hodge structure
  with its tensors is isomorphic to that of x₀ (the Hecke orbit) are analytically dense in S, by real approximation
  for the generic Mumford–Tate group. For such x there is an isogeny ψ_x : A_x → A_{x₀} with ψ_x^* t_{x₀} = c_x·t_x,
  c_x a non-zero rational number. So if N₀·t_{x₀} = [Z₀], then [ψ_x^* Z₀] = N₀·c_x·t_x: **algebraicity at one point
  gives the rational Hodge conjecture on its whole Hecke orbit, with denominators c_x.** With 2.1: t is algebraic on
  all of S if and only if on the Hecke orbit of x₀ the class t_x has representatives of bounded N and D. I call
  this *bounded division* of ψ_x^* Z₀ by c_x.
- **2.3 Dichotomy (proved, given André–Oort, from memory).** Either S_C = S for some C, or for every C the CM
  points of S_C lie in a finite union of proper special subvarieties, and then c tends to infinity along every
  sequence of CM points that leaves every proper special subvariety. So Hodge for (S, t) is equivalent to
  boundedness of c along one such sequence.
- **2.4 Lemma (proved for the Weil family; no bound from Lefschetz-type cycles).** Let S be the family of abelian
  2n-folds of Weil type for an imaginary quadratic field K, n ≥ 2, and t a Weil class. At the K-rational points of
  the period domain (dense; the fibre is isogenous to E^{2n}, E with CM by K) every Hodge class is a polynomial in
  divisor classes and the Weil classes are spanned by components of classes of abelian n-folds, the component of
  the graph of a homomorphism φ between the two eigen-parts being proportional to det φ. But the points of S whose
  fibre contains an abelian subvariety of degree ≤ D, or a divisor class of degree ≤ D not proportional to the
  polarization, form a proper closed subset, because the generic fibre is simple with Néron–Severi rank one. So
  along a generic sequence these representatives have degree tending to infinity: **a bounded representative cannot
  be built from divisors and abelian subvarieties.** The same argument applies to every endomorphism outside the
  generic ring O_K: its degree tends to infinity along a generic sequence. As I read 032 §§1.2–1.3, it isolates its
  lines with the full CM field of the point, so its cycles, as constructed, should not be expected to stay bounded
  (this is an expectation, not a proof: a composite can be smaller than its parts; T6 and T9 measure it). A uniform
  construction must isolate the Weil line with the generic endomorphisms only; for Weil type that is possible, since
  the projector onto the Weil classes is a polynomial in the action of K. What it then needs is one n-dimensional
  subvariety Z, in every fibre and of bounded degree, with ∫_Z dz₁…dz_n dw̄₁…dw̄_n ≠ 0 (z on the σ-part, w on the
  σ̄-part of the Lie algebra): the family form of 032's surface criterion. A subvariety stable under an order of K
  gives zero, and so does every cycle built from divisors and curves by intersection and Pontryagin product (they
  are Lefschetz classes), so Z has to be skew to the action of K. Schoen's surfaces in Prym varieties of cyclic
  covers are of this kind (from memory).
- **2.5 Lemma (proved; arithmetic form).** Let X be smooth projective over a number field and t an absolute Hodge
  class. Then N·t is algebraic over the algebraic closure if and only if for infinitely many primes v the reduction
  t_v is represented by a difference of effective cycles of degree at most D with the same N and D. *Proof.* The
  scheme of such pairs with class N·t is projective over an open part of the ring of integers (the class condition
  is open and closed by smooth proper base change); if it has points in infinitely many residue characteristics, its
  image is constructible and contains the generic point. ∎
- **2.6 (read: 032, Remark 8.5, pp. 50–51).** For A over the algebraic closure of Q with good reduction A₀ at a
  place over p, every rational Hodge class on A specializes to the class of one rational algebraic cycle on A₀, in
  all realizations. The mechanism given there: the specialization is the pull-back of a specialized CM Hodge class
  by a rational homomorphism of special fibres (CM transport, its reference [32]); Theorem 1.1 makes the CM class
  algebraic, and the cycle is its pull-back after clearing the denominator of the homomorphism. The remark says
  itself that this is algebraicity on the special fibre, not the Hodge conjecture for A. With 2.5: **a Hodge class
  on an abelian variety is algebraic modulo every good prime, and it is algebraic if and only if the complexity of
  its representatives stays bounded along infinitely many primes.** A non-algebraic Hodge class would pass the test
  at every single prime and fail only through unbounded complexity. In the project's vocabulary it would be a ghost.
  The two forms are one: the representative modulo p comes from a CM point x_p of the same special subvariety and
  an isogeny with a denominator, so it is an instance of the division of 2.2 at x_p. Bounded division at the points
  x_p, with bounded denominators, gives the bound over primes.

**Mechanism known to give the bound.** In codimension one it is the theta group: ψ^* L₀ = L^{⊗c} ⊗ P with P in
Pic⁰, which is divisible. For semi-homogeneous bundles (Mukai, from memory) the pull-back splits into copies of a
simple one. In Markman's cases, as I understand the method (to verify in arXiv 2502.03415), the bound is the
properness of a moduli space of sheaves with fixed numerical invariants, entered through semiregularity. So the
candidate form of the gate is: *represent the 032 class at one CM point by an object of the derived category whose
semiregularity map is injective.*

**Where GRH does and does not enter.** Point 2 of the sketch brings GRH in through Colmez's formula. Heights do not
give the bound: Faltings heights of CM points tend to infinity with the discriminant, so a degree bound in terms of
the height says nothing along a dense set. What GRH gives here is the size of the 032 cycles: their degrees are
integrals of squares of theta one-forms over the surface, that is Petersson norms of theta lifts, which the Rallis
inner product formula turns into values of Hecke L-functions at the edge times a volume (mine, sketched). GRH pins
such values between powers of log log of the conductor (**conditional (Masullo)** for Hecke characters; by Alpöge
where the character is Dirichlet). That measures the growth; it does not remove it.

**Gate.** Bounded division on one Hecke orbit of each (S, t).

**First tests.**
- T5. S the Weil family of abelian fourfolds for K = Q(ω), x₀ = E⁴ with E = C/Z[ω] (the curve of Alpöge's step 3),
  t a Weil class. Markman's theorem gives the bound a posteriori. Exhibit it: write the bounded representatives on
  the fourfolds isogenous to E⁴ and name what divides.
- T6 (the sketch's test c, made exact). Compute the degree of the 032 cycle for one four-factor relation as a
  function of the level, by the Rallis inner product formula.
- T7. Is the 032 surface semiregular in ∏ B(vᵢ) (Bloch's map H¹(N) → H^{p+1}(Ω^{p−1}))?
- T8. First open cases of 2.2 after Markman: the Hecke orbit of E⁸ (n = 4), and E⁶ for discriminants other than
  −1. (As 032's introduction reports his theorem: Weil classes on abelian sixfolds of Weil type with polarization
  discriminant −1, and from it the Hodge conjecture for all abelian fourfolds.)
- T9. For one abelian variety A over Q with a Weil class and the CM points x_p of Remark 8.5: how do the degree of
  the 032 cycle at x_p and the denominator of the transport grow with p?

### Route 3. Positivity

**Statements.**

- **3.1 (read: 032 §1.3).** 032's non-vanishing is a positivity argument. Two decompositions of the same Hermitian
  plane give two-forms η and η′; weak approximation makes them close at the compact places, so the pairing of η′
  with η stays close to the self-pairing of η, which is not zero. The self-pairing of a holomorphic two-form is
  positive (Hodge–Riemann on H^{2,0} of the surface). So in 032 a sign and a continuity argument produce the
  non-zero period, and the period produces the cycle. This is the one instance I know where "positivity run
  backwards" makes an exceptional Hodge class algebraic, and it answers point 3 of the sketch better than Λ does.
- **3.2 (read: cote 16 scans 44–50, letter to Coates of 4.1.67; his lettering, C = "Λ algebraic").** "A + index
  implies B"; C(X) ⟺ C(Y) and A(X × X) in the critical degree H^{2n−2} → H^{2n+2} (scan 45); "C(X) together with
  the index relation I(X × X) implies that the ring of correspondance classes for X is semi-simple" (scan 49); "the
  deduction of the Weil conjectures from the conjectures C and A" (scan 50); Λ_Y = φ^*Λ_X²φ_*, so C(X) implies C(Y)
  (scan 40). So the answer to "does the sign make Λ algebraic" is his own: with the index theorem, as in
  characteristic 0, algebraicity of Λ_X is an equality of two ranks of algebraic classes on X × X. The sign gives
  injectivity, never the missing cycle. Beyond codimension one I know no theorem where a sign alone produces a cycle
  except through a period, as in 3.1.
- **3.3 (read: cote 16 scans 14–17).** His universal Lefschetz ring is defined on an abelian variety: "un module
  libre M₀ de rang 2n sur Z, muni d'une 2-forme alternée non dégénérée (sur Z !)", M₀^* = ΛM₀, L x = ξ₀x,
  Λ₀x = ξ₀^* ⌟ x, Φ₀ = Z[L₀, Λ₀] ⊂ End_Z(M₀^*). That is the integral cohomology of a principally polarized abelian
  variety with its theta class. Calibrating there (from memory unless marked): Λ is the Fourier conjugate of L for
  the Fourier transform of cote 47 (Lieberman, Beauville, Künnemann); the Weyl element of the sl₂ is the Fourier
  transform and, up to the Weil operator, the Hodge star, so the Hodge–Riemann relations on an abelian variety say
  that "Fourier composed with the Weil operator" is positive; (sl₂, Sp_{2n}) is Howe's dual pair on the exterior
  algebra. **(mine, proved by a count)** For Weil type, with W the 2n-dimensional σ-part of H¹, the invariants of
  U(W) in Λ^*(W ⊕ W^*) are the Lefschetz string Sym^{2n}(C²), and the two Weil classes are the one-dimensional
  GL₂-types det⁰ and det^{2n}, paired with the characters det^{∓1} of U(W). So exceptional classes of Weil type are,
  in Howe's duality, the lifts of one-dimensional characters: the same slot as the lifts of Hecke characters in
  Route 1.
- **3.4 (read: cote 44 scans 2, 4, 8–9).** Th. 4 ("Hodge"): for dim X = 2m − 1 the self-duality of P^m(X) is a
  polarization. Th. 5 ("Néron"): ⟨ζ, ζ′⟩ = (−1)^m Z·Z′ for the Néron–Tate form on the generic hyperplane section of
  a pencil, with the margin "Doit résulter d'un énoncé plus général sur des fibrations, et admet une variante
  locale". Letter to Serre, 12.8.1964: "le théorème de positivité de Hodge se ramène à l'énoncé suivant", the
  positivity of D = r_*(p^*(z).q^*(z)) on T × T, with the margin "il faut tenir compte de la décomposition
  primitive". **(mine, sketched)** For a curve C and z on C × X, D is the transposed correspondence composed with z,
  and its positivity is the Hodge standard conjecture for the Künneth component H¹ ⊗ H^{2m−1} on J(C) × X, primitive
  part. **So Th. 4 holds, on the primitive part, for every abelian variety X in every characteristic, given 032,
  Cor. 8.4** (J(C) × X is an abelian variety). In characteristic 0 it is Hodge theory, as his margin "Connu
  tel quel" says. Hunch H9 of 12 Nov (Th. 5 is the Mordell–Weil lattice formula in codimension m; Th. 4 over
  function fields gives the Hodge standard conjecture in the middle degree) stands, and Milne's theorem now verifies
  its conclusion for abelian varieties.
- **3.5 (from memory; the arithmetic sibling).** Over a number field the height pairing of Beilinson and Bloch on
  cycles algebraically equivalent to zero is the Néron–Tate pairing on higher Picard varieties (Künnemann; H. Saito's
  varieties are Grothendieck's P^i), so its sign there is Th. 4. For cycles only homologically trivial the sign is
  the arithmetic Hodge index conjecture (Gillet–Soulé). GRH implies that a central derivative is ≥ 0 when the
  central value vanishes, so wherever a formula of Gross–Zagier type equals a height to a central derivative, GRH
  gives the sign Th. 5 predicts. For CM forms the L-functions are Hecke L-functions: **conditional (Masullo)**.
- **3.6 Correction of my suggestion 4 of 20 November.** I wrote that Alpöge's sign-only proof of Weil is the
  Hodge-index route of cote 16. Footnote 3 of the note, reread: the definite sign it takes from middle cohomology
  is the concentration of the new cohomology of a hypersurface section in one degree (it names Bertini), which
  fixes the parity in the trace formula so that inverse roots cannot cancel; the bound comes from applying Parseval
  k times. That is the Fourier-transform line (Katz, Laumon; cote 47), not the Hodge index. The Hodge index enters
  through 3.1 and 3.3.

**Mechanism.** A definite form gives injectivity, semisimplicity, or the non-vanishing of a pairing between two
nearby objects. It gives a cycle only where a criterion already turns a non-zero period into a cycle: 032's surface
criterion, or its family form at the end of 2.4.

**Gate.** A period whose non-vanishing follows from a sign, for classes with non-CM sources (the gate of Route 1),
or a uniform object (the gate of Route 2).

**First test (the sketch's test a).** On E^k, E = C/Z[ω], the bundle ⊗ P_{i,i+1} of step 3 has first Chern class
the path form, whose matrix is the adjacency matrix of a path with k vertices (eigenvalues 2cos(jπ/(k + 1)),
determinant ±1 for k even and 0 for k odd). So it is non-degenerate exactly for k even, with index k/2 and Euler
characteristic ±1: its only cohomology is one class in degree k/2 (proved; Mumford's index theorem). Composing the
kernels along the path is the (k − 1)-st power of the Fourier–Mukai transform, which is "Parseval". Check that the operators
of the count are words in multiplication and Fourier transform, that is in the group U(1,1)(Z[ω]) of derived
autoequivalences of E (Mukai, Orlov, Polishchuk; from memory), and that the sign in footnote 3 is the parity sign.
Then the answer to (a) is: not the Hodge–Riemann sign.

### Route 4. Integral structures (division, divided powers, Fourier)

- The division of Route 2 is an integral Hodge statement along an isogeny tower. Alpöge's steps 9, 10, 14, 15, 18
  are integral statements about theta lifts: divisibility of the iterated lift (10), the need for a division (14),
  an integral structure glued across Hecke characters to take a gcd (15), the index of theta series (18). His
  steps 11 and 19 choose an Iwasawa tower; the tower of Route 2 is the ℓ-power Hecke orbit of a CM point.
- What we have: H8 (12 Nov): integral hard Lefschetz on Λ^*(Z^{2n}) is Wilson's diagonal form; the minimal class
  θ^{g−2}/(g − 2)! gives cokernel Z/(g − 1) from H² to H^{2g−2}. It is the correct integral form of cote 16 no 7:
  with Λ₀ the contraction, Λ₀²L₀² = 4 on H⁰ for n = 2, so Z[L₀, Λ₀] is not the ring of matrix units his basis
  describes (proved; two lines). H7: the compatibility left open in cote 47. RESEARCH_SA06 C.4a–x: denominators of
  Lefschetz inverses through the unimodular Poincaré bundle on A × Â (C.4j, C.4n, C.4p checked by the intake). The
  integral Hodge conjecture for one-cycles is equivalent to an integral Fourier transform (Beckmann–de Gaay Fortman,
  from memory).
- **Proposed (mine).** Alpöge's divisibility of the m-fold lift is the automorphic counterpart of the integrality
  of the divided powers θ^m/m!. Evidence: the Fourier transform exchanges θ^k/k! and θ^{g−k}/(g − k)! (Beauville,
  from memory), and the formal-group statement of suggestion 2 has the same m! against a·p/(p² − 1).
- **Proposed (mine).** The theta series' index of step 18 equals, up to explicit factors, the index of the span of
  basic-locus cycles in the integral Tate classes of the special fibre (1.3). For n = 2 this is Emerton's theorem on
  supersingular points and weight-two forms (from memory).
- Gate: the integral form of 1.7. First test: n ≤ 6 Smith normal forms (already in the prompt LEFSCHETZ_RINGS).

### Route 5. The CM test bed: what becomes unconditional in our own files

- **Motives.** For CM abelian varieties Grothendieck's motives (algebraic cycles) and Deligne's (absolute Hodge
  cycles) now agree; over finite fields the motives of abelian varieties satisfy B (Lieberman), the Hodge standard
  conjecture, D and Tate (032, Cor. 8.3 and 8.4, read).
- **Rows of RESEARCH_SA06 stated "under Tate" or "under the standard conjectures"** become theorems for abelian
  varieties: C.2c (A and positivity give D), C.2h, C.2j (integrality, functional equation, absolute values,
  semisimplicity from the standard conjectures), C.3ac (already written "under the cited 2026 CM-Hodge theorem"),
  D.4f (spectral effectivity equivalent to Tate), E.2a (effectivity as slope half-spaces, "motivic effectivity
  under Tate"). The transfers need checking row by row.
- **Effectivity (cote 14 scan 9; E.1a–e; hunch c14a-H1).** 032, Lemma 8.1 and Cor. 8.2 (read): a simple CM Hodge
  structure W of weight k with least Hodge index r₀ is a quotient of H^{k−2r₀}(B)(−r₀) for a CM abelian variety B,
  and a Hodge substructure W of H^k(A) with W(r) effective is supported in codimension r. So for CM motives
  effectivity is read from the Hodge types, which is the CM case of the cone question of 14:9.
- **Cote 15 scans 100–106 ("Conjecture forte", B.1a).** Unchanged (Honda–Tate); now each Weil number comes with Tate
  for its abelian variety.
- **Periods (cote 18 scans 11, 13; RESEARCH_SA07 A.2–A.4).** For CM abelian varieties the period relations of
  Shimura and Deligne now come from cycles; Grothendieck's "transcendance forte" in the CM case is the bare
  statement trdeg = dim of the Mumford–Tate torus.
- **The Fermat tower (LM7).** Fermat Jacobians have CM by abelian fields. There 032 gives Hodge on all powers,
  Colmez's formula is a theorem (Colmez, Obus; from memory) and its L-values are Dirichlet, so Alpöge gives Faltings
  heights up to O(log log); the periods are Beta values; and the Galois action on the meta-abelian quotient of the
  tripod group is given by Jacobi sums (Ihara, from memory), which are the Hecke characters of this route. The
  hexagonal curve of step 3 is the Fermat cubic, level 3 of the tower.
- Gate: Beilinson–Bloch for CM motives. First test: Ceresa-type cycles on Fermat Jacobians.

### Route 6. What GRH itself supplies (support only)

- By Alpöge, unconditional: no exceptional zeros of Dirichlet L-functions, so L(1, χ_d) ≥ c/log log |d| effectively
  and h(−d) ≥ c′√|d|/log log |d| (Littlewood's conditional bounds, from memory); sharp sizes of CM periods and
  heights for abelian CM fields (SA07 intake §4.1 has the elliptic case); effective lower bounds for Galois orbits of
  CM points on products of modular curves. The André–Oort statements once proved under GRH for imaginary quadratic
  fields are already unconditional by other means.
- **Conditional (Masullo):** effective Chebotarev for every number field; GRH for the Dedekind zeta functions of CM
  fields, the hypothesis of the first proofs of André–Oort (from memory); the sign statements of 3.5.
- None of this enters the gates of Routes 1–3.

---

## 4. The starting sketch, point by point

0. Shape: right about the edge; corrected in section 1 (central line against central point; what the pole count
   does and does not see).
1. CM test bed: right, with two corrections (section 2).
2. From CM to all: the gate "are the degrees bounded" is the right one, and 2.1–2.3 make it exact; Colmez's heights
   do not bound degrees; the variational step is also implied by the Lefschetz standard conjecture for abelian
   schemes over curves (André 1996, from memory). New: 2.2 (one point suffices; division on a Hecke orbit), 2.4,
   2.5–2.6.
3. Positivity backwards: for Λ the answer is Grothendieck's (3.2): no. But 032's own non-vanishing is a positivity
   argument (3.1), and on abelian varieties Λ is the Fourier conjugate of L (3.3).
4. Theta lifts make cycles: this is literally the mechanism of 032, which cites Kudla–Millson and
   Bergeron–Millson–Moeglin (1.1). Test (b) is T4, undecided.

## 5. Where the programme touches the Hodge conjecture

| place | what is there | meets |
|---|---|---|
| cote 16 scans 14–18 | no 7: Φ₀ = Z[L₀, Λ₀] on ΛM₀, "(sur Z !)"; "anneau de correspondances Lefschetzien" | 3.3, Route 4; H8; R1 of the war game |
| cote 16 scan 40 | Λ_Y = φ^*Λ_X²φ_*; the evanescent part E^{n−1} | 3.2 |
| cote 16 scans 44–50 | letter to Coates, 4.1.67: index conjecture, A, A′, A″, C; semisimplicity; Weil from C and A | section 1, 3.2 |
| cote 44 scans 2, 4, 6 | Th. 1–7: P^i(X), duality, Th. 4 "Hodge", Th. 5 "Néron", Th. 6 "Lefschetz", Th. 7 "Matsusaka" | 3.4, 3.5; H9 |
| cote 44 scans 8–9 | letter to Serre, 12.8.1964: Hodge positivity reduced to a polarization | 3.4 |
| cote 47 scans 3, 5–9 | the Fourier transform on abelian schemes (not reread today) | 3.3, Route 4; H7 |
| cote 54 scans 5–7 | p-Lie algebras, universal vector extension (not reread today) | 1.6; suggestion 2 |
| cote 14 scan 9 | effectivity structures as cones; the saturation question | Route 5; E.1a–e |
| cote 14 scans 38–39 | Th. 3.1; "A-t-on une réciproque" | E.3b, E.3e; E.3u, E.3c (no over C) |
| cote 14 scans 44–47 | the letter's A, A′, A″ modulo algebraic equivalence | C.1a–e (they fail) |
| cote 15 scans 100–106 | "Conjecture forte" on Weil numbers | B.1a; Route 5 |
| cote 18 scans 11, 13, 36–38 | period conjecture; Hodge splitting; real Frobenius | SA07 A.2–A.4, C.3.1; Route 5 |
| cote 1 sheets 79–80, 111–112 | RH as positivity of an operator (the main session's intake; not read by me) | 3.3 |
| LM7 | the Fermat tower; frames at the harmonic and equianharmonic points | Route 5; suggestion 1 |
| RESEARCH_SA06 | C.1j, C.1o, C.1p, C.2c, C.2h, C.2j, C.2k, C.3a–d, C.3h, C.3l, C.3ac, C.4a–x, D.4d, D.4f, E.2a, E.3 | Routes 3–5 |
| RESEARCH_SA07 | A.4.2–A.4.9, F.3.21–F.3.22 (CM periods, the Jacobian of y² = 1 − x⁵) | Routes 5, 6 |
| war game of 12 Nov | H7, H8, H9; R1 | Routes 3, 4 |

SA06 and SA07 are the Pro runs as their intakes of 20 Nov record them; row statements are quoted at the level the
intakes give.

## 6. The suggestions of 20 November, carried further

- **Suggestion 2** (divided powers of a formal group of height 2): now tied to Gross's quasi-canonical liftings and
  to the Kudla–Rapoport multiplicities (1.6).
- **Suggestion 3** (the count as moments of "multiply, then Fourier"): the words are words in the Weil
  representation; for Gaussian weights they are elements w·u(a₁)·w·u(a₂)⋯ of SL₂ and the path form with diagonal
  terms is the tridiagonal form whose determinant is a continuant (elementary); on E^k they are Fourier–Mukai words
  (first test of Route 3). The proposal about cote 1 is unchanged and untested.
- **Suggestion 4**: corrected in 3.6; its Arakelov part is 3.5.
- **Suggestion 6**: the identification of the SL₂ of the lift chain with the Lefschetz sl₂ is Arthur's principle
  (1.4); what remains proposed is the comparison of step 10 with Wilson's form (Route 4).
- **Suggestions 1, 5, 7, 8, 9**: unchanged. For 1, note that C/Z[ω] is the Fermat cubic (Route 5).

## 7. Research prompts for ChatGPT Pro, ranked (one line each)

1. **THETA_THREE_SIGNATURES.** Set 032 §§4–6 beside the theta-lift statements of Alpöge's archive (paths from the Lean map); prove or refute 1.7; decide whether 032's non-vanishing has an explicit lower bound.
2. **HECKE_DIVISION.** Prove 2.1–2.4 in full; carry out T5 on the fourfolds isogenous to E⁴, E = C/Z[ω], from Markman's construction; then decide bounded division on the Hecke orbit of E⁸.
3. **GHOST_CLASSES.** Prove 2.5; check 032's Remark 8.5 with its CM transport; carry out T9; for the Weil class of T5 compute the least complexity of t_v at supersingular and at ordinary primes as a function of v.
4. **JACOBIANS_1964, revised.** Prove 3.4 (Th. 4 for abelian varieties in every characteristic) and H9 (a), (b); prove the arithmetic sibling 3.5 with its sign against Th. 5.
5. **DEGREES_ARE_L_VALUES.** T6 and T7: the degree of the 032 cycle by the Rallis inner product formula; semiregularity of the 032 surface.
6. **QUASI_CANONICAL_MULTIPLICITY.** Decide 1.6 against step 2 of the Lean; give the statement for formal groups of height h and its Kudla–Rapoport form.
7. **LEFSCHETZ_RINGS, revised.** The integral form of cote 16 no 7 (H8 (i)–(iv)); the Howe-duality statement of 3.3 for every Albert type; the two proposals of Route 4.
8. **N_BALL_RELATIONS.** T3: realize 2n-factor relations by n-ball quotients and compare degrees with the four-factor route.
9. **CM_TESTBED_TRANSFER.** Go through the rows of Route 5 and prove each transfer to an unconditional statement for abelian varieties, or say exactly what blocks it.
10. **FERMAT_TOWER_CM.** Hodge classes on powers of Fermat Jacobians against 032; heights by Colmez–Obus with Alpöge; the dictionary with Ihara's power series; Ceresa cycles and the central point.
11. **PATH_BUNDLE.** The first test of Route 3 on E^k, with the sign identified.

## 8. Literature cited from memory (to verify before use)

Tate 1965 (poles); Pohlmann 1968; Lieberman 1968; Kleiman 1968, 1994; Deligne 1982 (absolute Hodge); André 1996
(motivated cycles); Cattani–Deligne–Kaplan 1995; Milne 1999, 2002, 2009; Mukai 1978, 1981; Beauville 1983;
Künnemann 1993, 1996; H. Saito 1979; Looijenga–Lunts 1997; Golyshev–Lunts–Orlov 2001; Orlov 2002; Polishchuk 2003;
Howe (dual pairs); Arthur 1989; Rogawski 1990; Murty–Ramakrishnan 1992; Blasius–Rogawski 1992; Kudla–Millson;
Bergeron–Millson–Moeglin 2016; Gross 1986; Gross–Keating 1993; Kudla–Rapoport 2011, 2014; Li–Zhang 2022; Li–Liu
2021; Vollaard–Wedhorn 2011; Xiao–Zhu 2017; Emerton 2002; Colmez 1993; Obus 2013; Gillet–Soulé 1994;
Bloch–Esnault–Kerz 2014; Buchweitz–Flenner 2003; Beckmann–de Gaay Fortman 2023; Tsimerman 2018 and
Pila–Shankar–Tsimerman 2021 (André–Oort); Littlewood 1928; Ihara 1986.

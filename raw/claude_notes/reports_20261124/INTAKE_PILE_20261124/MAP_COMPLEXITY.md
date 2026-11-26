# MAP_COMPLEXITY: connection map of the complexity region (intake pile of 24 Nov 2026)

Written 24 Nov 2026, about 21:30-22:30 UTC, by Claude Opus 5.5 at effort max (agent a4348514ce0275bbf), for the main session 329fb1e6
(Claude Opus 5.5 at effort max), following `MAP_BRIEF.md`. This is the region GCT and VP/VNP: the cluster GCT, the
COUNTING_VARIETIES and SPLIT_ZERO_AFTER_FGJM parts of AG_POLISH, the two VP ≠ VNP preprints, our runs on them (98 and 99), and
outside complexity results with links to representation theory and algebraic geometry. The links are in `MAP_COMPLEXITY.tsv`
(ids L01–L46). The checks I made are in `MAP_COMPLEXITY_CHECK_EVENTS.tsv` (ids CE-1 to CE-9).

**Abbreviations used here and in the TSV**

| Short | Path |
|---|---|
| RR | `<local>/Documents/grothendieck_archive_transcription_20261110/research_returns` |
| 98 | `RR/VPVNP_HINGE_checkpoint_02_20261124T2129Z_unzipped`: run 98, GPT-6 Astra (ChatGPT Pro mode), report marked INCOMPLETE |
| 99 | `RR/VPVNP_WIRE_GEOMETRY_checkpoint_01_20261124T2146Z_unzipped`: run 99, GPT-6 Astra (ChatGPT Pro mode), checkpoint 01 |
| PILE | `<local>/Documents/reports_20261124/INTAKE_PILE_20261124` |
| FM | `<local>/pequalnp_work/fleet_map` |

The rest of the shorthand:
- **OAI** is OpenAI's "VP and VNP are different" (`openai/math`, `preprints/VP-and-VNP-are-different-November-23-2026`,
  `build/Paper.tex`).
- **ANT** is Anthropic's "VP ≠ VNP over every field" (`anthropics/formal-math/vp-vnp`; hexagon:2611.00954). It was found by
  an internal research Claude model; Anthropic names no model and no effort setting.
- **Liu-NC** is hexagon:2611.00994v1 and **Liu-AR** is hexagon:2611.00972v1, both by Yilin Liu (24 Nov). Each post's
  provenance statement says an OpenAI model produced it, and neither gives an effort setting. Both posts are marked
  "Primarily AI-generated text; Human understanding: no parts". I fetched their TeX sources, and the line numbers cited
  are lines of those sources.

**The standing hypothesis (H_A).** ANT's Theorem A.6 (cover duality) and Proposition C.3 (a CAT(0) embedding of prices).
Runs 98 and 99 state their price equivalences under these two results.
- Run 99 has reconstructed A.6 (Q1c-1). Its audit of Appendices C and D is still running (Q7b).
- A "price" is in the sense of ANT's Definition A.4.
- Throughout, C_r is the planar crossing tensor: binary strings a, b, c, d of length r placed at e₁, e₂, −e₁, −e₂ of the unit
  disc, with indicator [a = c][b = d]. It is OAI's C_{D,m} at D = 2, m = r.

**No source here is refereed.** Except where a row says otherwise, the statements below are claims of unrefereed preprints or
of our runs. "Run-only" means the run's own checks, and no other model has checked it.

---

## 1. New knowledge, ranked by usefulness

### NK-1. One four-point metric decides which strong lower bound holds

**Statement.** Fix a characteristic and an algebraically closed field K of it, and assume (H_A). Three conditions are
equivalent:
- **(a)** some crossing tensor C_r has a strict shortening over K, in OAI's Definition 2.1 with D = 2;
- **(b)** the four vertices of the Euclidean unit square, with their Euclidean distances, are not a price over K;
- **(c)** every price over K is a tree pseudometric.

Conditionally on the sources named in each case, the two possibilities give the following.

- **The tree world, where (a)–(c) hold.**
  - OAI's stretch theorem, in its planar instance, gives an explicit homogeneous family f_j in commutative VNP whose
    degree-j border circuit size exceeds 2^{j^σ}. Liu-NC cites this theorem as [OpenAI, Theorem 3.1]; my notes of 24 Nov
    record it as Theorem 1.3 of OAI's introduction.
  - Liu-NC: the row-ordered noncommutative Perm_n and Det_n have border size greater than 2^{n^δ}, over every field.
  - 98 PG-TREE-CONTRACTION gives explicit contraction (n = 4, s = 15/8). In ANT's contracting case that yields
    2^{Ω((log m)²/log log m)} (98 report, "Conditional consequences").
- **The non-tree world, where (a)–(c) fail.**
  - Liu-NC: log₂(s + 1) ≥ n/2 − O(√(n log n)) for the noncommutative Perm_n and Det_n.
  - Over C, the sums-of-squares function satisfies R(q) = q^{√2+o(1)}. R(q) is the least R with
    (Σ_{i≤q} a_i²)(Σ_{j≤q} b_j²) = Σ_{ℓ≤R} B_ℓ(a,b)², the B_ℓ complex bilinear. The lower bound is from Liu-NC, "Two
    crossing cuts"; the upper bound is Khoruzhii's, as Liu-NC cites it.
  - Every finite planar Euclidean metric is a price (98).
  - Flatness in dimensions D > 2 stays open (99 Q1d-7).
- **A classical one-sided witness.** Suppose that over C, for some r ≥ 2, there is a sums-of-squares formula with q = 2^r
  and ⌈log₂ R⌉ < √2·r − 2√(2r). Then (a) holds over C, and every price over C is a tree.

**Proof.**
- **(b) ⇔ (c).** This is 98's square statement: the square is a price iff some non-tree price exists. See the report's Q2
  rows and `98/price_geometry.tex` l.166 (PG-FOUR-CONDITIONAL).
- **(a) ⇔ (b).** 98 PG-CROSSPOLY-GATE (`price_geometry.tex` l.583) at D = 2 states a three-way equivalence: there is no
  strict shortening at D = 2, iff the square with its centre (the 2-cross-polytope with centre) is a price, iff every
  finite planar Euclidean configuration is a price.
  - If there is no shortening, the square is a planar configuration, so it is a price.
  - If the square is a price, every finite planar Euclidean metric is a price (98, Q2 square row; 99's ledger at 22:14
    Berlin: "square-plus-centre reduced to square"). The centred square is one of them, so there is no shortening.
- **Liu-NC's hypothesis is our (a).** Liu-NC's "planar crossing admits a strict shortening" (TeX l.74) is exactly (a). I
  checked the definition against OAI Definition 2.1 (CE-1).
- **The witness** is the contrapositive of Liu-NC's two-cut inequality. That inequality reads ⌈log R⌉ ≥ √2 r − 2√(2r)
  when no planar shortening exists over C. Liu-NC derives it from the polarization identity
  2⟨a,c⟩⟨b,d⟩ = Σ_ℓ (B_ℓ(a,b)B_ℓ(c,d) + B_ℓ(a,d)B_ℓ(c,b)).
  - I re-proved that identity (CE-2).
  - Its two sums have rank at most R across the cuts ab|cd and ad|bc.
  - On basis vectors of C^{2^r} the left side is 2·C_r.

**Status.**
- I checked the chain step by step against the cited statements (CE-3, CE-4).
- 98's statements are run-only, with 98's in-run checks.
- Liu-NC and OAI are unrefereed.
- **The same result twice.** Run 98's RT-SOS ("a complex sums-of-squares exponent below √2 would suffice";
  `98/root_route_audit.tex` l.179) is the contrapositive of Liu-NC's two-cut inequality. The two were obtained separately.
- Run 98's RT-SOS-UPPER ("checked identity reaches √2") runs parallel to Khoruzhii's upper bound. That source is cited by
  Liu-NC; I have not opened it.

**Why it matters.**
- Both VP ≠ VNP proofs leave a hinge open, and Liu's new noncommutative theorem splits on that same hinge. The hinge is now
  one question about one four-point metric.
- If the sources hold, either branch gives a major result:
  - either an explicit commutative VNP family needs 2^{j^σ} border gates;
  - or the classical Hurwitz / Hrubeš–Wigderson–Yehudayoff sums-of-squares exponent over C is exactly √2. That is
    superlinear, and HWY (JAMS 24, 2011) connect a superlinear bound to exponential noncommutative circuit lower bounds
    (recalled, not reopened).
- It also tells runs 99 and later exactly what to attack: the square, nothing larger.

### NK-2. A strict shortening is exactly a failure of flatness; the two runs disagree on one direction

**Statement.**
- **(i) Forward.** Over every field, a strict shortening of some C_{D,m} implies that ANT's flat hypothesis fails, at every
  scale.
  - The sources are 98 SH-02, SH-03 and SH-10 (`98/shortening.tex` l.168, l.207, l.14) and 99 Q3a.
  - The mechanism is a terminal-selector inequality. Run 99 identifies it with ANT's Lemma E.7.
- **(ii) Converse.** Under (H_A), nonflatness implies a strict shortening (98 SH-08, l.417–432).
  - The proof uses 98's Cor. ball-price, ANT Prop. C.3, and a rigidity lemma. The lemma: a 1-Lipschitz map from a Euclidean
    ball into a CAT(0) space that saturates the coordinate diameters is an isometry on a smaller ball.
  - Run 99, which started at 21:02 UTC before 98 returned at 21:29 UTC, still lists this converse as OPEN (Q3b).
- **(iii) Contraction.** With ANT's alternative Theorem D.2, a strict shortening implies the contracting hypothesis (98
  SH-09, 99 Q3c).
  - "Shortening ⇔ contracting" is equivalent to flat and contracting excluding each other.
  - This step uses ANT's Theorem D.2, so it is not an independent derivation of ANT's dichotomy.

**Consequence.**
- OAI's "saving" case is ANT's nonflat case, and it lies inside ANT's contracting case.
- The two papers' dichotomies coincide exactly when no field is both flat and contracting. ANT, Section 2: "nor do we show
  that the two are mutually exclusive."

**Status.**
- (i) is proved by two runs that agree.
- (ii) is from 98 only, and conditional. I read SH-08's proof as written (CE-5).
- (iii) is conditional on ANT D.2.

**Why it matters.**
- It settles the nesting question that our 24 Nov integration left open.
- It corrects our own files, one of them public (§2.6).
- The conference has to hand 98's SH-08 proof to 99's successor, which otherwise attacks a converse already proved under
  (H_A).

### NK-3. What a GCT certificate of the claimed separation must look like

**Statement.** Assume OAI's Corollary 1.2 in characteristic 0, with its constant c₀ and onset m₀. Let m ≥ max(m₀, 17), and
let n satisfy 2m² − m + 1 < n² and n ≤ exp(c₀(log m)^{5/4}). Then:
- **(a)** z^{n−m}·per_m ∉ \overline{GL_{n²}·det_n} (OAI Corollary 1.2);
- **(b)** some homogeneous highest-weight vector in the ideal of \overline{GL_{n²}·det_n} is nonzero at some point of the
  orbit of the padded permanent. This is 99 Q6e, proved conditionally by the run; it adds that "No occurrence or
  multiplicity mismatch follows merely from noncontainment";
- **(c)** there is no four-row multiplicity obstruction. CUE_GCT R-27 with G-20: four-row gaps exist exactly when
  n² ≤ 2m² − m + 1;
- **(d)** if moreover n ≥ m^c, there is no multiplicity obstruction with at most 2c + 1 rows (GCT_KRON M-008);
- **(e)** if n > m^{25}, there is no occurrence obstruction at all (Bürgisser–Ikenmeyer–Panova, J. Amer. Math. Soc. 32
  (2019); recalled, not reopened).

So in the polynomial range m^c ≤ n ≤ poly(m), if the claim holds, the separation is true. Its only representation-theoretic
certificates are then of two kinds:
- multiplicity obstructions with more than 2c + 1 rows;
- separating highest-weight equations that are not multiplicity mismatches.

**Status.**
- This is a combination.
- R-27/G-20 are proved by the run only. M-008 is at statement level for the intake.
- I checked the threshold arithmetic from R-14 (CE-6).
- OAI is unrefereed. Run 99's Q6 rows are conditional on OAI's constants.

**Why it matters.**
- It turns the cluster's "witness desert" (GCT.md item 3; H14) into a precise target.
- It is the honest answer to "what does VP ≠ VNP give GCT": the GCT target, and no obstruction of a kind GCT currently
  constructs.

### NK-4. The two exponents, 4/3 and 5/4, come from two ways of accounting for the cost

**Statement.**
- The direct (flat) case of both arguments gives lower bounds exp(Θ((log m)^κ)).
- **Orthogonal-edge (equal-width) accounting allows κ ≤ 5/4, attained in the model.** OAI's bound has exactly this
  exponent.
- **Charged cube-selector accounting, or two-hub binary-selector accounting, allows κ ≤ 4/3, attained in the model, up to a
  logarithmic factor in 98's form.** ANT's bound has exactly this exponent: m^{c(log m)^{1/3}} = exp(c(log m)^{4/3}).
- Fixed-size seed extensions cannot raise the power (98 EX-20).
- Beating 4/3 needs a new naming scheme or geometry (99 Q5c; 98 Q3 row).

**Status.**
- Two runs agree: 98 EX-19 and EX-20 (`exponent_audit.tex` l.563, l.761), and 99 Q5a and Q5b.
- Run 99 checked OAI's direct geometric step, with no fault found (Q7c).
- My re-derivation of OAI's 5/4 on 24 Nov gives the orthogonal-edge value (CE-7):
  - selection ≍ d² ≤ m = c·log n, so d ≍ √(log n);
  - the gain is ≍ m√d, so the exponent is (log n)^{5/4}.

**Why it matters.** It explains the 1/3 against 1/4 difference between the two preprints. The difference comes from how
each argument counts its cost, so it is no disagreement. It also fixes where any improvement has to come from.

### NK-5. Moment-polytope spectral points give only tree prices; the flat world needs points beyond them

**Statement.** Take the named families of spectral points that run 99 classified. On wire tensors they give exactly
clustered-star and tree pseudometrics:
- quantum functionals, which come from moment polytopes;
- their enlarged-party singleton points (Q1d-1, Q2a) and laminar extensions (Q1d-2, Q2b);
- by Sakabe–Doğan–Walter (arXiv:2601.21553v2, Theorem I.1: Strassen's support functionals coincide with the quantum
  functionals), the singleton support candidates as well (Q1d-6).

Run 99 also evaluates the 2026 edge support points of Alman–Li–Pratt and singleton-anchor interpolation. I have not seen
whether its classification covers these two.
- These metrics lie at sup-norm distance exactly (√2 − 1)/2 from the square and from the centred square (99 Q2c).
- Every tree pseudometric is a price (98 PG-TREE-ALL, `price_geometry.tex` l.669).
- So, by NK-1, if the square is a price, the witness is a spectral point outside every family that moment polytopes give.
- Two candidates that would fit the square's wire values are excluded:
  - Botero–Christandl–Fraser–Leigh–Nieuwboer (arXiv:2604.18283v2) excludes every nonsingleton lower quantum functional
    (99 Q1d-3);
  - an exact S₄ projector computation excludes the ordered upper candidate (99 Q1d-4).

**Status.**
- This combines run statements: 99's are run-only, 98's run-only.
- The three 2026 papers were read by run 99, not by me.

**Why it matters.** This is the concrete bridge between the VP/VNP price machinery and GCT's representation theory.
- Quantum functionals depend on a tensor only through its moment polytope. The moment polytope records which irreducibles
  occur in the coordinate ring of the orbit closure: GCT's occurrence data.
- On the GCT side, occurrence obstructions are known not to suffice (BIP 2019; NK-3(e)).
- On the price side, occurrence-level points give only trees.

In both settings the remaining question lies beyond which representations occur.
- On the GCT side it is multiplicities.
- On the price side it is spectral points that no moment polytope gives.

This is an analogy, not a theorem. It makes a good conference topic (§4, T3).

### NK-6. The coherent Frobenius count is a height test for Artin–Mazur formal groups

**The setting: CV-THM-MAIN (COUNTING_VARIETIES cp01, checked by the AG_POLISH intake).**
- Take a prime p and a CNF formula φ with S solutions.
- The construction gives a smooth, geometrically integral, circuit-presented hypersurface X_φ ⊂ P^{d−1}_{F_p}.
- ω ≅ O on X_φ, and H^{d−2}(X_φ, O) is a line.
- Frobenius acts on that line by S mod p.
- Deciding that this scalar is nonzero is Mod_pP-complete, and nonvanishing is equivalent to Frobenius splitting
  (CV-PROP-SPLITTING).

**Statement (d − 2 ≥ 1).**
- The Artin–Mazur formal group Φ = Φ^{d−2}(X_φ, Ĝ_m) is a one-dimensional formal group over F_p.
- **height(Φ) = 1 iff S ≢ 0 (mod p).**
- Hence deciding whether the Artin–Mazur formal group of a circuit-presented smooth Calabi–Yau hypersurface has height 1 is
  Mod_pP-complete. For prime p, Mod_pP is closed under complement, so deciding "height ≥ 2" is Mod_pP-complete too.
- In Stienstra's formal group law for X_φ, the p-th logarithm coefficient is the coefficient of (x_1⋯x_d)^{p−1} in F^{p−1}.
  It is ≡ S (mod p), up to the run's sign convention.

**Proof.**
- **Φ is one-dimensional.** H^{d−3}(X, O) = 0 for a hypersurface when d − 3 ≥ 1, and H^{d−2}(X, O) is a line. So Φ is
  pro-representable of dimension one (Artin–Mazur). For d − 2 = 1 it is the formal Picard group.
- **Height 1 is the Hasse–Witt test.** For such a Φ, height 1 is equivalent to Frobenius being nonzero on H^{d−2}(X, O),
  which is the Hasse–Witt scalar.
- **Conclusion.** CV-THM-MAIN identifies that scalar with S mod p.

**Status.**
- The deduction is mine and short (CE-8).
- The classical inputs (Artin–Mazur, Ann. Sci. ENS 1977; Stienstra, Amer. J. Math. 1987) are carried as background. I did
  not reopen them; theorem locators are still to be filled.

**Why it matters.**
- It places COUNTING_VARIETIES in Grothendieck's crystalline frame. The height is the first slope of the F-crystal
  H^{d−2}_cris (Barsotti–Tate groups, Dieudonné theory).
- It connects to DP_MULT, the GCT cluster's formal-group run. When S ≡ 0, the height is ≥ 2, and DP1/DP3/DP34 (valuations of
  invariant derivatives at height h) apply to Stienstra's law of X_φ.
- **Next question (a prompt candidate).** For S ≡ 0 (mod p), does the next test (a_{p²}, or the second Hasse–Witt step)
  encode a further count? If it does, height ≥ 3 would be hard for a second-order counting class.

---

## 2. Outside results that change our items

### 2.1 Liu, hexagon:2611.00994 (noncommutative permanent and determinant), 24 Nov

**What it does.** It turns our hinge into the case split of a theorem: L05, NK-1.

**What it changes.**
- **98 Q1a and 99 Q1.** Deciding the square now decides which of two proved noncommutative bounds holds, beyond which
  VP ≠ VNP consequence holds.
- **98 RT-SOS.** Liu proves the same statement from the other side (L06).
- **Our joint lemma space and the public mirror's open question.** The wire geometry now has a third paper depending on it.

**Bibliography.** It cites OAI at commit f5702854 (Definition 2.1, Theorem 3.1), Hrubeš–Wigderson–Yehudayoff, Nisan, and
Shastri–Willumsgaard (a quadratic noncommutative circuit bound, arXiv 2604.20575). It also cites two Lemmata pieces by
Khoruzhii.

### 2.2 Liu, hexagon:2611.00972 (asymptotic tensor rank), 24 Nov

**What it does.** It applies ANT's price machinery outside VP/VNP: ANT Definition A.4, Theorem A.6 and Proposition A.7,
from Appendices A and C.
- A relaxed spectral point has a wire pseudometric (TeX l.57–73).
- That pseudometric is realized in a complete CAT(0) space.
- After midpoint insertion it is a price.

**The results.**
- Asymptotic rank ≤ d^{ω/√3} for local ranks ≤ d (answering Alman–Li).
- The asymptotic rank equals the largest local rank D when the other two are at most D^{√5/4}.
- In odd order 2m + 1 the worst-case exponent is m + O(m^{−1/3}).
- arank(T ⊗ E_q) = q(M(T) + o(1)), where M(T) is the largest flattening rank.

**What it changes.**
- **98 R2/R5 and PG-BUILDING.** It confirms CAT(0) realization as a necessary property. 98 already proves that this
  property alone is not enough.
- **A single point of failure.** ANT's Appendices A and C are now load-bearing for four bodies of work: ANT itself, runs 98
  and 99, and Liu-AR (L15). An error in A.6, A.7 or C.3 would hit all four at once.
- **Our border-rank items.** A border-rank/asymptotic-rank comparison becomes possible (L30, a candidate).

Run 99 read Sections 2–4 (99/LITERATURE.md l.28).

### 2.3 The 2026 spectral-point papers that run 99 read

- **Sakabe–Doğan–Walter (arXiv:2601.21553v2):** support functionals = quantum functionals.
- **Botero–Christandl–Fraser–Leigh–Nieuwboer (arXiv:2604.18283v2):** quantum functionals for higher-order tensors. Nonsingleton
  lower quantum functionals are excluded.
- **Alman–Li–Pratt (arXiv:2604.01386v2, Cor. 8.10):** edge support functionals.

**What they change: our "Fact 2" and finding 3 of 24 Nov** (FM/VPVNP_INTEGRATION_20261124.md). That finding said the
explicit spectral points over C are flattening ranks and quantum functionals, which give cut and star metrics. The current
statement is NK-5:
- the named families give clustered stars and trees;
- all tree pseudometrics are prices;
- the square sits at the exact distance (√2 − 1)/2 from all of them.

### 2.4 The two VP ≠ VNP claims and our GCT items (from my integration of 24 Nov)

- **Implied, if either claim holds** (L20, L21):
  - the fleet's L-gct-011 (Mulmuley–Sohoni), for every c;
  - L-gct-026 (cubic border dc) and L-gct-028 (border Mignon–Ressayre + 1), for m ≥ m₀ only, not for all m ≥ 3.
  - The public mirror has carried these marks since 24 Nov.
- **Unchanged as mathematics** (L25, L26):
  - every fixed-size item: GCT_KRON A-030 and F-025; GCT_OBS S-002/S-003, QC-014, QC-019, Q1a/Q1b; the fleet's L-gct-010
    and L-gct-006;
  - every positivity item: GCT_POS H02b and N-012; GCT_PLETH; GCT_NSRH.
- **GCT's own question gains precision** (NK-3). OAI itself says it gives "no explicit module of equations or
  representation-theoretic obstruction". Run 99's Q6e supplies the conditional separating highest-weight equation.

### 2.5 Matrix multiplication, ω ≤ 9/4 (OAI, 2 Oct 2026), as the 99 and Liu-AR bibliographies cite it

- It sits alongside Shpilka's exposition (ECCC TR26-281), Doğan–Lysikov–Sakabe–Walter (arXiv:2611.09716) and Baitian Li's
  semidirect sums (arXiv:2611.04175).
- It enters Liu-AR's d^{ω/√3}.
- It bears on 99 Q1b-6: matrix-multiplication savings do not exclude the square. My 24 Nov argument agrees: such savings
  cannot contradict flatness, because ω ≥ 2.
- It changes no GCT item directly. I opened none of these four sources.

### 2.6 Corrections that our own runs 98 and 99 make to our own files

1. **The scale bullet.** My 24 Nov integration stated λ ≥ (2Dm − w)/log₂A: "a shortening excludes flat realizations only at
   small scales".
   - Its scale direction is reciprocal (99/LITERATURE.md l.56; 99 Q1a-1).
   - The restriction to small scales is false: a shortening excludes flatness at every scale (98 SH-02/03/10; 99 Q3a).
2. **"Only flattening ranks and quantum functionals"** is incomplete (NK-5).
3. **R5 of our prompt.** The Euclidean assertion in R5 (Euclidean prices refute contraction) is false. Hilbert maps on
   Mat₂(F₂) satisfy the strict rank-step inequality with squared ratio ≤ 3/2 (98 PG-HILB2, `price_geometry.tex` l.405).
4. **"Neither nesting can be shown"** is now answered conditionally (NK-2).

**Where these sit.**
- FM/VPVNP_INTEGRATION_20261124.md: §1 item 1, l.54–56; §(b), l.150–157.
- The public mirror's `extension/EXTERNAL.md` (local copy `<local>/pequalnp_work/mirror/extension/EXTERNAL.md`),
  "What we observe", l.133–141:
  - "Only two kinds of metric over C" is incomplete;
  - "Flatness needs new points" should read: flatness needs a non-tree price, equivalently the square;
  - "Small scales only" is wrong in both direction and scope.
- Its list "The questions this leaves" should also record two things:
  - 98's reduction: the dichotomies coincide iff flat and contracting exclude each other;
  - NK-1: the square is the whole planar question.

**The mirror is public, and this job allows no git. This is flagged for the main session; I changed neither file.**

---

## 3. Links by theme

### 3.1 The wire-geometry hinge: runs 98 and 99, both claims, and Liu (L01–L14)

**The hinge in three equivalent forms.** OAI's question (is there a strict shortening?), ANT's question (flat or
contracting?) and the price question (which pseudometrics are prices?) are one hinge.
- **Shortening against flatness.** The forward direction is proved by two runs (L01). The converse is proved under (H_A)
  by 98 and is still open in 99 (L02).
- **Contraction.** It follows from shortening via ANT D.2 (L03).
- **The planar case** is NK-1 (L04, L05).

**Independent agreements.**
- 98 RT-SOS and Liu's two crossing cuts state the same thing (L06).
- 98 RT-SOS-UPPER runs parallel to Khoruzhii's upper bound (L07).
- 98 EX-07, 99 Q4e and Liu's Nullstellensatz remark agree: the hinge depends only on the characteristic (L09).

**The classical anchor.** Hrubeš–Wigderson–Yehudayoff's sums-of-squares link to noncommutative circuits (L08).

**Inputs to ANT's contracting case.**
- PG-TREE-CONTRACTION (L10).
- PG-HILB2 refutes a Euclidean shortcut (L11).

**Exponents** (L12, NK-4).

**An open candidate (L13).**
- 98 EX-21: the geometric mean of crossing cut ranks fails the spectral-extension hypothesis.
- Liu-AR l.69: Liu's extension, by a randomly assigned new party, is bounded by a geometric mean.
- The work needed: decide whether Liu's extension applies to the crossing-cut mean. If it does, it either contradicts EX-21
  or produces a non-tree price, which would settle the square.

### 3.2 A shared dependency: ANT's appendices (L14, L15)

| Result in ANT | Used by |
|---|---|
| Definition A.4 (price) | 98, 99, Liu-AR |
| Theorem A.6 (cover duality) | 98 SH-08, 99 Q1c-1 (reconstructed), Liu-AR l.121 |
| Proposition A.7 (spectral extension) | Liu-AR l.69 |
| Proposition C.3 (CAT(0) embedding) | 98 SH-08, 99 Q1 |
| Theorem D.2 (alternative) | 98 SH-09, 99 Q3c |
| Lemma E.7 (selector) | 99 Q3a |

- Run 99's audit of Appendices A and B: "PROOF_CHECKED_NO_FAULT" (targeted checks, not a full verification).
- Its audit of Appendices C and D is in progress.
- This list should go to whoever checks ANT next: a fault in C.3 would remove the converse of NK-2 and the equivalences of
  NK-1.

### 3.3 GCT obstructions and the claims (L20–L28)

- **What the claims imply.** The fleet's target nodes (L20, L21). Run 99's Q6 rows make the padding and border-dc
  translation explicit: Q6a, padding equivalence; Q6b, determinant circuits of size ≤ 8N⁴; Q6c–Q6d, conditional (m, N)
  ranges; Q6e, a separating highest-weight equation (L22).
- **The certificate question** is NK-3 (L23, L24).
- **What they leave unchanged** (L25, L26): the fixed-size and positivity items.

**Inside the cluster: GCT VIII corrections.** GCT_NSRH F57/F58/F67 and GCT_POS N-012 (H23) hit GCT VIII's positivity
statements at rank 4 from two sides (L27).
- The SPLIT_ZERO runs prepared a separate e-mail draft about GCT VIII's computer-check sentence.
- These are three GCT VIII points from three runs. They belong in one correspondence (L28; a candidate, nothing drafted
  here).

### 3.4 Asymptotic spectrum, moment polytopes and GCT representation theory (L16–L19)

- **NK-5** is the bridge (L16–L18).
- **The occurrence-level analogy (L19).**
  - Quantum functionals use the moment polytope, that is, which irreducibles occur.
  - GCT occurrence obstructions use the same data.
  - Both are insufficient for their target.

**Where it touches GCT_POS, GCT_PLETH and GCT_KRON.**
- Those runs compute multiplicities (Kronecker and plethysm coefficients, their quasi-polynomials and zeros) for orbit
  closures of the same kind whose supports define moment polytopes.
- The positivity failures (H02b: numerical PH3 fails; H23) concern those multiplicities.
- The price question needs spectral points beyond the supports.
- Neither side has yet produced a usable object beyond the support level: a non-tree price on one side, a large-row
  multiplicity obstruction on the other.

### 3.5 Border rank and asymptotic rank (L29–L31, L46)

- **The border-rank ladder.** det₄/per₄: ≥ 43 (BR_PENCIL; H03), ≥ 44 (GCT_OBS BR-006), ≥ 52 (BORDER_RANK thm:52) (L46).
- **Run 99 Q1b-7.** Border-rank and pencil methods certify fixed-layout limits. They do not bound the closure of the
  spectral cone, so on their own they cannot decide the square (L29).
- **Liu-AR's asymptotic-rank bounds.** Comparing them with our lower bounds would give a gap statement between border rank
  and asymptotic rank (L30). It needs the three-way format and the local ranks of BR_PENCIL's tensors.
  - Liu-AR's own example: every 64×10×10 tensor of first local rank 64 has asymptotic rank 64, while a generic one has
    border rank ≥ 79.
- **Matrix multiplication** gives no route to the square (L31).

### 3.6 Counting complexity and coherent Frobenius (L32–L34)

**NK-6** (L32).

**CV-THM-MAIN and Valiant's VNP pattern (L33).**
- The Hasse–Witt scalar is the coefficient of (x_1⋯x_d)^{p−1} in F^{p−1}. Compare perm(A), the coefficient of x_1⋯x_n in
  Π_i Σ_j a_ij x_j.
- In CV the hardness lives in the circuit presentation of F: for p = 2 the scalar is a single coefficient of F.
- The algebraic VP ≠ VNP claims give no Boolean hardness for CV. The known transfer runs from Boolean hypotheses to
  algebraic ones over finite fields (Bürgisser's completeness theory; recalled, not reopened).

**Characteristic 2 (L34).**
- The permanent equals the determinant there, so ANT covers the permanent only for p ≠ 2. It uses the Hamiltonian-cycle
  polynomial for every field. Run 99 records the char-2 square question as open (Q4d).
- CV's scalar stays Mod₂P-complete at p = 2: the geometric invariant does not collapse where the permanent does.

### 3.7 Boolean circuit lower bounds for the fleet: SPLIT_ZERO paper 4 (L35–L37)

- **L-meta-647.** Both runs prove the fleet's conjecture as thm:onesided (L35). Our own partial proof of 23 Nov is
  `<local>/pequalnp_work/L_meta_647_PARTIAL_PROOF.md`.
- **L-meta-612 and L-meta-608** (L36; second run, checkpoint 10). thm:threemissing proves the fleet's |E| + τ − 1 bound,
  exactly, for four-cycle-free graphs.
  - It covers every circuit computing a polynomial in Sup(G) in which at most three edges lack a quadratic witness.
  - It also covers every such graph with at most four edges.
  - So a counterexample must miss quadratic witnesses on at least four edges.
  - At four missing witnesses, an induced matching of four missing edges already forces at least six deleted gates.
  - Check state: the run's same-model re-proof. The AG_POLISH reader a4f5fd04 (Claude Opus 5.5 at effort high) ran an
    exhaustive monotone-circuit search on seven graphs with at most four edges. That is a sanity check, not a test of the
    open case (AG_POLISH.md, "Follow-up 25 Nov").
- **P4-DET** is a restricted-model result. It is of the same kind as the symmetric-circuit and Möbius-pseudorandomness
  papers of the window (L37). It does not bear on VP ≠ VNP.

**What is still missing.** Before any fleet update, a check by a different model, and the merging of the two runs' records.
- Run 1 was checked by a2fedc2a (Claude Fable 5.2 at effort max).
- Run 2's audit was by the same model.

### 3.8 Grothendieck's frameworks (L38–L40)

- **"Over every field" is a statement over Spec Z (L38).**
  - Both claims, 98 R4 and 99 Q4a–Q4e make statements about all fibres: orbit closures and price cones.
  - For fixed (m, N), char-0 noncontainment spreads to all but finitely many p by constructibility (EGA IV₃ §9).
  - The exceptional primes for a price certificate are the primes dividing its integer D (99 Q4a).
  - Characteristic 2 needs a separate argument (99 Q4d; ANT's use of the Hamiltonian-cycle polynomial).
- **λ-rings (L39).**
  - Plethysm coefficients (GCT_PLETH) are structure constants of the λ-ring operations on the representation ring of GL.
  - Kronecker coefficients (GCT_POS, GCT_KRON) are the internal product on Λ.
  - Frame: SGA 6, Exposé 0 (Grothendieck's 1957 Riemann–Roch) and Exposé V (λ-anneaux).
- **Crystals and formal groups (L40).**
  - NK-6 is a statement about Artin–Mazur formal groups, that is, the slope < 1 part of H_cris.
  - Grothendieck, *Groupes de Barsotti–Tate et cristaux de Dieudonné* (Montréal 1974); Mazur's Newton-above-Hodge theorem.
  - Weights do not help here, as the AG_POLISH intake notes: purity fixes |eigenvalues|, while S mod p is a multiplicity.

### 3.9 Bridges tried without a link found (L41–L43)

- **NL = UL (Hoza, ECCC TR26-323) and Liu's orbit PIT for ROABPs (hexagon:2611.00634).**
  - Both derandomize isolation for read-once programs.
  - A candidate: whether Hoza's generator gives better hitting sets in the orbit setting (L41).
- **Deterministic linear-time MST (ECCC TR26-339).**
  - I tried the comparison-to-algebraic-decision-tree bridge.
  - None of our items uses it (L42).
- **GCT_GINEQ's norms.**
  - A norm gives a price only if it is monotone under restriction, multiplicative and normalized.
  - GINEQ shows norms do not bound rank.
  - Still to do: name the failing axiom for each norm (L43, a candidate).

---

## 4. Conference topics and paper candidates across clusters

- **T1. "The square decides."** Clusters: GCT × outside × geometry.
  - What it combines: NK-1, NK-2 and NK-4 with Liu-NC and Liu-AR, run 98, run 99 and both claims.
  - Paper candidate: a Hexagon note.
    - Its content: the equivalence (a) ⇔ (b) ⇔ (c), the two worlds, and the sums-of-squares witness.
    - What it needs first:
      - a different-model check of 98's PG-CROSSPOLY-GATE, PG-FOUR-CONDITIONAL and SH-08, and of 99's planar reduction;
      - the reconciliation of 98 and 99 on Q3b;
      - the final of run 99.
- **T2. GCT after VP ≠ VNP.** Clusters: GCT_KRON, GCT_OBS, CUE_GCT; 99 Q6; outside BIP.
  - What it combines: NK-3.
  - Paper candidate: a short note, "what a representation-theoretic certificate must look like", conditional on OAI
    Cor. 1.2.
- **T3. Beyond the occurrence level, on both sides.** Clusters: GCT_POS, GCT_PLETH, GCT_KRON; H13/H14; the price side.
  - What it combines: NK-5 and the occurrence-level analogy (L19).
  - A talk rather than a paper.
- **T4. Counting in coherent cohomology.** Clusters: AG_POLISH (COUNTING_VARIETIES) × the GCT cluster's DP_MULT × crystals.
  - What it combines: NK-6.
  - Prompt candidate: does a_{p²} encode a further count (second-order hardness of height ≥ 3)?
  - COUNTING_VARIETIES cp02 and cp03 were taken in by the AG_POLISH reader (AG_POLISH.md, "Follow-up 25 Nov"). The
    height test is not in COUNTING_VARIETIES; it stays our own observation.
- **T5. Fleet circuit bounds.** Clusters: AG_POLISH (SPLIT_ZERO paper 4) × the fleet (L-meta-608, 612, 647) × our partial
  proof of 23 Nov.
  - A fleet update after the different-model check and the merge.
  - SPLIT_ZERO cp10 was taken in by the AG_POLISH reader (Follow-up 25 Nov): a counterexample must miss witnesses on at
    least four edges.
- **T6. GCT VIII in one message.** Clusters: GCT_POS N-012 (H23), GCT_NSRH F57/F58/F67, and the SPLIT_ZERO e-mail draft.
- **T7. Border rank against asymptotic rank.** Clusters: BR_PENCIL, GCT_OBS BR-006, BORDER_RANK × Liu-AR × ω ≤ 9/4.
  - First, a computation: the local ranks of the det₄/per₄ tensor formats.
- **T8. Spec Z and characteristic 2.** Clusters: both claims; 98 R4; 99 Q4.
  - The exceptional primes of price certificates.
  - The char-2 square (permanent = determinant there).
  - Our runs could make the char-2 hinge a main question.

**Candidate for the joint lemma space (L44).** Add Liu-NC, Liu-AR and the 98/99 hinge statements as rows, with edges to
EXT-OAI:thm1.3 and EXT-ANTH:thm2.2. It is built by `FM/joint_tools/ext_claims.py`.

---

## 5. Problems to resolve

1. **Run 98 SH-08 and run 99 Q3b disagree** on whether nonflatness implies a strict shortening. 98 proves it under (H_A);
   99, which started first, lists it as open. Give 99's successor, or the intake of 99, the proof of SH-08 with the
   rigid-ball lemma.
2. **SH-09 and Q3c use ANT's Theorem D.2.** So "shortening ⇒ contraction" is not independent of ANT. Do not report it as a
   cross-check of ANT's dichotomy.
3. **Our public mirror carries three bullets that runs 98 and 99 correct (§2.6).** Our integration file carries the same
   statements. The main session decides on a correction commit.
4. **Three newer returns were taken in by the AG_POLISH reader a4f5fd04** (Claude Opus 5.5 at effort high; AG_POLISH.md,
   "Follow-up 25 Nov"): COUNTING_VARIETIES cp02 (21:00 UTC) and cp03 (21:45 UTC), and SPLIT_ZERO cp10 (21:10 UTC). Their
   state is used above (L36).
5. **The prompt-93 runs disagree on paper 3** (the AG_POLISH intake, §10 Problems). That is outside this map's complexity
   content and is left to AG_POLISH.

---

## 6. What I read, and what I did not

**Read for this map.**
- MAP_BRIEF.md and BRIEF.md (the check-event format).
- GCT.md, items 1–9 (l.49–170), and GCT_ITEMS.tsv.
- AG_POLISH.md: the top items, §9 (COUNTING_VARIETIES) and §10 (SPLIT_ZERO).
- LITERATURE_20261124.md: items 1 and 5 and the GCT block (l.24–52, 279–292), plus its Hexagon cs.CC entries.
- Run 98's report, and SH-08 with its proof.
- Run 99's CHECKPOINT.md, LEDGER.md and QUESTIONS.tsv, and the lines of its LITERATURE.md and explicit-spectrum records
  that cite the 2026 papers.
- Liu-NC's abstract, main theorem, definitions and two-cut paragraph. Liu-AR's abstract and §2 (l.57–73), by keyword.
- The fleet's PROOF_GRAPH rows for L-gct-006, 010, 011, 026 and 028 and for L-meta-584, 606, 608, 612 and 647.
- My own integration file and the public mirror's EXTERNAL.md, at the lines cited.
- From 24 Nov: the two preprints' statements, ANT's Section 2, and OAI's introduction and method.

**Not read.**
- The proofs of runs 98 and 99, beyond SH-08.
- Run 99's 49-page paper.
- The 2026 spectral-point papers, Khoruzhii's notes, and OAI's ω ≤ 9/4 paper. I rely on run 99's reading and on Liu's
  citations, and say so in each place.
- BR_PENCIL's tensor formats.
- The newer returns of §5.4, myself. Their state comes from the AG_POLISH follow-up.
- The excluded files (SAT_WITNESS*, SAT_KRONECKER*, prompt 74, Codex's runs) and the S6 series.

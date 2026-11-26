# Paper seed: the Hodge line

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 22 November 2026, for the main session (Claude Opus 5.5 at
effort max). One paper. It joins the bridge sketch, the division attack, HECKE_DIV, GHOSTS and two separate runs of
prompt 46 by GPT-6 Astra (ChatGPT Pro mode):

- **run A** began 21 Nov at 10:38:55 UTC; newest here is checkpoint 34 (22 Nov 12:08 UTC);
- **run B** began 21 Nov at 10:36:29 UTC, also received follow-up 46b, and is the folder named checkpoint_28
  (22 Nov 12:40 UTC). It is not an older checkpoint of run A. The two runs use the same ids for different statements
  (HD-G01, for example), so every id below carries its run.

Citation marks: **[opened]** means that I opened that source. **[from memory]** means what it says.
**[not opened]** means that the locator comes from a run's source log or from an intake, and the prompt must have it
opened.

Check words are those of the rubric. Where I wrote a proof, my reading of it is an author's check.

---

## Title

**The Hodge conjecture for abelian varieties as a uniform bound on cycles over finite fields**

Second choice: **Hodge classes on abelian varieties and the degrees of cycles modulo primes**

## What the paper says, for a reader with none of our files

A rational Hodge class t is algebraic when Nt = [Z⁺] − [Z⁻] for some positive integer N and effective cycles Z⁺, Z⁻. The
conjecture asks only that such cycles exist. The paper shows that, for abelian varieties, it is equivalent to a bound
on their degree, and that this bound may be tested entirely on reductions of CM abelian varieties over finite fields.

At a single CM point, and at a single good prime, such cycles are now claimed to exist: the Hodge conjecture for CM
abelian varieties and algebraicity modulo each good prime (OpenAI family 032; human proof by van Hoften and Sempliner;
both unrefereed). If one accepts this, the Hodge conjecture for abelian varieties is exactly an exchange of
quantifiers. We have "for each point and prime there is a bound". It is equivalent to "there is a bound for all the
points and, at each, infinitely many primes". The equivalence does not use 032.

The second half makes the bound explicit for Weil classes, the standard exceptional classes. One effective cycle with
nonzero projection to the Weil plane already gives the whole plane, at a cost quadratic in its degree, and in several
families that cycle has very small degree: at most 48 on the even principal Gaussian fourfolds, at most 36 on the
principal Eisenstein fourfolds.

The paper does not prove the Hodge conjecture, and does not say that it does.

---

## Main theorem

### Definitions

A *special family with a Hodge class* is a triple (S, θ, t):

- S is a connected smooth Shimura variety with a map to the moduli space A_{g,N} (N ≥ 3) of principally polarized
  abelian g-folds;
- f: A → S is the pulled-back family, with principal polarization θ;
- t ≠ 0 is a global section of R^{2p}f_*Q(p), of type (p,p) at every point.

For s ∈ S, let c_t(s) be the least max(N, deg_θ Z⁺, deg_θ Z⁻) over integers N ≥ 1 and effective integral cycles Z^± on
A_s with Nt_s = [Z⁺] − [Z⁻]; it is ∞ if there are none. Degrees are ∫_Z θ^{g−p}.

### Theorem (the reduction)

The following are equivalent.

1. The rational Hodge conjecture holds for every complex abelian variety, in every codimension.
2. For every special family with a Hodge class, c_t is bounded on the CM points of S.
3. For every special family with a Hodge class there is an integer D such that, for every CM point x and some (hence
   every) model of (A_x, θ, t_x) over a number field, the reduction of t_x at infinitely many places v is
   ([Z⁺] − [Z⁻])/N in ℓ-adic cohomology over the algebraic closure of k(v), with effective integral cycles of degree
   ≤ D and v prime to ℓ. The multiplier N is unrestricted.

In (2), the CM points may be replaced, family by family, by any one Zariski-dense set, for example one tensor-compatible
Hecke orbit. In (3), the infinitely many places may lie in any prescribed infinite set of good places of x, for example
the ordinary or the supersingular ones where there are infinitely many. When (1) holds, the bound in (3) holds at every
good place.

**Every input is published.** None of 032, Markman, Perry, Severn or André–Oort is used.

| Input | Where it enters | Citation |
|---|---|---|
| Zarhin's trick | reduction to principal polarizations | Zarhin 1974; Milne, *Abelian varieties*, 13.12 [from memory] |
| Mumford–Tate groups, connected Shimura varieties, Baily–Borel, Borel's extension theorem | every Hodge class lies in a special family | Milne, *Introduction to Shimura varieties*, §§3–6 [from memory] |
| Density of CM points and of Hecke orbits | (2) | Deligne 1971; Milne, Th. 5.4 (real approximation) [not opened] |
| Bounded families of cycles, projective Hilbert schemes | closed loci | Grothendieck, FGA 221, Lemma 2.4 and Th. 3.2 [not opened] |
| Relative cycle class | the class condition is open and closed | SGA 4½, *Cycle*, 2.3.1–2.3.8; SGA 4 XVI 2.2 [not opened] |
| Hodge classes on abelian varieties are absolute, with finite Galois orbit | the ℓ-adic section in (3) | Deligne, LNM 900, Main Theorem 2.11 and Prop. 2.9 [not opened] |
| Wirtinger and Hodge theory | bounded degree bounds N | textbook |

### Proof

**Every Hodge class lies in a special family.**

- If A is an abelian variety, B = (A × A^∨)⁴ is principally polarized and has A as a direct factor. Pull u back by the
  projection. Restriction to the factor preserves algebraicity, so it is enough to treat a principally polarized (B,u).
- Let G be the Hodge group of H¹(B,Q), X⁺ the G(R)⁺-orbit of its Hodge structure and Γ = G(Q) ∩ G(R)⁺ ∩ Γ(N).
  S = Γ\X⁺ is a connected Shimura variety, smooth since Γ is neat, with an algebraic map to A_{g,N}.
- G fixes u. So Γ fixes u, and u is a global section t. At every point of X⁺ the Hodge group is contained in G, so t has
  type (p,p) there. CM points are dense in S.

**Closed loci.** For fixed D and N, pairs of effective cycles of degree ≤ D are parametrized by a scheme projective over
S. Their class minus Nt is a flat section, so its vanishing is constant on connected components. Hence
S_C = {s : c_t(s) ≤ C} is closed.

**Bounded degree bounds N.** With d = g − p, h = ‖t_s‖ (constant, since t is flat of type (p,p) and θ is flat) and
V = ∫θ^g/g! = 1, pairing with the Hodge dual and Wirtinger give N·h ≤ (deg Z⁺ + deg Z⁻)/(d!√V). So bounded numerator
degrees bound N.

**(1) ⇒ (2).** S is the union of the closed sets S_C. An irreducible complex variety is not a countable union of proper
closed subvarieties (Baire), so S = S_C for some C.

**(2) ⇒ (1).** S_C contains the dense set of CM points, hence is S. Apply this to the family of (B,u).

**(2) ⇒ (3).** A CM point and its cycles are defined over a number field after descent without increase of degree (the
parameter scheme over Q̄ has a Q̄-point in each component). Specialize by properness: degree and multiplicity are
unchanged.

**(3) ⇒ (2).** Fix x. After a finite extension t_x is Galois invariant, by Deligne. On each component of the projective
parameter scheme over the ring of integers with degrees ≤ D at most one N satisfies the class equation, so one N
occurs at infinitely many places. The image of that component locus is closed in a curve and infinite, so it contains
the generic point. Thus Nt_x = [Z⁺] − [Z⁻] over Q̄ with degrees ≤ D, and N ≤ 2D/(d!h). So
c_t(x) ≤ max(D, 2D/(d!h)), independently of x. ∎

### Consequences, at their exact strength

- **With 032 [unrefereed]:** every c_t(x) at a CM point is finite, so the whole content of the Hodge conjecture for
  abelian varieties is the finiteness of sup_x c_t(x) in each special family.
- **Ghosts.** For one abelian variety over a number field and one Hodge class, either the local minimum c(v) equals the
  characteristic-zero minimum at almost all v, or {v : c(v) ≤ C} is finite for every C. 032 Remark 8.5
  with CM transport is said to give algebraicity modulo every good prime (GHOSTS C01; [unrefereed; not reopened;
  C01 checked at statement level only]). Granting it, a counterexample would be a class algebraic modulo every good
  prime whose least cycle degree tends to infinity with the prime. Remark 8.5 does not put the lifting CM point on
  the same special subvariety (GHOSTS C02); our bridge sketch, 2.6, said it did and must not be followed there.
- **One prime.** For fixed (x, D) there is an integer b_D such that one place v not dividing b_D with cycles of degree
  ≤ D already gives cycles of degree ≤ D over Q̄. No size bound on b_D is proved.
- **Beyond abelian varieties.** The complex half holds for every smooth projective family over a connected smooth
  quasi-projective base and every flat Hodge class: algebraic on every fibre ⟺ bounded numerator degrees on one
  Zariski-dense set. The arithmetic half holds for every absolute Hodge class on a variety over a number field.
  Neither is a reduction of the Hodge conjecture for all varieties to finite fields: that would also need every Hodge
  class to be absolute, and a dense set of points over Q̄ in each Hodge locus.
- **Not implied:** the Hodge conjecture for abelian varieties over Q̄ alone is not shown here to give it over C. A dense
  set of points each with its own bound is not enough; uniformity is the point.

### What must not be written

- "The Hodge conjecture is proved", or "reduced to a finite computation".
- "Reduced to Weil classes". André's 1992 theorem reduces the CM case to split Weil classes; nothing here does so for
  non-CM abelian varieties.
- That the abelian-variety equivalence depends on 032. Our attack file's R2 reads that way; it does not.
- From our attack: "for n ≥ 5 the source must have imprimitive reflection monodromy" (false as stated);
  "curve-cover sources reach only n ≤ 3" (Proposition O′ covers only functorial one-copy sources); "never by transport"
  (Theorem E proves only that the detector degree stays bounded while the core index grows); the exponent 4 of
  Theorem W (now 2); D₀(Q(i)) = 914,248,581,120 and the Eisenstein 132,269,760 as the best bounds (now 48 and 36).

---

## Why it matters, and the works it answers

- **Hodge, with Grothendieck's standard conjectures and cote 16.** Existence of cycles becomes boundedness. In
  Grothendieck's notes (Montpellier, cote 16, scans 048–050) conditions A, C and I separate the algebraic inverse, the
  comparison and the positivity. In our division theorem positivity does one job, inverting the Gram form of cycles one
  already has, and the projector is the algebraic inverse. Condition A is exactly what remains. Our scan number is the
  PDF page; the folio is scan − 1 at the places checked.
- **Deligne, *Hodge cycles on abelian varieties* (LNM 900, 1982), Th. 2.11** [not opened]: continues it. Absoluteness
  is what makes the test modulo primes possible.
- **Brünjes–Serpé, *Uniform bounds and ultraproducts of cycles*, arXiv:0901.4853, Def. 2.3(ii), Th. 3.4**
  [not opened; GHOSTS read it]: precedes the arithmetic criterion. The paper credits it and adds the proper parameter
  space, automatic boundedness of N, and the special families.
- **Cattani–Deligne–Kaplan, *On the locus of Hodge classes* (1995), Th. 1.1; Voisin, *Hodge loci and absolute Hodge
  classes* (2007), §0** [from memory]: the closed-locus background and the passage to Q̄.
- **van Hoften–Sempliner, Hexagon 2610.00259v2, and OpenAI family 032, Th. and Remark 8.5** [not opened in this pass]:
  supply pointwise finiteness. The paper shows exactly what uniformity they would need in order to give the
  conjecture for all abelian varieties.
- **André, "Une remarque à propos des cycles de Hodge de type CM" (1992)** [from memory]: the CM case and split Weil
  classes.
- **Schoen, Compositio Math. 65 (1988), Th. 2.0 pp. 11–12, construction pp. 12–13, Cor. 3.1 p. 25** [opened: those
  pages; Lemma 2.6 and the proof of Th. 2.0 not read]; **Th. 3.2 p. 26** [opened: it proves dominance for the
  Eisenstein (4,3) case only]. The paper continues it with integral bounds.
- **Schoen, Addendum, Compositio Math. 114 (1998), §7 p. 332, Lemma 13 pp. 334–335** [not opened]: the stabilization
  from split (2n+2)-folds to all determinants, and Eisenstein sixfolds.
- **van Geemen, Math. Z. 221 (1996), Lemma 3.3, Prop. 3.6, Th. 3.7, Th. 5.3, pp. 621–630** [not opened]: the Gaussian
  theta construction. Our bound 48 is read off from it.
- **Schoen's 2007 smoothing, as described in van Geemen, SIGMA 18 (2022) 097, Lemma 3.3, §§6.1–6.2** [not opened]: the
  surfaces behind the bound 36.
- **Koike, Canad. Math. Bull. 47 (2004), Th. 2.1** [not opened]: Gaussian sixfolds.
- **Markman, arXiv:2502.03415 (preprint), Cor. 1.6.1** [not opened]: algebraicity for all Weil fourfolds. It gives
  boundedness without a number. Not an input of any explicit bound below.
- **Perry, arXiv:2604.00511v2 (preprint), Th. 1.2** [not opened]: an input of the all-field bounds, marked there.
- **Severn, Hexagon 2610.00387v2 (unrefereed)** [not opened in this pass]: priority for the Eisenstein eightfold
  candidate, root data and intervals. The runs recompute them and use no theorem of it as a premise.

**Corrections of other works:** none claimed. No literature search has been made for the main theorem, on Hexagon,
arXiv or in journals. The closed-locus half is likely to be known in some form. The prompt searches first, in general
terms, and words the novelty by what it finds, without priority claims.

---

## The other results, in the order of the argument

### 1. One detector gives the Weil plane, quadratically

Let (A, θ) have dimension 2n, with an action of an order in an imaginary quadratic K, signature (n,n), Rosati inducing
conjugation. W = ∧_K^{2n}H¹(A,Q), e_W its projector, δ_W the least degree of an integral n-dimensional subvariety Y
with e_W[Y] ≠ 0. Let 0 ≠ t ∈ W, δt integral, T = (−1)^n∫t², and let a act integrally with a/ā not a root of unity.
Then

> δ_W ≤ c_t ≤ ⌈8·16^n/n!⌉ · δ · ⌈√T⌉ · Nm(a)^{2n(n+1)} · δ_W².

For n = 2, 3, 4 the first factor is 1024, 5462, 21846. The projector is ∏_{j=1}^n(S − α_j), with S = [a]^* + [ā]^* and
α_j = a^jā^{2n−j} + a^{2n−j}ā^j.

**Consequences.**
- The monodromy on W preserves a positive integral form, so it is finite. Hence the Weil classes on a connected family
  are all algebraic ⟺ δ_W is bounded on a dense set ⟺ δ_W has one bound at the CM points modulo infinitely many primes.
  The quantity does not depend on the class.
- For n = 2, K = Q(i), maximal order: c_t ≤ 61,440 δ⌈√T⌉D², from the explicit projector (1+[i]^*)(4−[1+i]^*) = 16e_W.

### 2. Gaussian fourfolds: degree 48

On the even principal family (Hermitian lattice U⊕U): δ_W ≤ 48 and c_t ≤ 141,557,760 δ⌈√T⌉. The proof is three lines,
given van Geemen: his detecting surface Y is a component of the intersection of two divisors in |2θ|, of class 4θ² and
degree 96. The residual R has e_W[R] = −e_W[Y], so one of the two has degree at most 48. Closedness carries this to
every fibre. By an explicit degree-16 polarized isogeny, the odd principal family (containing E_i⁴) has δ_W ≤ 192 and
c_t ≤ 2,264,924,160 δ⌈√T⌉.

### 3. Eisenstein fourfolds: degree 36, multiplier 3

On the principal component containing (E_ω⁴, product polarization, diag(ω,ω,ω̄,ω̄)):

- δ_W ≤ 36;
- c_t ≤ max{3δ, 36⌊δ√(2T)/3⌋} ≤ 17δ⌈√T⌉;
- 3(W ∩ H⁴(A,Z)) consists of classes of integral algebraic cycles.

Along a sequence of CM points with core index p^{4k}, explicit graphs give δ_W ≤ 8.

### 4. Split in one dimension higher gives every determinant

If split Weil (2n+2)-folds over a class-number-one K have detector bound D_{n+1}(Δ) in terms of the polarization
product Δ, every Weil 2n-fold over K, of any determinant, has

> δ_W ≤ (1 + Nm τ) · D_{n+1}(Δ²), O_K = Z[τ].

The construction takes the product with a balanced CM surface and contracts with four divisors. The qualitative
stabilization is Schoen's.

### 5. The explicit table

Δ is the polarization product, f the conductor, d the squarefree integer of the field Q(√−d), D_G = 39,191,040 the order
of the reflection group G₃₄.

| Family | Bound on δ_W | Inputs | My check on 22 Nov |
|---|---|---|---|
| Q(i) fourfolds, even principal | 48 | published | proof checked given van Geemen |
| Q(i) fourfolds, odd principal | 192 | published | proof checked |
| Q(ω) fourfolds, principal | 36 | published, with the run's smoothing and conormal section | quotient and lattice step checked; smoothing section not read |
| Q(i), Q(ω) fourfolds, every determinant | 63,700,992 f⁴⁶Δ¹²; 2,592,000 f⁴⁶Δ¹² | published sources and the runs' proofs | statements only |
| Q(i), Q(ω) sixfolds, split principal | 746,496 (even), 5,971,968 (odd); 30,375 | published sources and the runs' proofs | statements only |
| Q(√−7), Q(√−2) sixfolds, split | explicit (curve families with groups G₂₄ and the F₄ extension) | the runs' proofs | statements only |
| Q(ω) sixfolds, every determinant | from the next row through result 4 | the runs' proofs | result 4 checked; the application not |
| Q(ω) eightfolds, split | (4D_G⁸Δ)⁸B₀, with B₀ explicit | the runs' reconstruction; HECKE_DIV SQ1–SQ7; Severn's data recomputed | statement and group order only |
| Q(i) sixfolds, signed determinant class −3 | explicit | the runs' interval certificate and Fermat suppliers | statement only |
| all nine class-number-one fields, split sixfolds | 10^258 d^69 f^33 Δ⁶ (run B) | **Perry, preprint** | statements only |
| the same fields, fourfolds of every determinant | b_d 10^258 d^69 f^46 Δ^12 (run B) | **Perry, preprint** | statements only |
| all Weil fourfolds | finite, no number | **Markman, preprint** | statement only |

b_d = 2, 2, 2, 2, 3, 4, 8, 12, 28 for d = 1, 2, 3, 7, 11, 19, 43, 67, 163. **Do not use run A's all-field numbers as printed beside these.** Its
"2^324 d^57 Δ⁶" (HD-CM6), and the 2^661 and 2^658 forms built on it, look small but have d = 4mL², where
L = lcm(1, …, 2^2048): d is about exp(2^2049) (SF-QC01, quantitative_cm_section.tex, "Put P = …"). Run B's d is
the squarefree integer itself, so run B's bound replaces run A's.

### 6. What the attempts rule out

Both runs prove exclusions for restricted source classes (natural imprimitive families for n ≥ 5 have period rank
≤ 15 < 25 at n = 5; many monodromy and deformation exclusions). They belong in a short final section, each with its
exact restriction, and none as evidence against the conjecture. I have them at statement level only.

---

## The research question of the prompt

> **Prove that, for every imaginary quadratic field K, every n and every split Weil family of 2n-folds over K, the
> detector degree δ_W is bounded on the CM points.**

By results 1 and 4 (Schoen's stabilization for general K) this is the Hodge conjecture for all Weil classes, of every
determinant, in every dimension. It is the theorem that would turn this paper from a criterion into a proof for the
standard exceptional classes. The same uniformity for every special family is the Hodge conjecture for all abelian
varieties.

**The gate now.**
- n = 2: closed with explicit bounds for the nine class-number-one fields (Q(√−11), Q(√−19), Q(√−43), Q(√−67) and
  Q(√−163) through Perry's preprint, the other four from the runs' curve constructions), and
  without numbers for every K (Markman, preprint).
- n = 3: split closed for the nine fields, with the inputs above. Nonsplit open, except every determinant over Q(ω) and
  signed class −3 over Q(i). By result 4 these open cases all follow from split eightfolds over the same field.
- n = 4: split closed over Q(ω) only.
- n ≥ 5: no case. The standard imprimitive curve families do not dominate.
- So the first theorem needed is a bounded detector on split eightfolds over K ≠ Q(ω), and the general one is a
  construction uniform in n.
- Both runs' live gate on the deformation side (Q5i in A, the RM-seed rows in B) is an auxiliary object on an RM
  fourfold. Run A says itself that its bridge to a Weil eightfold (Q5au) is unproved.

**Routes not yet tried. None of these is a proved statement unless marked.**

1. **Make the proof of 032 uniform.** Track the degree of every cycle in the proof for CM abelian varieties as a
   function of the discriminant, and find which step makes it grow. If every step has bounded degree on a dense set of CM points, the theorem follows.
2. **A gap theorem.** c_t is invariant under Galois on CM points, and S_C is closed. An upper bound for the degree of
   S_C in terms of C, with lower bounds for Galois orbits, would show that c_t is either bounded or grows at least at a
   definite rate along suitable CM points. Any pointwise construction below that rate would then prove boundedness.
3. **Complete intersections.** This one step is proved. Let m_W be the least m such that n divisors in |mθ| meet
   properly with a component of nonzero Weil projection. Then δ_W ≤ m_Wⁿ(2n)!Δ/2 and m_W ≤ 3^{n+1}δ_W.
   *Proof:* the intersection has class mⁿθⁿ, which e_W kills, so a detecting component and its residual both detect,
   and their degrees total mⁿ(2n)!Δ. Conversely, a detector Y of degree D has degree 3ⁿD for the very ample 3θ and is
   cut out set-theoretically by forms of at most that degree; n general ones meet properly and contain Y. ∎
   So the question becomes: is there one m such that, at every CM point of a split family, some complete intersection
   in |mθ| splits off a Weil-detecting component? For Gaussian fourfolds m = 2. A dimension count or a theta-function
   construction in this linear system has not been tried for n ≥ 3.
4. **One large prime.** Bound the exceptional integer b_D at CM points, and construct bounded cycles at one prime
   beyond it (Honda–Tate, supersingular reductions).
5. **An equivariant seed.** A μ₃-equivariant balanced object on E_ω⁸, or a μ₄-equivariant one on E_i⁸. The exclusions so
   far use the real-multiplication bivectors and do not address these actions.
6. **van Geemen's mechanism one dimension up:** odd theta sections on split Gaussian sixfolds or eightfolds mapping to
   a quadric or Grassmannian with detecting linear subspaces, read through route 3.

---

## Proof files, programs and checks

`who` in every run row is GPT-6 Astra (ChatGPT Pro mode), checking inside its run. My rows are Claude Opus 5.5 at effort
high, agent abcaba9b6ae84b747. No statement has a proof-assistant certificate. The two runs got the same prompt and
use the same model, so their agreement is a second derivation, not a check by another model.

| Result | File and lines | In-run check | My check |
|---|---|---|---|
| reduction theorem | this seed, "Main theorem" | none | author's check, one reading; assembled 22 Nov from the rows below |
| closed loci, Hecke orbits | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HECKE_DIV_final_20261121T0204Z_unzipped/HECKE_DIV.tex 80–154 (P0, R21, R22); <local>/Documents/reports_20261120/hodge_bridge/HODGE_DIVISION_ATTACK_20261121.md 46–130 (R1–R3) | HECKE_DIV's own | targeted proof check, 21 Nov; attack: author's check |
| B01, B02, B03, B04, B05, B06 | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/GHOSTS_final_20261121T0256Z_unzipped/sections/bounded.tex 49–113, 126–163, 185–213, 228–249, 276–294, 296–336 | GHOSTS's own | targeted proof checks: 21 Nov B01–B06; reread 22 Nov |
| Theorem W, closed detector loci, Lemma Dom | <local>/Documents/reports_20261120/hodge_bridge/HODGE_DIVISION_ATTACK_20261121.md 131–208, 224–227, 310–337 | rechecked in both runs | author's check |
| uniform quadratic division (A: HD-WQ, HD-U) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/research/uniform_division.tex 1–128; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/research/gaussian_fourfold.tex 268–334 (HD-WQ) | independent re-proof by a second agent of run A | rederived 21 Nov; projector recomputed 22 Nov for ten fields, n ≤ 6 |
| quadratic division (B: HD-D01, D02) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/extraction.tex 12–107 | targeted check and exact script | targeted proof check; D02 recomputed |
| Gaussian 48 and 192 (B: HD-Q03, Q04) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/gaussian.tex 73–117 | targeted check and exact script | targeted proof check given van Geemen; constants recomputed |
| earlier Prym route, Gaussian type and dominance | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/gaussian.tex 4–71; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/research/gaussian_fourfold.tex 32–387; <local>/Documents/reports_20261120/hodge_bridge/HODGE_DIVISION_ATTACK_20261121.md 467–end | both runs | targeted proof check 21 Nov (Schoen Lemma 2.6 unread) |
| Eisenstein 36 (B: HD-F1-S07) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/followup_fixed_surface.tex 475–600; its input S05–S06 at 249–474 | run B review 10 | 475–600 targeted check; 249–474 not read |
| multiplier 3 (B: HD-F1-T05) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/followup_exact_division.tex 1–202 | run B | targeted proof check, 1–202; lattice norm 6 and index 3 recomputed |
| graphs of degree 8 (B: HD-F1-S02) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/followup_fixed_surface.tex 66–126 | run B | targeted proof check; the sequence T02 not read |
| stabilization (A: HD-COMP, COMP4) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/research/general_compensation.tex 3–123 | run A | targeted proof check of COMP; the supplied sixfold bounds of COMP4 not checked |
| all-determinant fourfolds (B) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/fourfold_all_determinants.tex 1–251; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/all_fields_fourfolds.tex 1–212 | run B | statements |
| split sixfolds, cyclic (both) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/sixfolds.tex 1–612; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/agents/sixfolds/sixfold_section.tex | both runs | statements |
| Q(√−7), Q(√−2) | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/agents/g34_eightfolds/g24/g24_section.tex 1–495; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/agents/g34_eightfolds/gf4/gf4_section.tex 1–384 | run A | statements |
| Eisenstein sixfolds, every determinant | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/research/eisenstein_compensation.tex 1–134; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/g34_descent.tex 1–433 | both runs | statements |
| split Eisenstein eightfolds | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/agents/g34_eightfolds/g34_section.tex 31–677; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/g34.tex 1–616 | both runs | attribution and 594–677 read; 131–593 not; group invariants checked 21 Nov by the main session (Claude Opus 5.5 at effort max) |
| Gaussian class −3 | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/e8_quantitative_transfer.tex 1–285 and the e8 sections it cites | both runs | statement |
| all fields through Perry | <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/agents/sixfolds/quantitative_cm_section.tex 1–896; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/cm.tex 1–687; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/sections/cm_effective.tex 6–726 | second-agent re-proofs in both runs | statements, inputs and the last arithmetic of B only |

**Programs.**
- Mine, run 22 Nov, PASS: <local>/Documents/reports_20261122/overnight_intake/HODGE_DIVISION/check_main_constants.py, output check_main_constants.out. It imports nothing from a return.
- Mine, 21 Nov: <local>/Documents/reports_20261120/hodge_bridge/division_attack_scripts/weil_detector_constants.py and qi_bezout.py.
- The runs': <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/scripts/gaussian_certificate.py; <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/work/imprimitive/cm_effective_degree.py; the G₃₄ certificates of both
  runs. None was run by me today.

---

## LaTeX to attach

Ours:
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/GHOSTS_final_20261121T0256Z_unzipped/sections/bounded.tex (with local_weil.tex and family_checked.tex)
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HECKE_DIV_final_20261121T0204Z_unzipped/HECKE_DIV.tex
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/HODGE_DIVISION.tex with the files in the table
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/HODGE_DIVISION.tex with sections/ (the files in the table, sections/overview.tex and sections/bibliography.tex)
- <local>/Documents/reports_20261120/hodge_bridge/HODGE_DIVISION_ATTACK_20261121.md, with the list "What must not be written" from this seed beside it, because the file is stale there
- <local>/Documents/reports_20261120/hodge_bridge/HODGE_BRIDGE_SKETCH_20261121.md
- this seed, and <local>/Documents/reports_20261122/overnight_intake/HODGE_DIVISION/check_main_constants.py

Others', for reading only (attach to the prompt, never to GitHub):
- arXiv e-prints 0901.4853, 2502.03415 (TeX on disk at <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/original_sources/LIT_Markman_Hodge_abelian_fourfolds_2502.03415/250531.tex),
  2604.00511v2, 2212.10638;
- van Geemen, SIGMA 18 (2022) 097: its arXiv e-print (the prompt builder looks up the number; I have not);
- no TeX found by me, so PDF: Schoen 1988, van Geemen 1996, 032, Hexagon 2610.00259v2.

## Never to GitHub: other people's files

Lists by path, made by name and folder pattern (they also catch our own compiled PDFs, so read them before any push,
and they are not proof that nothing else is foreign):
- <local>/Documents/reports_20261122/overnight_intake/HODGE_DIVISION/sources_runA_cp34.txt
- <local>/Documents/reports_20261122/overnight_intake/HODGE_DIVISION/sources_runB_cp28.txt

Known foreign files and folders:
- <local>/Documents/recent_results_20261110/papers/hodge_sources_20261121/Schoen_1988_Hodge_classes_on_self-products_Compositio_65.pdf
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/original_sources/: 032_*.pdf, OPENAI_032_*.pdf (two), ALPOGE_remark.pdf, ALPOGE_Main.lean, ALPOGE_Statements.lean,
  HEXAGON_2610.00259v2_*.pdf, Hexagon_2610.00259v2_*.pdf, HEXAGON_2611.00244v1_Milne_report.pdf,
  LIT_Markman_Hodge_abelian_fourfolds_2502.03415/ (whole folder)
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/contributions/replacement/sources/saito_1990_review_p312.png, p313, p323, p324
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/contributions/transport/sources/bimas_2018405_landing.html
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/research/sources/shioda1979/gdz.html
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/work/sixfolds/provenance/secant_objects.html
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped/intake/DEG_L_checkpoint_06/provenance/reference_scans/ (whole folder: archive, SGA and Knudsen–Mumford pages)
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/research/sources/ (chevie, collins2008, monderer_neftin, neftin_zieve)
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/agents/imprimitive/e8_search/sources/certificates/ (downloaded certificates)
- <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/tmp/pdfs/
- every copy of these inside <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/_from_earlier_checkpoints/, and the ZIPs of sent prompts 46 and 46b

The folder <local>/Documents/grothendieck_archive_transcription_20261110/research_returns/HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped/_from_earlier_checkpoints/ also holds files of run B (its checkpoints of 12:06, 15:06, 16:36 and 21:07
UTC), so nothing from it may be published or cited as run A's.

## Workbench

**Hodge conjecture for abelian varieties: bounded cycles, Weil classes, ghosts.** The paper points to one folder per
run, with run A and run B kept apart and their check events beside them.


---

## Update after HODGE_FINISH (23 Nov 2026, Claude Opus 5.5 at effort high, agent aaf694615cb43adc1)

The finishing run (prompt 70c, GPT-6 Astra (ChatGPT Pro mode)) split this seed's paper into two standalone papers:
`grothendieck_archive_transcription_20261110/research_returns/HODGE_FINISH_final_20261123T1713Z_unzipped/workbench/work/UNFILED-A/v1/paper/main.tex`
(66 pp., "The Hodge conjecture for abelian varieties as a uniform bound over finite fields") and `UNFILED-B` (88 pp.,
"Obstructions to cycle constructions and criteria for Mumford's exceptional classes"). Superseding this seed:
- the multiplier bound is the Poincaré-pairing bound M^2 q_t <= C(2d,d)(deg Z+ + deg Z-)^2, valid in every characteristic
  (replaces the Wirtinger bound above);
- extraction: c_t <= ceil(2*16^n/n!) delta ceil(sqrt T) Nm(a)^{n(2n+1)} delta_W^2 (replaces 8*16^n/n! and 2n(n+1));
- stabilization factor max(1, Nm tau/Delta)/(n+1) (replaces 1 + Nm tau);
- every split Weil family over any K reduces to one principal family U^n at cost (t_K f m_K)^n Delta (Paper A, principal quotient);
- Gaussian sixfolds of determinant class [-3]: 3 | Delta and delta_W <= (Delta/3) B, relative to Severn's unrefereed
  E8 construction (Paper A, Theorem gaussian-volume-bound and Lemma gaussian-maximal-lattice);
- the state of the field: the Hodge conjecture is known for abelian varieties of dimension at most 5 (Markman; Voisin,
  Bourbaki 1248, Th. 1.3, p. 1248-03). The research question of this seed (split eightfolds and higher) stands.
Intake: `field_experts/intake_20261121/intakes/HODGE_FINISH/INTAKE_HODGE_FINISH_20261123_final.md`.

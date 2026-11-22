# Intake of RESEARCH_SA12 (return cp23): the mathematics

Intake by Claude Opus 5.5 at effort max (agent of sweep 3, reader A of SA12, who read cote 29 scans 2-140 on 19 Nov 2026),
resumed on 20 Nov 2026 by the main session (Claude Opus 5.5 at effort max) under
`field_experts/intake_20261120/INTAKE_BRIEF.md`. The run: GPT-6 Astra (ChatGPT Pro mode). Written as I go; the state at
the end of the run is the state of this file.

## 0. What was read, and the scope

- **Return folder:** `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`
  (checkpoint 23, 20 Nov 2026 17:25 UTC). Register `RESEARCH_SA12_results.csv`, 404 rows; the run's report opens
  "INCOMPLETE". Prompt as sent: `pro_prompt_builds/RESEARCH_SA12/PROMPT.md` (parts A-D: A cote 31, the cd of affine
  schemes; B Pic^tau, 29/071-077; C Proposition 4 and 29/131; D the other pi_1 questions of cotes 29 and 31).
- **My rows:** all 404 rows of RESEARCH_SA12 in packets 12-18 (42 + 48 + 70 + 86 + 65 + 52 + 41), about 50,000 proof
  lines. No earlier intake of this run exists (the sort says every row is untreated).
- **Scope (filled in as the reading goes; final in section 0.1):** the rows read in full with their proofs are the
  headline rows of each part and the rows the others rest on; every other row is reported at the level of its
  statement, its status in the run, and the run's own check events.

### 0.1 Rows read in full, and rows at statement level
- **Read in full with their proofs: 48 rows.** Part A 16 (listed in 1A), part B 14 (listed in 1B), part C 7 (listed
  in 1C), part D 11 (listed in 1D).
- **Read in part: 3 rows.** B.2g (structure; it rests on B.2e and B.2f, not read in full), C:etale-moduli (statement
  and the first half of the proof), D:cohomology-crown-criterion (statement, forward direction, start of the converse).
- **At the level of the statement: 353 rows** (45 in A, 25 in B, 7 in C, 276 in D), each with the run's status and its
  recorded check events; they are listed by name in 1A-1D.
- **Order of reading:** the headline rows of each part and the rows other rows rest on first (A.1-A.2 refutations,
  B.1-B.2, C:literal-141, D.1-D.2 positive case, the programme rows D:cohomology-crown-criterion,
  D:local-complete-Lang, D:local-surface-constant-H2), then the rest. At about 70 % of my context I stopped reading
  proofs and wrote up from what I had read (context guard, 20 Nov).
- **Counts:** see 1E.

## 1. Verdicts, row by row
(filled in part by part: A, B, C, D)

### 1A. Part A (cote 31, the cohomological dimension of affine schemes; 61 rows, A:basic ... A:wild-affine-upper)

**Read in full, with their proofs (16 rows):** A:basic, A:spread, A:realcone, A:general-upper, A:mixedreal, A:nagata,
A:nagata-global-consequences, A:nagata-local-consequences, A:hens-affine-unit, A:artin-NB, A:wild-generic-open,
A:double-trait, A:A2-wreath-calculation, A:A2-quadratic-step, A:A2-persistent-arithmetic-counterexample,
A:wild-affine-counterexample.

| row | the run's status | my check | verdict |
|---|---|---|---|
| A:realcone (A.1) | refuted | T = Spec R[x,y,z]/(x^2+y^2+z^2), l = 2: normal (S_2, singular only at the origin), K nonreal (-1 = (y/x)^2+(z/x)^2), cd_2(K) = cd_2(K(i)) = 2; the origin's residue field R gives H^q(T, i_*Z/2) = H^q(R, Z/2) = F_2 for all q. Re-derived. | targeted proof check, confirmed. The obstruction is the real point; SGA 4 X 4.5 already has it (the run says so). |
| A:mixedreal (A.3, A.4 upper) | refuted | T = Z[x,y]/(x^2+y^2) semilocalized at P=(x,y) and Q=(2,x-1,y-1): a domain (Gauss), maximal ideals PA (residue Q) and QA (residue F_2), Frac = Q(i)(x) of cd_2 = 3, delta(V(2)) = 1 (T/2T reduced is F_2[x]), 3 a unit; cd_2 infinite through the real residue field Q. Re-derived. | targeted proof check, confirmed (again a real-field obstruction). |
| A:nagata, -global-, -local-consequences (A.1, A.6(i)(ii); A.5 and affine A.7 without quasi-excellence) | known construction; refuted | Gabber's construction (ILO, Exposé XVIII_B §2, locator not opened by me): B strictly henselian regular, not quasi-excellent, of dimension 2; U = Spec B[1/F] an excellent Dedekind scheme with cd_l(U) = 3, cd_l(K) = 2, all residue fields nonreal. The consequences follow line by line: every summand cd k(u) + dim O_u is 2 < 3. | consequences: targeted proof check, confirmed; the construction carried as background (known). |
| A:double-trait (A.7(ii), nonaffine (iii)) | refuted | two copies of Spec k[[t]] glued along the generic point; Mayer-Vietoris gives H^2(X, Z/l) = H^1(k((t)), Z/l) = Z/l(-1), so cd = 2 > 1. Re-derived. | confirmed (a nonseparatedness technicality, as the run says). |
| A:A2-wreath-calculation | proved | G = (V+V) x| C_2, Sigma(x,y;e) = x+y; A = ker Sigma = {(u,u;b)}, action v.(b,u) = (b,u+bv), phi(e_g) = (1,g) onto, transfer (x,y;e) -> (x+y,x+y), squares (b,u;v)^2 = (0,bv). Each identity re-derived. | independent re-proof, confirmed. |
| A:A2-quadratic-step | proved | M = the 2-split Hilbert class field quotient (V = C_F); b by weak approximation with prescribed local square classes above S; the ray class field E/M; a Chebotarev prime with Frobenius the class of (b); eta with (eta) = P; N~ = M(sqrt(sigma eta)), Gal = F_2[V] x| V, quotient by ker phi; ramification only at the sigma P, with inertia meeting H trivially; inertness at S in both Frobenius cases (v = 0; v != 0 through the square formula); C_L ->> H and the transfer diagram. Re-derived step by step. | targeted proof check, confirmed. |
| A:A2-persistent-arithmetic-counterexample (A.2; also A.1 with no real residue field) | refuted | F_0 = Q(sqrt(-35)), h = 2 (P = (3,w) is not principal: x^2+xy+9y^2 = 3 has no solution); the tower F_n in which every rational prime is eventually inert; R = union of O_{F_n}[1/2] is Dedekind and excellent; Br(T)[2] = 0 for finite T/K by unbounded 2-power local degrees, so cd_2(K) = 1; Pic(U)/2 is infinite for every nonempty open U, so cd_2(U) = 2 (upper bound: closed residue fields have cd_2 = 0). Re-derived. | targeted proof check, confirmed. **The main result of part A.** |
| A:wild-affine-counterexample (A.5 in residue characteristic 2) | refuted | A = W(Fbar_2)[[t]], U = Spec A[1/t]: H^2(V) -> H^2(L) -> H^3(U) -> 0 from the localization at the point (2) of U; the image of H^2(V) consists of the a + {t,u}; Kato's filtration with gr^0 = E*/E*^2 and gr^1 = Omega^1_E (e = 1, p = 2) puts their gr^1 images in B dt + k t^-1 dt, while c = {1+2/t, t} has gr^1 image t^-2 dt. Each step checked; the filtration identifications and the strictness of H^2(R) -> H^2(L) are taken from the cited Suzuki 2024 and Gabber-Orgogozo (locators not opened by me). | targeted proof check, confirmed conditional on the cited filtration theorems. The run credits the lead to Gabber's 2015 IHES lecture and claims no priority. |
| A:basic, A:general-upper, A:hens-affine-unit, A:artin-NB, A:wild-generic-open | known | read in full; standard (SGA 4 VI, VII 5.7, IX, XIX 6.2; ILO XV 1.2.2, XVIII_A 1.1, 2.2; Gabber-Orgogozo 6.1; locators not opened by me). | carried as background without fault found. |
| A:spread | proved | spreading a nonzero class of H^n(K, M) to an affine open; it survives on every smaller open by restriction to the generic point. Re-derived. | targeted proof check, confirmed. |

**At statement level only (45 rows):** A:valuation-lower, A:proper-fibre, A:allresidues-lower, A:hens-nonreal,
A:local-lower, A:p-rank-margin, A:realexception, A:strict-field, A:one-divisor, A:generic-plus-dimension,
A:quadratic-descent, A:eventual-field, A:arithmetic-test, A:A2-approximation, A:A2-arithmetic-two,
A:A2-split-tower-exclusion, A:A2-PAC-exclusion, A:A2-approximation-equality, A:A2-tower-Dedekind,
A:cyclotomic-domain, A:cyclotomic-Pic, A:Iwasawa-equivalence, A:Dedekind-Pic-criterion, A:canonical-Iwasawa,
A:Dedekind-Milnor-obstruction, A:Dedekind-Milnor-criterion, A:semilocal-Dedekind, A:curve-normalization,
A:principal-completion-bound, A:A2-local-surface, A:strict-model-rigidity, A:arithmetic-affine-relative,
A:arithmetic-transcendence, A:A2-arithmetic-maximal, A:A2-Galois-tower-procyclic, A:A2-class-persistence,
A:Dedekind-overring-cd, A:strict-normalization-rigidity, A:A2-all-surface-models, A:semilocal-topnormalization,
A:strict-overring-bound, A:A2-topnormal-models, A:relative-affine, A:wild-affine-upper,
A:A2-sharp-curve-consequences. Their statements are consistent with the rows read in full. The run records no check
event for 10 of them: A:proper-fibre, A:allresidues-lower, A:hens-nonreal, A:arithmetic-transcendence,
A:A2-arithmetic-maximal, A:Dedekind-overring-cd, A:A2-all-surface-models, A:semilocal-topnormalization,
A:strict-overring-bound, A:A2-topnormal-models.
- A:canonical-Iwasawa has kind "conjecture" and status "Proved" in the register: it is a proved reduction (one
  arithmetic instance contains the odd-prime mu-conjecture), not a proof of the mu-conjecture. The A.2 counterexample
  above does not use it ("No positive Iwasawa mu-invariant ... is assumed").
- A:A2-sharp-curve-consequences is the persistent one-dimensional refutation of A.1, A.6 and the leads L1, L2; it
  follows from the counterexample I checked.

### 1B. Part B (Pic^tau, 29/071-077; 40 rows, B.1a ... B:Pic-finite-constants-sheaf, with L6a-L6c)

**Read in full, with their proofs (15 rows):** B.1a, B.1b, B.1c, B.1, B.1d, B.1e, L6a, L6c, B.2a, B.2b, B.2, B.2d,
B.3, B.3a; B.2g for its structure (it rests on B.2e, B.2f and de Jong).

| row | the run's status | my check | verdict |
|---|---|---|---|
| B.1a | refuted (the inference on 29/072) | alpha_p in alpha_{p^2}: Hopf ideals, one point, both cotangent spaces generated by t, coordinate dimensions p and p^2. The counterexample I gave in sweep 3 (c29a.md). | confirmed. |
| B.1b | known with derivation | finite flat torsors are invariant under proper birational normal-to-regular maps: purity of finite flat torsors across codimension two on a regular base (Moret-Bailly; the run cites "Marrama2026, Theorem 6", locator not opened by me) and full faithfulness on normal schemes. For the two groups L6c uses, alpha_p and Z/p, I re-derived purity directly (Z/p: Zariski-Nagata; alpha_p: Frobenius is injective on the local cohomology of a regular ring, by Kunz). | carried as background; the two cases used in L6c re-proved. |
| B.1c | proved | a closed subgroup Q of a proper commutative P over k = kbar that receives every map from finite commutative H equals P: l-torsion density gives A = (P_red)^0 in Q; torsion points in every component give P_red in Q; the kernel of F^r (r killing the nilradical) is finite and lies in Q; fppf-locally x = a + h. Re-derived. | independent re-proof, confirmed. |
| B.1 (the theorem of 29/071 in char p) | proved | Q = Pic^tau_Y -> P = Pic^tau_X is a closed immersion (f_*O = O universally; Kleiman's properness); Raynaud's H^1(Z, H^D) = Hom(H, Pic_{Z/k}) with B.1b makes Hom(H,Q) -> Hom(H,P) bijective for all finite commutative H; B.1c concludes. Each step checked. | targeted proof check, confirmed, given B.1b and Raynaud 6.2.1. **Grothendieck's theorem of 29/071 holds in characteristic p**; the gap I found in sweep 3 is real and this argument closes it. |
| B.1d | proved | the Frobenius split of H^1(O), as on 29/072-073 (F_*O/O torsion-free on normal X, locally free on regular Y by Kunz; Hartogs; Artin-Schreier with B.1b for F_p). The same argument as my sweep-3 re-derivation. | confirmed. |
| B.1e | proved | over an imperfect k: geometric normality of X makes Y_kbar normal; Hom(H, Pic) = H^1(Z, H^D)/H^1(k, H^D) with a rational point after a finite separable extension; finite P[n] and the Frobenius kernels lie in Q; conclude over kbar. Read; consistent. | targeted proof check, confirmed. |
| L6a | proved under hypotheses | an H^1 isomorphism and an H^2 injection give an isomorphism of formal Picard functors (induction on the length of Artinian R; obstruction in H^2 x I, lifts a torsor under H^1 x I). This is the repair I proposed in sweep 3. | independent re-proof, confirmed. |
| L6c | proved | **R^1 f_* O_X = 0 for every proper birational f: X -> Y with X normal and Y regular, in characteristic p, without resolution.** Localize at a minimal point of the support and strictly henselize; M = H^1(T, O_T) has finite length; purity for alpha_p- and Z/p-torsors gives ker F = 0 and ker(F-1) = 0 on M; semilinearity gives m M = 0; on the finite-dimensional M an injective p-semilinear F has a nonzero fixed vector (stabilized spans and an étale Artin-Schreier system of degree p^r over the separably closed residue field). Each step re-derived. | independent re-proof, confirmed. I do not know this result in the literature for normal X (for smooth X it is in Chatzistamatiou-Rülling). |
| B.2a, B.2b, B.2 (his Question on 29/075, item (iii)) | proved | one geometric generic complete-intersection curve C on a fixed normal projective model M detects reflexive 1-forms, misses every k-defined codimension-2 set, and stays irreducible in every finite k-defined cover; then H^1(W_E, O) -> H^1(C, O) is injective for every normal modification W (the F-nilpotent part through d: F_*O/O -> Omega and B.2a(1); the F-bijective part through F_p-torsors and B.2a(3)); so h^1(O_X) <= g(C) for every proper normal model X. Each step checked. | targeted proof check, confirmed. **His Question (iii) on 29/075 is answered: h^1(O) is bounded over all proper geometrically normal models.** |
| B.2d | proved | all Pic^tau of modifications embed in one Jacobian J(C): the kernel has zero Lie algebra (B.2b), is finite étale, and has no l-torsion (Kummer torsors and B.2a(3) for l != p; mu_p-torsors, dlog and B.2a(1) for l = p). Read in full. | targeted proof check, confirmed. An increasing chain of closed subgroups of J need not stabilize (J[p^n]), so B.2d alone does not give essential constancy; the run does not claim that it does. |
| B.2g | proved | essential constancy of the full Pic^tau system over kbar, from de Jong's regular Galois alterations, B.2e (invariant fields of finite groups acting on smooth projective varieties) and B.2f (purely inseparable descent). The structure read; B.2e and B.2f (361 and 281 lines) not read in full. | not read in full; no fault found in the structure. **If B.2e and B.2f hold, his Corollaire 2 on 29/075 holds over kbar with normal models only** (his Question). |
| B.3 (29/077) | proved | dim Pic <= h^1(O) (the tangent space, Kleiman 5.11) <= b(K/k). The proof uses Artin-Schreier torsors and finite covers, not pi_1. | confirmed; it answers his request for a proof "n'utilisant pas la théorie du groupe fondamental". |
| B.3a | refuted and corrected | the rank formula holds for l != p (Kummer) and fails for l = p: y^2 + y = x^3 over Fbar_2 (inverse (x,y) -> (x,y+1), no nonzero 2-torsion). | confirmed (my sweep-3 correction, now with an explicit curve). |

**At statement level only (25 rows):** B.1f, B.1g, B.2c, B.2-U, L6b, B.2e, B.2f, B.2h, B.2i (refuted: the marked model
category is not always filtered), B.2j, B.2k, B.2l, B.2m, B.2n, B.2o, B.2p (refuted: an abelian target does not ensure
a geometrically normal graph over an imperfect field), B.2q (refuted: a constant domination-cofinal Pic^tau diagram
fails over an imperfect field), B.2r, B.2s, B.2s.cor, B.2t, B.2u, B:equivariant-constant-data,
B:invariant-abelian-realization, B:Pic-finite-constants-sheaf. They treat imperfect ground fields and the category of
marked models; the run records no check event for B.1f, B.1g, B.2j, B.2k, B.2n, B.2o, B:equivariant-constant-data,
B:invariant-abelian-realization, B:Pic-finite-constants-sheaf. The three refutations (B.2i, B.2p, B.2q) concern
imperfect fields and marked models; they leave B.1, B.2 and B.2g over kbar untouched.

### 1C. Part C (Proposition 4 and 29/131; 15 rows, C:literal-141 ... C:all-constant-classification)

**Read in full, with their proofs (7 rows):** C:literal-141, C:criterion, C:cusp-all-subgroups,
C:normal-counterexample, C:k-morphisms, C:etale-nonseparated, C:non-sheaf; **partly (1 row):** C:etale-moduli
(statement and the first half of the proof).

| row | the run's status | my check | verdict |
|---|---|---|---|
| C:literal-141 | proved | **The run separates 29/139 from 29/141**: on 141 the category is closed under kernels of pairs and images, all admissible. Proof: G acts on G' by u(g) z v(g)^-1 with stabilizer E = Eq(u,v); G/E embeds as a closed orbit, nilpotently inside an open and closed U of G' (the radicial kernels have one geometric point, so the component group of E is the equalizer of the component maps); a pointed isomorphism of pushouts is a section of P x^G G' meeting P/E at a; connectedness puts it in P x^G U and reducedness of S in P/E; pulling back P -> P/E gives the E-reduction. Each step checked. | targeted proof check, confirmed. It is my sweep-3 refined statement (c29a.md: "true when the equalizer of u, v is admissible") with the decisive observation that this is what 29/141 itself assumes. |
| C:criterion | proved | Proposition 4 for all minimal classes is equivalent to lifting along equalizers; with image factorizations, also to pro-representability by a strict pro-object. Read; the argument is the minimal-reduction one of 29/128. | targeted proof check, confirmed. |
| C:cusp-all-subgroups | refuted (29/139) | the cusp A = k[t^p, t^{p+1}], P: z^p = x, u = 0, v = [x]; minimality even against nonflat subgroups with fppf torsors (generic fibre of a proper subgroup trivial, local sections glue by schematic density). Matches my sweep-3 re-derivation of Pro N033. | confirmed. |
| C:normal-counterexample (C.1(i)) | refuted | S = A^2 (regular), G = alpha_p^2, P: s^p = x^{p+1}, t^p = x y^p, u = (y, -x), v = 0: (ys - xt)^p = 0; minimality: a generic line (c,d) reduction needs x (dx - cy)^p in K^p, so the line is (x,y), whose closure is not flat (fibre length p(p+1)/2 at the origin); the trivial reduction fails since x^{p+1} is not a p-th power. Re-derived. | independent re-proof, confirmed. **Normality, even regularity, of S does not save Proposition 4 for S-morphisms**; this sharpens my sweep-3 remark that the error is confined to morphisms varying along S. |
| C:k-morphisms (C.1(ii)) | proved | finite k-groups and k-homomorphisms over any connected reduced noetherian k-scheme: equalizers are constant, hence admissible; C:literal-141 applies. A second proof through the reduced finite stack [G'/G] (Borne-Vistoli 7.15(c), locator not opened). | targeted proof check, confirmed (first proof). |
| C:etale-moduli (C.2, étale) | proved under stated hypotheses | pointed G-torsors on X/S, G finite étale: Hall-Rydh algebraicity, trivial pointed automorphisms, quasi-finite étale algebraic space; a separated scheme when the fibres are geometrically reduced. First half read. | not read in full; statement consistent with C:etale-nonseparated. |
| C:etale-nonseparated | refuted (separatedness asked in C.2) | X = (Q_0 x E)/(tau, z -> -z) over k[t]_(t), E: z^2 = t^2; H^0(X_R, O) = R; the pointed torsor P is trivial on the generic fibre and the nontrivial cover Q_0 -> C on the special fibre, so two sections agree generically and not on the trait. Re-derived. | independent re-proof, confirmed (the special fibre is nonreduced, as it must be by C:etale-moduli). |
| C:non-sheaf (C.2, finite flat) | refuted | char 3, X the split square-zero thickening of an elliptic curve C by a 2-torsion L, G = alpha_3 x| mu_2, P induced from the mu_2-torsor of L: the pointed automorphism sheaf is G_a (odd functions b epsilon), so a nonzero class in H^1(T, G_a) on a curve T of positive genus gives a pointed torsor locally isomorphic to P_T and not globally. Re-derived. | independent re-proof, confirmed. The class functor is not a Zariski sheaf; C:finite-flat-stack (an algebraic stack with affine diagonal) is the right object. |

**At statement level only (7 rows):** C:nori (the rationally pointed pro-object is Nori's group; with the
manuscript's geometric marking the identification fails), C:constant-all-maps, C:nonfield-all-maps (with geometric
marking in characteristic p, Proposition 4 for constant groups and all S-maps holds iff Gamma(S,O) = k, failing when
Gamma(S,O) is not a field), C:field-descent (refuted: with non-rational marking it can fail even when Gamma(S,O) = L
is a field), C:detect-proper-subgroup, C:all-constant-classification, C:finite-flat-stack. They are consistent with
the rows read: the dividing line is always whether the equalizer of u and v is finite flat (admissible).

**What C changes for 29/124-142.** Proposition 4 on 29/139 is false as written (S-morphisms; the cusp), even over a
regular base (A^2); it is true as restated on 29/141 (category closed under admissible equalizers and images) and for
the 1959 letter's own setting (constant groups, k-morphisms), over any connected reduced noetherian base. His margin
"Sans rigueur" (139) and his warning on 142 ("on perd le fait que S est réduit") mark exactly the step that needs the
equalizer to be flat. For 29/131: the étale case is representable (quasi-finite étale algebraic space; separated
scheme under geometrically reduced fibres); separatedness fails without reduced fibres; for finite flat G the class
functor is not a sheaf, and the stack replaces it.

### 1D. Part D (the other pi_1 questions of cotes 29 and 31; 288 rows, D:fixed-boundary-positive ... D:wild-swap-exact-image)

**Read in full, with their proofs (11 rows):** D:fixed-boundary-positive, D:kernel-counterexample, D:kernel-regular,
D:Chow-surface-boundary-obstruction, D:arithmetic-invertible, D:arithmetic-tame, D:vanishing-conjugacy,
D:proper-descent, D:prime-to-p, D:local-complete-Lang, D:local-surface-constant-H2. **Partly (1 row):**
D:cohomology-crown-criterion (statement, the forward direction and the first part of the converse).

#### D.1 and D.2 (29/061 and 29/066)

| row | the run's status | my check | verdict |
|---|---|---|---|
| D:fixed-boundary-positive (D.1 and D.2(ii), positive cases) | proved under stated hypotheses | Q(X,Y) = pi_1(X - Y) modulo the wild inertia at the codimension-1 components of Y is finitely generated when X is projective (the geometric generic complete-intersection curve misses every k-defined codimension-2 set, meets the boundary divisors transversally at points where the covers are tame Kummer, and every connected cover stays connected on it, so pi_1^t(C°) ->> Q(X,Y)); when char k = 0 (Orgogozo 2003, Th. 4.11); when X is regular with normal-crossings boundary (cited AHLS 2026, locator not opened). Projective case checked step by step. | targeted proof check, confirmed (projective case); the other two cases carried as background. **This is the projective case of 29/066 I isolated in sweep 3 (c29a.md: "the theorem is proved for projective Z"), extended to his question of 29/061.** |
| D:kernel-counterexample (D.2(i), the margin question of 29/066) | refuted | X = Spec C[a,b,c,(a+1)^-1]/(ac - b^2) (invariants of (y,z) -> (-y,-z) on C[y,z,(y^2+1)^-1]), Y the vertex: pi_1(X - Y) = C_2 * Z, pi_1(X) = Z, the kernel is the normal closure of the order-2 element, with quotients (C_2)^m for all m (wreath W_m = C_2^m x| C_m). Re-derived. | independent re-proof, confirmed. Scope: X is affine; his question sits under a theorem on complements of codimension >= 2 in proper schemes, and that restricted question is not settled (see prompt updates). |
| D:kernel-regular | proved (known) | for X regular, Zariski-Nagata purity (SGA 1 X 3.3) gives pi_1(X - Y) = pi_1(X). | carried as background without fault found (it is my sweep-3 check of the margin remark on 29/070). |
| D:Chow-surface-boundary-obstruction | refuted (the slicing inference) | Y = Bl_L P^3 with H = O(1,1)|_Y: every integral ample B != E meets each exceptional fibre, so L is in pi(B) and the boundary acquires a divisorial trace; the explicit smooth quadric x_0x_2 + x_1x_3 shows it. Re-derived the numerical argument. | independent re-proof, confirmed. **It is the explicit form of F12** (my sweep-3 analysis of the Chow step of 29/066-068): an ample section of a projective Chow modification meets the exceptional divisors over Y. |
| D:cohomology-crown-criterion (the backbone of D.1, used by 11 rows) | proved | G profinite is finitely generated iff (1) dim H^1(G,V) <= c dim V for every irreducible F_l[G]-module V and (2) the crown multiplicity delta_F(A) <= |A|^c for nonabelian chief factors. Forward direction re-derived (cocycles determined on d generators; distinct coordinate d-tuples in a crown-based power). The converse rests on the crown reduction of Lucchini-Marion-Tracey 2020 (Lemma 2.5, Prop. 2.6, with the classification of finite simple groups); its first steps read. | not read in full (forward direction confirmed); consistent with the known crown-based criteria for generation (Detomi-Lucchini; locator not opened by me). |
| D:local-complete-Lang (used by 11) | proved | two unit q-Frobenius structures on a reflexive module over a complete local ring are isomorphic: Lang's argument on the finite-dimensional residue algebra (orbit map g -> g a tau(g)^-1 with invertible differential, connected unit group), then successive approximation using tau(m^a E) in m^{qa} E. Re-derived. | independent re-proof, confirmed (needs the residue field algebraically closed, which is the run's setting). |
| D:local-surface-constant-H2 (used by 12; bridge-flagged) | proved | resolution with SNC exceptional E; Gabber's absolute purity gives R^q j_* Lambda; proper base change H^a(Y) = H^a(E); Leray: |H^2(U, Z/d)| <= d^{v + 2 sum g_i + e}; H^2(pi_1(U)) injects into H^2(U). Re-derived the three Leray terms and the injection. | targeted proof check, confirmed. |

**D.1 and D.2(ii) at statement level (253 rows).** The run proves Q(X,Y) finitely generated in the projective, char-0
and regular normal-crossings cases, and when X has a dense open identified with an open of a projective normal model
with complement of codimension >= 2 (D:codimension-one-projective-model; D:complete-toric-fixed-boundary for every
complete toric variety, where a projective fan with the same rays exists). For proper non-projective X it attacks the
two conditions of the crown criterion: (1) rank-linear H^1 is proved for proper normal surfaces with divisorial
boundary (so the maximal prosolvable quotient is finitely generated), and transferred to finite omitted loci in all
dimensions through a geometric generic surface; (2) polynomial crown multiplicity is proved for defining-characteristic
representations of quadratic rank growth and, through Brauer-zero and bounded-period projective classes, for the
classical and exceptional Lie families in the stated local and one-curve scopes. Negative rows: D:fierce-small-excess
and D:wild-genus2-single-curve (wild covers above one positive-genus exceptional curve are not automatically tame),
D:pure-root-rational-tail-obstruction, D:bounded-ramification-generation-obstruction,
D:fixed-different-unbounded-rational-chain, D:elliptic-cone-order-generators, D:A-chain-internal-framing-obstruction,
D:pronilpotent-obstruction and D:uniform-H1-obstruction (strategy obstructions, not counterexamples to D.1). Open:
D:fixed-boundary-gate (proper non-projective compactifications in general). None of these rows was read with its
proof in full; their statements are consistent with the rows read and with the crown criterion; the run records at
least one check event for every one of them. Rows: D:finite-field-surfaces, D:boundary-neighborhood, D:mutation-surfaces, D:lc-elliptic-tame, D:single-curve-residue-tameness, D:fierce-small-excess, D:Gorenstein-lc-configurations, D:cusp-tame, D:Gorenstein-lc-valuative-tame, D:prime-to-p-index-tame, D:prime-to-p-index-boundary, D:lc-exceptional-configurations, D:lc-cusp-tame, D:lc-core-valuative-tame, D:formal-torus-lift, D:graded-cone-tame, D:negative-curve-linearization, D:negative-curve-tame, D:formal-cone-mixed-boundary, D:formal-cone-fixed-boundary, D:weighted-graded-extraction, D:weighted-graded-boundary, D:schroer-all-genera, D:Schroer-horizontal-tame, D:schroer-elliptic, D:elliptic-surface-boundary, D:finite-exceptional-wild, D:Gorenstein-lc-boundary, D:rational-tree-Qfactorial, D:Qfactorial-partial-resolution, D:surface-mixed-boundary, D:lc-surface-boundary, D:mixed-fixed-boundary, D:finite-regular-cover, D:local-purity-boundary, D:finite-local-groups, D:finite-local-images-arbitrary, D:klt-threefold-boundary, D:finite-local-images, D:codim-two-small, D:fixed-boundary-small, D:vertical-fibration-exact, D:vertical-fibration-multiplicity, D:surface-map-to-curve, D:vertical-fibration-models, D:log-fibration-criterion, D:surface-map-all-boundaries, D:generic-fibre-generation, D:vertical-boundary-all-dimensions, D:projective-generic-normalization, D:residual-inseparability-bound, D:projective-base-generation, D:projective-image-corollaries, D:hereditary-base-generation, D:iterated-fibration-generation, D:proper-log-finite-generation, D:log-regular-boundary, D:generically-finite-projective-target, D:wild-genus2-single-curve, D:wild-genus2-source, D:wild-genus2-pro2, D:finite-formal-cone-cover, D:finite-cone-wild-bound, D:negative-curve-finite-wild, D:torsion-first-obstruction-cover, D:negative-curve-equality-finite-wild, D:wild-genus2-finite-inertia, D:formal-retraction-cone-cover, D:formal-retraction-tame, D:finite-jet-cone-cover, D:split-first-neighborhood-finite-wild, D:finite-cone-mixed-boundary, D:finite-cone-fixed-boundary, D:pronilpotent-obstruction, D:uniform-H1-obstruction, D:fixed-vs-valuation, D:pure-root-rational-tail-obstruction, D:fixed-boundary-gate, D:different-conductor-bound, D:surface-uniform-different, D:fixed-boundary-uniform-different, D:surface-uniform-conductor, D:psl2-bounded-conductor-covers, D:bounded-ramification-generation-obstruction, D:surface-curvewise-conductor, D:local-p-linear-H1, D:unit-reflexive-linear-cohomology, D:punctured-surface-all-characteristics-H1, D:Kummer-uniform-Frobenius-defect, D:local-tame-p-linear-H1, D:tame-boundary-summed-index, D:tame-canonical-Euler, D:tame-canonical-linear-cohomology, D:tame-surface-all-characteristics-H1, D:local-surface-reduction, D:relative-Noether-different-jets, D:relative-Artin-module-realization, D:quadratic-cyclic-Frobenius-witnesses, D:uniform-local-representation-growth, D:uniform-local-growth-all-dimensions, D:local-reflexive-constructible-atlas, D:effective-constructible-quotient, D:constructible-periodic-count, D:local-fixed-rank-representation-growth, D:bounded-matrix-simple-product, D:global-periodic-reflexive-boundedness, D:surface-fixed-rank-representation-growth, D:polynomial-monad-diagrams, D:global-quadratic-representation-bound, D:tame-parabolic-boundedness, D:tame-parabolic-fixed-rank-growth, D:quadratic-growth-alternating-obstruction, D:persistent-first-neighborhood, D:surface-residual-genus-bound, D:saturated-boundary-two-sided-slopes, D:cover-uniform-MCM-annihilator, D:fixed-different-unbounded-rational-chain, D:proper-curve-arithmetic-defect, D:cover-uniform-relative-jets, D:filtered-linear-curve-resolution, D:filtered-polynomial-diagrams, D:tame-global-quadratic-representation-bound, D:surface-tame-cross-characteristic-H2, D:surface-tame-central-obstructions, D:bounded-centre-projective-growth, D:surface-bounded-centre-simple-product, D:nonnormal-bounded-centre-projective-growth, D:local-bounded-central-obstructions, D:strict-local-open-cohomology-finite, D:bounded-scalar-projective-growth, D:bounded-centre-unitary-simple-product, D:local-bounded-scalar-simple-product, D:symplectic-orthogonal-simple-product, D:exceptional-arithmetic-genus-bound, D:normalization-Frobenius-saturation, D:exceptional-degree-linear-core, D:superperfect-quadratic-obstruction, D:contract-zero-cost-blocks, D:RDP-uniform-local-generators, D:RDP-branch-gluing-obstruction, D:generic-surface-finite-punctures, D:normal-finite-puncture-quantitative-transfer, D:nonnormal-finite-puncture-quantitative-transfer, D:generic-surface-controlled-boundary, D:nonnormal-controlled-boundary-quantitative-transfer, D:weighted-exceptional-chain-compression, D:codimension-one-projective-model, D:complete-toric-fixed-boundary, D:punctured-cover-linear-resolution, D:finite-normal-tame-descent, D:cover-uniform-canonical-defect, D:cover-thickening-linear-cohomology, D:cover-uniform-Noether-different, D:exceptional-weighted-genus, D:local-Eisenstein-linear-atlas, D:local-branch-data-linear-complexity, D:RDP-full-sheaf-degree, D:unpointed-Eisenstein-witness, D:fixed-formal-curve-fibre-bound, D:exceptional-canonical-energy, D:punctured-cover-linear-energy, D:elliptic-cone-order-generators, D:integral-antinef-energy-cycle, D:punctured-cover-antinef-cycle, D:fixed-tensor-boundary-comparison, D:finite-tensor-cyclic-quadratic-atlas, D:Brauer-zero-projective-representation-growth, D:RDP-full-Hom-vanishing, D:A-chain-two-end-Hom-bound, D:A-chain-internal-framing-obstruction, D:Brauer-zero-detecting-surface-transfer, D:Brauer-zero-normalization-transfer, D:A-chain-finite-jet-framing, D:A-block-total-jet-budget, D:RDP-Artinian-full-bundle-framing, D:local-Picard-prime-to-p-generators, D:local-fixed-tensor-cyclic-atlas, D:local-Brauer-zero-projective-growth, D:Brauer-zero-selected-simple-product, D:local-Brauer-zero-surface-transfer, D:one-variable-residue-primitive, D:sparse-DVR-linear-atlas, D:sparse-DVR-normalized-different-complexity, D:bounded-geometric-Brauer-period, D:bounded-Brauer-period-selected-simple-product, D:reflexive-pullback-uniform-generation, D:hereditary-fixed-determinant-cycle-chart, D:single-curve-Brauer-residue-cover, D:canonical-pullback-uniform-jet-loss, D:canonical-module-two-level-recovery, D:energy-controlled-reduction-cycle, D:reduction-cycle-full-module-correspondence, D:single-curve-Cartier-parameter-ideal, D:single-curve-Cartier-module-jet-recovery, D:residual-twisted-spectral-category, D:residual-twisted-Frobenius-transport, D:Artinian-full-neighbourhood-realization, D:Artinian-canonical-two-level-jets, D:fixed-determinant-finite-Hom, D:twisted-connected-anchor-minimal-slopes, D:twisted-period-independent-normal-depth, D:weighted-affine-component-bound, D:weighted-normal-layer-budget, D:weighted-normal-layer-background-budget, D:weighted-fixed-residual-bundle-deformations, D:weighted-fixed-determinant-normal-presentation, D:compressed-minor-background-charts, D:moving-line-polynomial-background, D:one-curve-coefficient-root-gerbe, D:meromorphic-unit-jet-contraction, D:finite-jet-unit-Isom, D:controlled-one-curve-gerbe-anchors, D:one-curve-unbounded-period-projective-count, D:unramified-semilinear-determinant-budget, D:etale-resolution-hereditary-linear-count, D:unramified-permutation-linear-crowns, D:twisted-deck-Frobenius-semilinear-model, D:etale-resolution-semilinear-count, D:unramified-field-permutation-crowns, D:radial-tame-cover-one-curve, D:one-curve-radial-tame-generators, D:tame-resolution-hereditary-linear-count, D:tame-resolution-semilinear-count, D:tame-field-permutation-crowns, D:SNC-tree-Brauer-geometry, D:SNC-tree-residual-category, D:SNC-tree-minimal-marked-windows, D:SNC-tree-uniform-Hom-depth, D:radial-tame-cyclic-H2, D:fixed-partial-resolution-unit-atlas, D:tame-hereditary-projective-count, D:nonsplit-automorphism-wreath-lifts, D:bounded-graph-projective-crown-reduction, D:bounded-field-automorphism-crowns, D:SNC-tree-small-marked-source, D:SNC-tree-fixed-normal-presentation, D:SNC-tree-finite-unit-comparison, D:SNC-tree-projective-quadratic-count, D:coherent-full-root-coefficient-gerbe, D:single-sector-root-compression, D:compressed-skew-Frobenius-unit-jets, D:tame-projective-semilinear-count, D:tame-projective-automorphism-crowns, D:normal-subgroup-projective-crowns, D:SNC-general-Brauer-geometry, D:SNC-general-residual-category, D:classical-defining-characteristic-crowns, D:SNC-general-weighted-presentation, D:SNC-general-projective-quadratic-count, D:complete-local-projective-growth-all-dimensions, D:exceptional-defining-characteristic-crowns, D:one-curve-wild-swap-cover, D:wild-swap-exact-image.

**Verdict for D.1 and D.2(ii) as a whole:** settled for projective X (and char 0, regular NC, toric, and the
codimension-one-projective case); open in general for proper non-projective X in characteristic p, where the run has
proved condition (1) of its crown criterion for surfaces and large parts of condition (2), not all of it.

#### D.3 to D.6 (29/098, 29/116, 29/180, 29/041)

| row | the run's status | my check | verdict |
|---|---|---|---|
| D:arithmetic-invertible | known | Schmidt, "Rings of integers of type K(pi,1)" (Doc. Math. 2007), Prop. 2.3 and 2.1: Spec O_K - S is a pro-l K(pi,1) when S contains the places above l (locator not opened by me). | carried as background without fault found. |
| D:arithmetic-tame (D.3, "Mais qu'est Pi_2^t(X_0/D'_0) ???" on 29/098) | proved | every positive-degree F_l-class on a tame cover Y of U = X_0 - D (l invertible on X_0) dies in a finite l-power cover, which is tame along D because l differs from the residue characteristics there; so H^q(pi_1^t, M) = H^q(U, M) for permitted coefficients, and Pi_2^{t,L} = 0. Re-derived the argument. | targeted proof check, confirmed. **His question of 29/098 is answered in the permitted-coefficient convention of 29/088: Pi_2^t(Spec Z - S) = 0, with allowed primes exactly S**; this was my sweep-3 hunch 4 (Schmidt). |
| D:vanishing-conjugacy (D.4, 29/116) | known with an integral deduction | Deligne, Weil II, Cor. 4.2.7(ii) (as cited: char 2, dim X odd, sufficiently general pencil; locator not opened by me), then: r_delta - 1 has image Z_l delta (2 a unit), conjugate reflections send delta to u delta' with u^2 = 1, and r_delta'(delta') = -delta' handles the sign. Re-derived the deduction. | targeted proof check of the deduction, confirmed; the input carried as background. **His open question of 29/116 ("j'ignore si elle reste vraie pour un pinceau général") was answered by Deligne in 1980 for sufficiently general pencils.** |
| D:proper-descent (D.5, 29/180) | known | Rydh 2010, Th. 5.19(ii): effective descent of étale algebraic spaces along proper surjective maps of noetherian schemes, any discrete G. | carried as background without fault found. |
| D:prime-to-p (D.6, 29/041 1 b)) | known | Orgogozo 2003, Th. 4.11: pi'_1 of a connected finite-type scheme over a separably closed field is finitely presented, by alterations. | carried as background without fault found. **The "présentation finie" of 29/041 1 b) is a theorem without resolution** (my sweep-3 hunch 8). |

#### D.7 to D.10 (29/180-217 and cote 31; 23 rows at statement level)
D:alpha-counterexample, D:alpha-geometric-counterexample, D:alpha-products-image, D:alpha-products-finite, D:alpha-strict-filtering, D:alpha-common-refinement, D:root-stacks, D:prop5, D:prop5-counterexample, D:prop5-completion, D:G5-Zsets, D:nominal-orbits, D:G5-Hom-finite, D:G5-uniform-Hom, D:wild-units, D:wild-GLn, D:tame-GLn, D:boundary-criterion, D:boundary-arbitrary, D:boundary-nonconstructible, D:curve-Swan, D:tame-sufficient, D:boundary-cancellation. These answer questions on pages outside my sweep-3 stretch (29/141-217 was read by reader B; cote 31 by
reader B and the lead): 29/207 ("Prouvons que alpha est essentiellement surjectif": refuted for a fixed sieve, exact
image and finite-product replacement proved), the unwritten Proposition 5 (unqualified version refuted, finite version
proved), 29/212 (G5: G0-G4 do not imply it, even with finite Hom sets; a uniform relative Hom criterion is equivalent),
31/044 (wild injectivity refuted for units and for GL_n in every rank; tame cyclic comparison proved) and 31/101 (an
exact boundary-hypercohomology criterion for local constancy of R^i h_* G; specialization isomorphisms and pointwise
cancellation refuted; constant total Swan conductor suffices on curves; relative tameness sufficient, SGA 7 XIII). Not
read with proofs; the run records check events for all of them.

### 1E. Verdict counts (rows read in full or partly: 51 of 404)

- **Confirmed by my check (37):** part A 10, part B 13, part C 7, part D 7. Among them 15 of the run's refutations
  (A:realcone, A:mixedreal, A:nagata-global-consequences, A:nagata-local-consequences, A:double-trait,
  A:A2-persistent-arithmetic-counterexample, A:wild-affine-counterexample, B.1a, B.3a, C:cusp-all-subgroups,
  C:normal-counterexample, C:etale-nonseparated, C:non-sheaf, D:kernel-counterexample,
  D:Chow-surface-boundary-obstruction). A:wild-affine-counterexample is confirmed conditional on the cited Kato
  filtration identifications.
- **Carried as background without fault found (11):** A:basic, A:general-upper, A:hens-affine-unit, A:artin-NB,
  A:wild-generic-open, A:nagata, B.1b (its alpha_p and Z/p cases re-proved), D:kernel-regular,
  D:arithmetic-invertible, D:proper-descent, D:prime-to-p.
- **Not read in full (3):** B.2g (structure read; rests on B.2e, B.2f), C:etale-moduli (first half read),
  D:cohomology-crown-criterion (forward direction confirmed).
- **Gaps found: 0. Refuted by me: 0.** No row I read is wrong.
- **At statement level (353 rows):** 45 in part A, 25 in part B, 7 in part C, 276 in part D. Their statements are
  consistent with the rows read in full; the run records at least one check event for all but 24 of the 404 rows.

## 2. What is new

Against the literature (as far as I know; the run claims no priority anywhere, and I did no literature search beyond
the run's citations):
1. **A:A2-persistent-arithmetic-counterexample**: an excellent Dedekind domain of characteristic 0 with cd_2(Frac) = 1
   and cd_2(U) = 2 for every nonempty open U, built from a tower of quadratic steps with group V wr C_2 that keep every
   ideal class mod 2 and double the 2-rank. I know no published example of this persistence. It refutes Conjecture 1°
   of 31/085 and his margin "égalité pour les ouverts assez petits ?" with no real residue field.
2. **A:wild-affine-counterexample**: H^3(Spec W(Fbar_2)[[t]][1/t], F_2) != 0, so Conjecture 4° fails in residue
   characteristic p even for excellent regular complete local rings. The run says Gabber's 2015 lecture pointed to it.
3. **L6c**: R^1 f_* O_X = 0 for every proper birational f from a normal to a regular noetherian scheme in
   characteristic p, without resolution (purity of alpha_p- and Z/p-torsors plus a semilinear fixed-point lemma).
   For smooth X this is Chatzistamatiou-Rülling; for normal X I know no source.
4. **B.1, B.2, B.2g**: Grothendieck's birational invariance of Pic^tau (29/071) holds in characteristic p (finite flat
   torsor purity, Raynaud's duality and detection by finite subgroups); h^1(O) is bounded over all proper normal models
   of K/k (one generic curve detects H^1(O) of every modification); the full Pic^tau system is essentially constant
   over kbar (B.2g, via de Jong; B.2e, B.2f not read in full).
5. **C**: the separation of 29/139 (false) from 29/141 (true under its written hypotheses), the regular-base
   counterexample over A^2, and the two answers to 29/131 (non-separated étale moduli; a class functor that is not a
   sheaf) are new as written.
6. **D**: the run identifies known answers to 29/041 (Orgogozo 2003), 29/098 (Schmidt 2007, extended to tame
   covers), 29/116 (Deligne, Weil II), 29/180 (Rydh 2010); it proves the projective case of 29/061 and 29/066; it
   refutes the literal margin question of 29/066 with an affine surface; the D.1 programme (crown criterion,
   representation growth, local surface punctures) is a large body of partial results, not read by me with proofs.

Against our own results (c29a.md, my sweep-3 reading of 29/002-140):
- Confirmed and closed: the Pic^tau gap (B.1a is my example; B.1 and L6 close it, and my hunch 2 that the theorem is
  true holds); the rank formula (B.3a); the projective case of 29/066 and the Chow obstruction F12
  (D:fixed-boundary-positive, D:Chow-surface-boundary-obstruction); Proposition 4 (my refined statement is exactly
  C:literal-141, and C:normal-counterexample shows regularity of S does not help for S-morphisms).
- My hunches 4 (Schmidt for Pi_2^t) and 8 (Orgogozo for 29/041) are confirmed by D.3 and D.6. Hunch 3 (pi_1 of a
  proper non-projective Z minus codimension two) stays open: it is the run's D:fixed-boundary-gate.

## 3. Implications

**For the reading of the archive (corrections to the edition notes, by cote and scan):**
- **31/085-087** (reader B's and the lead's stretch): Conjecture 1° and its margin are false (A.1, A.2), the unnumbered
  conjecture and 2° are false through real residue fields, 4° is false in residue characteristic p and without
  quasi-excellence, and true in residue characteristic 0 (Artin, SGA 4 XIX 6.2). **31/080** "Th": A.7(i) true over a
  quasi-excellent base (Gabber), false otherwise; the nonaffine clauses need separatedness. **31/082**: refuted.
  **31/070, 31/023**: proved, with the exact real-field exception.
- **29/071-077** (my stretch): the theorem of 071 is true in characteristic p; the inference on 072 is false (alpha_p
  in alpha_{p^2}); the Question of 075 is answered (h^1(O) bounded; Pic^tau essentially constant over kbar); 077's
  request for a proof without pi_1 is met (B.3); 076's rank formula needs l != p. The c29a.md notes stand, with "the
  theorem holds (RESEARCH_SA12 B.1, L6c)" added.
- **29/124-142**: Proposition 4 on 139 is false; it is true under the hypotheses written on 141 and in the letter's
  constant-group setting; his "Sans rigueur" (139) and his warning on 142 mark the step. **29/131**: answered.
- **29/061, 29/066**: proved for projective X; the margin kernel question is false for affine X; the non-projective
  case is open. **29/098**: Pi_2^t(Spec Z - S) = 0 for permitted coefficients. **29/116**: settled by Deligne (1980).
  **29/041**: finite presentation holds (Orgogozo). **29/180, 207, 212** and **31/044, 31/101**: answered with
  counterexamples and exact criteria (not read by me with proofs).

**For our programme:** RESEARCH_SA12 has settled A, B, C and D.2-D.10 with proofs I could check where I read them; the
one main open item is D.1 for proper non-projective X in characteristic p (D:fixed-boundary-gate), on which the run
spent most of its rows. The open item A:canonical-Iwasawa is a reduction of one A.2 instance to the odd-prime
mu-conjecture, outside the archive's question.

## 4. Bridges (corrected criterion of 20 Nov; RH and GRH cited to L. Alpöge, *Remark*, https://alpo.ge/remark.pdf, with the Lean archive, files in `Papors/Chatnotes/Zeta-Function-Foundation/literature/alpoge_rh_20261120/`; purity cited to P. Deligne, *La conjecture de Weil* I, Publ. IHÉS 43 (1974), and II, Publ. IHÉS 52 (1980))

**Rows where a bridge carries content:**
- **D:vanishing-conjugacy (D.4; flagged strong).** The row rests on Deligne, Weil II, Cor. 4.2.7(ii): conjugacy of the
  Picard-Lefschetz reflections for a sufficiently general pencil in characteristic 2, dim X odd. What it uses is the
  Lefschetz-pencil part of Weil II; the statement itself is about geometric monodromy over an algebraically closed
  field and involves no Frobenius weights, so purity enters, if at all, only through the proof of the cited corollary
  (not opened by me). Alpöge's RH and GRH carry nothing: no zeta or Dirichlet L-function occurs. The row gives back
  the integral form (signed cycles, l odd) of Deligne's statement.
- **B.3a and B.1 (Picard schemes over a finite field).** Purity gives: for a normal proper X dominating a smooth proper
  Y over F_q, H^1(Xbar, Q_l) = H^1(Ybar, Q_l) (pi_1 isomorphism by purity of the branch locus, B.1's input) is pure of
  weight 1 (Weil I, or Weil's theorem for the abelian variety Pic^0_red), so the factor P_1(T) of the zeta function of
  X equals that of Y and has its inverse roots of absolute value q^{1/2}. B.1 gives back more than ℓ-adic H^1: the
  whole group scheme Pic^tau, with its infinitesimal part, is a birational invariant, so the slope-<1 part of the
  Frobenius on the p-adic side (Dieudonné module of the p-divisible group, and the unipotent part) is the same for X
  and Y. B.3a's curve y^2 + y = x^3 over F_2 is supersingular (Frobenius trace 0 over F_2, #E(F_2) = 3): its zeta
  function satisfies Hasse's RH, and p-rank 0 is the reason the l = p formula fails. RH for zeta and Dirichlet L
  (Alpöge) carries nothing here.
- **D:arithmetic-invertible, D:arithmetic-tame (D.3).** The K(pi,1) property identifies H^i_et(O_K[1/S], Z/l^n(m))
  with the cohomology of the (tame, permitted-prime) fundamental group. These are the étale motivic-cohomology groups
  whose orders enter Lichtenbaum's formula for zeta_K(1 - m) (Bloch-Kato for Q(m); proved for abelian K through the
  main conjecture). The row gives back a group-theoretic description of those groups; GRH (Alpöge) gives nothing to it
  (the special-value formulas at negative integers are unconditional for abelian K and do not involve zeros on the
  critical line).
- **A:cyclotomic-domain, A:cyclotomic-Pic, A:Iwasawa-equivalence, A:canonical-Iwasawa, A:A2-split-tower-exclusion
  (Iwasawa theory; A.2).** The rows reduce A.2 on cyclotomic Dedekind domains to an Iwasawa mu-condition, and one
  instance to the odd-prime mu-conjecture. The mu-invariant is the p-adic divisibility of the Kubota-Leopoldt p-adic
  L-function, i.e. of the special values L(chi, 1 - n); mu = 0 is known for abelian fields (Ferrero-Washington).
  GRH (Alpöge) concerns complex zeros and gives nothing to mu; the rows give back nothing to RH.
- **A:A2-persistent-arithmetic-counterexample, A:A2-quadratic-step (class groups and Brauer groups of a tower).** By
  the analytic class number formula, h R of each F_n is the residue of zeta_{F_n} at 1 up to elementary factors;
  GRH would bound that residue above by (log log |d|)^{O(1)}, but only for Dedekind zeta functions of the F_n, which are
  not abelian over Q (wreath-product groups), so Alpöge's Dirichlet case covers only F_0 = Q(sqrt(-35)), whose class
  number 2 is unconditional. The construction needs lower bounds on 2-ranks (transfer, class field theory) and
  Chebotarev existence, not effectivity, so the link carries nothing; under GRH for the E_n one would get an explicit
  bound on the Chebotarev primes (Lagarias-Odlyzko), which the existence proof does not need.
- **A:Dedekind-Milnor-obstruction, A:Dedekind-Milnor-criterion (Milnor K-theory).** They use Galois symbols (the norm
  residue isomorphism of Merkurjev-Suslin, Rost-Voevodsky) to compute top-degree cohomology; K-theory enters as
  Milnor K-groups of residue fields. RH, GRH and purity carry nothing to these cohomological-dimension statements.

**Bridge-flagged rows where the link carries nothing (with the reason):**
- **A:nagata-local-consequences, A:hens-affine-unit, A:artin-NB, A:allresidues-lower, A:local-lower,
  A:eventual-field** (flag "weak"): the flagged string is the subscript of cd_l(k) (and d_l(k)); no Tate twist, weight
  or L-function occurs. Their content is the Galois cohomological dimension of fields and affine schemes.
- **D:local-surface-constant-H2, D:bounded-geometric-Brauer-period, D:SNC-tree-Brauer-geometry, D:radial-tame-cyclic-H2**
  (flag "strong", Tate twists): the residue field is algebraically closed, so Z/d(n) is (non-canonically) constant and
  there is no Frobenius; the rows count orders. If the base had a finite residue field, purity (Weil II) would put the
  three Leray terms of D:local-surface-constant-H2 in weights 2 (H^2(E)), 3 (H^1(E_i)(-1), E_i smooth proper) and 4
  (nodes, (-2)), and the tame inertia I = prod Z_l(1) of D:radial-tame-cyclic-H2 would carry weight -2; nothing in
  the rows' bounds uses this.
- **D:graded-cone-tame** (flag "weak"): "weight" there means the grading of a positively graded ring (a G_m-action),
  not Frobenius weights.
- **Positivity, by theme:** D:integral-antinef-energy-cycle, D:punctured-cover-antinef-cycle,
  D:exceptional-canonical-energy and the rows on exceptional configurations use the negative definiteness of the
  intersection form of an exceptional curve configuration (Mumford; Du Val), the local form of the Hodge index theorem
  for surfaces, i.e. the standard conjecture of Hodge type in dimension 2, which is a theorem. They give nothing back to
  the standard conjectures, and RH or purity give nothing to them.
- **Word coincidences found by search, carrying nothing:** "Weil" in B.2m, B.2r, B:invariant-abelian-realization,
  B:Pic-finite-constants-sheaf means Weil restriction; "Brauer period" in the D representation-growth rows means the
  period of a Brauer class of a central extension (projective representations), not a motivic period; "Kummer" in
  D:proper-log-finite-generation and D:Kummer-uniform-Frobenius-defect means mu_n-torsors over algebraically closed
  fields.

## 5. Prompt updates for a successor of RESEARCH_SA12

1. **D.1, the one main open item.** State the gate as the run leaves it: Q(X,Y) for X proper normal non-projective in
   characteristic p, Y arbitrary (D:fixed-boundary-gate). Give the successor the run's proved surface results
   (condition (1) of D:cohomology-crown-criterion for proper normal surfaces with divisorial boundary; the transfers
   by a geometric generic surface) and ask for condition (2) in full (all nonabelian chief factors, cross
   characteristic included), or a route that avoids crowns: a projective modification small over Y, or a mobile linear
   system of degree 0 on the exceptional fibres over Y (the obstruction of D:Chow-surface-boundary-obstruction), or
   alterations. Keep the ledger and the two-reviews stop of the 17 Nov rule: the run spent about 250 rows on D.1.
2. **D.2(i) in its own setting.** The kernel question of 29/066 is asked under a theorem on complements of
   codimension >= 2 in proper (projective) normal schemes; D:kernel-counterexample uses an affine X. Ask: for X proper
   (or projective) normal over kbar and Y of codimension >= 2, is ker(pi_1(X - Y) -> pi_1(X)) topologically finitely
   generated, or normally finitely generated?
3. **A.1 and A.2 for schemes of finite type.** The counterexamples are of infinite type (an infinite algebraic
   extension; Gabber's non-quasi-excellent local ring) or have real residue fields. Ask whether A.1 and A.2 hold for
   affine schemes of finite type over Z or over a field, with no real points, and to settle it.
4. **Audit B.2e and B.2f** in full (the basis of B.2g, essential constancy over kbar), and C:etale-moduli and
   C:finite-flat-stack (the positive half of 29/131).
5. **The 24 rows with no check event in the register** (12 in A, 12 in B; none in C or D) should get theirs. This
   intake supplies events for five of them: A:nagata-local-consequences, B.1d, B.3 and L6a (checked) and A:basic
   (carried as background). The other 19 are listed in 1A and 1B.
6. **Bridges:** the successor need not use RH or GRH; it should record, for any arithmetic row, whether an effective
   (GRH-conditional) Chebotarev bound would make a construction explicit, citing Alpöge for the Dirichlet case only.

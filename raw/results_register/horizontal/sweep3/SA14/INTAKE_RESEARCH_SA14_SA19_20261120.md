# Intake of RESEARCH_SA14_SA19 (cp05): the mathematics, row by row

Claude Opus 5.5 at effort max, agent a262249a0710a599b (the sweep-3 reader of cotes 43, 44, 58, 59 and 60), resumed on
20 Nov 2026 by the main session (Claude Opus 5.5 at effort max) for this intake. Brief:
`field_experts/intake_20261120/INTAKE_BRIEF.md`. The run: GPT-6 Astra (ChatGPT Pro mode), prompt
`pro_prompt_builds/RESEARCH_SA14_SA19/PROMPT.md` (drafted 19 Nov 2026 by agent a28ea31fa17dd65e1, Claude Opus 5.5 at
effort max, from the sweep-3 readings, mine among them). Check events of this intake:
`INTAKE_RESEARCH_SA14_SA19_20261120_CHECK_EVENTS.tsv` (same folder).

## 0. What was read, and the scope

- **Return read:** checkpoint 05,
  `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA14_SA19_checkpoint_05_20261120T1748Z_unzipped`
  (its report opens with "INCOMPLETE"; register `RESEARCH_SA14_SA19_results.csv`, 207 rows; paper sections
  `sections/A.tex` to `sections/K.tex`, work files under `work/`, programs under `code/`).
- **Rows:** all 207 rows of the run, in packets 18-20 (`field_experts/intake_20261120/packets/PACKET_18.tsv` to
  `PACKET_20.tsv`), read in the order of `READING_PLAN.md`: the main results and the rows others depend on first.
- **Scope (final, 20 Nov 2026 ~21:15 UTC).** Read in full, statement and proof, for Parts A-G: `sections/A.tex` to
  `sections/G.tex` and `work/root/A2_determinantal.tex`, about 150 rows. Those settled by a cited theorem are marked
  'background' (source not opened).
- **Not reached:** Parts H, I and J and the priority and register rows (about 55 rows). They were stopped under the
  coordinator's token cap and are listed in §1.H-K at statement level, with no verdict.
- **Effort:** this intake ran at effort max. It was meant to be done at effort high.
- **Earlier intakes:** none recorded for this run.
- **Verdict counts, A-G (approximate, from the tables):**
  - about 118 confirmed (refutations confirmed included);
  - about 36 background;
  - 1 false step (C2-char0, whose statement is covered by C2.D/C2.G);
  - 13 open, correctly labelled;
  - 5 with no mathematical claim;
  - 0 refuted against the run.
  - Caveat: D4o/D4s contradict published claims and need a source check.
- **Check events:** `INTAKE_RESEARCH_SA14_SA19_20261120_CHECK_EVENTS.tsv`.

## 1. Verdicts, row by row

Terms:
- **confirmed**: targeted proof check; the proof was read in full and found correct.
- **re-proved**: independent re-proof.
- **gap**: says where the gap is and what is missing.
- **refuted**: a counterexample or a false step.
- **statement level**: not read in full; what was read is said.
- **background**: a cited theorem carried without opening the source; the run's locator is repeated.

"New" is measured against the literature as far as I know it, and against our own results (the sweep-3 readings R1-R10
and the Leads). No source was opened in this intake unless that is said.

### 1.A Part A: Lefschetz for Pic in characteristic p (57:97-102)

Files: `sections/A.tex` and `work/root/A2_determinantal.tex`, both read in full.

| Row | Statement | Run status | Check in this intake | Verdict |
|---|---|---|---|---|
| A4 | Pic(X) ≅ Pic(Y_N), and 0 -> H^1(Y,U_N) -> Pic X -> Pic Y -> H^2(Y,U_N), where U_N = 1 + I/I^{N+1} is filtered by the L^{-m}\|Y | Proved | targeted proof check of: Leff(X,Y) for n >= 3 (SGA 2 XII 3.4); Pic(X̂) = lim Pic(Y_m) (the units are k^× at every level, so lim^1 = 0); the layer sequences; stabilization past N; the unit sequence on Y_N | **confirmed**. Known in substance (SGA 2 XI-XII; Hartshorne, ASAV IV). The U_N packaging is the run's. It describes the kernel as H^1(Y,U_N) and the cokernel as im δ_N; this is a description, not a closed form |
| A4b (= R4) | in char p with n >= 4, kernel and cokernel are finite and killed by p^e when p^e >= N+1; for n = 3 the kernel is a finite p-group | Proved | targeted: (1+a)^{p^e} = 1 + a^{p^e} = 1 in 1 + I/I^{N+1}; Pic(X)[p^e] is finite; the image contains the divisible group Pic^0(Y)(k), so the cokernel is a bounded quotient of NS(Y) | **confirmed**; confirms our R4 |
| A4c | if H^1 (resp. H^1 and H^2) of every L^{-m}\|Y vanishes, restriction is injective (resp. an isomorphism) | Known | targeted: the transitions are injective, resp. bijective | **confirmed**; SGA 2 XII 3.6 (the run's locator; not opened) |
| A3r | a very ample counterexample in dimension > 2 yields one on a surface | Proved | targeted: take the largest a with H^1(X,L^{-a}) != 0 and D in \|L\| by Bertini; 0 -> L^{-a-1} -> L^{-a} -> L^{-a}\|D -> 0 injects H^1, and L^a\|D is very ample | **confirmed** |
| A1r | A1 for all n >= 4 is equivalent to A1 for n = 4 | Proved | targeted: take D in \|L^d\| general with d large. H^j(X,L^{-a}) = 0 for j <= 3 and a >= d gives H^1 = H^2 = 0 on D for all L^{-md}\|D, and the same holds on Y (dim >= 4). A4c then gives vertical isomorphisms, and Y ∩ D is a smooth hyperplane section of D for L\|D | **confirmed** |
| A2b | on P^1×P^1 the diagonal has restriction kernel Z(1,-1) | Proved | computation | **confirmed**. n = 2 lies outside A2's range; the example only bounds the threshold below by 3 |
| R3 (A3t) | the Lie algebra of the scheme kernel is h·H^1(X,L^{-1}) | Proved | targeted: Lie Pic = H^1(O); left exactness; H^0(O_X) = H^0(O_Y) = k | **confirmed**; confirms our R3 (the c57 reader's) |
| R3g | the geometric generic kernel on Pic^τ is finite and connected, and nontrivial iff H^1(X,L^{-1}) != 0 | Proved | targeted: the kernel is proper; it has no ℓ-torsion (π_1 surjection, Kummer); its torsion points are defined over k; p-torsion is excluded by dlog: Pic[p] ↪ H^0(Ω^1), with the incidence argument (a k-form vanishing on the generic hyperplane vanishes) | **confirmed** |
| SA14-H1 = R3u | for X normal, the generic kernel is finite, connected and unipotent | Proved | targeted: as for R3g, with a rational dlog on X_sm. Hom(μ_p, G) = 0 follows from Hom(μ_p, Pic) = H^1(Z/p) (Raynaud 1970 6.2.1 and 6.2.3, the run's locators) and the π_1 surjection; so G has no multiplicative part and is unipotent | **confirmed**. Settles Lead SA14-H1 as he wrote it (57:100: "p-groupe fini unipotent ... purement infinitésimal") |
| A3n | an A3 example needs q_nil >= h^0(L) >= 5 | Proved (known deduction) | the deduction was read: h^0 <= 4 gives P^2 or a hypersurface in P^3, both with H^1(O) = 0. The cited theorem (Enokizono 2021, Th. 4.20) was not opened | **background**; the deduction is confirmed |
| A3s | an A3 surface is of general type, satisfies bounds on L^2, and has no W_2 lifting | Proved (known deductions) | the deductions were read. Not opened: Terakawa 1999 Th. 1.6, Zhang 2022 Th. 3.1, Langer 2011 Cor. 11.2 | **background**; consistent with the explicit A3 surface (K_S = f^*N^5) |
| A3f | for 0 <= a < ℓ, the system \|O_F(a∞)\| on the cuspidal fibre k[u^p,u^ℓ] is not an immersion | Proved | targeted: the exponents <= a < ℓ in ⟨p,ℓ⟩ are multiples of p, so every section is a polynomial in u^p | **confirmed** |
| A3R | no Raynaud polarization O(aẼ)⊗φ^*N^b with a, b > 0 is both very ample and has H^1(Z^{-1}) != 0 | Proved | targeted: (i) the connection lemma: canonical connection on F^*E, second fundamental form β != 0, horizontality kills the components of Sym^n for n < p; (ii) the degree arithmetic -(i+b)deg N < 0 and n = id-1 <= p-d; (iii) the step a -> a+1 by restriction to Ẽ; (iv) the case a < ℓ by A3f. Zheng's pushforward formula (Prop. 3.3) is carried as background | **confirmed**, modulo the cited formula. I checked that formula independently in the case A3 uses (n = 2; see A3) |
| **A3** | a smooth projective surface Y in characteristic 2 with L very ample, h^1(Y,L^{-1}) = 1, h^0(L) = 562 and h^1(O_Y) = 565; so the least dimension in A3's range is 2 | Proved | **targeted proof check of every step** (listed below) | **confirmed: proved.** The main new result of the run |
| A-CZ346ii | for smooth X -> Y, injectivity on H^0(Ω^1) gives injectivity on H^1_fppf(α_p) | Proved | targeted: H^1(Z,α_p) ↪ H^0(Z,Ω^1) via z^p = a_j and da_j; ker d = k(Z)^p | **confirmed**. Its consequence for Cotner-Zavyalov's Ex. 3.4.6(ii) is the run's reading of that paper (not opened) |
| A2D | for M != O with M^p = O, the smooth Y on which M is trivial are finitely many and form a maximal-minor locus; if that locus is nonempty, b - a >= h^0(L) - 2 | Proved | targeted: by the conormal sequence η = dlog M vanishes on such a Y, so Y is a divisorial component of Z(η); H^0(M\|Y) = ker(h: H^1(M⊗L^{-1}) -> H^1(M)); the rank is a-1 at a bad member; locally the minor ideal reduces to b-a+1 entries, and Krull's height theorem applies | **confirmed**. A finite test for a given (X, L); it does not settle A2 |
| SA14-H3 | Bhatt-de Jong gives local injectivity up to p-power torsion, not an isomorphism up to it, so the Lead's recollection is wrong | Refuted as recalled | statement level: a recollection corrected from the literature (Bhatt-de Jong 2014, Th. 0.1, not opened) | **background**. The Lead (the c57 reader's H3) is to be corrected as the run says |
| A1 | Pic(X) -> Pic(Y) is an isomorphism for n >= 4 and Y a smooth hyperplane section, with no vanishing hypothesis | Undecided | the gate was read: A1 reduces to n = 4 (A1r); a counterexample is a nonzero class in H^1 or in im δ_N of A4 on a fourfold | **open**, correctly labelled |
| A2 | his boxed "noyau nul si n >= 4", and the least dimension of universal injectivity | Undecided | the gate was read: the kernel is a finite p-group (A4b); the p-torsion test is A2D; n = 2 fails (A2b) | **open** |
| SA14-H4 | the boxed injectivity for n >= 4 (Lead) | Undecided | same as A2 | **open** |

**A3: the steps checked.**
1. **The curve C** (y^2 + y = x^15 over F_2).
   - It has genus 7 and one point ∞, with v(x) = -2 and v(y) = -15.
   - For t = y/x^8: div(t) = 7P_0 + ∞ - 8P_1.
   - x + t^{-2} = x/y (from xy^2 + x^16 = xy in char 2), of order 13 at ∞.
   - dt = x^6 dx, and div(dx) = 12∞.
2. **The extension** 0 -> O -> E -> N^3 -> 0, with N = O(2∞), given by v_0 = e_0 and v_1 = t^{-6}(e_1 - t^{-1}e_0).
   - The quotient is O(6∞).
   - It does not split: a splitting needs a function on C - ∞ with a single simple pole at ∞, which is impossible
     since 1 is a gap of ⟨2, 15⟩.
   - F^*E splits: v_1^2 + t^{-12}(x + t^{-2})v_0^2 = t^{-12}(e_1^2 + xe_0^2), and t^{-12}(x/y) is regular on V and of
     order 1 at ∞.
3. **The branch divisor and the triple cover.**
   - C'' ∈ \|O_P(2)⊗π^*N^{-6}\| (in char 2, F^*E -> Sym^2 E is linear). It is smooth (equation w^2 + x with dx != 0;
     order 1 at ∞) and disjoint from E_∞.
   - M = O_P(-1)⊗π^*N^2 and M^{-3} = O(E_∞ + C'').
   - The triple cyclic cover S is smooth (3 is invertible; the branch locus is smooth and disjoint), and H^0(O_S) = F_2.
4. **Q = O_S(2T)⊗f^*N.**
   - Q is ample: Q^3 = ψ^*(O_P(2)⊗π^*N^3), which is ample by Nakai (degree 2 on fibres, positive on horizontal curves,
     self-intersection 48).
   - The floor formula ψ_*O_S(aT) = ⊕ M^i(⌊(a+i)/3⌋E_∞), re-derived from z^3 = u.
   - f_*Q = N ⊕ N^3, globally generated, so h^0(Q) = 6.
   - ψ_*Q^{-1} is as displayed, and R^1π_*O_P(-2) = N^{-3}; so h^1(S,Q^{-1}) = h^0(C, N^{-2} ⊕ O) = 1.
   - H^1(S,Q^{-2}) = 0, re-derived directly from the floor formula: the summands give H^0(N^{-5}), H^0(N^{-3}) and
     Hom(E, N^{-1}) = 0.
   - h^1(O_S) = 7 + h^0(N) = 9; Q^2 = 16; K_S = f^*N^5; K_S·Q = 20; χ(O_S) = 1 - 9 + 6 = -2.
5. **The dimensions.** Riemann-Roch on the filtration pieces N^{b+3j} (all of degree > 2g - 2 = 12 after removing two
   points) gives h^0(P,B) = Σ_{j=0}^{6}(12 + 6j) = 210, h^0(BM) = 186 and h^0(BM^2) = 160, so h^0(Q^9) = 556.
6. **The root cover** Y = Spec ⊗_i(⊕_{r<9}Q^{-r}), over a generic basis s_i of H^0(Q^9).
   - Y is smooth: at most two branch divisors meet, transversally, and 9 is invertible.
   - ρ_*O_Y = ⊕ Q^{-Σr_i}, so H^0(O_Y) = k.
   - L = ρ^*Q is very ample. Take u one of the six old sections. S_u is a closed subscheme of an affine chart of the
     \|Q^9\|-embedding, so O(S_u) is generated by the s_i/u^9. Hence O(Y_u) = O(S_u)[z_i]/(z_i^9 - s_i/u^9) is generated
     by the z_i = t_i/u.
   - h^1(Y,L^{-1}) = h^1(S,Q^{-1}) + Σ_{Σr>=1} h^1(S,Q^{-1-Σr}) = 1. The vanishing for exponents >= 2 is the first half
     of A3R.
   - h^0(L) = 6 + 556 and h^1(O_Y) = 9 + 556.

Every step holds. The program `code/certify_A3.py` only fixes one explicit basis; the existence proof does not depend on
it, and I did not run it.

**Remark.** This is new against our results; its status in the literature was not checked here.
- Going from Raynaud's ample counterexamples to a very ample one needs nothing of Q beyond these properties:
  - Q is ample and globally generated;
  - H^1(Q^{-1}) != 0;
  - Q^m is very ample for some m prime to p.
- The reason: the summand Σr = 0 of the root cover keeps H^1(Q^{-1}).
- The run says it searched and found no published very ample surface counterexample to Kodaira vanishing for H^1. The
  trick may be folklore. Before any claim is made, a literature check should come first, for example the surveys of
  Kodaira vanishing failures in characteristic p.

### 1.B Part B: Seshadri's theorem and Question 2 (57:103-114)

File: `sections/B.tex` (= `work/bce/section_B.tex`), read in full.

| Row | Statement | Run status | Check in this intake | Verdict |
|---|---|---|---|---|
| B1 | "Seshadri without Pic" as the prompt formulated it: proper flat, geometrically integral S_2 fibres, normal base, a horizontal Weil divisor Cartier on X_η is Cartier | Refuted | targeted, on the counterexample X = Proj R[x,y,z,w]/(xy - z(z - tw)), R = k[[t]], D = V(x,z), every characteristic. Checked: the generic fibre is a smooth quadric; the special fibre is the cone xy = z^2 with only the vertex singular (also in char 2), normal and CM; D ≅ P^1_R; at the vertex, B = R[x,y,z]_{(t,x,y,z)}/(xy - z^2 + tz) has a relation of order 2, x and z are independent in m/m^2, so (x,z) needs two generators and is not invertible | **confirmed (refuted)**. The run also notes that 57:110 keeps "le foncteur de Picard essentiellement propre", which the prompt's B1 and Lead H2 dropped. Its verdict is on the prompt's formulation, not on his page |
| SA14-H2 | the same, as a Lead | Refuted as formulated | same counterexample | **confirmed (refuted as formulated)** |
| R1 | our R1: X = Spec k[[t]][x,y,z,w]/(xy - z^2 - t^2), D = V(x, z - it) | Corrected and rechecked | the sign checked: (z - it)(z + it) = z^2 + t^2, valid for char != 2 | **confirmed**. The split projective example removes the restriction on the characteristic |
| B2-sufficiency | S regular integral, f flat of finite type and a relative local complete intersection, geometric fibres R_2: every horizontal Weil divisor Cartier on X_η is Cartier | Proved with original lci hypothesis | targeted: the fibres are CM + R_2, hence normal; at points of codimension <= 3 over s != η the fibre is regular, so O_{X,x} is regular; the non-Cartier locus has codimension >= 4; at its generic point O_{X,x} is a complete intersection of dimension >= 4, hence parafactorial (SGA 2 XI 3.13(ii)) | **confirmed**. It corrects our R1's refined form: the lci hypothesis of 57:111 ("intersection complète relative de dim relative >= 3") is needed |
| B2-necessity | is R_2 necessary? | Refuted | targeted: X_1: xy - z^2 - tw^2 = 0 over k[[t]] (char != 2) has a regular total space (∂/∂t = -1 at the vertex), so every divisor is Cartier, while its special fibre is a node, not R_2 | **confirmed (refuted)**: R_2 is not necessary |
| B2-exact | an exact condition on fibres and S | Proved impossibility of a fibre-type-only criterion | targeted: X_1 and X_2: xy - z^2 - t^2w^2 = 0 have the same special and generic fibre types, and opposite answers ((x, z - itw) is not Cartier on X_2); products with P^1 give relative dimension 3. Without lci, the rank-1 2×3 determinantal cone family (a + e = tw) has R_2 (indeed R_m) fibres and the non-Cartier D = V(a,b,c). For a fixed family, criterion (B.1): ker(Cl/Pic(X) -> Cl/Pic(X_η)) = 0 | **confirmed**. The "Determine" is answered negatively (no criterion on abstract fibre types and S alone), with the per-family criterion (B.1), which is a reformulation |
| B2 | exact conditions in Question 2 and necessity of R_2 | Refuted as a fibre-type-only criterion | the three rows above | **confirmed** |
| SA14-H13 | R_2 refinement and necessity (Lead) | Proved/refuted components | the rows above | **confirmed**: sufficiency with lci proved, necessity refuted |

### 1.C Part C: the henselian questions of 1962 (57:193-194, 227-231, 272)

File: `sections/C.tex` (= `work/bce/section_C.tex` and its additions), read in full.

| Row | Statement | Run status | Check in this intake | Verdict |
|---|---|---|---|---|
| C1 | X proper over a henselization A: X̂ projective ⇒ X projective | Proved | targeted: Artin 1969 Th. 3.5 (injective with dense image; run's locator, not opened); approximate an ample bundle modulo m; ampleness on the closed fibre spreads to an open neighbourhood of the closed point (openness of relative ampleness), which is all of Spec A | **confirmed** (given Artin 3.5) |
| C3 | Pic(Y - y) = Pic(Ŷ - ŷ) at isolated singularities | Proved | statement level: Elkik 1973 III §1 Th. 3 for henselian pairs, as cited (not opened); taking J maximal | **background**; the deduction from the cited theorem is immediate |
| C2-char0 | Pic(X) = Pic(X̂) when H^1(X,O_X) has finite length, characteristic 0 | Proved in characteristic zero | targeted; **false step found**. The proof says that "the proof of Perling-Schröer Prop. 1.2 shows H^1(X, m^n O_X) = 0 for n >> 0". This is false: for X flat proper over k[[t]] with nonzero torsion H^1(O_X) (for instance a flat family of twisted cubics whose special fibre is a plane nodal cubic with an embedded point), t^n O_X ≅ O_X, so H^1(X, t^n O_X) ≅ H^1(X,O_X) != 0 for every n. The graded Rees module is finite, but its high terms need not vanish | **gap (false step)**. The statement itself is covered by C2.D (DVR, all characteristics) and C2.G (general), below |
| C2-mixed, C2-DVR | C2 over an excellent henselian DVR, every characteristic, no flatness | Proved | targeted, every step of Theorem C2.D. (i) π^e kills H^1(O_{X_n}) (e = c + d). (ii) If L\|X_n is trivial with n > e, then H^1(L)/π^n ↪ H^1(O_{X_n}), so π^eH^1(L) = 0 by Nakayama. (iii) Naturality of the connecting maps under multiplication by π^e lifts a_{n-e}. (iv) The lifted section is nowhere zero (proper image in a local base). (v) Artin density then gives surjectivity. (vi) The non-flat case by I ∩ π^N O = 0 and Milnor patching over O_{X'} ×_{O_{X'_N}} O_{X_N} | **confirmed** |
| C2 | C2 over an excellent henselian local ring of any dimension and characteristic, any proper X with H^1(O_X) of finite length (Theorem C2.G) | Proved | read in full: removal of m-power torsion by fibre-product patching; blow-up of mO_X with Stein factorization T (J = mO_T invertible); the C2.D argument chart by chart on T gives a formal line bundle M with h^*M = (π^*L)^∧, trivial mod J^{N-e}; T has H^1 and H^2 of finite length; finite determinacy on T by Perling-Schröer Prop. 1.2 / Th. 1.1 (not opened); descent from X' to X through the Stein space Y and conductor patching with (C2.G.2) | **confirmed in structure**: no false step found in the steps I checked. It rests on Perling-Schröer's finite-determinacy theorem for T (finite-length H^1 and H^2), which I did not open. Note the run's own char-0 use of the same paper (above) states a false vanishing; the C2.G use is a different statement (triviality of a formal line bundle trivial on T_q), which C2.D's argument proves when J is principal |
| SA14-H5 | all henselian claims (Lead) | Proved | the rows above | **confirmed**, with C3 as background and C2.G resting on Perling-Schröer |
| C4-cones | the cone context of 57:184-194: local Pic of S, S~, Ŝ agree modulo bounded p-power torsion | Proved in original cone context | targeted: the blow-up of the vertex is the total space of O_V(-1); the completion along E projects to V, so restriction to V is split; the kernel is filtered by subquotients of H^1(V,O_V(n)), n >= 1, finitely many nonzero, each killed by p; removing E quotients by O_V(1) on both sides; Elkik for henselian vs complete | **confirmed** (the Elkik step as background) |
| C4-general, C4, SA14-H12 | the general local NS comparison modulo p-groups | Refuted (scope-dependent) | targeted, on A = (k[x,y,z,t]/(xy - z^2 - t^2(1+t)))_m, char 3. Checked: isolated singularity (all partials vanish only at 0 in char 3); z^2 + t^2(1+t) is irreducible; (x) is prime and A[1/x] is factorial, so Cl(A) = 0 and Pic(U) = 0; s = √(1+t) in A^h, u = z - its, v = z + its with independent linear terms, Â ≅ k[[x,y,u,v]]/(xy - uv), Cl = Z, punctured Pic of A^h and Â equal to Z; H^1(U,O) = H^2_m(A) = 0 (CM, dim 3), so there is no connected part | **confirmed (refuted)**: the comparison 0 -> Z has cokernel Z, not a 3-group. The run is right that the result depends on the definition of the local NS; under Pic(U)/Pic^0(U) it is false in general and true in the cone context |

### 1.D Part D: pathologies of Pic from quotients (A×B)/Γ (57:283-297, 311)

File: `sections/D.tex` (= `work/dgj/section_D*.tex`), read in full.

| Row | Statement | Run status | Check in this intake | Verdict |
|---|---|---|---|---|
| D0-tau | Pic^τ_{X/S} ≅ Y^∨ ×_S (A^∨)^Γ for X = (A×B)/Γ, Γ acting on A by group automorphisms and on B by translations through Γ_S ⊂ B | Proved under stated hypotheses | targeted: the section j: Y -> X from 0 ∈ A splits off Pic_Y; a fixed rigidified class has a unique rigidified linearization and descends; a τ-class pulls back into Pic^0(A×B) = A^∨ × B^∨ (NS(A×B) torsion-free); the descent discrepancy is a character of Γ, removed along j since Γ^D ↪ Y^∨ is the kernel of the dual isogeny | **confirmed**. It is the corrected form of our R6 (Pic^τ part) |
| R6, D0-R6 | the unrestricted product formula Pic_X = Pic_Y × Pic_A^Γ | Refuted as stated | targeted: Γ = 1, A = B = E: the Poincaré bundle on E×E is not an exterior product (its restriction to E×{b} varies) | **confirmed (refuted)**. The hypotheses of 57:286 ("A_Γ = 0", Γ trivial on Pic^τ_B) were dropped in the prompt's R6; the c57 reading should carry them |
| D1, D1-positive, D1-negative | both signs of dim (t_{A^∨})^Γ - dim (t_A)_Γ | Proved | targeted: g(x,y) = (-x + u(y), y) is an involution; in char 2, g - 1 = [[0,du],[0,0]] and g^∨ - 1 = [[0,0],[du^∨,0]], so the difference is rank du - rank du^∨; u = F gives -1 and u = V gives +1 (E ordinary); with B = Q (y^2 + xy = x^3 + 1, P = (0,1)): h^{01} = 1 + dim (t_{A^∨})^Γ (from D0-tau) and h^{10} = 1 + dim (t_A)_Γ (étale descent of forms), so (h^{01}, h^{10}) = (2,3) and (3,2) | **confirmed**. Answers 57:287 ("> 0, ou < 0") with smooth projective threefolds |
| D1-family | variation in a smooth family | Proved | targeted: E: y^2 + txy + y = x^3 over k[[t]], Δ = 1 + t^3 (unit), ordinary generic fibre (a_1 = t), supersingular special fibre; the difference goes -1 -> 0 and +1 -> 0 | **confirmed** |
| D2, D2-flatness | a nonflat fixed group (A^∨)^Γ and a nonflat Pic^τ in a smooth projective family | Proved | targeted: A_0 = C×E, C = E^{(4)}, Γ = ⟨g, -1⟩; A_0^Γ = C[2] × H, H = ker F^2 ∩ E[2]; [-1](z) = z + tz^2 + ..., so c = t in the formal group law and [2](z) ≡ tz^2 mod z^4 (no cubic term in char 2); O_H = R[z]/(z^4, tz^2) has ranks 2 and 4; flatness of Y^∨ × G would descend to G | **confirmed**. Answers 57:288 (relative dimension 4) |
| D3, D2-specialization | no abelian subscheme with the fibrewise reduced neutral components; formation of the Picard variety does not commute with specialization | Proved | targeted: G = ker([2]x - F^2y) with (G_s^0)_red = n(E_s), n(y) = (F^2y,[2]y); ker n = H has lengths 2 and 4; an abelian subscheme would make E -> P an isogeny of constant degree | **confirmed** |
| D4-product | the product Igusa family (E×Q)/⟨(-1,+P)⟩: Pic^τ = Y^∨ × E^∨[2], flat; torsion NS Z/2 on ordinary fibres, 0 on supersingular ones | Proved under stated hypotheses | targeted: D0-tau with (E^∨)^{-1} = E^∨[2]; π_0(E[2]) | **confirmed** |
| D4-gap | different absolute tangent dimensions of a torsor and its group do not imply nonflatness | Refuted inference | targeted: P = Spec R[z]/(z^2 - e_1) over R = k[e_1..e_4]/(e_ie_j) is a μ_2-torsor (unit 1 + e_1) with cotangent dimension 4 against 5 for μ_2 × Spec R, and P(R) = ∅ | **confirmed**: the inference in the published proof (Chai, Th. 2.4) is invalid |
| D4-modular-Picvar (D4m) | over W(k), an ordinary Igusa degeneration with flat Pic^τ whose fibrewise Picard varieties do not form an abelian subscheme | Proved | targeted: Δ(y^2 + xy = x^3 + x) = -63; P = (0,0) of order 2; w ≡ 0 root of 2w^2 - w + 8 (Hensel, f' odd), Q_F = [-2:1:w] on F and fixed by negation, reducing to O; the action is free; Albanese of the fibres F_s/⟨P_F, Q_F⟩ of degree 4 generically and 2 specially; Pic^τ of degree 8 over F^∨ | **confirmed** |
| D4-first-order, D4-versal (D4o) | the universal first-order (and every Artinian) ordinary Igusa deformation has **flat** Pic^τ; the hull is W[[t,s,u,v]]/(s^2 + 2s) | Refuted (the nonflatness claim); Proved (the hull) | targeted, of the algebra: (I1) q_12^2 = q_21^2 = 1 from the lifting of σ_0 = (-1,1); (I3) (1+σ)c = (q_21, q_22 z_2^2) from [2]c_0 = (q_21, q_22) (Katz's pushout recovery, pp. 150-152, not opened); (I5)-(I7): 0 -> E^∨[2] -> G -> F^∨ -> 0 and 0 -> μ_2 -> Pic^τ -> G -> 0 are fppf exact, so Pic^τ is finite locally free of degree 8 over F^∨ | **confirmed in structure**, given Katz 1981 Th. 2.1 (not opened). It contradicts the published first-order claim (Chai-Oort §3.9(iv); Chai Th. 2.4(iii); the footnote of the 1962 Grothendieck-Mumford letter as annotated). Flatness is robust: Pic^τ is an extension of an abelian scheme by finite flat groups; what fails is the existence of R-points on the nonneutral component, not flatness. **Needs a second check by someone who opens Katz and Chai before it is stated publicly** |
| D4-supersingular (D4s) | the supersingular Igusa hull W[[t,s,u,v]]/(s^4 - ts^2 - 2s) and flat Pic^τ for every Artinian deformation | Proved | targeted: (S14) Δ(y^2 + txy + y = x^3) = t^3 - 27; (S15) the inversion -s/(1+ts+w); (S16) (w - 1)(w + 2 + ts) = s^3 - ts - 2, so the 2-torsion ideal is (s^4 - ts^2 - 2s), all re-derived. The Barsotti-Tate construction of the canonical elliptic subgroup F (Steps 2-3; Katz Th. 1.2.1, Tate 1967) and the norm elimination of q (S12) were read and found coherent | **confirmed** for the explicit equations; the p-divisible steps are **carried as background** (sources not opened) |
| D4-artin-Picvar (D4a), E4-311canonicalArtin | over k[ε], no abelian B -> Pic^τ_{X/R} lifting Pic^var_{X_0} | Refuted | targeted: by Katz's criterion (Th. 2.1(4)) a lift f: B -> A^∨ needs q_B(x, f_0^∨e_E) = q_{A^∨}(f_0 x, e_E); the left side is 1 and the right side is q_12 = 1 + ε | **confirmed (refuted)**, given Katz. Answers 57:311 ("Existence de Pic^{00} ... dans le cas Artinien") negatively in the compatible-subscheme reading |
| D2-Igusa, E4-311Igusa | "étudier la famille modulaire de la surface de Igusa" (57:311) | Proved | through D4o, D4s, D4m and D4a | **confirmed**, with D4o and D4s as above |

### 1.E Part E: the structure of Pic_{X/S} (57:21-32, 64, 73-79, 277, 308-315)

File: `sections/E.tex` (= `work/bce/section_E.tex` with its added theorems E4.N, E4.R, E4.H, E4.Q, E4.T, E4.S, H8, H10,
H11.N and H11.G), read in full. The rows below give a few register entries of `sections/K.tex` as they were read there.
Most E4 rows answer the leaves 57:308-315 one by one. Many are settled by a theorem in the literature; the run cites it
with a locator, and I did not open it. The run's own counterexamples and proofs were checked.

**The run's own constructions, checked:**

| Row(s) | Statement | Run status | Check in this intake | Verdict |
|---|---|---|---|---|
| E1, E1-literal, E4-315extension (literal) | X normal and proper over a trait with a section: every L on X_η algebraically equivalent to 0 extends | Refuted as stated | targeted, on X: Y^2Z = X^3 + X^2Z + t^2Z^3 over C[[t]]. Checked: the discriminant -t^2(4 + 27t^2); the special fibre is nodal; the total space is a normal surface (isolated singularity); P = [0:t:1] lies on X, and at the node its ideal (x, y - t) has two independent linear generators, so P is not Cartier; an extension of O(P_η - O_η) would make P Cartier, since the only vertical prime is div(t) | **confirmed (refuted)** |
| E1-relative, E4-315extension (intended), E4-314normal0 | for proper flat f with geometrically normal, geometrically connected fibres and a section, the generic algebraically trivial class extends with algebraically trivial special fibre | Proved in intended valuative sense | statement level: Raynaud 1970 Th. 3.3.1 and FGA VI Th. 1.1(i), Cor. 2.3 (not opened) | **background** |
| E1-functor | the Pic^0 subfunctor is a proper algebraic space | Refuted in general | statement level: Laurent-Schröer 2024 Prop. 2.2 (Enriques), not opened | **background** |
| E2, SA14-H9, E4-313Corr | Corr_S(X,Y) is separated (hence, by Murre's Th. 4, an unramified scheme locally of finite type) | Proved | targeted: the bi-rigidified bundle defines a: X_T -> Pic_{Y_T/T} with a_η = 0; it factors through the closure E of the generic identity, which is étale (Raynaud 1970 Prop. 5.2, not opened); constancy on connected fibres and openness of the equalizer give a = 0 | **confirmed** (given Raynaud 5.2) |
| E3, SA14-H11-flattening | "Problem A": the flattening functor is a monomorphism of finite presentation | Proved | statement level: Stacks 05PS / 0CWQ (Raynaud-Gruson), not opened | **background** (known) |
| SA14-H6 | Pic/Pic^τ exists as an algebraic space when Pic^τ is flat of finite presentation; it is a separated scheme when Pic^τ is moreover closed | Proved | targeted: fppf quotient by a flat group (Stacks 06PH); the relation is open and closed, so the quotient is separated and unramified, hence a scheme (0418) | **confirmed** |
| E4-309a, 309aprime, 309adoubleprime, 3108, 3108copies | Pic a disjoint sum of finite-type schemes; closures of quasi-compact sets quasi-compact; Pic^τ closed; components of finite type; Pic = ⊔ copies of Pic^τ | Refuted | targeted: xy = tz^2 in P^2 over C[[t]] (Kleiman 2005 Ex. 4.14, split form): S_n glues copies (a,b), a + b = n, along the generic point; the closure of the generic point of S_0 contains every special point (a,-a), so Pic^τ (the copy (0,0)) is not closed | **confirmed (refuted)**; known example |
| E4-309b | the quotient scheme Pic/Pic^τ exists (57:309) | Refuted in written generality | targeted: Mumford's conic x^2 + y^2 - tz^2 over R[[t]] (Kleiman Ex. 4.14): Pic is an algebraic space, not a scheme (conjugate origins (a,b), (b,a) without a common affine neighbourhood); Pic^τ is the identity, so P/P^τ = P | **confirmed (refuted)**, given Kleiman's example |
| E4-3104 (field case), E4-3106 | multiplication by n universally open; only finitely many points killed by n | Refuted | targeted: the cuspidal cubic: Pic^0 = Pic^τ = G_a ((k[ε])^×/k^×), [p] = 0 is not open, and every point is p-torsion | **confirmed (refuted)** |
| E4-309e | Pic^τ separated when representable | Refuted even when represented | targeted, on X = (Y × Spec C[[u]])/⟨(g, u -> -u)⟩, with Y the K3 complete intersection Σ i^j X_i^2 = 0 (j = 0,1,2) in P^5 and g = diag(1,1,1,-1,-1,-1). Checked: g is free (Vandermonde columns on the fixed planes); Z = Y/g is an Enriques surface; the special fibre 2Z has H^0 = C and H^1 = 0 (H^1(Z,O) = H^1(Z,ω) = 0), so Pic is an unramified scheme; L = O(Z) has L^2 = O(div t) and L_η = O, but L\|Z = T != O | **confirmed (refuted)** |
| E4-309c, E4-313dim, E4-3103 (general) | Pic^τ universally open; dim Pic^0 constant | Refuted (non-reduced fibres) | targeted: X = Spec_V(O_V ⊕ M), M = P ⊗ O_{P^1}(-2) on E×P^1×S, S = E; f_*O = O_S; Pic_{X_s} = Pic(E×P^1) × H^1(V_s,M_s), and h^1(M_s) = 1 at s = o, 0 elsewhere (Künneth); the dimension jumps, so it is not universally open (SGA 3 VI_B 4.2) | **confirmed (refuted)** |
| E4-313dim-reduced, E4-309c (reduced) | the same with geometrically reduced fibres (E4.R) | Refuted | targeted: X = Spec_V(O_V ×_{O_D} O_V), D = 2C the split ribbon O_C ⊕ P; the fibres are reduced and connected (two copies of V_s glued along D_s); units Mayer-Vietoris gives Pic^0(X_s) = E × G_a^{h^0(E,P_s)}, of dimension 1 for s != o and 2 at o | **confirmed (refuted)** |
| E4-309f | the ℓ-rank of the Pic fibres is continuous | Refuted generally | targeted: the nodal family y^2z = x^3 + x^2z + tz^3: Pic[ℓ] has F_ℓ-dimension 2 generically and 1 on the nodal fibre (Pic^0 = G_m); positive under geometric normality (FGA VI Cor. 2.7, background) | **confirmed (refuted)** |
| E4-309g | Pic^τ_X × Pic^τ_Y ≅ Pic^τ_{X×Y} under universal H^0 = O | Proved under universal H^0 = O | targeted: a τ-correspondence gives a based map X -> Pic^0_Y[n], whose target is affine (Chevalley: an L-torsor over the finite B[n], plus nilpotents), so it is constant; openness of the equalizer in the unramified Corr. The counterexample without universal H^0 (Spec k[ε] × E) checked | **confirmed** |
| E4-3105proper, E4-3105projective (normal branch), E4-3105prime | Pic^τ proper (projective) for normal projective morphisms; universal openness implies properness | Refuted | targeted, on Theorem E4.N. Checked: A(t) has every 3×3 minor nonzero over K, and at t = 0 only columns 0,1,2 are dependent, with kernel (1,-2,1); the special fibre has four nodes, with local equation t + 6x_3^2 + 20x_4^2 + 42x_5^2, so the total space is regular; X = Y/g is flat with normal integral fibres; T_K (the Enriques canonical class) is a τ-point. Extending it to L would give q^*L ≅ O_Y with a linearization c = -1, while a pulled-back linearization is trivial at the four fixed points | **confirmed (refuted)**. The τ-part is not proper, although it is universally open (char 0) |
| E4-3103-normal-p, E4-311open, E4-311flatimp, E4-3104 (smooth family), E4-310Howard (multiplicities) | Pic^τ universally open for normal (even smooth) families in residue characteristic p; Pic^0 flat implies Pic^τ flat; [n] open; multiplicities invariant | Refuted | targeted, on Theorem E4.H, Raynaud's (1979, Astérisque 64, §4.2) Heisenberg construction made explicit. G = μ_2 × (Z/2)^2 with the cocycle (-1)^{ba'} is dihedral of order 8 generically and commutative specially. I re-derived its character functor: the commutator gives (-1)^n = 1, so n = 1 exists only over k, and Hom(G, G_m) = μ_2^2 ×_R (Spec R ⊔ Spec k). Pic^τ_X = Hom(G, G_m) since Pic^τ_Y = 0. The component μ_{2,k}^2 lies over the closed point, so the map is not open; over R/4 the neutral part μ_2^2 is flat and the τ-part is not. The realization (21 sections of L^{96} on P^23/G, Bertini and jet interpolation) was read; its Pic^τ_Y = 0 rests on Cotner-Zavyalov Th. 1.1.8(iii) (not opened) | **confirmed (refuted)**. Known phenomenon (Raynaud 1979); the explicit realization is the run's |
| E4-309bprime-fibreSmooth, E4-309bprime-defect | fibrewise smoothness of Pic^τ is open; dim Lie - dim is upper semicontinuous | Refuted | targeted, on Theorem E4.S. Checked: y^2z + txyz + tyz^2 = x^3 has Δ = t^4(1+t^2), c_4 = t^4, j = t^8/(1+t^2), so the generic fibre is ordinary, and the special fibre is the cusp; σ = [x : y + tx + tz : z] is the inversion generically and the identity at t = 0; Pic^τ = Y^∨ × G[2], with G[2] = μ_2 × Z/2 generically (nonsmooth, defect 1) and G_a specially (smooth, defect 0) | **confirmed (refuted)** |
| E4-314removeProjective, E4-314closedProjective | for proper flat f with geometrically integral fibres over any base, the locus where L is numerically trivial is open and closed, so Pic^τ is closed in Pic (Theorem E4.T) | Proved | targeted. Checked: on a regular alteration (Zheng 2009 Lemma 3.8, not opened), the matrix A_{ij} = Y_i·Y_j·H^{d-1} is negative semidefinite with kernel Qm; the vertical correction N = M + D is numerically trivial on every special component (Hodge index, Kleiman Th. 6.3(h)); Galois averaging makes a_i/m_i constant on the dominating components, so D is h-exceptional; the negativity lemma (Kollár, Families, 11.60) on ±D gives D = 0; then noetherian approximation | **confirmed in structure**, given the cited lemmas. Novelty in the literature not checked |
| SA14-H8 | 57:7-8: D -> NS(X_0) is injective | Proved with complete dimension correction | targeted: for components of dimension >= 2, ±B is f-nef with f_*B = 0, so B = 0 by the negativity lemma; for dimension 1 the kernel is generated by the closed points of the one-dimensional components (A = k[[t]] gives D = Z -> NS = 0) | **confirmed**, with the run's correction (his "I expect that this is always the case" holds in dimension >= 2) |
| SA14-H10, SA14-H10-main, SA14-H10-conormal | 57:64: in residue characteristic 0, ω_{G/S} locally free implies G smooth along the unit section; Pic^0 of a smooth projective X/S in char 0 is an abelian scheme over any base | Proved | statement level for the sources (SGA 3 VI_B 1.6; Deligne 1968 Th. 5.5, not opened); the deduction (the tangent functor R^1f_*(O ⊗ f^*M) = R^1f_*O ⊗ M is locally free, so Pic is smooth along the identity) checked | **confirmed** as a deduction from cited theorems; known (Kleiman, Remark 5.21) |
| SA14-H11, SA14-H11-affinity, SA14-H11-affinity-normal, SA14-H11-affinity-general | 57:74, 78: after shrinking a one-dimensional base, f^*: Pic_X -> Pic_{X'} is affine (H11.N normal; H11.G general) | Proved | targeted, structure. H11.G: f^* is quasi-affine of finite presentation (SGA 6 XII 1.1-1.2); the kernel K is affine after shrinking (SGA 3 VI_B 11.11); Q = P/K; v: Q -> P' is a monomorphism, fibrewise a closed immersion (SGA 3 VI_B 1.4.2), hence affine over a base of dimension <= 1 (SGA 3 XVI Lemma 4.2) | **confirmed in structure** (sources not opened) |

**Rows settled by cited theorems (statement level; sources not opened):**

| Rows | Source cited by the run | Verdict |
|---|---|---|
| E4-309d, E4-3105ft, E4-314open, E4-314locus | Laurent-Schröer 2024 Th. 2.1 (the τ-part is open of finite presentation) | **background** |
| E4-3104ft, E4-3107 | SGA 6 XIII Th. 3.6, Th. 5.1 (Kleiman Rem. 6.19, 6.28) | **background** (Known) |
| E4-3101 | FGA VI Cor. 2.3 (represented setting) | **background** |
| E4-313i | Laurent-Schröer Prop. 2.3(i) | **background** |
| E4-313ii, E4-313ntorsion | Raynaud 1970 Ex. 6.1.6, Th. 6.4.1(3), Cor. 6.4.5 (property (N)); the run's deduction for n-torsion read | **background** |
| E4-313alpha, E4-313lambda | Gille-Guralnick (arXiv 2211.09876) Th. 1.1, 4.1; the run's deduction read (B/H unipotent through Kummer lifting, upper semicontinuity of d_c) | **background**; deduction coherent |
| E4-313ellrank | counting ℓ-torsion (ℓ^{2α+μ}) in the separated étale P[ℓ] | **confirmed** |
| E4-3105projective-smooth | Laurent-Schröer 2.3(ii); Kleiman Ex. 6.18 | **background** (Known) |
| E4-309bprime-dimension, E4-309bprime-relativeSmooth | FGA VI Cor. 2.7; openness of the smooth locus | **background** (Known) |
| E4-3109 | the quotient Pic/Pic^τ over a field | **confirmed** (standard) |
| E4-311flat0 | Laurent-Schröer Prop. 2.2 (Pic^0 not flat in general) | **background** |
| E4-311canonicalReduced, E4-311NS, E4-309cflat, E4-3102 | Part D (D3; D2 and the product Igusa family) | **confirmed** through Part D |
| E4-309h | delegated to Part A | see A1, A2 |

**Rows with no mathematical claim, or open:**
- **E4-308, E4-312.** A title leaf and a tensor-product insertion; no claim to check.
- **E4-309bprime.** A reading question ("Min."/"Dim." Lissité, pale ink). Its mathematical readings are settled by E4.S and
  by FGA VI Cor. 2.7.
- **E4-3105diagram, E4-3106criterion.** Readings of 57:310 left open; I did not look at the scan. E4.H gives the failure
  of [2]-openness that the drawing "Non, exemple" suggests.
- **SA14-H7, E4-315schemeNormal, E4-315schemeIntegral, E4.** Open:
  - over a trait the Picard space is a scheme (Raynaud 3.3.1);
  - over an arbitrary base it is not settled;
  - the run correctly notes that Mumford's conic does not refute the version with integral fibres.

  These are correctly labelled.

### 1.F Part F: the local Lefschetz conjecture for π_1 (58:2-19)

File: `sections/F.tex` (= `work/fhi/F*.tex`), read in full.

| Row | Statement | Run status | Check in this intake | Verdict |
|---|---|---|---|---|
| F1 | for a complete normal local surface with algebraically closed residue field: the prime-to-p quotient is finitely presented; the pro-nilpotent quotient is finitely generated; strong F-regularity makes the group finite of order prime to p | Known | statement level: Grothendieck-Murre LNM 208 Th. 9.2; Suzuki 2023 Th. 1.2; Carvajal-Rojas-Schwede-Tucker 2018 Th. A (all not opened); the hypothesis checks were read (F-finiteness from a Cohen presentation over perfect k) | **background** |
| F1b | log terminal surfaces: the whole punctured π_1 is finite, in every characteristic | Known | statement level: Carvajal-Rojas-Yasuda 2025 Th. B / Cor. 6.4 (not opened) | **background** |
| F1c | mixed characteristic, BCM-regular pairs: finite of order prime to p, bounded by the inverse perfectoid signature | Known | statement level: Cai-Lee-Ma-Schwede-Tucker, Invent. Math. 244 (2026), Th. D / Th. 7.0.2 (not opened) | **background** |
| F2 | the consequence quoted from 58:19 for "every complete local ring" is false in dimension 1 | Refuted | targeted: for A = k[[t]] in char p, H^1(k((t)), Z/p) = k((t))/(F-1) contains the independent classes t^{-n}, p ∤ n (pole orders: g^p - g has pole order pm), so π_1 is not finitely generated | **confirmed (refuted)**. It corrects the wording of our R8: the conjecture of 58:19 is for dimension >= 2, as in SGA 2 XIII Conj. 3.1 |
| R8 | our R8: the local Lefschetz reductions and finite H^1 of open subgroups | Corrected and rechecked in stated cases | through F2 and F5 | **confirmed** with the dimension correction |
| F3 | a metabelian profinite G = V ⋊ Z_3 (V = Π L_n^n, L_n = F_{2^{f_n}}, scalar action of ζ_n of order 3^n) whose pro-nilpotent quotient is Z_3 and whose open subgroups have finitely generated abelianizations, but which is not finitely generated | Proved | targeted: [Γ,V] = V (ζ_n - 1 invertible), and coprime-order parts commute in nilpotent quotients; T = Π_{n>r}V_n ⊂ [H,H] for an open H; d generators keep the coordinates in an L_n-subspace of dimension <= d, proper for n > d | **confirmed**. It sharpens the warning of our R8 (∏A_5) to a metabelian group |
| F3b | H^1(G, M_n) ≅ L_n^n, so h^1/dim M_n = n is unbounded, against h^1(G,M) <= d·dim M for d-generated G | Proved | targeted: cocycles restricted to Γ are coboundaries; normalized cocycles are Γ-equivariant maps V -> L_n, nonzero only on V_n, L_n-linear there; no coboundaries among them | **confirmed** |
| F4 | a prosolvable G with h^1(G,M) <= C·dim M for every finite simple M has at most ⌈C⌉ + 1 generators | Proved | targeted: induction through a minimal normal M of a finite quotient F; non-generating lifts lie in complements, counted by \|Z^1(H,M)\| = \|H^1(H,M)\|·\|M\|/\|M^H\| <= \|M\|^{C+1}/ℓ < \|M\|^D, using H^1(F,M) ≅ H^1(H,M) ⊕ End_H(M) in the split case; compactness | **confirmed**. Close to known results (Gaschütz's lifting lemma; Lubotzky's formula for d(G) of finite solvable groups through h^1 of irreducible modules, J. Algebra 2001; not opened), so "new" is doubtful |
| F5 | for a complete normal local surface of char p > 0 with algebraically closed residue field, h^1(U,M) <= C_A·rank M for every F_p-local system M with abelian prime-to-p monodromy | Proved | targeted, structure. Checked: the Kummer argument b·a_i ≡ 0 mod n (b = \|det\| of the negative definite intersection matrix), so the abelian tame inertia I is finite; a fixed prime-to-p cover kills it at every exceptional divisor, and purity extends every such M over the fixed resolution; injectivity of restriction (degree prime to p); V = ⊕ L_a of degree 0 on the D_i; the uniform pole cutoff m_0 (the layers inject into negative-degree line bundles for m >= m_0); the F_p-kernel of (semilinear - injective linear) is bounded by the k-dimension; the five-term sequence with proper base change. The nearby-cycle filtration (F5.1)-(F5.2) follows Suzuki 2023 Props. 2.1, 3.1-3.4 (not opened) | **confirmed in structure**, given Suzuki's propositions. New as far as I know |
| F6 | quotients of π_1(U) that are extensions of an abelian pro-prime-to-p group by a pro-p group are finitely generated, with one bound for all; also for virtually abelian Γ | Proved | targeted: for ℓ = p, P acts trivially on a simple M, so M has abelian prime-to-p monodromy and F5 applies; for ℓ != p, H^1(P,M) = 0 gives H^1(G,M) = H^1(Γ,M^P) <= d_0·dim M (d_0 from F1); finite quotients are solvable; F4 | **confirmed** (given F5) |
| F, F-full | his conjecture of 58:19 for every complete normal local surface | Undecided | the gate read: nonabelian or p-divisible monodromy of simple modules; F6 covers pro-p-by-abelian quotients | **open**, correctly labelled |

### 1.G Part G: canonical points of the torsors Pic^δ (59:2-28)

File: `sections/G.tex` (= `work/dgj/section_G.tex`), read in full.

| Row | Statement | Run status | Check in this intake | Verdict |
|---|---|---|---|---|
| G1 | over Z[1/2], the universal T_δ = Pic^δ_{A/S} over the moduli stack of type D = (d_1 \| ... \| d_n) has a section iff r = #{i : d_i odd} <= 1 | Proved (reduction) | targeted. The symmetric classes form the torsor of quadratic refinements of b(x,y) = e_2(x, λy) on A[2] (Poonen-Rains Prop. 3.6, not opened). Existence: q = 0 if r = 0; if r = 1, q = 1 off the radical R (the odd refinement of the rank-2 quotient). Necessity: integral transvections reduce to every transvection of W = the span of the odd pairs, forcing q(v) = 1 for all v != 0 in W; for r >= 2, two orthogonal independent v, w give q(v+w) = 0 | **confirmed**. This settles our RP-S3 (c58_c60 §7), as conjectured there: the dividing line is r <= 1 |
| G2a, R9 | the box of 59:10 with typed signs: λ_L^*F_δ(L) = L^χ, so λ_δλ_δ' = [χ]; φ(δ) = -δ'; χ(δ') = χ^{n-1}, δ'' = χ^{n-2}δ | Proved under stated hypotheses | targeted: the theorem of the square and the change of variables (x,a) -> (x+a,a); cancellation of the faithfully flat isogeny | **confirmed**. Agrees with my Mukai re-proof (R9) and with the sign correction of Ex. 1 (59:9) |
| G2b, G2 | the determinant trivializations of 59:12-14 equal the canonical sections c_η = L ⊗ [-1]^*L, and for χ even with n = 2 the section of G1 | Proved | targeted: [-1]-invariance of every construction; uniqueness, because a natural section of A[2] or A^∨[2] over the degree locus is 0 (SL_2(Z) on each pair has no fixed vector mod 2), carried to char p by Mumford-Norman-Oort lifting (Oort 2014 (8.3).1, not opened) | **confirmed**. Two further slips are recorded: "ppcm" -> "pgcd" (as in our correction row), and 59:13's "χ even implies δ divisible by 2" is false (E×E, type (1,2)) |
| G3, G3-Albanese, G3-principal | c = -λ_Θ (59:24 "sans doute la symétrique" is right); K = L ⊗ [-1]^*L = c_δ; for curves K = [ω_{C/S}] | Proved | targeted: Milne Lemma 6.9 (not opened) for a^*λ_Θ = -1; uniqueness of the theta involution; Serre duality L -> ω ⊗ L^{-1} | **confirmed**. Agrees with my g = 1 computation and my re-proof of K = Ω^1 (c58_c60 §4.7-4.8). It needs no Franchetta argument |

### 1.H-K The remaining rows (not read in full; statement level)

Not reached under the token cap (20 Nov ~21:10 UTC). I read only their statements and run statuses, from the sort
(`field_experts/intake_20261120/SORTED/RESEARCH_SA14_SA19.tsv`). **No verdict** is given for them. They were not checked by
this intake. The sort records no earlier intake of this run.

- **H** (`sections/H.tex`, geometric class field theory, 43:80): H-Ga, H-all, H1-H5, H3b, H4b; SA19-H4.
- **I** (`sections/I.tex`, the residual complex, 43:45-69): I-2d, I-all, I1-I8, I-full; SA19-H3.
- **J** (`sections/J.tex` and the `work/dgj/section_J*` files, the programme of 1964, 44:2-9):
  - J0, J1-Th1 to J1-Th7;
  - J1i, J2-isomorphism, J2-positivity, J2a, J2b;
  - J6L, J6P, J6Z;
  - SA19-H5, SA19-H6.
- **Priority and register rows:** SA19-H1, SA19-H2, R10 (priority); R2, R5, R7 (carried as background by the run, not
  used); K (the register itself).

What their statuses say is in the sort. In particular:
- J1-Th7 is refuted (numerical equivalence != τ-equivalence, Bloch 1984 Th. 4.1, Griffiths), in line with the refutation
  in our c43_c44 §2.3.
- J2a and J2b (the canonical self-duality and polarization of Ab^2 for threefolds, his Th. 3-4 on 44:2) are refuted.
- I8 (a full residual endomorphism presentation for complete algebras with open-left-ideal topology) and H1/H2/H5 (Ext^{>=2}
  vanishing in Serre's category) are proved.

These are the next rows to take in.

## 2. What is new

Against the literature as far as I know it (no source opened in this intake) and against our own results:
1. **A3: a very ample counterexample to Kodaira vanishing for H^1 on a surface.** It is a smooth projective surface Y in
   characteristic 2 with L very ample and H^1(Y, L^{-1}) = F̄-dimension 1 (h^0(L) = 562, h^1(O_Y) = 565). So Grothendieck's
   infinitesimal kernel at 57:100 is nonzero for a very ample embedding, and its least dimension is 2. The method:
   - an explicit Raynaud-type triple cover S of a P^1-bundle over y^2 + y = x^15, with Q ample, globally generated,
     h^1(Q^{-1}) = 1 and h^1(Q^{-n}) = 0 for n >= 2;
   - followed by the cover by 9th roots of a generic basis of H^0(Q^9).

   The root-cover trick turns any ample, globally generated Q with H^1(Q^{-1}) != 0 into a very ample counterexample. It
   may be folklore; the literature is to be checked before any public claim.
2. **D4o/D4s: flatness of Pic^τ for every Artinian Igusa deformation.** This holds in the ordinary case (hull
   W[[t,s,u,v]]/(s^2 + 2s)) and in the supersingular case (hull W[[t,s,u,v]]/(s^4 - ts^2 - 2s)).
   - It contradicts the published first-order nonflatness (Chai-Oort §3.9(iv); Chai Th. 2.4(iii)), whose tangent-dimension
     inference D4-gap refutes with a μ_2-torsor of tangent dimension 4 under a group of tangent dimension 5.
   - What fails over k[ε] is a compatible abelian Picard subscheme (D4a), not flatness.
   - To be checked by someone who opens Katz 1981 and Chai before it is used.
3. **D1-D3: both signs of the Hodge asymmetry, and a variation.** h^{01} - h^{10} = ±1 on smooth projective threefolds
   (A×Q)/Γ in char 2, and it varies in a smooth family. There is a nonflat (A^∨)^Γ, a nonflat Pic^τ, and no abelian
   subscheme of Picard varieties. This answers 57:287-288 explicitly.
4. **Part E, explicit counterexamples to the questions of 57:308-315:**
   - E4.N: a projective family with normal integral fibres whose Pic^τ is not proper;
   - E4.R: reduced fibres with a dimension jump;
   - E4.S: fibrewise smoothness of Pic^τ is not open;
   - the Enriques multiple fibre: Pic^τ is not separated when represented;
   - E4.H: Raynaud's Heisenberg family made explicit, where Pic^τ is not open and Pic^0 flat does not imply Pic^τ flat.

   Positive results:
   - E4.T: Pic^τ is closed for geometrically integral fibres, without projectivity;
   - H11.G: f^* on Pic is affine after shrinking a one-dimensional base.
5. **Parts B and C.**
   - B: R_2 is not necessary, and fibre types cannot decide Question 2.
   - C2.D: Pic(X) = Pic(X̂) over an excellent henselian DVR, in every characteristic and without flatness.
   - C4: the local NS comparison holds for cones and fails in general (char 3, xy - z^2 - t^2(1+t)).
6. **Part F.**
   - F5: a uniform bound h^1(U, M) <= C_A·rank M for abelian prime-to-p monodromy.
   - F6: pro-p-by-abelian quotients of the local π_1 are finitely generated.
   - F3: a metabelian group showing that finite H^1 of open subgroups is not enough.
   - Partial progress on his conjecture of 58:19, which stays open.
7. **Part G: the exact answer to our RP-S3.** Pic^δ has a section over the moduli of type D iff at most one d_i is odd;
   his determinant trivializations equal the canonical ones.
8. **Corrections to our readings** (to be carried into c57 and c58_c60):
   - R1 needs the relative lci hypothesis;
   - R6's full product formula needs 57:286's hypotheses;
   - R8's conjecture is for dimension >= 2;
   - the sign of φ in Ex. 1 of 59:9 (agreed);
   - 59:13 "χ even ⇒ δ divisible by 2" is false.

## 3. Implications

**For the reading of the archive:**
- **57:97-100 (SA14-3).**
  - The boxed "noyau nul si n >= 4" and the "Question" remain open. The run reduces them to n = 4 and to an explicit
    finite obstruction H^1(Y, U_N), im δ_N.
  - His "p-groupe fini unipotent ... purement infinitésimal" holds for the geometric generic hyperplane (SA14-H1).
  - That kernel can be nonzero for a very ample embedding (A3).
  - The transcription of 57:100 (H^1(O)^{1-F}) is to be corrected to ker F, and O^×/O^{×p} (A.tex).
- **57:110-111.** His lci hypothesis is essential.
- **57:184-194.** The cone statement is right and the general extrapolation is wrong.
- **57:283-297 and 57:308-315.** Every leaf has an answer, open, or reading-dependent status (§1.D-1.E). The reading
  questions on 57:309-310 (pale "Min./Dim.", the margin diagram, the bracketed criterion) need a look at the scans.
- **58:19.** The conjecture stands for dimension >= 2, with F5/F6 as the strongest partial results.
- **59 (SA14-14).**
  - Settled: G1-G3 settle every open point of my reading (§4.2-4.8).
  - Errata to the c58_c60 reading: the sign question of 59:24, and K = ω.
- **60:53.** R7 is carried, not rechecked, by the run.

**For the programme:**
- Part A is the live gate: a fourfold with nonzero A4 obstruction, or a proof that none exists.
- D4o should be second-checked before it is cited against Chai-Oort.
- Parts H-J of this return still need their intake.

## 4. Bridges (criterion of 20 Nov, corrected)

GRH for Dirichlet L-functions (L. Alpöge, *Remark*, https://alpo.ge/remark.pdf, with the Lean archive) is RH for the
Artin-Tate motives χ ⊗ Q(n). Deligne's purity (*La conjecture de Weil* I, II) is RH over finite fields.

**The ten flagged rows.** BRIDGE_FLAGS lists F, F3, J0, J1i, J1-Th7, J2a, J2b, J6L, J6P and J6Z as "uses
motives/Tate twists". The J rows are not read; for them the bridge is given at statement level.

**F and F3.**
- The tame part of the local π_1 is generated through Kummer theory, μ_n = Z/n(1): the Tate twist enters only as the
  coefficient of the tame characters (F5's b·a_i ≡ 0 mod n).
- No Frobenius acts here (the residue field is algebraically closed), so purity and RH give nothing.
- The question is group-theoretic: the wild, non-abelian part.
- F3 is an abstract profinite group with no zeta content.

**J1-Th7.** Numerical equivalence != τ-equivalence (Griffiths, Bloch).
- The link is to the standard conjecture D (numerical = homological equivalence) and to weights. Over F_q, purity makes
  the cycle class of an algebraic cycle land in weight 0 of H^{2i}(X)(i).
- The row gives a geometric instance where numerical and algebraic (τ-) equivalence differ in codimension 2. That bears
  on D only through Griffiths-type examples, so it carries nothing for RH.

**J0, J1i, J2a, J2b, J6L, J6P, J6Z.**
- These are algebraic representatives Ab^i and their intersection pairings.
- Weights: Ab^2(X) is the abelian variety whose ℓ-adic Tate module is the weight-1 part of H^3(X)(1) cut out by algebraic
  cycles (coniveau 1). By purity (Deligne) its Frobenius eigenvalues have absolute value q^{1/2}.
- The intersection autoduality asked in his Th. 3-4 (44:2) is the duality H^3(1) × H^3(1) -> H^6(3) = Q_ℓ(0). Its
  positivity (J2b) is a case of the Hodge-type standard conjecture on H^3.
- The run's refutations (J2a, J2b) say that the canonical isomorphism and its polarization fail as he stated them. The
  link to purity is therefore this: purity gives the weights, and the refuted positivity is a positivity statement (Hodge
  standard conjecture type) that neither RH nor purity implies.

**Other rows with Tate twists, weights or Tate modules** (not flagged):
- **R7 / 60:53 (my result μ_x = 0).**
  - Purity (Weil II 1.8.4, weight-monodromy for curves over F_q) gives the weights of α_x ≅ im(N\|V)(-1). With α_x^∨ ≅
    α_x(1+ρ), it makes each local factor self-dual of weight 1+ρ.
  - The row gives back an exact self-duality D(E^♮) = Ě^♮(1). The functional equation of L(E^♮) then has sign ε^♮ = ±1
    with δ^♮² = q^{χ^♮}.
  - This is the function-field analogue of the sign of the functional equation of L(χ ⊗ Q(n)). GRH (Alpöge) concerns the
    zeros, not the sign, so it adds nothing to the row.
- **D4o, D4s, D4a (Serre-Tate coordinates q_{ij} ∈ 1 + m on T_2A × T_2A^∨).**
  - The pairing takes values in Ĝ_m = μ_{2^∞}, a Tate twist Z_2(1).
  - Flatness of Pic^τ is a question about finite flat μ_2 versus Z/2 over Artinian bases. It carries no Frobenius weight,
    so purity gives nothing.
- **G1-G3 (the Weil pairing e_2 on A[2] with values in μ_2 = Z/2(1); theta characteristics).**
  - These are combinatorial over Z[1/2].
  - The weight of the Weil pairing (A[ℓ] × A^∨[ℓ] -> μ_ℓ, weight 2 on H^1 × H^1 -> H^2(1)) is the input of RH for abelian
    varieties over F_q (Weil). The rows use only its alternating form mod 2, so the link carries nothing.
- **A, B, C, E.**
  - These are Kodaira vanishing, Cartier divisors and the structure of Pic. They involve no L-function, zeta value or
    weight.
  - The Raynaud surfaces of A3 are wild char-p phenomena where Kodaira vanishing fails, while purity (Deligne) holds on
    them. So purity says nothing about H^1(L^{-1}).

## 5. Prompt updates (for a successor of RESEARCH_SA14_SA19)

1. **Part A.**
   - State A3 as settled and drop it.
   - Make the main item a smooth projective fourfold X with Y ∈ \|L\| and a nonzero class in H^1(Y, U_N) or im δ_N (A4),
     or a proof that none exists.
   - Supply A1r, A4b and A2D as the gate. The A3 surface times a curve, its root covers, and cyclic covers of P^4-bundles
     over it are the first candidates.
2. **D4o and D4s: a targeted check against Chai-Oort §3.9(iv) and Chai Th. 2.4.** It should open Katz 1981 Th. 2.1 and
   pp. 150-152, before the refutation of the published first-order claim is stated anywhere.
3. **Part F.** Start from F5/F6. The open gates are simple modules with nonabelian or p-divisible monodromy; a uniform h^1
   bound for them would give the prosolvable case (F4).
4. **C2-char0.** The vanishing H^1(X, m^nO_X) = 0 used there is false. Cite C2.D/C2.G instead.
5. **The reading questions on 57:309-310.** Send them to a scan check, not to a research run.
6. **Parts H-J of this return** await their intake (this intake stopped at G).

# Intake of GCT_GINEQ (prompt 27), 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (an agent launched by the main session, Claude Opus 5.5 at effort max).
The run: GPT-6 Astra (ChatGPT Pro mode), run id GCT_GINEQ-2026-11-20-R1, root and three sub-agents; the run's own
ledger says the effort setting was not exposed.

## 0. What was read

- **Return folder:** `research_returns\GCT_GINEQ_final_20261120T2340Z_unzipped` (the final; the run ended at 23:40 UTC
  before its first checkpoint was due, so there are no checkpoints).
- **Prompt as sent:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\27_GCT_GROTHENDIECK_INEQUALITY_and_tensor_norms\PROMPT.md`.
- **Read in full, with every proof:** F-01 to F-23 (all 23 findings) in `GCT_GINEQ.tex` (lines 90-1620), the
  background statements B-01 to B-09 at statement level, `QUESTIONS.tsv` (Q-01 to Q-32), `LEDGER.md`,
  `IMPLICATIONS.md`, `ID_MAP.tsv`, `README.md`.
- **Not read:** the audit notes in `audit\` (the paper controls; the ID map was used), Part III's long implications
  section beyond what IMPLICATIONS.md repeats.
- **Computations:** both of the run's scripts (`checks\check_tensor_decompositions.py`, `checks\agent_sdp_checks.py`)
  rerun from a copy: all PASS. My own script (scratchpad, `gineq\intake_check.py`) checks independently: the F-03
  spectrum of the k=1 flattening of the normalized det_3 and per_3 tensors (9 singular values, each 1/3); the F-04
  sign-average identities for n=3, exactly over Q (det and per: both true); the F-14 constant alpha for P_4, b=2 (random
  search 0.7497 against 0.75); the F-23 claim that every 2x2-minor contraction of det_3 has matrix rank 4 (true).
- **Source check:** Friedland-Lim v3 from the prompt's ZIP (`LIT_Friedland_Lim_nuclear_norm_of_tensors\main.tex`):
  the display `anidlsnrm` (lemma before Theorem 9.4) has `\|M\|_\sigma` in the denominator, and the display just
  before `eq:bdnn` reads `\|M_i\|_* <= \sqrt{rank M_i}\|M_i\|_\sigma`. Both are false as printed, as F-08 says
  (A = e (x) I_m gives m against 1; I_m gives m against sqrt m). The conclusion `eq:bdnn` is right, because its proof
  needs only the Frobenius form.
- **Literature:** one web search, for the det_4 border rank. Kim, arXiv:2510.11051, proves BR(D_4) = 12 for the
  *row* tensor, as the run's B-04 cites (HJK4). For the *polynomial* tensor det_4, Farnsworth (arXiv:1505.05079,
  Theorem 1.6) gives symmetric border rank >= 38, and I found nothing stronger.

## 1. The answer to the prompt's main question, in one paragraph

The mid-run report was right: the matrix inequality "nuclear^2 / Frobenius^2 <= rank" fails for tensors. For M_2 all
three norm ratios equal 8, while Strassen gives rank 7. Tensor powers give 8^k against 7^k, so no fixed constant,
and no power of K_G, repairs it (F-05). Three things replaced it:

1. **The valid full-norm inequality (F-01).** BR(T) >= (pi^2/HS^2)^{1/(d-1)}. It is always dominated by a mode
   flattening.
2. **Certificates on one linear map (F-02, F-12).** Nuclear/operator norm certificates on a fixed linear map
   (flattening, Koszul flattening) recover exactly that map's rank bound and no more. So they inherit the
   rank-method barriers (B-05: EGOW; Lovitz's 2N-1).
3. **Norms on the whole image (F-13, F-14).** These beat the plain flattening. The run then turned this into
   an exact algebraic reduction that needs no norm at all (F-23):

   min over 0 != u in U_{n,b} of BR(u) = BR(T_b), hence BR(T_n) >= C(n,b)^s + BR(T_b) - 1.

Grothendieck's inequality proper gives only a matrix-rank test (F-11). That test needs a dimension-dependent constant
K_G(s) and a separate upper certificate on the sign norm, and it gives nothing on the natural target matrices,
whose Grothendieck gap is 1 (F-10). **The strongest outputs of the run (F-13, F-23) are border substitution and do not
use Grothendieck's inequality at all.** The norms are one way to certify the residual minimum, and F-23 supersedes
them on the four determinant/permanent families.

## 2. Verdicts, finding by finding

Every proof below was read in full by me. "Confirmed" means a targeted proof check with no gap found.

| id | statement (short) | my check | verdict |
|---|---|---|---|
| F-01 | BR(T) >= ceil(b(T)^{1/(d-1)}), also with a, c; each <= max mode rank | orthogonal expansion over the supports, Cauchy-Schwarz, Q_T <= r^{d-1}: every step checked | confirmed |
| F-02 | linear-map nuclear/operator certificates; saturation under invertible preconditioning | singular-value inequalities; the preconditioner keeps c_Phi | confirmed |
| F-03 | flat spectra: M_n n^2 x sqrt n; D_n,P_n C(n,k) x sqrt(k!(n-k)!); polynomial C(n,k)^2 x 1/C(n,k) | block argument checked; n=3 polynomial spectra computed | confirmed (+ computation) |
| F-04 | eps, pi of the normalized det/per tensors; symmetric nuclear decompositions with n!2^{n-1}, 4^{n-1} terms | Hadamard/AM-GM; Carlen-Lieb-Loss Th. 1.1; sign-averaging identities checked by hand and exactly for n=3 | confirmed (+ computation). The 4^{n-1} decomposition is Glynn's formula; F-04 does not name it |
| F-05 | no constant C with a,b,c <= C rank on M_n, and the same along the four families | M_{2^k}: 8^k vs 7^k; A_{n+1}/A_n >= 9/8 checked; the Derksen decompositions rechecked by the run's script | confirmed |
| F-06 | W: rank 3, BR 2; T_{1/100} has rank 2 and a > 2 | eps(W) = 2/sqrt3 (FL Lemma 6.2); margin 7500/3721 > 2 | confirmed |
| F-07 | bounded-summand certificate; weights diverge for any rank-r approximation of a rank > r tensor | compactness argument | confirmed |
| F-08 | correct flattening/norm comparisons; two FL v3 displays false | checked against the FL source in the ZIP (see section 0) | confirmed, source defect confirmed |
| F-09 | SDP primal/dual directions: L <= S <= U, L/K <= Q <= U | weak duality | confirmed |
| F-10 | the unscaled sign-SDP route is trivial; natural flattenings have Q = S = sum of absolute entries | op <= Q (multilinear on the cube), Q >= HS, S >= nuclear (SVD rows); sign removal blockwise | confirmed |
| F-11 | a rank-q matrix attains S in dimension q; L > kappa_s U implies rank > s; CHSH-type example 14/5 > 2 | alternating-maximization argument checked; SOS identity f^2 - 4 = H_0 and 2 - f = (2-f)^2/4 - H_0/4 checked by hand | confirmed. The dimension-q attainment is classical (it is the reason K_G(q) is used for rank-q forms); F-11 does not cite a source for it |
| F-12 | Koszul flattening cost C(a-1,p), ceiling min(ba/(a-p), ca/(p+1)) | standard; ratios checked | confirmed (known: Landsberg-Ottaviani) |
| F-13 | border substitution: BR(T) >= q + min_{u in U} BR(u) - 1, any order b >= 2; norm form with alpha(U) | atom-span argument: dim U_nu + dim L_nu = s_nu + 1; limits in U by Grassmannian convergence; alpha = injective norm of P_U | confirmed. For b=2 and 3 factors this is Landsberg-Michalek Prop. 2.3 with a one-dimensional restriction. The arbitrary-order form is a direct extension |
| F-14 | alpha for M_n (1/n), D_n (1/b!), P_n (b!C(n,b)/n^b), polynomial det (C(n,b)/n^b), polynomial per (upper bound); bounds (strong-MM)...(strong-polyP) | stable-rank argument for alternating u; e_b Maclaurin; Cauchy-Binet; alpha for P_4 checked numerically | confirmed. Numerically n^2+n-1 for M_n is weak (LO give 2n^2-n). The permanent bound C(n,h)+1 equals Han-Song Prop. 4.1. The polynomial-det bound 38 at n=4 equals Farnsworth's BSR bound, but for CP border rank |
| F-15 | integral secant image over Z, flat; complex fiber = secant cone | subring of a domain; flat base change | confirmed |
| F-16 | Koszul maps as morphisms of locally free sheaves; minors vanish over Z | integer-coefficient identities | confirmed |
| F-17 | Hilbert-Grassmann graph closure; P(S) maps onto sigma_r(X) | properness + density | confirmed |
| F-18 | the incidence locus I_{q,s} in Gr(q,W) is closed; border rank <= r puts the image in I_{q,r-q+1} | proper projection of a zero locus | confirmed |
| F-19 | no norm is GL-invariant; the ratios vary on one orbit | e_1^d + t e_2^d | confirmed |
| F-20 | K_0 / lambda / gamma classes of source and target do not determine the rank of a map | 0 vs id; z.id; G_a extension | confirmed (elementary) |
| F-21 | constant stalks, weight 0 and the unit motive of an abstract point do not determine tensor rank | two F_q points | confirmed (elementary) |
| F-22 | Hasse/divided-power catalecticant over Z, rank C(n,k)^2 over every field | disjoint monomial supports, coefficients +-1 | confirmed |
| F-23 | min_{U_{n,b}} BR = BR(T_b); BR(T_n) >= C(n,b)^s + BR(T_b) - 1; BR(det_4), BR(per_4) >= 39; with CHL, CHuangL: det_5 >= 116, per_5 >= 115, det_6 >= 416, per_6 >= 415 | coordinate projections kill every other basis vector and preserve the chosen one; projection does not raise BR; the numbers recomputed (36+4-1; 100+17-1; 100+16-1; 400+17-1; 400+16-1) | confirmed (+ computation for the b=2 seed rank 4). The seeds BR(det_3)=17 (CHL Th. 1.2) and BR(per_3)=16 (CHuangL Th. 1.1) were carried as background; I did not open those papers |

**Background B-01..B-09:** carried at statement level; no fault found in what I could check (Derksen's norms are
consistent with Table 1; the FL locators match the ZIP source). The 2026 preprints (Han, Lovitz, Heilman-Jones-
Malavolta, Peng) were not checked by me.

**Counts:** 23 findings read in full. 23 confirmed by targeted proof check, 5 of them also by computation. No gaps,
none refuted. One source defect (FL v3) confirmed against the source.

**Two points for the record, not faults:**
- F-14's eq. (strong-D) for the row determinant, C(n,h)+b-1, is far below the known C(n,h)-type bounds of Han-Ju-Kim
  (n^n/n!). The run says so in B-04.
- In LEDGER and CHECK_EVENTS the run writes "effort not exposed". By our rule the run is "GPT-6 Astra (ChatGPT Pro
  mode)".

## 3. What is new

- **Against the literature.**
  - **The degree-4 polynomial tensors (F-23).** CP border rank of det_4 and of per_4 is at least 39, as tensors in
    (C^16)^{(x)4}. This also bounds symmetric border rank. For det_4 it improves the best published symmetric bound
    I found, 38 (Farnsworth Th. 1.6). Farnsworth's bound does not bound CP border rank.
    [Superseded: BR(det_4), BR(per_4) ≥ 42 (BR_PENCIL R-05, with R-01 multidimensional substitution and the fifth minimum
    μ_5 = 11; confirmed with an independent exhaustive enumeration in the BR_PENCIL intake). F-23's identity
    min_U BR = BR(T_b) stays as the j = 1 case, and R-01 (j = 1) re-proves F-13/F-23 with proper incidence over every
    algebraically closed field, the field translation asked for in §5.5 below. (corrected 21 Nov 2026 after the intake of
    BR_PENCIL, Claude Opus 5.5 at effort high)]
  - **Degrees 5 and 6.** det_5 >= 116 and det_6 >= 416, against Farnsworth's (1+delta_n)C(n,h)^2, which gives 107 and
    410. per_5 >= 115 and per_6 >= 415.
  - **Large n.** Farnsworth's additive term (about 4^n/n^4) overtakes F-23's (about C(n/2,n/4)^2, roughly 2^n/n). So
    F-23 is the better bound in small degrees, not asymptotically.
  - **Scope of the claim.** The run makes no priority claim. These numbers should be listed as "new as far as we
    found" until a literature check covers the post-2015 papers on det_n and perm_n border rank.
  - **Already known.** The method of F-13 is known (Landsberg-Michalek border substitution). The exact
    coordinate-restriction identity min_U BR = BR(T_b) is simple. I did not find it stated for these families.
- **Known, re-derived with exact constants.** F-01 to F-12 and F-15 to F-22 are known or elementary. F-04 recovers
  Glynn's 4^{n-1} formula as a nuclear decomposition. F-08 is a real correction to Friedland-Lim v3, two displays.
- **Against tonight's other runs.** GCT_KRON, GCT_PLETH, GCT_NSRH and ALPOGE_GCT treat representation-theoretic
  positivity. None treats tensor rank or border rank. GINEQ overlaps with none of them.
- **Against our own results.** Our earlier runs have no tensor-rank results. The Alpöge bridges (Q07) say "GCT:
  nothing changes" for the positivity side. GINEQ is consistent with that: nothing in it touches GRH.

## 4. Scope of the two proofs

No statement uses GRH in any form: not Alpöge (GRH for Dirichlet L-functions), not Masullo (Hecke/Dedekind), not more.
The paper says so at line 81, and a search of the tex and IMPLICATIONS.md finds no use. The UGC statement (B-06) is
conditional on UGC, and on P != NP when phrased as non-existence of an algorithm. The run states both. **No
statement claims more than its input gives.**

## 5. Integration: how each finding bears, and the next attack

The user's framing (21 Nov, through the coordinator): say how each finding bears on the open problems and what
attack it now makes possible, and locate exactly where a route stops.

1. **F-23 (exact residual reduction): the strongest lever.**
   - *How it bears.* It turns "certify that a flattening image avoids a secant variety" (F-18's incidence locus
     I_{q,s}) into a smaller instance of the same problem. So every new seed propagates.
   - *Attack (a): feed the recursion.* With BR(det_4) >= 39, the recursion gives BR(det_8) >= C(8,4)^2 + 38 =
     4938 at b=4, and with det_5 >= 116, BR(det_10) >= C(10,5)^2 + 115. Each certified seed (border apolarity,
     Conner-Harper-Landsberg) lifts the whole tower.
   - *Attack (b): substitute more than one dimension. This is where F-13 stops.* F-13 extracts a single vector
     u_nu in U_nu ∩ L_nu. If L_nu has dimension s - q + j, the intersection has dimension >= j. That gives
     BR(T) >= q - j + min over U' in Gr(j,U) of BR(T|U'), where T|U' is the j-dimensional pencil of residual tensors
     (Landsberg-Michalek's full substitution). The obstacle is the minimum over the Grassmannian of pencils of b x b
     minors. Koszul flattenings of such a pencil in C^j (x) E^{(x)b} are the tool that has not been tried. For
     j=2, b=2 these are pencils of quadrics of rank 4: the residual question is the classical classification of
     pencils inside the span of the 2x2 minors.
2. **F-13/F-14 (the norm certificate alpha(U)): where Grothendieck-type SDP genuinely enters.**
   - *How it bears.* alpha(U) is the largest overlap of a subspace with product vectors, the injective norm of the
     projector, in quantum terms the maximal product-state fidelity of a subspace. Upper bounds on it are exactly
     what the DPS / symmetric-extension SDP hierarchy certifies.
   - *Attack.* Certify alpha(U) for residual images where min BR is not known, that is for tensors outside the four
     families, through the DPS hierarchy with its proved convergence rates. The run's Q-30 ("no generic efficient
     SDP for residual projector norms") is the precise open row, and this is its next attack.
3. **F-02, F-10, F-11 (the barrier for Grothendieck's inequality proper).**
   - *Where the route stops.* Any certificate from Q against S on one matrix certifies only that matrix's rank, so it
     is capped by the rank-method barrier (EGOW; Lovitz 2N-1). The natural flattenings are sign-equivalent to
     nonnegative matrices (gap 1).
   - *Next attack.* Grothendieck's inequality can only help inside a nonlinear argument: either as the rounding
     certificate for alpha(U) (item 2), or on matrices with genuine sign frustration, such as Koszul flattenings,
     where K_G(s) for small s differs from 1. The run tried neither.
4. **F-19 (norms are not GL-invariant): the obstacle for GCT proper.** The det-versus-padded-permanent orbit
   problem is GL-invariant, and the norms are not. The bridge to that problem is a GL-invariant use of alpha: take
   the maximum of alpha over the orbit, which is a moment-map/Kempf-Ness quantity (the Bürgisser-Garg-Oliveira-
   Walter-Wigderson scaling framework). That is the attack that connects F-13 to orbit closures; the run does not
   name it.
5. **Grothendieck's frameworks (F-15 to F-18, F-22).**
   - *A translation the run did not state.* By F-18 the border-substitution bound is the statement that the image
     point [U] in Gr(q,W) lies in the closed locus I_{q,r-q+1}, the proper image of an incidence scheme (EGA II
     5.4-5.5). With F-22's integral catalecticant and the coordinate projections, which are morphisms of free
     Z-modules, the proof of F-23 works over every algebraically closed field, with Zariski border rank. In
     characteristic p use F-22's divided-power form of the polynomial tensors, and take the limit through the
     properness of I_{q,s}, not through Euclidean compactness. The run states F-23 only over C and R; give this
     translation in the successor.
   - *Elementary, and not in Grothendieck's language.* F-20 and F-21 are correct but elementary nonimplications.
     They close no open row of ours.
6. **Open rows of earlier runs settled or changed.**
   - *None of our earlier runs.* No earlier run of ours has a tensor-rank row.
   - *ALPOGE_GCT (prompt 23), on its tensor-norm side.* For its rows about the tensor-norm side, if any, F-05 settles
     "nuclear-norm rank bounds" in the negative and F-13/F-23 give the positive replacement.
   - *How to enter these rows.* Each should go in as: GCT_GINEQ, F-05, refutation; GCT_GINEQ, F-23, the positive
     bound.
   - *Not done here.* I did not open the ALPOGE_GCT checkpoint, so I have not checked whether such rows exist.
7. **Grothendieck's texts.**
   - *What GINEQ changes.* No cote of the Montpellier archive is concerned. The text is the published Résumé:
     catalogue CSG17; USP 1996 facsimile, printed pp. 8, 8', 59-62, one-based scan leaves 8, 9, 60-63. The reading
     it changes: the Résumé's projective/injective norms and the fundamental inequality (§4 no. 2, Th. 1-2, pp. 59-60)
     give tensor-rank information only through the image method. Their direct use as rank bounds fails (F-05).
   - *Verification.* I did not verify the scan leaves myself.
8. **Study and companion notes.** We hold no study of the Résumé.
   - *If a companion note on the Résumé is written:* one paragraph with F-05, F-13 and F-23, worded as in section 1,
     placed under §4 no. 2.
   - *For the successor prompt of 23/27 and for prompt 36 (CUE_GCT):* a background line saying "CP/Waring border-rank
     lower bounds for det/per from border substitution: GCT_GINEQ F-23; they do not bear on the padded-permanent orbit
     problem (F-19)".
9. **Our prompts 30-36.**
   - Only 36 (CUE_GCT, isolation and Noether normalization) is near this run. GINEQ's F-19 and section 4 of its
     IMPLICATIONS are background there, and it feeds nothing else.
   - Prompts 30-35 are on the RH/GRH side and untouched.

## 6. Prompt updates for a successor of GCT_GINEQ

1. **The main question.** Make the main question the substitution of more than one dimension (5.1b) on the four
   families: the minimum over Gr(j, U_{n,b}) of the border rank of the residual pencil, through Koszul flattenings
   of the pencil, with a computation at n=4, b=2, j=2. The aim is a bound above 39 for det_4 and per_4.
2. **The SDP question.** Certify alpha(U) by the DPS hierarchy, with proved error bounds, for one residual image
   outside the four families. Q-30 is the open row.
3. **Fields.** State F-23 over every algebraically closed field, using F-18 (properness) and F-22 (the integral
   catalecticant).
4. **Orbits.** Treat the orbit-invariant version of alpha (max over the GL orbit, Kempf-Ness) against F-19.
5. **Literature.** Before anything is called new, check the bounds on det_n/per_n polynomial border rank against
   the literature after Farnsworth (2015) and against Conner-Harper-Landsberg's border apolarity.
6. **Provenance.** Name the run "GPT-6 Astra (ChatGPT Pro mode)", not "effort not exposed".
7. **No minimums, no ways out.** The prompt, as before, asks for the whole task.

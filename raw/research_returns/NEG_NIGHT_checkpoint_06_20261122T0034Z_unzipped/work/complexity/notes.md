# NEG_NIGHT complexity track — working research notes

Owner: `/root/complexity`, GPT-6 Astra Pro (inherited). Effort: not exposed by runtime.
Start assigned by root: 2026-11-21 20:04:37 UTC. This is a working track, not the final package.

## Scope and premise discipline

E and A are designated input theorems. M is an unrefereed claimed input; every use of M is explicitly conditional. No consequence below treats a deterministic mildly subexponential algorithm as a polynomial algorithm or as membership in the stronger complexity class SUBEXP = intersection over epsilon > 0 of DTIME(2^(N^epsilon)). Prior CX-E01–E08 and CX-K01–K06 are background, not newly counted findings.

## Full read coverage completed

- `LIT_OpenAI_ETH_is_False/main_full_version.tex`: all 4,829 lines, including the complete Section 6 construction. The initial truncated interval was reread. This is source-reading coverage, not a Lean replay or an independent reproof of E.
- E's `quantitative-circuits.tex`, `quantitative-reduction.tex`, and all 619 lines of `quantitative-contraction.tex`: full read.
- `OURS_split_zero_corpus/01_split_zero_secondary_note.tex`: all 1,997 lines, completed before 20:13 UTC.
- `OURS_split_zero_corpus/02_split_zero_repair_dossier.tex`: all 2,300 lines, completed before 20:15 UTC.
- Prior `RETURN_CX_GRH_final_20261121T0005Z/QUESTIONS.tsv`: all 39 rows; ETH consequences, Koiran/Chebotarev and root-premise working chapters read for de-duplication.
- Hoza, *NL = UL*: all 362 extracted lines, including the full proof and references, read by 20:34 UTC. This is full source coverage, not a formal or independent validation of the theorem.

## Exact E locators

The source's theorem counter is shared among theorem, lemma, proposition, corollary, definition and remark within each section. `eth_number_map.json` records the labels and computed numbers. Key locators: Theorem 1.1; Proposition 3.4 (`prop:general-count`); Lemmas 4.7–4.8 (`lem:layout`, `lem:incidence-parameters`); Lemmas 5.1–5.2 (`lem:rational-idempotent`, `lem:total-order`); Lemmas 6.1–6.2 (`lem:sparse-checks`, `lem:greedy-hashes`); Lemma 6.3 (disjoint sparsification); Appendix B Lemma B.1; Appendix D Theorem D.1 (Boolean tensor contraction) and Lemma D.2 (sharper sparse-system counter).

The prompt quotes the weaker Theorem 2.2 core exponent n(loglog n)^2/sqrt(log n). Appendix D Lemma D.2 gives the stronger n loglog n/sqrt(log n) exponent for the same fixed-degree, linear-equation-count, polylogarithmic-sparsity interface. Section 6 can use that sharper counter.

## Corpus corrections (not novelty claims)

1. Paper01 `thm:monoid-reconstruction` and paper02's similarly named theorem omit `[tau]=0` when starting with the ordinary free monoid semiring N[M]. The displayed absorbing-addition relations leave its empty sum distinct from `[tau]`. Adjoining a second external zero to G(R) is a countermodel. Root reports that paper15's contracted monoid semiring N_0[M] already repairs this. Record as an earlier error corrected in the corpus.
2. Paper01 `prop:separated-weight-nonmultiplicative` assumes only finiteness of nonzero quotients but uses multiplicativity of N(J)=|R/J|. This requires a further hypothesis. For R=Z[2i], J=(2,2i), N(J)=2 while N(J^2)=8. Paper02 explicitly assumes a multiplicative norm and repairs this.
3. Paper01's Bernoulli expression for D_t(-m) needs a convention at m=0. Under standard B_1=-1/2, the uniform formula is [B_{m+1}(1+t)-B_{m+1}(1)]/(m+1); otherwise the printed m=0 formula gives t+1 although D_t(0)=t. Root/analytic track notified.
4. The semimodule classification is a diagram of arbitrary R-module fibers over a join-semilattice. In particular, the bottom fiber need not be zero. The sign-fixed subobject is the union of fiberwise 2-torsion, and equals the Boolean skeleton only if every fiber has no 2-torsion. Root owns the complete fixed-fiber correction.
5. A supported zero records its value and support, not whether it arose by cancellation. Root owns the provenance-loss theorem and the precise monotone-circuit formulation. Root also owns the split-determinant matching example and failure of multiplicativity.

## Primary literature newly audited

- Bürgisser, *Completeness and Reduction in Algebraic Complexity Theory*, Springer 2000, Chapter 4, Theorem 4.5(A), Corollary 4.6(1), Theorem 4.12, Remark 4.17, Theorem 4.18, Corollary 4.19, and proof of Theorem 4.5(A3), pp. 64–78. Publisher chapter: https://link.springer.com/chapter/10.1007/978-3-662-04179-6_4 . Original book text was read through its OCR reproduction: https://www.scribd.com/document/1064260688/B-Completeness-and-Reduction-in-Algebraic-Complexity-Theory-Burgisser . The journal article *Cook's versus Valiant's hypothesis*, TCS 235 (2000), 71–88, DOI 10.1016/S0304-3975(99)00183-8, was verified at the publisher abstract; do not invent its internal theorem number from the book's numbering.
- Valiant–Vazirani, TCS 47 (1986), 85–93, Theorem 1.1; Theorems 2.3–2.4; Corollaries 3.1–3.4. Author-hosted primary PDF: https://ics.uci.edu/~vazirani/ValVaz.pdf .
- Toda, SIAM J. Comput. 20 (1991), 865–877, DOI 10.1137/0220053. Publisher abstract explicitly states PH subset P^PP and PH subset BP·⊕P. Full journal theorem numbering was not recovered; cite the article's main theorem rather than fabricate a number.
- Katz, *On a theorem of Ax*, AJM 93 (1971), 485–499, Theorem 1.0 and §0.3; primary author PDF https://web.math.princeton.edu/~nmk/old/ax.pdf .
- SGA7 II, Exposé XXII, Theorem 3.1 (3.1.1) and Corollary 3.2 (3.2.1), proper schemes over F_q. Verified text: https://grothendiecksga.com/read/sga7/fr/22-3.html . This is a text edition, not an archive cote or a scanned manuscript.
- SGA5, Exposé III, §6.13: equation (6.13.2) is stated in the proper smooth case; Theorem 6.13.3 is the compact-support F_p étale version for separated finite type. Text edition https://grothendiecksga.com/read/sga5/en/III-6.html .
- SGA4 XVII, Theorem 6.2.3, relative-dimension-zero trace: verified text edition https://grothendiecksga.com/read/sga4/en/XVII-6.html . The proposed EGA IV 18.2.1–18.2.2 locator at https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html is an LLM-generated secondary translation, as root discovered; its exact original locator is PENDING original-page verification. All finite-algebra trace and base-change statements used here are proved directly by diagonal multiplication matrices and do not rely on this proposed locator. No archive cote is asserted.
- Kabanets–Impagliazzo's author page verifies the standard PIT/lower-bound disjunction: https://www.cs.sfu.ca/~kabanets/Research/poly.html . Downloaded PDF text is font-encoding corrupted; do not claim its numbered theorem was text-audited without visual inspection.
- Newly published primary preprint Chukhin–Gajulapalli–Golovnev–Mihajlin, ECCC TR26-313, 5 November 2026, *A Little Derandomization Goes a Long Way*. Theorem 1 (p.5) gives the unconditional constant-free arithmetic/NE lower-bound disjunction. Theorem 1.1 (p.3) explicitly defines NSUBEXP and recalls the strengthened PIT conditional. Theorem 8.8 and the proof of Theorem 1 are pp.46–47. https://eccc.weizmann.ac.il/report/2026/313/download/ . This result is independent background, not a deduction from E/A and not an independently verified breakthrough here.

## Active gates

- Complete, parameter-audited proofs of sparse-equation compression and its characteristic-two extension.
- Weighted arithmetic has real bit-cost: rational weights of B bits cannot be inserted into Theorem D.1 while keeping P_0=O(n) automatically. Proposition 3.4 supplies a different, weaker-exponent route for bounded-arity rational partition functions.
- Fixed algebraic weight alphabet permits P_0, ell=O(number of wires), so D.1 does yield exact fixed-gate-set amplitudes at its sharper exponent.
- Polynomial-dimensional Frobenius data would solve a hard coefficient-extraction problem; existence of a finite Weil object or of weight zero does not construct that data efficiently.
- Bürgisser's needed GRH is RH for Dedekind zeta functions of general bounded-height witness fields in the constant-elimination systems. A supplies only the abelian cases. M supplies the general family through its trivial Hecke character, conditional on M. No Artin holomorphy or normal closure is needed at this particular gate.


## Checkpoint state at 20:46 UTC

All 16 complete deduction proofs have now passed root's independent targeted mathematical review. C004 was checked against the exact D.1 interface; C003 received an explicit common-denominator and Hermite-minor bit proof before root approved it at 20:43 UTC. C014–C016 were fully read and approved in the same review. Imported E, M and recent classical input results are not claimed independently proved. C016 is a genuine symbolic family extension through Proposition 3.4 over Q[y]; it does not import the modulo-2^n readout into a Q-arithmetic circuit. C015 keeps constant-free formal degree explicit. Working TeX compilation remains blocked by missing formats/bundle access; JSON and Python generation are checked.

## Post-checkpoint movement: NN-C017

At 20:50 UTC, the full odd-characteristic extension is proved and self-checked. E Lemma5.1 already provides characteristic-independent polynomial congruences; evaluating at L^(p-1) gives p-adic indicator lifting. The same shared V order controls total degree. E Section6's graph proof extends by replacing the binary local matrix with a p-ary one, with an explicit union bound. All fixed finite fields follow by basis coordinates and valid binary encodings. The stronger AppendixD exponent is not claimed. Independent review is pending. 15668 finite checks pass.

At 20:57 UTC, NN-C018 extends the unweighted sparse equation theorem to every fixed finite commutative ring, via primary decomposition, fixed additive coordinates and binomial-digit polynomials. Integer-valued rational digit polynomials become integral after Boolean multilinear reduction, proved by finite differences. This avoids division by p modulo p. Fixed-alphabet bounded-arity weights extend over p-primary rings; arbitrary weight heights and mixed-prime coupled weights remain explicit gates. 4636 finite checks pass; independent proof review pending.

## Primary trace locator settled,21:05 UTC

The original NUMDAM scan of EGA IV4, PMIHES32(1967), printedp111/PDFpage110, was downloaded and visually checked. Paragraphs18.2.1--18.2.2 are indeed finite-free and finite-locally-free algebra trace, with base change in18.2.1.2. The tentative source removal has been superseded by this primary-page verification. Full original SHA256:b4277fb99c6edf8feec5b01f54368e4b8521bcd52871316c0edf6ff4ae69389e. No archive cote is claimed.

## Transfer gate sharpened,21:07 UTC

NN-C020 removes the formal-degree restriction from Boolean simulation when the coefficient algebra has an explicit polynomial-rank integral presentation and all Boolean outputs are bounded integers. Reduction modulo D*2^(w+1)+1 makes every denominator invertible without prime search. The full quotient algebra is retained; no rational point or residue-degree-one prime is needed. This sharply isolates the absent small presentation in the general Burgisser complex-constant transfer.


## 2026-11-21 21:21:42 UTC — proof-system and coefficient-presentation gates

C019 and C020 have now passed root's complete deduction-proof review. C021 has also passed after source audit found a printed directional omission in BGIP Corollary21: Lemma2 supplies BTS→TS under their own definition, whereas the hardness transfer needs TS→BTS. The register proves the missing reverse simulation over F4 using degree-two Lagrange indicators and explicit bounded-degree local ideal derivations. The complete primary source passages are saved in bgip01_source_excerpt.pdf/.txt and bsw01_source_excerpt.pdf/.txt. BSW locators are corrected to Lemma4.2 p155, Theorem4.4/Corollary4.5 p156, Corollary3.6 p155, and the proof in Section6.1 p161. The size-degree/3-CNF chain is explicitly stated in BGIP Corollary22's proof, printed p19.

Berkowitz's original 1982 Toronto slice manuscript was not located. The complete published primary reconstruction is Goldreich--Izsak (2012), Theorem3.1 and proof p234, saved locally; its DOI and source URL are in the source-audit message to root. Do not fabricate an original Berkowitz theorem/page number. Root independently read that proof and is using it in the split-zero circuit track.

C022 pushes the cryptographic original-witness gate: fixed locality permits arbitrarily many polynomial output constraints while retaining n seed variables. Fixed-degree predicates on logarithmic-size scopes with quasilinear output counts are separately covered by C001. Random logarithmic-locality predicates of growing degree are explicitly outside the proved interface.


## 2026-11-21 21:33:28 UTC — smaller coherent-Frobenius gate

C023 replaces the dimension-size concern in C006 by a single-entry gate: a polynomial-time, linear-size factored equation produces a degree-r hypersurface in P^(r-1) whose only nontrivial coherent group besides H0 is one-dimensional, yet its Frobenius scalar is parity-SAT. The explicit Cech calculation extends Katz's smooth formula to the singular/reducible hypersurfaces actually constructed; the original smooth hypothesis is not silently dropped. Original Katz pp35--36 and his smooth formula2.3.7.17 were visually checked and saved. Every original variable is made incident to a factor, and empty/zero-variable input cases have explicit nonzero cubic replacements. Exact integer coefficient and projective parity certificates pass (328 and86 cases respectively). Root review is pending at this timestamp.

This is movement in main question3: a low-dimensional or explicitly based coherent group is insufficient. The unresolved operation is now construction of one particular Frobenius scalar from a succinct equation. E gives subexponential evaluation; polynomial-time evaluation would give P=parity-P and NP=RP.

## 2026-11-21 21:46:51 UTC — the smooth projective gate

C023 and C024 have both passed root's complete targeted deduction-proof reading. C024 replaces F by the Fermat pencil H+uF. An explicit degree-L Jacobian minor is I+uA; its determinant has constant term one and degree at most T=binom(r(r-1),r-1). This proves generic smoothness without constructing the exponentially sized minor. An explicit quadratic tower constructs a field with b=O(r log r) bits per element, and an affine half-space sample is nonzero and smooth with probability above three quarters. The finite-field q-Frobenius scalar is c, whereas the generic absolute Frobenius coefficient is the semilinear uc. SGA7's full zeta congruence gives (1-ct)/(1-t) modulo two. Deligne's original Weil I Theorem1.6 applies to the good fibers, so genuine pure finite Weil objects exist for these counting gadgets; their existence does not calculate the single hard scalar or construct GCT's missing canonical objects.

The promise reduction first gives parity-P contained in BPP. The separately proved NP=RP implication uses isolation, amplification, SAT self-reduction and direct witness verification. Nonsmooth inputs may receive arbitrary oracle answers. This distinction has been checked by root. The generic family instead has a deterministic parity-completeness statement over F2(u). Finding a good finite-field parameter deterministically with polynomial-length field data remains open here: choosing an element of degree greater than T is valid but uses exponentially long field coordinates.

The finite arithmetic certificate finite_checks_smooth.py passes 31 tower-basis checks, 676 semilinear iteration cases, and 80 plane-cubic parameter cases, including 72 invertible Macaulay minors and 17808 projective point evaluations. It does not verify sheaf cohomology, smoothness over the entire algebraic closure, E, or the general complexity-class implications. Root separately read the exact SGA1 II4.10(iii)/4.12 text, Deligne Weil I1.6 p276 and the original Katz pages35--36.


## 2026-11-21 22:14 UTC — smooth arithmetic purity with hard multiplicity

C025 and C026 both passed root's complete deduction-proof review. C025 gives a smooth geometrically integral Artin--Schreier affine n-fold with a triangular quadratic complete-intersection presentation and exactly twice the original satisfying count. The mod-two count is always zero, while mod four retains parity. C026 supplies a deterministic smooth projective curve with exactly one plus twice the count. Its degree and genus have succinct binary descriptions but can be exponential. Its explicitly based coherent Frobenius is a coefficient-independent nilpotent shift; the pure l-adic trace still contains the hard next binary digit. The finite arithmetic certificates passed316 formulas for each construction,2122 trace-coordinate checks and4552 point cases; they do not mechanically verify cohomology.

C027 strengthens the principal purity gate much further. A single sparse cubic overZ, t^2-t=sum y_i f_i(x), is smooth with geometrically integral fibers and actual compact-support cohomology Q_l(-h)^N in degree2h plus one top Tate line. Here N is the original Boolean count. A global relative-trace map and the involution projectors establish the sheaf decomposition; positivity of its Grothendieck class is not substituted for this proof. Its arithmetic zeta is zeta(s-v-h) zeta(s-h)^N. Replacing t^2-t by t^2+1 overZ[1/2] gives the actual quadratic sign-Tate summand and zeta^(2)(s-v-h)L(s-h,chi_-4)^N. Both variants have parity of F3-point count equal to1+N modulo2. Root read the full combined proof and separately read the expanded sign-cover/global-stalk/zero-order/parity addenda, all passing.

The analytic order identities at shifted nonreal nontrivial zeros are unconditional:0<Re(rho)<1 andv>=1 suffice to make the other zeta/Euler factors nonzero. A identifies the shifted critical lines, and does not compute multiplicities. M is unused. Pure representations, smooth integral geometry, constant degree, sparse presentation, concrete sign action, and A-covered global factors therefore coexist with a counting-complete multiplicity problem. No unconditional lower bound or GCT canonical-basis identification is asserted. A temporary separate twist draft was merged into C027 before registration; there is no additional C028 finding at this checkpoint.

All C025--C027 geometry translations are now standalone AG statements, with equations and precise realizations. C027's finite check enumerated315297 assignments in28 small-field cases and verified97028 Jacobian identities. This is finite arithmetic evidence only. E still supplies an original-n subexponential evaluator, not a polynomial method for extracting the hard cohomology multiplicity.


## 2026-11-21 22:22 UTC — actual pure-representation comparison

Checkpoint03 has been saved by root and the freeze released. The additional C025--C027 standalone geometric formulations and unconditional zero-order refinements passed root's targeted reading before the freeze. C028 now transfers G015's comparison gate into actual smooth integral cubic cohomology: after parsimonious padding of coordinates and equations, the lower groups are Q_l(-H)^N with common H, and injection exists exactly when their witness counts compare. PP-hardness holds with both ranks positive; direct PP membership handles the equality case with one extra accepting path. This is an actual geometric realization comparison, not scheme containment or a map induced by a correspondence. C028 self-reading is complete; root's full independent reading is pending.

The deterministic small-field specialization issue in C024 remains open. Inspection of F=z0P shows every singular point of H+uF has z0P nonzero, but its remaining logarithmic-gradient critical-value equations still have an exponential general degree bound. No polynomial-size explicit good finite-field parameter follows from this observation, so it is not counted as movement.

C028 passed root's complete deduction-proof reading at22:23:47UTC. Root separately read Aaronson's primary strict-majority definition. All28 registered complexity deductions now have complete independent targeted readings; this does not claim formal verification or independent reproving of designated inputs.

## 2026-11-21 22:48 UTC — an ordinary ideal-certificate gate closes over Q

C029 constructs actual ordinary integral ideal multipliers, represented by rational arithmetic circuits of size poly(v) exp(O(v(loglog v)^2/sqrt(log v))), for the bounded-density quadratic Boolean-verifier systems. The preliminary multilinear first-violation coefficients are fixed-arity symbolic partition functions, so C016 applies. Their local correction uses at most eight specializations per equation and constant-size Boolean division; it avoids global multilinear expansion. A homogeneous-component construction can enforce syntactic variable degree v with constants assigned degree zero, with polynomial overhead and no PIT.

For fixed-width CNFs with O(n) clauses, the stronger original-n certificate omits Boolean axioms altogether. The first-violated-clause identity is exactly classical Grochow--Pitassi Lemma4.2, author JACM manuscript pp1:26--1:28, equations(4)--(6). This identity is credited as background. The new conclusion is its E-based subexponential circuit construction and the local lift for quadratic verifier presentations. The primary definition and complete local proof are retained in grochow_pitassi_ips_excerpt.pdf/.txt. The full author paper is newly acquired third-party material; checkpoint persistence can record its locator and checksum.

The ordinary multipliers make root's NN-S016 empty-case affine-space isomorphism effective in the same rational-circuit model. The maps are integral polynomials of degrees at most v+2 and v+6. This does not provide integral-gate or fixed-characteristic-two circuit descriptions: rational interpolation denominators are a real remaining gate. It does not make IPS verification polynomial-time, imply polynomial-size certificates, contradict exponential monomial-PC lower bounds, or prove NP=coNP.

C029's entire deduction, including the homogeneous-component paragraph, passed root's full targeted reading before22:47:46UTC. The finite certificate checks754 local divisions,26 ordinary local-verifier identities and30 ordinary clause identities by equality of expanded polynomials over Z; all pass. They do not execute E or verify its complexity theorem. All29 registered deductions now have root's complete targeted proof readings.

I read every line of combined NN-S016 in work/root/chapter8.tex at22:45:05UTC: Chow calculation and integral independence, cycle-class maps, full local-quadric topology, degree/height bounds, and every-field/stabilization statements. This is a targeted reading of a jointly authored proof, not an independent re-proof of my topology and degree portions. Stacks42.32.1 explicitly covers the Zariski-local affine product used, so no global vector-bundle trivialization is required. Hatcher's exact cited interfaces and local proof passages were read in the author text. C027's trace/projector proof has now been explicitly stated over every field, with Frobenius used only when the field is finite. Its fixed-modulus and p-adic-digit addendum also passed root's targeted reading.

## 2026-11-21 23:00 UTC — deterministic smooth-specialization gate closed

C030 closes the precise deterministic finite-field gate left in C024. The actual encoding F=z0 P has degree two in every rail pair. At a singular point of the Fermat pencil, z0 is nonzero; normalize it to one. Pairwise Euler identities force the two rail rth powers equal. Their ratios lie in F_(2^d), d=ord_r(2), and each remaining normalized scale has rth power in that field. The divisibility r(2^d-1) | (2^(dr)-1) confines every normalized singular point, and hence every bad parameter, to F_(2^(dr)). A power-of-two field degree b>dr and its explicit quadratic-tower generator avoid that bad field deterministically, with b<=2r^2. No construction or enumeration of the bad field is required.

The resulting hypersurface is smooth projective over an explicit finite field, with its known rank-one top coherent basis. Absolute Frobenius has semilinear coefficient theta*c; q-Frobenius has scalar c exactly. Thus the finite-field scalar/parity problem now has a deterministic parity-counting-complete reduction, strengthening C024's earlier randomized-promise conclusion. E still evaluates c using the original source-variable bound. The pairwise homogeneity is essential; this does not derandomize arbitrary smooth-pencil specialization or produce GCT canonical objects.

The full C030 proof was self-read at22:59:04UTC and then fully read and approved by root before integration. All30 registered deductions have complete targeted independent root readings, subject to the explicit imported-input limits. No optional new finite testing was performed for C030 before checkpoint04. C024 is retained as the historical randomized result, and its current impact points to C030's gate closure.

C029's large-characteristic addendum also passed root's complete targeted reading: all symbolic constants can lie in Z[1/B!] for B=max(2,ceil(log2 v)), and Hasse-Hermite CRT requires only unit node differences, not J<p. E Lemma4.6 and4.8 were re-read directly by root. Therefore the circuit presentation transfers to every prime characteristic above that explicit threshold. Fixed small characteristic and integral-gate circuit compilation remain separate open gates.

## 2026-11-21 23:14 UTC — fixed F4 specialization

C031 replaces the varying finite field in C030 by fixed F4. Padding with forced variables makes r=2^k-1 for odd k, with only linear incidence growth. The bad-parameter field has odd absolute degree rk, so either nontrivial F4 element avoids it. This preserves the parity bit exactly under four-power Frobenius and gives a deterministic parity-counting-complete family of smooth projective hypersurfaces over one fixed field. The complete proof was self-read at23:08:35UTC and approved by root at23:09:54UTC. All31 integrated complexity deductions now have complete targeted root readings. The explicit fixed-F2 projective descent is under self-review as C032.

## 2026-11-21 23:17 UTC — explicit descent to the fixed prime field

C032 realizes the fixed-F4 family over fixed F2 using explicit Hermitian rank-one matrix equations in projective space. Over F4 the equations identify scheme-theoretically with X times its conjugate under the Segre map, with factor-exchange descent, giving the Weil restriction. Its coherent cohomology ranks are1,2,1, with explicit Frobenius matrices1, c[[0,1],[1,0]], c. The semilinear base-change action is Frobenius tensor squaring; restricting to the descended basis is essential. An independent exact Hermitian-matrix point bijection proves #W(F2)=#X(F4), and the full mod2 zeta congruence follows separately from the coherent determinants. All outputs are smooth geometrically integral projective schemes. The presentation is a system of homogeneous circuit equations, not an asserted F2 hypersurface.

The entire C032 deduction passed root reading at approximately23:16UTC. All32 integrated complexity deductions now have complete targeted root readings. The needed primary Stacks lemmas and their proofs were read with exact tags. This supplies a known four-dimensional coherent realization over the prime field while preserving a parity-counting-complete Frobenius scalar; no l-adic rank bound or GCT canonical-basis identification follows.

Root S017 was read in full at23:15:50UTC together with the exact ADO theorem proof and its purity/Thom interfaces. Its actual motivic wedge statement, normal framing and counting interpretation check. This is recorded as an independent targeted reading of root's deduction, with classical motive inputs retained.

## 2026-11-21 23:32 UTC — formal circuits in every prime characteristic

C033 closes the fixed-small-characteristic gate. The swap-matrix generating identity proves M0 integral despite its rational-looking original formula. Retaining exact integer Boolean measurement fibers avoids any invalid inference about the reduced matrix kernel. Replacing the numeric nodes by distinct nonzero elements of an explicit small extension field preserves the full ring-valued Boolean-difference and Hasse-jet routine. Coordinate simulation descends the formal output polynomial to the prime field. No symbolic identity tests, numerical interpolation in the weight parameters, or division by a factorial is used.

The complete draft and the relevant full E source proofs passed root reading at23:29:14UTC, and root independently read/reran the finite certificate. All33 integrated deductions are now root-reviewed. The construction includes ordinary IPS multipliers and affine maps over F2, and constant-free prime-field circuits with polynomial formal degree. Integral-gate circuits over Z are still open in this row; a new cyclotomic-node construction is being developed separately as C034.

## 2026-11-21 23:42 UTC — integral and constant-free compilation

C034 closes the remaining integral-gate gate. Root proposed taking two primes above Q and the finite free quotient Z[T]/Phi_pq(T). Its Q selected powers are units with pairwise integral unit differences because Phi_pq(1)=1. The complete proof verifies these identities directly, constructs normalized Hasse cardinal polynomials using only integral additions and products, proves polynomial bit heights by an explicit norm recurrence, and projects the resulting formal polynomial to its scalar coordinate. Cyclotomic irreducibility and a ring-of-integers oracle are unnecessary. The same integral circuit therefore works over every commutative coefficient ring.

The actual factor-block homogeneity and scalar-height bounds yield a constant-free circuit of polynomial formal degree by replacing scalar multiplication with binary doubling and addition/subtraction. This supplies ordinary integral ideal multipliers and integral affine-space maps at the same subexponential original-variable or verifier-wire parameter bound. It does not give polynomial-size circuits or efficient unrestricted PIT. The original C016/C029/C033 theorems are retained, and their remaining-gate wording now points to C034.

The complete main draft passed root reading23:37:57UTC. The added C021 comparison passed23:41:34UTC: on the same fixed-density mod-three Tseitin3-CNF family over F2, ordinary monomial-PC size is2^Omega(n), while the constructed circuit-IPS size is2^o(n), yielding an eventual ratio at least2^(kappa*n/2). Actual degree, formal degree and the two proof-size measures are stated separately. My small integral checker passed; root separately read its complete code and announced a rerun, whose completion is not yet claimed in this record. All34 integrated deductions now have whole-draft root reviews, with exact source and finite-check events separated.

## 2026-11-21 23:56 UTC — positive arithmetic versus Boolean support

Root S019 was read in full at23:43:22UTC; its internal-gate convention and representation-primitive limits were read again after revision at23:47:27UTC. Its positive arithmetic lower bound and C034 integral upper bound concern formal multiplicities. The new companion shows the same polynomial support has O(n^3) monotone Boolean circuits: forbidden tuples form a two-CNF, reachability computes unsatisfiability monotonically in forbidden bits, and gatewise dualization gives a monotone circuit in allowed bits. The exact classical SCC criterion is imported from Aspvall-Plass-Tarjan1979 Theorem1 p122, not reproved. The finite-etale allowed-assignment scheme makes the rank-versus-support distinction explicit. Root read the complete companion at23:53:55UTC. The final addendum file is ready for root integration.

A separate proposed C034 addendum is fully drafted and self-read but awaits root reading: explicit monomial-list factors with polylogarithmic scope and linear total input degree preserve the same original-variable exponent and integral formal output. Its proof records the actual E Taylor parameter and coefficient bit costs. This broader trace statement is not yet represented as independently reviewed in the integrated finding.

## 2026-11-22 00:01 UTC — growing-scope integral trace extension checked

Root read the entire proposed C034 growing-scope theorem and freshly audited its full E interfaces; review timestamp23:59:12UTC. It is now integrated into C034, with a standalone geometric statement and the correct term original number of Boolean coordinates (the Boolean scheme has relative dimension zero). The original review events remain separate. A factor may have polylogarithmic scope, but the sum of its listed polynomial degrees must stay linear. Arbitrary local truth tables do not automatically have that property. All34 integrated findings remain reviewed.

## 2026-11-22 00:20 UTC — symbolic counting over F2 and Z at original n

C035 is integrated and root-reviewed00:06:53UTC. Exact zero-set compression is independent of the formal weights, giving full arbitrary-density fixed-width CNF weight polynomials over every characteristic-two ring at the sharper n(loglog n)^2/sqrt(log n) exponent. Arbitrary-graph independence polynomials inherit the original vertex parameter. Its integral coefficient-lift gate is not silently discarded.

C036 now supplies a different integral construction, root-reviewed00:18:29UTC. Slower disjoint sparsification is balanced against the actual larger input degree in E Proposition3.4. The exact integer parameter s satisfies s^(2k) nu^(2k+2)<=lambda, giving exponent O(n/s)=O(n(loglog n)^(1+1/k)/(log n)^(1/(2k))). All polynomial identities hold over Z before any specialization. Constant-free polynomial formal degree and exact rational specialization bit-time are proved. The stronger characteristic-two exponent is retained.

C034 also includes the reviewed Ryser application for row-polylogarithmic permanent supports in the matrix-order parameter, with no column bound. Its total-support refinement and the C036 ordinary ideal-certificate consequence are being drafted separately and are not covered by the preceding review events. All36 integrated findings now have whole-draft root readings.

## 2026-11-22 00:27 UTC — checked dense ideal and total-support permanent consequences

C036 now includes the root-reviewed00:24:15UTC ordinary integral ideal-certificate addendum. Its multipliers are exactly GP Lemma4.2 first-violation coefficients, computed as the C036 two-rail polynomials of restricted prefixes. This gives the original-n bound for every fixed-width CNF density, without Boolean axioms or verifier wires, and integral affine-space coordinate maps of degrees<=n+2 and<=n+2k+2. Actual degree and circuit formal degree remain distinct.

C034 now includes the total-support permanent strengthening, root-reviewed00:27:08UTC. Supports of size C*r*log^a(r) need no individual row or column bound: expanding h=O(r/log^2 r) heavy rows yields at most2^{O(r/log r)} light-row minors, preserving the original matrix-order exponent and formal degree<=2r. The integral trace and actual torus-module direct-sum restatements are included. All36 current findings and these separately dated addenda have full root deduction readings.

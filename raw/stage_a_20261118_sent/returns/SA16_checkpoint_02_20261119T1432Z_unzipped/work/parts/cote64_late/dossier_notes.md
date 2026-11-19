# Cote 64, scans 78–157: consolidation dossier

This portion consolidates all 63 entries of `MPL_64_078-115_notes.md` and all 71 entries of `MPL_64_116-157_notes.md`. Both complete Pro transcriptions and both complete doubts tables were read. Each verdict was made against the actual passage, with 1-based physical transcript line numbers. The source files contain diplomatic uncertainty and deletion markers; this run changes none of them. The Codex notes are documentary leads, and the root consolidation handles their topic-wide integration.

The dominant unfinished task is a **canonical symmetric passage from relative level-four data to Legendre pinning**. The author determines a line and several symmetry laws, but explicitly postpones its tensor-square scale. Much of the rest is completed mathematics, sometimes with a correction already made on the page: cubic coordinates and addition, complex structures and framed analytic families, then quadratic orders and their normalization. The distinctions between an original statement, an authorial correction, an earlier run’s extension, a modern source and this run’s reconstruction are recorded separately in the items, claims, problems and check events.

## 1. The author’s line of work

### The standard square, twists and the pinned moduli problem

Scans 78–100 continue the earlier square and level-four geometry. The standard square `Q0` supplies the scalar twist used in the tangent line. Scan 78’s rotation group is μ4: the misleading star is already deleted. The polynomial model `s⁴=−4`, with `i=−s²/2`, is a useful earlier-run example that this run verifies; the manuscript itself specifies the sides and their rotation relation. It is not permissible to turn that example into a quotation from the page. See SA16-501–503 and C-SA16-501–502.

The text distinguishes three related structures. With an orientation identification α fixed, pinnings form a μ2-torsor. Allowing α to vary gives the stated μ4-torsor. Adding an ordering of the three nonzero two-torsion points gives the combined rigid moduli problem. This ordering matters: the uncombined pinned problem can retain a cyclic order-three stabilizer at an equianharmonic parameter. The characteristic-three fixed scheme needs its own treatment, because its defining quadratic becomes a repeated factor. It is a different issue from the characteristic-five exception to an earlier bare-octahedron assertion. See C-SA16-503–506 and the crosslinks to scans 48–53.

The modular group calculation is concrete. After choosing `i`, the stabilizer is

\[
D'_3=S_3\times_{C_2}C_4\cong C_3\rtimes C_4.
\]

Its order is twelve, its centre has order two, its commutator subgroup is `C3`, and its abelianization is `C4`. A transposition lifts to order four, so its central extension of `S3` does not split. The full finite group was enumerated, and the tangent and quotient-tangent characters were checked. These checks establish the finite group and the displayed characters; they do not identify an arithmetic Galois image or the monodromy of an external family. See C-SA16-507–510 and `proof_notes.md`, §§1–2.

The reconstruction of an elliptic curve from the cubic étale set `J`, the disjoint section `t` and the pinning data is stated at scans 83 and 94–95. The elementary part is precise: after one square root of a line has been fixed, all its square roots form the groupoid of μ2-torsors. The team’s early64 proof, independently read and checked here, also establishes the geometric elliptic/branch-data to tangent-square-root equivalence: locally both sides are the same μ2 twist groupoid, their automorphism sheaves match, and the equivalence descends. The particular symmetric `Q0`-twisted pinning normalization remains a separate comparison. The opened modern references provide ordinary Legendre models and a twisted descent action, but do not themselves assert this exact symmetric normalization. That is the meaning of class C here; it is not a claim that ordinary Legendre or level-four representability is an unsolved problem. See C-SA16-504–505, 509–512, MP-SA16-161 and [AntieauMeier2020, §4; ConradLevel, §§2–3].

At scans 98–100 the author writes coordinate conditions for the pinning. They determine a one-dimensional kernel, not its scale. Equation 73 is still to be expressed. The same issue returns at scan 121 as condition 83c and is explicitly postponed. The cyclic-difference calculations on scans 123–126 determine the line and its basis signs; they do not close that gap. The continuation across the package boundary is one problem, MP-SA16-164, within the level-four construction MP-SA16-165. A canonical ordinary level-four construction in the opened literature is a comparison target; matching its ordering, tangent variance and symmetric fourth-root action is a separate task. This remains the highest-priority direction in `directions.md`.

### Pole filtrations, Weierstrass coordinates and the group law

The title at scan 101 starts the explicit Weierstrass construction. Scans 102–115 use the spaces `F_n=H⁰(E,O(nO))`, the invariant derivation associated to a tangent vector, parity under negation and the resulting cubic. The standard algebraic content is recoverable, but several distinctions must be preserved.

For ordinary principal parts, the associated graded derivation has coefficient `−n`. A multiplicatively rescaled convention changes this to `−nc`; no such convention makes every graded coefficient equal to one while retaining multiplication and the Leibniz rule. The all-degree assertion is therefore defective independently of the choice of normalization. In contrast, the leading coefficient of the cubic is convention-dependent: ordinary principal parts lead to the familiar factor four, while the rescaling `ε_n=(−1/2)^n pp_n` makes the particular cubic monic. The text does not explicitly state which normalization it is using. An unconditional instruction to replace every monic cubic by one with factor four would go beyond the evidence. See C-SA16-517–518, 523 and the associated readings.

The constant-kernel statement requires a characteristic restriction. For a nonzero invariant derivation over an algebraically closed field of odd characteristic `p`,

\[
\ker(D|F_n)=\{g^p:g\in F_{\lfloor n/p\rfloor}\}.
\]

The first nonconstant example is `x^p`, of pole order `2p`. It remains in `F_(2p+1)`, so the proposed rescue “p does not divide n” does not work. The filtered union and the graded section ring must also be separated. The latter has constants in every degree: its kernel is `k[S]` in characteristic zero and `R^p[S]` over a perfect field of characteristic `p`. These are mathematical reconstructions, not readings of additional ink. See C-SA16-519–520, [Stacks031W], and the direct argument in `proof_notes.md`, §4.

The coordinate construction needs a nonzero tangent vector. Scan 105 does not visibly state that qualification, whereas scan 115 calls the vector a basis. At zero the proposed coordinate basis collapses. The cubic degree, the constant sign, the ambiguous exponent on the `a2` term and the prime/double-prime mark all have exact algebraic tests. Their compatible alternatives are in `readings.tsv`; the tests do not decide which marks were written.

Several apparent open steps are actually completed on the pages. Scan 106 finishes the restriction-to-branch-points argument with a Vandermonde determinant. Scans 110–111 repair the determinant criterion by inserting distinctness and explain why repeated rows fail. Scans 112–113 derive the third secant intersection and state the final domain `x(P)≠x(Q)`. The displayed point is the negative of the sum. The tangent continuation retained in the notes is an earlier-run addition, independently checked here, not a separate manuscript formula. See MP-SA16-166–167 and C-SA16-524–530.

Scans 115–118 continue one calculation across the package boundary. For a root `r` of the cubic and the other roots `u,v`, translation by `(r,0)` descends to

\[
\sigma_r(z)=r+\frac{(r-u)(r-v)}{z-r}.
\]

Its fixed values give the halves of the corresponding two-torsion point. The undivided expression covers `r=0`; an expression containing `a3/r` requires that qualification. The correctly expanded radical is

\[
(r-u)(r-v)=-(a_1r+2a_2-3uv).
\]

The later written plus sign gives `−34` instead of `2` at roots `1,2,3`. This is a decisive mathematical alarm, while the scan still has to decide the mark. The distinctness hypothesis of the earlier determinant proposition is satisfied in the half-division application because the three doubles are different. See C-SA16-532–535 and SA16-534, 537, 561.

### Two analytic drafts and their corrections

After title sheets and reused printed notices, scans 131–152 describe complex tori, lattice frames, the upper half-plane and a nonzero tangent vector. The physical sequence is retained even where exposition would be smoother in a different order. The title’s doubtful page count does not authorize reordering or discarding a sheet.

The first draft transports a complex structure through the real-part map. Its second formula requires an inverse for type correctness. With the stated line convention `L_z=C(z,1)`, direct computation gives

\[
J_z=\frac1{\operatorname{Im}z}
\begin{pmatrix}
-\operatorname{Re}z&|z|^2\\
-1&\operatorname{Re}z
\end{pmatrix}.
\]

The induced orientation is opposite to the one initially asserted. The author himself withdraws that assertion and later considers the other line convention. The first displayed period `−\bar z` is antiholomorphic in the stated parameter; the second draft uses a holomorphic `τ`. These are two formulations with a visible correction, not one silently modernized family. See C-SA16-540–544, MP-SA16-168–169 and [Hain2008, §§2.3–2.4].

The subsequent action formulas work after their conventions are fixed. The right change of a Torelli frame produces `(dτ+b)/(cτ+a)`; an explicitly defined anti-automorphism converts it to the usual left action. The automorphy factor and the semidirect action on lattice translations were recomputed. The symbol `τ∞` is a determinant-minus-one matrix in this calculation. Its infinity subscript does not make it the arithmetic inertia source mentioned in an unavailable La Longue Marche passage.

The total elliptic family is not the simply connected covering base of the elliptic moduli stack. Its fundamental group is `Z²`, whereas the framed base is the upper half-plane. The coarse parameter also has a different covering theory because it forgets stabilizers. Similarly, the once-punctured torus has free group `F2` and rank-two abelianization; the first draft’s rank-one parenthesis is false. The second formulation omits it. Explicit lifts of modular generators were computed and their relations checked modulo inner automorphisms. The full discrete outer-automorphism theorem is used from the opened primary literature, rather than claimed as a new theorem proved by those word calculations. See C-SA16-548–550 and [BuxErshovRapinchuk2011, §3].

Finally, two separately free actions need not have a free product action. The pair `(-1,-I)` fixes the doubly framed base and acts as negation on the elliptic fibre. Removing zero leaves three fixed two-torsion points. Scan 152 already notices the obstruction and deletes the erroneous assertion. MP-SA16-171 records the correction as closed, with both places retained.

### Quadratic orders and the arithmetic appendix

Scans 154–157 contain a separate algebraic line of work. The uncertain hypothesis “anneau jauge” is not deciphered here. Under the **DVR** interpretation, with uniformizer `π`, the local normality criterion has a short proof. In odd residue characteristic, `A[S]/(S²−a)` is normal precisely when `v(a)≤1`. A unit is étale; valuation one gives a DVR; larger valuation leaves the integral element `S/π` missing. The necessity fails for a regular local ring of higher dimension: `Q[[x,y,S]]/(S²−xy)` is normal although `xy` lies in the square of the maximal ideal. Thus the ring hypothesis is mathematically consequential. See C-SA16-555 and MP-SA16-172’s background.

For a dyadic unit, nonsquare residue gives a normal DVR with inseparable residue extension, which is not étale. In the square-residue case choose `α` and put `b=α²−a`. The class of `b` modulo `m²` is independent of the lift. Normality holds exactly when that class is nonzero. If it vanishes, `(S−α)/π` is integral and missing from the order. The completion formula is valid as a `T`-adic completion; identifying it with the local completion needs the topology comparison made in `proof_notes.md`, §10. Noncompleteness of `A` alone does not invalidate it.

The additional description as an ordinary node needs a stronger hypothesis. The tangent quadratic has distinct geometric lines exactly when `v(2)=1`. Both an equal-characteristic-two cusp and a ramified mixed-characteristic example refute the unrestricted assertion. This is a statement about the singularity type, not a counterexample to the DVR normality test. The c63 deformation-divisor question is related, but it has a different ambient ring and cannot be decided by importing this one-dimensional calculation.

The proposed finite exceptional nonnormal locus disappears once all height-one local rings are normal: the quadratic hypersurface satisfies `S2`, and the normality criterion applies. The full primary theorem and proof in EGA IV2, 5.8.6, printed p.108, were opened and checked. Its application here is explicit in `proof_notes.md`, §11.

The last global assertion is true after the order and its normalization are distinguished. Let `P=εqQ` be squarefree in `Z[T]`, with positive content `q` and primitive `Q`, and suppose it defines a genuine quadratic field over `Q(T)`. Generic étaleness of the normalization over every integer fibre is equivalent to `q=1` and

\[
P=r^2+4h,\qquad r,h\in\mathbf Z[T].
\]

The integral generator `u=(S+r)/2` gives the full normalization

\[
\mathbf Z[T,u]/(u^2-ru-h).
\]

Its discriminant is `P`, so it is finite étale on `D(P)`. Necessity, globalization of the square congruence and normality of this order are proved in this run; the manuscript merely asserts sufficiency. The source comparison identifies the classical ingredients, without claiming to locate the first occurrence of this specialized global formulation. See C-SA16-560–561, MP-SA16-172 and [Voight2016, Lemmas 3.7, 3.10 and Proposition 3.13].

The signed radicand matters. An unsigned `Q=1` cannot distinguish `P=3` and `P=−1`; whether the author’s `Q` abbreviates the full radicand remains an ink question. In the example `T(T−λ)`, the square condition modulo four is exactly `4|λ`, while the displayed congruence modulo two only asks that `λ` be even. At infinity `x=1/T` gives `(S/T)²=1−λx`. The opposite written sign fails at `λ=4,x=0`, where it gives the dyadically ramified field `Q(i)`. For the corrected sign and `λ=4m`, the normalized chart `u²−u+mx=0` is étale on the specified open and splits at infinity. Identifying the unnamed exceptional `λ` with `1728` is an earlier-run interpretation, not a manuscript value.

## 2. What the earlier notes got right, and what changed in scope

The supplied notes are generally careful about the division between manuscript, correction and new calculation. Consequently the verdict table has 99 kept entries and 35 merged entries, with no entries discarded merely because they are speculative or documentary. “Kept” preserves the attributed report; it does not endorse an unavailable external theorem or promote an earlier-run calculation to manuscript content.

The most valuable corrections already recognized by the notes survive independent checking: the tensor-square factor, positive-characteristic kernel, determinant distinctness, fourth-division signs, analytic orientation and antiholomorphic parameter, rank-two abelianization, product-action fixed points, DVR hypothesis, ordinary-node qualification, signed mod-four test and infinity sign. The present run supplies new executions and proof records rather than inheriting their certificates.

Topic-wide access changes several packet boundaries. Earlier square and level-four passages, the later normalization deferral, the second analytic draft and the arithmetic appendix are now available and read at both endpoints. Their former “outside this packet” labels are replaced by exact folder links. Original files from La Longue Marche, Les Dérivateurs, cotes 93/159 and the earlier modernization are still not supplied. Their 21 leads remain in `our_project_links.tsv`, with the precise note report checked and the original endpoint explicitly unavailable. No absent proof or project status is certified.

A source check also found a bounded defect in a modern comparison: the literal strict `C2×S3` quotient in Hain’s Proposition 3.15 has the wrong harmonic stabilizer. The manuscript audit does not rely on that quotient. Its independent counterexample is R-SA16-L64-Hain315; the other period and frame results are used at their separate stated scope. The public November 2026 modernization is credited as a comparison, with no Lean certificate claimed.

## 3. Coverage, classes and verification

| Register | Count |
|---|---:|
| Source entries | 134 |
| Items | 99 |
| Entry verdicts: kept / merged | 99 / 35 |
| Manuscript claims | 66 |
| Claims class E / C / F | 56 / 6 / 4 |
| Authorial problems, including closed steps | 12 |
| Reading alarms, all ink-unresolved | 75 |
| Folder / published-work / external-project links | 16 / 5 / 21 |
| Ranked directions | 7 |
| Exact computation groups rerun | 31 |
| Bibliographic records: verified / primary-text-unverified | 25 / 2 |
| Check events | 340 |

The claim statuses on the pages are: 13 proved there, 27 proof sketched, 7 stated without proof, 5 corrected by the author later, 11 false under the specified literal or unrestricted reading, and 3 open on the pages. The four F classifications concern the unstated principal-part convention, the uncertain ring hypothesis, the signed-radicand abbreviation and the undefined cancelled diagram. A false literal reading is not evidence that the transcription’s uncertain mark has been deciphered.

All 66 claims have exact search-group mappings in `claim_search_coverage.tsv`. The searches, actual batched results and opened locators are recorded in `search_log.tsv`, `search_requests.json` and `literature_notes.md`. A failed targeted search is not used as proof of absence. The two unverified bibliography entries are backward historical leads whose original texts were not opened; the mathematical statements actually used are supported by opened modern primary sources and the independent arguments specified in the check events.

The computations are exact symbolic identities, complete finite-group enumerations, free-word reductions and explicitly scoped characteristic-p calculations. The universal Hasse recurrence is proved separately from the sample primes. The single initial implementation failure was a zero-matrix comparison requiring entrywise simplification in Sympy; the corrected run passed all 31 groups. No Lean library, inherited research script or manuscript scan was audited. The complete proof supplement, code and output are retained with the tables.

Printed notices on scans 124, 127 and 157 document the sheets’ reuse. Their dates do not establish mathematical composition dates. The doubtful leading digit before the June 1981 notice date remains unresolved, and no chronology is inferred from it.

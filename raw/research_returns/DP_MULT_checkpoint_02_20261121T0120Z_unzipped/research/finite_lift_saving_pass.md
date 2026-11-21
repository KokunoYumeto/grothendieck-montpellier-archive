# A fresh pass at a finite saving in the number of theta lifts

Date: **2026-11-21 UTC**. Author/reviewer: `/root/step2_higher`, **GPT-6 Astra Pro**; runtime effort setting not exposed. This memo records new work after the earlier local estimates and unchanged-logarithm obstructions. It does not edit the main paper and does not audit RH/GRH.

## 1. Outcome

A bounded higher-height improvement does **not** numerically exclude a finite saving. There is an exact positive-ramp example, with the source's lower weight condition and finite cutoff, in which twelve height-three contributions equal thirteen height-two contributions. Doubling gives a parity-compatible numerical comparison, twenty-four versus twenty-six. This is DP26 below. It is a certificate calculation, not a geometric theta-lift construction.

The actual source imposes further discrete structure that was not visible from the scalar bound. Its `Ranks` structure requires an **even** number of lifts. Its terminal rank, auxiliary signatures, and period-map domain depend on that same integer. Thus deleting one lift is incompatible with the unchanged parameter type, and literal truncation does not preserve the old endpoint and period data. This is the carefully limited DP27 below. The column groups `X_j` are definite at every stage; they must not be confused with the auxiliary `W_j`, which change signature.

There is also a stronger geometric obstruction to the explicit genus-three substitution than the fixed `oneLog` formula alone. The actual host CM type is **induced from a fixed imaginary quadratic subfield**. At an unramified prime inert in that quadratic field, every rank-one full-CM factor has slope one half; a one-dimensional factor has height two. At a split prime, those factors are ordinary. Enlarging the CM field while retaining that induced type therefore cannot produce a one-dimensional height greater than two. This is DP25.

For the Jacobian of `y²=x⁷−1`, the prime `11` is split in the unique quadratic subfield `Q(sqrt(−7))`, and the actual CM type `{1,2,3}` is not induced from that subfield. The first failed input in the inspected geometric construction is consequently its CM-type/Serre-tensor input, before the normalized theta identity `B0` is reached. A balanced product does not repair the source's surjective comparison with induced-type building blocks, because its slopes at `11` remain nonordinary.

These facts settle the literal old-host replacement and make the first missing datum for an alternative construction precise. They do not prove that a different mixed-type theta construction could never save a finite number of lifts.

## 2. Newly inspected primary source declarations

These files were extracted directly from the already-downloaded fourteen-part author archive, not inferred from the mirror. Each extraction streamed all 175,190 tar entries without unpacking the entire archive. The consolidated manifest is `research/finite_lift_added_sources.json`; it gives exact archive members, byte counts, SHA-256 hashes, and actual reading scopes. Forty unique files were extracted during targeted tracing, thirty-nine absent from the baseline `author_source_verification_final.json`. Some were search matches only; extraction is not described as a whole-file proof review. The mathematical source reading used the declarations below.

All paths in the table are relative to `lean/src/` in the author archive.

| File and exact locator | What it supplies |
|---|---|
| `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean`, `HostRaw.sqd`, `sqd_sq`, lines 29–31 | The distinguished element satisfies `sqd²=−d` |
| Same, `HostRaw.K`, line 60 | The quadratic subfield is explicitly `Q(sqd)` |
| Same, `HostRaw.cmType`, line 66 | The type is exactly the embeddings sending `sqd` to `i sqrt(d)`; thus it is induced from one quadratic embedding |
| Same, `HostDer.finrank_E`, line 91; `HostDer.cmType`, lines 95–96 | The host degree and type cardinality/compatibility data |
| `Formalism/LocalRingCardinality/DataHost.lean`, `PrimeClass`, lines 24–31; `primeClass`, lines 33–37; `Host.cls`, line 138 | Split-quadratic primes are selected by `jacobiSym(−d,p)=1`, before the signal/inert classes |
| `Formalism/SharpRestriction/GlobalTheoremInputs.lean`, `InertK`, lines 97–98; `LinkG_at`, lines 129–135 | The relevant ramp gain statement applies to signal/inert quadratic classes |
| `Development/AbelianVarietyTheory/Definitions/CMLattices/IsDiffOf.lean`, `Ell`, lines 31–39; `HasType`, lines 64–67; `IsTen`, lines 73–77 | An elliptic CM building block, the uniform multiplicities on the two quadratic embedding classes, and the data of a Serre tensor comparison |
| Same, `CMObj`, lines 115–130; `typeP`, `typeM`, `typeB`, lines 120–122; `onto`, lines 126–128 | The two basic abelian factors have types `(1,0)` and `(0,1)`; the target has type `(p,q)` and a specified surjective comparison from these factors |
| `Formalism/LocalRingCardinality/Params.lean`, `Ranks`, lines 6–22 | `m` is an integer, `m_even` is a field, and `m≥2` is required |
| Same, `Ranks.r`, `N`, `rS`, `rankY`, `rankX'`, `sigY0`, `sigW`, lines 32–46 | Exact dependence of ranks and signatures on `m` and the stage index |
| `Formalism/LocalRingCardinality/DataSpaces.lean`, `Spaces.X_rank`, `X_def`, lines 84–87; `W_rank`, `W_sigval`, lines 121–124 | Actual hermitian spaces have these ranks and signatures; all `X_j` are definite |
| `Formalism/LocalRingCardinality/DataKernels.lean`, `ColumnChain.col`, lines 70–71; `PeriodMap.evz`, line 174 | The chain has exactly `R.m` steps and the period consumes its specific terminal function space |
| `Formalism/ThetaLiftIndependence/Statement.lean`, `kerMul`, lines 14–16; `chainOpM`, lines 52–57; `ChainIntM`, lines 59–67 | Abstract composition of kernels, the iterated chain, and the product of its denominator factors |
| `Formalism/LocalRingCardinality/DataParams₂.lean`, `lifts`, line 208; `MAIN`, lines 232–234; `vonMangoldtClassSum`, lines 240–242 | The same `m` indexes the lift sum and occurs in the period main term; the actual finite odd-prime-power ramp |

`HasType` is not inferred from the definiteness of a unitary group. Its two-class condition is an explicit definition, and `HostRaw.cmType` gives a direct independent confirmation at the host level. The general target `B` in `CMObj` need not be a rank-one full-CM object; the slope-one-half conclusion below is stated only for full-CM factors of the induced type, including the basic `A+` and `A−` blocks.

## 3. DP25: induced-type obstruction, including larger CM fields

### Statement

Let `E` be a CM field containing an imaginary quadratic field `K`, and let a full CM type `Phi` of `E` be induced from one embedding `kappa:K→C`:

`Phi={tau:E→C | tau|K=kappa}`.

Let `A` have good reduction and full integral CM by `O_E` at a rational prime `p` unramified in `E`. For a Frobenius orbit `O` of embeddings, write `d=|O|`. The corresponding rank-one local CM factor has height `d` and dimension `|Phi intersect O|`.

1. If `p` is inert in `K`, then `d` is even, `|Phi intersect O|=d/2`, and every such factor has Newton slope `1/2`. A one-dimensional factor has height exactly two.
2. If `p` splits in `K`, then `|Phi intersect O|` is either zero or `d`. The factor is respectively étale or of multiplicative slope one. A one-dimensional connected factor has height one.

Consequently a one-dimensional local factor of height greater than two cannot be obtained by enlarging `E` while keeping this induced type. The inert-prime assertion does not require an orbit to be stable under complex conjugation.

### Proof

At an unramified prime, Frobenius permutes the embeddings of `E`; restriction to `K` commutes with this action. If `p` is inert in `K`, its action on the two embeddings of `K` is their transposition. Membership in `Phi` therefore changes at each Frobenius step. Returning to the original embedding requires an even number `d` of steps, and exactly half the orbit belongs to `Phi`.

If `p` splits in `K`, Frobenius fixes each quadratic embedding. Membership in `Phi` is constant on each orbit, giving the second count.

The standard full-CM height/type formula identifies the local height with `d`, the dimension with the type count, and the Newton slope with their ratio. It is the same cited Tate formula used for the earlier CM decomposition and the concrete Jacobian. The displayed dimensions and slopes follow. In the inert case dimension one forces `d/2=1`; in the connected split case dimension one forces `d=1`. No self-conjugacy assertion was used. ∎

### Exact application to the inspected source

`HostRaw.K` and `HostRaw.cmType` satisfy the induced-type premise by their definitions. `CMObj.typeP` and `typeM` impose its two conjugate multiplicity-one versions. `IsTen` records the Serre tensor comparison with the quadratic CM elliptic curve; that structure declaration alone is not an existence theorem. Therefore the proposal “use a larger CM field but retain these building blocks and the old host type” is structurally blocked, independently of the later `oneLog` calculation.

This proposition does not assert that every higher-rank `HasType(p,q)` object is isoclinic of slope one half. A higher-rank action has more information than a rank-one full-CM type, and the existing source itself allows additional ranks and defects.

## 4. Trying the genus-three example in the actual geometric input

Let `E=Q(zeta_7)` and `J=Jac(y²=x⁷−1)`, with the type already computed as `Phi={1,2,3}`. Put

`S=zeta_7+zeta_7²+zeta_7⁴`, `T=zeta_7³+zeta_7⁵+zeta_7⁶`.

Direct multiplication gives `S+T=−1` and `ST=2`, so `(S−T)²=−7`. The cyclic group `Gal(E/Q)` of order six has a unique subgroup of index two. Its cosets on embeddings are

`R={1,2,4}`, `R'={3,5,6}`,

and its quadratic fixed field is `K=Q(sqrt(−7))`. A CM type induced from `K` is exactly `R` or `R'`. The type of `J` meets them in two and one elements, and therefore is neither induced type. Galois relabeling only preserves or exchanges those counts, so it does not repair the mismatch. An `E`-linear isogeny also preserves the characteristic-zero type.

At `11`, Frobenius is multiplication by `4`, which preserves each of `R` and `R'`. Hence `11` splits in `K`. Equivalently, `−7` is `4` modulo `11`, a nonzero square. In the source's `primeClass`, such a prime is assigned `splitK`, unless an earlier exceptional branch gives a ramified class; it is never `signal` or `inertClass`. Thus the height-three factor at `11` cannot simply be inserted as an extra term in the existing `InertK` ramp theorem.

### Earliest failed geometric field

Using `J` for the basic source object `A+` already fails `CMObj.typeP : HasType(1,0)`, and using it for `A−` fails `typeM`. This is earlier than the theta generator, `B0`, or the derivative estimate. The failure is a proved inequality of CM types, not merely an unconstructed normalization.

The same obstruction affects powers and the elementary balanced product. For `J^a × bar(J)^b`, the multiplicity is `a` on `{1,2,3}` and `b` on its complementary type. On the two quadratic classes the multiplicity lists are

`R: (a,a,b)`, `R': (a,b,b)`.

They are constant on both classes only when `a=b`; in that case the product has `HasType(a,a)`, never a nonzero type `(1,0)` or `(0,1)`.

Could the balanced product at least be the general target `B`? Its type matches `(a,a)`, but the source also requires `CMObj.onto`, a surjective CM-linear comparison from `a` copies of each basic induced-type factor. Both sides have the same dimension, so such a homomorphism would be an isogeny. At `11`, all induced-type source blocks are ordinary by the split-prime part of DP25. The target `J^a × bar(J)^a` has slopes only `1/3` and `2/3`. Isogeny invariance of Newton slopes rules out that comparison. Thus balancing this example does not supply the old `onto` datum either.

These conclusions are confined to the specified CM action and the source's existing construction. They do not prove that `J` cannot enter a theta construction with a different type, different correspondences or different endpoint representations.

## 5. DP26: an exact finite certificate saving is numerically possible

### Statement

For any prime `p`, use the positive ramps of DP17 with `A=p³` and `w_i=1` for every `i`. Then

\[
R_2(p^3,p;1)=p^2-1=(p-1)(p+1),
\]

\[
R_3(p^3,p;1)=p^2+p-2=(p-1)(p+2),
\]

and consequently

\[
(p+1)R_3=(p+2)R_2.
\]

For `p=11`, these are exactly `R_2=120`, `R_3=130`, so

\[
12\cdot130=13\cdot120=1560,
\qquad
24\cdot130=26\cdot120=3120.
\]

The second equality compares two even lift counts. These equalities show that a finite numerical saving is not excluded by boundedness or summability of the local improvement. They do not certify a geometric saving with the same other data.

### Proof and finite cutoff check

For height two the active odd term `i=1` is `p²−1`; the next odd term `i=3` is `max(0,1−1)=0`; all subsequent terms vanish. For height three the two positive terms are `i=1`, giving `p²−1`, and `i=2`, giving `p−1`. The index `i=3` is excluded, and `i≥4` gives `p^(3−i)≤1/p<1`, hence zero. This proves both formulas and the equality.

The source uses `range(Nat.log p A+2)` rather than an infinite sum. Here `A=p³` is a nonnegative integer, `Nat.log p A=3`, and the range is exactly `{0,1,2,3,4}`. The original odd-index sum contains `1` and `3`, with the latter term zero. The proposed height-three index set contains `1,2,4`, with the last term zero; `0` is divisible by three and contributes nothing. Thus the equality is exact for the source-shaped finite cutoff. All weights equal one and satisfy its field `wPart_ge`. ∎

The `13→12` comparison is a one-step saving only in the bare numerical model. It does not satisfy the original even-`m` condition on both sides. Doubling gives `26→24`, avoiding that parity objection but still lacking a geometric realization. The example also uses the prime `11`, which is outside the old inert-quadratic gain class for this Jacobian. These are explicit limitations, not reasons to discard the arithmetic observation.

## 6. DP27: parity and endpoint data under literal shortening

### Statement in the source's exact framework

Let `R` be an existing `Ranks` object, with `M=R.m`, and hold its `k,t` fixed. Then:

1. Both an old and a newly instantiated `Ranks` object must have an even lift count. A replacement `M→M−1` cannot retain this parameter specification. Any change between two allowed counts has even size.
2. For `0≤L<M`, the terminal rank numbers satisfy

\[
N(M)-N(L)=(M-L)(t+1)>0.
\]

Hence the old hermitian spaces `X_L` and `X_M` have different ranks and cannot be identified by a linear isometry.
3. For `1≤L<M`, the auxiliary signature is

\[
\operatorname{sig}W_L=(k+L-1,M-L),
\]

with both entries positive, whereas `W_M` has signature `(k+M−1,0)`. These are not the same auxiliary endpoint data. **The column spaces `X_j` remain definite at every stage**; this assertion concerns `W_j`.
4. `ColumnChain.col` is the actual iterate `chainOpM(...,M)`, with output `C.cls M→C.Y M→C`, and `PeriodMap.evz` consumes that terminal space. Literal truncation to `L` produces the stage-`L` space. The source provides no equality of these types merely from a stronger local valuation.

### Proof

The first assertion is `Ranks.m_even`; if two natural numbers are even, their integer difference is even. The second is the exact definition `N(j)=k+j(t+1)`, together with `t+1>0` and the source field `Spaces.X_rank`. Rank is invariant under linear equivalence, hence under linear isometry.

The third follows from `Ranks.sigW(j)=(k+j−1,M−j)` and `Spaces.W_sigval`. Since `k≥M+3` and `L≥1`, its first entry is positive; since `L<M`, its second entry is positive. At `j=M` the second entry is zero. The source independently requires `Spaces.X_def` for all `j≤M`, so there is no claim that the definite column chain becomes indefinite when stopped early.

Finally the formulas for `ColumnChain.col` and `PeriodMap.evz` give the stated domains and codomains directly. A stronger divisibility estimate is a property of values in fixed lattices; it does not identify these different stage spaces, their ranks or their period maps. ∎

This proposition obstructs **literal truncation with the old endpoint held fixed**. It does not prohibit constructing new admissible data with a smaller even `m`, a changed terminal group and a new period comparison. Such a construction changes `r=k+m−1`, `rS=m/2−1`, the Harish–Chandra parameter arrays indexed by `Fin m`, the terminal `N(m)`, and the main term that is linear in `m`; the stronger local coefficient alone supplies none of those changes.

## 7. A further attempted shortcut: combine two kernels

There is an elementary formal compression available at the level of finite linear operators. If

\[
(T_1 f)(y)=\sum_x w_1(x)K_1(x,y)f(x),
\quad
(T_2 g)(z)=\sum_y w_2(y)K_2(y,z)g(y),
\]

then define

\[
K'(x,z)=\sum_y w_2(y)K_2(y,z)K_1(x,y).
\]

Expanding the finite sums proves that `T_2T_1` is the one written kernel `K'` with the original outer weights `w_1`. The source defines this operation as `kerMul`; the operator-valued version uses composition in place of multiplication. This algebraic regrouping preserves the old endpoint.

Algebraic regrouping alone provides no cancellation of denominators or geometric costs. If the two stages have denominator factors `D_1,D_2`, the direct integral bound for their composite retains the product `D_1D_2`; this is precisely the product structure encoded in `ChainIntM`. This does not rule out cancellation established by some additional theorem. Nor does the finite-sum identity assert that `K'` is one standard theta kernel for a new admissible dual pair, with the cost and period normalization of one original lift. None of the inspected `ColumnChain`, `ThetaLiftIndependence`, `IsTen`, `CMObj` or local normalized-kernel declarations supplies that additional geometric identification. The inspected `ChainScalar` lemmas propagate adjoints through the chain; they do not prove such a cost-saving identification.

Thus one may shorten the *written composition* without proving fewer geometric theta lifts. A substantive compression would require a theorem realizing the composite, or a replacement with equal target effect, as a genuinely new single-step theta correspondence with a favorable full cost comparison.

## 8. Precise remaining construction datum

The first missing input depends on which proposal is made:

* **Keep the induced host and merely enlarge its CM field:** impossible for a one-dimensional higher-height factor, by DP25. This route is closed.
* **Insert the explicit genus-three Jacobian as an old basic block:** its `HasType(1,0)`/`HasType(0,1)` field fails. Its prime `11` also lies outside the old `InertK` gain class. Balancing with its conjugate does not supply the required old `onto` isogeny, as proved above. This literal route is closed.
* **Truncate the old chain:** one-step truncation violates the even count, and all nontrivial truncation changes the rank/period endpoint. This route cannot retain the old endpoint data without an additional correspondence or identification.
* **Build a genuinely new mixed-type shorter chain:** the first unsupplied datum is a geometric single-step theta kernel for that mixed CM input, together with the correct source and terminal representations and an integral normalized period comparison. In the inspected source interfaces this would require a replacement for the `CMObj`/Serre-tensor comparison and for the geometric realization of `ColumnChain.unf` and its normalization exponents. An arbitrary abstract linear operator can fill a raw `unf` field; that is not a construction of the required geometric and arithmetic admissibility data.

Only after that first datum is constructed can one ask whether the height-three formal derivative gain survives in the relevant determinant/exponential entries. It would need the corresponding normalized theta identity and coefficient hypotheses, then a global path expansion, controlled nonvanishing/denominators, and the new period, rank and norm costs. The earlier recovered `B0`–`B4` and path interfaces identify what must be proved; they do not construct it for `J`.

The numerical DP26 example shows why a finite saving remains worth distinguishing from a polynomial shortening. It makes no assertion that the geometric gate has been met. Conversely the failures of the old host, parity and fixed endpoint are concrete obstructions to those particular substitutions, not a universal theorem that every shorter theta construction fails.

## 9. Actual checks and provenance

All the events below occurred on **2026-11-21 UTC**, by `/root/step2_higher`, **GPT-6 Astra Pro**, effort setting not exposed. The complete proofs in §§3–6 were derived and then reread in full. No computer enumeration is used as a substitute for their proofs; no Lean execution is claimed.

| Event ID | Object | Actual work | Outcome |
|---|---|---|---|
| FLS-S-001 | New author-source recovery | Streamed the existing fourteen archive parts in three targeted passes; saved exact matching files and archive-member/SHA metadata, then rehashed every consolidated file | Forty unique files extracted; all consolidated hashes agree; no full extraction or new mirror assumption |
| FLS-S-002 | Host and type data | Read `HostRaw`/`HostDer` definitions, all of `DataHost`, and the exact `HasType`, `IsTen`, `CMObj` fields | Induced type and split/inert classification confirmed directly |
| FLS-S-003 | Chain parameter and endpoint | Read all of `Params`, `DataKernels` through its period definitions, and `DataSpaces` through the actual rank/signature fields | Even lift count, rank dependence, definite `X_j` and changing auxiliary `W_j` confirmed |
| FLS-S-004 | Formal kernel composition | Read the finite kernel/chain/denominator definitions and the complete newly extracted `FinalThetaLiftAMFKIndep` and `ChainScalar` files | Composition is available algebraically; no inspected declaration realizes a cheaper mixed-type single theta lift |
| FLS-P-001 | DP25 | Derived and reread the complete Frobenius restriction/count proof, including split primes and non-self-conjugate inert orbits; applied the cited full-CM height/type formula | Passed with rank-one/full-CM scope |
| FLS-P-002 | The explicit genus-three substitution | Computed the quadratic subfield from `S+T=−1`, `ST=2`; checked the type lists, splitting at `11`, product multiplicities and ordinary/nonordinary obstruction to the old `onto` isogeny | Passed for the stated CM action and old source comparison |
| FLS-P-003 | DP26 | Evaluated every possibly nonzero ramp term, checked the exact `range(5)` cutoff, and verified both integer equalities and the parity distinction | Passed; numerical illustration only |
| FLS-P-004 | DP27 | Derived the parity, rank and auxiliary-signature statements from exact source definitions; checked that all column `X_j` remain definite and that the old period domain is stage `M` | Passed with literal-truncation scope |
| FLS-P-005 | Kernel regrouping attempt | Expanded the finite sums and tracked both denominator factors; checked that rebracketing alone does not establish a new theta-kernel realization or cost bound | Passed as an algebraic identity and a precise limitation |

The root's latest DP22 proof was also reread in full after its explicit two-chart Čech genus calculation was added. That separate integrated-paper check is recorded as **SPR-P-016s** in `paper_review_step2.md`, with paper hash `3ecf680f5d003bf431f17ad15e9b424cb44474ea73dc903a6f2ed14198d405b1` and DP22 block hash `f075a530804b757f7eb2ffd9b515abb71e90f3f702ea1ab92c19df21e931e57c`.

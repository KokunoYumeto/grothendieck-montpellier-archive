# AM-K028 — the literal unramified etaT does not exist for the ordinary J² host type

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

For the actual positive host
\[
 E'=\mathbb Q(\zeta_{28}),\qquad A=J^2,
 \qquad\Phi'=\{1,3,9,15,17,23\}\pmod{28},
\tag{ET1}
\]
there is **no Hecke character satisfying the source's literal `IsEtaT`**, when its chosen embeddings are this actual CM type. The obstruction already follows from its `unr` and `inf` clauses and from the defining triviality of a Hecke character on principal ideles. It is independent of all theta-lift estimates, the old `IsTen` issue, and the separate raw-Xi issue.

This statement is about the specified field/type pair. It is not a claim that such a character is impossible for every CM type, every larger host, or every infinity exponent.

## 1. Exact source conventions

The definition in `Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`, lines 308–312, is:

```lean
structure IsEtaT (X : Fields) (σ₀ : X.K →+* ℂ) (χ : HChar X.E) : Prop where
  unitary : χ.IsUnitary
  unr : ∀ v, χ.UnrAt v
  res : χ.ResEta X.F
  inf : χ.HasInf (X.embC σ₀) (fun _ => 1)
```

The exact imported definitions were recovered and read in
`Formalism/LocalToGlobal/UnitaryNorms/IsUnitaryNormOf.lean`:

| Lines | Literal definition or consequence |
|---|---|
| 11–19 | `HChar L` is a continuous homomorphism on the ideles, trivial on `diagUnits L k` for every \(k\in L^\times\). |
| 37 | `infDiag` is the product of the infinite local embeddings of a principal element. |
| 59–65 | `loc`, `locK`, and `inf` are restrictions of that same global character. |
| 71 | `UnrAt v` means the local character is one on every local unit. |
| 90–91 | `HasInf φ n` prescribes the angular exponent n itself. |
| 93–94 | `HasInfQ φ a` instead requires an integer n with \(n=2a\). |
| 194–204 | `TrivOn` and `ResEta` impose separate restrictions to the real subfield. |

In particular the actual infinity convention is
\[
 \chi_\infty(k)=
   \prod_{\tau\in\Phi'}
       \left(\frac{\tau(k)}{|\tau(k)|}\right)^{n_\tau}.
\tag{ET2}
\]
The `IsEtaT` exponent is exactly \(n_\tau=1\), with no factor two and no inverse. The nearby `IsMu0.inf` uses `HasInfQ` and has a different convention. Confusing the two would change this test.

`Chars.Tied.etaT`, in `AbelianHostFieldConditions.lean`, lines 325–333, actually requires this `IsEtaT`; it is not an optional later specialization. The separate `res` and `unitary` clauses can only restrict the possibilities further.

## 2. The global-unit obstruction

### Lemma ET3

Let L be a number field, let \(\chi:\mathbb A_L^\times/L^\times\to\mathbb C^\times\) be a continuous Hecke character, and assume every finite local component is unramified. Then
\[
                    \chi_\infty(\varepsilon)=1
             \qquad(\varepsilon\in\mathcal O_L^\times).
\tag{ET3}
\]
Consequently, if \(\chi\) has the angular infinity prescription (ET2), then necessarily
\[
       \prod_\tau
       \left(\frac{\tau(\varepsilon)}{|\tau(\varepsilon)|}\right)^{n_\tau}
                           =1
       \qquad(\varepsilon\in\mathcal O_L^\times).
\tag{ET4}
\]

**Proof.** Put \(U_f=\prod_{v<\infty}\mathcal O_{L_v}^\times\), embedded in the ideles with infinite component one. The direct sum of the local unit groups, namely the subgroup whose entries are one outside a finite set, is dense in this product. The unramified hypotheses kill every factor and hence this dense subgroup. Continuity then gives \(\chi|_{U_f}=1\). For a global unit \(\varepsilon\), its principal idele is the product of its infinite idele and a member of \(U_f\). The global character is one on that principal idele by definition. Dividing by the finite value one proves (ET3), and (ET2) gives (ET4). ∎

The density argument is included because the finite components of a principal root of unity need not be one at all but finitely many primes. One must not replace that idele by an unjustified finite product. Equivalently, the usual Hecke product formula gives (ET3), but no unproved `ProductRule` field is needed here.

### Theorem ET5

For the field and actual CM type (ET1), no character satisfies `IsEtaT`.

**Proof.** Apply (ET4) to the global unit \(\varepsilon=\zeta_{28}\). Every archimedean absolute value is one. The actual six embeddings give
\[
 \prod_{a\in\Phi'}\zeta_{28}^a
       =\zeta_{28}^{1+3+9+15+17+23}
       =\zeta_{28}^{68}=\zeta_{28}^{12}.
\tag{ET5}
\]
This has order \(28/\gcd(28,12)=7\), so it is not one. Lemma ET3 contradicts the simultaneous `unr` and `inf` clauses. ∎

There is a useful check using the original primitive CM field. The type \(\Phi'\) restricts to two copies of \(\{1,2,3\}\) modulo 7. Therefore the unit \(\zeta_7\) has prescribed infinity value \(\zeta_7^{2(1+2+3)}=\zeta_7^{12}=\zeta_7^5\ne1\). This is the same order-seven obstruction. No ambiguity in the choice of a primitive 28th root affects it.

Changing the coefficient embedding or applying a Galois conjugation to the whole field/type pair multiplies the exponent 12 by a unit modulo 28, so the nontrivial value still has order seven. Complex conjugation merely inverts it. A different choice of integral frame or a norm-one theta translate does not affect a global infinity-type obstruction.

## 3. What twisting or taking powers can and cannot change

Every everywhere-finite-unramified character with **uniform integer angular exponent n** on this same type must satisfy
\[
                     28\mid68n,
             \quad\text{equivalently}\quad 7\mid n.
\tag{ET6}
\]
Thus the literal exponent one is excluded. Taking a seventh power can kill this particular root-unit value, but changes the infinity exponent to seven and therefore does not produce the prescribed `IsEtaT.inf`. Taking a root to restore exponent one would restore the same contradiction if it were still unramified everywhere finite.

Similarly, multiplying by an everywhere-unramified finite-order character cannot compensate (ET5): that character has trivial value on all finite global-unit components and trivial continuous angular infinity type. Any Hecke character with the prescribed angular type one must have some finite ramification. Allowing such ramification is a change to the literal `unr` clause, with additional local and global data to control; it is not a solution of the same source record.

These statements concern a necessary unit condition. They do not assert that the exponent-seven character exists with every remaining source restriction merely because (ET6) is then satisfied. Other units and the exact restriction `ResEta` must also be checked.

## 4. Ordinary J powers and a type-preserving extension

### Proposition ET7. Compatible full CM actions on ordinary J powers

Suppose a full CM field L of degree \(6s\) acts on \(J^s\), contains the specified central cyclotomic field \(E=\mathbb Q(\zeta_7)\), and its chosen CM type \(\Psi\) is the actual holomorphic type of that ordinary product. Any Hecke character of L that is unramified at every finite place and has uniform angular exponent one on \(\Psi\) necessarily satisfies
\[
                                7\mid s.
\tag{ET7}
\]

**Proof.** On \(H^0(J^s,\Omega^1)\), each of the three E-characters \(1,2,3\) occurs with multiplicity s. On restricting the full CM type \(\Psi\) to E, its embeddings therefore have exactly those multiplicities. The prescribed angular value on the global unit \(\zeta_7\in E\subset L\) is
\[
 \prod_{\tau\in\Psi}\tau(\zeta_7)
                    =\zeta_7^{s(1+2+3)}=\zeta_7^{6s}.
\]
Lemma ET3 says this value is one. Since 6 is invertible modulo 7, one obtains \(7\mid s\). ∎

This applies to compatible maximal CM subfields in the standard matrix endomorphism algebra of an ordinary J power. It does not apply unchanged to products with conjugated E-actions, to a type unrelated to the actual Hodge representation, or to a CM field that does not contain the specified central E. For the host (ET1), s=2, recovering the contradiction above. Passing merely from J² to another ordinary multiplicity prime to seven cannot repair it.

### Totally real extension of the current host

Let \(F'=(E')^+\), let \(\widetilde F/F'\) be totally real of degree e, and set \(\widetilde E=E'\widetilde F\). Since every real element of E′ lies in F′, one has \([\widetilde E:E']=e\). Give \(\widetilde E\) the CM type induced from \(\Phi'\), consisting of every lift of each chosen embedding. The old root \(\zeta_{28}\) then has prescribed angular value
\[
                  \zeta_{28}^{68e}.
\tag{ET8}
\]
Hence any literal unramified type-one character on this induced pair necessarily has
\[
                               7\mid e.
\tag{ET9}
\]
For degrees prime to seven the obstruction persists, including extensions of degrees that are powers of two. This is also Proposition ET7 with the resulting ordinary multiplicity \(s=2e\). Degree seven kills this **particular** obstruction without changing the exponent one on the enlarged CM type.

There is an elementary explicit degree-seven candidate extension: let B be the unique degree-seven subfield of \(\mathbb Q(\zeta_{29})\). Its fixing subgroup in the cyclic group of order 28 has order four and contains complex conjugation, so B is totally real. Since \([F':\mathbb Q]=6\) is coprime to 7, \(F'\cap B=\mathbb Q\); therefore \(\widetilde F=F'B\) has degree seven over F′. For this candidate, (ET8) is one.

Nothing here proves that all unit angular values on \(\widetilde E\) are trivial, that an unramified character with `ResEta` exists, or that the enlarged CM lattice satisfies the required source frame and polarization conditions. New units of the extension, its class group, the finite restrictions, and the enlarged arithmetic host remain exact tasks. This is a narrowly identified possible repair, not a completed one.

Nor is the obstruction universal among CM types on E′ itself. For example the type induced from the quadratic residue choice modulo seven,
\[
                   \{1,9,11,15,23,25\}\pmod{28},
\]
has exponent sum 84, so this root-unit test is trivial for it. That is a different type from the ordinary primitive-J² type in (ET1); passing to it does not preserve the geometric construction already checked here. No existence conclusion is inferred from its passing this one test.

## 5. Consequence for the current machine adapter

The positive ordinary host, its exact theta germ and canonical gauge, its selected compact Cauchy shapes, and its permitted finite-jet arithmetic are unaffected as independently stated results. But on this unchanged field/type pair, the literal `Chars.Tied` record cannot be completed because its required `etaT` does not exist. This is stronger than merely leaving its construction open. It does not question the accepted source theorem, whose hypotheses concern its own arithmetic host.

Accordingly, AM-K027's exact selected-family slope and the class-supported constructions remain results in the actual indicated positive local/global model, with the full source arithmetic adapter still absent. A valid eventual adaptation must change or enlarge the host/type or explicitly replace the unramified auxiliary-character interface and account for that change. It cannot fill this field with a conventionally normalized character on the same pair.

## 6. Provenance and checks

The source definition of `IsEtaT` was already present in the intake-pinned recovery. The additional imported file `IsUnitaryNormOf.lean` was retrieved in this run from the exact pinned mirror commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`:

https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Formalism/LocalToGlobal/UnitaryNorms/IsUnitaryNormOf.lean

Its SHA256 is `503df2de36607142871ffe2399c86c903953535658077b7e06b4f6ce593d6739`. It is **absent from the supplied selected author-file manifest**, so this run does not claim a new byte comparison of that member with the author's original archive. The precise retrieval and that null comparison status are recorded in `work/research/source_recovery_20261121T231352Z.json`. The infinity convention is directly visible in the recovered source, and the mathematical obstruction is proved above from that displayed convention.

The actual host/type input is accepted DP57 and AM-DO-022 (DO22.1)–(DO22.3). The only new mathematical input is the elementary global-unit argument and its explicitly scoped consequences. The exact residue sums and orders have a separate arithmetic certificate. No Lean compilation, unramified-character existence theorem, or full enlarged-host construction is claimed.

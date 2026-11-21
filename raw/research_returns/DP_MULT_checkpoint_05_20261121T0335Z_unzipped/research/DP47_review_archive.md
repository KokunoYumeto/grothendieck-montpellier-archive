# DP47: independent complete hyperbolic pullback proof and broadened integration review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime effort **not exposed**. Date: **2026-11-21 UTC**. Events **ABA-CE51** (complete original proof) and **ABA-CE52** (complete broadened integrated proof). Review interval **02:47:00–02:49:02 UTC**. No main-paper edits.

## Outcome and versions

**PASS.** I read the full original memo §§1–7, the entire intended paper subsection, and the final broadened fragment covering DP46's unit-arrow models. I independently challenged the actual adjunction, torus ambiguity, trace-one sign and coefficient, gauge difference, integral frame changes, and polarized-block criterion. The broadened statement is justified by the same proof, because DP46 establishes exactly the torus and invariant-frame properties it uses.

| Scope | SHA-256 |
|---|---|
| Entire original memo | `23224c9710cf293bf22637a1e37fccd5a36657b4a184d7fa6b40b00eb4e99b42` |
| Complete original statements/proofs, §§1–6 | `fdbd824b0116a82c09560510b0f1ea0b81366e621e3228d8a5a1b101385eac81` |
| Entire broadened integrated fragment | `2687aacb43e64dc6a1c8ed6b5fd7fd8faf3842c52add11c73950c619d3f432a3` |
| Complete integrated proposition and proof | `4c5142ef8e950fefd5e1dfc25c2c19f6bd200f3691328df033810e76298e8723` |

The whole current fragment occurs exactly once in the main paper. Frozen versions and `DP46_DP47_DP48_integration_metadata.json` are under `late_proof_snapshots`.

## 1. Actual adjunction and its bilinear ambiguity

The actual Cartier-dual pairing supplies an integral adjunction preserving the laws and axial rigidifications. Its scalar in integral frames is therefore an integral normalized unit. The quotient of the transported rational bilinear sections is a formal bihomomorphism. In characteristic zero its logarithm is bilinear in the additive logarithm coordinates; comparing binomial coefficients establishes degree one separately in each variable.

The adjunction is natural under the torus when the endomorphism commutes with it. Both chosen frames and splittings are equivariant. None of the characters `1−p^i`, `1≤i<h`, is trivial modulo `p^h−1`, so the invariant bilinear ambiguity is zero. This proves that the specific ratio `B(ax,y)/B(x,a^D y)` is an integral unit, rather than merely that some rationally adjusted ratio could be integral. The argument is unchanged for DP46's arbitrary unit arrows: their exact torus and invariant primitive frame were independently checked in ABA-CE47/50.

## 2. Trace-one identity and sign

With `c=1−a`, additivity of actual Cartier duality gives `a^D y+_H c^D y=y`. Substituting into the dual addition factor produces the stated product identity. Taking its inverse gives `U_0=C_H/J_a` and one factor `B^(−1)`. The two contributions are added by the trace-one relation; no eigenvalue difference occurs.

The product gauge is the negative logarithm of the two cross factors. Its symmetry is literal, its axes vanish, and its negative coboundaries are the integral addition factors. The actual adjunction units give the corresponding adjoint scalar. Thus the source sign yields primitive coefficient exactly `−1`, and integer tensor power gives exactly `−κ`. Only ordinary nonnegative integer powers of the integral unit are used. The requirement `p∤κ` for the unit-exponential radius theorem is retained.

## 3. Gauge changes and quadratic remainder

After the frames have been identified, dividing the two canonical gauge equations and using injectivity of formal exponential shows that the difference is biadditive. Symmetry and adjoint balance are inherited from the other identities. Passing to formal logarithms makes it bilinear; the integral endomorphism `w_0` becomes its tangent linear map. Pullback along the diagonal therefore gives a homogeneous quadratic form.

An integral frame change must be accounted for first. It contributes the logarithm of an integral normalized unit, and the integral pullback preserves that property. The remaining difference is then bilinear. This order of operations is correct and prevents an invalid assertion that every integral frame change itself is bilinear. The final expression separates an integral prefactor, the primitive factor and the rational quadratic remainder exactly as stated.

## 4. Geometric criterion

The conjugate integral idempotents and adjoint balance canonically trivialize the same-factor restrictions as biextensions, using the axial rigidification. A polarization that is an isomorphism on the p-divisible block gives perfect cross factors and identifies the complementary block with the actual Cartier dual. Symmetry identifies the opposite cross restriction with its transpose, and biadditivity reconstructs the hyperbolic product. Every step is integral. The alternating finite-torsion Weil pairing does not insert a minus sign between these symmetric-biextension cross factors.

The assumptions about an actual integral decomposition and prime-to-p polarization are retained. A Newton-slope count does not replace them. The broadened local theorem does not assert a new global mixed-CM family or supply a prescribed path.

## 5. Direct source checks during this event

I directly read `CocycleRightZeroThd.lean` lines85–192, including the integral FB adjunction laws, all `IsCanonGauge` conditions, `hL`, and `nabVal`. The displayed source convention is exactly the negative-coboundary convention used here. I also read the complete saved `CanonGaugeSubIsBiadd.lean` proof and the `CanonGaugeIndependenceAll.lean` theorem statements, and checked `ExpConjConnectionIntegral.lean` lines32–46, whose theorem explicitly assumes `w_0+star(w_0)=1` at line40.

These are direct textual checks of the recovered author source. No Lean execution or machine validation is claimed. The actual Zink dual-pairing functoriality uses the already checked primary-source construction and exact locators retained in the paper.

## Limits

The result identifies the actual local primitive kernel under the stated polarized-block assumptions. The nonzero-restriction condition is explicit: global nonvanishing of a theta section alone does not establish it. The rational quadratic remainder is retained and passed to DP48, rather than discarded. The prescribed global path, selected harmonic module, nonzero minors and global cost comparison remain separate inputs.

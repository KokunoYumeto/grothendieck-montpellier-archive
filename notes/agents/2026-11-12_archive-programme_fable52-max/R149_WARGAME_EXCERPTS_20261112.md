# War-game excerpts cited by the prompts LM6 (revised), CYCLOTOMIC_KERNEL and FLAGGED_149

Cut by R-149 (Claude Fable 5.2, effort max), 12 November 2026, from the two war-game files and the hunches file of the same day (all by Claude Fable 5.2, effort max). Every statement below is unchecked unless R149_NOTES_20261112.md says otherwise. Marks: [C] checked that day in a file or by a lookup, [B] believed, [G] guess. "Astra" is GPT-6 Astra (ChatGPT Pro mode).

## From round 2, section 7: results R1-R4

**R1. The threshold in 16 scan 29 is 6.** *Statement.* Let V have dimension 4, χ ≠ 0 a 4-form, Q(a, b) = χ(a∧b) on
Λ²V, ξ ∈ Λ²V with Q(ξ, ξ) = 1 and φ(x, y) = Q(x∧y, ξ) non-degenerate, φ̌ ∈ Λ²V the inverse bivector, and
u = Λ²(φ^♯) ∘ Q^♭ (the convention of the notes' D19). Then u(ξ) = 2ξ, u = −2 on the Q-orthogonal complement of ξ,
and φ̌ is a multiple of ξ. So the orbits of ξ and φ̌ under u span a line: nothing happens in dimension 4, and the notes' example
(D19) shows that spans of dimension 3 occur in dimension 6. *Sketch.* All such (χ, ξ) are equivalent over an
algebraic closure; in the normal form ξ = a e₁∧f₁ + b e₂∧f₂, χ = c e₁*∧f₁*∧e₂*∧f₂* with 2abc = 1 one finds
u(e₁∧f₁) = e₂∧f₂/(a²c), u(e₂∧f₂) = e₁∧f₁/(b²c) and u = −2 on the four mixed basis vectors. *Meaning.* For an
abelian surface u is twice the Hodge star on H²: the Fourier transform followed by pull-back along the
polarization. *What would check it.* A six-by-six computation by script; the reading of "4 (ou 6 ?)" and of the
definition of u on the scan.

**R2. The cyclotomic kernel sees the cusps (S6 of round 1, argued in full).** *Statement.* K a number field, U a
hyperbolic curve over K, π its geometric fundamental group, s a section, Γ° the kernel of the cyclotomic character,
C the centralizer of s(Γ°) in π. If U is proper, C = 1. If U is affine, C = 1 unless s normalizes an inertia group
I_x, and then C = I_x and x is unique. *Sketch.* (1) Let z ≠ 1 be in C, N an open characteristic subgroup of π not
containing z, H = N⟨z⟩. An open subgroup of Γ normalizes H through s, so H belongs to a covering defined over a
finite extension K′, and the class of z in H^ab is fixed by Gal(K̄/K′(μ_∞)). (2) Proper case: H^ab is the Tate
module of a Jacobian; it has no invariants under that group, because the torsion of an abelian variety over K′(μ_∞)
is finite (Ribet [C, lookup 10]); but z generates H/N ≠ 1. (3) Affine case: by the same theorem the class of z lies
in the image W of the inertia groups in H′^ab, for every open H′ containing z; by the weight criterion for inertia
(Nakamura; Stix, Theorem 20 [C for its existence, lookup 6; its exact form to be checked]) z lies in an inertia
group. (4) C lies in one inertia group: if z ∈ I_x and z′ ∈ I_y were non-trivial elements of C with x ≠ y, then
zz′ ∈ C lies in some I_w; in an open H containing C with at least four cusps in which x and y are distinct, W is
the free module on the cusps modulo the diagonal, and the relation [z] + [z′] = [zz′] forces [z] = 0 or [z′] = 0,
while an inertia group of H injects into H^ab. (5) Γ° is normal, so s(Γ) normalizes C and hence I_x; conversely a
section normalizing I_x acts on it through the cyclotomic character, so I_x ⊂ C. *What it gives in 149.* His
"précisions" to Conjecture A (scan 56 margin); (3) of scan 55; the missing case (0,3) of the Proposition of scan
54; the "conséquence conjecturale" of scan 49 for curves; for Γ°, at most one fixed point at infinity in
Conjecture B; and the reading that his Conjecture fondamentale for V a point is the section conjecture. It
repairs the Longue Marche §34 (FINDINGS F17). *What would check it.* CYCLOTOMIC_KERNEL. *Novelty.* None claimed;
recent work over cyclotomic extensions uses the same theorem of Ribet (1.7).

**R3. The centralizer in Γ_Q of the absolute Galois group of k(μ_∞) is trivial** (149 scan 45, "à vérifier !").
*Sketch.* Enlarge k to be Galois over Q; put F = k(μ_∞). Let σ commute with every element of G_F. Then for every
x the stabilizers of x and σx in G_F agree, so F(σx) = F(x); in particular σ(F) ⊂ F, and for a ∈ F* and a prime ℓ,
Kummer theory gives σ(a) = a^j c^ℓ with j prime to ℓ. If σ moved a number field k′ ⊂ F, Galois over Q, take p
split completely and unramified in k′, a prime 𝔭 above it (so σ𝔭 ≠ 𝔭), a ∈ k′ of valuation 1 at 𝔭 and 0 at the
other primes above p, and ℓ not dividing p(p − 1). At a place of F above 𝔭 the value group is (1/(p − 1))·Z[1/p], in
which 1 is not divisible by ℓ; the valuations of σ(a) = a^j c^ℓ give 0 ≡ j modulo ℓ, a contradiction. So σ fixes
F. The same argument over every finite extension of F, each again of the form k″(μ_∞), shows σ = 1. *What would
check it.* One Part of FLAGGED_149; it is probably in the literature on Hilbertian fields.

**R4. The limit action at a place of bad reduction is not that of a curve** (149 scans 101–103, e ⟹ a).
*Statement.* Let U_η be a proper hyperbolic curve over the fraction field of a henselian trait with residue field
k of finite type over Q, with stable bad reduction. For any splitting of 1 → T → 𝓔_η → 𝓔_k → 1, the resulting
outer action of 𝓔_k on π is not the outer action attached to a smooth proper curve over a finite extension of k,
(i) if the Jacobian has toric rank t > 0, (ii) if t = 0 and the components of the special fibre have pairwise
non-isogenous Jacobians with endomorphism ring Z. *Sketch.* (i) On π^ab ⊗ Q_ℓ the Frobenius weights of the limit
action are 0 and −2 with multiplicity t and −1 elsewhere (the monodromy filtration; the graded pieces do not depend
on the splitting), while H₁ of a smooth proper curve is pure of weight −1. (ii) π determines H₁ with its symplectic
form; here it is that of the product of the Jacobians of the components with the product polarization; an
isomorphism with H₁ of a smooth curve C, for all ℓ and compatible with the forms, makes Jac C isomorphic to that
product as a polarized variety (Faltings; the hypothesis leaves no other principal polarization), and the theta
divisor of a Jacobian is irreducible. *Left open.* Compact type with isogenous components, where H₁ with its form
does not decide. *What would check it.* A Part of LM6 revised.

**A reading, not a result.** Th. 5 of 44 ("Néron") is the height pairing of Beilinson and Bloch over a function
field, twenty years before it was defined [B]: to be confirmed by JACOBIANS_1964.

## From round 2, section 1.7: rows S23, S24 and the note on S7

- **S7 (B, B′).** After R2: for Γ° there is at most one fixed point at infinity, and it exists exactly for cuspidal sections. Uniqueness at finite distance for Γ° is injectivity of points → sections over K(μ_∞), where the toric part does have divisible elements (roots of unity): this is the hard part, and the subject of the recent work just named.
| | Statement | Rests on | Plausibility; what would decide it | V | T |
|---|---|---|---|---|---|
| S23 | The "Conjecture-à-tout-hasard" of 149: status table of a)–f) | 149 scans 99–103 | a ⟺ b known; c, d ⟹ a false; e ⟹ a by weights and by Torelli except when the components of a compact-type reduction are isogenous (R4, unchecked) | 3 | 4 |
| S24 | Characterize profinitely the geometric tangential sections (the torsor under K* inside the torsor under K̂*) | 149 scan 85 | Open, to my knowledge; it is the integrality question for Kummer classes. Record | 4 | 1 |

## From round 1, section 3: S6 and S7

### S6. The cyclotomic kernel sees the cusps (found in this pass; unchecked)

- **Statement.** Let U be a hyperbolic curve over a number field K, π its geometric fundamental group, s any section
  of π₁(U) → Γ_K, and Γ° the kernel of the cyclotomic character. Then the centralizer of s(Γ°) in π is trivial if s
  is not cuspidal, and is the inertia group L_i if s is cuspidal at the cusp i. Hence s is cuspidal if and only if
  that centralizer is non-trivial, and the inertia groups are exactly the non-trivial centralizers of this kind for
  germs of sections.
- **Argument** [B, mine]. Proper case. Let z ≠ 1 centralize s(Γ°); take a characteristic open N with z ∉ N and put
  H = N⟨z⟩. For a finite extension K′, s(Γ_K′) normalizes H, so H is the geometric group of a covering defined over
  K′, and the class of z in H^ab is fixed by Gal(K̄/K′(μ_∞)). H^ab is the Tate module of a Jacobian, and its
  invariants under that group vanish because the torsion of an abelian variety over K′(μ_∞) is finite (Ribet, 1981,
  appendix to Katz–Lang; cited, not opened today). But z generates H/N ≠ 1. Affine case. The invariants of H^ab are
  its part of weight −2, so z lies in an inertia group by Nakamura's characterization of inertia elements (1994,
  near (2.1.1)–(2.1.4); from memory); the centralizer lies in one L_i; the normalizer statements of FINDINGS F5
  then put s(Γ) in the decomposition group of i.
- **Rests on.** 149 scan 55 ("hautement plausible", to be put among the "conjectures-clefs") and the margin of scan
  56; LM 2:sc433; FINDINGS F17 (2:sc483 is false as written) and hunch H5, whose note calls the point case
  conjectural. It agrees with LM3b D.5: a line with complex multiplication has an open normalizer and is not
  centralized by Γ°.
- **Plausibility.** Proper case: I hold it proved, given Ribet's theorem. Affine case: it hangs on one lemma quoted
  from memory. Novelty: one search found nothing; none is claimed.
- **What would decide it.** A check by GPT-6 Astra; then finitely generated fields (Katz–Lang), M(g,n), real places.
- **Bears on.** III (149; LM §§32–34); LM6. **V 4, T 5. Pursue** (CYCLOTOMIC_KERNEL; then into LM6).

### S7. The fixed-point conjectures B and B′

- **Statement** (149 scans 59, 63). B: every action of Γ on the universal profinite covering Ũ that comes from a
  section has exactly one fixed point in its completion, and so has Γ°. B′: for a "courbe de Poincaré" 𝒰 over K̄
  with completion 𝒳 and any action of Γ compatible with its action on K̄, Γ° has exactly one fixed point on 𝒳; no
  group π is assumed normalized.
- **Rests on.** B for Γ is the section conjecture with cusps in its limit form [B]. B′ is stronger; I know no
  counterpart.
- **Plausibility.** B: that of the section conjecture; uniqueness for Γ° may follow as in S6. B′: unknown. An
  action that normalizes no π is a tower of K-forms cofinal in the universal tower; the test is whether such towers
  exist beyond those of sections.
- **Bears on.** 149; LM6. **V 3, T 2. Record; one Part in the revised LM6.**

## From the hunches file: H1 and H2

## H1. The centralizer theorem holds for every subgroup with no invariants in Tate modules (sharpens S6/R2). Believe.

**Statement.** Let K be a number field, U a hyperbolic curve over K, π its geometric fundamental group, s a section
of π₁(U) → Γ_K, and Δ a closed normal subgroup of Γ_K such that for every finite extension K′ and every abelian
variety A over K′ the Tate module T(A) = ∏_ℓ T_ℓ(A) has no non-zero invariant under Δ ∩ Γ_K′. Let C be the
centralizer of s(Δ) in π. Then C = 1, except when U is affine, s normalizes an inertia group I_x, and the cyclotomic
character is trivial on Δ; in that case C = I_x. Instances: Δ = Γ° (Ribet); Δ the group of K(μ_(ℓ^∞)) for one ℓ
(Imai, Serre). For Δ the group of K^ab the hypothesis fails exactly in the presence of complex multiplication
(Ruppert), and the statement should fail with it.

**Why.** The proof of R2 uses Γ° only through the vanishing of invariants: for z ≠ 1 in C and H = N⟨z⟩, the class
of z in H^ab is Δ-invariant, hence zero in the Tate module of the Jacobian of the covering; in the proper case this
contradicts z generating H/N; in the affine case it puts z in the weight −2 part for every H, hence in an inertia
group (Nakamura's criterion), and the relation [z] + [z′] = [zz′] in a covering with four cusps forces one inertia
group.

**Smallest test.** U = P¹ minus {0, 1, ∞} over Q, s the tangential section at 0, z = [x, y]. In the Fermat covering
of level ℓ^n the class of z generates H^ab over the group ring, and σ acts on it by Ihara's power series F_σ. The
prediction is that z is not centralized by s(Γ°), that is, F_σ ≠ 1 for some σ fixing all roots of unity. This is
known (the series F_σ carries Jacobi sums). The same test with y in place of z gives a class in the weight −2 part,
as it must.

**What would refute it.** A non-trivial non-inertia element whose class is of weight −2 in every open subgroup
containing it (the criterion quoted from Nakamura would then be misquoted); or a covering in which two distinct
inertia groups of C cannot be separated among four cusps.

**Bears on.** 149 scans 45, 49, 54–56, 59–63; LM 2:sc433, 2:sc483; FINDINGS F5, F17; LM3b D.5; R2 and R3 of round 2.

**Prompt (CYCLOTOMIC_KERNEL, extended).** Prove the statement for a general Δ as above, each step written out, with
the weight criterion for inertia quoted from its source with its hypotheses. List the Δ for which the hypothesis is
a theorem (Ribet, Imai, Serre, and the recent results on Kummer-type extensions of cyclotomic fields). For Δ the
group of K^ab and a curve with a CM Jacobian, decide whether C can be larger, by an explicit computation on a
two-step nilpotent quotient and then in π. Done: a proof or counterexample per item. Unacceptable: assuming any form
of the section conjecture.

---

## H2. A limit action always carries its vanishing cycle; a smooth proper curve never does (completes R4). Believe.

**Statement.** (a) Let C be a smooth proper curve of genus ≥ 2 over a number field k, π its geometric fundamental
group, Γ′ an open subgroup of Γ_k. There is no element γ ≠ 1 of π such that Γ′ preserves the conjugacy class of the
closed subgroup ⟨γ⟩ and acts on it through the cyclotomic character. For a smooth affine curve the classes with this
property are exactly those of subgroups of inertia groups. (b) For a stable degeneration over a henselian trait with
residue field k and any splitting of 1 → T → 𝓔_η → 𝓔_k → 1, the limit action of 𝓔_k preserves the conjugacy class of
the procyclic group of each vanishing cycle and acts on it through the cyclotomic character. Hence the limit action
is never that of a smooth proper curve over a finite extension of k, in all cases of bad reduction; and for affine
curves, good reduction holds if and only if the number of such classes of maximal procyclic subgroups equals the
number of cusps. This closes the case R4 left open (compact type with isogenous components).

**Why.** (a) is the argument of H1 with weights in place of Ribet: the normalizer of ⟨γ⟩ in π₁(C) maps onto an open
subgroup of Γ_k; in H = N⟨γ⟩ the class of γ spans a Galois-stable line of H^ab on which Galois acts by the cyclotomic
character, and Hom(Z_ℓ(1), T_ℓ(A)) = 0 over a number field by weights; so the class is zero, against γ generating
H/N. (b): inertia acts through a profinite multitwist; 𝓔_k normalizes it and acts on T by the cyclotomic character;
a profinite Dehn twist determines its curve up to conjugacy (results of combinatorial anabelian geometry, Hoshi and
Mochizuki, quoted from memory).

**Smallest test.** Genus 2 degenerating to two elliptic curves E₁, E₂ joined at a point, with E₁ = E₂ of complex
multiplication: here H₁ with its symplectic form cannot decide, and the separating vanishing cycle γ in [π, π]
does.

**What would refute it.** A smooth proper curve over a number field whose outer Galois action normalizes a
procyclic subgroup with cyclotomic action; or a limit action in which the class of ⟨γ⟩ is not preserved, which would
contradict the rigidity of profinite Dehn twists.

**Bears on.** 149 scans 99–103 (the "conjecture-à-tout-hasard", e ⟹ a); 147 §§9–10; cote 64 (unread); RESIDUE H.3
(the lifting category BZ at a node; the returns' claim); R4 of round 2.

**Prompt (a Part of LM6 revised, or GOOD_REDUCTION).** Prove (a) and (b) with every profinite step written out,
citing the exact statement on profinite Dehn twists that is used. Deduce the full table of 149's
"conjecture-à-tout-hasard" a) to f): a ⟺ b (Oda, Tamagawa, cited), c and d strictly weaker (example of compact
type), e ⟹ a in all cases. State what "pas trop loufoque" (his f) can be made to mean so that f ⟺ a. Done: proofs,
or the precise missing statement.

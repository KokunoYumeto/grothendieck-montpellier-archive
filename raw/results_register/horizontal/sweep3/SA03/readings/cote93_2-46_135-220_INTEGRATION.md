# Cote 93, scans 2-46 and 135-220: integration (reader R4, Claude Opus 5.5 at effort max, for a6d42bf6fe2b0d8a8)

The full reading is `cote93_2-46_135-220.md`. Hunches are numbered H93-R4-n, so that they do not collide with R1's H93-n.

## STUDY

These pages hold one line of work, on characteristic p, connections and crystals. They are written on reused paper: Deligne's formulaire typescript, Wanderley's 1981 offprint, a functional-analysis offprint and an IHES letterhead. They fall into five blocks.

**93/3-25: genus-one curves.** Deligne's typescript gives Tate's formulas for genus-one curves over any base. His notes add:
- the Hasse invariant, Legendre's j and Hasse's polynomial;
- the supersingular j-values by p mod 12;
- the formal moduli at j = 0 = 1728 in characteristics 2 and 3;
- "a_1 et ±b_2 sont les invariants de Hasse Witt".

Every identity tested holds (sympy). His question whether the Hasse invariant at the cusp is 1 in du/u has the answer yes.

**93/27-46: orientation, the operator G, the crystal programme.**
- 93/27-33: Wanderley's axiomatic orientation of manifolds with boundary, and his own axioms. They use the "rives" of a hypersurface, the banks of cotes 81 and 154.
- 93/36: a sheet on the operator G of 93/72-84 under g = exp f. There "3(df)²" is a slip for df² (K93-01).
- 93/37-46: "V Programme de la Théorie (Cristaux)", the opening of the Montréal Barsotti-Tate notes. It covers Dieudonné crystals over a base where p is locally nilpotent, Problems 1-3, the deformation theorems later proved by Messing and Mazur-Messing, and the universal vectorial extension as a crystal.

**93/135-167: characteristic 0.** The uniformization of 93/92-134 gives a canonical projective connection on a curve.
- He takes "régulière à l'infini" to mean "at most simple poles". That is not regularity: the uniformizing connection has a double pole (1/2)dq²/q² at every cusp and is regular singular in Fuchs's sense (K93-02).
- His space of choices, H^0(X̂, ω²(D)), of dimension 3g-3+ν, ν or max(0, ν-3), is canonically the cotangent space of M_{g,ν}; his "can. ?" has the answer yes. It is the right space for connections with fixed principal parts, the accessory parameters.
- The rest of the block:
  - connections and stratifications on torsors (H^1_DR classifies torsors with integrable connection);
  - Picard-Fuchs operators and the "section de Manin";
  - Gauss-Manin after Katz-Oda.

**93/168-218: characteristic p.**
- *The Cartier operation with a p-basis.* The inverse Cartier map lands in de Rham cohomology, not in closed forms (K93-03, found first by the stage-A dossier).
- *p-curvature.* Jacobson's formula, and the criterion that d + ω has zero p-curvature iff C̃ω = ω̃. Then logarithmic forms, the top-degree Cartier map as the trace of Frobenius, and V on Pic with the p-th power on Lie (his "Demazure-Gabriel ?": yes).
- *Curves.* The pairing C̃(f dg) on Q = F_*O/Λ is perfect and alternating; the condition is i + j = p, not p - 1 (K93-04).
  - Its determinant is (-1)^{(p+1)/2}, not always +1. The canonical square root of det(Q)² ≅ Ω^{⊗(p-1)} is the Pfaffian, ±((p-1)/2)! (K93-05).
  - In characteristic 2, Q is the canonical theta characteristic.
  - Pointless smooth conics do not exist over every imperfect field of characteristic 2 (K93-06).
- *93/188-198.* Cartier descent, finite monodromy and rank one. Then the p-curvature conjecture in his own hand, "La réciproque est-elle vraie ?", with variants for abelian schemes and group schemes.
  - c), the rank-one case through the universal vectorial extension, is now known.
  - e), lifting by Verschiebung at closed points only, is false: y² = x³ - 2x with P = (2, 2), the dossier's example, recomputed.
- *To the end.* Katz's Picard functors with connection (P^cip ≅ Pic^{(p)}, mapping to Pic by V), obstructions on a line bundle, and the plan of the canonical Gauss-Manin connection, which R1's 93/221-236 continue.

**What is left:**
- 93/135-220 has a single transcription, with 7.6 unsure marks per scan;
- the margin "à 0|1 trou";
- his verification (48), ν_Δ = μ_D;
- the isomorphism (24) under "Ω flat" alone;
- question d).

## HUNCHES

**H93-R4-1. The characteristic-p Schwarzian of 93/074 (R1).**
- *Grounds:* 93/36 (G under exp), 93/135-140 (the canonical connection) and 93/171-177 (the p-curvature calculus of d + ω).
- *The hunch:* the characteristic-p analogue of the canonical projective connection is an oper with zero or nilpotent p-curvature. These are Mochizuki's dormant or nilpotent indigenous bundles (Foundations of p-adic Teichmüller theory, 1999). Dormant opers are finite in number over the moduli, and Wakabayashi counts them (locators to be checked).
- *What it sharpens:* R1's question becomes a computation. Write the rank-two oper of G in Riccati/Miura form, apply the rank-one calculus of 93/176 to it, and find when its p-curvature vanishes.

**H93-R4-2. The torsor device of 93/234-236 against Deligne-Illusie.**
- *Grounds:* 93/142-153 classify torsors with integrable connection by H^1_DR, and 93/169-170, corrected (K93-03), give C^{-1} into H^*_DR.
- *The hunch:* these are the two ingredients of the decomposition of P. Deligne and L. Illusie (Invent. Math. 89 (1987) 247-270). The missing step is that a lifting of X^{(p)} modulo p² makes local Frobenius lifts into a torsor under Hom(Ω^1_{X'}, F_*O_X/O_{X'}) or the tangent module, whose class splits τ_{≤1}F_*Ω^•. Nothing in this stretch reaches mod p². R1's 93/234-236 should be read for it.

**H93-R4-3. "Sont-elles algébriques ?" (93/115, R1's H93-5), if "elles" are the uniformizing projective connections.**
- *As a family over M_{g,ν}:* no. 93/136 makes them a section of an affine bundle modelled on T*M_{g,ν}. That section is real-analytic but not holomorphic: by P. Zograf and L. Takhtajan (Math. USSR Sb., 1988; locator to be checked), ∂̄ of its difference with a holomorphic section is a nonzero multiple of the Weil-Petersson form.
- *For a curve over Q̄ punctured at the full preimage of {0, 1, ∞} under a Belyi map β:* yes. X minus β^{-1}{0, 1, ∞} → P^1 minus 3 points is finite étale, so the uniformizing connection is β^* of the hypergeometric connection (exponent differences 0, 0, 0), which is defined over Q. The connection is therefore defined over Q̄.
- *Other punctures:* algebraicity of the accessory parameters is a transcendence question (to be checked).
- *Links:* this ties 93/135-138 to cote 81's special Belyi functions (SA01) and to the cartographic groups of cotes 79-80 (SA04).

**H93-R4-4. His "Questions" of 93/194-198.**
- *a), b), c):* the rank-one Grothendieck-Katz conjecture, known (Chudnovsky 1985; Bost 2001; André 2004; locators to be checked).
- *e):* false. Lifting by V at closed points loses the connection data, and the dossier's elliptic curve shows it.
- *d):* the local-global questions for points of group schemes (proper connected, unipotent rank zero, affine, unipotent subgroups) were not examined. For E the universal vectorial extension, pE_s ≅ A_s^{(p)} is an abelian subvariety, so the hypothesis of c) is a case of that of d). Whether d) reduces to c) there is to be checked.

**H93-R4-5. Problems 1-2 of the crystal programme (93/38-40).**
- *Full faithfulness.* It holds over bases formally smooth over a perfect field (A. J. de Jong, Publ. Math. IHES 82, 1995). It fails over some bases; the dossier cites Berthelot-Messing counterexamples. For later results with exact hypotheses, the dossier cites E. Lau, 2018/2026.
- *Problem 2 over perfect bases.* The dossier cites Lau (2013), crediting Berthelot and Gabber.
- *Status:* all locators are from the dossier (GPT-6 Astra, ChatGPT Pro mode), not checked by me.
- *Link:* 93/37-46 are the opening of the programme whose Problem 4 is on 93/49-51 (sweep 2's SA03-C3).

## PACKAGES

**P-R4-6. Projective connections across characteristic 0 and p in cote 93.**
- **Question.** Three parts:
  - (a) Restate his regularity criterion (93/135-138) in Fuchs's form, and redo his counts for fixed principal parts.
  - (b) Settle 93/115 for the uniformizing connections: Belyi-punctured curves (algebraic, by pullback), and general punctures (not holomorphic in the moduli). Give the exact statements and their sources.
  - (c) Answer R1's 93/074. Compute the p-curvature of the rank-two oper attached to the operator G of 93/72-84 with the calculus of 93/171-177, and identify the characteristic-p "canonical" connections with dormant or nilpotent opers.
- **Why it matters.** Three of his cote-93 threads meet here: the operator G (93/36, 72-84), the uniformization (93/92-134) and the Cartier and p-curvature calculus (93/168-218). Cote 81's Belyi functions join them too. It is where his pages come closest to Mochizuki's p-adic Teichmüller theory.
- **What it rests on:** R1's readings of 93/47-91 and 92-134; this reading of 93/135-140 and 168-218; K93-02.
- **The strongest known reduction:**
  - in characteristic 0, the accessory parameters form a torsor under T*M_{g,ν} (93/136, R93-08);
  - for Belyi punctures, the connection is β^* of the hypergeometric one;
  - in characteristic p, rank one: zero p-curvature ⇔ C̃ω = ω̃ (93/176);
  - rank two: the dormant locus is finite over the moduli (Mochizuki; locator to be checked).
- **Material:** cote 93 scans 36, 72-140 and 168-218 (R1 and R4); cote 81 (SA01: special Belyi functions); cotes 79-80 (SA04: cartographic groups).

**P-R4-7. The "Questions" of 93/194-198, with exact hypotheses.**
- **Question.** For each of a)-e), state the current answer and its exact hypotheses: a), b), c) the rank-one case (known); e) false (the counterexample); d) open on his page.
- **Why it matters.** This is the first statement of the p-curvature conjecture in his own hand, with an arithmetic base and group-scheme variants that the published form does not carry.
- **What it rests on:** R93-22, R93-23, H93-R4-4.
- **The strongest known reduction:** rank one is reduced to the universal vectorial extension of the Albanese or Picard variety (his own translation on 93/197), and is proved there.
- **Material:** cote 93 scans 188-198 and 205-213; the stage-A dossier §3.7, with its counterexample (SA03-1040).

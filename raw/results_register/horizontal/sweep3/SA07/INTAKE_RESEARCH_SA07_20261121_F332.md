# RESEARCH_SA07 F.3.32 against LM6 A.22: a targeted check (22 Nov 2026)

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), at the main session's request, after the full intake of
RESEARCH_SA07 by agent a922466087ec53798 flagged F.3.32.
- The run: RESEARCH_SA07, checkpoint 12, GPT-6 Astra (ChatGPT Pro mode).
- Checked: `sections/F_audit.tex`, lines 4628-4937, and `code/check_all_genus_single_line.py`.
- Check events: `INTAKE_RESEARCH_SA07_20261121_F332_CHECK_EVENTS.tsv`, beside this file.

## What F.3.32 claims

**(UC.1), a Lie-algebra statement.** For every g ≥ 3, every prime ℓ, every nonzero a ∈ Q_ℓ^{2g} and every D in the
actual universal degree-six image U_{g,6}: if D(a) ∈ [L₆(V), a], then the arithmetic quotient q_{g,6}(D) is 0.
- Genus 3 is F.3.29.
- For g ≥ 4, a symplectic invariant projector reduces the claim to a twelve-dimensional space. There, seven necessary
  scalar rows M₇(s) and the five detector contractions K(s) satisfy the polynomial identity N₀M₇ = d₀LK (UC.5), where
  s = g − 1 and d₀ = 9(2s+3)(4s²+6s−1) > 0.
- So ker M₇ ⊂ ker LK in every genus.

**Arithmetic consequence (part 5, through the witness map F.3.31).** Take X₀ = E₀ ∖ {O} with E₀: y² = x³ − x, the
harmonic CM curve, j = 1728. Every nontrivial closed procyclic subgroup of the geometric profinite π₁ whose arithmetic
normalizer has open image in G_{Q(i)} lies in a conjugate of cusp inertia.
- Cusp inertia meets R = ⋂_ℓ ker(π₁ → π₁^{(ℓ)}) trivially.
- So no such subgroup lies in R.

## What I checked, and at what level

1. **The certificate, rerun.** I ran the run's code from my own folder with `python -I -B`.
   - It is byte-identical to the run's record (SHA-256 7d11658b…f653).
   - It imports only numpy, sympy and the standard library, and does no file or network access.
   - It computes the twelve inputs, K and M₇ from the diagram calculus, and checks N₀M₇ − d₀LK = 0 exactly in Q[s]
     (exit 0, 7.4 s).
   - This reruns their code. It is not an independent derivation of M₇ and K.
2. **By hand.**
   - LJ = 0, with rank J = 2 and rank L = 3, so ker L = im J.
   - d₀(3+t) = 9(9+2t)(53+30t+4t²) > 0.
   - The deduction ker M₇ ⊂ ker LK.
   - I ∩ R = 1: [x,y] ↦ 1+E₁₃ in UT₃(Z/ℓⁿ) has exact order ℓⁿ.
   - The conclusion is exactly A.22's open assertion. A.22 (final return of 14 Nov, PDF p. 16) asks for the existence or
     exclusion of a nontrivial closed procyclic C ⊂ R whose normalizer in the arithmetic full profinite group has open
     image in G_{Q(i)}.
3. **Not checked by me.**
   - The arithmetic reduction: F.3.31's proof and the inputs from F.3.24-F.3.30 and F.3.34.
   - Nakamura 1996 (Math. Ann. 304, 99-119), pp. 115-117. `find_paper.py` returned no hit during the check. I used the
     run's own readings: the degree-six arithmetic quotient has rank 1 with character χ³; Lemma 4.5 gives the fibre
     surjection; finite base change leaves it invariant.
   - This is the step that makes R visible to a pro-ℓ argument:
     - a finite cover detects the element in homology (Nakamura 1994, Lemma 2.1.4);
     - the open normalizer then forces the χ³ class (weight 6) to appear;
     - (UC.1) kills that class.
   - It answers the stopping point that A.22 itself recorded: "its line can have weight one".

## What F.3.32 settles

- **The algebraic gate (UC.1)** is settled for every genus ≥ 4 at the level of a rerun exact certificate, given the
  run's definitions and inputs.
- **The CM common-kernel assertion of LM6 A.22** (for E₀ ∖ {O} and its finite base changes) is **proved in the run**:
  - its algebraic gate is rerun and confirmed here;
  - its arithmetic reduction (F.3.31, F.3.24) and its Nakamura 1996 input have no check outside the run.
- **A.22's second half** (a general affine hyperbolic curve) is F.3.33's claim, not checked here.

## The F.3 chain behind F.3.32 (added after the main session's second message, 22 Nov)

**Rows checked before, by agent a922466087ec53798** (targeted proof check, in part): F.3.11, F.3.13, F.3.14, F.3.16,
F.3.20 and F.3.23. Its F.3.20 row confirms Nakamura 1996, pp. 115-117, against the GDZ scan: Cor. 4.2; table (4.3),
with r_{0,3}(6) = 1; Lemma 4.5; Cor. 4.6; (4.7.1)-(4.7.2).

**Checked here:**

| Row | Check | Result |
|---|---|---|
| F.3.31 (the witness map) | targeted proof check, read in full | confirmed as a derivation; depends on F.3.29, F.3.30, F.3.24 and Nakamura 1994 Lemma 2.1.4 |
| F.3.32 | certificate rerun; I ∩ R; statement against A.22 | confirmed (above) |
| F.3.34 | certificate rerun (SHA a516e276…, PASSED in 1.9 s; 6×6 detector minor −203784; R = 0 on six brackets); logic | confirmed, given the published bound J₇[1] ≤ 6 (not opened) |
| F.3.20, the final step | against Nakamura 1995, (4.3)-(4.4), p. 214 | confirmed: by uniqueness of the lift, an element of G_K(6) has its lift in Γ̃_{1,1}(6), so the leading derivation is special of degree 6 |
| Nakamura 1995 | read in the source (open-access PDF, J. Math. Sci. Univ. Tokyo 2 (1995) 197-231) | (4.3)-(4.4), p. 214, and Lemma (4.10), p. 217, are as F.3.15 and F.3.20 cite them |
| Hain 1997 | read in the arXiv source, alg-geom/9512001 | Theorem 3.4, Lemma 4.5 and Corollary 4.8 are as F.3.24 cites them; the numbering agrees |

**The F.3.31 argument as I read it:**
1. Nakamura 1994's full-class detector finds a prime ℓ and an open H in which the ℓ-part u of z has a nonzero class in
   T_ℓ J(C_H).
2. A normal core inside H and the Fermat-quartic cover keeps [u^{ℓ^r}] nonzero, by transfer. It also gives genus ≥ 3 and
   a rational cusp (F.3.16, F.3.23).
3. Filling the cusp and passing to the pro-ℓ quotient give a nonzero Z_ℓ-line, normalized with open arithmetic image.
4. Nakamura 1996 supplies σ ∈ G_L(6) with a nonzero degree-six quotient.
   - σ acts on the line with exponent one.
   - Comparing the two lifts degree by degree gives D_σ(a) = [Z₆, a] (FC.5b). This uses that the centralizer of a in
     the free Lie algebra is Q_ℓ a.
5. So the class lands in U_{g,6} ∩ P_a with nonzero quotient. That contradicts F.3.29 (g = 3) or (UC.1) (g ≥ 4).

**Not checked here (the remaining gate):**
- The proofs of F.3.24 (the strict geometric image and [U_{g,6}, J₁] ⊂ J₇), F.3.29 (genus 3) and F.3.30 (the invariant
  projector and the five-detector inclusion (LI.6)).
- Nakamura 1994, Lemma 2.1.4, in the source.
- The F.3.32 rerun recomputes F.3.30's twelve inputs, which checks that construction computationally, not its proof.

**At the level of the statement only:** F.3.10, F.3.12, F.3.15, F.3.17, F.3.18, F.3.19, F.3.21, F.3.22, F.3.25, F.3.26,
F.3.27, F.3.28 and F.3.33. All but F.3.33 are earlier restricted cases. The run says their normalizer obligations are
discharged by F.3.29-F.3.34, and none of them is on F.3.32's path except through F.3.24-F.3.30.

**What the chain settles for LM6 A.22.** A.22's CM common-kernel assertion is proved in RESEARCH_SA07 by
F.3.31 + F.3.32.
- These are checked here except for three inputs: F.3.24, F.3.29 and F.3.30. Those three, and Nakamura 1994 Lemma 2.1.4,
  are the gate before A.22 can be called settled outside the run.
- The sources the chain cites (Nakamura 1995, Nakamura 1996, Hain 1997) say what the run says.

## Consequences for our records

- **LM6 A.22:** change "Open" to "proved in RESEARCH_SA07 F.3.32 (checkpoint 12)". Record the check level: certificate
  rerun by Claude Opus 5.5 at effort max on 22 Nov; arithmetic reduction F.3.24-F.3.31 not checked outside the run. Its
  register edges are internal to LM6 (A.36, A.52, A.53; A.52 uses A.22), so A.52 inherits the same status.
- **EXIT_TOWER and GT_TOWER_CHECK:** no change. No row of theirs uses LM6 A.22 (`EDGES.tsv`, `CROSS_RUN_EDGES.tsv`).
- **Hexagon, H17 (Δ vanishes on GT̂):** no change. F.3.32 is a Galois-side statement about E₀, the curve at the
  harmonic point. It says nothing about GT̂ or Δ.
- **Hexagon, H16 (cote 149, tangential sections; K17):** no change. K17's checkpoint 08 does not cite LM6 A.22; its
  "common kernel" is an unrelated five-lemma step.
- **A possible new Hexagon entry:** F.3.32 with F.3.33, a full-profinite cuspidality theorem for affine hyperbolic curves
  over number fields. It is of high interest if it holds. Gates left before it is a candidate:
  - an independent check of F.3.24-F.3.31;
  - Nakamura 1996 read in the source;
  - a literature check of whether the statement is already known. The group-theoretic characterizations of cusp inertia
    by Nakamura, Tamagawa and Mochizuki come first.

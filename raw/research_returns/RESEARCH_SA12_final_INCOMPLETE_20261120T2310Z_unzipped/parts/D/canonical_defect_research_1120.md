# Canonical defect under punctured finite covers: proof and source audit

Research record begun 20 November 2026, 11:20 UTC. This is separate from the frozen checkpoint-15 paper. Agent C owns the proposed theorem file and will request a full actual-file audit. No finite-generation conclusion is inferred here.

## Algebraic simplification

Let R be a complete excellent normal equicharacteristic local surface ring with algebraically closed residue field. Let A be the finite normalization of R in the function field of a connected finite étale cover of the puncture. Then A is a complete normal local domain and is unramified over R at every height-one point.

The trace pairing identifies Hom_R(A,R) with A, even when A is not flat over R. Indeed, the trace complementary module is

    {u in Frac(A): Tr(uA) is contained in R}.

We test this condition at every height-one prime of the normal domain R. The finite étale DVR algebras there have complementary module equal to themselves. Every height-one prime of A lies above a height-one prime of R, so intersection of these local conditions is A by normality. No surjectivity of the trace of 1 is used, and the degree may be divisible by the characteristic.

Choose a generically separable finite Noether normalization S=k[[x,y]] inside R. Since R is Cohen--Macaulay of dimension two, it is finite free over S. Normalize canonical modules using the trace complementary modules over S and write beta for the canonical base generator. If z belongs to the Noether different N(R/S), then

    z omega_R is contained in R beta.

One exact proof is Stacks Lemma 49.6.7: z=phi(tau) for an R-linear phi:omega_(R/S)->R. Since the module is torsion free of rank one and tau is a generic basis, z alpha=phi(alpha) tau. This yields the displayed containment without any Gorenstein assumption on R.

Finite duality gives omega_A=Hom_R(A,omega_R), compatibly with the generic trace identifications. Therefore

    z omega_A is contained in Hom_R(A,R) beta = A beta.

For a projective regular resolution pi:Z->Spec(A), the composition Z->Spec(S) is a local complete-intersection morphism of virtual relative dimension zero. Its fundamental class is a regular map O_Z->omega_(Z/S) which at the generic finite-étale point is the trace-normalized section 1. Consequently A beta is contained in pi_*omega_Z. This handles complete rings using relative duality, without silently identifying non-finite-type absolute differential modules with canonical modules.

Summing over finitely many Noether normalizations whose differents generate a fixed primary ideal J of R gives the stronger first-power statement

    J omega_A is contained in pi_*omega_Z

for every such cover. The source for the existence of a primary sum of Noether differents is the already audited Dao--Takahashi input used by B/C; it has not been freshly reread in this pass.

## Duality consequence

Stacks Proposition 54.7.8 applies to every normal modification of a normal Nagata two-dimensional local domain having a dualizing complex. It gives R^1 pi_*omega_Z=0 in every characteristic. Apply proper duality to the truncation triangle R -> R pi_*O_Z -> H^1(Z,O_Z)[-1], with R replaced by A. Local duality for the finite-length H^1 term yields

    0 -> pi_*omega_Z -> omega_A -> D_A H^1(Z,O_Z) -> 0.

Thus J also annihilates H^1(Z,O_Z), and its length equals the length of the canonical quotient. If Q is one fixed parameter ideal of R contained in J, the R-module omega_A is maximal Cohen--Macaulay of rank n=[Frac(A):Frac(R)]. Hence

    p_g(A) <= length_R(omega_A / Q omega_A)
           = n length_R(R/Q).

The common algebraically closed residue field makes R-length, A-length and residue-field dimension agree for these finite-length modules. The fixed-annihilator assertion is stronger than a numerical length estimate. It still does not supply a uniform object atlas, a bound on the number of covers, or finite generation.

## Fresh primary reads in this pass

- Stacks 54.7, tag 0AX7: full Lemmas 54.7.5 and 54.7.6, and the complete proof of Proposition 54.7.8; individual proposition tag 0AXD. Exact scope: normal Nagata local domain of dimension two with dualizing complex; no restriction on characteristic or finite type over a field.
- Stacks 49.6, tag 0BVK: full pairing construction 49.6.4, Lemmas 49.6.5--6 and complete Lemma 49.6.7; individual tag 0BVT. The Noether different is the image of evaluation at the trace element.
- Stacks 49.8, tag 0BW0: complete Lemmas 49.8.1--3, especially trace complementary-module identification 0BW2 and trace-normalized different characterization 0BW3.
- Stacks 48.29.2, tag 0E9Z: complete fundamental-class construction through the local Koszul determinant formula. The map is an isomorphism on the smooth locus; in virtual dimension zero its source is O_Z.
- Stacks 49.15, tag 0DWM: complete Lemmas 49.15.1--2 comparing finite duality with Hom and identifying the section tau with the trace map. Also full Remark 49.16.3 in tag 0C14, concerning canonical-module normalization.

Agent C independently accepted the first-power simplification in a message and is writing the complete theorem with all normalization details. The present record is an independent mathematical and primary-source check of the argument above, not a read of that not-yet-received final file.

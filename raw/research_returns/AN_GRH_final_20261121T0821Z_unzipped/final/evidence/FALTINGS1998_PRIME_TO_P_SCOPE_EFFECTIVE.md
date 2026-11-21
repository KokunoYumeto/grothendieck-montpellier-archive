# Faltings 1998, Theorem 3: exact prime-to-characteristic scope

Date: 2026-11-21. Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Primary: Gerd Faltings, Curves and their fundamental groups, Bourbaki exposé840 (March1998), pp131–150, https://www.numdam.org/item/SB_1997-1998__40__131_0/ .
Retained PDF: work/sources/Faltings1998_curves.pdf, SHA256 8cde8dfc592e50580745b1429665261c973444679daab3c93bf112bf70a01233.

## Exact reading

Read all of §3, Theorem3 and its complete displayed proof, printed pp134–135, including the final existence-only compactness paragraph. Both primary page images work/root/faltings_page-05.png and -06.png were individually displayed and inspected. The preceding geometric-centre/corollary context was read in extracted text. No whole-paper audit or uninspected prime-to-p theorem is claimed. No scans are copied into this report or deliverables.

## What the printed argument proves and uses

The group G is the full geometric étale fundamental group. From a section it forms pointed neighbourhoods Y(H). Theorem3 assumes each such neighbourhood has a rational point. For every positive integer n, the proof uses the intersection H_n of kernels G→Z/n. Vanishing of the induced pullback on H1(Z/n), flat duality and a Frobenius power imply divisibility of the Jacobian trace by n on rational points. Choosing n annihilating J_X(k) makes the image of rational points in X(k) a singleton. Repeating inside all neighbourhoods gives a unique compatible system. The last paragraph explicitly separates existence: nonempty finite inverse systems already supply a compatible system without uniqueness.

## Independent check of the prime-to-p restriction

The existence-only argument also works with the full arithmetic extension whose geometric group is the maximal prime-to-p quotient. If every permitted pointed neighbourhood has a rational point, a common refinement establishes the finite-intersection property for their finite point sets. Their inverse limit is nonempty. The resulting compatible sections agree with the original section modulo every finite geometric quotient, and compactness yields conjugacy. This conclusion supplies at least one point; the counting/trace argument is the additional uniqueness step. The premise that every neighbourhood is nonempty is not manufactured by this observation.

For the uniqueness step, restricting n to integers prime to p leaves the rational p-primary subgroup. If n annihilates the prime-to-p part of J_X(k), then nJ_X(k)=J_X(k)[p^infinity], so the displayed divisibility proves only that rational image differences lie in that residual subgroup. This is exactly the Kummer limitation already retained in A1/A51. If J_X(k)[p^infinity]=0, an annihilator n prime to p suffices; this is an existing special case, not a general repair.

The high Frobenius power in the printed proof cannot by itself remove rational residual p-torsion: Frobenius fixes all k-rational points. A direct norm calculation makes the obstruction precise. For any finite étale prime-to-p cover h:Y→X of degree d,

    h_* h^* = [d].

On actual rational p-primary groups, [d] is invertible. Thus h_* is split surjective there, with section d^(-1)h^*. If J_X(k)[p^infinity] is nonzero, this norm cannot vanish on the entire rational p-primary group upstairs. Composing it with any power of Frobenius has the same action on rational points. This does not prevent special point-difference classes from vanishing; it rules out replacing the printed general n-divisibility step by the same claim for every prime-to-p cover.

In the pro-prime-to-p geometric quotient, Hom(G,Z/p^a)=0. The subgroups H_n for n with p-divisibility therefore carry no new geometric p-level information. They cannot be assumed to have the full-group vanishing on characteristic-p étale cohomology used in the printed proof.

## Conclusion and limits

The inspected primary proof gives a prime-to-p existence criterion under the same all-neighbourhood nonemptiness premise and gives uniqueness in the rational-p-primary-free case. It supplies no new general characteristic-prime-free uniqueness argument eliminating the residual point-difference classes. This is a limitation of these specific inspected steps, not an assertion that no different prime-to-p proof or no stronger theorem exists. No curve computation, new witness construction or universal main-gate improvement is claimed.

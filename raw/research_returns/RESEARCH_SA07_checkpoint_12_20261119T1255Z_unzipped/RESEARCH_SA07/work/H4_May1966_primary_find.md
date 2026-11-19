# May 1966 Tate letter: exact priority evidence and comparison map

## Primary source and date

The original thirty-page typescript is at <https://csg.igrothendieck.org/wp-content/uploads/2024/10/L9u.pdf>, downloaded in full to `work/sources_audit_next/Grothendieck_Tate_May1966_original.pdf`. SHA256: `23fc31e371f2cc38edd03c74e460ed6d730427df5b03413c1ff45d289b38b97f`; 8,392,758 bytes. The first leaf visibly carries a handwritten heading identifying Thil and May 1966. The official Montpellier inventory calls cote6 “Lettre Tate (mai66) (Cristaux)”; its broader date range also covers later documents in that dossier. CSG catalogues this letter as unpublished. The first and last leaves were inspected visually, not solely by OCR.

Exact source locator: **§3.2, original numbered p.30, PDF p.30, penultimate sentence**. The sentence asks for the Tate module of the generic fibre from the preceding filtration-lift data. The preceding paragraph specifies a complete DVR, possibly mixed characteristic, with perfect residue field; a Dieudonné module over Witt vectors; and a lift of its special-fibre filtration. Its reduction hypothesis refers back to §3.1's extension of an ind-étale group by a toric p-divisible group. The concluding sentence separately asks how much information the analogous extension carries for more general p-divisible groups. No universal classification theorem is proved by this passage.

Visual files: `Tateletter1966_first.png`, `Tateletter1966_final.png`, in `work/sources_audit_next/`. The relevant primary-text web references are `turn947712467view1`, `turn211359856view0`, and the two screenshots `turn211359856view1/2`. The parent opened the original independently.

## Exact map into the cohomological problem

Use the mixed-characteristic field and period-ring conventions of B. Let `A/O_K` be an abelian scheme, with ordinary reduction for the letter's expressly stated starting case, and put `G=A[p^∞]`. The exact covariant map to the Galois object is

`T_pG = lim_n A[p^n](Kbar)`.

The canonical étale pairing identifies

`H^1_et(A_Kbar,Z_p) = Hom_Zp(T_pG,Z_p)`.

Hence rational cohomology `V=H^1_et(A_Kbar,Q_p)` and the covariant Tate representation satisfy `V_pG = V^vee` as continuous `G_K`-representations. This is the duality connecting the letter's Tate-module target to the cohomological target; no equality with the cohomology lattice is asserted without the dual.

In the contravariant cohomological Dieudonné convention, define

`D = H^1_cris(A_k/W(k))[1/p]`, with its sigma-semilinear Frobenius,

and put on `D_K` the filtration transported from `H^1_dR(A_K/K)` through the crystalline/de Rham comparison. The proved comparison of B gives the functorial filtered-Frobenius isomorphism

`D_cris(V) -> D`.

The quasi-inverse is the actual period-ring construction

`V_cris(D) = (D tensor_{K0} B_cris)^{phi=1} intersection Fil^0(D_K tensor_K B_dR)`.

Thus the covariant rational Tate representation is `V_cris(D)^vee`, and the integral Tate lattice requires the integral classification of B, not merely rational `D`. An ordinary abelian scheme supplies an actual common instance of §3.2 and the later smooth-proper cohomological comparison problem. Applying higher cohomology enlarges the question; that enlargement is not part of the degree-one identification just proved.

For a covariant Dieudonné convention, Cartier duality gives a second completely specified dictionary. Set `D_cov(G)=D_contra(G^vee)`. The perfect pairing of Cartier dual groups, with target `Q_p(1)`, induces

`D_cov(G) = D_contra(G)^vee(-1)` and `D_cris(V_pG)=D_cov(G)(1)`.

Here `K0(-1)` has Frobenius `p sigma`. On the underlying dual module the covariant operators are explicitly

`F_cov(f)=sigma composed with f composed with V_contra`,

`V_cov(f)=sigma^{-1} composed with f composed with F_contra`.

They satisfy `F_cov V_cov = V_cov F_cov = p`. Rationally `F_cov=p phi_dual`, so twisting by `(1)` recovers precisely the Frobenius on `D_cris(V_pG)`. On the two-step filtration, `Fil^1 D_cov,K` is the annihilator of `Fil^1 D_contra,K`; the general formula is `Fil^r D_cov,K = ann(Fil^{2-r} D_contra,K)`. This records the variance and Tate factor instead of assigning an unstated Frobenius convention to the letter's symbol M.

## What this decides, and what remains documentary

There is now a dated written formulation in May1966 of the ordinary-type p-divisible-group reconstruction question, with an additional inquiry concerning more general p-divisible groups. The unpublished letter does not supply a printed occurrence before1966. Nice1970/1971 remains the independently inspected printed formulation in the manuscript's history discussion.

The exact frozen leaf18:5 is PDF5/archive-number4 of the original cote18 scan. It was inspected at180dpi. No date or dated reused typescript is visible on this question leaf. PDF4 is a tan title cover; PDF6 is a smaller handwritten two-splitting sheet, and PDF7 is a reused SGA6 typescript. Their sequence alone does not establish that the reused text is the verso of the question leaf. Consequently the official dossier range1969–72 cannot yet be used as a proved individual terminus post quem. The absolute ordering of the undated leaf against the May1966 letter remains a separate dating obligation.

No assertion that the letter is the earliest formulation anywhere is made. The new source substantially limits any claim of novelty for18:5 and must appear in H4's chronology, while the exact manuscript-date comparison remains explicit.

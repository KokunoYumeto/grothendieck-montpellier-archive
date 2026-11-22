# Supported K1 families and the attempted two-parameter specialization

Status: complete auxiliary proof under independent review; no numbered main result, no main-gate movement and no ordinary K0 vanishing claim. Credit: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, /root/cycles_continuation; effort not separately exposed. No priority claim.

The proof is SNC_supported_K1_family_RESEARCH.tex, HK.1–HK.3. Its exact assertion is that any component degree-zero zero-cycle tuple, multiplied by one constant unit, is the component endpoint tuple of an actual K1 family on a fixed smooth proper product E×P. All characteristic-positive projective SNC surfaces are allowed; negative ampleness is unnecessary for this auxiliary construction.

The key simplification is to apply the already proved marked family lemma VE to a transverse curve A_i inside each smooth component, and then push it to that smooth component. Every A_i/double-curve intersection is marked. Supported base change makes its edge restriction zero in the supported K1 group, and the union of the A_i avoids all triple points. Actual supported closed-union descent is therefore a two-column fibre, so the component tuple lifts. No unsupported singular pushforward from A_i directly into E is used; no K1 weight decomposition is assumed.

## Primary sources actually read in this block

Thomason, R. W., & Trobaugh, T. (1990). Higher algebraic K-theory of schemes and of derived categories. In *The Grothendieck Festschrift, Volume III* (pp.247–435). Birkhäuser. Primary https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf . Freshly read the complete Sections3.14–3.16, printed pp.317–320; Proposition3.17 and its full proof, pp.320–321; Proposition3.18 and its complete proof, pp.321–322. The proof explicitly concludes that the supported analogue also holds. Also freshly read Theorem7.4 and its complete localization proof, pp.365–366; Theorem8.1 and its complete proof, p.367; Corollary8.1.4 and its complete support-union proof, p.368. Retrieval references: turn336360707view0–view2 and turn978586003view0–view2. Prior definitions and the prior theorems cited inside these proofs are not claimed newly fully read.

The positive-characteristic rational closed-union descent, curve moving/Bertini construction and VE marked lemma are the exact previously fully audited bq/br/bt dependencies. Their statement and proof files were read in full in this continuation. No fresh full Geisser–Hesselholt or Quillen source reopening is claimed in this auxiliary block.

## Proper two-parameter route and remaining gap

Suppose the desired component tuple is defined over an algebraically closed field k0 and adjoin a transcendental u. The HK construction over an algebraic closure of k0(u) descends, with all classes and endpoints, to some finite extension of k0(u) by finite presentation. A regular semistable proper model of its parameter would allow a support-localization boundary. At smooth special parameter components this is an actual K0 family only when the global support boundary decomposes through those components.

Support Mayer–Vietoris places the obstruction in node coefficients from K_{-1}(E). Each component's sum of point pushforwards vanishes. For a tree dual graph, successive leaf removal would force the node coefficients to vanish, because pushing further to E sends every point pushforward to the identity. A general semistable dual graph has cycles. In that case pushforward-zero gives only a relation in K_{-1}(E×P_j), not the zero abstract tensor Ω in PL.5. This distinction remains after C.3bt.

The Frobenius reviewer has supplied the elementary elliptic warning: a nontorsion L yields nonzero abstract tensor L⊗L over Q, while c1(L) exterior-product c1(L) vanishes rationally on the square of an elliptic curve, by pulling back L along addition and squaring. Thus point-pushforward vanishing cannot be upgraded to tensor injectivity by declaration.

For the explicit norm-one VE parameter, writing the interpolating h as a coefficient with a pole in u typically degenerates the cover into two copies of its base joined above the zeros of the leading h coefficient. The forced divisor supports can create multiple connections and therefore cycles. No compact-type reduction is proved. Merely taking a finite cover does not remove the PL tensor, by norm pull-push. These are limitations of the present route, not evidence that UK.7 survives.

## Other exact source check in this block

Iwasa, R., & Kai, W. (2021). Isomorphisms up to bounded torsion between relative K0-groups and Chow groups with modulus. *Journal of the Institute of Mathematics of Jussieu,20*(6),1947–1968. https://doi.org/10.1017/S1474748020000055 . Author manuscript dated9January2020: https://ryomei.com/papers/K0CHmodulus.pdf . Opened the full17-page primary and read Introduction/Theorem0.1, pp.1–2, Theorem2.2 statement and Lemma2.3 statement, p.5, and Example4.8 in full, p.14. The main comparison requires D to admit an affine open neighbourhood in X. This fails for a positive-dimensional projective boundary curve. Example4.8 distinguishes CH1(P1×P1|diagonal)=0 from Pic(P1×P1,diagonal)=Z. The main proof was not fully read and no theorem from this paper is used in HK. It is retained only as an exact scope exclusion for the proposed modulus shortcut.

Searches also returned Friedlander–Walker’s affine-curve algebraic equivalence, Binda–Krishna’s singular/modulus comparisons, and the already known Kohrita parameter-class distinction. No theorem was imported from those snippets, and no absence or novelty claim is made.

Written: 2026-11-19T19:10:46.678645+00:00


## Final standalone typography and first independent receipt

2026-11-19T19:14:54.986805+00:00: Frobenius completed a full independent HK.1–3 proof/source PASS in ../frobenius/SNC_supported_K1_family_independent_REVIEW.md. The subsequent source change only shortened the heading and moved z_i to a display. Final SHA256 `7b9b1db9ccae381156ea243ef524912f388ad4d455e1582a2127d4be9a99de0c`. Four-stage LuaLaTeX/BibTeX run completed 2026-11-19T19:14:14.129483+00:00 in 2.7345728680011234 seconds, all commands zero, no overflow or undefined diagnostics. The 116228-byte PDF has two pages. Both final rendered pages were actually viewed in the contact sheet; no clipping or display collision. The lemma remains an unregistered auxiliary, with no ordinary K0 or main-gate movement claim.

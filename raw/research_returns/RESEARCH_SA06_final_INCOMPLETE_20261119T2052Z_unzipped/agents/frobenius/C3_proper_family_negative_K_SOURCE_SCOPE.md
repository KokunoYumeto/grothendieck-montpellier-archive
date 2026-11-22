# Exact source scopes for the fixed proper-family obstruction

Research note, 19 November 2026. These readings were completed during the checkpoint18 write freeze and recorded after the 16:20:24 UTC thaw. No new numbered statement, ordinary Chow conclusion, or main-gate movement is claimed.

## Kelly–Saito: formal pro-cdh continuity is not actual family algebraization

Kelly, S., & Saito, S. (2026). A pro-cdh topology on formal schemes. *Advances in Mathematics, 497*, 110998. https://doi.org/10.1016/j.aim.2026.110998

The publisher's indexed primary introduction and metadata were opened at <https://www.sciencedirect.com/science/article/pii/S0001870826002203>; a direct follow-up opening was disabled. We therefore distinguish the published metadata from the full author version actually read: <https://www.lcv.ne.jp/~smaki/articles/proCdh-fSch-arxiv-v3.pdf>, 47 pages, with the internal date 20 September 2024. The filename's `v3` is not used as evidence that this equals the final published version. The arXiv canonical PDF separately returned an older version. Exact full-author retrieval: `turn160250527view0`.

We read the relevant definitions and complete statements around equations (22)–(23), author pp.20–21, equation (44), author p.38, Theorem 5.1, pp.38–39, and Lemma 5.3, p.39. Equation (23) compares pro-cdh sheaves with **continuous** formal pro-cdh sheaves. Equation (44) defines the continuous extension by the homotopy limit over nilpotent quotients. Theorem 5.1 derives a dimension-dependent connectivity bound from descent, finitarity, nilpotent relative connectivity and henselian valuation-ring inputs. Lemma 5.3 applies it to K-theory, yielding the usual vanishing below minus the dimension.

These statements do not identify actual K(R×P) with its formal completion, do not algebraize a compatible K0 class as an actual product family, and do not give K−1(R×P)=0 for the positive-dimensional parameter scheme in FF. The `(Rig)_0` axiom concerns nilpotent relative connectivity, not an unrestricted proper henselian rigidity statement. No formal-limit conclusion is imported into FF.1.

## Clausen–Mathew–Morrow: the published scope expressly excludes this shortcut

Clausen, D., Mathew, A., & Morrow, M. (2021). K-theory and topological cyclic homology of henselian pairs. *Journal of the American Mathematical Society, 34*(2), 411–473. https://doi.org/10.1090/jams/961

The complete 63-page published PDF was opened at <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/CMM21.pdf> (`turn158022600view0`). We read the introduction's exact scope, especially printed pp.411 and 414. The paper works with connective K-theory in its rigidity comparison; p.414 explicitly says that the methods do not control negative K-theory and are limited to affine schemes, leaving a general smooth proper henselian comparison outside the asserted theorem. The p-adic continuity statement likewise does not supply the rational fixed-family lifting required here. This is a positive statement about the source's exact limitations, not a criticism of its results.

## A local singularity-category statement does not globalize automatically

We also opened Burban–Kalck's full primary author version, <https://arxiv.org/pdf/1103.3936>, v3 dated 17 May 2012, 22 pages (`turn545836742view0`). The relevant Theorem 3.2, author p.9, and Lemma 3.1, p.8, concern a relative category over a **complete local** ring and idempotent completeness of its maximal Cohen–Macaulay category. No theorem about K−1 of an actual proper product R×P is asserted there. This is retained only as a source-scope exclusion; no bibliographic novelty or general impossibility claim is made.

## Exact remaining question

Drinfeld's original Theorem 3.7 and Remark (ii) settle K−1(R)=0 when R is henselian local. In the tetrahedral example, FF.4 consequently gives K0(Z)[1/p]≅K0(E)[1/p], so every individual coefficient class lifts. For a fixed proper parameter curve P and a class ξ∈K2(P), the remaining obstruction is the actual product

\[
(\partial\kappa)\boxtimes\xi\in K_{-1}(R\times P)_{\mathbf Q}.
\]

Its pointwise restrictions vanish, but none of the opened sources above proves that this global class vanishes. A generic-parameter Drinfeld lift lives over the henselization of a local ring of R⊗k k(P); descent to a varying étale neighbourhood does not itself produce a class on the fixed product. A transfer would have to control every additional branch and the ramification over omitted parameter points. No such control has yet been proved.

## Further exact scopes read after the checkpoint18 thaw

Devadas, S. *Henselian schemes*, full 57-page author version, <https://arxiv.org/pdf/2212.08644>. Remark 2.1.4, author p.9, expressly warns that the Zariski local rings obtained by henselizing along the chosen ideal need not be henselian with respect to their maximal ideals. This blocks the proposed direct use of Drinfeld at every Zariski stalk of a proper henselian scheme. Lemma 5.3.7, author pp.47–48, identifies the h-etale stalks with the corresponding strict local rings; Proposition 5.3.3 identifies the h-etale site with that of the closed fibre. Those results repair the stalk issue only after changing the topology. They do not establish the K-theory descent and actual-product comparison that would still be required. Full retrieval turn709414094view0; the exact Remark 2.1.4 page was also visually inspected (turn495236416view1).

The already opened published *GAGA for henselian schemes*, Journal of the Institute of Mathematics of Jussieu 24(4), 1547–1589, <https://doi.org/10.1017/S147474802500009X>, is equally precise: Corollary 4.3.3 proves full faithfulness for coherent sheaves, with image closed under subobjects and quotients; it is not essential surjectivity. Corollary 4.3.4 algebraizes maps between the indicated proper henselizations. Section 4.4 leaves the general positive-characteristic algebraization problem outside those assertions. No negative-K injectivity or unrestricted actual vector-bundle lifting is inferred from full faithfulness.

Wedhorn's *Extension and lifting of G-bundles for stacks*, published online 10 October 2026, was opened in full Cambridge HTML at <https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/extension-and-lifting-of-gbundles-for-stacks/F15C2DC06ACB687AD55F6F73DA6C4928>. Situation 3.10 and Theorem 3.11 concern a quotient of an affine scheme by a finite-type group of multiplicative type, with the specified henselian invariant affine pair. They do not give the desired theorem for the actual proper product Z times P. Retrievals turn160058906view0–2. This is a source-scope record, not a claim that no stronger result exists elsewhere.

## A proved affine-parameter obstruction

The following separate calculation shows why pointwise lifting and compatible virtual classes on all nilpotent thickenings cannot alone prove actual-family lifting. It is not a counterexample for a proper curve parameter.

For the tetrahedral E over an algebraically closed k containing Fpbar, choose its nonzero dual-complex class kappa in K−2(E)_Q. The exact point-parameter sequence gives a nonzero boundary delta(kappa) in K−3(R)_Q. Take the fixed affine parameter T=Gm squared and its two coordinate units t1,t2. External multiplication gives

`beta = kappa * {t1,t2} in K0(E times T)_Q`.

The same KST/GH proof as FF.1 applies to this smooth finite-type parameter; properness was not used in that K-theory argument. Its obstruction is

`delta(kappa) * {t1,t2} in K−1(R times T)_Q`.

This obstruction is nonzero. Thomason–Trobaugh, Theorem 6.6(d), printed pp.361–362, constructs the Bass boundary retraction of multiplication by a Laurent coordinate in every integer degree. Applying it twice recovers delta(kappa). No vanishing of a Nil group is needed. The full 189-page primary PDF was freshly opened at <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf>, and the complete relevant statement and proof were read (turn156277277view0; exact turn524867450view1).

Consequently beta has no actual K0 lift on Z times Gm squared. Nevertheless it has compatible rational lifts to every nilpotent exceptional thickening, by GH, and every individual k-point specialization lifts by FF.4. Thus neither of those two weaker facts supplies an actual fixed-product lift.

There is also a one-variable version when k has a non-torsion unit a. The audited TS splitting after extension of coefficients gives K−1(E)_Q containing kappa times K1(k)_Q; it is not zero over such k. The point boundary maps kappa times a nontrivially to K−2(R)_Q. Its product with the Laurent coordinate t is nonzero in K−1(R times Gm)_Q by one Bass retraction. Thus kappa times {a,t} provides the analogous obstruction on Gm. Over Fpbar the rational K1 coefficient vanishes, so this one-variable construction is not asserted there.

The distinction between E over Fpbar and its extension to k is essential. The rational group K−1(E0) is zero over Fpbar; K−1(E) can contain K1(k)_Q after extension. No incorrect base-independent vanishing is used.

## Endpoint lifting under separate audit

At 16:47–16:50 a different proof was fully typed and independently checked in `../real_weil/C3_endpoint_family_lifting_draft.tex`. It represents filtration-two perfect classes modulo filtration three by lci degeneracy curves, places each on an actual regular hypersurface family, and lifts one Cartier line bundle after a finite p-power using properness, relative Serre vanishing, Grothendieck existence and a prescribed finite-jet Popescu specialization. It proves equality at two endpoints, not equality with the original exceptional class over the entire parameter. Accordingly it neither contradicts the affine obstruction above nor proves the vanishing of the fixed-product group in FF.1. The full independent audit is `C3_endpoint_family_lifting_independent_REVIEW.md`. Registration and any main-gate assessment belong to the parent after complete review.



## Dated scope update after C.3bu — 2026-11-19T19:45:30.500069+00:00

The complete whole-proper-family theorem `C3_whole_proper_top_family.tex`, WP.1–WP.8, has passed root and both peer mathematical audits. Under the **additional geometric hypotheses of C.3bn**, for exceptional dimension d≤2 and a **fixed smooth proper curve** P, it proves full rational K0 restriction surjectivity and therefore K_(-1)(Spec R×P)_Q=0 by FF.1. The previous retention of that obstruction is superseded in precisely this scope. The earlier calculations and failed coefficient-faithfulness approach remain as dated research history.

FF's general exact Z[1/p] formula is unchanged. The new conclusion is rational; it does not assert general Z[1/p] vanishing, a higher-dimensional proper-parameter result, an affine-family compactification, or locality after adjoining k(u). In particular, the retained nonzero affine two-dimensional-parameter example remains outside the theorem. The component Albanese-kernel quotient UK.7 is still the main gate, and this auxiliary strengthening is not counted as main movement.

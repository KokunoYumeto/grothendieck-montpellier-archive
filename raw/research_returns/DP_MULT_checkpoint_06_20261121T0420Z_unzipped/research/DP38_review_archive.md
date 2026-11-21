# DP38: independent whole-proof review and corrected-version closure

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**; inherited model, runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Actual review interval: **01:57:00–02:07:46 UTC**, with the final clock read after the complete corrected draft and integrated proof had both been read. Events **ABA-CE35** and **ABA-CE36** distinguish error discovery from corrected-version closure. The main paper was not edited by this reviewer.

## Outcome

**PASS for the corrected versions identified below.** I read all statements and proofs in the author's complete memo, §§1–8, and the integrated DP38 theorem, complete proof, and following generic-path paragraph. The proof establishes the actual-dual display construction, the exact primitive first coefficients, their stated gauge properties, the finite mixed-jet and last-dual-path assertions, and the stated denominator-rate conclusions. It does not identify these display coordinates with the entire DP32 logarithm, claim an optimal denominator rate, or prove failure of a prescribed harmonic theta construction.

The initially inspected version did **not** pass unchanged. This review caught an integrated assertion about Witt negation and an exact sign error caused by using the usual positive Artin–Hasse convention instead of Zink's convention. Both were corrected by the author/root, and the complete revised versions were then reread. The valuations and unit conclusions survive the sign correction, but the exact coefficient formulas genuinely changed.

In the corrected Zink convention the two coefficients and first homogeneous term are

\[
[S^pY_1]B=-\frac1p,\qquad [SY_d^p]B=\frac1p,
\qquad
(\log B)_{p+1}=B_{p+1}=\frac{-S^pY_1+SY_d^p}{p}.
\]

The mixed derivative values are consequently \(-(p-1)!\) and \((p-1)!\). The last-dual invariant logarithmic path, for \(h>2\), begins with \(+\epsilon^pt^{p+1}/p\).

## 1. Caught errors and scope refinements

### 1.1 Witt negation is not componentwise at every prime

An initially integrated sentence replaced the components of the Witt-vector negative \(-\xi\) by \(-\xi_i\). This is false in general at \(p=2\). The corrected proof defines the Witt vector \(w=-\xi\), uses the valid Teichmüller multiplication rule

\[
(w[Y])_i=w_iY^{p^i},
\]

and uses only \(w_0=-\xi_0\), which is valid at every prime. Only this zeroth component can contribute linearly in \(Y\). Thus the original erroneous componentwise assertion was unnecessary, and the corrected proof does cover \(p=2\).

The initially observed integrated whole-block hash was `8f18cfeb853e9d34fe8a2708bc54222069de5b661bd26b801e8116d2e5b97eac`. The later pre-hex-correction snapshot already incorporates this repair and the explicit invariant-splitting scope below.

### 1.2 The primary source uses negative Artin–Hasse normalization

I directly viewed the original published **Zink, printed p. 232, formula (196)** and **printed p. 236, formula (211)**, not just extracted text. On p. 232 the map into the big Witt group is \(z\mapsto1-zt\), and (196) reads the positive Witt coordinates from factors \(1-x_it^i\). The projector retains the powers \(p^r\) in the ordinary logarithm. Formula (211) embeds the resulting p-typical summand and evaluates at \(t=1\), with no further inverse. Therefore

\[
\operatorname{hex}([Z])
=\exp\!\left(-\sum_{r\ge0}\frac{Z^{p^r}}{p^r}\right)
=1-Z+O(Z^2).
\]

The original DP38 draft asserted linear coefficient \(+1\). Combined with its otherwise correct quotient/cocycle signs, that reverses both exact coefficients relative to Zink's canonical construction. The corrected draft and main paper now explicitly state the source normalization, reverse both coefficients and derivative signs, and consistently reverse the last-axis and height-two path signs. This is an exact-sign correction, not merely a presentational clarification.

Primary PDF: T. Zink, *The display of a formal p-divisible group*, Astérisque **278** (2002), [published PDF](https://www.numdam.org/article/AST_2002__278__127_0.pdf), local SHA-256 `2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69`.

The exact original pages viewed are preserved as:

| File | Original locator | SHA-256 |
|---|---|---|
| `late_proof_snapshots/zink_p232_hex_normalization.png` | PDF page 107, printed p. 232, including (196) | `10a1f644be71f6f2ffabe42601c321aee39523fb59b6e99f5578a00608661939` |
| `late_proof_snapshots/zink_p236_hex_definition.png` | PDF page 111, printed p. 236, including (210)–(211) | `1b3b529b0bcf3acf5d5d5a43f68edf104bf2a77c0374c83c0abca0a41520bec8` |

The earlier attempted image output that was truncated was not counted as a visual inspection. Both successful page displays were subsequently inspected.

### 1.3 The path statement needs its invariant representative and height restriction

The two individual mixed coefficients are unchanged by every rational bilinear gauge. The collapsed one-variable path assertion is more specific: it uses the **unique invariant splitting**. Main DP38 now says this explicitly. A rational non-invariant bilinear gauge can add lower-degree terms on the path, whose exponential powers contribute in degree \(p+1\).

For example, in the corrected sign convention take \(p=3\), \(h>2\), \(\epsilon=1\), \(U=1\), and replace the invariant logarithm by \(b_{\rm inv}+xy_d/3\). Along the last-dual path,

\[
24[t^4]\exp\!\left(\frac12(b_{\rm inv}(t)+t^2/3)\right)
=24\left(\frac16+\frac1{72}\right)=\frac{13}{3},
\]

whose valuation is \(-1\), not zero. This does not contradict the corrected theorem, which fixes the invariant splitting.

The memo also now explicitly retains \(h>2\) in both the odd-prime half-power statement and the any-prime unit-power variant. At \(h=2\), the first path coefficient is \((\epsilon^p-\epsilon)/p\), and may vanish. The main theorem already had the required height restriction; the review requested that it remain explicit in the following variants.

## 2. Display, actual-dual identification, and integral coordinates

I checked the displayed cyclic formulas against the evaluation pairing identities of **Zink, Definition 19 and (22), printed p. 143**. The formulas for the dual normal decomposition and its semilinear operators satisfy those identities, including the terms in \(IT\). The linearized normal-decomposition maps are cyclic permutation matrices. Their Frobenius cycles and their dual cycles have positive powers of \(p\), so the connectedness/nilpotence requirements hold for every \(h\ge2\).

The Teichmüller sections have the identity tangent maps into \(P/Q\) and \(P'/Q'\). Hence they are integral formal coordinate systems by the formal inverse theorem. They need not be group homomorphisms. Their formulas and the quotient construction are compatible modulo all \(p^n\), so the inverse-limit frame is not assembled from unrelated choices.

On the special fibre, the relation \(p[S]=V[S^p]\) and successive display relations carry the scalar input around exactly one cycle to \([S^q]e_0\). This gives \([p]_G(S)\equiv S^q\pmod p\), with tangent coefficient \(p\). The previously read **Hazewinkel §5, (5.1)–(5.4) and its uniqueness statement, printed p. 77**, applies to identify the line with the integral Lubin–Tate/Honda line. The second display is the actual dual of this first display. No identification of all its coordinates with DP32's separate logarithm is required or claimed.

The exact cokernel/injectivity statement used below is **Zink Theorem 81 and (145)–(146), printed p. 204**. The evaluation-pairing biextension and quotient signs use **Proposition 106, p. 226**, and **(216)–(218), pp. 238–239**. These source formulas were directly read in the preceding DP35 review and their relevant signs were checked again here; the primary `hex` normalization was separately checked as above. The proofs of the cited classical classification theorems are not being independently re-audited.

## 3. Carry calculations and quotient degree filtration

The first two ghost equations give

\[
[S]+[S']-[S+S']=V\xi,\qquad
\xi_0=-\frac{(S+S')^p-S^p-S'^p}{p}=-C_p(S,S').
\]

Weighted homogeneity of the integral Witt addition/subtraction polynomials gives ordinary degree \(p^{i+1}\) for \(\xi_i\). Thus the components of \(F^r\xi\) have ordinary degrees at least \(p^{r+1}\). The proof correctly restricts this assertion to this homogeneous carry vector; it would be false as a general claim that Frobenius raises every arbitrary coefficient-degree filtration.

I checked the entire telescoping calculation

\[
\kappa_0=-V\xi e_0-\sum_{j=1}^{d}F^{j-1}\xi e_j,
\qquad
(V^{-1}-1)\kappa_0=V\xi e_0-F^d\xi e_0.
\]

The endpoint has degree at least \(q\). Reducing the exact resolution to the nilpotent test algebra truncated in that degree proves both ordinary addition to that precision and equality of the true defect with \(\kappa_0\). This uses actual injectivity after reduction; it does not assume that an uncomputed inverse preserves a chosen filtration.

With corrected `hex`, the zeroth component of \(-\xi[Y_1]\) gives \([Y_1]\log C_G=-C_p+O(q)\). Extracting \(S^{p-1}S'\) gives \(p[S^pY_1]b=-1\). Higher powers of an axes-zero logarithm cannot change a coefficient linear in the whole dual side.

The dual telescoping calculation is also exact:

\[
\kappa'_0=-V\xi e_d^*-\xi e_0^*,\qquad
(V'^{-1}-1)\kappa'_0=V\xi e_d^*-F\xi e_1^*.
\]

Its endpoint has degree at least \(p^2\). Pairing with \([S]e_0\), and retaining the inverse in the second quotient cocycle, gives \([S]\log C_H=+C_p+O(p^2)\). Hence \(p[SY_d^p]b=1\). The opposite signs now agree with the exact source convention.

## 4. Gauge properties and the first invariant homogeneous term

The same low-degree addition identities imply \(\log_G(S)=S+O(S^q)\) and \(\log_H(Ye_d)=Ye_d+O(Y^{p^2})\), by comparing the additive logarithm identity in characteristic zero. Thus a bilinear change in logarithm coordinates contributes neither of the two specified mixed coefficients. An axes-normalized integral frame unit changes their logarithmic coefficients only by integral amounts: every higher power of its axes-zero augmentation has degree at least two on each relevant side. The same coefficients in the unit itself are side-linear and therefore have the stated invariance.

The diagonal display automorphism commutes with all operators, including coefficient Frobenius and the cyclic wrap. Its line coordinate action is exactly \(S\mapsto\zeta S\), so its inverse dual gives the stated characters \(\zeta^{-p^j}\). The evaluation pairing, chosen lifts, defects and scalar-one quotient frame are invariant. Averaging is valid, and the absence of invariant bilinear characters makes the invariant rational logarithmic splitting unique.

I checked the complete small-degree monomial classification, including \(p=2,h=2\). For total degree at most \(p+1\), write \(W=\sum p^jb_j\). Then \(pb\le W\le p^db\le q\), while \(a\le p\). Thus \(W<a\) is impossible. Equality forces \((a,b,j)=(p,1,1)\). A strictly positive divisible difference \(W-a\) is exactly \(q-1\), which forces \(a=1\), \(b=p\), all on the last dual coordinate. Hence there are exactly the two claimed degree-\(p+1\) monomials and none below them. Identity-linear substitution of inverse logarithms preserves their first homogeneous polynomial.

## 5. Integral operators, path unit, and numerical rate

The translation coefficient at source degree \(p\) is \(D_G^p/p!\) on the line and \(D_d^p/p!\) on the last dual source axis because the relevant logarithms have no nonlinear terms of degree at most \(p\). Translation is integral, so both powers take the entire integral function ring into \(p\) times that ring. Composition with the other integral invariant derivation preserves that divisibility, whereas the two primitive mixed values are units.

For the fixed invariant splitting, \(h>2\) kills the first monomial on the last-dual logarithmic path and leaves \(+\epsilon^pt^{p+1}/p\). The integral derivations commute. In \((D_G+\epsilon D_d)^p\), the pure powers and every interior binomial term are divisible by \(p\). Thus an integral \(U\) contributes a multiple of \(p\) to its next derivative. The exponential gauge has no earlier positive term, and its degree-\(p+1\) contribution is

\[
U(0)\epsilon^p\frac{(p+1)!}{2p},
\]

a unit for odd \(p\). It cannot cancel the integral-factor contribution. Replacing the half-power by a unit scalar multiple proves the stated any-prime version, with the same invariant-splitting and height restrictions.

The degree-\(p+1\), valuation-\(-1\) coefficient and DP35 give the weighted-infimum failure for every rational \(0<t<1/(p+1)\), hence the liminf rate. This is a necessary rate bound, not a claim that the optimum equals that number.

For the final generic-path paragraph, restriction to \(S,Y_1\) preserves the **first** integral coboundary, which is all DP35's rigidity argument needs. It does not require that this dual coordinate axis be a formal subgroup. A residue-transcendental unit makes each nonzero lowest-valuation homogeneous residue polynomial remain nonzero on \((t,\epsilon t)\). Thus degreewise minimum valuations, and hence the same rate, are preserved. This is a formal generic **group-coordinate** diagonal after an unramified residue extension. It is not a conclusion for a prescribed algebraic CM parameter or an arbitrary logarithmic diagonal.

## 6. Exact checked versions and review limits

| Scope | SHA-256 |
|---|---|
| Initial complete draft, as first read | `4209c45180d5d45f8a8837c30d05642b110e00a13c6c7fd5d6aff74c0123d6d3` |
| Pre-hex-correction draft, after explicit height-scope additions | `04145cafece8139f469871e0c2e14efd23968c89f474e1d3611c2848c8ad772c` |
| Pre-hex-correction integrated DP38 plus generic paragraph, after Witt/scope repairs | `35fa08ef6458ca5b97d56fd4eaca93d163fc1a2db32430d14325d766a95a9d0a` |
| Corrected complete draft | `11a64f894a19b90eaf073a7e99ee153010b696ab558996fb2c34c53d36771bdb` |
| Corrected draft statements and complete proofs, §§1–7 | `713e0ac41a2b1c3cc8f5d16d5cf8df372f0acde73370c90c61eb6c4356f3389e` |
| Corrected integrated theorem, proof, and following generic-path paragraph | `b7b985999358309fe18b1929722979e01ac65902459348bc896e959b64d2f08f` |
| Corrected complete integrated proof environment | `260b24564d5d83eea8ae45b62a725c79808803a1c30a58fdf85ad85b883524e0` |

Snapshots and machine-readable metadata are in `late_proof_snapshots/DP38_*`. The integrated block begins at `\\begin{theorem}[DP38:` and ends immediately before `\\begin{proposition}[DP39:`, preserving intervening whitespace. The proof hash includes its complete `proof` environment. The draft proof-scope hash begins at `## 1. Statement` and ends immediately before `## 8. Source locators`.

The corrected integrated text preserves all substantive content of the corrected draft. The event is a complete manual reread and proof challenge, not a machine formalization. This record does not claim a whole-proof review of the adjacent DP39 or of later edits. It also does not convert full-series nonintegrality or these particular finite unit jets into a statement about all selected harmonic operators, all theta normalizations, or global chain-length costs.

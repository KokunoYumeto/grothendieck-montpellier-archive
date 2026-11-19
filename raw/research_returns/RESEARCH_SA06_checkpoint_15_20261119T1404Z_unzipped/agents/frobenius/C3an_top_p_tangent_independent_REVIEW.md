# Independent audit of C.3an

**Verdict:** passed the complete typed proof, with primary geometry and symbol-source checks. Historical certification: **2026-11-19 09:56:09 UTC**. The Dennis–Stein sign comparison was corrected before **09:59:01 UTC**. This file is a reconstructed copy following the 10:14 UTC scratch reset; the audit was actually performed before that reset. The separately rerun certificate records its own fresh runtime.

Owner: `agents/real_weil/C3_top_p_tangent_draft.tex`.

## Exact scope

For every algebraically closed field of characteristic five, the construction gives an excellent normal strictly henselian local ring of dimension three, with regular puncture X, and an integral surjection `CH²(X)/CH²_alg(X) → (k,+)`. It is an exponent-five invariant. No rational nonvanishing, characteristic-zero result, or unrestricted higher-dimensional conclusion follows.

## Geometry checked

The plane quintic `Y⁵−YW⁴=Z⁴W` is smooth, has its unique point at infinity `(0:1:0)`, and has genus six. The affine differential dz has divisor `10∞`. With `q=Y/Z`, `h=W/Z`, the equation is `h=q⁵−qh⁴` and `z−q⁻⁵=h³/q⁴=q¹⁰c`, where `c=q(h/q⁵)³` is a uniformizer. This verifies the exact normalization rather than just its valuation.

For the extension `0→O(−2∞)→E→O→0` arising from dz, the lines convention gives a section with positive normal bundle O(2∞). The inseparable curve G has class `5S∞−10g*∞`. The double cover has inverse-root line bundle `O(−3S∞+5g*∞)` and equation `T²=s⁵−z`. The reduced section S has normal bundle O(∞), hence S²=1. For `D=S+g*∞`, the intersections are D²=3, D·S=2, and D·F=1; irreducible fibres and nonnegative intersections of distinct horizontal curves prove ampleness. The line bundle is L=5D.

At the section, `x=1/s_i`, `w=T_i/s_i³` give `w²=x−c_i x⁶` and `dT_i=−x³ dc_i/(2w)`. The vanishing order is five. The base-infinity transition `dT=q⁵dT_i` contributes the other part of 5D. The local calculation at the intersection verifies that no additional zero is hidden. Thus `η=dT` defines a nonzero section of `Ω¹_V⊗L⁻¹`.

The full section ring of L is normal and finitely generated. No degree-one generation or global generation of L is assumed. A sufficiently positive Veronese gives the standard proper contraction of Tot(L⁻ᵉ); the fibre-power map from Tot(L⁻¹) is finite. Properness over the original cone follows by the graph argument. Ratios of nonvanishing sections of consecutive sufficiently high powers give an invertible degree-one element locally away from the vertex, proving that the puncture is the Gm-bundle. The reduced exceptional fibre is V; the scheme fibre can be nonreduced. Pointed étale base change and strict henselization preserve regularity and the split first infinitesimal neighbourhood.

## Integral detector and actual curves

The typed proof separately establishes the integral map from CH² of the regular resolution to H² of relative K₂ on V₂. The relevant K₀ filtration comparison has coefficient `(2−1)!=1`; this is not a rational Chern-character shortcut. The only incoming descent differential comes from global units, which lift to actual K₁. Restriction to the surface thickening kills the third filtration step. The exceptional pushforward has K₀ representative `π*γ(1−L)`, hence pulls back from V and has zero relative class. Serre pairing with η gives the additive invariant.

The actual curve equations are `s=0,T=at,z=−a²t²,y⁵−y=a⁸t⁸`. For a≠0 the Artin–Schreier equation is irreducible: a hypothetical rational solution has no finite poles, and its pole order at infinity would make eight divisible by five. The germ at t=y=0 is smooth. Its closure and the finite normalization of its cone image allow a henselian branch factor to isolate precisely the chosen point. The proof therefore uses actual cycles on one fixed scheme, rather than a formal germ or a nonexistent simultaneous family.

The local Koszul difference maps to `ta ds/(sT)`. With the positive Steinberg normalization and the chosen wedge order, pairing with `η=t⁻¹dT` gives a. Ordinary algebraically trivial cycles form a divisible group because actual proper-curve families factor through Pic⁰ of their parameter curves. Every homomorphism from this group to the exponent-five additive target is zero. These facts yield the claimed surjection after quotienting by ordinary algebraic equivalence.

## Primary sources and sign correction

Mukai, RIMS1736 (2011), full primary PDF: <https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1736.pdf>. Read Example1.3 p3, Lemma1.4 p4, §1.3/Definition1.6/Proposition1.7 pp5–6, Lemma2.2/Proposition2.3 p8, equation(25) p13, and p14. The p5 display and p14 divisor convention conflict. The minus sign used above was independently derived from local equations and the normal bundle. This is a statement about the opened preprint, not about an unopened published version. RIMS1505 pp2–3 was also opened; its normal-bundle derivation has the required minus sign.

Weibel, Chapter III, Definition5.11 p43, Theorem5.11.1(b) p44 and Exercise5.14 pp46–47 were opened in full. His map sends `⟨m,r⟩` to `+m dr`, and with his definition `⟨r,s⟩={r,1−rs}` it sends `{1+tc,u}` to `−tc dlog u`. The map used in C.3an is explicitly the negative, so it sends `⟨m,r⟩` to `−m dr` and `{1+tc,u}` to `+tc dlog u`. This is a conventional negation, not a change of group or scope. The source comparison is explicit in the reconstructed auxiliary lemma.

Van der Kallen's 1971 original four-page scan was visually read in full. Its dual-number isomorphism assumes 1/2, and therefore applies in characteristic five without any characteristic-zero hypothesis.

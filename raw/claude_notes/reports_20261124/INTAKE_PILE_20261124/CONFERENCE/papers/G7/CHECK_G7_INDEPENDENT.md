# G7: independent check

**Who and when.** Claude Opus 5.5 at effort max (agent a65dbdc241d1a129a, the reader of SA12 in the horizontal sweeps), 25 Nov 2026, 14:36-14:55 UTC.

**Brief.** `agent_notes/a65dbdc2_G7_CHECK_BRIEF_20261125.md`, from the main session 329fb1e6 (Claude Opus 5.5 at effort max).

**What I read.**
- `src/G7_paper.tex`, every line; `PROVENANCE.md`; `CHECK_EVENTS.tsv`; `who_checked.py D:wild-genus2-single-curve`.
- The run's proof of the last sentence of Theorem A: `parts/C/D_graded_cone_tameness.tex`, lines 186-206.
- The arXiv full texts, as PDFs fetched from arxiv.org and converted to text (`pdftotext`):
  - Lorenzini-Schröer 1904.08371 (v1) and 2101.08090 (v1);
  - Ito-Schröer 1209.3605 (v2);
  - Matsumoto 1812.03466 (v5).
- **Artin 1975 was not opened.** The publisher's site (ams.org) answered HTTP 403 to automated access. **Artin 1977 has no free copy**, so it was not opened either.

**I did not edit the paper.** The repairs are at the end, R1-R10, with their exact wording.

The check types below are the seven of the rubric (memory `check-rubric.md`), named as there. The events are in `CHECK_G7_INDEPENDENT_CHECK_EVENTS.tsv`.

## Verdicts

| Statement | Verdict |
|---|---|
| Lemma 2.3 (the extension along C), in full | **Confirmed.** Every step holds. |
| The writer's non-triviality proof (x̄ is not a square in k(C)) | **Confirmed.** |
| §2.3, "the cover on the completed germ" | **Confirmed.** Add one reason (R7). |
| Corollary C (i), the formal neighbourhood is not linear | **Confirmed.** The step from a linear neighbourhood to Theorem A is the run's own last assertion, which I re-derived. |
| Corollary C (ii), S₀ has only tame covers | **Confirmed.** The identification of the radial valuation needs one more sentence (R6). |
| Corollary C (iii), the germs are not isomorphic | **Confirmed.** Add why Ŷ is minimal and a citation for the uniqueness of minimal resolutions (R7). |
| Is T regular at o′? | **No.** T is singular at o′, and moreover not a rational singularity. The note never says so; it should (R3, R8). |
| "In all of them the source of the cover is a smooth germ or a rational double point" | **True** for LS20, LS23, IS and Ma, checked in their full texts. Two corrections: IS quotients by special p-groups, not by ℤ/p; and Artin 1977 is unverified. Replace the sentence by one that is proved (R2, R3). |
| Novelty: a wild ℤ/2 cover over a single genus-two exceptional curve | **Not in LS20, LS23, IS or Ma**: none has an exceptional curve of positive genus over a wild cover, nor this equation. **It cannot be in any work whose covers have a regular or rational source, or a rational double point as base** (R3). |
| Bibliography [Ar75] | **Wrong title.** It is "Wildly ramified Z/2 actions in dimension two" (R1). |
| Hartshorne 1962 §2; Matsumura Thm. 23.7; Serre, Local Fields III §6 Cor. 2; Stichtenoth Prop. 3.7.8 | **Standard uses.** The locators agree with what I know. None was opened (no free copies). |
| Abstract and §1 against what is proved | **Two claims go a little beyond the letter of the proofs** (R4, R5). One locator should be sharpened (R9). |
| Lemmas 2.1, 2.2 and 2.5 (part of Theorem B, not asked) | **No fault.** I read them for wording and re-derived their steps in passing. |

## 1. Corollary C

### (i): the formal neighbourhood is not that of a line bundle's zero section
- The argument is by contradiction with Theorem A.
- Theorem A's last sentence passes from a linear formal neighbourhood to the graded case. It is the run's (D:graded-cone-tame), proved at `parts/C/D_graded_cone_tameness.tex`, lines 186-206. I re-derived it:
  - Let C' be a smooth proper curve and N a negative line bundle on it, and suppose Y along C is isomorphic to the completion of N along its zero section.
  - By the theorem on formal functions (f_*O_Y = O_S, since S is normal), Ô_{S,o} = lim H⁰(Y_n, O).
  - That limit is ∏_{n≥0} H⁰(C', N^{⊗−n}), the completion at R₊ of the section ring R = ⊕ H⁰(C', N^{⊗−n}). R is finitely generated, normal, of dimension two, with R₀ = k, and effectively graded, since all large degrees occur.
  - The valuation of the zero section, which is v_C, is the radial valuation.
- So Theorem A applies, and the completed cover of §2.3, which is wild at v_C, contradicts it. **Confirmed.**

### (ii): S₀
- **Lemma 2.1** (S₀ normal, singular only at o) and **Lemma 2.2** (the resolution, C₀ ≅ C, C₀² = −1) cover S₀. I re-derived their steps: the irreducibility argument, (F₀)_b = t⁵, and on the second chart G₂ = ξ²(1+ξ)+τ⁵ with ∂_ξ = ξ² a unit.
- **The hypotheses of Theorem A** hold for R = k[a,b,t]/(F₀) with weights (2,5,1): a normal domain of dimension two, R₀ = k, effective since deg t = 1. Its completion at R₊ is Ô_{S₀,o}.
- **The radial valuation equals v_{C₀}.**
  - For homogeneous f of degree e, f(t²x, t⁵y, t) = t^e f(x,y,1).
  - If f(x,y,1) vanished on C₀, then y²+y+x⁵ would divide it in k[x,y], say f(x,y,1) = (y²+y+x⁵)q. Weighted degrees, with weights 2 and 5 on x and y, add, so q has weighted degree at most e − 10. Hence t^{e−10}q(a/t², b/t⁵) is a polynomial, and F₀ divides f. That is the paper's "F₀ would divide f", which deserves its parenthesis.
  - For the completion, the tail Σ_{d≥N} f_d lies in the ideal generated by homogeneous elements of degree ≥ N, so the valuation of C₀ on Ŷ₀ is at least N there. Hence that valuation is min{d : f_d ≠ 0}.
  - The text says "Its radial valuation is v_{C₀}". The radial valuation lives on Frac(Ô_{S₀,o}), while v_{C₀} was defined on k(S₀). The statement is right once read as "the valuation of C₀ on Ŷ₀ = Y₀ ×_{S₀} Spec Ô_{S₀,o}". R6 says so.
- **Confirmed.**

### (iii): the germs are not isomorphic
- **The argument.** An isomorphism Ô_{S,o} ≅ Ô_{S₀,o} would induce an isomorphism of the minimal resolutions, carrying v_C to v_{C₀}, and so would transport the wild cover. This is correct.
- **Two points left implicit.**
  - Why Ŷ is the minimal resolution: C has genus two, so it is not a (−1)-curve, and Ŷ contains no (−1)-curve. The same holds for Ŷ₀.
  - That minimal resolutions of excellent normal surface singularities are unique up to unique isomorphism (Lipman). The text uses this without citation.
- **Confirmed**, with R7.

### §2.3, the cover on the completed germ
- T ×_S Ŝ = Spec Ô_{T,o′}, because T → S is finite with one point over o.
- The punctured spectrum is connected, by Hartshorne's depth ≥ 2 criterion. Simpler still: Ô_{T,o′} is a normal domain, since T is normal and excellent.
- Ŷ → Y is flat, and its fibre over the generic point of C is that point, since k ⊗_{O_{S,o}} Ô_{S,o} = k. So O_{Y,C} → O_{Ŷ,C} is flat and local, with maximal ideal tO_{Ŷ,C} and the same residue field k(C). Being one-dimensional, it is a DVR, without even using the regularity of Ŷ.
- Ŷ is regular by Matsumura Thm. 23.7 (ii): regular base and regular fibres. The fibres are regular because Ô_{S,o} is a regular O_{S,o}-algebra (S excellent) and regularity of a morphism survives base change locally of finite type.
- **Confirmed.** Only the minimality reason above is missing.

## 2. Lemma 2.3 in full, and the shorter non-triviality proof

Each step, checked:
1. O = O_{Y,C} is a DVR with uniformizer t. On D₊(ts), Y ∩ {t = 0} is the reduced irreducible curve y²+y+x⁵ = 0, so t vanishes to order one along C. The function x = a/t² is regular there and not identically zero on C, so it is a unit of O.
2. **x̄ is not a square in k(C).** The polynomial y²+y+x̄⁵ has y-derivative 1, so k(C)/k(x̄) is separable. Then x̄ is a separating transcendence basis, Ω_{k(C)/k} = k(C)·dx̄, and dx̄ ≠ 0. A square g² has d(g²) = 2g·dg = 0. **This is the writer's shorter proof. Confirmed.** It is correct and self-contained; the run's Čech-torsor proof is not needed.
3. O' = O[z]/(g) is free of rank two, and O'/tO' = k(C)[z]/(z² + x̄) = k(C)(√x̄) is a field, by 2.
   - Every maximal ideal of O' lies over tO, so O' is local with maximal ideal tO'.
   - t is a non-zerodivisor (O' is free over O).
   - dim O' = 1, so O' is a DVR.
4. O' is a domain, so g is irreducible over K. g'(z) = 2z + t = t ≠ 0, so L/K is separable. O' is normal and finite over O, so it is the integral closure of O in L.
5. **The different.** O' = O[z] is monogenic, so D = (g'(z)) = (t): Serre, Local Fields III §6, Cor. 2 (B = A[x] ⇒ D = f'(x)B; it needs only L/K separable). Different exponent one, ramification index one, residue degree two, inseparable.

**Lemma 2.3: confirmed in full.** SWEEP3_A (Claude Opus 5.5 at effort high) had checked only step 2.

## 3. Is T regular at the point over o? The novelty statement

### T is not regular at o′: it is a non-rational double point
- **Singular.** Every monomial of H has total degree ≥ 2: the degrees are 2, 4, 5, 6, 7, 9, 10, 11. So H ∈ m², and O_{T,o′} has embedding dimension three. The quadratic part is d², so o′ is a double point whose tangent cone is a double plane.
- **Not a rational singularity: an argument that does not use the run's resolution of T (R3).**
  1. Let Y_T be the normalization of Y in L. It is proper and birational over T, and an irreducible curve C_T ⊂ Y_T maps onto C and lies over o′.
  2. On a resolution Z → Y_T, the strict transform of C_T is an exceptional curve E_Z of the resolution Z → T.
  3. If T were a rational singularity at o′, then H¹(Z, O_Z) = 0. Moreover H¹(Z, O_Z) → H¹(E_Z, O_{E_Z}) is onto, since the fibres have dimension ≤ 1 and so H² vanishes. Hence E_Z ≅ P¹.
  4. Then C would be dominated by P¹, hence rational by Lüroth. But C has genus two.
  5. So T is neither regular nor a rational double point.
- **A consistency computation, by program** (`scratchpad/g7_check/t_point.py`, sympy over F₂). This agrees with the run's Proposition 4.61 (D:wild-genus2-source), one exceptional curve isomorphic to C, which I did not recheck.
  - With weights (1,3,1) on (c,d,t), the initial form of H is d² + t³d + tc⁵.
  - On the chart t ≠ 0, the exceptional curve is d₁² + d₁ + c₁⁵ = 0, the genus-two curve again. The strict transform is smooth along it: its d₁-derivative is 1 on t = 0.
- **This matters for the novelty claim, and the note should state it.** The cover's source is a singular, non-rational double point. By the argument above, that is forced: no cover with a regular or rational source can lie over a genus-two exceptional curve.

### The four papers on arXiv, read in full text
- **Lorenzini-Schröer, arXiv:1904.08371 (Math. Z. 2020).**
  - Moderately ramified ℤ/p-actions on k[[u₁,…,u_n]], ramified precisely at the origin. The source is regular.
  - No resolution of a quotient singularity is computed. There is no exceptional curve of positive genus and no equation of this shape.
  - The Introduction recalls Artin 1975: wild ℤ/2-actions on k[[u,v]] ramified precisely at the origin, whose invariant ring is k[[x,y,z]]/(z² − abz − ya² + xb²).
- **Lorenzini-Schröer, arXiv:2101.08090 (ANT 2023).**
  - Wild ℤ/p-actions on A = k[[u,v]], some ramified only at the origin and some in codimension one.
  - The resolutions computed are of quotient and related weighted homogeneous or Brieskorn singularities. Their exceptional curves are rational; the paper proves, for instance, that the central node is a rational curve.
  - Several of these quotients are not rational singularities: they have positive "fundamental genus" h¹(O_Z). Their exceptional curves are still rational.
  - The only exceptional curve of positive genus in the paper is the characteristic-0 example z² + x³ + y⁶ = 0, a smooth elliptic curve of self-intersection −1, quoted from Laufer. It is not a wild cover.
  - Neither genus two nor this equation occurs.
- **Ito-Schröer, arXiv:1209.3605.**
  - Quotient singularities are taken by definition inside a regular local ring. Its examples are diagonal quotients of products of Hermitian curves by special p-groups of order q³: non-abelian analogues of Heisenberg groups, **not ℤ/p**.
  - On p. 5 it states the general fact behind R3: dual graphs of quotient singularities in dimension two are trees, and all components are ≅ P¹. It cites Cutkosky-Srinivasan Thm. 1 and Lorenzini, Math. Z. 275 (2013), Thm. 2.8.
  - The genera mentioned are those of the Hermitian curves, not of exceptional curves.
- **Matsumoto, arXiv:1812.03466 (JAG 2023).**
  - §6 is "ℤ/pℤ-, μ_p-, α_p-coverings of RDPs"; §6.2 is "ℤ/pℤ- and α_p-coverings", over RDPs of types D_{4m}^r, E₈^r (p = 2), E₆^r (p = 3) and E₈^r (p = 5).
  - Lemma 6.6 (2): the covering U is regular.
  - Every singularity in the paper is an RDP. There is no exceptional curve of positive genus and no such equation. The only z² + … + y⁵ there is E₈.
  - The note's "[Ma, §6]" is the right place. §6.2 with Lemma 6.6 is sharper.
- **Artin 1975 (PAMS 52, 60-64)**, not opened: ams.org refused the automated fetch. Its content, wild ℤ/2-actions on k[[u,v]], is stated in LS20's Introduction and abstract, so its source is regular.
- **Artin 1977 (the Kodaira volume, pp. 11-22)**, not opened: no free copy is known to me. By its title its bases are rational double points.

**Verdict on the novelty claim.**
- None of the four papers read contains a wild cover over a surface singularity with a single exceptional curve of genus two, or this equation.
- Artin 1975 has a regular source and Artin 1977 has RDP bases. By R3 neither can contain such a cover, whatever its details.
- The sentence "In all of them the source of the cover is a smooth germ or a rational double point" is true of the four papers read. It is unverified for Artin 1977's sources, and it is not what the novelty needs. R2 replaces it by a statement that is proved.
- "New, to our knowledge after the search described" stands, with R2, R3 and R10.
- **Risk beyond the brief, not searched here:** papers whose covers have non-rational sources, such as elliptic or other non-rational Gorenstein double points in characteristic 2. R3 shows that only such work could contain the example.

## 4. Citations made from memory

None was opened; none has a free copy that I know of.
- **Hartshorne, Complete intersections and connectedness, Amer. J. Math. 84 (1962), §2.** It is used for: depth ≥ 2 implies a connected punctured spectrum. That is the standard statement of §2 (Prop. 2.1, as I remember it). The use is right. An alternative needing no citation: Ô_{T,o′} is a normal domain.
- **Matsumura, Commutative Ring Theory, Thm. 23.7.** Flat local A → B: (i) B regular ⇒ A regular; (ii) A and B/m_AB regular ⇒ B regular. It is used through (ii), with regular fibres from excellence. The use and the locator are right as far as I know. Writing "Thm. 23.7 (ii)" would be sharper.
- **Serre, Local Fields, III §6, Cor. 2.** B = A[x] ⇒ D_{B/A} = (f'(x)). This is the standard monogenic formula, in the section on computing the different (§6, after Euler's lemma), as far as I remember. It needs L/K separable, not the residue extension, so the inseparable residue extension here is no obstacle.
- **Stichtenoth, Algebraic Function Fields and Codes, 2nd ed., Prop. 3.7.8.** The Artin-Schreier genus formula. For y² + y = x⁵ (p = 2, m = 5 at ∞): g = (1/2)(−2 + 6) = 2. It agrees, and the note proves the genus directly anyway.
- **Cutkosky-Srinivasan, Thm. 1.** The finiteness consequence used is part (b), which holds in every characteristic. Only §3 assumes p > 3 (main session's record `GATE_CS1993_20261123.md`). Cite "Thm. 1(b)" (R9).

## 5. Wording, abstract and introduction

- **Abstract, "and only tame covers".** (ii) proves tameness at v_{C₀}. That is enough for every divisorial valuation: a cover étale off o and tame along the smooth curve C₀ is, by Abhyankar's lemma, locally Kummer along C₀, hence tame on every blow-up. But the note does not say this, so the abstract should say what (ii) says (R4).
- **§1 "Why it matters", "Where Y has isolated points one resolves them".** At a regular point of X a cover étale off the point extends, by purity, so new exceptional curves arise only over singular points of X (R5).
- **"In all of them the source …"**: see §3 (R2). The parenthetical "Ito-Schröer's wild ℤ/p-quotients" is wrong: their groups are special p-groups (R2).
- **The note never says that T is singular**, though its novelty rests on it (R3, R8).
- **Bibliography [Ar75]: the title.** It is given by the AMS record (DOI 10.1090/S0002-9939-1975-0374136-3) and by the bibliographies of LS20 (ref. 4), LS23 (ref. 2) and IS (ref. 2) (R1).
- **[Ar77].** The three papers give the editors (W. Baily, T. Shioda). Adding them is optional.
- **"Checks" and "search" in §3** should mention this check (R10).
- **Everything else** was read for wording and needs no change. That includes the proof overview, Lemmas 2.1, 2.2, 2.4, 2.5 and the proof of Theorem B. The steps of Lemmas 2.1, 2.2 and 2.5 I re-derived in passing:
  - irreducibility by the odd value −1 or −5;
  - the singular locus;
  - the Rees generators and D₊ inclusions;
  - both charts and their derivatives;
  - the exceptional fibre;
  - π_*O_C ≅ O ⊕ O(−3);
  - C·div(t) = C² + 1 = 0;
  - the discrepancy;
  - the Jacobian db∧dt = c⁴dc∧dt at t = 0.

## Repairs, with exact wording (LaTeX of `src/G7_paper.tex`)

**R1 (bibliography).** Replace
`\bibitem[Ar75]{Ar75} M. Artin, \emph{Wild $\mathbb Z/2$ actions in dimension two}, Proc. Amer. Math. Soc. 52 (1975), 60--64.`
by
`\bibitem[Ar75]{Ar75} M. Artin, \emph{Wildly ramified $\mathbb Z/2$ actions in dimension two}, Proc. Amer. Math. Soc. 52 (1975), 60--64.`

**R2 (§1, "Context").** Replace
`the wild $\Z/p$-quotients of Lorenzini--Schr\"oer \cite{LS20,LS23} and Ito--Schr\"oer \cite{IS}, and Matsumoto's $\Z/p$-coverings of rational double points \cite[\S6]{Ma}. In all of them the source of the cover is a smooth germ or a rational double point.`
by
`the wild $\Z/p$-quotients of $k[[u,v]]$ of Lorenzini--Schr\"oer \cite{LS20,LS23}, the wild quotients of Ito--Schr\"oer \cite{IS} by special $p$-groups acting diagonally on products of Hermitian curves, and Matsumoto's $\Z/p$-coverings of rational double points by regular germs \cite[\S6.2 and Lemma~6.6]{Ma}. In all of them the source of the cover is regular or its base is a rational double point, and then every exceptional curve over the base is rational (Remark~\ref{rem:rational}; for quotients of regular germs see also \cite[p.~5]{IS}). Here $C$ has genus two, and $T$ is not a rational singularity.`

**R3 (new remark, at the end of §2.2, after Lemma `lem:etale`).** Insert
```latex
\begin{remark}\label{rem:rational}
Let $T'\to S'$ be a finite surjective morphism of normal two-dimensional
excellent local schemes with algebraically closed residue field, and let $E$
be an exceptional curve of a resolution $Y'\to S'$. If $T'$ is a rational
singularity, for instance regular, then $E$ is a rational curve. Indeed, the
normalization $Y'_T$ of $Y'$ in $k(T')$ is proper and birational over $T'$,
and some irreducible curve $E_T\subset Y'_T$ maps onto $E$ and lies over the
closed point of $T'$. Let $Z\to Y'_T$ be a resolution and $E_Z$ the strict
transform of $E_T$; then $Z\to T'$ is a resolution, $H^1(Z,\cO_Z)=0$, and
$H^1(Z,\cO_Z)\to H^1(E_Z,\cO_{E_Z})$ is onto because the fibres of $Z\to T'$
have dimension at most one; so $E_Z\cong\PP^1$, and $E$, being dominated by
$E_Z$, is rational by L\"uroth's theorem. Since $C$ has genus two, the point
$o'$ of $T$ is therefore not a rational singularity; in particular it is
neither regular nor a rational double point. Directly: every monomial of $H$
has degree at least two, and its quadratic part is $d^2$.
\end{remark}
```

**R4 (abstract).** Replace
`has the same exceptional curve, with the same self-intersection, and only tame covers; so the two germs are not formally isomorphic.`
by
`has the same exceptional curve, with the same self-intersection, and every connected Galois cover of it that is \'etale away from the singular point is tame along that curve; so the two germs are not formally isomorphic.`

**R5 (§1, "Why it matters").** Replace
`Where $Y$ has isolated points one resolves them, and a cover \'etale over $X\setminus Y$ may then be wildly ramified along the new exceptional curves,`
by
`Where $Y$ has isolated points at which $X$ is singular, one resolves $X$ there (at a regular point a cover \'etale off the point extends, by purity), and a cover \'etale over $X\setminus Y$ may then be wildly ramified along the new exceptional curves,`

**R6 (proof of Corollary C (ii)).** Replace
`Its radial valuation is $v_{C_0}$: a homogeneous $f\ne0$ of degree $e$ equals $t^ef(x,y,1)$ on the chart $D_+(ts)$, and $f(x,y,1)$ does not vanish on $C_0$, since otherwise $y^2+y+x^5$ would divide it and $F_0$ would divide $f$; so $v_{C_0}(f)=e$. For $f=\sum_df_d$ in the completion, the part of degree at least $N$ has value at least $N$, so $v_{C_0}(f)=\min\{d:f_d\ne0\}$.`
by
`Its radial valuation is the valuation $\hat v_{C_0}$ of $C_0$ on $\widehat Y_0=Y_0\times_{S_0}\Spec\widehat\cO_{S_0,o}$, which is regular as $\widehat Y$ is, and $\hat v_{C_0}$ restricts to $v_{C_0}$ on $k(S_0)$. Indeed, a homogeneous $f\ne0$ of degree $e$ equals $t^ef(x,y,1)$ on the chart $D_+(ts)$, and $f(x,y,1)$ does not vanish on $C_0$: otherwise $y^2+y+x^5$ would divide it, the quotient would have weighted degree at most $e-10$ for the weights $(2,5)$ on $(x,y)$, and so $F_0$ would divide $f$. So $v_{C_0}(f)=e$. For $f=\sum_df_d$ in the completion, the part of degree at least $N$ lies in the ideal generated by the homogeneous elements of degree at least $N$, so its value under $\hat v_{C_0}$ is at least $N$; hence $\hat v_{C_0}(f)=\min\{d:f_d\ne0\}$.`

**R7 (§2.3 and the proof of (iii)).**
- Replace
`proper and birational over $\widehat S$, with exceptional curve $C$ of genus two; so it is the minimal resolution of $\widehat S$.`
by
`proper and birational over $\widehat S$, with exceptional curve $C$ of genus two; as $C$ is not rational, $\widehat Y$ contains no $(-1)$-curve, so it is the minimal resolution of $\widehat S$. The same holds for $\widehat Y_0$ over $\widehat S_0$.`
- In (iii), replace
`lifts to an isomorphism of the minimal resolutions,`
by
`lifts to an isomorphism of the minimal resolutions (minimal resolutions of excellent normal surface singularities are unique up to unique isomorphism \cite{Li78}),`
- Add to the bibliography:
`\bibitem[Li78]{Li78} J. Lipman, \emph{Desingularization of two-dimensional schemes}, Ann. of Math. (2) 107 (1978), 151--207.`
- The exact locator in Lipman was not opened: add it when the paper is opened, or cite another source that has been opened.

**R8 (§1, "Scope").** Replace
`The run also resolves $T$ (one curve, the Frobenius twist of $C$, with self-intersection $-2$)`
by
`The point $o'$ of $T$ is a singular, non-rational double point (Remark~\ref{rem:rational}). The run also resolves $T$ (one curve, the Frobenius twist of $C$, with self-intersection $-2$)`

**R9 (§1, "Context").** Replace `Cutkosky and Srinivasan \cite[Thm.~1]{CS} show` by `Cutkosky and Srinivasan \cite[Thm.~1(b)]{CS} show`.

**R10 (§3).**
- In "Checks", after the sentence ending `in the folder \texttt{checks} of the paper's workbench.`, insert
`On 25 November an independent check (Claude Opus~5.5 at effort max) made a targeted check of Lemma~\ref{lem:ext} and of Corollary~\ref{cor:C}, and found that $T$ is singular at $o'$; its record is CHECK\_G7\_INDEPENDENT.md in the paper's workbench.`
- In "The search of the literature", after `None of these contains the example.`, insert
`On 25 November the same independent check read the arXiv full texts of \cite{LS20,LS23,IS,Ma}: none of them has a wild cover over, or a quotient singularity with, an exceptional curve of positive genus. \cite{Ar75} (the publisher's site refused automated access) and \cite{Ar77} (no free copy) were not opened; their sources are regular (\cite{Ar75}, as recalled in \cite[Introduction]{LS20}) or their bases are rational double points (\cite{Ar77}), so Remark~\ref{rem:rational} excludes the example from them.`
- PROVENANCE.md's paragraph "Not opened in this task" should be updated to match. That file is not mine to edit.

**Who should check R3 and R6.** They are my own wording and proofs, not checked by anyone else. A reader other than me should check them before the note is posted.

# Literature gates for D2 (finite monoids) and FREX (exactness against amenability)

Written 25 Nov 2026 by the gate agent of the main session 329fb1e6 (this agent: Claude Fable 5.2 at effort max; the
main session: Claude Opus 5.5 at effort max). Brief: `<local>/Documents\agent_notes\GATES_D2_FREX_BRIEF_20261125.md`.
Running notes: `<local>/Documents\agent_notes\GATES_D2_FREX_NOTES.md`. Downloaded sources, one folder each:
`<local>/Documents\agent_notes\GATES_D2_FREX_sources\`. Check events:
`<local>/Documents\reports_20261124\INTAKE_PILE_20261124\CONFERENCE\GATES_D2_FREX_CHECK_EVENTS.tsv`.

What "read" means below: the arXiv TeX or the PDF text was opened and the named statements were read at the named
places; "grep" means a search of the full text for the named words, with the hits read. Everything marked "my
derivation" was worked out here and has been read by nobody else.

---

## Verdicts

### Gate 1 (D2): new in its main theorems, known in part; two old sources could not be opened

- **New** (found in no source opened, in no arXiv title or abstract, on no web page found, in no Hexagon work):
  Theorem 1.1 of the paper (bounded homology of a finite monoid forces a trivial universal group; p dividing |U(M)|
  forces mod-p homology in infinitely many degrees), Theorem 1.2 (homotopy-finite, finite-dimensional and bounded
  homology coincide), Theorem 2.1 (the K-theory statement), Corollary 1.4 and the failure of Ben-Bassat's Conjecture 7.1.
- **Ben-Bassat's paper** is still at version 1 (arXiv API, 25 Nov 2026); his computation repository has no commit after
  30 Oct 2026. Nothing public settles Conjecture 7.1 except our own page of 12 Nov. By our runbook he answered the note
  of 12 Nov the same day, and the user agreed to his using it in a next arXiv version
  (`<local>/Documents\RUNBOOK_20261110.md`, l.949-959); no later exchange is recorded there.
- **Known in part**, and the paper as written cites none of it:
  1. The case of a completely simple semigroup with an identity adjoined is in Steinberg, arXiv:2405.06594, Theorem A
     and Theorem 3.1: the homology equals that of the maximal subgroup G from degree 3 on. With Swan's theorem this
     gives Theorem 1.1 there, with the stronger conclusion G = 1.
  2. Corollary 3.4 (finite cohomological dimension) follows, in a stronger form, from the restriction functor of Gray
     and Pride, arXiv:1003.3227, Lemmas 2-4 and Theorem 2: a finite monoid of finite left or right cohomological
     dimension has trivial maximal subgroups in its minimal ideal (my derivation from their lemmas, which they state
     for the property FP_n). No K-theory is needed for that corollary.
  3. Lemma 3.1 (c) (the group eMe of the minimal ideal maps onto U(M)) is Sweeney's Lemma 2.1, which he attributes to
     Larisse (1972) and to Högnäs and Mukherjea (2003); Steinberg calls it well known.
  4. Finite aperiodic regular monoids have finite projective resolutions and bounded homology (Martinian-Steinberg,
     arXiv:2511.12657, Corollary 5.15): a known class to which Theorem 1.2 applies.
- **Not opened**: McDuff 1979 and Fiedorowicz 1984 (reasons in section 1.3). The verdict "new" is therefore conditional
  on these two. The risk is small: Ben-Bassat, who cites page 323 of Fiedorowicz, conjectures the opposite of
  Theorem 1.1; Martinian and Steinberg, who quote the same passage, say only that the fundamental group is finite; and
  the statement needs Miller's theorem (1984) or Atiyah's completion theorem, since Swan's theorem does not give it
  (section 1.2, item 9).

### Gate 2 (FREX): the independence is new; three ingredients are known and must be credited

- **Question 1. No**: the signed averaging of FREX A.9-A.10 is not a measure in the sense of Harman and Snowden,
  neither for the group nor for the expanded Fraïssé class. A Harman-Snowden measure lives on finitary sets with open
  stabilizers and is multiplicative on embeddings (Definition 3.1 (e), Definition 6.2 (b)); FREX's object is an
  invariant, finitely additive function on the clopen sets of one compact space of expansions, and its weights are
  not multiplicative (a three-point example, section 2.1). **But** the integer weights of A.10 are the values of
  Harman and Snowden's Euler-characteristic measure for Aut(R, <) (their Example 3.5, Theorem 16.7, Remark 16.8) on
  the pieces of the order cone, and the restriction identity of A.10 is their push-forward formula (Proposition 4.8):
  my derivation, section 2.1. So A.10 follows from their theory and must be cited to it. Nothing else of FREX does:
  their exactness results (Theorem 13.2) concern modules over the completed group algebra, not all smooth modules
  (their Remark 10.10), and Snowden's poset paper proves that the class of posets has no regular measure
  (Proposition 8.2) and does not treat posets with an added linear order.
- **Question 2. Yes**, exactness of colimits over the Fraïssé category is a property of the topos Cont(Aut M): it says
  that the left adjoint of the constant-sheaf functor is exact on R-module objects (short proof in section 2.2).
  Caramello's paper states the equivalence of toposes (Theorem 2.9, Proposition 2.10) and nothing about module
  objects, homology, exactness, amenability or Ramsey classes.
- **Question 3.** No source states either direction of the independence. Known parts: the automorphism group of the
  generic poset with an independent linear order is not amenable (Kechris-Sokić 2012, Remark 3.2, pp. 78-79: exactly
  FREX's class); extreme amenability gives integral exactness (Evans, arXiv:2603.29606v2, Lemma 3.7 (i) and
  Theorem 1.4, in dual form). The nearest open question in print is Evans's Remarks 2.12 (does his separation property
  hold for reducts of Ramsey structures?); FREX A.9 and A.11 bear on it directly and FREX does not mention it.

---

## 1. Gate 1: classifying spaces of finite monoids

The paper read: `<local>/Documents\reports_20261124\INTAKE_PILE_20261124\CONFERENCE\papers\D2\src\D2_paper.tex`
(800 lines, read in full; written by afceadd46f7598ec4, Claude Fable 5.2 at effort max). Its numbering is used below.

### 1.1 Sources read, with what D2 must cite or change

| Source (copy read) | What it states, where | Relation to D2 | D2 must |
|---|---|---|---|
| **Ben-Bassat**, [arXiv:2610.38760v1](https://arxiv.org/abs/2610.38760) (TeX, 1409 lines, read in full; sha256 102ceaa7…) | Conjecture 1.1 (attributed to Fiedorowicz 1984, p. 323). Theorems A, B, C (Introduction): cofibres of maps into BL are classifying spaces of finite monoids; every finite simply connected complex is BM with M finite aperiodic. Lemma 2.4 (retracts). Lemma 5.2 (aperiodic gives simply connected). Example 3.4: with L = C_2 a monoid of 11 elements with BM ≃ BC_2 ∨ S² and fundamental group C_2. Section 7: U(M) is finite and η is onto; Conjecture 7.1; the sentence that it would make the realizable finite types exactly those with finite fundamental group. Example 6.4 and Appendix: monoids of type CP² with 1795 and 122 elements, least order stated open. | Contains nothing of Theorems 1.1, 1.2; Conjecture 7.1 contradicts them. Example 3.4 agrees with Corollary 3.3 (unbounded homology). | Keep its citations: all locators in the paper are right (Theorem C, Conjecture 7.1 wording, Introduction for j_e, Lemma 2.4, section 7). Add Example 3.4 as the paper's own instance of a non-trivial U(M). Remark 4.1's "only version on 25 November 2026" is confirmed. |
| **Sweeney**, [arXiv:2502.05276v2](https://arxiv.org/abs/2502.05276) (PDF text; §§1, 2, 5, 6 and references read) | p. 2: Fiedorowicz's conjecture; Swan cited for groups. Table 1 (p. 3): facts about finite groups that fail for semigroups, among them "p-torsion in some H_i recurs in infinitely many degrees" (fails: Examples 5.4, 5.5, Moore spaces). Lemma 2.1: GS = G(K(S)) = H modulo the normal closure of the sandwich entries. Proposition 2.2, Corollary 2.3 (homology as Tor). Remark 2.5 (universal cover, from Fiedorowicz's Proposition 4.4). Theorem 2.7, Corollary 2.8. Example 5.2 (H_i = Z for i ≥ 2), 5.3. Example 6.1 and Theorem 1.1 (BM ≃ ΣBC_2; suspensions). Tables 4, 5 (homology of all small semigroups). | No statement that bounded homology forces GS = 1. His tables agree with Corollary 3.3: every listed class with H_1 ≠ 0 has H_3 and H_5 ≠ 0. | Cite Lemma 2.1 in Lemma 3.1 (c) for the surjection onto U(M), not only for "H is a group", and say the fact is known. After Corollary 3.3 add: torsion coming from U(M) (that is, from H_1) recurs, whereas torsion in higher degrees need not (Sweeney, Table 1 and Examples 5.4, 5.5). Proposition 5.2 (b) = his Example 5.2: right. |
| **Steinberg**, [arXiv:2405.06594v1](https://arxiv.org/abs/2405.06594) = Semigroup Forum 110 (2025), 745-761 (PDF text, pp. 1-10 read, rest grepped) | Theorem A (p. 2): for S = M(G, A, B, C) completely simple, H_n(S) = H_n(G) for n ≥ 3, H_2 = H_2(G) ⊕ ker φ, H_1 = coker φ. Theorem 3.1 (p. 6): S¹ has a classifying space equivalent to BG with a disc glued on each loop C_ba. p. 7: G(S) = G modulo the normal closure of the C_ba is "well known". p. 8: a finite rectangular band with identity gives a wedge of (|A|−1)(|B|−1) two-spheres. p. 9: algebraic proof through the bimodule Z L (projective on the left, free on the right over ZG). | Gives Theorems 1.1 and 1.2 when M is a completely simple semigroup with identity adjoined, with the stronger conclusion G = 1 (by Swan). | **Cite** (missing). State in the introduction that this case was known and that there the conclusion is stronger. |
| **Martinian-Steinberg**, [arXiv:2511.12657v1](https://arxiv.org/abs/2511.12657) = Semigroup Forum (2026), DOI 10.1007/s00233-026-10648-0 (PDF text; pp. 1-3 and 12-14 read, rest grepped) | p. 1: the fundamental group of BM is finite for finite M; Fiedorowicz's sentence that the conjecture "seems likely". Theorems A, B (finite wedges of simply connected Moore spaces are BM). Theorem C and Theorem 5.13 (finite regular M: KM of finite global dimension iff K is and the orders of all maximal subgroups are units). Corollary 5.15: finite aperiodic regular M has a finite resolution of Z by finitely generated projectives and H_n(M, Z) = 0 for large n. Corollary 5.16: finite regular M has H_n(M, Z) finite for large n. | Nothing on bounded homology forcing U(M) = 1. Corollary 5.15 supplies a class for Theorem 1.2 and Corollary 3.4. | **Cite** (missing; Ben-Bassat's own bibliography has it). Add: by Corollary 5.15 and Theorem 1.2 the classifying space of every finite aperiodic regular monoid (every finite band) is a finite simply connected complex. |
| **Gray-Pride**, [arXiv:1003.3227v1](https://arxiv.org/abs/1003.3227) = J. Pure Appl. Algebra 215 (2011) (PDF text; pp. 4-6 and §8 read) | Theorem 1, Lemmas 2-4, Theorem 2 (pp. 5-6): for an idempotent e of a completely simple minimal ideal with finitely many left ideals, A ↦ eA is exact and takes free ZS-modules to free ZH-modules, H the maximal subgroup; so left-FP_n passes from S to H. §8 has an example on cohomological dimension (a group of infinite cohomological dimension with a zero adjoined: finite cohomological dimension, a maximal subgroup outside the minimal ideal of infinite one); the inequality for the minimal ideal is not stated. | The same functor carries a projective resolution of Z over ZM to one over ZH, so cd H ≤ cd M (my derivation). For finite M of finite left or right cohomological dimension this gives H = eMe = 1, stronger than Corollary 3.4's "U(M) = 1", without Theorem 2.1. | **Change Corollary 3.4**: state the stronger conclusion, prove it by this functor (four lines, section 1.2 item 5) and cite Gray-Pride; keep the present proof as a remark. Change the sentence of the introduction that presents Corollary 3.4 as an application of Theorem 1.1. |
| **Gray-Steinberg**, [arXiv:1706.04387v1](https://arxiv.org/abs/1706.04387) = Algebr. Geom. Topol. 22 (2022) (TeX and PDF text; §6.3-6.4 read, rest grepped; arXiv numbering) | Corollary 6.7 (classifying spaces of M are homotopy equivalent). Theorem 6.27: M has an equivariant classifying space of dimension max{cd M, 3}. Proposition 6.28: right zero ⟺ left cohomological dimension 0. Introduction: |BM| alone does not control the one-sided finiteness properties. | No statement on the universal group of a finite monoid of finite cohomological dimension. Theorem 6.27 with Corollary 6.7 gives "finite cd ⟹ BM homotopy finite-dimensional". | Cite at Corollary 3.4 (optional but expected by readers from semigroup theory). |
| **Fiedorowicz 2002**, [arXiv:math/0202260](https://arxiv.org/abs/math/0202260) = Algebr. Geom. Topol. 2, 33-35 (read in full) | Lemma (pp. 33-34): the five-element monoid P with BP ≃ S², by an explicit resolution; says McDuff's theorem is also proved in his 1984 paper. | Nothing on finite monoids beyond the example. | Optional citation for the five-element monoid (free copy of the fact that D2 attributes to the 1984 paper only through others). |
| **Swan 1960**, Proc. Amer. Math. Soc. 11, 885-887 ([free at ams.org](https://www.ams.org/journals/proc/1960-011-06/S0002-9939-1960-0124050-2/), DOI 10.1090/S0002-9939-1960-0124050-2; read in full) | Theorem 1 (restriction to a non-trivial subgroup is non-zero in infinitely many degrees), Corollary 1 (p. 885: p-torsion in H^i(π, Z) for infinitely many i when p divides |π|), Theorem 2 (compact Lie groups), Corollary 2 (p. 887: the homology version). | Is what D2 calls "the classical fact". Concerns inclusions of subgroups only. | Give the locators "Corollaries 1 and 2" and move Swan from "from memory" to "opened" in §6 and in PROVENANCE.md. |
| **Nico 1972**, Proc. Amer. Math. Soc. 35, 34-36 (free at ams.org; read in full) | Theorem (p. 35): finite regular monoid, combinatorial or with kG semisimple for all subgroups: finite left global dimension of kS, with a bound. | Background for Corollary 3.4; superseded by Martinian-Steinberg Theorem 5.13. | Nothing. |
| **Carcacía-Campos**, [arXiv:2611.09718v1](https://arxiv.org/abs/2611.09718) (PDF text; grep "monoid" and the hits read) | Theorem 6.2 (BC_{Z/2,n} homeomorphic to RPⁿ). Remark 3.5, Theorem 7.4 (spreading a finite monoid over n+1 objects), Corollaries 7.9, 7.12 (use Ben-Bassat's Theorem C). | Nothing on Conjecture 7.1 or on D2's statements. | Nothing; the locator in Remark 4.1 is right. |
| **Palmer-Wu**, [arXiv:2510.16879v1](https://arxiv.org/abs/2510.16879) (Introduction) | Theorem A (V(G) is acyclic); properties (1) G embeds, (4) type F_n iff G is, (5) no proper subgroups of finite index. | Supports Remark 2.3 (b). | Nothing; locator right. |
| **Hurwitz 1989**, J. Austral. Math. Soc. A 47, 171-185 (free at Cambridge; abstract and statements) | Every connected small category embeds in a "semi-groupoid" with the same classifying space; generalizes McDuff; finitely presented monoids. | Nothing on finite monoids. | Nothing. |

### 1.2 What D2 must change, in the order of the paper

1. **Introduction, a paragraph "what was known"** (new): Steinberg's Theorem A (completely simple case, conclusion
   G = 1); Martinian-Steinberg Corollaries 5.15, 5.16 and Theorem C; Gray-Pride's restriction functor; Sweeney's
   Table 1. At present the paper cites Sweeney, Ben-Bassat and Carcacía-Campos only.
2. **"conjectured by Fiedorowicz [p. 323]"**: nobody on our side has opened the 1984 paper. The wording quoted by
   Martinian and Steinberg (p. 1) is a remark that the statement "seems likely"; Ben-Bassat and Sweeney call it a
   conjecture. Write "suggested by Fiedorowicz (p. 323, as quoted in Martinian-Steinberg, p. 1) and stated as a
   conjecture by Ben-Bassat", and keep the note that the page was not opened.
3. **Swan**: locators as in the table; now opened.
4. **Lemma 3.1 (a)**: McDuff's Lemma 1 was not opened here either. Either keep the flag, or add the one-sentence proof
   already in `G6_VERDICT.md` (the nerve is a reduced simplicial set, so the fundamental group has the 1-simplices as
   generators and one relation for each 2-simplex) and cite McDuff as the original only.
5. **Lemma 3.1 (c)**: known; cite Sweeney, Lemma 2.1 (with his attributions) and Steinberg, p. 7.
6. **Corollary 3.4**: replace by the stronger statement, with this proof (my derivation from Gray-Pride, Lemmas 2-4;
   to be checked by the writer). Let e be an idempotent of the minimal ideal K and H = eMe. The right ideal eM = eK
   is one R-class of the completely simple semigroup K, so eM ≅ H × F with F the right zero semigroup of the
   idempotents of eM, and Z[eM] is a free left ZH-module on F. The functor A ↦ eA from left ZM-modules to left
   ZH-modules is exact, takes ZM to Z[eM], hence free modules to free modules and projectives to projectives, and
   takes the trivial module to the trivial module. So a projective resolution of Z of length n over ZM gives one over
   ZH; a non-trivial finite group has none (Swan, Corollary 1). Hence H = 1, the minimal ideal is a rectangular band,
   and U(M) = η(H) = 1. For right modules use Me. Then Theorem 1.2 (iii) ⟹ (i) needs only Hatcher 4C.1.
   A second route to the old statement: Gray-Steinberg, Theorem 6.27 and Corollary 6.7, give "finite cohomological
   dimension ⟹ BM homotopy finite-dimensional", and Remark 2.3 (a) (Miller) applies.
7. **After Corollary 3.3**: the comparison with Sweeney's Table 1 (item in the table above).
8. **A question worth stating** (mine; not settled here): if a finite monoid has bounded homology, are the maximal
   subgroups of its minimal ideal trivial? Yes for a completely simple semigroup with identity (Steinberg) and under
   finite cohomological dimension (item 6); Theorem 1.1 gives only that they die in U(M); all of Ben-Bassat's
   realizations are aperiodic.
9. **Remark 2.3 (a), one sentence more** (mine): Swan's theorem cannot replace the K-theory. For the surjection
   C_{p²} → C_p the generator y of H²(BC_p; Z) goes to p·x and y² goes to p²x² = 0, so the map on integral cohomology
   vanishes above degree 2; only K-theory sees that the map is non-trivial. This is why the statement is not in the
   semigroup literature, whose tools are resolutions and Swan-type arguments.
10. **Bibliography**: add Steinberg 2025, Martinian-Steinberg 2026 (Semigroup Forum, DOI above), Gray-Pride 2011,
    Gray-Steinberg 2022; optional Fiedorowicz 2002.
11. **Section 6, "Citations"**: Swan opened; McDuff 1979 and Fiedorowicz 1984 not opened by the gate (section 1.3);
    "a search of the literature … is being made separately" becomes a reference to this file.

### 1.3 Not opened, and why

- **McDuff, Topology 18 (1979), 313-320.** In Elsevier's open archive (Crossref: licence for the version of record from
  18 July 2013; Unpaywall: open at the publisher). ScienceDirect answers a script with a challenge page and answered
  the app's built-in browser with a CAPTCHA, which I did not solve; Claude in Chrome was not connected. The tab I used
  is back on the page it showed before. A person can open it at
  [doi.org/10.1016/0040-9383(79)90022-3](https://doi.org/10.1016/0040-9383(79)90022-3). What open sources say it
  contains: every connected CW complex is BM for a discrete monoid (Ben-Bassat l.79; Sweeney p. 2; Fiedorowicz 2002
  p. 33); Lemma 1, the fundamental group is the universal group (Ben-Bassat l.117; Sweeney §2.3); its monoids are
  infinite (Martinian-Steinberg p. 1).
- **Fiedorowicz, Amer. J. Math. 106 (1984), 301-350.** JSTOR; Unpaywall "closed"; his university pages are gone and the
  Wayback Machine lists no copy of the paper under them. A copy sits on a University of Oslo course page (found by
  search, URL in the notes); it is neither the author's nor the publisher's, so under the brief's rule I did not open
  it. What open sources quote: the conjecture, p. 323; the five-element monoid with BM ≃ S²; Proposition 4.4
  (homology of the universal cover, Sweeney Remark 2.5); Theorem 4.1 (Fiedorowicz 2002, p. 34).
- Same wall (ScienceDirect) for Nico 1969 and 1971, Adams-Rieffel 1967 (J. Algebra) and Nunes 1995 (J. Pure Appl.
  Algebra); known here only through Sweeney, Steinberg and Gray-Steinberg. Burke's Cambridge thesis (cited by
  Ben-Bassat, Remark 1.4) was not opened.
- **To close the gate fully**: one look by a person at Fiedorowicz pp. 322-324 and at McDuff's Lemma 1 and its
  surroundings, for any sentence on the fundamental group or the dimension of BM for finite M.

### 1.4 Searches (25 Nov 2026)

arXiv API, titles and abstracts: "finite monoid" with "classifying space"; "finite monoids" with "homotopy type" or
"classifying spaces"; "finite semigroup" with "classifying space" or homology; Fiedorowicz with monoid; monoid, and
semigroup, with "classifying space" since 2020; monoid with "cohomological dimension". Hits on the subject: Sweeney,
Martinian-Steinberg, Ben-Bassat, Carcacía-Campos, Steinberg 2405.06594, Gray-Steinberg, Gray-Pride (and Zhang,
arXiv:2311.18280, an equivariant McDuff theorem). One extended web search: nothing more. Hexagon: all 1,546 works
(dump of 25 Nov in the sources folder) searched for monoid, semigroup, classifying space, Fiedorowicz, McDuff,
Sullivan conjecture, Kan-Thurston, nerve, homotopy type, finite categories, Ben-Bassat: no work on the subject.
The arXiv API does not search full texts.

---

## 2. Gate 2: exactness of colimits against amenability

The run read: `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112_work\FRAISSE_EXACT\FREX_final_20261118T1235Z_unzipped\FREX\`
(a run of GPT-6 Astra, ChatGPT Pro mode), `sections/A.tex` l.1-1310, `sections/F.tex`, `notes/F_source_audit.tex`,
`notes/F_harman_snowden_scope.tex`, `notes/ordered_vector_bridge.tex`, the bibliography. Labels: A.1 =
`A:coinvariants`, A.9 = `A:signed-averaging`, A.10 = `A:poset-weights`, A.11 = `A:ordered-posets`.

### 2.1 Question 1: Harman-Snowden measures

Sources: Harman-Snowden, [arXiv:2204.04526v2](https://arxiv.org/abs/2204.04526) (135 pp.; TeX and PDF text; published
in Invent. Math. on 29 Sep 2026, DOI 10.1007/s00222-026-01452-2, by Crossref); Snowden,
[arXiv:2609.02021v1](https://arxiv.org/abs/2609.02021) (56 pp.; TeX; Introduction, §§2, 3.4, 8, statements of §§4-9).

- **Their notion.** Definition 3.1: a measure for a pro-oligomorphic group G assigns a value to every finitary set with
  an action of an open subgroup, additively, invariantly, and multiplicatively in fibrations (axiom (e)).
  Definition 6.2 (= Snowden's Definition 2.2): on a Fraïssé class, a value for every embedding, multiplicative under
  composition, with a sum rule over amalgamations. Definition 3.24 and Proposition 3.25 (p. 28): equivalently a
  "generalized index" for pairs of open subgroups. Regular: non-zero (a unit) on all transitive sets
  (Definition 3.18).
- **FREX's notion** (A.9, A.tex l.389-408): G non-archimedean, H a closed co-precompact subgroup, X the completion of
  G/H; a G-invariant finitely additive function μ on the clopen sets of X with μ(X) = 1 and values in a ring k. In
  the language of classes: weights w_P(π) on the expansions π of each finite structure P, of sum 1, compatible with
  restriction and with isomorphisms. This is what Angel-Kechris-Lyons and Zucker call a consistent random expansion
  and Jahel-Joseph and Braunfeld-Jahel-Marimon an invariant random expansion, with positivity dropped and values in k.
- **Why it is not one of theirs.** (i) The clopen sets of X are not sets with open point stabilizers, and H is not
  open, so μ is not a value of a measure for G or a generalized index. (ii) It is not a measure for the expanded
  class either: w is not multiplicative. Take Q = {x, y} an antichain with reference order x < y; then
  w_Q(x, y) = 0 and w_Q(y, x) = 1. Add z with x ≺ z, incomparable to y, and y < z in the reference order; then
  w_P(x, y, z) = −1, w_P(x, z, y) = 1, w_P(y, x, z) = 1 (computed by hand from the formula of A.10; the restriction
  identities hold). A multiplicative rule would force every expansion over (x, y) to have weight 0. (iii) No
  rescaling by a measure of the unexpanded class helps, for the same reason.
- **What does come from their theory (my derivation).** Let μ be their measure μ_{−1,−1} for Aut(R, <), the compactly
  supported Euler characteristic (Example 3.5; Theorem 16.7 and Remark 16.8, pp. 119-120). For a finite ordered poset
  P let O(P) ⊂ R^P be the strictly monotone maps (P, ≺) → R and O_π(P) those that sort to π, ties broken by the
  reference order. These are finitary sets for Aut(R, <), their orbits are the cells of A.10, a cell with b distinct
  values has measure (−1)^b, and μ(O(P)) = (−1)^{|P|}. Hence

      w_P(π) = μ(O_π(P)) / μ(O(P)),

  and the restriction identity of A.10 is transitivity of push-forward (their Proposition 4.8; Fubini, Corollary 4.9)
  along O(P) → O(Q), whose fibres are open intervals of measure −1. So A.10 is an instance of integration against a
  Harman-Snowden measure of another group, and FREX's remark "the compactly supported Euler characteristic of the
  indicated cells" (A.tex l.530-531) should carry this citation. FREX's own proof of A.10 is self-contained.
- **What does not come from it.** A.9 (the transfer from H-coinvariants to G-coinvariants and its converse over
  fields) and the exactness in A.11. Their Theorem 13.2 is about the category of smooth modules over the completed
  group algebra A(G; μ), for a quasi-regular measure with property (P); Remark 10.10 (p. 79) says that a module smooth
  as a k[G]-module need not be one of those. Their averaging operators (§11.8) go between open subgroups and act on
  A-modules. The source has no occurrence of "amenab" or "coinvariant", and "Ramsey" only in a bibliography entry
  that is commented out. FREX's own scope note says the same for Theorem 13.2; it does not notice the identification
  of the weights.
- **Snowden on posets.** Abstract, Theorem A and Corollary B of the Introduction (body form: Theorem 5.1): the measures
  on the class of finite posets form a plane, eight lines and 15 points. Proposition 8.2: no measure on posets is
  regular; with Schmerl's classification (Theorem 8.1) and Theorem 8.4 the supports are classes of bounded
  antichains, bounded unions of chains and ordinal sums of bounded antichains. His class has no added linear order;
  the paper has no linear extensions, no amenability, no exactness. His "cuts" (§3.4), the ways of placing a marked
  point between elements incomparable to it, are close in spirit to the cells of A.10; I did not compare them
  further, and no statement of his is used or reproved by FREX. Nekrasov-Snowden, arXiv:2407.19131 (abstract
  only) bounds the number of measures on distal classes; nothing on exactness.

### 2.2 Question 2: Caramello and the topos

Source: Caramello, [arXiv:0805.2778v3](https://arxiv.org/abs/0805.2778) (TeX, §2 read; published as Logica
Universalis 8 (2014), 261-281; numbering reconstructed from the TeX and equal to FREX's): Theorem 2.7 (the theory of
homogeneous models is complete and countably categorical), Theorem 2.9 (Set[T′] ≃ Sh(f.p.T-mod(Set)^op, J_at) ≃
Cont(Aut M)), Proposition 2.10 (the same equivalence from the "Galois property", proved from Mac Lane-Moerdijk,
p. 154, Theorem 2). The proof of Theorem 2.5 uses that atomic toposes are locally connected. A search of the TeX
finds no abelian or module object, no homology, no exactness, no amenability, no Ramsey property; the same for her
"Topological Galois theory" (arXiv:1301.0300, grep only).

- **The answer (my derivation; three lines).** Let E = Sh(A^op, J_at) ≃ Cont(G), a: [A, Set] → E the associated sheaf
  and γ: E → Set. Constant presheaves on A^op are sheaves for the atomic topology, so for V: A → R-Mod and an R-module
  B, Hom(V, const B) = Hom(aV, γ*B). Hence colim_A V = γ_!(aV), where γ_! is the left adjoint of γ* on R-module
  objects (coinvariants, under E ≃ Cont(G)); this is A.1's formula. Since a is exact and has the fully faithful right
  adjoint i with a∘i = id, colim_A is exact over R if and only if γ_! is exact on R-module objects of E. That is a
  property of the topos, so of the Morita class of the theory, and it is invariant under passage to a dense subgroup.
- **What to cite for A.1.** The functors of A.1, T(N)(B) = N^{G_B} and S(V) = colim V(B), are those of Artin's theorem
  as written out for modules by Di-Li-Liang-Xu, [arXiv:2108.13600v4](https://arxiv.org/abs/2108.13600), Theorem 5.1
  and the displayed equivalence after it (discrete representations ≃ sheaves of R-modules on the orbit category; the
  paper was grepped and that passage read). Harman-Snowden point to the same paper in Remark 10.10. FREX's
  bibliography has Caramello and Li (arXiv:2510.15348) but not this paper. So K3 of
  `MAP_HOMOTOPY_CATEGORIES.md` is right, and Caramello supplies only the equivalence.

### 2.3 Question 3: anything else

| Source (copy read) | What it states, where | Relation to FREX |
|---|---|---|
| **Kechris-Sokić**, Fund. Math. 218 (2012), 69-94 (open PDF at impan.pl) | Proposition 2.1 (a criterion for non-amenability); Remark 3.2 (pp. 78-79): the class OP of finite posets with an arbitrary linear ordering, its expansion by a linear extension (a reasonable expansion with the ordering property, by Sokić), and Aut(Flim OP) is not amenable. | Exactly the class of A.11: the non-amenable half is **known**. FREX says so (A.tex l.605-606) and adds a proof of its own. |
| **Evans**, [arXiv:2603.29606v2](https://arxiv.org/abs/2603.29606) (TeX and PDF text; §1, Remarks 2.9-2.12, Lemma 3.7 read) | Theorem 1.4: for an ω-categorical Ramsey structure and any commutative ring R, membership in a submodule of a permutation module RW is decided by the orbit augmentation Ω_S. Corollary 1.5: separation by an invariant function. Lemma 3.7 (p. 17): invariants are exact on compact continuous modules of an extremely amenable group. Remarks 2.12 (p. 14): **open question** whether the separation property holds for a reduct N of a Ramsey structure; he expects a negative answer in positive characteristic and suggests characteristic 0 first. | "Extremely amenable ⟹ integrally exact" is **known** in this dual form (FREX A.3, last clause). Remarks 2.12 is the published question nearest to FREX; FREX cites Evans only in its source audit and does not mention it. |
| **Zucker**, Fund. Math. 226 (2014), 41-61 (open PDF at impan.pl) | §3, Theorem 3.1 (p. 45), for an excellent pair: with V the rational span of the vectors "an expansion minus the sum of its extensions along an embedding", Aut(K) is amenable iff every non-zero vector of V has coefficients of both signs. | The positive counterpart of A.9. In this notation A.9 over a field k reads: exact iff the total-mass vector is not in V ⊗ k (my restatement). |
| **Hexagon** 2611.00356 (Pongrácz, 12 Nov 2026; abstract) | Finite composition length of permutation modules for free-amalgamation structures with a generic order, extending Yang-Bojańczyk-Klin. | Neighbouring; nothing on coinvariants or amenability. |
| Abstracts only: Jahel-Joseph 2307.06253; Braunfeld-Jahel-Marimon 2408.08370; Jahel-Tsankov 2007.00281 | Invariant random expansions; invariant Keisler measures are such; invariant measures on the space of linear orders. | Terminology for the positive case of FREX's μ. |

- **Bearing on Evans's question (my derivation).** Exactness of smooth F-coinvariants for G passes to every open
  subgroup U (induction from U to G is exact and turns U-coinvariants into G-coinvariants), and for U it gives that
  Q^U → Q_U is injective for every smooth Q; applied to Q = FW/V and U the stabilizer of a finite set containing the
  support of x, this is Evans's separation. Hence: (a) by A.11 the separation property holds over every field, and
  the membership test of his Theorem 1.4 over every ring, for the generic poset with an independent linear order,
  which is a reduct of a Ramsey structure and is not Ramsey; (b) by A.9 it holds in characteristic 0 for every
  reduct whose automorphism group is amenable. The converse fails (for a finite group separation is trivial and
  exactness is not), so FREX's examples of non-exactness do not by themselves answer his question negatively; that
  needs a witness which survives in all small open subgroups, and it is a natural next step for the FREX writer.
- **The direction "amenable, not exact".** Trivial examples exist without any theory (Z; the infinite symmetric group
  over Z, by the finite-index obstruction of A.5). What is new in FREX is an example with every structural hypothesis
  in force and no finite-index obstruction (independently ordered F_2-spaces) and the example A_2(Q), amenable and
  exact over every F_p but not over Q. No source found has such an example.
- **Searches.** arXiv API, titles and abstracts: oligomorphic with amenable; with measures; with "smooth
  representations"; "extremely amenable" with modules, cohomology or homology (only Evans); "exact colimits";
  Fraïssé with exact and colimits; "tensor categories" with Ramsey; "invariant random expansions"; atomic topos with
  amenable, Ramsey or homology. One extended web search. Hexagon, 1,546 works, for Fraïssé, amenab-, oligomorphic,
  colimit, coinvariant, Ramsey, homogeneous structure, topos, invariant measure, linear extension, poset. No source
  states either direction. These are bounded searches of titles and abstracts, not of full texts.

### 2.4 What the FREX paper must cite, and how

1. **Kechris-Sokić, Remark 3.2**: the non-amenability in A.11 is theirs; FREX's four-point argument is a second proof.
   Sokić, "Ramsey property of finite posets, II" (Order 29 (2012)), is their source for the expansion; I did not open
   it; FREX uses Bodirsky, Corollary 1.4 (3), which its run opened.
2. **Evans**: Lemma 3.7 (i) and Theorem 1.4 as the known statement "extremely amenable ⟹ exact over Z" (dual form);
   Remarks 2.10-2.12 as the open question that A.9 and A.11 address, with the implication "exact for all open
   subgroups ⟹ separation" stated and proved.
3. **Harman-Snowden**: Example 3.5, Theorem 16.7, Remark 16.8 and Proposition 4.8 for the weights of A.10;
   Definitions 3.1 and 6.2, Remark 10.10 and Theorem 13.2 to say why their theory does not give A.9 or A.11.
   **Snowden 2609.02021**: Proposition 8.2 and Theorem 8.4 (no regular measure on posets).
4. **Zucker 2014, Theorem 3.1**, with Angel-Kechris-Lyons (opened by the FREX run, not by me): A.9 is the same linear
   system without positivity. Jahel-Joseph and Braunfeld-Jahel-Marimon for the name "invariant random expansion".
5. **Di-Li-Liang-Xu, Theorem 5.1**, Caramello, Theorem 2.9 and Proposition 2.10, and Mac Lane-Moerdijk III.9
   (through Caramello's proof; not opened by me) for A.1; the topos statement of section 2.2 as a remark.
6. Isbell-Mitchell 1973 and 1976 and Oberst 1968 as in FREX's own audit (opened by the run, not by me).

Not opened for this gate: Mac Lane-Moerdijk; Johnstone's Elephant; Sokić 2012; Bodirsky 2014; Angel-Kechris-Lyons;
Isbell 1974 (the FREX run could not obtain it either); Nekrasov's "Smooth representations of oligomorphic groups",
announced as in preparation in Harman-Snowden's bibliography and not found on arXiv by title or abstract.

## Addendum, 25 Nov 2026 ~05:0x UTC: Fiedorowicz 1984 opened (main session 329fb1e6, Claude Opus 5.5 at effort max)

The user supplied a copy: `<local>/Downloads/fiedorowicz-classifying-spaces-of-topological-monoids-and-categories-amer-j-math-1984.pdf`
(Amer. J. Math. 106 (1984), no. 2, 301-350; PDF page = journal page minus 299). Read: pp. 321-324 (end of Section 4, start of Section 5).
- p. 321, Theorem 4.7: every connected Delta-set X has a discrete monoid RX with BRX equivalent to |X| (the McDuff/Kan-Thurston
  type result, for discrete monoids, built in pp. 321-323 by the construction R_n; nothing on finite monoids).
- p. 323, end of Section 4: an example left as an exercise, the five-element monoid of a unit 1 and x_ij (i, j = 1, 2) with
  x_ij x_kl = x_il, for which BM is equivalent to S^2; and the sentence "It seems likely that any finite simply connected complex
  should be equivalent to the classifying space of a finite monoid."
- p. 324: Section 5 (proof of Theorem 4.1), Lemmas 5.1-5.2 on pushouts of monoids; nothing on finite monoids.
Verdict: pp. 321-324 do not contain or imply D2's Theorems 1.1, 1.2 or 2.1. The Fiedorowicz half of the gate is CLOSED.
For D2: cite Fiedorowicz p. 323 directly for the suggestion (it concerns simply connected complexes only, which is the
direction Ben-Bassat's Theorem C proves) and for the five-element example with BM equivalent to S^2, next to D2's own
examples; replace "as quoted in Martinian-Steinberg" by the direct citation. McDuff 1979 (Lemma 1) is still unopened.

## Addendum 2, 25 Nov 2026 ~05:1x UTC: McDuff 1979 opened in full (main session 329fb1e6, Claude Opus 5.5 at effort max)

The user supplied a copy: `<local>/Downloads/1-s2.0-0040938379900223-main.pdf` (D. McDuff, On the classifying spaces of
discrete monoids, Topology 18 (1979), 313-320). All eight pages read.
- Lemma 1 (p. 314): "The natural homomorphism M -> pi_1 BM is universal for homomorphisms of M into a group", with its proof. This
  is exactly the use D2 makes of it (pi_1 BM is the universal group U(M); D2's Lemma 3.1(a)). Confirmed.
- Theorem 1 (every path-connected space has the weak homotopy type of BM for a discrete monoid M), Theorem 2 (Heller's
  construction: G in M as maximal subgroup with BG -> BM a homology equivalence and G/P = pi_1 BM), its Corollary, Lemmas 2-8
  (right-free inclusions, pushouts, Lemma 4: B of a pushout is the pushout of B's; Lemma 6 on maximal subgroups of amalgams).
  Every monoid she constructs is infinite; nothing in the paper concerns finite monoids or bounded homology.
Verdict: McDuff 1979 neither contains nor implies D2's Theorems 1.1, 1.2 or 2.1. With Addendum 1, the D2 gate is now fully
CLOSED: the main theorems are new as far as every source named in the brief shows.

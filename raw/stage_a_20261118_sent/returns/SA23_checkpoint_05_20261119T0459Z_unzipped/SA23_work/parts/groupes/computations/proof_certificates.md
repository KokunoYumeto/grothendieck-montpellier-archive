# Indexed verification certificates — cotes 161-1 and 161-2

These are the arguments, counterexamples, and exact-scope audits performed in this run, dated 19 November 2026. They are present reconstructions; they do not amend the transcription. A certificate for a question may establish a conditional result, refute an overbroad formulation, or identify the unfilled hypothesis. It does not assert that every historical question is solved.

The extended arguments for the delicate cases are in [extended_proofs.md](extended_proofs.md). Executed finite and symbolic checks are in [check_groupes.py](check_groupes.py), with their actual [output](check_groupes.output.json). Nineteen program sections cover twenty-three claim identifiers. Finite checks certify the named examples and identities only.

Bibliographic keys refer to `../references.bib`; exact opened passages and quantifier comparisons are in `../search_log.jsonl` and `../claim_search_map.json`. A quotation below is a literal excerpt of the supplied transcription. Its separate English paraphrase, full source locator, page status, and competing readings remain in `../claims.json`.

## C-SA23-groupes-001

**Source:** sources/texts/codex/K161-1-01_transcription.tex:5–59.

**Literal excerpt:**

```tex
u|E'\ \text{pl. fidèle et }vu(E')\subset\overline{E'}\quad\Longleftrightarrow\quad
\forall\,Y\in\operatorname{Ob}E',\quad i(Y):Y\xrightarrow{\sim}vu(Y)\tag*{\textcircled{1}}\]
```

**Precise statement or question:** For L⊣R and full E′⊂E with RL(E′) in its essential closure, L|E′ is fully faithful iff η_Y is invertible for every Y∈E′; the dual counit statement holds.

**Check and its limit:** The adjunction comparison is Hom(X,η_Y). Bijectivity for X,Y∈E′ and closure of RL(Y) let Yoneda in E′ detect invertibility. The converse needs no closure.

**Literature match:** RiehlContextOnline Lemma 4.5.11 gives the global criterion; the full-subcategory version is re-proved here with its closure condition.

**References:** RiehlContextOnline.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-002

**Source:** sources/texts/codex/K161-1-01_transcription.tex:5–59.

**Literal excerpt:**

```tex
\margin{donner un exemple montrant que cette condition n'est pas surabondante, avec $E'$ réduit à un élément}
```

**Precise statement or question:** The closure condition cannot be omitted, even for a one-object E′.

**Check and its limit:** Take E the poset 0<1, F the terminal category, L unique and R selecting 1. For E′={0}, L|E′ is fully faithful, but η_0:0→1 is not invertible. All adjunction hom-sets are singletons.

**Literature match:** The standard unit criterion in RiehlContextOnline Lemma 4.5.11 isolates the missing global hypothesis; this exact two-object counterexample is supplied in this run.

**References:** RiehlContextOnline.

**Executed checks:** two-object restricted-unit counterexample. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-003

**Source:** sources/texts/codex/K161-1-01_transcription.tex:27–36.

**Literal excerpt:**

```tex
il suffit que $\forall Y\in\operatorname{Ob}E'$ \deleted{\unsure{on ait}}, $i(Y):\deleted{\unsure{soit}}Y\to vu(Y)$ soit \deleted{\unsure{un isom.}}\inserted{un mono} (resp. un \uline{\unsure{isom|mono}}). C'est aussi nécessaire si on sait que $vu(E')\subset\overline{E'}$
```

**Precise statement or question:** If the claimed necessity means η_Y monic in all of E, faithfulness of L|E′ and RL(E′)⊂E′ do not suffice. They give only E′-relative monicity.

**Check and its limit:** E has objects Z,Y,T, distinct f,g:Z→Y, unique h:Y→T and k:Z→T with hf=hg=k, and identities. T is terminal. Let L:E→1, R(*)=T, E′={Y,T}. The restricted L is faithful on each hom-set and RL(E′)⊂E′, but η_Y=h is not monic because f≠g.

**Literature match:** RiehlContextOnline Lemma 4.5.11 is a statement for the whole adjoint functor; it does not assert this false restricted criterion. The relative correction and finite witness are present reconstruction.

**References:** RiehlContextOnline.

**Executed checks:** ambient monicity fails despite restricted faithfulness. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-003; computation or formal certificate.

## C-SA23-groupes-004

**Source:** sources/texts/codex/K161-1-01_transcription.tex:61–210.

**Literal excerpt:**

```tex
c) L'ensemble des $E'$ \inserted{strictement pleines $\subset E$} satisfaisant (1), et des $F'$ \inserted{strictement pleines} satisfaisant (2), sont en correspondance biunivoque, en posant
```

**Precise statement or question:** The full subcategories E0={η_X invertible}, F0={ε_Y invertible} correspond by L,R. If η_R is invertible (equivalently ε_L), E0 is reflective in E and F0 coreflective in F.

**Check and its limit:** Triangle identities restrict L,R to inverse equivalences. If η_R is invertible then μ=RεL is its inverse and monad identities give Tη=ηT. Transposing this equality gives Lη·ε_L=id; the other triangle gives ε_L·Lη=id. Thus ε_L is invertible. Unit/counit give reflector RL and coreflector LR.

**Literature match:** RiehlContextOnline Exercise 5.1.iii and Proposition 5.3.3 match idempotent monads and their reflective fixed objects; the adjunction equivalence and dual statement are checked directly.

**References:** RiehlContextOnline.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-005

**Source:** sources/texts/codex/K161-1-01_transcription.tex:214–231.

**Literal excerpt:**

```tex
a) $E$ catégorie ponctuelle, $v$ l'unique foncteur $F\to E$. Il a un adjoint à g. \inserted{$u$} sss $F$ a un objet initial, et alors $u(P)=\varnothing_F$. Alors $u$ est pl. fidèle.
```

**Precise statement or question:** Adjunction with the terminal category selects an initial object on the left and a terminal object on the right.

**Check and its limit:** The required Hom(-,-) sets are singletons exactly by the defining initial/terminal universal properties. Singleton inclusions are fully faithful.

**Literature match:** RiehlContextOnline Chapter 4 supplies the adjunction framework; the complete elementary argument is given here.

**References:** RiehlContextOnline.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-006

**Source:** sources/texts/codex/K161-1-01_transcription.tex:233–281.

**Literal excerpt:**

```tex
Un foncteur $\psi:E_1^{\circ}\to(\mathrm{Ens})$ tel que $\psi\circ\alpha'$ est rep, est-il représentable ?
```

**Precise statement or question:** For a reflector a:E→E1 with fully faithful right adjoint j, a presheaf ψ on E1 whose pullback along a is representable is representable. If βa has a right adjoint R then β has right adjoint aR.

**Check and its limit:** A representing ξ is local because Hom(-,ξ) inverts every arrow inverted by a, in particular the units. Applied to η_ξ this supplies a retraction; naturality and the invertibility after a give the other inverse identity. Hence ξ≅j(aξ); Yoneda and the counit descend the representing isomorphism. Apply this objectwise to Hom(βa(-),Y) to obtain aR. Full faithfulness of β is unnecessary.

**Literature match:** RiehlContextOnline Definition 4.5.12 and Proposition 5.3.3 identify the local objects. The descent and adjoint-composition assertion are independently proved here, not attributed as verbatim statements in that source.

**References:** RiehlContextOnline.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-007

**Source:** sources/texts/codex/K161-1-01_transcription.tex:284–334.

**Literal excerpt:**

```tex
d'une bijection $\tau:I\to J$ et d'isom. $\varphi_i:L_i\xrightarrow{\sim}M_{\tau(i)}$
```

**Precise statement or question:** With the literal component-isomorphism convention Φ₁(A)≃A_core. The free symmetric monoidal category on arbitrary A must allow all component morphisms; the literal statement is correct when A is a groupoid.

**Check and its limit:** For A=[0→1], the singleton part has no arrow from 0 to 1 although A does. With all component arrows, extension by tensor products and symmetric coherence gives the usual free symmetric monoidal universal property.

**Literature match:** Batanin–Kock–Weber §1.1, p154 defines the free symmetric monoidal category using all component arrows. The hypothesis mismatch is therefore decisive, not terminological.

**References:** BataninKockWeber2018.

**Executed checks:** isomorphism-only free-family construction loses an arrow. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-007; computation or formal certificate.

## C-SA23-groupes-008

**Source:** sources/texts/codex/K161-1-01_transcription.tex:336–367.

**Literal excerpt:**

```tex
la donnée d'une structure $\unsure{\mathrm{AUC}|\mathrm{ANC}}$ sur celle-ci est \unsure{équivalent|équivalente} à la donnée d'un foncteur $\Pi:\Phi(e)\to C$
```

**Precise statement or question:** A symmetric monoidal structure is equivalently a coherent pseudoalgebra for the free symmetric monoidal 2-monad. An arbitrary ordinary Π with the stated restrictions is insufficient without flattening, unit and substitution coherence.

**Check and its limit:** The two composites that flatten a family of families need a specified natural isomorphism satisfying associativity and unit laws. An ordinary functor on permutation/component arrows does not specify those comparison maps. Under the coherent pseudoalgebra interpretation the universal construction is valid.

**Literature match:** Batanin–Kock–Weber §1.1 describes the free symmetric monoidal 2-monad; the source does not locally supply the pseudoalgebra comparison data.

**References:** BataninKockWeber2018.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-009

**Source:** sources/texts/codex/K161-1-01_transcription.tex:369–405.

**Literal excerpt:**

```tex
\[\Pi\circ\operatorname{inc}\xrightarrow[\text{Contraction}]{c}\Pi\circ\operatorname{res}\]
```

**Precise statement or question:** In a symmetric monoidal category, disjoint pairs with specified pairings to the tensor unit give a natural contraction map, independent of the ordering after coherence identifications.

**Check and its limit:** Choose an ordering, move paired factors next to each other, apply their pairings, and remove units. Symmetric coherence identifies different orderings. Perfectness of the pairings is not needed to define the map, only for duality assertions.

**Literature match:** The standard symmetric monoidal coherence framework of Batanin–Kock–Weber §1.1 supports the construction; the actual disjoint-pair argument is re-proved here.

**References:** BataninKockWeber2018.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-010

**Source:** sources/texts/codex/K161-1-01_transcription.tex:407–442.

**Literal excerpt:**

```tex
le passage d'un isom. de $\Pi L_i$ avec $L^{\otimes n}$ à un autre, via une permutation $\sigma$ de $[1,n]$, se fait par $\varepsilon(L)^{\operatorname{sign}(\sigma)}$
```

**Precise statement or question:** For a tensor-invertible object L in a symmetric monoidal category, c_{L,L} corresponds to ε(L)∈Aut(1), ε(L)²=1, and a permutation of n factors acts by ε(L) raised to its parity in {0,1}.

**Check and its limit:** Tensoring by an inverse identifies End(L⊗L) with End(1), a commutative monoid. Symmetry gives ε²=1; adjacent transpositions generate S_n and each acts by ε. The n! resulting arrows need not be distinct. The source’s L⊗2 at the permutation formula has the wrong tensor degree.

**Literature match:** Established symmetric coherence; an explicit odd-superline certificate in computations checks the sign convention. The manuscript additionally imposes trivial self-braidings in its use of Picard, stronger than a general modern Picard groupoid.

**References:** BataninKockWeber2018.

**Executed checks:** self-braiding permutation parity. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-011

**Source:** sources/texts/codex/K161-1-01_transcription.tex:443–466.

**Literal excerpt:**

```tex
Relation entre $\varphi_{L',L}$ et $\psi_{L',L}$ ? \unsure{Ils|Id.}
```

**Precise statement or question:** If φ:L⊗L′→1 is an inverse pairing and ψ:L′⊗L→1 is determined by φ⊗id_L=id_L⊗ψ with associators, then ψ=ε(L)(φ∘c_{L′,L}). Equality without ε requires trivial self-braiding.

**Check and its limit:** An odd one-dimensional superline L with odd inverse has φ=1, φ∘c=-1, while the triangle condition gives ψ=1. The scalar correction ε(L)=-1 is necessary. The general formula follows by moving L past L′ and using the two triangle identities.

**Literature match:** The symmetric monoidal framework is established; the question as literally phrased is answered by the supplied superline counterexample and its corrected formula, not by an unqualified identity.

**References:** BataninKockWeber2018.

**Executed checks:** self-braiding permutation parity. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-011; computation or formal certificate.

## C-SA23-groupes-012

**Source:** sources/texts/codex/K161-1-01_transcription.tex:469–514.

**Literal excerpt:**

```tex
Ces constructions \deleted{\unsure{(resp. $T$)}} forment donc une catégorie $\Gamma^T_{\deleted{\unsure{0}}}=\underline{\operatorname{Hom}}(T,i)$ (resp. \inserted{$\Gamma_0^T=$}$\underline{\operatorname{Hom}}_0(T,i)$], qui a des $\varprojlim$ finies (resp. des $\varprojlim$) et qui est munie de
```

**Precise statement or question:** For a doctrine of specified (co)limits and a pseudofunctor T on categories and functors preserving them, the corresponding (co)limits in Nat(T,τ) are computed objectwise when they exist in every target and are preserved by target-change functors.

**Check and its limit:** Pointwise (co)limits of the component functors carry the pseudonaturality isomorphisms because every transition functor preserves them. The component universal properties assemble uniquely. The missing preceding page is not reconstructed; 161-2-07:394–425 supplies the fuller statement.

**Literature match:** This is the pointwise functor-category theorem, within the enriched naturality framework of Kelly §§2–3. The later manuscript explicitly restores the preservation hypothesis.

**References:** Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-013

**Source:** sources/texts/codex/K161-1-01_transcription.tex:517–545.

**Literal excerpt:**

```tex
\uline{Mais c'est tjrs faux}
```

**Precise statement or question:** The contravariant functor Nat(-,φ):Fun(C,Set)^op→Set is never right exact, regardless of the additional finite-colimit hypotheses on C and φ. The truncated abelian variant is not a complete assertion.

**Check and its limit:** The initial presheaf 0 has 0×0=0, but Nat(0,φ)=1. A coproduct-preserving functor from the opposite would therefore require 1⊔1≅1. This also verifies the stronger elementary obstruction without relying on the manuscript’s injectivity argument.

**Literature match:** The obstruction is an independent proof using the standard opposite-category universal properties in Riehl. No external theorem matching the unfinished abelian symbols was located.

**References:** RiehlContextOnline.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-014

**Source:** sources/texts/codex/K161-1-01_transcription.tex:546–566; sources/texts/codex/K161-1-01_transcription.tex:558–575.

**Literal excerpt:**

```tex
Sous quelles conditions d'exactitude sur $E$ peut-on dire que $\bar\varphi$ est aussi exact à g ? [\uline{NB} si $E=(\mathrm{Ens})^\circ$, ce n'est \uline{jamais} le cas !]
```

**Precise statement or question:** For C small finitely complete and E a Grothendieck topos, Lex(C,E) is equivalent to left-exact cocontinuous functors PSh(C)→E. Arbitrary finitely complete, cocomplete E cannot replace a topos.

**Check and its limit:** The exact positive statement is the flat-functor theorem. For the negative assertion take E=Set^op: a functor preserving initial objects and binary products from any presheaf topos would send 0×0=0 to 1×_E1=2, yet its value at 0 is 1, a contradiction.

**Literature match:** SGA4 IV 1.2 gives the presheaf-topos correspondence in the author’s published work; the Set^op counterexample is re-proved here.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-015

**Source:** sources/texts/codex/K161-1-01_transcription.tex:567–575.

**Literal excerpt:**

```tex
Donc si $\bar\varphi$ est exact à g, $E$ est un topos.
```

**Precise statement or question:** If φ:C→E is small and dense, E is cocomplete, and its nerve N:E→PSh(C) has the canonical left-exact colimit-extension left adjoint, then E is a Grothendieck topos. Density, not only detection of arrows, is needed.

**Check and its limit:** Density makes N fully faithful. A left-exact reflector onto its image presents E as sheaves for the localizing topology on the small presheaf site. Conversely a small finitely complete site and its canonical sheafified Yoneda functor yield this presentation.

**Literature match:** SGA4 IV 1.2 and 9.1.2–9.1.7 are exact published forms of the localization characterization. Kelly §5 distinguishes dense from merely generating.

**References:** SGA4I1972, Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-016

**Source:** sources/texts/codex/K161-1-01_transcription.tex:579–620.

**Literal excerpt:**

```tex
\[\boxed{{}^{\sigma}j_\Omega=\operatorname{int}\rho(\sigma)^{-1}\circ j_\Omega}\]
```

**Precise statement or question:** For a neutral Tannakian fibre functor over Ω with tensor-compatible grading, let j:G_m→G_Ω be its cocharacter. If the grading is invariant under ρ(σ)∘σ, then σ(j)=ρ(σ)^−1jρ(σ).

**Check and its limit:** Invariance means ρ(σ)σ(j(t))ρ(σ)^−1=j(t) when the parameter is treated semilinearly, hence the formula. For j=SDS^−1 and ρ=Sσ(S)^−1, substitution gives σ(j)=ρ^−1jρ. A symbolic two-weight computation records the direction.

**Literature match:** Ziegler Theorem 3.6 identifies tensor gradings and cocharacters (arXiv 2011; journal volume 2015). The semilinear formula is checked directly and is conditional on the action convention.

**References:** Ziegler2015.

**Executed checks:** semilinear cocharacter conjugation direction. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-017

**Source:** sources/texts/codex/K161-1-01_transcription.tex:621–636.

**Literal excerpt:**

```tex
De plus, on a un $\otimes$-isom \unsure{$K$|$L$}-linéaire \unsure{fonct.|für} $M$ \unsure{variable}
\[
\operatorname{gr}(\bar T_p(M)_\Omega)\simeq\sum_i\operatorname{gr}^i(\mathrm{DR}_{L}(M))\otimes\underbrace{\unsure{\bar T_p|T_p}(T^{\unsure{i|'}}(1))}_{\deleted{\unsure{\text{de Tate}}}\ S_\Omega^{\unsure{i|{}}}}
\]
```

**Precise statement or question:** The sheet does not define enough of Ω, DR_L, T′(1), W,V and the final groups to identify an unconditional comparison theorem. Filtered F-crystals need admissibility before they can be identified with crystalline representations.

**Check and its limit:** No theorem is filled into these symbols. The nearby tensor-conjugation computation is C016. The actual Barsotti–Tate comparison under Liu’s finite totally ramified extension K/K0, with K0 the fraction field of the Witt vectors of a perfect residue field is narrower than arbitrary filtered F-crystals or two-weight Hodge–Tate objects.

**Literature match:** Searches of Ziegler, Liu and the linked 161-5 analysis match the grading and admissible Barsotti–Tate setting but do not identify the final underdefined statement. This is a searched identification limit, not a new open comparison conjecture.

**References:** Ziegler2015, Liu2013.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-018

**Source:** sources/texts/codex/K161-1-01_transcription.tex:639–670.

**Literal excerpt:**

```tex
\[\beta\alpha(\varphi)(\deleted{\unsure{X}}Y)=\alpha(\varphi)(Y)=\varinjlim_{Z\in C/Y}\varphi(Z)=\varphi(Y)\]
```

**Precise statement or question:** For a full inclusion i:C→E, small comma categories C/X and cocomplete F, (Lan_iφ)(X)=colim_{C/X}φ is left adjoint to restriction, and its unit is invertible.

**Check and its limit:** A cocone to ψ(X) is exactly the naturality datum for a transformation φ→ψi. At X∈C the comma category has terminal object id_X, so the colimit is φ(X). Fullness is needed for that terminal object.

**Literature match:** Riehl §6.2 gives pointwise Kan extensions; Kelly Chapter 4 gives the enriched analogue. The size hypothesis is retained explicitly.

**References:** RiehlContextOnline, Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-019

**Source:** sources/texts/codex/K161-1-01_transcription.tex:673–699; sources/texts/codex/K161-1-01_transcription.tex:704–707.

**Literal excerpt:**

```tex
Donc on trouve que $\beta':\underline{\operatorname{Hom}}'(E,F)\to\underline{\operatorname{Hom}}'(C,F)$ est pleinement fidèle.
```

**Precise statement or question:** For C small and dense in cocomplete E, restriction is fully faithful on cocontinuous E→F, and each such functor is its own pointwise Kan extension from C.

**Check and its limit:** Density expresses X as colim_{C/X}Y. Cocontinuity of ψ identifies the counit colim ψ(Y)→ψ(X) with an isomorphism. The adjunction then gives full faithfulness.

**Literature match:** Kelly §5.1 and Theorem 5.56 give the density/comodel formulation; the elementary counit proof is rechecked here.

**References:** Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-020

**Source:** sources/texts/codex/K161-1-01_transcription.tex:697–723.

**Literal excerpt:**

```tex
\uline{Lemme}\quad Si $\varphi\in\underline{\operatorname{Hom}}'(\unsure{C|E},F)$, alors pour $\forall$ système inductif $Y_i$ dans $C$ ayant une limite inductive $Y$ \uline{dans} $E$, on a $\varinjlim\varphi(Y_i)\xrightarrow{\sim}\beta\varphi(Y)$.
```

**Precise statement or question:** For a small dense K:C→E with E cocomplete, cocontinuous E→F correspond exactly to K-comodels C→F. Replacing the comodel condition by an unspecified set of internal C-colimit relations needs a density presentation.

**Check and its limit:** Flattening the small iterated colimits is valid. The essential-image assertion requires that every Hom_F(φ(-),b) be a nerve Hom_E(K(-),e_b); Kelly’s comodel criterion states exactly that requirement. The page’s cofinality shortcut is separately false (C021).

**Literature match:** Kelly Theorem 5.56, pp107–108, proves the precise equivalence; §§5.4 and 5.12 explain density presentations. No claim that the manuscript’s unqualified internal-colimit test is sufficient is made here.

**References:** Kelly1982.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-021

**Source:** sources/texts/codex/K161-1-01_transcription.tex:724–727.

**Literal excerpt:**

```tex
$I\to C/Y$, cela est-il cofinal ? C'est vrai en tous cas si pour $\forall$ diagramme \uline{fini} dans $C$, la $\varinjlim$ \uline{dans $E$} existe et est dans $C$.
```

**Precise statement or question:** Finite-colimit closure of a dense C does not imply the displayed cofinality. It holds for a filtered diagram when every C-object is finitely presentable in E.

**Check and its limit:** Let E=Set and C a small skeleton of countable sets, dense and closed under finite colimits. The filtered sequence Y_n={0,…,n−1} has colimit N∈C, but id_N:N→N does not factor through any Y_n. Thus its comma category against I is empty. Finite presentability supplies factorization and eventual equality, which repair the claim.

**Literature match:** Kelly’s density/comodel theorem does not justify this cofinality. The counterexample and the exact finite-presentability repair are independent proofs; Gabriel–Ulmer theory supplies the standard setting where the repaired hypothesis holds.

**References:** Kelly1982, LackPower2009.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-021.

## C-SA23-groupes-022

**Source:** sources/texts/codex/K161-2-01_transcription.tex:5–263.

**Literal excerpt:**

```tex
b) il soit universel en le sens suivant : Pour tt $E\in\mathrm{Ob}\,\Delta$, le foncteur $\varphi\longmapsto\varphi\circ i$ induit une équivalence

\[
\underline{\mathrm{Hom}}_{\Delta,i(\delta)}(\bar C_{\deleted{\delta}},E)\longrightarrow\underline{\mathrm{Hom}}_\delta(C,E)
```

**Precise statement or question:** For a small sketch and a set of bounded diagram shapes, free completion and forcing designated comparisons are small constructions in a sufficiently large universe. The particular mixed exactness doctrine additionally needs the stated compatibility and successor universal properties.

**Check and its limit:** Adjoin formal cone objects, factorization arrows and uniqueness relations in regular-cardinal stages. With a regular bound larger than all arities, every operation and relation occurs before a common later stage. This supplies the bounded term/sketch construction; it does not prove unspecified large or incompatible mixed doctrines have the same envelope.

**Literature match:** Lack–Tendas Theorem 4.4 identifies accessible categories with small sketches, and Proposition 5.12/Corollaries 5.13–5.14 give exact model-category hypotheses. Kelly’s free-cocompletion theory gives the bounded one-sided completions. The manuscript’s universal mixed 2-doctrine is only matched under these explicit conditions.

**References:** LackTendas2023, Kelly1982.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-023

**Source:** sources/texts/codex/K161-2-01_transcription.tex:102–124;253–258;436–461.

**Literal excerpt:**

```tex
\deleted{\unsure{$2^\circ$) Soit}} Soit pour ceci $\pi$ un cardinal tel que
\[
\pi>\mathrm{card}\,\mathrm{Fl}\,\Theta,\ \deleted{\unsure{\text{card Ob}}}\left\{\begin{aligned}
&\text{si }\Theta\ \deleted{\unsure{\in d'\text{ ou}}}\ \inserted{\in d'\text{ ou }\Theta\in d''}\\
&\text{ou }\Theta\ \deleted{\unsure{\in}}\text{ indexe un }\in\delta'\text{ ou un }\in\delta''
\end{aligned}\right.
\]
et $\omega$ le plus petit ordinal de cardinal $=\pi$. Donc l'ens $S_\omega$ des
```

**Precise statement or question:** The capture argument requires cofinality larger than every indexing size, achieved by a sufficiently large regular cardinal. Cardinal inequality alone is insufficient.

**Check and its limit:** At π=aleph_omega a countable list of stages aleph_n is unbounded, although omega<π. With regular κ, fewer than κ stages have a common bound; this captures diagrams, natural transformations, inverse arrows and equality witnesses. File02 later explicitly asks for an index set grand devant the bound.

**Literature match:** The sharply-larger/regular-cardinal framework is explicit in Lack–Tendas §§2.1–2.3. The concrete cofinality counterexample and the repaired transfinite proof are checked here.

**References:** LackTendas2023.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-023.

## C-SA23-groupes-024

**Source:** sources/texts/codex/K161-2-01_transcription.tex:268–416.

**Literal excerpt:**

```tex
Vérifier que cel permet \inserted{bien} d'exprimer l'\unsure{injectivité|intégralité|égalité} resp. surjectivité de $\varphi^*_C\vert\underline{\mathrm{Hom}}_\delta$ sur les Hom ....
```

**Precise statement or question:** For a small f:R→R′, fullness of Fun(R′,E)→Fun(R,E) is encoded by extending maps from the glued two-endpoint cylinder S=R′⊔_R(R×[1])⊔_R R′ to R′×[1]; faithfulness is encoded by the fold from two such cylinders. Carry the marked cones on the endpoints.

**Check and its limit:** A functor from S specifies two extensions and a transformation of their restrictions; a cylinder extension is precisely a lift of the transformation. Two lifts agree exactly when a functor from the doubled cylinder factors through the fold. Isomorphism invariance converts strict representatives to essential-surjectivity conditions. Composition and intersections of compatible exactness conditions follow by composition and union of tests.

**Literature match:** Small sketch and presentation methods in Kelly and Lack–Tendas support the ambient construction; the exact cylinder/fold formulas are independent reconstruction in this run. The manuscript’s compatibility condition is retained.

**References:** Kelly1982, LackTendas2023.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-025

**Source:** sources/texts/codex/K161-2-02_transcription.tex:294–535.

**Literal excerpt:**

```tex
$(*)$ Définition de foncteurs \uline{$\delta$-préexacts} $D.\xrightarrow{u}F$, $D$ muni d'un ens $\delta=(\delta',\delta'')$ de cônes....
```

**Precise statement or question:** Assuming K satisfies the listed universal and exactness obligations, regular iteration gives the claimed envelope and exact-cone lifting. The text ends before completing the definition of preexactness and never constructs the whole K.

**Check and its limit:** The underlying small diagram factors at one stage; its required cone is adjoined next. An isomorphism in the colimit is represented by an arrow and inverse, whose two identities hold at a later common stage. Thus exactness is witnessed eventually, up to isomorphism. Duplicating a cone vertex and inverting its comparison tests exactness, but does not alone construct all successor operations.

**Literature match:** The exactness-lifting argument is established under regular smallness; the general doctrine is only partly matched by small-sketch theory. No later source found in the searched literature supplies a theorem for the unfinished local notion of preexactness as written.

**References:** LackTendas2023, Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-026

**Source:** sources/texts/codex/K161-2-02_transcription.tex:6–148.

**Literal excerpt:**

```tex
Si on veut seulement montrer que \deleted{les} topos $R$ est ``algébrique'' c'est encore plus court
```

**Precise statement or question:** Every Grothendieck topos classifies a small geometric theory. A small site with finite limits gives the theory of left-exact functors satisfying its covering axioms. Here algebraic includes geometric disjunction/cover axioms, and is not restricted to an equational variety.

**Check and its limit:** Use a small finite-limit presenting site C; PSh(C) classifies Lex(C,-), and each covering family imposes that its image is jointly epimorphic. Compatible extra operations are represented by bicategorical amalgamation and then these axioms. The empty I-sorted theory has classifier PSh((FinSet^I_fin)^op).

**Literature match:** SGA4 IV 1.2 and 9.1.2–9.1.7 establish the presheaf and quotient constructions. The original IV9.1.6(d) explicitly records existence of the 2-fiber products used in the relative formulation.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-027

**Source:** sources/texts/codex/K161-2-02_transcription.tex:161–174.

**Literal excerpt:**

```tex
\uline{Question} Si $\forall E$, $T(E)$ admet des \deleted{produits fibrés quelconques} \inserted{$\underleftarrow{\lim}$ finies}, \inserted{(et les $T_R(E)\longrightarrow T_R(E')$ y commutent)} aura-t-on $T=$ restriction à $\Delta$ d'une théorie algébrique sur $\Delta_0$, i.e. $R\simeq\widehat C$, avec $C$ \inserted{(petite)} $\in\operatorname{Ob}\Delta_0$ i.e. $C$ stable par $\underleftarrow{\lim}$ finies ?
```

**Precise statement or question:** Geometric models have objectwise filtered colimits. Cartesian models Lex(C,E) have pointwise limits and, for E a Grothendieck topos, a locally presentable category structure; their arbitrary colimits need not be pointwise. The converse based only on existence of limits is a distinct question.

**Check and its limit:** Filtered colimits commute with finite limits in a topos and preserve covering axioms. Groups show nonpointwise coproducts: the underlying set of G*H is not the disjoint union. Merely existing limits without specifying their creation and compatibility with all geometric inverse images is weaker than a cartesian presentation.

**Literature match:** Makkai–Pitts Theorem 3.3/Corollary 3.4 and Lack–Tendas Proposition 5.12 give precise hypotheses for models; Beke’s presheaf-type criteria show why the converse needs more than a slogan. Searches did not identify the manuscript’s bare existence-only converse as stated.

**References:** MakkaiPitts1987, LackTendas2023, BekePresheafType.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-028

**Source:** sources/texts/codex/K161-2-02_transcription.tex:43–77;127–148.

**Literal excerpt:**

```tex
b) \deleted{\unsure{Ra}} Mettre axiomes sur théorie algébrique $T_R$, $R$ un topos, cela relève du Pb 2 traité. On trouve $R'$ et $R-R'$ \unsure{ess.|en} surjectif (et aussi surjectif sur les Hom).
```

**Precise statement or question:** A quotient of term categories can be full and essentially surjective. A left-exact reflector between topoi need not be full. Restriction along a full essentially-surjective ordinary quotient is fully faithful, but its left adjoint is not automatically left exact.

**Check and its limit:** On C=[0→1] with the covering {0→1}, PSh(C) has diagrams X1→X0 and sheafification is evaluation at0 followed by the constant-arrow embedding. Let P=(1→1), Q=(empty→1). There is no P→Q, while their sheafifications are both terminal and have one map. The finite Hom enumeration is saved.

**Literature match:** SGA4 IV9 describes geometric localization without requiring the reflector to be full. The finite-site counterexample distinguishes the two quotient levels; the ordinary restriction assertion follows directly from naturality along a full quotient.

**References:** SGA4I1972.

**Executed checks:** left-exact sheafification is not full. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-028; computation or formal certificate.

## C-SA23-groupes-029

**Source:** sources/texts/codex/K161-2-01_transcription.tex:494–524.

**Literal excerpt:**

```tex
Or ceci caractérise les morphismes de topos $R'-R$ qui sont des plongements.
```

**Precise statement or question:** For a geometric morphism i:E′→E, all Hom_top(F,E′)→Hom_top(F,E) are fully faithful exactly when i is a geometric inclusion. Subtopoi correspond to localizing topologies, hence to a set of covering axioms on a small presenting site.

**Check and its limit:** SGA IV9.1.4 proves the forward implication. Exercise9.1.6(b,c) gives the converse for full faithfulness on all 2-cells, with slices as tests; (d) gives base-change stability. This is stronger than injectivity on isomorphism classes or full faithfulness only on invertible 2-cells. Inverting literally every mono, as line520 might say, would invert0→1 and degenerate the topos.

**Literature match:** Exact own later published result: SGA4 I, Exposé IV, Proposition9.1.4 printed433; Exercise9.1.6(b,c,d) printed434–435. All three original pages were opened/rendered and read in this run.

**References:** SGA4I1972.

**Recorded event types:** targeted proof check.

## C-SA23-groupes-030

**Source:** sources/texts/codex/K161-2-02_transcription.tex:179–249.

**Literal excerpt:**

```tex
En résumé, on a $6$ sous-topos, avec diagramme d'implications
```

**Precise statement or question:** The six displayed theories are valid examples: unrestricted, inhabited, subterminal, terminal, empty and inconsistent objects. They are not an exhaustive list of quotient theories.

**Check and its limit:** In a topos epi+mono is an isomorphism, giving the displayed intersections. Another quotient imposes that the union of the three diagonals covers X³, with Set models |X|≤2, distinct from all six. The analogous n+1-variable axiom bounds cardinality by n.

**Literature match:** The small geometric quotient construction is SGA4 IV9.1. The additional finite-cardinality quotient is a direct syntactic reconstruction; no exhaustive classification is inferred from the diagram.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-031

**Source:** sources/texts/codex/K161-2-02_transcription.tex:248–264.

**Literal excerpt:**

```tex
$V$\inserted{$\unsure{?}$} représente le \inserted{$?$} foncteur
\[
 E\longmapsto\unsure{\mathfrak P|\mathscr P|\mathcal P}(E)=\mathfrak P(e_E)
\]
```

**Precise statement or question:** Subterminal objects are classified by the Sierpinski topos. This quotient of the object classifier is neither open nor closed; lattice complements must be taken in the full subtopos lattice.

**Check and its limit:** A subterminal object is precisely an open of the base topos; a frame map from the three-element Sierpinski frame chooses exactly one such open. Sentences in the empty one-sort geometric theory have only false, inhabited and true truth conditions: existentially quantified equalities have a witness in any inhabited object. Thus its nontrivial open quotient is the inhabited-object theory; the corresponding nontrivial closed quotient is the empty-object theory. The subterminal quotient is neither.

**Literature match:** SGA4 IV9.2.1–9.2.6 and9.3.4–9.3.5 give the exact open and complementary closed constructions; IV9.1 gives the quotient lattice. The Sierpinski frame argument is independently checked here. The finite-diagram complement guesses are not promoted to a full lattice calculation.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-032

**Source:** sources/texts/codex/K161-2-02_transcription.tex:265–273.

**Literal excerpt:**

```tex
\text{Pas d'objets loc. constants, ou constants}\\
 \text{Pas d'objets \deleted{constants} qui \unsure{après un pr. sup|après une pr. sup} ont}\\
 \hspace{3em}\text{\deleted{\unsure{qui après}} (resp. id sur }e\text{)}\\
 \text{Pas d'objets constructibles}
```

**Precise statement or question:** Local constancy and constancy of objects, with all ambient maps, need not be closed under filtered colimits and therefore are not in general geometric full subtheories. Constructibility requires an explicit finiteness convention.

**Check and its limit:** On Cantor space choose p and increasing clopens U_n whose union is C minus{p}. The subterminal sheaves U_n are locally constant, but their union is not. For constant objects use the constant two-point sheaf with successive maps collapsing the second point on U_n; the colimit has two stalk elements at p and one elsewhere, hence is not locally constant.

**Literature match:** Geometric models’ filtered-colimit closure follows from SGA4’s finite-limit/cover axioms; these fully specified topological examples refute automatic geometric definability. No undefined constructibility convention is supplied.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-033

**Source:** sources/texts/codex/K161-2-02_transcription.tex:274–279.

**Literal excerpt:**

```tex
\margin{\unsure{C'est} donc des structures alg. définissables par $\underleftarrow{\lim}$ finies et même par produits finis, et sauf les deux derniers \unsure{$\Longleftarrow$} par \unsure{l'un des deux|l'un des trois} ---}
```

**Precise statement or question:** The inhabited-object theory with all functions is neither a finite-limit theory with pointwise limits nor an ordinary equational theory. The other displayed theories require their own presentations.

**Check and its limit:** The two maps1⇉2 in nonempty sets have empty equalizer, outside the category. Nonempty sets have no initial object, whereas an equational variety has the free algebra on the empty set. The source cannot use one algebraic characterization for all six quotients.

**Literature match:** Gabriel–Ulmer finite-limit theory and Lawvere variety characterizations, as stated by Lack–Power and Adámek–Lawvere–Rosický, provide the exact closure tests.

**References:** LackPower2009, AdamekLawvereRosicky2003.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-033.

## C-SA23-groupes-034

**Source:** sources/texts/codex/K161-2-02_transcription.tex:153–160;280–288.

**Literal excerpt:**

```tex
\uline{Structure représentée par} $B_G=\widehat C\qquad C=\deleted{\unsure{(G,}}(\mathord{.},G)$
```

**Precise statement or question:** The group presheaf topos B_G classifies G-torsors, while its objects are G-sets. An unconstrained endomorphism has N-actions as Set models, but its classifying topos is the presheaf topos on its finite-limit syntactic category, not automatically B_N. Each listed small operation signature has a small cartesian presentation.

**Check and its limit:** Flat functors from a one-object group are torsors; the regular action condition follows from filteredness of the category of elements. Arbitrary N-actions include the empty action, whereas a flat action has a nonempty category of elements. Thus the two classifier interpretations differ. Operations and equations generate the finite-limit syntactic category.

**Literature match:** SGA4 IV1.2 supplies the flat-functor classification; finite-limit syntactic presentations are Gabriel–Ulmer theory. Classification of all subtopoi is not claimed to be completed by these examples.

**References:** SGA4I1972, LackPower2009.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-035

**Source:** sources/texts/codex/K161-2-02_transcription.tex:546–736.

**Literal excerpt:**

```tex
\margin{\unsure{Ben|Beck} \unsure{'Barr|'Baur|Barr} \uline{Linton} \qquad $U$ tripleable}
```

**Precise statement or question:** For U:A→C with a left adjoint, Beck’s theorem requires conservativity and creation/preservation of the relevant U-split coequalizers. The source’s numbered blank cannot be omitted. A split fork with its displayed identities is an absolute coequalizer.

**Check and its limit:** For a split fork X1⇉X0→Y with section and contracting map, any equalizing map factors through the section formula and uniqueness follows from the split epi. Every functor preserves these identities. Comparison with the monad is an equivalence under Beck’s full conditions, not solely from the generator and adjunction.

**Literature match:** Riehl Theorem5.5.1 pp204–205 and Proposition5.5.8 pp208–209 give exact criteria. Adámek–Lawvere–Rosický Lemma2.1 identifies the finitely presentable regular projectives needed by the Lawvere-generator discussion.

**References:** RiehlContextOnline, AdamekLawvereRosicky2003.

**Executed checks:** split coequalizer identities and universal property. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-036

**Source:** sources/texts/codex/K161-2-02_transcription.tex:739–776.

**Literal excerpt:**

```tex
\pi=f^*f_*\colon B-B\quad \boxed{\underline{\text{exact à g.}}}\quad\uline{\text{accessible}} […] \[
\underset{\text{tous deux}}{[\text{conserv.tif}]}\ 
\overset{\mathrm{déf}}{\Longleftrightarrow} f^*\ \text{fidèle}\ (= \underline{\text{conserv.tif}})\
\overset{\mathrm{th}}{\Longleftrightarrow}\underline{B_\pi\xrightarrow{\sim}B}
```

**Precise statement or question:** For a geometric morphism f:B→B′, π=f*f_* is a left-exact accessible comonad on B. Its coalgebras form a Grothendieck topos; if f* is conservative, B′≃Coalg(B,π). The source’s B rather than B′ has the wrong type.

**Check and its limit:** Dual Beck applies because f* preserves equalizers. For an accessible left-exact comonad, coalgebras are accessible, have finite limits created in B and all colimits created in B; the topos exactness axioms and a small generator follow. In the G-set example f_*(Y)=Set(G,Y), counit evaluates at1, and comultiplication is induced by group multiplication.

**Literature match:** Beck’s dual criterion follows from Riehl5.5.1; the accessible-category/sketch theorem supplies smallness. The topos part is also the left-exact comonad form of Giraud’s theorem, reconstructed with explicit accessibility rather than asserted for arbitrary large comonads.

**References:** RiehlContextOnline, LackTendas2023, SGA4I1972.

**Executed checks:** cofree finite-group comonad. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-037

**Source:** sources/texts/codex/K161-2-02_transcription.tex:778–808.

**Literal excerpt:**

```tex
Soit $B$ un topos

$\exists\ B'$ topos avec assez de pts
```

**Precise statement or question:** Every Grothendieck topos Sh(C,J) is a geometric subtopos of PSh(C), whose evaluation points form a conservative set.

**Check and its limit:** The inclusion of sheaves has left-exact sheafification as left adjoint. Presheaf maps are isomorphisms iff all component maps are; each evaluation preserves colimits and finite limits and has a right adjoint. This is the requested inclusion direction, not a surjective cover from a point-rich topos.

**Literature match:** SGA4IV1.2 and the sheaf presentation settle the stated inclusion direction. The separate detached formula is C111.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-038

**Source:** sources/texts/codex/K161-2-03_transcription.tex:6–136;248–267.

**Literal excerpt:**

```tex
1) anneau (comm. unifère) \quad $X_{\mathrm{ann}}=\widehat R$\quad
$R=\text{schémas affines de t.f.}/\mathbb Z\simeq(\text{alg de t.f. sur }\mathbb Z)^\circ$
```

**Precise statement or question:** Internal commutative unital rings are classified by PSh((CRing_fp)^op); over Z, finite type is finite presentation. The Zariski and étale topologies give nonzero local and strictly henselian local rings respectively. Ambiguous arrows in the opening property lattice are not assertions.

**Check and its limit:** Finite-limit models of (CRing_fp)^op are rings. Covering by D(f),D(1−f) gives the local axiom; the empty cover excludes the zero ring. Étale lifting gives strict henselianity. The elementary implications field⇒domain/local and reduced+irreducible nonempty⇒domain are checked, but connected does not imply local (Z), and reduced does not imply domain (k×k).

**Literature match:** SGA4 IV1.2 supplies the classifier mechanism. Gabber–Kelly Theorems2.3 and2.6/Table1 give exact Zariski/Nisnevich/étale local-ring descriptions under a separated noetherian base.

**References:** SGA4I1972, GabberKelly2015.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-039

**Source:** sources/texts/codex/K161-2-03_transcription.tex:28–136;414–458;462–486.

**Literal excerpt:**

```tex
\margin{$\forall f(a)\ \exists\unsure{e|\deleted{e}}\in\Pi(M)$ tel que $fe$ inv. et $f(1-e)$ \unsure{nilp.}}
```

**Precise statement or question:** For a commutative ring A, Spec(A) is zero-dimensional iff each f admits an idempotent decomposition A≃A_f×A/f^nA for some n, iff the principal ideals f^nA eventually stabilize. Compact here means Hausdorff compact, not merely quasi-compact.

**Check and its limit:** If Spec(A) is zero-dimensional, D(f) is clopen and equals D(e) for an idempotent e; on eA, f is a unit, and on(1−e)A it is nilpotent. Conversely the decomposition forces every prime quotient to be a field. Stationary powers give f^n=f^{n+1}g and hence the same unit/nilpotent separation. Testing only artinian local rings is not established by this argument.

**Literature match:** Stevenson §3 verifies the reduced zero-dimensional/absolutely-flat case; the nilpotent extension and stabilization criterion are proved here. Schröer’s nonnoetherian local examples show why no artinian-testing reduction is silently assumed.

**References:** Stevenson2014, Schroer2016.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-040

**Source:** sources/texts/codex/K161-2-03_transcription.tex:268–275.

**Literal excerpt:**

```tex
\uline{Question} Soit $X'\to X$ dans $R$ \deleted{tel} que $\forall$ anneau ultralocal noetherien $A$,
$X'(A)\to X(A)$ est épi, alors $X'\to X$ est-il couvrant fppf ? Résulterait du lemme : tout anneau local noeth $A$
(\unsure{ess$^t$ de|Rés. de} t.f., sur $\mathbb Z$) admet un hom local dans un anneau ultra-local qui est limite inductive d'algèbres fid. plates de t.f. sur $A$.
```

**Precise statement or question:** If ultralocal means fppf-local as in the displayed lifting condition, noetherian test rings do not detect fppf coverings. The correct conservative family must allow nonnoetherian fppf-local rings.

**Check and its limit:** Schröer Corollary4.5 shows these noetherian rings are exactly algebraically closed fields: p=p² and Nakayama kill the maximal ideal. Spec(F_p)→Spec(F_p[ε]/ε²) lifts every algebraically closed field point but is not an fppf covering sieve: any faithfully flat extension is injective and cannot kill ε. The finite dual-number computation is saved.

**Literature match:** Schröer, Points in the fppf topology, arXiv2014/final2016, Corollary4.5 and Theorem5.5; §6 constructs points. The exact fppf interpretation is retained because the manuscript’s ultralocal term is not independently defined elsewhere here.

**References:** Schroer2016.

**Executed checks:** dual numbers invisible to algebraically closed field tests. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-040; computation or formal certificate.

## C-SA23-groupes-041

**Source:** sources/texts/codex/K161-2-03_transcription.tex:253–275;497–509.

**Literal excerpt:**

```tex
\uline{4)} anneau str. local \quad $X_{\mathrm{anstrloc}}=\widetilde R_{\mathrm{et}}$ \quad et $=$ topologie étale
```

**Precise statement or question:** Over a separated noetherian base, the topology-local affine test objects identify local rings for Zariski, henselian local rings for Nisnevich, and strictly henselian local rings for étale. Integral-domain/AIC and valuation descriptions depend on the precise topology; fppf needs a separate theorem.

**Check and its limit:** Gabber–Kelly’s Table1 matches each named topology and its affine local objects, with finite-refinable covering hypotheses. A separably closed field is strictly henselian, while an algebraically closed field is fppf-local. The fppf table entry is not inferred from Gabber–Kelly, which omits it; Schröer supplies it separately.

**Literature match:** Gabber–Kelly arXiv1407.5782 (2014), Theorems2.3,2.6 and Table1; Schröer Corollary4.5 and §§5–6. The noetherian source/base condition does not say the local test rings are noetherian.

**References:** GabberKelly2015, Schroer2016.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-042

**Source:** sources/texts/codex/K161-2-03_transcription.tex:277–306.

**Literal excerpt:**

```tex
6) anneau réduit \quad $X_{\rm red}\simeq\widetilde R_{\deleted{\unsure{\rm top}}\rm red}\simeq\widehat R_{\rm red}$
```

**Precise statement or question:** Reduced commutative rings are models of the cartesian sequents x^n=0⇒x=0 (n≥1); their finitely presentable theory objects are reductions of finitely presented rings, and the classifier is the corresponding presheaf topos.

**Check and its limit:** Reduced rings are a reflective full subcategory of rings with reflector A↦A_red and are closed under filtered colimits and all limits. The category is locally finitely presentable; maps from A_red to reduced B are maps A→B. Its finite colimits are reduced ring colimits. Power-map kernels in the source are subsets, not additive kernels; their union is the nilradical.

**Literature match:** Makkai–Pitts Theorem2.4 gives the limits/filtered-colimit closure criterion; the explicit reduction adjunction proves the finite-presentation and classifier identification.

**References:** MakkaiPitts1987, SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-043

**Source:** sources/texts/codex/K161-2-03_transcription.tex:308–357.

**Literal excerpt:**

```tex
A_{\rm red}\overset{\rm df}{=}A/\underbrace{\varinjlim_n (I_n}_{\text{nilradical }N}=\operatorname{Ker}(A\xrightarrow{x\mapsto x^n}A))
 \quad\text{est intègre}
```

**Precise statement or question:** Domains require0≠1 and ab=0⇒a=0∨b=0. Irreducible rings require proper prime nilradical, equivalently A_red a domain; their geometric axiom uses an unbounded disjunction over nilpotence exponents. Reduced irreducible components impose domains, not arbitrary irreducible rings.

**Check and its limit:** The two axes jointly cover the zero-product locus exactly for a domain. For irreducibility, (ab)^n=0 implies locally a^m=0 or b^m=0 for some m. A finite cover by reduced irreducible components has the ordinary overlap equalizer sheaf condition; it does not make the components disjoint. The source’s reduced/induced component alternative changes the theory.

**Literature match:** Gabber–Kelly Table1 identifies integral domains with closed-topology local objects. The nilradical-prime formulation is checked directly; the exact alternative topology for nonreduced irreducible rings is left sensitive to the recorded reading.

**References:** GabberKelly2015.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-044

**Source:** sources/texts/codex/K161-2-03_transcription.tex:355–365.

**Literal excerpt:**

```tex
On obtient un exemple d'un sous-topos $X_{\rm irr}$ \deleted{\unsure{non quasi-compact}}\inserted{cohérent} du topos cohérent $X_{\rm ann}$.
```

**Precise statement or question:** In the given ring signature, irreducibility of Spec is not axiomatizable by a coherent first-order theory. This does not by itself decide whether its classifying topos has some different coherent presentation.

**Check and its limit:** For n≥2 let A_n=k[x,y]/(xy,x^n,y^n), each with one prime ideal. In a nonprincipal ultraproduct, x and y are nonnilpotent because every fixed power survives eventually, yet xy=0. Its nilradical is not prime. First-order coherent axioms are preserved by ultraproducts, so no such axiomatization in this signature exists. Failure of one site to be coherent is not an intrinsic topos invariant.

**Literature match:** The geometric/coherent distinction is explicit in Beke’s opening definitions. Searches found no exact theorem deciding the intrinsic coherence of the manuscript’s ambiguously specified quotient; the rigorous signature-level counterexample is the result established here.

**References:** BekePresheafType.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-044.

## C-SA23-groupes-045

**Source:** sources/texts/codex/K161-2-03_transcription.tex:367–410.

**Literal excerpt:**

```tex
$\forall f\in A(U)$, $f^2=f\Rightarrow f=1$ ou $f=0$ loc.
```

**Precise statement or question:** Connected spectrum is the idempotent axiom e²=e⇒e=0∨e=1; nonempty connected spectrum additionally excludes the zero ring. On finite-type affine schemes, the connected-component topology yields the presheaf description on the connected pieces, with the empty-object convention made explicit.

**Check and its limit:** Finite-type affines have finitely many connected components. A sheaf is determined by its values on those components and takes their coproduct to a product. Preserving nonempty finite coproducts leaves the empty value unconstrained; preserving the empty coproduct forces it to1. The source’s two conventions must not be merged.

**Literature match:** The small-site comparison and open/closed quotient mechanism are SGA4 IV1.2 and9.2–9.3. The component decomposition gives the exact elementary proof for this site.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-046

**Source:** sources/texts/codex/K161-2-03_transcription.tex:462–486.

**Literal excerpt:**

```tex
On trouve, si $D_n\subset A\times A\times A$ formé des $g,f,e$ avec $e^2=e$
$f^n(1-e)=0$, $g(1-e)=0$, $fg=e$, \unsure{on voit|on voit se|un mono} induit par \deleted{\unsure{pr}} \unsure{proj$_2$}
```

**Precise statement or question:** The equations e²=e, f^n(1−e)=0, g(1−e)=0, fg=e define D_n→A¹ as a monomorphism. As an affine scheme, D_n≃G_m⊔Spec(Z[t]/t^n); this is not the coproduct of the represented presheaves.

**Check and its limit:** The idempotent is uniquely the component D(f); g is f inverse on that component and0 elsewhere. Decomposing by e=1 and e=0 gives the displayed affine coproduct. A section over a disconnected test affine may use both components, so it need not choose one presheaf summand. Finite ring checks are saved.

**Literature match:** The absolute-flat/quasi-inverse literature (Olivier Proposition5 and Caramello–Johnstone §1) matches n=1; the general nilpotent equation calculation is independently checked.

**References:** Olivier1967, CaramelloJohnstone2009.

**Executed checks:** unit-nilpotent decomposition uniqueness. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-047

**Source:** sources/texts/codex/K161-2-03_transcription.tex:466–480.

**Literal excerpt:**

```tex
$\forall U$, $A(U)$ à spectre cpct i.e.
$\forall f\in A(U)$, $\exists(1)\ e\in A(U)$, $e^2=e$, $ef$ inversible dans $eA(U)$,
\deleted{$e$} $(1-e)f$ nilpotent. Suffit de le faire pour $f$ universel, $U=A$.
```

**Precise statement or question:** The geometric internal unit-or-nilpotent condition permits locally varying exponents. It is weaker than demanding every ordinary section ring A(U) be zero-dimensional.

**Check and its limit:** In E=Set^N let A_n=k[ε]/ε^{n+1}. Each component satisfies the geometric condition, hence the internal ring does. Global sections are the product, and f=(ε_n) is not nilpotent. On any nonzero idempotent component it is never a unit, so no global unit/nilpotent decomposition exists.

**Literature match:** The local meaning of geometric disjunction follows from the sheaf/topos semantics in SGA4. The explicit product example refutes only the global-section reading and does not alter the transcription.

**References:** SGA4I1972, CaramelloJohnstone2009.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-047.

## C-SA23-groupes-048

**Source:** sources/texts/codex/K161-2-03_transcription.tex:487–509.

**Literal excerpt:**

```tex
$\exists(1)\ e\in A(U)$, $e^2=e$, $ef$ inv., $e(1-f)=0$
i.e. $i_1:D_1\hookrightarrow A$ est un isom
```

**Precise statement or question:** Reduced zero-dimensional commutative rings are absolutely flat and have unique quasi-inverses a*, a²a*=a and a(a*)²=a*. The universal reflection A→A_abs is obtained by adjoining these elements and induces a bijection on spectra with identical residue fields.

**Check and its limit:** Uniqueness follows by comparing two quasi-inverses and using reducedness. For f=2 in Q, the source’s e(1−f)=0 fails with e=1; the needed relation is f(1−e)=0. Olivier’s construction A[x_a]/(a²x_a−a,ax_a²−x_a) gives the universal reflection, and its spectrum has the constructible topology.

**Literature match:** Olivier, seminar talks20Dec1967/3Jan1968, Proposition5; Stevenson arXiv2012/journal2014, Proposition3.3 and Theorem3.9; Caramello–Johnstone §1 proves uniqueness. This is an exact match to the identifiable reflection, not a license to identify every proposed coverage.

**References:** Olivier1967, Stevenson2014, CaramelloJohnstone2009.

**Executed checks:** quasi-inverse relations and product decomposition. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-049

**Source:** sources/texts/codex/K161-2-03_transcription.tex:513–614.

**Literal excerpt:**

```tex
&X_{\mathbb Q}=X_{\mathrm{car.}\,0}=\deleted{\unsure{\mathrm{car}\neq p}}\bigcap_{n\geq2}X_{\mathbb Z[1/n]}
```

**Precise statement or question:** n·1=0 and n invertible are cartesian ring quotients represented by subterminal objects of the affine syntactic category and hence open subtopoi. Requiring every positive integer invertible gives Q-algebras, not all rings of characteristic0.

**Check and its limit:** For n=1 the first quotient permits only the zero ring, whose theory has classifier Set rather than the degenerate topos. Z has characteristic0 but is not a Q-algebra. A Λ-algebra structure is uniquely determined by the underlying ring only when Z→Λ is an epimorphism in commutative rings; arbitrary Λ does not have this property. Over nonnoetherian Λ use finitely presented, not merely finite-type, algebras.

**Literature match:** SGA4 IV9.2 gives the open-quotient criterion. Olivier’s ring-epimorphism framework supplies the relevant meaning of uniqueness. Each elementary ring assertion is separately checked here.

**References:** SGA4I1972, Olivier1967.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-050

**Source:** sources/texts/codex/K161-2-03_transcription.tex:606–630.

**Literal excerpt:**

```tex
Comme $\operatorname{Pro} R\hookrightarrow\widehat R$, \deleted{\unsure{on peut}} on peut supposer plus gén. $S\in\operatorname{Ob}\widehat R$, \inserted{$S\subset e_{\widehat R}$}
```

**Precise statement or question:** The naive limit-of-representables functor Pro(R)→PSh(R) need not be fully faithful. Pro-objects are fully faithfully represented by covariant left-exact functors with the opposite convention, not by this unrestricted presheaf limit.

**Check and its limit:** For R=FinSet, a profinite set P maps to the presheaf T↦Map(T,underlying P), since finite discrete test sets impose no continuity. The indicator of the all-zero sequence {0,1}^N→{0,1} is a natural transformation of these presheaves but is discontinuous, hence not a pro-morphism.

**Literature match:** The correct Ind/Pro universal-property framework is in Kelly and Lack–Power. The discontinuous-map example completely checks the claimed full-faithfulness failure.

**References:** Kelly1982, LackPower2009.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-050.

## C-SA23-groupes-051

**Source:** sources/texts/codex/K161-2-03_transcription.tex:597–670;738–755.

**Literal excerpt:**

```tex
Ou encore $\mathcal E\to\widehat R$ se factorise localement sur $\mathcal E$ par la ``réunion'' $V=\deleted{\ensuremath{X}}_{\mathrm{car}>0}$ des sous-topos ouverts \deleted{\ensuremath{V}} $\widehat{R_{\mathbb Z/p\mathbb Z}}\simeq\widehat R_{\mathrm{Sp}\,\mathbb Z/p\mathbb Z}$, et le sous-topos $W=\widehat{R_{\mathbb Q}}$ (qui n'est pas un sous-topos ouvert) avec mêmes images \deleted{inverses}
```

**Precise statement or question:** An infinite intersection of open classifying subtopoi need not be open. In the ring classifier the Q-algebra subtopos is nontrivial and not the open represented by lim_n Spec Z[1/n].

**Check and its limit:** A nonzero finitely generated Z-algebra has a maximal ideal with finite-characteristic residue field (Stacks00GB), so it cannot contain Q. Thus on finite-type affine Z-tests the inverse-limit presheaf is the same as the representable empty affine, although Q is a model of the Q-algebra theory. This identifies the failed presheaf-limit step.

**Literature match:** SGA IV9.2.6 states preservation of finite intersections, not arbitrary intersections. Stacks00GB supplies the exact finite-type Jacobson fact; C050 identifies the general pro-embedding error.

**References:** SGA4I1972, StacksJacobson.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-052

**Source:** sources/texts/codex/K161-2-03_transcription.tex:140–205;618–670.

**Literal excerpt:**

```tex
&\text{On a}\quad i_{\unsure{!|1}}^{\deleted{\unsure{*}}}=\text{inclusion de $R_{/S}$ ds $R$},
 \quad i^*(X)=X\times_e S/S\\
 &i_*(\underset{\text{Objet de $R$ sur $S$}}Y)
 =\{ \underset{\operatorname{Ob}R}{X}\longmapsto\operatorname{Hom}_S(X\times S,Y)=\operatorname{Hom}(X\times S,Y)\},\\
 &\text{ou}\quad i_*(\deleted{\unsure{F|Y}}Y)=\underline{\operatorname{Hom}}(S,Y).
```

**Precise statement or question:** For a mono S→1 in small finitely complete R, PSh(R/S)≃PSh(R)/yS; i_! is forgetful, i* is product with S, and i_* is internal Hom(S,-). Inverting a small filtered family Sα→1 uses the finite-limit localization colim R/Sα, not the ambient presheaf inverse limit.

**Check and its limit:** The slice equivalence follows by the category of elements of yS. The adjunctions follow from product/exponential universal properties. Exact functors on the filtered localization are exactly lex functors making every Sα terminal, giving the classifier. For an arbitrary subterminal presheaf use its sieve of objects rather than R/S if it is not representable.

**Literature match:** SGA IV9.2.1–9.2.6, especially Remark9.2.3 printed451–452, explicitly warns against confusing the two full embeddings. These exact pages were opened in the retypeset primary text.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-053

**Source:** sources/texts/codex/K161-2-03_transcription.tex:674–731.

**Literal excerpt:**

```tex
p\,1_A=0,\qquad A\xrightarrow{x\mapsto x^p}A\quad\text{isom} […] \margin{en car. $0$, on convient que parfait signifie réduit ?}
```

**Precise statement or question:** In characteristic p, requiring Frobenius to be invertible defines the theory of perfect rings and implies reducedness. Its finitely presentable objects are perfections of finitely presented F_p-algebras in the perfect-ring category. The characteristic0 margin proposes a convention, not a standard theorem.

**Check and its limit:** Frobenius injective kills any nilpotent after enough p-powers. Adjoining inverse Frobenius is an algebraic operation with equations, and perfection is the filtered colimit along Frobenius; the adjunction transports finite presentations. Adding quasi-inverses gives perfect absolutely flat rings; adding nontriviality/locality gives perfect fields.

**Literature match:** The algebraic-theory presentation mechanism is established in Adámek–Lawvere–Rosický; the explicit perfection argument is re-proved. Searches did not identify a standard char0 definition matching the marginal question.

**References:** AdamekLawvereRosicky2003, CaramelloJohnstone2009.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-054

**Source:** sources/texts/codex/K161-2-03_transcription.tex:771–815.

**Literal excerpt:**

```tex
le plus grand ouvert de $\mathcal E$ \deleted{sur lequel} \inserted{tel que} $f$ t. $\mathcal E_{/e'}$ se factorise par \unsure{$V$|$0$}
```

**Precise statement or question:** If the factorization loci are open and stable under geometric inverse image, and the specified open pieces glue along their open overlap, the resulting map to B is an inclusion by local full faithfulness. Existence of such stable largest opens for arbitrary subtopoi is not automatic.

**Check and its limit:** When largest opens exist, the one for V∩W is their intersection by its universal property, as the text itself notes. On an open cover, maps and natural transformations glue; full faithfulness on each included piece gives full faithfulness globally, hence the SGA9.1.6 inclusion criterion. This does not prove the missing stability/existence premise for arbitrary V,W.

**Literature match:** SGA IV9.1.6 and9.2.5 settle the inclusion and open base-change tools. Theorem9.5.4 proves a different precise open/closed recollement theorem; it must not be substituted for the source’s arbitrary two-subtopos criterion. Searches did not locate the unqualified stable-factorization-locus theorem.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-055

**Source:** sources/texts/codex/K161-2-03_transcription.tex:729–760;816–830.

**Literal excerpt:**

```tex
on sait que $V$ est déjà un ouvert de $B=\widehat R$ […] Donc \uuline{OK}
```

**Precise statement or question:** Rings whose base is locally partitioned into prime-field algebra structures are classified by the presheaf category on finite-type affine schemes over the prime fields, with their empty affine objects identified. Components excluding the zero ring are disjoint; those allowing it meet in the common open Set point.

**Check and its limit:** Different prime characteristics have only the zero ring in common. The opposite affine categories therefore amalgamate at the empty affine; flat functors give the corresponding local choices of a prime-field component. Open gluing of the pieces gives the topos and its point criterion: the glued topos has enough points iff each open piece does. This is local constancy of the prime-field choice in the base topos, not a claim that every ring has such a decomposition.

**Literature match:** SGA IV9.2 and the site/flat-functor theorem give the checked gluing mechanism. The source’s explicit small amalgamated category allows a direct proof even though the general criterion C054 remains conditional.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-056

**Source:** sources/texts/codex/K161-2-03_transcription.tex:832–860.

**Literal excerpt:**

```tex
22) Anneau quasi \deleted{\unsure{irrédu|indé}} connexe de rang $\leq n$ (dont le spectre a au plus $n$ comp connexes \deleted{\unsure{$\}$|?}}, donc qui est somme d'au plus $n$ schémas connexes)

\deleted{A} \uline{Déf} On peut trouver loc. une décomposition en produit $A_1\times A_2\times\cdots\times A_n$, avec les $A_i$ connexes $\Longleftrightarrow$ on peut trouver loc. \deleted{d'un produit} des projecteurs $e_i$ ($1\leq i\leq n$) orthogonaux de somme $1$, avec $A_j=A/\sum_{j\ne i}e_j A$ connexe pour tt $1\leq j\leq n$.
```

**Precise statement or question:** For ordinary rings, at most n connected components is equivalent to a finite Boolean idempotent algebra with at most n atoms, and is expressed by the coherent bound that any n+1 orthogonal idempotents summing1 contain0. Its equivalence to the source’s local decomposition in every topos needs a constructive argument.

**Check and its limit:** The Boolean bound makes the Boolean algebra finite, hence decomposes1 into at most n atoms and A into connected factors. Conversely a product of at most n connected rings has exactly that idempotent bound. This Set-level proof does not construct stable largest connected-factor loci internally.

**Literature match:** The geometric axiom/classifier construction is SGA IV9.1; the finite Boolean calculation is proved here. No searched primary source was found proving the exact unqualified internal-largest-locus construction.

**References:** SGA4I1972.

**Executed checks:** component bounds and exact-rank collapse. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-057

**Source:** sources/texts/codex/K161-2-04_transcription.tex:4–16.

**Literal excerpt:**

```tex
Je ne sais si les \uline{pseudo}-\uline{torseurs} commutent à tt chgt de base \inserted{$\unsure{E'|E_i'}\mathbin{-}E$}, mais le torseur oui, si on se borne aux $E$ munis de $A$ quasi-connexe de rang exact $n$. Or la donnée d'un tel revient à la donnée
```

**Precise statement or question:** For a fixed ring with n connected nonzero factors, ordered decompositions form an S_n-torsor. An already given G-pseudotorsor, defined by G×P≃P×P, is preserved by geometric inverse image; adding P→1 epi gives a torsor.

**Check and its limit:** Atoms of the Boolean idempotent algebra determine the decomposition, uniquely up to permutation. The pseudotorsor defining isomorphism is a finite-limit identity and is preserved by f*; epimorphic local inhabitance is also preserved. This answers the property-level question but not whether the assignment of all decompositions is geometric.

**Literature match:** SGA IV1.2 and the classifying topos B_G identify torsors; preservation of the displayed defining equation is a direct check.

**References:** SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-058

**Source:** sources/texts/codex/K161-2-04_transcription.tex:4–16.

**Literal excerpt:**

```tex
Il n'est pas clair cependant que la formation des $e'_n$ commute aux chgt de topos de base $E'\mathbin{-}E$
```

**Precise statement or question:** For n≥2, the full category of rings with exactly n connected components, with all ring homomorphisms, is not a geometric full subtheory. A theory retaining decomposition/torsor data has different morphisms.

**Check and its limit:** Take A=k^n and repeat the idempotent endomorphism (a1,…,an)↦(a1,…,a1). Each stage has n connected components, while the filtered colimit is its image k and has one. A geometric full subtheory must be closed under these filtered colimits. The finite k example and idempotent-image calculation are saved.

**Literature match:** The SGA geometric-model closure test settles the full-property interpretation negatively. It does not refute a moduli theory with specified decomposition and equivariant morphisms.

**References:** SGA4I1972.

**Executed checks:** component bounds and exact-rank collapse. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-058; computation or formal certificate.

## C-SA23-groupes-059

**Source:** sources/texts/codex/K161-2-04_transcription.tex:19–52.

**Literal excerpt:**

```tex
$M$ \uline{plat} cela est-il une propriété typique [elle est stable par $\varinjlim$ \unsure{filtr|filtr.} et par chgt de topos $\}$
```

**Precise statement or question:** For an internal module over an internal commutative ring, flatness is expressed geometrically by the finite equational criterion: each relation factors through a finite matrix of relations. It is preserved by geometric inverse image and filtered colimits.

**Check and its limit:** For Σa_i m_i=0 require finitely many n_j and b_ij with m_i=Σb_ij n_j and Σa_i b_ij=0. The disjunction over finite matrix sizes and the existential witnesses are geometric. The usual ideal-injectivity criterion follows by tensoring0→I→A and the reverse implication reduces arbitrary relations to finitely generated ideals.

**Literature match:** Stacks00HK proves the exact equational criterion; Stacks058C Theorem10.81.4 gives Lazard’s finite-free filtered-colimit formulation. These are stronger than a mere keyword match to flatness.

**References:** StacksFlatness.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-060

**Source:** sources/texts/codex/K161-2-04_transcription.tex:54–69.

**Literal excerpt:**

```tex
$M$ \uuline{fid} \uline{plat}\\est-ce typique?
```

**Precise statement or question:** Faithfully flat modules, with all module maps, are not a geometric full subtheory. Faithfully flat unital algebras are a different case.

**Check and its limit:** The filtered sequence Z --2→ Z --2→… has faithfully flat terms but colimit Z[1/2]. Tensoring the colimit with Z/2 gives0, so it is not faithfully flat. Multiplication by2 is a module map but not a unital Z-algebra map; that distinction is essential.

**Literature match:** Stacks flatness criteria and the geometric filtered-colimit closure test settle the interpretation by this independent explicit counterexample.

**References:** StacksFlatness, SGA4I1972.

**Executed checks:** additivity does not imply exactness; faithful flatness fails under module colimits. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-060; computation or formal certificate.

## C-SA23-groupes-061

**Source:** sources/texts/codex/K161-2-04_transcription.tex:54–69;90–95; sources/texts/codex/K161-2-04_transcription.tex:104–117.

**Literal excerpt:**

```tex
\left\{\begin{array}{l}\text{Localement libre}\\ \text{libre, projectif / injectif (?)}\end{array}\right.\\
```

**Precise statement or question:** With all module maps, finite generation/presentation, cyclicity, projectivity and invertibility fail geometric filtered-colimit closure. Ordinary categorical injectivity also fails preservation by geometric inverse image; a different internal injectivity convention would need to be specified.

**Check and its limit:** The same Z --2→Z sequence has free rank-one stages and non-finitely-generated colimit Z[1/2], which is not projective over Z (a projective abelian group is free, and a nonzero free group cannot be indefinitely2-divisible). For injectivity, pull the injective k-module k from Set to sheaves on a circle. The constant sheaf k embeds in the rank-two local system with monodromy [[1,1],[0,1]], but no invariant splitting exists; hence it is not injective. The matrix obstruction is checked in the certificate.

**Literature match:** Stacks0B8I identifies tensor-invertible modules with finite locally free rank1; the explicit colimit and local-system arguments settle these full-property readings. No claim is made that the same examples refute moduli with a chosen basis or duality.

**References:** StacksInvertible, SGA4I1972.

**Executed checks:** ordinary injectivity fails after constant-sheaf inverse image. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-062

**Source:** sources/texts/codex/K161-2-04_transcription.tex:70–87.

**Literal excerpt:**

```tex
\margin{Considérons une Algèbre qui est déjà de \uuline{\deleted{\unsure{t}}p.f.} On veut ``la \unsure{vendre|rendre}'' plate, ou lisse etc. Cela se fait-il par un sous-topos ??}
```

**Precise statement or question:** Integrality, radiciality, surjectivity on spectra, flatness and formal unramifiedness have geometric finite-witness formulations; universal homeomorphism combines integral, radicial and surjective. Smoothness/étaleness without a retained finite-presentation hypothesis must not be conflated with their formal versions.

**Check and its limit:** Integrality has a monic-polynomial witness. For radiciality the diagonal is surjective, so every element of ker(B⊗_A B→B) is nilpotent. Surjectivity is equivalent to rad(IB)∩A=rad(I) for every finitely generated ideal I, expressible by finite equations with an unbounded disjunction of powers. Flatness is C059; Ω_B/A=0 expresses formal unramifiedness. For a fixed finite presentation, flatness can therefore be forced by a geometric quotient; smoothness needs the standard finite-presentation/Jacobian criterion. The unqualified formal-smooth/formal-étale geometric classification is not identified by the source fragment.

**Literature match:** Stacks01S4 gives the exact diagonal criterion; Stacks00FF gives spectrum base-change facts; Stacks00UM identifies formal unramifiedness with Ω=0; Stacks00TH Proposition10.138.13 separates formal smoothness from smoothness by finite presentation. The broad remaining formal-property question is retained rather than inferred from ind-smoothness.

**References:** StacksRelativeAlgebra, StacksFlatness.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-063

**Source:** sources/texts/codex/K161-2-04_transcription.tex:96–117.

**Literal excerpt:**

```tex
Une condition nécessaire pour qu' \deleted{\unsure{A soit un}} un Anneau se plonge \unsure{$\to X$|$X'\to X$} dans un corps, c'est que la section nulle (donc tte autre section) soit \unsure{sommande|sommante} direct de $A$, et c'est sans doute suffisant
```

**Precise statement or question:** In a topos, a domain with decidable zero embeds in its internal fraction field. A subring of a geometric field necessarily has decidable zero. Domain alone does not imply this constructive condition.

**Check and its limit:** If zero is complemented, nonzero elements form a multiplicative subobject; localization at them is a field and the domain map is monic. Conversely a geometric field has complementary zero and units, whose pullback gives decidable zero in a subring. For the generic domain, a nonunit can vanish after quotient to a prime-domain residue, so the universally nonzero elements are only units.

**Literature match:** Caramello–Johnstone §1 gives the geometric field decomposition and distinguishes ordinary field models from their internal classifier. The internal fraction argument is reconstructed explicitly with its decidability hypothesis.

**References:** CaramelloJohnstone2009.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-064

**Source:** sources/texts/codex/K161-2-04_transcription.tex:118–132.

**Literal excerpt:**

```tex
M\ \text{inv.}\quad\Longleftrightarrow\quad M\otimes_A\underbrace{\underline{\operatorname{Hom}}_A(M,A)}\xrightarrow{\sim}A
```

**Precise statement or question:** If the evaluation M⊗Hom_A(M,A)→A is an isomorphism, M is finite locally free of rank1. Monogenicity holds locally, not necessarily globally.

**Check and its limit:** Write the inverse image of1 under evaluation as a finite sum of tensors m_i⊗phi_i; the values phi_i(m_i) generate the unit ideal. Locally where one is invertible, m_i is unimodular and M splits as A⊕N. The cross term N⊗A lies in the kernel of evaluation, so injectivity forces N=0. This finite open cover proves M finite locally free rank1. The ideal(2,1+sqrt(-5)) has I²=(2) and norm2, but a²+5b²=2 has no integer solution, so it is invertible and nonprincipal. Hom base change is used only after finite projectivity is established.

**Literature match:** Stacks0B8I proves precisely tensor inverse⇔finite locally free rank1 and identifies the inverse with Hom(M,A). The global-monogenic assertion is refuted by the stated ideal.

**References:** StacksInvertible.

**Executed checks:** invertible nonprincipal rank-one module. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-064; independent re-proof; computation or formal certificate.

## C-SA23-groupes-065

**Source:** sources/texts/codex/K161-2-04_transcription.tex:137–179;202–217;373–392.

**Literal excerpt:**

```tex
a) $E$ $\pi$-accessible

b) $E$ équivalente à une catégorie $\operatorname{Ind}_\pi(C)$, $C$ petite

c) La sous-catégorie $E_\pi$ de $E$ formée des objets $\pi$-accessibles est équiv. à une petite cat. et elle est strictement génératrice.
```

**Precise statement or question:** For small C and regular κ, Ind_κ(C) is the free κ-filtered-colimit completion; its κ-presentables are the retract closure of C. An identification of a given E with that particular Ind_κ(C) requires the density and κ-filtered comma presentation. Accessible functors admit such a description at suitable ranks.

**Check and its limit:** An object presented by a κ-filtered colimit is κ-presentable only if its identity factors through a stage, hence is a retract. Conversely retracts of representables remain presentable. The canonical comma presentation is κ-filtered in the valid Ind setting. Density alone does not imply Ind of the selected C: {1} is dense in Set but its Ind category is terminal. This does not refute Set’s accessibility with a larger small presentable subcategory.

**Literature match:** Lack–Tendas §2, Theorem2.3 and Corollary2.5 give exact Ind/rank statements; Beke Proposition0.1 states the finitely accessible/presheaf-points correspondence. The source’s later stronger formulation is kept as the final version.

**References:** LackTendas2023, BekePresheafType.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-066

**Source:** sources/texts/codex/K161-2-04_transcription.tex:157–170.

**Literal excerpt:**

```tex
\uline{Corollaire} Supposons $f$ $\pi$-accessible. Alors \deleted{\unsure{il y a}} $\exists\ \pi_0$ tel que
\[
 \pi\geq\pi_0\Longrightarrow f(E_\pi)\subset F_\pi .
\]
```

**Precise statement or question:** There is a rank α such that an accessible functor preserves β-presentables for every β sharply larger than α. Arbitrary sufficiently large regular cardinals cannot replace this condition.

**Check and its limit:** F(X)=X^N on Set preserves aleph1-filtered colimits. For arbitrarily large singular λ with cf(λ)=omega, a set X of sizeλ is λ^+-presentable but |X^N|=λ^omega>λ by König, so F(X) is not λ^+-presentable. The counterexample uses ordinary regular presentability ranks λ^+.

**Literature match:** Lack–Tendas Corollary2.6 p5 is the exact repaired theorem, following Adámek–Rosický Theorem2.19. The sharply-larger restriction is mathematically essential.

**References:** LackTendas2023.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-066.

## C-SA23-groupes-067

**Source:** sources/texts/codex/K161-2-04_transcription.tex:171–184;219–263.

**Literal excerpt:**

```tex
b) Un foncteur covariant \deleted{\unsure{en}} $C\to(\mathrm{Ens})$ est proreprésentable \inserted{(resp.)} \deleted{ssi $\unsure{\Pi|\pi}$ est accessible et} \inserted{ssi il est} exact à gauche (resp. commute aux petites $\varprojlim$) et \uline{accessible}
```

**Precise statement or question:** On a locally presentable category, a small-colimit-to-limit presheaf is representable; an accessible limit-preserving functor between locally presentable categories is a right adjoint. Accessible finite-limit-preserving Set-valued functors are prorepresentable. Topoi and Grothendieck abelian categories are locally presentable, with all the generator/exactness hypotheses retained.

**Check and its limit:** Accessibility supplies a solution set. The adjoint functor theorem then yields the adjoint, and evaluation at the singleton gives representability for a Set-valued right adjoint. A lex Set functor is a filtered colimit of representables via its cofiltered category of elements, with accessibility supplying smallness. A merely accessible source need not have all limits; a generator plus exact filtered colimits without the other axioms is not the theorem.

**Literature match:** Riehl Theorem4.7.10 gives the exact solution-set/SAFT package; Makkai–Pitts and Lack–Power supply locally presentable models. Beke, Sheafifiable Homotopy Model Categories, Proposition3.10 treats Grothendieck abelian categories.

**References:** RiehlContextOnline, LackPower2009, Beke2000.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-068

**Source:** sources/texts/codex/K161-2-04_transcription.tex:394–414;427–445.

**Literal excerpt:**

```tex
\margin{Peut-on avoir $\operatorname{Fil}^{\pi'}(E)\ne E_{\pi'}$ ?}
```

**Precise statement or question:** For κ=aleph1 and C=countable sets, Ind_κ(C)=Set. At singular λ>aleph0 of countable cofinality, some λ^+-presentable sets have no κ-directed presentation by C with a cofinal index set of size≤λ. Thus the unqualified Fil^λ equality fails.

**Check and its limit:** Let |X|=λ. Such a presentation would yield a cofinal family of≤λ countable subsets of X, since countably many representing stages have a common upper bound. Enumerate this family and choose λ_n↑λ with λ_n<λ. Pick x_n outside the union of the firstλ_n members. The countable set{x_n} is contained in no listed member, contradiction. X is λ^+-presentable in Set.

**Literature match:** Lack–Tendas Theorem2.3/Corollary2.5 gives the positive statement at sharply larger ranks. The diagonal counterexample answers the manuscript’s unrestricted question in ZFC; no cardinal-arithmetic assumption is hidden.

**References:** LackTendas2023.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-068.

## C-SA23-groupes-069

**Source:** sources/texts/codex/K161-2-04_transcription.tex:427–460.

**Literal excerpt:**

```tex
Enfin, si $X\in\operatorname{Fil}^{\pi''}$, on peut prendre \deleted{\unsure{$C$}} $I$ tel que $\operatorname{Card} I\leq\pi''$, donc $\operatorname{Card} J\leq{\pi''}^{\pi'}$.
```

**Precise statement or question:** Ordinary filtered subdiagrams cannot replace κ-directed ones when κ>omega. The cardinal estimate |J|≤(π′′)^{π′} does not imply |J|≤π′′ without an additional bound. The retract argument remains valid for bounded ordinary filtered presentations in a cocomplete finite-colimit-generated setting.

**Check and its limit:** Closing a set of stages under κ-small upper bounds may increase its cardinal to a power. C068 shows the increase cannot always be avoided. A retract of an object is an ordinary filtered colimit of its repeated idempotent endomorphism; this countable chain splits the retract but is not generally κ-directed for uncountableκ.

**Literature match:** Lack–Tendas2.3–2.6 identifies exactly where sharp cardinal bounds repair the argument. The idempotent-chain construction is an independent elementary proof with its filteredness limit stated.

**References:** LackTendas2023.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-070

**Source:** sources/texts/codex/K161-2-04_transcription.tex:267–324.

**Literal excerpt:**

```tex
p.ex. $C$ stable par $\varprojlim$ finies et $\varphi$ exact à g
```

**Precise statement or question:** A small dense C in cocomplete locally small E gives a fully faithful nerve with a left adjoint. But C finitely complete and C→E lex does not make C/X filtered; finite colimits preserved in E give that variance. Essential surjectivity of the colimit extension alone is not density.

**Check and its limit:** Take C={1}→Set: it is lex and dense, but C/2 is discrete with two objects, hence not filtered. For the essential-surjectivity warning, C a discrete set of two copies of1 maps to Set; its colimit extension Set²→Set is coproduct and essentially surjective, while the nerve X↦(X,X) is not full. Density itself follows from the canonical counit criterion.

**Literature match:** Kelly §5.1/Theorem5.56 gives the exact density theorem. The two finite counterexamples separate the extra assertions and also explain why the earlier 161-1 cofinality shortcut cannot be reused.

**References:** Kelly1982.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-070.

## C-SA23-groupes-071

**Source:** sources/texts/codex/K161-2-04_transcription.tex:255–263;345–359.

**Literal excerpt:**

```tex
les seuls objets accessibles sont les ensembles ponctuels !
```

**Precise statement or question:** The only presentable object of Set^op at any regular rank is a singleton; hence Set^op is not accessible. Ab^op is also not accessible. A strict cogenerator is not automatically a small codense subcategory.

**Check and its limit:** For nonempty X with at least2 elements, a map2^S→X detecting the all-zero tuple cannot factor through any<κ coordinate projection. For X=empty, use the κ-cofiltered system Inj(J,κ), J⊂κ^+, |J|<κ: all stages nonempty but the limit empty. Thus Hom(-,X) fails the required preservation; singleton Hom is constant1. For Ab^op use the established theorem that an accessible opposite of a locally presentable category forces a small preorder; Ab is not one.

**Literature match:** Beke2000 Remark3.3 explicitly invokes Adámek–Rosický1.64 for the opposite-category theorem. The complete Set^op proof, including the empty-object edge case, is supplied here.

**References:** Beke2000, ColimitDense2019.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-072

**Source:** sources/texts/codex/K161-2-04_transcription.tex:345–359.

**Literal excerpt:**

```tex
Une catégorie satisfaisant les conditions a) est-elle \uline{accessible}, i.e. ses éléments sont ils accessibles ?
```

**Precise statement or question:** The statement that every cocomplete bounded category is locally presentable is equivalent to Vopěnka’s principle. Set^op is bounded exactly under the set-theoretic condition(M): some λ has no nonprincipal λ-complete ultrafilter. It is not an unconditional bounded counterexample.

**Check and its limit:** Cocomplete accessible means locally presentable, so the exact question is the bounded-cocomplete statement. The 2019 source states its equivalence with VP and separately proves the Set^op criterion. It also corrects the older false assertion that colimit-density alone implies boundedness under VP; these two notions cannot be exchanged.

**Literature match:** Rosický–Trnková–Adámek1990 is the backward reference; Adámek et al.2019 Introductionp448 and Corollary3.5p452 explicitly state the equivalence and the correction. Adámek–Rosický1996 gives the related equalizer/connected-limit version under VP.

**References:** ColimitDense2019, AdamekRosicky1996.

**Recorded event types:** targeted proof check.

## C-SA23-groupes-073

**Source:** sources/texts/codex/K161-2-04_transcription.tex:180–184;204–217.

**Literal excerpt:**

```tex
\uline{Th.} a) Soit $E\to B$ une catégorie fibrée, avec $B$ équiv. à une \deleted{\unsure{petit|petite}} \inserted{petite} catégorie, les catégories fibres accessibles, les foncteurs changement de base accessibles. Alors $\varprojlim E/B$ et $\underline{\operatorname{Hom}}_B(B,E)$ sont accessibles. En particulier, si $C$ accessible et $I$ équiv. à une petite catégorie, $\underline{\operatorname{Hom}}(I,C)$ est accessible, ainsi que la sous-catégorie pleine des foncteurs qui transforment tte flèche en un iso.

\margin{9.22}

b) Même hyp. sur $E,B$. Alors $\varinjlim E/B^\circ$ est accessible.
```

**Precise statement or question:** The 2-category of accessible categories and accessible functors admits flexible limits, pseudolimits and bilimits. Ordinary strict equalizers are a different matter. Pointwise colimits of accessible functors are accessible at a common rank; pointwise limits need a sufficiently suitable rank and target exactness. The blanket bicolimit claim is not settled by the cited limit theorem.

**Check and its limit:** Choose one common regular/sharply enlarged rank for the small diagram. Products, inserters, equifiers and the other flexible constructions are accessible; this builds bilimits. Commutation of the relevant small limits with directed colimits at that rank gives the functor-category assertion. Accessibility is not self-dual, so no bicolimit result follows by reversing arrows.

**Literature match:** Lack–Tendas Theorem5.5p33 proves the exact limit theorem and cites Makkai–Paré5.1.6; Bird–Kelly–Power–Street1989 is the earlier flexible-limit reference. Searches for arbitrary bicolimits in Acc did not locate an exact unconditional theorem matching the sheet, so that component remains precisely delimited.

**References:** LackTendas2023, BirdKellyPowerStreet1989.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-074

**Source:** sources/texts/codex/K161-2-04_transcription.tex:361–369.

**Literal excerpt:**

```tex
À prouver : Si $C,C'$ accessibles, alors la ss-catégorie de $\underline{\operatorname{Hom}}(C^\circ\times C'^\circ,\mathrm{Ens})$ \inserted{$\underline{\operatorname{Hom}}^*(C^\circ\times C'^\circ,\mathrm{Ens})$} formée des bifoncteurs qui commutent aux $\varprojlim$ \unsure{quelc.|quelq.|petites} en chaque argument, $(\simeq\underline{\operatorname{Hom}}'(C^\circ,C')\simeq\underline{\operatorname{Hom}}'(C'^\circ,C)$, où les $\underline{\operatorname{Hom}}'$ dénotent les foncteurs qui commutent aux petites $\varprojlim$) est accessible, et des foncteurs commutant aux $\varprojlim$ $C_1\mathbin{-}C,C'_1\mathbin{-}C'$ définissent un foncteur accessible entre les $\underline{\operatorname{Hom}}^*$. Or il est assez clair que plus généralement, si $D$ \inserted{variable} stable par petites $\varprojlim$ (et pour les foncteurs qui y commutent\ldots cf \inserted{note} $\Delta$)
```

**Precise statement or question:** For locally presentable categories, accessible limit-preserving structure-forgetting functors have left adjoints, and there is a tensor product representing separately cocontinuous bifunctors. A formulation with arbitrary accessible categories and unspecified limits does not follow.

**Check and its limit:** At a common regular rank, use the small presentable subcategories and their bounded cocompletion/tensor universal properties; Ind completion gives the locally presentable tensor. Caviglia–Horel§2 gives the explicit category of separately small-limit-preserving functors and its continuous-functor description. The right-adjoint/continuous formulation is its adjoint dual and needs consistent variance. These hypotheses are stronger than mere accessibility.

**Literature match:** Kelly§6.5, formulas(6.24)–(6.28), proves the small bounded-cocomplete tensor construction. Caviglia–Horel§2, pp4–5, gives the exact unenriched locally presentable version. The backward Bird1984 thesis lead was retrieved only as an indexed passage; both full-PDF routes failed503/502, so no uninspected Bird proof is used.

**References:** CavigliaHorel, Kelly1982.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-075

**Source:** sources/texts/codex/K161-2-05_transcription.tex:1–83; sources/texts/codex/K161-2-07_transcription.tex:394–425.

**Literal excerpt:**

```tex
Alors les $\varprojlim$ de type $\delta$ existent dans $T(C)$, et se calculent dans $\underline{\mathrm{Hom}}_{\Delta}(R,C)$ ``\uline{argument} par \uline{argument}'' (en d'autres termes, les foncteurs $r_{C}:T(C)\longrightarrow C$ associés aux \inserted{$T$-}constructions commutent aux $\varprojlim$ de type $\delta$)

De plus, pour un hom de théories \unsure{repr.} $T\longrightarrow T'$, $T(C)\longrightarrow T'(C)$ commute aux $\varprojlim$ de type $d$. Id pour $C\longrightarrow C'$, $C'$ satisfaisant les $\unsure{\text{mêmes}|\leftrightarrows}$ hyp. que $C$, $T(C)\longrightarrow T(C')$ commute aux $\varprojlim$ de type $d$.
```

**Precise statement or question:** For a doctrine prescribing specified limits and colimits, a J-limit of models is pointwise when it exists in the target and commutes there with the prescribed colimits; limits commute with the prescribed limits. Change of target preserves this construction when the target functor preserves the J-limit. The dual statement exchanges limits and colimits.

**Check and its limit:** For each prescribed cone, interchange the two limits. For a prescribed cocone use the stated interchange isomorphism. The cone universality is inherited from the functor category, since the model subcategory is full. Evaluation and precomposition then preserve these pointwise limits. A target functor with no preservation condition cannot be used in that last step.

**Literature match:** Lack–Tendas Proposition5.12 and Corollaries5.13–5.14 give the model-category limit framework; the elementary interchange proof here makes the exact target hypotheses explicit. The later manuscript formulation is the corrected one.

**References:** LackTendas2023.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-076

**Source:** sources/texts/codex/K161-2-05_transcription.tex:42–83; sources/texts/codex/K161-2-07_transcription.tex:423–554; sources/texts/codex/K161-2-05_transcription.tex:15–39.

**Literal excerpt:**

```tex
Si $C\longrightarrow C'$ dans $\Delta$ est pl. fidèle (resp. fid) alors $T(C)\longrightarrow T(C')$ l'est aussi (pour $T$ 2-repr.).
```

**Precise statement or question:** T(Fun(J,C))≃Fun(J,T(C)) for pointwise doctrine operations. A faithful, respectively fully faithful, operation-preserving C→D induces the same property on models. If a specified basis generates the representing category by the prescribed operations, the model square over that basis is a 2-pullback for a fully faithful C→D.

**Check and its limit:** Currying identifies the first two categories and all natural transformations. For the last assertion lift the basis objects and their structure arrows through the fully faithful embedding, then extend along the specified operations; their universal properties give unique coherent lifts. Mere determination of transformations on a faithful basis does not establish the generation hypothesis; C101 separates them.

**Literature match:** Kelly5.35 supplies the free-completion universal property; Lack–Tendas5.12–5.14 covers the bounded sketch setting. The lift argument is independently checked and is explicitly conditional on genuine operation generation.

**References:** Kelly1982, LackTendas2023.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-077

**Source:** sources/texts/codex/K161-2-05_transcription.tex:45–83; sources/texts/codex/K161-2-07_transcription.tex:490–575.

**Literal excerpt:**

```tex
est pl. fidèle, et identifie $T_{\deleted{R}}(C)$ à la sous-catégorie str. pleine de $\underline{\mathrm{Hom}}_{\mathrm{Cat}}(C^{\circ},S)$ formée des $\varphi:C^{\circ}\longrightarrow S$ tels que, pour tte \uline{construction} $r\in R$, \inserted{d'où $\widetilde r:S\longrightarrow(\mathrm{Ens})$,} $\widetilde r\circ\varphi:C^{\circ}\longrightarrow(\mathrm{Ens})$ \unsure{sont|soit} repr. Et il suffit d'exiger cette condition pour les $r_i$ qui $\Delta$-\uline{engendrent} (i.e. on a un diagramme 2-cartésien
```

**Precise statement or question:** For a small limits-only theory R, S=Hom_lambda(R,Set), and a locally small lambda-complete C, models R→C identify with functors C^op→S whose construction presheaves are representable. A genuinely operation-generating basis suffices. The evaluation functor R→Fun(S,Set) is fully faithful.

**Check and its limit:** Yoneda C→PSh(C) preserves limits; currying gives Hom_lambda(R,PSh(C))≃Fun(C^op,S). A model lands in the fully faithful representable image exactly when its component presheaves are representable. Closure of representables under the designated limits reduces this to a generating basis. Evaluation at r is represented in S by Hom_R(r,-), which preserves all existing limits; two applications of Yoneda give Nat(ev_r,ev_s)≃Hom_R(r,s).

**Literature match:** Kelly5.35 and ordinary Yoneda identify the exact completion mechanism. This statement retains the selected constructions; it is not an intrinsic recovery from S alone. The canceled early paragraph is not treated as a second independent theorem.

**References:** Kelly1982, RiehlContextOnline.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-078

**Source:** sources/texts/codex/K161-2-05_transcription.tex:85–103.

**Literal excerpt:**

```tex
Les théories Algébriques sont exactement celles qui sont représentées par des \uline{petites} catégories.
```

**Precise statement or question:** A no-operation small presentation represents a small category. Inverting all arrows gives its groupoid completion; identifying parallel arrows gives its reachability preorder; further identifying mutually comparable objects gives its poset reflection.

**Check and its limit:** Formal words of arrows and inverses, modulo compositions and inverse relations, have the groupoid universal property. The preorder has one arrow exactly when a path exists. Its antisymmetrization identifies x and y when paths exist both ways. A preorder need not already be a poset, so those last two constructions must remain distinct.

**Literature match:** Stacks04VB gives the universal localization framework; the preorder and poset quotients are checked directly. This is an elementary settled construction, not a new priority assertion about the undated sheet.

**References:** StacksLocalization.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-079

**Source:** sources/texts/codex/K161-2-05_transcription.tex:104–115.

**Literal excerpt:**

```tex
donc $I$ a la $\Delta$-enveloppe $\widetilde I=\underline{\mathrm{Hom}}(I,\unsure{C|e})^\circ$ (qui est l'opposé d'un topos). Notons que $I\longrightarrow\widetilde I$ définit les objets de $I$ comme famille \uline{cogénératrice} (donc $I^\circ\longrightarrow\widetilde I^\circ$ comme famille génératrice).
```

**Precise statement or question:** For small I, its free completion under all small limits is Fun(I,Set)^op, in an enlarged universe. Continuous functors out of it correspond to arbitrary functors I→C into a complete target.

**Check and its limit:** Dualize the free cocompletion PSh(I^op)=Fun(I,Set): an object is a small colimit of representables, so the dual extension is the corresponding limit in C. Natural transformations extend uniquely by these universal properties. The completion is generally not small in the original universe.

**Literature match:** Kelly Theorem5.35 and the all-indexing-types example immediately following it, pp99–100, give the exact free cocompletion theorem. The target-variable ambiguity in the displayed manuscript formula is separately registered.

**References:** Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-080

**Source:** sources/texts/codex/K161-2-05_transcription.tex:116–149.

**Literal excerpt:**

```tex
Mais alors on voit tout de suite que les produits de $C$ sont des produits de $C\Sigma^{-1}$. OK ! […] \margin{Mais il faut \deleted{Si $C$ est} vérifier que la catégorie obtenue est une $\mathcal U$-catégorie.}
```

**Precise statement or question:** A right-fraction localization preserves existing finite limits. If the denominator class is additionally closed under the relevant products, the same roof argument preserves those products. Local smallness of the saturated localization and preservation of the manuscript’s strict-cogenerator condition require separate hypotheses; the proposed transitivity is explicitly withdrawn.

**Check and its limit:** Pullbacks put finitely many roofs over a common denominator and prove finite-limit universality. For an arbitrary product, the product of the component denominators is a denominator by hypothesis; this gives the required common roof. These arguments do not bound the set of all roof classes for a large category. Nor does a Cat colimit by itself establish strict cogeneration in a later doctrine completion.

**Literature match:** Stacks04VB Lemmas4.27.9 and4.27.17 prove the exact finite-limit fraction result, following Gabriel–ZismanI.3.1. Kelly5.35 gives a bounded small completion, not the unbounded strict-cogenerator theorem. The remaining local-smallness and generation issue is therefore retained as a precise gap.

**References:** StacksLocalization, Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-081

**Source:** sources/texts/codex/K161-2-05_transcription.tex:132–184.

**Literal excerpt:**

```tex
Les théories algébriques pour $\Delta$ sont celles qui sont 2-représentées par des $R\in\mathrm{Ob}\,\Delta$ admettant des \uline{petites familles \inserted{str.} cogénératrices}.
```

**Precise statement or question:** The asserted conclusions hold for a complete locally small source with a small coseparating family and intersections of every collection of subobjects of a fixed object. Well-poweredness plus completeness is one sufficient way to obtain the intersection condition. A bare small cogenerator is not the full stated theorem.

**Check and its limit:** The special adjoint functor theorem constructs initial objects in each comma category by intersecting subobjects of a product of cogenerators. For F:R→Set continuous, its left adjoint L then gives F(X)≃Hom_R(L1,X), establishing representability. With this package, the all-limit reconstruction and its contravariant adjoint dictionary follow. Without it, the changing manuscript cogenerator terminology does not supply the missing solution-set argument.

**Literature match:** Riehl Theorem4.7.10 and Lemma4.7.11 pp178–179 were read with their proofs; their exact intersection hypothesis is retained. The manuscript’s broader wording is not identified with this theorem by terminology alone.

**References:** RiehlContextOnline.

**Recorded event types:** targeted proof check.

## C-SA23-groupes-082

**Source:** sources/texts/codex/K161-2-05_transcription.tex:186–253; sources/texts/codex/K161-2-04_transcription.tex:476–479.

**Literal excerpt:**

```tex
\margin{Pb 1 et Pb $1'$ Cela marche pour \uline{tout} ens. $d'$ de petits diagrammes (pas néc. finis)}
```

**Precise statement or question:** For a small category and a small set of small limit shapes, the free completion is small and obtained by a regular-bounded transfinite closure. Yoneda gives the fully faithful embedding into Hom_lambda(C,Set)^op when C has the designated limits. Any further localization construction must retain local-smallness and preservation hypotheses.

**Check and its limit:** Dualize Kelly5.35. At a regular ordinal above the sizes of all specified shapes, every diagram in the union has appeared before that stage, so closure stabilizes. The evaluation embedding is fully faithful because covariant representables are models and detect natural transformations. One-step closure works for the family of all finite products but is not valid for arbitrary shape families; Kelly gives explicit multi-stage examples.

**Literature match:** Kelly5.35pp99–100 supplies the exact smallness and free-completion result, including the warning that one closure step need not suffice. This answers the bounded-shape part and isolates the large localization issue already recorded in C080.

**References:** Kelly1982.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-083

**Source:** sources/texts/codex/K161-2-05_transcription.tex:255–306.

**Literal excerpt:**

```tex
Donc $\Sigma$ se réconstitue à partir de $S$ comme l'\deleted{\unsure{ens. des|ens. des ob.}} sous-catégorie (str.) pleine des objets ``de présentation finie'' !
```

**Precise statement or question:** For small finitely complete R, Lex(R,Set)≃Ind(R^op), and its finitely presentable subcategory is equivalent to R^op. This extends to Gabriel–Ulmer duality with filtered-colimit-preserving right adjoints on the model side.

**Check and its limit:** Every lex functor is a filtered colimit of covariant representables. A finitely presentable object is a retract of a representable; R is idempotent complete because it has equalizers, so that retract is representable. This proves the recovery and identifies the variance. It uses finite colimits on the dual small subcategory, not arbitrary small colimits.

**Literature match:** Lack–Power2009 Theorem8p270 states the exact biequivalence. Kelly5.10 supplies the filtered-colimit/left-exact description; Makkai–Pitts1987 provides related intrinsic criteria. The original Gabriel–Ulmer monograph is a backward reference, not a claimed first-edition proof inspection.

**References:** LackPower2009, Kelly1982, MakkaiPitts1987.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-084

**Source:** sources/texts/codex/K161-2-05_transcription.tex:332–336; sources/texts/codex/K161-2-06_transcription.tex:379.

**Literal excerpt:**

```tex
transforme objets de P.F. en objets de P.F. [ On pourrait les appeler les morphismes de présent. finie, ou cohérents, de théories \ldots ].
```

**Precise statement or question:** For locally finitely presentable S,S′ and L⊣U:S′→S, U preserves filtered colimits exactly when L sends finitely presentable objects of S to finitely presentable objects of S′. The manuscript first puts the latter condition on U and later moves it to its left adjoint.

**Check and its limit:** For a finitely presentable a, Hom(L a,-)≃Hom(a,U-); commutation with filtered colimits gives the forward implication. Conversely the finitely presentable a form a strong generator, so these Hom comparisons detect that U commutes with filtered colimits. U:Groups→Set does preserve filtered colimits but sends the finitely presentable group Z to an infinite, non-finitely-presentable set, refuting the first wording.

**Literature match:** Lack–Power Theorem8 uses precisely filtered-colimit-preserving right adjoints. The adjoint equivalence above is independently proved and locates the manuscript’s own correction exactly.

**References:** LackPower2009.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-085

**Source:** sources/texts/codex/K161-2-05_transcription.tex:339–340.

**Literal excerpt:**

```tex
Comment trouver \inserted{toutes} les $\Sigma$ qui marchent
```

**Precise statement or question:** A category of models determines the finite-product presentation only up to the appropriate Morita/Cauchy completion; the selected finite-coproduct generators remain presentation data. Strongly finitely presentable projectives, not all finitely presentable objects, are relevant for algebraic theories.

**Check and its limit:** FinSet and its full subcategory of even finite sets both have finite coproducts and the same idempotent completion. Every finite set is a retract of an even finite set. Their opposite finite-product theories have equivalent Set-model categories because idempotents split in Set, but the presentation categories are not equivalent.

**Literature match:** Adámek–Lawvere–Rosický2003p36 gives this exact example; Lemma2.1, Corollary2.4, Proposition2.6 and Theorem4.1 give the projective and Cauchy-completion recovery. This settles the literal uniqueness question and supplies the precise classification framework.

**References:** AdamekLawvereRosicky2003.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-086

**Source:** sources/texts/codex/K161-2-06_transcription.tex:40–45.

**Literal excerpt:**

```tex
\textcircled{$6'$} Topos essentiels $(\simeq\widehat C$, i.e. ayant assez de pts essentiels, i.e. ayant les propriétés \inserted{d'exactitude} pour $\varinjlim$ et $\varprojlim$ de la cat. des ens)

Morphismes essentiels de topos.

Je m'attends à des ennuis \inserted{(de sortie de l'Univers)} \uline{au moins} avec \textcircled{6} et \textcircled{$6'$}
```

**Precise statement or question:** A Grothendieck topos has a conservative family of essential points iff it is equivalent to a presheaf topos. Essential points correspond to nonempty connected projectives; for PSh(C) their category is the Karoubi completion of C. An essential geometric morphism is characterized by its inverse image preserving all small limits, equivalently products.

**Check and its limit:** A point is essential iff its inverse image is represented; preservation of coproducts and epimorphisms makes the representing object connected nonempty projective. A generating family of such objects has trivial induced topology, yielding a presheaf presentation. Retracts of representables give exactly the essential points of PSh(C). This does not turn the phrase all exactness properties of Set into a complete independent axiom system.

**Literature match:** SGA4I, ExposéIV Exercise7.6(a–g), printedpp414–417, is the exact published statement and explicitly credits the presheaf criterion to J.-E. Roos. The retyped text was checked here; the original facsimile was separately checked in the spaces work.

**References:** SGA4I1972.

**Recorded event types:** targeted proof check.

## C-SA23-groupes-087

**Source:** sources/texts/codex/K161-2-06_transcription.tex:47–173; sources/texts/codex/K161-2-07_transcription.tex:95–229.

**Literal excerpt:**

```tex
\margin{$\begin{aligned}\rho(T)&=B_T\quad\text{cat. des constructions sur }T\\&=\underline{\mathrm{Hom}}(T,\tau)\end{aligned}$}
```

**Precise statement or question:** With pseudonatural transformations and modifications, the two-Yoneda equivalence PsNat(Hom_Delta(R,-),T)≃T(R) gives rho(sigma R)≃R. Evaluation has direction T→sigma(rho T). Variance in R is contravariant, and the claimed category of constructions must lie in the chosen universe.

**Check and its limit:** Evaluate a transformation at id_R. Its inverse sends x∈T(R) to the transformation f↦T(f)(x); pseudofunctor coherence gives the inverse equivalences and the modification correspondence. Applied to the underlying-category pseudofunctor tau this recovers R. Evaluation sends a model to the functor evaluating each construction on that model, hence has the stated direction.

**Literature match:** Vistoli2007§3.6.2pp62–63 gives the fibred two-Yoneda proof; Kelly§2.4 gives the enriched analogue. The pseudofunctor version is independently proved by the displayed identity evaluation, with all size assumptions exposed.

**References:** VistoliDescent, Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-088

**Source:** sources/texts/codex/K161-2-06_transcription.tex:80–88;130–173;295–314; sources/texts/codex/K161-2-07_transcription.tex:130–163;278–350; sources/texts/codex/K161-2-04_transcription.tex:466–479.

**Literal excerpt:**

```tex
\boxed{T\longrightarrow\sigma\rho(T)}
\]

\deleted{C'est le morphisme universel de $T$ dans une théorie 2-représentable, car}
```

**Precise statement or question:** If rho(T)=PsNat(T,tau) is a locally small object of the chosen doctrine and evaluation is doctrine-exact, currying gives PsNat(T,sigma R)≃Hom_Delta(R,rho T). Those assumptions do not follow from the definition of an arbitrary large type. Small bounded sketches and specific finitary exactness doctrines have established free constructions.

**Check and its limit:** Currying a transformation T→Hom_Delta(R,-) gives a functor R→PsNat(T,tau), and the exactness requirement is exactly what makes it a Delta-functor. This proves the conditional universal property, not that rho(T) is small or that T≃sigma rho(T). The manuscript’s large transfinite argument has no demonstrated stopping ordinal.

**Literature match:** Kelly5.35 handles small bounded completion. Di Liberti–Osmond2025§6.3 and Theorem6.4.5/Corollary6.4.6 establish bipresentability for Lex and specified finitary exactness doctrines. They do not establish the unbounded arbitrary-Delta claim or remove its local-smallness question.

**References:** Kelly1982, DiLibertiOsmond2025.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-089

**Source:** sources/texts/codex/K161-2-06_transcription.tex:121–166.

**Literal excerpt:**

```tex
Construction des 2-limites dans $(\mathrm{Cat})$ : elle est faite dans SGA 4 \uline{VI} en prenant la catégorie totale de la catégorie cofibrée envisagée et en rendant inversibles les morphismes cartésiens.
```

**Precise statement or question:** For F:I→Cat, its pseudocolimit is the localization of the Grothendieck opfibration at its cocartesian arrows. A bicolimit in a doctrine can then be obtained by its free envelope and by inverting the required comparison arrows, provided those constructions exist with the stipulated size.

**Check and its limit:** A functor from the total category specifies the component functors and transition comparisons of a lax cocone. Sending cocartesian arrows to isomorphisms makes those comparisons invertible, which is precisely a pseudococone. The localization universal property therefore proves the pseudocolimit formula. Inverting limit-comparison maps subsequently enforces exactness only when the comparisons form admissible data.

**Literature match:** Di Liberti–Osmond2025§1.2.16 gives the exact localization formula; Lemma6.3.2 proves the filtered lex case by computing finite limits at a common stage. The manuscript’s word cartesian is retained as a variance alarm, not silently replaced.

**References:** DiLibertiOsmond2025, StacksLocalization.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-090

**Source:** sources/texts/codex/K161-2-06_transcription.tex:175–273; sources/texts/codex/K161-2-07_transcription.tex:178–315; sources/texts/codex/K161-2-04_transcription.tex:470–472;483–485;492–509.

**Literal excerpt:**

```tex
\margin{il faut aussi prévoir les axiomes du type ``flèches rendues égales'' (en réalité, \unsure{un des|cas des|pas des} précédents si on suppose p.ex. $d'=d''=\varnothing$)}
```

**Precise statement or question:** Small theories can be presented by objects, arrows and relations, together with the prescribed operation comparisons. Equality of parallel arrows can be forced by inverting their equalizer inclusion when that equalizer exists. Independent products of represented types correspond to coproducts of classifiers; products over a common basis correspond to amalgamated coproducts.

**Check and its limit:** For f,g:X⇒Y, their equalizer e:E→X becomes invertible exactly when the preserved f,g become equal. Without equalizers, merely requiring f and g individually invertible does not impose f=g; one needs a relation quotient. Functors out of an ordinary or amalgamated classifier coproduct encode exactly independent or basis-compatible model pairs. A small category is presented using its complete small arrow set and composition relations.

**Literature match:** Kelly5.35 gives the completion component; Stacks04VB gives universal inversion; Di Liberti–Osmond6.3–6.4 gives the finitary doctrine setting. These match the small presentation mechanism and leave the author’s large-family caveat intact.

**References:** Kelly1982, StacksLocalization, DiLibertiOsmond2025.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-091

**Source:** sources/texts/codex/K161-2-06_transcription.tex:295–314; sources/texts/codex/K161-2-07_transcription.tex:309–350; sources/texts/codex/K161-2-04_transcription.tex:476–485;490–503.

**Literal excerpt:**

```tex
Alors pour $\alpha$ assez grand \inserted{(dans l'univers $\mathcal U$)}, on a $R_\alpha\xrightarrow{\simeq}R$.
```

**Precise statement or question:** A small classifier has a small presentation. For a large locally small classifier, determination of transformations on a small basis alone does not prove operation generation or a uniform small stopping bound. The particular transfinite stabilization proposed on the sheet remains unproved at its stated level of generality.

**Check and its limit:** C101 gives finite counterexamples to the proposed implication from a faithful basis to operation generation. Even after strengthening to generation, an unbounded family of shapes can evade a fixed regular closure ordinal. The small bounded theorem C082 supplies a valid replacement with an explicit bound, but cannot justify the unrestricted argument.

**Literature match:** Searches through Kelly5.35 and modern doctrine bipresentability (Di Liberti–Osmond6.3–6.4) found the bounded/small results, not a theorem with these unrestricted quantifiers. This is a delimited residual formulation, not an assertion that no broader theorem exists.

**References:** Kelly1982, DiLibertiOsmond2025.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-092

**Source:** sources/texts/codex/K161-2-06_transcription.tex:300–314.

**Literal excerpt:**

```tex
cel implique que les foncteurs $R_\alpha$ sont \deleted{pl. fidèl} \uline{fidèles}, donc les $R_\alpha$ sont des sous-catégories.
```

**Precise statement or question:** A conservative functor preserving equalizers is faithful. It need not be full.

**Check and its limit:** If Ff=Fg, the image of the equalizer of f,g is an isomorphism, so conservativity makes the original equalizer an isomorphism and f=g. The forgetful functor Groups→Set preserves finite limits and reflects isomorphisms but is not full: many underlying-set maps do not preserve multiplication.

**Literature match:** Riehl’s adjunction/limit framework supports the exact interpretation; the two-line proof and explicit counterexample are independently checked. This validates the retained claim while preserving the canceled strengthening.

**References:** RiehlContextOnline.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-093

**Source:** sources/texts/codex/K161-2-06_transcription.tex:316–338.

**Literal excerpt:**

```tex
d) Plus précisément, $S_0$ est la catégorie stable par $\varprojlim$ finies \uline{enveloppante} de la $\underset{\leftarrow}{\lambda}$-catégorie \deleted{\unsure{S|\Sigma}}$\Sigma$, et $S$ est la $\varinjlim$-catégorie enveloppante de la $\varinjlim_{\unsure{0|\circ}}$-catégorie $S_0$.
```

**Precise statement or question:** A small finite-limit sketch has a locally finitely presentable model category. Its finitely presentable objects are closed under finite colimits and retracts; they need not be closed under finite limits. In the manuscript setting with actual designated limits, the representable models generate the finite-colimit closure.

**Check and its limit:** Take R=k⊕V with V a countably infinite-dimensional square-zero ideal. Multiplication by a nonzero x∈V is an endomorphism R→R between finitely presented modules; its kernel is V, which is not finitely generated because R acts on V through k. Thus the kernel is not finitely presentable. Finite colimits and retracts of finitely presentable objects are finitely presentable by the Hom/filtered-colimit criterion.

**Literature match:** Lack–Tendas Theorem4.4 and the model results5.12–5.14 give the sketch theorem; Lack–Power8 gives its finite-limit completion formulation. The noncoherent-ring example independently refutes the wrong-variance closure at line337.

**References:** LackTendas2023, LackPower2009.

**Executed checks:** kernels of finite-presentable modules need not be finite-presentable. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-093; computation or formal certificate.

## C-SA23-groupes-094

**Source:** sources/texts/codex/K161-2-06_transcription.tex:341–405.

**Literal excerpt:**

```tex
& $\mathscr C=\overline{\underline{\mathrm{Hom}}_{\lambda}}(R,\mathrm{Ens})=T(\mathrm{Ens})$ $\left\{=\underline{\mathrm{Hom}}_{\lambda^\circ}(S^\circ,\mathrm{Ens})\right.$ ($=\mathrm{Ind}(S)$ si $\lambda_1=$ tous les \inserted{diagrammes finis}) $\mathscr C=\underline{\mathrm{Pt}}(B)^\circ$ \par $\cup\hspace{1.4em}\cup$\par $S=\underline{\mathrm{Ptess}}(B)^\circ$
& $\sim$\par $B=\widehat R=\underline{\mathrm{Hom}}(S,\mathrm{Ens})$ \deleted{$\unsure{\underline{\mathrm{Hom}}(C,\mathrm{Ens})}$} ($=\underline{\mathrm{Hom}}_{\unsure{\mathrm{fib}|\varprojlim|{}}}(\mathscr C,\mathrm{Ens})$ si $\lambda_1=$ ts les diag finis,\\
\multicolumn{2}{@{}p{.35\linewidth}|}{$=$ sous-catégorie pleine de $\underline{\mathrm{Hom}}(C^\circ,\mathscr C)$ formée des foncteurs $u:C^\circ\mathbin{-}\mathscr C$ dont les composés avec les $\mathrm{Hom}(X,-)$, $X\in\mathrm{Ob}\,S$, sont représentables $=\underline{\mathrm{Homtop}}(C,B)^\circ$ (si $C$ est un topos}
& & \multicolumn{2}{p{.43\linewidth}@{}}{(et \unsure{admet|plutôt} les diagrammes filtrants\ldots) $B=$ topos classifiant pour $T$}\\ \hline
```

**Precise statement or question:** The finite-limit dictionary is valid with the adjoint correction C084. For an arbitrary limits-only doctrine, PSh(R) classifies flat functors, not all operation-preserving functors R→Set; essential points recover Kar(R), not R without idempotent completeness.

**Check and its limit:** For the finite-product theory R=(finite free abelian groups)^op, operation-preserving Set models are all abelian groups. Flat functors are filtered colimits of its representable models, hence filtered colimits of finite free abelian groups and therefore torsion-free by Lazard. Z/2 is a model but not such a point. Separately SGAIV7.6(e) gives the necessary Karoubi completion for essential points.

**Literature match:** SGA4IV7.6(e) and Stacks058C Theorem10.81.4 provide the exact two distinctions. Beke2004 Proposition0.1 and Corollary2.2 warn that equality of Set-model categories alone does not identify the original classifying topos.

**References:** SGA4I1972, StacksFlatness, BekePresheafType.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-094.

## C-SA23-groupes-095

**Source:** sources/texts/codex/K161-2-06_transcription.tex:395–399.

**Literal excerpt:**

```tex
\deleted{foncteur}\inserted{morphisme} fidèle de théories $T'\mathbin{-}T$
& $R\mathbin{-}R'$ $\lambda$-engendre $R'$
& $S\mathbin{-}S'$ $\lambda$-engendre $S'$
& $\mathscr C'\to\mathscr C$ fidèle (2-fid ??) ou $\mathscr C\to\mathscr C'$ induit $S\mathbin{-}S'$ qui \inserted{$\lambda$ engendre $S'$}
& $f^{\inserted{\ast}}_{\deleted{\unsure{\ast}}}:B'\mathbin{-}B^{\unsure{\xi|\prime|{}}}$ est fidèle\\ \hline
```

**Precise statement or question:** Faithfulness of a structure-forgetting morphism on all internal model categories does not imply faithfulness of the induced classifying-topos inverse image. The table’s arrow direction and overwritten adjoint notation also require an ink check.

**Check and its limit:** Forgetting a group structure is faithful in every topos. The corresponding geometric morphism from the group classifier to the object classifier factors through the proper inhabited-object open subtopos, since every group has its unit. The generic object is not forced inhabited (the empty Set model witnesses propriety). Thus the inverse image is not conservative, hence not faithful: a faithful finite-limit/colimit-preserving functor between topoi reflects isomorphisms.

**Literature match:** SGA4IV9.2 gives the open-subtopos interpretation and IV9.1.4 separates full faithfulness from geometric inclusion. The group/inhabitation counterexample is an independent reconstruction; it does not depend on the arbitrary-lambda failure in C094.

**References:** SGA4I1972.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-095.

## C-SA23-groupes-096

**Source:** sources/texts/codex/K161-2-06_transcription.tex:407–423.

**Literal excerpt:**

```tex
$\mathbb Z[t]\longrightarrow\mathbb Z[t,t^{-1}]\times\mathbb Z\simeq\mathbb Z[x,y]/((xy-1)x,(xy-1)y)$ […] La réciproque est vraie, \inserted{et connue}
```

**Precise statement or question:** The commutative von Neumann regular rings, including the zero ring, are exactly rings with a unique quasi-inverse a* satisfying a²a*=a and a(a*)²=a*. Equivalently they invert the represented map Z[t]→Z[t,t^-1]×Z. The displayed product is Z[x,y]/((xy−1)x,(xy−1)y), with t sent to x.

**Check and its limit:** Put e=xy in the quotient. The relations give e²=e, x=ex, y=ey. On the e-component xy=1; on the 1−e-component x=y=0. Chinese remainder decomposition gives Z[t,t^-1]×Z. Uniqueness follows by the standard commuting generalized-inverse calculation, so adjoining the inverse is a property, not additional nonunique structure. Olivier’s reflection T(A) identifies the universal category and inverts exactly the spectrum/residue-field test used here.

**Literature match:** Olivier1967–68 Proposition5 printed6-04 constructs the universal absolutely flat ring with constructible spectrum and unchanged residue fields. Stevenson2014 Proposition3.3/Theorem3.9 and Caramello–Johnstone2009§1 give the explicit quasi-inverse presentation. The orthogonality implication is checked through that reflection, rather than inferred merely from a shared name.

**References:** Olivier1967, Stevenson2014, CaramelloJohnstone2009.

**Executed checks:** quasi-inverse relations and product decomposition. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-097

**Source:** sources/texts/codex/K161-2-06_transcription.tex:422–435;453–462.

**Literal excerpt:**

```tex
de $R$. \deleted{\unsure{Par le foncteur contravariant} \unsure{can.}}\deleted{\inserted{\unsure{identique}}} Or un ss-objet dans $R$ est un \deleted{objet \unsure{quoti}} sous-objet dans (Sch-aff), en effet $\mathbb Z[t,t^{-1}]=\underline{\mathbb Z[x,y]}/(xy-1)$. Donc O.K. \deleted{\unsure{si }\unsure{$\exists$} \unsure{lim}} avec $\varprojlim$ finies

Ceci dit, considérons pour un objet $A$ le morphisme $\deleted{\unsure{e\amalg{}}}A^\ast\longrightarrow A$, où $e$ est l'objet final. On pourra dire que $A$ (\deleted{\unsure{dans}}\inserted{anneau} dans une catégorie \deleted{quelconque}\inserted{avec $\varprojlim$ finies et $\varinjlim$ finies}) est un objet corps si ce morphisme est un isom.
```

**Precise statement or question:** In a finitely complete category, the unit object A× of a commutative ring object is the subobject of A defined by pairs (x,y) with xy=1. In a Grothendieck topos a geometric field is characterized by 1⊔A×→A, zero on the first summand, being an isomorphism.

**Check and its limit:** Uniqueness of y makes the projection from inverse pairs monic, and multiplication and inversion restrict by the ring equations. In a topos the coproduct map is monic exactly when zero and units are disjoint (0≠1), and epic exactly when every element is locally zero or invertible. Both conditions together are equivalent to an isomorphism. Omitting the zero summand would incorrectly require every element, including zero, to be invertible.

**Literature match:** Caramello–Johnstone2009§1 writes the exact coherent field axiom and nontriviality condition. The finite-limit inverse-pair construction and coproduct equivalence are independently re-proved here.

**References:** CaramelloJohnstone2009.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-098

**Source:** sources/texts/codex/K161-2-06_transcription.tex:428–473; sources/texts/codex/K161-2-07_transcription.tex:1–9.

**Literal excerpt:**

```tex
La catégorie (ou \unsure{un} \uline{lieu} quelc.) universelle
pour ceci est la catégorie des faisceaux sur
$R'$ pour la top. de Zariski (= foncteurs
contravariants $R\longrightarrow\mathrm{Ens}$ qui transforment
sommes en produits). Il se trouve que
c'est un topos \deleted{$\unsure{E|\mathcal E|\circledast}$} Le corps universel est
le faisceau structural évident sur ce topos....
```

**Precise statement or question:** The coherent theory of fields is classified by sheaves on the opposite of finitely presented commutative regular rings, with the topology generated by the disjoint zero/invertible decompositions and the empty cover of the zero ring. Its ordinary coherent ring-language formulation is not of presheaf type.

**Check and its limit:** First impose unique quasi-inverses to obtain the presheaf classifier of regular rings. The additional field axioms force the two component quotients R/(a) and R/(aa*−1) to cover and force the zero ring to have an empty cover. These are jointly the decomposition topology. The algebra coproduct in the affine site is not already the coproduct of representable presheaves, which explains the failed shortcut.

**Literature match:** Caramello–Johnstone2009§1pp1–3 gives exactly this site and topology; Beke2004 Corollary2.2 proves no coherent presheaf-type axiomatization of fields exists. The category of fields nevertheless is finitely accessible, so a different infinitary enriched presentation can be of presheaf type; this does not restore the deleted assertion.

**References:** CaramelloJohnstone2009, BekePresheafType.

**Recorded event types:** targeted proof check.

## C-SA23-groupes-099

**Source:** sources/texts/codex/K161-2-06_transcription.tex:471–473.

**Literal excerpt:**

```tex
\margin{$\Big\Vert$}\uline{On trouve}\quad Si $C$ est une catégorie avec $\varprojlim$ finies et $\varinjlim$ quelconques (suffit-il qu'il y ait $\varinjlim$ finies, voire des sommes finies ?) \deleted{alors \unsure{les}} \inserted{et si} les \deleted{``\unsure{morph}'' dans $C$} bimorphismes sont des isom, alors les ``corps'' dans $C$ correspondent aux foncteurs $F:R'\to\unsure{\mathscr C|C}$ qui \deleted{commutent} sont exacts à gauche \inserted{et commutant aux sommes.}
\margin{\unsure{tgrp|trop|tgrps}}
```

**Precise statement or question:** The stated Grothendieck-topos result is valid; the extension to every finitely complete, finitely cocomplete balanced category is not justified by those axioms alone. Stable disjoint coproducts and the relevant effective descent/exactness conditions must be specified before one can assert the same classification.

**Check and its limit:** Balancedness says only that a mono-epi is invertible. It does not imply disjoint, pullback-stable coproducts, nor that a cover relation in a site is interpreted by the intended descent property. Thus the preceding topos argument supplies no proof in the advertised generality. No counterexample to every possible interpretation of the underdefined functor condition is claimed.

**Literature match:** The exact field-site theorem in Caramello–Johnstone§1 and the finitary exactness-doctrine results of Di Liberti–Osmond6.4.5–6.4.6 give positive settings. Searches did not identify the broad balanced-category formulation as a precise theorem; the residual task is to specify its exactness and preservation conditions.

**References:** CaramelloJohnstone2009, DiLibertiOsmond2025.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-100

**Source:** sources/texts/codex/K161-2-07_transcription.tex:13–31.

**Literal excerpt:**

```tex
$\overline{\mathrm M}$ question avec \uline{anneau intègre}. Soit
$O'\subset O$ le sous-objet ``qui opère régulièrement sur $O$'',
$(O'\supset O^*)$ est il définissable par $\varprojlim$ et $\varinjlim$ ? Commute-t'il aux images inverses \unsure{par un morphisme} de topos ?
```

**Precise statement or question:** The internally defined subobject of regular elements of the universal ring in the ring-classifying presheaf topos is its unit subobject. Formation of regular elements in arbitrary rings is therefore not geometric and need not commute with inverse image.

**Check and its limit:** A section a over a finitely presented ring A is internally regular only if it stays regular under every finitely presented base change. If a is not a unit, A/(a) is nonzero and finitely presented over A; there a becomes zero and fails regularity. Conversely units stay units and regular. Pull back to the Set model Z: 2 is regular but not a unit, so the regular-element subobject cannot commute with that inverse image. The quotient argument avoids any unjustified finite-presentation assumption on residue fields.

**Literature match:** Caramello–Johnstone§1 supplies the ring/field classifier framework; the exact universal-base-change computation is independently re-proved. It answers the manuscript’s question without identifying domain and field theories.

**References:** CaramelloJohnstone2009, SGA4I1972.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-101

**Source:** sources/texts/codex/K161-2-07_transcription.tex:309–315.

**Literal excerpt:**

```tex
\uline{On a envie de prouver} $5.\unsure{5|6}$. Soit $S\subset\mathrm{Ob}\,R$, $R\in\mathrm{Ob}\,C_\lambda$,
supposons que $\forall R'\in\mathrm{Ob}\,C_\lambda$, et $\forall F,G\in\underline{\mathrm{Hom}}_\lambda(R,R')$,
\[
\mathrm{Hom}(F,G)\longrightarrow\prod_{s\in S}\mathrm{Hom}\bigl(F(s),G(s)\bigr)\quad\text{est injectif.}
\]
Alors $R$ est-il $\lambda$-engendré par $S$ ? (la réciproque
étant évidemment vraie...)
```

**Precise statement or question:** No for the empty doctrine, and no for finite products. Determination on a retract-dense basis is weaker than generation by the prescribed operations. This counterexample does not refute a separately strengthened finite-limit version.

**Check and its limit:** For no operations, take the Karoubi completion of the one-object monoid {1,e}, e²=e≠1. Its new retract object is not isomorphic to the original object, but a transformation’s component on it is determined by the component on the original object using the retraction. For finite products take R=FinSet^op and S={2}. Since1 is a retract of2, its component is determined; every n is a finite power of1 in R. Yet products of2 in R have even cardinality2m (including0), so1 and3 are outside the product closure.

**Literature match:** Kelly5.36 identifies retract completion; Adámek–Lawvere–Rosický2003p36/Proposition2.6 gives the same even-finite-set Cauchy phenomenon. The exact transformation-detection counterexamples answer the sheet’s question independently.

**References:** Kelly1982, AdamekLawvereRosicky2003.

**Executed checks:** retract detection is weaker than operation generation. See the program and output linked above.

**Recorded event types:** refuted, with refined statement RF-SA23-groupes-101; computation or formal certificate.

## C-SA23-groupes-102

**Source:** sources/texts/codex/K161-2-07_transcription.tex:317–358; sources/texts/codex/K161-2-05_transcription.tex:326–330; sources/texts/codex/K161-2-04_transcription.tex:512–538.

**Literal excerpt:**

```tex
\margin{? $||$} $\gamma_{\lambda,\lambda'}$ est-il tjrs \deleted{\unsure{pl}}-fidèle ?, i.e
$\underline{\mathrm{Hom}}_\lambda(T_1,T_2)\longrightarrow\mathrm{Hom}_{\lambda'}(T_1,T_2)$
est-il tjrs une équivalence pour $T_1$ et $T_2$ deux $\lambda$-types ? Sans
doute faux, mais ce doit être pl. fidèle si $\underset{\rightarrow}{\lambda}=\varnothing$,
```

**Precise statement or question:** Restriction along a doctrine inclusion is represented by the corresponding free completion when it exists. The finite-limit to all-limit passage uses Pro completion, and the dual finite-colimit passage uses Ind. Restriction can be fully faithful on transformations between given finite constructions without making every construction on complete targets finite.

**Check and its limit:** A construction X↦X^N commutes with every continuous functor between complete categories. It is not a finite-limit construction of a bare object: on Set a finite such construction is a finite power, and2^N is infinite while every2^n is finite. The free-completion universal property identifies modifications between the existing finite constructions; it does not make this new object of the Hom category lie in the image. All Pro/Ind uses retain the smallness or universe enlargement needed for the completion.

**Literature match:** Kelly5.35 and5.10 give the completion/Ind machinery; the infinite-power witness is independently checked. This matches the manuscript’s earlier definition of 1-faithful at file05:328–330, and avoids conflating full faithfulness with essential surjectivity.

**References:** Kelly1982.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-103

**Source:** sources/texts/codex/K161-2-07_transcription.tex:359–393.

**Literal excerpt:**

```tex
\fbox{7} \uline{Dualité}. \uline{Opposé} d'un ``type'' $\lambda=(\underset{\leftarrow}{\lambda},\underset{\rightarrow}{\lambda})$ : on échange
les types de diagrammes utilisés pour des $\varprojlim$ resp $\varinjlim$.
Alors pour tt $\lambda$-type $T_{\deleted{\unsure{\lambda}}}$, on définit un $\lambda^o$-type $T^o$ \unsure{t.q}
\[
T^o_{\deleted{\unsure{\lambda}}}(C)\simeq T_{\deleted{\unsure{\lambda}}}(C^o)^o\tag*{(\unsure{7.1|6.3})}
\]
```

**Precise statement or question:** For a doctrine lambda=(lambda_limits,lambda_colimits), opposite categories exchange the two families, and the type-level dual is T^op(C)=T(C^op)^op, with the appropriate reversal of natural-transformation directions.

**Check and its limit:** Opposite reverses every cone/cocone and sends an exact functor to an exact functor for the dual doctrine. Applying opposite twice is canonically the identity. A natural transformation F⇒G becomes G^op⇒F^op, so the two-category convention must include reversal of2-cells; it is not a literal strict covariant endofunctor of unmodified Cat.

**Literature match:** Kelly’s enriched opposite and universal-property framework and Di Liberti–Osmond’s explicit pseudofunctor convention provide the checked comparison; the elementary duality is independently verified.

**References:** Kelly1982, DiLibertiOsmond2025.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-104

**Source:** sources/texts/codex/K161-2-07_transcription.tex:555–595.

**Literal excerpt:**

```tex
Pour résumer, si $T$ est un $\lambda$-type $(\underset{\rightarrow}{\lambda}=\varnothing)$, alors
\deleted{pour \unsure{toute} $C\in\mathrm{Ob}\,\mathrm{Cat}_{\lambda}$,} $S=T(\mathrm{Ens})$ est muni d'une sous-catégorie
pleine $\Sigma\subset S$, formée des $\varphi\in\mathrm{Ob}\,S$ tels que pour
tout $C\in\mathrm{Ob}\,\mathrm{Cat}_{\lambda}\deleted{\unsure{C}}$ et tout \deleted{\unsure{fon}} $\xi\in C_\lambda$, \deleted{\unsure{on a un fon}}
\deleted{\unsure{s'expr}} définissant un \deleted{\unsure{hom}} foncteur
\[
 \widetilde\xi:C^o\longrightarrow S\qquad X\longmapsto\mathrm{Hom}(X,\xi)
\]
le foncteur composé avec $\mathrm{Hom}_S(\varphi,-)$ soit
représentable\unsure{s} : […] \Sigma^o\xrightarrow{\inserted{\lambda\text{-foncteur}}}\underline{\mathrm{Hom}}\,(T(C),C),\qquad T(C)\longrightarrow\underline{\mathrm{Hom}}_\lambda(\Sigma^o,C)
\]
On voit alors que l'on trouve ainsi une
```

**Precise statement or question:** The evaluation copy R⊂Fun(S,Set) is recoverable when the chosen theory and its representable constructions are retained. The proposed intrinsic Sigma test on these lines still quantifies over T and arbitrary target categories and therefore is not a definition from the bare category S alone.

**Check and its limit:** C077 proves the full-faithful evaluation embedding. Closure under the dual operation shapes follows because representing presheaves are closed under the original limits. But the later criterion uses T(C), exact functors and their evaluations, so it has not eliminated T. For finite limits, C083 recovers R from S_fp; for finite products, C085 shows the remaining Morita/presentation choice.

**Literature match:** Gabriel–Ulmer in Lack–Power8 and the ALR2003 Cauchy/Morita theorem settle those two precise special cases. Searches of those reconstruction sources and Kelly’s density theory did not identify the unfinished arbitrary-lambda criterion as a complete intrinsic theorem.

**References:** LackPower2009, AdamekLawvereRosicky2003, Kelly1982.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-105

**Source:** sources/texts/codex/K161-2-07_transcription.tex:597–644; sources/texts/codex/K161-2-07_transcription.tex:645–660.

**Literal excerpt:**

```tex
$U\in\mathrm{Ob}\,E$, $X\in\mathrm{Ob}\,B$ \inserted{(p. ex. $X\in\mathrm{Ob}\,C$)}, on va définir une
\deleted{bijection}\inserted{application}
\[
 \mathrm{Hom}_E(U,f^*X)\xrightarrow{\deleted{\unsure{\sim}}}
 \mathrm{Hom}_{T(\mathrm{Ens})\inserted{=\mathrm{Ind}(C^o)}}\bigl(O_B(X),O_E(U)\bigr)\tag*{(1)}
\]
```

**Precise statement or question:** For B=PSh(C), C small finitely complete, and f:E→B, the displayed comparison Hom_E(U,f*X)→Nat(O_B(X),O_E(U)) is natural in X,U. It is bijective for X representable, but not for arbitrary X.

**Check and its limit:** For X=y(c), O_B(y(c)) is the covariant representable Hom_C(c,-), so Yoneda gives Nat(O_B(y(c)),O_E(U))≃Hom_E(U,f0(c)). For C=1, E=B=Set, f=id, U=1 and X=empty, the left side has0 elements while both O-functors are the unique terminal lex functor and the right side has1.

**Literature match:** The exact representable argument is ordinary Yoneda (Riehl§2.2); the0-versus1 counterexample checks the necessity of the manuscript’s own correction. No full embedding of all B into the model-functor category is inferred.

**References:** RiehlContextOnline.

**Executed checks:** Yoneda comparison fails for arbitrary X. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-106

**Source:** sources/texts/codex/K161-2-07_transcription.tex:645–684.

**Literal excerpt:**

```tex
On \deleted{trouve que}\inserted{commence} par \deleted{que la catégorie fibrée}\inserted{noter que la catégorie fibrée}
\deleted{sur $E$} $\mathcal F'_0$ \inserted{sur $C$} se prolonge en Catégorie cofibrée sur
$\mathrm{Pro}(C)\simeq T(\mathrm{Ens})^o$, \deleted{soit} $\overline{\mathcal F'_0}$, donc $\overline{\mathcal F'_0}(O_E(U))$
est défini [mais covariant en l'objet $(\ )\in T(\mathrm{Ens})$.
Pour $U$ variable, $U\longmapsto\overline{\mathcal F'_0}(O_E(U))$ donne donc une
catégorie fibrée sur $U$ [image inverse de $\overline{\mathcal F'_0}$ par $\underline O_E:E^o\to T(\mathrm{Ens})\underset{\unsure{\simeq|=|\cong}}{\vphantom A}$
$\mathrm{Pro}(C)^o$
```

**Precise statement or question:** For a left-exact site functor f0:C→E and a contravariant stack F on C, the inverse image is obtained by stackifying the bicategorical Kan-extension presheaf U↦2-colim_(c,U→f0(c))^op F(c). Site continuity and the chosen topology remain part of the hypotheses.

**Check and its limit:** The category I_U of pairs(c,U→f0c) is cofiltered: terminal object, products and equalizers follow from finite-limit preservation by Hom_E(U,f0−). F is contravariant, so the actual filtered colimit is over I_U^op. Localization of the appropriate fibred category gives the prestack universal property; stackification imposes descent. This is a bicategorical colimit, not an ordinary colimit of object sets.

**Literature match:** Stacks04WA, Lemmas8.12.5–8.12.10, constructs the localization, its universal property, and pullback by stackification. The comma formula is the present explicit Kan-extension reconstruction; it includes the source’s subsequent subsite/topology variant.

**References:** StacksPullback, VistoliDescent.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-107

**Source:** sources/texts/codex/K161-2-07_transcription.tex:687–712.

**Literal excerpt:**

```tex
Donc on cherche un produit
2-fibré $B\times_{B_I}X$, dans la 2-catégorie (Top)
(On n'a pas encore prouvé que cela marche)
```

**Precise statement or question:** Let B classify a geometric theory with chosen underlying objects b_i and let E_i∈X. If b:B→B_I and E:X→B_I classify these families, the relative classifier is the bicategorical pullback B×_(B_I)X. It classifies a structure together with specified isomorphisms of its underlying objects with the pulled-back E_i.

**Check and its limit:** A geometric morphism Y→the pullback is a pair Y→B,Y→X with an invertible comparison of their composites to B_I. Since B_I classifies I-families of objects, that comparison is exactly the chosen underlying-object isomorphism. This proves the represented functor once the pullback exists; Grothendieck-topos2-pullbacks supply existence.

**Literature match:** SGA4IV Exercise9.1.6(d), original printed435, states existence of topos base change. Vickers2017 Theorems5.11–5.12pp242–244 give relative classifying toposes and their geometric base-change property for theory extensions. The exact fixed-object pullback is independently derived from that universal property.

**References:** SGA4I1972, Vickers2017.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-108

**Source:** sources/texts/codex/K161-2-06_transcription.tex:339.

**Literal excerpt:**

```tex
Q. Relation avec ``analyseurs'' de \unsure{Lazard|Lazare}.
```

**Precise statement or question:** The requested comparison concerns Lazard’s graded polynomial-operation systems and their formal completions. It is not an identified equivalence with arbitrary finite-limit sketches; a specific translation of the operation, substitution and completion data is still required.

**Check and its limit:** Lazard§§4–6 starts with multigraded polynomial operations on modules, substitutions and neutral-variable relations, then passes to completed products of homogeneous components. The manuscript’s general finite-limit categories do not automatically include this grading or completion. Ordinary finite-product algebraic operations supply a common part; the infinitary completion is extra structure.

**Literature match:** Lazard’s Bourbaki109 was delivered February1955 and published in the1956 volume, pp77–91; §§4–6 were opened and read. The full1955AnnENS article is the backward bibliographic reference. Bénabou1968 cites both Lawvere and Lazard, but only its bibliography was inspected, so it is not used as a proved equivalence.

**References:** Lazard1956.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-109

**Source:** sources/texts/codex/K161-2-03_transcription.tex:48–53;90–92;123–133.

**Literal excerpt:**

```tex
\text{noethériens}&\quad\text{\uline{non}}\\
\text{régulier \unsure{n.-régulier ?}}&\quad\text{\uline{non}}\\
\text{CM ?}&\quad\text{\uline{non}}\\
\text{Gor ?}&\quad\text{\uline{non}}\\
\text{int. complèt$^{e}$ ?}&\quad\text{\uline{non}}
```

**Precise statement or question:** As full ring properties with all ring maps, noetherianity, the usual noetherian regular/CM/Gorenstein/complete-intersection conditions, finite type/presentation over a fixed base, artinianness and finiteness of the idempotent set fail filtered-colimit closure. They are therefore not geometric full subtheories in that interpretation.

**Check and its limit:** The sequence k[x1,…,xn] has finite-type regular complete-intersection stages, but colimit k[x1,x2,…] is not noetherian and not finitely generated. For artinianness and finitely many idempotents take finite Boolean rings F2^{2^n} with the duplication embeddings; their colimit is the Boolean ring of clopen cylinder sets on Cantor space, with infinitely many idempotents and descending nonstabilizing ideals. This does not address alternative nonnoetherian definitions of regularity or CM, which the fragment does not specify.

**Literature match:** The geometric filtered-colimit criterion is the same one checked in C027. Stacks flatness and finite-presentation criteria distinguish these finiteness conditions from geometric flatness; the explicit directed-system witnesses supply the negative answers.

**References:** SGA4I1972, StacksFlatness.

**Executed checks:** finite Boolean stages acquire infinitely many idempotents. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-110

**Source:** sources/texts/codex/K161-2-02_transcription.tex:168–174.

**Literal excerpt:**

```tex
$T_R(\mathrm{Ens})\simeq\underline{\mathrm{Pt}}(R)^o\simeq\underline{\mathrm{Fib}}(R)$. Peut être vide et $R\not\simeq\operatorname{Top}(\varnothing)$
```

**Precise statement or question:** There are nondegenerate Grothendieck topoi with no Set-valued points. Thus absence of Set models does not mean that the geometric theory is inconsistent in all topoi.

**Check and its limit:** Let B be a complete atomless Boolean algebra, for example regular opens of R. A frame map B→2 preserves complements and arbitrary joins, hence arbitrary meets. The meet of its1-fiber would be a nonzero atom, impossible. Therefore Sh(B) has no points, while0≠1 in its subterminal frame proves nondegeneracy. The associated propositional geometric theory has B-valued models despite no Set model.

**Literature match:** Barr1974, Toposes without points, Introductionp265 gives this exact complete-Boolean-algebra example and argument, with a backward reference to SGA4IV7.4. Its stronger Boolean-localization theorem is not needed here.

**References:** Barr1974.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-111

**Source:** sources/texts/codex/K161-2-02_transcription.tex:540–544; sources/texts/codex/K161-2-03_transcription.tex:206–244.

**Literal excerpt:**

```tex
H^n(K(G,1),\unsure{\mathbb Z|\Pi})\qquad
 \overset{\unsure{3}}{\boxed{\underline{H^n(\underline{K(G,1)}\unsure{,|;}\Pi)}}}
 \underset{Z^{\unsure{n|i}}(\Pi)}{\overset{\unsure{\sim|n}}{\longrightarrow}}\mathrm{Simpl}(\mathrm{ENS})
```

**Precise statement or question:** No single precise proposition is identifiable from these detached expressions. The cohomology coefficient, degree-map type and direction are unclear; the ring-topology fragments do not specify P1,P2 or the displayed n-model limit.

**Check and its limit:** The surrounding text establishes neither the missing definitions nor a typed assertion. Classical group cohomology of K(G,1), simplicial Eilenberg–Mac Lane constructions, and the adjacent ring-topology discussion were searched as leads; none licenses choosing one reading. The expressions are retained verbatim in the archival source and registered for ink/context checking.

**Literature match:** Searches of group-cohomology/K(G,1) and the adjacent published classifying-topos/ring-site literature found several possible frameworks but no exact match to this incomplete fragment. This is classF identification failure, not a claim of a new open theorem.

**References:** SGA4I1972, Lazard1956.

**Recorded event types:** used and rechecked in this run.

## C-SA23-groupes-112

**Source:** sources/texts/codex/K161-2-06_transcription.tex:18–23.

**Literal excerpt:**

```tex
\textcircled{$2^{(\mathrm{iv})}$} Catégories \uline{abéliennes}, foncteurs exacts

\hfill[foncteurs additifs ?]
```

**Precise statement or question:** Additive functors between abelian categories need not be exact. Exactness is additional doctrine data, so the two entries cannot be interchanged.

**Check and its limit:** Tensoring abelian groups with Z/2 is additive but sends the monomorphism2:Z→Z to the zero endomorphism of Z/2, which is not monic. Thus it is not left exact. Additivity only preserves the finite biproduct structure, not all kernels and cokernels.

**Literature match:** Stacks00HK states the exact relation between tensor exactness and flatness. The explicit multiplication-by2 witness answers the parenthetical question.

**References:** StacksFlatness.

**Executed checks:** additivity does not imply exactness; faithful flatness fails under module colimits. See the program and output linked above.

**Recorded event types:** independent re-proof; computation or formal certificate.

## C-SA23-groupes-113

**Source:** sources/texts/codex/K161-2-07_transcription.tex:714–726.

**Literal excerpt:**

```tex
Soit $\unsure{\mathscr S|S|\mathcal S}_{\deleted{\unsure{X}}}$ \deleted{la catégorie}\inserted{le champ sur $X$} formée des structures
de ce type dans $(X,(E_i))$, \inserted{et les fonctrs induits} i.e. des functs ex
à g. $f:R\longrightarrow X$ avec $f(r_i)\simeq E_i$ donnés, et […] soit. $\unsure{\Phi|I|\underline I}_X$ le champ \inserted{en topos} des flèches de $\deleted{\unsure{B}}X$.
```

**Precise statement or question:** For a fixed small finite-limit theory and fixed base objects in X, assigning to U the category of structures on their pullbacks in X/U is a stack for the canonical topology, by descent of objects, arrows, equations and finite-limit cones. The fragment does not specify a complete equivalence between this stack and its proposed stack of slice topoi.

**Check and its limit:** Descent is effective in a topos. A finite-limit model is a family of objects/arrows satisfying equations and invertibility of comparison maps; these properties descend along epimorphic covers, as do the chosen underlying-object isomorphisms. This proves the stated model stack. Identifying the unfinished topos-valued object or using it to replace the relative classifier requires the missing variance and2-morphism conventions.

**Literature match:** Vistoli’s descent framework, Stacks04WA and Vickers5.11–5.12 supply the established model-stack and relative-classifier ingredients. The last incomplete sentence is not promoted to a fully specified topos-stack theorem.

**References:** VistoliDescent, StacksPullback, Vickers2017.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-114

**Source:** sources/texts/codex/K161-2-04_transcription.tex:506–509.

**Literal excerpt:**

```tex
\textcircled{2} \uline{Autre Pb :} caractériser les théories algébriques par des propriétés intrinsèques (plutôt que par ``construction'' via une suite transfinie de constructions, ou la représentabilité par un $R$ tel que\ldots).
La seule condition (probablement pas suffisante) que je voie est : \uline{$T$ commute aux 2-limites projectives de $\Delta$}, i.e. : $T$ transforme \deleted{\unsure{foncteurs}} \inserted{\unsure{ens|sans}} pl. fid (prod.) en \unsure{itou|isos|idem}, $\underline{\operatorname{Hom}}_{\mathrm{Cat}}(J,C)$ en $\operatorname{Hom}_{\mathrm{Cat}}(J,T(C))$\ldots
```

**Precise statement or question:** A representable pseudofunctor Hom_Delta(R,-) preserves existing weighted bilimits. A converse requires a specified doctrine and size/accessibility hypotheses; the page does not state a sufficient intrinsic criterion.

**Check and its limit:** The weighted-bilimit universal property, tested at R, is exactly the required preservation equivalence. For a sufficient comparison theorem in a specified setting, a pseudofunctor from a finitely bi-accessible 2-category with weighted bilimits to Cat, preserving weighted bilimits and bifiltered bicolimits, has a left biadjoint. Evaluating that biadjunction at the terminal category gives a representing object. This adds hypotheses that the manuscript has not established for its arbitrary Delta.

**Literature match:** Di Liberti–Osmond Theorem 5.2.3 (printed theorem number; online section 6.2) gives the exact conditional biadjoint result. It does not identify the page’s arbitrary large doctrine with that setting.

**References:** DiLibertiOsmond2025.

**Recorded event types:** independent re-proof.

## C-SA23-groupes-115

**Source:** sources/texts/codex/K161-2-03_transcription.tex:478–483.

**Literal excerpt:**

```tex
A-t-elle assez de pts ??
```

**Precise statement or question:** The zero-dimensional commutative-ring classifier on the stated finite-type affine Z-site has enough points. Its displayed countable covering family D_n has no finite subcover; this fact alone is not a Morita-invariant noncoherence theorem.

**Check and its limit:** There are countably many finite presentations over Z and countably many maps between any two such rings, so choose a countable skeleton of the finite-type affine site; it has finite limits. The D_n family over the generic element is countable, and its pullbacks along the countably many site arrows generate a countable coverage. Makkai–Reyes6.2.4 therefore supplies enough points. No finite subfamily covers: for maximal exponent N, the element t in F_2[t]/(t^(N+1)) has neither a unit component nor t^n=0 for n≤N. This is a general nilpotence-order argument, not a finite-sample inference.

**Literature match:** Makkai–Reyes, First Order Categorical Logic (1977), Theorem6.2.4, proves enough points for separable topoi. The opened 2018 corrected retyping states the countable-category/countable-basic-cover hypothesis and gives the proof on printed p125. The original book metadata and retyping provenance were separately opened; no earlier circulation date is asserted.

**References:** MakkaiReyes1977.

**Recorded event types:** targeted proof check.


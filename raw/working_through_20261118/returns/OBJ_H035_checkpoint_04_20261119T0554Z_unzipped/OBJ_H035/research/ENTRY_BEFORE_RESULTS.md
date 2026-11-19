# H035 — Coherent modules from a functor and prorepresentability

**Working entry. The central Theorem 12 is proved in the reconstruction below;
H035.39–40 remain open. This is not a completed audit certificate.**

This entry separates the manuscript, later sources, and this run's mathematics.
The six supplied model notes are treated as leads. There are 46 statement rows,
44 individually adjudicated note subclaims, and 32 disputed-reading rows.
The complete proofs, counterexamples and current open arguments are in
`PROOFS.tex`; the second checks are in `research/SECOND_CHECKS.md`.
All work was done in one stream. “Second check” means a new derivation from
the hypotheses by the same model, not another reader or a formal certificate.

## 1. The object in his terms and in current terms

> « Construction de faisceaux de modules »

The cover names the construction of module sheaves from functors and an
application to prorepresentation along a section (94/002.1–15). The central
working object is a covariant functor from modules to sets. The problem is to
recover a finite module P for which the functor is naturally Hom(P,−).
The later sheets apply the criterion to proper Hom functors and to affine
restriction of scalars. The cover's final Ω¹-expression has an unidentified
following mark; its meaning is not supplied from the later argument.

**Our terminology.** “Finite” means finitely generated; over a noetherian
ring this is equivalent to finitely presented. A strict prorepresentation
is a filtered colimit of Hom(P_i,−) with finite P_i and surjective inverse
transition maps. Eventual stationarity means actual isomorphisms of the
transition maps beyond a stage, a stronger assertion than isomorphism of
the pro-object with a constant object. These distinctions decide H035.29.

A left exact set-valued functor on modules has a canonical module structure:
apply it to the addition, scalar and finite-product diagrams. This fact,
proved in H035.2, makes the subsequent tensor comparisons meaningful. Once
left exactness is removed, additivity and A-linearity must be stated. The
question mark attached to additivity in Remarque 18 is therefore substantive.

> « module de différentielles pour un C.M. »

The heading on 94/011.1 is retained as written. The parameter-quotient
property beneath it is the property of a canonical module of a
Cohen–Macaulay local ring. That identification is our reconstruction,
proved in H035.16. It is not a corrected reading of the word, and it would
be false if interpreted as ordinary Kähler differentials. The later
“faisceau fondamental” is used in this canonical-module sense, with the
normalization specified in the proofs.

> « foncteur constructible »

On 94/022 the proposed name refers to the non-left-exact conditions of
Theorem 12. It must not be identified without proof with a functor having
a finite presentation by Hom functors in Auslander's sense. That smaller
category has useful closure properties, but the full composition assertion
under the manuscript's axioms remains the main unresolved continuation here.

## 2. Where he writes about it, in page order

The source is Montpellier cote 94, catalogued as *Dualité des modules /
Construction de faisceaux de modules: notes manuscrites (s.d.)*, with the
catalogue qualification **[à partir de 1965]**. No exact date is written on
the relevant mathematical leaves. The inserted absolute-value typescript
has no established author or separate date in the supplied evidence.
The official [cote 94 PDF](https://grothendieck.umontpellier.fr/94.pdf) was
opened and the additional relevant pages were inspected personally.

| Scans | Content and status of the leaf |
|---|---|
| 002 | Cover: construction of module sheaves; prorepresentation along a section; unidentified invariant notation. |
| 003–005 | Restriction of scalars, faithfully flat descent, principal completion and noetherian induction: Lemme 1, Lemme 2, Proposition 3. |
| 005–007 | Complete-local criterion and strict prorepresentation: Proposition 4 and Lemme 5. |
| 008 | Remarque 5 bis: constructible rank and the flawed converse, repaired using an additional finite-value hypothesis. |
| 009–010 | Generic graded freeness, Tor vanishing and Hom base change; two distinct errors in the written Hom-complex argument. |
| 011 | Canonical-module reconstruction, regular and parameter quotients, generic existence; EGA/excellence margin. |
| 012 | Separate absolute-value typescript, outside H035. Included only because the supplied notes make mathematical claims about it. |
| 013 | Continuation of Corollaire 10, parameter Hom detection, cancelled Corollaire 11 and its reformulation note. |
| 015–017 | Rewritten Corollaire 11; Theorem 12 and its proof; Remarque 13. The missing strictness in the rewrite is separated from the strict system actually supplied to the theorem. |
| 018 | Proper Hom representability, quasi-coherent extension and arbitrary base change: Theorem 14. |
| 019–021 | Higher underived Ext/cohomology functors and generic regular-quotient comparisons: Lemmas 15–17. |
| 022 | Remarque 18, the prospective constructible-functor theory; Theorem 19 on affine restriction of scalars. |
| 023–024 | Finiteness refinements, closed immersions, cones, the Murre pointer and Remarque 21. |

The initial citations covered only scans 2–13. Targeted searches for the
names and notation in the supplied whole-folder transcription located
15–24; the folder was not read through indiscriminately. Scan 14 is an
intervening documentary report about local fields and is not imported into
the mathematical argument. The scan numbers above are PDF positions, not
the handwritten folio numbers.

Locators count main written horizontal rows from the top, including headings,
displays and cancelled rows; interline and marginal additions use “a” and “m”.
The convention and principal anchors are in `readings/LINE_INDEX.md`.
Every disputed locus also has a pixel crop in `readings/`, with coordinates
in `CROP_MANIFEST.tsv`. The original transcriptions have not been rewritten.

## 3. His statements, precise reconstructions and verdicts

Each quotation below is the manuscript's short phrase, on its own. The
following paragraph is this run's precise formulation. “False as written”
is accompanied by the counterexample and the strongest corrected version
proved here; it does not mean every surrounding conclusion fails. The
two open rows remain working items, with their reduction and failed
approaches preserved rather than presented as settled.

### H035.1 — 94/002.1–15

> « Construction de faisceaux de modules »

**Our precise formulation.** Programme on the cover: construct modules from functors and prorepresent a functor along a section. Our precise affine realization: for an augmented commutative A-algebra C→A with ideal I, its formal functor on augmented A-algebras with nilpotent augmentation ideal is prorepresented by {C/I^(n+1)}. On square-zero extensions A⊕M its tangent functor is Hom_A(I/I²,M), with I/I²=Ω¹_(C/A)⊗_C A and a surjection Sym_A(I/I²)→gr_I(C). No universal prorepresentability claim for arbitrary functors follows from the title.

**Reconstruction or textual qualification.** Programme; precise affine realization supplied by Theorem 12

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.1; research/SECOND_CHECKS.md H035.1.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.2 — 94/003.2–7

> « F : Mod A → (Ens) »

**Our precise formulation.** For a ring map A→B, restriction of scalars sends Hom_A(P,−) to Hom_B(B⊗_A P,−). A finite-limit-preserving functor F:Mod(A)→Sets has a canonical additive A-linear module structure. If it also preserves filtered colimits, F(M)⊗_A B→F(M⊗_A B) is an isomorphism for every flat A-algebra B and every A-module M; in particular this holds for localization.

**Reconstruction or textual qualification.** Canonical A-linearity is our explicit reconstruction

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.2; research/SECOND_CHECKS.md H035.2.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.3 — 94/003.8–13

> « Lemme 1 »

**Our precise formulation.** For a faithfully flat ring map A→B, a functor F:Mod(A)→Sets is left exact and represented by an A-module if and only if it is left exact and its restriction to Mod(B) is represented by a B-module. Finite generation and finite presentation of the representing module descend and ascend separately. No noetherian hypothesis is needed.

**Reconstruction or textual qualification.** Noetherianity unnecessary

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.3; research/SECOND_CHECKS.md H035.3.

**Literature:** Stacks023N, Proposition 35.3.9 (faithfully flat module descent).

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.4 — 94/003.14–004.13

> « Lemme 2 »

**Our precise formulation.** Let A be noetherian and f∈A. A functor F:Mod(A)→Sets is represented by a finite A-module if and only if it preserves finite limits and filtered colimits, its restrictions to A_f and to every A/(f^n), n≥1, are representable, and for every finite module M over C=lim_n A/(f^n), F(M)→lim_n F(M/f^nM) is bijective. The formal test modules need not be completions of finite A-modules.

**Reconstruction or textual qualification.** Finite modules over the completed ring are literal test objects

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.4; research/SECOND_CHECKS.md H035.4.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.5 — 94/004.14–005.12

> « Proposition 3 »

**Our precise formulation.** Let A be noetherian. Finite representability of F is equivalent to left exactness, preservation of filtered colimits, the principal-completion comparison of H035.4 for every f∈A, and this generic condition: for every nonzero quotient B of A there is a nonnilpotent g∈B such that F restricted to Mod(B_g) is representable. Literally including the zero quotient makes the necessity direction false.

**Reconstruction or textual qualification.** Exclude the zero quotient in the nonnilpotent-element clause

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.5; research/SECOND_CHECKS.md H035.5.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.6 — 94/005.15–006.10

> « Proposition 4 »

**Our precise formulation.** Let (A,m) be noetherian local. A left exact functor F preserving filtered colimits is represented by a finite A-module if F(M)→lim_n F(M/m^nM) is bijective for every finite Ahat-module M and F(E_n) is finite for the residue-field injective hull E_n over each A/m^n. The page's sufficient assumption that F takes every finite original A-module to a finite module implies these tests. The displayed stronger finite-value condition over Ahat is also sufficient. Necessity holds for finite representable F.

**Reconstruction or textual qualification.** Matlis duality supplies the omitted argument

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.6; research/SECOND_CHECKS.md H035.6.

**Literature:** Stacks08Z9, Proposition 47.7.8 (Matlis duality).

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.7 — 94/006.11–007.2

> « Lemme 5 »

**Our precise formulation.** Let A be noetherian and F:Mod(A)→Sets preserve finite limits and filtered colimits. Suppose for every p∈Spec(A) it commutes with maximal-ideal reduction on every finite A_p-hat module, and takes every finite-length A_p-module to a finite A_p-module. Then F restricted to Mod(A_p) is represented by a finite A_p-module Q_p, with Q_p⊗_(A_p) A_q=Q_q for every q⊂p.

**Reconstruction or textual qualification.** Separated from the strict prorepresentation assertion

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.7; research/SECOND_CHECKS.md H035.7.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.8 — 94/006.22–007.27

> « F est strictement proreprésentable »

**Our precise formulation.** Under all hypotheses of H035.7, assume additionally that for every prime p there is a nonzero f∈A/p for which F on Mod((A/p)_f) is representable. Then F is a filtered colimit of Hom_A(P_i,−), with finite P_i and surjective inverse transition maps; after localization at any fixed prime the system is eventually stationary. For every finite M and α∈F(M) there is a unique smallest submodule defining α. The written condition allowing f=0 is insufficient.

**Reconstruction or textual qualification.** The displayed f in A/p must be nonzero; literal zero is vacuous

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.8; research/SECOND_CHECKS.md H035.8.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.9 — 94/008.1–7

> « la fonction … est constructible »

**Our precise formulation.** Let A be noetherian and F be an additive A-linear functor preserving filtered colimits. If on each integral quotient B of A its restriction is represented by a finite module on some nonempty open, then p↦dim_(k(p))F(k(p)) is a constructible integer-valued function on Spec(A). Generic normality is unnecessary for this direction.

**Reconstruction or textual qualification.** Noetherian stratification

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.9; research/SECOND_CHECKS.md H035.9.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.10 — 94/008.8–26

> « En sens inverse »

**Our precise formulation.** Under H035.7, constructibility of p↦dim F(k(p)), even together with a dense normal open in every integral quotient, does not imply generic representability. Counterexample: A=Z, L=Σ_(p prime)(1/p)Z⊂Q, F=L⊗−. The corrected implication holds if F(B) is finite for every integral quotient B: then on a constant-rank open the local representing modules are free and F is represented by the dual of the finite locally free module F(B).

**Reconstruction or textual qualification.** False without an extra finite-value hypothesis; repaired by Theorem 12(iv)

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.10; research/SECOND_CHECKS.md H035.10.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.11 — 94/009.1–3

> « Lemme 6 »

**Our precise formulation.** For a locally noetherian scheme S, its nilradical J, and a coherent module F, there is a dense open U such that every graded piece of gr_J(O_S) and gr_J(F), restricted to U, is locally free over O_(U_red). This is a finite graded-freeness assertion locally; it does not assert that every noetherian scheme has a dense Cohen–Macaulay open.

**Reconstruction or textual qualification.** The scheme is locally noetherian; this is not generic Cohen–Macaulayness

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.11; research/SECOND_CHECKS.md H035.11.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.12 — 94/009.4–19

> « Tor »

**Our precise formulation.** For a locally noetherian scheme S and coherent F, there is a dense open U such that for every s∈U, every O_(S,s)-regular sequence x_1,…,x_r, and every i>0, Tor_i^(O_(S,s))(F_s,O_(S,s)/(x_1,…,x_r))=0. The module denoted M without definition in the written proof is reconstructed as the coefficient module; the filtration proof uses all positive Tor degrees.

**Reconstruction or textual qualification.** Undefined M in the proof is the coefficient module

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.12; research/SECOND_CHECKS.md H035.12.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.13 — 94/009.20–010.19

> « Corollaire 7 »

**Our precise formulation.** For coherent modules P,Q on a locally noetherian scheme S, there is a dense open U such that for all s∈U and every regular sequence x in O_(S,s), Hom(P,Q)_s⊗O_(S,s)/(x)→Hom_(O_(S,s))(P_s,Q_s/(x)Q_s) is an isomorphism. The same parameter list is used on both sides in our reconstruction of the doubtful final index.

**Reconstruction or textual qualification.** Correct the coefficient and use all positive Tor vanishing

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.13; research/SECOND_CHECKS.md H035.13.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.14 — 94/010.5–11

> « K »

**Our precise formulation.** For a finite presentation L_1→L_0→P→0 with finite free L_i and coefficient Q, Hom(P,Q) is H⁰ of [L_0^∨⊗Q→L_1^∨⊗Q]. The manuscript's two occurrences of P instead of Q give a false formula, already for P=k and Q=k² over a field. The corrected formula also computes Hom(P,Q⊗M) after tensoring this complex with M.

**Reconstruction or textual qualification.** The scan writes P where the coefficient must be Q

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.14; research/SECOND_CHECKS.md H035.14.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.15 — 94/010.12–18

> « Tor »

**Our precise formulation.** For a two-term cochain complex K=[K⁰→K¹] and module M, the written conditions Tor_1(M,H¹(K))=Tor_1(M,Z¹(K))=0 do not ensure H⁰(K)⊗M→H⁰(K⊗M) is an isomorphism. Counterexample: A=k[x,y]/(xy), M=A/(x), K=[A --y--> A]. A sufficient corrected condition is Tor_1(M,H¹(K))=Tor_1(M,B¹(K))=0, where B¹=im(d); alternatively retain Tor_1(M,K¹)=0 and require Tor_1(M,H¹(K))=Tor_2(M,H¹(K))=0.

**Reconstruction or textual qualification.** Z^1 is insufficient; B^1 or a Tor_2 hypothesis is required

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.15; research/SECOND_CHECKS.md H035.15.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.16 — 94/011.1–3

> « module de différentielles pour un C.M. »

**Our precise formulation.** Our canonical-module interpretation of the heading: for a noetherian Cohen–Macaulay local ring A and finite module Ω, Ω is canonical if and only if, for every system of parameters x, Ω/(x)Ω is the injective hull of the residue field as an A/(x)-module. Canonical means that its completion is the normalized canonical module of Ahat. The literal term differentials is retained; interpreting it as Kähler differentials would be false, for example Ω¹_(k/k)=0 rather than k.

**Reconstruction or textual qualification.** Canonical-module equivalence is ours; the ink says differentials, and the Kähler interpretation is refuted.

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.16; research/SECOND_CHECKS.md H035.16.

**Literature:** Stacks0DW3 (canonical-module definition); Stacks0B5A, Lemma 47.16.7 (MCM duality).

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.17 — 94/011.4–9

> « Lemme 8 »

**Our precise formulation.** Let X be a locally noetherian Cohen–Macaulay scheme with a canonical (fundamental, in the reconstructed terminology) sheaf Ω. For an O_X-regular sequence of sections x_1,…,x_r defining Y, the coherent sheaf Ω/(x)Ω is a canonical sheaf on the Cohen–Macaulay scheme Y. The assertion is local on X and includes the empty sequence.

**Reconstruction or textual qualification.** Modern interpretation of faisceau fondamental

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.17; research/SECOND_CHECKS.md H035.17.

**Literature:** Stacks0DW4, Lemmas 47.20.1–5; dual Koszul proof here.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.18 — 94/011.10–14

> « Corollaire 9 »

**Our precise formulation.** Under H035.17, for x∈X and every system of parameters t of the Cohen–Macaulay local ring O_(X,x), Ω_x/(t)Ω_x is the indecomposable injective hull of k(x) over the artinian local ring O_(X,x)/(t). It is also an injective cogenerator of the finite-module category there.

**Reconstruction or textual qualification.** Over the artinian local parameter quotient

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.18; research/SECOND_CHECKS.md H035.18.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.19 — 94/011.15–22;013.1–7

> « Corollaire 10 »

**Our precise formulation.** If X is locally noetherian and locally embeddable in a regular scheme, there are a dense open U⊂X and a coherent module Ω on X such that U is Cohen–Macaulay and Ω_x is canonical for all x∈U. Thus every parameter quotient gives H035.18 and its Hom detection property. Our stronger sufficient hypothesis is Gor-2: locally, every integral closed subscheme has a nonempty Gorenstein open.

**Reconstruction or textual qualification.** Locally embeddable in a regular scheme

**Status:** known; exact source matched and reduction proved. **Proof and check:** PROOFS.tex section H035.19; research/SECOND_CHECKS.md H035.19.

**Literature:** Lyu2025, Corollary 4.7 p.225, Lemma 6.1(ii) p.230; EGAIV2, 6.11.8 p.162.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.20 — 94/011.17m

> « excellent »

**Our precise formulation.** The conclusion of H035.19 also holds for a locally noetherian excellent scheme, because every integral quotient has a dense regular, hence Gorenstein, open. This is generic canonical-module existence; it does not assert existence of a global dualizing complex on every excellent scheme.

**Reconstruction or textual qualification.** Generic canonical module, not a global dualizing complex

**Status:** known; exact source matched and reduction proved. **Proof and check:** PROOFS.tex section H035.20; research/SECOND_CHECKS.md H035.20.

**Literature:** Lyu2025, Remark 7.9 p.233 distinguishes global dualizing complexes.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.21 — 94/011.17m

> « EGA IV 6.11.8 »

**Our precise formulation.** The conclusion of H035.19 does not follow merely from the EGA IV 6.11.8 condition CMU, which asks for a nonempty Cohen–Macaulay open in every integral closed subscheme. A noetherian one-dimensional domain obtained by localizing k[t_i³,t_i⁴,t_i⁵:i≥1] away from its block maximal ideals is Cohen–Macaulay but has non-Gorenstein points in every nonempty open, so admits no finite generic canonical module. Gor-2 is the corrected uniform all-integral-quotients hypothesis; its sufficiency is H035.19 and its necessity for that uniform assertion follows from generic freeness of a rank-one canonical module.

**Reconstruction or textual qualification.** False: CMU does not ensure generic Gorenstein or canonical modules

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.21; research/SECOND_CHECKS.md H035.21.

**Literature:** EGAIV2, 6.11.8–6.11.9 pp.162–163; Lyu2025, Remark 7.7 p.233; explicit counterexample proved here.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.22 — 94/012.5–8

> « valeur absolue »

**Our precise formulation.** On the inserted absolute-value typescript, multiplicativity, subadditivity, and f(x)=0⇒x=0 alone do not make f(x−y) a distance: f≡1 is a counterexample. Add f(0)=0. Then the resulting normalized absolute value gives a field topology. A real additive valuation v, with v(0)=+∞, gives the absolute value exp(−v), satisfying the maximum inequality. This arithmetic leaf is outside H035 and its authorship is not established.

**Reconstruction or textual qualification.** Off H035; f(0)=0 is missing literally

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.22; research/SECOND_CHECKS.md H035.22.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Inserted typescript undated; authorship unestablished; folder catalogue dating is not a date for this leaf. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.23 — 94/012.13–20

> « PROPOSITION 1 »

**Our precise formulation.** For a normalized absolute value f on a field K, the following are equivalent: f=exp(−v) for a real additive valuation; f(x+y)≤max(f(x),f(y)); f(n·1)≤1 for all natural n. Equivalently the values on the prime subring are bounded. The binomial estimate f(x+y)^n≤(n+1)max(f(x),f(y))^n proves the nontrivial implication.

**Reconstruction or textual qualification.** Normalize f(0)=0; prove the binomial criterion

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.23; research/SECOND_CHECKS.md H035.23.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Inserted typescript undated; authorship unestablished; folder catalogue dating is not a date for this leaf. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.24 — 94/012.21–23

> « COROLLAIRE 1 »

**Our precise formulation.** Every normalized absolute value on a field of characteristic p>0 is valuative. The supporting sentence that every n·1 is a root of unity is false at n=p. The corrected supporting statement is that every nonzero element of the prime field has finite multiplicative order; zero has absolute value zero.

**Reconstruction or textual qualification.** Only nonzero elements of the prime field are roots of unity

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.24; research/SECOND_CHECKS.md H035.24.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Inserted typescript undated; authorship unestablished; folder catalogue dating is not a date for this leaf. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.25 — 94/012.24–25

> « équivalentes »

**Our precise formulation.** For normalized absolute values f,g on a field, equivalence is the relation f=g^s for some strictly positive real s, and is equivalent to inducing the same field topology. The unqualified real exponent in the typescript permits s=0 on K^×, destroying symmetry, and leaves 0^0 undefined at zero. Both trivial and nontrivial topology cases are included in the corrected proof.

**Reconstruction or textual qualification.** The exponent must be strictly positive

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.25; research/SECOND_CHECKS.md H035.25.

**Literature:** BourbakiTopIX, IX section 3 no.2 Proposition 6, pp.TG IX.29–30.

**Date:** Inserted typescript undated; authorship unestablished; folder catalogue dating is not a date for this leaf. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.26 — 94/012.26–30

> « PROPOSITION 2 »

**Our precise formulation.** A normalized absolute value on Q is either trivial, a positive power |·|_p^s of the p-adic absolute value for a unique prime p and s>0, or a power of the ordinary absolute value with 0<s≤1. Thus the classification by the two nontrivial types must either assume nontriviality or include the trivial case separately. The completed archimedean proof is ours, since this leaf stops mid-argument.

**Reconstruction or textual qualification.** Include the trivial absolute value; complete the interrupted proof

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.26; research/SECOND_CHECKS.md H035.26.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Inserted typescript undated; authorship unestablished; folder catalogue dating is not a date for this leaf. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.27 — 94/013.1–7

> « c) »

**Our precise formulation.** Let A be noetherian Cohen–Macaulay local, Ω a finite module with the parameter-injective property in H035.18, and u:R→R′ a map of finite modules. If Hom(R′,Ω/qΩ)→Hom(R,Ω/qΩ) is an isomorphism for every parameter ideal q, then u is an isomorphism. The page assumes u surjective; our proof shows this assumption is unnecessary. A single parameter ideal does not suffice.

**Reconstruction or textual qualification.** All parameter systems are essential; surjectivity can be removed

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.27; research/SECOND_CHECKS.md H035.27.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.28 — 94/013.8–20

> « Corollaire 11 »

**Our precise formulation.** In the cancelled draft, let A=O_(X,x) for x∈U of Corollaire 10, Ω=Ω_x, and u:R→R′ a surjection of finite modules. Use the final rewritten functors Φ_R(M)=Hom(R,M), Φ_(R′)(M)=Hom(R′,M). If both commute on Ω with every parameter quotient and Hom(u,Ω) is an isomorphism, then u is an isomorphism. The page's regular-sequence comparison is stronger and implies the needed parameter comparisons because A is Cohen–Macaulay.

**Reconstruction or textual qualification.** Retain cancellation and separate rewritten definitions

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.28; research/SECOND_CHECKS.md H035.28.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.29 — 94/015.7–016.9

> « Corollaire 11 »

**Our precise formulation.** On an affine U with the finite canonical module Ω of Corollaire 10, suppose F=colim_i Hom(P_i,−), F(Ω) is finite, and its canonical comparisons with Ω_p/qΩ_p are isomorphisms for all p and all parameter ideals q. Eventual isomorphism of the transition maps requires finite P_i and a strict inverse system. Without strictness the zero-transition system P_i=k over a field satisfies the tests but is never stationary. With finite terms and surjective transitions, the system is eventually stationary and F is represented by its eventual term.

**Reconstruction or textual qualification.** Strictness and finite terms dropped in the rewrite; required for the explicit stage assertion

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.29; research/SECOND_CHECKS.md H035.29.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.30 — 94/016.10–017.22

> « Théorème 12 »

**Our precise formulation.** Let A be a noetherian quotient of a regular noetherian ring and F:Mod(A)→Sets. Then F=Hom_A(P,−) for a finite P if and only if: (i) F preserves filtered colimits; (ii) F preserves finite limits; (iii a) for every prime p and every finite A_p-hat module M, F(M)→lim_n F(M/(pA_p)^nM) is bijective; (iii b) for every a∈A and every finite module M over the (a)-adic completion of A, F(M)→lim_n F(M/a^nM) is bijective; (iv) F(M) is finite for every finite A-module M; (v) p↦dim_(k(p))F(k(p)) is constructible; (vi) for every nonzero quotient B of A and every finite B-module Ω, some nonnilpotent b∈B makes F(Ω)⊗_B B_p/q→F(Ω⊗_B B_p/q) bijective for every p∈D(b) and every parameter ideal q of B_p. The canonical module structures follow from (ii).

**Reconstruction or textual qualification.** Main question; repair dependencies without changing its hypotheses

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.30; research/SECOND_CHECKS.md H035.30.

**Literature:** No exact published match to all six axioms located; the proof in this run matches them. Hall2014 proves related geometric Hom representability under different hypotheses.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.31 — 94/017.23–26

> « Remarque 13 »

**Our precise formulation.** In H035.30 one may instead assume A noetherian with the property that every integral quotient B has a nonempty regular principal open. Under (i), (ii), (iv), (vi), condition (v) then follows; the full representability criterion remains valid with the two completion conditions and without a separate rank condition. The regular-quotient-of-a-ring hypothesis is not retained.

**Reconstruction or textual qualification.** Use (vi) with Omega=B and generic freeness

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.31; research/SECOND_CHECKS.md H035.31.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.32 — 94/018.1–25

> « Théorème 14 »

**Our precise formulation.** Let f:X→S be proper and finitely presented. Let F,G be finitely presented quasi-coherent O_X-modules and suppose G is flat over S. There is a finitely presented quasi-coherent P on S, with a natural isomorphism Hom_sheaf(P,M)=f_*Hom_sheaf(F,G⊗f^*M) for every quasi-coherent M on S. The representing object and isomorphism commute with arbitrary base change. Uniqueness is uniqueness respecting the representation.

**Reconstruction or textual qualification.** Arbitrary base change; Hall C,D and Example 3.10

**Status:** known; exact source matched and reduction proved. **Proof and check:** PROOFS.tex section H035.32; research/SECOND_CHECKS.md H035.32.

**Literature:** Hall2014, Theorems C–D p.4 and Example 3.10 p.18 of final author version; EGAIII2 7.7.8 p.70 has an extra source-presentation hypothesis, announced for removal in 7.7.9(iii) p.71.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.33 — 94/018.5m;024.17–21

> « passage à la limite »

**Our precise formulation.** Under H035.32, allow F to be arbitrary quasi-coherent, while G remains finitely presented and S-flat. The same representation and arbitrary-base-change result hold with P quasi-coherent, without a finiteness assertion. If locally F=colim_i F_i with finitely presented terms, then P=colim_i P_i in the same index direction.

**Reconstruction or textual qualification.** Filtered union of finitely presented modules, then colimit of representing modules

**Status:** known; exact source matched and reduction proved. **Proof and check:** PROOFS.tex section H035.33; research/SECOND_CHECKS.md H035.33.

**Literature:** Hall2014, Theorem C p.4 and Example 3.10 p.18; Stacks01PJ, Lemma 28.23.6.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.34 — 94/019.1–9

> « En fait »

**Our precise formulation.** Let A be a noetherian quotient of a regular noetherian ring, X proper over Spec(A), and F,G coherent on X. For each i,j≥0, the additive A-linear functors M↦H^j(X,Ext_sheaf^i(F,G⊗_A M)) and M↦Ext_X^j(F,G⊗_A M) satisfy H035.30(i),(iii a,b),(iv),(v),(vi). Tensor is underived and G need not be A-flat. Left exactness is not asserted and can fail. The claim does not identify this whole class with Auslander coherent functors.

**Reconstruction or textual qualification.** Underived coefficient tensor product must be retained

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.34; research/SECOND_CHECKS.md H035.34.

**Literature:** EGAIII1 4.5.1–3 pp.138–139; Stacks02OB 30.20.4 and Stacks02OC 30.20.5; Hall2014 Theorem E uses derived tensor, while Jaffe1997 section 7 pp.26–29 of 1994 version separates underived coherence.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.35 — 94/019.10–020.9

> « Lemme 15 »

**Our precise formulation.** Let X be of finite type over a noetherian ring A, F,G coherent on X, Ω a finite A-module, and N≥0. There is a dense open U⊂Spec(A) such that, for every p∈U, every A_p-regular sequence x, and 0≤i≤N, Ext_sheaf_X^i(F,G⊗_A Ω)⊗_A A_p/(x)→Ext_sheaf_X^i(F,G⊗_A Ω⊗_A A_p/(x)) is an isomorphism. Ext is computed using the original source F, so no unproved exactness of its base-changed resolution is assumed.

**Reconstruction or textual qualification.** Finite-type morphism and coherent coefficients over a noetherian base

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.35; research/SECOND_CHECKS.md H035.35.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.36 — 94/019.21–020.8

> « les K »

**Our precise formulation.** Let K be a bounded complex of A-modules and M an A-module. If Tor_i^A(M,K^j)=Tor_i^A(M,H^j(K))=0 for all i>0 and all j, then the canonical map H^j(K)⊗_A M→H^j(K⊗_A M) is an isomorphism for every j. There is no finiteness or flatness hypothesis beyond these Tor conditions.

**Reconstruction or textual qualification.** All positive Tor for terms and cohomology; explicit double-complex proof

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.36; research/SECOND_CHECKS.md H035.36.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.37 — 94/020.10–23

> « Lemme 16 »

**Our precise formulation.** Let X be of finite type over a noetherian ring A and R coherent on X. There is a dense open U⊂Spec(A) such that for every p∈U, every A_p-regular sequence x, and all i>0, the sheaf Tor_i^A(R,A_p/(x)) vanishes. The proof requires generic flatness of the finitely many graded coefficient pieces as well as the graded pieces of A. The inserted R/displayed F mismatch is definite; the first graded coefficient in the ink remains uncertain.

**Reconstruction or textual qualification.** R/F mismatch retained; the first graded coefficient remains uncertain. Our proof explicitly handles gr_J(R) and gr_J(A).

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.37; research/SECOND_CHECKS.md H035.37.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.38 — 94/021.1–21

> « Lemme 17 »

**Our precise formulation.** For a proper morphism X→Spec(A), with A noetherian and E coherent on X, there is a dense open U such that H^i(X,E)⊗_A A_p/(x)→H^i(X,E⊗_A A_p/(x)) is an isomorphism for all p∈U, all A_p-regular sequences x, and all i. The page's literal p∈S instead of p∈U is false: on P¹_(k[t]), the extension of O by O(−2) with class t has H⁰(E)=0 but H⁰(E_0)=k.

**Reconstruction or textual qualification.** Literal quantifier s in S is false; corrected s in U

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.38; research/SECOND_CHECKS.md H035.38.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.39 — 94/022.1–8

> « foncteur constructible »

**Our precise formulation.** Prospective constructible-functor programme. Our exact affine question takes additive A-linear functors Mod(A)→Mod(A), with A a noetherian quotient of a regular noetherian ring, satisfying H035.30(i),(iii a,b),(iv),(v),(vi), and asks whether their composition satisfies the same axioms. Filtered colimits, finite values, constructible ranks, and (vi) are proved stable. Only completion remains open. Full closure is proved for Dedekind domains and artinian rings; maximal-ideal completion is proved stable for countable A. Over a countable local A, finiteness over principal completions is also proved, leaving the inverse-system continuity problem.

**Reconstruction or textual qualification.** Exact affine composition class remains under investigation; do not substitute a smaller class

**Status:** open — completion closure unresolved. **Proof and check:** PROOFS.tex section H035.39; research/SECOND_CHECKS.md H035.39.

**Literature:** No exact theorem for this broad class verified. The smaller finite-Hom-presentation class is closed under composition, but equality with this class is unproved. See research/COMPOSITION_ATTEMPTS.md.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for proved reductions; no confidence claim of full closure.

### H035.40 — 94/022.4–8

> « Ext … Tor … R^q f_* »

**Our precise formulation.** The proposed two-scheme class Qcoh(Y)→Qcoh(X) is not defined on the page. The contextual affine realizations Ext_A^i(P,−), Tor_i^A(Q,−), for finite P,Q over a noetherian quotient A of a regular ring, and M↦H^q(X,E⊗_A M) for proper X/A and coherent E, satisfy the non-left-exact axioms of H035.30. An unqualified assertion for arbitrary direct image is false: A¹_k→Spec(k) sends O to k[t], violating finite values. The general two-scheme formulation and its composition properties remain open here; no unique definition is imputed to the manuscript.

**Reconstruction or textual qualification.** Unqualified direct image fails finite values without properness

**Status:** open — general two-scheme formulation; contextual examples proved. **Proof and check:** PROOFS.tex section H035.40; research/SECOND_CHECKS.md H035.40.

**Literature:** Hall2014, Theorem E p.4 (derived coefficients, different statement); Jaffe1997, section 7 of 1994 version; affine/proper realizations proved here.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for contextual examples and nonproper counterexample; broader scope unspecified.

### H035.41 — 94/022.10–023.8

> « Théorème 19 »

**Our precise formulation.** Let f:X→S be proper, flat and finitely presented, and let Z→X be affine, with no finiteness assumption on Z/X. Then T↦Hom_(X_T)(X_T,Z_T), for S-schemes T, is represented by an affine S-scheme, compatibly with arbitrary base change. Here Hom means sections over X_T, equivalently O_(X_T)-algebra maps from the pulled-back affine algebra to O_(X_T).

**Reconstruction or textual qualification.** Represent algebra maps by linear maps plus closed equations

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.41; research/SECOND_CHECKS.md H035.41.

**Literature:** Hall2014, Theorem D p.4 supplies the linear Hom cone; multiplicativity and unit equations are constructed here.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.42 — 94/022.13–15;023.1–8

> « de prés. finie (resp de type fini) »

**Our precise formulation.** Under H035.41, if Z→X is of finite type, its restriction of scalars is of finite type over S. If Z→X is finitely presented, its restriction is finitely presented over S. No noetherianity of S is required. The proof uses finitely presented module generators and, separately, finitely generated algebra relations.

**Reconstruction or textual qualification.** Separate the two finiteness assertions

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.42; research/SECOND_CHECKS.md H035.42.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.43 — 94/023.9–17

> « Corollaire 20 »

**Our precise formulation.** Under H035.41, a closed immersion Z→Z′ of affine X-schemes induces a closed immersion between their representing S-schemes of sections. The assertion permits arbitrary quasi-coherent defining ideals and arbitrary base changes; it does not assert finite presentation of the closed immersion.

**Reconstruction or textual qualification.** Reduce by universal section to the closed-subscheme condition

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.43; research/SECOND_CHECKS.md H035.43.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.44 — 94/023.18–24.6

> « premier cas »

**Our precise formulation.** For f:X→S proper, flat and finitely presented, the restriction of the linear cone V(F)=Spec_X Sym(F) is V(P_F), where P_F represents Hom(F,O_X⊗f^*M), with f_* inserted in the sheaf formula on S. F may be quasi-coherent; finite presentation of F gives finite presentation of P_F. Calling V(F) a vector bundle for coherent F is false in general: F=A/(t) over A=k[t] gives A[x]/(tx). Every affine finite-type X-scheme embeds in such a cone with finitely presented F when X is quasi-compact and quasi-separated.

**Reconstruction or textual qualification.** Coherent need not be locally free; formula needs f_*

**Status:** false as written; corrected statement proved. **Proof and check:** PROOFS.tex section H035.44; research/SECOND_CHECKS.md H035.44.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.45 — 94/024.7–16

> « Murre, th. 3 »

**Our precise formulation.** Let X→S be proper, flat and finitely presented, and Y⊂X a closed subscheme with arbitrary quasi-coherent ideal. The subfunctor of S consisting of T→S for which Y_T=X_T is represented by a closed subscheme of S, compatibly with all base changes. This is the proper special case of Murre exposition 294, Theorem 3, p.255, after the manuscript's noetherian reduction; our proof removes the noetherian-base restriction.

**Reconstruction or textual qualification.** Murre exp.294 Theorem 3, printed page 255, hypotheses matched

**Status:** known; exact source matched and reduction proved. **Proof and check:** PROOFS.tex section H035.45; research/SECOND_CHECKS.md H035.45.

**Literature:** Murre294, Theorem 3 p.255; SGA3VIII, Theorem 6.4 pp.18–19 in 2009 revision uses essentially-free morphisms, a different hypothesis.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

### H035.46 — 94/024.17–21

> « Remarque 21 »

**Our precise formulation.** For f:X→S proper, flat and finitely presented and any quasi-coherent F on X, the restriction of scalars of V(F) is a linear cone V(P) for a quasi-coherent module P on S. Locally, if F=colim_i F_i with finitely presented terms, P=colim_i P_i and V(P)=lim_i V(P_i). No finite-type conclusion is asserted for arbitrary F.

**Reconstruction or textual qualification.** General quasi-coherent coefficient, no finiteness claim

**Status:** proved in the explicitly stated reconstruction. **Proof and check:** PROOFS.tex section H035.46; research/SECOND_CHECKS.md H035.46.

**Literature:** Complete proof in this run; standard inputs are identified in PROOFS.tex and references.bib.

**Date:** Undated; catalogue: [à partir de 1965]; no exact page date. **Confidence:** High for stated mathematical reconstruction; disputed ink separately graded in READINGS.tsv.

## 4. Groundwork beside the manuscript

### The proof of the central criterion

**Our proof structure.** First recover finite representers after localizing
at each prime, using the completed-local condition and artinian Matlis
duality. Constructible residue rank then gives generic representation on
integral quotients, because Theorem 12(iv) supplies precisely the finite-value
hypothesis missing in Remarque 5 bis. The minimal-support argument produces
a strict system of finite modules representing the functor pro-objectwise.

Next choose a finite module Ω canonical on a **dense** open. Density matters
on a reducible base: it guarantees intersection with the merely nonempty
open furnished by (vi). On that intersection, finite F(Ω) and the parameter
comparisons make the strict system stationary. The repaired Corollaire 11
uses a commutative square whose right vertical map is injective by strictness;
surjectivity follows from the upper comparison. It does not assume base
change for each individual Hom stage. Finally Proposition 3's noetherian
induction and principal-completion gluing return a finite representer on A.

The proof passes the axioms to quotient rings, using exactness of noetherian
completion. It does not assume that arbitrary localization commutes with
completion. It uses the valid regular-embedding/Gor-2 version of the
canonical-module assertion, not the false CMU-only enlargement. Nor does it
use the false Z¹ two-Tor criterion. These distinctions are why the theorem
survives defects in several intermediate drafts.

### Standard inputs, with checked locators

| Input | Role | Opened source or proof |
|---|---|---|
| Finite-limit preservation and canonical linearity | Turns the set-valued functor into an A-linear functor and supplies the canonical tensor maps. | Direct diagrams, PROOFS.tex H035.2; no extra hypothesis hidden. |
| Flat modules as filtered colimits of finite free modules | Flat scalar extension for additive finitary functors. | [Stacks 058G, Theorem 10.81.4](https://stacks.math.columbia.edu/tag/058G). |
| Faithfully flat module descent | Descends local/completed representing modules and their finiteness. | [Stacks 023N, Proposition 35.3.9](https://stacks.math.columbia.edu/tag/023N); H035.3 gives the equalizer reduction. |
| Exactness and flatness of noetherian completion | Quotient inheritance and completed-module gluing. | [Stacks 00MB, Lemma 10.97.2](https://stacks.math.columbia.edu/tag/00MB); H035.4 gives compatible presentations. |
| Artinian Matlis duality | Finite representers from the injective cogenerator; parameter Hom detection. | [Stacks 08Z9, Proposition 47.7.8](https://stacks.math.columbia.edu/tag/08Z9). |
| Krull intersection | All parameter-power tests detect a zero kernel. | [Stacks 00IP, Lemma 10.51.4](https://stacks.math.columbia.edu/tag/00IP). |
| Canonical modules and CM duality | Interprets Ω and its regular/parameter quotients. | [Stacks 0DW3](https://stacks.math.columbia.edu/tag/0DW3), [0DW4](https://stacks.math.columbia.edu/tag/0DW4), and [0B5A, Lemma 47.16.7](https://stacks.math.columbia.edu/tag/0B5A); H035.16–18 give the quotient arguments. |
| Relative generic freeness | Handles coherent coefficients finite over finite-type algebras, not necessarily finite over the base. | [Stacks 051S, Lemma 10.118.2](https://stacks.math.columbia.edu/tag/051S); H035.11–12 and H035.37 give the nilpotent-filtration argument. |
| Proper formal functions in the pro-category | Makes higher underived Ext commute with the actual formal-module tests. | [Stacks 02OB, Lemma 30.20.4(1),(3)](https://stacks.math.columbia.edu/tag/02OB) and [02OC, Theorem 30.20.5](https://stacks.math.columbia.edu/tag/02OC); H035.34 spells out the spectral-sequence step. |
| Quasi-coherent approximation | Extends Hom representation from finite presentation to arbitrary quasi-coherent source. | [Stacks 01PJ, Lemma 28.23.6](https://stacks.math.columbia.edu/tag/01PJ). |

All uses have individual check events. Sources checked only as background
are labeled as such in `CHECK_EVENTS.tsv`; opening or reading a page is
not recorded as an independent proof of its contents.

### Corrections that change the mathematics

The most substantial false assertion before the main theorem is the
converse in Remarque 5 bis. The flat module Σ_p(1/p)Z has free rank-one
localizations at every prime and constant residue rank, but it is not finite
on any nonzero principal open. The proof on the page explicitly invokes
finite generation of F(N), which its earlier hypotheses do not provide.
Theorem 12(iv) repairs this without changing that theorem.

The two errors on scan 10 are independent. The Hom complex needs Q as its
coefficient, while the written P gives the wrong dimensions even over a
field. Separately, Tor₁ with cycles Z¹ is insufficient: the explicit
k[x,y]/(xy) example satisfies both written vanishings and fails base change.
Using the boundary module B¹, or the specified stronger Tor₂ condition,
repairs the criterion. The generic Hom theorem itself is true.

The CMU margin is false for a different reason. Cohen–Macaulayness of a
dense open in every integral closed subset does not provide a generic
canonical module. The explicit noetherian one-dimensional example in
H035.21 has non-Gorenstein local rings in every open; modulo its local
parameter t³, the socle has basis t⁴,t⁵. A finite generic rank-one canonical
module would be free on a smaller open, contradicting that socle dimension.
The valid uniform replacement is Gor-2; excellence implies it.

Other literal defects are kept separate: the zero quotient in Proposition 3,
zero f in Lemme 5(v), lost strictness in the rewritten Corollaire 11, “s∈S”
instead of the dense open in Lemme 17, the missing pushforward in the cone
formula, and coherent modules called vector bundles. The absolute-value
leaf has its own normalization, positive-exponent and nonzero-element
issues; those do not belong to the representability argument.

## 5. What became of these claims

### Published mathematical counterparts

The folder's loose dating does not establish that every sheet precedes or
follows a particular publication. The table identifies exact mathematical
counterparts and differences, not an undocumented chain of influence.

| Date | Opened source | Exact relevance |
|---|---|---|
| 1961 | [EGA III₁, 4.5.1–3, pp.138–139](https://www.numdam.org/item/PMIHES_1961__11__5_0.pdf) | Coherent Ext and formal completion. The pro-Artin–Rees argument in H035.34 retains the stronger underived coefficient formulation being checked here. |
| 1963 | [EGA III₂, 7.7.6–9, pp.69–71](https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf) | Hom representation with a source-presentation hypothesis in 7.7.8; 7.7.9(iii) announces removing it. It is not an exact certificate for unrestricted Theorem 14. |
| 1965 | [EGA IV₂, 6.11.8 and Remarques 6.11.9, pp.162–163](https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf) | The exact margin reference establishes CMU consequences. It does not establish canonical-module existence. |
| May 1965 talk; 1966 volume | [Murre, exposition 294, Theorem 3, p.255](https://www.numdam.org/article/SB_1964-1966__9__243_0.pdf) | The cited closed condition Y_T=X_T under flat finite type and the adic condition, including properness. |
| SGA 3; checked 2009 revision | [Exposé VIII, Theorem 6.4 and Corollary 6.5, pp.18–19](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp8-8nov09.pdf) | A related closed-condition theorem for essentially-free morphisms. Its hypothesis is recorded as different. |
| 1994 preprint; 1997 publication | [Jaffe, section 7, pp.26–29 of the opened preprint](https://arxiv.org/pdf/alg-geom/9410009) | Proper flat and Dedekind positive cases, and a nonflat underived-cohomology obstruction to coherence. This prevents replacing all the manuscript's functors by the finite-Hom-presentation class. |
| 1997 lecture; full article cited there in 1998 | [Hartshorne, section 2, pp.88–89](https://www.mate.polimi.it/smf/vol67/hartshorne.pdf) | The finite-Hom-presentation category is abelian. Its composition closure follows by a finite presentation of the outer Hom argument. The lecture also distinguishes nonflat cohomology. |
| 2014 | [Hall, Theorems C–D p.4, Example 3.10 p.18, final author version](https://bpb-ap-se2.wpmucdn.com/blogs.unimelb.edu.au/dist/5/501/files/2021/05/coho_bc.pdf) | Matches the full proper Hom result, including quasi-coherent first argument and flat finitely presented target. Theorem E concerns derived tensor and must be distinguished from H035.34. |
| 2025 | [Lyu, Corollary 4.7 p.225, Lemma 6.1 and Theorem 6.2 p.230](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/formal-lifting-of-dualizing-complexes-and-consequences/5B440834E8251BAF3DA3752276F6C31B) | Gives the precise canonical-module spreading result used for the Gor-2 reconstruction. Remarks 7.7 and 7.9 p.233 explain why CMU and excellence must be handled with care in stronger duality questions. |

The exact six-axiom statement of Theorem 12 was not found as a matching
published theorem in the sources checked; it has a complete proof here.
This is not a novelty claim. The search covered Numdam, arXiv, MathOverflow,
EGA/SGA, collected-text indexes and author bibliographies. zbMATH Open was
attempted twice but was inaccessible. Failed searches and unmatched modern
terminology are not evidence that an assertion was never published.

### The remaining composition problem

For the explicit affine class in H035.39, every axiom except completion
is proved stable under composition. The generic condition can be upgraded
from a nonempty open to a dense open component by component, so reducible
bases no longer present an obstruction. For a finite module M over a
completion C, the remaining comparison is

\[
F(G(M))\longrightarrow\varprojlim_n F(G(M/I^nM)).
\]

It is not legitimate to apply F's completion axiom immediately: its input
G(M) must first be controlled over C, and the inner tower need not already
be its ordinary adic quotient system. The proofs establish the entire
assertion over Dedekind domains and artinian rings. Over countable A they
establish maximal-ideal completion; over countable local A they also
establish finiteness of outputs on finite principal-completed modules.
The principal-adic continuity issue remains in dimension two.

The direct torsion-weight counterexample attempted over k[[x,y]] fails
the original hypothesis at p=(x), so it is explicitly rejected. Replacing
the class by coherent functors, assuming arbitrary finite inverse systems
are Mittag–Leffler, or applying flat base change to nonalgebraizable
formal modules does not close the argument. The exact failed steps and
next attacks are in `research/COMPOSITION_ATTEMPTS.md`. “Open” here means
unresolved in this run; no claim is made that it is an established open
problem in the literature.

## 6. Links to other catalogue objects

`LINKS.tsv` contains its header and no asserted relation. The supplied
catalogue places H038 (local cohomology and duality), H02M (Hilbert schemes,
norms, Tor and Ext), and H03A (scheme-valued functor gluing) nearby. That is
evidence of thematic proximity, not a checked “uses,” “same question,” or
generalization relation between the relevant passages. No cross-object
claim has been manufactured from the shared vocabulary.

H02X is a documentary object that includes the local-fields report in cote
94. It is not a supplied mathematical tag for the absolute-value assertions
on scan 12. Those rows are explicitly marked off object, with their correct
mathematical subject named and no invented tag.

## 7. Verdicts on the six supplied entries

Every entry was read in full, independently of its sweep placement.
`NOTES_VERDICTS.tsv` gives an anchor, mathematical verdict, placement and
reason for each of its 44 subclaims.

| Entry | Subclaims | Verdict in brief |
|---|---:|---|
| work:K94-01#1 | 14 | Broadly faithful descriptive overview, but it silently supplies “nonzero” in Proposition 3 and does not expose the missing hypothesis in 5 bis, the false Tor criterion, or the absolute-value defects. The inserted arithmetic leaf is outside H035. |
| work:K94-01#2 | 9 | Correctly identifies many missing proofs. The two-Tor item is false as written, so “unproved” is insufficient; the others receive proofs with their exact qualifications. |
| work:K94-01#3 | 3 | The possible question mark remains uncertain; the reformulation margin is confirmed. Its no-other-conjecture statement is confined to scans 2–13; the later programme is now included. |
| work:K94-01#4 | 7 | P/Q and nonzero root-of-unity corrections confirmed. The undefined coefficient is identified. Singular agreement is editorial; the final curl and cancelled-preposition claims remain uncertain on the ink. |
| work:K94-01#5 | 7 | Internal dependencies and exact EGA and Bourbaki pointers checked. The EGA citation does not justify the marginal enlargement. The unspecified valuations chapter remains unidentified. |
| work:K94-01#6 | 4 | Proof-order arrow and Tor linkage confirmed with the false criterion isolated. The s/n index and overwritten Hom definitions retain their uncertainty; no convention change is inferred. |

The supplied CHECKS.tsv contained no prior mathematical check rows. This
run's events distinguish computation, targeted proof checks, exact-source
matching, and background use. The model is GPT-6 Astra Pro; the environment
does not expose the reasoning-effort setting, so no “max” setting is claimed.

## 8. Our research results bearing on this object

The results attachment remains closed at this stage. This complete pre-results entry records the archive reading and mathematical assessment before those claims are consulted. A dated opening event and evidence-only comparison will be added in the next phase.

---

Entry generated at 2026-11-19T04:57:19.455652+00:00. Detailed state and mandatory reviews: PROGRESS_LEDGER.md. All cited works and verification qualifications: references.bib.

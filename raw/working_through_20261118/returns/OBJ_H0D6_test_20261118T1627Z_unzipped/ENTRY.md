INCOMPLETE

# H0D6 — formally simple algebras, Cohen algebras, and open questions

## Object and scope

Grothendieck's terms are *algèbre de Cohen*, *formellement simple*, *algèbre universellement régulière*, and *topologie discrète / topologies habituelles*. In today's terminology the principal setting is a local homomorphism of Noetherian local rings and the formal-smoothness/formal-simplicity criteria expressed through flatness and the fibre over the residue field. The archive tag H0D6 is the narrower dossier of the open questions 1–4, with the Cohen-algebra discussion that motivates them.

The relevant material in cote 22 is in scan order: scan 14 (existence of Cohen algebras and a remaining infinitesimal lifting problem); scans 17–18 (Corollaries 4.12–4.13 and editorial remarks); scan 20 (Questions ouvertes 1 and 2); scan 21 (Questions 3 and 4); scans 22–25 (notes on the discrete topology and a proposed obstruction using differentials). Scans 26–27 continue the differential discussion. Scan 19 is a cover. Scan 28 begins a separate typescript on repartitions, idèles, divisors and their topologies; scans 28–30 of that typescript are not evidence about H0D6 and are excluded from the mathematical statements below. Scan 27's field example is part of the differential discussion, but its exact construction is not needed for the settled EGA comparisons below.

The supplied passage transcriptions identify manuscript pages 28, 31–32 for scans 14, 17–18, and pages 18 onward for the handwritten questions. No reliable date is written on these cited sheets. The folder catalogue dates the folder broadly 1963–[circa 1967]; this is not a date for an individual statement.

## Grothendieck's statements and present status

### H0D6.1 — fibre criterion / universal regularity (22/020; Corollary 4.13 on 22/018)

His question 1: “Est-il vrai que A formt simple sur k si A est univt régulière sur k” (22/020; the scan's abbreviations are retained). The nearby “OK” is a marginal annotation, not a proof.

Today's precise field-base version: for a field k and a Noetherian local k-algebra A with its preadique topology, formal smoothness of A over k is equivalent to geometric regularity over k; equivalently, A⊗k k' is regular for every finite extension k'/k with k'^p⊂k (p the characteristic exponent). This is EGA 0_IV, 22.5.8. Thus the field-base implication asked in question 1 is **known/proved in EGA**, under these hypotheses. Do not extend the verdict to every broader formulation on the handwritten line without matching its local-map hypotheses.

Corollary 4.13 on 22/018 states a relative criterion: for a local map A→B of Noetherian local rings, under the residue-extension hypothesis “multiplicité radicielle finie” (or the handwritten alternative r(B)=r(A)B), formal simplicity of B over A is equivalent to flatness over A and universal regularity of B₀=B⊗A k over k. The page's proof reduces to the complete case and cites earlier results 4.11/3.12 and 3.6. The supplied EGA 0_IV, 19.7.1 is a formally-lisse analogue, not by itself an exact verification of every qualification in the manuscript's formal-simplicity formulation. **Status: not independently proved here; the field-base implication is known as above.**

### H0D6.2 — change to the discrete topology (22/020, continued 22/022–025)

His question 2: whether an algebra formally simple for its usual local topology remains so for the discrete topology; he asks separately about the complete case. The page records a tentative characteristic-dependent guess, then a heavily marked “Faux”/doubtful margin. The exact attachment of that marginal correction is unresolved.

Today's precise statements:
- In the finite-type situation of a k-algebra C, with k/k₀ separable as in EGA 0_IV, 22.6.7(i), the locus of primes p for which C_p is formally smooth over k₀ for the discrete topology equals the locus for the p-adic topology, is the geometrically regular locus, and is open. This is a **proved special case**, not a general answer to the manuscript's question.
- The manuscript's proposition on 22/024 asserts: if Ω¹_{K/k} has infinite K-dimension and A=K[[t₁,…,tₙ]], n>0, then A with the discrete topology is not formally smooth over K relative to k (hence not over k). The proposed proof on 22/024–025 is **incomplete**: the final series f=Σaₙtⁿ is proposed, but the text stops at dots and does not establish all coefficient/component requirements. No proof is claimed here.
- The EGA 0_IV, 22.5.10(i) example shows that testing only monogenic purely inseparable extensions does not suffice for the geometric-regularity criterion. It is not, without further argument, a counterexample to the full discrete-versus-preadic question.

**Status: open in this return beyond the finite-type/separable case; manuscript proposition unproved here.**

### H0D6.3 — openness of the formally simple locus in fibres (22/020–021)

His question 3 asks whether the locus of points in Spec B at which the fibre local ring is formally simple over the residue field is open. The next sheet separately asks “stable par localisation ?” and has further qualifications involving generization/neighbourhoods.

The field-base localization statement is proved in EGA 0_IV, 22.5.9: if A is a Noetherian local k-algebra formally smooth for its preadic topology, then A_p is formally smooth for the p-preadic topology for every prime p. The proof uses 22.5.8 and the fact that A_p⊗k k' is a localization of the regular ring A⊗k k'. EGA 0_IV, 22.5.10(ii) explicitly records the openness question for the locus {p | A_p formally smooth over k} and says that only certain special cases will be treated later. EGA 0_IV, 22.6.7(i) proves openness for finite-type algebras over a separable field extension by identifying the locus with the geometrically regular locus.

**Status: localization stability is proved for the field-base formal-smoothness setting; openness is proved in the finite-type/separable case. The full relative fibre-locus question as written on 22/020–021 is not settled by these references.**

### H0D6.4 — openness of the flat locus (22/021)

His question 4: “Lieu des pts de Spec B en lesquels B est plat sur A est-il ouvert?” The note then proposes a reduction involving primes p⊂A, q⊂B and an open nonempty subset after passing to primed rings.

Today's precise general statement is the openness of {q∈Spec B | B_q is flat over A_{q∩A}} for a homomorphism of Noetherian rings A→B. The supplied passages of EGA 0_IV, 19.7.1 concern a local flatness/formal smoothness criterion, not this arbitrary-map openness assertion. The manuscript's reduction is not fully legible/verified and no proof or counterexample is supplied here.

**Status: open in this return.** The exact reduction and its hypotheses require a fresh scan-level and mathematical check.

## Groundwork and context

- EGA 0_IV, 19.7.1: for Noetherian local rings A,B and a local map, formal smoothness of B over A is equivalent to flatness of B over A together with formal smoothness of the fibre B₀ over k. This is the local formal-smoothness criterion, not a substitute for every statement about “formellement simple”.
- EGA 0_IV, 22.5.8: over a field, formal smoothness for the preadic topology is equivalent to geometric regularity, and to regularity after all finite extensions k'/k with k'^p⊂k.
- EGA 0_IV, 22.5.9: localization preserves the field-base formal-smoothness property.
- EGA 0_IV, 22.5.10(ii): explicitly poses the openness question for the field-base formally smooth locus.
- EGA 0_IV, 22.6.7(i): for finite-type C over a separable extension k/k₀, the formally smooth locus for the discrete topology, the preadic topology and the geometrically regular locus coincide and are open.
- Scan 14 explicitly says the general Cohen-algebra existence problem reduces by successive lifting to an infinitesimal/square-zero problem and that the author does not know whether a solution always exists. EGA 0_IV, 19.7.2 treats a complete-local lifting situation; EGA 0_IV, 19.7.3(i) preserves a question about weakening completeness to the base-ideal topology. These are distinct formulations and must not be conflated.

## What became of the questions

The published EGA material answers the field-base equivalence and localization questions in 22.5.8–22.5.9, records the openness problem in 22.5.10(ii), and proves a finite-type/separable openness theorem in 22.6.7. The exact broad relative versions in the handwritten notes are not all identical to those published statements. The discrete-topology problem is treated in a special finite-type setting in 22.6.7, while the infinite-differential proposition on scans 24–25 remains unfinished on the manuscript page and is not promoted here to a theorem.

## Nearby objects

OBJECTS_NEARBY.tsv identifies H0D5 as the broader EGA 0_IV formally smooth/formally simple/Cohen-algebra dossier; H0D7 as derivations, p-bases and infinite support on scans 22–25; and H0D9 as the counterexample on scans 27–29. These are documentary/topic relations, not proofs of H0D6 statements. H0D4 concerns trace and norm for finite morphisms and the divisor/idèle typescript; it is the better home for the unrelated scan 28–30 material.

## Entry verdicts

There are 13 sweep entries. The two substantive groups that belong to H0D6 are: (i) the Cohen-algebra and questions/differentials material on scans 14, 17–25; (ii) the A13–A17 entries on questions 1–4. The codex entry has no text in its source file. The broad Work summary also includes scans 28–30 on divisors, repartitions and idèles; those passages begin a separate subject and are not H0D6 statements. The complete row-by-row decisions are in NOTES_VERDICTS.tsv. No entry is silently treated as a verified mathematical result.

## Our runs

See CONSEQUENCES.tsv. The source archive is opened only after this entry was written. Its rows are reports of earlier runs, not mathematical verification.

## Confidence and limitations

High confidence in the literal core questions 1–4 and in the cited EGA theorem statements, because the second reading and the supplied French EGA source were inspected. Medium confidence in the reconstruction of the full relative scope of questions 1, 3 and 4. Low confidence in the attachment of the marginal “Faux” on scan 20 and in the exact reduction under question 4. The overall entry is incomplete: the discrete-topology proposition, general relative openness questions, all independent proofs/counterexamples, full per-entry audit, and some manuscript reading decisions remain unresolved.

# Continuous cote100 Codex witness audit

Completed on 2026-11-19 against root claims C-SA04-655–687. This is a textual and hypothesis comparison. It is not a new proof check or a new literature search. All four supplied Codex transcription files were read continuously, including cancellations, margins, reused typescripts and administrative matter. Pro remains the principal supplied witness. No physical scan was available for deciding competing readings.

## Coverage

| Source file under SA04_texts/codex | Lines read | Scan labels present | Content checked against root register |
|---|---:|---|---|
| K100-01_transcription.tex | 1–304, all | 2–14 | Initial abelian/BT extension theorem, closed algebraicity locus, effectiveness reductions, GIT quotient/base-change sheets, detached errata, SL2 example and beginning of Gm properness lemma; C655–657, C677–678, C685, C687. |
| K100-02_transcription.tex | 1–336, all | 15–27 | Local-system gluing doubts, uniform-neighborhood lemma, EGA proof corrections, closed algebraicity criterion, proper-epimorphism descent, GIT example/orbit properness, effective-descent reductions and 1963 preface attribution; C656–664, C677–679, C683–685. |
| K100-03_transcription.tex | 1–251, all | 28–40 | GIT definitions, formal-moduli descent, Illusie letter, algebraization and polarization loci, component gluing, smooth nilpotent lifting, Baire argument, Mumford conjectures and EGA letter; C664–669, C679–686. |
| K100-04_transcription.tex | 1–394, all | 41–46, 48–53 | Picard hypotheses and projective algebraization, EGA corrections, proper-flat descent, full Néron/BT typescript and its handwritten strengthening; C670–676, C683–685. |

The four files total 1,285 lines. There is no scan47 label in these four files; this records the supplied file structure and does not infer the contents of a missing physical page. The initial combined display of files01/02 was truncated; the affected portions were read again separately, so the attestation includes the full text rather than merely the saved output.

Saved full-file or complementary read outputs are:

- `outputs/read_K100-01_transcription_1_304_20261119T024534304532.txt`, supplemented by the separate read of lines161–304.
- `outputs/read_K100-02_transcription_1_336_20261119T024534304504.txt`, supplemented by the separate read of lines1–163.
- `outputs/read_K100-03_transcription_1_251_20261119T024558366958.txt`.
- `outputs/read_K100-04_transcription_1_209_20261119T024621240540.txt` and `outputs/read_K100-04_transcription_210_394_20261119T024629049700.txt`.

The source SHA256 values are `c4f00e5e2dd11f7fbdf4e58097662a006083cb8708136050674388e6a23d8776` (01), `2207395853ba313e573de58f2fde58b128a03b076c280924a52ff64ab9c4eb31` (02), `17c43dffc05b93e6dc681da3e1ac36c4aaa9495644ef314e506b8aa291697b9f` (03), and `e622b76ca41f2dc54fb80aa383f3c1a96a10853264a9097e0a44bae6a5828113` (04).

## Corrections to the root register

### 1. C686 has the wrong scan and line locator

The Illusie letter dated 24 February1968 is **scan30**, not scan32, in both witnesses. Its locators are Codex K100-03:40–59 and Pro:2029–2048. Pro:2077–2097, currently attached to C686, is scan32 and contains the GIT convention sheet and group-scheme associativity definition. This is a root-register locator error, not a disagreement between witnesses. Correct C686 and the corresponding item; in C677's broad GIT source list, use scan32 for this definition sheet and do not count the Illusie letter as a GIT theorem.

### 2. C672 and C676 should preserve the general Néronian target

Codex K100-04:217–220 and Pro:2429–2430 bracket the initial semiabelian generic-fibre hypothesis and label the bracket unnecessary. The later handwritten argument, Codex K100-04:375–393 and Pro:2539–2545, explicitly starts with an arbitrary Néronian group scheme. It says that its generic fibre has no subgroup isomorphic to Ga **because that generic fibre admits a Néron model**, and then factors the BT image through a semiabelian subgroup. Thus C676's current explanation based only on a semiabelian assumption is weaker than the manuscript's actual argument. C672 should distinguish the initial restricted statement from this subsequent broadening. The exact broad published counterpart is already documented in `SGA7I_primary_memo.md`, IX Remark5.9.1. This comparison does not itself prove the no-Ga assertion or the factorization lemma.

### 3. Preserve the restricted Tate subclaim within C673

Codex K100-04:325–330 and Pro:2501 both acknowledge that the two uses of the general Tate theorem are rigorously available there only in generic characteristic zero. They also say that the étale-target case is easy, and that the author now knows the theorem when the connected part of the generic target is of multiplicative type. This restricted claimed result should remain visible within C673's source assessment. It is not an assertion that the manuscript has proved unrestricted equal-characteristic full faithfulness.

No new claim or item ID is required for these three corrections: the existing root records contain the relevant subject and should preserve its exact source scope.

## Substantive reading alternatives

These alternatives are supplied separately in `c100_witness_readings.tsv`. They are reasons to inspect the physical scan, not authority to overwrite Pro.

| Scan and subject | Pro reading | Codex reading | Mathematical consequence |
|---|---|---|---|
| 29, residue-field descent | Pro2012 has an opaque reading resembling “une galère.” | K100-03:34 reads that the morphism has a section. | A section explains the claimed universal effective descent, under the preceding algebraically closed residue-field reduction. It is a strong mathematical reading candidate, not an ink decision. |
| 33, polarization locus | Pro2107 gives “ouvert et fermé,” while2109 separately deletes “fermé.” | K100-03:120–126 gives an induced open subscheme and separately cancelled “fermé.” | Preserve the correction state of the openness/clopenness description; the later finite unramified pieces are a separate assertion. |
| 41, condition(iv) | Pro2292: “rationnellement projectif.” | K100-04:28–30: “algébrique et projectif.” | The strength of the componentwise algebraization/projectivity condition differs. C670 must retain this uncertainty rather than silently identify the predicates. |
| 43, formal descent hypotheses | Pro2345 joins absence of infinitesimal automorphisms to enough sections with “et”; the sections are read “plates par descente.” | K100-04:98–104 uses “ou” and reads sections stable under descent. | The two conditions may be alternatives or simultaneous hypotheses. A safe modern reconstruction cannot erase this difference. |
| 45, cover in the projectivity argument | Pro2385 favors a projective surjective cover. | K100-04:153 leaves “projectif” versus “quasi-fini” uncertain. | Projective and quasi-finite are different hypotheses; retain the alternative in C671's source qualification. |

## Hypotheses confirmed by the second witness

The initial theorem keeps the locally noetherian base, the characteristic-p complement, and the requirement that U meet every connected component. Its effectiveness part separately uses the finite geometrically unibranch cover and depth/third-face condition. Codex K100-01:8–27 agrees with the scope of C655–656. The shorthand diagram on scan5 is not grounds for replacing the initial global BT datum by a group only on the closed complement.

The proper-epimorphism argument distinguishes descent of morphisms from effective descent of objects. The finite/integral radicial corollary retains its alternatives: finite with locally noetherian base, or a target locally of finite type. Codex K100-02:191–234 and259–273 supports C661–663's qualified treatment. The local-ring system lemma remains explicitly doubtful and probably false at K100-02:46–52; the uniform-neighborhood quantifiers at84–87 remain as in C660.

The Picard passage retains flatness of Pic0 on the infinitesimal thickenings, with smooth special-fibre Pic0 as a sufficient example. Its margin changes the finite unramified/étale-cover formulations to finite flat ones when that smoothness fails, explaining that a polarization need not itself be an invertible sheaf. Codex K100-04:3–33 and Pro2270–2295 agree on this qualification. The separate claim about pairs with an invertible sheaf on scan45 does not explicitly assume that sheaf ample; adding positivity is a proposed repair, not a transcription.

The EGA edits at K100-04:39–65 agree with Pro2305–2325: dropping the noetherian hypothesis is accompanied by local finite presentation in15.6.3/15.6.4 and quasi-separatedness in15.6.4. The same paragraph claims compatibility of universal openness of finite-presentation morphisms with projective limits. That precise additional scope can be retained within C684. The detached scan12 errata remain unattributed; Codex does not supply a title or enough missing hypotheses to promote their fragmentary assertions into identified standalone theorems.

The GIT witness retains the exact Example0.4 data: nonzero linear form, quartic equal to the square of a quadratic of discriminant1, trivial stabilizers, the quotient formula, and the explicit nonclosed action-map image (K100-02:17–35; K100-01:274–289). Lemma0.5 still assumes an equivariant projective immersion (K100-01:292–304). The correction from a closed immersion to a monomorphism in the terminology of a free action is retained at K100-01:199–203. No extra Codex-only theorem or new counterexample was found.

## Result

The continuous Codex check supplies one definite locator correction, a necessary preservation of the final Néronian scope, a restricted Tate subclaim, and five substantive reading alternatives. It supplies no new independently proved mathematics. No IDs in the reserved C726–739 or item667–679 ranges were used. The twelve check events are recorded as textual comparisons only in A's main event ledger and separately in `c100_witness_events.tsv`. The latter is an exact subset, so final assembly must not append it a second time if it already imports A's full ledger. No continuous-read omission remains in these four supplied Codex files.

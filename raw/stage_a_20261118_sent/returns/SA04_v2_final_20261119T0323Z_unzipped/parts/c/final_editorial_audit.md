# Final dossier editorial audit: C sequence

This review read §§3.6, 4, 5, 9 and 10 of `final/SA04_dossier.md` against the C claim register, source passages and detailed proof analysis. The main dossier was not edited. The following were concrete corrections, all independently confirmed applied in the final mainbody after the coordinating agent’s 03:09:36 UTC assembly notice. They are not a renewed audit of unrelated mathematical topics.

| Location in reviewed draft | Defect | Exact correction and evidence |
|---|---|---|
| §3.6, square-zero paragraph | The opening omits the base and relative hypotheses used by the Cartan proof. | Say “For local smooth lifts across a base square-zero thickening, the difference of comparison maps is a relative derivation. Cartan contraction supplies the homotopy between the relative de Rham maps.” C-SA04-419–420; C analysis §3; P93 lines318–373. |
| §4, printed-argument paragraph | Range C-SA04-424–450 includes the handwritten comparison-category claim450. | End the printed range at449. |
| §4, handwritten comparison-category paragraph | Range451–454 omits the category/Tate-curve claim450. | Use C-SA04-450–454. |
| §4, nonabelian paragraph | The torsor-to-homogeneous-space correction is460, absent from456–459. | Use C-SA04-456–460. |
| §5.1, finite-local-freeness paragraph | Current references468–470,475–476 do not locate the nonflat counterexample or permutation-module invariant argument. | Use C-SA04-465–466,468,472. C465 gives the nonflat section counterexample;466 preserves the already-qualified scheme premise;468 is symmetric descent;472 is invariant orbit sums. |
| §5.1, degree-axioms paragraph | The unfinished contracted product is475, outside471–474; Rydh §6 addresses Hilbert–Chow rather than the empty-degree contradiction. | Extend the claim range through475. Remove the Rydh citation here, or explicitly add the distinct Hilbert–Chow comparison C-SA04-476 and attach Rydh §6 to it. |
| §5.2, group-set category | “Finite-orbit G-sets” can mean finite orbit cardinalities, which is a different category. | Say “G-sets with finitely many orbits.” P98 line402 explicitly requires E/G finite; the regular orbit used at lines409–413 is infinite when G is infinite. |
| §5.2, monodromy output reference | `outputs/c_computations.json` does not exist. | Use `outputs/c_computations.txt`, the saved and rerun output. |
| §5.3, field-extension paragraph | Current range496–502,512–515 omits transitivity492, finite descent493 and prescribed-compositum counterexample494, while including unrelated later operations. | Use C-SA04-492–498. Stacks01ZR remains a finite-presentation descent comparator, not an independent attribution of every universal-field statement. |
| §5.3, Tor paragraph | Null homotopies are incorrectly said to act “on the resulting homology.” | Say “the kernel ideals act null-homotopically on the tensor complex, hence trivially on its homology.” C-SA04-506 and C analysis §9 supply the argument. |

## Component correction completed

The main dossier correctly calls Stacks tag0620 **Example15.63.3**. I reopened the exact primary page, confirmed its label and flatness hypotheses, and corrected the C published-work link from “Lemma15.63.3” to “Example15.63.3.” The C serializer, claim wording and proof prose now consistently say G-sets with finitely many orbits. These are clerical scope clarifications; no judgment, identifier, count or mathematical computation changed. `c_supplement.py` and `c_finalize.py` were rerun successfully, with stdout in `outputs/c_supplement_final.txt` and `outputs/c_finalize_final.txt`.

Primary page: https://stacks.math.columbia.edu/tag/0620 (opened 19 November2026). Its assumptions are A→B flat and both B-modules A-flat, and its displayed sequence is Tor_i^A(Tor_j^B(M,N),A′) ⇒ Tor_{i+j}^{B′}(M′,N′).

## Sections9–10

No additional substantive defect was found in these sections. The reviewed final event table already has the canonical39 refutation events. The independent final register audit was rerun at03:10:23 UTC after the coordinating agent’s last-assembly notice; it found zero missing event records, invalid event types, broken identifiers, wrong-cote/out-of-range source intervals or omitted declared scans. Parent explicitly requested that final files and mainbody remain unedited.

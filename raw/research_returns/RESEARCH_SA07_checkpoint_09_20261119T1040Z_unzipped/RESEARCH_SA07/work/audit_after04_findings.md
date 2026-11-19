# Checkpoint 05 audit addendum

## Three independently checked results

**F.3.15** proves the recognition assertion of LM6 A.20 for the once-punctured curve `y²=x³−x` over `Q(i)`, at every prime. The proof uses actual finite-cover homology to constrain the first Magnus degree; Frobenius eigenvalues handle inert primes and 2. At split primes it checks the hypotheses of Ishii's nonvanishing theorem and the exact Nakamura comparison that places it in degree four. An independent Lie calculation supplies both conjugacy obstructions. The proof explicitly removes the lower inner-conjugator term even when the original abelian image is nonprimitive. Degree two then gives the actual cyclotomic character, and Nakamura's primary recognition theorem yields cusp inertia. Root checked the complete proof and the exact source scope. The separate integral class-four lift at 5 and the normalization κ/48 are not certified by this result.

**F.3.16** constructs an actual degree-32 finite étale cover of that punctured elliptic curve from the smooth Fermat quartic. Its genus-three compactification has a CM elliptic curve in the Prym, proved through explicit pullback and norm maps, including integral Tate-module injectivity at 2. Thus universal exclusion of CM weight-one lines from these Pryms fails. Three quotient maps exist on the same punctured curve; their differential pullbacks form a basis. Applying F.3.15 through those actual morphisms excludes proper-homology normalizer lines on this cover. A nonzero boundary-homology image yields cusp recognition for the full procyclic subgroup. Root checked all maps and compositions.

**F.3.17** gives the exact reach of this cover and its Fermat power tower. Their geometric Galois closures are 2-groups. Every corresponding subgroup therefore contains the kernel of the maximal pro-2 quotient and the common pro-prime kernel R. For `S=R_nil(F′)`, the perfect quotient `F→A₅` proves that `S′` is nontrivial. Its elements are killed by the first homology of every open subgroup containing R. This produces actual nontrivial procyclic invisible subgroups, but supplies no open arithmetic normalizer for them. Root checked the tower, infinity branch points, and perfect-quotient argument. The full LM6 A.22 requirement remains OPEN.

All three results are integrated in `output/RESEARCH_SA07/sections/F_audit.tex`. The section contains 17 numbered results. No root combined report, ledger, results table, or compilation was modified by this addendum.

## Exact sources and access

The bibliography is `audit_after04_references.bib`; source access and SHA256 records are in `audit_after04_source_checks.csv`.

| Source | Exact inspected scope | Access |
|---|---|---|
| Ishii, arXiv:2312.04175v2 | Definition 1.1 and Theorem 1.3 p.3; standing assumptions pp.4–5; Theorem 4.9 and Corollary 4.10 p.21 | Complete author PDF downloaded; p.21 image checked. This is the version used. |
| Nakamura 1995 | (4.3)–(4.4) p.214; Proposition 4.7/(4.8) p.215; (4.9.2) p.216; diagram (4.9.3)/Lemma 4.10 p.217; Corollary 4.12 p.221 | Complete original downloaded; original pp.216–217 images checked. |
| Nakamura 1994 | §2.1 pp.93–94; Theorem 2.1.1 p.94; Lemma 2.1.2 p.95; Lemma 2.1.4 and proof pp.96–97 | Complete original downloaded; root independently checked the exact recognition scope. |
| Ishii final journal edition | Publisher metadata and subscription preview | Landing page opened; final full text not obtained. |
| Ishii, arXiv:2312.04196v3 | Introduction and main-result premises pp.1–4 | Full PDF opened as a source lead; no theorem imported. |
| Kisin author index | Exact link to `Crystalline representations and F-crystals` | Index opened; linked DVI unsupported by web reader and direct download returned HTTP 403. Original-source gate remains. |

## Certificates and canonical events

The exact programs and their outputs are `check_CM_degree_four`, `check_CM_Prym_cover`, and `check_A5_invisibility` in the deliverable code folder. The dedicated computation record contains source/output hashes and actual wall times. Root separately added them to the independent 29-job verification run and recorded that run in its own manifest. The finite certificates do not claim to prove the arithmetic source input or an open arithmetic normalizer for the A₅ construction.

`audit_after04_CHECK_EVENTS.tsv` has 16 events using the prescribed event vocabulary, including F.3.15–17, the source accesses, and the three strengthened original inventory entries. Root's separate independent-review events are not duplicated as new root-authored rows in this file.

## Inventory status

Coverage remains **307 assertions from 154 requested entries**: **195 PROVED, 44 REFUTED, 28 OPEN, 30 READING, 9 DOCUMENTARY-GAP, and 1 NAMED-CONJECTURE-IMPLICATION**. No status changed. Only the proof dependencies and explicit scope of **I.B05.01, I.B05.02, and II.MB15.02** were strengthened. Original claim identifiers, witnesses, source files and source lines remain intact.

The final update script is `build_audit_after04_records.py`; run it after the earlier inventory/event builders to preserve these updates. Its validation JSON checks coverage, unchanged counts and complete event references. The remaining source route is Nakamura1995's introduction and its reference to the higher-genus normalizer theorem, with exact hypotheses to be checked before any application to arbitrary covers.

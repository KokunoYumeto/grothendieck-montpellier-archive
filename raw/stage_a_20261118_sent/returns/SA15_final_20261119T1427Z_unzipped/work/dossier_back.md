## 6. What the earlier notes got right, and what changed

The earlier notes are not uniformly unreliable. Many already separate their
own diagnostics from the manuscript, preserve cancellations, and state the
hypotheses of the later theorems more carefully than a short thematic summary
would. Their Amitsur, convergence, Borel, period-normalization, principal-PD,
CM and Tate-twist tests remain attributed to them. The present run has
checked them; it has not claimed their authorship. The absence of a
“corrected” verdict for a page whose formula is false often means that the
earlier note had already diagnosed that false formula correctly.

The substantive changes fall into the following groups. Each is documented
at the item and claim level, rather than inferred from an automated search
of the notes.

| Issue | Consolidated finding | Principal records |
|---|---|---|
| A false or cancelled intermediate statement treated as the final position | Follow the correction on the same or later supplied leaf: the ordinary cohomology hope, the determinant sign argument, and the revised torsion sequence have different final statuses. | P56-I133; P67-C037; P894-C037–P894-C044; P894-C050–P894-C057 |
| “Hypersingulière” silently modernized to supersingular | Preserve the author's p-rank-zero meaning. The broad higher-dimensional formal-isogeny conclusion is false; the all-slope-1/2 case is different. | P67-C010–P67-C013 |
| The ordinary cusp used as a singular de Rham counterexample | The full exterior Kähler complex includes its second term and has Euler contraction. A non-quasihomogeneous example is needed for the claimed failure. | P56-C042; P67-C045; P56-P014; P67-P021 |
| An ordinary connection, a full stratification and a PD crystal treated alike | Their local-freeness and comparison theorems have different scopes. BO's ordinary coherent stratification result does not require smoothness, while a general connection or PD lattice is another object. | P56-C102–P56-C104 |
| A literature title taken as a solution of the exact assertion | Retain the theorem's base, coefficient, completion and finiteness hypotheses. Rational comparison is not integral saturation; a theorem for moduli of curves is not a theorem for every fixed-X family. | P78-C009–P78-C012; P894-C051; P894-C073 |
| Every small nonzero mod-p lifting obstruction expected to be universal | There is an explicit GL₂(F₂) splitting; the complete classification is supported by the precisely identified later source, not an unread original proof. | P894-C004–P894-C007 |
| Generic mod-p torsion expected to determine finite potentially-good inertia | The explicit p=5 elliptic pair refutes the restricted comparison as well. Its hypotheses and finite-inertia scope are checked. | P894-C023; P894-C077 |
| Stable-rank growth left as a research obstacle | Katz's precise positivity theorem and Koblitz's leading-term/generic-transfer argument settle that part. The monodromy input remains separate. | P894-C065; P894-C073–P894-C076 |
| Arithmetic normalization omitted | A× versus K×, Ω/p versus Ω/π, the inverse dual, a Tate twist, a Frobenius twist, or a missing degree shift can change the assertion. | P78-C039; P78-C046–P78-C047; P894-C041; P67-C026 |

The current run additionally supplies the general weighted-ideal proof for
W(ν,r), the explicit two-curve inertia counterexample, the stable-torsion
dimension calculation, and the finite-local-field deduction for the
virtual-good-reduction length question. Their precise scope and dependence
on previously established theorems are recorded in the proof audits and
check events. Finite computations corroborate some of these arguments;
they do not prove their universal quantifiers. Refinement records and
counterexample certificates have separate provenance, so their presence in
the claim map does not enlarge what the manuscript itself asserted.

## 7. Reading alarms, links and historical limits

The reading table contains mathematical alarms: inconsistent F/V products,
missing shifts, logarithm signs, truncation indices, scalar-ring changes,
Frobenius twists, inequality/equality discrepancies, cancelled clauses,
reversed arrows and omitted determinants. It also records where Pro and
Codex disagree. Each row gives the alternative suggested by the mathematics
and its weight. **No row chooses a reading, and no diplomatic file was
changed.** The next scan-based companion can decide the ink using this
prioritized register.

The main link table contains only links checked at both endpoints. This
includes continuations across the package boundaries, reused-text order,
the exact passages of EGA and SGA, and selected later mathematical
counterparts. Archive order is not treated as a chronology. In particular,
the continuation 7:005 → 7:059 → 7:006 and the reverse jet typescript order
are documentary findings, whereas a proposed date for the handwriting
would be an additional inference.

The references to cote 54 are genuine leads in the earlier notes, but that
cote is not supplied. They remain in `SA15_unverified_links.tsv` rather
than the two-ended link table. A Demazure–Gabriel locator whose exact
passage was not obtained is handled the same way. Opened bibliographic
metadata do not turn it into a checked mathematical endpoint.

No in-scope note explicitly names a La Longue Marche, Dérivateurs, S6, or
other external research-run endpoint. The empty
`SA15_project_leads.tsv` is therefore an audited result, not an omission.
The earlier notes' cote 100 references stay archive links. Neither those
references nor a general similarity of subject licenses attributing a
connection to an absent project.

The problem register includes every retained question, hope, self-flagged
step and doubt, including ones later resolved or retracted. It is not a
list of contemporary open conjectures. Where no source explains why a
question was abandoned, `why_open` says so. A mathematical explanation of a
failed argument is not invented as a historical account of the author's
motivation. Similarly, a searched but unidentified modern endpoint is not
labelled an unsolved theorem.

## 8. What the dossier makes possible next

The most useful next work is narrow. First fix the conventions and missing
data that control a definite argument: the finite-group triangles, the two
integral Lubin–Tate lattices, the dual variance, and the stable-torsion
criterion. Then compare the exact reconstructed objects to the exact later
categories. The directions file ranks those tasks by mathematical interest
and what one research run of a few hours could establish. It also states
where a scan-based reading task must precede a proof attempt.

Several attractive-looking tasks are deliberately absent: re-proving the
now-checked W(ν,r) coefficient formula as though it were still open,
seeking an affirmative p-rank-zero Barsotti isogeny theorem contradicted by
the counterexample, deriving a Weil theory from the rejected non-PD
construction without changing it, or pursuing stable-rank growth as an
unresolved prerequisite. Their checks belong to this dossier; future work
should begin from the corrected status.

## 9. Counts and completion record

{{COUNTS}}

Counts are computed from the final linked records after the manually
specified identity decisions, not from keyword matches. The complete
original page-status wording remains in every claim. The normalized
status census separates present-run refinements and mixed documentary
statuses; it does not backdate a modern refutation into an authorial
retraction. A reader can reproduce the structural joins and count tables
with `work/code/validate_final.py`. Its PASS certifies file structure,
coverage and references, not a formal proof of the mathematics.

The source inventory, source-read ledgers, per-claim search ledger,
bibliographic evidence, independent proof files, exact calculation code and
saved outputs are included under `work/`. The original attachments are
not duplicated. `progress.log` gives the UTC start, stage milestones,
checkpoint events and completion. The final archive is the complete
deliverable; none of its registers is a sample or a proposed future
catalogue.

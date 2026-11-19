# Bounded independent audit of the bibliography and Part E source coverage

Audit date: 19 November 2026, 04:43--04:52 UTC. This is a read-only
audit of other agents' files. The manuscript and its consolidated
bibliography are still changing. Counts below are a snapshot, not a
claim about the next build.

## Machine-readable outputs

`audit_bibliography.py` reads the consolidated bibliography, all part
fragments and the recursively included manuscript. It writes
`audit_bibliography_output.json` and `bibliography_inventory.tsv`.
The snapshot contained 90 consolidated entries. The proposed aliases
are in `bibliography_alias_suggestions.tsv`; no aliases were applied.

## Explicit opening status

Ten consolidated entries lacked the literal status required by the
prompt: BLichtenbaum2009, BMilne2006, BMilneErrata2025, BBlochKato1990,
BBorel1974, BNickel2022, BKurihara1992, BKeller2019, BElkies2021 and
BPari2026. Part B's literature ledger already records each as opened.
Thus this is a bibliography-annotation omission, not evidence that the
sources were unread. Part B was notified to add the status.

The auxiliary `part_d/c6_general_sources.bib` also originally omitted
the literal opening status. Part D corrected its own file during this
audit. The main C bibliography already had expanded status notes for
the C6 entries it had copied.

The Cadoret--Tamagawa author PDF has no verified publication or
manuscript date in the inspected material. Its retrieval year should
not be presented as its publication year; the auxiliary entry now
uses `n.d.` and records the retrieval date explicitly.

## Duplicate works and version discipline

The eight rows in `bibliography_alias_suggestions.tsv` are exact-work
duplicates. Before replacing citation keys, merge the **union** of
the theorem/page locators and the distinct independent checks. In
particular, merging the two Arithmetic Duality Theorems entries must
retain Part B's Chapter II finite-duality locators as well as Part A's
I.4.20 torus duality.

Do not merge the Milne 2006 ADT book with its 2025 erratum; the
original October 2026 rationality manuscript with its later exposition;
Oort's 2009 CM-lifting notes with Chai--Conrad--Oort's 2008 manuscript;
or the original CM Hodge theorem with the van Hoften--Sempliner
exposition. Those are distinct works or source versions.

## Consolidation lag, not missing references in owner files

At the snapshot, twelve citation keys used by the main manuscript
were absent from the consolidated file but present in owner
bibliographies: BKahn2003, BFontaine1992, BStacksSmoothLift,
BStacksClosedPushout, BStacksPushoutMorphisms, BdeJong1996,
BConrad2006, BGeisserDedekind2004, BVoevodsky2011, c_stacksdescent,
c_saito2003weights and c_serre1970local. Re-running the existing
consolidator should import them; it already lists the relevant owner
files. These should not be recorded as sources not obtained.

The c_sga7 opening note in the consolidated snapshot was also stale:
Part C's owner bibliography now records the original scan and exact
IX locators (2.1.8), 2.2.5, 2.2.9, 2.4, 3.5, 3.5.2 and 3.6.

## Coverage of the prompt's explicitly named mathematical works

Every work in the prompt's main paragraph beginning “Not attached”
is represented in an owner bibliography and recorded as opened:
Langlands--Rapoport 1987; Milne 1994, 2003 and 1999; Kisin 2017;
Deligne's Taniyama chapter; Milne--Shih's Taniyama chapter;
Lichtenbaum 2005 and 2009; Geisser 2004; Flach--Morin 2018;
Bloch--Kato 1990; Milne ADT; Beauville--Voisin 2004;
Gross--Schoen 1995; O'Sullivan 2011; and Vasiu--Zink 2010.
All have exact numbered locators in the owner entries or ledgers,
except that the Langlands--Rapoport entry currently gives only
sections 2--3. The unnumbered main theorem in Deligne's Taniyama
chapter is correctly identified as unnumbered and placed at p.262;
it should not be assigned an invented number.

The three attached modern sources are covered in Part B's ledger:
Scholbach's f-cohomology article (Remark6.2, Theorems6.8,6.11,6.13),
Scholbach's Special L-values manuscript (the mixed-motive axioms and
labels `motcomp`, `numrat`), and Adrien Morin's constructible-sheaf
article (Theorem A / label `thm:main`, n≤0). Only the first currently
has a bibliography entry. If the latter two are discussed in the
report as used scope checks, add marked bibliography entries, or
retain their complete one-line records in the consolidated literature
ledger with title, source path, version and exact locators.

The prompt also names Fontaine--Perrin-Riou for the corrected
arithmetic comparison. Part B's ledger honestly says “not obtained”
and records exact-title searches and both author publication pages;
the expected III.3.1.4 is labelled unverified. Do not silently promote
that expectation to an opened locator. Schneider's original article,
although not explicitly titled in the prompt, is likewise properly
marked not obtained; the opened Nickel formulation supplies the
actual statement used.

SGA7 I, Exposé IX, Borel's rank theorem and the needed Soulé inputs
are named later in the prompt. SGA7 and Borel have exact opened
records. The name “Soulé” covers different inputs: the opened 2003
torsion bound is a different theorem from the comparison theorem
used in B.2. Make the final literature line identify the precise
opened comparison source (the new Fontaine1992 and
Voevodsky2011 entries, as applicable), instead of letting the
2003 torsion-bound citation appear to support both.

## Contextual titles and global ledger completeness

The prompt also mentions Lipman's Rational singularities paper and
Mumford's Geometric Invariant Theory solely to date the reused
typescripts; Larsen--Lunts is named in the carried R8 background.
They have no current run source row in the inspected owner ledgers.
If Part E interprets “every source named in this prompt” literally,
add context-only rows, with `not obtained in this run; no mathematical
claim imported` unless actually opened. The background ledger's
earlier checks must not be re-labelled as this run's opening event.
Likewise, the background's corrected Lipman pagination/chronology
should remain attributed to the earlier ledger unless independently
checked. Named theorems such as Honda--Tate can be recorded through
the exact opened Milne theorem used in the proof; no unread original
paper should be asserted opened.

There was no root-level `LITERATURE_CHECK.tsv` at the snapshot.
Parts B and D have explicit tables; Parts A and C put much of the
same information in annotated bibliography entries and notes. A
root-level union should normalize these into one row per **work**,
preserving opening status, exact locator, URL/local supplied path,
retrieval evidence and limitation. It should also include inspected
scope-check sources that are not cited in a theorem, such as the
Fontaine, Lu--Zheng, Ayoub and Cadoret--Tamagawa C6 searches.

## Remaining locator refinements

1. Langlands--Rapoport: the main comparison currently relies on the
   explicit Kisin/Milne dictionary, but its bibliography entry only
   says §§2--3. Add the exact numbered constructions/propositions or
   printed pages actually used, if the original has no theorem
   carrying the combined statement. No invented theorem number.
2. The forthcoming C1 finite criterion needs its freshly opened
   Procesi FFT/SFT locators and Milne Algebraic Groups Theorem4.14,
   Theorem22.42 and Remark12.53(a); Part C has been sent the opened
   text and will import the bibliography entry.
3. Unused unsuccessful searches should remain labelled as such.
   The general C6 gate is not resolved by Fontaine C_WD, Serre C3/C5,
   Lu--Zheng's equal-characteristic result, or Ayoub's geometric-DVR
   conservativity conjecture. Each supplies at most the specifically
   recorded implication or an inapplicable scope.

No mathematical result was promoted, no other agent's bibliography
was changed, and the audit does not certify sources not personally
opened by its author. Opening assertions about other parts are
cross-checks of those parts' own recorded evidence.

## Post-audit updates

Before the04:57 freeze, actual contextual source lookup resolved the
Lipman and Larsen--Lunts missing rows; original1965 GIT remains
honestly not obtained, with publisher history opened. Root reports
the global literature union is implemented and the original German
Langlands--Rapoport numbered locators have been checked and added.
These updates supersede the corresponding snapshot omissions above.

# A home for the mathematics, in the manner of Stacks and Kerodon: a sketch

18 November 2026. Written by the main session (Claude Opus 5.5 Max) at the user's word: "take all the concepts, notes,
organize how they should go in a stacks-like thing or Kerodon thing. And you can definitely use a different tone. It
doesn't have to be dense and most general necessarily, although ... trying to be rigorous is making things general"
(USER_INPUTS.md P6847). The discussion behind it: P6825-P6848, in `Documents/task_notes/foundations_strategy.md`. This
is a sketch to talk over, not a rule.

## 1. What it is

All the mathematics of the programme in one place. Every definition, statement, proof, claim of Grothendieck's, open
question and refuted claim is one **item**, with one permanent **tag** and one page. The items come from his
manuscripts, the research runs, and the notes of every reading.

- **The mechanics come from Stacks:**
  - permanent tags;
  - proofs that cite only earlier tags, so a script builds the dependency graph and a refuted item flags everything
    that uses it;
  - a page per item, with comments.
- **The tone comes from Kerodon:**
  - it reads in order;
  - the why comes before the what, with examples and warnings;
  - it is rigorous and general where rigour makes it general, not general for its own sake.
- **The status layer is what neither has.** Every item says what it is:
  - proved, with its check record;
  - known, and cited;
  - his claim, with the gap named;
  - open, with the strongest proved reduction;
  - refuted, with the refined item.

  A familiar format carries a promise (in Stacks: everything here is proved), and the status line is what keeps ours
  honest. Proved and unproved items stay apart: the main text holds what is proved; claims and questions sit in their
  own marked environments and in each chapter's open section.

Why this shape, in the user's words (P6845): a researcher puts a Stacks- or Kerodon-like site "in a mental category that
they understand and trust as a resource", instead of "I need to now read 4,000 pages before I can trust this". The
returns themselves, the runs' long explorations, stay on GitHub as provenance. Each item links to the raw return it
came from.

## 2. One tag space, three views

The items are kept once. The books are views of them.

| View | Ordered by | What it shows |
|---|---|---|
| **The handbook** | topic, in logical order | the theory done properly: the proved items in the main text, statuses visible, each chapter's open items in their own section |
| **The companion** | his pages: cote, then unit | the reading of each unit of his notes, pointing to the items it discusses |
| **The programme** | research line | the open questions, conjectures, new results, and refuted claims with their refinements |

- **No duplication:** a statement is written once.
- **A correction reaches every view:** fix the item, and all three views change.
- **The check record belongs to the item,** not to a document.

The companion keeps his text beside our commentary (the T/A split of the design, 4.6). The handbook and the programme
are entirely ours.

## 3. The item

| Field | Content |
|---|---|
| tag | permanent, never reused (see below) |
| kind | definition, construction, lemma, proposition, theorem, corollary, example, counterexample, remark, warning, **his claim**, **question**, **conjecture** |
| statement | LaTeX, in the handbook's one notation |
| status | proved / known (with the citation) / his claim / open (with the strongest proved reduction) / conjecture / refuted (with the tag of the refined item) |
| proof | the proof, or where it is |
| uses, used by | tags; *uses* is read from the proof's references, *used by* is computed |
| his places | every place he treats it: cote, scan, line, with the link into the reader |
| literature | EGA, SGA and FGA by their own numbers (the French-school site's addresses); Stacks and Kerodon by tag; HTT and HA by number; papers by statement and page |
| provenance | run, statement id, model and effort, date; the raw return on GitHub; Hua's project where the finding is his, credited |
| checks | every check event (type, who, date, outcome) and the cumulative count: the runs that reworked or used it, the intakes that read it, the targeted checks, the computations |
| place | part, chapter, section; topic |
| history | each change of status, dated |

**Tags.** Four characters from 0-9 and A-Z, as in Stacks and Kerodon, but in our own namespace, and always shown with
the work's short name (for example "[name] 0A3F") so that no one takes them for Stacks tags. Until a topic's last sweep,
items carry **draft tags** (run and statement id). The tags are frozen chapter by chapter.

## 4. The outline

Built from the programme map (`notes_headlines/PROGRAMME_MAP.md`), the archive's 22 sections and the 30 STAGE_A topic
dossiers. The parts are mathematical, not archival; a cote may feed several chapters.

- **Part 0. Conventions and the foundations we use.** Pointers, not proofs: what the items rely on in EGA, SGA, Stacks,
  Kerodon and the literature, by locator. Our own proof appears only of a form the sources do not state.
- **Part I. The Galois theory of the tower** (La Longue Marche, the Esquisse):
  - GT̂ and its finite subgroups;
  - the tower of moduli spaces and its Lego (strata, frames, the five-point diagram);
  - dessins and the Galois action;
  - anabelian geometry and sections (the section conjecture, points as sections over finite fields);
  - the Fermat curves.
- **Part II. Homotopy** (Pursuing Stacks, Les Dérivateurs):
  - small categories (filtered, exact, total, quasi-filtered; truncated totality);
  - test categories and fundamental localizers (the weak and the relative localization axiom);
  - dérivateurs;
  - finite models of homotopy types (FINMON, the tests for S²).
- **Part III. Cohomology and motives:** motives, crystals, the de Rham complex, Picard, Jacobians, abelian varieties,
  elliptic curves, descent, and the SGA and EGA themes of his notes.
- **Part IV. Shapes and stratifications:** stratified spaces, *Vers une géométrie des formes*, combinatorial geometry and
  topology.
- **Part V. Around his teaching.**

Chapters are topics; sections are units of mathematics, not his pages. S6 is not part of the programme. It gets its
own tag space in the same format: the six S6_10 papers are its first content.

## 5. How it is built: horizontal sweeps, layer by layer

The user (P6848): "do a light sweep, see where everything goes, do another light sweep, see how everything interlinks,
see if there are obvious inconsistencies ... just Bayesian refinement. And like layer per layer".

1. **Sweep 0, by script, no model: the register.**
   - Every result of every run (the runs' results tables and inventories: 6,271 statements in 44 runs on 17 Nov, more
     since) becomes an item with a draft tag, its status, provenance and check events.
   - The lineage across runs comes from the carried ids and source rows, such as `S6_01_INVARIANTS:C3.8`.
   - The claims in the notes (Pro's heavy notes, Work's light ones, Hua's credited findings) become his-claim items with
     their locators.
   - The dependencies come from the ids the proofs cite.
2. **Sweep 1, light: where everything goes.**
   - Every item gets a place in the outline.
   - Duplicates are merged.
   - The obvious inconsistencies are flagged: the same statement with two statuses, two forms with different
     hypotheses, an item that uses a refuted one.
   - This is done by the Pro topic dossiers SA01-SA30 now running on account 4, and by Opus 5.5 Max agents over the
     register.
3. **Sweep 2, light: how everything interlinks.**
   - The dependency graph is closed.
   - Every claim of his is linked to the items that prove or refute it.
   - Every item is linked to the units that discuss it.
   - The corrections and refinements found on the way are noted.
4. **Sweep 3, dense, topic by topic.**
   - A Pro run writes the chapter from its items in the handbook's tone, checking the proofs as it uses them.
   - Work checks the ink of every his-claim item.
   - Each check is a check event on the item.
   - Then the chapter's tags are frozen and it is rendered.

## 6. What it builds on

- **The French-school site** (`french_school_site_20261110/`: design by Claude Fable 5.2 High, 10 Nov; built in part,
  13 Nov):
  - the printed numbering as the address (EGA IV 17.5.1);
  - a works registry with include flags, so that a takedown is a rebuild;
  - languages, and others' editions linked, not copied.

  The handbook becomes one more work in that hub, and its citations of EGA and SGA are links.
- **The Stacks translations site** (`DESIGN_STACKS.md`): tags as addresses in five languages, with two AI layers kept
  apart from the Stacks text:
  - layer 2: suggested corrections;
  - layer 3: an AI-integrated Stacks with additions. The earlier Stacks-style formattings of EGA and SGA material
    that the user recalls (made by earlier agents, not integrated) belong here; I have not located them in the files
    yet (memory stacks-core-open-split, 19 Oct, has the design of that integration).

  The handbook cites Stacks by tag and links to our translations.
- **The courses' theorem graph** (tag system v1, 24 Oct: 6,140 results, facets, typed edges, a validator): the same
  machinery can carry the items.
- **The companion design** (`COMPANION_DESIGN_20261118.md`): the units (`UNITS_DRAFT_20261118.tsv`, 3,020 draft units),
  the eight kinds of note, the status lines, the results register (4.5), the CC0 split (4.6), and run A's placements of
  each note (the place and topic fields).

## 7. Rights and publication

- **Everything in the handbook and the programme is ours: CC0.** His words appear there only as short quotations with
  their locators; his text lives in the readers, under the rights notice, as separate works that can be switched off.
- **Published on GitHub, in the hub,** with the raw returns as provenance. No DOIs.
- **The S6 tag space is ours entirely.**

## 8. The name

The user's proposal (18 Nov 13:17 UTC, P6855): name the layers in French, as his series are named (*Éléments*,
*Séminaire*): "Fondations", "Chantier", and the cathedral, because "the joke about Grothendieck is, you know, he builds
cathedrals". As working names:

- **Fondations:** the handbook, the proved theory in logical order. It sits beside FGA, whose F is already
  *Fondements*.
- **Chantier:** the work site: the open questions, conjectures and research in progress (the programme view).
- **Cathédrale:** the whole, the umbrella name. His manuscripts are the architect's sketches, and the companions read
  them.

The public title is the user's to choose.

## 9. First steps

1. **Sweep 0, the register by script:** the main session, now.
2. **Sweep 1 over the register, research line by line:** Opus 5.5 Max agents, bounded; each writes its placements,
   inconsistencies, corrections and refinements.
3. **One pilot chapter in the handbook's tone,** from its items: a Pro prompt, after the register exists. Part II's
   small categories are a good pilot: their items are many, well checked, and they interlock.

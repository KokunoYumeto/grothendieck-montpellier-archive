# The companion's first two layers, seamless: models and a page design (18 Nov 2026)

Written by the main session (Claude Opus 5.5 at effort max) at the user's request, 18 Nov ~00:4x UTC:
- "note taking is a check on transcription. And like makes companion layer one professional as fuck ... that needs to
  be seamless. Layer one and layer two. So layer one being the transcription translation, layer two being the sort of
  modern shit ... the contextualization of it ... seamlessness is the key, right? So same register, but you know,
  contextualizing modern results";
- "the transcription is janky as fuck, right? It's literally just notes ... not readable. So you just make a nice little
  introduction, contextualization, a little bit of history ... and then writing what Grothendieck writes";
- "Find some good examples of historical shit like what we're trying to do here ... commentaries or companions."

## 1. Models: editions and commentaries held up as the standard

| Work | What it does that we want |
|---|---|
| D. T. Whiteside (ed.), *The Mathematical Papers of Isaac Newton*, 8 vols., Cambridge University Press, 1967-1981 | The closest model: a great mathematician's working papers, drafts and notes. Each piece has an introduction (date, context, what it is for). The text has editorial insertions in brackets, and the Latin is translated. Dense footnotes, keyed to the lines, explain each step in modern terms, fill in what Newton left out, correct his slips, and link to his other papers and the literature. The commentary runs on the same pages as the text, which is what makes it seamless. |
| B. C. Berndt, *Ramanujan's Notebooks*, Parts I-V, Springer, 1985-1998; G. E. Andrews and B. C. Berndt, *Ramanujan's Lost Notebook*, Parts I-V, Springer, 2005-2018 | The model for notes full of unproved claims. Entry by entry: the claim as he wrote it, in today's notation; a proof, or the source where it is proved, or the statement that it is false or still open; then the history. This is our layer 3 laid out for a reader. |
| R. Netz, *The Works of Archimedes: Translation and Commentary*, vol. 1, Cambridge University Press, 2004 (vol. 2, 2017) | The translation keeps the author's own register: his order, terms and diagrams. After each proposition come "textual comments" (on the text) and "general comments" (on the mathematics), kept apart from the text. |
| T. L. Heath, *The Thirteen Books of Euclid's Elements*, Cambridge University Press, 1908 (2nd ed. 1926) | A long historical introduction, then each proposition followed by its commentary: the history of the idea, other proofs, the later development. |
| P. M. Neumann, *The Mathematical Writings of Évariste Galois*, European Mathematical Society, 2011 | French manuscripts and drafts, with the struck passages kept, on facing pages with an English translation, and introductions and notes for a modern reader. It is the nearest case to ours in language and kind. |
| P. Colmez and J.-P. Serre (eds.), *Correspondance Grothendieck-Serre*, SMF, 2001; bilingual edition, AMS, 2004 | Grothendieck himself. Short footnotes that place each statement in today's mathematics and point to where it was later proved or published, in the same register as the letters. |
| G. Maltsiniotis (ed.), *Pursuing Stacks*, SMF, Documents Mathématiques 20, 2022; Künzer, Malgoire and Maltsiniotis, *Les Dérivateurs* | Grothendieck's own manuscripts edited with notes by mathematicians of the field. The specialists' standard for this author, and in part already our source. |
| C. Goldstein, N. Schappacher and J. Schwermer (eds.), *The Shaping of Arithmetic after C. F. Gauss's Disquisitiones Arithmeticae*, Springer, 2007 | How a commentary volume places a text in the history of what it started. A model for the companion's introductions. |

**What they share:**
- the author's text is given whole and faithfully;
- the commentary sits next to it, keyed to its lines, in a plain expository voice, never mixed into it;
- each unit opens with a short introduction that says where we are and what he is doing;
- each claim's status and later history is stated.

None of them is "a book on the mathematics" written instead of the text, and that is the seamlessness the user means.

## 2. The page design for the Montpellier companion (layers 1 and 2)

One **unit** is one piece of his argument: a construction, a definition with its examples, a proof attempt, a list.
The units come from layer 2 of the working-through.

1. **Introduction to the unit,** a short paragraph, as Whiteside and Heath do:
   - where we are in the folder and in his work;
   - the date;
   - what he is doing, in today's terms;
   - a little history: what came before, what came after, in his work and in the field.
2. **His text, in two renderings,** in French with the English beside it (facing, as Neumann):
   - the **reading text:** his words, with abbreviations expanded in brackets and the struck passages moved to the
     apparatus. It is readable, and it is still only his words;
   - the **diplomatic transcription** (the current layer 1) for whoever needs the ink: struck text, insertions,
     margins, the doubt marks. It is linked from each line to the scan.
3. **Running commentary keyed to his lines** (Whiteside's footnotes; Netz's comments; the Colmez-Serre notes):
   - his notation explained;
   - the steps obvious to him filled in;
   - the modern equivalent;
   - a slip, with its corrected form;
   - a reading that is uncertain, with its alternatives;
   - links to his other folders and to the literature.

   This is where Pro's consolidated notes go: each note becomes a commentary item anchored to its line.
4. **Status and connections,** after the unit (Berndt's entries):
   - each of his claims, with its status (proved, with the proof or where it is; known, with the source; false, with
     the counterexample; open, with what is known);
   - what later work did with it;
   - where our own results bear on it.

   The full proofs of our new results go to layer 3 (C2), and the open problems to C3. Only a line and a link appear
   here.

**Status lines are dated and linked** (the user, 18 Nov ~00:5x UTC). Not "open when this was written, solved by AI two
days later", which the user calls "a little dumb". A status line says how the claim stood as he left it, and links to
where it was developed further:
- "Open as he states it (1986). Developed further in C2, section x; proved there for ..."
- "Proved by Y in 19xx (reference)."

That is how Berndt's entries record later proofs. The developments themselves live in C2 and C3.

**Later, not now** (the user): the same kind of companion for Gauss, in the register of the Goldstein-Schappacher-Schwermer
volume. "One massive project at a time."

**Register:** one plain expository voice, the voice of a colleague who knows the field and the period, the same in
the introductions, the commentary and the status blocks. His words and ours never share a paragraph (memory
companion-ideology). The reader is the career algebraic geometer who must find it good.

## 3. What this means for the notes processing (alignment with the working-through)

The working-through run (`grothendieck_archive_transcription_20261110/second_pass/PLAN_WORKING_THROUGH_PRO_20261118.md`)
writes its outputs in the shapes of this page:

| Run output | Becomes |
|---|---|
| unit list and groundwork | the unit introductions (item 1) |
| corrected transcription, plus a reading text with abbreviations expanded in brackets | item 2 |
| consolidated notes, each anchored to scan and line | the running commentary (item 3) |
| CLAIMS_STATUS and FOR_EXPERTS | the status-and-connections block (item 4) |
| RESEARCH_DIRECTIONS and the layer-3 work | layers C2 and C3 |

So processing the notes is writing the companion's commentary, with no further step between them. A script sets the
pages from these files; the reader builds stay as they are.

## 4. How the companions are offered (the user, 18 Nov ~00:5x UTC)

The user: "say these are draft companions by AI. If you want to take them up, feel free, especially if you are
knowledgeable of the topic ... if you happen to be read in on the topic or personally involved in any of it, please
just take these and adapt as you see fit."

So every companion opens with a short notice. A draft, for the user to see before it is used:

> This companion is a draft written by AI (GPT-6 Astra in ChatGPT Pro mode, and Claude). If you know this
> mathematics, or were part of its history, please take it up: correct it, rewrite it, adapt it as you see fit. Our
> parts carry no rights we would enforce (CC0), and we will gladly link to or step aside for a better version.

It goes beside the rights notice of the editions, never in place of it. The models and the efforts are named in the
methodology.

# Grothendieck's Montpellier archive: transcriptions, checks and research notes

This repository is the hub of our work on the manuscripts of Alexander Grothendieck held at the Université de
Montpellier (Fonds Grothendieck; the scans are published by the university at
https://grothendieck.umontpellier.fr/archives-grothendieck/ and are not copied here). Everything below is AI-produced:
AI-transcribed text, AI-written research notes, AI-produced checks and corrections. It is work in progress, published as
it is made, with the prompts that produced it.

**Where the work stands (17 Nov 2026):** [status/STATUS_2026-11-17.html](status/STATUS_2026-11-17.html), a snapshot of the whole project on that date (an HTML page: download it and open it in a browser).

## Comment ce travail a été fait : les défaillances de l'IA, et ce que nous faisons contre elles

Tout ce qui se trouve ici a été produit par IA. La transcription par IA de mathématiques manuscrites échoue de façons
connues, et un lecteur a raison de s'y attendre. La méthode est construite contre chacune d'elles, et nous mesurons ce
qui reste.

**Les défaillances, et ce que nous faisons contre chacune**
- **Lire ce que l'argument demande au lieu de ce qui est écrit.** Le modèle marque d'un `\unsure{…}` tout mot qu'il n'a
  pas vu lettre par lettre, si bien qu'il s'insère, et lit les inégalités, le sens des flèches et les inclusions
  uniquement à l'encre. Toute correction des mathématiques de Grothendieck va dans les notes de recherche, jamais dans
  la transcription.
- **Petites omissions.** Après chaque formule centrée, note marginale et insertion, le modèle vérifie symbole par
  symbole que tout ce qui est sur la page est dans le texte : un « ≠ 0 », un signe d'inclusion entre deux lignes, des
  parenthèses intérieures.
- **Mise au propre silencieuse.** Les mots barrés vont dans `\deleted{…}`, les insertions dans `\inserted{…}` à
  l'endroit que désigne son renvoi, les notes marginales dans `\margin{…}`. Son orthographe, ses terminaisons et ses
  abréviations restent telles qu'il les a écrites.
- **Lettres et chiffres qui se ressemblent** (E et F, 3 et 5, u et n, 1 et l) : lus à l'encre, ou marqués.
- **Le même signe lu de façons différentes dans un même lot.** Nous l'avons constaté quand des pages étaient réparties
  entre des processus parallèles. Désormais un seul modèle lit tout un lot d'un seul tenant et tient une table de
  notations, et chaque signe récurrent est comparé sur tout le lot avant que le texte soit définitif.
- **Le contexte qui oriente la lecture.** La transcription est écrite, relue page par page contre les images, puis
  figée (une empreinte SHA-256 de chaque page) avant que le modèle puisse ouvrir le moindre contexte : transcriptions
  antérieures, nos notes. Les notes de recherche ne viennent qu'ensuite.
- **Pas d'OCR.** Chaque page est lue sur l'image, agrandie si nécessaire.
- **Travail perdu ou interrompu.** Le modèle enregistre un point de sauvegarde toutes les heures, chaque retour est
  vérifié fichier par fichier à son arrivée, et le prompt tel qu'envoyé est publié avec chaque lot.

**Des modèles choisis selon la tâche**
- **Écriture manuscrite, premier passage :** GPT-6 Astra (ChatGPT, mode Pro), un lot d'environ 45 scans par
  conversation.
- **Second passage :** Claude Opus 5.5 (effort max), 15 à 18 scans par agent. Chaque ligne est lue contre des
  demi-scans et des agrandissements, et chaque modification est consignée avec sa justification et un degré de
  confiance.
- **Pages dactylographiées et imprimées :** Claude Opus 5.5 (effort high, Message Batches API) et GPT-6 Astra à son
  réglage de raisonnement maximal dans Codex web.

**Ce que mesurent nos vérifications**
- Une vérification indépendante de nos premiers passages contre l'encre, par Claude Opus 5.5 (effort max) le
  15 novembre 2026, situe leur taux d'erreur à environ 1,4 pour 100 mots, formules comprises. Pour la prose seule, il
  est de 1,9 pour 100 mots, avec un intervalle à 95 % de 1,2 à 2,9.
- Ce chiffre est un minimum ; des vérifications antérieures plus légères en avaient trouvé environ la moitié.
- La plupart des erreurs portent sur un seul mot, et les lectures douteuses sont marquées.
- C'est pourquoi un premier passage n'est pas une fin : des seconds passages sont en cours.
- Les scans sont publics à l'Université de Montpellier : chaque lecture peut être vérifiée. Les corrections sont les
  bienvenues sous forme d'issues GitHub. Détails : [METHODOLOGY.md](METHODOLOGY.md).

## How this was made: AI's failure modes, and what we do about them

Everything here was produced by AI. AI transcription of handwritten mathematics fails in known ways, and a reader is
right to expect them. The method is built against each of them, and we measure what is left.

**The failure modes, and what we do about each**
- **Reading what the argument needs instead of what is written.** The model marks every word it has not seen letter by
  letter with `\unsure{…}`, however well it fits, and reads inequalities, arrow directions and inclusions only from the
  ink. Any correction of Grothendieck's mathematics goes into the research notes, never into the transcription.
- **Small omissions.** After every display, margin note and insertion, the model checks symbol by symbol that
  everything on the page is in the text: a "≠ 0", an inclusion sign between two lines, inner parentheses.
- **Silent tidying.** Struck words go in `\deleted{…}`, insertions in `\inserted{…}` where his caret points, margin
  notes in `\margin{…}`. His spellings, word endings and abbreviations stay as written.
- **Look-alike letters and digits** (E and F, 3 and 5, u and n, 1 and l) are read from the ink, or marked.
- **The same sign read in different ways across a package.** We saw this when pages were split among parallel workers.
  Now one model reads a whole package in one stream and keeps a notation table, and every recurring sign is compared
  across the package before the text is final.
- **Context steering the reading.** The transcription is written, read a second time page by page against the images,
  and frozen (a SHA-256 hash of every page) before the model may open any context: earlier transcriptions, our notes.
  The research notes come only after that.
- **No OCR.** Every page is read from the image, enlarged where needed.
- **Work lost or cut short.** The model saves a checkpoint every hour, each return is checked file by file when it
  arrives, and the prompt as sent is published with each package.

**Models matched to the task**
- **Handwriting, first pass:** GPT-6 Astra (ChatGPT Pro mode), one package of about 45 scans per conversation.
- **Second pass:** Claude Opus 5.5 at effort max, 15–18 scans per agent. Every line is read against scan halves and
  enlarged crops, and every change is logged with its evidence and a confidence.
- **Typed and printed pages:** Claude Opus 5.5 at effort high (Message Batches API), and GPT-6 Astra at its maximum
  reasoning setting in Codex web.

**What our checks measure**
- An independent check of our first passes against the ink, by Claude Opus 5.5 at effort max on 15 Nov 2026, puts
  their error rate at about 1.4 per 100 words with formulas counted. For prose alone it is 1.9 per 100 words, with a
  95 % interval of 1.2–2.9.
- That figure is a floor; lighter earlier checks had found about half of it.
- Most errors are single words, and doubtful readings carry a mark.
- That is why a first pass is not the end: second passes are under way.
- The scans are public at the University of Montpellier, so every reading can be checked. Corrections are welcome as
  GitHub issues. Details: [METHODOLOGY.md](METHODOLOGY.md).

## Readers

### Which book to read

Each work comes in several books, all made from one checked transcription. **Start with the reading text** (the English one where there is one): the clean corrected text, for reading the mathematics.

- **Diplomatic**: the typescript or manuscript as it is, page for page, with the author's own corrections shown as they stand, for checking against the archive.
- **Corrected, with apparatus**: the corrected text with every editorial change numbered and listed, for anyone who wants to see what was changed and why. An apparatus entry records one change: what the source has, what the corrected text has, and why.
- **Corrected, with translator's notes** (Esquisse, EGA V): the English translation with the same apparatus and the translator's notes, for seeing how the French was rendered.
- **Annotated master** (Pursuing Stacks): the editors' copy from which the other books are printed; as a PDF it shows the same content as the corrected reader with apparatus.
- **Guide**: a companion on the text and its mathematics.
- **Blass's typescript** (EGA V, cote 24): Piotr Blass's 1987 English translation in the same three forms, a historical witness.

The notes of each release open with the same list for its own books.

- *Esquisse d'un programme* (1984, cote 119), final edition of 14 November 2026: French diplomatic text (both
  typescript copies), French corrected text with apparatus, French reading text, English translation with
  translator's notes, English reading text and a guide, each as PDF and LaTeX, in the release
  [esquisse-readers-2026-11-14](https://github.com/KokunoYumeto/grothendieck-montpellier-archive/releases/tag/esquisse-readers-2026-11-14).
  Built by GPT-6 Astra (ChatGPT Pro mode) from the transcription by Claude Opus 5.5 at effort high (Message Batches
  API); the run's records are in `raw/pro_returns/ESQUISSE_READERS_20261114/FINAL_20261114T2138Z/`.
- *Nouveau EGA V* (cote 25) and Piotr Blass's 1987 translation typescript of it (cote 24), final edition of
  14 November 2026: French diplomatic text, corrected text with apparatus and reading text; a new English translation
  (with apparatus and translator's notes, and reading text); Blass's translation in three forms; a guide; each as PDF
  and LaTeX, in the release
  [ega-v-readers-2026-11-14](https://github.com/KokunoYumeto/grothendieck-montpellier-archive/releases/tag/ega-v-readers-2026-11-14).
  Built by GPT-6 Astra (ChatGPT Pro mode) from the transcription by Claude Opus 5.5 at effort high (Message Batches
  API); the run's records are in `raw/pro_returns/EGA_V_READERS_20261114/FINAL_20261114T2314Z/`.
- *Pursuing Stacks* (1983, cotes 134-2 to 134-8), with R. Brown's English translation of the appendix, final edition of
  14 November 2026: diplomatic reader, corrected reader with apparatus (11,291 variants), reading text, annotated master
  and guide, as PDF, with the LaTeX sources, in the release
  [ps-readers-2026-11-14](https://github.com/KokunoYumeto/grothendieck-montpellier-archive/releases/tag/ps-readers-2026-11-14).
  Rebuilt on 15 November 2026 with changes to the layout only: each book now opens with the list of the five books and a
  key to its marks, and has running heads (book, archive scan, page) and bookmarks for the numbered sections.
  AI-transcribed by Claude Opus 5.5 at effort high; checked against the scans, corrected and typeset by GPT-6 Astra
  (ChatGPT Pro mode); the run's records are in `raw/pro_returns/PS_READERS_20261114/FINAL_20261114T2230Z/`.

## What is here

- `packages/<package>/first_pass/`: the transcription of one package of scans (cote and scan range in its name), as
  returned: `*_transcription.tex` (all pages), `pages/` (one file per scan), `*_notes.md` (research notes written after
  the transcription was frozen), `*_doubts.md`, `*_inventory.csv`, `progress.log`. A folder named
  `first_pass_checkpoint_<NNN>` holds a checkpoint of a package still being transcribed.
- `packages/<package>/PROMPT.md`: the prompt as sent.
- `packages/<package>/second_pass/`: the line-by-line check against the scans: corrected page files, `*_changes.md`
  (every change with the first reading, the corrected one, what the scan shows and a confidence) and
  `*_notes_checked.md` (the research notes checked), with the prompts in `second_pass/prompts/`.
- `typescripts/api_20261112/`: typed and printed pages transcribed through the Anthropic API (Pursuing Stacks, both EGA
  V versions, two copies of the Esquisse d'un programme, the Montreal seminar of 1970, Tapis de Quillen, the typed part
  of cote 119, Brown's translations of two letters), with the run records.
- `typescripts/codex_web_20261113/`: typed letters, lists, tables and the cote 10 typescript transcribed in Codex web,
  one folder per batch with its prompt.
- `research/plans/`: the archive plan, the section map and the reading of the archive as one programme.
- `research/prompts/`: research prompts on the archive's mathematics (their returns are published with La Longue Marche).

## Packages

| Package | First pass | Prompt as sent | Second pass |
|---|---|---|---|
| `MPL_142_001-093` | yes | yes | yes (100 files) |
| `MPL_142_094-122` | yes | yes | yes (33 files) |
| `MPL_144_001-061` | yes | yes | not yet |
| `MPL_144_062-121` | yes | yes | not yet |
| `MPL_144_122-167` | checkpoint_164 | yes | not yet |
| `MPL_144_168-184+148_001-028` | yes | yes | not yet |
| `MPL_146_001-099` | yes | yes | not yet |
| `MPL_146_100-134` | yes | yes | not yet |
| `MPL_147_003-047` | yes | yes | yes (51 files) |
| `MPL_147_048-137` | yes | yes | yes (100 files) |
| `MPL_147_138-190` | yes | yes | not yet |
| `MPL_149_001-090` | yes | yes | yes (100 files) |
| `MPL_149_091-136` | yes | yes | yes (52 files) |
| `MPL_16+47+54+44` | yes | yes | not yet |
| `MPL_1_002-050` | yes | yes | not yet |
| `MPL_5+6_001-037` | yes | yes | not yet |
| `MPL_6_038-067+7_001-060` | yes | yes | not yet |
| `MPL_7_061-072+8_001-078` | yes | yes | not yet |
| `MPL_8_079-081+9+4+100` | yes | yes | not yet |

## Related repositories

- La Longue Marche à travers la théorie de Galois (edition, companion, research returns):
  https://github.com/KokunoYumeto/grothendieck-longue-marche
- Les Dérivateurs (edition and companion): https://github.com/KokunoYumeto/grothendieck-derivateurs
- The French-school editions (EGA, FGA, SGA) and their site: https://github.com/KokunoYumeto/ega-fga-sga and
  https://kokunoyumeto.github.io/ega-fga-sga/
- SGA in French and English: https://github.com/KokunoYumeto/sga-fr, https://github.com/KokunoYumeto/sga-en

## Droits / Rights

Les droits sur l'œuvre originale appartiennent à son auteur ou à ses représentants ou ayants droit. Notre transcription, notre traduction, nos corrections et notre composition ont été produites par IA. Elles n'ont pas d'auteur humain et, selon notre compréhension, ne sont pas protégées par le droit d'auteur ; là où un droit nous appartiendrait malgré tout, il est versé au domaine public sous CC0 1.0. Tout ce travail reproduit ou traduit le texte de Grothendieck, dont les droits appartiennent à ses ayants droit : rien ici n'accorde de licence ni n'autorise une reproduction, une traduction ou un autre usage de son œuvre. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons
aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici,
veuillez ouvrir une issue GitHub et nous la retirerons.

**Prompts et méthode.** Les prompts, les gabarits, les scripts et la méthode de travail publiés ici sont versés au domaine public sous CC0 1.0. Si vous voulez faire un travail semblable, utilisez-les librement ; nous n'y revendiquons aucun droit.

The rights in the original work belong to its author or the author's representatives or heirs. Our transcription, translation, corrections and typesetting were produced by AI. They have no human author and, in our understanding, are not protected by copyright; where any right of ours exists nonetheless, it is dedicated to the public domain under CC0 1.0. All of this work reproduces or translates Grothendieck's text, whose rights belong to his heirs, so nothing here licenses or authorizes any reproduction, translation or other use of his work. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.


**Prompts and method.** The prompts, templates, scripts and working method published here are dedicated to the public domain under CC0 1.0. If you want to do similar work, use them freely; we claim no rights in them.

## Considérations sur les droits

**Les textes de Grothendieck.** Les droits appartiennent à ses ayants droit ; ses textes sont protégés jusqu'à la fin
de 2084. L'Université de Montpellier publie les scans de ses papiers mathématiques (https://grothendieck.umontpellier.fr/archives-grothendieck/) avec l'accord de ses
ayants droit. Nous ne détenons aucune licence de ses ayants droit et ne revendiquons aucun droit sur ses textes.

**La déclaration de Grothendieck du 3 janvier 2010.** Il y déclarait n'avoir pas l'intention de publier ou de republier ses textes, ni leurs traductions, et tenait pour illicite à ses yeux toute édition faite sans son accord par le passé, ou à l'avenir de son vivant. Depuis sa mort en 2014, la décision appartient à ses ayants droit, qui ont accepté la publication en ligne de ses papiers mathématiques par l'Université de Montpellier. C'est sur cette base que nous publions.

**Éditions et transcriptions antérieures.** D'autres ont édité ou transcrit avant nous des parties de ces papiers :
- *Les Dérivateurs* : l'édition électronique de M. Künzer, J. Malgoire et G. Maltsiniotis (https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html) ;
- *La Longue Marche à travers la théorie de Galois* : le tome 1, édité par J. Malgoire (Université Montpellier II,
  1995), et les transcriptions de M. Carmona avec M. Künzer (https://agrothendieck.github.io/) ;
- *Pursuing Stacks* : la transcription de M. Carmona (https://arxiv.org/abs/2111.01000), qu'il a versée au domaine public sous CC0, et
  l'édition de G. Maltsiniotis, *À la poursuite des champs*, vol. I (SMF, 2022) ;
- les transcriptions du Centre d'études grothendieckiennes (https://csg.igrothendieck.org/), qui déclare les publier avec le consentement des
  ayants droit.

À part cette déclaration, aucune de ces éditions n'indique détenir une licence des ayants droit, et une transcription ne
donne à son auteur aucun droit sur le texte transcrit. Nous faisons le même travail avec l'IA pour l'ensemble des
archives : pour rendre le tout disponible en LaTeX modifiable, avec des traductions, et comme une seconde lecture à côté
de celles qui existent. Ce n'est ni une revendication d'antériorité ou de supériorité, ni une revendication de droits
que nous ne détenons pas. Si les éditeurs d'une édition antérieure préfèrent que nous retirions ce que nous avons fondé
sur leur travail, pour que le leur reste seul, nous le ferons par courtoisie.

**Œuvres ayant une édition autorisée.** Lorsqu'une œuvre a une édition publiée avec l'autorisation des ayants droit,
comme *Récoltes et Semailles* (Gallimard, 2022), nous ne la reproduisons ni ne la traduisons ; tout au plus écrivons-nous
notre propre commentaire sur ses mathématiques.

**Textes d'autres auteurs.** Nous ne transcrivons ou ne traduisons les textes d'autres auteurs que lorsque les ayants
droit, ou l'institution qui détient ces textes, les ont rendus publiquement accessibles pour l'étude. Par exemple les
carnets de Daniel Quillen, que le Clay Mathematics Institute a numérisés et mis à la disposition de la communauté
mathématique (https://www.claymath.org/online-resources/quillen-notebooks/), et les exposés du Séminaire Bourbaki et les rédactions de Bourbaki que Grothendieck a
réutilisés ou gardés parmi ses propres notes, que l'Université publie avec ses papiers. C'est notre lecture de bonne
foi, non une revendication de droits. Si vous détenez des droits sur l'un de ces textes et vous y opposez, ouvrez une
issue GitHub et nous le retirerons.

## Rights considerations

**Grothendieck's texts.** The rights belong to his heirs; his texts are protected until the end of 2084. The University
of Montpellier publishes the scans of his mathematical papers (https://grothendieck.umontpellier.fr/archives-grothendieck/) with his heirs' agreement. We hold no licence
from his heirs and claim no rights in his texts.

**Grothendieck's declaration of 3 January 2010.** He declared that he did not intend to publish or republish any of his texts, or translations of them, and that any edition made without his agreement in the past, or in the future during his lifetime, was illicit in his eyes. Since his death in 2014 the decision lies with his heirs, who have agreed to the University of Montpellier's online publication of his mathematical papers. We publish on that basis.

**Earlier editions and transcriptions.** Others have edited or transcribed parts of these papers before us:
- *Les Dérivateurs*: the electronic edition by M. Künzer, J. Malgoire and G. Maltsiniotis (https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html);
- *La Longue Marche à travers la théorie de Galois*: tome 1, edited by J. Malgoire (Université Montpellier II, 1995),
  and the transcriptions by M. Carmona with M. Künzer (https://agrothendieck.github.io/);
- *Pursuing Stacks*: M. Carmona's transcription (https://arxiv.org/abs/2111.01000), which he dedicated to the public domain under CC0, and
  G. Maltsiniotis's edition *À la poursuite des champs*, vol. I (SMF, 2022);
- the transcriptions of the Centre for Grothendieckian Studies (https://csg.igrothendieck.org/), which states that it publishes them with the
  consent of the rights holders.

Apart from that statement, none of these says it holds a licence from the heirs, and a transcription gives its maker no
rights in the author's text. We do the same work with AI for the whole archive: to make all of it available as editable
LaTeX, with translations, and as a second reading beside the existing ones. This is no claim of priority or
superiority, and no claim to rights we do not hold. If the editors of an earlier edition would rather we took down what
we based on their work, so that theirs stands alone, we will do so as a courtesy.

**Works with an authorized edition.** Where a work has an edition published with the rights holders' authorization, as
*Récoltes et Semailles* has (Gallimard, 2022), we do not reproduce or translate it; at most we write our own commentary
on its mathematics.

**Texts by others.** We transcribe or translate other people's texts only where the rights holders, or the institution
that holds the texts, have made them publicly available for study. Examples are Daniel Quillen's notebooks, which the
Clay Mathematics Institute has digitized and made available to the mathematical community (https://www.claymath.org/online-resources/quillen-notebooks/), and the Séminaire
Bourbaki exposés and Bourbaki drafts that Grothendieck reused or kept among his own notes, which the University
publishes as part of his papers. This is our good-faith reading, not a claim of rights. If you hold rights in any of
this and object, please open a GitHub issue and we will take it down.


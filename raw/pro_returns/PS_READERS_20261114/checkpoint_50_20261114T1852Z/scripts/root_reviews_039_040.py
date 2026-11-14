from review_root import review
from pathlib import Path
import json
k='ps_134-2_039'
review(k,changes=[
(r'\mspage{24}',r'\mspage{\hand{24}}','The centered folio is handwritten.'),
(r'\mspage{39}',r'\margin{\hand{39}}','The lower-left 39 is archive numbering, separate from the author folio.'),
(r'\unsure{corres-|derres-}',r'derres-','The enlarged beginning has a d ascender followed by e, rr and es. Preserve the literal derres- rather than normalize the word.'),
(r'\xout{\unsure{1}}',r'\deleted{\unsure{1}}','The dark cancellation before torseurs is penned, not a row of typed x characters. Its underlying character remains uncertain.'),
(r'\unsure{Picard}',r'Picard','The complete word is legible on enlargement.'),
(r'\unsure{correspondaht|correspondant}',r'correspondaht','The penultimate consonant has the tall ascender of h, not n. Preserve the literal source spelling.'),
(r'\unsure{interprétation}',r'interprétation','The complete word remains legible through the locally heavy impression.'),
(r'une\inserted{2-}catégorie',r'une \inserted{2-}catégorie','The handwritten 2- prefix belongs to catégorie, with a preceding word space.'),
(r'les\inserted{0-}objets',r'les \inserted{0-}objets','The handwritten 0- prefix belongs to objets, with a preceding word space.')
],doubts={'unsure':[
(r'\unsure{Hes|les}','doubt retained','The first character is densely overtyped and has more than one vertical stem. The image does not settle the live H/l layer.'),
(r'\over{\unsure{g}}{g}','doubt retained','The live pen g is clear, but its underlying typed character is heavily covered.'),
(r'\unsure{cette}','doubt retained','The apparent word is cette, but overtyping at its initial letter leaves its exact layer unresolved.'),
('derres-','doubt resolved','The enlarged character forms read derres-, including a d ascender and following e.'),
(r'\xout{\unsure{liées par Z et le 2-champ des}}','doubt retained','Large portions of the cancelled phrase are legible, but the densely struck segment around Z prevents a secure complete reading.'),
(r'\deleted{\unsure{1}}','doubt retained','The small old character is covered by a thick pen cancellation; 1 remains plausible, not certain.'),
(r'\over{\unsure{gerbe}}{champ}','doubt retained','The live handwritten champ is clear, but the older gerbe is substantially obscured.'),
('Picard','doubt resolved','All six letters are visible.'),
('correspondaht','doubt resolved','The final cluster is aht, with an unmistakably tall h.'),
('interprétation','doubt resolved','The accented word is recoverable despite the dark initial impression.')
],'illegible':[]},notes=[
'Both numbers are handwritten; 24 is the centered folio, while 39 is now correctly represented as marginal archive numbering.',
'The overtyped first character in Hes/les remains unresolved and marked.',
'Both Gamma signs and the inequality signs are handwritten as represented; none is silently replaced by a different symbol.',
'The long phrase after Z-gerbes is cancelled on the typewriter. Its whole reading remains doubtful because some letters are covered.',
'Derres- and correspondaht are resolved as literal source spellings; interprétation is clear. The overtyped cette remains doubtful.',
'The left-margin cross beside item 2 is present and retained.',
'The first Ext range ends with the clearly typed numeral 1. The witness numeral 2 changes the formula and is rejected.',
'Exemples, is handwritten above the penned cancellation of uns.'
],summary='Both scan halves and eight enlarged details inspected. Distinguished the handwritten author and archive numbers, resolved literal derres- and correspondaht, resolved Picard and interprétation, corrected the pen cancellation before torseurs, and repaired two whole-word spaces. Six original doubts remain under overtyping or cancellation. The source has Z-1-gerbes, Z-1-champ, and the first Ext range 0 through 1; these are not replaced by witness readings.',differences={
547:('sous la gerbe précédente','the typescript reads as our transcription','The typed article is la, not le.'),
549:('sss','the typescript reads as our transcription','The typescript has the three-letter abbreviation; the witness expands it.'),
550:('le 2-champ de Picard strict,','the typescript reads as our transcription','Champ is singular, strict is an interlinear typed insertion, and its comma is visible.'),
551:(r'Picard \inserted[typed]{strict,} des Z-gerbes\xout{\unsure{liées par Z et le 2-champ des}}','the typescript reads as our transcription','The interlinear typed correction and cancelled continuation are both present; the old phrase remains uncertain.'),
552:(r'Z-\inserted{1-}gerbes','the typescript reads as our transcription','The inserted character is the numeral 1; it is not the letter L used by the witness.'),
555:(r'la Z-1-\over{\unsure{gerbe}}{champ}','the typescript reads as our transcription','The baseline has numeral 1. The handwritten live replacement is champ; its older word remains doubtful.'),
557:('des Z-1-gerbes','the typescript reads as our transcription','The typed numeral 1 has its clear top stroke and foot; the witness L is unsupported.'),
558:('correspondaht','our transcription corrected','The image resolves the original doubt as a literal h, whereas the witness normalizes it to n.'),
559:(r'\hand{tronquée} en degré 3','the typescript reads as our transcription','The handwritten word includes final e and agrees grammatically with résolution, not the witness tronqué.'),
566:(r'0 \hand{\leqslant} i \hand{\leqslant} 1','the typescript reads as our transcription','The upper bound is 1. This separates the ordinary lower Ext groups from the unusual Ext2 mentioned just before; the witness 2 alters that distinction.')
})

k='ps_134-2_040'
space=r'\margin{\(\uparrow\) espace \(\downarrow\)}'
review(k,changes=[
(r'\xout{\unsure{envoyer}}',r'\xout{envoyer}','The cancelled word is recoverable letter by letter under the typed x impressions.'),
(r'n \geq 1',r'n \hand{\geq} 1','The greater-than-or-equal sign is drawn in pen.'),
(r'(E,\emptyset)',r'(E,\hand{\phi})','The named isomorphism is a handwritten phi with a long curved stem through the oval; it is not an empty-set sign.'),
(r'et $\emptyset$ un isomorphisme',r'et $\hand{\phi}$ un isomorphisme','The same handwritten phi recurs as the isomorphism variable.'),
(r'\underline{\unsure{H|G}}_m',r'\underline{H}_m','The enlarged underlined character has the two upright stems and crossbar of H. Preserve the mathematical slip rather than substitute G.'),
(r"\unsure{qu'objets|qui objets}",r"qu'objets",'The pen trace after qu is an apostrophe; there is no intervening i.'),
(r'\unsure{leut|leur}',r'leut','The final letter is a typed t with a crossbar. Preserve this reading in the diplomatic form.'),
(r'\margin{espace}',space,'The handwritten spacing instruction has both an upward and a downward arrow. Both arrows were omitted and are now represented.')
],doubts={'unsure':[
('envoyer','doubt resolved','The seven underlying letters are recoverable despite cancellation.'),
(r'\unsure{vérfie|vérifie}','doubt retained','Several superposed interior impressions do not securely separate the intended live sequence from the overtyped letters. The following cancelled phrase is legible.'),
('H','doubt resolved','The underlined character is visibly H, not G; its mathematical significance is addressed only in the guide.'),
("qu'objets",'doubt resolved','The handwritten apostrophe is clear.'),
('leut','doubt resolved','The final character is t; the same phrase uses correctly typed leur immediately afterward.')
],'illegible':[]},notes=[
'The centered 25 and lower-left 40 are penned; their distinct foliation functions are preserved.',
'The cancelled word after copie de is envoyer; its reading is now certain.',
'The interior letters of vérfie/vérifie remain uncertain under overlapping impressions. The cancelled passant aux champs correspondant, qui sont is retained.',
'The image settles H in H1(X,Hm). No mathematical correction is made in any reader.',
'The arrow joining the two Hom expressions is handwritten and remains marked.',
'The inserted phrase reads en tant qu\'objets de catégories dérivées, with apostrophe.',
'The word espace and its two opposed arrows instruct additional separation between App.1 and App.2. The graphic is preserved diplomatically and the spacing applied through an explicit master variant.'
],summary='Both scan halves and six enlarged details inspected. Resolved envoyer, underlined H, qu\'objets and leut; retained the densely overtyped vérfie/vérifie. Corrected two empty-set misreadings to handwritten phi, marked the pen inequality, and restored both arrows of the marginal spacing instruction. The source mathematical Hm remains untouched, while one-off leut has a separately recorded corrected-form variant supported by leur in the next clause.',differences={
569:('complexe tronqué','the typescript reads as our transcription','The word tronqué is present, despite a darker impression at its beginning; the witness omits it.'),
575:(r'H^1(X,\underline{H}_m)','our transcription corrected','The image resolves the original H/G doubt as H. The witness G is mathematically natural but does not reproduce the source.'),
577:('sans doute','the typescript reads as our transcription','The final s of sans is clear; the witness san omits it.'),
578:('no descriptive heading','the typescript reads as our transcription','The image contains the handwritten App.2 marker, without the witness editorial section title.'),
579:(r'\inserted{(App.2)}','the typescript reads as our transcription','The handwritten numbered call is preserved in its own form; it is not expanded into the witness heading.'),
580:(r"\inserted{(en tant qu'objets de catégories dérivées)}",'our transcription corrected','The apostrophe is visible; the witness qui objets is unsupported.'),
582:('leut','our transcription corrected','The image settles final t. A separate one-off-slip variant changes it to leur only in the corrected forms, supported by leur in the following clause on this checked page.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json'
v=json.loads(p.read_text());v=[x for x in v if x.get('source_id') not in ['SPACE:040:1','DIFF:582']]
v.extend([
dict(key=k,before=space,after=r'\par\medskip',kind='author spacing cue',reason='Apply the opposed arrows and espace instruction as additional paragraph separation before App.2; retain the graphic diplomatically.',source_id='SPACE:040:1'),
dict(key=k,before='leut caractère',after='leur caractère',kind='slip corrected',reason='One-off t for r; leur is correctly typed in the following clause referring to the same Picard structure.',source_id='DIFF:582')])
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

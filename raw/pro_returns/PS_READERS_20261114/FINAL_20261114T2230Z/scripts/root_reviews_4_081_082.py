from review_root import review
from pathlib import Path
import json

P=Path(__file__).resolve().parents[1]

def arrows(key, changes):
    s=(P.parent/'inputs/text/transcription/ps_pages'/(key+'.tex')).read_text()
    for a,b,_ in changes:s=s.replace(a,b,1)
    for line in s.splitlines():
        new=line
        for macro in [r'\longrightarrow',r'\longmapsto',r'\mapsto',r'\to']:
            new=new.replace(macro,r'\hand{'+macro+'}')
        if new!=line:changes.append((line,new,'The shafts, heads and mapsto bars are continuous irregular pen strokes, while the object and functor letters remain typed.'))
    return changes

c=[
 (r'\unsure{de|do}','de','The enlarged scan clearly has a closed e with a horizontal middle bar. The diplomatic text keeps the typed de.'),
 (r"(M'\xout{p},W')",r"(M'\over{p}{,}W')",'The p is covered by a short heavy pen comma; it is not cancelled by a regular typewriter x.'),
 (r'\unsure{localizer|hocalizer}',r'\unsure{\over[typed]{h}{l}}ocalizer','A regular l-shaped stem and an h shoulder are both visible in the initial cell. The h-to-l overwrite order is plausible but remains doubtful.'),
 (r'\underline{W} \subset F\unsure{l}',r'\underline{W} \hand{\subset} F\over{l}{\ell}','The inclusion curve is drawn in pen. The typed l is crossed by a separate diagonal pen stroke.'),
 (r'\xout{dxfx}',r'\xout{\unsure{def.}}','The cancelled short abbreviation has clear d and f, while the middle and last impressions are partly blackened; def. is retained only as a doubtful reading, not literal cancellation x characters.'),
 (r'\inserted{below} \deleted{on}',r'\inserted[typed]{below} on','Below has regular typewriter letters. The single placement curve under it grazes the tops of on but does not cancel that word; independent image inspection agrees that on remains live.'),
 ('A can be considered',r'A \over{c}{c}an be considered','The c has a long irregular pen retracing extending above the typed body.'),
 ('The category',r'T\unsure{\ensuremath{\overset{\perp\perp}{\mathrm h}}}e category','Two small raised marks sit above h. Their graphic shape is retained without an unsupported provenance or letter replacement.'),
 (r'\inserted{of $\underline{W}_{\unsure{A^{\wedge}|A}}$}',r'\inserted[typed]{of $\underline{W}_{A^{\wedge}}$}','The insertion is typed, with a pen placement curve. A distinct raised caret follows the subscript A; this source subscript is preserved even though the preceding definition uses W_A.'),
 (r'A_{/F\mathrm{x}G} \longrightarrow A_{/G}',r'A_{/F\mathrm{x}G} \longrightarrow A_{/\over[typed]{F}{G}}','The live target is G, with a regular F-shaped earlier impression visible inside it; independent inspection confirms both layers.')
]
review('ps_134-4_081',owner='134_4_tail',changes=arrows('ps_134-4_081',c),doubts={'unsure':[
 ('de','doubt resolved','The final letter has the visible crossbar and open-right shape of typed e.'),
 (r'\unsure{\over[typed]{h}{l}}ocalizer','doubt narrowed','Both initial h/l impressions are visible; the proposed overwrite order remains doubtful.'),
 (r'\over{l}{\ell}','doubt resolved','The typed l and added diagonal pen stroke are separately legible.'),
 (r'A^{\wedge}','doubt resolved','The raised caret after the subscript A is clearly visible in the enlarged insertion.')
 ]},notes=[
 'The word is clearly typed de, not do. An explicit corrected-form slip variant is supported by the same construction do not on p162.',
 'The comma is a short heavy pen stroke over the typed p, not an additional comma after a typewriter cancellation.',
 'The initial h/l cell is a regular typed overprint, whose order remains doubtful. Fl has a separate diagonal pen stroke on its l; the inclusion sign is handwritten.',
 'The insertion reads of W with subscript A-caret; both the words and the subscript are typed, with a handwritten placement curve.',
 'The isolated dark speck lies above the gap before it, well to the left of the apostrophe. It does not cancel the apostrophe and supplies no readable replacement.',
 'Two raised short marks above h are retained as an uncertain graphic, as on neighbouring pages; darkness alone does not settle their provenance.',
 'The short isolated left-margin strokes contain no legible lexical or mathematical content or clear attachment to a text correction.',
 'The lower-left 81 is handwritten archive foliation.'
 ],summary='Both halves and ten enlarged details inspected. Resolved de, the Fl pen stroke and the subscript A-caret; preserved the initial h/l overwrite uncertainty. Restored the pen comma over p and the pen retracing of c. Below and of W_A-caret are typed insertions. The placement curve under below is not a deletion of on, confirmed independently. All arrows are marked as pen. The displayed target is G over typed F, while the missing prime on M and the noun basic modelizer remain unchanged for discussion in the guide.',differences={
 4637:(r"\bar{u}:W^{-1}M\hand{\to}W'^{-1}M",'the typescript reads as our transcription','The final M has no prime on the scan; the witness supplies it and parentheses around W-prime. This mathematical correction is confined to the guide.'),
 4639:('a basic modelizer','the typescript reads as our transcription','The source noun is plainly modelizer. The witness changes it to localizer.'),
 4641:('on','our transcription corrected','The purported strike is the single placement curve for typed below. It does not cancel on, which remains live; a second inspection agrees.'),
 4642:('more general test functors','the typescript reads as our transcription','The typed vowel is o in more; the witness mere is not supported by the scan.'),
 4649:(r'A_{/F\mathrm{x}G}\hand{\longrightarrow}A_{/\over[typed]{F}{G}}','our transcription corrected','The live target is G, not the witness F. The older typed F beneath G is now also recorded; the arrow is handwritten.'),
 4650:('for G an object a','the typescript reads as our transcription','The source says an, without the additional d of the witness and.')
 })
vp=P/'records/MASTER_VARIANTS_134_4_tail.json';vv=json.loads(vp.read_text())
vv=[v for v in vv if v['source_id']!='UNSURE:ps_134-4_081:1']
vv.append(dict(key='ps_134-4_081',before='We de not assume',after='We do not assume',kind='slip corrected',reason='The scan clearly types de. The identical auxiliary construction do not on p162 and the present clause settle this isolated wrong vowel; the diplomatic source retains de.',source_id='UNSURE:ps_134-4_081:1'))
vp.write_text(json.dumps(vv,indent=2)+'\n')

c=[
 (r'\simeq',r'\hand{\simeq}','Both the wavy upper stroke and straight lower stroke are visibly hand-drawn.'),
 (r'for \deleted{a}\inserted{the} \uline{map}',r'for \xout{a}\inserted[typed]{the} \uline{map}','The a has a regular typewriter x cancellation and the interlinear the is typed; only its placement curve is pen.'),
 (r'(\deleted{a}\inserted{the} localization',r'(\xout{a}\inserted[typed]{the} localization','The second a is likewise cancelled by a regular x and the interlinear the uses typewriter letters.'),
 (r'\inserted{and map $a \to G$}',r'\inserted[typed]{and map $a \to G$}','The inserted words and letters are regular typing; its placement bracket and arrow are pen.'),
 (r'G\unsure{\xout{x}}',r'G\xout{\unsure{a}}','The extra subscript cell has a clear typewriter x across an older a-like lower bowl. The cancellation is certain, but the base letter remains doubtful.'),
 (r'\hand{A)}',r'\noindent\hand{\rule{6em}{.3pt}}\par\hand{A)\deleted{\illegible{1}}}','Restore the separate horizontal pen rule above the heading and the blackened earlier label immediately under A). The earlier label cannot be read securely.'),
 (r'th\unsure{\over{is}{e}} condition',r'th\over{is}{e} condition','A continuous pen e loop and middle stroke cross the still-visible typed is; the correction to the is clear.')
]
review('ps_134-4_082',owner='134_4_tail',changes=arrows('ps_134-4_082',c),doubts={'unsure':[
 (r'\xout{\unsure{a}}','doubt narrowed with corrected reading','The cancelling x is clear; the old subscript letter has an a-like bowl but remains partly obscured.'),
 (r'\over{is}{e}','doubt resolved','The visible continuous pen e crosses both typed letters is, yielding the.')
 ]},notes=[
 'The equivalence sign has continuous pen strokes, both upper wave and lower bar, and is now marked as handwriting.',
 'The extra subscript letter after G is cancelled by a typewriter x. Its a-like base remains doubtful.',
 'The heading underline crosses the top of Before starting because of its position, without cancelling that sentence. A) stands above a blackened earlier label, now retained as an unreadable pen cancellation. A separate pen rule above the heading is also restored.',
 'The pen e loop and cross stroke clearly replace typed is in this, so the final reading is the.',
 'The lower-left 82 is handwritten archive foliation.'
 ],summary='Both halves and five enlarged details inspected. Corrected the provenance of the two typed the insertions and their typewriter cancellations, and of the and-map insertion; marked the equivalence and all arrows as pen. The extra subscript character remains doubtful under a clear x strike. Restored the horizontal pen rule and unreadable earlier heading label. Resolved the final the correction. The typed and handwritten qualifications defining total asphericity, including the added requirement that A itself be W-aspheric, are preserved.',differences={
 4653:('nor is it implied by it','the typescript reads as our transcription','The source clearly types implied, not the witness implies.'),
 4661:(r'objects \inserted{in $A^\wedge$} is again','the typescript reads as our transcription','The pen qualification in A-caret is clearly inserted at objects and is absent from the witness.'),
 4662:(r'This is \deleted{just} a tautology','the typescript reads as our transcription','The pen zigzag clearly cancels just; the witness incorrectly retains it as live text.'),
 4664:(r'\uline{totally} \uline{$\underline{W}$} - aspheric\hand{(*)}.','the typescript reads as our transcription','The handwritten parenthesized asterisk is present after aspheric; the witness omits it.'),
 4665:(r'\margin{X}','the typescript reads as our transcription','The handwritten marginal cross beside Definition1 is visible and is absent from the witness.')
 })

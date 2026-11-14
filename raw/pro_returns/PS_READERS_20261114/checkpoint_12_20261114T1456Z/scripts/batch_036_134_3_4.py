import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_036';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');edits=[]
def e(a,b,r):edits.append([a,b,r])
e(r'\margin{ch}',r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=3pt] (n) {ch};\end{tikzpicture}}}','The marginal ch is enclosed in an oval, which the original source omitted.')
e(u[0][0],'c','The enlargement retains the typewriter c beneath the hand-written ch correction.')
e(u[1][0],'n','The underlying typed n is legible above the lower pen retracing in In.')
e(u[2][0],r'\over{h}{h}','The hand mark beneath the typed h is a retracing of h; the word The is unambiguous.')
e(u[3][0],'for our','The enlarged cancellation has for, an x over the blank, and the three letters our; it is not for us.')
e(u[4][0],'p','The typed p bowl and descending stem remain visible under the handwritten g in giving.')
e("it's fibers",r"it\hand{'}s fibers",'The apostrophe is dark hand retouching in the enlarged crop; retain its source presence and mark its pen layer.')
e(r'\margin{$|$}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\draw (0,0)--(0,-3.6);\end{tikzpicture}}}','The left margin has a long vertical pen line spanning the final four lines, rather than a single short bar glyph.')
conf=dict(key=key,edits=edits,diffs={
2076:[r'\over{c}{ch}aracterization','The old c is recognizable beneath the handwritten ch; the margin repeats ch in an oval.','correct transcription'],
2078:['we actually knew it','Knew has the typed e and w; do not replace it with the witness know.'],
2079:[r"it\hand{'}s fibers",'The apostrophe is present and penned or retraced; the author\'s possessive spelling is retained.','correct provenance'],
2080:['30.','The section starts with the number30 and has no title on the page.'],
2081:['Since Last week','A capital L is visibly present, with an overtyped trace; retain capitalization.'],
2086:[r'Last thing I did\hand{,} before reading','The comma is handwritten at the end of did and is absent from the witness wording.'],
2088:[r'as \over{p}{g}iving','The scan has as followed directly by corrected giving; there is no added a between them. The preceding cancelled group reads for our.','correct transcription']},
unsure=[['c','The old typed c remains visible under the ch correction.'],['n','The upper typed n and lower retracing are distinguishable.'],[r'\over{h}{h}','The hand trace is a second h over the typed h.'],['for our','The enlarged cancellation resolves our with a final r.'],['p','The p body and descender can be distinguished below the new g.']],
illegible=[],notes=['The typed c beneath ch is resolved; the matching circled margin ch is reconstructed.','The old typed n is clear despite the lower pen retracing.','The lower mark under h in The is a retracing, now retained without doubt.','The canceled phrase is for our and the old first letter of giving is p, both resolved in the enlargement.','The apostrophe in it\'s is visible and darkly retouched by hand, now marked.','The parenthetical or aspheric and even are typewritten insertions with pen placement brackets, as already marked.','The long vertical margin line spans the final four lines and is reconstructed to express its extent.','The first letter of Last is capital L despite overtyping; it is not silently lowercased.'],
evidence='Both halves inspected and five close crops reviewed. The old c under ch, n in In, retraced h in The, cancelled for our and p under giving are all resolved from the image. The apostrophe in it\'s is a visible pen touch. The circled ch and long final margin bar are reconstructed. The hand additions we started with and which I took up remain, while or aspheric and even are typed insertions with pen positioning marks. The source reads knew, Since Last, conrete, dependant spelling independant, and catégorie-style accented catégory; no witness normalization is adopted. Section30 is numbered without a title and begins the explicit withdrawal of the earlier model-category assumption with the stipulated weak equivalences and cofibrations.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)

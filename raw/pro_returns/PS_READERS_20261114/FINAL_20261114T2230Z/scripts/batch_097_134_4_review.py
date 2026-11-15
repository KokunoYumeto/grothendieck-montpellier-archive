import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_097'
edge=r'\xout{\illegible{1}}\unsure{\diagram{\begin{tikzpicture}[baseline=-.3ex]\draw[color=blue] (0,0) to[out=110,in=225] (.10,.18);\end{tikzpicture}}}'
edits=[
 [r'\unsure{t}\hand{h}ird',r'\over[typed]{\unsure{n|t}}{t}\over{h}{h}ird','The live initial t is regular typing over a crowded older n/t-like cell; the h is pen retracing over a typed h. Preserve the older-cell doubt.'],
 [r'T\hand{h}ese',r'T\over{h}{h}ese','The long penned h stem and lower arch overlie a visible typed h.'],
 [r'because\inserted{say} of',r'because \inserted{say} of','Keep the word boundary before the hand-inserted say.'],
 [r'\unsure{endowed}',r'e\over[typed]{\unsure{h}}{n}dowed','The live n resolves, but the older tall-stemmed h-like impression remains tentative.'],
 [r'$W \subset F\ell(M)$',r'$W \hand{\subset} F\over{l}{\ell}(M)$','The inclusion is hand-drawn, and the typed l has a separate slanted pen stroke.'],
 [r'\uline{in the gontext}',r'\uline{in the gonte\over[typed]{x}{x}t}','The x has repeated regular impressions. Keep the typed initial g diplomatically; its isolated-slip correction is recorded separately.'],
 ['localizing\nmaps',r'localiz\over[typed]{a}{i}ng'+'\nmaps','The second i has its dot and stem over the rounded body of an earlier typed a.'],
 [r'a\hand{ll} maps',r'a\over{f}{l}\over{l}{l} maps','The two live l letters are penned; the first overlies a typed f with crossbar and the second a typed l.'],
 [r"\inserted{I'd think}",r"\inserted[typed]{I'd think}",'The interlinear phrase is typed; its pen placing curve points after maps and leaves in live.'],
 [r'UW \subset W \subset F\ell(M)',r'UW \hand{\subset} W \hand{\subset} F\over{l}{\ell}(M)','Both inclusion signs and the slanted stroke on the typed l are handwritten.'],
 [r'\inserted{a property,}',r'\inserted{a property}','The apparent terminal comma is the upturned end of the continuous placing curve, not independent punctuation.'],
 [r'f \in UW',r'f \hand{\in} UW','The membership sign has an irregular handwritten curve and crossbar.'],
 [r'\xout{\unsure{x}}',edge,'The older clipped character under the regular x cancellation is unreadable. Preserve the separate raised curved mark graphically under a doubt instead of naming it x.']
]
save_review({'key':key,'edits':edits,'diffs':{
4901:[r'basic ones\hand{,}','The independent right-edge comma is visibly handwritten.'],
4905:[r'$F\over{l}{\ell}(M)$\hand{,}','The comma after M is present; the l also bears a handwritten slanted stroke.'],
4908:['coarse','Coarse is plainly typed, unlike the witness course.'],
4913:[r'case\xout{s}','The final s is machine-cancelled. The witness wrongly leaves it live.'],
4915:['a property, with no textual terminal comma','The comma-like right hook is continuous with the long placing curve. It is not an independent handwritten comma.','correct transcription; placing mark'],
4916:['closing quotation marks after UW','The typed pair is present.'],
4909:['gontext diplomatically; context only in corrected forms','The first glyph is typed g. The same word context is correctly typed on reviewed 134-4/095 and the present phrase uniquely requires it.','isolated slip recorded'],
4917:['notes diplomatically; noted only in corrected forms','The final s is typed. The identical construction It should be noted is attested on reviewed 134-3/017,032 and088.','isolated slip recorded']
},'unsure':[
[r'\over[typed]{\unsure{n|t}}{t}','The live t resolves, while its older overprinted cell remains uncertain.'],
[r'e\over[typed]{\unsure{h}}{n}dowed','The live word is endowed; the old tall cell beneath n remains tentative.'],
[r'\unsure{``}','The left-margin spot is a compact dark blob, with no separable pair of quote strokes. Retain the tentative quote.'],
[r'\illegible{1}','The edge clips the old character beneath the x and the added raised curve. No earlier letter can be recovered securely.']
],'notes':[
'The initial t of third resolves over an uncertain older n/t cell. Both third and These have pen h over visible typed h, rather than wholly new h insertions.',
'Endowed has live n over a tentative older h-like type impression. The second i of localizing is typed over a clear rounded a.',
'The opening quotation mark remains tentative because the dark spot has no separable strokes.',
'The old final character is unreadable under its typewriter x and edge clipping. The separate raised curved mark is preserved as a doubtful graphic.',
'The three inclusion signs and the final membership sign are penned. Both Fl expressions have typed l plus an oblique pen stroke.',
'The pencil archive folio 97 is visible at the bottom left.'
],'extra_records':[
{'source_id':'OBS:ps_134-4_097:gontext','before':r'\uline{in the gonte\over[typed]{x}{x}t}','after':r'\uline{in the conte\over[typed]{x}{x}t}','decision':'isolated typing slip in corrected forms','reason':'The unique contextual word is context, correctly typed in reviewed 134-4/095. Retain the typed g and repeated x in the diplomatic source; change only the initial g in corrected forms.'},
{'source_id':'OBS:ps_134-4_097:notes','before':'It should be notes that','after':'It should be noted that','decision':'isolated typing slip in corrected forms','reason':'The image types notes. The same construction and word noted are correctly typed in reviewed 134-3/017,032 and088; the participial construction settles this isolated final s/d slip.'}
],'evidence':'Both original halves and fourteen enlarged panels inspected. Third has a clear live typed t over an older doubtful n/t cell and a pen h over type; These also has pen h over typed h. Endowed resolves except for the old h-like impression under n. Devise retains its handwritten i over a. The three inclusion signs, membership sign and slanted strokes over typed l are handwritten. Gontext and notes are literal typed slips, recorded for corrected-only variants with same-word evidence on reviewed pages. Localizing has typed i over a, and all has pen l over f followed by pen l over l. The phrase I would think in contracted form is typed interlinearly, with the following in left live. The hook after a property is continuous with its placing curve and is removed as spurious verbal punctuation. The opening quote and clipped cancelled terminal character remain unresolved; a distinct raised curved mark at that edge is preserved graphically. The page explicitly retracts the earlier generic use of aspheric and introduces UW without assuming its saturation.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';vs=json.loads(p.read_text())
for before,after,sid,reason in [(r'\uline{in the gonte\over[typed]{x}{x}t}',r'\uline{in the conte\over[typed]{x}{x}t}','gontext','The same word context is correctly typed on reviewed 134-4/095; preserve gontext only diplomatically.'),('It should be notes that','It should be noted that','notes','The same construction It should be noted is correctly typed on reviewed 134-3/017,032 and088.')]:
 v={'key':key,'before':before,'after':after,'kind':'isolated typing slip','reason':reason,'source_id':f'OBS:{key}:{sid}'};vs=[x for x in vs if x['source_id']!=v['source_id']]+[v]
p.write_text(json.dumps(vs,ensure_ascii=False,indent=2)+'\n')
s=(OUT/'checked_pages'/f'{key}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
for m in re.finditer(r'(?<!\\)[{}]',s):
 n+=1 if m.group()=='{' else -1
 assert n>=0,(key,m.start())
assert n==0,(key,n)

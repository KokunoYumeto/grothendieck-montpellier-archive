import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_035';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');edits=[]
def e(a,b,r):edits.append([a,b,r])
for no in [20,38,40,42]:
 a=s.splitlines()[no-1];b=a.replace(r'\hat{}',r'\hand{\hat{}}')
 e(a,b,'The presheaf hat over typed A is handwritten, distinct from the nearby separator stroke.')
e(r"ij(a')\hand{\to}",r"i\over{j}{j}(a')\hand{\to}",'The j has a looped handwritten retracing below its typed stem; the i remains typed.')
e(r'i_A j_A(B)',r'\over{i}{i}_A \over{j}{j}_A(B)','Both i and j in the (T) display are retraced in pen over the typed letters; the A subscripts remain typed.')
e(u[0][0],r"\hand{'}",'The enlarged crop shows a distinct black apostrophe between t and s, added by hand.')
e('homotopy type by an object','homotopy type \\over{by}{by} an object','The b and y are retraced in dark pen, with the descending curved y stroke visible beneath the line.')
e('it appears a lot more','it \\over{app}{app}ears a lot more','The a and the two p letters are retraced in dark pen; the rest of appears remains typed.')
conf=dict(key=key,edits=edits,diffs={
2062:['and hence all we have to see','The word we is typed between all and have.'],
2064:[r'\inserted{[small]}','The handwritten qualifier is enclosed by square brackets, not round parentheses.'],
2068:['atest-category','The a occupies the immediately preceding typewriter position without an extra blank character; retain the joined source form.'],
2069:['elementary normalizer','The word normalizer is plainly typed on the page, although the intended surrounding terminology is modelizer.'],
2070:[r'stronger\hand{(${}^{33}$)}','Only the call33 appears at the phrase stronger; the witness retrospective footnote is absent here.'],
2071:[r"it\hand{'}s favor",'The apostrophe is visible and handwritten; retain the author\'s possessive usage.','correct transcription']},
unsure=[[r"\hand{'}",'The enlargement clearly shows a separate apostrophe above the t/s interval.']],
illegible=[],notes=[
'The j in ij has a handwritten retracing that descends below the typed letter; this layer is now marked.',
'The i_A and j_A letters in the T display are retouched by pen, with typed subscripts; now marked separately.',
'The subset signs, membership sign and arrows are all handwritten; the existing marks are retained and the four previously plain A hats are marked.',
'By and app in appears have pen retouching and are now marked; whether and One remain legible through typewriter overstrikes.',
'The separator after the first A hat, the vertical stroke after the comma in A-hat by, and the later slash by A-hat will are retained. The call33 remains distinct.'],
evidence='Both complete halves inspected; enlarged the atest-category spacing and the apostrophe in it\'s. The upper adjunction conditions and two-way localized arrows match the scan. The j of ij and both i,j in the T display have pen retouching; all subset and membership signs and arrows were already hand marked, while four A hats needed provenance markup. The inserted [small] uses square brackets. The source explicitly says all we have to see, M prime is saturated and M is saturated, normalizer, adcordingly and atest-category; none is normalized from the witness. The apostrophe in it\'s is clear handwriting. The lower by and app of appears are penned over typed letters. The three separation strokes and sole call33 are preserved.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)

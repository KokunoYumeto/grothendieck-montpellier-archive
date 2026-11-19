"""Manual status choices from source assessments; never keyword classification."""
from pathlib import Path
import json,collections
D=Path(__file__).resolve().parent
categories={
'proved there':[1,2,3,4,5,6,7,8,9,10,11,14,15,18,19,20,21,24,26,27,28,30,32,34,35,38,39,41,44,46,48,50,51,53,55,57,66,69,71,72,74,84],
'proof sketched':[22,33,37,60,62,68,73,76,77,81],
'stated without proof':[58,63],
'corrected by himself later':[36,52,59],
'false as stated':[12,17,23,29,31,42,45,47,49,54,56,61,64,65,67,70,75,82,85],
'open on the pages':[13,16,25,40,43,78,79,80,83],
}
E=D.parent/'ega'
core={
'proved there':[14,15,16,18,20,26,28,29,36,53,54,58,59,65,67,85],
'proof sketched':[5,9,11,22,23,27,31,33,35,38,39,40,44,49,55,56,60,62,66,68,70,77,79,84],
'stated without proof':[1,2,3,4,6,8,10,12,13,34,41,47,48,52,57,61,63,64,82,88,95],
'corrected by himself later':[46,50,74],
'false as stated':[7,17,30,32,37,43,71,72,75,78,80,81],
'open on the pages':[19,21,24,25,42,45,51,69,73,76,83,86,87,89,90,91,92,93,94,96,97],
}
notes={
13:'Definitions are given; the surjectivity-only marginal extension is open.',
16:'Definitions and Hom reductions are given, but the unrestricted category-valued programme lacks hypotheses.',
25:'The early leaf recalls the inequality with uncertain indices; the later proof is separately claim082.',
31:'The main exterior theorem is proved, but the normalization assertion included in this record is literally false.',
36:'Earlier equality is replaced by the valid inequality at K1-03 scan79; both source ends are in links.tsv.',
52:'The later operator summary restores the inclusion direction; this is internal evidence, not a silent emendation.',
59:'The later reciprocal-order calculation corrects the earlier order1 remark.',
62:'Scalar result has a proof sketch; vector/set-valued proposals remain undefined research sketches.',
63:'The core Jensen/counting formulas are invoked and calculated; subsidiary literal faults remain in readings.tsv.',
65:'The denial of modern entire holomorphy is false; historical entière may denote bounded type, so no ink decision is made.',
68:'The determinant conclusion is valid; its supplied proof uses a false unitary-polar step and needs a contraction repair.',
70:'The proposed unitary equivalence, marked by an uncertain question glyph, is false; nonzero spectral equivalence survives.',
75:'The Hölder conclusion is proved, but the terminal strict inequality included in this claim is false at equality.',
80:'An explicit conjectural question on the pages; refuted in the present run, not withdrawn by the manuscript author.',
83:'Unbounded ratio is asserted and a pointwise majorant is asked; the present construction resolves both, not authorially.',
}
# The separate source-origin overlay adds this explicitly deferred proof request.
# Include its manually assigned category when validating an already-final build;
# it is absent during the earlier source-builder stage of a full rebuild.
if any(c['id']=='C-SA23-ega-098' for c in json.loads((E/'claims.json').read_text())):
 core['open on the pages'].append(98)
for folder,prefix,mapping,extra in [(D,'C-SA23-analysis_curves-',categories,notes),(E,'C-SA23-ega-',core,{46:'The signed errata are Lê Dũng Tráng’s later correction; the category does not attribute the letter to Grothendieck.',50:'The letter explicitly reinstates the earlier objection on15December1966.',74:'An unconditional converse is cancelled in the source; the corrected restricted argument is retained.',88:'The question is annotated answered, but no proof of the answer is supplied here.',95:'The question is annotated answered, but no proof of the answer is supplied here.'})]:
 data=json.loads((folder/'claims.json').read_text());result={}
 for category,nums in mapping.items():
  for n in nums:
   key=prefix+f'{n:03}'
   assert key not in result,key
   result[key]=category
 assert set(result)=={x['id'] for x in data},(folder,set(result)^{x['id'] for x in data})
 for c in data:
  c['status_category']=result[c['id']]
  n=int(c['id'].rsplit('-',1)[1])
  if n in extra:c['status_category_note']=extra[n]
 (folder/'status_categories.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 (folder/'claims.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(folder.name,dict(collections.Counter(result.values())))

"""Save root's full cote24 site19 visual review."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1];key='ega24_24_019';p=ReviewedPage(source_path(key).read_text())
p.change(r'k^1',r'k1','The enlarged k1 crop and the other two occurrences show a full-size numeral1 with its foot on the main baseline. No prime or raised exponent is supplied.','notation-placement-corrected')
observations=[
 'The folio19 is regular serif printing, without a visible pen layer.',
 'The star after (or20.3) is typed. The bottom star and entire Ask Grothendieck about the numbering system. sentence are penned.',
 'The bar over f(X) is a straight regular rule matching the typed rules elsewhere; no pen irregularity is visible. The following relation is >=0 exactly.',
 'All three k1 forms have a baseline full-size1, confirmed in an enlarged crop. The draft exponent is corrected.',
 'The v after the underlined P is a baseline lowercase letter, retained literally.',
 'The Y in the theorem statement has an underline; the Y in the function-field phrase does not. The existing scopes are correct.',
 'The handwritten footnote is one short sentence; no long handwritten passage occurs.'
]
ns={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}[key]
assert len(ns)==len(observations)
for i,(before,seen) in enumerate(zip(ns,observations),1):p.note(f'NOTES item{i}',before,seen,'checked','Each concern was examined against the full images and the indicated crop.','NOTES')
p.note('7--35','Complete end of Section2 and start of Section3','Every line, heading, formula, index, underline, bar, accent, query and handwritten note was read in both full scan halves.','confirmed','The acute accent in á fortiori, >=0, the n in K(S1,...,Sn), and the baseline k1 strings are retained literally.','full-text')
p.note('11,35','(or20.3)*; Ask Grothendieck about the numbering system.','French counterpart: cote25/site15, the overwritten heading ending20.3.','cross-reference','The translator’s numbering question is retained and tied to the corresponding French heading.','cote24-crossreference')
p.note('30','[en fonction Fr]','French counterpart: cote25/site16, en fonction des S_i after the displayed linear relation.','cross-reference','The literal French gloss is kept within the English witness.','cote24-crossreference')
p.note('33','[PB: check this!] after sending S_i to S_i','French counterpart: cote25/site16, l’inclusion canonique k prime to L s’obtient en envoyant S_i sur S_i.','cross-reference','The query is preserved; the matching French clause is identified without rewriting the map.','cote24-crossreference')
p.note('26','dim bar f(X)>=0','French cote25/site16 has the handwritten strict relation >0. Blass types >=0.','comparison-recorded','Both relations are preserved; the guide records the discrepancy.','cote24-comparison')
p.note('28','L=K(S1,...,Sn)','French cote25/site16 ends this list at S_(n-1). Blass’s final index is n.','comparison-recorded','The different endpoint remains in the text; no mathematical correction is imposed.','cote24-comparison')
p.note('9','characteristic zero arrow smooth=regular','French cote25/site15 has car0, lisse= régulier without this intermediate arrow.','comparison-recorded','The extra typed English arrow remains.','cote24-comparison')
text,ds=p.finish();save(key,text,ds,0,'Every line in both full scan halves read; all queries and the handwritten note inspected; the baseline k1 forms were checked again in a magnified crop.')
print(aggregate())

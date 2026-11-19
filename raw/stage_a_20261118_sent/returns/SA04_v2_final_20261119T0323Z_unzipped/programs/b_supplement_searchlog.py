"""Persist actual supplementary query strings and manually assessed results."""
import csv,json,re
from pathlib import Path
out=Path('/workspace/scratch/594d1dc856a9/SA04_work/parts/b')
rows=[]
def q(n,engine,query,ids,urls,result):
    rows.append([f'B-SQ{n:02}', '2026-11-19',engine,query,ids,urls,result])
dos='https://imag.umontpellier.fr/~dos-santos/Scientific_publications/Fundamental_group_schemes_for_stratified_sheaves.pdf'
katz='https://web.math.princeton.edu/~nmk/old/nilpconn.pdf'
milne='https://jmilne.org/math/Books/EC2.pdf'
chai='https://www.claymath.org/wp-content/uploads/2022/03/cmip08c.pdf'
lara='https://arxiv.org/pdf/1911.01884'
fm='https://arxiv.org/pdf/2201.06402'
stacks='https://stacks.math.columbia.edu/tag/0GIY'
q(1,'Websearch2; author bibliography; primary PDF','dos Santos "Fundamental group schemes for stratified sheaves" 2389 2415','C-SA04-698;C-SA04-699;C-SA04-700;C-SA04-703',dos+';https://imag.umontpellier.fr/~dos-santos/','The deliberately tentative page guess in the query was corrected by author bibliography: Journal of Algebra317(2)(2007),691–713. Proposition13 author pp13–14 opened, with regular/algebraically closed hypotheses and nonclosed-field warning. Publisher direct opening403; author PDF supplies theorem text.')
q(2,'Websearch2; primary volume','site.jmilne.org "Verschiebung" "p" "F" abelian varieties','C-SA04-702;C-SA04-707',milne+';'+chai,'Milne supplies torsion specialization and Hasse; the precise VF=FV=p identity was located and opened in Chai–Oort§10.24 p531, following the Frobenius coordinate description§10.23.')
q(3,'Websearch2; Numdam/IHES discovery','site.numdam.org Cartier 1957 dérivations corps characteristic p connexion','C-SA04-700;C-SA04-701',katz,'Results included Cartier1957 and later derivation expositions. Exact QC connection-category theorem was checked directly in Katz1970 Thm5.1; no uninspected Cartier theorem is credited for the full equivalence.')
q(4,'Websearch2; author primary PDF','site.math.princeton.edu Katz nilpotent connections monodromy theorem 5.1 Cartier','C-SA04-700;C-SA04-701;C-SA04-704;C-SA04-705;C-SA04-706',katz,'Opened exact Theorem5.1 pp190–191, Proposition5.2 pp191–192, and Theorem5.9 pp195–196. QC descent, p-linearity and inverse-image stability checked with hypotheses.')
q(5,'Websearch2','smooth geometrically connected fibers characteristic zero horizontal sections pullback fully faithful coherent modules connection','C-SA04-709',dos+';'+lara,'No exact arbitrary-base quasi-coherent horizontal full-faithfulness theorem found. Point-base and relative-proper neighboring references remain limited comparisons. Search-only generic notes are not used as authority.')
q(6,'Websearch2','relative stratified sheaves horizontal constants fully faithful pullback smooth morphism','C-SA04-698;C-SA04-709',dos+';'+lara,'Related relative stratification and homotopy results found; exact source quantifiers not matched. The field-case proof is supplied independently, not inflated to an arbitrary-base result.')
q(7,'Websearch1 verification','"stratified" "relative" "étale" "coherent" fundamental group representation equivalence','C-SA04-698',dos+';'+lara,'Verification search returned Gieseker/Esnault–Sun and relative stratification leads, which do not establish the source’s arbitrary Π/coherent fiberwise criterion. Opened primary comparison remains dos Santos13 and Lara3.1.')
q(8,'Websearch1 verification','"Verschiebung" "universal extension" affine','C-SA04-707;C-SA04-708',chai+';'+fm,'Found elliptic integral-structure and universal-extension leads; no opened exact universal Vkilled-affine formulation. Chai–Oort and Fonseca–Matthes supply components. Independent naturality/pushout proof is recorded with a perfect-field commutative category.')
q(9,'Websearch1 verification','"stratified line bundles" "torsion" "unibranch"','C-SA04-699;C-SA04-703',dos+';'+stacks,'Exact full singular/arbitrary-field statement not identified. Finite locally constant sheaf theorem0GIY and regular point-base finite-monodromy comparison were opened. Kummer sufficiency and horizontal-unit consequence proved directly.')
q(10,'Websearch1 verification','"connection" "fully faithful" "geometrically connected" characteristic zero pullback','C-SA04-709',dos+';'+lara,'Results include Gauss–Manin/Tannaka and projective-bundle comparisons, not the exact broad statement. No claim of novelty or falsity from this negative search.')
q(11,'Websearch2 targeted fate','"Verschiebung" "reductions" "section" "torsion"','C-SA04-702',milne+';'+chai,'No exact published version of the manuscript criterion found. Its literal assertion is independently refuted; the opened references supply Hasse, torsion specialization, and VF=p, not a publication claim for the counterexample.')
q(12,'Websearch2 targeted fate','"étale trivial" "stratified" "line" "units"','C-SA04-703',dos+';'+stacks,'No distinct primary provenance for this elementary unit consequence located. Its proof is supplied from the preceding Kummer criterion; no modern novelty is asserted.')
q(13,'Websearch2 targeted fate','"p-curvature" "tensor" "Frobenius" Katz 5.2','C-SA04-705;C-SA04-706',katz,'Later primary leads cite Katz5.2 and show Frobenius-valued p-curvature. Audit relies on the directly opened Katz statement and its independent tensor and nilpotent-base counterexamples, not search snippets.')
with(out/'root_supplement_search_log.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['query_id','date','sources_searched','query','claims','opened_urls','result']);w.writerows(rows)

# Schema and referential checks, not scholarly classifications.
claims=json.loads((out/'root_supplement_claims.json').read_text())
items=json.loads((out/'root_supplement_items.json').read_text())
problems=json.loads((out/'root_supplement_problems.json').read_text())
known_items={x['id'] for x in items}|{'SA04-627','SA04-628','SA04-631'}
keys=set(re.findall(r'@\w+\{([^,]+),',(out/'root_supplement_references.bib').read_text()))
status={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'}
event_types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted'}
for c in claims:
    assert set(c['items'])<=known_items,(c['id'],c['items'])
    assert set(c['refs'])<=keys,(c['id'],c['refs'])
    assert c['status_on_pages'] in status,(c['id'],c['status_on_pages'])
    assert c['confidence'] in {'high','medium','low'}
    assert c['class'] in set('ABCDEF')
for p in problems:
    assert set(p['refs'])<=keys
    assert all(o['item'] in known_items for o in p['occurrences'])
with(out/'root_supplement_events.tsv').open() as f:
    events=list(csv.DictReader(f,delimiter='\t'))
assert all(e['type'] in event_types for e in events)
assert any(e['statement_id']=='C-SA04-644' and e['type']=='refuted' and 'C-SA04-702' in e['outcome'] for e in events)
covered=set()
for r in rows:covered.update(r[4].split(';'))
assert {c['id'] for c in claims}<=covered
result={'schema_and_refs':'pass','claims':len(claims),'items':len(items),'problems':len(problems),'references':len(keys),'searches':len(rows),'events':len(events),'all_supplement_claims_have_search_mapping':True,'verdicts':'No automated verdicts; checks only validate schema/links.'}
Path('/workspace/scratch/594d1dc856a9/SA04_work/outputs/b_supplement_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

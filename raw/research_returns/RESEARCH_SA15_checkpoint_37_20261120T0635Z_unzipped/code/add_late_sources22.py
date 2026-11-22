"""Record actual late primary-source reads; no theorem imported into frozen PDF."""
from pathlib import Path
import datetime,json
w=Path(__file__).resolve().parents[1]
p=w/'notes/late_source_census.json';rows=json.loads(p.read_text())
new=[
 {'key':'KnutsenLelliChiesa2022LateLead','author':'Knutsen, A. L., and Lelli-Chiesa, M.','year':'2022','title':'Genus two curves on abelian surfaces. Annales Scientifiques de l Ecole Normale Superieure,55(4),905-918. DOI:10.24033/asens.2508','access':'Original institutional PDF opened; introduction and selected exact statements read','locators_and_limits':'The12-page IRIS original was opened. Introduction through Theorems1.1,1.2,1.4 and Section2.1 opening actually read. The scope is general complex abelian surfaces and general genus-two curves, not every fixed nonordinary characteristic-two surface. No theorem is imported. A later request for Section2.2 returned403; the Bergen URL redirected to a JavaScript wall. Publisher metadata verified on SMF. Full theorem proofs not yet read.','url':'https://iris.uniroma3.it/retrieve/a11f0575-02ba-48f4-8cf8-3f7f31d2c42b/knutsen-lelli-chiesa%20genus_two_curves_new_version.pdf'},
 {'key':'DolgachevLehavi2008LateLead','author':'Dolgachev, I., and Lehavi, D.','year':'2008','title':'On isogenous principally polarized abelian surfaces. Original arXiv0710.1298v3,8March2008.','access':'Original arXiv PDF opened; selected statements and proof passages read','locators_and_limits':'Introduction explicitly excludes characteristic two. Proposition2.1 and Corollary2.2 statements, Proposition2.4 with its complete printed proof, and Proposition3.1 with its complete printed proof were read. The latter counts difference pairs; it is not imported as a proof that triple coincidences are absent in the present characteristic-two problem. No theorem from this paper is used in the frozen PDF. The original Michigan URL failed after redirect; arXiv original succeeded. No final journal metadata is asserted here.','url':'https://arxiv.org/pdf/0710.1298'}]
keys={r['key'] for r in rows}
for r in new:
    if r['key'] not in keys:rows.append(r)
p.write_text(json.dumps(rows,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/ROOT_SEARCH_LOG_22.md').open('a') as f:
    f.write('\n## '+now+': late theta-norm singularity search\n\nSearch queries were "genus 2 (3,3) isogeny image theta divisor triple points nodes isotropic" and "genus two three points 3 torsion Weil pairing isotropic theta divisor", followed by an independent-engine exact-title search for Knutsen--Lelli-Chiesa. The two original reads and exact limits are recorded in the late source census. Neither resolves fixed characteristic-two theta-norm triple points. In particular a generic complex nodality theorem is not substituted for that missing uniform assertion. The frozen checkpoint22 PDF uses neither source.\n')
(w/'outputs/late_sources22.json').write_text(json.dumps({'actual_utc':now,'keys':[r['key'] for r in new],'status':'Actual lead reads recorded; no theorem promotion'},indent=2)+'\n')
print(json.dumps({'actual_utc':now,'late_source_rows':len(rows),'new_keys':[r['key'] for r in new]},indent=2))

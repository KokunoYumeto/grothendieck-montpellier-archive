"""Preserve bounded catalogue/literature search scope and the newly identified branch-sign gate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,time

R=Path(__file__).resolve().parents[1];start=time.perf_counter();now=datetime.now(timezone.utc)
outpath=R/'code/root_search_scope_followup07_output.json'
assert not outpath.exists()
cache=R.parent/'source_reading/recorded_web_search'
cache.mkdir(parents=True,exist_ok=True)
reductions=[]
for name in ['root_toric_literature_search.json','root_toric_literature_verify.json']:
 p=R/'code'/name;raw=p.read_bytes();d=json.loads(raw)
 if 'result' not in d:continue
 cp=cache/name;assert not cp.exists();cp.write_bytes(raw)
 content=d['result'].get('content',[])
 text='\n'.join(x.get('text','') for x in content if x.get('type')=='text')
 chunks=re.split(r'\n-{5,}\n',text)
 sources=[dict(heading=x.split('\n')[0],refs=re.findall(r'【([^】]+)】',x)) for x in chunks if x.strip()]
 reduced={k:v for k,v in d.items() if k!='result'}
 reduced.update(results=sources,raw_cache_sha256=hashlib.sha256(raw).hexdigest(),
  scope='Search-query record with factual result headings/URLs/refs only. Long third-party search extracts are omitted from the deliverable; the raw response is held in the reproducible source cache, not treated as an original theorem reading.',
  outcome='No exact prior global unequal-toric fiber statement was identified. The preliminary search had weak coverage and was followed by the second engine. No priority or exhaustive absence claim.')
 p.write_text(json.dumps(reduced,indent=2)+'\n')
 reductions.append(dict(file=str(p.relative_to(R)),raw_bytes=len(raw),cache_sha256=reduced['raw_cache_sha256'],source_records=len(sources)))
initial=dict(queries=['"Fujiwara" "tubular" site:mpim-bonn.mpg.de','"Pfluger" "Verheftung" "National Digital"','"Journal of the Indian Mathematical Society" "1960" "ndl.iitkgp"','"Pfluger" "401-412" pdf'],
 engine='system1',ref_group='turn545576826search',query_count=4,measured_seconds=None,
 time_limitation='This earlier tool call did not preserve an elapsed-time measurement; none is inferred.',
 outcome='Results supplied the MPIM public repository, NDLI and a Google Books1961 catalogue record. Modern unrelated Fujiwara results did not supply the1995 article. These routes were subsequently opened through advertised links; no theorem text was obtained.')
(R/'code/root_initial_catalogue_queries_1545.json').write_text(json.dumps(initial,indent=2)+'\n')
forms=json.loads((R/'code/root_public_catalogue_forms_output.json').read_text())
search=json.loads((R/'code/root_mpim_ndli_search_output.json').read_text())
note='''# Public catalogue and toric-literature follow-up

## Missing originals: bounded new routes

The four discovery queries are retained in `code/root_initial_catalogue_queries_1545.json`. They produced public repository/catalogue entry points, not a missing original. The web opens and observed advertised forms are documented in `root_public_catalogues_open_web.json` and `root_public_catalogues_forms_web.json`.

The first Python form-fetch prototype failed at importing `requests`, before any network request. Its actual body and traceback are preserved as `root_public_catalogue_forms_failed01.py` and its output. No duration was measured for that failure. The working standard-library version made exactly three GET requests: MPIM's advanced form and NDLI's public home page were200; Google Books' normal1961-record request redirected to a429 challenge page and was stopped. Batch wall time was13.532168659 seconds. No challenge was bypassed.

Only observed form actions were used. MPIM's basic GET search for Fujiwara returned nine results, all nine actually read: modern Druţu–Mackay, two final reports, Pimenov, Gordeev, Gromadzki, Dranishnikov, Grunewald and Bell–Fujiwara2005 curve-graph material. None was the1992 preprint or1995 tubular-neighborhood article; no content PDF was fetched from those unrelated results. NDLI's live advertised `/search?key=Verheftung` endpoint returned404, not an empty search result. Batch time was12.189128438 seconds; individual MPIM12.187971946 seconds, NDLI8.259522739 seconds.

The Part A delayed Fatcat check made exactly two DOI lookups, Fujiwara and Lieberman, both503 upstream timeouts (11.899788230 and11.898996335 seconds; batch11.901000857 seconds). This supplied no records or files, and was stopped without retries. Part C's IISc audit separately records the public catalogue/repository failures; it is not an absence result. None of these attempts closes Pfluger1960, Lieberman1968 or Fujiwara1995.

## Unequal-toric and raw-descent literature scope

Three preliminary queries (`root_toric_literature_search.json`,0.463 seconds) were followed by two verifying queries (`root_toric_literature_verify.json`,0.957 seconds). They did not identify the exact global fiber theorem. Search headings and references are retained, without republishing long unrelated third-party extracts. The proof depends only on the previously opened capping, convex-variation and welding inputs. No priority is claimed.

A further three queries on hyperbolic capping/isotopy and conformal welding of pants are preserved in `root_toric_descent_search.json` with the measured tool time. They returned general welding and quantum/random-surface results, plus an asymptotic-Teichmüller reduction article, but no statement establishing the raw cap-size invariance under examination. Search results alone were not treated as opened proof sources.

## Audit status change

The new A6 audit identified a separate literal parenthesis in049(b): automatic cyclotomic action at a node requires checking branch interchange. This is recorded as a live proof gate pending the explicit corrected character and counterexample. It is separate from the previously proved graph-recovery and framed-logarithmic statements. The B3 complete37-row scope audit found no new mathematical gap; the phrase “finite R-modules” in Raynaud's theorem was clarified to “R-modules finite as sets”, matching the source's explicit convention.
'''
(R/'notes/root_public_catalogue_followup07.md').write_text(note)
gaps=json.loads((R/'notes/live_mathematical_scope_gaps.json').read_text())
assert not any(x['id']=='A6-nonsplit-node-character' for x in gaps)
gaps.append(dict(id='A6-nonsplit-node-character',opened_utc=now.isoformat(),status='open: exact local Kummer sign and example under proof check',
 claim='The node inertia action in049(b) is automatically cyclotomic without a split-branch condition.',
 issue='Branch interchange can invert the oriented node-inertia generator.',
 gate='Prove the corrected cyclotomic character times branch sign and verify an explicit nonsplit nodal curve with invariant nonzero framing.',
 affects=['A.6(a),049(b)','L6 scope']))
(R/'notes/live_mathematical_scope_gaps.json').write_text(json.dumps(gaps,indent=2)+'\n')
with (R/'PROGRESS_LEDGER.md').open('a') as f:
 f.write(f'\n\n## Additional literal049(b) scope gate — {now.isoformat()}\n\nA6-nonsplit-node-character is open pending its local proof and explicit certificate. The original automatically-cyclotomic parenthesis must distinguish branch-preserving action from branch interchange. This discovery does not itself count as a closure or a strictly smaller gate. The companion B3 complete scope audit found no further mathematical gap and only clarified the original finite-as-sets convention.\n')
out=dict(recorded_utc=now.isoformat(),source_requests=5,discovery_queries=4,literature_queries=8,
 source_scope_files=['code/root_public_catalogue_forms_output.json','code/root_mpim_ndli_search_output.json'],
 reductions=reductions,seconds=time.perf_counter()-start,
 scope='Record consolidation only; no new network request, mathematical calculation or historical timing reconstruction.')
outpath.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

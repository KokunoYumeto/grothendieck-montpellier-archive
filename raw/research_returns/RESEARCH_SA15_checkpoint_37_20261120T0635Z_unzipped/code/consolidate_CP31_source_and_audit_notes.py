"""Consolidate one duplicate source row and record completed CP31 proof audits."""
from pathlib import Path
import datetime,difflib,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
folder=w/'notes/CP31_source_census_consolidation';assert not folder.exists()
source=w/'notes/late_source_census.json'
rows=json.loads(source.read_text())
matches=[r for r in rows if r['key']=='Pareschi2021ThetaTorsionLead']
assert len(matches)==1
bib=(w/'notes/root_references.bib').read_text()
assert '@misc{Pareschi2021ThetaTorsion,' in bib
assert '2007.12252' in bib and 'genus-two proof of Theorem C' in bib
folder.mkdir();shutil.copy2(source,folder/source.name)
before=source.read_text()
rows=[r for r in rows if r['key']!='Pareschi2021ThetaTorsionLead']
source.write_text(json.dumps(rows,indent=2)+'\n')
(folder/'late_source_census.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),source.read_text().splitlines(True),fromfile='before',tofile='after')))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,
 'removed_duplicate_key':'Pareschi2021ThetaTorsionLead','retained_canonical_key':'Pareschi2021ThetaTorsion',
 'removed_row_preserved':matches[0],
 'reason':'The same original preprint is now cited by the canonical auxiliary theta-torsion subsection. Its complete actual reading scope and characteristic-zero limitation are preserved in the canonical bibliography entry; the earlier lead row would duplicate it. No source reading or limitation is discarded.',
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'after_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(w/'outputs/CP31_source_census_consolidation.json').write_text(json.dumps(record,indent=2)+'\n')
with(w/'notes/checkpoint31_changes.md').open('a')as f:
 f.write('''\n## Completed proof audits and source consolidation\n\nThe principal theta bridge has full root, monodromy-companion and reduction-agent proof/source audits. The exact Moore classification has full root, monodromy and reduction-agent audits, including unchanged isolated reruns in 3.244205315990257, 3.249439478997374 and 3.3375787070108345 seconds respectively, all mathematical outputs identical. It classifies the geometric zero set only; no scheme-structure claim is made.\n\nThe seven-label twisted cubic Cartier/Moore theorem has complete root and obstruction-agent proof/source audits, recorded at 01:37:50.135808 and 01:35:24.622429 UTC. Its actual coefficient vector is the coordinatewise square of the cubic theta embedding, shifted by a fixed geometric two-torsion point. This proves invertible cross blocks for every non-two-torsion twist and maximal dual alternating rank in all fixed odd principal-cube degrees. No new numerical program is claimed for these geometric audits; the exact universal Moore certificate is a separately audited input.\n\nB87 has complete root and obstruction-agent proof/code audits, with unchanged isolated reruns in 0.037566576997051015 and 0.034868966991780326 seconds. The same actual diagonal quotient of two degree-25 point fields excludes a three-dimensional first layer. At p=5 the residual-tame sector therefore requires the full wild congruence kernel of order5^8, with mu25 absent from the base. This is a necessary condition only; other residual sectors remain open.\n\nThe source-census-only key Pareschi2021ThetaTorsionLead was removed as a duplicate of the now cited canonical entry Pareschi2021ThetaTorsion. Its exact old row, prior file and diff are retained in notes/CP31_source_census_consolidation and outputs/CP31_source_census_consolidation.json. The complete source-reading scope, the complex-field limitation and the unexamined external dependencies remain in the canonical entry. No source was silently dropped.\n\nEleven already completed root audit events were copied unchanged from the generated register to its durable root input before rebuilding the register. Their actual dates and event types were preserved; no audit or mathematical computation was rerun for that administrative step. The record is outputs/CP31_root_audit_event_persistence.json.\n''')
with(w/'notes/ROOT_SEARCH_LOG_31.md').open('a')as f:
 f.write('\n## Source-census identity consolidation\n\n'+now+': the duplicate Pareschi lead row was consolidated into its canonical cited entry; exact prior row and file retained. No new source reading is claimed by this administrative change.\n')
print(json.dumps({k:v for k,v in record.items() if k!='removed_row_preserved'},indent=2))

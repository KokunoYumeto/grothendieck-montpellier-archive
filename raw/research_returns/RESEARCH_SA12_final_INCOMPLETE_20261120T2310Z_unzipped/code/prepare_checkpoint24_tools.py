"""Prepare review16 and checkpoint24 tooling, without running either early."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]

p = root / 'code/render_checkpoint.py'
s = p.read_text()
marker = 'if number==5: pages.update(range(18,24));'
addition = """if number==24:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,365,385,405,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\\\newlabel\\{([^}]+)\\}\\{\\{[^}]*\\}\\{(\\d+)\\}',aux)}
    first=label_pages['D:different-Frobenius-invariant-lattice']
    pages.update(range(max(1,first-1),len(doc)+1))
"""
assert 'if number==24:' not in s and marker in s
p.write_text(s.replace(marker, addition + marker, 1))

s = (root / 'code/verify_checkpoint23.py').read_text()
s = s.replace('CP23', 'CP24').replace('checkpoint23', 'checkpoint24').replace('Checkpoint23', 'Checkpoint24').replace('CHECKPOINT23', 'CHECKPOINT24')
s = s.replace('build_pass147', 'build_pass152')
s = s.replace('RESEARCH_SA12_checkpoint_22.zip', 'RESEARCH_SA12_checkpoint_23.zip')
s = s.replace('2026-11-20T17:25:00+00:00', '2026-11-20T18:10:00+00:00').replace('17:25UTC', '18:10UTC')
start = s.index("scope='''# Checkpoint24 scope")
end = s.index("\n(root/'CHECKPOINT24_SCOPE.md')", start)
scope_code = """scope='''# Checkpoint24 scope

INCOMPLETE. Scheduled creation:20 November2026,18:10UTC, after formal review16 at the same scheduled time. This full archive contains all current deliverables and accumulated documentation, excluding original supplied attachments and earlier ZIPs.

The verified manuscript has {pages}pages, final {build}, SHA256 {sha}, {rows}statement rows and {events}actual central check events. Newly assembled units and exact hashes are recorded in code/output/integrate_post19_post23*.json. Research files not assembled retain their explicit individual status.

The global finite-puncture unrestricted-PGL theorem and its fixed-curve, dimensional, normalization and defining-characteristic simple-product consequences are proved. A separate restricted alternating factorial bound, with fixed finitely generated local quotient control, is proved in its exact stated scope. Further developments are described in the report and the exact formal-review assessment. General D.1, general D.2(ii), and residual L8 remain open. Only a completed requested-row change or a strictly smaller strongest main gate can reset the stopping counter; prerequisites, closures, searches, audits and packaging are not counted independently.

Formal review16 is executed before this checkpoint is created. Its completed record, comparison with review15 and stopping counter are in code/output/formal_review16.json; review15 was the latest completed review when this PDF verification was staged. The next scheduled checkpoint after this one is18:55UTC.

The final PDF has zero warnings, missing characters and undefined citations/references. Overfull boxes before/after:{before}/{after}; maximum final overflow:{overflow}pt, within the2pt limit. Actual image inspection is recorded in qa/checkpoint24_actual_inspection.json and qa/pdf_verified_checkpoint24.json. New inspection images use lossless WebP with exact RGB round-trip checks. Historical contact sheets and individual pages retain every decoded pixel; old/current paths and hashes are in qa/historical_contact_encoding_map.json and qa/historical_page_encoding_map.json. Earlier immutable archives retain their original bytes. Only the exact certified PDF hash is delivered.
'''.format(pages=render['pdf_pages'],build=build,sha=sha,rows=nrows,events=nevents,before=len(initial_overfull),after=len(overfull),overflow=max(overfull,default=0))"""
s = s[:start] + scope_code + s[end:]
(root / 'code/verify_checkpoint24.py').write_text(s)

s = (root / 'code/formal_review15.py').read_text()
s = s.replace('formal_review15', 'formal_review16').replace('formal_review14', 'formal_review15')
s = s.replace('review15_main_assessment', 'review16_main_assessment')
s = s.replace('Formal review15', 'Formal review16').replace('Formal review14', 'Formal review15')
s = s.replace('Review15', 'Review16').replace('review15', 'review16')
s = s.replace('2026,11,20,17,10', '2026,11,20,18,10')
s = s.replace('2026-11-20T18:10:00+00:00', '2026-11-20T19:10:00+00:00')
s = s.replace('2026-11-20T17:25:00+00:00', '2026-11-20T18:55:00+00:00')
s = s.replace('17:10UTC', '18:10UTC').replace('checkpoint22_saved_receipt', 'checkpoint23_saved_receipt')
s = s.replace("'review_number':15", "'review_number':16").replace("'review':15", "'review':16")
s = s.replace("'latest_successful_checkpoint':22", "'latest_successful_checkpoint':23")
s = s.replace("'scheduled_checkpoint_now':None", "'scheduled_checkpoint_now':24")
s = s.replace('Checkpoint22 is the most recent saved archive at review time; the next scheduled checkpoint is17:25UTC.', 'Checkpoint23 is the most recent saved archive at review time; scheduled checkpoint24 follows this review at18:10UTC.')
# Preserve the actual previous-review filename and the report line being replaced.
s = s.replace("prior=json.loads((root/'code/output/formal_review16.json').read_text())", "prior=json.loads((root/'code/output/formal_review15.json').read_text())")
s = s.replace('if line.startswith("\'Formal review16 was completed"):', 'if line.startswith("\'Formal review15 was completed"):')
assert "prior=json.loads((root/'code/output/formal_review15.json')" in s
assert "code/output/review16_main_assessment.json" in s
assert '2026,11,20,18,10' in s and "'scheduled_checkpoint_now':24" in s
(root / 'code/formal_review16.py').write_text(s)
print('Prepared checkpoint24 render/verification and review16 logic; no review or archive performed.')

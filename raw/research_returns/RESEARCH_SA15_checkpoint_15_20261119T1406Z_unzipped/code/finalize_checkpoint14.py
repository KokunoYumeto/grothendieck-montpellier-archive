"""Record actual CP14 page inspection and finalize its report/registers."""
from pathlib import Path
import csv, datetime, json, subprocess, sys
w = Path(__file__).resolve().parents[1]
dest = w / 'outputs/visual_qa_checkpoint14.json'
assert not dest.exists()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
groups = {
    'root': [1,14,24,28,39,55,70,85,350],
    'obstructions_crystals': [167,168,169,170,171,172,173,191],
    'monodromy': [192,193,194,195,196,209,267,268],
    'reduction_descent': [269,270,271,272,273,274,275,276,277,278,279,283]}
pending = json.loads((w / 'outputs/visual_qa_pending.json').read_text())
assert sorted(sum(groups.values(), [])) == pending['pages_rendered']
build = json.loads((w / 'outputs/build_summary.json').read_text())
assert build['over_2pt'] == 0 and not build['undefined_references'] and not build['undefined_citations']
identity = json.loads((w / 'outputs/statement_identity_checkpoint14.json').read_text())
qa = {'checkpoint':14, 'actual_observed_utc':now, 'status':'PASS', 'pdf_pages':350,
      'pdf_bytes':build['pdf_bytes'], 'build_seconds':build['seconds'],
      'actually_viewed_pages_by_reviewer':groups, 'total_distinct_pages':37,
      'initial_overfull_boxes':len(build['overfull_boxes']),
      'final_overfull_boxes':len(build['overfull_boxes']),
      'max_overfull_points':max((b['points'] for b in build['overfull_boxes']), default=0),
      'over_2pt_before':0, 'over_2pt_after':0,
      'criteria':'All10 montages actually viewed. Complete new A3/A4/B subsections plus earlier samples and final bibliography inspected. Root viewed montages1,2,10; each delegated reviewer returned explicit actual-page confirmation. One0.41342pt line is below the required2pt threshold and visually harmless.',
      'build_attempts':1, 'undefined_references':False, 'undefined_citations':False}
dest.write_text(json.dumps(qa, indent=2) + '\n')
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    csv.writer(f, delimiter='\t').writerow([
        'CP14-VISUAL-QA', now,
        'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
        'artifact verification',
        'PASS:350-page PDF2592825bytes; single successful build34.179s. One0.41342pt overfull line, zero above2pt, no undefined references/citations. All37 selected pages actually viewed, including every new subsection and the overflow page; no clipping, overlap, glyph or margin defect.'])
with (w / 'notes/checkpoint14_changes.md').open('a') as f:
    f.write('''
## Final checkpoint verification

The complete paper has350 pages and2,592,825 bytes. Its single build took34.179 seconds. There is one0.41342pt overfull line, below the required2pt threshold; the before/after counts above2pt are both zero. No undefined references or citations remain. All37 selected pages were actually viewed, including every new subsection, the reported overfull page, earlier samples and the last bibliography page. Root viewed9 pages, obstruction/crystal8, monodromy8 and reduction/descent12. Every reviewer reported clean displays, glyphs, paths, margins and pagination.

There are395 numbered statements, a net addition of22. The27 identifiers absent from checkpoint13 consist of those22 additions and5 existing scope remarks whose content-derived labels changed after proved forward references were added. Every new identifier has an explicit check event. The exact old/current passage pairs and reasons are retained in outputs/statement_identity_checkpoint14.json. An overly restrictive similarity guard in the first bookkeeping utility rejected one correctly matched updated remark; the utility and failure output are retained, and all five mappings were manually checked before using exact title/injectivity checks. This was a bookkeeping correction, not a mathematical failure.

The current bibliography has140 entries; the source census has141 rows including the unused Hua witness. No manuscript scans have become available, and no priority claim is made. The final regenerated registers provide the exact check-event and exported-program counts.

The uniform-collision candidate file was renamed to its promoted canonical file after three full independent audits. Its initial executed certificate version and output are retained under the agent's code/history and outputs, with the reason for the stronger branch-substitution replacement. B42's failed structural-equality certificate is likewise retained. No executed mathematical program is discarded merely because its check failed or was superseded.

New tangent-triple source-smoothness work and a proposed characteristic-two8-torsion ambiguity were developed after the paper freeze. They are separate candidates outside this inspected paper and its current result table. The next actual review is due13:50:40UTC; checkpoint15 is due14:05:40UTC. The present checkpoint is not an additional progress review.

### Existing scope remarks superseded by proved forward references

| Earlier identifier | Current identifier | Reason |
|---|---|---|
''')
    for pair in identity['remark_identity_map']:
        f.write(f"| {pair['old_id']} | {pair['current_id']} | {pair['reason']} |\n")
for name in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current14.py']:
    subprocess.run([sys.executable, str(w / 'code' / name)], check=True, cwd=w)
with (w / 'RESEARCH_SA15_report.md').open('a') as f:
    f.write('\n' + (w / 'notes/SOURCE_CENSUS.md').read_text() + '\n')
assert (w / 'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa, indent=2))

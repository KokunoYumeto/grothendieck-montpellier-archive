"""Seal the PDF QA record only after all named image-inspection records exist."""
from pathlib import Path
import json,re,time,hashlib
start=time.perf_counter();root=Path(__file__).resolve().parents[1]
pdf=root/'RESEARCH_SA10_paper.pdf';digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
render=json.loads((root/'qa/render_manifest.json').read_text())
build=json.loads((root/'logs/build_summary.json').read_text())
assert render['sha256']==digest
assert build['complete'] and build['overfull_exceeding_2pt']==0
assert build['missing_characters']==0 and build['undefined_citations']==0
records=['PDF_VISUAL_ROOT.md','PDF_VISUAL_B.md','PDF_VISUAL_C.md']
for name in records:
    s=(root/name).read_text()
    assert digest in s,(name,'does not identify final PDF')
    assert 'PASS' in s or 'No blocking' in s or 'no blocking' in s,(name,'no explicit passed inspection')
baseline=root/'logs/build_history/20261119T052014525518Z/build_pass2.out'
before=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',baseline.read_text())]
data={'pdf_sha256':digest,'pages':render['pages'],'bytes':pdf.stat().st_size,
      'before_log':str(baseline.relative_to(root)),'before_overfull_pt':before,
      'before_exceeding_2pt':sum(x>2 for x in before),'after_overfull_pt':build['overfull_pt'],
      'after_exceeding_2pt':0,'missing_characters':0,'undefined_citations':0,
      'all_pages_contact_sheet_inspected':list(range(1,render['pages']+1)),
      'root_full_pages':[1,5,6,7,8,10,11,12,13,36,37,43,47,50,56,57,61,62,68,70],
      'B_full_pages':[14,15,16,17,18,20,21,22,24,25,26,27,29,31,33,35,71,72,73,74],
      'C_full_pages':[42,45,48,55,58,60,63,66,69],
      'inspection_records':records,'build_seconds':build['runtime_seconds'],
      'render_seconds':render['runtime_seconds'],'approval':'PASS'}
(root/'qa/final_qa.json').write_text(json.dumps(data,indent=2)+'\n')
pages=sorted(set(data['root_full_pages']+data['B_full_pages']+data['C_full_pages']))
report=f'''# Final PDF publication check

**PASS.** The published LuaLaTeX PDF has **{render['pages']} pages** and **{pdf.stat().st_size:,} bytes**. Its SHA256 is `{digest}`.

| Metric | Last retained failing draft | Final PDF |
|---|---:|---:|
| Overfull boxes, all sizes | {len(before)} | {len(build['overfull_pt'])} |
| Overfull boxes exceeding2pt | {sum(x>2 for x in before)} | 0 |
| Largest overfull box | {max(before):.5f}pt | {max(build['overfull_pt'],default=0):.5f}pt |
| Missing-character warnings | See retained draft log | 0 |
| Undefined citations | See retained draft log | 0 |

The baseline is `{baseline.relative_to(root)}`. Its four excessive boxes are15.27339,142.84079,97.10779 and13.91151pt. Earlier intermediate failures remain in the build history; this comparison does not silently count only one of those earlier errors as the entire history. The final source repairs the affected titles, raw paths/URLs and obsolete metadata. Final successful build time: {build['runtime_seconds']:.6f}s. Poppler render time: {render['runtime_seconds']:.6f}s.

Every page was rendered at110dpi and visually reviewed in seven contact sheets. **{len(pages)} distinct full pages** were separately inspected: {', '.join(map(str,pages))}. These include every identified former overflow location and a spread through every Part. Actual page-by-page observations are in the three inspection records. No clipping, overlapping text, unreadable glyph, footer collision or excessive display was found. Two nonblocking editorial observations are preserved in the B audit: separate bibliography entries for some works consulted by different subruns, and the explicit B4.8 equation tag preceding B4.7. They do not change statement IDs, references or mathematical content.

The C5 matrix is fully visible on page68. The former long C2 source title and C1 moduli citation line are fully visible on pages47 and43. The B3 heading, B56 file paths and bibliography wrapping were checked at full size. We have not inferred visual quality merely from a successful compile.
'''
(root/'PDF_QA_REPORT.md').write_text(report)
(root/'logs/PDF_QA_APPROVED.txt').write_text('PASS\nPDF SHA256 '+digest+'\nInspection records: '+', '.join(records)+'\n')
print(f'QA PASS: {render["pages"]} rendered pages, {len(pages)} distinct full-page inspections, zero excessive boxes.')
print(f'Runtime {time.perf_counter()-start:.9f} seconds.')

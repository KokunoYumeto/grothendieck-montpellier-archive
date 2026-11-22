from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
own=Path(__file__).resolve().parents[1];work=own.parents[1]
pdf=work/'RESEARCH_SA15_paper.pdf'
expected='dcf4fdae25ae05e1b6c55ff69f60b0a54f0a3dafbc402d2e33e0a37717b977bd'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
pages=[587,588,589,590]
observations={
 587:'Actually opened the full individual PNG. B81 corollary/provenance and B82 opening fit; long code path wraps within the text width. B-RD82.1 and82.2 are legible with unobstructed tags; lemma statement ends cleanly at foot of text.',
 588:'Actually opened the full individual PNG. B82 Newton proof and terminal-plane lemma are legible; V2 definition and B-RD82.3 fit; proof continuation at the lower margin is natural, with no clipped glyphs or overlap.',
 589:'Actually opened the full individual PNG. B-RD82.5 through82.8 and their inequality signs/exponents are clear; theorem follows without collision; continuing proof at bottom remains inside margins.',
 590:'Actually opened the full individual PNG. B-RD82.9, direct determinant proof and exact-audit provenance fit. The code path breaks across lines but is legible; B83 heading, hypotheses and first lemma/proof are clear. Normal proof continuation at bottom; no premature blank block.'}
now=datetime.now(timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'pdf_sha256':expected,'pdf_pages':672,'pages':pages,
        'method':'Each of the four full PNGs was individually opened and emitted with view_image; no inference from build logs or unseen montage.',
        'scope':'Text/math legibility, clipping, overlap, equation tags, glyphs, margins and page continuations.',
        'observations':observations,'defects':[],
        'png_sha256':{p:hashlib.sha256((work/f'outputs/qa30/page_{p:03d}.png').read_bytes()).hexdigest() for p in pages}}
(own/'outputs/CP30_visual_QA.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for p in pages:
        f.write('\t'.join([now,f'CP30-page-{p}','ACTUAL_VISUAL_PASS',observations[p],
                          f'outputs/qa30/page_{p:03d}.png;agents/reduction_descent/outputs/CP30_visual_QA.json',expected])+'\n')
print(json.dumps(record,indent=2))

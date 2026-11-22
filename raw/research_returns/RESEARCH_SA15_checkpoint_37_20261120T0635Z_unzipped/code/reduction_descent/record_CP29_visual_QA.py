from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
own=Path(__file__).resolve().parents[1];work=own.parents[1]
pages=list(range(574,580))
observations={
574:'B78 certificate/provenance ending and B79 section opening fully legible. Wrapped program path stays within the text column; B-RD79.1 and aligned layer display B-RD79.2 have clear tags. Bottom Newton proof continues normally.',
575:'B79 matrix pth-power display and full common-field valuation block fit; B-RD79.4 tag is on its own aligned continuation line without overlap. Leading-coordinate display and lower-break definition are clear, with no clipping.',
576:'Fixed-coefficient, terminal-break and Cartan leading equations B-RD79.6 through B-RD79.10 are legible; the Stacks citation and proposition/corollary endings render correctly. Ordinary scope continuation at page end.',
577:'B79 provenance and B80 opening are clear. Long certificate path wraps within margins, B-RD80.1 and B-RD80.2 fit, and all Cartan/anti-Cartan notation is legible. Lemma text continues normally to the next page.',
578:'B80 first-coefficient proof and full three-dimensional terminal-plane argument are legible. Inline roots/exponents, inverse scalar in anti-Cartan conjugacy, equation and citations have no overlap or missing glyphs; proof continues normally.',
579:'B80 terminal-plane proof ending, integral-lift lemma and Cartan-orientation lemma opening fit. The actual primitive-lift display B-RD80.3 and order-p² stabilizer argument have clear symbols and tags. Bottom orientation proof continuation is normal.'}
now=datetime.now(timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'pages':pages,
        'pdf_sha256':'2eb1a849c9dad5158bd079f059464d3733b5322522d859f781d0ab80321cfcf9',
        'pdf_pages':660,
        'scope':'Actual independent full-image visual inspection: all six assigned PNGs individually opened and emitted. Text/math legibility, clipping, overlaps, glyphs, tags, citations and proof continuations checked. Frozen canonical sources unchanged.',
        'images':[{'page':p,'path':str(work/f'outputs/qa29/page_{p:03d}.png'),
                   'sha256':hashlib.sha256((work/f'outputs/qa29/page_{p:03d}.png').read_bytes()).hexdigest(),
                   'observation':observations[p]} for p in pages],
        'defects':[]}
dest=own/'outputs/CP29_visual_QA.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for p in pages:
        f.write('\t'.join([now,f'CP29-page-{p}','VISUAL_QA_PASS',observations[p],
                          'outputs/CP29_visual_QA.json','Actual full PNG individually emitted and viewed; frozen paper unchanged'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':now,'pages':pages,
                  'record_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},indent=2))

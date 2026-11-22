#!/usr/bin/env python3
"""Record the root's already-performed image inspection of build46."""
from pathlib import Path
import json, shutil
root=Path(__file__).resolve().parents[1]
qa=root.parent/'qa_checkpoint08_committed'
p=qa/'render_log.json';data=json.loads(p.read_text())
data['individual_pages']=[128,129,154,160,164,165,166]
data['visual_inspection']='Root viewed the35-page contact sheet and individual pages128,129,154,160,164,165,166 by20:38:32UTC. The previously repaired display on page129 and the new theorem pages are readable. No clipping, overlap or missing glyphs observed.'
p.write_text(json.dumps(data,indent=2)+'\n')
for n in [129,154,164]:
    shutil.copyfile(qa/f'page-{n:03}.png',root/'qa'/f'checkpoint08_page{n}.png')
print(json.dumps({'reviewed_contact_pages':35,'individual_pages':data['individual_pages'],'result':'PASS'}))

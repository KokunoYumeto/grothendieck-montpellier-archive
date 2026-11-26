# -*- coding: utf-8 -*-
"""Assemble TO_SEND/PRO/1_Archive_research_by_topic/98_VPVNP_HINGE/ for vpvnp_integration/PROMPT.md (24 Nov 2026).
Copies only; one download (OpenAI's references.tex) into its own new scratch folder first. Prints the manifest."""
import os, shutil, sys, zipfile, urllib.request, hashlib, json
sys.stdout.reconfigure(encoding='utf-8')
DST = '<local>/Documents/TO_SEND/PRO/1_Archive_research_by_topic/98_VPVNP_HINGE'
SP = '<local>/AppData/Local/Temp/claude/f2c80a22394db22f/329fb1e6-0570-47be-9060-a2a454bf3e15/scratchpad/'
RR = '<local>/Documents/grothendieck_archive_transcription_20261110/research_returns/'
URL = ('https://raw.githubusercontent.com/openai/math/main/preprints/'
       'VP-and-VNP-are-different-November-23-2026/build/references.tex')
DL_DIR = SP + 'download_oai_references_20261124/'
SRC = [
    ('PROMPT.md', '<local>/pequalnp_work/fleet_map/vpvnp_integration/PROMPT.md'),
    ('openai_vp_vnp_Paper.tex', SP + 'oai_vpvnp/Paper.tex'),
    ('openai_vp_vnp_references.tex', DL_DIR + 'references.tex'),
    ('anthropic_vp_vnp_paper.pdf', SP + 'anthropic_vpvnp/paper.pdf'),
    ('anthropic_vp_vnp_Statement.lean', SP + 'anthropic_vpvnp/Statement.lean'),
    ('GCT_GINEQ.tex', RR + 'GCT_GINEQ_final_20261120T2340Z_unzipped/GCT_GINEQ.tex'),
    ('border_rank.tex', 'ZIP:<local>/Downloads/BORDER_RANK_checkpoint_31.zip!border_rank.tex'),
    ('BR_PENCIL_substitution.tex', RR + 'BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped/sections/substitution.tex'),
    ('BR_PENCIL_pencils.tex', RR + 'BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped/sections/pencils.tex'),
    ('BR_PENCIL_permanent_apolar.tex', RR + 'BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped/sections/permanent_apolar.tex'),
    ('GCT_POS_KRONECKER_FINDINGS.tex', RR + 'GCT_POS_final_20261122T0219Z_unzipped/branches/kronecker/KRONECKER_FINDINGS.tex'),
    ('GCT_POS_AMPLIFYING_GADGET.tex', RR + 'GCT_POS_final_20261122T0219Z_unzipped/branches/kronecker/AMPLIFYING_GADGET.tex'),
    ('GCT_POS_AMPLIFIER_FULL_STABILIZERS.tex', RR + 'GCT_POS_final_20261122T0219Z_unzipped/branches/kronecker/AMPLIFIER_FULL_STABILIZERS.tex'),
    ('ALPOGE_GCT_bridges.tex', RR + 'ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped/work/bridges.tex'),
    ('VPVNP_INTEGRATION_20261124.md', '<local>/pequalnp_work/fleet_map/VPVNP_INTEGRATION_20261124.md'),
]
if os.path.exists(DST):
    raise SystemExit('exists: ' + DST)
os.makedirs(DL_DIR, exist_ok=True)
if not os.path.exists(DL_DIR + 'references.tex'):
    req = urllib.request.Request(URL, headers={'User-Agent': 'send-folder-builder/1.0'})
    data = urllib.request.urlopen(req, timeout=60).read()
    open(DL_DIR + 'references.tex', 'wb').write(data)
os.makedirs(DST)
man = []
for name, src in SRC:
    out = os.path.join(DST, name)
    if src.startswith('ZIP:'):
        zpath, member = src[4:].split('!')
        data = zipfile.ZipFile(zpath).read(member)
        open(out, 'wb').write(data)
    else:
        shutil.copyfile(src, out)
    b = open(out, 'rb').read()
    man.append(dict(name=name, bytes=len(b), sha256=hashlib.sha256(b).hexdigest()[:16], source=src.replace('ZIP:', '')))
bad = [m['name'] for m in man if 'SAT_WITNESS' in m['source'] or 'SAT_KRONECKER' in m['source'] or m['name'].endswith('.zip')]
print('excluded-name check:', bad or 'clean')
for m in man:
    print('%-42s %9d  %s  %s' % (m['name'], m['bytes'], m['sha256'], m['source']))
json.dump(man, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'send_folder_manifest_20261124.json'), 'w'), indent=1)

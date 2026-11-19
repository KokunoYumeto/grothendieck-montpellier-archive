"""Build the attachment ZIPs of RESEARCH_SA13 (agent a84c887cf408574ed, Claude Opus 5.5 at effort max, 19 Nov 2026).
Each ZIP has MANIFEST.tsv at its root: path, origin (relative to C:/Users/user/Documents), sha256."""
import hashlib, os, zipfile
DOC = r'C:\Users\user\Documents'
OUT = os.path.join(DOC, r'pro_prompt_builds\RESEARCH_SA13')
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(DOC, r'pro_prompt_builds\RESEARCH_SA13_work'), exist_ok=True)
S3 = r'results_register\horizontal\sweep3\SA13'
RET = r'grothendieck_archive_transcription_20261110\returns'
CW = r'grothendieck_archive_transcription_20261110\codex_web_20261113\returns'
SGA = r'sga7_readers_publish_20261112\sga-fr\volumes'

study = [(f'study/{n}', f'{S3}\\{n}') for n in ['STUDY.md', 'HUNCHES.md', 'RESEARCH_PACKAGES.md', 'CHECK_EVENTS.tsv',
                                               'CORRECTIONS.tsv', 'DEPENDS.tsv', 'DELIVERABLES.tsv']]
study += [(f'study/readings/{n}', f'{S3}\\readings\\{n}') for n in ['c34.md', 'c33_c36_c39.md', 'c32_c35_c37_c40.md', 'c27_c28_c41_c42.md']]
study += [('study/sweep2_OBJECTS.tsv', r'results_register\horizontal\sweep2\SA13\OBJECTS.tsv'),
          ('study/sweep2_SA13_scan_readings.md', r'results_register\horizontal\sweep2\REPORTS\SA13_scan_readings.md'),
          ('broad/SA12_sweep2_TOPIC_NOTES.md', r'results_register\horizontal\sweep2\SA12\TOPIC_NOTES.md'),
          ('broad/SA12_sweep2_OBJECTS.tsv', r'results_register\horizontal\sweep2\SA12\OBJECTS.tsv')]

trans = [('PREAMBLE.tex', r'results_register\horizontal\inputs\SA13\PREAMBLE.tex')]
for pkg in ['MPL_33_098-146', 'MPL_33_147-181+34_002-017', 'MPL_36_002-052', 'MPL_36_053-085+39']:
    for suf in ['_transcription.tex', '_notes.md', '_doubts.md']:
        trans.append((f'pro/{pkg}{suf}', f'{RET}\\{pkg}_unzipped\\{pkg}{suf}'))
for f in ['A36-01', 'A36-02', 'K27-01', 'K27-02', 'K27-03', 'K28-01', 'K32-02', 'K32-03', 'K40-02', 'K41-01', 'K42-01']:
    for suf in ['_transcription.tex', '_notes.md', '_mathnotes.md']:
        trans.append((f'codex/{f}{suf}', f'{CW}\\{f}\\out\\{f}{suf}'))

lit = [('SGA5_fr/s5.tex', f'{SGA}\\sga5\\current\\s5.tex')]
for e in ['XVIII', 'XX', 'XXI']:
    lit.append((f'SGA7II_fr/expose_{e}_body.tex', f'{SGA}\\sga7ii\\current\\expose_{e}_body.tex'))
for e in ['VII', 'VIII', 'IX']:
    lit.append((f'SGA7I_fr/expose_{e}_body.tex', f'{SGA}\\sga7i\\current\\expose_{e}_body.tex'))


def build(name, items):
    path = os.path.join(OUT, name)
    man = ['path\torigin\tsha256']
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for arc, rel in items:
            src = os.path.join(DOC, rel)
            if not os.path.exists(src):
                print('MISSING', rel)
                continue
            data = open(src, 'rb').read()
            z.writestr(arc, data)
            man.append(f'{arc}\t{rel.replace(chr(92), "/")}\t{hashlib.sha256(data).hexdigest()}')
        z.writestr('MANIFEST.tsv', '\n'.join(man) + '\n')
    print(name, len(man) - 1, 'files', round(os.path.getsize(path) / 1e6, 2), 'MB')


build('RESEARCH_SA13_study.zip', study)
build('RESEARCH_SA13_transcriptions.zip', trans)
build('RESEARCH_SA13_literature.zip', lit)

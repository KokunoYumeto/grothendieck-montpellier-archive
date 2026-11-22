"""Record preserved primary-file hashes; this is provenance, not a finite proof certificate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
files = [
    'parts/D/sources/DeJongKatzCurves/curves.dvi',
    'parts/D/sources/DeJongKatzCurves/curves.pdf',
    'parts/D/sources/DeJongKatzCurves/curves.txt',
    'parts/C/sources/GustavsenIle2018/author_v3.pdf',
    'parts/C/sources/GustavsenIle2018/author_v3.txt',
]
record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'kind': 'primary-source file provenance; no mathematical certificate',
    'de_jong_katz_primary_url': 'https://www.math.columbia.edu/~dejong/papers/curves.dvi',
    'de_jong_katz_read_scope': 'Root freshly read all12 pages of the converted primary text; used Proposition4.2 pp4–6 in full.',
    'gustavsen_ile_read_scope': 'Root freshly read §2.1 p4 and complete Proposition2.7 proof pp7–8 of the preserved author version.',
    'conversion': {
        'initial_dvipdfmx_exit_code': 1,
        'initial_message': 'Unable to find TFM file cmbx10',
        'successful_command': "TEXMF='{/workspace/scratch/3f5f32d249c5/sa12_tex_support/texmf,/usr/share/texlive/texmf-dist,/usr/share/texmf}' dvipdfmx -q -o curves.pdf curves.dvi",
        'successful_exit_code': 0,
        'text_command': 'pdftotext -layout curves.pdf curves.txt',
        'text_exit_code': 0,
    },
    'files': [],
}
for rel in files:
    p = root / rel
    b = p.read_bytes()
    record['files'].append({'path': rel, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})
(root / 'code/output/post15_primary_files.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))

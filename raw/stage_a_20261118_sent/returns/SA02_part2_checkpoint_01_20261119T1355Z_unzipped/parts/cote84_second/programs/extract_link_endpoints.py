"""Extract complete selected source leaves and the public R&S text for link checking.
This program locates passages only; it does not assign verdicts or assert matches.
"""
from pathlib import Path
import re, subprocess
W=Path(__file__).resolve().parents[1]
R=W.parents[2]
f=R/'source/SA02_texts/pro/MPL_84_097-145_transcription.tex'
want={104,105,128,136,142}
scan=None; out=['SOURCE: '+str(f)]
for n,l in enumerate(f.read_text().splitlines(),1):
    m=re.search(r'\\scanpage\{(\d+)\}',l)
    if m:scan=int(m[1])
    if scan in want:out.append(f'L{n}: {l}')
(W/'outputs/cross_package_endpoints.txt').write_text('\n'.join(out)+'\n')
pdf=W.parent/'cote84_first/outputs/RS_public.pdf'
subprocess.run(['pdftotext','-layout',str(pdf),str(W/'evidence/RS_public_layout.txt')],check=True)
text=(W/'evidence/RS_public_layout.txt').read_text()
ls=text.split('\n'); ranges=[(9555,9590),(9680,9730),(12200,12245),(12618,12660),(15920,15980),(21300,21350),(21538,21585),(22858,22905),(24245,24412)]
out2=[]
for a,b in ranges:
    out2.append(f'PUBLIC R&S, extracted lines {a}–{b}; reading endpoint only')
    out2.extend(f'L{n}: {ls[n-1]}' for n in range(a,b+1))
(W/'outputs/RS_reference_endpoints.txt').write_text('\n'.join(out2)+'\n')
with (W/'outputs/RS_reference_page_map.txt').open('w') as z:
    for n,page in enumerate(text.split('\f'),1):
        for needle in ['9.3. (35) Mes passions','9.4. (36) Désir et méditation','Note 23iv Depuis','Note 42 "L’événement','Note 69 (27 avril)','Note 98 (22 septembre)','Note 99 (23 septembre)','Note 106 (2 octobre)','Note 113 (21 octobre)','Note 112 53']:
            if needle in page:z.write(f'PDF page {n}\t{needle}\n')
print('\n'.join(out))
print('Public R&S text extracted for targeted reference-endpoint reading; not a claim to have read the whole book.')

import re,sys,pathlib,hashlib
F=pathlib.Path(sys.argv[1]); B=F/'branches'
pat=re.compile(r'(K-?0[0-9][0-9]|PNEW-?0[0-9][0-9]|R-NEW-?0[0-9][0-9]|R-DIAG-?[0-9]+)')
for p in sorted(list((B/'kronecker').glob('*.tex'))+list((B/'root').glob('*.tex'))+list((B/'plethysm').glob('*.tex'))+list((B/'plethysm').glob('explorations/*'))):
    if not p.is_file(): continue
    t=p.read_bytes().decode('utf-8','replace')
    ls=t.split('\n')
    head=next((l.strip() for l in ls if l.startswith('\section')),'')
    print(str(p.relative_to(B)).replace('\','/'),len(ls),'|',head[:92])

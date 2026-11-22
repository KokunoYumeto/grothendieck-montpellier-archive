import gzip, pathlib, subprocess, tarfile, time, json, urllib.request
root=pathlib.Path(__file__).resolve().parents[1]
start=time.monotonic()
records=[]
for f in (root/'sources').glob('*_source.tar.gz'):
    d=f.parent/f.name.replace('_source.tar.gz','')
    d.mkdir(exist_ok=True)
    try:
        with tarfile.open(f) as t:
            t.extractall(d,filter='data')
        records.append({'file':f.name,'format':'tar.gz'})
    except tarfile.ReadError:
        (d/'source.tex').write_bytes(gzip.decompress(f.read_bytes()))
        records.append({'file':f.name,'format':'gz-single-tex'})
subprocess.run(['pdftotext','-layout',str(root/'sources'/'Orgogozo2003.pdf'),str(root/'sources'/'Orgogozo2003.txt')],check=True)
url='https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf'
path=root/'sources'/'Deligne_WeilII.pdf'
path.write_bytes(urllib.request.urlopen(url,timeout=45).read())
subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
records.append({'file':path.name,'url':url,'bytes':path.stat().st_size})
records.append({'total_seconds':round(time.monotonic()-start,3)})
output=json.dumps(records,indent=2)+'\n'
(root/'code'/'extract_sources_output.json').write_text(output)
print(output)

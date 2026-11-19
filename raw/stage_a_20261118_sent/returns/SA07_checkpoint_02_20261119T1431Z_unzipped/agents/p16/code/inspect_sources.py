"""Download public primary sources and extract searchable text for targeted reading.
All downloads are internal research evidence, excluded from delivered ZIP.
"""
import urllib.request,pathlib,subprocess,json,concurrent.futures
B=pathlib.Path(__file__).parents[1]; D=B/'evidence'
SOURCES={
'Grothendieck1969':'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1968.Grothendieck.StandardConjs.pdf',
'Kleiman1968':'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf',
'Jannsen1992':'https://epub.uni-regensburg.de/26642/1/jannsen10.pdf',
'KatzMessing1974':'https://web.math.princeton.edu/~nmk/old/katzmessing.pdf',
'Laumon1996':'https://arxiv.org/pdf/alg-geom/9603004',
'Beauville1983':'https://math.univ-cotedazur.fr/u/beauvill/pubs/fourier.pdf',
'Moonen2026':'https://www.math.ru.nl/~bmoonen/Papers/RPDM.pdf',
'BeckmannFortman2023':'https://olivierfortman.github.io/degaaybeckman-integralfourierAVs.pdf',
'Oda1969':'https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf',
'Kahn2021':'https://webusers.imj-prg.fr/~bruno.kahn/preprints/Murre-regular3.pdf',
'ACMV2023':'https://arxiv.org/pdf/1911.09911',
'OttemSuzuki2020':'https://arxiv.org/pdf/1906.08994',
'Matlis1958':'https://msp.org/pjm/1958/8-3/pjm-v8-n3-p13-s.pdf',
'Mumford1961':'https://www.dam.brown.edu/people/mumford/alg_geom/papers/1961a--TopSingSurface-NumDam.pdf',
'Coleman1998':'https://www.numdam.org/article/AIF_1998__48_5_1379_0.pdf',
'GrothendieckBrauer1968':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Alltenlectures.pdf',
'Clemens1983':'https://www.numdam.org/item/PMIHES_1983__58__19_0.pdf',
'Kunnemann2001':'https://www.numdam.org/item/ASENS_2001_4_34_4_503_0.pdf',
'SGA3VIIb':'https://wstein.org/sga/SGA3/Exp7B-20jan2010.pdf',
'GrothendieckPicard1962':'https://www.numdam.org/item/SB_1961-1962__7__221_0.pdf',
'EGAIV4':'https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf',
'MumfordAbelianII':'https://ncatlab.org/nlab/files/Mumford-AbelianVarieties-II.pdf',
'DeligneWeilII1980':'https://pmihes.centre-mersenne.org/item/10.1007/BF02684780.pdf',
}
def fetch(k,url):
    path=D/(k+'.pdf');result={'key':k,'url':url}
    try:
        if not path.exists():
            with urllib.request.urlopen(url,timeout=25) as r:
                data=r.read();result.update(final_url=r.geturl(),content_type=r.headers.get('Content-Type'))
            if not data.startswith(b'%PDF'): raise ValueError('Not a PDF: '+str(result))
            path.write_bytes(data)
        result['bytes']=path.stat().st_size
        p=subprocess.run(['pdftotext','-layout',str(path),str(D/(k+'.txt'))],capture_output=True,text=True)
        result.update(extract_status=p.returncode,stderr=p.stderr[:250])
    except Exception as e: result['error']=repr(e)
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    out=list(ex.map(lambda kv:fetch(*kv),SOURCES.items()))
(D/'primary_fetch_results.json').write_text(json.dumps(out,indent=2))
for r in out: print(json.dumps(r))

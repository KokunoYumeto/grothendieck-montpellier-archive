"""Select and optionally render the final systematic and overflow page checks.

Selection is not visual certification. Each selected image must actually be
opened, and its observation entered in a separate reviewed evidence record.
"""
from pathlib import Path
import argparse,csv,hashlib,json,re
import fitz
P=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('stem');a.add_argument('--render',action='store_true');args=a.parse_args()
path=P/'readers'/(args.stem+'.pdf');data=path.read_bytes();sha=hashlib.sha256(data).hexdigest();doc=fitz.open(stream=data,filetype='pdf')
meta=json.loads((P.parent/'inputs/text/records/PAGES_PS.json').read_text())
lookup={(str(m['cote']),int(m['site'])):m['key'] for m in meta}
pagekeys={};current=None
for i,page in enumerate(doc,1):
    found=re.search(r'scan\s*(134-\d)\s*/\s*(\d+)',page.get_text())
    if found:current=lookup[(found[1],int(found[2]))]
    pagekeys[i]=current
sample={round(i*(len(doc)-1)/39)+1 for i in range(40)} if len(doc)>=40 else set(range(1,len(doc)+1))
overflow_keys=set();history=P/'records/OVERFLOW_HISTORY.tsv'
form='corrected_apparatus' if args.stem.endswith(('corrected_apparatus','master_annotated')) else 'diplomatic' if args.stem.endswith('diplomatic') else 'reading'
if history.exists():
    for r in csv.DictReader(history.open(),delimiter='\t'):
        if r.get('page_key'):overflow_keys.add(r['page_key'])
unmapped_historical_keys=sorted(overflow_keys-{key for key in pagekeys.values() if key is not None})
historical_raster_overflow_mapping=[]
if form=='corrected_apparatus':
    for hp in sorted((P/'records').glob('INK_HISTORY_PS_EN_corrected_apparatus_*.json')):
        h=json.loads(hp.read_text());logpath=P/h['source_log'];log=logpath.read_text(errors='replace')
        oldmap={};key=None;physical=0;offsets={}
        for m in re.finditer(r'(?m)^PS-SOURCE: (\S+)|^\[(\d+)(?=$|[\s{\]])',log):
            if m[1]:key=m[1]
            else:
                physical+=1;offset=offsets.get(key,0);offsets[key]=offset+1;oldmap[physical]=(key,offset)
        for row in h['candidate_pages']:
            if not any(c['bbox_pt'][1]>=779 for c in row['components']):continue
            key,offset=oldmap[row['page']]
            mapped=[p for p,k in pagekeys.items() if k==key]
            assert mapped,('Unmapped raster overflow',hp.name,row['page'],key)
            final=mapped[min(offset,len(mapped)-1)]
            historical_raster_overflow_mapping.append({'history':str(hp.relative_to(P)),'old_pdf_page':row['page'],'source_key':key,'source_page_offset':offset,'final_pdf_page':final})
raster_overflow_pages={r['final_pdf_page'] for r in historical_raster_overflow_mapping}
rows=[];dest=P/'qa/rendered'/('final_'+args.stem);dest.mkdir(parents=True,exist_ok=True)
for i,page in enumerate(doc,1):
    reasons=[]
    if i in sample:reasons.append('systematic forty-page sample')
    if pagekeys[i] in overflow_keys:reasons.append('source page had overflow in at least one retained build, checked in every final reader')
    if i in raster_overflow_pages:reasons.append('corresponding source sheet had bottom ink overflow in the historical raster audit')
    if page.rect.width>page.rect.height:reasons.append('landscape page')
    if not reasons:continue
    target=dest/f'page_{i:04d}.png'
    if args.render:page.get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(target)
    rows.append({'pdf':str(path.relative_to(P)),'pdf_sha256':sha,'page':i,'key':pagekeys[i],'image':str(target.relative_to(P)),'reasons':reasons,'viewed':False})
result={'pdf':str(path.relative_to(P)),'pdf_sha256':sha,'pdf_pages':len(doc),'systematic_sample_pages':sorted(sample),'historical_overflow_keys':sorted(overflow_keys),'unmapped_historical_keys':unmapped_historical_keys,'landscape_pages':[i for i,p in enumerate(doc,1) if p.rect.width>p.rect.height],'selections':rows}
result['historical_raster_overflow_mapping']=historical_raster_overflow_mapping
(P/'records'/('QA_SELECTION_'+args.stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
if args.stem in {'PS_EN_diplomatic','PS_EN_corrected_apparatus','PS_EN_reading'}:
    assert not unmapped_historical_keys,('Historical overflow sources are unmapped in the final reader',args.stem,unmapped_historical_keys)
print(json.dumps({k:v for k,v in result.items() if k not in ['selections','historical_overflow_keys','historical_raster_overflow_mapping']}|{'selected_pages':len(rows),'historical_raster_overflow_mappings':len(historical_raster_overflow_mapping)}))

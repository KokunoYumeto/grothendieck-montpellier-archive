"""Record an explicit, complete visual collation of one page pair.

Calling collate certifies that the reviewer inspected both halves of both
copies. No source-string difference is assigned an outcome by this utility.
"""
from pathlib import Path
import csv,difflib,fcntl,hashlib,json,os,tempfile
from audit_inventory import read_tsv,write_tsv
from audit_apply import COLLATION_FIELDS

KINDS={'typed difference','misreading in one transcription','handwriting only in copy 1','handwriting only in copy 2','handwriting in both copies'}
COVERAGE_FIELDS=['pair_id','typescript_page','copy1_key','copy2_key','full_inspection','original_transcription_comparison','copy1_images','copy2_images','entry_count','shared_mark_count','copy2_annotation_count','copy1_checked_sha256','copy2_checked_sha256']

def write_json(path,data):
    with tempfile.NamedTemporaryFile('w',encoding='utf-8',dir=path.parent,prefix='.collation-',suffix='.json',delete=False) as f:
        f.write(json.dumps(data,ensure_ascii=False,indent=2)+'\n');temporary=f.name
    os.replace(temporary,path)

def require(value,name):
    if not isinstance(value,str) or not value.strip():raise ValueError(f'{name} requires an explicit observation')
    return value

def prepare(key2):
    """Return exact source comparisons as inspection aids; assign no outcome."""
    edition=Path(__file__).resolve().parent.parent;work=edition.parent
    p2=json.loads((work/'review_packets'/(key2+'.json')).read_text())
    if p2['copy']!=2:raise ValueError('A copy 2 page key is required')
    site1=int(p2['metadata']['site'])-76
    p1=json.loads((work/'review_packets'/f'esq_119_{site1:03d}.json').read_text())
    if p1['metadata']['ts_page']!=p2['metadata']['ts_page']:raise ValueError('Typescript page mapping mismatch')
    result={'copy1_key':p1['key'],'copy2_key':key2,'typescript_page':p1['metadata']['ts_page'],
        'required_images':p1['required_images']+p2['required_images'],
        'original_copy1':p1['source_text'],'original_copy2':p2['source_text'],
        'copy1_source_sha256':p1['source_sha256'],'copy2_source_sha256':p2['source_sha256']}
    for number,p in [(1,p1),(2,p2)]:
        path=edition/'checked_pages'/(p['key']+'.tex')
        result[f'checked_copy{number}']=path.read_text() if path.exists() else None
        result[f'copy{number}_checked_sha256']=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
    # This exact unified comparison retains comments, scan markers, macros, and
    # whitespace. Its differences are inspection targets, never conclusions.
    a=result['checked_copy1'] or result['original_copy1']
    b=result['checked_copy2'] or result['original_copy2']
    result['literal_comparison']=''.join(difflib.unified_diff(a.splitlines(keepends=True),b.splitlines(keepends=True),fromfile='copy 1',tofile='copy 2'))
    return result

def collate(key2, *, full, originals, entries, folio1=None, folio2=None, annotations=()):
    """Commit reviewed loci plus a full-page inspection declaration.

    entries: dictionaries containing line, copy1_reading, copy2_reading, kind,
    decision, reason, and optional source_ids (a list of stable source IDs).
    folio1/folio2: optional dictionaries with reading, place, reason, source_ids;
    supplying either explicitly records that observed copy-specific foliation.
    annotations: explicit bilingual copy2 apparatus entries. Each supplies kind,
    text_fr, text_en and source_ids; optional collation_loci (one-based indices)
    add the exact resulting collation IDs. All entries attach to this copy1 page.
    """
    require(full,'full-page inspection');require(originals,'original-transcription comparison')
    edition=Path(__file__).resolve().parent.parent
    lock=(edition/'.audit-records.lock').open('w');fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
    packet=prepare(key2);key1=packet['copy1_key']
    if packet['checked_copy1'] is None or packet['checked_copy2'] is None:
        raise ValueError('Both page files must be scan-checked and committed before their collation is finalized')
    site1=int(key1.rsplit('_',1)[1]);pair=f'COL-119-{site1:03d}'
    explicit_entries=[dict(e) for e in entries]
    for number,folio in [(1,folio1),(2,folio2)]:
        if folio is None:continue
        require(folio.get('reading'),'folio reading');require(folio.get('reason'),'folio observation')
        explicit_entries.append({'line':folio.get('place','bottom-left foliation'),
            'copy1_reading':folio['reading'] if number==1 else '',
            'copy2_reading':folio['reading'] if number==2 else '',
            'kind':f'handwriting only in copy {number}',
            'decision':'retain the observed copy-specific foliation',
            'reason':folio['reason'],'source_ids':folio.get('source_ids',[])})
    rows=[]
    for i,e in enumerate(explicit_entries,1):
        if isinstance(e.get('line'),int):e['line']=str(e['line'])
        for field in ['line','decision','reason']:require(e.get(field),field)
        for field in ['copy1_reading','copy2_reading']:
            if not isinstance(e.get(field),str):raise ValueError(f'{field} must contain the exact reading or an explicit empty string')
        if e.get('kind') not in KINDS:raise ValueError('Unsupported collation kind: '+str(e.get('kind')))
        ids=e.get('source_ids',[])
        if not isinstance(ids,list):raise ValueError('source_ids must be a list')
        rows.append({'collation_id':f'{pair}-{i:03d}','typescript_page':packet['typescript_page'] or 'sommaire',
            'line':e['line'],'copy1_key':key1,'copy2_key':key2,'copy1_reading':e['copy1_reading'],
            'copy2_reading':e['copy2_reading'],'kind':e['kind'],'decision':e['decision'],
            'reason':e['reason'],'decision_ids':';'.join(ids)})
    review={'pair_id':pair,'copy1_key':key1,'copy2_key':key2,'inspected_images':packet['required_images'],
        'full_inspection':full,'original_transcription_comparison':originals,'entries':explicit_entries,
        'copy1_checked_sha256':packet['copy1_checked_sha256'],'copy2_checked_sha256':packet['copy2_checked_sha256']}
    apparatus=[]
    for i,a0 in enumerate(annotations,1):
        a=dict(a0)
        for field in ['kind','text_fr','text_en']:require(a.get(field),field)
        ids=a.get('source_ids',[])
        if not isinstance(ids,list):raise ValueError('Annotation source_ids must be a list')
        for index in a.pop('collation_loci',[]):
            if not isinstance(index,int) or not 1<=index<=len(rows):raise ValueError('Annotation collation_loci must address an observed locus')
            ids.append(rows[index-1]['collation_id'])
        if not ids:raise ValueError('Each copy2 apparatus entry requires observed source or collation IDs')
        a.update(id=a.get('id',f'A2-119-{int(key2.rsplit("_",1)[-1]):03d}-{i:03d}'),
            key=key1,copy2_key=key2,source_ids=list(dict.fromkeys(ids)))
        apparatus.append(a)
    review['copy2_annotations']=apparatus
    dest=edition/'collation_reviews'/(key2+'.json');dest.parent.mkdir(exist_ok=True)
    serialized=json.dumps(review,ensure_ascii=False,indent=2)+'\n'
    if dest.exists() and dest.read_text()!=serialized:
        history=edition/'collation_reviews/history';history.mkdir(exist_ok=True)
        serial=1
        while (history/f'{key2}_{serial:03d}.json').exists():serial+=1
        (history/f'{key2}_{serial:03d}.json').write_text(dest.read_text())
        prior=[r for r in read_tsv(edition/'COLLATION.tsv') if r['copy2_key']==key2]
        if prior:write_tsv(history/f'{key2}_{serial:03d}_COLLATION.tsv',prior,COLLATION_FIELDS)
    dest.write_text(serialized)
    path=edition/'COLLATION.tsv';old=read_tsv(path) if path.exists() else []
    all_rows=[r for r in old if r['copy2_key']!=key2]+rows
    write_tsv(path,all_rows,COLLATION_FIELDS)
    write_tsv(edition/'records/COLLATION_COMMON_MARKS.tsv',[r for r in all_rows if r['kind']=='handwriting in both copies'],COLLATION_FIELDS)
    annotation_path=edition/'copy2_annotations.json'
    old_annotations=json.loads(annotation_path.read_text()) if annotation_path.exists() else []
    all_annotations=[a for a in old_annotations if a.get('copy2_key')!=key2]+apparatus
    if len({a['id'] for a in all_annotations})!=len(all_annotations):raise ValueError('Duplicate copy2 apparatus identifiers')
    write_json(annotation_path,all_annotations)
    coverage={'pair_id':pair,'typescript_page':packet['typescript_page'] or 'sommaire',
        'copy1_key':key1,'copy2_key':key2,'full_inspection':full,'original_transcription_comparison':originals,
        'copy1_images':' '.join(packet['required_images'][:2]),'copy2_images':' '.join(packet['required_images'][2:]),
        'entry_count':len(rows),'shared_mark_count':sum(r['kind']=='handwriting in both copies' for r in rows),
        'copy2_annotation_count':len(apparatus),'copy1_checked_sha256':packet['copy1_checked_sha256'],
        'copy2_checked_sha256':packet['copy2_checked_sha256']}
    path=edition/'records/COLLATION_PAGE_COVERAGE.tsv';old=read_tsv(path) if path.exists() else []
    write_tsv(path,[r for r in old if r['copy2_key']!=key2]+[coverage],COVERAGE_FIELDS)
    result={'pair_id':pair,'loci_recorded':len(rows),'images_declared_reviewed':4}
    print(json.dumps(result));return result

"""Render every final guide page, retaining older selected image versions."""
from pathlib import Path
import fitz,hashlib,json,re
P=Path(__file__).resolve().parents[1];R=P/'records'
f=P/'readers/PS_GUIDE.pdf';data=f.read_bytes();sha=hashlib.sha256(data).hexdigest();d=fitz.open(stream=data,filetype='pdf')
dest=P/'qa/rendered/final_PS_GUIDE';selectionfile=R/'QA_SELECTION_PS_GUIDE.json'
if selectionfile.exists():
    old=json.loads(selectionfile.read_text());oldsha=old['pdf_sha256']
    if oldsha!=sha:
        archived=dest.with_name(dest.name+'_'+oldsha[:8])
        if dest.exists() and not archived.exists():dest.rename(archived)
        oldtext=json.dumps(old,indent=2).replace('qa/rendered/final_PS_GUIDE/','qa/rendered/'+archived.name+'/')
        (R/('HISTORICAL_SELECTION_PS_GUIDE_'+oldsha[:8]+'.json')).write_text(oldtext+'\n')
        for rec in R.glob('HISTORICAL_VISUAL_QA_guide_*.json'):
            s=rec.read_text()
            if oldsha in s:rec.write_text(s.replace('qa/rendered/final_PS_GUIDE/','qa/rendered/'+archived.name+'/'))
dest.mkdir(exist_ok=True)
sample=sorted({round(i*(len(d)-1)/39)+1 for i in range(40)});targets={22,57,60,64,90,108,121,137};headingmap={};entries=[]
for number,page in enumerate(d,1):
    headings=[]
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            spans=line['spans'];s=''.join(x['text'] for x in spans)
            if any('Bold' in x['font'] and x['size']>11 for x in spans):
                headings.append(s);m=re.match(r'(?:§\s*)?(\d+)(?:\.|\s)',s)
                if m and int(m[1]) in targets:headingmap[int(m[1])]=number
    image=dest/f'page_{number:04d}.png';page.get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(image)
    reasons=['complete guide visual inspection, including all previous overflow and bottom-ink locations']
    if number in sample:reasons.append('systematic forty-page sample')
    entries.append({'pdf':'readers/PS_GUIDE.pdf','pdf_sha256':sha,'page':number,'key':'guide; '+('; '.join(headings) or 'continuation'),'image':str(image.relative_to(P)),'reasons':reasons,'viewed':False})
assert set(headingmap)==targets
result={'pdf':'readers/PS_GUIDE.pdf','pdf_sha256':sha,'pdf_pages':len(d),'systematic_sample_pages':sample,'historical_overflow_section_pages':headingmap,'unmapped_historical_keys':[],'landscape_pages':[],'selections':entries}
selectionfile.write_text(json.dumps(result,indent=2)+'\n')
(R/'GUIDE_HISTORICAL_OVERFLOW_LOCATIONS.json').write_text(json.dumps({'pdf':'readers/PS_GUIDE.pdf','pdf_sha256':sha,'sections':headingmap,'original_log_events':10,'basis':'Every previously overflowing section heading is located by its bold heading text in the final PDF; all guide pages receive actual visual inspection.'},indent=2)+'\n')
print(json.dumps({'pages':len(d),'pdf_sha256':sha,'historical_headings':headingmap}))

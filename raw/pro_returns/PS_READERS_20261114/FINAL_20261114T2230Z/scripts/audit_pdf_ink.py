"""Raster-screen every PDF page for ink outside the declared page regions.

This produces candidates for visual adjudication, not an automatic certificate.
An immutable byte snapshot prevents concurrent PDF replacement during scanning.
"""
from pathlib import Path
import argparse,hashlib,json
import fitz,numpy as np
from scipy import ndimage
P=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('stem');args=a.parse_args()
path=P/'readers'/(args.stem+'.pdf');data=path.read_bytes();sha=hashlib.sha256(data).hexdigest();doc=fitz.open(stream=data,filetype='pdf')
scale=2;mm=72/25.4;tolerance=.5;candidates=[];outside_sheet=[]
for number,page in enumerate(doc,1):
    width,height=page.rect.width,page.rect.height
    pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
    rgb=np.frombuffer(pix.samples,np.uint8).reshape(pix.height,pix.width,pix.n)
    ink=rgb[:,:,:3].min(axis=2)<220
    allowed=np.zeros(ink.shape,dtype=bool)
    left,right,top,bottom=18*mm,width-45*mm,18*mm,height-22*mm
    body_center=(left+right)/2
    regions=[(left,top,right,bottom),(right+7*mm,top,right+35*mm,bottom),(body_center-30,height-51,body_center+30,height-30),(right-35,20,right,37)]
    for x0,y0,x1,y1 in regions:
        ix0=max(0,int((x0-tolerance)*scale));iy0=max(0,int((y0-tolerance)*scale))
        ix1=min(pix.width,int(np.ceil((x1+tolerance)*scale)));iy1=min(pix.height,int(np.ceil((y1+tolerance)*scale)))
        allowed[iy0:iy1,ix0:ix1]=True
    mask=ink&~allowed;labels,count=ndimage.label(mask)
    components=[]
    for label,sl in enumerate(ndimage.find_objects(labels),1):
        if sl is None:continue
        y,x=sl;pixels=int(np.count_nonzero(labels[sl]==label))
        components.append({'bbox_pt':[x.start/scale,y.start/scale,x.stop/scale,y.stop/scale],'pixels':pixels})
    if components:candidates.append({'page':number,'components':components,'adjudication':'pending visual inspection'})
    for entry in page.get_bboxlog():
        kind,box=entry[:2]
        x0,y0,x1,y1=box
        if kind!='ignore-text' and (x0<-.5 or y0<-.5 or x1>width+.5 or y1>height+.5):
            outside_sheet.append({'page':number,'kind':kind,'bbox_pt':list(box)})
result={'pdf':str(path.relative_to(P)),'pdf_sha256':sha,'pages_screened':len(doc),'raster_dpi':144,'ink_threshold':220,'raster_quantization_tolerance_pt':tolerance,'declared_regions':'Body18mmleft,45mmright,18mmtop,22mmbottom;28mmrightmargin at7mmgap;page-number/header rectangles. Landscape pages require manual region verification.','candidate_pages':candidates,'objects_outside_sheet':outside_sheet,'complete_visual_adjudication':False}
(P/'records'/('INK_AUDIT_'+args.stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'pdf':result['pdf'],'pages_screened':len(doc),'candidate_pages':len(candidates),'candidate_page_numbers':[c['page'] for c in candidates],'objects_outside_sheet':len(outside_sheet)}))

"""Render a scheduled checkpoint's spread pages and newly added proofs."""
import fitz,json,time,sys,re
from PIL import Image,ImageDraw
from pathlib import Path
root=Path(__file__).resolve().parents[1];t=time.perf_counter();number=int(sys.argv[1])
doc=fitz.open(root/'build/RESEARCH_SA12_paper.pdf')
pages=set([1,4,5,9,10,11,12,13,15,20,25,26,30,32,33,35,38,39,40,45,50,len(doc)])
for i,p in enumerate(doc):
    text=p.get_text()
    if any(s in text for s in ['algebraically closed ground','wild affine','cyclic quartic','relative tame','Full stabilization','Iwasawa','proper subgroup','imperfect field','arbitrary base','nonnoetherian','genuine local cofiltering','common-refinement','Frobenius kernels','Milnor residue','normalization removes','principal quotient','nonexcellent class','normal models of a','alteration constants','punctured mutation','finite local groups','finite-field surfaces','unqualified filtered','general construction with clopen','surface stabilization','finite-length sheaf','Dedekind overrings','specified strictly local surface','virtually procyclic','arithmetic transcendence','number-ring base','cofinal Picard','elliptic branch','bad divisor','Picard scheme of the graph','smallness','pronilpotent','first direct image','two-group calculation','quadratic step','counterexample to eventual','invariant abelian','upper-cone stabilization','topological normalization','finite global images','semilinear action','finite constant extensions','positive-genus exceptional','elliptic three-point','minimal resolution']):pages.add(i+1)
if number==6:
    pages.update(range(21,34))
    pages.update(range(65,82))
if number==7:
    pages.update(range(90,131))
    pages.update(range(140,len(doc)+1))
if number==8:
    new_starts=[i+1 for i,p in enumerate(doc) if 'formal linearization of a curve' in p.get_text().lower()]
    assert new_starts, 'Could not locate the first post-checkpoint07 proof.'
    pages.update(range(min(new_starts),len(doc)+1))
if number==9:
    # Preserve earlier complete render records, and inspect the entire new
    # proof block plus a fresh document-wide spread and the updated end matter.
    # Avoid repeating all old proof pages at every checkpoint under the500MB cap.
    pages={1,3,5,8,15,25,35,45,55,65,75,85,95,105,115,125,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(
        r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=json.loads((root/'code/output/integrate_D_post08.json').read_text())['labels']
    assert all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    last=max(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),min(len(doc),last+2)+1))
    # Any precisely scoped failed-route supplement belongs in this check too.
    for key,page in label_pages.items():
        if key.startswith('D:pure-root-'):
            pages.update(range(max(1,page-1),min(len(doc),page+2)+1))
    end_starts=[i+1 for i,p in enumerate(doc)
                if i+1>last+2 and (
                    'Remaining proof gates' in p.get_text()
                    or 'Remaining unchecked' in p.get_text()
                    or 'Unresolved statements' in p.get_text())]
    if end_starts:
        pages.update(range(min(end_starts),len(doc)+1))
    else:
        pages.update(range(max(1,len(doc)-14),len(doc)+1))
if number==13:
    pages={1,3,5,8,15,25,35,45,55,65,75,85,95,105,115,125,135,145,155,165,175,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=json.loads((root/'code/output/integrate_post09.json').read_text())['labels']
    assert all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==14:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=json.loads((root/'code/output/integrate_post13.json').read_text())['labels']
    assert all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==15:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=json.loads((root/'code/output/integrate_post14.json').read_text())['labels']
    assert all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==16:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=json.loads((root/'code/output/integrate_post15.json').read_text())['labels']
    assert all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==17:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    manifests=['integrate_post16.json','integrate_Brauer_zero_post16.json',
               'integrate_post16_supplements.json','integrate_post16_final.json']
    added=[]
    for manifest in manifests:
        added.extend(json.loads((root/'code/output'/manifest).read_text())['labels'])
    assert len(set(added))==17
    assert all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==18:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=set()
    for manifest in sorted((root/'code/output').glob('integrate_post17*.json')):
        if manifest.name.endswith('.run.json'):
            continue # execution metadata, not a theorem-integration manifest
        added.update(json.loads(manifest.read_text())['labels'])
    assert added and all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==19:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=set()
    for manifest in sorted((root/'code/output').glob('integrate_post18*.json')):
        if manifest.name.endswith('.run.json'):
            continue
        added.update(json.loads(manifest.read_text())['labels'])
    assert added and all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==20:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=set()
    for manifest in sorted((root/'code/output').glob('integrate_post19*.json')):
        if manifest.name.endswith('.run.json'):
            continue
        added.update(json.loads(manifest.read_text())['labels'])
    assert added and all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==21:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    first=label_pages['D:controlled-one-curve-gerbe-anchors']
    pages.update(range(max(1,first-1),len(doc)+1))
if number==22:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    first=label_pages['D:SNC-tree-Brauer-geometry']
    pages.update(range(max(1,first-1),len(doc)+1))
if number==23:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    first=label_pages['D:normal-subgroup-projective-crowns']
    pages.update(range(max(1,first-1),len(doc)+1))
if number==24:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,365,385,405,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    first=label_pages['D:different-Frobenius-invariant-lattice']
    pages.update(range(max(1,first-1),len(doc)+1))
if number==25:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,347,365,385,405,425,445,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    first=label_pages['D:permutation-matrix-model-count']
    pages.update(range(max(1,first-1),len(doc)+1))
if number==26:
    pages={1,3,4,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,347,365,385,405,425,445,465,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    first=label_pages['D:strict-Cartier-separating-parameters']
    pages.update(range(max(1,first-1),len(doc)+1))
if number==27:
    pages={1,3,4,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,347,365,385,405,425,445,465,485,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=set()
    for manifest in sorted((root/'code/output').glob('integrate_post19_post26*.json')):
        added.update(json.loads(manifest.read_text())['labels'])
    assert added and all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==28:
    pages={1,3,4,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,347,365,385,405,425,445,465,485,505,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=set()
    for manifest in sorted((root/'code/output').glob('integrate_post19_post27*.json')):
        added.update(json.loads(manifest.read_text())['labels'])
    assert added and all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==29:
    pages={1,3,4,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,347,365,385,405,425,445,465,485,505,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=set()
    for manifest in sorted((root/'code/output').glob('integrate_post19_post28*.json')):
        added.update(json.loads(manifest.read_text())['labels'])
    assert added and all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    pages.update(range(max(1,first-1),len(doc)+1))
if number==30:
    # Inspect every newly assembled proof, the changed opening/end matter,
    # and fresh spread pages; retain earlier complete image provenance.
    # Avoid another full rendering of unchanged bibliography under the cap.
    pages={1,2,3,4,5,75,175,275,375,475,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
    added=set()
    for manifest in sorted((root/'code/output').glob('integrate_post19_post29*.json')):
        added.update(json.loads(manifest.read_text())['labels'])
    assert added and all(key in label_pages for key in added)
    first=min(label_pages[key] for key in added)
    last=max(label_pages[key] for key in added)
    end_starts=[i+1 for i,p in enumerate(doc) if i+1>last and any(
        phrase in p.get_text() for phrase in
        ['Remaining proof gates','Remaining unchecked','Unresolved statements'])]
    assert end_starts, 'Locate the unresolved section before rendering CP30.'
    end=min(end_starts)
    pages.update(range(max(1,first-1),min(len(doc),end+4)+1))
    for i,p in enumerate(doc):
        if i+1<=end:continue
        text=p.get_text()
        if any(phrase in text for phrase in [
            'Colliot-Th', 'Quadratic forms over fraction fields',
            'On the equations defining abelian varieties',
            'Central Simple Algebras and Galois Cohomology']):
            pages.update(range(max(1,i),min(len(doc),i+2)+1))
if number==5: pages.update(range(18,24)); pages.update(range(51,61)); pages.update(range(74,79))
pages=sorted(p for p in pages if p<=len(doc));thumbs=[]
extension='webp' if number>=18 else 'png'
pixel_checks=[]
for p in pages:
    pix=doc[p-1].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
    out=root/f'qa/checkpoint{number:02d}_page_{p:02d}.{extension}'
    if extension=='png':pix.save(out)
    else:
        page_image=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        page_image.save(out,'WEBP',lossless=True,quality=100,method=4)
        assert Image.open(out).convert('RGB').tobytes()==page_image.tobytes()
        pixel_checks.append(str(out.relative_to(root)))
    im=Image.open(out).convert('RGB');im.thumbnail((398,565))
    card=Image.new('RGB',(418,601),'#dddddd');card.paste(im,((418-im.width)//2,26))
    ImageDraw.Draw(card).text((10,7),f'Page {p}',fill='black');thumbs.append(card)
for group in range((len(thumbs)+8)//9):
    items=thumbs[group*9:group*9+9];sheet=Image.new('RGB',(1254,601*((len(items)+2)//3)),'white')
    for i,im in enumerate(items):sheet.paste(im,((i%3)*418,(i//3)*601))
    out=root/f'qa/checkpoint{number:02d}_contact_{group+1}.{extension}'
    if extension=='png':sheet.save(out)
    else:
        sheet.save(out,'WEBP',lossless=True,quality=100,method=4)
        assert Image.open(out).convert('RGB').tobytes()==sheet.tobytes()
        pixel_checks.append(str(out.relative_to(root)))
record={'pdf_pages':len(doc),'rendered_pages':pages,'seconds':time.perf_counter()-t,'image_format':extension,'lossless_pixel_roundtrip_checks':pixel_checks,'note':'From checkpoint18, new inspection images use lossless WebP with exact RGB pixel round-trip checks. Historical contact PNGs were re-encoded losslessly after checkpoint20; every decoded RGB pixel was verified equal and all old/current paths and hashes are retained in qa/historical_contact_encoding_map.json. Earlier immutable archives retain the original image bytes.'}
(root/f'qa/checkpoint{number:02d}_render.json').write_text(json.dumps(record,indent=2))
print(record)

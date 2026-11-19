"""Reproducible navigation and bounded absence search, not a verdict generator.

The targets below were read from the 125 Context paragraphs and note #118.
Searches examine every UTF-8 textual file of each recovered context package.
Mathematical identity and status decisions are authored separately.
"""
from pathlib import Path
import hashlib, json, re

BASE = Path('/workspace/scratch/4017236f14bf')
OUT = Path(__file__).parent
ROOTS = {'package69':BASE/'prior_context/extracted',
         'package138':BASE/'prior_context_138/extracted'}
TARGETS = {
 'WG2-B15':r'\bB15\b', 'WG2-3.1-2':r'§\s*3[.]1\s*#?\s*2\b',
 'R121-08':r'R121[-–]08', 'STRATA-A4':r'\bA[.]4\b',
 'BISITE-G10':r'\bG[.]10\b', 'STRATA-A12':r'\bA[.]12\b',
 'MPL150-N18':r'\bN18\b', 'STRATA-0.1':r'\bSTRATA\s+0[.]1\b',
 'MPL150-Q1b':r'\bQ1b\b', 'INTAKE-13.2':r'§\s*13[.]2\b',
 'MPL150-Q4b':r'\bQ4b\b', 'MPL151-Q4-02':r'Q4[-–]02',
 'MPL148-R29':r'\bR29\b', 'MPL150-N39':r'\bN39\b',
 'EXIT-P4e':r'\bP4e\b', 'MPL148-R34':r'\bR34\b',
 'MPL150-Q9':r'\bQ9\b', 'BISITE-D11':r'\bD[.]11\b',
 'RESIDUE-H1':r'\bH[.]1\b', 'PATHS-E10':r'\bE[.]10\b',
 'MPL150-N35':r'\bN35\b', 'STRATA-C8':r'\bC[.]8\b',
 'RESIDUE-H2':r'\bH[.]2\b', 'MPL150-Q2':r'\bQ2\b',
 'EXIT-P1a1':r'\bP1a1\b', 'MPL147-69':r'MPL_147_138[-–]190|§\s*69\b',
 'MPL151-Q4-03':r'Q4[-–]03', 'RESIDUE-A7':r'\bA[.]7\b',
 'MPL148-R39':r'\bR39\b', 'INTAKE-13.6':r'§\s*13[.]6\b',
 'MPL121-Q4.2':r'\bQ4[.]2\b', 'DER-XVI-87-96':r'87.{0,8}96',
 'MPL121-Q4.3':r'\bQ4[.]3\b', 'STRATA-B1':r'\bB[.]1\b',
 'PATHS-D13':r'\bD[.]13\b', 'MPL148-R16':r'\bR16\b',
 'MPL148-T01':r'\bT01\b', 'LM4-C12':r'\bC[.]12\b',
 'RESIDUE-E6':r'\bE[.]6\b', 'EXIT-P3c':r'P3c[-–]general',
 'PATHS-C10':r'\bC[.]10\b', 'RESIDUE-C8':r'\bC[.]8\b',
 'RESIDUE-F6':r'\bF[.]6\b', 'RESIDUE-I7':r'\bI[.]7\b',
 'RESIDUE-J2':r'\bJ[.]2\b', 'RESIDUE-J3':r'\bJ[.]3\b',
 'PATHS-B8':r'\bB[.]8\b', 'PATHS-C9':r'\bC[.]9\b',
 'TOTASPH-F27':r'\bF[.]27\b',
 'GALOIS-A8':r'GALOIS.{0,8}A[.]8',
 'GALOIS-B3':r'GALOIS.{0,8}B[.]3',
 'GALOIS-B5':r'GALOIS.{0,8}B[.]5',
}
manifest=[]; files=[]
for package,root in ROOTS.items():
    for file in sorted(root.rglob('*')):
        if not file.is_file() or file.suffix not in {'.md','.tex','.txt','.csv','.tsv','.json'}:
            continue
        data=file.read_bytes()
        try: lines=data.decode('utf-8-sig').splitlines()
        except UnicodeDecodeError: continue
        rel=str(file.relative_to(root))
        manifest.append({'package':package,'path':rel,'bytes':len(data),
                         'sha256':hashlib.sha256(data).hexdigest(),'lines':len(lines)})
        files.append((package,rel,lines))
results={}
for target,expr in TARGETS.items():
    pattern=re.compile(expr,re.I)
    hits=[]
    for package,rel,lines in files:
        for n,line in enumerate(lines,1):
            if pattern.search(line):
                hits.append({'package':package,'path':rel,'line':n,
                             'characters':len(line),
                             'line_sha256':hashlib.sha256(line.encode()).hexdigest()})
    results[target]={'query':expr,'hits':hits}
(OUT/'candidate_hits.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
(OUT/'search_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(OUT/'candidate_summary.tsv').write_text('target\tquery\thit_count\n'+''.join(
 f"{k}\t{v['query']}\t{len(v['hits'])}\n" for k,v in results.items()))
print(json.dumps({'files':len(files),'packages':list(ROOTS),'targets':len(TARGETS),
                  'zero_token_hit_targets':[k for k,v in results.items() if not v['hits']]},indent=2))

#!/usr/bin/env python3
"""Apply the specifically reviewed final guide copyedits, with exact diffs.

No checked page, annotated text master, formula token or manuscript quotation
is normalized. The authorized duplicate-paragraph consolidation has its own
clause-to-retained-passage crosswalk.
"""
from pathlib import Path
from datetime import datetime,timezone
import difflib,json,re
from edition_core import sha256,read_tsv,write_tsv,math_fragments

EDITION=Path(__file__).resolve().parents[1]
PROTECTED=re.compile(r"(``.*?''|\$[^$]*\$|\\\(.*?\\\)|https?://[^}\s]+)",re.S)

def prose_only(s,fn):
    parts=PROTECTED.split(s)
    for n in range(0,len(parts),2):parts[n]=fn(parts[n])
    return ''.join(parts)

def spaces(s):
    parts=PROTECTED.split(s)
    for n in range(0,len(parts),2):
        t=parts[n]
        t=re.sub(r'\b([A-Za-z]+)(?=\d)',r'\1 ',t)
        t=re.sub(r'Chapter(?=[IVX]+\b)','Chapter ',t)
        t=re.sub(r'(?<=[,;:])(?=\d)',' ',t)
        t=re.sub(r'\b(clause|clauses|and)(?=\()',r'\1 ',t)
        t=re.sub(r'(?<=[A-Za-z])(?=\\S)',' ',t)
        if n+1<len(parts) and parts[n+1].startswith(('$',r'\(')) and t and t[-1].isalnum():t+=' '
        if n>0 and parts[n-1].startswith(('$',r'\(')) and t and t[0].isalnum():t=' '+t
        parts[n]=t
    return ''.join(parts)

def main():
    target=EDITION/'records/guide_copyedit';target.mkdir(exist_ok=True)
    marker=target/'COMPLETED.json'
    if marker.is_file():
        print('The documented final guide copyedit has already run.');return
    originals={p.name:p.read_text() for p in (EDITION/'guide_parts').glob('*.tex')}
    changed=dict(originals);reasons={}
    for name in ['IV20_08.tex','21_1.tex','21_2.tex','21_3.tex']:
        changed[name]=spaces(changed[name]);reasons[name]='Restore ordinary editorial prose/number/math boundaries outside quoted source fragments and formulas.'
    substitutions={
      'iv16_singular_supersingular.tex': [('locally direct summands','local direct factors')],
      'iv17_15_smooth_forms.tex': [('invertible locally direct summand','invertible Module locally a direct factor')],
      '20_11.tex':[('neighbouring','neighboring')],
      '20_14.tex':[('generic-centre','generic-center'),('generic centre','generic center')],
      '21_1.tex':[('pullback formula','inverse image formula')],
      '21_2.tex':[('sub-prescheme','subprescheme')],
      '21_3.tex':[('behaviour','behavior'),('pullback of','inverse image of')],
      'iv17_16_quadratic_forms.tex':[('fibred categories','fibered categories'),('pullback','inverse image')],
    }
    for name,pairs in substitutions.items():
        for before,after in pairs:
            assert before in changed[name],(name,before)
            changed[name]=prose_only(changed[name],lambda part,a=before,b=after:part.replace(a,b))
        reasons[name]=reasons.get(name,'')+' Apply the supplied glossary and root-confirmed editorial terminology; quoted source words remain unchanged.'
    name='iv21_4_linear_systems.tex'
    assert changed[name].count('``fibre réduite;')==1
    changed[name]=changed[name].replace('``fibre réduite;',"``fibre réduite'';")
    reasons[name]='Close the editorial quotation after the unchanged French words fibre réduite; preserve the source phrase exactly.'
    for name,after in changed.items():
        assert math_fragments(after)==math_fragments(originals[name]),('math changed',name)
        assert re.findall(r'https?://[^}\s]+',after)==re.findall(r'https?://[^}\s]+',originals[name]),('URL changed',name)
    name='20_11.tex'
    changed[name]=changed[name].replace('neighboring handwritten dual accents','neighboring handwritten V-shaped dual accents')
    ending='Site 66 begins the separate section on generalizing earlier results to linear sections.'
    assert changed[name].count(ending)==1
    changed[name]=changed[name].replace(ending,"Site 66 begins the separate section on generalizing earlier results to linear sections, under the revised title ``Généralisation de résultats antérieurs aux sections linéaires''.")
    reasons[name]+=' Consolidate the duplicate tail paragraph, retaining its V-shaped accent detail and exact next-section title in the preceding text; see GUIDE_IV20_11_CLAUSE_MAP.tsv.'
    changed['20_11_tail_notes.tex']='% The supplementary observations formerly printed here are consolidated into guide_parts/20_11.tex.\n% The complete prior text and clause mapping are retained in records/guide_copyedit/ and records/GUIDE_IV20_11_CLAUSE_MAP.tsv.\n'
    reasons['20_11_tail_notes.tex']='Remove the duplicate rendered paragraph after explicit root approval; preserve its complete prior text and all clauses in the neighboring IV20.11 prose, with a clause map.'
    clauses=[
      ('Affine charts for the Grassmannian, sites63–64','site 63 gives the affine charts indexed by choices of $n$ basis vectors'),
      ('Local lifting of rational points','local lifting of a rational point to a section'),
      ('Correspondence between quotient Modules and linear subvarieties','Sites 64--65 interpret the Grassmannian in terms of linear subvarieties'),
      ('Unaccented E and the exact source quotation','visible unaccented $E$ in ``soit E son dual\'\''),
      ('Adjacent V-shaped handwritten dual accents','neighboring handwritten V-shaped dual accents'),
      ('Crossed section12 heading and replacement quotient functor','A canceled section-12 heading is followed by the handwritten addition introducing the quotient functor'),
      ('No prescribed rank and uncertain small index','no prescribed rank and representing it by the coproduct over $n\\geq0$. Its small index is partly uncertain.'),
      ('Rank and relative dimension vary over a disconnected base','rank, and hence relative dimension, to vary over a disconnected base'),
      ('Site66 and the exact revised title','Site 66 begins the separate section on generalizing earlier results to linear sections, under the revised title ``Généralisation de résultats antérieurs aux sections linéaires\'\'.'),
    ]
    for _,fragment in clauses:assert fragment in changed['20_11.tex'],fragment
    write_tsv(EDITION/'records/GUIDE_IV20_11_CLAUSE_MAP.tsv',[dict(prior_file='guide_parts/20_11_tail_notes.tex',clause=a,retained_file='guide_parts/20_11.tex',retained_passage=b,source_sites='63--66',note='The prior tail paragraph contained site references but no hyperlink URL; all prior URLs elsewhere remain byte-identical.') for a,b in clauses])
    ledger=EDITION/'records/GUIDE_REVISIONS.tsv';rows=read_tsv(ledger);proof=[]
    stamp=datetime.now(timezone.utc).isoformat()
    for name,after in changed.items():
        before=originals[name]
        if before==after:continue
        (target/('before_'+name)).write_text(before)
        (target/('after_'+name)).write_text(after)
        diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='guide_parts/'+name+' (before)',tofile='guide_parts/'+name+' (after)'))
        (target/(name+'.diff')).write_text(diff)
        (EDITION/'guide_parts'/name).write_text(after)
        rows.append(dict(utc=stamp,file='guide_parts/'+name,kind='final editorial copyedit',before_sha256=sha256(before),after_sha256=sha256(after),reason=reasons[name]+' Exact diff: records/guide_copyedit/'+name+'.diff.'))
        proof.append(dict(file='guide_parts/'+name,before_sha256=sha256(before),after_sha256=sha256(after),math_tokens_identical=math_fragments(before)==math_fragments(after),urls_identical=re.findall(r'https?://[^}\s]+',before)==re.findall(r'https?://[^}\s]+',after)))
    write_tsv(ledger,rows)
    marker.write_text(json.dumps(dict(utc=stamp,files=proof,note='The duplicate optional tail loses its redundant E occurrence; that exact token and every factual clause remain in20_11.tex as documented. All other formula lists and all URLs remain byte-identical.'),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(changed_files=len(proof),clause_map=len(clauses))))

if __name__=='__main__':main()

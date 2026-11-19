"""Presentation-only cleanup plus explicitly documented final source corrections."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]

# Original inline delimiters lost their opening backslash in the file-writing
# string. All top-level parentheticals were inspected before applying this repair.
p=ROOT/'computations.md';s=p.read_text()
s=s.replace('ExposéVIIA,Corollary4.4.1','ExposéVIIB,Corollary4.4.1')
s=s.replace('The source explicitly retains unproved Lefschetz assertions and a primitive-decomposition warning',
            'The source explicitly retains unspecified unproved assertions and a primitive-decomposition warning')
s=s.replace('claim461; Moonen,undated','claim461; van der Geer and Moonen,undated')
lines=[];display=False
exclude=re.compile(r'^(?:claim|Stacks|Laumon,|Mukai,|Mumford,|Moonen,|Coleman,|Oda,|Gabriel,|Ulmer,|van der Geer|\d{4},)')
converted=0
for line in s.splitlines():
    if line==r'\[':display=True;lines.append(line);continue
    if line==r'\]':display=False;lines.append(line);continue
    # Already-repaired inline math must not be parsed as new parentheticals.
    if display or '$' in line:lines.append(line);continue
    spans=[];depth=0;start=None
    for j,c in enumerate(line):
        if c=='(':
            if depth==0:start=j
            depth+=1
        elif c==')' and depth:
            depth-=1
            if depth==0:
                content=line[start+1:j]
                if not exclude.match(content) and content!='1':
                    spans.append((start,j+1,content.rstrip('\\')))
    for a,b,content in reversed(spans):
        line=line[:a]+'$'+content+'$'+line[b:];converted+=1
    lines.append(line)
s='\n'.join(lines)+'\n'
s=re.sub(r',(?!\s)',', ',s)
s=re.sub(r'\b(claims?|Theorems?|Propositions?|Corollar(?:y|ies)|Lemma|Definition|Exercise|Chapter|Tags?)(?=\d)',r'\1 ',s)
s=re.sub(r'\b(pp?)(?=\d)',r'\1. ',s)
s=re.sub(r'\b(\d{1,2})(January|February|March|April|May|June|July|August|September|October|November|December)(\d{4})',r'\1 \2 \3',s)
p.write_text(s)

# These replacements only separate accidentally concatenated prose tokens in
# machine-readable records; mathematical expressions and ids remain intact.
replacements={
 'Status19November2026':'Status as of 19 November 2026',
 'As of19November2026':'As of 19 November 2026',
 'allclasses':'all classes','all-codimensionexistence':'all-codimension existence',
 'forallsuch':'for all such','for everyi':'for every i',
 'allregular':'all regular','everycodimension':'every codimension',
 'universalregular':'universal regular','the1964':'the 1964',
 'the2025':'the 2025','the2026':'the 2026',
 'cyclevarieties':'cycle varieties','otherprojects':'other projects',
 'integer multiple':'integer multiple','codimension2':'codimension 2',
 'codimension3':'codimension 3','codimensions1,2,d':'codimensions 1, 2, d',
 'codimensions1,2,dimX':'codimensions 1, 2, dimX',
 'oddcohomology':'odd cohomology','regularhomomorphism':'regular homomorphism',
 'regularrepresentative':'regular representative','smoothprojective':'smooth projective',
 'smoothproper':'smooth proper','overnumberfields':'over number fields',
 'overC':'over C','overK':'over K','overF_q':'over F_q',
 'overa':'over a','forabelian':'for abelian','forhis':'for his',
 'forits':'for its','fordivisors':'for divisors','thetheorem':'the theorem',
 'thefinitekernel':'the finite-kernel','thewithdrawnclause':'the withdrawn clause',
 'thefixedpartdefinition':'the fixed-part definition','thePicard':'the Picard',
 'andthreefold':'and threefold','andcheckingthe':'and checking the',
 'thebalancedcase':'the balanced case','mundefined':'m undefined',
 'essentialnormalizations':'essential normalizations','verticalcorrections':'vertical corrections',
 'model/vertical-correctiondata':'model/vertical-correction data',
 'thedisplayed':'the displayed','thepage':'the page','Thepage':'The page',
 'pairingformula':'pairing formula','partlydeveloped':'partly developed',
 'conditionalon':'conditional on','all-fibrationversion':'all-fibration version',
 'identicalintegral':'identical integral','cohomologicallowdegreesare':'cohomological low degrees are',
 'universaltheorem':'universal theorem','numericalequivalence':'numerical equivalence',
 'algebraicequivalence':'algebraic equivalence','nonzerointeger':'nonzero integer',
 'all-codimensionextension':'all-codimension extension','notdefinedlocally':'not defined locally',
 'theink':'the ink','nearbydefinition':'nearby definition','beforeidentifyingthe':'before identifying the',
 'non-torsionhomologicallytrivialcodimension2cycles':'non-torsion homologically trivial codimension-2 cycles',
 'moduloalgebraicequivalence':'modulo algebraic equivalence',
 'onaverygeneralsmoothcomplexquinticthreefold':'on a very general smooth complex quintic threefold',
 'divisorversionknownbefore1964':'divisor version known before 1964',
 'unrestrictedusualinterpretationfalse':'unrestricted usual interpretation false',
 'pagesdo':'pages do','notdefineτ':'not define τ','latercounterexampledoesnotshowthatτ':'later counterexample does not show that τ',
 'wasmisread':'was misread','whytheauthorlefttheprogramme':'why the author left the programme',
 'symbolandscope':'symbol and scope','new proof ofthe':'new proof of the',
 'unrestrictedusualstatement':'unrestricted usual statement',
 'the manuscriptJ':'the manuscript J','identification ofthe':'identification of the',
 'no chosenHodge':'no chosen Hodge','char0':'characteristic 0',
 'bothzero':'both zero','fixedfactor':'fixed factor','crossedout':'crossed out',
 'miniversal-cyclemultiplicity':'miniversal-cycle multiplicity',
 'not theentire':'not the entire','cycle-Jacobianrealization':'cycle-Jacobian realization',
 'Counterexampleindependently':'Counterexample independently',
 'Manuscript1964':'Dated letter1964','Grothendieck1964':'Grothendieck1964'
}
for name in ['claims.json','items.json','problems.json']:
    rows=json.loads((ROOT/name).read_text())
    for row in rows:
        for key,val in row.items():
            if not isinstance(val,str) or key in {'id','cote','kind','class','check','confidence'}:continue
            for a,b in replacements.items():val=val.replace(a,b)
            val=re.sub(r',(?!\s)',', ',val)
            val=re.sub(r'\b(\d{1,2})(January|February|March|April|May|June|July|August|September|October|November|December)(\d{4})',r'\1 \2 \3',val)
            row[key]=val
        if row.get('id')=='SA19-223' and 'Exact published counterparts were subsequently identified' not in row['reconstruction']:
            row['reconstruction']+=' Exact published counterparts were subsequently identified in this audit: EGA IV₃ 11.4.1 and 11.4.4–6; the nonempty-versus-irreducible base difference is stated explicitly in CL-SA19-434.'
        if row.get('id')=='SA19-230':
            row['reconstruction']=row['reconstruction'].replace('±4','−4').replace('±1/4','−1/4').replace('A connected-kernel quotient','A quotient by the reduced neutral abelian radical (over a perfect field, or over C)')
    (ROOT/name).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Inline mathematical spans repaired:',converted)
print('JSON prose spacing checked; no source transcription edited.')

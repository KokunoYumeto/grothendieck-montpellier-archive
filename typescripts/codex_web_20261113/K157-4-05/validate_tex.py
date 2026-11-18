"""Static source checks only. This program never invokes a TeX engine."""
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re
from datetime import datetime, timezone

OUT=Path(__file__).resolve().parent
ID='K157-4-05'
CUSTOM=set('cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible'.split())
STANDARD=set('Big S alpha backslash begin bigl bigr bullet cap circ cup end geq in infty input lambda ldots leq longleftarrow longmapsto longrightarrow mapsto mathbb mathrm mu ne overset prod quad rho sim simeq subset text textsuperscript to underset varinjlim varprojlim Delta Psi Upsilon Rightarrow approx amalg'.split())
PACKAGES=set('arrow operatorname tag xrightarrow'.split())
ENVIRONMENTS={'tikzcd','gathered','aligned','array','tikzpicture','document'}

def tokens(s):
    # Match a control sequence as one token, so \\W after a line break is not
    # mistaken for an undefined control word named W.
    pattern=re.compile(r'\\(?:[A-Za-z]+|[^\n])|%[^\n]*|.',re.S)
    return [(m.group(),m.start()) for m in pattern.finditer(s) if not m.group().startswith('%')]

def check(q):
    s=q.read_text(); ts=tokens(s); errors=[]; braces=[]; display=[]; parmath=[]; dollars=0; cmds=set(); counts=Counter()
    for tok,pos in ts:
        line=s.count('\n',0,pos)+1
        if re.fullmatch(r'\\[A-Za-z]+',tok):
            cmd=tok[1:];cmds.add(cmd);counts[cmd]+=1
            if cmd not in CUSTOM|STANDARD|PACKAGES: errors.append(f'line {line}: unapproved/unknown command {tok}')
        if tok=='{':braces.append(line)
        elif tok=='}':
            if braces:braces.pop()
            else:errors.append(f'line {line}: unmatched closing brace')
        elif tok==r'\[':display.append(line)
        elif tok==r'\]':
            if display:display.pop()
            else:errors.append(f'line {line}: unmatched display close')
        elif tok==r'\(':parmath.append(line)
        elif tok==r'\)':
            if parmath:parmath.pop()
            else:errors.append(f'line {line}: unmatched inline math close')
        elif tok=='$':dollars+=1
    if braces:errors.append(f'unclosed braces at lines {braces}')
    if display:errors.append(f'unclosed displays at lines {display}')
    if parmath:errors.append(f'unclosed inline math at lines {parmath}')
    if dollars%2:errors.append(f'odd dollar count: {dollars}')
    clean=''.join(tok for tok,pos in ts)
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        action,env=m.groups()
        if env not in ENVIRONMENTS:errors.append(f'unapproved environment {env}')
        if action=='begin':stack.append(env)
        elif not stack or stack.pop()!=env:errors.append(f'environment nesting mismatch at {env}')
    if stack:errors.append(f'unclosed environments: {stack}')
    if counts['diagram']!=clean.count(r'\begin{tikzcd}'):
        errors.append('diagram/tikzcd count mismatch')
    if clean.count(r'\begin{tikzcd}')!=clean.count('ampersand replacement=\\&'):
        errors.append('a tikzcd is missing the supplied ampersand replacement option')
    return {'file':q.name,'status':'PASS' if not errors else 'FAIL','errors':errors,'dollars':dollars,'commands':sorted(cmds),'marks':{c:counts[c] for c in ['unsure','illegible','deleted']}}

def main():
    pages=sorted((OUT/'pages').glob('*.tex'))
    results=[check(q) for q in pages+[OUT/f'{ID}_transcription.tex',OUT/f'{ID}_standalone.tex']]
    errors=[e for r in results for e in r['errors']]
    assembly=(OUT/f'{ID}_transcription.tex').read_text()
    expected='\n'.join(q.read_text().rstrip()+'\n' for q in pages)
    if assembly!=expected:errors.append('assembly differs from page concatenation')
    if not assembly.startswith(r'\cotefile{157-4}') or assembly.count(r'\cotefile')!=1:errors.append('cotefile placement/count')
    if [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',assembly)]!=list(range(66,82)):errors.append('scan order')
    supplied=OUT.parents[2]/'upload'/'PREAMBLE(20261118-200556).tex'
    if not supplied.exists():errors.append('supplied preamble path missing')
    elif (OUT/'PREAMBLE.tex').read_bytes()!=supplied.read_bytes():errors.append('preamble differs from attachment')
    rows=list(csv.DictReader((OUT/f'{ID}_inventory.csv').open()))
    allowed_kinds={'text','letter part','display','diagram','drawing','margin note','insertion','deletion','handwritten'}
    for r in rows:
        if r['transcribed']!='yes' or r['sheet_kind'] not in {'text','letter','reused_typed','cancelled_draft','cover'} or r['kind'] not in allowed_kinds: errors.append(f'invalid/incomplete inventory row {r}')
    for q in pages:
        n=int(re.search(r'scan(\d+)',q.name).group(1));s=q.read_text()
        for macro,kind in [('deleted','deletion'),('inserted','insertion'),('diagram','diagram'),('margin','margin note')]:
            a=len(re.findall(r'\\'+macro+r'\b',s));b=sum(r['scan']==str(n) and r['kind']==kind for r in rows)
            if a!=b:errors.append(f'scan {n}: {macro} count {a} versus inventory {b}')
    totals={c:sum(r['marks'][c] for r in results[:len(pages)]) for c in ['unsure','illegible','deleted']}
    when=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    report={'checked_utc':when,'mode':'static checks; no TeX compilation','status':'PASS' if not errors else 'FAIL','pages':len(pages),'totals':totals,'inventory_rows':len(rows),'errors':errors,'files':results}
    (OUT/f'{ID}_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    lines=['# K157-4-05 — Static validation','',f'Checked: {when}', '', '**'+report['status']+'**. No TeX compilation was attempted.','',
           'Checks: braces; display delimiters; dollar parity; explicit inline-math delimiters; environment nesting; command whitelist; tikz-cd ampersand replacement; scan order; exact page concatenation; single initial cotefile; supplied preamble bytes; inventory metadata and correction/diagram/margin counts.','',
           '| File | Result | unsure | illegible | deleted |','|---|---|---:|---:|---:|']
    for r in results:lines.append('| '+r['file']+' | '+r['status']+' | '+' | '.join(str(r['marks'][c]) for c in ['unsure','illegible','deleted'])+' |')
    lines+=['',f'Page totals (not double-counting assembled copy): {totals}.', '', 'The check establishes source-level balance and recognized command names. It does not establish successful rendering, visual layout, or mathematical correctness.']
    if errors:lines+=['','## Errors','']+errors
    (OUT/f'{ID}_validation.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:report[k] for k in ['checked_utc','status','totals','inventory_rows','errors']},indent=2))
    if errors:raise SystemExit(1)

if __name__=='__main__':main()

"""Static checks requested by the task; deliberately does not run TeX."""
from pathlib import Path
import re, json, hashlib
from workflow import OUT,TASK,utc

ALLOWED=set('Rightarrow aleph alpha approx arabic arrow bar begin bigl bigr cdot circ coprod cotefile deleted diagram draw end epsilon exists figure forall geq handwritten illegible in inserted item joinrel ldots leq lhook longmapsto longrightarrow margin mathbf mathbb mathcal mathfrak mathrm mathscr mid mspage neq not operatorname overset phi pi qquad quad scanpage sharp sigma simeq subset subseteq substack supset tag text textcircled textsuperscript times uline underbrace underline underset unsure uuline varepsilon varinjlim varphi varprojlim widehat xrightarrow'.split())

def check(path):
    original=path.read_text();s=re.sub(r'(?<!\\)%[^\n]*','',original)
    errors=[];brace=0;env=[];math=None;tokens=re.finditer(r'\\[A-Za-z]+\*?|\\.|[{}$]',s,re.S)
    commands=set()
    for m in tokens:
        t=m.group();line=s[:m.start()].count('\n')+1
        if t.startswith('\\') and re.match(r'\\[A-Za-z]',t):
            name=t[1:].rstrip('*');commands.add(name)
            if name not in ALLOWED:errors.append(f'line {line}: unknown command {t}')
            if name in ('begin','end'):
                em=re.match(r'\{([^{}]+)\}',s[m.end():])
                if not em:errors.append(f'line {line}: missing environment name');continue
                e=em[1]
                if name=='begin':env.append(e)
                elif not env or env.pop()!=e:errors.append(f'line {line}: mismatched end {e}')
        elif t=='{':brace+=1
        elif t=='}':
            brace-=1
            if brace<0:errors.append(f'line {line}: negative brace depth')
        elif t=='\\[':
            if math is not None:errors.append(f'line {line}: display entered inside math')
            math='display'
        elif t=='\\]':
            if math!='display':errors.append(f'line {line}: display close mismatch')
            math=None
        elif t=='$':
            if math=='display':errors.append(f'line {line}: dollar inside display')
            else:math=None if math=='inline' else 'inline'
    if brace:errors.append(f'final brace depth {brace}')
    if env:errors.append(f'unclosed environments {env}')
    if math:errors.append(f'unclosed math {math}')
    if re.search(r'\\(?:newcommand|def|renewcommand)',s):errors.append('custom macro definition')
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?',s):
        if not m[1] or 'ampersand replacement=\\&' not in m[1]:errors.append('tikzcd missing ampersand replacement')
    return {'file':path.name,'pass':not errors,'errors':errors,'commands':sorted(commands),'counts':{k:s.count('\\'+k+'{') for k in ['unsure','illegible','deleted']}}

def run():
    pages=sorted((OUT/'pages').glob('*.tex'))
    results=[check(p) for p in pages];assembled=OUT/f'{TASK}_transcription.tex'
    expected='\n'.join(p.read_text().rstrip()+'\n' for p in pages)
    assembly_ok=assembled.exists() and assembled.read_text()==expected
    cote_ok=expected.startswith('\\cotefile{157-5}\n') and expected.count('\\cotefile{')==1
    report={'checked_utc':utc(),'method':'static token/brace/math/environment/explicit-command-whitelist check; no TeX compilation','pages':results,'assembly_matches_pages':assembly_ok,'single_initial_cotefile':cote_ok,'pass':all(r['pass'] for r in results) and assembly_ok and cote_ok,'total_counts':{k:sum(r['counts'][k] for r in results) for k in ['unsure','illegible','deleted']}}
    (OUT/'static_check_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='pages'},indent=2))
    for r in results:
        if not r['pass']:print(r['file'],r['errors'])
    if not report['pass']:raise SystemExit(1)

if __name__=='__main__':run()

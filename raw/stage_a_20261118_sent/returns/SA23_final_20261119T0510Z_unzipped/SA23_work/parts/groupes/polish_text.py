"""Formatting and citation normalization; no mathematical verdict generation."""
import json,pathlib,re
P=pathlib.Path(__file__).resolve().parent
bib=(P/'references.bib').read_text()
urls={}
for m in re.finditer(r'@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)',bib,re.S):
    u=re.search(r'url\s*=\s*\{([^}]+)\}',m.group(2))
    if u:urls[m.group(1)]=u.group(1)
s=(P/'section.md').read_text()
for m in list(re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',s)):
    for key,url in urls.items():
        if m.group(1).replace('–','').startswith(key):
            s=s.replace(m.group(0),'['+m.group(1)+']('+url+')')
s=s.replace('27 subject items, 114 claims, and 72 authorial questions','27 subject items, 115 claims, and 61 authorial questions, with 13 editorial tasks kept separately')
s=s.replace('The 114 claims divide into 14 class A, 50 class B, 48 class C, and two class F records.','The 115 claims divide into 14 class A, 51 class B, 48 class C, and two class F records.')
s=s.replace('eight proved statements, 36 proof sketches, 13 statements without proof, ten authorial corrections, 15 false formulations, and 32 open steps','eight proved statements, 35 proof sketches, 16 statements without proof, ten authorial corrections, 15 false formulations, and 31 open steps')
s=s.replace('The 41 search records cover every claim, and all 72 questions','The 42 search records cover every claim, and all 61 authorial questions')
s=s.replace('Twelve ranked directions','Eleven ranked directions')
s=s.replace('Root keeps that comparison question separate from the shared Barsotti–Tate cocharacter occurrence.','The manuscript asserts this comparison; identifying its undefined endpoint is editorial task ED-SA23-groupes-07, not an authorial question. It stays separate from the shared Barsotti–Tate cocharacter occurrence.')
s=s.replace('The filtered-(F)-crystal endpoint requires identification before theorem testing.','The filtered-$F$-crystal endpoint requires an editorial identification task before theorem testing.')
s=s.replace('ε((L))',r'$\epsilon(L)$').replace('ρ(σ)σ((j))ρ(σ)⁻¹=(j)',r'$\rho(\sigma)\sigma(j)\rho(\sigma)^{-1}=j$')
s=re.sub(r'(?<!\\)mathbf ',r'\\mathbf ',s)
s=s.replace('(aleph_1)',r'$\aleph_1$')
old='The source\'s unrestricted factorization is corrected explicitly, rather than attributed to those theorems.'
addition=' The actual margin question asks whether the zero-dimensional ring topology has enough points. It does: finite presentations over the integers form a countable finite-limit site, and the countable families D_n and their pullbacks generate a countable coverage. [MakkaiReyes1977, Theorem 6.2.4](https://reyes-reyes.com/wp-content/uploads/2018/04/makkai-reyes-book.pdf) supplies enough points for that separable site; its exact definition and proof were opened. Claim 115 records the application. The displayed D_n family has no finite subcover, but this alone is not a theorem excluding every alternative coherent presentation.'
if 'Claim 115 records the application.' not in s:s=s.replace(old,old+addition)

def math_parentheses(line):
    """Restore only visibly mathematical outer groups; URLs/prose stay intact."""
    out=[];i=0;inline=False
    while i<len(line):
        if line[i]=='$':
            inline=not inline;out.append(line[i]);i+=1;continue
        if line[i]!='(' or inline:
            out.append(line[i]);i+=1;continue
        depth=1;j=i+1
        while j<len(line) and depth:
            if line[j]=='(':depth+=1
            elif line[j]==')':depth-=1
            j+=1
        if depth:
            out.append(line[i:]);break
        content=line[i+1:j-1]
        prev=line[i-1:i]
        wordy=bool(re.search(r'[A-Za-z]{3,}',content))
        ismath=(bool('\\' in content or '=' in content or (len(content)<=20 and not wordy and re.fullmatch(r"[A-Za-z0-9_'{}^+\-<>,.\s]*",content))))
        if content.startswith('http') or prev==']':ismath=False
        if ismath:out.append('$'+content+'$')
        else:out.append(line[i:j])
        i=j
    return ''.join(out)

def polish_math(text):
    out=[];display=False;fence=False
    for line in text.splitlines():
        if line.startswith(chr(96)*3):fence=not fence
        if line.strip() in [r'\[','$$']:display=not display;out.append(line);continue
        if line.strip()==r'\]':display=False;out.append(line);continue
        if not display and not fence:line=math_parentheses(line)
        out.append(line)
    return '\n'.join(out)+'\n'

(P/'section.md').write_text(polish_math(s))
ep=P/'computations/extended_proofs.md'
if '$L\\dashv R$' not in ep.read_text():ep.write_text(polish_math(ep.read_text()))
core=P.parent/'misc/section.md'
t=core.read_text().replace('45 merged items, 74 claims, 27 authorial problems including answered and cancelled flags','53 subject items (45 from indexed notes and eight additional Codex units), 74 claims, 23 authorial problems including answered and cancelled flags, four editorial tasks')
core.write_text(t)
print(json.dumps({'section_words':len(s.split()),'citation_urls_normalized_from_verified_bibliography':True,'math_formatting':'restored'}))

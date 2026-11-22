"""Number independently audited conditional lemmas; no main gate is closed."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=w/'notes/post_CP28_dual_alternating_kernel_route.tex'
assert sha(source)=='4cd9c30f2115bbc7faee6f2624e1e1cbd1a76d72bb8d92a8daafd092901ddb9f'
audit=json.loads((w/'agents/monodromy/outputs/independent_dual_alternating_kernel_route_audit.json').read_text())
assert audit['source_sha256']==sha(source) and audit['status'].startswith('PASS')
history=w/'notes/root_routes29_before_integration';assert not history.exists();history.mkdir()
for rel in ['code/consolidate.py','code/prepare_checkpoint29.py','notes/root_references.bib',str(source.relative_to(w))]:
 p=w/rel;shutil.copy2(p,history/p.name)
t=source.read_text()
g=t.split(r'\paragraph{Full-radical generation.}',1)[1].split(r'\paragraph{Differential of the left-kernel map.}',1)[0]
gs,gp=g.split(r'\emph{Proof.}',1)
gp,gscope=gp.split('\nThe hypothesis is generation',1)
gscope='The hypothesis is generation'+gscope
d=t.split(r'\paragraph{Differential of the left-kernel map.}',1)[1].split(r'\paragraph{The rank inference that is not allowed.}',1)[0]
ds,dp=d.split(r'\emph{Proof.}',1)
dp,cp=dp.split('\nIn particular, if',1)
cp='In particular, if'+cp
x=t.split(r'\paragraph{The rank inference that is not allowed.}',1)[1].split(r'\paragraph{Exact geometric status.}',1)[0]
xs,xp=x.split('This is alternating.',1);xp='This is alternating.'+xp
scope=t.split(r'\paragraph{Exact geometric status.}',1)[1].split('\nNo computation was executed',1)[0]
labels=['lem:root-full-radical-generation','prop:root-dual-kernel-differential','cor:root-dual-kernel-birational','ex:root-kernel-compression-countermodel']
status=r'\status{Proved; complete direct proof and independent mathematical audit passed.}'
def statement(env,title,label,body,proof):
 return '\\begin{'+env+'}['+title+']\n\\label{'+label+'}\n'+status+'\n'+body.strip()+'\n\\end{'+env+'}\n\\begin{proof}\n'+proof.strip()+'\n\\end{proof}\n'
result=r'''\subsection{Full radicals and the dual alternating kernel map}
These elementary statements are conditional tools. Their higher-degree
geometric hypotheses remain unproved; no additional monodromy group is
determined by this subsection.
'''
result+=statement('lemma','Generation by full hyperplane radicals',labels[0],gs,gp)+'\n'+gscope
result+=statement('proposition','The differential of the left-kernel map',labels[1],ds,dp)
cs=r'''In the setting of Proposition~\ref{prop:root-dual-kernel-differential},
suppose that $h$ is odd and that $B_{\ell_s}$ has rank $h-1$ at one
point of $\mathcal U$. Then $\kappa$ is birational.'''
result+=statement('corollary','A conditional birational kernel map',labels[2],cs,cp)
result+=statement('example','Generic section rank does not force kernel movement',labels[3],xs,xp)
result+='\n'+r'\paragraph{Exact geometric status.}'+'\n'+scope
result+=r'''
\paragraph{Primary comparison and verification scope.}
The Jacobian-dual method of Russo and Simis~\cite{RussoSimis2001Birational},
Theorem~1.4, Proposition~2.2 and Example~2.5, gives related conditional
birationality criteria. We read the original proof chain through
Lemma~1.1 and Proposition~1.2, as well as the complete indicated passages.
Their linear-type, presentation and rank hypotheses are not established
for the higher-degree Cartier family, so no such application is made.
The proofs above are direct. The complete independent proof audit is
retained with the original source hash; no numerical computation was
used for these four elementary statements.
'''
section=w/'sections/A_route_limitations_29.tex';assert not section.exists();section.write_text(result)
con=w/'code/consolidate.py';text=con.read_text()
needle="   out.write('\\n\\\\input{sections/A_route_limitations}\\n')"
assert needle in text
text=text.replace(needle,needle+"\n   out.write('\\n\\\\input{sections/A_route_limitations_29}\\n')",1)
con.write_text(text)
prep=w/'code/prepare_checkpoint29.py';text=prep.read_text()
needle='for rel in required:';assert needle in text
text=text.replace(needle,"required.append('sections/A_route_limitations_29.tex')\n"+needle,1);prep.write_text(text)
bib=w/'notes/root_references.bib';text=bib.read_text();assert '{RussoSimis2001Birational,' not in text
text+=r'''
@article{RussoSimis2001Birational,
 author={Russo, Francesco and Simis, Aron},
 title={On Birational Maps and Jacobian Matrices},
 journal={Compositio Mathematica},
 volume={126},
 number={3},
 pages={335--358},
 year={2001},
 doi={10.1023/A:1017572213947},
 url={https://doi.org/10.1023/A:1017572213947},
 note={Opened original publisher PDF on 19--20 November 2026. Read the introduction and complete Lemma 1.1 proof, pp.337--338; Proposition 1.2 with its proof and supplement, pp.339--340; Theorem 1.4 proof, p.341; Proposition 2.2 proof and condition (3), p.342; Example 2.5 complete argument, p.344. The cited linear-type and acyclicity dependencies are not all independently re-proved. Comparison only: the hypotheses are not established for the higher-degree Cartier family, and no monodromy theorem is imported.}
}
'''
bib.write_text(text)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in labels:
  writer.writerow([label,audit['actual_utc'],'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root/monodromy','targeted proof check','PASS: full independent elementary proof audit of source SHA '+sha(source)+'. Numbered integration changes presentation only; no geometric hypothesis or main-gate movement asserted.'])
record={'status':'PASS','actual_utc':now,'source':str(source.relative_to(w)),'source_sha256':sha(source),
 'section':str(section.relative_to(w)),'section_sha256':sha(section),'labels':labels,
 'preserved_inputs':str(history.relative_to(w)),
 'independent_audit':'agents/monodromy/outputs/independent_dual_alternating_kernel_route_audit.json',
 'scope':'Four direct elementary statements with complete independent audit; conditional geometric route only. Bibliographic scope updated after actual original proof reading.'}
out=w/'outputs/root_routes29_integration.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

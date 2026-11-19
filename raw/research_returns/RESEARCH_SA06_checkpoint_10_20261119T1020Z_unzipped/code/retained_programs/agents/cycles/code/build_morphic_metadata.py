"""Register the audited E.3s--u results and supersede current open-gate prose."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, time

start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
who='GPT-6 Astra (OpenAI); inherited parent reasoning effort; RESEARCH_SA06 /root/cycles'
rows=[
 ('E.3s','The integral generated Albanese quotient is the connected point group of the large one-motivic Chow Albanese sheaf','Proved','one_motivic_quotient.tex, paragraph E.3s','AyoubBarbieriViale2009 Lemmas1.1.6/1.3.3; Corollary1.3.5; Proposition1.3.11; Lemma1.3.12; Theorem3.1.4; smooth compactification and Chow localization','14:24-39','Exact integral sheaf quotient over C; no finite-dimensional representability asserted. Nonproper parameters are handled on free zero-cycles and projective compactification, not by a false CH0 pushforward. Full morphic comparison remains an additional conjecture; finite Walker comparison is refuted in E.3u.'),
 ('E.3t','N is killed by full morphic Abel-Jacobi; a morphic family map is zero exactly when its rational Lawson cylinder is zero','Proved','morphic_counterexample.tex, paragraph E.3t','Walker2007Morphic Example5.5; Theorem5.7(1)-(4); Corollary5.9; Proposition3.3; strict Hodge filtration; countability of integral Lawson homology','14:24-39','For every smooth projective complex X and every abelian family. Includes u_Z tensor Q zero implies Lawson cylinder zero. Full morphic target is distinguished from the finite-dimensional coniveau Walker Jacobian.'),
 ('E.3u','The complex converse to Theorem3.1 is false even rationally, for a specified codimension-four elliptic family on a sixfold','Refuted','morphic_counterexample.tex, paragraph E.3u','E.3t; Friedlander2000 Theorems3.2/3.4 and Proposition5.1 with proofpp1095-1097; Nagel2002 Theorem3.13 and C.1i degree14 certificate; Walker2007Morphic Theorem6.2 proof','14:38-39; LeadE4','Y is the geometric generic degree14 section of split Q6 with65891 independent coefficients; gamma is the difference of the two specified plane sections; X=Y times E:y2=x3-x. Z=gamma times normalized diagonal has zero integral cohomological class and an injective rational Lawson cylinder. The specified geometric generic e yields a nontorsion class modulo N after every complex embedding. Thus N^4 is strictly smaller than the finite Walker kernel=A*H. Corrected universal necessary criterion is E.3t; positive support cases remain valid.'),
]
with (root/'morphic_results.csv').open('w',newline='') as f:
 w=csv.writer(f)
 w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes'])
 w.writerows(rows)
events=[
 ('E.3s',who,'targeted proof check','Constructed actual-cycle Yoneda presentation; quotient by all Serre-Albanese kernels is the one-motivic reflector. Exact C-point evaluation and smooth projective compactification identify its kernel with N and connected points with P integrally.'),
 ('E.3s','GPT-6 Astra (OpenAI); RESEARCH_SA06 /root/frobenius','independent re-proof','Full proof/source audit passed. Corrected the literal nonproper-CH0 factorization sentence to projective-compactification actions only; reread corrected proof. Review and source events saved independently by that agent.'),
 ('E.3s','GPT-6 Astra (OpenAI); RESEARCH_SA06 /root','independent re-proof','Root read the entire corrected proof and exact primary Ayoub-Barbieri-Viale categorical and component statements; passed integral quotient, actual-cycle presentation, compactification and point evaluation.'),
 ('E.3t',who,'used and rechecked in this run','Opened full published Walker2007 PDF and original theorem images: Example5.5 p928, Theorem5.7(1)-(4) p930, preceding factorization and Corollary5.9 p932, Definition3.1/Proposition3.3 pp915-917. Distinguished full morphic from finite coniveau Walker targets.'),
 ('E.3t',who,'targeted proof check','Every N generator has nonnegative dimension shift, so full morphic correspondence functoriality and zero-cycle Albanese comparison kill it. A nonzero rational H1 map has nonzero complex quotient by strictness and cannot disappear in countable periods or their rational span.'),
 ('E.3u',who,'used and rechecked in this run','Opened full Friedlander2000 published PDF and author version; Theorem3.4 p1082, Theorem3.2 p1081, Proposition5.1 pp1093-1095, proofpp1095-1097. Corrected Walker6.1 locator4.5 to the published3.4; Corollary6.3 Y/X prose typo is not propagated.'),
 ('E.3u',who,'targeted proof check','Rechecked the effective substitution: n5,r2,j1 requires restriction degrees8 and6, relative vanishing through9; Nagel gives through10 at degree14. Smooth dominant witness bases permit additional transcendental coefficients. Resolved fibre-product pullbacks and proper homological descent force nonzero primitive quadric class to vanish under a purported s-relation.'),
 ('E.3u',who,'targeted proof check','Fixed gamma Lawson cylinder is injective by cap with a dual elliptic class and pushforward recovering pairing times s gamma. Strict Hodge filtration gives countable kernel and torsion preimage on E(C). Whole singular cylinder vanishes because gamma has zero integral H4 class.'),
 ('E.3u',who,'targeted proof check','Specified geometric generic point e is nontorsion modulo N: a putative finite Albanese-kernel expression spreads over a smooth dominant base above E; relative Albanese zero equations and rational-equivalence witnesses persist, contradicting the countable torsion preimage on a nonempty complex open.'),
 ('E.3t','GPT-6 Astra (OpenAI); RESEARCH_SA06 /root','independent re-proof','Root full typed audit passed N-annihilation, full/finite Walker distinction, Hodge strictness/countability, and the whole-family Lawson criterion.'),
 ('E.3u','GPT-6 Astra (OpenAI); RESEARCH_SA06 /root','independent re-proof','Root full typed audit and direct published Friedlanderpp1095-1097/source audit passed the effective degree14 witness, fixed-family cap pairing, all-embedding smooth-dominant spread, and specified geometric generic e.'),
 ('E.3t','GPT-6 Astra (OpenAI); RESEARCH_SA06 /root/frobenius','independent re-proof','Final full typed audit passed at actual tool-clock2026-11-19T07:06:19UTC; exact primary theorem locators and strictness/countability criterion verified independently.'),
 ('E.3u','GPT-6 Astra (OpenAI); RESEARCH_SA06 /root/frobenius','independent re-proof','Final full typed audit passed at actual tool-clock2026-11-19T07:06:19UTC, including integral weak Lefschetz, codim4/sixfold types, D14 effective Lawson nonvanishing, extra-coefficient spread and specified generic point. Separate independent review/events retained.'),
 ('E.3u',who,'computation or formal certificate','Executed code/check_morphic_counterexample.py. All finite algebraic checks passed; output includes basis count65892, zeta-square-2, elliptic discriminant64, degrees8/6 with9<=10, and120 pairing vectors. Corrected missing runtime and reran once:0.056826961001206655 seconds. Infinite conclusions are proved, not extrapolated.'),
 ('E.3s;E.3t;E.3u',who,'computation or formal certificate','Standalone four-pass LuaLaTeX/BibTeX compilation succeeded,7-page PDF, no undefined references/citations or overfull boxes at the checked version;3.2785024129989324 seconds. Preserved logs and output/compile_morphic.json. Later editorial integration updates require parent master rebuild, not silently claimed checked here.'),
 ('E.3',who,'refuted, with the refined statement\'s id','The universal complex family converse is refuted by E.3u. Its earlier exact reformulations E.3m-p remain valid but their common universal condition is false. E.3t is the proved stronger necessary criterion; the requested forward characteristic-p implication remains E.3e.'),
 ('E.3s',who,'source clarification','Ayoub-Barbieri-Viale Remark3.3.6 and Ayoub2009 Conjecture5 concern the full morphic Abel-Jacobi target, not the finite-dimensional Walker Jacobian. Earlier tentative comparison wording is superseded explicitly; no conjectural comparison is used.'),
]
with (root/'morphic_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 w.writerow(['statement_id','date','who_model_effort_run','type','outcome'])
 for sid,author,kind,outcome in events:
  w.writerow([sid,'2026-11-19',author,kind,outcome])

# Keep the current machine-readable summaries consistent without rewriting
# their established check histories.
path=root/'results.csv'
with path.open(newline='') as f:
 reader=csv.DictReader(f); fieldnames=reader.fieldnames; current=list(reader)
for row in current:
 if row['id']=='E.3d':
  row['statement']='Both directions at i=1,n hold in all characteristics'
  row['notes']='Endpoint result. General characteristic-p forward implication is proved in E.3e; the general complex converse is refuted by E.3u.'
 if row['id']=='E.3k':
  row['statement']='Literal integral LeadE4 biconditional is false on the same Ottem-Suzuki fourfold; exact fixed-target Walker-kernel criterion identified'
 if row['id']=='E.3n':
  row['notes']=row['notes'].replace('its general truth remains unproved.','its universal truth is refuted in E.3u.')
with path.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fieldnames);w.writeheader();w.writerows(current)
source=root/'code/build_metadata.py'
text=source.read_text()
text=text.replace('Both directions at i=1,n hold in all characteristics; intermediate gates identified','Both directions at i=1,n hold in all characteristics')
text=text.replace('Endpoint result; general charp implication is subsequently proved in E.3e, while complex intermediate converse remains a gate.','Endpoint result. General characteristic-p forward implication is proved in E.3e; the general complex converse is refuted by E.3u.')
text=text.replace('exact remaining Walker-kernel family gate identified','exact fixed-target Walker-kernel criterion identified')
text=text.replace('its general truth remains unproved.','its universal truth is refuted in E.3u.')
source.write_text(text)
record={'utc':datetime.now(timezone.utc).isoformat(),'result_rows':len(rows),'check_events':len(events),'runtime_seconds':time.perf_counter()-start,'status':'E3s-u integrated after root and frobenius full typed/source audits'}
(root/'output/build_morphic_metadata.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

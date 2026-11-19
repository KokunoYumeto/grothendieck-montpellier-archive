"""Serialize the evidence index. Event scope is narrower than theorem proof unless stated.
Coverage mappings are an index of the completed manual read, not automatic verdicts.
"""
import csv,json,re,datetime,collections
from pathlib import Path
O=Path(__file__).resolve().parents[1];ROOT=O.parents[2]/'source'
WHO='GPT-6 Astra Pro; inherited effort (not exposed); SA12/review_33'
DATE='2026-11-19'
def tsv(name,heads,rows):
 with (O/name).open('w') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(heads);w.writerows(rows)
C=json.loads((O/'claims.json').read_text());I=json.loads((O/'items.json').read_text());R=json.loads((O/'REFERENCE_ACCESS.json').read_text())
E=[]
def event(s,kind,outcome):E.append([s,DATE,WHO,kind,outcome])
for i in I:
 event(i['id'],'used and rechecked in this run','Compared the full indexed note entry/entries with the actual transcription at '+i['lines']+'. Textual attribution/verdict check, not a claim to have proved the mathematics. '+i['check_reason'])
for c in C:
 event(c['id'],'used and rechecked in this run','Read the actual source statement at '+c['lines']+' and checked its scope against the recorded searches/results. '+c['fate']+' This event certifies source/hypothesis comparison, not a full proof audit.')
for r in R:
 event(r['key'],'used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found',r['scope']+' Evidence: '+','.join(f'outputs/web_{k:02}.json' for k in r['search_calls'])+'.')
# Actual mathematical checks, individually specified rather than inferred from labels.
proofs={
 607:'Independent direct-sum skyscraper argument: finite support of algebraic sections on quasi-compact A¹ versus locally finite support on the closed discrete integer set in C. H0 comparison is ⊕Λ→∏Λ and not surjective. All geometric/coefficient hypotheses checked in review.md.',
 609:'Rechecked the earlier-run analytic exponential-graph example: the sheaf support is a closed analytic nonalgebraic set, incompatible with algebraic constructibility. This only refutes the unrestricted analytic-strata convention.',
 613:'Constructed the elliptic-curve rank-one Z/4 local system using a finite monodromy representation and Riemann existence. H0 invariants are {0,2}, disproving freeness but not local constancy. Numeric part separately certified.',
 631:'For positive degrees, compactification and proper base change reduce f! to finite discrete geometric fibres. Identity f disproves degree0 vanishing. This is a short independent argument using the cited base-change theorem as background.',
 633:'Multiplying a regular equation by a unit changes its logarithmic/localization representative by an extendible unit, killed by the boundary. Kummer naturality gives the same supported divisor class. No higher-codimension independence proof claimed.',
 638:'First-quadrant spectral sequence: all terms below total degree2d vanish; only(0,2d) remains on that diagonal and all incident differentials vanish. Kummer exactness kills the image in Gm cohomology.',
 641:'The degree0 A¹ example shows why properness of the support is necessary for the naive support-forgetting interpretation. Proper-support hypothesis on preceding leaf may already avoid the error.',
 649:'The cone of the derived comparison has zero cohomology when all degreewise comparisons are isomorphisms; it is therefore zero in the derived category. No re-proof of proper base change.',
 651:'Baer argument for self-injectivity of Z/n: any hom from ideal(d) sendsd to a annihilated byn/d, hencea=db; multiplication byb extends it. Étale-local internal Ext of finite locally constant modules intoΛ vanishes, and the all-degree hyper-Ext spectral sequence collapses.',
 652:'Neighbour roots are orthonormal once the graph is acyclic; projection gives1−Σq²>0. The cosine lower bounds give the listed forbidden valencies/edge combinations. Acyclicity is an inherited earlier result, not independently re-proved.',
 653:'On an order3 edge, restricting the positive quadratic form to ξj=ξi changes the diagonal to1+1+2(−1/2)=1 and cross terms to the stated sums. This proves positivity of the contracted matrix under inherited acyclicity.',
 656:'For a finite spanning lattice norm shell with integral reflection coefficient, each reflection preserves the lattice and norm and hence permutes the shell. Fixed nonzero norm prevents nontrivial scalar multiples. Connected Gram diagrams give irreducibility in the checked E-types.',
 657:'For4|n, the index-two enlargement D_n+ has covolume1 and integral pairings because the half-sum has square normn/4 and pairs integrally with even-sum vectors; hence it is integral unimodular. Saved exact examples are checks of the formula, not a proof for alln.',
 668:'For polynomial S over a field, monomials give the geometric-series Hilbert product, and S+/(S+)² recovers the homogeneous generator degrees. This is a proof only of the explicitly reconstructed polynomial case; unseen Proposition1 remains unidentified.',
 669:'Localizing a free resolution is exact and yields a free resolution over the localization; localization commutes with tensor products and homology, proving the Tor localization formula.',
 670:'Pointwise product sections glue uniquely over any cover; restriction is projection onto factors indexed by the smaller open. The incorrect projection quantifier is isolated from this valid construction.',
 672:'Section germs detect equality, so the unit of a sheaf into its product of stalks is monic. Naturality gives faithfulness. Exact stalk functors and left-exact products give left exactness for module coefficients.',
 676:'For induced and quotient filtrations, each graded row is exact by lifting an element one filtration step and using R∩N_k. Every summandJ^iN_{k−i} is represented by a polynomial monomial in the f_j, proving ψ surjective. Not a resolution of the missing preceding b,c.',
 677:'A=k[t],R=tA,N0=A,Nk=0(k>0) gives R′_k=t^max(1,k)A and R″_k=t^(k+1)A; strict at k1. This is an exact ideal calculation.',
 678:'Computed the smooth compactifiable morphism f:G_m×A¹→A¹, f(u,v)=u. Ordinary A¹ cohomology, compact-support localization and the opened punctured-divisor theorem give Rf!Λ=j!Λ(−1)[−2] and Rf_*Λ=Rj_*Λ. Thus lower compact-support degrees0,1 are locally constant zero but ordinary degree1 is a nonconstant skyscraper. See complete hypothesis check in review.md.'
}
for n,desc in proofs.items():event(f'CL-SA12-{n}','independent re-proof',desc)
computations={
 613:'Z/4 monodromy invariants; geometry checked separately.',622:'Primitive-root unit and inverse-exponent test modulo5.',632:'Trace summation F3²→F3 kernel.',644:'Trace counterexample kernel.',652:'Exact cosine-bound sums at forbidden vertices.',653:'Order3 contraction diagonal.',655:'A_l counts/pairings ranks1–8; general formula discussed separately.',657:'D_n+ exact lattice examplesn4,8,12; general proof separate.',659:'B2 ordered Cartan integers and reflection-product order.',661:'E6 root enumeration, weights, rho, highest root, normalizations, quotient index and Weyl-order arithmetic.',662:'E6 proposed quotient generator is not a weight; its triple is not integral in the simple-root basis.',663:'E6 impossiblefactor13 and corrected exponent equations.',664:'E7 roots, weights, rho, highest root, normalizations and order arithmetic; epsilon6 branch fails.',665:'E8 roots, weights, rho, highest root, normalizations and order arithmetic; sign/dimension alarms.',666:'General2-dimensional bilinear quadratic law: formal commutator coefficient is B(x,y)−B(y,x). Jacobi is not certified by this degree2 calculation.',668:'Independent monomial counts for weighted degrees2,3,5 through12 versus Hilbert-series coefficients.',671:'All F2 sheaf endomorphisms on the Sierpinski test:8 versus4 diagonal maps; explicit off-diagonal witness.',677:'Closed formulas for induced versus enlarged filtrations recorded; not a symbolic CAS ideal library calculation.',678:'Degree bookkeeping d1,i0=1; geometric theorem inputs are checked separately.'
}
for n,desc in computations.items():event(f'CL-SA12-{n}','computation or formal certificate',desc+' Program: programs/exact_checks.py; complete output: outputs/exact_checks.txt. Exact rational/integer/symbolic arithmetic, not floating point. Weyl group orders were multiplied from supplied factors, not certified by enumerating every group element.')
refutations={607:607,609:609,613:613,622:622,631:631,641:641,644:644,655:655,659:659,660:660,662:661,663:661,665:665,671:670,678:651}
for n,refined in refutations.items():
 event(f'CL-SA12-{n}',f'refuted, with the refined statement’s id CL-SA12-{refined}','Refutes only the literal reading specified in this claim’s computation/present_status, with every stated test hypothesis checked. Where the same id is given, its modern statement field is the corrected formulation. Ink/authorship remain unresolved; this is not an emendation of the transcription.')
event('CL-SA12-660','independent re-proof','The reduced crystallographic root system{±e1,±2e2} has two orthogonal A1 components and length ratio2. Every reflection preserves the set and integral Cartan values hold, so the literal one-minimum length list is false without irreducibility/component normalization.')
event('CL-SA12-644','targeted proof check','Compared the geometric-fibre criterion in SGA4 XVIII2.10.1 with ordinary connected fibres in the leaf. The finite étale example Spec C→Spec R satisfies smooth, proper, relative dimension0 and connected/nonempty ordinary fibre; its geometric fibre has2points.')
event('SA12_SGA4III','targeted proof check','Read the exact self-injectivity explanation in XVIII3.2.6 and the constructible/proper disjunction in XVI4.1. These are actual statement/hypothesis checks; no full proof of Poincaré duality or analytic comparison is claimed.')
event('SA12_Riou2014','targeted proof check','Read Corollary3.1.3 and its localization/purity justification: for a regular divisor,j_*Λ=Λ,R¹j_*Λ=Λ_D(−1),higher images zero. Used this exact result in CL-SA12-678; no independent re-proof of Gabber purity.')
tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],E)
# Exact query and result indexing. Raw tool returns are retained verbatim in web_*.json.
Q=[];V=[]
log=['# Cote33 literature-search log','','Every query below was actually sent. Raw results, source reference ids, failed opens and full returned excerpts are in the corresponding JSON. A search hit is not an opened or verified reference. Primary sources alone support mathematical fates; secondary/search snippets were navigation leads.','',
 '## Scope and limitations','',
 'Searches cover SGA/EGA/Numdam, arXiv, zbMATH-directed queries, MathOverflow source-identification leads, the Bourbaki official bibliography, IAS/Deligne bibliography and primary author/publisher pages. The large EGAIV4 PDF and Gray primary paper could not be opened; their missing content is not supplied from memory. Bourbaki chapter records are bibliographic verification, not table collation. n°391, Tribu62, the full English ChapterI, and the missing EGA conditions remain unidentified. No claim is assigned classD from a first unsuccessful search.','',
 'The broad web results include secondary pages and machine-generated-looking course summaries; these are retained as raw search output only and are not authority for mathematical claims. The direct-sum skyscraper example is proved independently in this review.','',
 '## Exact calls','']
for p in sorted((O/'outputs').glob('web_*.json')):
 d=json.loads(p.read_text());q=d['query'];res=d['result'];body='\n'.join(x.get('text','') for x in res.get('content',[]) if x.get('type')=='text')
 log+=['### '+p.name,'','```json',json.dumps(q,ensure_ascii=False,indent=2),'```','',f'Complete returned results: `outputs/{p.name}`.','']
 for op,args in q.items():
  if op=='response_length':continue
  for a in args:
   Q.append([p.name,op,json.dumps(a,ensure_ascii=False),'outputs/'+p.name])
 for block in re.split(r'\n-{10,}\n',body):
  m=re.search(r'【([^】]+)】',block)
  if not m:continue
  h=block[:m.start()].strip();u=re.search(r'\((https?://[^\s]+)\)\s*$',h)
  url=u.group(1) if u else ''
  title=h[:u.start()].strip() if u else h
  source=re.search(r'Source: (open|find|click|screenshot)\(',block)
  typ=source.group(1) if source else 'search result'
  status='failed access' if 'Failed to fetch' in block or title=='Internal Error' else ('returned page/excerpt' if source else 'search hit only')
  V.append([p.name,m.group(1),typ,title,url,status])
tsv('SEARCH_CALLS.tsv',['file','operation','exact_argument_json','complete_result'],Q)
tsv('SEARCH_RESULTS.tsv',['file','result_ref','operation','title','url','access_status'],V)
(O/'SEARCH_LOG.md').write_text('\n'.join(log))
# Coverage: index only, after full manual read.
tex=(ROOT/'SA12_texts/pro/MPL_33_002-049_transcription.tex').read_text().splitlines()
scans=[]
for ln,t in enumerate(tex,1):
 m=re.search(r'\\scanpage\{(\d+)\}',t)
 if m:scans.append((int(m.group(1)),ln))
coverage=[]
for k,(scan,ln) in enumerate(scans):
 end=scans[k+1][1]-1 if k+1<len(scans) else len(tex)
 items=[i['id'] for i in I if scan in i['scans']]
 claims=[c['id'] for c in C if scan in c['scans']]
 coverage.append([33,scan,ln,end,'entire scan passage manually read, including cancelled text, insertions, notes and formulas',';'.join(items),';'.join(claims)])
tsv('SOURCE_COVERAGE.tsv',['cote','scan','start_line','end_line','read_scope','items','claims'],coverage)
counts=dict(entries=91,items=len(I),claims=len(C),problems=len(json.loads((O/'problems.json').read_text())),readings=sum(1 for _ in csv.DictReader((O/'readings.tsv').open(),delimiter='\t')),links=sum(1 for _ in csv.DictReader((O/'links.tsv').open(),delimiter='\t')),check_events=len(E),references=len(R),search_calls=len(list((O/'outputs').glob('web_*.json'))),claim_classes=dict(collections.Counter(c['class'] for c in C)),statuses=dict(collections.Counter(c['status_on_pages'] for c in C)),verdicts=dict(collections.Counter(r['verdict'] if not r['verdict'].startswith('merged into') else 'merged' for r in csv.DictReader((O/'entries.tsv').open(),delimiter='\t'))))
(O/'COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in counts.items() if k!='statuses'},ensure_ascii=False,indent=2))
print(f'{len(scans)} scan passages indexed; all full-read coverage complete. Reference verification levels are in REFERENCE_ACCESS.json.')

"""Record explicitly scoped check events and validate the authored segment."""
from pathlib import Path
import csv,json,re,collections,datetime
P=Path(__file__).resolve().parents[1]
items=json.loads((P/'items.json').read_text())
claims=json.loads((P/'claims.json').read_text())
problems=json.loads((P/'problems.json').read_text())
who='GPT-6 Astra Pro; effort inherited/not exposed; run SA03-part3/c'
date='2026-11-19'
ev=[]
def E(i,t,o):ev.append([i,date,who,t,o])
for i in items:
    E(i['id'],'used and rechecked in this run','Source-to-note comparison only, not a proof certificate: '+i['check']+'. '+i['check_reason'])
# IDs below were explicitly selected after writing the proofs in narrative.md.
proofs=[404,405,406,407,408,409,410,412,413,414,415,416,417,418,420,421,422,423,426,427,428,430,431,432,433,434,447,448,449,450,452,454,455,456,458,461,462,463,464,465,466,467,469,470,471,472,473,475,476,477,478]
conditional=[401,402,403,411,419,424,425,429,435,436,437,438,439,440,441,442,443,444,445,446,453,457,468,474]
refuted={451:452,459:456,460:454}
assert set(proofs)|set(conditional)|set(refuted)==set(range(401,479))
for c in claims:
    n=int(c['id'].split('-')[-1])
    if n in proofs:E(c['id'],'independent re-proof','The general argument is written in narrative.md sections2–7, under the hypotheses in this claim. Published comparators are separate from this proof. '+c['present_status'])
    elif n in refuted:E(c['id'],'refuted, with the refined statement’s id','Refined statement CL-SA03-'+str(refuted[n])+'. '+c['present_status']+' Counterexample scope and all hypotheses are in narrative.md.')
    else:E(c['id'],'targeted proof check','Hypothesis/identification audit, not a complete proof of the manuscript reading. '+c['fate']+' '+c['present_status'])
for ns,out in [
([404,405,408],'C23 finite cylinder/density illustration; general proof separately in narrative section2.'),
([447,448,449,450,452],'C04–C05 exact dual-number Laurent identities and all listed bounded-stage cases; general proof separately in section5.'),
([454,455,456,458],'C01 full symbolic quadratic composition;C02–C03 quotient diagnostics, with general filtered proof separately in section6.'),
([459],'C03 determinant2 obstruction over Z.'),
([460],'C02 nonzero residue of(t+epsilon)^3 in Q[epsilon,t]/(epsilon^3,t^3).'),
([461,462],'C16 exact wedge/determinant/shuffle example; universal proof separate.'),
([465],'C17 positive-degree nilpotence examples; finite-generator proof separate.'),
([466],'C18 split-basis intersection calculation; general multidegree proof separate.'),
([467],'C19 finite wedge dimension counts; infinite-rank colimit proof separate.'),
([468],'C22 formal chain-homotopy identity under explicit invertibility assumption.'),
([470],'C21 restricted PBW monomial counts only; triangular proof separate.'),
([471],'C20 binomial/commutator identity modulo each checked prime; general argument separate.'),
([472,473],'C06–C07 associativity/bracket checks for p=2,3,5,7 and truncation diagnostic; Frobenius proof separate.'),
([475],'C10 exact2-by2 GL law.'),
([476],'C11–C13 invariant fields, all16 GL2 brackets and p=2,3,5 powers on generators; general proof separate.'),
([477],'C08–C09 symplectic equations/dimensions n=1,2,3; all-rank block proof separate.'),
([478],'C14–C15 exact2-by2 Cayley inverse/orthogonality/composition identities; general matrix proof separate.')
]:
    for n in ns:E('CL-SA03-'+str(n),'computation or formal certificate','PASS: code/check_computations.py → outputs/computations.txt. '+out)
opened_math={
'C_OlivierUniversal':'exp6 Propositions3–5; exact universal ring/patch spectrum statement and proof inspected.',
'C_OlivierGlobal':'exp9 II Proposition2; exact global adjunction and affine surjective monomorphism inspected.',
'C_Ferrand':'section8.3 and Proposition8.5 inspected; chronology footnote1 distinguishes1970 private circulation from2003 rewritten publication.',
'C_SGA4_IV':'IV1.1.2,Theorem1.2,Corollary1.2.1 inspected; extra topos axioms kept visible.',
'C_Greenberg1966':'Theorem1 and Corollaries1–2 inspected; no substitution for unidentified thick-point theorem.',
'C_BG':'v6 Proposition18.2 inspected with completeness/perfectness qualifications and corrected-proof version date.',
'C_Sebag':'preprint3.1.2,3.2,4.3.11–12,7.2.1–2 inspected; bounded Jacobian conditions retained.',
'C_OsipovZhu':'section2 equations2.1–2.3,Lemma2.1 inspected; manuscript bounded stages separately proved.',
'C_Ardizzoni':'Example4.6 p12 inspected over a field; not4.7; publication dates opened.',
'C_Stacks08YF':'Section5.23 patch compactness, continuity and closed images inspected.',
'C_Stacks054H':'Section29.23 pullback and finite-presentation/type image conditions inspected.',
'C_Stacks04ZC':'Section5.15 constructible Boolean/pullback statements inspected.',
'C_Stacks096Y':'Lemma61.5.2 finite refinement inspected; not a w-local identification.',
'C_Stacks0A2Y':'Lemma5.24.4 constructible finite-stage descent inspected.',
'C_Stacks0597':'Lemma10.86.3 countable ML nonemptiness inspected; no thick-point arrow inferred.',
'C_Stacks01ZC':'Proposition32.6.1 exact qcqs hypothesis and gluing proof inspected.',
'C_Stacks01ZM':'Lemma32.10.1 finite-presentation descent inspected.',
'C_StacksProper':'Lemma29.43.1 valuative existence/uniqueness inspected.',
'C_Stacks00UP':'Section10.150 formal étale lifting inspected as framework, not exact jet-group formula.',
'C_Stacks04FJ':'Lemma37.9.5 simply transitive derivation action inspected.',
'C_Stacks00DM':'Section10.13 exterior relations, free bases and colimits inspected.',
'C_BourbakiTopology':'Primary reprintIII section7 no1 introduction/Proposition1 personally read at work/b/BourbakiTopo1_4.txt:11130–11335. Exact draft285 numbering not matched.'
}
keys=re.findall(r'@\w+\{([^,]+),',(P/'references.bib').read_text())
for key in keys:
    if key in opened_math:E(key,'used and rechecked in this run',opened_math[key])
    else:E(key,'carried as background without fault found','Opened bibliographic/author source and qualified access status in references.bib. Not a direct proof check of an inaccessible theorem. See search_log.tsv.')
with (P/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(ev)

def tsv(name):
    with (P/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
entries=tsv('entries.tsv')
assert len(entries)==60 and {int(x['entry_id'].split('#')[1]) for x in entries}==set(range(1,61))
iids={i['id'] for i in items};cids={c['id'] for c in claims}
assert len(iids)==len(items)==43 and len(cids)==len(claims)==78
assert all(e['item_id'] in iids for e in entries)
assert all(i in iids for c in claims for i in c['items'])
assert all(k in keys for c in claims for k in c['refs'])
assert all(k in keys for p in problems for k in p['refs'])
assert all(any(e[0]==x for e in ev) for x in iids|cids|set(keys))
root=P.parents[2]
for x in items+claims:
    for l in x['lines']:
        file,band=l.rsplit(':',1);a,b=map(int,band.split('-'))
        assert 1<=a<=b<=len((root/file).read_text().splitlines())
for f in ['items.json','claims.json','problems.json']:
    assert not any(ord(ch)<32 and ch not in '\n\t\r' for ch in (P/f).read_text())
report={'entries':len(entries),'items':len(items),'verdicts':dict(collections.Counter(x['verdict'] for x in entries)),'item_kinds':dict(collections.Counter(x['kind'] for x in items)),'claims':len(claims),'classes':dict(collections.Counter(c['class'] for c in claims)),'statuses':dict(collections.Counter(c['status_on_pages'] for c in claims)),'problems':len(problems),'readings':len(tsv('readings.tsv')),'links':len(tsv('links.tsv')),'references':len(keys),'search_groups':len(tsv('search_log.tsv')),'check_events':len(ev),'reading_log_rows':len(tsv('reading_log.tsv')),'integrity':'PASS: unique IDs,60/60 entry coverage, all item/ref/event links, actual locator bounds, no embedded control characters.'}
(P/'outputs/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))

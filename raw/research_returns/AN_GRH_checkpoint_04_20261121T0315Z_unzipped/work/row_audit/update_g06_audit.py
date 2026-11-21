#!/usr/bin/env python3
"""Targeted G06 update; preserve source data, classifications and scope."""
from pathlib import Path
import csv, io, json, hashlib, copy
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/row_audit'
DATE='2026-11-21'
WHO='GPT-6 Astra Pro; effort not exposed; AN_GRH /root/row_audit'
OBJECT='F_a/Q: y^2=x^3-3x+a, a=6 or -6; j=-216; rad(2N_Fa)=6. The recovered proof then restricts rho_{F_a,ell} to its chosen finite number field L; A.33 explicitly reuses the same F_a and A.32 Serre argument.'
LFUN='The original qualitative Serre input and the unconditional Lombardo index refinement require no GRH L-function. The separate conditional G06.1-G06.2 refinement uses Dedekind zeta_M(s) for the actual finite auxiliary fields and avoidance composita in G-MW1/G-CHEB, supplied by trivial-character Hecke GRH over those fields; no Hasse-Weil L(F_a,s) hypothesis is used.'
ALP='Original qualitative openness and commutator Zariski density are already unconditional. Also unconditionally, the adelic index over L is <[L:Q]*exp(10^21483)*max{1,h_F(F_a)}^(4.8*10^10), by Lombardo over Q and restriction. The separate Mayle-Wang numerical mod-ell refinement is established here under H_M; it is not established from Dirichlet GRH alone.'
MAS='The original qualitative conclusion remains unconditional. Under H_M, for every prime ell>964*log(6)+5760, the mod-ell image over Q is GL_2(F_ell); after restriction to the actual L its index in GL_2(F_ell) is at most [L:Q]. This does not assert full GL_2(F_ell) image over L. The adelic Lombardo bound in the preceding column is unconditional.'
GAP='Descent to Q is explicit in the recovered models, so no descent gate remains. Numerical evaluation of the unconditional adelic bound requires the actual [L:Q] and stable Faltings height h_F(F_a). The bounds do not determine the exact restricted image; the source rows only require qualitative openness.'
EVIDENCE='Targeted source reread: A.32 explicitly defines F_a/Q and uses Serre after restriction to L; A.33 displays the same F_a and inherits that non-CM/Serre argument. The complete newly written G06 proof and G06_source_audit.md were read; discriminant, j, point counts and the image-index restriction argument were rechecked. Lombardo and Mayle-Wang are cited results, not independently re-proved here; no whole-proof certification of A.32 or A.33 is claimed.'
CLASSIFICATION='Original qualitative Serre input is unconditional. Actual factors descend to Q. G06 supplies the unconditional adelic bound <[L:Q]*exp(10^21483)*max{1,h_F(F_a)}^(4.8*10^10); under H_M it supplies full mod-ell image over Q for ell>964*log(6)+5760 and restricted image index at most [L:Q] over L, not full image over L.'
OLD_TEX=r'''LM8 A.32--A.33 need Serre's qualitative non-CM open-image theorem,
not an explicit index. An effective theorem for elliptic curves over
$\mathbb Q$ needs an actual descent to $\mathbb Q$ before it applies.
'''
NEW_TEX=r'''LM8 A.32--A.33 use Serre's qualitative non-CM open-image theorem;
their commutator Zariski-density conclusion was already unconditional.
The recovered proofs explicitly identify
$F_a/\mathbb Q:y^2=x^3-3x+a$, for $a=6,-6$, with $j=-216$;
the later choice of a number field $L$ is a restriction of this
representation. Thus there is no unresolved descent condition.
Finding G06 applies to these actual factors, for which
$\operatorname{rad}(2N_{F_a})=6$. Under $\mathrm H_M$, the mod-$\ell$
image over $\mathbb Q$ is $\operatorname{GL}_2(\mathbb F_\ell)$ for
$\ell>964\log6+5760$, and its restricted image over $L$ has index
at most $[L:\mathbb Q]$. Full image over $L$ is not asserted.
Independently of $\mathrm H_M$, the cited Lombardo theorem over
$\mathbb Q$ and the same restriction argument give
\[
 [\operatorname{GL}_2(\widehat{\mathbb Z}):\rho_{F_a,\infty}(G_L)]
 <[L:\mathbb Q]\,\exp(10^{21483})
       \max\{1,h_F(F_a)\}^{4.8\cdot10^{10}}.
\]
Here $h_F$ is the stable Faltings height in the cited theorem's
convention. These refinements do not change the original rows' status.

'''
OLD_NOTE="LM8 A.32 and A.33 use Serre's qualitative open-image theorem for a non-CM elliptic factor over its stated number field. No explicit index is required. An explicit theorem restricted to elliptic curves over Q cannot be applied without proving that the actual curve descends to Q. "
NEW_NOTE="LM8 A.32 and A.33 use Serre's qualitative open-image theorem and commutator Zariski density, already unconditionally. Their actual models are F_a/Q: y²=x³−3x+a, a=±6, with j=−216 and rad(2N)=6; the later number field L restricts these representations. Thus no descent gate remains. G06 gives, under H_M, full mod-ell image over Q for ell>964 log6+5760 and image index at most [L:Q] over L, without asserting full image over L. Unconditionally, Lombardo over Q and restriction give adelic index <[L:Q] exp(10^21483) max{1,h_F(F_a)}^(4.8·10^10), using the stable Faltings height. These numerical refinements do not alter the original qualitative conclusions. "
changes=[]
def save(p,data,extra=None):
 old=p.read_bytes()
 if old!=data:
  p.write_bytes(data)
  changes.append(dict(path=str(p.relative_to(ROOT)),sha256_before=hashlib.sha256(old).hexdigest(),sha256_after=hashlib.sha256(data).hexdigest(),**(extra or {})))
NAMES={'ROW_ANALYTIC_LEDGER.tsv':108,'ROW_ANALYTIC_CANDIDATES.tsv':108,'ROW_FULL_REGISTER_AUDIT.tsv':800,'ROW_FLAG_AUDIT.tsv':575,'ROW_UNIQUE_AUDIT.tsv':525}
for folder in (OUT,ROOT/'final'):
 for name,count in NAMES.items():
  p=folder/name
  reader=csv.DictReader(io.StringIO(p.read_text()),delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
  before=copy.deepcopy(rows); assert len(rows)==count,(p,len(rows)); altered=[]
  for row in rows:
   if row.get('run')!='LM8_PUSH' or row.get('row_id') not in ('A.32','A.33'):continue
   row['L_functions']=LFUN; row['evidence_scope']=EVIDENCE
   if 'exact_finite_field_or_object' in row:row['exact_finite_field_or_object']=OBJECT
   if 'under_Alpoge_Dirichlet_GRH' in row:
    row['under_Alpoge_Dirichlet_GRH']=ALP; row['under_Masullo_all_field_Hecke_GRH']=MAS; row['missing_theorem_or_data']=GAP
   else:
    row['classification']=CLASSIFICATION; row['missing_statement_or_data']=GAP
    row['evidence_scope']+=' recovered/LM8_PUSH_cp17_text/sections/A_nonstable_C3_fixed.tex:1'
   altered.append(row['row_id'])
  assert altered==(['A.33'] if name in ('ROW_FLAG_AUDIT.tsv','ROW_UNIQUE_AUDIT.tsv') else ['A.32','A.33']),(p,altered)
  allowed={'L_functions','evidence_scope','exact_finite_field_or_object','under_Alpoge_Dirichlet_GRH','under_Masullo_all_field_Hecke_GRH','missing_theorem_or_data','classification','missing_statement_or_data'}
  for old,new in zip(before,rows):
   delta={k for k in fields if old[k]!=new[k]}; assert delta<=allowed,(p,delta)
   if delta:assert old['run']=='LM8_PUSH' and old['row_id'] in ('A.32','A.33')
   if name in ('ROW_FLAG_AUDIT.tsv','ROW_UNIQUE_AUDIT.tsv'):assert all(old[k]==new[k] for k in fields[:12])
  s=io.StringIO(); w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)
  save(p,s.getvalue().encode(),dict(rows=count,updated_row_ids=altered))
for p in (OUT/'row_audit.tex',ROOT/'final/proof_sources/row_audit.tex'):
 text=p.read_text()
 if OLD_TEX in text:
  assert text.count(OLD_TEX)==1; save(p,text.replace(OLD_TEX,NEW_TEX).encode())
 else:assert NEW_TEX in text,p
p=OUT/'ROW_AUDIT_NOTES.md'; text=p.read_text()
if OLD_NOTE in text:
 assert text.count(OLD_NOTE)==1; save(p,text.replace(OLD_NOTE,NEW_NOTE).encode())
else:assert NEW_NOTE in text
p=OUT/'build_row_audit.py'; lines=p.read_text().splitlines(keepends=True)
ids=[i for i,s in enumerate(lines) if s.startswith("add('LM8_PUSH','A.32 A.33',")]; assert len(ids)==1
args=['LM8_PUSH','A.32 A.33','QUALITATIVE_SERRE_OPEN_IMAGE','Use openness of the non-CM elliptic Tate-module image and Zariski density of the commutator.',OBJECT,LFUN,ALP,MAS,GAP]
lines[ids[0]]='add('+','.join(repr(v) for v in args)+',evidence='+repr(EVIDENCE)+')\n'; save(p,''.join(lines).encode())
arithmetic=[]
for a in (6,-6):
 delta=-16*(4*(-3)**3+27*a*a); j=Fraction(1728*4*(-3)**3,4*(-3)**3+27*a*a)
 assert delta==-(2**9)*(3**3) and j==-216
 for p in (5,11):
  n=1+sum(1 for x in range(p) for y in range(p) if (y*y-x**3+3*x-a)%p==0); t=p+1-n
  expected={(6,5):(7,-1,-19),(6,11):(9,3,-35),(-6,5):(7,-1,-19),(-6,11):(15,-3,-35)}[a,p]
  assert (n,t,t*t-4*p)==expected
  arithmetic.append(dict(a=a,p=p,points=n,trace=t,frobenius_discriminant=t*t-4*p))
(OUT/'G06_ARITHMETIC_RECHECK.json').write_text(json.dumps(dict(date=DATE,who=WHO,discriminant=-(2**9)*(3**3),j=-216,point_counts=arithmetic),indent=2)+'\n')
assert (ROOT/'final/ROW_ANALYTIC_LEDGER.tsv').read_bytes()==(ROOT/'final/ROW_ANALYTIC_CANDIDATES.tsv').read_bytes()
rows=list(csv.DictReader((ROOT/'final/ROW_FULL_REGISTER_AUDIT.tsv').open(),delimiter='\t'))
reachable=sum(bool(r['recorded_dependency_paths']) for r in rows)
curated=list(csv.DictReader((ROOT/'final/ROW_ANALYTIC_LEDGER.tsv').open(),delimiter='\t'))
seeds=sum(r['analytic_dependency_seed']=='yes' for r in curated); assert reachable==201 and seeds==38,(reachable,seeds)
events=[
 ('LM8-A32-A33-G06-source-scope','used and rechecked in this run','PASS: reread the actual Q models, A.32 Serre application over L, and A.33 displayed factor and explicit reuse of A.32. Original qualitative openness remains unconditional; no claim to have re-proved all other steps of these rows.','recovered/LM8_PUSH_cp17_text/sections/A_nonstable_D3_fixed.tex; recovered/LM8_PUSH_cp17_text/sections/A_nonstable_C3_fixed.tex'),
 ('G06-targeted-whole-new-proof','used and rechecked in this run','PASS: read all of new G06 and its source-audit note; checked discriminant-minimality reasoning, substitution into the cited Mayle-Wang bound, the coset-index restriction inequality (also for non-Galois L/Q), and Lombardo over Q followed by restriction. The cited published theorems were not independently re-proved here. Literal product/exponent comma typos in the work G06.3 display were reported to its owner; corrected notation is used in the updated row section.','work/effective_galois/effective_galois.tex G06; work/effective_galois/G06_source_audit.md; final/proof_sources/row_audit.tex'),
 ('G06-concrete-model-arithmetic','computation or formal certificate','PASS: independent exact rational calculation gives j=-216 and discriminant -2^9*3^3 for both signs; direct point enumeration at 5 and 11 reproduces all four counts and Frobenius discriminants -19,-35. This supports the input arithmetic, not an independent proof of the CM-specialization theorem.','work/row_audit/update_g06_audit.py; work/row_audit/G06_ARITHMETIC_RECHECK.json'),
 ('G06-row-table-update-integrity','computation or formal certificate','PASS: five final TSVs retain 108,108,800,575,525 rows, respectively; only LM8 A.32/A.33 appended analytic-audit fields change. Original statements, statuses, dependencies and all 12 source flag columns are unchanged. Ledger/candidates remain identical; 201 dependency-path rows and 38 qualitative-prime seeds are unchanged. Updated entries expressly distinguish full image over Q from index at most [L:Q] over L.','work/row_audit/update_g06_audit.py; work/row_audit/G06_UPDATE_MANIFEST.json; final/ROW_ANALYTIC_LEDGER.tsv; final/ROW_ANALYTIC_CANDIDATES.tsv; final/ROW_FULL_REGISTER_AUDIT.tsv; final/ROW_FLAG_AUDIT.tsv; final/ROW_UNIQUE_AUDIT.tsv')]
with (OUT/'CHECK_EVENTS_G06_UPDATE.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n'); w.writerow(['statement_id','date','who_model_effort_run','type','outcome','evidence'])
 for ident,kind,outcome,evidence in events:w.writerow([ident,DATE,WHO,kind,outcome,evidence])
manifest=dict(date=DATE,who=WHO,changed_files=changes,counts={**NAMES,'dependency_path_rows':reachable,'qualitative_prime_seeds':seeds},scope='Only the requested final ROW TSVs and final/proof_sources/row_audit.tex were edited; corresponding work files and the original builder were synchronized. Other final files remain owned by root.')
(OUT/'G06_UPDATE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(changed_files=[x['path'] for x in changes],counts=manifest['counts'],check_events=len(events)),indent=2))

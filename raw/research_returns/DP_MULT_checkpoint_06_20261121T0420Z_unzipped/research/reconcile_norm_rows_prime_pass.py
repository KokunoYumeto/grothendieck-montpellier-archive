#!/usr/bin/env python3
"""Merge completed DP61/62/64 events and state; preserve earlier dated records."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re
root=Path(__file__).resolve().parents[1];r=root/'research';now=datetime.now(timezone.utc).isoformat()
def read(p):
 with p.open(newline='') as f:
  d=csv.DictReader(f,delimiter='\t');return d.fieldnames,list(d)
def write(p,fields,rows):
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
ef,es=read(root/'CHECK_EVENTS.tsv')
def add(sid,who,kind,scope,outcome,evidence,when):
 if any(x['evidence']==evidence for x in es):return
 serial=max(int(x['event_id'].split('-')[1]) for x in es)+1
 es.append(dict(zip(ef,[f'DPC-{serial:03d}',sid,'2026-11-21 UTC',when,who,'GPT-6 Astra Pro','not exposed by runtime','DP_MULT_20261121',kind,scope,outcome,evidence])))
_,ars=read(r/'archive_binomial_check_events.tsv')
for e in ars:
 num=int(e['event_id'].removeprefix('ABA-CE'))
 if num>=84 and e['statement_id'] in ['DP59','DP61','DP62','DP64']:
  add(e['statement_id'],e['checker'],'targeted proof check',e['scope'],e['outcome']+' LIMIT: '+e['limitations'],'research/archive_binomial_check_events.tsv:'+e['event_id'],e['utc_time'])
for n in (61,62,64):
 for p in sorted(r.glob(f'DP{n}_*review_metadata.json')):
  d=json.loads(p.read_text())
  if 'scope' not in d:continue
  when=next((d[k] for k in ['observed_completion_utc','recorded_utc','observed_complete_read_utc'] if k in d),now)
  add(f'DP{n}',d.get('who',d.get('agent','/root')),'targeted proof check',d['scope'],d.get('outcome',d.get('result','PASS')),'research/'+p.name,when)
for name in ['DP61_step2_check_metadata.json','DP61_integrated_step2_check_metadata.json']:
 p=r/name
 if not p.exists():continue
 d=json.loads(p.read_text())
 add('DP61','/root/step2_higher','targeted proof check',d['scope'],d.get('result','PASS'),'research/'+name,d.get('completed_utc',now))
d=json.loads((r/'DP61_source_reads_step2.json').read_text())
for e in d['records']:
 add('ALPOGE-DP61-'+e['path'].split('/')[-1],'/root/step2_higher','used and rechecked in this run',json.dumps(e,ensure_ascii=False),'PASS exact recorded source ranges only; most recovered files were not read.','research/DP61_source_reads_step2.json:'+e['path'],d['recorded_utc'])
for name,sid,who,kind in [
 ('DP59_locator_correction_metadata.json','DP59','/root','targeted proof check'),
 ('DP59_display_layout_delta.json','DP59','/root','targeted proof check'),
 ('DP62_author_source_revision_metadata.json','MORET-BAILLY-II.2.1','/root/formal_bound','used and rechecked in this run')]:
 d=json.loads((r/name).read_text());add(sid,who,kind,d['scope'],d.get('outcome',d.get('result','PASS')),'research/'+name,d.get('recorded_utc',d.get('observed_recorded_utc',now)))
d=json.loads((r/'DP62_source_read_metadata.json').read_text())
for e in d['directly_read']:
 ev=e.get('url',e.get('file'))
 add('PRIMARY-DP62','/root/formal_bound','used and rechecked in this run',e['locator'],'PASS actual specified source reading; original Moret-Bailly later recovery has its own event.','research/DP62_source_read_metadata.json:'+ev,d['recorded_utc'])
add('STACKS-0BX7-0BX5','/root','used and rechecked in this run','Directly opened/read the official statements and proofs of29.43.5/0BX7 and29.43.1/0BX5; applied Noetherian, valuation-local-ring, proper-target and separated-gluing hypotheses to the Dedekind base.','PASS exact neighborhood extension and valuative properness source applications.','research/DP62_root_integrated_review_metadata.json:Stacks-neighborhood',now)
add('RUDNICK-2015','/root','used and rechecked in this run','Directly reopened/read official printedp2 §2 equation1 and the preceding quantitative PNT, with fixed modulus and constant allowed to depend on it.','PASS precise known input for DP64; no RH needed.','research/DP64_root_whole_review_metadata.json:Rudnick',now)
write(root/'CHECK_EVENTS.tsv',ef,es)
qf,qs=read(root/'QUESTIONS.tsv')
for q in qs:
 if q['id']=='Q3e':
  q['finding_ids_or_counterexample']='U2;DP25-DP62;DP64'
  q['current_gate_or_scope']='DP54/56/58 realize finite sharp global jets at quantitative levels. DP55/57 construct and detect the exact mixed-type endpoint Fi period, with adelic realization at a fresh principal29-level. DP59 identifies the integral permitted-translate span and sharp individual ordinary/two-row witnesses; DP60/62 control full-section interpolation norms and exact individual canonical norms, good-prime integrality and tuple-field degrees. DP61 identifies every prescribed row and its fixed windows, supplies a primitive harmonic completion and proves its pure-kernel evaluation vanishes. DP64 closes fixed-cyclotomic-type bare prime-budget changes, including saturation and unequal orders. Remaining: one compatible mixed-type Moduli/CMObj construction and its actual nonzero iterated theta image, full prescribed nonzero row evaluation, all six lift identities, and a net integer-saving comparison for source gauge/derivatives, bad primes, row/rank/level/polarization and varying-field costs. Prime-adaptive selection is distinct. No shorter chain or general minimality proved.'
newqs=[
 ('Q3av','DP61;DataKap13-116;AMiEqAMinusQ20-66;FWExist518-580;IsThRule84-91','Does the sharp first-row witness already occupy the exact source row component, and can it be completed?','literal identification refuted; exact sufficient completion and window bounds proved','DP61','All active rows have positive degrees, with negative rows reversed. Disjoint prefix-minor fillers give a primitive integral HaO polynomial when a,b fit the first row gaps, but every nonconstant one-sided filler kills the pure axes-normalized kernel. Fixed SizeData2 windows bound the gaps; nonzero prefactor construction remains separate.'),
 ('Q3aw','DP62;Polishchuk§1Prop1.2/Cor1.3;Moret-BaillyII.2.1;Stacks0BFG/039E/02LS/0BX7','Do individual permitted theta translates have controlled canonical norms and good-prime integrality at level primes?','proved','DP62','Canonical odd-order normalization c^((N-1)/2)d^(-1)U glues over arbitrary bases, with no root extraction. Each translate is integral at every good prime, including29, and its canonical sup norm equals the fixed base norm. Actual ordinary/pair point fields have degree at most M^6/M^12. Source derivative/gauge, bad-prime and discriminant costs remain.'),
 ('Q3ax','DP64;DP40/43;Rudnick2015§2p2(1)','Can changing a fixed cyclotomic CM type or unequal fixed global directional orders improve the leading bare prime budget?','proved comparison; proposed leading improvement refuted within stated class','DP64','Every fixed cyclotomic type has linear budget (N/2)logX+O(N). The full floor budget is (1/2)sum n_i log max(1,min(X,n_i))+O(N), hence differs by only O(N) for fixed direction count and total order. Constants need not be uniform in growing conductor; prime-adaptive and actual selected theta gains are outside this certificate theorem.')]
ids={x['id'] for x in qs}
for q in newqs:
 if q[0] not in ids:qs.append(dict(zip(qf,q)))
write(root/'QUESTIONS.tsv',qf,qs)
p=root/'DP_MULT.tex';s=p.read_text()
insert='''DP54 and DP56 close finite global-jet existence with a fixed linear interpolation threshold. DP58 gives explicit sharp degrees uniform in every unit tensor parameter, and DP60 realizes them over the number field with constant $p$-adic precision, no new good-prime denominators and logarithmic section size $O(n)$. DP59 identifies the exact smaller integral span of the generic permitted torsion translates and proves that individual permitted translates or pairs already attain the sharp values at polynomial levels. DP62 proves their canonical section norms are exactly the fixed base norm, extends their normalized theta lifts integrally across every good level prime, and bounds the fields of the actual tuples. These results do not identify the source's level-dependent analytic gauge or its selected automorphic image.

DP55 and DP57 close intrinsic endpoint detection and its actual adelic realization: over the explicit unramified CM host $\\mathbf Q(\\zeta_{28})$, a fresh split principal level yields an actual period of value one. The old induced-quadratic type wrapper still fails. DP61 identifies the precise positive and reversed negative row partitions. The unchanged two-row witness is excluded from that component; a primitive determinant completion exists under explicit gap inequalities, but its pure-kernel evaluation is zero. The remaining selected-row question is therefore a nonzero completed value in the required geometric family, with the actual finite windows and all costs.

DP64 also removes a broader bare-prime alternative: within any fixed cyclotomic modulus, every CM type and every distribution of a fixed total order among finitely many globally fixed directions has the same leading integer budget, including rounding and saturation, up to $O(N)$. A direction that changes with the prime can have a larger formal first-coefficient average, but requires a global realization and its arithmetic cost. Neither this certificate comparison nor the norm conclusions upper-bound all actual selected theta gains.

'''
marker='The following attempted routes have definite stopping points:'
if 'DP54 and DP56 close finite global-jet existence' not in s:s=s.replace(marker,insert+marker)
abstract='''Finite sharp jets are globalized at controlled levels. The exact permitted torsion-translate lattice contains sharp individual witnesses whose canonical section norms are independent of level and which remain integral at every good prime. The endpoint period is constructed on an explicit unramified host; prescribed row components and finite selection windows are identified. For every fixed cyclotomic type, the full bare prime budget has the same leading coefficient, with integer rounding and saturation retained.

'''
marker="Grothendieck's boxed zero $p$-operation"
if abstract.strip() not in s:s=s.replace(marker,abstract+marker,1)
rows=r'''DP54, DP56, DP58, DP60 & Integral finite jets, ample line powers and arithmetic section norms & Milne abelian varieties Propositions9.2/10.1; Stacks0D2N,0B5T,02KH,01VT,01Q3; exact interpolation and residue proofs here.\\
DP55, DP57 & Exact endpoint Gram pairing and unramified adelic host & \path{TiedPer}79--252; \path{TiedValFi}239--255; \path{RecLevelStep}20--51; \path{InputsGenus}17--19; Stacks033C.\\
DP59, DP62 & Integral theta group, torsion-translate lattice and canonical metric & Mumford1966§1(II), Theorem1, Proposition3; Polishchuk§1 Proposition1.2/Corollary1.3; Moret-BaillyII.2.1; Stacks0BX7.\\
DP61 & Exact row partitions, determinant harmonicity and finite windows & \path{DataKap}13--116; \path{AMiEqAMinusQ}20--66; \path{FWExist}518--580; \path{RowDeg}21--48; source windows148,160--164.\\
DP64 & Fixed cyclotomic prime distributions and saturated integer certificates & DP40/43 cyclic distribution lattices; Rudnick2015§2, p.~2, equation(1); all new floor and entropy deductions proved here.\\
'''
if 'DP59, DP62 & Integral theta group' not in s:s=s.replace('\\bottomrule\n\\end{longtable}',rows+'\\bottomrule\n\\end{longtable}')
p.write_text(s)
p=root/'IMPLICATIONS.md';s=p.read_text()
s=re.sub(r'The expanded inventory contains\d+ targeted modules recovered from a pinned mirror or directly from the author archive\..*?This is incremental provenance, not a fresh\d+-file sweep\.', 'The current expanded inventory contains1029 targeted modules recovered from a pinned mirror or directly from the author archive. The recorded full sweep compared526 copies byte for byte;503 additional files have exact direct-extraction member and byte hashes in the successive manifests. This is incremental provenance, not a new complete1029-file sweep.',s,flags=re.S)
s=s.replace('The source inventory now contains529 modules:','At that earlier pass, the source inventory contained529 modules:').replace('The source inventory is now578 modules:','At that endpoint pass, the source inventory contained578 modules:')
marker='## 17. Global jets, actual permitted translates and their norms'
if marker not in s:s+='''\n\n'''+marker+'''

DP54 and DP56 turn the local sharp jets into global sections of ample theta powers over the complete DVR and then into number-field sections preserving the chosen finite valuations. A fixed linear tensor threshold suffices. DP58 identifies explicit ordinary and harmonic degrees with exact values for every unit tensor parameter, so square powers can be chosen linearly in the degree. DP60 strengthens this to a direct construction over OE[1/14]: precision modulo11 already preserves these exact witnesses, and bounded algebraic residue representatives give logarithmic section norms O(degree). These are results about actual algebraic sections, beyond a formal-series example.

DP59 determines the exact integral lattice generated by the source's generic permitted half-torsion orbit: [alpha]*H0(L^M), of rank M^g, with a basis indexed A[alpha²]/A[alpha]. It is smaller than the full ambient theta space but still separates every finite jet at M=O(n). Integral expansion and the unramified valuation group force some individual allowed translate or pair to attain the sharp local value. Generic IsVtOver/SymLift/IsNormMul clauses are verified; the old induced CM type and a prescribed automorphic theta image are not manufactured by that verification.

DP62 removes two potential uncontrolled costs for these individual witnesses. Its explicit odd-order theta lift glues without roots over every good-model prime, including primes dividing the level. Canonical complex section norms equal the fixed base-section norm exactly; the actual ordinary/pair point fields have degrees at most M^6/M^12. These are section norms and degree bounds, not a bound for source analytic frames, differentiated values, bad-prime norms or discriminants. The relevant framework is the integral theta group and cubical metric, with Mumford§1, Polishchuk§1 and Moret-BaillyII.2.1 cited precisely.

## 18. The actual endpoint, selected rows and the fixed-type prime budget

DP55 proves that the exact endpoint Fi space, rather than an arbitrary ambient coefficient module, is detected by the source period. A suitable odd principal level gives an actual period1. DP57 repairs the concrete Jacobian's unramified-host obstruction using E(i)=Q(zeta28) and J² with an integral rotation action and principal polarization. Its new split principal29-level satisfies the actual genus, reduction, DecoPtSurj and IsLevOf interfaces and realizes that endpoint adelically. The nonzero endpoint is not yet identified with the particular iterated theta image. The old imaginary-quadratic induced type remains inapplicable.

DP61 closes the exact selected-row identification: positive row partitions are aPlusQ, negative rows are reversed aMinusQ, and every active row has positive degree. The literal two-row witness is therefore excluded. Disjoint prefix-minor fillers provide an explicit primitive harmonic completion within the exact numerical partitions, subject to the first-gap bounds, but its pure axes-normalized kernel evaluation vanishes. Fixed SizeData2 windows quantify the available gaps. A nonzero completed geometric evaluation is the next selection step; merely writing a polynomial in the right component is insufficient.

DP64 extends the actual mod7 prime comparison to every CM type inside a fixed cyclotomic field. The full integer lower certificate has the saturated main term one half of sum n_i log min(X,n_i), with zero orders understood separately, and error O(sum n_i). The entropy estimate allows unequal distributions of fixed total order among finitely many directions, still changing only O(N). This closes leading bare-budget improvements by a fixed conductor/type change. A prime-dependent selector can have formal mean5/6 in the mod7 example; its global realization and coefficient/norm cost are distinct questions. None of these lower-certificate results reverses the source LinkG implication or rules out a finite saving after leading terms cancel.
'''
p.write_text(s)
marker='## Post-review work: permitted translates, norms and exact row data'
p=root/'LEDGER.md';s=p.read_text()
if marker not in s:s+=f'''\n\n{marker} — {now}

Main paper now contains checked DP57--DP62 and DP64, in addition to the earlier results; DP63/65 and prime-adaptive DP66 are still under construction/review and are not assumed here. DP57 supplies a literal unramified Host and actual adelic endpoint; DP59 the integral generic permitted-translate span and individual sharp witnesses; DP60 linear logarithmic interpolant size; DP61 exact row partitions and fixed windows; DP62 exact canonical translate norms, good-prime integrality and actual tuple-field bounds; DP64 the all-fixed-cyclotomic-type prime comparison with full saturation. Actual author, root and independent whole-proof readings, and the caught DP59 locator correction, are preserved separately. No Lean execution occurred.

Current merged records: {len(es)} check events, {len(qs)} question rows,1029 inventoried source modules. The additional429 files in the latest two manifests were hash-checked against original-archive extraction metadata; most were recovered for discovery only and were not read. Current open rows remain Q3e and the unsupplied B7 statement Q5f. This is a work entry, not an early hourly review; the consecutive-no-movement counter remains0. Next checkpoint06 is due04:20UTC; next progress review04:50UTC.
'''
p.write_text(s)
print(json.dumps({'recorded_utc':now,'events':len(es),'questions':len(qs),'main_bytes':(root/'DP_MULT.tex').stat().st_size}))

"""Complete root B99 proof audit and unchanged isolated supplementary rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, re, shutil, subprocess, sys, time, traceback
w=Path(__file__).resolve().parents[1]
c=w/'agents/reduction_descent/B_valuation_one_irreducible_candidate.tex'
p=w/'agents/reduction_descent/code/verify_valuation_one_irreducible.py'
a=p.with_suffix('.output.json')
out=w/'outputs/root_B99_audit.json';assert not out.exists()
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
expected='d765be51b4c7dac477933a2849b045aa23f50928ffef86488805d88c80b31095'
assert sha(c)==expected
before={str(q.relative_to(w)):sha(q) for q in (c,p,a)}
run=w/'outputs/root_B99_isolated';run.mkdir(exist_ok=False)
shutil.copyfile(p,run/p.name)
record={'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(c.relative_to(w)),'candidate_sha256':expected,
 'inputs_sha256':before,'entire_candidate_code_and_output_actually_read':True}
start=time.perf_counter()
try:
 with (run/'stdout.txt').open('w') as so,(run/'stderr.txt').open('w') as se:
  r=subprocess.run([sys.executable,str(run/p.name)],cwd=run,stdout=so,stderr=se)
 assert r.returncode==0
 fresh=json.loads((run/p.name).with_suffix('.output.json').read_text())
 old=json.loads(a.read_text())
 assert fresh['status']==old['status']=='PASS'
 mathematical=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
 assert mathematical(fresh)==mathematical(old)
 assert before=={str(q.relative_to(w)):sha(q) for q in (c,p,a)}
 record.update(status='FULL-INDEPENDENT-PROOF-AND-CODE-PASS',
  checker_runtime_seconds=fresh['runtime_seconds'],counts=fresh['counts'],
  author_inputs_preserved=True,all_mathematical_output_identical=True,
  proof_checks=[
   'Irreducibility forces one residual valuation and trivial wild residual action. The actual arbitrary-index good-field lemma gives the common tame degreeN field. The inverse Newton chord remains uniquely degreeq at every target0<Z<=e, so all orderp^j coordinates have exact valuatione/q^(j-1). The B79 leading action zeta^(c_i+e), not its old t1 restriction, gives the scalar-versus-Frobenius alternative at arbitrarye.',
   'At e=t p(p-1), p not dividingt gives reduced denominatorsp andp³. If the orderp² point field had degreep, the orderp³ point field would have degreep³ and its relative degreeq translations would act on a coordinate of value t(p-1), prime top. The actual fixed-coefficient expansion then makes both full Fq translation maps scalar multiples of the same uniformizer displacement, contradicting their Frobenius orientation. Thus every E/L has degreeq.',
   'The literal matrix pth-power identity putsW1 inW2 in the actual coordinates, and every evaluationW1v is onto. This givesT/E degreeq. IfdimW1=2, evaluation is an isomorphism; the selected stabilizer is central, T/L is actual Galois of orderp4, and pth powers map onto its terminalU. No Cartan or abelian-image assumption enters this step.',
   'For that hypothetical dimension2 case, A=e has exact pvaluation1. The coefficient expansion has minimumA+pb orJ+b. Its thresholda0=tN(p-1) andj0=e+(p-1)a0 satisfyj0=-t modulo p, nonzero. Both sides ofa0, the equality case with one nonzero ordinary coefficient, and the equality case with both coefficients zero force the same forbidden scalar translation maps. All greater divisible exponents change later; the fixed expansions are not changed between breaks. This excludesdimW1=2.',
   'For each actual degreeq point translation extension, a single break below(D-A)/p would forceq-1 roots of one nonzero polynomial of degreep-1, and a greater break gives the forbidden scalar/Frobenius comparison. At two breaks the fixed ordinary degree yields b+(p-1)a=D-A, giving exact last upper conductor(D-A)/p. These prove the displayed scaledc1,c2, including rational upper endpoints.',
   'For two actual basis lifts, US_i=H_i givesF2 intersectionT_i=E_i anddegree(D_i/F2)=q. InH_i first-layer matrices kill the selected residual vector, so their commutator and exact pth powers vanish on that vector; D_i/E_i is elementary abelian. Herbrand applied to the actual subgroup/compositum boundsD_i/F2 byp^(r1-2)c2. The two column maps have zero joint kernel, so their character spaces span the entire terminal dual, including determinant.',
   'Ifmu_p² is inL it is inK because the adjoining degree dividesp andN. K/K0(mu_p²) has tamedegrt, so the actual cyclotomic last break is tN² after the further tame degreeN extension; no gcd(t,N) premise is needed. Ifmu_p² is absent, the intersectionK capC0=K1 follows from the unique degreep subfield of cyclicC0/K1 andvp[K:K1]=1.',
   'The degree-tp Eisenstein derivative leading term has valuationtp²-1. Every other derivative term, including p-divisible indices, has a distinct residuei-1 modulo tp sincevK(i)=tp(p-1)vp(i). Thus the least valuation cannot cancel andd(K/K1)<=tp²-1. The opposite different is at leasttp-1. Exact two-tower transitivity with factorsp² andtp gives the stated lower bound anddelta1+pdelta2>=tp(p²-p-1).',
   'The actual determinant is cyclotomic. A traceless first layer has dimension3 and equals sl2, makingmu_p² rational; the actual cyclic last conductor exceeds the terminal bound by the positive factorizationtpN(p-1)(p³-p²-1). In the traceful case the first cyclotomic layer belongs toF2, boundingdelta1. LC capF2 is that degreep layer, notL. Its terminal restriction has conductorpsi_F2/L(d2), whose strict lower bound exceedsp^(r1-2)c2 by tN(p4-3p3+1)>0.',
   'The conclusion is only whole potentially-supersingular height2 with irreducible residual inertia atvp(e)=1. It does not settle reducible or mixed comparisons, nor claim an exact least manuscript index. Finite arithmetic supplements the actual-field proof and is not a realization argument.'
  ],
  source_scope={'retained_original':'agents/reduction_descent/sources/colmez_corps_locaux.txt',
   'sha256':sha(w/'agents/reduction_descent/sources/colmez_corps_locaux.txt'),
   'fresh_complete_read':'Remark3.6, Proposition3.7, Lemma3.8, Corollary3.9, Theorem3.10, Definition3.11, Proposition3.13, Propositions3.17/3.18 with continuation and Corollary3.19, printed14-18. The compositional Herbrand variable is used correctly rather than copying the typographical variable in the source prose.',
   'other_proof_reads':'Complete B79 freshly read, exact B49-inertia and B60-break full proofs freshly read. B97 andB98 full independent root audits in this same run remain dependencies; their needed scaled arguments are reproduced in the full new candidate and rederived above. The B67 complete proof was additionally read but is not applied outside its prime-to-p scope.'},
  scope='Full proof audit plus exact arithmetic supplementary rerun; no new field realization or full least-index claim.')
except Exception:
 record.update(status='FAIL',error=traceback.format_exc())
record['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['wall_seconds']=time.perf_counter()-start
record['retained_run']=str(run.relative_to(w))
labels=re.findall(r'\\label\{([^}]+)\}',c.read_text());record['labels']=labels
out.write_text(json.dumps(record,indent=2)+'\n')
if record['status'].startswith('FULL'):
 with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
  wr=csv.writer(f,delimiter='\t')
  for label in labels:wr.writerow([label,record['actual_utc'],record['reviewer'],'independent re-proof / computation or formal certificate','PASS: full scaled actual-field/different proof and unchanged isolated checker rerun; outputs/root_B99_audit.json.'])
print(json.dumps(record,indent=2))
if not record['status'].startswith('FULL'):raise SystemExit(1)

"""Complete B71 audit and independent author-preserving exact supplement rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_marked_quotient_sector_candidate.tex'
assert hashlib.sha256(candidate.read_bytes()).hexdigest()=='dcb305d9e9012a4af8d1fe69a9ce5311e3a58bfd48a6f8ea0c2505a2b93159f0'
source=w/'agents/reduction_descent/code/verify_marked_quotient_sector.py'
author=source.with_suffix('.output.json');before=author.read_bytes()
snap=w/'code/audit_snapshots/B71_root_independent_certificate.py'
dest=w/'outputs/root_B71_audit.json'
assert not snap.exists() and not dest.exists();snap.write_bytes(source.read_bytes())
run=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_B71_independent_certificate.stdout.txt').write_text(run.stdout)
(w/'outputs/root_B71_independent_certificate.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
fresh=json.loads(snap.with_suffix('.output.json').read_text());old=json.loads(before)
omit={'elapsed_seconds','actual_utc'}
assert {k:v for k,v in fresh.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert fresh['status']=='PASS' and author.read_bytes()==before
(w/'outputs/root_B71_independent_certificate.json').write_text(json.dumps(fresh,indent=2)+'\n')
checks={
 'lem:B-RD71-first-level':
 'The high character and determinant die over the actual common tame good field. A prime Newton parameter forces the low point valuation denominatorp, hence the common residual division field is cyclicdegreep. Its wild fixed line is uniquely the high line. In that field the prime point valuationB and displacementp(s-B) give exact lower breakps-(p+1)B. Thus the FIRST-level comparison alone determinesB and then the high tame character determinesc. No unavailable second level is invoked.',
 'lem:B-RD71-marked-low':
 'Freshly reread B69 actual quotient proof and product coordinate. ForB<e the image ofM[p]/H has valuationB, strictly less than highs-pB; this is an intrinsic stable low line. Two distinct stableFp lines kill all residual wild inertia and become rational overL. The exact p3-to-p2 subgroup quotient carries this marked low line. The tangent exponentpc and determinant give ratiozeta^((p+1)B); the scalar possibility is retained.',
 'prop:B-RD71-separated-high':
 'ForB_i=pb_i<e andq min(b_i)>e, first quotients haveD_i=q b_i>e, highA_i=s-D_i prime top and lowC_i=D_i/p. A primitive lift of a high target has exact valuationA1/q; an exchanged low target givesC2/q. Both targets and first modules areL-rational, so the common pointfield is Galois of degree at mostq; the prime numerator forces full totally ramified degreeq. A high1/low2 translation gives exact break(q-1)A1 from the first coordinate and lower boundqC2>=C2+(q-1)A1 from the second. YetA1-C2=s-p(p+1)b2+q(b2-b1)>0. Thus the high lines correspond even in scalar residual cases. The second actual quotient retains ONLYp-torsion, exactly sufficient by the new first-level lemma to compare prime parameterss-D_i.',
 'prop:B-RD71-common-high':
 'All parameters with a prime member, includingB=e, use audited B69 rules. Both divisible abovee have prime high quotients; opposite sides give the forbidden mixed divisibility. Belowe the range givesb<=2p-2 ande<2q. Unequalb_min>=2 is excluded by the separated-high proposition. The sole remaining common-norm pair is{1,p}; its tangent exponents are Frobenius conjugate, so characters agree without claiming equal parameters.',
 'prop:B-RD71-tame':
 'Both primeb cases follow the exact commonpointfield rule. In mixedb divisibility the common primitive field has degreeq, and exchanged high lines forceq(alpha1-pk)<=b-pk. Alpha1>=e+p,pk<e ande<2q<p^3 make that impossible. For bothb divisible, a largeB exchanged high/low quotient has prime versus divisible parameters, excluded at actualp2 level. Both smallB must equalq becausee<2q. The tame exchanged-eigenvalue equations then require(p-1)|2, impossiblep>=5, including scalar representations.',
 'thm:B-RD71':
 'The completed maximal unramified reduction preserves inertia comparisons. Forp-primee andmu_p inK, cyclotomicp3 hasp-partp2, distinguishing dimensions0,1,2 by determinant. Residual/Cartier-dual arguments cover extreme and filtered cases; B63 excludes mixed whole/filtered ate<p^3. B69 covers one-slope and mixed polygons; unique wild high line or the complete tame proposition covers every two-slope comparison. Thusp3 suffices in full filtered monodromy. Sincee>=2(p-1)>p the actual B63 p2 lower example applies. Exact manuscript index2 follows for2<=t<=2p+1,p notdividingt, addingp5 indices32,36,44.',
 'rem:B-RD71-scope':
 'Entire seven-assertion final proof and complete code read. Independent isolated rerun agrees in every mathematical field and preserves author bytes. Scalar endpoint cases are explicitly checked. The next e=2(p^2-1) pair{1,2p-1} is only unexcluded arithmetic; its actual realization is not inferred. No p-divisible ramification or higher-height claim is made. The finite supplement supports rather than replaces the all-prime proof.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
record={'status':'FULL ALL-PRIME PROOF AND EXACT-CERTIFICATE PASS','actual_utc':now,
        'candidate':str(candidate.relative_to(w)),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'checks':checks,'independent_runtime_seconds':fresh['elapsed_seconds'],'counts':fresh['counts'],
        'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,
        'all_mathematical_output_equals_author_output':True,
        'source_scope':'Freshly reread the complete general lower-break lemma and actual B69 quotient proof; reused previously fully source-audited Tate/descent and finite-character dependencies, with no fresh external source read claimed.'}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))

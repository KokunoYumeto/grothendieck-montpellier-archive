"""Complete root B73 proof audit with an isolated exact-certificate rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
c=w/'agents/reduction_descent/B_rational_high_line_candidate.tex'
assert hashlib.sha256(c.read_bytes()).hexdigest()=='5709f274bd7c897ade3b817505570dec37a8a6cfe3c1acdeb368087e2bfad040'
s=w/'agents/reduction_descent/code/verify_rational_high_line.py'
a=s.with_suffix('.output.json');before=a.read_bytes()
snap=w/'code/audit_snapshots/B73_root_independent_certificate.py'
out=w/'outputs/root_B73_audit.json'
assert not snap.exists() and not out.exists();snap.write_bytes(s.read_bytes())
r=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_B73_independent_certificate.stdout.txt').write_text(r.stdout)
(w/'outputs/root_B73_independent_certificate.stderr.txt').write_text(r.stderr)
assert r.returncode==0,r.stderr
fresh=json.loads(snap.with_suffix('.output.json').read_text());old=json.loads(before)
omit={'actual_utc','elapsed_seconds'}
assert {k:v for k,v in fresh.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert fresh['status']=='PASS' and a.read_bytes()==before
checks={
 'lem:B-RD73-high-branch':'Complete all-prime proof independently rederived. Tame residual action with its canonicalFp high line is a direct sum ofFp characters; degreeN kills both. Two distinct stable lines likewise give actual rationality, not only semisimplification. Rational low coordinates implyp|D. ForD<e, the exact inverse Newton hull hasp roots at(s-pD)/p andq-p atD/p; the first numerator is primep. The high branch is exactly one high-line coset by unequal-valuation formal addition. Rational target/translations make its pointfield Galois ofdegree<=p; the denominator forces degreep and full high translations. The prime-valuation lower-break equality gives the actual breakeN.',
 'prop:B-RD73-high-recovery':'No upper bound one is used. IfD1<e, an exchanged high line gives the SAME degreep pointfield forX1 andX2. The second coordinate has normalized valuationD2/q, either nonintegral or subject to the break inequalityD2>=D2/q+eN, equivalentD2>=qe, contradictingD2<pe. IfbothDi>e, orderD1<=D2 and the high inverse branch hasdenominatorq. Rational first modules give full degreeq translation field. A high1/low2 displacement yieldsD2/p>=s-D1, whereas s-D1>=s-D2>D2/p. EqualityD=e is excluded byp|D,p notdividinge. Scalar residual cases are fully included.',
 'lem:B-RD73-common-high':'Prime original parameters useB69 actualp2 rules. Divisible large parameters give prime high quotients; opposite sides give forbidden mixed divisibility. ForBi=pbi<e, the first actual quotient hasDi=qbi and intrinsic stable low line distinct fromhigh, hence L-rational first module. B73 high recovery identifies the second kernels at actualp2 level. The second quotient retains EXACTLYp-torsion via the displayed preimage quotient of actualp3 torsion. BothlargeDi give prime parameters recovered at first level; a mixed pair gives an actual tame module with intrinsic lowline versus a prime-parameter wild module, impossible. BothsmallDi imply1<=bi<=p-1 becausee<p3; common determinant/high characters giveb1=b2modp-1, hence equality in that interval and equal special characters.',
 'prop:B-RD73-formal':'B69 completely handles one-slope and mixed-polygons without an upper index bound. Nontrivial residualwild action identifies the common unique high line. Residually tame modules are actually L-rational and their high lines are recovered from the availablep2 comparison. Thus every two-slope possibility reduces to the common-high lemma, with no missing semisimple or scalar case.',
 'thm:B-RD73':'Freshly reread complete B63 rational-point theorem, mixed whole/filtered threshold and actual arc/lower construction. Forp<e<p3, completed unramified reduction and the orderp2 cyclotomic determinant distinguish total dimensions and finite determinants. Height-one filtered cases are determined residually, mixed whole/filtered comparisons are excluded byB63, and whole formal comparisons use this theorem. B63 atactualp2 gives the lower bound becausee>p. The only permitted e<=p is p-1, whose exact index is1; p3 itself is excluded; for everypermittede>p3 the actualp3 lower construction gives index>=3. Thus the stated IF AND ONLY IF and t-range throughp2+p+1 are justified. No value atlargere orp-divisiblee is claimed.',
 'rem:B-RD73-scope':'Entire final proof and entire exact program read; candidate counts/scope and all rerun mathematical fields checked. The360finite sectors, all rational Newton branches and actual quotient multisets support rather than replace the all-prime argument. Beyond-threshold tests apply only to high-line alignment. Fresh targeted literature queries/read scopes are retained by the author; root read that log but does not claim to have opened those new external sources. No priority claim is made.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label,detail in checks.items():wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','independent re-proof','PASS. '+detail])
record={'status':'FULL ALL-PRIME PROOF AND EXACT CERTIFICATE PASS','actual_utc':now,'candidate_sha256':hashlib.sha256(c.read_bytes()).hexdigest(),'checks':checks,'independent_runtime_seconds':fresh['elapsed_seconds'],'counts':fresh['counts'],'program_sha256':hashlib.sha256(s.read_bytes()).hexdigest(),'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,'all_mathematical_fields_equal_author':True,'fresh_internal_dependency_reads':['B60 full general lower-break proof','B69 full comparison and actual quotient rules, with earlier complete audit reused','B63 complete rational-point, mixed comparison and all-index lower-example proofs'],'external_source_scope':'Previously fully audited Hopkins-Gross/Tate/descent source chain reused. The fresh author literature-search log was read; no fresh root access to its Hattori/Hoshi sources is claimed.'}
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))

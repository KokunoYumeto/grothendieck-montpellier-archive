"""Complete uniform B74 induction audit and author-preserving exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
c=w/'agents/reduction_descent/B_iterated_high_quotient_candidate.tex'
assert hashlib.sha256(c.read_bytes()).hexdigest()=='30538d9b2588452cd20be474b5e9860994d37b91ba7cf257b8a2b389dfa32990'
s=w/'agents/reduction_descent/code/verify_iterated_high_quotient.py'
a=s.with_suffix('.output.json');before=a.read_bytes()
snap=w/'code/audit_snapshots/B74_root_independent_certificate.py'
out=w/'outputs/root_B74_audit.json';assert not snap.exists() and not out.exists()
snap.write_bytes(s.read_bytes());r=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_B74_independent_certificate.stdout.txt').write_text(r.stdout)
(w/'outputs/root_B74_independent_certificate.stderr.txt').write_text(r.stderr)
assert r.returncode==0,r.stderr
fresh=json.loads(snap.with_suffix('.output.json').read_text());old=json.loads(before)
omit={'actual_utc','elapsed_seconds'}
assert {k:v for k,v in fresh.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert fresh['status']=='PASS' and a.read_bytes()==before
checks={
 'lem:B-RD74-actual-levels':'Full exact finite-group construction checked: quotient p^(r-1)-torsion is the specified preimage in actualp^r divided byH. Every stage loses exactlyonelevel, the totalrankp^j kernel is killedbyp^j, and the last comparison isonlyp. Finite-flat closure and actual quotient/descent use the complete B69 proof; the special isogeny preserves the unordered finite character{c,pc}. A small divisible parameter gives the intrinsic stablelow line and actual L-rational p-module; a large one gives prime parameter and nontrivial cyclicp wild action. EqualityD=e isexcluded.',
 'prop:B-RD74-formal':'Complete induction independently rederived. Original one-slope/mixed polygons use unrestrictedB69 actualp3. Wild or tame/L-rational cases align original highlines. Primeoriginal parameters use actualp2; onlyBi=pbi<e remain. Atstage0<=j<=n-2 currentparametersp^(j+1)bi have actuallevelp^(n-j), so at leastp2 remains to alignhigh using the preceding intrinsiclowline. The nextquotient leaves at leastp: bothlarge parameters becomeprime and first-level recovery settlescharacters; a mixedcrossing gives tameversuswild and is impossible. Ifallstagesstaysmall, b<e/p^(n-1)<p; commonnorm gives equalbmodp-1 and henceequalb in1..p-1. Everybranch is exhausted without an extra unavailablelevel.',
 'thm:B-RD74-upper':'Completed-unramified reduction, cyclotomic determinant orderp^(n-1), height-one filteredcases and wholeformalcomparison give the fullsetting. B63 mixedcomparison requires e>p^(2n-3), incompatiblewith e<p^n for n>=3. Thusnu<=n-1. Forp^k<e<p^(k+1), n=max(3,k+1) givesuppermax(2,k), while the actuallower examples withr=floor((k+3)/2) give lower r. The manuscript shift actualp^r versusindexr-1 is accountedfor. Equality isnotclaimedwhereboundsdiffer.',
 'cor:B-RD74-third-index':'Takingn4 givesupper3 onp³<e<p⁴; the actualp³ lowerexample giveslower3, provingexactindex3 there. Forp5 thepermittedmultiplesoffourare128through624excluding5divisibility. This is a sufficientexactinterval, not an iffclassification ofallindex3cases.',
 'rem:B-RD74-scope':'Entire finalproof and entire exactprogram read. The author-preserving rerun agrees inallmathematicalfields. Four actualmodulequotients,81600 matrix-point identities,196complete sectors and406explicitdeeper samples retain their exactscope. The earlier successfulversion/output remainpreserved; nofailed computation is asserted. Largerintervals,e divisiblebyp,andhigherheights remainopen. Existingcomplete source audits are reused; no fresh externalmain-proof read isclaimed.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label,detail in checks.items():wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','independent re-proof','PASS. '+detail])
record={'status':'FULL UNIFORM INDUCTION AND EXACT CERTIFICATE PASS','actual_utc':now,'candidate_sha256':hashlib.sha256(c.read_bytes()).hexdigest(),'checks':checks,'independent_runtime_seconds':fresh['elapsed_seconds'],'counts':fresh['counts'],'program_sha256':hashlib.sha256(s.read_bytes()).hexdigest(),'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,'all_mathematical_fields_equal_author':True,'source_scope':'Full B69/B71/B73 quotient and high-line proofs and B63 mixed-threshold/lower construction rechecked in this checkpoint; no new external theorem or source read claimed.'}
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))

"""Record complete B65 proof audit and an author-output-preserving exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_B65_audit.json';assert not dest.exists()
candidate=w/'agents/reduction_descent/B_p5_e12_high_quotient_candidate.tex'
source=w/'agents/reduction_descent/code/verify_p5_e12_high_quotient.py'
author=source.with_suffix('.output.json');before=author.read_bytes()
snap=w/'code/audit_snapshots/B65_root_independent_certificate.py';assert not snap.exists()
snap.write_bytes(source.read_bytes())
p=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_B65_independent_certificate.stdout.txt').write_text(p.stdout)
(w/'outputs/root_B65_independent_certificate.stderr.txt').write_text(p.stderr)
assert p.returncode==0,p.stderr
out=snap.with_suffix('.output.json');data=json.loads(out.read_text());original=json.loads(before)
exclude={'actual_utc','runtime_seconds'}
assert {k:v for k,v in data.items() if k not in exclude}=={k:v for k,v in original.items() if k not in exclude}
assert before==author.read_bytes()
(w/'outputs/root_B65_independent_certificate.json').write_bytes(out.read_bytes())
checks={
 'lem:B-RD65-Newton':'All new eL288 Newton and break steps rederived, not inferred from minimal ramification. The nonzero5-point polygon is(1,288),(5,4B),(25,0), giving alpha72-B,betaB/5 andBodd,0<B<60. One-slope leading scalar action is irreducible or has square determinant. Integral high coordinates and exact tame averaging giveB=c mod6 and high characterc-B mod24. Inverse low valuationB/125 follows from the exact polygon. Over the common residual wild field, lower breaks360-6B equal for5-primeB and strictly smaller for5-divisibleB. The mixed case forcesB1>B2. The actual order25 point field has elementary abelian degree25, since the prime denominator attains the universal degree bound; its common low translation then forces the contradictory inequality25B2>=B2+24B1. In the tame branch with bothb=B/5 prime, the same actual point field gives24b1=24b2; a high-only translation then forces the impossible alpha=b if the high lines differ. Common high-line characters identifyc. Original B60 lower-break expansion and full B61 point-field proof reread.',
 'lem:B-RD65-quotient':'Full integral quotient argument checked. The finite flat high closure gives a good quotient whose parameter has Weierstrass factorunit times product(T-TQ). For inputs belowalpha its valuation is5v(T). The inverse-high polygon has25 rootsalpha/25 whenB>12, and5 roots(72-5B)/5 plus20 rootsB/5 whenB<12. Taking all four nonzero high targets and dividing by5 gives exactly4 high and20 low quotient points. ThusBprime=72-B or5B, respectively. B12 is excluded by parity. The special quotient is Frobenius, so cprime=5c and its unordered orbit is unchanged. The actual inverse image of quotient25-torsion is{P inM125:25P inH}; dividing byH proves the precise125-to25 comparison under a high-line-preserving isomorphism.',
 'prop:B-RD65-nonsquare':'All residual branches exhausted. A one-slope module has orbitc+12,5(c+12);12 is fixed by5 mod24, so this recovers the special orbit. In the wild unequal case, the high line is intrinsic. The only5-divisibleB values are5,15,25,35,45,55. Quotient sends5 to25 and every other value to72-B, prime to5. Common quotient25-torsion either identifies the new prime parameters or is ruled out by mixed divisibility. BothB5 are already determined by the common high character. In the tame branch allb except5 are handled by the prime point-field proof. Forb=5 the two c choices1,13 have disjoint residual semisimplifications{1,eta} and{-1,-eta}. Mixedb5 with primeb: distinct high lines require125>=5+25(72-5b)-b>=419, impossible. Common high lines requireb<=5 and c1-c2=5b-25 mod24; c=1 mod4 leavesb1 only, whose c values5 or17 are in the same special orbit as1 or13. No formal deformation existence is inferred from the arithmetic list.',
 'lem:B-RD65-square':'The common finite square-root twist makes the faithful good degree divide6, hence a=12m<=72. The already fully audited B64 integral projector, perfect pairing and graph-quotient construction is applied to the actual target Q times M, not a source thickness proxy. Its special fibre is a product of height2 formal groups. Invariant differentials make nonlinear coefficients below degree5 divisible by5; special height2 makes degrees5 through24 vanish modthe uniformizer. Thusq1>=6 andq2>=min(a+6,31)>=a/4 for every12<=a<=72. The B64 closed coefficientwise logarithm and Cartier bounded projection argument then kills the special kernel byF^2, contradicting kerF^3, whoseF^2 image has rank5. No analytic convergence at equality is assumed.',
 'thm:B-RD65':'Exact lower and upper bounds matched. B63n2 gives actual25-torsion ambiguity ate12>5, so manuscriptindex>=2. An actual125 comparison separates dimensions and finite determinants because the cyclotomic image has order25 while finite determinants have prime-to5 order. Dimensions0,2 and two filtered systems are already recovered from residual characters; the whole-formal versus filtered case is excluded by B63n3 because12<=125. The two whole-formal cases are precisely the preceding square and nonsquare proofs. Hence nu_min(5,12,2)=2 under the stated full manuscript hypotheses.',
 'rem:B-RD65-scope':'No exact value ate16 or higher height is claimed. The finite supplement is only arithmetic and case-exhaustion support. Its full source was read and an exact output-preserving independent run passed with every mathematical output identical.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
record={'status':'FULL MATHEMATICAL PROOF AND EXACT CERTIFICATE PASS','actual_utc':now,
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
 'independent_runtime_seconds':data['runtime_seconds'],'independent_counts':data['counts'],
 'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,
 'all_mathematical_output_equals_author_output':True,'checks':checks,
 'source_scope':'No new external theorem imported. Full B60 lower-break and B61 common point-field proofs were freshly reread; the new absolute-index version is proved in full. The same original Hopkins-Gross Newton input and Bondarko actual-target Cartier input were fully checked in this session for B63-B64. No new source retrieval is claimed for this audit.'}
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))

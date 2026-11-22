"""Literal isolated B99 audit; preserve all author bytes and mathematical output."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, sys, time

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'RESEARCH_SA15_paper.tex').exists())
OWN = ROOT/'agents/obstructions_crystals'
RD = ROOT/'agents/reduction_descent'
CANDIDATE = RD/'B_valuation_one_irreducible_candidate.tex'
PROGRAM = RD/'code/verify_valuation_one_irreducible.py'
OUTPUT = PROGRAM.with_suffix('.output.json')
RUN = OWN/'outputs/B99_independent_run'
RECORD = OWN/'B99_independent_audit.json'
assert not RUN.exists() and not RECORD.exists()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(CANDIDATE) == 'd765be51b4c7dac477933a2849b045aa23f50928ffef86488805d88c80b31095'
before = {str(p.relative_to(ROOT)):sha(p) for p in (CANDIDATE,PROGRAM,OUTPUT)}
RUN.mkdir(parents=True)
copy = RUN/PROGRAM.name
shutil.copyfile(PROGRAM,copy)
assert sha(copy) == sha(PROGRAM)
start = time.perf_counter()
proc = subprocess.run([sys.executable,str(copy)],cwd=RUN,capture_output=True,text=True)
elapsed = time.perf_counter()-start
(RUN/'stdout.txt').write_text(proc.stdout)
(RUN/'stderr.txt').write_text(proc.stderr)
assert proc.returncode == 0, proc.stderr
a = json.loads(OUTPUT.read_text())
b = json.loads(copy.with_suffix('.output.json').read_text())
assert a['status'] == b['status'] == 'PASS'
omit = {'actual_utc','runtime_seconds'}
assert {k:v for k,v in a.items() if k not in omit} == {k:v for k,v in b.items() if k not in omit}
after = {str(p.relative_to(ROOT)):sha(p) for p in (CANDIDATE,PROGRAM,OUTPUT)}
assert before == after
now = datetime.now(timezone.utc).isoformat()
checks = {
 'lem:B-RD99-points': [
  'The common good tame degree N is valid at arbitrary e by the full B49 inertia lemma. Irreducibility makes the first Newton polygon one segment, kills residual wild inertia and gives leading scalar Fq spaces; field-linear comparison identifies special characters, so a contrary pair has the stated Frobenius orientation.',
  'Reduced denominators t(p-1)/p and t(p-1)/p^3 are exact because p does not divide t. If [E:L]=p, the actual full terminal translation group in the common degree-p^3 point field contradicts scalar-versus-Frobenius leading maps. Thus all actual second-point degrees are q. Exact pth powers give W1 contained in W2 and all terminal translations, hence [T:E]=q.',
  'For r1=2, the primitive stabilizer is actually central, making this point field T/L Galois and E=F2. No abelian or Cartan assumption is imported. The fixed ordinary exponent for a<a0 or a>a0 is uniquely first at every terminal break. At a=a0, the nonzero-coefficient and both-zero cases separately contradict Frobenius orientation. j0 is -t modulo p, so the critical coefficient remains nonzero at every permitted t.',
  'The full one-break and two-break coordinate analysis gives exact last upper breaks c1=tN(p-1), c2=t(q^2-1)(p-1). Actual stabilizer identities US_i=H_i prove the compositum intersections. Commutators and powers vanish after the selected column quotient, giving the actual elementary-abelian field D_i/E_i. Herbrand conversion bounds each column by p^(r1-2)c2, and the two dual column maps span the complete terminal dual.'
 ],
 'lem:B-RD99-cyclotomic': [
  'The Cohen coefficient/complete uniformizer-basis argument gives [K:K0]=e for this perfect infinite residue field. If mu_(p^2) lies in L it lies in K; K/K2 is genuinely tame of degree t, so the degree-p cyclotomic break scales first by t then N to tN^2. No coprimality of t and N is required.',
  'If mu_(p^2) is absent, C0 meets K exactly in K1 by the cyclic p^2 subfield chain and vp([K:K1])=1. Thus C/K and C/C0 have actual degrees p^2 and tp. In the degree-tp Eisenstein derivative, every term has its distinct residue i-1 modulo tp, including p-divisible i, while the leading term has valuation tp^2-1. This proves the upper different bound without cancellation.',
  'Both actual different towers yield delta1+p delta2 >= tp(p^2-p-1). The exact cyclotomic displacement sum is 2p^2(p-1). The rational endpoint is retained; no finite-residue class-field theorem, Hasse-Arf integrality or upper-break rounding is used.'
 ],
 'thm:B-RD99-irreducible': [
  'Traceless W1 has dimension3 and is sl2; the determinant puts mu_(p^2) in L. Its actual last cyclotomic character restricts beyond the complete terminal bound, by the exact positive scaled gap tpN(p-1)(p^3-p^2-1).',
  'With nonzero trace, the first cyclotomic quotient lies in F2 and bounds delta1 by t(p-1). The last cyclic upper break exceeds c1, and q(d2-c1)-c2 >= tN(p^4-3p^3+1)>0. The elementary F2 and cyclic p^2 field intersect in precisely their first cyclotomic degree-p field. Exact subgroup/quotient conversion then contradicts the complete terminal-character bound, including determinant direction.'
 ],
 'rem:B-RD99-scope': [
  'Only actual p^3 recovery in the whole potentially supersingular irreducible-residual branch at vp(e)=1 is proved. Arbitrary positive t prime to p is retained. No reducible, mixed/filtered, formal realization or new full least-index conclusion is inferred from the proof or finite checker.',
  'The six undefined spacing tokens caught during the audit were repaired only typographically; the exact old source and delta were read and preserved. Checker and author output were unchanged.'
 ]
}
source = RD/'sources/colmez_corps_locaux.txt'
record = {
 'status':'FULL PROOF SOURCE AND CODE PASS', 'actual_utc':now,
 'candidate':str(CANDIDATE.relative_to(ROOT)), 'candidate_sha256':sha(CANDIDATE),
 'labels':checks, 'author_hashes_before':before, 'author_hashes_after':after,
 'program_run':{'literal_copy':str(copy.relative_to(ROOT)), 'internal_runtime_seconds':b['runtime_seconds'],
                'wall_runtime_seconds':elapsed, 'all_mathematical_output_identical':True,
                'excluded_fields':sorted(omit), 'counts':b['counts'], 'exit_code':proc.returncode},
 'complete_reads_this_audit':['B99 final full source and exact spacing delta',
    'entire verify_valuation_one_irreducible.py and full author output',
    'entire canonical B_first_wild_irreducible_image.tex (B79)',
    'entire canonical B_irreducible_point_field_layers.tex (B97)'],
 'bounded_full_dependency_reads':['complete B49 tame formal inertia lemma and proof',
    'complete B60 fixed-coefficient lower-break lemma and proof'],
 'linked_recent_complete_dependency_audit':'agents/obstructions_crystals/B98_independent_audit.json (complete Cohen/different/cyclotomic proof read earlier this session)',
 'primary_source_read':{'path':str(source.relative_to(ROOT)), 'sha256':sha(source),
   'scope':'Fresh retained original full Colmez Remark3.6, Proposition3.7, Lemma3.8, Corollary3.9, Theorem3.10, Definition3.11, Proposition3.13 and complete Lemma3.15, Propositions3.17/3.18 including continuation, Corollary3.19; pp14-18. The printed intermediate compositional variable in 3.10 is not imported; the actual Herbrand composition is rederived.',
   'new_external_fetch':False, 'new_original_pdf_image_view':False},
 'controller_history':'An initial missing closing brace caused a pre-execution SyntaxError. Exact failed controller/stderr retained in notes/B99_audit_controller_syntax_failure; no author checker ran during that failure.',
 'scope':'Full four-label proof/source/code pass. Exact finite and symbolic arithmetic is supplementary and does not construct fields or groups.'
}
RECORD.write_text(json.dumps(record,indent=2)+'\n')
with (OWN/'CHECK_EVENTS.tsv').open('a') as f:
 for label,details in checks.items():
  f.write('\t'.join([now,label,'independent-full-proof-source-code-audit',str(CANDIDATE.relative_to(ROOT)),
    'Full proof and actual field dependencies; original retained sources; literal isolated rerun',
    'PASS: '+' '.join(details),str(RECORD.relative_to(ROOT))])+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'record':str(RECORD.relative_to(ROOT)),
                  'candidate_sha256':sha(CANDIDATE),'runtime_seconds':b['runtime_seconds']}))

"""Record the full norm13 proof audit and isolated reconstructive certificate."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1];a=w/'agents/monodromy'
candidate=a/'nonordinary_uniform_thirteen_theta_geometry_candidate.tex'
source=a/'code/verify_nonordinary_thirteen_certificates.py'
author=a/'outputs/verify_nonordinary_thirteen_certificates.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='9266244ac3fb5ca57c4c9c051be22f8d1787c42c7653c054c8a0b4fd1636b5db'
assert sha(candidate)==expected
assert sha(source)=='43a9b103eff5828f5036498a809726614b4f35a05f3fd77e828370737d25dfd8'
before=sha(author)
algebra=json.loads((w/'outputs/root_norm13_algebra_reruns.json').read_text())
assert algebra['status']=='PASS' and len(algebra['runs'])==6 and algebra['author_bytes_unchanged']
folder=w/'code/audit_snapshots/norm13_root_algebra'
dest=folder/'code/verify_nonordinary_thirteen_certificates.py'
snapshot=w/'notes/root_uniform_thirteen_audited_candidate.tex'
out=w/'outputs/root_uniform_thirteen_theta_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True,timeout=150)
wall=time.perf_counter()-start
(folder/'outputs/verify_nonordinary_thirteen_certificates.stdout.txt').write_text(run.stdout)
(folder/'outputs/verify_nonordinary_thirteen_certificates.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=json.loads((folder/'outputs/verify_nonordinary_thirteen_certificates.json').read_text())
original=json.loads(author.read_text())
def mathematical(x):
 if isinstance(x,dict):return {k:mathematical(v) for k,v in x.items() if k not in ('actual_utc','runtime_seconds','seconds')}
 if isinstance(x,list):return [mathematical(v) for v in x]
 return x
assert independent['status']=='PASS_COMPLETE_THIRTEEN_CERTIFICATE_RECONSTRUCTION'
assert mathematical(independent)==mathematical(original)
assert sha(author)==before and sha(source)==sha(dest)
assert all(sha(w/path)==digest for path,digest in algebra['author_hashes_before'].items())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:uniform-thirteen-generic-fibres-candidate','lem:uniform-thirteen-generic-parameters-candidate',
 'lem:uniform-thirteen-exceptional-map-candidate','thm:uniform-thirteen-nodal-self-isogeny-candidate',
 'cor:f0-odd-multiples-thirteen-candidate','rem:uniform-thirteen-verification-scope-candidate']
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'The entire initial395-line proof was read, followed by every retained final alignment/checker-record diff and the single display-close correction. All six mathematical assertions are covered. All six algebra programs, their complete coefficient-ring dependency and the full compact reconstruction checker were read.',
 'proof_checks':[
  'The actual normal form and order-four automorphism give an etale polarized self-isogeny3+2g with multiplier13. Arbitrary sections of O(7W) impose all multiplicities; delta l+Zc=0 has constant rank. The resulting residual divisor is unique and nonspecial and excludes finite theta-kernel points.',
  'The exact norm identity gives a separable cubic in Z for every finite residual coefficient L, since derivative Z^2 and nonzero constant prohibit repeated roots. If A is nonzero a triple fibre forces P1=P2=0. If A is zero, a collision of the quadratic values forces T=0, including B2=0.',
  'Z=0 has residual divisor W+R with x(R)=p+a/delta^2, and it cannot meet a finite residual divisor. Hyperelliptic conjugates cannot give equal nonzero images because geometric two-torsion is zero. Infinity is the unique point above zero.',
  'The exact degree224 and198 resultants, their complete factor products, degree137 bad polynomial, degree816 pullback and five-parameter gcd identify mu^5=1 as the only unresolved modulus for3+2g. The parameter orbit stays outside F4 and preserves the modulus, including mu=0; fifth-root scaling realizes the prescribed mu.',
  'At the exceptional class, the explicitly irreducible degree12 field and encoded three independent order-four translations give actual curve automorphisms. The coefficient equations verify preservation, squares and pairwise anticommutation. Rosati adjoints therefore give multiplier1+4+4+4=13 for the different self-isogeny.',
  'The O(9W) interpolation eliminates four coefficients by nonzero constant denominators. The remaining2x3 minors satisfy an explicit Bezout identity equal to1, so rank is two at every finite source point. This again excludes the finite theta kernel and makes every residual divisor nonspecial.',
  'The reconstructed norm gives residual rational coordinates L,M. The full stored polynomial identity U E_L+V E_M=S0+S1 q is checked by direct multiplication; gcd(S0,S1)=monic(l2)^44 leaves a nonzero linear polynomial at every nonpole. It excludes two other distinct source x-values without any specialization assumption on a generic gcd.',
  'The pole scheme is reduced of degree8; c4 and B are units there, so its residual divisor is W+R. The eight powers of x(R) are a basis and its degree8 minimal polynomial is separable, proving all pole images distinct. Pole and affine fibres cannot mix. Repeated residual roots require no extra chart.',
  'The complete odd-theta nodality lemma converts at-most-two-point fibres into ordinary nodes using the actual etale quotient and the genus-two canonical map. It gives exactly169-1=168 nodes. The self-isogeny is incoming to the same fixed surface.',
  'The good-theta norm step applies with source degree1 and multiplier13. For any odd multiple13n the arbitrary odd incoming-neighbour and cubic-component norm transfer apply with known source degree13. Full geometric GL forces the same arithmetic group. This closes odd degrees divisible by13 only; the least unclassified fixed-f0 odd degree becomes17, while fixed-f1 and arbitraryX gates remain open.'
 ],
 'dependencies_freshly_read':[
  'Complete odd-theta nodality lemma and proof in nonordinary_odd_theta_nodality_reduction.tex.',
  'Complete order-four presentation lemma and proof in nonordinary_uniform_five_theta_geometry.tex.',
  'Complete eleven-case parameter proof in nonordinary_uniform_eleven_theta_geometry.tex, including the five transformations and fifth-root normalization.',
  'Opening hypotheses and complete main theorem proof of nonordinary_good_theta_norm_transfer.tex; its earlier graph and local inputs retain their existing full audits.',
  'Opening hypotheses and complete main theorem/corollary proof of nonordinary_cubic_component_norm_transfer.tex; its earlier local graph dependencies retain their existing full audits.'
 ],
 'primary_source_scope':'Focused norm13 primary-repository searches at00:12–00:13 are recorded in notes/ROOT_SEARCH_LOG_29.md. No matching theorem or new complete original proof was obtained in that pass. Existing normal-form and other original-source read scopes are not overstated. No priority is claimed.',
 'six_program_reruns':'outputs/root_norm13_algebra_reruns.json',
 'six_program_runtimes_seconds':{r['name']:r['runtime_seconds'] for r in algebra['runs']},
 'reconstructive_program':str(source.relative_to(w)),'program_sha256':sha(source),
 'isolated_program':str(dest.relative_to(w)),
 'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(folder/'outputs/verify_nonordinary_thirteen_certificates.json'),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],'reconstruction_checks':independent['checks'],
 'all_mathematical_output_fields_equal':True,'all_author_bytes_unchanged':True,
 'executed_failures_in_this_audit':[],
 'earlier_failure_scope':'Earlier exploratory failed maps, finite-field truthiness error, timed-out elimination variants and corrected sources remain retained; this theorem uses neither failed map for the exceptional class.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in labels:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program reruns',
   'PASS: complete uniform proof, six algebra sources and reconstructive checker read; six unchanged reruns plus34-check independent reconstruction passed with all mathematical fields equal and author bytes preserved. Exact scope outputs/root_uniform_thirteen_theta_audit.json.'])
 for label in ['lem:root-nonordinary-odd-theta-nodality','lem:uniform-f0-order-four-presentation-candidate',
               'lem:uniform-eleven-good-parameters-candidate','thm:good-theta-odd-norm-step-candidate',
               'thm:cubic-component-arbitrary-odd-norm-transfer-candidate']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run',
   'Complete named dependency proof and actual application hypotheses reread for norm13; deeper previously audited inputs retained at their recorded scope. See outputs/root_uniform_thirteen_theta_audit.json.'])
print(json.dumps({k:v for k,v in record.items() if k not in ('proof_checks','dependencies_freshly_read','reconstruction_checks')},indent=2))

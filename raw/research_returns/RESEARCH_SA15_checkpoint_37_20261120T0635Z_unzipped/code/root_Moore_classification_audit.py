"""Retain a complete root proof audit and an unchanged isolated certificate run."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w = Path(__file__).resolve().parents[1]
candidate = w/'agents/obstructions_crystals/post_CP30_Moore_singular_parameter_classification_candidate.tex'
source = w/'agents/obstructions_crystals/code/verify_Moore_singular_parameter_classification.py'
author = source.with_suffix('.output.json')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate) == '234608ae83437e80577d715b17f43bcc075c8fef479d444e2c2cf52c1a343067'
assert sha(source) == 'f6be2e4a4936ba4b324333e21cc966ee00d5973190bfefdb1738ba0293e7ba60'
before = sha(author)
assert before == '810398ac56d49b9100cfce562c3bbe09d0dc8d074b16cff48eb2300fe4aca9e6'
dest = w/'code/audit_snapshots/Moore_classification_root_independent_certificate.py'
snapshot = w/'notes/root_Moore_classification_audited_candidate.tex'
out = w/'outputs/root_Moore_classification_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source, dest)
shutil.copy2(candidate, snapshot)
start = time.perf_counter()
run = subprocess.run([sys.executable, str(dest)], cwd=w, capture_output=True, text=True)
wall = time.perf_counter()-start
(w/'outputs/root_Moore_classification_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_Moore_classification_independent_stderr.txt').write_text(run.stderr)
assert run.returncode == 0, run.stderr
original = json.loads(author.read_text())
independent = json.loads(dest.with_suffix('.output.json').read_text())
mathematical = lambda x: {k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original) == mathematical(independent)
assert sha(author) == before and sha(dest) == sha(source)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
labels = ['lem:DE-Moore-support','lem:DE-Moore-six-matching',
          'thm:DE-Moore-singular-parameters','rem:DE-Moore-classification-scope']
record = {
 'status':'PASS', 'actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)), 'candidate_sha256':sha(candidate),
 'labels':labels,
 'proof_scope':'Entire four-label candidate and entire standalone checker read; all algebraic reductions independently checked; full unchanged exact certificate rerun in an isolated retained path.',
 'proof_checks':[
  'The 4-bit exponent encoding is collision-free because every determinant monomial has total c-degree and x-degree 9, and all intermediate displayed factor products have degree at most 9. Characteristic-two signs are all 1, and the symmetric-difference set reconstructs exactly the full determinant.',
  'Every one of the 511 nonempty supports is tested for an actual single-monomial x-coefficient. Each such coefficient is everywhere nonzero on its support torus. The surviving 111 supports equal precisely the affine orbits of sizes 2,4,6,8; no finite-field sample replaces a torus argument.',
  'Affine covariance permutes rows by Ta+h and columns by Tb while reindexing c and x by Tg+h. It preserves the determinant-zero condition and transports the center and linear character as claimed.',
  'All eight displayed factor identities and the four uniform x_0^7 x_v x_-v coefficient locators are exact polynomial identities. On the eight-support torus the latter force each ratio to be a cube root of unity. Every rejected phase has a single nonzero monomial coefficient in independent d-variables, so exclusions hold over every algebraically closed characteristic-two field.',
  'For three selected matching edges, distinct rows give either distinct columns or a star by the sum of indices. Exactly two rows force exactly two columns since three distinct columns have index sum zero. The 2-by-2 case identifies four values, and the sum identifies the unused pair; the two possible completions contain one reflection. In a star, sum and nonzero product give v^2=u^2, hence v=u.',
  'On the six-support torus, cubed coordinate values satisfy the matching lemma. The uncubed product identity forces the sum of the three cube-root exponents to vanish, exactly the affine functions alpha+beta i. Choosing 2h_2=r_0 supplies the required center on the missing line and a linear character on F3^2.',
  'For c in V_(h,ell), row permutation a->a+h and scaling by zeta^(-ell(a)) make the actual Moore matrix symmetric with zero diagonal, hence alternating of odd order and singular. This is a universal identity even when some free coordinates vanish.',
  'Each claimed vector space has four free opposite-pair coordinates; its unique identically zero individual coordinate identifies its center, and different characters impose different pair equations. Thus the 81 projective three-spaces are distinct. The result is set-theoretic only.'
 ],
 'source_scope':'Self-contained exact polynomial and finite matching argument; no external classification theorem used or priority claim made.',
 'program':str(source.relative_to(w)), 'program_sha256':sha(source),
 'author_output_sha256':before, 'author_output_unchanged':True,
 'independent_program':str(dest.relative_to(w)),
 'independent_output':str(dest.with_suffix('.output.json').relative_to(w)),
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'author_runtime_seconds':original['runtime_seconds'],
 'independent_runtime_seconds':independent['runtime_seconds'],
 'independent_subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True, 'counts':independent['counts'],
 'scope_guard':'No actual Cartier coefficient or theta-embedding identification follows from this algebraic theorem alone; no main A3/A4 gate is claimed closed.',
 'executed_failures':[]}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in labels:
  writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
   'independent re-proof / computation or formal certificate',
   'PASS: full proof and checker read; unchanged isolated universal certificate rerun, all mathematical output identical. Complete details in outputs/root_Moore_classification_audit.json. Abstract set-theoretic Moore locus only; no actual Cartier identification asserted.'])
print(json.dumps({k:record[k] for k in ('status','actual_utc','candidate_sha256','independent_runtime_seconds','all_mathematical_output_identical','counts')},indent=2))

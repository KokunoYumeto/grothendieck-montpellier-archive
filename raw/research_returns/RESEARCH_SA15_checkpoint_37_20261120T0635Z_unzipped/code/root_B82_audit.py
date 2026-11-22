"""Record the actual complete B82 proof audit and unchanged isolated certificate rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_reducible_terminal_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_reducible_terminal.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='594f019abab5cd378c489671f7ff021c7e0e446ac53166f696dafa035f0f761b'
assert sha(candidate)==expected
assert sha(source)=='fa0816d90ad10cd616219c9ee4f7df12bca8d2e66bbfc33301f701c4e9974889'
before=sha(author)
dest=w/'code/audit_snapshots/B82_root_independent_certificate.py'
snapshot=w/'notes/root_B82_audited_candidate.tex';out=w/'outputs/root_B82_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B82_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B82_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
def mathematical(x):return {k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['lem:B-RD82-Newton','lem:B-RD82-terminal','prop:B-RD82-recovery','thm:B-RD82','rem:B-RD82-scope'],
 'proof_scope':'Every paragraph of the original complete candidate and entire exact checker read; exact final determinant-simplification diff read in full. All terminal-matrix and two-break steps independently rederived.',
 'proof_checks':[
  'Universal height-two coefficient bounds at absolute index eN give the two-slope vertices without requiring p not dividing e. The high F_p-line is inertia-stable and its character is killed by the tame degree-N extension; this gives integral alpha=s-B and low beta=B/p.',
  'The exact tame Honda framing gives high-line character zeta^(c-B), since s=pN. Two successive inverse Newton polygons at low targets give every primitive outside-high third-level valuation B/p^5. The residual determinant and high line are trivial over L, leaving only trivial or order-p residual wild image.',
  'At full division degree p^4 and B=pb with p not dividing b, all outside-high primitive coordinates have prime-to-p integral valuation b. The fixed-coefficient lower-break equality prevents any nonzero terminal matrix from killing an outside vector and makes every outside image uniformly high or uniformly low.',
  'Varying residual vectors (x,1) forces the lower-left entry to vanish. If the lower-right entry vanishes, the upper-left entry must also vanish. Hence the terminal space maps to F_p by the lower-right coefficient with kernel contained in F_p E12, so its dimension is at most two.',
  'The actual pth-power identity embeds V1 into V2, and the exact group order 4=epsilon+dimV1+dimV2 forces terminal dimension two. Both an actual E12 terminal element and an element with nonzero lower-right coefficient exist; no orbit-rank inference is used.',
  'A vector outside both high lines gives p|B2 in the common field. The E12 break rN=p^4(s-pb1)-b1 contradicts distinct high lines: the displacement gap is increasing in both b parameters and its maximum at e-1 equals -p^4(p+1).',
  'After high-line alignment, the nonzero lower-right element gives (p^4-1)(b2-b1)>=0; E12 gives (p^5+1)(b1-b2)>=0. Thus b1=b2 and equality of the actual high-line characters recovers c modulo N.',
  'Nontrivial residual wild inertia excludes a one-slope first polygon, since its injective leading-coordinate map would be fixed by wild inertia. The unique residual wild fixed lines align. Integrality for r<=4 forces B_i=pb_i; a prime-to-p b forces r=4 and the preceding proposition applies.',
  'If both B_i=p^2 k_i, then 1<=k_i<=p-2. The finite determinants directly give c1=c2 modulo p-1. Combining the common high-line characters gives k1=k2 modulo p-1, hence equality in this interval and then c1=c2 modulo N. This direct argument was proposed in this root audit and replaces unnecessary square/twist dependencies in the final candidate.',
  'The remaining residual-wild different-character orders satisfy 5<=r<=9: one residual dimension plus at most four in each congruence layer. Residual-tame exchanged high lines, larger images, existence and the unrestricted least-index interval remain open.'
 ],
 'dependencies_read_scope':'Freshly read complete B49-point coefficient proof and B49-inertia proof; complete B60-break proof; the B60 Newton argument through high-line integrality; complete B69-rules proof; B67 exact integral Honda framing and tame-averaging proof steps; complete B76-determinant and B77-square proofs; B50 actual common-twist and normalization proofs. The final simplified proof does not need the B77-square/B50 branches. No prime-to-p-index theorem is imported at the wild index without rederiving the needed coefficient step.',
 'primary_source_scope':'No new original-source reading. Earlier recorded Hopkins-Gross and Tate source bridges are used only in their previously audited scope. New terminal-matrix and break proofs are direct.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'isolated_program':str(dest.relative_to(w)),'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],'all_mathematical_fields_equal':True,
 'counts':independent['counts'],'executed_failures':[],
 'checkpoint_scope':'Separate post-freeze candidate audit. The frozen checkpoint29 paper, canonical sections and current gates are unchanged.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program rerun',
    'PASS: complete proof and checker read; Newton valuations, terminal matrices, opposite break inequalities and direct determinant recovery rederived. Literal isolated rerun agrees in all mathematical fields and preserves author output. Candidate only at CP29 freeze. See outputs/root_B82_audit.json.'])
 for label in ['lem:B-RD49-point','lem:B-RD49-inertia','lem:B-RD60-break','lem:B-RD69-rules','lem:B-RD67-normalization','lem:B-RD76-determinant']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run',
    'Invoked coefficient, inertia, lower-break, actual line-character, coordinate-framing or determinant proof steps freshly reread and explicitly reapplied; precise scope in outputs/root_B82_audit.json.'])
print(json.dumps(record,indent=2))

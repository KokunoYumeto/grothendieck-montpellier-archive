from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib,re
own=Path(__file__).resolve().parents[1]
p=own/'B_full_Iwahori_selected_point_candidate.tex'
old=p.read_text()
before='coefficient lemma carry the proof; a finite arithmetic supplement\nwill be retained separately and will not replace these arguments.\n'
after=r'''coefficient lemma carry the proof. The standalone exact supplement
\path{code/reduction_descent/verify_full_Iwahori_selected_point.py}
passed at 05:03:18.016815 UTC on 20 November 2026 in
11.402156060998095 seconds. It enumerates all 1,953,125 matrices
of the full Iwahori image and 15 actual field-image maps, checks
15,625,000 direct vector-stabilizer conditions and 187,500 literal
relative-quotient products in both the original and selected quotient
orientations, and checks 3,125 traceful conjugations. It independently
checks 2,625 binomial coefficients, 1,820 mixed-last-line inequalities,
3,366 exact Herbrand arithmetic cases, and the ten different-character
rows in the five orientations. These finite checks supplement the
complete actual-field proof; no numerical range proves a ramification
or existence assertion. The exact executed source, complete output
and stdout are retained. No checker failure occurred. The initial
abstract coefficient-lemma scope was explicitly restricted to totally
ramified extensions at the root auditor's request; its exact prior
source, wording delta and scope-repair record are retained.
'''
assert old.count(before)==1
new=old.replace(before,after)
history=own/'notes/B96_certificate_finalization'
history.mkdir(exist_ok=False)
(history/'candidate.before.tex').write_text(old)
(history/'candidate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='candidate.before.tex',tofile=p.name)))
p.write_text(new)
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
code=own/'code/verify_full_Iwahori_selected_point.py'
output=code.with_suffix('.output.json')
result=json.loads(output.read_text())
assert result['status']=='PASS'
record={'actual_utc':datetime.now(timezone.utc).isoformat(),
        'candidate':str(p),'candidate_sha256':sha(p),
        'labels':re.findall(r'\\label\{([^}]+)\}',new),
        'program':str(code),'program_sha256':sha(code),
        'output':str(output),'output_sha256':sha(output),
        'author_actual_utc':result['actual_utc'],
        'author_runtime_seconds':result['runtime_seconds'],
        'counts':result['counts'],
        'status':'CANDIDATE; complete proof and exact supplement await both full independent audits',
        'retention':'Exact initial candidate, total-ramification scope delta, pre-certificate candidate, diffs, executed code, full output and stdout retained. Outside frozen CP35; no shared file modification.'}
(own/'outputs/B96_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

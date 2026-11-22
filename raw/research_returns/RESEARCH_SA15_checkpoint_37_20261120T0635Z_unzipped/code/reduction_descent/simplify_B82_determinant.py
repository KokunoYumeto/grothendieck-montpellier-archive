from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib
own=Path(__file__).resolve().parents[1]
p=own/'B_first_wild_reducible_terminal_candidate.tex';raw=p.read_bytes()
expected='1fc957292d7075037e58964a058c77ca52c2460b610bc222329ca8dc05afffb1'
assert hashlib.sha256(raw).hexdigest()==expected
pre=own/'notes/B_first_wild_reducible_terminal.before_determinant_simplification.tex'
assert not pre.exists();pre.write_bytes(raw)
old=r'''The finite determinant characters
agree by the actual torsion determinant comparison.
If this common character is square,
Proposition~\ref{prop:B-RD77-square} already gives equality.
Otherwise apply a common finite height-one tame twist
to normalize the finite determinant to the primitive
level-one character, exactly as in B50 and B77.
This preserves the actual torsion isomorphism, both
polygons over \(L\), and the wild image. Now
\(c_i\equiv1\pmod{p-1}\). The common high-line character
gives \(c_1-B_1\equiv c_2-B_2\pmod N\), so'''
new=r'''The finite determinant characters
agree by the actual torsion determinant comparison: both
generic determinants are the same cyclotomic character
times a finite \(\mu_{p-1}\)-valued character, and reduction
is injective on these prime-to-\(p\) roots. Therefore
\(c_1\equiv c_2\pmod{p-1}\). The common high-line character
gives \(c_1-B_1\equiv c_2-B_2\pmod N\). Reducing this
congruence modulo \(p-1\), and using \(p^2\equiv1\)
there, proves'''
s=raw.decode();assert s.count(old)==1;s=s.replace(old,new);p.write_text(s)
now=datetime.now(timezone.utc).isoformat()
diff=''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),
                               fromfile='B82.before',tofile='B82.after'))
(own/'notes/B82_determinant_simplification.diff').write_text(diff)
record_path=own/'outputs/B82_candidate_record.json'
prior=record_path.read_bytes();(own/'notes/B82_candidate_record.before_simplification.json').write_bytes(prior)
record=json.loads(prior);record['actual_utc']=now
record['candidate_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
record['determinant_simplification']={
    'actual_utc':now,'previous_sha256':expected,'preserved':str(pre),
    'scope':'Root-proposed direct finite-determinant congruence replaces unnecessary square-character and finite-twist branch. No statement or certificate changed.',
    'prior_full_companion_audit':'../obstructions_crystals/B82_independent_audit.json',
    'delta_audit_pending':True}
record_path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'actual_utc':now,'candidate_sha256':record['candidate_sha256'],
                  'program_and_output_unchanged':True,'diff':diff},indent=2))

"""Promote the fully audited all-odd local wall theorem; no global-image claim."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib,csv
agent=Path(__file__).resolve().parents[1]
work=agent.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=agent/'ppav_all_odd_full_root_inertia_candidate.tex'
canonical=agent/'ppav_all_odd_full_root_inertia.tex'
expected='0bb79d06ae2ec1a09d9ad1ac3b9cbad85d34621d91357129a4a9c5c11a4de8cf'
assert sha(source)==expected and not canonical.exists()
audits=[work/'outputs/root_odd_wall_full_audit.json',
 work/'agents/reduction_descent/outputs/independent_odd_wall_full_audit.json',
 work/'agents/obstructions_crystals/odd_full_hyperplane_inertia_independent_audit.json']
for p in audits:
 d=json.loads(p.read_text())
 assert 'PASS' in p.read_text() and expected in p.read_text()
dependency=work/'agents/obstructions_crystals/A4_Moore_Fermat_nondivisibility.tex'
assert dependency.exists() and r'\status{Candidate' not in dependency.read_text()
before=source.read_text()
text,n=re.subn(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; independent audits passed.}',before)
assert n==5
text=text.replace('% Separate CP32 candidate. No global generation or connectedness is asserted.',
 '% Promoted after three complete independent proof audits; exact candidate retained.')
ending='is needed or claimed for the present deductions.\n\\end{remark}'
assert ending in text
text=text.replace(ending,
 'is needed or claimed for the present deductions.  The complete\n'
 'reduction/descent proof audit passed at 02:40:09.581059 UTC,\n'
 'the complete parent proof audit at 02:41:58.898779 UTC, and\n'
 'the complete obstruction/crystal proof audit at 02:42:18.498233 UTC,\n'
 'all on 20 November 2026.  Each checked the fixed-coordinate\n'
 'comparison, the maximal common-rank open, the all-member Euler\n'
 'model and the smooth-family image transfer.  The exact candidate\n'
 'and all detailed audit records are retained.\n\\end{remark}')
canonical.write_text(text)
history=agent/'history';history.mkdir(exist_ok=True)
diff=history/'ppav_all_odd_full_root_inertia_promotion.diff'
assert not diff.exists()
diff.write_text(''.join(difflib.unified_diff(before.splitlines(True),text.splitlines(True),
 fromfile=str(source.relative_to(work)),tofile=str(canonical.relative_to(work)))))
consolidate=work/'code/consolidate.py'
prior=consolidate.read_text()
anchor="   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')"
assert prior.count(anchor)==1 and 'A4_Moore_Fermat_nondivisibility.tex' in prior
addition=("   odd_full_inertia=a/'monodromy/ppav_all_odd_full_root_inertia.tex'\n"
 "   if odd_full_inertia.exists() and '\\\\status{Candidate' not in odd_full_inertia.read_text():\n"
 "    out.write('\\n'+odd_full_inertia.read_text()+'\\n')\n")
assert 'ppav_all_odd_full_root_inertia.tex' not in prior
after=prior.replace(anchor,addition+anchor)
saved=history/'pre_all_odd_full_root_inertia_code__consolidate.py'
assert not saved.exists();saved.write_text(prior)
shared_diff=saved.with_name(saved.name+'.diff')
shared_diff.write_text(''.join(difflib.unified_diff(prior.splitlines(True),after.splitlines(True),
 fromfile=str(saved.relative_to(work)),tofile=str(consolidate.relative_to(work)))))
consolidate.write_text(after)
now=datetime.now(timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',before)
record={'status':'PROMOTED','actual_utc':now,'candidate':str(source.relative_to(work)),
 'candidate_sha256':expected,'canonical':str(canonical.relative_to(work)),
 'canonical_sha256':sha(canonical),'labels':labels,
 'audits':[str(p.relative_to(work)) for p in audits],
 'algebra_dependency':str(dependency.relative_to(work)),
 'algebra_dependency_sha256':sha(dependency),
 'proof_diff':str(diff.relative_to(work)),'consolidate_before':str(saved.relative_to(work)),
 'consolidate_diff':str(shared_diff.relative_to(work)),
 'consolidate_sha256':sha(consolidate),
 'scope':'For every odd etale principal-cube pullback and every fixed odd principal-cube degree, the maximal common-rank wall is nonempty and supplies full hyperplane inertia. No global generation, connectedness, irreducibility or new exact full-image degree is claimed.',
 'new_numerical_run':False}
(agent/'outputs/ppav_all_odd_full_root_inertia_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(agent/'outputs/checkpoint32_required_all_odd_inertia.json').write_text(json.dumps(
 {'required':str(canonical.relative_to(work)),'canonical_sha256':sha(canonical),'note':'Parent owns the CP32 preparer.'},indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  if not label.startswith('subsec:'):
   wr.writerow([label,now,'/root/monodromy','PROMOTED-root-RD-OC-full-proof-PASS',record['scope']])
with (agent/'post_CP16_notes.md').open('a') as f:
 f.write('\n## '+now+' — Uniform odd full-inertia wall promoted\n\n'+record['scope']+
 ' The exact candidate and prior shared include file are retained with diffs. Only short proved statuses and completed audit metadata were changed in the canonical theorem. No previous canonical proof was modified and no mathematical experiment was rerun.\n')
assert sha(source)==expected
print(json.dumps(record,indent=2))

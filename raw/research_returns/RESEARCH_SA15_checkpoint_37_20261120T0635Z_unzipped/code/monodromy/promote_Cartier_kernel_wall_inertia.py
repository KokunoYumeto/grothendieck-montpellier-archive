"""Promote the audited conditional local Cartier-wall criterion only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib, csv

agent=Path(__file__).resolve().parents[1]; work=agent.parents[1]
candidate=agent/'post_CP30_Cartier_kernel_wall_inertia_candidate.tex'
canonical=agent/'Cartier_kernel_wall_inertia.tex'
expected='b6eb395dbbeafb4587486b34c22af5070af538b45cd8784cf48e3acdcf2be163'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)==expected and not canonical.exists()
audits=[work/'outputs/root_Cartier_kernel_wall_audit.json',work/'agents/obstructions_crystals/Cartier_kernel_wall_independent_audit.json']
for p in audits:
    x=json.loads(p.read_text()); assert 'PASS' in x['status']
    assert expected in p.read_text()
before=candidate.read_text()
text,n=re.subn(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; independent audits passed.}',before)
assert n==3
anchor='The common Cartier-incidence argument using the typed Moore slices\n'
assert anchor in text
text=text.replace(anchor,'The common Cartier-incidence argument\n(Corollary~\\ref{cor:DE-odd-principal-cube-kernel-birational})\nusing the typed Moore slices\n')
end='application.\n\\end{remark}'
assert end in text
text=text.replace(end,'application.  The complete parent proof audit passed at\n01:54:07.610775 UTC on 20 November 2026, and the complete\nobstruction/crystal proof audit passed at 01:54:54.065452 UTC.\nBoth independently reread the entire earlier Artin--Schreier proof.\nThe exact candidate and the two detailed audit records remain retained.\n\\end{remark}')
canonical.write_text(text)
diff=agent/'history/Cartier_kernel_wall_inertia_promotion.diff'
assert not diff.exists()
diff.write_text(''.join(difflib.unified_diff(before.splitlines(True),text.splitlines(True),fromfile=str(candidate.relative_to(work)),tofile=str(canonical.relative_to(work)))))
consolidate=work/'code/consolidate.py'; prior=consolidate.read_text()
assert "A4_common_Cartier_incidence.tex" in prior
anchor="   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')"
assert prior.count(anchor)==1
addition=("   kernel_wall=a/'monodromy/Cartier_kernel_wall_inertia.tex'\n"
          "   if kernel_wall.exists() and '\\\\status{Candidate' not in kernel_wall.read_text():\n"
          "    out.write('\\n'+kernel_wall.read_text()+'\\n')\n")
after=prior.replace(anchor,addition+anchor)
saved=agent/'history/pre_Cartier_kernel_wall_code__consolidate.py';assert not saved.exists();saved.write_text(prior)
shared_diff=saved.with_name(saved.name+'.diff')
shared_diff.write_text(''.join(difflib.unified_diff(prior.splitlines(True),after.splitlines(True),fromfile=str(saved.relative_to(work)),tofile=str(consolidate.relative_to(work)))))
consolidate.write_text(after)
now=datetime.now(timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',candidate.read_text())
record={'status':'PROMOTED','actual_utc':now,'candidate':str(candidate.relative_to(work)),'candidate_sha256':expected,'canonical':str(canonical.relative_to(work)),'canonical_sha256':sha(canonical),'labels':labels,'audits':[str(p.relative_to(work)) for p in audits],'proof_diff':str(diff.relative_to(work)),'consolidate_before':str(saved.relative_to(work)),'consolidate_diff':str(shared_diff.relative_to(work)),'scope':'Maximal kernel variation forces stable loss one, and any nonempty common Cartier wall supplies a full hyperplane radical. Wall nonemptiness and global generation remain unproved requirements; no unconditional monodromy degree added.'}
(agent/'outputs/Cartier_kernel_wall_inertia_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(agent/'outputs/checkpoint31_required_Cartier_kernel_wall.json').write_text(json.dumps({'required':str(canonical.relative_to(work)),'canonical_sha256':sha(canonical),'note':'Parent owns CP31 preparer.'},indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label in labels:wr.writerow([label,now,'/root/monodromy','PROMOTED-root-OC-full-proof-PASS',record['scope']])
with (agent/'post_CP16_notes.md').open('a') as f:
    f.write('\n## '+now+' — Conditional Cartier kernel-wall inertia promoted\n\n'+record['scope']+' The exact candidate remains unchanged. Status, completed-audit wording and an explicit common-incidence reference are the only canonical text changes. Prior shared-file bytes and exact diffs are retained; no proof or executed program was removed.\n')
assert sha(candidate)==expected
print(json.dumps(record,indent=2))

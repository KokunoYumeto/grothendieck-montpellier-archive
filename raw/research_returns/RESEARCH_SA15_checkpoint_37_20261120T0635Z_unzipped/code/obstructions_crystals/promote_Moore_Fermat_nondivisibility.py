"""Promote only after two complete audits supplied explicitly on the command line."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib,re,sys

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
candidate=own/'post_CP31_Moore_Fermat_nondivisibility_candidate.tex'
canonical=own/'A4_Moore_Fermat_nondivisibility.tex'
expected='35451b9383a4772ab7114cb9f47b444670bac239eedcd772def059475e0071f6'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert len(sys.argv)==3,'Pass the complete root and companion audit record paths.'
audits=[root/p for p in sys.argv[1:]]
assert all(p.exists()for p in audits)
assert sha(candidate)==expected and not canonical.exists()
prior=candidate.read_text()
text=re.sub(r'\\status\{Candidate[^}]*\}',r'\\status{Proved; complete independent proof/code audits passed.}',prior)
assert '\\status{Candidate'not in text
labels=re.findall(r'\\label\{((?:lem|thm|rem):[^}]+)\}',text)
assert len(labels)==5
history=own/'notes/CP32_Moore_Fermat_promotion'
history.mkdir(exist_ok=False)
(history/'candidate.tex').write_bytes(candidate.read_bytes())
(history/'promotion.diff').write_text(''.join(difflib.unified_diff(prior.splitlines(True),text.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
canonical.write_text(text)
consolidate=root/'code/consolidate.py'
old=consolidate.read_text()
(history/'consolidate.py').write_bytes(consolidate.read_bytes())
needle="   moore_parameters=a/'obstructions_crystals/A4_Moore_singular_parameters.tex'\n   if moore_parameters.exists() and '\\\\status{Candidate' not in moore_parameters.read_text():\n    out.write('\\n'+moore_parameters.read_text()+'\\n')\n"
assert old.count(needle)==1 and canonical.name not in old
addition="   moore_fermat=a/'obstructions_crystals/A4_Moore_Fermat_nondivisibility.tex'\n   if moore_fermat.exists() and '\\\\status{Candidate' not in moore_fermat.read_text():\n    out.write('\\n'+moore_fermat.read_text()+'\\n')\n"
new=old.replace(needle,needle+addition)
compile(new,str(consolidate),'exec');consolidate.write_text(new)
(history/'consolidate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='prior_consolidate.py',tofile='consolidate.py')))
now=datetime.now(timezone.utc).isoformat()
record={'status':'PROMOTED AFTER TWO FULL INDEPENDENT PROOF AND CODE AUDITS','actual_utc':now,
 'candidate':str(candidate.relative_to(root)),'candidate_sha256':expected,
 'canonical':str(canonical.relative_to(root)),'canonical_sha256':sha(canonical),'labels':labels,
 'audits':[str(p.relative_to(root))for p in audits],
 'author_program':'agents/obstructions_crystals/code/verify_Moore_Fermat_nondivisibility.py',
 'author_runtime_seconds':4.910654410996358,
 'changes':'Five short proved statuses and one coordinated optional include immediately after the Moore singular-parameter classification. Exact candidate and prior shared bytes/diffs retained. No workflow/current-table/build execution.',
 'scope':'Universal algebraic equivalence: Fermat divides the Moore determinant iff it vanishes identically. No actual same-coordinate geometric bridge or global monodromy assertion in this file.'}
rp=own/'Moore_Fermat_nondivisibility_promotion.json'
with rp.open('x')as f:json.dump(record,f,indent=2);f.write('\n')
with(own/'CHECK_EVENTS.tsv').open('a')as f:
 for label in labels:
  f.write('\t'.join([now,label,'promotion_after_two_full_independent_audits',str(canonical.relative_to(root)),
    'Universal remainder, repaired affine-line zero orbits, full-torus contradiction, independent-variable phases',
    'PROVED; universal algebraic scope',str(rp.relative_to(root))])+'\n')
with(own/'D_results.md').open('a')as f:
 f.write('\n\n## Exact Moore/Fermat nondivisibility — '+now+'\n\n')
 f.write('`A4_Moore_Fermat_nondivisibility.tex` proves that the Fermat cubic divides a characteristic-two 9-by-9 Moore determinant exactly when that determinant is identically zero. The lower-support argument uses actual remainder coefficients. The missing eight-support cube identities are repaired by the four zero-position orbits of a nonconcurrent affine-line configuration. Full support is excluded by three cubed product equations forcing a product of nonzero coordinates to vanish. The standalone universal checker retains all support and phase witnesses; the initial failed ideal expression and all exploratory limits are preserved. The separate same-coordinate Cartier bridge remains necessary for any geometric wall consequence.\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'canonical':record['canonical'],
                  'canonical_sha256':record['canonical_sha256'],'record':str(rp.relative_to(root))}))

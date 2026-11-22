"""Promote the fully audited common incidence and two authorized include edits."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib,re

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
candidate=own/'post_CP30_common_Cartier_incidence_candidate.tex'
canonical=own/'A4_common_Cartier_incidence.tex'
expected='a66b95b4de7a405fe4f0aa143a57ad5f6186254d530b846995de573206a5b8f7'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)==expected and not canonical.exists()
audits=[root/'outputs/root_common_Cartier_incidence_audit.json',
        root/'agents/reduction_descent/outputs/independent_common_Cartier_incidence_audit.json']
assert all(p.exists() for p in audits)
prior=candidate.read_text()
text=re.sub(r'\\status\{Candidate;[^}]+\}',
            r'\\status{Proved; complete root and reduction/descent audits passed.}',prior)
text=text.replace('\\status{Candidate scope; no full monodromy or divisorial-inertia conclusion.}',
                  '\\status{Proved scope; no divisorial inertia or full-group conclusion.}')
assert '\\status{Candidate' not in text
labels=re.findall(r'\\label\{((?:lem|prop|cor|rem):[^}]+)\}',text)
assert len(labels)==4
history=own/'notes/CP31_common_incidence_promotion'
history.mkdir(exist_ok=False)
(history/'candidate.tex').write_bytes(candidate.read_bytes())
(history/'promotion.diff').write_text(''.join(difflib.unified_diff(
    prior.splitlines(True),text.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
canonical.write_text(text)
consolidate=root/'code/consolidate.py'
old=consolidate.read_text()
(history/'consolidate.py').write_bytes(consolidate.read_bytes())
needle="   twisted_cartier=a/'monodromy/ppav_twisted_Cartier_Moore.tex'\n   if twisted_cartier.exists() and '\\\\status{Candidate' not in twisted_cartier.read_text():\n    out.write('\\n'+twisted_cartier.read_text()+'\\n')\n"
assert old.count(needle)==1
addition="   common_incidence=a/'obstructions_crystals/A4_common_Cartier_incidence.tex'\n   if common_incidence.exists() and '\\\\status{Candidate' not in common_incidence.read_text():\n    out.write('\\n'+common_incidence.read_text()+'\\n')\n"
assert canonical.name not in old
new=old.replace(needle,needle+addition)
log30=r'\\path{notes/ROOT_SEARCH_LOG_30.md}'
log31=r'\\path{notes/ROOT_SEARCH_LOG_31.md}'
assert new.count(log30)==1 and log31 not in new
new=new.replace(log30,log30+'\n'+log31)
compile(new,str(consolidate),'exec')
consolidate.write_text(new)
(history/'consolidate.diff').write_text(''.join(difflib.unified_diff(
    old.splitlines(True),new.splitlines(True),fromfile='prior_consolidate.py',tofile='consolidate.py')))
now=datetime.now(timezone.utc).isoformat()
record={'status':'PROMOTED AFTER TWO COMPLETE INDEPENDENT PROOF AUDITS',
        'actual_utc':now,'candidate':str(candidate.relative_to(root)),
        'candidate_sha256':expected,'canonical':str(canonical.relative_to(root)),
        'canonical_sha256':sha(canonical),'labels':labels,
        'audits':[str(p.relative_to(root)) for p in audits],
        'changes':'Only short proved statuses, one coordinated optional include after the cubic Moore bridge, and parent-requested ROOT_SEARCH_LOG_31 path immediately after LOG30. Candidate and prior shared bytes/diffs retained. No build/current table/review execution.',
        'numerical_scope':'No new computation needed or claimed; complete typed tensor and geometric proof.',
        'scope':'Actual common section/dual maximal-rank incidence, sharpness of this pullback family, and birational dual kernel map for every fixed odd principal-cube degree. No wall-intersection, local-inertia or full-global-group assertion.'}
rp=own/'common_Cartier_incidence_promotion.json'
with rp.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join([now,label,'promotion_after_two_full_independent_audits',str(canonical.relative_to(root)),
                      'Exact tensor triality, actual character blocks, common incidence and differential criterion',
                      'PROVED; typed rank and birational scope',str(rp.relative_to(root))])+'\n')
with (own/'D_results.md').open('a') as f:
 f.write('\n\n## Actual common Cartier incidence — '+now+'\n\n')
 f.write('`A4_common_Cartier_incidence.tex` proves that the same actual section and its actual left kernel attain maximal multiplication rank and maximal dual alternating rank. The exact Moore tensor reindexing supplies every nontrivial character multiplication determinant; the degree-one symmetrizer makes the trivial left kernel a fixed linear function of the section. Their nonempty opens meet in one nine-dimensional section space. The chosen etale pullback is smooth, connected and relatively Frobenius-bijective. The previously proved differential criterion then makes the dual kernel map birational for every fixed odd principal-cube degree. The wall-intersection, divisorial-inertia and full-group requirements remain separate. Root and reduction/descent completed full independent proofs; no additional numerical experiment is used.\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'canonical':record['canonical'],
                  'canonical_sha256':record['canonical_sha256'],'record':str(rp.relative_to(root))}))

from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];work=own.parents[1]
items=[(85,'B_first_wild_diagonal_projection','7ae032b8394c8209094c53cdbf26d13d23868fd3c39ab026841527f9dd65cb18',
        'Actual second-level degree-p point fields force both diagonal projections. For p=1mod4, the tame reducible sector has wild order at leastp6; no bound across other residual types.',3),
       (86,'B_first_wild_cyclotomic_quotient','ad8b70dc7b353f54ac8833794a2f962d916ec6f663f31f616fef85ddb33ddee6',
        'The actual cyclotomic subfield excludes W1=W2=sl2. Together with B85, the tame reducible p=1mod4 sector has wild order at leastp7; p5 tame ambiguity only at5^7 or5^8, with B25/75. Full index remains{2,3}.',4)]
records=[]
for number,stem,expected,scope,count in items:
    candidate=own/(stem+'_candidate.tex');raw=candidate.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    root=json.loads((work/f'outputs/root_B{number}_audit.json').read_text())
    oc=json.loads((own.parent/f'obstructions_crystals/B{number}_independent_audit.json').read_text())
    assert root['candidate_sha256']==oc['candidate_sha256']==expected
    assert all('PASS' in a['status'] for a in (root,oc))
    pre=own/('notes/'+stem+'.prepromotion.tex');assert not pre.exists();pre.write_bytes(raw)
    s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion proof and exact-code audits passed.}',raw.decode())
    first=s.splitlines()[0];s=s.replace(first,'% Proved after checkpoint30 archive release; exact candidate and full audits retained.',1)
    if number==86:
        old=('The separate B85 dependency must itself\n'
             'have completed audits before this corollary is\n'
             'promoted. All current proofs remain outside the\n'
             'frozen checkpoint30.')
        assert old in s
        s=s.replace(old,'The separate B85 dependency and this full proof\n'
                        'both completed independent audits before promotion.\n'
                        'They were promoted after the immutable checkpoint30\n'
                        'archive and first enter the following checkpoint.')
    paragraph=('\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
               'The complete independent root and companion audits passed.\n'
               'Their author-output-preserving exact reruns took\n'
               f"\\({root['independent_runtime_seconds']}\\) and\n"
               f"\\({oc['independent_runtime_seconds']}\\) seconds, respectively.\n"
               'Their exact proof and source read scopes, all prior\n'
               'candidate bytes and every executed output remain retained.\n')
    assert s.count(r'\end{remark}')==1;s=s.replace(r'\end{remark}',paragraph+r'\end{remark}')
    canonical=own/(stem+'.tex');assert not canonical.exists();canonical.write_text(s)
    labels=re.findall(r'\\label\{([^}]+)\}',s)
    assert labels==root['labels']==oc['labels'] and len(labels)==count
    assert r'\status{Candidate' not in s
    now=datetime.now(timezone.utc).isoformat()
    record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
            'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
            'audited_candidate_sha256':expected,'preserved_candidate':str(pre),'labels':labels,
            'root_audit':f'../../outputs/root_B{number}_audit.json','root_audit_utc':root['actual_utc'],
            'root_runtime_seconds':root['independent_runtime_seconds'],
            'companion_audit':f'../obstructions_crystals/B{number}_independent_audit.json',
            'companion_audit_utc':oc['actual_utc'],'companion_runtime_seconds':oc['independent_runtime_seconds'],
            'author_runtime_seconds':root['author_runtime_seconds'],'scope':scope,
            'source_scope':('Full internal B60/B69/B83 arguments; no new original-source reading.' if number==85 else
                            'Fresh Stacks032A full proof and Colmez2.12/3.7 full original proofs; exact per-auditor scope retained.'),
            'checkpoint_scope':'Post-CP30 canonical for CP31; immutable CP30 unchanged.','executed_failures':[]}
    (own/f'outputs/B{number}_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
    (own/f'notes/B{number}_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
    with (own/'CHECK_EVENTS.tsv').open('a') as f:
        for label in labels:
            f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,
                              f'{stem}.tex;outputs/B{number}_promotion.json',
                              'Full root+OC proof/code audits; exact source scope and candidate retained'])+'\n')
    with (own/'STATUS_CURRENT.md').open('a') as f:
        f.write(f'\n## {now} — B{number} promoted\n\n{scope}\n')
    records.append(record)
history=own/'notes/CP31_before_B85_B86_wiring';assert not history.exists();history.mkdir()
path=work/'code/consolidate.py';before=path.read_bytes();text=before.decode()
old="'B_tame_residual_one_prime_recovery.tex']:"
new="'B_tame_residual_one_prime_recovery.tex',\n                    'B_first_wild_diagonal_projection.tex',\n                    'B_first_wild_cyclotomic_quotient.tex']:"
assert text.count(old)==1;after=text.replace(old,new)
(history/path.name).write_bytes(before)
(history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(text.splitlines(True),after.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')))
path.write_text(after)
wiring={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
        'path':'code/consolidate.py','before_sha256':hashlib.sha256(before).hexdigest(),
        'after_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'prior_versions':str(history),'changes':['B85 and B86 canonicals after B84'],
        'workflow_scope':'Parent/OC own prepare/update31; neither edited.'}
(own/'outputs/B85_B86_CP31_wiring.json').write_text(json.dumps(wiring,indent=2)+'\n')
print(json.dumps({'promotions':records,'wiring':wiring},indent=2))

from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re

own=Path(__file__).resolve().parents[1];work=own.parents[1]
candidate=own/'B_first_wild_Cartan_exclusion_candidate.tex'
raw=candidate.read_bytes()
expected='8b7c13a40f6c40f2f55a54d3d17a5c214e01c4456cbf0a0c81eeb27462da332b'
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B81_audit.json').read_text())
mono=json.loads((own.parent/'monodromy/outputs/independent_B81_Cartan_exclusion_audit.json').read_text())
assert root['candidate_sha256']==mono['source_sha256']==expected
assert 'PASS' in root['status'] and 'PASS' in mono['status']
preserved=own/'notes/B_first_wild_Cartan_exclusion.prepromotion.tex'
assert not preserved.exists();preserved.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and monodromy proof and exact-code audits passed.}',raw.decode())
s=s.replace('% Separate post-CP28 candidate; no claim about larger or reducible wild images.',
            '% Proved after complete independent audits; larger and reducible wild images remain open.')
needle='reread. No new original-source read is claimed.'
assert s.count(needle)==1
s=s.replace(needle,needle+r'''
The complete independent root and monodromy audits passed,
including every boundary coefficient and the actual Cartan
dependencies. Their unchanged isolated certificate reruns took
\(0.45372015300381463\) and \(0.4650933469965821\) seconds,
respectively, preserving the author output. The exact audited
candidate and all proof/code audit records are retained.''')
canonical=own/'B_first_wild_Cartan_exclusion.tex';assert not canonical.exists()
canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==[a['label'] for a in mono['assertions']]
assert len(labels)==4 and r'\status{Candidate' not in s
now=datetime.now(timezone.utc).isoformat()
scope=('At e=p(p-1), an actual p^3-congruent different-special-character pair with irreducible '
       'residual inertia cannot have wild order p^4. Combined with B79, remaining wild orders '
       'are p^5 through p^8; at p5/e20 the minimum is3125. No larger-image, reducible-residual, '
       'whole-CM, existence or unrestricted recovery assertion.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
        'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
        'audited_candidate_sha256':expected,'preserved_candidate':str(preserved),
        'labels':labels,'root_audit':'../../outputs/root_B81_audit.json',
        'root_audit_utc':root['actual_utc'],'root_runtime_seconds':root['independent_runtime_seconds'],
        'companion_audit':'../monodromy/outputs/independent_B81_Cartan_exclusion_audit.json',
        'companion_audit_utc':mono['actual_utc'],'companion_runtime_seconds':mono['exact_program_runtime_seconds'],
        'author_runtime_seconds':0.4355178660043748,'scope':scope,
        'source_scope':'Full internal B79/B80 proofs and code reread by both auditors; no fresh primary-source claim.',
        'checkpoint_scope':'CP29; immutable CP28 unchanged. Shared wiring awaits norm13 writer release.',
        'executed_failures':[]}
(own/'outputs/B81_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,
                          'B_first_wild_Cartan_exclusion.tex;outputs/B81_promotion.json',
                          'Full root+monodromy proof/code audits; candidate and author output preserved'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## '+now+' — B81 promoted: actual fourth-order Cartan excluded\n\n'+scope+'\n')
print(json.dumps(record,indent=2))

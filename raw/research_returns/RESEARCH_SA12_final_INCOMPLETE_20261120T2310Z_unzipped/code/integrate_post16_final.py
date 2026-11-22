"""Integrate the audited local Brauer-zero extension and finite-jet repairs."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
cm=json.loads((root/'parts/C/post16_research/integration_manifest_C_finite_jet_gluing.json').read_text())
dm=json.loads((root/'parts/D/post16_research/integration_manifest_local_Brauer_zero_D.json').read_text())
assert {a['auditor'] for a in cm['audits']}=={'/root','/root/part_b','/root/part_c','/root/part_d'}
assert set(dm['audit_scope'])=={'root','B','C','D'}
files=cm['files']+[dict(path=dm['path'],sha256=dm['sha256'])]
extra=root/'parts/D/post16_research/integration_manifest_Brauer_simple_product_root.json'
sm=json.loads(extra.read_text()) if extra.exists() else None
if sm:
    assert set(sm['audits'])=={'root','B','C','D'}
    files.append(dict(path=sm['path'],sha256=sm['sha256']))
pattern=re.compile(r'\\begin\{(proposition|corollary|lemma|example|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
cols=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
with (root/'parts/D/results_D.csv').open() as f:rows=list(csv.DictReader(f))
known={r['id'] for r in rows};added=[];labels=[]
for info in files:
    p=root/info['path'];source=p.read_text()
    assert hashlib.sha256(p.read_bytes()).hexdigest()==info['sha256']
    for m in pattern.finditer(source):
        assert m[2].startswith('Proved:'),(info['path'],m[2])
        labels.append(m[3])
        if m[3] in known:continue
        local=m[3] in dm['labels']
        note=('Complete-local surface extension of the one Brauer-zero main reduction. No algebraization hypothesis; fixed Picard generators and source-factorization tensor jets give q^(C r^2) for zero geometric Brauer image and unbounded scalar order. All four full actual-file and scoped primary audits passed; nonzero Brauer classes and full finite generation remain open.' if local else
              'Four complete actual-file audits. Auxiliary fixed-A-chain finite-jet and actual-full-bundle Artinian theorem, or formal selected-simple-product consequence of the one Brauer-zero reduction. Exact transverse/fixed-resolution or selected-kernel scope stated. Not an additional independent movement event.')
        rows.append(dict(id=m[3],statement=m[2].split(':',1)[1].strip(),status='Proved',where_proved=info['path']+': label '+m[3],depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',source)))),manuscript_pages='29/061,066',notes=note))
        known.add(m[3]);added.append(m[3])
    p=root/'parts/D/paper_D.tex';s=p.read_text();line='\\input{'+info['path']+'}'
    if line not in s:p.write_text(s+'\n'+line+'\n')
with (root/'parts/D/results_D.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)

p=root/'parts/D/references_D.bib';s=p.read_text();keys=set(re.findall(r'@\w+\{([^,]+),',s))
if not set(dm['bibliography_keys'])<=keys:
    assert not (set(dm['bibliography_keys'])&keys)
    b=(root/dm['bibliography']).read_text()
    assert hashlib.sha256(b.encode()).hexdigest()==dm['bibliography_sha256']
    p.write_text(s+'\n\n'+b)

p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
with (root/'parts/C/post16_research/CHECK_EVENTS_C_post16.tsv').open() as f:
    for e in csv.DictReader(f,delimiter='\t'):
        if e['label'] not in added:continue
        actor=e['auditor'].rsplit('; ',1)[-1]
        events.append(dict(statement_id=e['label'],date=now,who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type=e['type'],outcome=e['result']+' Recorded here at integration; original author event retained.'))
for manifest in [dm]+([sm] if sm else []):
    for e in manifest['events']:
        if e['label'] not in added:continue
        actor='/root' if e['actor']=='root' else '/root/part_'+e['actor'].lower()
        events.append(dict(statement_id=e['label'],date=e['recorded_utc'],who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type=e['kind'],outcome=e['status']+': '+e['scope']))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)

p=root/'parts/D/unresolved_D.tex';s=p.read_text()
s=s.replace('Complete local punctures, the remaining cross-characteristic\nfamilies and alternating multiplicities require their separate arguments.',
            'The remaining cross-characteristic families and alternating\nmultiplicities require their separate arguments. The local surface\nBrauer-zero extension is stated below.')
marker='% Post-checkpoint16 local Brauer-zero and finite-jet closure'
if marker not in s:
    s+='\n\n'+marker+r'''
\paragraph{The complete local Brauer-zero extension.}
Theorem~\ref{D:local-Brauer-zero-projective-growth} gives the same
$q^{Cr^2}$ count on the puncture of every complete excellent normal
equicharacteristic surface ring with algebraically closed coefficient
field, without a finite-type algebraization hypothesis.
Lemma~\ref{D:local-Picard-prime-to-p-generators} supplies fixed
generators modulo every prime-to-$p$ integer.
Proposition~\ref{D:local-fixed-tensor-cyclic-atlas} lifts the entire
tensor source from fixed jets using source identity factorizations;
the source itself need not be MCM or coefficient-flat. This is the
local scope of the same Brauer-zero reduction. It leaves nonzero
geometric Brauer classes, higher-dimensional local extensions outside
its hypotheses, and full generation unresolved.

\paragraph{Finite jets and their actual-bundle families.}
Proposition~\ref{D:A-chain-finite-jet-framing} replaces whole-branch
compatibility on an $A$-chain by fixed finite jets when attachments
are pairwise distinct and transverse. The inverse-Cartan reflection
identity and Schur complement give total length $O(n)$ in
Corollary~\ref{D:A-block-total-jet-budget}.
Proposition~\ref{D:RDP-Artinian-full-bundle-framing} proves rigidity
and the exact jet obstruction over Artinian coefficients for actual
vector bundles on the fixed resolution with full closed fibres.
It does not identify arbitrary relative MCM pullbacks with such
bundles, vary the resolution, control coincident-branch contacts,
or supply an effective hereditary object atlas. These three units
are auxiliary and do not create another movement event.
'''
if sm and '\\ref{D:Brauer-zero-selected-simple-product}' not in s:
    s+=r'''
\paragraph{The selected simple-product consequence.}
Corollary~\ref{D:Brauer-zero-selected-simple-product} proves finite
generation of the product defined by the selected Brauer-zero simple
quotient kernels, whenever the fixed faithful projective embeddings
satisfy $|H|\ge q^{\epsilon r^2}$. It includes no unselected kernel
of the same simple types and gives no general crown bound. This is
a consequence of the single Brauer-zero count, not separate movement.
'''
p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
s=s.replace('This packet does not yet cover complete local punctures, alternating multiplicities or general crowns, and does not close any requested row.',
            'Its separately proved complete-local surface extension has the same unbounded-centre Brauer-zero conclusion without an algebraization hypothesis. Alternating multiplicities and general crowns remain open, and no requested row closes.')
paragraph='The complete-local Brauer-zero extension is now proved by fixed Picard generators modulo all prime-to-p orders and exact whole-tensor finite-jet maps. Source identity factorizations permit the prescribed-map lifting even when the tensor source is not MCM; the target regular sequence and a fixed image ideal give the actual punctured isomorphism. All four audits passed. The same count implies finite generation of the product of the specifically selected Brauer-zero simple quotient kernels under the stated order lower bound; unselected kernels remain outside it. These are the completed local scope and direct consequences of the one post-review10 Brauer-zero reduction.'
aux='Three further auxiliary units prove a module-independent finite-jet framing criterion on transverse A-chains, a total jet length linear in cover degree, and Artinian rigidity and precise framed-map obstruction for actual full-bundle families on a fixed resolution. Their variable and degree bounds do not yet provide the effective global hereditary object atlas; coincident branch contacts, arbitrary relative-MCM pullbacks and moving resolutions are not included.'
for para in [paragraph,aux]:
    if para not in s:s=s.replace("'','## Files and continuation','',",repr(para)+",\n'','## Files and continuation','',")
p.write_text(s)
record=dict(utc=now,labels=labels,added_rows=len(added),files=files,main_reduction='Complete-local surface scope of the same Brauer-zero reduction',additional_independent_movement_events=0,auxiliary_labels=cm['labels'],requested_status_changes=[],archive_created=False)
(root/'code/output/integrate_post16_final.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

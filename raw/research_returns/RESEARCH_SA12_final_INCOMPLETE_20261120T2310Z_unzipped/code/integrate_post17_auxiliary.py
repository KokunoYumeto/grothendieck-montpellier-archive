"""Assemble three audited auxiliary inputs, preserving their realization limits."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re
root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
manifest_paths = [
    'parts/C/post17_research/integration_manifest_C_uniform_generation.json',
    'parts/D/post17_research/integration_manifest_single_curve_Brauer_D.json']
manifests = [json.loads((root / p).read_text()) for p in manifest_paths]
pattern = re.compile(r'\\begin\{(proposition|corollary|lemma|example|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
columns = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
p = root / 'parts/D/results_D.csv'
with p.open() as f:
    rows = list(csv.DictReader(f))
known = {r['id'] for r in rows}
added = []; labels = []; files = []; new_events = []
for m in manifests:
    assert set(m['audit_scope']) == {'root','B','C','D'}
    p = root / m['path']; source = p.read_text()
    assert hashlib.sha256(p.read_bytes()).hexdigest() == m['sha256']
    units = list(pattern.finditer(source))
    assert {u[3] for u in units} == set(m['labels'])
    assert all(u[2].startswith('Proved:') for u in units)
    files.append(dict(path=m['path'], sha256=m['sha256']))
    for u in units:
        labels.append(u[3])
        if u[3] in known:
            continue
        scope = m['scope_precision']
        if isinstance(scope, list): scope = ' '.join(scope)
        rows.append(dict(id=u[3], statement=u[2].split(':',1)[1].strip(), status='Proved',
            where_proved=m['path'] + ': label ' + u[3],
            depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',source)))),
            manuscript_pages='29/061,066', notes=scope + ' Four complete actual-file audits. '
            + m.get('movement_classification',m.get('movement',''))))
        added.append(u[3]); known.add(u[3])
        for actor, audit in m['audit_scope'].items():
            who = '/root' if actor == 'root' else '/root/part_' + actor.lower()
            new_events.append(dict(statement_id=u[3],date=m['recorded_utc'],
                who='GPT-6 Astra Pro; '+who+'; SA12 run1; effort setting not independently exposed',
                type='targeted proof check',outcome='PASS: '+audit))
    p = root / 'parts/D/paper_D.tex'; text = p.read_text()
    line = '\\input{' + m['path'] + '}'
    if line not in text: p.write_text(text + '\n' + line + '\n')
    b = m['bibliography']
    if isinstance(b,str):
        b = dict(path=b,sha256=m['bibliography_sha256'],keys=m['bibliography_keys'])
    bp = root / b['path']; bs = bp.read_text()
    assert hashlib.sha256(bp.read_bytes()).hexdigest() == b['sha256']
    assert 'Opened' in bs
    p = root / 'parts/D/references_D.bib'; text = p.read_text()
    old = set(re.findall(r'@\w+\{([^,]+),',text))
    assert not (set(b['keys']) & old) or set(b['keys']) <= old
    if not set(b['keys']) <= old: p.write_text(text + '\n' + bs)
assert len(labels) == 3
with (root/'parts/D/results_D.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(rows)
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f: events=list(csv.DictReader(f,delimiter='\t'))
events.extend(new_events)
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(events)
p=root/'parts/D/unresolved_D.tex';s=p.read_text()
marker='% Post-checkpoint17 generation charts and one-curve residues'
if marker not in s:
    s+='\n\n'+marker+r'''
\paragraph{Generation and a fixed-determinant object chart.}
Theorem~\ref{D:reflexive-pullback-uniform-generation} proves
uniform generation after one exceptional-cycle twist, using
automatic adjunction on every effective subcycle, including
nilpotent layers and the point-ideal Tor term.
Proposition~\ref{D:hereditary-fixed-determinant-cycle-chart}
combines the fixed Noether-different ideal with the energy
estimate and the cyclic Frobenius determinant recurrence.
It gives an actual $O(nr^2)$-coordinate section chart for a fixed
determinant on one finite exceptional cycle. Its energy-family
and complete-base hypotheses are explicit. The unresolved step
is finite-thickening realization and determination of the unit
objects, all Frobenius arrows and specified isomorphisms over
Artinian bases, with the same complexity. The chart alone
gives no hereditary representation count.

\paragraph{One smooth exceptional curve and a period-degree cover.}
Proposition~\ref{D:single-curve-Brauer-residue-cover} identifies
the prime-to-$p$ Brauer torsion with curve-character cohomology
and kills a period-$m$ class by a cyclic degree-$m$ cover
etale over the entire resolution. Genus and normal degree
scale as stated in that proposition. Constants on these
varying covers still need uniform control. A splitting cover
alone does not supply a global Clifford rank drop or a
formal weight-block decomposition. These three statements
are auxiliary; no main gate or requested status changes.
'''
p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
paragraph=('Three further audited auxiliary inputs are assembled. Uniform generation of '
    'reflexive pullbacks follows from the full nonreduced-cycle automatic-adjunction argument. '
    'A fixed Noether-different ideal and the integral energy cycle yield O(nr²) actual '
    'fixed-determinant section coordinates on a finite exceptional thickening, within the '
    'explicit complete-base and established energy family. Effective unit-object realization, '
    'Frobenius arrows and specified isomorphisms remain unresolved. Separately, when the '
    'resolution has one smooth exceptional curve, every prime-to-p Brauer class of period m '
    'is killed by a cyclic degree-m cover étale over the whole resolution. Its varying-cover '
    'constants are not yet uniform. These inputs create no main movement.')
if paragraph not in s:
    s=s.replace("'','## Files and continuation','',",repr(paragraph)+",\n'','## Files and continuation','',")
p.write_text(s)
record=dict(utc=now,labels=labels,added_rows=len(added),added_events=len(new_events),files=files,
    additional_independent_movement_events=0,requested_status_changes=[],archive_created=False)
(root/'code/output/integrate_post17_auxiliary.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

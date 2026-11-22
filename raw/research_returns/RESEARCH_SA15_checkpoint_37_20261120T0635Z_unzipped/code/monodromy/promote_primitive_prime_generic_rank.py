"""Parent-authorized promotion; requires both complete independent audits."""
from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re

agent = Path(__file__).resolve().parents[1]
root = agent.parents[1]
candidate = agent / 'post_CP35_primitive_prime_generic_rank_candidate.tex'
canonical = agent / 'primitive_prime_generic_rank.tex'
expected = '77705a12007f8963cf18df5382b9472b74bcf661404c19fb3ae42e3169e0fe2f'
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(candidate) == expected and not canonical.exists()
audits = [root / 'outputs/root_primitive_prime_generic_rank_audit.json',
          root / 'agents/obstructions_crystals/primitive_prime_generic_rank_independent_audit.json']
for audit in audits:
    record = json.loads(audit.read_text())
    assert 'PASS' in record['status']
    assert record['candidate_sha256'] == expected
before = candidate.read_text()
after, count = re.subn(r'\\status\{Candidate[^}]*\}',
                      lambda _: r'\status{Proved; independent audits passed.}', before)
assert count == 5
after = after.replace('% Isolated candidate. No canonical or checkpoint input is changed.',
                      '% Promoted after complete independent root and companion proof audits.')
history = agent / 'notes/CP36_primitive_prime_generic_rank_promotion'
history.mkdir(parents=True, exist_ok=False)
(history / 'candidate.tex').write_text(before)
(history / 'promotion.diff').write_text(''.join(difflib.unified_diff(
    before.splitlines(True), after.splitlines(True),
    fromfile=candidate.name, tofile=canonical.name)))

con = root / 'code/consolidate.py'
cfg = root / 'notes/checkpoint36_promoted_inputs.json'
changes = root / 'notes/checkpoint36_changes.md'
log = root / 'notes/ROOT_SEARCH_LOG_36.md'
old = {p: p.read_text() for p in (con, cfg, changes, log)}
anchor = "    out.write('\\n'+prime_Heisenberg_rank.read_text()+'\\n')\n"
assert old[con].count(anchor) == 1
addition = ("   primitive_prime_generic_rank=a/'monodromy/primitive_prime_generic_rank.tex'\n"
            "   if primitive_prime_generic_rank.exists() and '\\\\status{Candidate' not in primitive_prime_generic_rank.read_text():\n"
            "    out.write('\\n'+primitive_prime_generic_rank.read_text()+'\\n')\n")
newcon = old[con].replace(anchor, anchor + addition)
paths = json.loads(old[cfg]); canonical_path = str(canonical.relative_to(root))
assert canonical_path not in paths
paths.insert(paths.index('agents/monodromy/prime_Heisenberg_rank.tex') + 1, canonical_path)
newcfg = json.dumps(paths, indent=2) + '\n'
now = datetime.now(timezone.utc).isoformat()
scope = ('For every fixed nonordinary abelian surface and ample globally generated '
         'type(1,p) line bundle, p=3,5,7,11,13,17, a nonempty smooth open has '
         'genus p+1 and p-rank f(A)+p-1. The any-prime statement is conditional '
         'on actual maximal dual rank. No good-wall or full-monodromy inference.')
newchanges = old[changes] + ('\n## Generic sharpness of certified primitive prime systems\n\n'
    + 'Promoted ' + now + ' after full root and OC proof audits. ' + scope
    + ' The proof uses actual Cartier nonvanishing, birational Pfaffian radicals, '
    'the polynomial Q=sum(y_i sigma_i^2) with dQ=sigma^2, and the whole-space Euler '
    'map. Smooth members follow from odd principal descent and explicit nodal '
    'smoothing. There is no new numerical run or unsupported Bertini assertion. '
    'The candidate, all prior inputs and exact promotion differences are retained.\n')
newlog = old[log] + ('\n## Primitive prime Euler and smooth-member consequence\n\n'
    + 'Promoted ' + now + '. The full canonical odd theta-descent, primitive Euler '
    'construction, odd-Cartier-surjection and prime-Heisenberg proofs were reread. '
    'No new primary-source opening or numerical experiment is claimed. The proof '
    'uses the nonvanishing open of Q, not an unproved intersection of Q=0 with '
    'the birational isomorphism open. Full audit records are '
    'outputs/root_primitive_prime_generic_rank_audit.json and '
    'agents/obstructions_crystals/primitive_prime_generic_rank_independent_audit.json.\n')
new = {con: newcon, cfg: newcfg, changes: newchanges, log: newlog}
for path in old:
    (history / (path.name + '.before')).write_text(old[path])
    (history / (path.name + '.diff')).write_text(''.join(difflib.unified_diff(
        old[path].splitlines(True), new[path].splitlines(True),
        fromfile='before/' + path.name, tofile=path.name)))
canonical.write_text(after)
for path in new:
    path.write_text(new[path])
labels = re.findall(r'\\label\{([^}]+)\}', before)
record = {'status': 'PROMOTED', 'actual_utc': now,
          'candidate': str(candidate.relative_to(root)), 'candidate_sha256': expected,
          'canonical': canonical_path, 'canonical_sha256': digest(canonical),
          'labels': labels, 'audits': [str(p.relative_to(root)) for p in audits],
          'scope': scope, 'new_computation_at_promotion': False,
          'consolidate_sha256': digest(con), 'config_sha256': digest(cfg)}
(agent / 'outputs/primitive_prime_generic_rank_promotion.json').write_text(
    json.dumps(record, indent=2) + '\n')
with (agent / 'CHECK_EVENTS_post_CP16.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([label, now, '/root/monodromy',
            'PROMOTED-ROOT-OC-FULL-PROOF-PASS', scope]) + '\n')
assert digest(candidate) == expected
print(json.dumps(record, indent=2))

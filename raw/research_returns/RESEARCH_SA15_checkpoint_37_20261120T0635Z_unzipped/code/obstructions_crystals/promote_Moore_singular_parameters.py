"""Promote the fully audited universal Moore theorem and its single include."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import difflib
import re

root = Path(__file__).resolve().parents[3]
own = root/'agents/obstructions_crystals'
candidate = own/'post_CP30_Moore_singular_parameter_classification_candidate.tex'
canonical = own/'A4_Moore_singular_parameters.tex'
expected = '234608ae83437e80577d715b17f43bcc075c8fef479d444e2c2cf52c1a343067'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate) == expected and not canonical.exists()
audits = [root/'outputs/root_Moore_classification_audit.json',
          root/'agents/reduction_descent/outputs/independent_Moore_classification_audit.json',
          root/'agents/monodromy/outputs/independent_Moore_singular_parameter_audit.json']
assert all(p.exists() for p in audits)
old = candidate.read_text()
text = re.sub(r'\\status\{Candidate;[^}]+\}',
              r'\\status{Proved; complete root and companion proof/code audits passed.}', old)
text = text.replace('\\status{Candidate scope; no Cartier or fixed-surface rank implication asserted.}',
                    '\\status{Proved scope; no geometric implication from this algebra alone.}')
assert '\\status{Candidate' not in text
labels = re.findall(r'\\label\{((?:lem|thm|rem):[^}]+)\}', text)
assert len(labels) == 4
history = own/'notes/CP31_Moore_classification_promotion'
history.mkdir(exist_ok=False)
(history/'candidate.tex').write_bytes(candidate.read_bytes())
(history/'promotion.diff').write_text(''.join(difflib.unified_diff(
    old.splitlines(True), text.splitlines(True), fromfile=candidate.name, tofile=canonical.name)))
canonical.write_text(text)
consolidate = root/'code/consolidate.py'
previous = consolidate.read_text()
(history/'consolidate.py').write_bytes(consolidate.read_bytes())
needle = "   principal_bridge=a/'monodromy/principal_theta_Cartier_bridge.tex'\n   if principal_bridge.exists() and '\\\\status{Candidate' not in principal_bridge.read_text():\n    out.write('\\n'+principal_bridge.read_text()+'\\n')\n"
assert previous.count(needle) == 1
addition = "   moore_parameters=a/'obstructions_crystals/A4_Moore_singular_parameters.tex'\n   if moore_parameters.exists() and '\\\\status{Candidate' not in moore_parameters.read_text():\n    out.write('\\n'+moore_parameters.read_text()+'\\n')\n"
assert canonical.name not in previous
updated = previous.replace(needle, needle+addition)
compile(updated, str(consolidate), 'exec')
consolidate.write_text(updated)
(history/'consolidate.diff').write_text(''.join(difflib.unified_diff(
    previous.splitlines(True), updated.splitlines(True),
    fromfile='prior_consolidate.py', tofile='consolidate.py')))
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'PROMOTED AFTER THREE FULL INDEPENDENT PROOF/CODE AUDITS',
    'actual_utc': now,
    'candidate': str(candidate.relative_to(root)),
    'candidate_sha256': expected,
    'canonical': str(canonical.relative_to(root)),
    'canonical_sha256': sha(canonical), 'labels': labels,
    'audits': [str(p.relative_to(root)) for p in audits],
    'author_runtime_seconds': 3.2868060610053362,
    'root_runtime_seconds': 3.244205315990257,
    'reduction_descent_runtime_seconds': 3.3375787070108345,
    'monodromy_runtime_seconds': 3.249439478997374,
    'author_program': 'agents/obstructions_crystals/code/verify_Moore_singular_parameter_classification.py',
    'author_output': 'agents/obstructions_crystals/code/verify_Moore_singular_parameter_classification.output.json',
    'candidate_preserved': True,
    'changes': 'Only short proved statuses and one coordinated optional include after the principal theta bridge. Prior shared bytes and exact diffs retained. No build, current table, review or workflow execution.',
    'scope': 'Set-theoretic classification of the full universal9-by-9 Moore determinant singular parameters as81 projective3-spaces. No scheme-structure assertion or geometric Cartier implication is inferred from this algebraic theorem alone; the typed bridge is a separate audited source.'
}
path = own/'Moore_singular_parameters_promotion.json'
with path.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'promotion_after_full_independent_audits',
                           str(canonical.relative_to(root)),
                           'Full universal coefficient proof and unchanged complete certificate, root plus RD plus monodromy',
                           'PROVED; algebraic scope', str(path.relative_to(root))])+'\n')
with (own/'D_results.md').open('a') as f:
    f.write('\n\n## Universal Moore determinant classification — '+now+'\n\n')
    f.write('`A4_Moore_singular_parameters.tex` classifies every identically singular characteristic-two9-by-9 Moore parameter as lying in one of81 explicit translated character-scaled alternating projective3-spaces. The full9! determinant reconstruction excludes400 supports by retained monomial witnesses; the remaining2/4/6/8-support cases are proved by cube ratios, an elementary reflection-matching lemma and exact root-of-unity polynomial substitution. Root, reduction/descent and monodromy each fully audited the proof and reran the unchanged exhaustive symbolic certificate. This theorem is set-theoretic and algebraic; its actual Cartier/theta bridge is a separate result. The failed40-basis coordinate-product shortcut and all earlier probes remain retained.\n')
print(json.dumps({'status':record['status'], 'actual_utc':now,
                  'canonical':record['canonical'], 'canonical_sha256':record['canonical_sha256'],
                  'record':str(path.relative_to(root))}))

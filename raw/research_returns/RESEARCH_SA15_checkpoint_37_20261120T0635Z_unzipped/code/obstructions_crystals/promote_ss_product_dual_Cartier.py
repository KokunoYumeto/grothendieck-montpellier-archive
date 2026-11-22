"""Promote only the fully audited product dual-Cartier result and one include."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, difflib

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
candidate = own / 'post_CP29_ss_product_dual_Cartier_candidate.tex'
canonical = own / 'A4_ss_product_dual_Cartier.tex'
expected = '6bfbdec7f65a16c39f6094e86485364ad685c80d87ce23ad14cec266e495ba18'
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(candidate) == expected
assert not canonical.exists()
root_audit = root / 'outputs/root_ss_product_cross_audit.json'
mono_audit = root / 'agents/monodromy/outputs/independent_ss_product_dual_Cartier_audit.json'
assert root_audit.exists() and mono_audit.exists()
prior = candidate.read_text()
text = prior.replace('% Separate post-CP29 candidate. No frozen statement or current gate is changed.',
                     '% Proved after complete root and monodromy proof/code audits; no nonproduct assertion.')
statuses = {
    'Candidate; complete direct proof and exact identities supplied.':
    'Proved; full root and monodromy proof/code audits passed.',
    'Candidate; complete geometric proof supplied.':
    'Proved; full root and monodromy proof/code audits passed.',
    'Candidate; complete deduction supplied.':
    'Proved; full root and monodromy proof/code audits passed.',
    'Candidate scope; no fixed nonproduct-surface conclusion.':
    'Proved scope; no fixed nonproduct-surface conclusion.'
}
for old,new in statuses.items():
    assert old in text
    text = text.replace('\\status{'+old+'}', '\\status{'+new+'}')
assert '\\status{Candidate' not in text
canonical.write_text(text)
now = datetime.now(timezone.utc).isoformat()
history = own / 'notes/CP30_ss_product_dual_promotion'
history.mkdir(exist_ok=False)
(history/'candidate.tex').write_bytes(candidate.read_bytes())
(history/'promotion.diff').write_text(''.join(difflib.unified_diff(
    prior.splitlines(True),text.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
consolidate = root / 'code/consolidate.py'
old = consolidate.read_text()
(history/'consolidate.py').write_bytes(consolidate.read_bytes())
needle = "   interpolation=a/'obstructions_crystals/A4_product_Frobenius_interpolation.tex'\n   if interpolation.exists() and '\\\\status{Candidate' not in interpolation.read_text():\n    out.write('\\n'+interpolation.read_text()+'\\n')\n"
assert old.count(needle) == 1
addition = "   product_cross=a/'obstructions_crystals/A4_ss_product_dual_Cartier.tex'\n   if product_cross.exists() and '\\\\status{Candidate' not in product_cross.read_text():\n    out.write('\\n'+product_cross.read_text()+'\\n')\n"
assert 'A4_ss_product_dual_Cartier.tex' not in old
new = old.replace(needle,needle+addition)
compile(new,str(consolidate),'exec')
consolidate.write_text(new)
(history/'consolidate.diff').write_text(''.join(difflib.unified_diff(
    old.splitlines(True),new.splitlines(True),fromfile='prior_consolidate.py',tofile='consolidate.py')))
labels = ['lem:DE-SS-cross-elliptic','lem:DE-SS-cross-product',
          'thm:DE-SS-odd-pullback-dual-rank','cor:DE-SS-odd-rectangle-dual-rank',
          'rem:DE-SS-cross-scope']
record = {
    'status':'PROMOTED AUXILIARY GEOMETRIC RANK RESULT; NO MAIN GATE MOVEMENT',
    'actual_utc':now, 'candidate':str(candidate.relative_to(root)),
    'candidate_sha256':expected, 'canonical':str(canonical.relative_to(root)),
    'canonical_sha256':sha(canonical), 'labels':labels,
    'root_audit':str(root_audit.relative_to(root)),
    'root_audit_utc':'2026-11-20T00:47:32.927596+00:00',
    'root_runtime_seconds':0.0587455460045021,
    'companion_audit':str(mono_audit.relative_to(root)),
    'companion_audit_utc':'2026-11-20T00:43:22.914042+00:00',
    'companion_runtime_seconds':0.06229643800179474,
    'author_output':'agents/obstructions_crystals/code/verify_ss_product_cross_Cartier.output.json',
    'author_runtime_seconds':0.07262399500177708,
    'changes':'Short proved statuses and exactly one optional include immediately after product Frobenius interpolation. Candidate and all prior shared bytes/diffs retained. No build, workflow, current table or review changed.',
    'scope':'Generic dual alternating Cartier rank 9n-1 for every odd etale pullback of the cubic principal bundle from E_ss squared; in particular every odd rectangle. No fixed indecomposable ppav, primitive mixed cup-rank, or new full-monodromy theorem.'
}
path = own / 'ss_product_dual_Cartier_promotion.json'
with path.open('x') as f:
    json.dump(record,f,indent=2)
    f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'promotion_after_two_full_independent_audits',
                           str(canonical.relative_to(root)),
                           'Complete direct proof plus universal 29-identity checker; root and monodromy full passes',
                           'PROVED; auxiliary scope only',str(path.relative_to(root))])+'\n')
with (own/'D_results.md').open('a') as f:
    f.write('\n\n## Product dual-Cartier blocks — '+now+'\n\n')
    f.write('`A4_ss_product_dual_Cartier.tex` proves uniform perfect twisted cross blocks on the supersingular elliptic product, including one trivial Picard coordinate, and generic dual alternating rank 9n−1 for every odd étale pullback of its cubic principal bundle. All odd rectangles follow by the previously proved odd self-isogenies. The direct relative-Cartier table, Schur complement, rank-eight trivial block, and character-open intersection have full root and monodromy proof/code audits. This is auxiliary: no fixed indecomposable principally polarized surface determinant, positive-index mixed cup lower bound, or new full monodromy follows.\n')
print(json.dumps({'status':record['status'],'actual_utc':now,
                  'canonical':record['canonical'],'canonical_sha256':record['canonical_sha256'],
                  'record':str(path.relative_to(root))}))

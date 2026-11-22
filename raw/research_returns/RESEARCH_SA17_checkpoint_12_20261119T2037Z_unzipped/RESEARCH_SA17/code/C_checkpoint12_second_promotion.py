"""Promote ten audited statements; editorial work, not a mathematical test."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, shutil, time

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
now = datetime.now(timezone.utc).isoformat()
promotions = [
    ('notes/C_odd_node_MCM_boundary_proposed.tex', 'sections/C_finish_odd_node_MCM_boundary.tex', 'ba568e0c728cb8918364a7e5fbe5bcbede44c7a2de85d659f1ced0ea345387f0'),
    ('notes/C_relative_Swan_MF_bridge_proposed.tex', 'sections/C_finish_relative_Swan_MF_bridge.tex', '38ea3c1d1a6ecdb143b064290caf6f7dc947ade7547bf94208215eabe5c9180a'),
    ('notes/C_finish_separably_closed_draft.tex', 'sections/C_finish_separably_closed.tex', '1813493c88303cf7e6a9323190488f251256e558537f33e6c8fd92d6b8cc79b1'),
    ('notes/C_Greenberg_congruence_decisions_proposed.tex', 'sections/C_finish_Greenberg_congruence_decisions.tex', '5ba3d8e51034e7e4e0d0d987060058b5358047595a19d14724539219d453dfcd'),
    ('notes/C_finish_infinite_residue_henselian_draft.tex', 'sections/C_finish_infinite_residue_henselian.tex', '3fd12092837611813ca69d161243785ad95b1527f0a8ec951c55af44bb4d5618'),
]
copies = {
    'notes/C_odd_node_MCM_boundary_proposed.csv': 'results_C_odd_node_MCM_boundary.csv',
    'notes/C_odd_node_MCM_boundary_proposed_checks.tsv': 'checks_C_odd_node_MCM_own.tsv',
    'notes/C_odd_node_MCM_mixed_s3_audit.tsv': 'checks_C_odd_node_MCM_peer.tsv',
    'notes/C_odd_node_MCM_root_audit.tsv': 'checks_C_odd_node_MCM_root.tsv',
    'notes/C_odd_node_MCM_boundary_proposed.bib': 'references/C_odd_node_MCM_boundary.bib',
    'notes/C_relative_Swan_MF_bridge_proposed.csv': 'results_C_relative_Swan_MF_bridge.csv',
    'notes/C_relative_Swan_MF_bridge_proposed_checks.tsv': 'checks_C_relative_Swan_MF_own.tsv',
    'notes/C_relative_Swan_MF_mixed_s3_audit.tsv': 'checks_C_relative_Swan_MF_peer.tsv',
    'notes/C_relative_Swan_MF_root_audit.tsv': 'checks_C_relative_Swan_MF_root.tsv',
    'notes/C_relative_Swan_MF_bridge_proposed.bib': 'references/C_relative_Swan_MF_bridge.bib',
    'notes/C_separably_closed_proposed.csv': 'results_C_separably_closed.csv',
    'notes/C_separably_closed_proposed_checks.tsv': 'checks_C_separably_closed_own.tsv',
    'notes/C_separably_closed_regular_coherent_audit.tsv': 'checks_C_separably_closed_peer.tsv',
    'notes/C_separably_closed_root_checks.tsv': 'checks_C_separably_closed_root.tsv',
    'notes/C_separably_closed_sources.bib': 'references/C_separably_closed.bib',
    'notes/C_Greenberg_congruence_decisions_proposed.csv': 'results_C_Greenberg_congruence_decisions.csv',
    'notes/C_Greenberg_congruence_decisions_own_checks.tsv': 'checks_C_Greenberg_own.tsv',
    'notes/C_Greenberg_mixed_s3_audit.tsv': 'checks_C_Greenberg_mixed_s3.tsv',
    'notes/C_Greenberg_regular_coherent_audit.tsv': 'checks_C_Greenberg_regular_coherent.tsv',
    'notes/C_Greenberg_congruence_flat_union_audit.tsv': 'checks_C_Greenberg_flat_union.tsv',
    'notes/C_Greenberg_sources.bib': 'references/C_Greenberg.bib',
    'notes/C_infinite_residue_henselian_proposed.csv': 'results_C_infinite_residue_henselian.csv',
    'notes/C_infinite_residue_henselian_proposed_checks.tsv': 'checks_C_infinite_residue_henselian_own.tsv',
    'notes/C_infinite_residue_henselian_regular_coherent_audit.tsv': 'checks_C_infinite_residue_henselian_peer.tsv',
    'notes/C_infinite_residue_henselian_root_audit.tsv': 'checks_C_infinite_residue_henselian_root.tsv',
}
# Check every input and one-shot target before the first mutation.
for src, dst, sha in promotions:
    assert hashlib.sha256((root/src).read_bytes()).hexdigest() == sha, src
    assert not (root/dst).exists(), 'Promotion was already run: '+dst
for src, dst in copies.items():
    assert (root/src).is_file(), src
    assert not (root/dst).exists(), dst

records = []
for src, dst, sha in promotions:
    value = (root/src).read_text().replace('[Proposed:', '[Proved:')
    (root/dst).write_text(value)
    records.append({'source':src, 'audited_sha256':sha, 'compiled_source':dst,
                    'compiled_sha256':hashlib.sha256(value.encode()).hexdigest(),
                    'post_audit_change':'Only Proposed to Proved labels where present'})
for src, dst in copies.items():
    shutil.copyfile(root/src, root/dst)

p = root/'sections/C.tex'
s = p.read_text()
needle = '\\input{sections/C_finish_MF_Swan_transfer}\n'
assert s.count(needle) == 1
s = s.replace(needle, needle+'\\input{sections/C_finish_odd_node_MCM_boundary}\n'
              +'\\input{sections/C_finish_relative_Swan_MF_bridge}\n')
needle = '\\input{sections/C_finish_henselian_global_WG}\n'
assert s.count(needle) == 1
s = s.replace(needle, needle+'\\input{sections/C_finish_separably_closed}\n'
              +'\\input{sections/C_finish_Greenberg_congruence_decisions}\n'
              +'\\input{sections/C_finish_infinite_residue_henselian}\n')
needle = 'exponent-three dyadic node. It does not decide the full comparison map.\n'
assert s.count(needle) == 1
s = s.replace(needle, needle+r'''Proposition~\ref{C:odd-node-MCM-comparison-boundary} shows that the
whole generic Swan kernel is invisible to the ordinary MCM Grothendieck
group on odd-exponent dyadic nodes. The true category retained by
Swan lattices is the relative matrix-factorization category of
Lemma~\ref{C:relative-Swan-MF-bridge}; its required Grothendieck group
has not been calculated. Neither comparison settles polynomiality.
''')
p.write_text(s)

p = root/'sections/unresolved.tex'
s = p.read_text()
needle = '\\begin{remark}[Open: the remaining modular orthogonal classification]'
assert s.count(needle) == 1
s = s.replace(needle, r'''The additional ordinary MCM comparison vanishes on the entire generic
kernel for odd-exponent nodes, by
Proposition~\ref{C:odd-node-MCM-comparison-boundary}.
Lemma~\ref{C:relative-Swan-MF-bridge} identifies the actual relative
category, but its Grothendieck group and the residual-zero pencil
component remain uncomputed. These route boundaries are not new
classifications of rings.

'''+needle)
needle = 'Thus the remaining task concerns coefficient bases outside the completed\n'
assert s.count(needle) == 1
s = s.replace(needle, r'''Theorems~\ref{C:separably-closed-effective-arithmetic} and
\ref{C:separably-closed-coefficient-WG} remove the explicit finite-imperfection
separably closed fields and their stated coefficient algebras and
coherent local henselizations. Computable $p$-components and Haran's
quantifier elimination give actual arithmetic; the computed division
fields may be purely inseparable, and the form blocks have free integer
coordinates. For imperfection degree at least two, the anisotropic
quasilinear form proves these fields are not $C_1$.
Theorems~\ref{C:infinite-residue-henselian-arithmetic} and
\ref{C:infinite-residue-henselian-WG} further settle all finite towers over
the explicit one-variable henselian fields with these infinite residue
fields. A certified whole residue-field table and an actual integral
basis give each finite quotient; Haran and
Lemma~\ref{C:Greenberg-congruence-decisions} decide the required
congruence, division-index and hermitian-isometry questions.
Corollary~\ref{C:infinite-residue-new-families} proves their separation
from the earlier global and finite-residue families. No unproved
iteration over these new henselian residue fields is asserted.

'''+needle)
p.write_text(s)

p = root/'code/finish_report.py'
lines = p.read_text().splitlines()
for j, line in enumerate(lines):
    if line.startswith("'C.1':"):
        row = list(ast.literal_eval(line.split(':',1)[1].rstrip(',')))
        row[1] += '; C:odd-node-MCM-comparison-boundary; C:relative-Swan-MF-bridge'
        row[2] += ' The whole generic Swan kernel maps to zero in ordinary MCM/G0 for odd-exponent dyadic nodes. The actual relative matrix-factorization category is now identified, but its K0 is not computed; these route boundaries are not counted as classification movement.'
        lines[j] = "'C.1':"+repr(tuple(row))+','
    if line.startswith("'C.3':"):
        row = list(ast.literal_eval(line.split(':',1)[1].rstrip(',')))
        row[0] = 'Lambda criterion settled; explicit global, henselian and separably closed arithmetic families solved; arbitrary coefficient bases open'
        row[1] += '; C:separably-closed-effective-arithmetic; C:separably-closed-coefficient-WG; C:Greenberg-congruence-decisions; C:infinite-residue-henselian-arithmetic; C:infinite-residue-henselian-WG'
        row[2] += ' The explicit separable closures of finite-variable rational function fields now have full algorithms through computable p-components and Haran quantifier elimination. Their actual purely inseparable division fields and symmetric-form blocks give free integer coordinates. All finite towers over the corresponding one-variable henselian fields with infinite separably closed residue are also solved: whole residue-field certificates and integral bases give finite quotient tables, and Greenberg approximation gives terminating projective and hermitian decisions. Each family includes all finite coefficient algebras and the stated effective coherent local henselizations. Explicit non-C1 witnesses and transcendence degree verify that these remove additional whole families; arbitrary affine equation decisions over the new henselian fields and further henselian iterations are not asserted.'
        lines[j] = "'C.3':"+repr(tuple(row))+','
p.write_text('\n'.join(lines)+'\n')

record = {'timestamp':now, 'promotions':records, 'numbered_statements':10,
          'compiled_files_added':5, 'seconds':time.perf_counter()-start,
          'movement_scope':'The two concrete C3 field/coefficient families only; abstract Greenberg method and C1 category boundaries do not separately count.',
          'source_freeze':False, 'checkpoint_created':False}
(root/'logs/C_checkpoint12_second_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

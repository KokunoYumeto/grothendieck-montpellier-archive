"""Retain actual cyclic/Prym literature scope checks without importing an inapplicable theorem."""
from pathlib import Path
import datetime,difflib,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
bib=w/'notes/root_references.bib';before=bib.read_text()
assert 'Nesterov2026CyclicScope' not in before and 'Rains2025CyclicPrymsScope' not in before
snapshot=w/'notes/CP34_cyclic_source_scope';assert not snapshot.exists();snapshot.mkdir()
shutil.copy2(bib,snapshot/'root_references.before.bib')
addition=r'''
@misc{Nesterov2026CyclicScope,
 author={Nesterov, Stepan},
 title={Mod p Monodromy of Cyclic Covers of the Projective Line},
 year={2026},
 eprint={2604.27391}, archivePrefix={arXiv},
 url={https://arxiv.org/html/2604.27391v1},
 note={Opened original arXiv version1 HTML and abstract on20November2026. Introduction, fixed odd-prime notation, Theorem2 statement and Theorem3 comparison with its short explanatory passage read. The family is over the complex numbers and the coefficient prime is odd. The big-monodromy proof was not fully audited and no theorem is imported into the characteristic-two coefficient-two Lang problem. This is a scope check, not a proof of the fixed cubic-surface source image.}
}
@misc{Rains2025CyclicPrymsScope,
 author={Rains, Eric M.},
 title={The monodromy of cyclic Pryms},
 year={2025},
 eprint={2512.19597}, archivePrefix={arXiv},
 url={https://arxiv.org/html/2512.19597v1},
 note={Opened original arXiv version1 HTML and abstract on20November2026. Introduction, Theorems9.2 and9.3 statements, the opening scope restriction of Section10.1, complete Theorem10.1 proof and Corollary10.2 statement read. Section10.1 explicitly excludes characteristic-p torsion from its large-monodromy definition. Thus it does not supply the needed etale two-torsion image in characteristic two; the fixed cubic linear-system specialization also requires a separate argument. No whole-paper proof audit or applicable theorem import is claimed.}
}
'''
bib.write_text(before+addition)
(snapshot/'root_references.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),bib.read_text().splitlines(True),fromfile='before',tofile='after')))
record={
 'actual_utc':now,'status':'PRIMARY-TEXT-SCOPE-CHECK; NO APPLICABLE MONODROMY THEOREM IMPORTED',
 'earlier_overflow':'At approximately03:48 before context recovery, one three-query primary search executed but its entire tool output was context-truncated and unread. No source or mathematical claim is credited to that call. The queries were p-rank monodromy abelian surfaces linear; (1,d) abelian surfaces positive characteristic curves; etale p-torsion linear system monodromy.',
 'queries':[
  '"p-rank" "monodromy" "abelian surfaces" "linear"',
  '"abelian surfaces" "positive characteristic" "linear systems" monodromy',
  '"cyclic covers" "p-rank" "monodromy"',
  'Prym p-adic monodromy etale cyclic covers Pries Achter',
  '"Hasse-Witt" "linear system" "abelian"',
  '"p-torsion" "monodromy" "Prym"'],
 'original_openings':[
  {'author':'Stepan Nesterov','year':2026,'url':'https://arxiv.org/html/2604.27391v1','tool_reference':'turn485570666view2','locators':'Introduction; fixed notation; Theorem2 statement; Theorem3 with its short explanatory passage','result':'Over C and odd coefficient prime; does not apply to characteristic2, coefficient2. No full theorem proof audit claimed.'},
  {'author':'Eric M. Rains','year':2025,'url':'https://arxiv.org/html/2512.19597v1','tool_reference':'turn642771406view1','locators':'Introduction; Theorems9.2/9.3 statements; Section10.1 opening restriction; complete Theorem10.1 proof; Corollary10.2 statement','result':'Characteristic-p torsion explicitly excluded from large monodromy in Section10.1. Does not establish our actual Lang image; no whole-paper proof audit claimed.'}],
 'other_search_results':'Results on general curve/Siegel p-rank strata, cyclic covers of the projective line, and Prym maps were only screened as search results. No fixed-surface characteristic-two unit-root theorem was obtained from them.',
 'gate_change':False,'numerical_computation':False,
 'bibliography_sha256':hashlib.sha256(bib.read_bytes()).hexdigest()}
(snapshot/'record.json').write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/ROOT_SEARCH_LOG_34.md').open('a') as f:
 f.write('\n## Cyclic-source and Prym scope search, '+now+'\n\n')
 f.write(record['earlier_overflow']+'\n\nThe fresh queries were:\n\n')
 for q in record['queries']:f.write('- `'+q+'`\n')
 f.write('\nNesterov (2026), original arXiv2604.27391v1: the introduction and Theorem2 statement concern a complex family with an odd coefficient prime; Theorem3 and its short comparison passage were also read. No full proof audit is claimed. This supplies no characteristic-two Lang theorem.\n\n')
 f.write('Rains (2025), original arXiv2512.19597v1: Theorems9.2/9.3 statements, Section10.1 and the complete short proof of Theorem10.1, plus Corollary10.2, were read. Section10.1 explicitly removes characteristic-p torsion from the meaning of large monodromy. This excludes the required coefficient-two application before any specialization to a fixed cubic linear system. No theorem from this source is imported.\n\n')
 f.write('Exact URLs and actual opening scopes are retained in notes/CP34_cyclic_source_scope/record.json and the two bibliography entries. The search yields no gate reduction.\n')
with (w/'notes/checkpoint34_changes.md').open('a') as f:
 f.write('\n## Literature scope check for the cyclic-source route\n\nThe original Nesterov2026 and Rains2025 cyclic-monodromy texts were opened at the locators recorded in ROOT_SEARCH_LOG_34. Their respective complex/odd-coefficient and away-from-characteristic-torsion hypotheses do not give the characteristic-two Lang image needed here. They are recorded as precisely scoped rejected applications, without a new theorem import or movement credit.\n')
print(json.dumps(record,indent=2))

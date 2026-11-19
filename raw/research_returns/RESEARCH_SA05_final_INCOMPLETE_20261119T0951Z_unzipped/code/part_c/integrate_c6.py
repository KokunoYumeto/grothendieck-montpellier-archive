from pathlib import Path
import csv, json, time

start = time.perf_counter()
root = Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work')
paper = root / 'sections/part_c.tex'
text = paper.read_text()
insert = (root / 'part_d/c6_insert.tex').read_text()
insert = insert[insert.index('\\begin{lemma}'):]
insert = insert.replace('\\label{c:potentially-good-generator}\n', '\\label{c:potentially-good-generator}\n\\status{Proved}\n')
insert = insert.replace('\\begin{remark}[The exact role of the new input]\n', '\\begin{remark}[The exact role of the new input]\n\\label{c:ell-independence-new-input}\n\\status{Proved scope clarification}\n')
old_start = text.index('\\begin{remark}[The unresolved descent and general-motive claim]') if 'The unresolved descent and general-motive claim' in text else text.index('\\begin{lemma}[A generator with potentially good reduction]')
general = r'''\begin{remark}[The remaining general-motive claim]
\label{c:ell-independence-gate}
\status{Unresolved in the general motivic category}
Theorem~\ref{c:ell-independence-abelian} settles the whole abelian-type assertion, including its finite-inertia descent. The direct argument from an arbitrary original generator would still be invalid: $\bigwedge^2H^1(E)=\Q_\ell(-1)$ is unramified at a place of residue characteristic different from $\ell$, even when $E$ has bad reduction. The weak-lift lemma and the trace argument are what repair that inference.

For general motives, a common Weil--Deligne representation with compatible motivic projectors would imply the desired independence: unramifiedness means trivial inertial type and zero monodromy. The $G$-valued form of this stronger expectation is formulated in \citet[Conjecture 1.1]{c_kisinzhou2025}. This is an implication, not an equivalence. Knowing only whether inertia is trivial contains less information than its conjugacy class or conductor, so no converse has been proved here. The theorem of \citet[Theorem 5.1]{c_commelin2019} concerns abelian motives and quasi-compatibility; by itself it does not supply finite-inertia traces for an arbitrary motive at a bad place. An exact equivalence with a named stronger conjecture remains an outstanding assertion, recorded separately from the now proved abelian-type theorem.
\end{remark}
'''
paper.write_text(text[:old_start] + insert + '\n' + general)
bib = root / 'part_c/references.bib'
contents = bib.read_text()
new_bib = (root / 'part_d/c6_sources.bib').read_text()
if '@article{c_noot2006,' not in contents:
    bib.write_text(contents + '\n' + new_bib)

results = root / 'part_c/results.csv'
with results.open(newline='') as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = {r['id']: r for r in reader}
data = [
    ('c:potentially-good-generator', 'One potentially unramified realization admits a potentially-good abelian generator after finite extension', 'Proved', 'Lemma', 'Noot 2.12,2.15,3.1,3.4; abelian Hodge full faithfulness; semistable monodromy; NOS', '12:140', 'Descent via B0 factors; common MT group has finite derived kernel; all places above v retained.'),
    ('c:ell-independence-abelian', 'Unramifiedness is independent of ell different from residue characteristic for all abelian-type motives', 'Proved using October 2026 rationality theorem', 'Theorem', 'c:potentially-good-generator; Milne rationality theorem1.1; finite etale induction; Lefschetz trace', '12:140', 'Includes arbitrary tensor summands, ramified descent, p=2, and ell=2 when p differs.'),
    ('c:ell-independence-new-input', 'The proof uses rationality of graph pairings and does not assume algebraicity of Hodge projectors', 'Proved scope clarification', 'Remark', 'c:ell-independence-abelian', '12:140', 'Also gives common finite inertia character for potentially unramified objects; no full nonzero-monodromy WD compatibility claimed.'),
]
for ident, statement, status, kind, dependencies, pages, notes in data:
    rows[ident] = dict(zip(fields, [ident, statement, status, 'sections/part_c.tex, ' + kind + ' label ' + ident, dependencies, pages, notes]))
rows['c:ell-independence-gate'].update(statement='General-motive independence and the requested exact named-conjecture equivalence', status='Unresolved in the general motivic category', depends_on='Common Weil-Deligne systems with compatible projectors imply independence; converse not proved', notes='The abelian-type ramified-descent gap is now closed by c:ell-independence-abelian.')
rows['c:ell-independence-cases']['notes'] = 'The elementary cases are now subsumed by c:ell-independence-abelian; retained to isolate the older SGA7/Kisin-Zhou inputs.'
with results.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows.values())
events_path = root / 'part_c/CHECK_EVENTS.tsv'
with events_path.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t'); event_fields = reader.fieldnames; events = list(reader)
events_added = [
    ('c:potentially-good-generator', 'independent re-proof', 'Part C independently read Noot and audited the complete lift/descent proof in c6_weak_lift_independent_audit.md; repaired direct Prop3.1 invocation for a general motive using B0 factors.'),
    ('c:ell-independence-abelian', 'independent re-proof', 'Part D constructed proof; root independently checked rationality scope, graph trace, crosscomponents and all places; Part C checked weak-lift and finite-kernel unipotence.'),
    ('c:ell-independence-new-input', 'targeted proof check', 'Graph of origin-preserving inertia isomorphism is Lefschetz via difference map and normalized top polarization; no algebraicity of Hodge projector assumed.'),
    ('c:ell-independence-gate', 'targeted proof check', 'Removed superseded abelian-type gap; retained only general-motive independence and requested equivalence as unresolved.'),
]
for ident, kind, outcome in events_added:
    event = dict(zip(event_fields, [ident, '2026-11-19', 'GPT-6 Astra (OpenAI), /root/part_c', kind, outcome]))
    if event not in events: events.append(event)
with events_path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=event_fields, delimiter='\t'); writer.writeheader(); writer.writerows(events)
report = {'integrated_labels': [r[0] for r in data], 'result_rows': len(rows), 'events': len(events), 'bib_appended': True, 'runtime_seconds': round(time.perf_counter()-start, 6)}
(root/'code/part_c/integrate_c6_output.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
